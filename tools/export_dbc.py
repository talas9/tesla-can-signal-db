#!/usr/bin/env python3
"""
Export the Tesla CAN signal database as Vector DBC files (+ JSON twins).

Library API (no hard-coded paths; every path is an argument)
------------------------------------------------------------
    load_signal_rows(path)            -> list[dict]
        Read a signals CSV (columns of data/<fw>/signals.csv). Extra columns
        are tolerated; a missing required column raises ExportError.

    load_inputs(fw_dir)               -> dict of export() keyword arguments
        Reads <fw_dir>/signals.csv plus, when present, messages.csv
        (message,length,cycle_ms,routes with routes = BUS:can_id:native|gateway
        joined by ';'), signal-meta.csv (message,signal,unit,enum_values,sna,
        models,cross_checked) and log-verdicts.csv (fw,signal,message,eth_id,
        can_id,bus,verdict,logs_seen,frames,in_range_pct,evidence; only
        fw/message/signal/verdict are used, evidence is never copied).

    export(signal_rows, firmware, out_dir, routing=None, msg_meta=None,
           signal_meta=None, verdicts=None)  -> {'files': [report, ...]}
        Writes <out_dir>/<fw>/ETH.{dbc,json} (Ethernet-side ids) and, when routing is given,
        <out_dir>/<model>/<fw>/<BUS>.{dbc,json}. Deterministic and idempotent:
        same inputs -> byte-identical files. Raises ExportError on any input it
        cannot handle.

    coverage_markdown(reports)        -> str (README coverage table)

    check(out_dir)                    -> list[str] (errors; empty = pass)
        Validate every .dbc under out_dir: generator checklist (ASCII,
        section order, NS_ block, empty BS_, identifiers, attributes and their
        defaults, ENUM indexes, nodes, BO_TX_BU_, FD lengths, duplicate
        ids/VAL_, one-line CM_), cantools strict load, cantools round trip,
        JSON twin agreement, canmatrix load (if installed), PII +
        source-disclosure gates (from tools/build.py).

CLI (thin wrapper):
    python3 tools/export_dbc.py            # regenerate dbc/ from data/
    python3 tools/export_dbc.py --check    # regenerate to a temp dir, diff
                                           # against committed dbc/, check()

Bit numbering: `start` in the input is DBC convention already (Intel = LSB
position, Motorola = MSB position in sawtooth numbering) and is written
unchanged. Verified: EPAS3S_torsionBarTorque 19|12 big-endian encodes the
same bits as the well-known public DBC definition 19|12@0+.
"""

import argparse
import csv
import filecmp
import json
import math
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import DEVICE_NAMES, scan_pii, scan_source_disclosure  # noqa: E402


class ExportError(Exception):
    """Raised on any input the exporter cannot handle (fail loudly)."""


REQUIRED_COLUMNS = [
    'signal', 'message', 'eth_id', 'mux_signal', 'mux_value', 'start', 'length',
    'little_endian', 'signed', 'scale', 'offset', 'unit', 'description', 'min',
    'max', 'enum_values',
]

GENERATOR_VERSION = 'dbc-export 1'
NS_SYMBOLS = [
    'NS_DESC_', 'CM_', 'BA_DEF_', 'BA_', 'VAL_', 'CAT_DEF_', 'CAT_', 'FILTER',
    'BA_DEF_DEF_', 'EV_DATA_', 'ENVVAR_DATA_', 'SGTYPE_', 'SGTYPE_VAL_',
    'BA_DEF_SGTYPE_', 'BA_SGTYPE_', 'SIG_TYPE_REF_', 'VAL_TABLE_', 'SIG_GROUP_',
    'SIG_VALTYPE_', 'SIGTYPE_VALTYPE_', 'BO_TX_BU_', 'BA_DEF_REL_', 'BA_REL_',
    'BA_DEF_DEF_REL_', 'BU_SG_REL_', 'BU_EV_REL_', 'BU_BO_REL_', 'SG_MUL_VAL_',
]
FD_SIZES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64]
SEND_TYPES = ['Cyclic', 'NotUsed', 'NotUsed', 'NotUsed', 'NotUsed', 'NotUsed',
              'NotUsed', 'IfActive', 'NoMsgSendType', 'NotUsed']
FRAME_FORMATS = ['StandardCAN', 'ExtendedCAN', 'reserved', 'J1939PG'] + \
    ['reserved'] * 10 + ['StandardCAN_FD', 'ExtendedCAN_FD']
CONFIDENCE = ['validated', 'plausible', 'layout-only', 'contradicted']
VERDICT_OVERRIDES = ('validated', 'plausible', 'contradicted')
BUS_LABELS = {'VEH': 'VEH (vehicle CAN)', 'CH': 'CH (chassis CAN)',
              'PARTY': 'bus1 (inferred PARTY)', 'ETH': 'ETH (Ethernet-side ids, not CAN ids)'}
MAX_NAME = 32
IDENT_RE = re.compile(r'^[A-Za-z_][A-Za-z0-9_]{0,31}$')
DBC_KEYWORDS = set(NS_SYMBOLS) | {'VERSION', 'NS_', 'BS_', 'BU_', 'BO_', 'SG_', 'EV_',
                                  'VECTOR__INDEPENDENT_SIG_MSG', 'VECTOR__XXX'}

# Plain-language ECU names for node comments (prefix of the message name).
NODE_NAMES = {k: v.split(' ', 1)[1] for k, v in DEVICE_NAMES.items()}
NODE_NAMES.update({
    'BMS': 'High-voltage battery management system',
    'HVP': 'High-voltage processor (pack contactor and isolation controller)',
    'PCS': 'Power conversion system (on-board charger and DC-DC converter)',
    'DI': 'Drive inverter', 'DIF': 'Front drive inverter', 'DIR': 'Rear drive inverter',
    'VCFRONT': 'Front body controller', 'VCLEFT': 'Left body controller',
    'VCRIGHT': 'Right body controller', 'VCSEC': 'Vehicle security controller',
    'GTW': 'Gateway', 'UI': 'Touchscreen user interface computer',
    'EPAS': 'Electric power steering', 'EPAS3P': 'Electric power steering (primary)',
    'EPAS3S': 'Electric power steering (secondary)', 'ESP': 'Electronic stability control',
    'DAS': 'Driver assistance computer', 'APP': 'Driver assistance computer (primary)',
    'APS': 'Driver assistance computer (secondary)', 'RCM': 'Restraint control module',
    'SCCM': 'Steering column control module', 'IBST': 'Electric brake booster',
    'CP': 'Charge port controller', 'TAS': 'Air suspension controller',
    'THC': 'Thermal controller', 'CMP': 'A/C compressor', 'PTC': 'Cabin heater',
    'EPBL': 'Left electric parking brake', 'EPBR': 'Right electric parking brake',
    'OCS1P': 'Occupant classification system', 'PARK': 'Parking assist sensors',
    'RADC': 'Radar', 'TPMS': 'Tire pressure monitoring', 'ADSP': 'Audio amplifier',
    'CC': 'Charge cable controller', 'SDM': 'Airbag control module',
})

UNIT_ASCII = {'°': 'deg', 'µ': 'u', 'μ': 'u', 'Ω': 'Ohm',
              'Ω': 'Ohm', '²': '2', '³': '3', '±': '+-'}


# ----------------------------------------------------------------- helpers

def fmt_num(x):
    """Decimal number text accepted by every DBC parser (no hex, no '.5')."""
    x = float(x)
    if x == 0:
        return '0'
    if x == int(x) and abs(x) < 1e15:
        return str(int(x))
    s = '%.12g' % x
    if 'e' in s or 'E' in s:
        mant, exp = s.lower().split('e')
        if '.' not in mant:
            mant += '.0'
        s = '%se%s' % (mant, exp)
    return s


def ascii_text(s):
    """One-line ASCII string safe inside DBC double quotes."""
    out = []
    for ch in s or '':
        if ch in UNIT_ASCII:
            out.append(UNIT_ASCII[ch])
        elif ch in '\r\n\t':
            out.append(' ')
        elif ch == '"':
            out.append("'")
        elif ch == '\\':
            out.append('/')
        elif 32 <= ord(ch) < 127:
            out.append(ch)
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def words_from_name(name):
    """'BMS_packVoltage' -> 'pack voltage' (drops the ECU prefix)."""
    parts = name.split('_')
    body = ' '.join(parts[1:]) if len(parts) > 1 else name
    body = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', body)
    body = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', body)
    toks = []
    for t in body.split():
        toks.append(t if (t.isupper() and len(t) > 1) else t.lower())
    return ' '.join(toks)


def node_of(name):
    pre = name.split('_', 1)[0]
    return pre if IDENT_RE.match(pre) and pre.upper() not in DBC_KEYWORDS else 'Vector__XXX'


