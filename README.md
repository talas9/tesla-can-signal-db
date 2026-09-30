# Tesla CAN Signal Database

Tesla Model 3 / Model Y CAN bus signal database and DBC files: decoded CAN
messages and signals (bit layout, byte order, scaling, units, value tables)
for firmware **2026.26.6.5** and **2025.20.8**.

Provenance is stated as firmware version (and vehicle model) only.

**Current state.** The CAN DBC files are `dbc/<model>/<firmware>/<BUS>.dbc`,
one per CAN bus (`VEH`, `CH`, `PARTY`), with the real on-bus CAN ids, built
from each model's own gateway id map. In 2026.26.6.5, 579 of 673 messages have
a known CAN id on Model 3 and 598 on Model Y (601 across both). The rest are
kept only in the Ethernet-side files and are listed below as not yet mapped.

## Repository structure

- `dbc/` - Vector DBC files (+ JSON twins) generated from `data/`
  - `dbc/<model>/<firmware>/<BUS>.dbc` - one DBC per vehicle model, firmware and CAN bus
  - `dbc/<firmware>/ETH.dbc` - every message under its Ethernet-side id (not CAN ids; see below)
- `data/<firmware>/signals.{csv,json}` - signal definitions per firmware
- `data/<firmware>/messages.csv` - frame length and cycle time per message
- `data/<firmware>/id-map.csv` - Ethernet-side id to (bus, CAN id) map per model
- `data/can-frame-lengths.csv` - frame lengths observed on recorded vehicle buses
- `data/can-flagged.csv` - on-bus ids whose frames do not follow the layout
- `data/can-only-signals.csv` - messages that exist only on a CAN bus (no Ethernet-side id)
- `dbc/renames.csv` - earlier signal/message names mapped to the names used here, with the
  on-bus CAN id and the Ethernet-side id
- `coverage-vs-previous.md` - comparison against earlier DBCs
- `data/<firmware>/signal-meta.csv` - units, value tables, SNA codes, per-model assignment
- `tools/build.py` - PII / disclosure gates and shared helpers
- `tools/export_dbc.py` - DBC exporter and validator (Python API + CLI)
- `INDEX.md` - device and signal summary by firmware
- `NOTICE.md` - rights and publication notice

## DBC files

Tesla Model 3 / Model Y CAN bus DBC files with decoded signals for firmware
2026.26.6.5 and 2025.20.8, one file per bus.

### Tree

```
dbc/
  Model3/<firmware>/{VEH,CH,PARTY}.dbc         Model 3: every message its gateway routes
  ModelY/<firmware>/{VEH,CH,PARTY}.dbc         Model Y: every message its gateway routes
  AllModels/<firmware>/{VEH,CH,PARTY}.dbc      union of Model 3 and Model Y
  <model>/<firmware>/ETH.dbc                   messages with no known CAN route
  Bayberry/<firmware>/<BUS>.dbc                product codename, model not confirmed
  GoldenSnitch/<firmware>/<BUS>.dbc            product codename, model not confirmed
  <firmware>/ETH.dbc                           every message, Ethernet-side ids (see below)
```

Every `.dbc` has a `.json` twin with the same content in machine-readable form
(messages, signals, value tables, confidence, dropped signals).

**Buses.** `VEH` = vehicle CAN bus, `CH` = chassis CAN bus, `PARTY` = the
gateway's third CAN bus ("bus1"). The party bus assignment is inferred, not
capture-proven; the JSON twins keep the label `bus1 (inferred PARTY)`. A
message that the gateway forwards onto several buses appears in each of those
bus files under its on-bus CAN id. A frame read from a bus uses the layout of
its Ethernet-side message; a frame the gateway sends onto a bus has `GTW` as
its transmitter, and its comment says so.

**Firmware coverage of the id map.** The CAN id maps are for firmware
2026.26.6.5 (Model 3 and Model Y). There is no 2025.20.8 map yet, so for
2025.20.8 the 2026.26.6.5 map is reused only where the message name and its
full bit layout are identical. The remaining 2025.20.8 messages stay
Ethernet-side only until a map for that firmware exists.

**Ethernet-side ids.** Inside the car, messages also travel on an internal
Ethernet link under their own message ids, which often differ from the CAN
ids. Two kinds of file use those ids and must not be used on a CAN bus:
`<model>/<firmware>/ETH.dbc` holds the messages with no known CAN route, and
`dbc/<firmware>/ETH.dbc` (the former `ALL.dbc`) holds every message.

