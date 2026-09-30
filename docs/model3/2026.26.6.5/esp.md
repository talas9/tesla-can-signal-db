---
layout: default
title: "Electronic stability control (ESP) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 ESP CAN bus messages and signals of the Electronic stability control (ESP) for firmware 2026.26.6.5: 6 messages, 466 signals with bit layout, scaling and value tables."
---

# Electronic stability control (ESP) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 6 messages of the Electronic stability control (ESP) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ESP_alertMatrix`](ch/esp/esp_alertmatrix.md) | CH | 0x3D5 | 8 | 1000 ms | 410 |
| [`ESP_info`](ch/esp/esp_info.md) | CH | 0x325 | 8 | 10000 ms | 14 |
| [`ESP_udsResponse`](ch/esp/esp_udsresponse.md) | CH | 0x655 | 8 | 100 ms | 1 |
| [`ESP_party3`](party/esp/esp_party3.md) | PARTY | 0x38D | 7 | 10 ms | 11 |
| [`ESP_status`](party/esp/esp_status.md) | PARTY | 0x145 | 8 | 20 ms | 26 |
| [`ESP_wheelSpeeds`](party/esp/esp_wheelspeeds.md) | PARTY | 0x175 | 8 | 20 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

