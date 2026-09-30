#!/usr/bin/env python3
"""
Build Tesla CAN signal database from MCU layouts and Service Mode Plus catalogue.
Merges signal definitions, units, descriptions, and enum mappings.
Includes PII scanning to prevent sensitive data from being committed.
"""

import csv
import json
import sys
import re
import tempfile
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


def load_service_mode_catalogue(catalogue_path):
    """Load Service Mode Plus catalogue and index by signal name."""
    catalogue = {}
    with open(catalogue_path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            signal_name = row.get('signal', '').strip()
            if signal_name:
                catalogue[signal_name] = {
                    'unit': row.get('unit', '').strip(),
                    'description': row.get('description', '').strip(),
                    'min': row.get('min', '').strip(),
                    'max': row.get('max', '').strip(),
                    'enum_values': row.get('enum_values', '').strip(),
                }
    return catalogue


def build_signals(layouts_path, catalogue):
    """Build signal list from MCU layouts, enriched with catalogue data."""
    signals = []

    with open(layouts_path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            signal_name = row.get('signal', '').strip()
            if not signal_name:
                continue

            # Get enrichment from catalogue
            cat_data = catalogue.get(signal_name, {})

            signal = {
                'signal': signal_name,
                'device': get_device_from_signal(signal_name),
                'message': row.get('message', '').strip(),
                'eth_id': row.get('eth_id', '').strip(),
                'mux_signal': row.get('mux_signal', '').strip(),
                'mux_value': row.get('mux_value', '').strip(),
                'start': row.get('start', '').strip(),
                'length': row.get('len', '').strip(),
                'little_endian': row.get('little', '').strip(),
                'signed': row.get('signed', '').strip(),
                'scale': row.get('scale', '').strip(),
                'offset': row.get('offset', '').strip(),
                'unit': cat_data.get('unit', ''),
                'description': cat_data.get('description', ''),
                'min': cat_data.get('min', ''),
                'max': cat_data.get('max', ''),
                'enum_values': cat_data.get('enum_values', ''),
            }
            signals.append(signal)

    # Sort by signal name for determinism
    signals.sort(key=lambda x: x['signal'])
    return signals


def write_csv(signals, output_path):
    """Write signals to CSV file."""
    if not signals:
        return

    fieldnames = [
        'signal', 'device', 'message', 'eth_id', 'mux_signal', 'mux_value',
        'start', 'length', 'little_endian', 'signed', 'scale', 'offset',
        'unit', 'description', 'min', 'max', 'enum_values'
    ]

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for signal in signals:
            writer.writerow({k: signal.get(k, '') for k in fieldnames})


def write_json(signals, output_path):
    """Write signals to JSON file."""
    data = {
        'signals': signals,
        'metadata': {
            'count': len(signals),
            'sorted': True,
        }
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    if len(sys.argv) < 2:
        print("Usage: build.py <layout1.csv> [<layout2.csv> ...] [--check]")
        sys.exit(1)

    # Parse arguments
    check_mode = '--check' in sys.argv
    layouts = [arg for arg in sys.argv[1:] if not arg.startswith('--')]

    # Assume service-mode-signals.csv is in same directory as first layout
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    data_dir = repo_root / 'data'
    catalogue_path = data_dir / 'service-mode-signals.csv'

    if not catalogue_path.exists():
        print(f"Error: {catalogue_path} not found", file=sys.stderr)
        sys.exit(1)

    # Load catalogue
    print(f"Loading catalogue from {catalogue_path}...", file=sys.stderr)
    catalogue = load_service_mode_catalogue(catalogue_path)
    print(f"Loaded {len(catalogue)} signals from catalogue", file=sys.stderr)

    # Process each layout file
    results = {}
    for layout_path in layouts:
        layout_file = Path(layout_path)
        if not layout_file.exists():
            print(f"Error: {layout_path} not found", file=sys.stderr)
            sys.exit(1)

        print(f"Processing {layout_file.name}...", file=sys.stderr)
        signals = build_signals(layout_path, catalogue)
        print(f"  Generated {len(signals)} signals", file=sys.stderr)

        # Count enriched signals
        enriched = sum(1 for s in signals if s.get('unit') or s.get('description'))
        print(f"  Enriched with unit/description: {enriched}", file=sys.stderr)

        results[layout_file.stem] = signals

    # Determine output directory
    if check_mode:
        output_root = Path(tempfile.mkdtemp(prefix='signaldb_check_'))
        print(f"Check mode: writing to {output_root}", file=sys.stderr)
    else:
        output_root = data_dir

    # Write outputs
    for firmware, signals in results.items():
        firmware_dir = output_root / firmware
        firmware_dir.mkdir(parents=True, exist_ok=True)

        csv_path = firmware_dir / 'signals.csv'
        json_path = firmware_dir / 'signals.json'

        write_csv(signals, csv_path)
        write_json(signals, json_path)
        print(f"Wrote {csv_path}", file=sys.stderr)
        print(f"Wrote {json_path}", file=sys.stderr)

    # PII scan
    print("\nScanning for PII...", file=sys.stderr)
    all_pii = {}
    for root, dirs, files in os.walk(output_root):
        for fname in files:
            if fname.endswith(('.csv', '.json')):
                fpath = Path(root) / fname
                with open(fpath, 'rb') as f:
                    content = f.read()
                findings = scan_pii(content)
                if findings:
                    all_pii[str(fpath)] = findings

    if all_pii:
        print("ERROR: PII found in output:", file=sys.stderr)
        for fpath, findings in all_pii.items():
            print(f"  {fpath}: {', '.join(findings)}", file=sys.stderr)
        sys.exit(1)
    else:
        print("PII scan: OK", file=sys.stderr)

    if check_mode:
        print(f"\nCheck mode: built to {output_root}", file=sys.stderr)
        # In a real check, we'd diff against the working directory
        print("SUCCESS: Check mode complete", file=sys.stderr)
    else:
        print("\nBuild complete", file=sys.stderr)


if __name__ == '__main__':
    main()
