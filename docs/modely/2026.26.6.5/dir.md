---
layout: default
title: "Rear drive inverter (DIR) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y DIR CAN bus messages and signals of the Rear drive inverter (DIR) for firmware 2026.26.6.5: 13 messages, 969 signals with bit layout, scaling and value tables."
---

# Rear drive inverter (DIR) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 13 messages of the Rear drive inverter (DIR) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DIR_alertLog`](veh/dir/dir_alertlog.md) | VEH | 0x5A5 | 8 |  | 583 |
| [`DIR_alertMatrix`](veh/dir/dir_alertmatrix.md) | VEH | 0x3A7 | 8 | 1000 ms | 188 |
| [`DIR_debug`](veh/dir/dir_debug.md) | VEH | 0x7D5 | 8 | 100 ms | 79 |
| [`DIR_hvStatus`](veh/dir/dir_hvstatus.md) | VEH | 0x279 | 8 | 100 ms | 15 |
| [`DIR_info`](veh/dir/dir_info.md) | VEH | 0x335 | 8 | 1000 ms | 29 |
| [`DIR_oilPump`](veh/dir/dir_oilpump.md) | VEH | 0x395 | 8 | 100 ms | 10 |
| [`DIR_power`](veh/dir/dir_power.md) | VEH | 0x266 | 8 | 1000 ms | 6 |
| [`DIR_temperature`](veh/dir/dir_temperature.md) | VEH | 0x315 | 8 | 1000 ms | 21 |
| [`DIR_thermalControl`](veh/dir/dir_thermalcontrol.md) | VEH | 0x5D7 | 5 | 1000 ms | 6 |
| [`DIR_udsResponse`](veh/dir/dir_udsresponse.md) | VEH | 0x616 | 8 |  | 1 |
| [`DIR_motorStatus`](party/dir/dir_motorstatus.md) | PARTY | 0x126 | 5 | 100 ms | 7 |
| [`DIR_status`](party/dir/dir_status.md) | PARTY | 0x256 | 8 | 10 ms | 15 |
| [`DIR_torque`](party/dir/dir_torque.md) | PARTY | 0x108 | 8 | 10 ms | 9 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

