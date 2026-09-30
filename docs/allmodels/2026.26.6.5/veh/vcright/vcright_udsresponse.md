---
layout: default
title: "VCRIGHT_udsResponse (0x609) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: uds response. Tesla Model 3 / Model Y CAN bus message VCRIGHT_udsResponse (0x609) of Right body controller, firmware 2026.26.6.5, 2 signals (VCRIGHT_udsResponseData_H, VCRIGHT_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# VCRIGHT_udsResponse (0x609) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Right body controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of VCRIGHT_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_udsResponse` |
| CAN id | 0x609 (1545) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of VCRIGHT_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_udsResponseData_H` | Right body controller: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `VCRIGHT_udsResponseData_L` | Right body controller: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
