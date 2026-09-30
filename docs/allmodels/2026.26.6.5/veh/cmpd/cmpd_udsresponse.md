---
layout: default
title: "CMPD_udsResponse (0x617) — CMPD ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "CMPD ECU message: uds response. Tesla Model 3 / Model Y CAN bus message CMPD_udsResponse (0x617) of CMPD ECU, firmware 2026.26.6.5, 1 signals (CMPD_udsResponseData). Bit layout, scaling, units and value tables."
---

# CMPD_udsResponse (0x617) — CMPD ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

CMPD ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of CMPD_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CMPD_udsResponse` |
| CAN id | 0x617 (1559) |
| ECU | [CMPD ECU](../../cmpd.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CMPD |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of CMPD_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `CMPD_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CMPD_udsResponseData` | CMPD ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All CMPD ECU messages (CMPD)](../../cmpd.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
