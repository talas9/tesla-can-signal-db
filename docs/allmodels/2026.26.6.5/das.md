---
layout: default
title: "Driver assistance computer (DAS) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y DAS CAN bus messages and signals of the Driver assistance computer (DAS) for firmware 2026.26.6.5: 24 messages, 549 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (DAS) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 24 messages of the Driver assistance computer (DAS) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`DAS_autonomyControl`](veh/das/das_autonomycontrol.md) | VEH | 0x20E | 3 | 100 ms | 12 |
| [`DAS_bodyControls`](veh/das/das_bodycontrols.md) | VEH | 0x3E9 | 8 | 500 ms | 27 |
| [`DAS_alertLog`](ch/das/das_alertlog.md) | CH | 0x5B9 | 8 |  | 25 |
| [`DAS_autonomyDebugInfo`](ch/das/das_autonomydebuginfo.md) | CH | 0x191 | 2 | 100 ms | 3 |
| [`DAS_autopilotDebug`](ch/das/das_autopilotdebug.md) | CH | 0x247 | 8 | 100 ms | 14 |
| [`DAS_carLog`](ch/das/das_carlog.md) | CH | 0x5D9 | 8 | 333 ms | 29 |
| [`DAS_gpsStatus`](ch/das/das_gpsstatus.md) | CH | 0x3CA | 8 | 1000 ms | 48 |
| [`DAS_info`](ch/das/das_info.md) | CH | 0x539 | 8 | 1000 ms | 12 |
| [`DAS_lanes`](ch/das/das_lanes.md) | CH | 0x239 | 8 | 100 ms | 13 |
| [`DAS_status`](ch/das/das_status.md) | CH | 0x399 | 8 | 500 ms | 26 |
| [`DAS_status2`](ch/das/das_status2.md) | CH | 0x389 | 8 | 500 ms | 19 |
| [`DAS_udsResponse`](ch/das/das_udsresponse.md) | CH | 0x659 | 8 |  | 1 |
| [`DAS_visualDebug`](ch/das/das_visualdebug.md) | CH | 0x24A | 8 | 100 ms | 26 |
| [`DAS_warningMatrix0`](ch/das/das_warningmatrix0.md) | CH | 0x32A | 8 | 1000 ms | 63 |
| [`DAS_warningMatrix1`](ch/das/das_warningmatrix1.md) | CH | 0x36A | 8 | 1000 ms | 42 |
| [`DAS_warningMatrix2`](ch/das/das_warningmatrix2.md) | CH | 0x349 | 8 | 1000 ms | 26 |
| [`DAS_warningMatrix3`](ch/das/das_warningmatrix3.md) | CH | 0x43A | 8 | 1000 ms | 40 |
| [`DAS_autonomyControl`](party/das/das_autonomycontrol.md) | PARTY | 0x20E | 3 | 100 ms | 12 |
| [`DAS_autonomyUiControl`](party/das/das_autonomyuicontrol.md) | PARTY | 0x248 | 3 | 100 ms | 8 |
| [`DAS_control`](party/das/das_control.md) | PARTY | 0x2B9 | 8 | 40 ms | 9 |
| [`DAS_smartShift`](party/das/das_smartshift.md) | PARTY | 0x12B | 4 | 100 ms | 8 |
| [`DAS_object`](eth/das/das_object.md) | ETH | 0x30A | 8 | 30 ms | 50 |
| [`DAS_positioningEngineStatus`](eth/das/das_positioningenginestatus.md) | ETH | 0x30D | 8 | 250 ms | 25 |
| [`DAS_telemetryRadar`](eth/das/das_telemetryradar.md) | ETH | 0x60C | 8 | 5 ms | 11 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

