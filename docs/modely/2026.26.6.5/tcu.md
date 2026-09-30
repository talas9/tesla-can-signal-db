---
layout: default
title: "TCU ECU (TCU) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y TCU CAN bus messages and signals of the TCU ECU (TCU) for firmware 2026.26.6.5: 4 messages, 71 signals with bit layout, scaling and value tables."
---

# TCU ECU (TCU) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 4 messages of the TCU ECU (TCU) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`TCU_alertLog`](eth/tcu/tcu_alertlog.md) | ETH | 0x485 | 8 |  | 22 |
| [`TCU_alertMatrix1`](eth/tcu/tcu_alertmatrix1.md) | ETH | 0x486 | 8 | 1000 ms | 16 |
| [`TCU_log`](eth/tcu/tcu_log.md) | ETH | 0x483 | 8 | 1000 ms | 32 |
| [`TCU_SleepConfig`](eth/tcu/tcu_sleepconfig.md) | ETH | 0x487 | 1 | 1000 ms | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