def node_label(node):
    return NODE_NAMES.get(node, '%s ECU' % node)


def motorola_bits(start, length):
    bits, b = [start], start
    for _ in range(length - 1):
        b = b + 15 if b % 8 == 0 else b - 1
        bits.append(b)
    return bits


def signal_bits(sig):
    if sig['little']:
        return list(range(sig['start'], sig['start'] + sig['length']))
    return motorola_bits(sig['start'], sig['length'])


def raw_range(length, signed):
    if signed:
        return -(1 << (length - 1)), (1 << (length - 1)) - 1
    return 0, (1 << length) - 1


def parse_float(v, what):
    try:
        f = float(v)
    except ValueError:
        raise ExportError('bad number for %s: %r' % (what, v))
    if math.isnan(f) or math.isinf(f):
        raise ExportError('non-finite number for %s: %r' % (what, v))
    return f


def parse_bool01(v, what):
    if v not in ('0', '1'):
        raise ExportError('bad 0/1 value for %s: %r' % (what, v))
    return v == '1'


def parse_int(v, what):
    v = v.strip()
    try:
        return int(v, 16) if v.lower().startswith('0x') else int(v)
    except ValueError:
        raise ExportError('bad integer for %s: %r' % (what, v))


def gated(text):
    """True if text would fail the source-disclosure gate."""
    return bool(scan_source_disclosure(text))


# ----------------------------------------------------------------- input

def load_signal_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ExportError('%s: missing required columns %s' % (path, missing))
        return list(reader)


def parse_enum(text, what):
    out = {}
    try:
        raw = json.loads(text)
    except ValueError:
        raise ExportError('%s: enum_values is not JSON: %r' % (what, text[:80]))
    if not isinstance(raw, dict):
        raise ExportError('%s: enum_values must be a JSON object' % what)
    for k, v in raw.items():
        out[parse_int(str(k), what + ' enum key')] = ascii_text(str(v)) or str(k)
    return out


def normalise_rows(rows, signal_meta=None, verdicts=None):
    """Validate + convert rows. Returns (signals, dropped).

    signal_meta: {(message, signal): {'unit', 'enum_values', 'sna', 'models',
    'cross_checked'}} fills unit/value table/SNA where the row has none and
    gives the per-model assignment. verdicts: {(message, signal): verdict}.
    """
    signal_meta = signal_meta or {}
    verdicts = verdicts or {}
    signals, dropped = [], []
    for r in rows:
        missing = [c for c in REQUIRED_COLUMNS if c not in r]
        if missing:
            raise ExportError('row %r missing columns %s' % (r.get('signal'), missing))
        name = r['signal'].strip()
        msg = r['message'].strip()
        if not IDENT_RE.match(name[:MAX_NAME]) or not re.match(r'^[A-Za-z_]\w*$', name):
            raise ExportError('bad signal name %r' % name)
        if not re.match(r'^[A-Za-z_]\w{0,31}$', msg):
            raise ExportError('bad message name %r' % msg)
        if r['start'].strip() == '' and r['length'].strip() == '':
            dropped.append({'message': msg, 'signal': name, 'reason': 'no bit layout'})
            continue
        sig = {
            'name': name, 'message': msg,
            'msg_id': parse_int(r['eth_id'], name + '.eth_id'),
            'mux_signal': r['mux_signal'].strip(),
            'mux_value': parse_int(r['mux_value'], name + '.mux_value') if r['mux_value'].strip() else None,
            'start': parse_int(r['start'], name + '.start'),
            'length': parse_int(r['length'], name + '.length'),
            'little': parse_bool01(r['little_endian'].strip(), name + '.little_endian'),
            'signed': parse_bool01(r['signed'].strip(), name + '.signed'),
            'scale': parse_float(r['scale'], name + '.scale'),
            'offset': parse_float(r['offset'], name + '.offset'),
            'unit': ascii_text(r['unit']),
            'description': r['description'].strip(),
            'min': r['min'].strip(), 'max': r['max'].strip(),
            'enum': {},
            'sna': None, 'is_float': False,
            'confidence_hint': (r.get('confidence') or '').strip(),
        }
        if bool(sig['mux_signal']) != (sig['mux_value'] is not None):
            raise ExportError('%s: mux_signal/mux_value must both be set or both empty' % name)
        if sig['length'] < 1 or sig['length'] > 64 or sig['start'] < 0:
            raise ExportError('%s: bad start/length %d|%d' % (name, sig['start'], sig['length']))
        if sig['scale'] == 0:
            raise ExportError('%s: scale is 0' % name)
        ev = r['enum_values'].strip()
        if ev:
            sig['enum'] = parse_enum(ev, name)
        sna = (r.get('sna') or '').strip()
        if sna:
            sig['sna'] = parse_int(sna, name + '.sna')
        if (r.get('is_float') or '').strip() == '1':
            sig['is_float'] = True
        meta = signal_meta.get((msg, name), {})
        if not sig['unit'] and meta.get('unit'):
            sig['unit'] = ascii_text(meta['unit'])
        if not sig['enum'] and meta.get('enum_values'):
            sig['enum'] = parse_enum(meta['enum_values'], name)
        if sig['sna'] is None and meta.get('sna'):
            sig['sna'] = parse_int(meta['sna'], name + '.sna')
        sig['models'] = sorted(m for m in (meta.get('models') or '').split(';') if m)
        for m in sig['models']:
            if not re.match(r'^[A-Za-z][A-Za-z0-9]*$', m):
                raise ExportError('%s: bad model name %r' % (name, m))
        sig['cross_checked'] = (meta.get('cross_checked') or '0') == '1'
        v = verdicts.get((msg, name))
        if v in VERDICT_OVERRIDES:
            sig['confidence_hint'] = v
        signals.append(sig)
    return signals, dropped


# ----------------------------------------------------------------- model

def short_names(names):
    """Deterministic <=32-char unique identifiers. Returns {long: short}."""
    out, used = {}, set()
    for n in sorted(names, key=lambda x: (len(x) > MAX_NAME, x)):
        if len(n) <= MAX_NAME and n not in used:
            out[n] = n
            used.add(n)
    for n in sorted(names):
        if n in out:
            continue
        cand = n[:MAX_NAME]
        i = 0
        while cand in used:
            i += 1
            cand = '%s_%04d' % (n[:MAX_NAME - 5], i)
        out[n] = cand
        used.add(cand)
    return out


def describe_signal(sig):
    d = ascii_text(sig['description'])
    if d and not gated(d):
        text = d
    else:
        w = words_from_name(sig['name'])
        text = '%s: %s' % (node_label(node_of(sig['message'])), w) if w else ''
        if not text or gated(text):
            text = 'Signal reported by %s' % node_label(node_of(sig['message']))
        text = text[0].upper() + text[1:]
    if sig['sna'] is not None:
        text = text.rstrip('. ') + '; raw %d = signal not available (SNA)' % sig['sna']
    if sig.get('not_on_can'):
        text = text.rstrip('. ') + '; not carried on CAN'
    return text


def describe_message(msg):
    origin = msg.get('routed_from') or msg['transmitter']
    w = words_from_name(msg['name'])
    text = '%s message: %s' % (node_label(origin), w) if w else '%s message' % node_label(origin)
    if gated(text):
        text = '%s message' % node_label(origin)
    if msg.get('routed_from'):
        text += '; forwarded onto this bus by the gateway'
    if msg.get('length_note'):
        text += '; ' + msg['length_note']
    return text


def phys_range(sig):
    lo, hi = raw_range(sig['length'], sig['signed'])
    if sig['sna'] is not None:
        if sig['sna'] == hi and hi - lo >= 2:
            hi -= 1
        elif sig['sna'] == lo and hi - lo >= 2:
            lo += 1
    a, b = lo * sig['scale'] + sig['offset'], hi * sig['scale'] + sig['offset']
    rmin, rmax = min(a, b), max(a, b)
    try:
        cmin, cmax = float(sig['min']), float(sig['max'])
        if cmin < cmax and cmax > rmin and cmin < rmax:
            return max(cmin, rmin), min(cmax, rmax)
    except ValueError:
        pass
    return rmin, rmax


def confidence_of(sig):
    if sig['confidence_hint'] in CONFIDENCE:
        return sig['confidence_hint']
    if sig.get('cross_checked'):
        return 'validated'
    if sig['unit'] or sig['enum'] or ascii_text(sig['description']):
        return 'plausible'
    return 'layout-only'


