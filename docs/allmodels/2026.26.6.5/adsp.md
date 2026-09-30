---
layout: default
title: "Audio amplifier (ADSP) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y ADSP CAN bus messages and signals of the Audio amplifier (ADSP) for firmware 2026.26.6.5: 5 messages, 140 signals with bit layout, scaling and value tables."
---

# Audio amplifier (ADSP) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 5 messages of the Audio amplifier (ADSP) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`ADSP_audioVisualizer`](veh/adsp/adsp_audiovisualizer.md) | VEH | 0x79F | 1 | 20 ms | 1 |
| [`ADSP_state`](ch/adsp/adsp_state.md) | CH | 0x567 | 8 | 200 ms | 26 |
| [`ADSP_alertLog`](eth/adsp/adsp_alertlog.md) | ETH | 0x550 | 8 |  | 37 |
| [`ADSP_alertMatrix1`](eth/adsp/adsp_alertmatrix1.md) | ETH | 0x551 | 8 | 1000 ms | 60 |
| [`ADSP_alertMatrix2`](eth/adsp/adsp_alertmatrix2.md) | ETH | 0x552 | 8 | 1000 ms | 16 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

