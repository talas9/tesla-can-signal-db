---
layout: default
title: "PM ECU (PM) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y PM CAN bus messages and signals of the PM ECU (PM) for firmware 2026.26.6.5: 7 messages, 468 signals with bit layout, scaling and value tables."
---

# PM ECU (PM) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 7 messages of the PM ECU (PM) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PM_alertLog`](veh/pm/pm_alertlog.md) | VEH | 0x5A4 | 8 |  | 299 |
| [`PM_alertMatrix`](veh/pm/pm_alertmatrix.md) | VEH | 0x384 | 8 | 1000 ms | 104 |
| [`PM_info`](veh/pm/pm_info.md) | VEH | 0x60F | 8 | 1000 ms | 12 |
| [`PM_locState`](veh/pm/pm_locstate.md) | VEH | 0x1E5 | 8 | 10 ms | 18 |
| [`PM_udsResponse`](veh/pm/pm_udsresponse.md) | VEH | 0x640 | 8 |  | 1 |
| [`PM_itpmsDisplay`](party/pm/pm_itpmsdisplay.md) | PARTY | 0x7B5 | 3 | 1000 ms | 14 |
| [`PM_vdcDebug`](party/pm/pm_vdcdebug.md) | PARTY | 0x7F6 | 8 | 20 ms | 20 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