def build_messages(signals, msg_meta=None):
    """Group signals into messages, resolve overlaps. Returns (msgs, dropped).

    msg_meta: {message_name: {'id': int, 'length': int, 'cycle_ms': int,
    'transmitter': str, 'routed_from': str}} overrides the frame id (bus files
    use the on-bus CAN id), frame length, cycle time and transmitter.
    """
    msg_meta = msg_meta or {}
    by_msg = {}
    for s in signals:
        by_msg.setdefault(s['message'], []).append(s)
    msgs, dropped = [], []
    for mname in sorted(by_msg):
        sigs = sorted(by_msg[mname], key=lambda s: s['name'])
        ids = {s['msg_id'] for s in sigs}
        if len(ids) != 1:
            raise ExportError('message %s has several ids %s' % (mname, sorted(ids)))
        meta = msg_meta.get(mname, {})
        sel_names = {s['mux_signal'] for s in sigs if s['mux_signal']}
        if len(sel_names) > 1:
            raise ExportError('message %s has several multiplexer switches %s' % (mname, sorted(sel_names)))
        names = {s['name'] for s in sigs}
        for sel in sel_names:
            if sel not in names:
                raise ExportError('message %s: multiplexer switch %s has no layout' % (mname, sel))
        base = [s for s in sigs if not s['mux_signal']]
        base.sort(key=lambda s: (s['name'] not in sel_names, s['name']))
        kept, occupied = [], set()
        for s in base:
            bits = set(signal_bits(s))
            if bits & occupied:
                dropped.append({'message': mname, 'signal': s['name'], 'reason': 'overlaps another signal'})
                continue
            occupied |= bits
            kept.append(s)
        groups = {}
        for s in sigs:
            if s['mux_signal']:
                groups.setdefault(s['mux_value'], []).append(s)
        for v in sorted(groups):
            occ = set(occupied)
            for s in sorted(groups[v], key=lambda s: s['name']):
                bits = set(signal_bits(s))
                if bits & occ:
                    dropped.append({'message': mname, 'signal': s['name'],
                                    'reason': 'overlaps another signal in mux page %d' % v})
                    continue
                occ |= bits
                kept.append(s)
        if not kept:
            continue
        maxbit = max(max(signal_bits(s)) for s in kept)
        nbytes = maxbit // 8 + 1
        want = int(meta.get('length') or 0)
        if nbytes <= want <= 8:
            size = want
        else:
            size = 8 if nbytes <= 8 else next((n for n in FD_SIZES if n >= nbytes), None)
        if size is None:
            for s in kept:
                dropped.append({'message': mname, 'signal': s['name'], 'reason': 'message longer than 64 bytes'})
            continue
        fid = meta.get('id', ids.pop())
        extended = fid > 0x7FF
        if fid > 0x1FFFFFFF:
            raise ExportError('message %s: id %d out of range' % (mname, fid))
        tx = meta.get('transmitter') or node_of(mname)
        msgs.append({
            'name': mname, 'frame_id': fid, 'extended': extended, 'size': size,
            'fd': size > 8, 'transmitter': tx, 'cycle_ms': int(meta.get('cycle_ms') or 0),
            'routed_from': meta.get('routed_from'), 'length_note': meta.get('length_note'),
            'selector': next(iter(sel_names)) if sel_names else None,
            'signals': sorted(kept, key=lambda s: (s['mux_value'] is not None, s['mux_value'] or 0, s['start'], s['name'])),
        })
    return msgs, dropped


# ----------------------------------------------------------------- render

def render_dbc(msgs, firmware, model, bus):
    """Render one DBC file. Returns (text, json_model)."""
    fd_file = any(m['fd'] for m in msgs)
    nodes = sorted({m['transmitter'] for m in msgs if m['transmitter'] != 'Vector__XXX'})
    L = ['VERSION "%s %s"' % (GENERATOR_VERSION, firmware), '', '', 'NS_ :']
    L += ['\t' + s for s in NS_SYMBOLS]
    L += ['', 'BS_:', '', 'BU_: ' + ' '.join(nodes), '', '']
    jmsgs, short_of = [], {}
    for m in msgs:
        dbc_id = m['frame_id'] | (0x80000000 if m['extended'] else 0)
        m['dbc_id'] = dbc_id
        smap = short_names([s['name'] for s in m['signals']])
        short_of[m['name']] = smap
        L.append('BO_ %d %s: %d %s' % (dbc_id, m['name'], m['size'], m['transmitter']))
        for s in m['signals']:
            if s['name'] == m['selector']:
                mux = ' M'
            elif s['mux_value'] is not None:
                mux = ' m%d' % s['mux_value']
            else:
                mux = ''
            lo, hi = phys_range(s)
            s['_min'], s['_max'] = float(fmt_num(lo)), float(fmt_num(hi))
            L.append(' SG_ %s%s : %d|%d@%d%s (%s,%s) [%s|%s] "%s" Vector__XXX' % (
                smap[s['name']], mux, s['start'], s['length'], 1 if s['little'] else 0,
                '-' if s['signed'] else '+', fmt_num(s['scale']), fmt_num(s['offset']),
                fmt_num(lo), fmt_num(hi), s['unit']))
        L.append('')
    for m in msgs:
        if m['transmitter'] != 'Vector__XXX':
            L.append('BO_TX_BU_ %d : %s;' % (m['dbc_id'], m['transmitter']))
    L.append('')
    L.append('')
    net_comment = ('Tesla %s CAN bus database; bus %s; firmware %s. Decoded CAN signal '
                   'definitions (layout, scaling, units, value tables).' % (model_label(model), BUS_LABELS.get(bus, bus), firmware))
    L.append('CM_ "%s";' % ascii_text(net_comment))
    for n in nodes:
        L.append('CM_ BU_ %s "%s";' % (n, ascii_text(node_label(n))))
    for m in msgs:
        L.append('CM_ BO_ %d "%s";' % (m['dbc_id'], ascii_text(describe_message(m))))
        for s in m['signals']:
            s['_comment'] = ascii_text(describe_signal(s))
            L.append('CM_ SG_ %d %s "%s";' % (m['dbc_id'], short_of[m['name']][s['name']], s['_comment']))
    defs = [
        ('', 'BusType', 'STRING', '"CAN"'),
        ('', 'DBName', 'STRING', '""'),
        ('', 'Baudrate', 'INT 0 1000000', '500000'),
        ('', 'BaudrateCANFD', 'INT 0 16000000', '2000000'),
        ('', 'Manufacturer', 'STRING', '""'),
        ('', 'FirmwareVersion', 'STRING', '""'),
        ('', 'VehicleModel', 'STRING', '""'),
        ('BU_', 'ECU', 'STRING', '""'),
        ('BO_', 'GenMsgCycleTime', 'INT 0 3600000', '0'),
        ('BO_', 'GenMsgSendType', 'ENUM ' + ','.join('"%s"' % x for x in SEND_TYPES), '"NoMsgSendType"'),
        ('BO_', 'VFrameFormat', 'ENUM ' + ','.join('"%s"' % x for x in FRAME_FORMATS), '"StandardCAN"'),
        ('BO_', 'CANFD_BRS', 'ENUM "0","1"', '"1"'),
        ('BO_', 'SystemMessageLongSymbol', 'STRING', '""'),
        ('SG_', 'GenSigStartValue', 'FLOAT -1000000000000 1000000000000', '0'),
        ('SG_', 'GenSigSNA', 'STRING', '""'),
        ('SG_', 'SystemSignalLongSymbol', 'STRING', '""'),
        ('SG_', 'Confidence', 'ENUM ' + ','.join('"%s"' % x for x in CONFIDENCE), '"layout-only"'),
    ]
    for obj, name, typ, _ in defs:
        L.append('BA_DEF_ %s"%s" %s;' % (obj + ' ' if obj else '', name, typ))
    for _, name, _, dflt in defs:
        L.append('BA_DEF_DEF_ "%s" %s;' % (name, dflt))
    dbname = '%s_%s' % (re.sub(r'\W', '_', model), bus)
    L.append('BA_ "BusType" "%s";' % ('CAN FD' if fd_file else 'CAN'))
    L.append('BA_ "DBName" "%s";' % dbname)
    L.append('BA_ "Baudrate" 500000;')
    L.append('BA_ "Manufacturer" "Tesla";')
    L.append('BA_ "FirmwareVersion" "%s";' % firmware)
    L.append('BA_ "VehicleModel" "%s";' % model_label(model))
    for n in nodes:
        L.append('BA_ "ECU" BU_ %s "%s";' % (n, n))
    for m in msgs:
        L.append('BA_ "GenMsgCycleTime" BO_ %d %d;' % (m['dbc_id'], m['cycle_ms']))
        L.append('BA_ "GenMsgSendType" BO_ %d %d;' % (m['dbc_id'], 0 if m['cycle_ms'] else 8))
        ff = (15 if m['extended'] else 14) if m['fd'] else (1 if m['extended'] else 0)
        L.append('BA_ "VFrameFormat" BO_ %d %d;' % (m['dbc_id'], ff))
    for m in msgs:
        smap = short_of[m['name']]
        for s in m['signals']:
            sn = smap[s['name']]
            s['_confidence'] = confidence_of(s)
            L.append('BA_ "Confidence" SG_ %d %s %d;' % (m['dbc_id'], sn, CONFIDENCE.index(s['_confidence'])))
            if s['sna'] is not None:
                L.append('BA_ "GenSigSNA" SG_ %d %s "%d";' % (m['dbc_id'], sn, s['sna']))
            if sn != s['name']:
                L.append('BA_ "SystemSignalLongSymbol" SG_ %d %s "%s";' % (m['dbc_id'], sn, s['name']))
    for m in msgs:
        smap = short_of[m['name']]
        for s in m['signals']:
            lo, hi = raw_range(s['length'], s['signed'])
            enum = {k: v for k, v in s['enum'].items() if lo <= k <= hi}
            if s['sna'] is not None and s['sna'] not in enum and lo <= s['sna'] <= hi:
                enum[s['sna']] = 'SNA'
            s['_enum'] = enum
            if enum:
                L.append('VAL_ %d %s %s ;' % (m['dbc_id'], smap[s['name']], ' '.join(
                    '%d "%s"' % (k, enum[k]) for k in sorted(enum, reverse=True))))
    for m in msgs:
        smap = short_of[m['name']]
        for s in m['signals']:
            if s['is_float']:
                L.append('SIG_VALTYPE_ %d %s : %d;' % (m['dbc_id'], smap[s['name']], 1 if s['length'] == 32 else 2))
    L.append('')
    text = '\n'.join(L)
    jm = {
        'firmware': firmware, 'model': model, 'bus': bus, 'db_name': dbname,
        'bus_type': 'CAN FD' if fd_file else 'CAN', 'bus_label': BUS_LABELS.get(bus, bus),
        'messages': [{
            'name': m['name'], 'frame_id': m['frame_id'], 'extended': m['extended'],
            'length': m['size'], 'fd': m['fd'], 'transmitter': m['transmitter'],
            'cycle_ms': m['cycle_ms'], 'comment': ascii_text(describe_message(m)),
            'signals': [{
                'name': s['name'], 'dbc_name': short_of[m['name']][s['name']],
                'start': s['start'], 'length': s['length'],
                'byte_order': 'little_endian' if s['little'] else 'big_endian',
                'signed': s['signed'], 'scale': s['scale'], 'offset': s['offset'],
                'min': s['_min'], 'max': s['_max'], 'unit': s['unit'],
                'multiplexer': s['name'] == m['selector'],
                'mux_value': s['mux_value'], 'sna': s['sna'], 'is_float': s['is_float'],
                'values': {str(k): v for k, v in sorted(s['_enum'].items())},
                'confidence': s['_confidence'], 'comment': s['_comment'],
            } for s in m['signals']],
        } for m in msgs],
    }
    return text, jm


