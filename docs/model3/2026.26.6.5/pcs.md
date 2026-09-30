---
layout: default
title: "Power conversion system (on-board charger and DC-DC converter) (PCS) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 PCS CAN bus messages and signals of the Power conversion system (on-board charger and DC-DC converter) (PCS) for firmware 2026.26.6.5: 10 messages, 583 signals with bit layout, scaling and value tables."
---

# Power conversion system (on-board charger and DC-DC converter) (PCS) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 10 messages of the Power conversion system (on-board charger and DC-DC converter) (PCS) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PCS_alertLog`](veh/pcs/pcs_alertlog.md) | VEH | 0x424 | 8 |  | 300 |
| [`PCS_alertMatrix`](veh/pcs/pcs_alertmatrix.md) | VEH | 0x3A4 | 8 | 1000 ms | 117 |
| [`PCS_chgLineStatus`](veh/pcs/pcs_chglinestatus.md) | VEH | 0x264 | 6 | 100 ms | 5 |
| [`PCS_chgStatus`](veh/pcs/pcs_chgstatus.md) | VEH | 0x204 | 8 | 100 ms | 17 |
| [`PCS_dcdcRailStatus`](veh/pcs/pcs_dcdcrailstatus.md) | VEH | 0x2B4 | 6 | 100 ms | 3 |
| [`PCS_dcdcStatus`](veh/pcs/pcs_dcdcstatus.md) | VEH | 0x224 | 8 | 100 ms | 19 |
| [`PCS_info`](veh/pcs/pcs_info.md) | VEH | 0x3C4 | 8 | 1000 ms | 16 |
| [`PCS_logging`](veh/pcs/pcs_logging.md) | VEH | 0x2C4 | 8 | 1000 ms | 99 |
| [`PCS_thermalStatus`](veh/pcs/pcs_thermalstatus.md) | VEH | 0x2A4 | 8 | 1000 ms | 6 |
| [`PCS_udsResponse`](veh/pcs/pcs_udsresponse.md) | VEH | 0x629 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

