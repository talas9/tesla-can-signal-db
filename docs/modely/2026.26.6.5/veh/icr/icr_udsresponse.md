---
layout: default
title: "ICR_udsResponse (0x658) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: uds response. Tesla Model Y CAN bus message ICR_udsResponse (0x658) of ICR ECU, firmware 2026.26.6.5, 1 signals (ICR_udsResponseData). Bit layout, scaling, units and value tables."
---

# ICR_udsResponse (0x658) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN

ICR ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of ICR_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_udsResponse` |
| CAN id | 0x658 (1624) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of ICR_udsResponse

Tesla Model Y CAN bus signals in `ICR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_udsResponseData` | ICR ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
