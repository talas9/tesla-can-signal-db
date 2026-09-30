---
layout: default
title: "VCBATT1_udsResponse (0x60D) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: uds response. Tesla Model Y CAN bus message VCBATT1_udsResponse (0x60D) of VCBATT1 ECU, firmware 2026.26.6.5, 1 signals (VCBATT1_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCBATT1_udsResponse (0x60D) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCBATT1_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_udsResponse` |
| CAN id | 0x60D (1549) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCBATT1_udsResponse

Tesla Model Y CAN bus signals in `VCBATT1_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_udsResponseData` | VCBATT1 ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
