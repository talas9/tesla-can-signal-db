---
layout: default
title: "Electric power steering (primary) (EPAS3P) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y EPAS3P CAN bus messages and signals of the Electric power steering (primary) (EPAS3P) for firmware 2026.26.6.5: 6 messages, 231 signals with bit layout, scaling and value tables."
---

# Electric power steering (primary) (EPAS3P) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 6 messages of the Electric power steering (primary) (EPAS3P) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPAS3P_alertLog`](party/epas3p/epas3p_alertlog.md) | PARTY | 0x592 | 8 |  | 35 |
| [`EPAS3P_alertMatrix`](party/epas3p/epas3p_alertmatrix.md) | PARTY | 0x392 | 8 | 1000 ms | 166 |
| [`EPAS3P_angleCalibration`](party/epas3p/epas3p_anglecalibration.md) | PARTY | 0x3D1 | 8 | 1000 ms | 6 |
| [`EPAS3P_info`](party/epas3p/epas3p_info.md) | PARTY | 0x331 | 8 | 1000 ms | 10 |
| [`EPAS3P_sysStatus`](party/epas3p/epas3p_sysstatus.md) | PARTY | 0x370 | 8 | 10 ms | 13 |
| [`EPAS3P_udsResponseCH`](eth/epas3p/epas3p_udsresponsech.md) | ETH | 0x638 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

