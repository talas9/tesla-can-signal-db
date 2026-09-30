---
layout: default
title: "ESP_wheelSpeeds (0x175) — Electronic stability control, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Electronic stability control message: wheel speeds. Tesla Model 3 / Model Y CAN bus message ESP_wheelSpeeds (0x175) of Electronic stability control, firmware 2026.26.6.5, 4 signals (ESP_wheelSpeedFrL, ESP_wheelSpeedFrR, ESP_wheelSpeedReL, ESP_wheelSpeedReR). Bit layout, scaling, units and value tables."
---

# ESP_wheelSpeeds (0x175) — Electronic stability control, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Electronic stability control message: wheel speeds; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of ESP_wheelSpeeds as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_wheelSpeeds` |
| CAN id | 0x175 (373) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 4 |

## Signals of ESP_wheelSpeeds

Tesla Model 3 / Model Y CAN bus signals in `ESP_wheelSpeeds`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_wheelSpeedFrL` | Electronic stability control: wheel speed fr l | 0\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedFrR` | Electronic stability control: wheel speed fr r | 13\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedReL` | Electronic stability control: wheel speed re l | 26\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |
| `ESP_wheelSpeedReR` | Electronic stability control: wheel speed re r | 39\|13 | little-endian | unsigned | 0.042 | 0 | km/h | 0 to 343.98 | 8191 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
