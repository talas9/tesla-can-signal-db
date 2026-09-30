---
layout: default
title: "High-voltage battery management system (BMS) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 BMS CAN bus messages and signals of the High-voltage battery management system (BMS) for firmware 2025.20.8: 25 messages, 745 signals with bit layout, scaling and value tables."
---

# High-voltage battery management system (BMS) CAN messages and signals — Tesla Model 3 2025.20.8

All 25 messages of the High-voltage battery management system (BMS) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`BMS_bmbMinMax`](veh/bms/bms_bmbminmax.md) | VEH | 0x332 | 6 | 1000 ms | 10 |
| [`BMS_driveLimits`](veh/bms/bms_drivelimits.md) | VEH | 0x2D2 | 8 | 100 ms | 4 |
| [`BMS_energyStatus`](veh/bms/bms_energystatus.md) | VEH | 0x352 | 8 | 2000 ms | 12 |
| [`BMS_info`](veh/bms/bms_info.md) | VEH | 0x300 | 8 | 1000 ms | 15 |
| [`BMS_kwhCounter`](veh/bms/bms_kwhcounter.md) | VEH | 0x3D2 | 8 | 1000 ms | 2 |
| [`BMS_kwhCountersMultiplexed`](veh/bms/bms_kwhcountersmultiplexed.md) | VEH | 0x3F2 | 8 | 1000 ms | 21 |
| [`BMS_stateOfHealth`](veh/bms/bms_stateofhealth.md) | VEH | 0x492 | 7 | 1000 ms | 9 |
| [`BMS_alertLog`](eth/bms/bms_alertlog.md) | ETH | 0x53F | 8 |  | 311 |
| [`BMS_alertMatrix`](eth/bms/bms_alertmatrix.md) | ETH | 0x320 | 8 | 1000 ms | 162 |
| [`BMS_chargeInfo`](eth/bms/bms_chargeinfo.md) | ETH | 0x472 | 8 | 1000 ms | 6 |
| [`BMS_contactorRequest`](eth/bms/bms_contactorrequest.md) | ETH | 0x232 | 8 | 100 ms | 2 |
| [`BMS_debugInfo_10Hz`](eth/bms/bms_debuginfo_10hz.md) | ETH | 0x7ED | 8 | 100 ms | 3 |
| [`BMS_hvBusStatus`](eth/bms/bms_hvbusstatus.md) | ETH | 0x132 | 8 | 10 ms | 4 |
| [`BMS_log1`](eth/bms/bms_log1.md) | ETH | 0x374 | 8 | 1000 ms | 19 |
| [`BMS_log2`](eth/bms/bms_log2.md) | ETH | 0x3B2 | 8 | 30000 ms | 92 |
| [`BMS_packConfig`](eth/bms/bms_packconfig.md) | ETH | 0x392 | 8 | 1000 ms | 7 |
| [`BMS_powerAvailable`](eth/bms/bms_poweravailable.md) | ETH | 0x252 | 8 | 100 ms | 6 |
| [`BMS_rippleRequest`](eth/bms/bms_ripplerequest.md) | ETH | 0x2A2 | 7 | 100 ms | 6 |
| [`BMS_socStatus`](eth/bms/bms_socstatus.md) | ETH | 0x292 | 8 | 100 ms | 7 |
| [`BMS_status`](eth/bms/bms_status.md) | ETH | 0x212 | 8 | 100 ms | 21 |
| [`BMS_thermalStatus`](eth/bms/bms_thermalstatus.md) | ETH | 0x312 | 8 | 1000 ms | 9 |
| [`BMS_thermalStatus2`](eth/bms/bms_thermalstatus2.md) | ETH | 0x7EC | 7 | 1000 ms | 7 |
| [`BMS_udsResponse`](eth/bms/bms_udsresponse.md) | ETH | 0x612 | 8 |  | 1 |
| [`BMS_vehicleNotifications`](eth/bms/bms_vehiclenotifications.md) | ETH | 0x32A | 5 | 5000 ms | 4 |
| [`BMS_vehNm`](eth/bms/bms_vehnm.md) | ETH | 0x2F2 | 2 | 100 ms | 5 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

