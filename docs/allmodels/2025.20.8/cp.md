---
layout: default
title: "Charge port controller (CP) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y CP CAN bus messages and signals of the Charge port controller (CP) for firmware 2025.20.8: 12 messages, 612 signals with bit layout, scaling and value tables."
---

# Charge port controller (CP) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 12 messages of the Charge port controller (CP) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CP_info`](veh/cp/cp_info.md) | VEH | 0x53E | 8 | 1000 ms | 15 |
| [`CP_IsoTpPipeToPncd`](veh/cp/cp_isotppipetopncd.md) | VEH | 0x6E7 | 8 |  | 1 |
| [`CP_alertLog`](eth/cp/cp_alertlog.md) | ETH | 0x50E | 8 |  | 310 |
| [`CP_alertMatrix`](eth/cp/cp_alertmatrix.md) | ETH | 0x31E | 8 | 1000 ms | 180 |
| [`CP_chargeStatusLog`](eth/cp/cp_chargestatuslog.md) | ETH | 0x43D | 6 | 100 ms | 9 |
| [`CP_dcChargeStatus`](eth/cp/cp_dcchargestatus.md) | ETH | 0x29D | 4 | 100 ms | 3 |
| [`CP_evseStatus`](eth/cp/cp_evsestatus.md) | ETH | 0x21D | 8 | 100 ms | 18 |
| [`CP_loggingFast`](eth/cp/cp_loggingfast.md) | ETH | 0x75D | 8 | 200 ms | 24 |
| [`CP_loggingSlow`](eth/cp/cp_loggingslow.md) | ETH | 0x7FA | 8 | 1000 ms | 25 |
| [`CP_status`](eth/cp/cp_status.md) | ETH | 0x210 | 8 | 100 ms | 22 |
| [`CP_thermalStatus`](eth/cp/cp_thermalstatus.md) | ETH | 0x37D | 8 | 1000 ms | 4 |
| [`CP_udsResponse`](eth/cp/cp_udsresponse.md) | ETH | 0x61E | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