**Models.** `Model3` and `ModelY` are built from each model's own gateway id
map and hold every message that model's gateway routes, with all its signals.
Load the file for your car and bus, for example
`Model3/2026.26.6.5/VEH.dbc`. `AllModels` is the union of both; no CAN id
maps to a different message between the two models. `Bayberry` and
`GoldenSnitch` are product codenames whose model is not confirmed. Their
folders hold only the signals with per-product evidence, keyed with the
union map.

**Frame lengths.** On a CAN bus a frame can be shorter than the
Ethernet-side layout. When a frame length has been observed on a recorded
vehicle bus, the bus file uses it (`AllModels`: the longest observed).
Signals past that length are left out of the bus file and marked "not
carried on CAN" in `dbc/<firmware>/ETH.dbc`. Messages without an observed
length keep the layout length, and their comment says so. Observations exist
for the VEH bus so far.

**Flagged.** VEH 0x213 (`UI_cruiseControl`) is a 2-byte frame from a
different sender whose counter never steps, so the Ethernet-side layout is not
asserted there; it is left out of the VEH files.

### What is in each file

- every message with its frame length (from the firmware message table; the
  CAN FD length when a layout extends past 8 bytes, with `BusType "CAN FD"`)
- every signal with start bit, length, byte order (`@1` Intel / `@0` Motorola,
  standard DBC sawtooth numbering: Motorola start = most significant bit),
  sign, factor, offset, min/max (SNA code excluded) and ASCII unit (`degC`)
- multiplexed messages (`M` switch, `mN` pages)
- `VAL_` value tables for enumerated signals, with the SNA code labelled `SNA`
- a one-line plain-language `CM_` comment for the network, every node,
  message and signal
- `BO_TX_BU_` transmitter per message
- attributes: `BusType`, `DBName`, `Baudrate`, `Manufacturer`,
  `FirmwareVersion`, `VehicleModel`, `ECU`, `GenMsgCycleTime`,
  `GenMsgSendType`, `VFrameFormat`, `GenSigSNA`, `Confidence` and
  `SystemSignalLongSymbol` for signal names longer than the 32-character DBC
  limit (the DBC identifier is shortened; cantools and CANoe restore the full
  name from the attribute)

### Coverage

Generated by `tools/export_dbc.py`; `--check` fails if it is stale.

