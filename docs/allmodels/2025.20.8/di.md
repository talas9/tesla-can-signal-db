---
layout: default
title: "Drive inverter (DI) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y DI CAN bus messages and signals of the Drive inverter (DI) for firmware 2025.20.8: 24 messages, 847 signals with bit layout, scaling and value tables."
---

# Drive inverter (DI) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 24 messages of the Drive inverter (DI) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DI_debug`](veh/di/di_debug.md) | VEH | 0x7D7 | 8 | 100 ms | 8 |
| [`DI_systemPower`](veh/di/di_systempower.md) | VEH | 0x268 | 5 | 100 ms | 5 |
| [`DI_chassisControl`](party/di/di_chassiscontrol.md) | PARTY | 0x148 | 8 | 20 ms | 18 |
| [`DI_chassisControl3`](party/di/di_chassiscontrol3.md) | PARTY | 0x74D | 8 | 1000 ms | 14 |
| [`DI_locStatus`](party/di/di_locstatus.md) | PARTY | 0x286 | 8 | 100 ms | 17 |
| [`DI_stalklessInterfaces`](party/di/di_stalklessinterfaces.md) | PARTY | 0x258 | 3 | 100 ms | 8 |
| [`DI_suggestedGear`](party/di/di_suggestedgear.md) | PARTY | 0x255 | 4 | 100 ms | 10 |
| [`DI_vdcRight`](party/di/di_vdcright.md) | PARTY | 0x11A | 8 | 20 ms | 11 |
| [`DI_vehicleEstimates`](party/di/di_vehicleestimates.md) | PARTY | 0x267 | 8 | 1000 ms | 13 |
| [`DI_alertLog`](eth/di/di_alertlog.md) | ETH | 0x527 | 8 |  | 409 |
| [`DI_alertMatrix1`](eth/di/di_alertmatrix1.md) | ETH | 0x367 | 8 | 1000 ms | 48 |
| [`DI_alertMatrix2`](eth/di/di_alertmatrix2.md) | ETH | 0x368 | 8 | 1000 ms | 51 |
| [`DI_alertMatrix3`](eth/di/di_alertmatrix3.md) | ETH | 0x36B | 8 | 1000 ms | 53 |
| [`DI_alertMatrix4`](eth/di/di_alertmatrix4.md) | ETH | 0x36E | 8 | 1000 ms | 57 |
| [`DI_chassisControl2`](eth/di/di_chassiscontrol2.md) | ETH | 0x745 | 8 | 100 ms | 22 |
| [`DI_chassisControlStatus`](eth/di/di_chassiscontrolstatus.md) | ETH | 0x2B6 | 2 | 100 ms | 13 |
| [`DI_estimatedBrakeTemp`](eth/di/di_estimatedbraketemp.md) | ETH | 0x74A | 7 | 1000 ms | 6 |
| [`DI_info`](eth/di/di_info.md) | ETH | 0x657 | 8 | 1000 ms | 11 |
| [`DI_locStatus2`](eth/di/di_locstatus2.md) | ETH | 0x4F6 | 7 | 100 ms | 14 |
| [`DI_maxRatedPower`](eth/di/di_maxratedpower.md) | ETH | 0x336 | 3 | 1000 ms | 4 |
| [`DI_odometerStatus`](eth/di/di_odometerstatus.md) | ETH | 0x3B6 | 8 | 1000 ms | 3 |
| [`DI_speed`](eth/di/di_speed.md) | ETH | 0x257 | 8 | 20 ms | 11 |
| [`DI_systemLimits`](eth/di/di_systemlimits.md) | ETH | 0x128 | 4 | 100 ms | 20 |
| [`DI_systemStatus`](eth/di/di_systemstatus.md) | ETH | 0x118 | 8 | 10 ms | 21 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

