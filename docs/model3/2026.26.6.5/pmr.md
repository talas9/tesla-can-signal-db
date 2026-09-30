---
layout: default
title: "PMR ECU (PMR) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 PMR CAN bus messages and signals of the PMR ECU (PMR) for firmware 2026.26.6.5: 5 messages, 306 signals with bit layout, scaling and value tables."
---

# PMR ECU (PMR) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 5 messages of the PMR ECU (PMR) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PMR_alertLog`](veh/pmr/pmr_alertlog.md) | VEH | 0x5A6 | 8 |  | 230 |
| [`PMR_alertMatrix`](veh/pmr/pmr_alertmatrix.md) | VEH | 0x386 | 8 | 1000 ms | 55 |
| [`PMR_info`](veh/pmr/pmr_info.md) | VEH | 0x6D4 | 8 | 1000 ms | 16 |
| [`PMR_udsResponse`](veh/pmr/pmr_udsresponse.md) | VEH | 0x614 | 8 |  | 1 |
| [`PMR_mfgData`](party/pmr/pmr_mfgdata.md) | PARTY | 0x554 | 7 | 1000 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

