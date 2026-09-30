---
layout: default
title: "PM ECU (PM) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y PM CAN bus messages and signals of the PM ECU (PM) for firmware 2025.20.8: 7 messages, 439 signals with bit layout, scaling and value tables."
---

# PM ECU (PM) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 7 messages of the PM ECU (PM) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PM_info`](veh/pm/pm_info.md) | VEH | 0x60F | 8 | 1000 ms | 12 |
| [`PM_vdcDebug`](party/pm/pm_vdcdebug.md) | PARTY | 0x7F6 | 8 | 20 ms | 20 |
| [`PM_alertLog`](eth/pm/pm_alertlog.md) | ETH | 0x5A4 | 8 |  | 296 |
| [`PM_alertMatrix1`](eth/pm/pm_alertmatrix1.md) | ETH | 0x384 | 8 | 1000 ms | 60 |
| [`PM_alertMatrix2`](eth/pm/pm_alertmatrix2.md) | ETH | 0x380 | 8 | 1000 ms | 39 |
| [`PM_systemState`](eth/pm/pm_systemstate.md) | ETH | 0x1CF | 8 | 10 ms | 11 |
| [`PM_udsResponse`](eth/pm/pm_udsresponse.md) | ETH | 0x640 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

