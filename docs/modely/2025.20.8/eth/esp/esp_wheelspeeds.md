---
layout: default
title: "ESP_wheelSpeeds (0x175) — Electronic stability control, Tesla Model Y 2025.20.8 ETH"
description: "Electronic stability control message: wheel speeds. Ethernet-side message ESP_wheelSpeeds of Electronic stability control for Tesla Model Y firmware 2025.20.8, 4 signals (ESP_wheelSpeedFrL, ESP_wheelSpeedFrR, ESP_wheelSpeedReL, ESP_wheelSpeedReR). Bit layout, scaling, units and value tables."
---

# ESP_wheelSpeeds (0x175) — Electronic stability control, Tesla Model Y 2025.20.8 ETH

Electronic stability control message: wheel speeds. This page documents the 4 signals of ESP_wheelSpeeds as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_wheelSpeeds` |
| Ethernet-side id | 0x175 (373) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 4 |

## Signals of ESP_wheelSpeeds

Tesla Model Y CAN bus signals in `ESP_wheelSpeeds`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_wheelSpeedFrL` | Electronic stability control: wheel speed fr l | 0\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedFrR` | Electronic stability control: wheel speed fr r | 13\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedReL` | Electronic stability control: wheel speed re l | 26\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedReR` | Electronic stability control: wheel speed re r | 39\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
