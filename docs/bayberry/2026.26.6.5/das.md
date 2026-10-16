---
layout: default
title: "Driver assistance computer (DAS) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5"
description: "Tesla Model Y (2025+ / Juniper; community mapping) DAS CAN bus messages and signals of the Driver assistance computer (DAS) for firmware 2026.26.6.5: 2 messages, 9 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (DAS) CAN messages and signals — Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5

All 2 messages of the Driver assistance computer (DAS) documented for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2026.26.6.5, across the buses that carry them.

API name / codename: `Bayberry`. Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DAS_autonomyDebugInfo`](ch/das/das_autonomydebuginfo.md) | CH | 0x191 | 2 | 100 ms | 1 |
| [`DAS_autonomyUiControl`](party/das/das_autonomyuicontrol.md) | PARTY | 0x248 | 3 | 100 ms | 8 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
