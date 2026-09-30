---
layout: default
title: "UMC ECU (UMC) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 UMC CAN bus messages and signals of the UMC ECU (UMC) for firmware 2025.20.8: 3 messages, 90 signals with bit layout, scaling and value tables."
---

# UMC ECU (UMC) CAN messages and signals — Tesla Model 3 2025.20.8

All 3 messages of the UMC ECU (UMC) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`UMC_smartAdapterInfo`](veh/umc/umc_smartadapterinfo.md) | VEH | 0x505 | 8 | 100 ms | 9 |
| [`UMC_alertLog`](eth/umc/umc_alertlog.md) | ETH | 0x5FD | 8 |  | 42 |
| [`UMC_alertMatrix1`](eth/umc/umc_alertmatrix1.md) | ETH | 0x338 | 8 | 1000 ms | 39 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

