#!/usr/bin/env python3
"""
Export the Tesla CAN signal database as Vector DBC files (+ JSON twins).

Library API (no hard-coded paths; every path is an argument)
------------------------------------------------------------
    load_signal_rows(path)            -> list[dict]
        Read a signals CSV (columns of data/<fw>/signals.csv). Extra columns
        are tolerated; a missing required column raises ExportError.

    export(signal_rows, firmware, out_dir, model_map=None, routing=None)
                                      -> report dict
        Build every DBC/JSON for one firmware under out_dir and return a
        report (files written, per-file counts, dropped signals).
        * model_map: {signal_name: [model, ...]} or None. Signals listed go
          to dbc/<model>/<fw>/...; None writes the single-file layout.
        * routing:   {message_name: [(bus, can_id), ...]} or None. None puts
          every message in ALL.dbc under its internal message id.
        Deterministic and idempotent: same inputs -> byte-identical files.

    check(out_dir)                    -> list[str] (errors; empty = pass)
        Validate every .dbc under out_dir: generator checklist (ASCII,
        section order, identifiers, attributes, nodes, FD lengths, duplicate
        ids/VAL_), cantools strict load, cantools round trip, JSON twin
        agreement, canmatrix load (if installed), PII + source-disclosure
        gates (from tools/build.py).

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
CONFIDENCE = ['layout-only', 'plausible', 'validated']
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


def normalise_rows(rows):
    """Validate + convert rows. Returns (signals, dropped)."""
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
            try:
                raw = json.loads(ev)
            except ValueError:
                raise ExportError('%s: enum_values is not JSON: %r' % (name, ev[:80]))
            if not isinstance(raw, dict):
                raise ExportError('%s: enum_values must be a JSON object' % name)
            for k, v in raw.items():
                sig['enum'][parse_int(str(k), name + '.enum key')] = ascii_text(str(v)) or str(k)
        sna = (r.get('sna') or '').strip()
        if sna:
            sig['sna'] = parse_int(sna, name + '.sna')
        if (r.get('is_float') or '').strip() == '1':
            sig['is_float'] = True
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
        text += '; raw %d = signal not available (SNA)' % sig['sna']
    return text


def describe_message(msg):
    w = words_from_name(msg['name'])
    text = '%s message: %s' % (node_label(msg['transmitter']), w) if w else \
        '%s message' % node_label(msg['transmitter'])
    if gated(text):
        text = '%s message' % node_label(msg['transmitter'])
    return text


def phys_range(sig):
    lo, hi = raw_range(sig['length'], sig['signed'])
    if sig['sna'] is not None:
        if sig['sna'] == hi and hi > lo:
            hi -= 1
        elif sig['sna'] == lo and hi > lo:
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
    if sig['unit'] or sig['enum'] or ascii_text(sig['description']):
        return 'plausible'
    return 'layout-only'


def build_messages(signals, msg_meta=None):
    """Group signals into messages, resolve overlaps. Returns (msgs, dropped).

    msg_meta: {message_name: {'id': int, 'cycle_ms': int, 'transmitter': str}}
    overrides the frame id / cycle time (bus files use the on-bus CAN id).
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
    L.append('')
    net_comment = ('Tesla %s CAN bus database; bus %s; firmware %s. Decoded CAN signal '
                   'definitions (layout, scaling, units, value tables).' % (model_label(model), bus, firmware))
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
        'bus_type': 'CAN FD' if fd_file else 'CAN',
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


def export(signal_rows, firmware, out_dir, model_map=None, routing=None, msg_meta=None):
    """Write DBC + JSON files for one firmware. Returns a report dict.

    Layout without model_map/routing: <out_dir>/<firmware>/ALL.{dbc,json}.
    """
    if not re.match(r'^\d{4}\.\d+(\.\d+)*$', firmware):
        raise ExportError('bad firmware version %r' % firmware)
    if model_map is not None or routing is not None:
        raise ExportError('model_map/routing layout not implemented in this version')
    out_dir = Path(out_dir)
    signals, dropped = normalise_rows(signal_rows)
    msgs, drop2 = build_messages(signals, msg_meta)
    dropped += drop2
    text, jm = render_dbc(msgs, firmware, 'AllModels', 'ALL')
    jm['dropped'] = sorted(dropped, key=lambda d: (d['message'], d['signal']))
    base = out_dir / firmware / 'ALL'
    _write(base.with_suffix('.dbc'), text)
    _write(base.with_suffix('.json'), json.dumps(jm, indent=1, sort_keys=True) + '\n')
    sigs = [s for m in jm['messages'] for s in m['signals']]
    rep = {
        'firmware': firmware, 'model': 'AllModels', 'bus': 'ALL',
        'file': str(base.with_suffix('.dbc').relative_to(out_dir)),
        'messages': len(jm['messages']), 'signals': len(sigs),
        'enums': sum(1 for s in sigs if s['values']),
        'validated': sum(1 for s in sigs if s['confidence'] == 'validated'),
        'plausible': sum(1 for s in sigs if s['confidence'] == 'plausible'),
        'layout_only': sum(1 for s in sigs if s['confidence'] == 'layout-only'),
        'dropped': len(jm['dropped']),
        'dropped_reasons': _count(d['reason'].split(' in mux')[0] for d in jm['dropped']),
    }
    return {'files': [rep]}


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
            if k in ('comment', 'reason', 'db_name', 'bus_type') and isinstance(v, str):
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

def _build_all(repo, out_dir):
    reports = []
    for fwdir in sorted((repo / 'data').iterdir()):
        csvp = fwdir / 'signals.csv'
        if fwdir.is_dir() and csvp.exists():
            rows = load_signal_rows(csvp)
            reports += export(rows, fwdir.name, out_dir)['files']
    return reports


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
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    committed = repo / 'dbc'
    if args.check:
        tmp = Path(tempfile.mkdtemp(prefix='dbc_check_'))
        try:
            reports = _build_all(repo, tmp)
            diffs = _diff_trees(tmp, committed) if committed.exists() else ['dbc/ missing']
            errors = check(committed if committed.exists() else tmp)
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
            print('%-40s messages=%d signals=%d enums=%d validated=%d plausible=%d layout-only=%d dropped=%d %s' % (
                r['file'], r['messages'], r['signals'], r['enums'], r['validated'], r['plausible'],
                r['layout_only'], r['dropped'], r['dropped_reasons']))
        for d in diffs:
            print('DETERMINISM: ' + d)
        for e in errors[:200]:
            print('ERROR: ' + e)
        nfiles = len(list(committed.rglob('*.dbc'))) if committed.exists() else 0
        if diffs or errors:
            print('CHECK FAILED: %d diffs, %d errors' % (len(diffs), len(errors)))
            return 1
        print('CHECK OK: %d DBC files regenerated identically, checklist lint clean, cantools strict load + '
              'round trip OK, JSON twins agree, canmatrix load OK, PII + source-disclosure gates clean' % nfiles)
        return 0
    reports = _build_all(repo, committed)
    for r in reports:
        print('wrote %s: %d messages, %d signals, dropped %d' % (r['file'], r['messages'], r['signals'], r['dropped']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
