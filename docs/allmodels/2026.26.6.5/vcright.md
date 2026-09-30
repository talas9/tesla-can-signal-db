---
layout: default
title: "Right body controller (VCRIGHT) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y VCRIGHT CAN bus messages and signals of the Right body controller (VCRIGHT) for firmware 2026.26.6.5: 31 messages, 2644 signals with bit layout, scaling and value tables."
---

# Right body controller (VCRIGHT) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 31 messages of the Right body controller (VCRIGHT) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCRIGHT_alertLog`](veh/vcright/vcright_alertlog.md) | VEH | 0x550 | 8 |  | 1366 |
| [`VCRIGHT_alertMatrix`](veh/vcright/vcright_alertmatrix.md) | VEH | 0x3C0 | 8 | 100 ms | 432 |
| [`VCRIGHT_AP_hvacState10Hz`](veh/vcright/vcright_ap_hvacstate10hz.md) | VEH | 0x45A | 8 | 50 ms | 23 |
| [`VCRIGHT_debugThermal10Hz`](veh/vcright/vcright_debugthermal10hz.md) | VEH | 0x703 | 8 | 10 ms | 37 |
| [`VCRIGHT_doorStatus`](veh/vcright/vcright_doorstatus.md) | VEH | 0x103 | 8 | 100 ms | 25 |
| [`VCRIGHT_doorStatus2`](veh/vcright/vcright_doorstatus2.md) | VEH | 0x123 | 8 | 100 ms | 8 |
| [`VCRIGHT_epbmDebug`](veh/vcright/vcright_epbmdebug.md) | VEH | 0x393 | 8 | 100 ms | 14 |
| [`VCRIGHT_hvacRequest`](veh/vcright/vcright_hvacrequest.md) | VEH | 0x20C | 8 | 100 ms | 15 |
| [`VCRIGHT_hvacStatus`](veh/vcright/vcright_hvacstatus.md) | VEH | 0x243 | 8 | 20 ms | 68 |
| [`VCRIGHT_hvacStatus2`](veh/vcright/vcright_hvacstatus2.md) | VEH | 0x68B | 8 | 100 ms | 9 |
| [`VCRIGHT_info`](veh/vcright/vcright_info.md) | VEH | 0x303 | 8 | 1000 ms | 16 |
| [`VCRIGHT_lightStatus`](veh/vcright/vcright_lightstatus.md) | VEH | 0x3E3 | 4 | 200 ms | 13 |
| [`VCRIGHT_logging0point1Hz`](veh/vcright/vcright_logging0point1hz.md) | VEH | 0x70B | 8 | 1000 ms | 58 |
| [`VCRIGHT_logging10Hz`](veh/vcright/vcright_logging10hz.md) | VEH | 0x263 | 8 | 20 ms | 47 |
| [`VCRIGHT_logging1Hz`](veh/vcright/vcright_logging1hz.md) | VEH | 0x2B3 | 8 | 60 ms | 178 |
| [`VCRIGHT_LVPowerState`](veh/vcright/vcright_lvpowerstate.md) | VEH | 0x225 | 4 | 100 ms | 18 |
| [`VCRIGHT_PTCRequest`](veh/vcright/vcright_ptcrequest.md) | VEH | 0x283 | 6 | 100 ms | 14 |
| [`VCRIGHT_recallStatus`](veh/vcright/vcright_recallstatus.md) | VEH | 0x743 | 1 | 1000 ms | 3 |
| [`VCRIGHT_restraintStatus`](veh/vcright/vcright_restraintstatus.md) | VEH | 0x31A | 8 | 50 ms | 17 |
| [`VCRIGHT_seatStatus`](veh/vcright/vcright_seatstatus.md) | VEH | 0x4E3 | 8 | 100 ms | 60 |
| [`VCRIGHT_seatStatus2`](veh/vcright/vcright_seatstatus2.md) | VEH | 0x2E3 | 7 | 200 ms | 61 |
| [`VCRIGHT_status`](veh/vcright/vcright_status.md) | VEH | 0x343 | 8 | 100 ms | 11 |
| [`VCRIGHT_switchStatus`](veh/vcright/vcright_switchstatus.md) | VEH | 0x3C3 | 8 | 100 ms | 42 |
| [`VCRIGHT_thsStatus`](veh/vcright/vcright_thsstatus.md) | VEH | 0x383 | 8 | 100 ms | 11 |
| [`VCRIGHT_udsResponse`](veh/vcright/vcright_udsresponse.md) | VEH | 0x609 | 8 |  | 2 |
| [`VCRIGHT_vehNm`](veh/vcright/vcright_vehnm.md) | VEH | 0x423 | 7 | 100 ms | 7 |
| [`VCRIGHT_windowStatus`](veh/vcright/vcright_windowstatus.md) | VEH | 0x2C3 | 8 | 100 ms | 31 |
| [`VCRIGHT_AP_hvacState1Hz`](party/vcright/vcright_ap_hvacstate1hz.md) | PARTY | 0x464 | 8 | 1000 ms | 9 |
| [`VCRIGHT_doorStatus`](party/vcright/vcright_doorstatus.md) | PARTY | 0x103 | 8 | 100 ms | 25 |
| [`VCRIGHT_epbmStatus`](party/vcright/vcright_epbmstatus.md) | PARTY | 0x263 | 8 | 100 ms | 7 |
| [`VCRIGHT_restraintStatus`](party/vcright/vcright_restraintstatus.md) | PARTY | 0x31A | 8 | 50 ms | 17 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

