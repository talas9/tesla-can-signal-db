---
layout: default
title: "Charge port controller (CP) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y CP CAN bus messages and signals of the Charge port controller (CP) for firmware 2026.26.6.5: 13 messages, 691 signals with bit layout, scaling and value tables."
---

# Charge port controller (CP) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 13 messages of the Charge port controller (CP) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CP_alertLog`](veh/cp/cp_alertlog.md) | VEH | 0x50E | 8 |  | 323 |
| [`CP_alertMatrix`](veh/cp/cp_alertmatrix.md) | VEH | 0x31E | 8 | 1000 ms | 218 |
| [`CP_chargeStatus`](veh/cp/cp_chargestatus.md) | VEH | 0x13D | 6 | 100 ms | 13 |
| [`CP_dcChargeStatus`](veh/cp/cp_dcchargestatus.md) | VEH | 0x29D | 5 | 100 ms | 5 |
| [`CP_evseStatus`](veh/cp/cp_evsestatus.md) | VEH | 0x21D | 8 | 100 ms | 18 |
| [`CP_gridFormControl`](veh/cp/cp_gridformcontrol.md) | VEH | 0x2DD | 6 | 1000 ms | 7 |
| [`CP_info`](veh/cp/cp_info.md) | VEH | 0x53E | 8 | 1000 ms | 15 |
| [`CP_IsoTpPipeToPncd`](veh/cp/cp_isotppipetopncd.md) | VEH | 0x6E7 | 8 |  | 1 |
| [`CP_loggingFast`](veh/cp/cp_loggingfast.md) | VEH | 0x75D | 8 | 200 ms | 26 |
| [`CP_loggingSlow`](veh/cp/cp_loggingslow.md) | VEH | 0x3DD | 8 | 1000 ms | 33 |
| [`CP_status`](veh/cp/cp_status.md) | VEH | 0x25D | 8 | 100 ms | 26 |
| [`CP_thermalStatus`](veh/cp/cp_thermalstatus.md) | VEH | 0x37D | 8 | 1000 ms | 5 |
| [`CP_udsResponse`](veh/cp/cp_udsresponse.md) | VEH | 0x61E | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

