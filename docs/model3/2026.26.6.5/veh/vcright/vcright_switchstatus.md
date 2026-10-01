---
layout: default
title: "VCRIGHT_switchStatus (0x3C3) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right body controller message: switch status. Tesla Model 3 CAN bus message VCRIGHT_switchStatus (0x3C3) of Right body controller, firmware 2026.26.6.5, 42 signals (VCRIGHT_switchStatusIndex, VCRIGHT_btnWindowUpRF, VCRIGHT_btnWindowAutoUpRF, VCRIGHT_btnWindowDownRF and 38 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_switchStatus (0x3C3) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Right body controller message: switch status; frame length observed on a vehicle bus. This page documents the 42 signals of VCRIGHT_switchStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_switchStatus` |
| CAN id | 0x3C3 (963) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 42 |

## Signals of VCRIGHT_switchStatus

Tesla Model 3 CAN bus signals in `VCRIGHT_switchStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_switchStatusIndex` | selector | Right body controller: switch status index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | validated |
| `VCRIGHT_btnWindowUpRF` |  | Position from firmware; message assignment inferred. | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowAutoUpRF` |  | Position from firmware; message assignment inferred. | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowDownRF` |  | Position from firmware; message assignment inferred. | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowAutoDownRF` |  | Position from firmware; message assignment inferred. | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowUpRR` |  | Position from firmware; message assignment inferred. | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowAutoUpRR` |  | Position from firmware; message assignment inferred. | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowDownRR` |  | Position from firmware; message assignment inferred. | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowAutoDownRR` |  | Position from firmware; message assignment inferred. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackUpLF` |  | Position from firmware; message assignment inferred. | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoUpLF` |  | Position from firmware; message assignment inferred. | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackDownLF` |  | Position from firmware; message assignment inferred. | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoDwnLF` |  | Position from firmware; message assignment inferred. | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackUpLR` |  | Position from firmware; message assignment inferred. | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoUpLR` |  | Position from firmware; message assignment inferred. | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackDownLR` |  | Position from firmware; message assignment inferred. | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoDwnLR` |  | Position from firmware; message assignment inferred. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_frontOccupancySwitch` |  | Front right seat occupancy status. Position from firmware; message assignment inferred. | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_trunkExtReleasePressed` |  | State of exterior trunk release switch. Position from firmware; message assignment inferred. | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackUpRR` |  | Position from firmware; message assignment inferred. | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoUpRR` |  | Position from firmware; message assignment inferred. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackDownRR` |  | Position from firmware; message assignment inferred. | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_btnWindowSwPackAutoDwnRR` |  | Position from firmware; message assignment inferred. | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_frontBuckleSwitch` | page 0 | Right body controller: front buckle switch | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_rearCenterBuckleSwitch` | page 0 | Right body controller: rear center buckle switch | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_rearRightBuckleSwitch` | page 0 | Right body controller: rear right buckle switch | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_trunkExtReleasePressedPersist` | page 1 | Right body controller: trunk ext release pressed persist | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTrackBack` | page 1 | Right body controller: front seat track back; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatTrackForward` | page 1 | Right body controller: front seat track forward; raw 0 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatTiltDown` | page 1 | Right body controller: front seat tilt down; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatTiltUp` | page 1 | Right body controller: front seat tilt up; raw 0 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatLiftDown` | page 1 | Right body controller: front seat lift down; raw 0 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatLiftUp` | page 1 | Right body controller: front seat lift up; raw 0 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatBackrestBack` | page 1 | Right body controller: front seat backrest back; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatBackrestForward` | page 1 | Right body controller: front seat backrest forward; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatLumbarDown` | page 1 | Right body controller: front seat lumbar down; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatLumbarUp` | page 1 | Right body controller: front seat lumbar up; raw 0 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatLumbarIn` | page 1 | Right body controller: front seat lumbar in; raw 0 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_frontSeatResistiveOccupancy` | page 1 | Front right seat occupancy status; raw 0 = signal not available (SNA) | 54\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_2RowSeatReclineSwitchpackState` | page 1 | State of the right second row powered recline adjustment switchpack | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DISCONNECTED`<br>1 = `INACTIVE`<br>2 = `FORWARD_SLOW`<br>3 = `FORWARD_FAST`<br>4 = `REARWARD_SLOW`<br>5 = `REARWARD_FAST`<br>6 = `FAULT` | validated |
| `VCRIGHT_hvacHeatingAllowedRight` | page 1 | Right body controller: hvac heating allowed right | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatThighSupportRetractSwitch` | page 1 | Status of the switch used to retract front seat thigh support; raw 0 = signal not available (SNA) | 60\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |

## Multiplexing

`VCRIGHT_switchStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals), page 1 (16 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
