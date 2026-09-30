---
layout: default
title: "IDB ECU (IDB) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y IDB CAN bus messages and signals of the IDB ECU (IDB) for firmware 2025.20.8: 3 messages, 251 signals with bit layout, scaling and value tables."
---

# IDB ECU (IDB) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 3 messages of the IDB ECU (IDB) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`IDB_info`](ch/idb/idb_info.md) | CH | 0x33C | 8 | 10000 ms | 5 |
| [`IDB_alertLog`](eth/idb/idb_alertlog.md) | ETH | 0x5BE | 8 |  | 101 |
| [`IDB_alertMatrix`](eth/idb/idb_alertmatrix.md) | ETH | 0x3D7 | 8 | 1000 ms | 145 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

