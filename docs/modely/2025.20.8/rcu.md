---
layout: default
title: "RCU ECU (RCU) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y RCU CAN bus messages and signals of the RCU ECU (RCU) for firmware 2025.20.8: 3 messages, 79 signals with bit layout, scaling and value tables."
---

# RCU ECU (RCU) CAN messages and signals — Tesla Model Y 2025.20.8

All 3 messages of the RCU ECU (RCU) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`RCU_info`](ch/rcu/rcu_info.md) | CH | 0x33F | 8 | 10000 ms | 5 |
| [`RCU_alertLog`](eth/rcu/rcu_alertlog.md) | ETH | 0x5BF | 8 |  | 15 |
| [`RCU_alertMatrix`](eth/rcu/rcu_alertmatrix.md) | ETH | 0x3E6 | 8 | 1000 ms | 59 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

