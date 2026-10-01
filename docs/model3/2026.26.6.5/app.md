---
layout: default
title: "Driver assistance computer (primary) (APP) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 APP CAN bus messages and signals of the Driver assistance computer (primary) (APP) for firmware 2026.26.6.5: 28 messages, 2047 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (primary) (APP) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 28 messages of the Driver assistance computer (primary) (APP) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`APP_cameraLux`](veh/app/app_cameralux.md) | VEH | 0x3FA | 8 | 500 ms | 8 |
| [`APP_VC_infoMessage`](veh/app/app_vc_infomessage.md) | VEH | 0x38D | 8 | 1000 ms | 23 |
| [`APP_alertLog`](ch/app/app_alertlog.md) | CH | 0x5E9 | 8 |  | 1403 |
| [`APP_backupDashCamStatus`](ch/app/app_backupdashcamstatus.md) | CH | 0x415 | 1 | 500 ms | 2 |
| [`APP_boardTemperatures`](ch/app/app_boardtemperatures.md) | CH | 0x3FC | 7 | 1000 ms | 7 |
| [`APP_camCalibrationStatus`](ch/app/app_camcalibrationstatus.md) | CH | 0x3F4 | 6 | 1000 ms | 46 |
| [`APP_cameraLux`](ch/app/app_cameralux.md) | CH | 0x3FA | 8 | 500 ms | 8 |
| [`APP_cameraStatus`](ch/app/app_camerastatus.md) | CH | 0x410 | 3 | 500 ms | 11 |
| [`APP_cameraTemperatures`](ch/app/app_cameratemperatures.md) | CH | 0x499 | 8 | 1000 ms | 2 |
| [`APP_dashCamStatus`](ch/app/app_dashcamstatus.md) | CH | 0x413 | 3 | 500 ms | 6 |
| [`APP_defogInfoMessage`](ch/app/app_defoginfomessage.md) | CH | 0x4FF | 8 | 1000 ms | 6 |
| [`APP_driverMonitorStatus`](ch/app/app_drivermonitorstatus.md) | CH | 0x3AB | 5 | 500 ms | 25 |
| [`APP_environment`](ch/app/app_environment.md) | CH | 0x25B | 3 | 1000 ms | 11 |
| [`APP_factorySummonGoal`](ch/app/app_factorysummongoal.md) | CH | 0x425 | 8 | 1000 ms | 3 |
| [`APP_frontParkAssistData`](ch/app/app_frontparkassistdata.md) | CH | 0x34B | 6 | 100 ms | 7 |
| [`APP_info`](ch/app/app_info.md) | CH | 0x549 | 8 | 1000 ms | 2 |
| [`APP_rearParkAssistData`](ch/app/app_rearparkassistdata.md) | CH | 0x38B | 5 | 100 ms | 5 |
| [`APP_status`](ch/app/app_status.md) | CH | 0x259 | 8 | 100 ms | 25 |
| [`APP_trafficControl`](ch/app/app_trafficcontrol.md) | CH | 0x25D | 6 | 500 ms | 14 |
| [`APP_visionOcsStatus`](ch/app/app_visionocsstatus.md) | CH | 0x35B | 5 | 100 ms | 7 |
| [`APP_warningMatrix0`](ch/app/app_warningmatrix0.md) | CH | 0x329 | 8 | 1000 ms | 64 |
| [`APP_warningMatrix1`](ch/app/app_warningmatrix1.md) | CH | 0x369 | 8 | 1000 ms | 42 |
| [`APP_warningMatrix2`](ch/app/app_warningmatrix2.md) | CH | 0x429 | 8 | 1000 ms | 64 |
| [`APP_warningMatrix3`](ch/app/app_warningmatrix3.md) | CH | 0x439 | 8 | 1000 ms | 43 |
| [`APP_warningMatrix4`](ch/app/app_warningmatrix4.md) | CH | 0x449 | 8 | 1000 ms | 63 |
| [`APP_warningMatrix5`](ch/app/app_warningmatrix5.md) | CH | 0x47F | 8 | 1000 ms | 64 |
| [`APP_warningMatrix6`](ch/app/app_warningmatrix6.md) | CH | 0x47D | 8 | 1000 ms | 63 |
| [`APP_warningMatrix7`](ch/app/app_warningmatrix7.md) | CH | 0x4D1 | 8 | 1000 ms | 23 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

