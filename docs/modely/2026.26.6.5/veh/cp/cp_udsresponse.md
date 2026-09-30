---
layout: default
title: "CP_udsResponse (0x61E) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: uds response. Tesla Model Y CAN bus message CP_udsResponse (0x61E) of Charge port controller, firmware 2026.26.6.5, 1 signals (CP_udsResponseData). Bit layout, scaling, units and value tables."
---

# CP_udsResponse (0x61E) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN

Charge port controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of CP_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_udsResponse` |
| CAN id | 0x61E (1566) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of CP_udsResponse

Tesla Model Y CAN bus signals in `CP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_udsResponseData` | Charge port controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
