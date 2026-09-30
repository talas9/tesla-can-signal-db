---
layout: default
title: "Driver assistance computer (primary) (APP) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 APP CAN bus messages and signals of the Driver assistance computer (primary) (APP) for firmware 2025.20.8: 24 messages, 1643 signals with bit layout, scaling and value tables."
---

# Driver assistance computer (primary) (APP) CAN messages and signals — Tesla Model 3 2025.20.8

All 24 messages of the Driver assistance computer (primary) (APP) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`APP_backupDashCamStatus`](ch/app/app_backupdashcamstatus.md) | CH | 0x415 | 1 | 500 ms | 2 |
| [`APP_boardTemperatures`](ch/app/app_boardtemperatures.md) | CH | 0x3FC | 7 | 1000 ms | 7 |
| [`APP_cameraLux`](ch/app/app_cameralux.md) | CH | 0x3FA | 8 | 500 ms | 8 |
| [`APP_dashCamStatus`](ch/app/app_dashcamstatus.md) | CH | 0x413 | 3 | 500 ms | 6 |
| [`APP_factorySummonGoal`](ch/app/app_factorysummongoal.md) | CH | 0x425 | 8 | 1000 ms | 3 |
| [`APP_frontParkAssistData`](ch/app/app_frontparkassistdata.md) | CH | 0x34B | 6 | 100 ms | 7 |
| [`APP_info`](ch/app/app_info.md) | CH | 0x549 | 8 | 1000 ms | 2 |
| [`APP_rearParkAssistData`](ch/app/app_rearparkassistdata.md) | CH | 0x38B | 5 | 100 ms | 5 |
| [`APP_trafficControl`](ch/app/app_trafficcontrol.md) | CH | 0x25D | 6 | 500 ms | 14 |
| [`APP_visionOcsStatus`](ch/app/app_visionocsstatus.md) | CH | 0x35B | 5 | 100 ms | 7 |
| [`APP_warningMatrix0`](ch/app/app_warningmatrix0.md) | CH | 0x329 | 8 | 1000 ms | 64 |
| [`APP_warningMatrix1`](ch/app/app_warningmatrix1.md) | CH | 0x369 | 8 | 1000 ms | 42 |
| [`APP_warningMatrix2`](ch/app/app_warningmatrix2.md) | CH | 0x429 | 8 | 1000 ms | 64 |
| [`APP_warningMatrix4`](ch/app/app_warningmatrix4.md) | CH | 0x449 | 8 | 1000 ms | 63 |
| [`APP_alertLog`](eth/app/app_alertlog.md) | ETH | 0x5E9 | 8 |  | 1124 |
| [`APP_camCalibrationStatus`](eth/app/app_camcalibrationstatus.md) | ETH | 0x7FE | 6 | 1000 ms | 41 |
| [`APP_cameraStatus`](eth/app/app_camerastatus.md) | ETH | 0x410 | 2 | 500 ms | 10 |
| [`APP_cameraTemperatures`](eth/app/app_cameratemperatures.md) | ETH | 0x499 | 8 | 1000 ms | 2 |
| [`APP_environment`](eth/app/app_environment.md) | ETH | 0x25B | 1 | 1000 ms | 2 |
| [`APP_status`](eth/app/app_status.md) | ETH | 0x259 | 8 | 100 ms | 24 |
| [`APP_VC_infoMessage`](eth/app/app_vc_infomessage.md) | ETH | 0x38D | 8 | 1000 ms | 23 |
| [`APP_warningMatrix3`](eth/app/app_warningmatrix3.md) | ETH | 0x439 | 8 | 1000 ms | 41 |
| [`APP_warningMatrix5`](eth/app/app_warningmatrix5.md) | ETH | 0x479 | 8 | 1000 ms | 64 |
| [`APP_warningMatrix6`](eth/app/app_warningmatrix6.md) | ETH | 0x47D | 8 | 1000 ms | 18 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

