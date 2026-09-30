#!/usr/bin/env python3
"""
Tesla CAN signal database: shared helpers and the repository gates.

    python3 tools/build.py            # run the gates (same as --check)
    python3 tools/build.py --check    # PII + source-disclosure gates over
                                      # data/, dbc/, docs/, README.md, INDEX.md
    python3 tools/build.py --fix      # rewrite gate-failing descriptions in
                                      # data/<fw>/signals.{csv,json}, then gate

Exit status 0 = clean. Signal/message names and value-table labels are the
vehicle's own identifiers and are not rewritten; the source-disclosure gate
applies to free text (descriptions, comments, docs).
"""

import csv
import json
import sys
import re
import os
from pathlib import Path


# Device name mappings from signal prefix
DEVICE_NAMES = {
    'BMS': 'BMS Battery computer',
    'HVP': 'HVP High Voltage Processor',
    'VCFRONT': 'VCFRONT Front body controller',
    'DI': 'DI Drive inverter',
    'PCS': 'PCS Charger / DC-DC',
    'VCLEFT': 'VCLEFT Left body controller',
    'VCRIGHT': 'VCRIGHT Right body controller',
    'GTW': 'GTW Gateway',
    'UI': 'UI Touchscreen',
    'EPAS': 'EPAS Power steering',
    'ESP': 'ESP Stability control',
}


def get_device_from_signal(signal_name):
    """Extract device name from signal prefix."""
    if not signal_name:
        return signal_name
    # Get prefix before first underscore
    prefix = signal_name.split('_')[0]
    return DEVICE_NAMES.get(prefix, prefix)


def scan_pii(content):
    """Scan for PII patterns and return list of findings."""
    findings = []

    # VIN pattern: 5YJ, 7SA, LRW, XP7, 7G2 followed by 14 alphanumeric (no I, O, Q)
    vin_pattern = rb'\b(5YJ|7SA|LRW|XP7|7G2)[A-HJ-NPR-Z0-9]{14}\b'
    if re.search(vin_pattern, content):
        findings.append('VIN number')

    # MAC address pattern
    mac_pattern = rb'([0-9A-F]{2}:){5}[0-9A-F]{2}'
    if re.search(mac_pattern, content, re.IGNORECASE):
        findings.append('MAC address')

    # IPv4 pattern: only flag private/common network ranges
    # 10.x.x.x, 172.16-31.x.x, 192.168.x.x, 127.x.x.x, 169.254.x.x
    # This avoids false positives from reference numbers or version strings
    private_ipv4_pattern = rb'(?:10|127|169\.254|172\.(?:[1][6-9]|[2]\d|3[01])|192\.168)\.\d+\.\d+\.\d+'
    if re.search(private_ipv4_pattern, content):
        findings.append('Private IPv4 address')

    # Email pattern
    email_pattern = rb'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if re.search(email_pattern, content):
        findings.append('Email address')

    # Local path pattern (/Users/...)
    if b'/Users/' in content:
        findings.append('Local path (/Users/...)')

    return findings


# Source-disclosure gate: published text (DBC comments/attributes, JSON
# descriptions, README) must carry provenance = firmware version (+ model)
# only. Any hit here means a description or doc leaks where data came from.
SOURCE_DISCLOSURE_PATTERNS = [
    (r'unpacker', 'unpacker'),
    (r'librar(?:y|ies)', 'library'),
    (r'service[\s_-]?mode', 'service mode'),
    (r'service-ui', 'service-ui'),
    (r'opt/diag', 'opt/diag'),
    (r'catalog', 'catalogue'),
    (r'\bodin\b', 'odin'),
    (r'\bDEJ\b', 'DEJ'),
    (r'qt[\s_-]?car', 'QtCar'),
    (r'extracted', 'extracted'),
    (r'reverse[\s_-]?engineer', 'reverse-engineered'),
    (r'decompil', 'decompiled'),
    (r'candb', 'candb'),
    (r'gateway[\s_-]?decomp', 'gateway decomp'),
    (r'tool[\s_-]?fox', 'ToolFox'),
    (r'\btf3', 'tf3'),
    (r'@\s*0x[0-9a-f]+', 'address @0x'),
    (r'\btable\s+\d', "'table N' source string"),
    (r'(?:^|[\s"\'(=])(?:~|\.{1,2})?/(?:[\w.-]+/)+[\w.-]*', 'file path'),
    (r'\b[\w-]+\.(?:so|py|csv|json|md|dbc|cpp|hpp|qml|bin|elf)\b', 'file name'),
    (r'/Users/|/home/|/opt/|/var/|/usr/', 'file path'),
]
_SOURCE_RE = [(re.compile(p, re.IGNORECASE), label) for p, label in SOURCE_DISCLOSURE_PATTERNS]


def scan_source_disclosure(text):
    """Return sorted list of source-disclosure labels found in text (str)."""
    return sorted({label for rx, label in _SOURCE_RE if rx.search(text)})


# Deterministic rewrites for descriptions that name internal software
# components; applied by --fix. Keys are exact phrases (case-sensitive).
DESCRIPTION_REWRITES = [
    ('Service mode plus', 'Extended service diagnostics mode active'),
    ('Service mode', 'Service diagnostics mode active'),
    ('QtCar uptime', 'Touchscreen UI software uptime'),
    ('QtCar', 'the touchscreen UI software'),
]


