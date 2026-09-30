# Tesla CAN Signal Database

A comprehensive database of Tesla vehicle CAN signal layouts, units, descriptions, and enumerations extracted from firmware unpacker outputs and vehicle diagnostics catalogues.

## Overview

This repository contains signal definitions for Tesla Model 3/Y CAN buses across multiple firmware versions:
- **2026.26.6.5**: Latest firmware release vehicle-interface library unpacker
- **2025.20.8**: Previous firmware release vehicle-interface library unpacker

Data is organized by firmware version, with each including signal name, message ID, position, scaling information, and human-readable descriptions where available.

## Repository Structure

- `README.md` - This file
- `INDEX.md` - Device and signal summary by firmware
- `NOTICE.md` - Rights and publication notice
- `data/` - Signal definitions by firmware version
  - `2026.26.6.5/signals.{csv,json}` - 2026.26.6.5 firmware signals
  - `2025.20.8/signals.{csv,json}` - 2025.20.8 firmware signals
  - `service-mode-signals.csv` - Service Mode Plus signal catalogue (source data)
  - `mcu-layouts-*.csv` - Raw firmware unpacker outputs (source data)
- `tools/` - Build and maintenance scripts
  - `build.py` - Regenerate signal databases from source files

## Signal Data Format

Each signal record includes:
- **signal**: Canonical signal name
- **device**: Device/ECU abbreviation with full name
- **message**: CAN message ID
- **eth_id**: Ethernet/CAN message identifier (hex)
- **mux_signal/mux_value**: Multiplexing information (if applicable)
- **start/length**: Bit position and width in message
- **little_endian/signed**: Encoding details
- **scale/offset**: Raw to physical value conversion
- **unit**: Physical unit (V, A, °C, rpm, etc.) when known
- **description**: Human-readable signal description
- **min/max**: Expected value ranges
- **enum_values**: Named enumeration map for discrete signals

## Data Quality

- **Status**: v0 - Raw extraction, not yet validated against live CAN logs
- **Enrichment**: ~10% of signals include units and descriptions from diagnostic catalogues; remainder have layout/scaling only
- **Coverage**: All signals extracted from firmware; cross-check with vehicle data in progress

See [CONFIDENCE_LEGEND](#confidence-legend) for how to interpret each field's reliability.

## Usage

### Load from CSV
```python
import csv
with open('data/2026.26.6.5/signals.csv') as f:
    signals = csv.DictReader(f)
    for sig in signals:
        print(f"{sig['signal']}: {sig['description']} [{sig['unit']}]")
```

### Load from JSON
```python
import json
with open('data/2026.26.6.5/signals.json') as f:
    data = json.load(f)
    for sig in data['signals']:
        print(f"{sig['signal']}: {sig['description']}")
```

## Building from Source

The database is regenerated from two source files:
1. **MCU layouts** (from vehicle-interface library unpacker): raw signal positions and scaling
2. **Service Mode Plus catalogue**: enriched descriptions, units, and enumerations

Rebuild the database:
```bash
python3 tools/build.py data/mcu-layouts-2026.26.6.5.csv data/mcu-layouts-2025.20.8.csv
```

Validate output without writing:
```bash
python3 tools/build.py data/mcu-layouts-2026.26.6.5.csv data/mcu-layouts-2025.20.8.csv --check
```

The build process:
- Reads all signals from MCU layout files
- Joins with Service Mode Plus catalogue by exact signal name
- Extracts device names from signal prefixes
- Outputs to both CSV and JSON formats
- Validates against PII patterns (no VINs, MACs, local paths, emails)

## Confidence Legend

| Level | Meaning | Field Examples |
|-------|---------|-----------------|
| High | Extracted from firmware; validated against multiple sources | message, eth_id, start, length, scale, offset |
| Medium | From diagnostic catalogue with some gaps | description, enum_values |
| Low | Derived or inferred; may have errors | device (prefix-based), min/max (ranges) |
| Unverified | Empty in v0; awaiting live validation | actual signal ranges in running vehicles |

## Roadmap

- [ ] Validate signals against live CAN logs from Model 3/Y vehicles
- [ ] Export as DBC (Vector CAN database format)
- [ ] Add per-device and per-bus summary files
- [ ] Extend coverage to other vehicle models

## Contact

This is a private research repository. Contact the owner for questions about publication, use, or contributions.

---

**Version**: v0 (raw extraction)  
**Last Updated**: 2026-09-30
