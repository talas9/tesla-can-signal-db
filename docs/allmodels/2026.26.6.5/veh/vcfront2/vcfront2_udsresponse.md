---
layout: default
title: "VCFRONT2_udsResponse (0x62F) — VCFRONT2 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCFRONT2 ECU message: uds response. Tesla Model 3 / Model Y CAN bus message VCFRONT2_udsResponse (0x62F) of VCFRONT2 ECU, firmware 2026.26.6.5, 1 signals (VCFRONT2_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCFRONT2_udsResponse (0x62F) — VCFRONT2 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCFRONT2 ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCFRONT2_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT2_udsResponse` |
| CAN id | 0x62F (1583) |
| ECU | [VCFRONT2 ECU](../../vcfront2.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT2 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCFRONT2_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT2_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT2_udsResponseData` | VCFRONT2 ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT2 ECU messages (VCFRONT2)](../../vcfront2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
