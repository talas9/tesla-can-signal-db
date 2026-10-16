---
layout: default
title: "Charge port controller (CP) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8"
description: "Tesla Model Y (2025+ / Juniper; community mapping) CP CAN bus messages and signals of the Charge port controller (CP) for firmware 2025.20.8: 4 messages, 55 signals with bit layout, scaling and value tables."
---

# Charge port controller (CP) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8

All 4 messages of the Charge port controller (CP) documented for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2025.20.8, across the buses that carry them.

API name / codename: `Bayberry`. Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CP_dcChargeStatus`](eth/cp/cp_dcchargestatus.md) | ETH | 0x29D | 4 | 100 ms | 3 |
| [`CP_loggingFast`](eth/cp/cp_loggingfast.md) | ETH | 0x75D | 8 | 200 ms | 23 |
| [`CP_loggingSlow`](eth/cp/cp_loggingslow.md) | ETH | 0x7FA | 8 | 1000 ms | 25 |
| [`CP_thermalStatus`](eth/cp/cp_thermalstatus.md) | ETH | 0x37D | 8 | 1000 ms | 4 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
