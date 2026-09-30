---
layout: default
title: "Front drive inverter (DIF) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y DIF CAN bus messages and signals of the Front drive inverter (DIF) for firmware 2026.26.6.5: 13 messages, 962 signals with bit layout, scaling and value tables."
---

# Front drive inverter (DIF) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 13 messages of the Front drive inverter (DIF) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DIF_alertLog`](veh/dif/dif_alertlog.md) | VEH | 0x526 | 8 |  | 580 |
| [`DIF_alertMatrix`](veh/dif/dif_alertmatrix.md) | VEH | 0x356 | 8 | 1000 ms | 184 |
| [`DIF_hvStatus`](veh/dif/dif_hvstatus.md) | VEH | 0x27A | 8 | 100 ms | 15 |
| [`DIF_power`](veh/dif/dif_power.md) | VEH | 0x2E5 | 8 | 1000 ms | 6 |
| [`DIF_temperature`](veh/dif/dif_temperature.md) | VEH | 0x376 | 8 | 1000 ms | 21 |
| [`DIF_thermalControl`](veh/dif/dif_thermalcontrol.md) | VEH | 0x557 | 5 | 1000 ms | 6 |
| [`DIF_udsResponse`](veh/dif/dif_udsresponse.md) | VEH | 0x615 | 8 |  | 1 |
| [`DIF_debug`](party/dif/dif_debug.md) | PARTY | 0x757 | 8 | 100 ms | 79 |
| [`DIF_info`](party/dif/dif_info.md) | PARTY | 0x656 | 8 | 1000 ms | 29 |
| [`DIF_motorStatus`](party/dif/dif_motorstatus.md) | PARTY | 0x1A5 | 5 | 100 ms | 7 |
| [`DIF_oilPump`](party/dif/dif_oilpump.md) | PARTY | 0x396 | 8 | 100 ms | 10 |
| [`DIF_status`](party/dif/dif_status.md) | PARTY | 0x2D5 | 8 | 10 ms | 15 |
| [`DIF_torque`](party/dif/dif_torque.md) | PARTY | 0x186 | 8 | 10 ms | 9 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

