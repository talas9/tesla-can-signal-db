---
layout: default
title: "PMR_udsResponse (0x614) — PMR ECU, Tesla Model Y 2025.20.8 ETH"
description: "PMR ECU message: uds response. Ethernet-side message PMR_udsResponse of PMR ECU for Tesla Model Y firmware 2025.20.8, 1 signals (PMR_udsResponseData). Bit layout, scaling, units and value tables."
---

# PMR_udsResponse (0x614) — PMR ECU, Tesla Model Y 2025.20.8 ETH

PMR ECU message: uds response. This page documents the 1 signals of PMR_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_udsResponse` |
| Ethernet-side id | 0x614 (1556) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PMR_udsResponse

Tesla Model Y CAN bus signals in `PMR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_udsResponseData` | PMR ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
