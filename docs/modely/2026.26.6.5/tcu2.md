---
layout: default
title: "TCU2 ECU (TCU2) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y TCU2 CAN bus messages and signals of the TCU2 ECU (TCU2) for firmware 2026.26.6.5: 4 messages, 71 signals with bit layout, scaling and value tables."
---

# TCU2 ECU (TCU2) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 4 messages of the TCU2 ECU (TCU2) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`TCU2_alertLog`](eth/tcu2/tcu2_alertlog.md) | ETH | 0x585 | 8 |  | 22 |
| [`TCU2_alertMatrix1`](eth/tcu2/tcu2_alertmatrix1.md) | ETH | 0x586 | 8 | 1000 ms | 16 |
| [`TCU2_log`](eth/tcu2/tcu2_log.md) | ETH | 0x584 | 8 | 1000 ms | 32 |
| [`TCU2_SleepConfig`](eth/tcu2/tcu2_sleepconfig.md) | ETH | 0x587 | 1 | 1000 ms | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

