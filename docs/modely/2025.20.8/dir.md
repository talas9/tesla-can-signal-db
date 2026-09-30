---
layout: default
title: "Rear drive inverter (DIR) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y DIR CAN bus messages and signals of the Rear drive inverter (DIR) for firmware 2025.20.8: 16 messages, 854 signals with bit layout, scaling and value tables."
---

# Rear drive inverter (DIR) CAN messages and signals — Tesla Model Y 2025.20.8

All 16 messages of the Rear drive inverter (DIR) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DIR_debug`](veh/dir/dir_debug.md) | VEH | 0x7D5 | 8 | 100 ms | 14 |
| [`DIR_oilPump`](veh/dir/dir_oilpump.md) | VEH | 0x395 | 8 | 100 ms | 10 |
| [`DIR_power`](veh/dir/dir_power.md) | VEH | 0x266 | 8 | 1000 ms | 6 |
| [`DIR_thermalControl`](veh/dir/dir_thermalcontrol.md) | VEH | 0x5D7 | 5 | 1000 ms | 6 |
| [`DIR_alertLog`](eth/dir/dir_alertlog.md) | ETH | 0x5A5 | 8 |  | 568 |
| [`DIR_alertMatrix1`](eth/dir/dir_alertmatrix1.md) | ETH | 0x3A7 | 8 | 1000 ms | 61 |
| [`DIR_alertMatrix2`](eth/dir/dir_alertmatrix2.md) | ETH | 0x3B5 | 8 | 1000 ms | 55 |
| [`DIR_alertMatrix3`](eth/dir/dir_alertmatrix3.md) | ETH | 0x3C5 | 8 | 1000 ms | 24 |
| [`DIR_alertMatrix4`](eth/dir/dir_alertmatrix4.md) | ETH | 0x3E5 | 8 | 1000 ms | 21 |
| [`DIR_hvStatus`](eth/dir/dir_hvstatus.md) | ETH | 0x279 | 7 | 100 ms | 14 |
| [`DIR_info`](eth/dir/dir_info.md) | ETH | 0x335 | 8 | 1000 ms | 26 |
| [`DIR_motorStatus`](eth/dir/dir_motorstatus.md) | ETH | 0x7F7 | 4 | 100 ms | 4 |
| [`DIR_status`](eth/dir/dir_status.md) | ETH | 0x256 | 7 | 10 ms | 16 |
| [`DIR_temperature`](eth/dir/dir_temperature.md) | ETH | 0x315 | 8 | 1000 ms | 20 |
| [`DIR_torque`](eth/dir/dir_torque.md) | ETH | 0x108 | 8 | 10 ms | 8 |
| [`DIR_udsResponse`](eth/dir/dir_udsresponse.md) | ETH | 0x616 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

