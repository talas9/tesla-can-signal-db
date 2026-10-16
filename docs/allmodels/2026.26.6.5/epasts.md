---
layout: default
title: "EPASTS ECU (EPASTS) CAN messages and signals — Tesla Model 3 / Model Y (union) 2026.26.6.5"
description: "Tesla Model 3 / Model Y (union) EPASTS CAN bus messages and signals of the EPASTS ECU (EPASTS) for firmware 2026.26.6.5: 2 messages, 547 signals with bit layout, scaling and value tables."
---

# EPASTS ECU (EPASTS) CAN messages and signals — Tesla Model 3 / Model Y (union) 2026.26.6.5

All 2 messages of the EPASTS ECU (EPASTS) documented for Tesla Model 3 / Model Y (union) firmware 2026.26.6.5, across the buses that carry them.

API name / codename: `AllModels`. Combined Model3/ModelY dataset; ETH includes messages without known CAN routes, not every Tesla model or variant.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPASTS_alertLog`](ch/epasts/epasts_alertlog.md) | CH | 0x594 | 8 |  | 276 |
| [`EPASTS_alertMatrix`](ch/epasts/epasts_alertmatrix.md) | CH | 0x398 | 8 | 1000 ms | 271 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)
