---
layout: default
title: "FC ECU (FC) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 FC CAN bus messages and signals of the FC ECU (FC) for firmware 2025.20.8: 16 messages, 226 signals with bit layout, scaling and value tables."
---

# FC ECU (FC) CAN messages and signals — Tesla Model 3 2025.20.8

All 16 messages of the FC ECU (FC) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`FC_alertLog`](veh/fc/fc_alertlog.md) | VEH | 0x52A | 8 |  | 8 |
| [`FC_alertMatrix3`](veh/fc/fc_alertmatrix3.md) | VEH | 0x37F | 8 | 1000 ms | 59 |
| [`FC_alertMatrix4`](veh/fc/fc_alertmatrix4.md) | VEH | 0x39F | 8 | 1000 ms | 1 |
| [`FC_alertMatrix5`](veh/fc/fc_alertmatrix5.md) | VEH | 0x3BE | 8 | 1000 ms | 57 |
| [`FC_alertMatrix6`](veh/fc/fc_alertmatrix6.md) | VEH | 0x3DE | 8 | 1000 ms | 1 |
| [`FC_evseBilling`](veh/fc/fc_evsebilling.md) | VEH | 0x45D | 8 | 1000 ms | 6 |
| [`FC_evseBilling2`](veh/fc/fc_evsebilling2.md) | VEH | 0x536 | 8 | 1000 ms | 3 |
| [`FC_identifier`](veh/fc/fc_identifier.md) | VEH | 0x517 | 8 | 1000 ms | 2 |
| [`FC_info`](veh/fc/fc_info.md) | VEH | 0x51E | 8 | 1000 ms | 37 |
| [`FC_limits`](veh/fc/fc_limits.md) | VEH | 0x244 | 8 | 100 ms | 4 |
| [`FC_limitsHighPower`](veh/fc/fc_limitshighpower.md) | VEH | 0x2BE | 8 | 100 ms | 6 |
| [`FC_maxLimits`](veh/fc/fc_maxlimits.md) | VEH | 0x541 | 8 | 100 ms | 2 |
| [`FC_serial`](veh/fc/fc_serial.md) | VEH | 0x514 | 8 | 1000 ms | 18 |
| [`FC_status`](veh/fc/fc_status.md) | VEH | 0x214 | 8 | 100 ms | 13 |
| [`FC_status2`](veh/fc/fc_status2.md) | VEH | 0x215 | 1 | 1000 ms | 1 |
| [`FC_status3`](veh/fc/fc_status3.md) | VEH | 0x217 | 8 | 1000 ms | 8 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