def rewrite_description(text):
    """Return text with DESCRIPTION_REWRITES applied if it fails the gate."""
    if not scan_source_disclosure(text):
        return text
    for old, new in DESCRIPTION_REWRITES:
        if text == old:
            return new
    for old, new in DESCRIPTION_REWRITES:
        text = text.replace(old, new)
    return text


def fix_data(repo):
    """Rewrite gate-failing descriptions in data/<fw>/signals.{csv,json}."""
    changed = 0
    for fwdir in sorted((repo / 'data').iterdir()):
        csvp, jsonp = fwdir / 'signals.csv', fwdir / 'signals.json'
        if not csvp.exists():
            continue
        with open(csvp, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fields, rows = reader.fieldnames, list(reader)
        for r in rows:
            new = rewrite_description(r['description'])
            if new != r['description']:
                r['description'] = new
                changed += 1
        with open(csvp, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n')
            w.writeheader()
            w.writerows(rows)
        if jsonp.exists():
            with open(jsonp, encoding='utf-8') as f:
                data = json.load(f)
            for sig in data['signals']:
                sig['description'] = rewrite_description(sig.get('description', ''))
            with open(jsonp, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
    return changed


def _free_text_of_data_file(path):
    """Description text of a data/ signals file (names are vehicle identifiers)."""
    if path.suffix == '.csv':
        with open(path, newline='', encoding='utf-8') as f:
            return '\n'.join(r.get('description', '') for r in csv.DictReader(f))
    if path.suffix == '.json':
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        return '\n'.join(s.get('description', '') for s in data.get('signals', []))
    return path.read_text(encoding='utf-8', errors='replace')


def docs_prose(text):
    """Prose of a generated docs page: link targets, code spans (vehicle
    identifiers, names with an underscore) and anchors are dropped; titles, descriptions and text stay."""
    text = re.sub(r'\]\([^)]*\)', ']', text)
    text = re.sub(r'`[^`]*`', '``', text)
    text = re.sub(r'\b\w*_\w*\b', '', text)  # vehicle identifiers with an underscore
    return re.sub(r'<a id="[^"]*"></a>', '', text)


def gate_docs_file(rel, raw):
    """Gate findings for one docs/ file given its docs-relative path and bytes."""
    findings = ['PII: %s' % l for l in scan_pii(raw)]
    if rel.endswith('.md'):
        findings += ['source disclosure: %s' % l
                     for l in scan_source_disclosure(docs_prose(raw.decode('utf-8', errors='replace')))
                     if l != 'file name']
    return findings


def run_gates(repo):
    """PII + source-disclosure gates over the repo's published content.

    Returns a list of 'path: finding' strings (empty = clean)."""
    findings = []
    targets = []
    for sub in ('data', 'dbc', 'docs'):
        base = repo / sub
        if base.exists():
            targets += sorted(p for p in base.rglob('*') if p.is_file())
    targets += [repo / n for n in ('README.md', 'INDEX.md', 'coverage-vs-previous.md') if (repo / n).exists()]
    for p in targets:
        rel = p.relative_to(repo)
        raw = p.read_bytes()
        for label in scan_pii(raw):
            findings.append('%s: PII: %s' % (rel, label))
        if rel.parts[0] == 'docs':
            for label in gate_docs_file(str(Path(*rel.parts[1:])), raw):
                if not label.startswith('PII'):  # PII already reported above
                    findings.append('%s: %s' % (rel, label))
            continue
        if rel.parts[0] == 'data':
            text = _free_text_of_data_file(p)
            labels = scan_source_disclosure(text)
        elif rel.parts[0] == 'dbc':
            # lazy import: export_dbc imports this module
            from export_dbc import dbc_free_text, json_free_text
            text = raw.decode('utf-8', errors='replace')
            if p.suffix == '.dbc':
                text = dbc_free_text(text)
            elif p.suffix == '.json':
                text = json_free_text(text)
            elif p.suffix == '.csv':
                # tables of vehicle identifiers: only the prose columns are gated
                with open(p, newline='', encoding='utf-8') as f:
                    text = '\n'.join(r.get(c, '') for r in csv.DictReader(f)
                                      for c in ('reason', 'description', 'comment', 'note'))
            labels = scan_source_disclosure(text)
        else:
            # docs name files legitimately (e.g. ALL.dbc, signals.csv)
            labels = [l for l in scan_source_disclosure(raw.decode('utf-8', errors='replace'))
                      if l != 'file name']
        for label in labels:
            findings.append('%s: source disclosure: %s' % (rel, label))
    return findings


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    unknown = [a for a in argv if a not in ('--check', '--fix')]
    if unknown:
        print('usage: build.py [--check | --fix]', file=sys.stderr)
        return 2
    repo = Path(__file__).resolve().parent.parent
    if '--fix' in argv:
        print('rewrote %d descriptions' % fix_data(repo), file=sys.stderr)
    findings = run_gates(repo)
    for f in findings:
        print('GATE: ' + f, file=sys.stderr)
    if findings:
        print('GATES FAILED: %d findings' % len(findings), file=sys.stderr)
        return 1
    print('GATES OK: PII + source disclosure clean (data/, dbc/, docs/, README.md, INDEX.md)', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
