---
layout: default
title: "Power conversion system (on-board charger and DC-DC converter) (PCS) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 PCS CAN bus messages and signals of the Power conversion system (on-board charger and DC-DC converter) (PCS) for firmware 2025.20.8: 10 messages, 593 signals with bit layout, scaling and value tables."
---

# Power conversion system (on-board charger and DC-DC converter) (PCS) CAN messages and signals — Tesla Model 3 2025.20.8

All 10 messages of the Power conversion system (on-board charger and DC-DC converter) (PCS) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PCS_chgLineStatus`](veh/pcs/pcs_chglinestatus.md) | VEH | 0x264 | 6 | 100 ms | 5 |
| [`PCS_dcdcRailStatus`](veh/pcs/pcs_dcdcrailstatus.md) | VEH | 0x2B4 | 6 | 100 ms | 3 |
| [`PCS_info`](veh/pcs/pcs_info.md) | VEH | 0x3C4 | 8 | 1000 ms | 16 |
| [`PCS_thermalStatus`](veh/pcs/pcs_thermalstatus.md) | VEH | 0x2A4 | 8 | 1000 ms | 6 |
| [`PCS_alertLog`](eth/pcs/pcs_alertlog.md) | ETH | 0x424 | 8 |  | 321 |
| [`PCS_alertMatrix`](eth/pcs/pcs_alertmatrix.md) | ETH | 0x3A4 | 8 | 1000 ms | 110 |
| [`PCS_chgStatus`](eth/pcs/pcs_chgstatus.md) | ETH | 0x204 | 8 | 100 ms | 16 |
| [`PCS_dcdcStatus`](eth/pcs/pcs_dcdcstatus.md) | ETH | 0x224 | 8 | 100 ms | 18 |
| [`PCS_logging`](eth/pcs/pcs_logging.md) | ETH | 0x2C4 | 8 | 1000 ms | 97 |
| [`PCS_udsResponse`](eth/pcs/pcs_udsresponse.md) | ETH | 0x629 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

