---
layout: default
title: "PTC_udsResponse (0x6D6) — Cabin heater, Tesla Model 3 2025.20.8 ETH"
description: "Cabin heater message: uds response. Ethernet-side message PTC_udsResponse of Cabin heater for Tesla Model 3 firmware 2025.20.8, 1 signals (PTC_udsResponseData). Bit layout, scaling, units and value tables."
---

# PTC_udsResponse (0x6D6) — Cabin heater, Tesla Model 3 2025.20.8 ETH

Cabin heater message: uds response. This page documents the 1 signals of PTC_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PTC_udsResponse` |
| Ethernet-side id | 0x6D6 (1750) |
| ECU | [Cabin heater](../../ptc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PTC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PTC_udsResponse

Tesla Model 3 CAN bus signals in `PTC_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PTC_udsResponseData` | Cabin heater: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Cabin heater messages (PTC)](../../ptc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
