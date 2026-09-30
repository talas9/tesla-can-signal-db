---
layout: default
title: "Driver assistance computer (DAS) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 DAS CAN bus messages and signals of the Driver assistance computer (DAS) for firmware 2025.20.8: 19 messages, 493 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (DAS) CAN messages and signals — Tesla Model 3 2025.20.8

All 19 messages of the Driver assistance computer (DAS) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DAS_bodyControls`](veh/das/das_bodycontrols.md) | VEH | 0x3E9 | 8 | 500 ms | 27 |
| [`DAS_alertLog`](ch/das/das_alertlog.md) | CH | 0x5B9 | 8 |  | 25 |
| [`DAS_carLog`](ch/das/das_carlog.md) | CH | 0x5D9 | 8 | 333 ms | 29 |
| [`DAS_info`](ch/das/das_info.md) | CH | 0x539 | 8 | 1000 ms | 12 |
| [`DAS_lanes`](ch/das/das_lanes.md) | CH | 0x239 | 8 | 100 ms | 13 |
| [`DAS_status`](ch/das/das_status.md) | CH | 0x399 | 8 | 500 ms | 26 |
| [`DAS_status2`](ch/das/das_status2.md) | CH | 0x389 | 8 | 500 ms | 19 |
| [`DAS_visualDebug`](ch/das/das_visualdebug.md) | CH | 0x24A | 8 | 100 ms | 26 |
| [`DAS_warningMatrix0`](ch/das/das_warningmatrix0.md) | CH | 0x32A | 8 | 1000 ms | 63 |
| [`DAS_warningMatrix1`](ch/das/das_warningmatrix1.md) | CH | 0x36A | 8 | 1000 ms | 42 |
| [`DAS_warningMatrix2`](ch/das/das_warningmatrix2.md) | CH | 0x349 | 8 | 1000 ms | 26 |
| [`DAS_warningMatrix3`](ch/das/das_warningmatrix3.md) | CH | 0x43A | 8 | 1000 ms | 40 |
| [`DAS_control`](party/das/das_control.md) | PARTY | 0x2B9 | 8 | 40 ms | 9 |
| [`DAS_smartShift`](party/das/das_smartshift.md) | PARTY | 0x12B | 4 | 100 ms | 8 |
| [`DAS_autopilotDebug`](eth/das/das_autopilotdebug.md) | ETH | 0x247 | 8 | 100 ms | 14 |
| [`DAS_gpsStatus`](eth/das/das_gpsstatus.md) | ETH | 0x7F9 | 8 | 1000 ms | 52 |
| [`DAS_object`](eth/das/das_object.md) | ETH | 0x309 | 8 | 30 ms | 50 |
| [`DAS_telemetryRadar`](eth/das/das_telemetryradar.md) | ETH | 0x60C | 8 | 5 ms | 11 |
| [`DAS_udsResponse`](eth/das/das_udsresponse.md) | ETH | 0x659 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

