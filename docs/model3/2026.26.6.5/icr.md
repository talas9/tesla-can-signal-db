---
layout: default
title: "ICR ECU (ICR) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 ICR CAN bus messages and signals of the ICR ECU (ICR) for firmware 2026.26.6.5: 8 messages, 137 signals with bit layout, scaling and value tables."
---

# ICR ECU (ICR) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 8 messages of the ICR ECU (ICR) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ICR_alertLog`](veh/icr/icr_alertlog.md) | VEH | 0x4B8 | 8 |  | 40 |
| [`ICR_alertMatrix`](veh/icr/icr_alertmatrix.md) | VEH | 0x3B8 | 8 | 100 ms | 40 |
| [`ICR_info`](veh/icr/icr_info.md) | VEH | 0x3AD | 8 | 10000 ms | 9 |
| [`ICR_nonLocalizedOccupancy`](veh/icr/icr_nonlocalizedoccupancy.md) | VEH | 0x29B | 5 | 100 ms | 11 |
| [`ICR_occupancy`](veh/icr/icr_occupancy.md) | VEH | 0x218 | 5 | 100 ms | 12 |
| [`ICR_occupancy2`](veh/icr/icr_occupancy2.md) | VEH | 0x29E | 8 | 100 ms | 16 |
| [`ICR_status`](veh/icr/icr_status.md) | VEH | 0x298 | 4 | 100 ms | 8 |
| [`ICR_udsResponse`](veh/icr/icr_udsresponse.md) | VEH | 0x658 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

