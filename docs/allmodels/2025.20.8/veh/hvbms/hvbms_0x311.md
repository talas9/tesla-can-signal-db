---
layout: default
title: "HVBMS_0x311 (0x311) — HVBMS ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vector__XXX ECU message: 0x311. Tesla Model 3 / Model Y CAN bus message HVBMS_0x311 (0x311) of HVBMS ECU, firmware 2025.20.8, 5 signals (HVBMS_0x311_b0_10, HVBMS_0x311_b10_1, HVBMS_0x311_b11_1, HVBMS_0x311_b12_1 and 1 more). Bit layout, scaling, units and value tables."
---

# HVBMS_0x311 (0x311) — HVBMS ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vector__XXX ECU message: 0x311; frame length observed on a vehicle bus. This page documents the 5 signals of HVBMS_0x311 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVBMS_0x311` |
| CAN id | 0x311 (785) |
| ECU | [HVBMS ECU](../../hvbms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | other |
| Frame length | 2 bytes |
| Cycle time | not cyclic or not known |
| Signals | 5 |

## Signals of HVBMS_0x311

Tesla Model 3 / Model Y CAN bus signals in `HVBMS_0x311`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVBMS_0x311_b0_10` | Battery computer field at bits 0-9; position from firmware, meaning not yet known | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `HVBMS_0x311_b10_1` | Battery computer field at bits 10-10; position from firmware, meaning not yet known | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVBMS_0x311_b11_1` | Battery computer field at bits 11-11; position from firmware, meaning not yet known | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVBMS_0x311_b12_1` | Battery computer field at bits 12-12; position from firmware, meaning not yet known | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVBMS_0x311_b13_1` | Battery computer field at bits 13-13; position from firmware, meaning not yet known | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All HVBMS ECU messages (HVBMS)](../../hvbms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
