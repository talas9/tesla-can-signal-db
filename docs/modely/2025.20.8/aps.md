---
layout: default
title: "Driver assistance computer (secondary) (APS) CAN messages and signals — Tesla Model Y 2025.20.8"
description: "Tesla Model Y APS CAN bus messages and signals of the Driver assistance computer (secondary) (APS) for firmware 2025.20.8: 11 messages, 892 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (secondary) (APS) CAN messages and signals — Tesla Model Y 2025.20.8

All 11 messages of the Driver assistance computer (secondary) (APS) documented for Tesla Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`APS_eacMonitor`](ch/aps/aps_eacmonitor.md) | CH | 0x27D | 3 | 100 ms | 3 |
| [`APS_powerStateInputs`](ch/aps/aps_powerstateinputs.md) | CH | 0x3E0 | 3 | 100 ms | 6 |
| [`APS_sysHealth`](ch/aps/aps_syshealth.md) | CH | 0x5E6 | 7 | 1000 ms | 6 |
| [`APS_warningMatrix0`](ch/aps/aps_warningmatrix0.md) | CH | 0x32B | 8 | 1000 ms | 64 |
| [`APS_warningMatrix1`](ch/aps/aps_warningmatrix1.md) | CH | 0x36C | 8 | 1000 ms | 42 |
| [`APS_warningMatrix2`](ch/aps/aps_warningmatrix2.md) | CH | 0x459 | 8 | 1000 ms | 58 |
| [`APS_warningMatrix3`](ch/aps/aps_warningmatrix3.md) | CH | 0x350 | 8 | 1000 ms | 59 |
| [`APS_alertLog`](eth/aps/aps_alertlog.md) | ETH | 0x5C9 | 8 |  | 586 |
| [`APS_state`](eth/aps/aps_state.md) | ETH | 0x7FC | 7 | 100 ms | 14 |
| [`APS_status`](eth/aps/aps_status.md) | ETH | 0x3CA | 8 | 500 ms | 21 |
| [`APS_warningMatrix4`](eth/aps/aps_warningmatrix4.md) | ETH | 0x310 | 8 | 1000 ms | 33 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

