---
layout: default
title: "PCS2 ECU (PCS2) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 PCS2 CAN bus messages and signals of the PCS2 ECU (PCS2) for firmware 2026.26.6.5: 4 messages, 737 signals with bit layout, scaling and value tables."
---

# PCS2 ECU (PCS2) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 4 messages of the PCS2 ECU (PCS2) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PCS2_alertLog`](veh/pcs2/pcs2_alertlog.md) | VEH | 0x444 | 8 |  | 510 |
| [`PCS2_alertMatrix`](veh/pcs2/pcs2_alertmatrix.md) | VEH | 0x3E4 | 8 | 1000 ms | 193 |
| [`PCS2_logging`](veh/pcs2/pcs2_logging.md) | VEH | 0x2E4 | 8 | 100 ms | 31 |
| [`PCS2_v2xInfo2`](veh/pcs2/pcs2_v2xinfo2.md) | VEH | 0x40F | 4 | 100 ms | 3 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

