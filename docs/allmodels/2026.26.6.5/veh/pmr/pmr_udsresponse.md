---
layout: default
title: "PMR_udsResponse (0x614) — PMR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "PMR ECU message: uds response. Tesla Model 3 / Model Y CAN bus message PMR_udsResponse (0x614) of PMR ECU, firmware 2026.26.6.5, 1 signals (PMR_udsResponseData). Bit layout, scaling, units and value tables."
---

# PMR_udsResponse (0x614) — PMR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

PMR ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PMR_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_udsResponse` |
| CAN id | 0x614 (1556) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PMR_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `PMR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_udsResponseData` | PMR ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
