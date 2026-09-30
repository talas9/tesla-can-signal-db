---
layout: default
title: "Left electric parking brake (EPBL) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y EPBL CAN bus messages and signals of the Left electric parking brake (EPBL) for firmware 2025.20.8: 7 messages, 867 signals with bit layout, scaling and value tables."
---

# Left electric parking brake (EPBL) CAN messages and signals — Tesla Model Y 2025.20.8

All 7 messages of the Left electric parking brake (EPBL) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPBL_info`](veh/epbl/epbl_info.md) | VEH | 0x7C8 | 8 | 1000 ms | 15 |
| [`EPBL_internalStatus`](veh/epbl/epbl_internalstatus.md) | VEH | 0x288 | 8 | 100 ms | 19 |
| [`EPBL_seatStatus3`](veh/epbl/epbl_seatstatus3.md) | VEH | 0x2E7 | 5 | 1000 ms | 6 |
| [`EPBL_alertLog`](eth/epbl/epbl_alertlog.md) | ETH | 0x5C8 | 8 |  | 629 |
| [`EPBL_alertMatrix`](eth/epbl/epbl_alertmatrix.md) | ETH | 0x3C8 | 8 | 100 ms | 163 |
| [`EPBL_status`](eth/epbl/epbl_status.md) | ETH | 0x2A9 | 8 | 100 ms | 33 |
| [`EPBL_udsResponse`](eth/epbl/epbl_udsresponse.md) | ETH | 0x625 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

