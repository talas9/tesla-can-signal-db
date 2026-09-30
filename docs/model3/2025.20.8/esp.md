---
layout: default
title: "Electronic stability control (ESP) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 ESP CAN bus messages and signals of the Electronic stability control (ESP) for firmware 2025.20.8: 6 messages, 435 signals with bit layout, scaling and value tables."
---

# Electronic stability control (ESP) CAN messages and signals — Tesla Model 3 2025.20.8

All 6 messages of the Electronic stability control (ESP) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ESP_info`](ch/esp/esp_info.md) | CH | 0x325 | 8 | 10000 ms | 14 |
| [`ESP_party3`](party/esp/esp_party3.md) | PARTY | 0x38D | 7 | 10 ms | 11 |
| [`ESP_status`](party/esp/esp_status.md) | PARTY | 0x145 | 8 | 20 ms | 26 |
| [`ESP_alertMatrix`](eth/esp/esp_alertmatrix.md) | ETH | 0x3D5 | 8 | 1000 ms | 379 |
| [`ESP_udsResponse`](eth/esp/esp_udsresponse.md) | ETH | 0x655 | 8 | 100 ms | 1 |
| [`ESP_wheelSpeeds`](eth/esp/esp_wheelspeeds.md) | ETH | 0x175 | 8 | 20 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

