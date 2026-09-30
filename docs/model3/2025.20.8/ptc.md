---
layout: default
title: "Cabin heater (PTC) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 PTC CAN bus messages and signals of the Cabin heater (PTC) for firmware 2025.20.8: 4 messages, 35 signals with bit layout, scaling and value tables."
---

# Cabin heater (PTC) CAN messages and signals — Tesla Model 3 2025.20.8

All 4 messages of the Cabin heater (PTC) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PTC_info`](veh/ptc/ptc_info.md) | VEH | 0x345 | 8 | 1000 ms | 13 |
| [`PTC_sensorStatus`](veh/ptc/ptc_sensorstatus.md) | VEH | 0x287 | 8 | 100 ms | 7 |
| [`PTC_feedbackStatus`](eth/ptc/ptc_feedbackstatus.md) | ETH | 0x207 | 8 | 100 ms | 14 |
| [`PTC_udsResponse`](eth/ptc/ptc_udsresponse.md) | ETH | 0x6D6 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

