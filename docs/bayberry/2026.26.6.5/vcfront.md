---
layout: default
title: "Front body controller (VCFRONT) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5"
description: "Tesla Model Y (2025+ / Juniper; community mapping) VCFRONT CAN bus messages and signals of the Front body controller (VCFRONT) for firmware 2026.26.6.5: 3 messages, 79 signals with bit layout, scaling and value tables."
---

# Front body controller (VCFRONT) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5

All 3 messages of the Front body controller (VCFRONT) documented for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2026.26.6.5, across the buses that carry them.

API name / codename: `Bayberry`. Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCFRONT_sensors`](veh/vcfront/vcfront_sensors.md) | VEH | 0x321 | 8 | 1000 ms | 11 |
| [`VCFRONT_systemStatus`](veh/vcfront/vcfront_systemstatus.md) | VEH | 0x545 | 8 | 33 ms | 34 |
| [`VCFRONT_vehicleStatus`](veh/vcfront/vcfront_vehiclestatus.md) | VEH | 0x3A1 | 8 | 50 ms | 34 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
