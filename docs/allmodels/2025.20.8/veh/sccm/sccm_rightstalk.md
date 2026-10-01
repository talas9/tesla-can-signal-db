---
layout: default
title: "SCCM_rightStalk (0x229) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Steering column control module message: right stalk. Tesla Model 3 / Model Y CAN bus message SCCM_rightStalk (0x229) of Steering column control module, firmware 2025.20.8, 6 signals (SCCM_rightStalkCrc, SCCM_rightStalkCounter, SCCM_rightStalkStatus, SCCM_rightStalkReserved1 and 2 more). Bit layout, scaling, units and value tables."
---

# SCCM_rightStalk (0x229) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Steering column control module message: right stalk; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of SCCM_rightStalk as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_rightStalk` |
| CAN id | 0x229 (553) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of SCCM_rightStalk

Tesla Model 3 / Model Y CAN bus signals in `SCCM_rightStalk`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_rightStalkCrc` | Steering column control module: right stalk crc | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SCCM_rightStalkCounter` | Steering column control module: right stalk counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_rightStalkStatus` | Active state of drive stalk position, does not indicate active drive gear; raw 6 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `IDLE`<br>1 = `UP_1`<br>2 = `UP_2`<br>3 = `DOWN_1`<br>4 = `DOWN_2`<br>5 = `INIT`<br>6 = `SNA` | plausible |
| `SCCM_rightStalkReserved1` | Steering column control module: right stalk reserved1 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_parkButtonStatus` | Active state of park button on the drive stalk; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_PRESSED`<br>1 = `PRESSED`<br>2 = `INIT`<br>3 = `SNA` | plausible |
| `SCCM_rightStalkReserved2` | Steering column control module: right stalk reserved2 | 18\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
