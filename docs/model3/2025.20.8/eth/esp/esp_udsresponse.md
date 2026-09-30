---
layout: default
title: "ESP_udsResponse (0x655) — Electronic stability control, Tesla Model 3 2025.20.8 ETH"
description: "Electronic stability control message: uds response. Ethernet-side message ESP_udsResponse of Electronic stability control for Tesla Model 3 firmware 2025.20.8, 1 signals (ESP_udsResponseData). Bit layout, scaling, units and value tables."
---

# ESP_udsResponse (0x655) — Electronic stability control, Tesla Model 3 2025.20.8 ETH

Electronic stability control message: uds response. This page documents the 1 signals of ESP_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_udsResponse` |
| Ethernet-side id | 0x655 (1621) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 1 |

## Signals of ESP_udsResponse

Tesla Model 3 CAN bus signals in `ESP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_udsResponseData` | Electronic stability control: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
