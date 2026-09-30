---
layout: default
title: "EPBR_udsResponse (0x627) — Right electric parking brake, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Right electric parking brake message: uds response. Tesla Model 3 / Model Y CAN bus message EPBR_udsResponse (0x627) of Right electric parking brake, firmware 2026.26.6.5, 2 signals (EPBR_udsResponseData_H, EPBR_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# EPBR_udsResponse (0x627) — Right electric parking brake, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Right electric parking brake message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of EPBR_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBR_udsResponse` |
| CAN id | 0x627 (1575) |
| ECU | [Right electric parking brake](../../epbr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of EPBR_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `EPBR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBR_udsResponseData_H` | Right electric parking brake: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `EPBR_udsResponseData_L` | Right electric parking brake: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Right electric parking brake messages (EPBR)](../../epbr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
