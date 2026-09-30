---
layout: default
title: "Drive inverter (DI) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y DI CAN bus messages and signals of the Drive inverter (DI) for firmware 2026.26.6.5: 22 messages, 884 signals with bit layout, scaling and value tables."
---

# Drive inverter (DI) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 22 messages of the Drive inverter (DI) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DI_alertLog`](veh/di/di_alertlog.md) | VEH | 0x527 | 8 |  | 409 |
| [`DI_alertMatrix`](veh/di/di_alertmatrix.md) | VEH | 0x367 | 8 | 1000 ms | 220 |
| [`DI_chassisControlStatus`](veh/di/di_chassiscontrolstatus.md) | VEH | 0x2B6 | 3 | 100 ms | 14 |
| [`DI_debug`](veh/di/di_debug.md) | VEH | 0x7D7 | 8 | 100 ms | 8 |
| [`DI_estimatedBrakeTemp`](veh/di/di_estimatedbraketemp.md) | VEH | 0x3FE | 8 | 1000 ms | 8 |
| [`DI_info`](veh/di/di_info.md) | VEH | 0x657 | 8 | 1000 ms | 12 |
| [`DI_odometerStatus`](veh/di/di_odometerstatus.md) | VEH | 0x3B6 | 8 | 1000 ms | 4 |
| [`DI_systemLimits`](veh/di/di_systemlimits.md) | VEH | 0x128 | 6 | 100 ms | 23 |
| [`DI_systemPower`](veh/di/di_systempower.md) | VEH | 0x268 | 5 | 100 ms | 5 |
| [`DI_systemStatus`](veh/di/di_systemstatus.md) | VEH | 0x118 | 8 | 10 ms | 21 |
| [`DI_autonomyHealth`](party/di/di_autonomyhealth.md) | PARTY | 0x54 | 8 | 100 ms | 15 |
| [`DI_chassisControl`](party/di/di_chassiscontrol.md) | PARTY | 0x148 | 8 | 20 ms | 18 |
| [`DI_chassisControl2`](party/di/di_chassiscontrol2.md) | PARTY | 0x745 | 8 | 100 ms | 23 |
| [`DI_chassisControl3`](party/di/di_chassiscontrol3.md) | PARTY | 0x74D | 8 | 1000 ms | 14 |
| [`DI_locStatus`](party/di/di_locstatus.md) | PARTY | 0x286 | 8 | 100 ms | 17 |
| [`DI_locStatus2`](party/di/di_locstatus2.md) | PARTY | 0x4F6 | 8 | 100 ms | 17 |
| [`DI_maxRatedPower`](party/di/di_maxratedpower.md) | PARTY | 0x336 | 3 | 1000 ms | 3 |
| [`DI_speed`](party/di/di_speed.md) | PARTY | 0x257 | 8 | 20 ms | 11 |
| [`DI_stalklessInterfaces`](party/di/di_stalklessinterfaces.md) | PARTY | 0x258 | 3 | 100 ms | 8 |
| [`DI_suggestedGear`](party/di/di_suggestedgear.md) | PARTY | 0x255 | 4 | 100 ms | 10 |
| [`DI_vdcRight`](party/di/di_vdcright.md) | PARTY | 0x11A | 8 | 20 ms | 11 |
| [`DI_vehicleEstimates`](party/di/di_vehicleestimates.md) | PARTY | 0x267 | 8 | 1000 ms | 13 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

