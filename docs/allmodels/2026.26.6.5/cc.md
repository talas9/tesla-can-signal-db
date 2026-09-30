---
layout: default
title: "Charge cable controller (CC) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y CC CAN bus messages and signals of the Charge cable controller (CC) for firmware 2026.26.6.5: 5 messages, 150 signals with bit layout, scaling and value tables."
---

# Charge cable controller (CC) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 5 messages of the Charge cable controller (CC) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CC_alertLog`](veh/cc/cc_alertlog.md) | VEH | 0x45C | 8 |  | 62 |
| [`CC_alertMatrix1`](veh/cc/cc_alertmatrix1.md) | VEH | 0x46C | 8 | 1000 ms | 55 |
| [`CC_chgStatus`](veh/cc/cc_chgstatus.md) | VEH | 0x31C | 8 | 100 ms | 10 |
| [`CC_chgStatus2`](veh/cc/cc_chgstatus2.md) | VEH | 0x31D | 8 | 100 ms | 5 |
| [`CC_logData`](veh/cc/cc_logdata.md) | VEH | 0x32C | 8 | 1000 ms | 18 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

