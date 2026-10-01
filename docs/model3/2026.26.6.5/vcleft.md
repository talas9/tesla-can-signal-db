---
layout: default
title: "Left body controller (VCLEFT) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 VCLEFT CAN bus messages and signals of the Left body controller (VCLEFT) for firmware 2026.26.6.5: 30 messages, 2449 signals with bit layout, scaling and value tables."
---

# Left body controller (VCLEFT) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 30 messages of the Left body controller (VCLEFT) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCLEFT_alertLog`](veh/vcleft/vcleft_alertlog.md) | VEH | 0x55D | 8 |  | 1427 |
| [`VCLEFT_alertMatrix`](veh/vcleft/vcleft_alertmatrix.md) | VEH | 0x360 | 8 | 100 ms | 470 |
| [`VCLEFT_doorStatus`](veh/vcleft/vcleft_doorstatus.md) | VEH | 0x102 | 8 | 100 ms | 25 |
| [`VCLEFT_doorStatus2`](veh/vcleft/vcleft_doorstatus2.md) | VEH | 0x122 | 8 | 100 ms | 14 |
| [`VCLEFT_epbmDebug`](veh/vcleft/vcleft_epbmdebug.md) | VEH | 0x272 | 8 | 100 ms | 14 |
| [`VCLEFT_etcBluetoothStatus`](veh/vcleft/vcleft_etcbluetoothstatus.md) | VEH | 0x4A2 | 1 | 1000 ms | 1 |
| [`VCLEFT_hvacBlowerFeedback`](veh/vcleft/vcleft_hvacblowerfeedback.md) | VEH | 0x282 | 8 | 100 ms | 13 |
| [`VCLEFT_info`](veh/vcleft/vcleft_info.md) | VEH | 0x302 | 8 | 1000 ms | 16 |
| [`VCLEFT_liftgateLeaderRequest`](veh/vcleft/vcleft_liftgateleaderrequest.md) | VEH | 0x124 | 8 | 500 ms | 11 |
| [`VCLEFT_liftgateStatus`](veh/vcleft/vcleft_liftgatestatus.md) | VEH | 0x142 | 8 | 50 ms | 22 |
| [`VCLEFT_lightStatus`](veh/vcleft/vcleft_lightstatus.md) | VEH | 0x3E2 | 7 | 200 ms | 27 |
| [`VCLEFT_logging0point1Hz`](veh/vcleft/vcleft_logging0point1hz.md) | VEH | 0x70A | 5 | 10000 ms | 6 |
| [`VCLEFT_logging10Hz`](veh/vcleft/vcleft_logging10hz.md) | VEH | 0x289 | 8 | 100 ms | 15 |
| [`VCLEFT_logging1Hz`](veh/vcleft/vcleft_logging1hz.md) | VEH | 0x3A8 | 8 | 200 ms | 16 |
| [`VCLEFT_pitchEstimation`](veh/vcleft/vcleft_pitchestimation.md) | VEH | 0x2D7 | 4 | 1000 ms | 6 |
| [`VCLEFT_recallStatus`](veh/vcleft/vcleft_recallstatus.md) | VEH | 0x744 | 1 | 1000 ms | 4 |
| [`VCLEFT_seatStatus`](veh/vcleft/vcleft_seatstatus.md) | VEH | 0x4E2 | 8 | 100 ms | 60 |
| [`VCLEFT_seatStatus2`](veh/vcleft/vcleft_seatstatus2.md) | VEH | 0x2E2 | 8 | 200 ms | 51 |
| [`VCLEFT_status`](veh/vcleft/vcleft_status.md) | VEH | 0x3A2 | 8 | 33 ms | 29 |
| [`VCLEFT_steeringColumnStatus`](veh/vcleft/vcleft_steeringcolumnstatus.md) | VEH | 0x262 | 8 | 1000 ms | 12 |
| [`VCLEFT_switchStatus`](veh/vcleft/vcleft_switchstatus.md) | VEH | 0x3C2 | 8 | 50 ms | 75 |
| [`VCLEFT_thermalLogging10Hz`](veh/vcleft/vcleft_thermallogging10hz.md) | VEH | 0x290 | 8 | 20 ms | 29 |
| [`VCLEFT_thermalLogging1Hz`](veh/vcleft/vcleft_thermallogging1hz.md) | VEH | 0x291 | 7 | 500 ms | 11 |
| [`VCLEFT_thermalStatus`](veh/vcleft/vcleft_thermalstatus.md) | VEH | 0x182 | 8 | 100 ms | 8 |
| [`VCLEFT_TLCStatus`](veh/vcleft/vcleft_tlcstatus.md) | VEH | 0x1FB | 8 | 5000 ms | 10 |
| [`VCLEFT_udsResponse`](veh/vcleft/vcleft_udsresponse.md) | VEH | 0x623 | 8 |  | 2 |
| [`VCLEFT_windowStatus`](veh/vcleft/vcleft_windowstatus.md) | VEH | 0x2C2 | 8 | 100 ms | 31 |
| [`VCLEFT_doorStatus`](party/vcleft/vcleft_doorstatus.md) | PARTY | 0x102 | 8 | 100 ms | 25 |
| [`VCLEFT_epbmStatus`](party/vcleft/vcleft_epbmstatus.md) | PARTY | 0x222 | 8 | 100 ms | 7 |
| [`VCLEFT_restraintStatus`](party/vcleft/vcleft_restraintstatus.md) | PARTY | 0x30A | 8 | 50 ms | 12 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

