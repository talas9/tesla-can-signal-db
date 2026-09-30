---
layout: default
title: "PMF ECU (PMF) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 PMF CAN bus messages and signals of the PMF ECU (PMF) for firmware 2025.20.8: 7 messages, 262 signals with bit layout, scaling and value tables."
---

# PMF ECU (PMF) CAN messages and signals — Tesla Model 3 2025.20.8

All 7 messages of the PMF ECU (PMF) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PMF_info`](veh/pmf/pmf_info.md) | VEH | 0x316 | 8 | 1000 ms | 16 |
| [`PMF_mfgData`](party/pmf/pmf_mfgdata.md) | PARTY | 0x524 | 7 | 1000 ms | 4 |
| [`PMF_alertLog`](eth/pmf/pmf_alertlog.md) | ETH | 0x525 | 8 |  | 189 |
| [`PMF_alertMatrix1`](eth/pmf/pmf_alertmatrix1.md) | ETH | 0x304 | 8 | 1000 ms | 38 |
| [`PMF_alertMatrix2`](eth/pmf/pmf_alertmatrix2.md) | ETH | 0x7E6 | 8 | 1000 ms | 13 |
| [`PMF_state4`](eth/pmf/pmf_state4.md) | ETH | 0x1D5 | 8 | 10 ms | 1 |
| [`PMF_udsResponse`](eth/pmf/pmf_udsresponse.md) | ETH | 0x654 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

