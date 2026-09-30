---
layout: default
title: "PMF ECU (PMF) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y PMF CAN bus messages and signals of the PMF ECU (PMF) for firmware 2026.26.6.5: 5 messages, 285 signals with bit layout, scaling and value tables."
---

# PMF ECU (PMF) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 5 messages of the PMF ECU (PMF) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PMF_alertLog`](veh/pmf/pmf_alertlog.md) | VEH | 0x525 | 8 |  | 211 |
| [`PMF_alertMatrix`](veh/pmf/pmf_alertmatrix.md) | VEH | 0x304 | 8 | 1000 ms | 53 |
| [`PMF_info`](veh/pmf/pmf_info.md) | VEH | 0x316 | 8 | 1000 ms | 16 |
| [`PMF_udsResponse`](veh/pmf/pmf_udsresponse.md) | VEH | 0x654 | 8 |  | 1 |
| [`PMF_mfgData`](party/pmf/pmf_mfgdata.md) | PARTY | 0x524 | 7 | 1000 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

