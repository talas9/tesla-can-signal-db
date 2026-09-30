---
layout: default
title: "Electric brake booster (IBST) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y IBST CAN bus messages and signals of the Electric brake booster (IBST) for firmware 2025.20.8: 4 messages, 255 signals with bit layout, scaling and value tables."
---

# Electric brake booster (IBST) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 4 messages of the Electric brake booster (IBST) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`IBST_info`](ch/ibst/ibst_info.md) | CH | 0x32D | 8 | 10000 ms | 11 |
| [`IBST_status`](party/ibst/ibst_status.md) | PARTY | 0x39D | 5 | 40 ms | 7 |
| [`IBST_alertMatrix`](eth/ibst/ibst_alertmatrix.md) | ETH | 0x35D | 8 | 1000 ms | 236 |
| [`IBST_udsResponse`](eth/ibst/ibst_udsresponse.md) | ETH | 0x65D | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

