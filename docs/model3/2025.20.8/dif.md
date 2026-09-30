---
layout: default
title: "Front drive inverter (DIF) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 DIF CAN bus messages and signals of the Front drive inverter (DIF) for firmware 2025.20.8: 16 messages, 853 signals with bit layout, scaling and value tables."
---

# Front drive inverter (DIF) CAN messages and signals — Tesla Model 3 2025.20.8

All 16 messages of the Front drive inverter (DIF) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DIF_power`](veh/dif/dif_power.md) | VEH | 0x2E5 | 8 | 1000 ms | 6 |
| [`DIF_thermalControl`](veh/dif/dif_thermalcontrol.md) | VEH | 0x557 | 5 | 1000 ms | 6 |
| [`DIF_debug`](party/dif/dif_debug.md) | PARTY | 0x757 | 8 | 100 ms | 14 |
| [`DIF_oilPump`](party/dif/dif_oilpump.md) | PARTY | 0x396 | 8 | 100 ms | 10 |
| [`DIF_alertLog`](eth/dif/dif_alertlog.md) | ETH | 0x526 | 8 |  | 568 |
| [`DIF_alertMatrix1`](eth/dif/dif_alertmatrix1.md) | ETH | 0x356 | 8 | 1000 ms | 61 |
| [`DIF_alertMatrix2`](eth/dif/dif_alertmatrix2.md) | ETH | 0x357 | 8 | 1000 ms | 54 |
| [`DIF_alertMatrix3`](eth/dif/dif_alertmatrix3.md) | ETH | 0x35A | 8 | 1000 ms | 23 |
| [`DIF_alertMatrix4`](eth/dif/dif_alertmatrix4.md) | ETH | 0x35B | 8 | 1000 ms | 20 |
| [`DIF_hvStatus`](eth/dif/dif_hvstatus.md) | ETH | 0x27A | 7 | 100 ms | 14 |
| [`DIF_info`](eth/dif/dif_info.md) | ETH | 0x656 | 8 | 1000 ms | 28 |
| [`DIF_motorStatus`](eth/dif/dif_motorstatus.md) | ETH | 0x1A5 | 4 | 100 ms | 4 |
| [`DIF_status`](eth/dif/dif_status.md) | ETH | 0x2D5 | 7 | 10 ms | 16 |
| [`DIF_temperature`](eth/dif/dif_temperature.md) | ETH | 0x376 | 8 | 1000 ms | 20 |
| [`DIF_torque`](eth/dif/dif_torque.md) | ETH | 0x186 | 8 | 100 ms | 8 |
| [`DIF_udsResponse`](eth/dif/dif_udsresponse.md) | ETH | 0x615 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

