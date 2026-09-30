---
layout: default
title: "Right electric parking brake (EPBR) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 EPBR CAN bus messages and signals of the Right electric parking brake (EPBR) for firmware 2026.26.6.5: 7 messages, 868 signals with bit layout, scaling and value tables."
---

# Right electric parking brake (EPBR) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 7 messages of the Right electric parking brake (EPBR) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPBR_alertLog`](veh/epbr/epbr_alertlog.md) | VEH | 0x5A8 | 8 |  | 623 |
| [`EPBR_alertMatrix`](veh/epbr/epbr_alertmatrix.md) | VEH | 0x3E8 | 8 | 100 ms | 167 |
| [`EPBR_info`](veh/epbr/epbr_info.md) | VEH | 0x7E8 | 8 | 1000 ms | 15 |
| [`EPBR_internalStatus`](veh/epbr/epbr_internalstatus.md) | VEH | 0x228 | 8 | 100 ms | 19 |
| [`EPBR_seatStatus3`](veh/epbr/epbr_seatstatus3.md) | VEH | 0x2E6 | 7 | 1000 ms | 7 |
| [`EPBR_status`](veh/epbr/epbr_status.md) | VEH | 0x2E8 | 8 | 100 ms | 35 |
| [`EPBR_udsResponse`](veh/epbr/epbr_udsresponse.md) | VEH | 0x627 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

