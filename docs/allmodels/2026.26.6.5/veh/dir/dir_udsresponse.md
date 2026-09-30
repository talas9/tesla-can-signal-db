---
layout: default
title: "DIR_udsResponse (0x616) — Rear drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Rear drive inverter message: uds response. Tesla Model 3 / Model Y CAN bus message DIR_udsResponse (0x616) of Rear drive inverter, firmware 2026.26.6.5, 1 signals (DIR_udsResponseData). Bit layout, scaling, units and value tables."
---

# DIR_udsResponse (0x616) — Rear drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Rear drive inverter message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of DIR_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_udsResponse` |
| CAN id | 0x616 (1558) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of DIR_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `DIR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_udsResponseData` | Rear drive inverter: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
