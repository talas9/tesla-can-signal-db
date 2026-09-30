---
layout: default
title: "ICR_udsResponse (0x658) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "ICR ECU message: uds response. Ethernet-side message ICR_udsResponse of ICR ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (ICR_udsResponseData). Bit layout, scaling, units and value tables."
---

# ICR_udsResponse (0x658) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

ICR ECU message: uds response. This page documents the 1 signals of ICR_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_udsResponse` |
| Ethernet-side id | 0x658 (1624) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of ICR_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `ICR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_udsResponseData` | ICR ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