<!-- coverage:begin (generated by tools/export_dbc.py) -->
| Model | Firmware | Bus | Messages | Signals | Enums | Validated | Plausible | Layout-only | Contradicted |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Model 3 / Model Y | 2026.26.6.5 | [CH](dbc/AllModels/2026.26.6.5/CH.dbc) | 156 | 10385 | 1259 | 959 | 1165 | 8261 | 0 |
| Model 3 / Model Y | 2026.26.6.5 | [PARTY](dbc/AllModels/2026.26.6.5/PARTY.dbc) | 53 | 1420 | 330 | 561 | 155 | 704 | 0 |
| Model 3 / Model Y | 2026.26.6.5 | [VEH](dbc/AllModels/2026.26.6.5/VEH.dbc) | 414 | 26259 | 4908 | 5671 | 5908 | 14680 | 0 |
| Model 3 / Model Y | 2026.26.6.5 | [ETH](dbc/AllModels/2026.26.6.5/ETH.dbc) | 72 | 4670 | 1366 | 614 | 1438 | 2618 | 0 |
| Model 3 / Model Y | 2026.26.6.5 | [ETH-side ids, all messages](dbc/2026.26.6.5/ETH.dbc) | 673 | 42316 | 7704 | 7566 | 8603 | 26147 | 0 |
| Model 3 / Model Y | 2025.20.8 | [CH](dbc/AllModels/2025.20.8/CH.dbc) | 90 | 2407 | 474 | 579 | 232 | 1596 | 0 |
| Model 3 / Model Y | 2025.20.8 | [PARTY](dbc/AllModels/2025.20.8/PARTY.dbc) | 23 | 525 | 130 | 252 | 4 | 269 | 0 |
| Model 3 / Model Y | 2025.20.8 | [VEH](dbc/AllModels/2025.20.8/VEH.dbc) | 151 | 2676 | 806 | 1956 | 195 | 525 | 0 |
| Model 3 / Model Y | 2025.20.8 | [ETH](dbc/AllModels/2025.20.8/ETH.dbc) | 357 | 27970 | 4874 | 3225 | 6564 | 18181 | 0 |
| Model 3 / Model Y | 2025.20.8 | [ETH-side ids, all messages](dbc/2025.20.8/ETH.dbc) | 609 | 33441 | 6240 | 5934 | 6971 | 20536 | 0 |
| Bayberry | 2026.26.6.5 | [CH](dbc/Bayberry/2026.26.6.5/CH.dbc) | 4 | 27 | 19 | 27 | 0 | 0 | 0 |
| Bayberry | 2026.26.6.5 | [PARTY](dbc/Bayberry/2026.26.6.5/PARTY.dbc) | 3 | 61 | 24 | 60 | 1 | 0 | 0 |
| Bayberry | 2026.26.6.5 | [VEH](dbc/Bayberry/2026.26.6.5/VEH.dbc) | 21 | 330 | 137 | 320 | 10 | 0 | 0 |
| Bayberry | 2025.20.8 | [CH](dbc/Bayberry/2025.20.8/CH.dbc) | 3 | 26 | 18 | 26 | 0 | 0 | 0 |
| Bayberry | 2025.20.8 | [VEH](dbc/Bayberry/2025.20.8/VEH.dbc) | 9 | 128 | 61 | 124 | 4 | 0 | 0 |
| Bayberry | 2025.20.8 | [ETH](dbc/Bayberry/2025.20.8/ETH.dbc) | 12 | 180 | 72 | 150 | 22 | 8 | 0 |
| GoldenSnitch | 2026.26.6.5 | [CH](dbc/GoldenSnitch/2026.26.6.5/CH.dbc) | 2 | 8 | 7 | 8 | 0 | 0 | 0 |
| GoldenSnitch | 2026.26.6.5 | [VEH](dbc/GoldenSnitch/2026.26.6.5/VEH.dbc) | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| GoldenSnitch | 2025.20.8 | [ETH](dbc/GoldenSnitch/2025.20.8/ETH.dbc) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| Model 3 | 2026.26.6.5 | [CH](dbc/Model3/2026.26.6.5/CH.dbc) | 146 | 9151 | 1130 | 951 | 1027 | 7173 | 0 |
| Model 3 | 2026.26.6.5 | [PARTY](dbc/Model3/2026.26.6.5/PARTY.dbc) | 50 | 862 | 313 | 548 | 138 | 176 | 0 |
| Model 3 | 2026.26.6.5 | [VEH](dbc/Model3/2026.26.6.5/VEH.dbc) | 405 | 24892 | 4732 | 5613 | 5619 | 13660 | 0 |
| Model 3 | 2026.26.6.5 | [ETH](dbc/Model3/2026.26.6.5/ETH.dbc) | 94 | 7829 | 1688 | 693 | 1882 | 5254 | 0 |
| Model 3 | 2025.20.8 | [CH](dbc/Model3/2025.20.8/CH.dbc) | 87 | 2126 | 471 | 571 | 229 | 1326 | 0 |
| Model 3 | 2025.20.8 | [PARTY](dbc/Model3/2025.20.8/PARTY.dbc) | 22 | 255 | 129 | 252 | 3 | 0 | 0 |
| Model 3 | 2025.20.8 | [VEH](dbc/Model3/2025.20.8/VEH.dbc) | 151 | 2676 | 806 | 1956 | 195 | 525 | 0 |
| Model 3 | 2025.20.8 | [ETH](dbc/Model3/2025.20.8/ETH.dbc) | 361 | 28521 | 4878 | 3233 | 6568 | 18720 | 0 |
| Model Y | 2026.26.6.5 | [CH](dbc/ModelY/2026.26.6.5/CH.dbc) | 153 | 9293 | 1208 | 946 | 1081 | 7266 | 0 |
| Model Y | 2026.26.6.5 | [PARTY](dbc/ModelY/2026.26.6.5/PARTY.dbc) | 53 | 1420 | 330 | 561 | 155 | 704 | 0 |
| Model Y | 2026.26.6.5 | [VEH](dbc/ModelY/2026.26.6.5/VEH.dbc) | 412 | 26235 | 4904 | 5665 | 5905 | 14665 | 0 |
| Model Y | 2026.26.6.5 | [ETH](dbc/ModelY/2026.26.6.5/ETH.dbc) | 75 | 5762 | 1417 | 627 | 1522 | 3613 | 0 |
| Model Y | 2025.20.8 | [CH](dbc/ModelY/2025.20.8/CH.dbc) | 90 | 2407 | 474 | 579 | 232 | 1596 | 0 |
| Model Y | 2025.20.8 | [PARTY](dbc/ModelY/2025.20.8/PARTY.dbc) | 23 | 525 | 130 | 252 | 4 | 269 | 0 |
| Model Y | 2025.20.8 | [VEH](dbc/ModelY/2025.20.8/VEH.dbc) | 149 | 2670 | 806 | 1956 | 195 | 519 | 0 |
| Model Y | 2025.20.8 | [ETH](dbc/ModelY/2025.20.8/ETH.dbc) | 357 | 27970 | 4874 | 3225 | 6564 | 18181 | 0 |
<!-- coverage:end -->

