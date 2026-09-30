---
layout: default
title: "PMF_udsResponse (0x654) — PMF ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "PMF ECU message: uds response. Tesla Model 3 / Model Y CAN bus message PMF_udsResponse (0x654) of PMF ECU, firmware 2026.26.6.5, 1 signals (PMF_udsResponseData). Bit layout, scaling, units and value tables."
---

# PMF_udsResponse (0x654) — PMF ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

PMF ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PMF_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_udsResponse` |
| CAN id | 0x654 (1620) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PMF_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `PMF_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_udsResponseData` | PMF ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
