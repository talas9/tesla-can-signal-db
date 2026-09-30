---
layout: default
title: "Audio amplifier (ADSP) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 ADSP CAN bus messages and signals of the Audio amplifier (ADSP) for firmware 2025.20.8: 4 messages, 124 signals with bit layout, scaling and value tables."
---

# Audio amplifier (ADSP) CAN messages and signals — Tesla Model 3 2025.20.8

All 4 messages of the Audio amplifier (ADSP) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ADSP_alertLog`](eth/adsp/adsp_alertlog.md) | ETH | 0x550 | 8 |  | 28 |
| [`ADSP_alertMatrix1`](eth/adsp/adsp_alertmatrix1.md) | ETH | 0x551 | 8 | 1000 ms | 60 |
| [`ADSP_alertMatrix2`](eth/adsp/adsp_alertmatrix2.md) | ETH | 0x552 | 8 | 1000 ms | 12 |
| [`ADSP_state`](eth/adsp/adsp_state.md) | ETH | 0x567 | 7 | 200 ms | 24 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

