---
layout: default
title: "VCBATT_udsResponse (0x621) — VCBATT ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT ECU message: uds response. Tesla Model Y CAN bus message VCBATT_udsResponse (0x621) of VCBATT ECU, firmware 2026.26.6.5, 1 signals (VCBATT_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCBATT_udsResponse (0x621) — VCBATT ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCBATT_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT_udsResponse` |
| CAN id | 0x621 (1569) |
| ECU | [VCBATT ECU](../../vcbatt.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCBATT_udsResponse

Tesla Model Y CAN bus signals in `VCBATT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT_udsResponseData` | VCBATT ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT ECU messages (VCBATT)](../../vcbatt.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
