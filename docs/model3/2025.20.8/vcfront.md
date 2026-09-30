---
layout: default
title: "Front body controller (VCFRONT) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 VCFRONT CAN bus messages and signals of the Front body controller (VCFRONT) for firmware 2025.20.8: 25 messages, 3491 signals with bit layout, scaling and value tables."
---

# Front body controller (VCFRONT) CAN messages and signals — Tesla Model 3 2025.20.8

All 25 messages of the Front body controller (VCFRONT) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCFRONT_coolant`](veh/vcfront/vcfront_coolant.md) | VEH | 0x241 | 7 | 100 ms | 12 |
| [`VCFRONT_lighting`](veh/vcfront/vcfront_lighting.md) | VEH | 0x3F5 | 8 | 100 ms | 20 |
| [`VCFRONT_lightStatus`](veh/vcfront/vcfront_lightstatus.md) | VEH | 0x3F6 | 8 | 1000 ms | 27 |
| [`VCFRONT_LVBMS_info`](veh/vcfront/vcfront_lvbms_info.md) | VEH | 0x737 | 7 | 1000 ms | 7 |
| [`VCFRONT_LVThermalMotors10Hz`](veh/vcfront/vcfront_lvthermalmotors10hz.md) | VEH | 0x2BC | 8 | 8 ms | 11 |
| [`VCFRONT_okToUseHighPower`](veh/vcfront/vcfront_oktousehighpower.md) | VEH | 0x2D1 | 2 | 100 ms | 9 |
| [`VCFRONT_parkedEnergyLoss`](veh/vcfront/vcfront_parkedenergyloss.md) | VEH | 0x3BD | 8 | 1000 ms | 17 |
| [`VCFRONT_sensors`](veh/vcfront/vcfront_sensors.md) | VEH | 0x321 | 8 | 1000 ms | 11 |
| [`VCFRONT_systemStatus`](veh/vcfront/vcfront_systemstatus.md) | VEH | 0x545 | 8 | 33 ms | 34 |
| [`VCFRONT_partyDebug`](party/vcfront/vcfront_partydebug.md) | PARTY | 0x104 | 7 | 100 ms | 18 |
| [`VCFRONT_12VBatteryStatus`](eth/vcfront/vcfront_12vbatterystatus.md) | ETH | 0x261 | 8 | 16 ms | 45 |
| [`VCFRONT_alertLog`](eth/vcfront/vcfront_alertlog.md) | ETH | 0x534 | 8 |  | 2145 |
| [`VCFRONT_alertMatrix`](eth/vcfront/vcfront_alertmatrix.md) | ETH | 0x340 | 8 | 100 ms | 577 |
| [`VCFRONT_eFuseDebugStatus`](eth/vcfront/vcfront_efusedebugstatus.md) | ETH | 0x2F1 | 8 | 100 ms | 96 |
| [`VCFRONT_info`](eth/vcfront/vcfront_info.md) | ETH | 0x301 | 8 | 1000 ms | 17 |
| [`VCFRONT_logging0point1Hz`](eth/vcfront/vcfront_logging0point1hz.md) | ETH | 0x709 | 8 | 322 ms | 23 |
| [`VCFRONT_logging10Hz`](eth/vcfront/vcfront_logging10hz.md) | ETH | 0x2C1 | 8 | 20 ms | 22 |
| [`VCFRONT_logging1Hz`](eth/vcfront/vcfront_logging1hz.md) | ETH | 0x381 | 8 | 38 ms | 184 |
| [`VCFRONT_loggingAndVitals10Hz`](eth/vcfront/vcfront_loggingandvitals10hz.md) | ETH | 0x201 | 8 | 25 ms | 47 |
| [`VCFRONT_LVHealth`](eth/vcfront/vcfront_lvhealth.md) | ETH | 0x7E1 | 8 | 100 ms | 5 |
| [`VCFRONT_LVHealthDebug`](eth/vcfront/vcfront_lvhealthdebug.md) | ETH | 0x7E0 | 6 | 1000 ms | 18 |
| [`VCFRONT_LVPowerState`](eth/vcfront/vcfront_lvpowerstate.md) | ETH | 0x221 | 8 | 50 ms | 23 |
| [`VCFRONT_status`](eth/vcfront/vcfront_status.md) | ETH | 0x2E1 | 8 | 14 ms | 88 |
| [`VCFRONT_udsResponse`](eth/vcfront/vcfront_udsresponse.md) | ETH | 0x601 | 8 |  | 1 |
| [`VCFRONT_vehicleStatus`](eth/vcfront/vcfront_vehiclestatus.md) | ETH | 0x3A1 | 8 | 50 ms | 34 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

