---
layout: default
title: "HVP_udsResponse (0x611) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage processor (pack contactor and isolation controller) message: uds response. Ethernet-side message HVP_udsResponse of High-voltage processor (pack contactor and isolation controller) for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (HVP_udsResponseData). Bit layout, scaling, units and value tables."
---

# HVP_udsResponse (0x611) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage processor (pack contactor and isolation controller) message: uds response. This page documents the 1 signals of HVP_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_udsResponse` |
| Ethernet-side id | 0x611 (1553) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of HVP_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `HVP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_udsResponseData` | High-voltage processor (pack contactor and isolation controller): uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