def model_label(model):
    return {'Model3': 'Model 3', 'ModelY': 'Model Y', 'AllModels': 'Model 3 / Model Y'}.get(model, model)


# ----------------------------------------------------------------- export

def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='ascii', newline='\n') as f:
        f.write(text)


def _report(jm, rel):
    sigs = [x for m in jm['messages'] for x in m['signals']]
    return {
        'firmware': jm['firmware'], 'model': jm['model'], 'bus': jm['bus'], 'file': rel,
        'messages': len(jm['messages']), 'signals': len(sigs),
        'enums': sum(1 for x in sigs if x['values']),
        'validated': sum(1 for x in sigs if x['confidence'] == 'validated'),
        'plausible': sum(1 for x in sigs if x['confidence'] == 'plausible'),
        'layout_only': sum(1 for x in sigs if x['confidence'] == 'layout-only'),
        'contradicted': sum(1 for x in sigs if x['confidence'] == 'contradicted'),
        'dropped': len(jm['dropped']),
        'dropped_reasons': _count(d['reason'].split(' in mux')[0] for d in jm['dropped']),
    }


def _emit(out_dir, rel, signals, dropped_in, firmware, model, bus, msg_meta):
    msgs, dropped = build_messages(signals, msg_meta)
    dropped = dropped_in + dropped
    text, jm = render_dbc(msgs, firmware, model, bus)
    names = {(m['name'], x['name']) for m in jm['messages'] for x in m['signals']}
    jm['dropped'] = sorted((d for d in dropped if (d['message'], d['signal']) not in names),
                           key=lambda d: (d['message'], d['signal'], d['reason']))
    base = out_dir / rel
    _write(base.with_suffix('.dbc'), text)
    _write(base.with_suffix('.json'), json.dumps(jm, sort_keys=True, separators=(',', ':')) + '\n')
    return _report(jm, str(Path(rel).with_suffix('.dbc')))


def _with_selectors(subset, all_signals):
    """Add the multiplexer switch of every multiplexed signal in subset."""
    by_key = {(x['message'], x['name']): x for x in all_signals}
    out = {(x['message'], x['name']): x for x in subset}
    for x in subset:
        if x['mux_signal']:
            k = (x['message'], x['mux_signal'])
            if k in by_key:
                out[k] = by_key[k]
    return [out[k] for k in sorted(out)]


def _check_routing(routing):
    for mname, routes in routing.items():
        for r in routes:
            if len(r) != 3 or not re.match(r'^[A-Z][A-Z0-9]*$', str(r[0])) or r[2] not in ('native', 'gateway') \
                    or not isinstance(r[1], int) or not 0 <= r[1] <= 0x1FFFFFFF:
                raise ExportError('bad route for %s: %r' % (mname, r))


def _max_bit(sig):
    return max(signal_bits(sig))


def _fit_frame(part, dlc):
    """Signals of part that fit in a dlc-byte frame (a multiplexed signal
    whose switch does not fit is dropped too). Returns (kept, cut)."""
    lim = 8 * dlc
    kept_names = set()
    for x in part:
        if _max_bit(x) < lim:
            kept_names.add((x['message'], x['name']))
    kept, cut = [], []
    for x in part:
        ok = (x['message'], x['name']) in kept_names and \
            (not x['mux_signal'] or (x['message'], x['mux_signal']) in kept_names)
        (kept if ok else cut).append(x)
    return kept, cut


