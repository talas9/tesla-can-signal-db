---
layout: default
title: "Right body controller (VCRIGHT) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 VCRIGHT CAN bus messages and signals of the Right body controller (VCRIGHT) for firmware 2025.20.8: 28 messages, 2295 signals with bit layout, scaling and value tables."
---

# Right body controller (VCRIGHT) CAN messages and signals — Tesla Model 3 2025.20.8

All 28 messages of the Right body controller (VCRIGHT) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCRIGHT_doorStatus2`](veh/vcright/vcright_doorstatus2.md) | VEH | 0x123 | 8 | 100 ms | 8 |
| [`VCRIGHT_hvacRequest`](veh/vcright/vcright_hvacrequest.md) | VEH | 0x20C | 8 | 100 ms | 15 |
| [`VCRIGHT_hvacStatus2`](veh/vcright/vcright_hvacstatus2.md) | VEH | 0x68B | 8 | 100 ms | 9 |
| [`VCRIGHT_lightStatus`](veh/vcright/vcright_lightstatus.md) | VEH | 0x3E3 | 4 | 200 ms | 13 |
| [`VCRIGHT_PTCRequest`](veh/vcright/vcright_ptcrequest.md) | VEH | 0x283 | 6 | 100 ms | 14 |
| [`VCRIGHT_recallStatus`](veh/vcright/vcright_recallstatus.md) | VEH | 0x743 | 1 | 1000 ms | 3 |
| [`VCRIGHT_thsStatus`](veh/vcright/vcright_thsstatus.md) | VEH | 0x383 | 8 | 100 ms | 11 |
| [`VCRIGHT_vehNm`](veh/vcright/vcright_vehnm.md) | VEH | 0x423 | 7 | 100 ms | 7 |
| [`VCRIGHT_windowStatus`](veh/vcright/vcright_windowstatus.md) | VEH | 0x2C3 | 8 | 100 ms | 31 |
| [`VCRIGHT_alertLog`](eth/vcright/vcright_alertlog.md) | ETH | 0x7DB | 8 |  | 1238 |
| [`VCRIGHT_alertMatrix`](eth/vcright/vcright_alertmatrix.md) | ETH | 0x3C0 | 8 | 100 ms | 386 |
| [`VCRIGHT_AP_hvacState10Hz`](eth/vcright/vcright_ap_hvacstate10hz.md) | ETH | 0x45A | 8 | 50 ms | 17 |
| [`VCRIGHT_debugThermal10Hz`](eth/vcright/vcright_debugthermal10hz.md) | ETH | 0x703 | 8 | 10 ms | 36 |
| [`VCRIGHT_doorStatus`](eth/vcright/vcright_doorstatus.md) | ETH | 0x103 | 8 | 100 ms | 24 |
| [`VCRIGHT_epbmDebug`](eth/vcright/vcright_epbmdebug.md) | ETH | 0x393 | 8 | 100 ms | 13 |
| [`VCRIGHT_epbmStatus`](eth/vcright/vcright_epbmstatus.md) | ETH | 0x463 | 8 | 100 ms | 6 |
| [`VCRIGHT_hvacStatus`](eth/vcright/vcright_hvacstatus.md) | ETH | 0x243 | 8 | 20 ms | 61 |
| [`VCRIGHT_info`](eth/vcright/vcright_info.md) | ETH | 0x306 | 8 | 1000 ms | 15 |
| [`VCRIGHT_logging0point1Hz`](eth/vcright/vcright_logging0point1hz.md) | ETH | 0x70B | 8 | 1250 ms | 32 |
| [`VCRIGHT_logging10Hz`](eth/vcright/vcright_logging10hz.md) | ETH | 0x263 | 8 | 20 ms | 34 |
| [`VCRIGHT_logging1Hz`](eth/vcright/vcright_logging1hz.md) | ETH | 0x2B3 | 8 | 60 ms | 161 |
| [`VCRIGHT_LVPowerState`](eth/vcright/vcright_lvpowerstate.md) | ETH | 0x225 | 4 | 100 ms | 16 |
| [`VCRIGHT_restraintStatus`](eth/vcright/vcright_restraintstatus.md) | ETH | 0x746 | 8 | 50 ms | 16 |
| [`VCRIGHT_seatStatus`](eth/vcright/vcright_seatstatus.md) | ETH | 0x4E3 | 8 | 100 ms | 51 |
| [`VCRIGHT_seatStatus2`](eth/vcright/vcright_seatstatus2.md) | ETH | 0x2E3 | 7 | 200 ms | 41 |
| [`VCRIGHT_status`](eth/vcright/vcright_status.md) | ETH | 0x343 | 8 | 100 ms | 10 |
| [`VCRIGHT_switchStatus`](eth/vcright/vcright_switchstatus.md) | ETH | 0x3C3 | 8 | 100 ms | 25 |
| [`VCRIGHT_udsResponse`](eth/vcright/vcright_udsresponse.md) | ETH | 0x609 | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

