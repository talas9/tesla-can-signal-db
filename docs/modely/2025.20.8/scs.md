---
layout: default
title: "SCS ECU (SCS) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y SCS CAN bus messages and signals of the SCS ECU (SCS) for firmware 2025.20.8: 3 messages, 131 signals with bit layout, scaling and value tables."
---

# SCS ECU (SCS) CAN messages and signals — Tesla Model Y 2025.20.8

All 3 messages of the SCS ECU (SCS) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`SCS_alertLog`](veh/scs/scs_alertlog.md) | VEH | 0x54A | 8 |  | 5 |
| [`SCS_alertMatrix1`](veh/scs/scs_alertmatrix1.md) | VEH | 0x365 | 8 | 1000 ms | 62 |
| [`SCS_alertMatrix2`](veh/scs/scs_alertmatrix2.md) | VEH | 0x370 | 8 | 1000 ms | 64 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