def export(signal_rows, firmware, out_dir, routing=None, msg_meta=None, signal_meta=None, verdicts=None,
           model_routing=None, frame_lengths=None, flagged=None):
    """Write the DBC + JSON files of one firmware under out_dir; return a report.

    Writes <out_dir>/<firmware>/ETH.{dbc,json}: every message under its
    Ethernet-side (internal) id - not CAN ids. When routing is given, also
    writes <out_dir>/<model>/<firmware>/<BUS>.{dbc,json}.

    signal_rows:   rows shaped like data/<fw>/signals.csv (see REQUIRED_COLUMNS).
    routing:       {message: [(bus, can_id, 'native'|'gateway'), ...]} for the
                   AllModels files (the union of all models); a routed message
                   goes to each bus file under its on-bus id, a message with no
                   route goes to ETH.dbc under its Ethernet-side id.
    model_routing: {model: routing} - per-model maps. Such a model's files hold
                   every message its own map routes (all signals). Models named
                   only in signal_meta 'models' get per-model-evidence subsets
                   routed with `routing`.
    frame_lengths: {model: {(bus, can_id): dlc}} observed on-bus frame lengths.
                   A bus file uses the observed length (AllModels: the longest
                   observed); signals past it are left out ("not carried on
                   CAN"). Without an observation the layout length is kept.
    flagged:       {(bus, can_id): reason} - on-bus ids whose frames do not
                   follow the Ethernet-side layout; left out of that bus file.
    msg_meta:      {message: {'length': int, 'cycle_ms': int}}.
    signal_meta:   {(message, signal): {...}} (see normalise_rows).
    verdicts:      {(message, signal): 'validated'|'plausible'|'contradicted'|...}.
    Raises ExportError on anything it cannot handle.
    """
    if not re.match(r'^\d{4}\.\d+(\.\d+)*$', firmware):
        raise ExportError('bad firmware version %r' % firmware)
    out_dir = Path(out_dir)
    msg_meta = msg_meta or {}
    model_routing = model_routing or {}
    frame_lengths = frame_lengths or {}
    flagged = flagged or {}
    signals, dropped = normalise_rows(signal_rows, signal_meta, verdicts)
    if routing is None:
        return {'files': [_emit(out_dir, '%s/ETH' % firmware, signals, dropped, firmware, 'AllModels', 'ETH',
                                msg_meta)], 'unresolved': []}
    _check_routing(routing)
    for r in model_routing.values():
        _check_routing(r)
    all_lengths = {}
    for fl in frame_lengths.values():
        for k, v in fl.items():
            all_lengths[k] = max(v, all_lengths.get(k, 0))

    def plan(model, subset, rt, lengths):
        """-> {bus: (signals, meta, dropped)} for one model."""
        buses = {}
        for x in subset:
            for bus, can_id, how in sorted(rt.get(x['message']) or [('ETH', None, 'native')]):
                buses.setdefault(bus, {})[x['message']] = (can_id, how)
        out = {}
        for bus in sorted(buses):
            route = buses[bus]
            part = [x for x in subset if x['message'] in route]
            meta, bus_dropped, keep = {}, [], []
            for mname in sorted({x['message'] for x in part}):
                can_id, how = route[mname]
                mp = [x for x in part if x['message'] == mname]
                d = dict(msg_meta.get(mname, {}))
                if can_id is not None:
                    d['id'] = can_id
                    if (bus, can_id) in flagged:
                        bus_dropped += [{'message': mname, 'signal': x['name'],
                                         'reason': 'on-bus frames do not follow this layout: %s' % flagged[(bus, can_id)]}
                                        for x in mp]
                        continue
                    dlc = lengths.get((bus, can_id))
                    if dlc is not None:
                        d['length'] = dlc
                        d['length_note'] = 'frame length observed on a vehicle bus'
                        mp, cut = _fit_frame(mp, dlc)
                        bus_dropped += [{'message': mname, 'signal': x['name'],
                                         'reason': 'not carried on CAN (beyond the %d-byte on-bus frame)' % dlc}
                                        for x in cut]
                    else:
                        d['length_note'] = 'frame length from the layout, not yet observed on a vehicle bus'
                if how == 'gateway':
                    d['transmitter'] = 'GTW'
                    d['routed_from'] = node_of(mname)
                meta[mname] = d
                keep += mp
            ids = {}
            for mname in sorted({x['message'] for x in keep}):
                fid = meta[mname].get('id', next(x['msg_id'] for x in keep if x['message'] == mname))
                if fid in ids:
                    raise ExportError('%s %s: id %d used by %s and %s' % (model, bus, fid, ids[fid], mname))
                ids[fid] = mname
            out[bus] = (keep, meta, bus_dropped, route)
        return out

    all_plan = plan('AllModels', signals, routing, all_lengths)
    # A signal left out of every CAN bus file it is routed to is "not carried on CAN".
    on_can = set()
    for bus, (keep, _, _, _) in all_plan.items():
        if bus != 'ETH':
            on_can |= {(x['message'], x['name']) for x in keep}
    for x in signals:
        routed = [r for r in routing.get(x['message']) or () if r[0] != 'ETH']
        x['not_on_can'] = bool(routed) and (x['message'], x['name']) not in on_can
    reports = [_emit(out_dir, '%s/ETH' % firmware, signals, dropped, firmware, 'AllModels', 'ETH', msg_meta)]
    plans = [('AllModels', all_plan)]
    for model in sorted(model_routing):
        plans.append((model, plan(model, signals, model_routing[model], frame_lengths.get(model, {}))))
    for model in sorted({m for x in signals for m in x['models']} - set(model_routing)):
        subset = _with_selectors([x for x in signals if model in x['models']], signals)
        plans.append((model, plan(model, subset, routing, all_lengths)))
    for model, pl in plans:
        for bus, (keep, meta, bus_dropped, route) in sorted(pl.items()):
            if not keep:
                continue
            base_drop = [d for d in dropped if d['message'] in route] if model == 'AllModels' else []
            reports.append(_emit(out_dir, '%s/%s/%s' % (model, firmware, bus), keep, base_drop + bus_dropped,
                                 firmware, model, bus, meta))
    unresolved = {}
    for x in signals:
        if not [r for r in routing.get(x['message']) or () if r[0] != 'ETH']:
            u = unresolved.setdefault(x['message'], [x['msg_id'], 0])
            u[1] += 1
    return {'files': reports,
            'unresolved': [{'firmware': firmware, 'message': m, 'eth_id': v[0], 'signals': v[1]}
                           for m, v in sorted(unresolved.items())]}


def coverage_markdown(reports):
    """Coverage table (Markdown) for README, generated from export reports."""
    rows = ['| Model | Firmware | Bus | Messages | Signals | Enums | Validated | Plausible | '
            'Layout-only | Contradicted |', '|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    order = lambda r: (r['model'] != 'AllModels', r['model'], [-int(p) for p in r['firmware'].split('.')],
                       r['bus'] == 'ETH', '/' not in r['file'].split('/', 1)[1], r['bus'])
    for r in sorted(reports, key=order):
        where = r['file'].rsplit('.', 1)[0]
        label = r['bus'] if '/' in where.split('/', 1)[1] else 'ETH-side ids, all messages'
        rows.append('| %s | %s | [%s](dbc/%s.dbc) | %d | %d | %d | %d | %d | %d | %d |' % (
            model_label(r['model']), r['firmware'], label, where, r['messages'], r['signals'],
            r['enums'], r['validated'], r['plausible'], r['layout_only'], r['contradicted']))
    return '\n'.join(rows) + '\n'


def _count(it):
    out = {}
    for x in it:
        out[x] = out.get(x, 0) + 1
    return dict(sorted(out.items()))


# ----------------------------------------------------------------- check

SECTION_ORDER = ['VERSION', 'NS_', 'BS_', 'BU_', 'VAL_TABLE_', 'BO_', 'BO_TX_BU_',
                 'CM_', 'BA_DEF_', 'BA_DEF_DEF_', 'BA_', 'VAL_', 'SIG_GROUP_',
                 'SIG_VALTYPE_', 'SG_MUL_VAL_']
FORBIDDEN_STATEMENTS = ('ENVVAR_DATA_', 'EV_DATA_', 'SGTYPE_', 'SIG_TYPE_REF_', 'BA_DEF_SGTYPE_',
                        'BA_SGTYPE_', 'SIGTYPE_VALTYPE_', 'CAT_DEF_', 'CAT_', 'FILTER', 'BU_EV_REL_')
QUOTED_RE = re.compile(r'"[^"]*"')


