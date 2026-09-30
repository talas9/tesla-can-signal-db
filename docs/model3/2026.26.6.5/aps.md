---
layout: default
title: "Driver assistance computer (secondary) (APS) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 APS CAN bus messages and signals of the Driver assistance computer (secondary) (APS) for firmware 2026.26.6.5: 13 messages, 1034 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (secondary) (APS) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 13 messages of the Driver assistance computer (secondary) (APS) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`APS_state`](veh/aps/aps_state.md) | VEH | 0x420 | 8 | 100 ms | 18 |
| [`APS_alertLog`](ch/aps/aps_alertlog.md) | CH | 0x5C9 | 8 |  | 668 |
| [`APS_eacMonitor`](ch/aps/aps_eacmonitor.md) | CH | 0x27D | 3 | 100 ms | 3 |
| [`APS_powerStateInputs`](ch/aps/aps_powerstateinputs.md) | CH | 0x3E0 | 3 | 100 ms | 6 |
| [`APS_state`](ch/aps/aps_state.md) | CH | 0x420 | 8 | 100 ms | 18 |
| [`APS_status`](ch/aps/aps_status.md) | CH | 0x3C9 | 8 | 500 ms | 23 |
| [`APS_status2`](ch/aps/aps_status2.md) | CH | 0x41C | 2 | 100 ms | 6 |
| [`APS_sysHealth`](ch/aps/aps_syshealth.md) | CH | 0x5E6 | 7 | 1000 ms | 6 |
| [`APS_warningMatrix0`](ch/aps/aps_warningmatrix0.md) | CH | 0x32B | 8 | 1000 ms | 64 |
| [`APS_warningMatrix1`](ch/aps/aps_warningmatrix1.md) | CH | 0x36C | 8 | 1000 ms | 42 |
| [`APS_warningMatrix2`](ch/aps/aps_warningmatrix2.md) | CH | 0x459 | 8 | 1000 ms | 58 |
| [`APS_warningMatrix3`](ch/aps/aps_warningmatrix3.md) | CH | 0x350 | 8 | 1000 ms | 59 |
| [`APS_warningMatrix4`](ch/aps/aps_warningmatrix4.md) | CH | 0x310 | 8 | 1000 ms | 63 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

