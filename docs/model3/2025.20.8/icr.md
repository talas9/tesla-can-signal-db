---
layout: default
title: "ICR ECU (ICR) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 ICR CAN bus messages and signals of the ICR ECU (ICR) for firmware 2025.20.8: 8 messages, 124 signals with bit layout, scaling and value tables."
---

# ICR ECU (ICR) CAN messages and signals — Tesla Model 3 2025.20.8

All 8 messages of the ICR ECU (ICR) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ICR_info`](veh/icr/icr_info.md) | VEH | 0x3AD | 8 | 10000 ms | 9 |
| [`ICR_alertLog`](eth/icr/icr_alertlog.md) | ETH | 0x4B8 | 8 |  | 37 |
| [`ICR_alertMatrix`](eth/icr/icr_alertmatrix.md) | ETH | 0x7EA | 8 | 100 ms | 38 |
| [`ICR_intrusionDebug`](eth/icr/icr_intrusiondebug.md) | ETH | 0x2F8 | 7 | 100 ms | 5 |
| [`ICR_occupancy`](eth/icr/icr_occupancy.md) | ETH | 0x7E9 | 8 | 100 ms | 18 |
| [`ICR_occupancy2`](eth/icr/icr_occupancy2.md) | ETH | 0x29E | 8 | 100 ms | 9 |
| [`ICR_status`](eth/icr/icr_status.md) | ETH | 0x7E7 | 5 | 100 ms | 7 |
| [`ICR_udsResponse`](eth/icr/icr_udsresponse.md) | ETH | 0x658 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