def _lint_dbc(path, text):
    """Generator checklist (format standard section 11) checks we own."""
    errs = []
    raw = text.encode('ascii', errors='replace')
    if any(b not in (9, 10, 13) and not 32 <= b <= 126 for b in text.encode('utf-8')):
        errs.append('non-ASCII byte')
    if '\r' in text:
        errs.append('CR line ending (file must be LF only)')
    lines = text.split('\n')
    kw_seq, body_lines = [], []
    in_ns = False
    for ln in lines:
        if ln.startswith('\t') and in_ns:
            continue
        in_ns = ln.startswith('NS_ :')
        if not ln.strip():
            continue
        kw = ln.split()[0].rstrip(':')
        if ln.startswith(' SG_ '):
            kw = 'SG_'
        if kw in FORBIDDEN_STATEMENTS:
            errs.append('forbidden statement %s' % kw)
        if kw not in ('SG_',):
            if not kw_seq or kw_seq[-1] != kw:
                kw_seq.append(kw)
        body_lines.append(ln)
        if re.search(r'(?<!\w)0x', QUOTED_RE.sub('""', ln).lower()):
            errs.append('hex number outside string: %s' % ln[:80])
        if re.search(r'(?<![\w.])\.\d', QUOTED_RE.sub('""', ln)):
            errs.append('leading-dot number: %s' % ln[:80])
    order = [k for k in kw_seq if k in SECTION_ORDER]
    if order != sorted(order, key=SECTION_ORDER.index) or len(order) != len(set(order)):
        errs.append('section order wrong: %s' % order)
    if 'BS_:' not in lines:
        errs.append('BS_: missing or not empty')
    ns_count = 0
    if 'NS_ :' in lines:
        i = lines.index('NS_ :') + 1
        while i < len(lines) and lines[i].startswith('\t'):
            ns_count += 1
            i += 1
    if ns_count != len(NS_SYMBOLS):
        errs.append('NS_ block has %d entries' % ns_count)
    bu = next((ln for ln in lines if ln.startswith('BU_:')), None)
    nodes = set(bu.split()[1:]) if bu else set()
    for n in nodes:
        if not IDENT_RE.match(n) or n.upper() in DBC_KEYWORDS:
            errs.append('bad node name %s' % n)
    msg_ids, msg_names, val_keys = set(), set(), set()
    cur, cur_sigs, cur_size = None, set(), 0
    ba_defs, ba_defaults = {}, set()
    for ln in lines:
        if ln.startswith('BO_ '):
            m = re.match(r'^BO_ (\d+) (\w+): (\d+) (\w+)$', ln)
            if not m:
                errs.append('bad BO_ line %s' % ln[:80])
                continue
            mid, name, size, tx = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)
            if mid in msg_ids:
                errs.append('duplicate message id %d' % mid)
            if name in msg_names:
                errs.append('duplicate message name %s' % name)
            msg_ids.add(mid)
            msg_names.add(name)
            if not IDENT_RE.match(name):
                errs.append('bad message name %s' % name)
            if tx != 'Vector__XXX' and tx not in nodes:
                errs.append('transmitter %s not in BU_' % tx)
            if size not in FD_SIZES:
                errs.append('invalid frame size %d for %s' % (size, name))
            if mid & 0x80000000:
                if mid & 0x7FFFFFFF > 0x1FFFFFFF:
                    errs.append('extended id out of range %d' % mid)
            elif mid > 0x7FF:
                errs.append('standard id > 0x7FF without extended flag: %d' % mid)
            cur, cur_sigs, cur_size = name, set(), size
        elif ln.startswith(' SG_ '):
            m = re.match(r'^ SG_ (\w+)(?: (M|m\d+M?))? : (\d+)\|(\d+)@([01])([+-]) \(([^,]+),([^)]+)\) '
                         r'\[([^|]+)\|([^\]]+)\] "([^"]*)" ([\w,]+)$', ln)
            if not m:
                errs.append('bad SG_ line %s' % ln[:80])
                continue
            sname = m.group(1)
            if not IDENT_RE.match(sname) or sname.upper() in DBC_KEYWORDS or re.match(r'^(M|m\d+M?)$', sname):
                errs.append('bad signal name %s' % sname)
            if sname in cur_sigs:
                errs.append('duplicate signal %s in %s' % (sname, cur))
            cur_sigs.add(sname)
            if float(m.group(7)) == 0:
                errs.append('factor 0 %s' % sname)
            if float(m.group(9)) > float(m.group(10)):
                errs.append('min > max %s' % sname)
            for rcv in m.group(12).split(','):
                if rcv != 'Vector__XXX' and rcv not in nodes:
                    errs.append('receiver %s not in BU_' % rcv)
            st, ln_ = int(m.group(3)), int(m.group(4))
            bits = range(st, st + ln_) if m.group(5) == '1' else motorola_bits(st, ln_)
            if max(bits) >= 8 * cur_size or min(bits) < 0:
                errs.append('signal %s does not fit %s' % (sname, cur))
        elif ln.startswith('BO_TX_BU_ '):
            m = re.match(r'^BO_TX_BU_ (\d+) : ([\w,]+);$', ln)
            if not m or int(m.group(1)) not in msg_ids:
                errs.append('bad BO_TX_BU_ %s' % ln[:80])
            else:
                for n in m.group(2).split(','):
                    if n not in nodes:
                        errs.append('BO_TX_BU_ node %s not in BU_' % n)
        elif ln.startswith('CM_'):
            if ln.count('"') != 2 or '\\' in ln or not ln.endswith('";'):
                errs.append('bad CM_ line %s' % ln[:80])
        elif ln.startswith('BA_DEF_DEF_ '):
            ba_defaults.add(re.match(r'^BA_DEF_DEF_ "(\w+)"', ln).group(1))
        elif ln.startswith('BA_DEF_ '):
            m = re.match(r'^BA_DEF_ (?:(BU_|BO_|SG_|EV_) )?"(\w+)" (.*);$', ln)
            if not m or len(m.group(2)) > MAX_NAME:
                errs.append('bad BA_DEF_ %s' % ln[:80])
                continue
            ba_defs[m.group(2)] = (m.group(1) or '', m.group(3))
        elif ln.startswith('BA_ '):
            m = re.match(r'^BA_ "(\w+)" (?:(BU_) (\w+) |(BO_) (\d+) |(SG_) (\d+) (\w+) )?(.*);$', ln)
            if not m or m.group(1) not in ba_defs:
                errs.append('BA_ without BA_DEF_: %s' % ln[:80])
                continue
            obj = m.group(2) or m.group(4) or m.group(6) or ''
            dobj, dtyp = ba_defs[m.group(1)]
            if obj != dobj:
                errs.append('BA_ object type mismatch %s' % ln[:80])
            val = m.group(9)
            if dtyp.startswith('ENUM'):
                n = len(re.findall(r'"[^"]*"', dtyp))
                if not val.isdigit() or int(val) >= n:
                    errs.append('ENUM BA_ value not a valid index: %s' % ln[:80])
            elif dtyp == 'STRING':
                if not (val.startswith('"') and val.endswith('"') and val.count('"') == 2):
                    errs.append('bad STRING BA_ %s' % ln[:80])
            elif dtyp.startswith('INT'):
                _, lo, hi = dtyp.split()
                if not re.match(r'^-?\d+$', val) or not int(lo) <= int(val) <= int(hi):
                    errs.append('INT BA_ out of range %s' % ln[:80])
        elif ln.startswith('VAL_ '):
            m = re.match(r'^VAL_ (\d+) (\w+) ((?:-?\d+ "[^"]*" )+);$', ln)
            if not m:
                errs.append('bad VAL_ line %s' % ln[:80])
                continue
            key = (m.group(1), m.group(2))
            if key in val_keys:
                errs.append('duplicate VAL_ %s' % (key,))
            val_keys.add(key)
            ks = re.findall(r'(-?\d+) "', m.group(3))
            if len(ks) != len(set(ks)):
                errs.append('duplicate VAL_ key %s' % (key,))
        elif ln.startswith('SIG_VALTYPE_ '):
            if not re.match(r'^SIG_VALTYPE_ \d+ \w+ : [12];$', ln):
                errs.append('bad SIG_VALTYPE_ %s' % ln[:80])
    for name in ba_defs:
        if name not in ba_defaults:
            errs.append('BA_DEF_ %s has no BA_DEF_DEF_' % name)
    for name in ba_defaults:
        if name not in ba_defs:
            errs.append('BA_DEF_DEF_ %s has no BA_DEF_' % name)
    return errs


def _gate_text(text):
    """Free-text parts of a DBC that the source gate applies to: comments and
    string attribute values other than long-name symbols (which are the
    vehicle's own identifiers). Identifiers and enum labels are vehicle data."""
    parts = []
    for ln in text.split('\n'):
        if ln.startswith('CM_') or (ln.startswith('BA_ ') and 'LongSymbol' not in ln
                                    and not ln.startswith('BA_ "ECU"')):
            parts.extend(q.strip('"') for q in QUOTED_RE.findall(ln))
        elif ln.startswith('VERSION'):
            parts.append(ln)
    return '\n'.join(parts)


def _sig_tuple(s):
    return (s.name, s.start, s.length, s.byte_order, s.is_signed, float(s.scale), float(s.offset),
            None if s.minimum is None else float(s.minimum),
            None if s.maximum is None else float(s.maximum), s.unit or '',
            s.is_multiplexer, tuple(s.multiplexer_ids or ()),
            tuple(sorted((int(k), str(v)) for k, v in (s.choices or {}).items())),
            s.comment or '', s.is_float)


