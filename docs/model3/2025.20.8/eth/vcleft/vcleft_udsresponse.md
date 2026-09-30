---
layout: default
title: "VCLEFT_udsResponse (0x623) — Left body controller, Tesla Model 3 2025.20.8 ETH"
description: "Left body controller message: uds response. Ethernet-side message VCLEFT_udsResponse of Left body controller for Tesla Model 3 firmware 2025.20.8, 2 signals (VCLEFT_udsResponseData_H, VCLEFT_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# VCLEFT_udsResponse (0x623) — Left body controller, Tesla Model 3 2025.20.8 ETH

Left body controller message: uds response. This page documents the 2 signals of VCLEFT_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_udsResponse` |
| Ethernet-side id | 0x623 (1571) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of VCLEFT_udsResponse

Tesla Model 3 CAN bus signals in `VCLEFT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_udsResponseData_H` | Left body controller: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `VCLEFT_udsResponseData_L` | Left body controller: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
