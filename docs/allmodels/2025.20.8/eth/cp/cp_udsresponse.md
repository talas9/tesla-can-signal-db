---
layout: default
title: "CP_udsResponse (0x61E) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Charge port controller message: uds response. Ethernet-side message CP_udsResponse of Charge port controller for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (CP_udsResponseData). Bit layout, scaling, units and value tables."
---

# CP_udsResponse (0x61E) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Charge port controller message: uds response. This page documents the 1 signals of CP_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_udsResponse` |
| Ethernet-side id | 0x61E (1566) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of CP_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `CP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_udsResponseData` | Charge port controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
