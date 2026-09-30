---
layout: default
title: "APSB ECU (APSB) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 APSB CAN bus messages and signals of the APSB ECU (APSB) for firmware 2026.26.6.5: 10 messages, 1001 signals with bit layout, scaling and value tables."
---

# APSB ECU (APSB) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 10 messages of the APSB ECU (APSB) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`APSB_alertLog`](eth/apsb/apsb_alertlog.md) | ETH | 0x5CA | 8 |  | 668 |
| [`APSB_eacMonitor`](eth/apsb/apsb_eacmonitor.md) | ETH | 0x2DB | 3 | 100 ms | 3 |
| [`APSB_powerStateInputs`](eth/apsb/apsb_powerstateinputs.md) | ETH | 0x3E0 | 3 | 100 ms | 6 |
| [`APSB_state`](eth/apsb/apsb_state.md) | ETH | 0x748 | 8 | 100 ms | 18 |
| [`APSB_status`](eth/apsb/apsb_status.md) | ETH | 0x3CB | 8 | 500 ms | 20 |
| [`APSB_warningMatrix0`](eth/apsb/apsb_warningmatrix0.md) | ETH | 0x34D | 8 | 1000 ms | 64 |
| [`APSB_warningMatrix1`](eth/apsb/apsb_warningmatrix1.md) | ETH | 0x477 | 8 | 1000 ms | 42 |
| [`APSB_warningMatrix2`](eth/apsb/apsb_warningmatrix2.md) | ETH | 0x3AE | 8 | 1000 ms | 58 |
| [`APSB_warningMatrix3`](eth/apsb/apsb_warningmatrix3.md) | ETH | 0x3D0 | 8 | 1000 ms | 59 |
| [`APSB_warningMatrix4`](eth/apsb/apsb_warningmatrix4.md) | ETH | 0x3EB | 8 | 1000 ms | 63 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

