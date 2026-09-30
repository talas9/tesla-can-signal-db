---
layout: default
title: "Left body controller (VCLEFT) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 VCLEFT CAN bus messages and signals of the Left body controller (VCLEFT) for firmware 2025.20.8: 28 messages, 2171 signals with bit layout, scaling and value tables."
---

# Left body controller (VCLEFT) CAN messages and signals — Tesla Model 3 2025.20.8

All 28 messages of the Left body controller (VCLEFT) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCLEFT_doorStatus2`](veh/vcleft/vcleft_doorstatus2.md) | VEH | 0x122 | 8 | 100 ms | 8 |
| [`VCLEFT_etcBluetoothStatus`](veh/vcleft/vcleft_etcbluetoothstatus.md) | VEH | 0x4A2 | 1 | 1000 ms | 1 |
| [`VCLEFT_hvacBlowerFeedback`](veh/vcleft/vcleft_hvacblowerfeedback.md) | VEH | 0x282 | 8 | 100 ms | 13 |
| [`VCLEFT_recallStatus`](veh/vcleft/vcleft_recallstatus.md) | VEH | 0x744 | 1 | 1000 ms | 4 |
| [`VCLEFT_steeringColumnStatus`](veh/vcleft/vcleft_steeringcolumnstatus.md) | VEH | 0x262 | 8 | 100 ms | 12 |
| [`VCLEFT_thermalStatus`](veh/vcleft/vcleft_thermalstatus.md) | VEH | 0x182 | 8 | 100 ms | 8 |
| [`VCLEFT_TLCStatus`](veh/vcleft/vcleft_tlcstatus.md) | VEH | 0x1FB | 8 | 50 ms | 10 |
| [`VCLEFT_windowStatus`](veh/vcleft/vcleft_windowstatus.md) | VEH | 0x2C2 | 8 | 100 ms | 31 |
| [`VCLEFT_alertLog`](eth/vcleft/vcleft_alertlog.md) | ETH | 0x7DD | 8 |  | 1294 |
| [`VCLEFT_alertMatrix`](eth/vcleft/vcleft_alertmatrix.md) | ETH | 0x360 | 8 | 100 ms | 429 |
| [`VCLEFT_doorStatus`](eth/vcleft/vcleft_doorstatus.md) | ETH | 0x102 | 8 | 100 ms | 23 |
| [`VCLEFT_epbmDebug`](eth/vcleft/vcleft_epbmdebug.md) | ETH | 0x272 | 8 | 100 ms | 13 |
| [`VCLEFT_epbmStatus`](eth/vcleft/vcleft_epbmstatus.md) | ETH | 0x474 | 8 | 100 ms | 6 |
| [`VCLEFT_info`](eth/vcleft/vcleft_info.md) | ETH | 0x302 | 8 | 1000 ms | 15 |
| [`VCLEFT_liftgateStatus`](eth/vcleft/vcleft_liftgatestatus.md) | ETH | 0x142 | 8 | 50 ms | 21 |
| [`VCLEFT_lightStatus`](eth/vcleft/vcleft_lightstatus.md) | ETH | 0x3E2 | 7 | 200 ms | 25 |
| [`VCLEFT_logging0point1Hz`](eth/vcleft/vcleft_logging0point1hz.md) | ETH | 0x70A | 6 | 10000 ms | 5 |
| [`VCLEFT_logging10Hz`](eth/vcleft/vcleft_logging10hz.md) | ETH | 0x289 | 8 | 100 ms | 15 |
| [`VCLEFT_logging1Hz`](eth/vcleft/vcleft_logging1hz.md) | ETH | 0x3A8 | 8 | 333 ms | 9 |
| [`VCLEFT_pitchEstimation`](eth/vcleft/vcleft_pitchestimation.md) | ETH | 0x2D7 | 5 | 100 ms | 6 |
| [`VCLEFT_restraintStatus`](eth/vcleft/vcleft_restraintstatus.md) | ETH | 0x747 | 8 | 50 ms | 10 |
| [`VCLEFT_seatStatus`](eth/vcleft/vcleft_seatstatus.md) | ETH | 0x4E2 | 8 | 100 ms | 51 |
| [`VCLEFT_seatStatus2`](eth/vcleft/vcleft_seatstatus2.md) | ETH | 0x2E2 | 8 | 200 ms | 23 |
| [`VCLEFT_status`](eth/vcleft/vcleft_status.md) | ETH | 0x3A2 | 8 | 33 ms | 25 |
| [`VCLEFT_switchStatus`](eth/vcleft/vcleft_switchstatus.md) | ETH | 0x3C2 | 8 | 50 ms | 72 |
| [`VCLEFT_thermalLogging10Hz`](eth/vcleft/vcleft_thermallogging10hz.md) | ETH | 0x290 | 8 | 20 ms | 27 |
| [`VCLEFT_thermalLogging1Hz`](eth/vcleft/vcleft_thermallogging1hz.md) | ETH | 0x291 | 8 | 500 ms | 13 |
| [`VCLEFT_udsResponse`](eth/vcleft/vcleft_udsresponse.md) | ETH | 0x623 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

