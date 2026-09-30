---
layout: default
title: "Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 VCSEC CAN bus messages and signals of the Vehicle security controller (VCSEC) for firmware 2026.26.6.5: 21 messages, 1542 signals with bit layout, scaling and value tables."
---

# Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 21 messages of the Vehicle security controller (VCSEC) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCSEC_additionalAuthInfo`](veh/vcsec/vcsec_additionalauthinfo.md) | VEH | 0x2F9 | 8 | 100 ms | 25 |
| [`VCSEC_alertLog`](veh/vcsec/vcsec_alertlog.md) | VEH | 0x530 | 8 |  | 437 |
| [`VCSEC_alertMatrix`](veh/vcsec/vcsec_alertmatrix.md) | VEH | 0x3F9 | 8 | 100 ms | 314 |
| [`VCSEC_authentication`](veh/vcsec/vcsec_authentication.md) | VEH | 0x339 | 8 | 100 ms | 30 |
| [`VCSEC_BLEEndpointInfo`](veh/vcsec/vcsec_bleendpointinfo.md) | VEH | 0x3C9 | 8 | 1000 ms | 93 |
| [`VCSEC_ChildSeatStatus`](veh/vcsec/vcsec_childseatstatus.md) | VEH | 0x25F | 8 | 500 ms | 21 |
| [`VCSEC_debug100ms`](veh/vcsec/vcsec_debug100ms.md) | VEH | 0x719 | 8 | 50 ms | 50 |
| [`VCSEC_DeviceStatus`](veh/vcsec/vcsec_devicestatus.md) | VEH | 0x359 | 8 | 100 ms | 341 |
| [`VCSEC_ecuConfig`](veh/vcsec/vcsec_ecuconfig.md) | VEH | 0x720 | 5 | 10000 ms | 3 |
| [`VCSEC_info`](veh/vcsec/vcsec_info.md) | VEH | 0x319 | 8 | 1000 ms | 19 |
| [`VCSEC_IsoTpPipeODIN`](veh/vcsec/vcsec_isotppipeodin.md) | VEH | 0x3B9 | 8 |  | 8 |
| [`VCSEC_IsoTpPipeRemoteUI`](veh/vcsec/vcsec_isotppiperemoteui.md) | VEH | 0x1DA | 8 |  | 8 |
| [`VCSEC_IsoTpUDPPipeUI`](veh/vcsec/vcsec_isotpudppipeui.md) | VEH | 0x1D9 | 8 |  | 8 |
| [`VCSEC_requests`](veh/vcsec/vcsec_requests.md) | VEH | 0x1F9 | 8 | 100 ms | 19 |
| [`VCSEC_requests2`](veh/vcsec/vcsec_requests2.md) | VEH | 0x119 | 4 | 100 ms | 9 |
| [`VCSEC_TPMSConnectionData`](veh/vcsec/vcsec_tpmsconnectiondata.md) | VEH | 0x42A | 8 | 200 ms | 20 |
| [`VCSEC_TPMSData`](veh/vcsec/vcsec_tpmsdata.md) | VEH | 0x219 | 7 | 100 ms | 45 |
| [`VCSEC_TPMSDisplay`](veh/vcsec/vcsec_tpmsdisplay.md) | VEH | 0x25A | 6 | 1000 ms | 13 |
| [`VCSEC_TPMSStatus`](veh/vcsec/vcsec_tpmsstatus.md) | VEH | 0x23A | 8 | 1000 ms | 50 |
| [`VCSEC_udsResponse`](veh/vcsec/vcsec_udsresponse.md) | VEH | 0x60B | 8 |  | 1 |
| [`VCSEC_UWBData`](veh/vcsec/vcsec_uwbdata.md) | VEH | 0x42B | 8 | 100 ms | 28 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

