---
layout: default
title: "Electric power steering (secondary) (EPAS3S) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 EPAS3S CAN bus messages and signals of the Electric power steering (secondary) (EPAS3S) for firmware 2025.20.8: 6 messages, 206 signals with bit layout, scaling and value tables."
---

# Electric power steering (secondary) (EPAS3S) CAN messages and signals — Tesla Model 3 2025.20.8

All 6 messages of the Electric power steering (secondary) (EPAS3S) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`EPAS3S_angleCalibration`](ch/epas3s/epas3s_anglecalibration.md) | CH | 0x3D1 | 8 | 1000 ms | 6 |
| [`EPAS3S_info`](ch/epas3s/epas3s_info.md) | CH | 0x311 | 8 | 1000 ms | 10 |
| [`EPAS3S_alertLog`](eth/epas3s/epas3s_alertlog.md) | ETH | 0x591 | 8 |  | 25 |
| [`EPAS3S_alertMatrix`](eth/epas3s/epas3s_alertmatrix.md) | ETH | 0x391 | 8 | 1000 ms | 151 |
| [`EPAS3S_sysStatus`](eth/epas3s/epas3s_sysstatus.md) | ETH | 0x372 | 8 | 10 ms | 13 |
| [`EPAS3S_udsResponse`](eth/epas3s/epas3s_udsresponse.md) | ETH | 0x738 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

