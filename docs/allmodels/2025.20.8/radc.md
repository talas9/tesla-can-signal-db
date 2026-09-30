---
layout: default
title: "Radar (RADC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y RADC CAN bus messages and signals of the Radar (RADC) for firmware 2025.20.8: 4 messages, 159 signals with bit layout, scaling and value tables."
---

# Radar (RADC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 4 messages of the Radar (RADC) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`RADC_alertLog`](ch/radc/radc_alertlog.md) | CH | 0x555 | 8 |  | 86 |
| [`RADC_alertMatrix0`](ch/radc/radc_alertmatrix0.md) | CH | 0x502 | 8 | 1000 ms | 55 |
| [`RADC_info`](ch/radc/radc_info.md) | CH | 0x531 | 8 | 1000 ms | 17 |
| [`RADC_udsResponse`](eth/radc/radc_udsresponse.md) | ETH | 0x681 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

