---
layout: default
title: "EPBL_udsResponse (0x625) — Left electric parking brake, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left electric parking brake message: uds response. Tesla Model 3 / Model Y CAN bus message EPBL_udsResponse (0x625) of Left electric parking brake, firmware 2026.26.6.5, 2 signals (EPBL_udsResponseData_H, EPBL_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# EPBL_udsResponse (0x625) — Left electric parking brake, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left electric parking brake message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of EPBL_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBL_udsResponse` |
| CAN id | 0x625 (1573) |
| ECU | [Left electric parking brake](../../epbl.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBL |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of EPBL_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `EPBL_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBL_udsResponseData_H` | Left electric parking brake: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `EPBL_udsResponseData_L` | Left electric parking brake: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left electric parking brake messages (EPBL)](../../epbl.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
