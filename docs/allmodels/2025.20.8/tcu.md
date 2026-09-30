---
layout: default
title: "TCU ECU (TCU) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y TCU CAN bus messages and signals of the TCU ECU (TCU) for firmware 2025.20.8: 4 messages, 34 signals with bit layout, scaling and value tables."
---

# TCU ECU (TCU) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 4 messages of the TCU ECU (TCU) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`TCU_alertLog`](eth/tcu/tcu_alertlog.md) | ETH | 0x582 | 8 |  | 7 |
| [`TCU_alertMatrix1`](eth/tcu/tcu_alertmatrix1.md) | ETH | 0x5C0 | 8 | 1000 ms | 6 |
| [`TCU_log`](eth/tcu/tcu_log.md) | ETH | 0x581 | 8 | 1000 ms | 17 |
| [`TCU_status`](eth/tcu/tcu_status.md) | ETH | 0x580 | 8 | 1000 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