def check(out_dir):
    """Validate every .dbc (and JSON twin) under out_dir. Returns error list."""
    import cantools  # validation-only dependency
    try:
        import canmatrix.formats as cmf
    except ImportError:
        cmf = None
    out_dir = Path(out_dir)
    errors = []
    files = sorted(out_dir.rglob('*.dbc'))
    if not files:
        return ['no .dbc files under %s' % out_dir]
    for p in files:
        rel = p.relative_to(out_dir)
        text = p.read_bytes().decode('utf-8', errors='replace')
        errors += ['%s: %s' % (rel, e) for e in _lint_dbc(p, text)]
        try:
            db = cantools.database.load_file(str(p), strict=True, encoding='ascii')
        except Exception as e:  # noqa: BLE001 - report any loader failure
            errors.append('%s: cantools strict load failed: %s' % (rel, str(e)[:300]))
            continue
        try:
            db2 = cantools.database.load_string(db.as_dbc_string(), strict=True)
            a = {m.frame_id: (m.name, m.length, m.is_extended_frame, tuple(sorted(_sig_tuple(s) for s in m.signals)))
                 for m in db.messages}
            b = {m.frame_id: (m.name, m.length, m.is_extended_frame, tuple(sorted(_sig_tuple(s) for s in m.signals)))
                 for m in db2.messages}
            if a != b:
                diff = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
                errors.append('%s: round trip differs for %d messages (e.g. id %s)' % (rel, len(diff), diff[:3]))
        except Exception as e:  # noqa: BLE001
            errors.append('%s: round trip failed: %s' % (rel, str(e)[:300]))
        jp = p.with_suffix('.json')
        if not jp.exists():
            errors.append('%s: JSON twin missing' % rel)
        else:
            jm = json.loads(jp.read_text(encoding='ascii'))
            for m in jm['messages']:
                try:
                    dm = db.get_message_by_name(m['name'])
                except KeyError:
                    errors.append('%s: message %s missing in DBC' % (rel, m['name']))
                    continue
                if dm.frame_id != m['frame_id'] or dm.length != m['length'] or len(dm.signals) != len(m['signals']):
                    errors.append('%s: message %s differs from JSON' % (rel, m['name']))
                    continue
                for s in m['signals']:
                    try:
                        ds = dm.get_signal_by_name(s['name'])
                    except KeyError:
                        errors.append('%s: %s.%s missing (long name not restored?)' % (rel, m['name'], s['name']))
                        continue
                    got = (ds.start, ds.length, ds.byte_order, ds.is_signed, float(ds.scale), float(ds.offset),
                           float(ds.minimum), float(ds.maximum), ds.unit or '', ds.comment or '',
                           {str(k): str(v) for k, v in (ds.choices or {}).items()})
                    want = (s['start'], s['length'], s['byte_order'], s['signed'], s['scale'], s['offset'],
                            s['min'], s['max'], s['unit'], s['comment'], s['values'])
                    if got != want:
                        errors.append('%s: %s.%s differs from JSON: %s vs %s' % (rel, m['name'], s['name'], got, want))
            if len(db.messages) != len(jm['messages']):
                errors.append('%s: message count %d != JSON %d' % (rel, len(db.messages), len(jm['messages'])))
        if cmf is not None:
            try:
                import logging
                logging.getLogger('canmatrix').setLevel(logging.ERROR)
                res = cmf.loadp(str(p), dbcImportEncoding='ascii')
                cm_db = next(iter(res.values()))
                if len(cm_db.frames) != len(db.messages):
                    errors.append('%s: canmatrix frame count %d != %d' % (rel, len(cm_db.frames), len(db.messages)))
            except Exception as e:  # noqa: BLE001
                errors.append('%s: canmatrix load failed: %s' % (rel, str(e)[:200]))
    for p in sorted(out_dir.rglob('*')):
        if p.is_file():
            raw = p.read_bytes()
            pii = scan_pii(raw)
            if pii:
                errors.append('%s: PII gate: %s' % (p.relative_to(out_dir), ', '.join(pii)))
            text = raw.decode('utf-8', errors='replace')
            if p.suffix == '.dbc':
                gtext = _gate_text(text)
            elif p.suffix == '.json':
                gtext = '\n'.join(_json_free_text(json.loads(text)))
            else:
                gtext = text
            hits = scan_source_disclosure(gtext)
            if hits:
                errors.append('%s: source-disclosure gate: %s' % (p.relative_to(out_dir), ', '.join(hits)))
    return errors


