# Tesla CAN Signal Database

Tesla Model 3 / Model Y CAN bus signal database and DBC files: decoded CAN
messages and signals (bit layout, byte order, scaling, units, value tables)
for firmware **2026.26.6.5** and **2025.20.8**.

Provenance is stated as firmware version (and vehicle model) only.

## Repository structure

- `dbc/` - Vector DBC files (+ JSON twins) generated from `data/`
  - `dbc/<firmware>/ALL.dbc` - every decoded message of that firmware in one file
- `data/<firmware>/signals.{csv,json}` - signal definitions per firmware
- `tools/build.py` - PII / disclosure gates and shared helpers
- `tools/export_dbc.py` - DBC exporter and validator
- `INDEX.md` - device and signal summary by firmware
- `NOTICE.md` - rights and publication notice

## DBC files

**Status: v1 first cut.** One `ALL.dbc` per firmware. The per-model / per-bus
split (`dbc/<model>/<firmware>/<BUS>.dbc`) and the full attribute set
(cycle times, SNA values, confidence from cross-checks) follow in the next
update.

What is in each file:

- every message with its frame length (8 bytes, or the CAN FD length when a
  layout extends past 8 bytes; such files set `BusType "CAN FD"`)
- every signal with start bit, length, byte order (`@1` Intel / `@0` Motorola,
  standard DBC sawtooth numbering), sign, factor, offset, min/max and unit
  (ASCII units, e.g. `degC`)
- multiplexed messages (`M` switch, `mN` pages)
- `VAL_` value tables for enumerated signals
- a one-line plain-language `CM_` comment for the network, every node,
  message and signal
- attributes: `BusType`, `DBName`, `Baudrate`, `Manufacturer`,
  `FirmwareVersion`, `VehicleModel`, `GenMsgCycleTime`, `GenMsgSendType`,
  `VFrameFormat`, `GenSigSNA`, `Confidence` (per signal) and
  `SystemSignalLongSymbol` for signal names longer than the 32-character DBC
  limit (the DBC identifier is shortened; tools such as cantools restore the
  full name from the attribute)

Frame ids in `ALL.dbc` are the vehicle's internal message ids. Messages that
are re-numbered when they are routed onto a physical CAN bus will carry the
on-bus id in the per-bus files of the next update.

### Load with cantools (Python)

```python
import cantools
db = cantools.database.load_file('dbc/2026.26.6.5/ALL.dbc', strict=True)
msg = db.get_message_by_name('BMS_status')
print(msg.frame_id, [s.name for s in msg.signals])
print(db.decode_message(msg.frame_id, bytes(msg.length)))
```

### Load with python-can + cantools (live bus)

```python
import can, cantools
db = cantools.database.load_file('dbc/2026.26.6.5/ALL.dbc')
with can.Bus(interface='socketcan', channel='can0') as bus:
    for frame in bus:
        try:
            print(db.decode_message(frame.arbitration_id, frame.data))
        except KeyError:
            pass
```

### SavvyCAN

`File > Load DBC File` (or the DBC manager, `Ctrl+D`), pick the `.dbc`, then
use *Frame Info* or the *Signal Viewer* on a capture.

### Vector CANoe / CANalyzer

Add the `.dbc` to the database list of the CAN channel in the simulation or
measurement setup, or open it directly in the Vector database editor. Long signal names are
restored from `SystemSignalLongSymbol`.

### Kayak

Kayak reads Kayak Bus Description (`.kcd`) files. Convert with
`cantools convert dbc/2026.26.6.5/ALL.dbc ALL.kcd`.

## Signal data format (`data/<firmware>/signals.csv`)

- **signal**: canonical signal name
- **device**: ECU abbreviation with full name
- **message**: message name
- **eth_id**: internal message id (hex)
- **mux_signal/mux_value**: multiplexing (if applicable)
- **start/length**: bit position and width (DBC convention)
- **little_endian/signed**: encoding details
- **scale/offset**: raw to physical value conversion
- **unit**: physical unit when known
- **description**: human-readable description when known
- **min/max**: expected value range when known
- **enum_values**: named value map for discrete signals (JSON)

## Regenerate and validate

```bash
python3 tools/export_dbc.py            # regenerate dbc/ from data/
python3 tools/export_dbc.py --check    # regenerate to a temp dir and diff,
                                       # cantools strict load + round trip,
                                       # PII and disclosure gates
```

`python3 tools/build.py` runs the PII and disclosure gates on their own
(no arguments needed; exit 0 = clean).

`--check` needs `cantools` (and optionally `canmatrix`) installed in a
virtual environment.

## Confidence

Each DBC signal carries a `Confidence` attribute:

| Value | Meaning |
|---|---|
| validated | bit layout confirmed by two independent definitions |
| plausible | layout plus unit, value table or description |
| layout-only | bit layout and scaling only |

## Contact

This is a private research repository. Contact the owner for questions about
publication, use, or contributions.
