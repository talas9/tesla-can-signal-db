---
layout: default
title: "VCBATT1 ECU (VCBATT1) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y VCBATT1 CAN bus messages and signals of the VCBATT1 ECU (VCBATT1) for firmware 2026.26.6.5: 6 messages, 1179 signals with bit layout, scaling and value tables."
---

# VCBATT1 ECU (VCBATT1) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 6 messages of the VCBATT1 ECU (VCBATT1) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCBATT1_alertLog`](veh/vcbatt1/vcbatt1_alertlog.md) | VEH | 0x53B | 8 |  | 829 |
| [`VCBATT1_alertMatrix`](veh/vcbatt1/vcbatt1_alertmatrix.md) | VEH | 0x3CE | 8 | 100 ms | 255 |
| [`VCBATT1_eFuseDebugStatus`](veh/vcbatt1/vcbatt1_efusedebugstatus.md) | VEH | 0x406 | 7 | 200 ms | 37 |
| [`VCBATT1_LVBMS_statusHigh`](veh/vcbatt1/vcbatt1_lvbms_statushigh.md) | VEH | 0x742 | 8 | 40 ms | 30 |
| [`VCBATT1_LVSelfTests`](veh/vcbatt1/vcbatt1_lvselftests.md) | VEH | 0x45F | 8 | 500 ms | 27 |
| [`VCBATT1_udsResponse`](veh/vcbatt1/vcbatt1_udsresponse.md) | VEH | 0x60D | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

