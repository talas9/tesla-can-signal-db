---
layout: default
title: "VCRIGHT_udsResponse (0x609) — Right body controller, Tesla Model 3 2025.20.8 ETH"
description: "Right body controller message: uds response. Ethernet-side message VCRIGHT_udsResponse of Right body controller for Tesla Model 3 firmware 2025.20.8, 2 signals (VCRIGHT_udsResponseData_H, VCRIGHT_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# VCRIGHT_udsResponse (0x609) — Right body controller, Tesla Model 3 2025.20.8 ETH

Right body controller message: uds response. This page documents the 2 signals of VCRIGHT_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_udsResponse` |
| Ethernet-side id | 0x609 (1545) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of VCRIGHT_udsResponse

Tesla Model 3 CAN bus signals in `VCRIGHT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_udsResponseData_H` | Right body controller: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `VCRIGHT_udsResponseData_L` | Right body controller: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
