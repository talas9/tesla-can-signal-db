---
layout: default
title: "PMF_udsResponse (0x654) — PMF ECU, Tesla Model 3 2025.20.8 ETH"
description: "PMF ECU message: uds response. Ethernet-side message PMF_udsResponse of PMF ECU for Tesla Model 3 firmware 2025.20.8, 1 signals (PMF_udsResponseData). Bit layout, scaling, units and value tables."
---

# PMF_udsResponse (0x654) — PMF ECU, Tesla Model 3 2025.20.8 ETH

PMF ECU message: uds response. This page documents the 1 signals of PMF_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_udsResponse` |
| Ethernet-side id | 0x654 (1620) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PMF_udsResponse

Tesla Model 3 CAN bus signals in `PMF_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_udsResponseData` | PMF ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
