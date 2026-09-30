---
layout: default
title: "Steering column control module (SCCM) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 SCCM CAN bus messages and signals of the Steering column control module (SCCM) for firmware 2025.20.8: 7 messages, 311 signals with bit layout, scaling and value tables."
---

# Steering column control module (SCCM) CAN messages and signals — Tesla Model 3 2025.20.8

All 7 messages of the Steering column control module (SCCM) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`SCCM_alertMatrix`](veh/sccm/sccm_alertmatrix.md) | VEH | 0x54F | 8 | 100 ms | 58 |
| [`SCCM_info`](veh/sccm/sccm_info.md) | VEH | 0x330 | 8 | 1000 ms | 18 |
| [`SCCM_leftStalk`](veh/sccm/sccm_leftstalk.md) | VEH | 0x249 | 4 | 50 ms | 6 |
| [`SCCM_rightStalk`](veh/sccm/sccm_rightstalk.md) | VEH | 0x229 | 3 | 100 ms | 6 |
| [`SCCM_steeringAngleSensor`](veh/sccm/sccm_steeringanglesensor.md) | VEH | 0x129 | 8 | 10 ms | 10 |
| [`SCCM_alertLog`](eth/sccm/sccm_alertlog.md) | ETH | 0x540 | 8 |  | 205 |
| [`SCCM_udsResponse`](eth/sccm/sccm_udsresponse.md) | ETH | 0x690 | 8 |  | 8 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

