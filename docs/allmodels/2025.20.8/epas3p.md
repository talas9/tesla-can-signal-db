---
layout: default
title: "Electric power steering (primary) (EPAS3P) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y EPAS3P CAN bus messages and signals of the Electric power steering (primary) (EPAS3P) for firmware 2025.20.8: 6 messages, 206 signals with bit layout, scaling and value tables."
---

# Electric power steering (primary) (EPAS3P) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 6 messages of the Electric power steering (primary) (EPAS3P) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPAS3P_angleCalibration`](party/epas3p/epas3p_anglecalibration.md) | PARTY | 0x3D1 | 8 | 1000 ms | 6 |
| [`EPAS3P_info`](party/epas3p/epas3p_info.md) | PARTY | 0x331 | 8 | 1000 ms | 10 |
| [`EPAS3P_alertLog`](eth/epas3p/epas3p_alertlog.md) | ETH | 0x592 | 8 |  | 25 |
| [`EPAS3P_alertMatrix`](eth/epas3p/epas3p_alertmatrix.md) | ETH | 0x7F4 | 8 | 1000 ms | 151 |
| [`EPAS3P_sysStatus`](eth/epas3p/epas3p_sysstatus.md) | ETH | 0x373 | 8 | 10 ms | 13 |
| [`EPAS3P_udsResponseCH`](eth/epas3p/epas3p_udsresponsech.md) | ETH | 0x638 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

