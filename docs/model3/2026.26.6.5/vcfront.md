---
layout: default
title: "Front body controller (VCFRONT) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 VCFRONT CAN bus messages and signals of the Front body controller (VCFRONT) for firmware 2026.26.6.5: 26 messages, 3675 signals with bit layout, scaling and value tables."
---

# Front body controller (VCFRONT) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 26 messages of the Front body controller (VCFRONT) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCFRONT_12VBatteryStatus`](veh/vcfront/vcfront_12vbatterystatus.md) | VEH | 0x261 | 8 | 16 ms | 47 |
| [`VCFRONT_alertLog`](veh/vcfront/vcfront_alertlog.md) | VEH | 0x534 | 8 |  | 2198 |
| [`VCFRONT_alertMatrix`](veh/vcfront/vcfront_alertmatrix.md) | VEH | 0x340 | 8 | 100 ms | 633 |
| [`VCFRONT_coolant`](veh/vcfront/vcfront_coolant.md) | VEH | 0x241 | 7 | 100 ms | 12 |
| [`VCFRONT_eFuseDebugStatus`](veh/vcfront/vcfront_efusedebugstatus.md) | VEH | 0x2F1 | 8 | 100 ms | 121 |
| [`VCFRONT_homelink`](veh/vcfront/vcfront_homelink.md) | VEH | 0x549 | 6 | 10000 ms | 6 |
| [`VCFRONT_info`](veh/vcfront/vcfront_info.md) | VEH | 0x301 | 8 | 1000 ms | 19 |
| [`VCFRONT_lighting`](veh/vcfront/vcfront_lighting.md) | VEH | 0x3F5 | 8 | 100 ms | 20 |
| [`VCFRONT_lightStatus`](veh/vcfront/vcfront_lightstatus.md) | VEH | 0x3F6 | 8 | 1000 ms | 27 |
| [`VCFRONT_logging0point1Hz`](veh/vcfront/vcfront_logging0point1hz.md) | VEH | 0x709 | 8 | 294 ms | 33 |
| [`VCFRONT_logging10Hz`](veh/vcfront/vcfront_logging10hz.md) | VEH | 0x2C1 | 8 | 20 ms | 23 |
| [`VCFRONT_logging1Hz`](veh/vcfront/vcfront_logging1hz.md) | VEH | 0x381 | 8 | 36 ms | 205 |
| [`VCFRONT_loggingAndVitals10Hz`](veh/vcfront/vcfront_loggingandvitals10hz.md) | VEH | 0x201 | 8 | 25 ms | 50 |
| [`VCFRONT_LVBMS_info`](veh/vcfront/vcfront_lvbms_info.md) | VEH | 0x737 | 7 | 1000 ms | 7 |
| [`VCFRONT_LVHealth`](veh/vcfront/vcfront_lvhealth.md) | VEH | 0x474 | 5 | 100 ms | 7 |
| [`VCFRONT_LVHealthDebug`](veh/vcfront/vcfront_lvhealthdebug.md) | VEH | 0x495 | 6 | 1000 ms | 19 |
| [`VCFRONT_LVPowerState`](veh/vcfront/vcfront_lvpowerstate.md) | VEH | 0x221 | 8 | 50 ms | 26 |
| [`VCFRONT_LVThermalMotors10Hz`](veh/vcfront/vcfront_lvthermalmotors10hz.md) | VEH | 0x2BC | 8 | 8 ms | 11 |
| [`VCFRONT_okToUseHighPower`](veh/vcfront/vcfront_oktousehighpower.md) | VEH | 0x2D1 | 2 | 100 ms | 9 |
| [`VCFRONT_parkedEnergyLoss`](veh/vcfront/vcfront_parkedenergyloss.md) | VEH | 0x3BD | 8 | 1000 ms | 17 |
| [`VCFRONT_sensors`](veh/vcfront/vcfront_sensors.md) | VEH | 0x321 | 8 | 1000 ms | 11 |
| [`VCFRONT_status`](veh/vcfront/vcfront_status.md) | VEH | 0x2E1 | 8 | 16 ms | 86 |
| [`VCFRONT_systemStatus`](veh/vcfront/vcfront_systemstatus.md) | VEH | 0x545 | 8 | 33 ms | 34 |
| [`VCFRONT_udsResponse`](veh/vcfront/vcfront_udsresponse.md) | VEH | 0x601 | 8 |  | 1 |
| [`VCFRONT_vehicleStatus`](veh/vcfront/vcfront_vehiclestatus.md) | VEH | 0x3A1 | 8 | 50 ms | 35 |
| [`VCFRONT_partyDebug`](party/vcfront/vcfront_partydebug.md) | PARTY | 0x104 | 7 | 100 ms | 18 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

