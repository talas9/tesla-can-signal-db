---
layout: default
title: "Right electric parking brake (EPBR) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y EPBR CAN bus messages and signals of the Right electric parking brake (EPBR) for firmware 2025.20.8: 7 messages, 867 signals with bit layout, scaling and value tables."
---

# Right electric parking brake (EPBR) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 7 messages of the Right electric parking brake (EPBR) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPBR_info`](veh/epbr/epbr_info.md) | VEH | 0x7E8 | 8 | 1000 ms | 15 |
| [`EPBR_internalStatus`](veh/epbr/epbr_internalstatus.md) | VEH | 0x228 | 8 | 100 ms | 19 |
| [`EPBR_alertLog`](eth/epbr/epbr_alertlog.md) | ETH | 0x5A8 | 8 |  | 628 |
| [`EPBR_alertMatrix`](eth/epbr/epbr_alertmatrix.md) | ETH | 0x3E8 | 8 | 100 ms | 163 |
| [`EPBR_seatStatus3`](eth/epbr/epbr_seatstatus3.md) | ETH | 0x2E6 | 5 | 1000 ms | 6 |
| [`EPBR_status`](eth/epbr/epbr_status.md) | ETH | 0x2E8 | 8 | 100 ms | 34 |
| [`EPBR_udsResponse`](eth/epbr/epbr_udsresponse.md) | ETH | 0x627 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

