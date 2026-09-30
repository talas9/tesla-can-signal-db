---
layout: default
title: "Left electric parking brake (EPBL) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y EPBL CAN bus messages and signals of the Left electric parking brake (EPBL) for firmware 2026.26.6.5: 7 messages, 868 signals with bit layout, scaling and value tables."
---

# Left electric parking brake (EPBL) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 7 messages of the Left electric parking brake (EPBL) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPBL_alertLog`](veh/epbl/epbl_alertlog.md) | VEH | 0x5C8 | 8 |  | 623 |
| [`EPBL_alertMatrix`](veh/epbl/epbl_alertmatrix.md) | VEH | 0x3C8 | 8 | 100 ms | 169 |
| [`EPBL_info`](veh/epbl/epbl_info.md) | VEH | 0x7C8 | 8 | 1000 ms | 15 |
| [`EPBL_internalStatus`](veh/epbl/epbl_internalstatus.md) | VEH | 0x288 | 8 | 100 ms | 19 |
| [`EPBL_seatStatus3`](veh/epbl/epbl_seatstatus3.md) | VEH | 0x2E7 | 5 | 1000 ms | 6 |
| [`EPBL_status`](veh/epbl/epbl_status.md) | VEH | 0x2A8 | 8 | 100 ms | 34 |
| [`EPBL_udsResponse`](veh/epbl/epbl_udsresponse.md) | VEH | 0x625 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

