---
layout: default
title: "HVBMS_0x452 (0x452) — HVBMS ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vector__XXX ECU message: 0x452. Tesla Model 3 / Model Y CAN bus message HVBMS_0x452 (0x452) of HVBMS ECU, firmware 2025.20.8, 1 signals (HVBMS_0x452_b0_10). Bit layout, scaling, units and value tables."
---

# HVBMS_0x452 (0x452) — HVBMS ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vector__XXX ECU message: 0x452; frame length observed on a vehicle bus. This page documents the 1 signals of HVBMS_0x452 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVBMS_0x452` |
| CAN id | 0x452 (1106) |
| ECU | [HVBMS ECU](../../hvbms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | other |
| Frame length | 3 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of HVBMS_0x452

Tesla Model 3 / Model Y CAN bus signals in `HVBMS_0x452`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVBMS_0x452_b0_10` | Battery computer field at bits 0-9; position from firmware, meaning not yet known | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All HVBMS ECU messages (HVBMS)](../../hvbms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
