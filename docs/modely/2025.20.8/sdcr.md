---
layout: default
title: "SDCR ECU (SDCR) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y SDCR CAN bus messages and signals of the SDCR ECU (SDCR) for firmware 2025.20.8: 4 messages, 171 signals with bit layout, scaling and value tables."
---

# SDCR ECU (SDCR) CAN messages and signals — Tesla Model Y 2025.20.8

All 4 messages of the SDCR ECU (SDCR) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`SDCR_alertMatrix`](veh/sdcr/sdcr_alertmatrix.md) | VEH | 0x5BB | 8 | 1000 ms | 35 |
| [`SDCR_info`](veh/sdcr/sdcr_info.md) | VEH | 0x63D | 8 | 1000 ms | 11 |
| [`SDCR_alertLog`](eth/sdcr/sdcr_alertlog.md) | ETH | 0x5FB | 8 |  | 124 |
| [`SDCR_udsResponse`](eth/sdcr/sdcr_udsresponse.md) | ETH | 0x6FB | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

