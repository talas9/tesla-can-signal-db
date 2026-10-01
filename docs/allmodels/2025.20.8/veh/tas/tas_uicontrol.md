---
layout: default
title: "TAS_uiControl (0x21A) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: ui control. Tesla Model 3 / Model Y CAN bus message TAS_uiControl (0x21A) of Air suspension controller, firmware 2025.20.8, 23 signals (TAS_yellowWarningLamp, TAS_redWarningLamp, TAS_veryLowAllowed, TAS_lowAllowed and 19 more). Bit layout, scaling, units and value tables."
---

# TAS_uiControl (0x21A) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Air suspension controller message: ui control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 23 signals of TAS_uiControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_uiControl` |
| CAN id | 0x21A (538) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 23 |

## Signals of TAS_uiControl

Tesla Model 3 / Model Y CAN bus signals in `TAS_uiControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_yellowWarningLamp` | Air suspension controller: yellow warning lamp | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_redWarningLamp` | Air suspension controller: red warning lamp | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_veryLowAllowed` | Air suspension controller: very low allowed | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_lowAllowed` | Air suspension controller: low allowed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_standardAllowed` | Air suspension controller: standard allowed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_highAllowed` | Air suspension controller: high allowed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_veryHighAllowed` | Air suspension controller: very high allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_extractAllowed` | Air suspension controller: extract allowed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_showSpinner` | Air suspension controller: show spinner | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_adaptiveRideModeOverride` | Air suspension controller: adaptive ride mode override; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `TAS_ADAPTIVE_RIDE_MODE_COMFORT`<br>1 = `TAS_ADAPTIVE_RIDE_MODE_AUTO`<br>2 = `TAS_ADAPTIVE_RIDE_MODE_SPORT`<br>3 = `TAS_ADAPTIVE_RIDE_MODE_SNA` | plausible |
| `TAS_levelSelectEnabled` | Air suspension controller: level select enabled | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_jackModeToggleEnabled` | Air suspension controller: jack mode toggle enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_adaptiveRideSelectEnabled` | Air suspension controller: adaptive ride select enabled | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_launchModeState` | Air suspension controller: launch mode state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_LAUNCH_MODE_STATE_BLOCKED`<br>1 = `TAS_LAUNCH_MODE_STATE_IDLE`<br>2 = `TAS_LAUNCH_MODE_STATE_LOWER_SUSPENSION`<br>3 = `TAS_LAUNCH_MODE_STATE_READY`<br>4 = `TAS_LAUNCH_MODE_STATE_RAISE_SUSPENSION` | plausible |
| `TAS_restrictUpLevelingFalcons` | Air suspension controller: restrict up leveling falcons | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictUpLevelingTrunk` | Air suspension controller: restrict up leveling trunk | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictDownLevelingDoors` | Air suspension controller: restrict down leveling doors | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictLevelingChargeCable` | Air suspension controller: restrict leveling charge cable | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictLevelingSystemCheck` | Air suspension controller: restrict leveling system check | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictLevelingTransport` | Air suspension controller: restrict leveling transport | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_restrictLevelingShowroom` | Indication that up and down leveling are restricted while showroom mode is active. | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `TAS_uiControlCounter` | Air suspension controller: ui control counter | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `TAS_uiControlChecksum` | Air suspension controller: ui control checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
