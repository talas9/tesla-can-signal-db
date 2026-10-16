---
layout: default
title: "Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8"
description: "Tesla Model Y (2025+ / Juniper; community mapping) VCSEC CAN bus messages and signals of the Vehicle security controller (VCSEC) for firmware 2025.20.8: 2 messages, 35 signals with bit layout, scaling and value tables."
---

# Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8

All 2 messages of the Vehicle security controller (VCSEC) documented for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2025.20.8, across the buses that carry them.

API name / codename: `Bayberry`. Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCSEC_TPMSConnectionData`](veh/vcsec/vcsec_tpmsconnectiondata.md) | VEH | 0x42A | 8 | 100 ms | 20 |
| [`VCSEC_debug100ms`](eth/vcsec/vcsec_debug100ms.md) | ETH | 0x719 | 8 | 50 ms | 15 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
