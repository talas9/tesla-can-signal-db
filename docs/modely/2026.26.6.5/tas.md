---
layout: default
title: "Air suspension controller (TAS) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y TAS CAN bus messages and signals of the Air suspension controller (TAS) for firmware 2026.26.6.5: 10 messages, 495 signals with bit layout, scaling and value tables."
---

# Air suspension controller (TAS) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 10 messages of the Air suspension controller (TAS) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`TAS_alertLog`](veh/tas/tas_alertlog.md) | VEH | 0x50B | 8 |  | 215 |
| [`TAS_alertMatrix`](veh/tas/tas_alertmatrix.md) | VEH | 0x354 | 8 | 100 ms | 171 |
| [`TAS_axleData`](veh/tas/tas_axledata.md) | VEH | 0x20B | 8 | 20 ms | 13 |
| [`TAS_dampingStates`](veh/tas/tas_dampingstates.md) | VEH | 0x576 | 8 | 100 ms | 23 |
| [`TAS_info`](veh/tas/tas_info.md) | VEH | 0x54D | 8 | 1000 ms | 17 |
| [`TAS_states`](veh/tas/tas_states.md) | VEH | 0x20D | 8 | 100 ms | 16 |
| [`TAS_udsResponse`](veh/tas/tas_udsresponse.md) | VEH | 0x65B | 8 |  | 1 |
| [`TAS_uiAdaptiveActivity0`](veh/tas/tas_uiadaptiveactivity0.md) | VEH | 0x199 | 8 | 50 ms | 12 |
| [`TAS_uiAdaptiveActivity1`](veh/tas/tas_uiadaptiveactivity1.md) | VEH | 0x19A | 4 | 50 ms | 4 |
| [`TAS_uiControl`](veh/tas/tas_uicontrol.md) | VEH | 0x21A | 5 | 100 ms | 23 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

