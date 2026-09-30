---
layout: default
title: "High-voltage battery management system (BMS) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 BMS CAN bus messages and signals of the High-voltage battery management system (BMS) for firmware 2026.26.6.5: 27 messages, 1143 signals with bit layout, scaling and value tables."
---

# High-voltage battery management system (BMS) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 27 messages of the High-voltage battery management system (BMS) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`BMS_alertLog`](veh/bms/bms_alertlog.md) | VEH | 0x53F | 8 |  | 315 |
| [`BMS_alertMatrix`](veh/bms/bms_alertmatrix.md) | VEH | 0x320 | 8 | 1000 ms | 223 |
| [`BMS_bmbMinMax`](veh/bms/bms_bmbminmax.md) | VEH | 0x332 | 6 | 1000 ms | 10 |
| [`BMS_brickMeasurements`](veh/bms/bms_brickmeasurements.md) | VEH | 0x401 | 8 | 1000 ms | 218 |
| [`BMS_chargeInfo`](veh/bms/bms_chargeinfo.md) | VEH | 0x472 | 8 | 1000 ms | 8 |
| [`BMS_contactorRequest`](veh/bms/bms_contactorrequest.md) | VEH | 0x232 | 8 | 1000 ms | 8 |
| [`BMS_driveLimits`](veh/bms/bms_drivelimits.md) | VEH | 0x2D2 | 8 | 100 ms | 4 |
| [`BMS_energyStatus`](veh/bms/bms_energystatus.md) | VEH | 0x352 | 8 | 2000 ms | 12 |
| [`BMS_hvBusStatus`](veh/bms/bms_hvbusstatus.md) | VEH | 0x132 | 6 | 10 ms | 3 |
| [`BMS_info`](veh/bms/bms_info.md) | VEH | 0x300 | 8 | 1000 ms | 15 |
| [`BMS_kwhCounter`](veh/bms/bms_kwhcounter.md) | VEH | 0x3D2 | 8 | 1000 ms | 2 |
| [`BMS_kwhCountersMultiplexed`](veh/bms/bms_kwhcountersmultiplexed.md) | VEH | 0x3F2 | 8 | 1000 ms | 21 |
| [`BMS_log1`](veh/bms/bms_log1.md) | VEH | 0x372 | 8 | 1000 ms | 30 |
| [`BMS_log2`](veh/bms/bms_log2.md) | VEH | 0x3B2 | 8 | 30000 ms | 131 |
| [`BMS_packConfig`](veh/bms/bms_packconfig.md) | VEH | 0x392 | 8 | 1000 ms | 8 |
| [`BMS_packTemperatureMeasurements`](veh/bms/bms_packtemperaturemeasurements.md) | VEH | 0x712 | 8 | 1000 ms | 38 |
| [`BMS_powerAvailable`](veh/bms/bms_poweravailable.md) | VEH | 0x252 | 8 | 100 ms | 6 |
| [`BMS_rippleRequest`](veh/bms/bms_ripplerequest.md) | VEH | 0x2A2 | 7 | 1000 ms | 6 |
| [`BMS_serialNumber`](veh/bms/bms_serialnumber.md) | VEH | 0x72A | 8 |  | 16 |
| [`BMS_socStatus`](veh/bms/bms_socstatus.md) | VEH | 0x292 | 8 | 100 ms | 6 |
| [`BMS_stateOfHealth`](veh/bms/bms_stateofhealth.md) | VEH | 0x492 | 7 | 1000 ms | 9 |
| [`BMS_status`](veh/bms/bms_status.md) | VEH | 0x212 | 8 | 100 ms | 20 |
| [`BMS_thermalStatus`](veh/bms/bms_thermalstatus.md) | VEH | 0x312 | 8 | 1000 ms | 18 |
| [`BMS_udsResponse`](veh/bms/bms_udsresponse.md) | VEH | 0x612 | 8 |  | 1 |
| [`BMS_v2xInfo`](veh/bms/bms_v2xinfo.md) | VEH | 0x42F | 7 | 1000 ms | 5 |
| [`BMS_vehicleNotifications`](veh/bms/bms_vehiclenotifications.md) | VEH | 0x32A | 5 | 5000 ms | 5 |
| [`BMS_vehNm`](veh/bms/bms_vehnm.md) | VEH | 0x2F2 | 2 | 100 ms | 5 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

