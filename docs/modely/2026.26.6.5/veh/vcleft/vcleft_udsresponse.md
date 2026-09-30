---
layout: default
title: "VCLEFT_udsResponse (0x623) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: uds response. Tesla Model Y CAN bus message VCLEFT_udsResponse (0x623) of Left body controller, firmware 2026.26.6.5, 2 signals (VCLEFT_udsResponseData_H, VCLEFT_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# VCLEFT_udsResponse (0x623) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Left body controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of VCLEFT_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_udsResponse` |
| CAN id | 0x623 (1571) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of VCLEFT_udsResponse

Tesla Model Y CAN bus signals in `VCLEFT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_udsResponseData_H` | Left body controller: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `VCLEFT_udsResponseData_L` | Left body controller: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