### Check against recorded vehicle logs

**Headline metric: frames decoded as the right message.** A frame counts
when its id is in the DBC, the DBC names the same message the CAN id map
assigns to that id, and the payload decodes without error. A frame shorter
than the DBC frame length counts as not decoded (strict decoding, no
truncation allowed).

Log A is a recorded Model 3 vehicle-bus (VEH) capture: 546,286 frames, 243
ids.

| DBC | Frames decoded as the right message | Ids decoded as the right message |
|---|---:|---:|
| Before: `dbc/2026.26.6.5/ETH.dbc` (Ethernet-side ids) | 48.4% | 108 / 243 |
| After: `Model3/2026.26.6.5/VEH.dbc` | **74.9%** | **170 / 243** |

How the after figure grew, step by step (same metric, Log A):

| Step | Frames decoded as the right message | Ids |
|---|---:|---:|
| Per-bus CAN files from the gateway id map | 70.8% | 157 |
| + firmware-defined messages missing from the tables, vehicle-bus-only time and VIN messages, pack serial layout | 72.2% | 162 |
| + vehicle-bus ids confirmed by the firmware bus database (0x102, 0x103, 0x31A, 0x420, 0x666, 0x7FF) and two battery-computer frames with firmware positions (0x311, 0x452) | 74.9% | 170 |

The "before" row is measured against the current CAN id map, so its figure
changes slightly as the map grows.

Secondary numbers on Log A, counting any successful decode whether or not it
is the right message: before 55.1% of frames (127 ids) with strict decoding
and 71.3% (175 ids) when truncated frames are allowed; after 74.9% (170 ids)
either way. The before file's extra lenient matches are mostly short frames
and ids read as the wrong message. Of its 179 id matches on Log A, 139 are
the right message, 12 are a different message, and 28 have no CAN mapping.

Log B is a recorded Model Y vehicle-bus capture from older firmware: 35,350
frames, 161 ids. `ModelY/2026.26.6.5/VEH.dbc` decodes 77.4% of its frames
(106 ids), against 61.3% (85 ids) for the before file with strict decoding.
`Model3/2025.20.8/VEH.dbc`, built on the reduced 2025.20.8 id map, decodes
13.9% of Log A and 17.5% of Log B.

Anchor checks on Log A with `Model3/2026.26.6.5/VEH.dbc`:

| Anchor | Result |
|---|---|
| 0x352 nominal full pack energy | pass: 62.2 kWh on every sample (expected about 62 kWh) |
| 0x5F3 odometer | pass: sane km value, monotonic over the capture |
| 0x72A pack serial (from Ethernet-side 0x7FA) | pass: pages 0 and 1 decode as printable ASCII on every frame |
| 0x318, 0x528, 0x405 (vehicle-bus only) | pass: UTC fields, clock and VIN pages in range on every frame of both logs |
| 0x111 / 0x112 not on VEH as body-controller messages | pass (asserted by `--check`) |
| CH 0x111 = inertial message (Ethernet-side 0x116) | pass (asserted by `--check`) |

### What Log A still does not decode

72 Log A ids have no sender-firmware layout available. Every one of them is
in one of these classes, so no id is unexplained:

| Class | Meaning | Ids | Frames |
|---|---|---:|---:|
| Gateway-local | Not keyed or not forwarded by the gateway on this bus; no firmware layout for the id is known | 56 | 102,017 |
| Mapped, no layout | Forwarded to the Ethernet side, but no layout for that message exists in our data | 6 | 15,355 |
| Id reuse, longer layout | A same-id layout exists, but it is longer than the frame on this bus | 6 | 12,459 |
| Id reuse, shorter layout | A same-id layout exists, but another bus owns that message | 4 | 6,389 |
| Flagged (decoded id excluded) | 0x213, whose frames do not follow the layout (see above) | 1 | 573 |
| Missing mux pages (id is decoded) | 0x75D `CP_loggingFast` pages 7 and 8; the firmware defines only pages 0 to 6 | 0 | 320 |

- Gateway-local: 0x113 0x1F8 0x1FA 0x20E 0x22B 0x289 0x2A1 0x2AA 0x2BD
  0x2BF 0x2EC 0x323 0x33D 0x348 0x35F 0x361 0x362 0x364 0x382 0x39B 0x3A3
  0x3AE 0x3CC 0x3ED 0x3FA 0x400 0x409 0x40A 0x414 0x419 0x41D 0x421 0x422
  0x42E 0x458 0x45B 0x49D 0x509 0x52F 0x552 0x55A 0x6C8 0x6E8 0x708 0x724
  0x726 0x727 0x752 0x77D 0x782 0x788 0x789 0x78A 0x798 0x7A8 0x7B8.
  0x782 has firmware positions for a multi-page battery-computer frame, but
  the pages are not resolved, so it is not added.
