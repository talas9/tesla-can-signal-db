---
layout: default
title: "VCBATT2_udsResponse (0x61B) — VCBATT2 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT2 ECU message: uds response. Tesla Model 3 / Model Y CAN bus message VCBATT2_udsResponse (0x61B) of VCBATT2 ECU, firmware 2026.26.6.5, 1 signals (VCBATT2_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCBATT2_udsResponse (0x61B) — VCBATT2 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCBATT2 ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCBATT2_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT2_udsResponse` |
| CAN id | 0x61B (1563) |
| ECU | [VCBATT2 ECU](../../vcbatt2.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT2 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCBATT2_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `VCBATT2_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT2_udsResponseData` | VCBATT2 ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCBATT2 ECU messages (VCBATT2)](../../vcbatt2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
