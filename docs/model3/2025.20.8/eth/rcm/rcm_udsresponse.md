---
layout: default
title: "RCM_udsResponse (0x651) — Restraint control module, Tesla Model 3 2025.20.8 ETH"
description: "Restraint control module message: uds response. Ethernet-side message RCM_udsResponse of Restraint control module for Tesla Model 3 firmware 2025.20.8, 1 signals (RCM_udsResponseData). Bit layout, scaling, units and value tables."
---

# RCM_udsResponse (0x651) — Restraint control module, Tesla Model 3 2025.20.8 ETH

Restraint control module message: uds response. This page documents the 1 signals of RCM_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_udsResponse` |
| Ethernet-side id | 0x651 (1617) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of RCM_udsResponse

Tesla Model 3 CAN bus signals in `RCM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_udsResponseData` | Restraint control module: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