- Candidates, unconfirmed: 0x20E, 0x289, 0x348, 0x3ED, 0x3FA, 0x458 and
  0x55A match a message already in this database on id, frame length and
  period, but their identity is not proven. They are not added as VEH routes.
- Mapped, no layout: 0x234 0x242 0x24A 0x407 0x553 0x797.
- Id reuse, longer layout: 0x286 0x428 0x448 0x748 0x7DD 0x7F4.
- Id reuse, shorter layout: 0x25B 0x27D 0x38B 0x3D3.
- Flagged: 0x31A (`VCRIGHT_restraintStatus`) is sent every 200 ms on Log A,
  while the firmware bus database gives 50 ms. Its layout and checksum match,
  so it is kept, but the period does not.

Messages that exist only on the vehicle bus, with no Ethernet-side id, come
from our own decoders and were confirmed on both logs: 0x318 UTC date and
time, 0x528 vehicle clock, and 0x405 VIN text pages. They are
`SystemTimeUTC`, `UnixTimeSeconds` and `VINbroadcast` in the VEH files.
`HVBMS_0x311` and `HVBMS_0x452` are battery-computer frames with firmware
bit positions and neutral positional names (`layout-only`).

### Not yet mapped

- Ethernet-side ids with no mapping: 0x111, 0x112, 0x113 (right body
  controller wake logging, on that controller's private bus).
- Id map entries whose Ethernet-side message has no layout in our data
  (2026.26.6.5; `--check` lists each one):
  - VEH: 0x143 0x234 0x242 0x24A 0x344 0x39A 0x3C6 0x3C7 0x407 0x461 0x553
    0x562 0x578 0x5A2 0x5A3 0x632 0x647 0x650 0x6E0 0x6E2 0x797
  - CH: 0x147 0x37B 0x38C 0x38D 0x3AC 0x3B0 0x575 0x61A 0x61C
  - PARTY: 0x031 0x051 0x105 0x2FB 0x73C 0x7B6
- Messages with no known CAN id stay in the Ethernet-side files
  (`<model>/<firmware>/ETH.dbc`). `--check` lists each of them with its
  signal count.

### Load with cantools (Python)

```python
import cantools
db = cantools.database.load_file('dbc/Model3/2026.26.6.5/VEH.dbc', strict=True)
msg = db.get_message_by_name('BMS_status')
print(msg.frame_id, [s.name for s in msg.signals])
print(db.decode_message(msg.frame_id, bytes(msg.length)))
```

### Load with python-can + cantools (live bus)

```python
import can, cantools
db = cantools.database.load_file('dbc/Model3/2026.26.6.5/VEH.dbc')
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
`cantools convert dbc/AllModels/2026.26.6.5/VEH.dbc VEH.kcd`.

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

Python API (for pipelines that add a new firmware):

```python
import sys; sys.path.insert(0, 'tools')
import export_dbc
kw = export_dbc.load_inputs('data/2026.26.6.5')    # or build the dicts yourself
report = export_dbc.export(out_dir='dbc', **kw)     # writes the whole tree for that firmware
errors = export_dbc.check('dbc')                    # [] when every file passes
print(export_dbc.coverage_markdown(report['files']))
```

`export(signal_rows, firmware, out_dir, routing=None, msg_meta=None,
signal_meta=None, verdicts=None)` takes no fixed paths. It is deterministic,
and it raises `ExportError` on any column or value it cannot handle. An
optional `data/<fw>/log-verdicts.csv` (`fw,signal,message,...,verdict,...`)
sets `Confidence` to validated, plausible or contradicted for the signals it
lists. Only the verdict is used; no other text from that file goes into the
DBC. The module docstring has the full contract.

`--check` needs `cantools` (and optionally `canmatrix`) installed in a
virtual environment.

## Confidence

Each DBC signal carries a `Confidence` attribute:

| Value | Meaning |
|---|---|
| validated | bit layout confirmed by two independent definitions, or confirmed on recorded vehicle logs |
| plausible | layout plus unit, value table or description |
| layout-only | bit layout and scaling only |
| contradicted | recorded vehicle logs disagree with the definition - treat with care |

## Contact

This is a private research repository. Contact the owner for questions about
publication, use, or contributions.