def _json_free_text(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('comment', 'reason', 'db_name', 'bus_type', 'bus_label') and isinstance(v, str):
                yield v
            else:
                yield from _json_free_text(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _json_free_text(v)


def dbc_free_text(text):
    """Public: free text of a DBC file that the source-disclosure gate scans."""
    return _gate_text(text)


def json_free_text(text):
    """Public: free text of a JSON twin that the source-disclosure gate scans."""
    return '\n'.join(_json_free_text(json.loads(text)))


# ----------------------------------------------------------------- CLI

def _read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_inputs(fwdir):
    """Load one data/<fw>/ directory into export() keyword arguments."""
    fwdir = Path(fwdir)
    kw = {'signal_rows': load_signal_rows(fwdir / 'signals.csv'), 'firmware': fwdir.name}
    mp = fwdir / 'messages.csv'
    if mp.exists():
        kw['routing'], kw['msg_meta'] = {}, {}
        for r in _read_csv(mp):
            for c in ('message', 'length', 'cycle_ms'):
                if c not in r:
                    raise ExportError('%s: missing column %s' % (mp, c))
            kw['msg_meta'][r['message']] = {
                'length': parse_int(r['length'], r['message'] + '.length') if r['length'] else 0,
                'cycle_ms': parse_int(r['cycle_ms'], r['message'] + '.cycle_ms') if r['cycle_ms'] else 0}
            routes = []
            for part in filter(None, (r.get('routes') or '').split(';')):
                bits = part.split(':')
                if len(bits) != 3:
                    raise ExportError('%s: bad route %r' % (mp, part))
                routes.append((bits[0], parse_int(bits[1], r['message'] + '.route'), bits[2]))
            if routes:
                kw['routing'][r['message']] = routes
    ip = fwdir / 'id-map.csv'
    if ip.exists():
        per_model = load_id_map(ip, kw['signal_rows'], fwdir.name)
        kw['routing'] = union_routing(per_model)
        kw['model_routing'] = {m: rt for m, rt in per_model.items() if m}
    fl = fwdir.parent / 'can-frame-lengths.csv'
    if fl.exists():
        kw['frame_lengths'] = {}
        for r in _read_csv(fl):
            for c in ('model', 'bus', 'can_id', 'dlc'):
                if c not in r:
                    raise ExportError('%s: missing column %s' % (fl, c))
            dlc = parse_int(r['dlc'], 'frame length dlc')
            if dlc not in FD_SIZES:
                raise ExportError('%s: bad dlc %d' % (fl, dlc))
            kw['frame_lengths'].setdefault(r['model'], {})[(r['bus'], parse_int(r['can_id'], 'frame length can_id'))] = dlc
    fp = fwdir.parent / 'can-flagged.csv'
    if fp.exists():
        kw['flagged'] = {}
        for r in _read_csv(fp):
            for c in ('bus', 'can_id', 'reason'):
                if c not in r:
                    raise ExportError('%s: missing column %s' % (fp, c))
            kw['flagged'][(r['bus'], parse_int(r['can_id'], 'flagged can_id'))] = ascii_text(r['reason'])
    sp = fwdir / 'signal-meta.csv'
    if sp.exists():
        kw['signal_meta'] = {(r['message'], r['signal']): r for r in _read_csv(sp)}
    vp = fwdir / 'log-verdicts.csv'
    if vp.exists():
        kw['verdicts'] = {}
        for r in _read_csv(vp):
            for c in ('fw', 'signal', 'message', 'verdict'):
                if c not in r:
                    raise ExportError('%s: missing column %s' % (vp, c))
            if r['fw'] == fwdir.name:
                kw['verdicts'][(r['message'], r['signal'])] = r['verdict'].strip()
    return kw


def load_id_map(path, signal_rows, firmware=None):
    """Load a pluggable internal-id -> CAN-bus id map into export()'s routing.

    CSV columns: eth_id, bus, can_id (required); fw, model, message, how
    (optional). Returns {model: routing}; rows without a model go under ''.
    eth_id/can_id may be decimal or 0x-hex; bus is an upper-case bus name
    (VEH, CH, PARTY, ...); how is 'native' (default) or 'gateway'. Rows whose
    fw differs from firmware are skipped. eth_id is joined to message names
    through signal_rows; a message column, when present, must agree.
    """
    rows = _read_csv(path)
    for c in ('eth_id', 'bus', 'can_id'):
        if rows and c not in rows[0]:
            raise ExportError('%s: missing column %s' % (path, c))
    by_eth = {}
    for r in signal_rows:
        by_eth[parse_int(r['eth_id'], r['signal'] + '.eth_id')] = r['message'].strip()
    per_model = {}
    for r in rows:
        if firmware and r.get('fw') and r['fw'] != firmware:
            continue
        model = (r.get('model') or '').strip()
        if model and not re.match(r'^[A-Za-z][A-Za-z0-9]*$', model):
            raise ExportError('%s: bad model %r' % (path, model))
        routing = per_model.setdefault(model, {})
        eth = parse_int(r['eth_id'], '%s eth_id' % path)
        if eth not in by_eth:
            continue
        msg = by_eth[eth]
        if r.get('message') and r['message'].strip() and r['message'].strip() != msg:
            raise ExportError('%s: eth_id %d is %s in the signals, %s in the map' % (path, eth, msg, r['message']))
        bus = r['bus'].strip().upper()
        if not re.match(r'^[A-Z][A-Z0-9]*$', bus):
            raise ExportError('%s: bad bus %r' % (path, r['bus']))
        how = (r.get('how') or 'native').strip() or 'native'
        route = (bus, parse_int(r['can_id'], '%s can_id' % path), how)
        if route not in routing.setdefault(msg, []):
            routing[msg].append(route)
    return {model: {m: sorted(v) for m, v in rt.items()} for model, rt in per_model.items()}


def union_routing(per_model):
    """Union of per-model routings (the AllModels files)."""
    out = {}
    for rt in per_model.values():
        for m, routes in rt.items():
            for r in routes:
                if r not in out.setdefault(m, []):
                    out[m].append(r)
    return {m: sorted(v) for m, v in out.items()}


def _build_all(repo, out_dir, id_map=None, unresolved=None):
    reports = []
    for fwdir in sorted((repo / 'data').iterdir()):
        if fwdir.is_dir() and (fwdir / 'signals.csv').exists():
            kw = load_inputs(fwdir)
            if id_map:
                per_model = load_id_map(id_map, kw['signal_rows'], fwdir.name)
                kw['routing'] = union_routing(per_model)
                kw['model_routing'] = {m: rt for m, rt in per_model.items() if m}
            res = export(out_dir=out_dir, **kw)
            reports += res['files']
            if unresolved is not None:
                unresolved += res.get('unresolved', [])
    return reports


COVERAGE_BEGIN = '<!-- coverage:begin (generated by tools/export_dbc.py) -->'
COVERAGE_END = '<!-- coverage:end -->'


def _readme_with_coverage(readme_text, reports):
    if COVERAGE_BEGIN not in readme_text or COVERAGE_END not in readme_text:
        raise ExportError('README.md lacks the coverage markers')
    head, rest = readme_text.split(COVERAGE_BEGIN, 1)
    _, tail = rest.split(COVERAGE_END, 1)
    return head + COVERAGE_BEGIN + '\n' + coverage_markdown(reports) + COVERAGE_END + tail


# Id anchors confirmed for 2026.26.6.5 (CAN id on a bus <-> Ethernet-side id).
ANCHORS = [
    # (bus file, CAN id, expected message or None, Ethernet-side id or None)
    ('VEH', 0x352, 'BMS_energyStatus', 0x2B2),
    ('VEH', 0x72A, 'BMS_serialNumber', 0x7FA),  # no signal layout yet -> skipped
    ('VEH', 0x5F3, 'UI_odo', 0x3F3),
    ('CH', 0x111, 'RCM_inertial2', 0x116),
]
ANCHORS_ABSENT = [('VEH', 0x111, 'VCRIGHT_'), ('VEH', 0x112, 'VCRIGHT_')]


def check_anchors(dbc_root, firmware='2026.26.6.5'):
    """Assert the known id anchors in AllModels/<fw>/<BUS>.dbc.

    Returns (errors, skipped): an anchor whose message has no signal layout in
    this firmware's data (absent from both files) is skipped, not failed."""
    import cantools
    dbc_root = Path(dbc_root)
    errs, skipped = [], []
    eth_path = dbc_root / firmware / 'ETH.dbc'
    if not eth_path.exists():
        return ['anchors: %s missing' % eth_path.relative_to(dbc_root)], skipped
    eth = {m.frame_id: m.name for m in cantools.database.load_file(str(eth_path), strict=False).messages}
    cache = {}

    def bus_ids(bus):
        if bus not in cache:
            p = dbc_root / 'AllModels' / firmware / ('%s.dbc' % bus)
            cache[bus] = {m.frame_id: m.name for m in cantools.database.load_file(str(p), strict=False).messages} \
                if p.exists() else None
        return cache[bus]
    for bus, can_id, name, eth_id in ANCHORS:
        ids = bus_ids(bus)
        if ids is None:
            errs.append('anchors: %s.dbc missing' % bus)
            continue
        got = ids.get(can_id)
        want = name or eth.get(eth_id)
        if got is None and eth_id is not None and eth.get(eth_id) is None:
            skipped.append('%s 0x%X (%s): no signal layout in the data yet' % (bus, can_id, name))
            continue
        if got is None or got != want or (eth_id is not None and eth.get(eth_id) != got):
            errs.append('anchor %s 0x%X: got %s, expected %s (Ethernet-side 0x%X = %s)' % (
                bus, can_id, got, want, eth_id or 0, eth.get(eth_id)))
    for bus, can_id, prefix in ANCHORS_ABSENT:
        ids = bus_ids(bus) or {}
        if (ids.get(can_id) or '').startswith(prefix):
            errs.append('anchor %s 0x%X must not be %s*' % (bus, can_id, prefix))
    return errs, skipped


def _diff_trees(a, b):
    diffs = []
    fa = {p.relative_to(a) for p in a.rglob('*') if p.is_file()}
    fb = {p.relative_to(b) for p in b.rglob('*') if p.is_file()}
    for rel in sorted(fa ^ fb):
        diffs.append('only in %s: %s' % ('generated' if rel in fa else 'committed', rel))
    for rel in sorted(fa & fb):
        if not filecmp.cmp(a / rel, b / rel, shallow=False):
            diffs.append('differs: %s' % rel)
    return diffs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent),
                    help='signal database repository root (default: this tool\'s repo)')
    ap.add_argument('--check', action='store_true',
                    help='regenerate to a temp dir, diff against committed dbc/, validate')
    ap.add_argument('--id-map', default=None,
                    help='CSV mapping internal ids to (bus, CAN id); overrides the routes in data/<fw>/messages.csv')
    args = ap.parse_args(argv)
    unresolved = []
    repo = Path(args.repo)
    committed = repo / 'dbc'
    if args.check:
        tmp = Path(tempfile.mkdtemp(prefix='dbc_check_'))
        try:
            reports = _build_all(repo, tmp, args.id_map, unresolved)
            diffs = _diff_trees(tmp, committed) if committed.exists() else ['dbc/ missing']
            errors = check(committed if committed.exists() else tmp)
            anchor_errs, anchor_skipped = check_anchors(committed if committed.exists() else tmp)
            errors += anchor_errs
            readme = repo / 'README.md'
            if readme.read_text(encoding='utf-8') != _readme_with_coverage(readme.read_text(encoding='utf-8'), reports):
                diffs.append('README.md coverage table is stale (run tools/export_dbc.py)')
            for doc in ('README.md', 'INDEX.md'):
                dp = repo / doc
                if dp.exists():
                    raw = dp.read_bytes()
                    # Docs legitimately name this repo's own files (ALL.dbc,
                    # signals.csv), so the 'file name' pattern is skipped here only.
                    labels = [l for l in scan_source_disclosure(raw.decode('utf-8', errors='replace'))
                              if l != 'file name']
                    for label in scan_pii(raw) + labels:
                        errors.append('%s: gate: %s' % (doc, label))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        for r in reports:
            print('%-36s msgs=%d sigs=%d enums=%d validated=%d plausible=%d layout-only=%d contradicted=%d dropped=%d %s' % (
                r['file'], r['messages'], r['signals'], r['enums'], r['validated'], r['plausible'],
                r['layout_only'], r['contradicted'], r['dropped'], r['dropped_reasons']))
        for u in unresolved:
            print('UNRESOLVED (no CAN-bus id): %s %s eth_id=%d signals=%d' % (
                u['firmware'], u['message'], u['eth_id'], u['signals']))
        print('UNRESOLVED total: %d messages, %d signals' % (len(unresolved), sum(u['signals'] for u in unresolved)))
        for d in diffs:
            print('DETERMINISM: ' + d)
        for e in errors[:200]:
            print('ERROR: ' + e)
        nfiles = len(list(committed.rglob('*.dbc'))) if committed.exists() else 0
        if diffs or errors:
            print('CHECK FAILED: %d diffs, %d errors' % (len(diffs), len(errors)))
            return 1
        for a in anchor_skipped:
            print('ANCHOR SKIPPED: ' + a)
        print('ANCHORS OK: %d of %d id anchors checked + %d must-not-be-on-VEH checks' % (
            len(ANCHORS) - len(anchor_skipped), len(ANCHORS), len(ANCHORS_ABSENT)))
        print('CHECK OK: %d DBC files regenerated identically, checklist lint clean, cantools strict load + '
              'round trip OK, JSON twins agree, canmatrix load OK, PII + source-disclosure gates clean' % nfiles)
        return 0
    before = {p for p in committed.rglob('*') if p.is_file()} if committed.exists() else set()
    reports = _build_all(repo, committed, args.id_map, unresolved)
    produced = set()
    for r in reports:
        produced |= {committed / r['file'], (committed / r['file']).with_suffix('.json')}
    for stale in sorted(before - produced):
        # generated output that the current inputs no longer produce (git keeps history)
        if stale.suffix in ('.dbc', '.json'):
            print('removed stale generated file %s' % stale.relative_to(repo))
            stale.unlink()
    readme = repo / 'README.md'
    readme.write_text(_readme_with_coverage(readme.read_text(encoding='utf-8'), reports), encoding='utf-8')
    for r in reports:
        print('wrote %s: %d messages, %d signals, dropped %d' % (r['file'], r['messages'], r['signals'], r['dropped']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
