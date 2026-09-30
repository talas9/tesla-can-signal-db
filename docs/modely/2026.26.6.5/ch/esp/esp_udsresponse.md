---
layout: default
title: "ESP_udsResponse (0x655) — Electronic stability control, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Electronic stability control message: uds response. Tesla Model Y CAN bus message ESP_udsResponse (0x655) of Electronic stability control, firmware 2026.26.6.5, 1 signals (ESP_udsResponseData). Bit layout, scaling, units and value tables."
---

# ESP_udsResponse (0x655) — Electronic stability control, Tesla Model Y 2026.26.6.5 CH CAN

Electronic stability control message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of ESP_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_udsResponse` |
| CAN id | 0x655 (1621) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 1 |

## Signals of ESP_udsResponse

Tesla Model Y CAN bus signals in `ESP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_udsResponseData` | Electronic stability control: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
