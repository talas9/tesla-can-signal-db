---
layout: default
title: "DAS_udsResponse (0x659) — Driver assistance computer, Tesla Model 3 2025.20.8 ETH"
description: "Driver assistance computer message: uds response. Ethernet-side message DAS_udsResponse of Driver assistance computer for Tesla Model 3 firmware 2025.20.8, 1 signals (DAS_udsResponseData). Bit layout, scaling, units and value tables."
---

# DAS_udsResponse (0x659) — Driver assistance computer, Tesla Model 3 2025.20.8 ETH

Driver assistance computer message: uds response. This page documents the 1 signals of DAS_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_udsResponse` |
| Ethernet-side id | 0x659 (1625) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of DAS_udsResponse

Tesla Model 3 CAN bus signals in `DAS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_udsResponseData` | Driver assistance computer: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
