---
layout: default
title: "PMR ECU (PMR) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y PMR CAN bus messages and signals of the PMR ECU (PMR) for firmware 2025.20.8: 7 messages, 282 signals with bit layout, scaling and value tables."
---

# PMR ECU (PMR) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 7 messages of the PMR ECU (PMR) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PMR_info`](veh/pmr/pmr_info.md) | VEH | 0x6D4 | 8 | 1000 ms | 16 |
| [`PMR_mfgData`](party/pmr/pmr_mfgdata.md) | PARTY | 0x554 | 7 | 1000 ms | 4 |
| [`PMR_alertLog`](eth/pmr/pmr_alertlog.md) | ETH | 0x5A6 | 8 |  | 208 |
| [`PMR_alertMatrix1`](eth/pmr/pmr_alertmatrix1.md) | ETH | 0x386 | 8 | 1000 ms | 38 |
| [`PMR_alertMatrix2`](eth/pmr/pmr_alertmatrix2.md) | ETH | 0x3A0 | 8 | 1000 ms | 14 |
| [`PMR_state4`](eth/pmr/pmr_state4.md) | ETH | 0x1D8 | 8 | 10 ms | 1 |
| [`PMR_udsResponse`](eth/pmr/pmr_udsresponse.md) | ETH | 0x614 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

