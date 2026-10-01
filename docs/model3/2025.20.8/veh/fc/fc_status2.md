---
layout: default
title: "FC_status2 (0x215) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: status2. Tesla Model 3 CAN bus message FC_status2 (0x215) of FC ECU, firmware 2025.20.8, 1 signals (FC_externalIsolationResistance). Bit layout, scaling, units and value tables."
---

# FC_status2 (0x215) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of FC_status2 as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_status2` |
| CAN id | 0x215 (533) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of FC_status2

Tesla Model 3 CAN bus signals in `FC_status2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_externalIsolationResistance` | Fast charger external isolation resistance; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 40 | 0 | kOhm | 0 to 10160 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
