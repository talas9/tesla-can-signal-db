---
layout: default
title: "Charge port controller (CP) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5"
description: "Tesla Model Y (2025+ / Juniper; community mapping) CP CAN bus messages and signals of the Charge port controller (CP) for firmware 2026.26.6.5: 4 messages, 70 signals with bit layout, scaling and value tables."
---

# Charge port controller (CP) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5

All 4 messages of the Charge port controller (CP) documented for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2026.26.6.5, across the buses that carry them.

API name / codename: `Bayberry`. Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CP_dcChargeStatus`](veh/cp/cp_dcchargestatus.md) | VEH | 0x29D | 5 | 100 ms | 5 |
| [`CP_loggingFast`](veh/cp/cp_loggingfast.md) | VEH | 0x75D | 8 | 200 ms | 26 |
| [`CP_loggingSlow`](veh/cp/cp_loggingslow.md) | VEH | 0x3DD | 8 | 1000 ms | 33 |
| [`CP_thermalStatus`](veh/cp/cp_thermalstatus.md) | VEH | 0x37D | 8 | 1000 ms | 6 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
