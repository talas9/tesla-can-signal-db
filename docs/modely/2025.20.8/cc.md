---
layout: default
title: "Charge cable controller (CC) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y CC CAN bus messages and signals of the Charge cable controller (CC) for firmware 2025.20.8: 5 messages, 147 signals with bit layout, scaling and value tables."
---

# Charge cable controller (CC) CAN messages and signals — Tesla Model Y 2025.20.8

All 5 messages of the Charge cable controller (CC) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CC_alertLog`](veh/cc/cc_alertlog.md) | VEH | 0x45C | 8 |  | 62 |
| [`CC_alertMatrix1`](veh/cc/cc_alertmatrix1.md) | VEH | 0x46C | 8 | 1000 ms | 55 |
| [`CC_chgStatus`](veh/cc/cc_chgstatus.md) | VEH | 0x31C | 8 | 100 ms | 10 |
| [`CC_logData`](veh/cc/cc_logdata.md) | VEH | 0x32C | 8 | 1000 ms | 18 |
| [`CC_chgStatus2`](eth/cc/cc_chgstatus2.md) | ETH | 0x31D | 8 | 100 ms | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

