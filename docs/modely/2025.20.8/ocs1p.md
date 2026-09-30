---
layout: default
title: "Occupant classification system (OCS1P) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y OCS1P CAN bus messages and signals of the Occupant classification system (OCS1P) for firmware 2025.20.8: 5 messages, 98 signals with bit layout, scaling and value tables."
---

# Occupant classification system (OCS1P) CAN messages and signals — Tesla Model Y 2025.20.8

All 5 messages of the Occupant classification system (OCS1P) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`OCS1P_alertLog`](eth/ocs1p/ocs1p_alertlog.md) | ETH | 0x595 | 8 |  | 22 |
| [`OCS1P_alertMatrix`](eth/ocs1p/ocs1p_alertmatrix.md) | ETH | 0x2FF | 8 | 100 ms | 34 |
| [`OCS1P_info`](eth/ocs1p/ocs1p_info.md) | ETH | 0x2FE | 8 | 1000 ms | 16 |
| [`OCS1P_status`](eth/ocs1p/ocs1p_status.md) | ETH | 0x303 | 8 | 500 ms | 25 |
| [`OCS1P_udsResponse`](eth/ocs1p/ocs1p_udsresponse.md) | ETH | 0x653 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

