---
layout: default
title: "Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y VCSEC CAN bus messages and signals of the Vehicle security controller (VCSEC) for firmware 2025.20.8: 20 messages, 1503 signals with bit layout, scaling and value tables."
---

# Vehicle security controller (VCSEC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 20 messages of the Vehicle security controller (VCSEC) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VCSEC_authentication`](veh/vcsec/vcsec_authentication.md) | VEH | 0x339 | 8 | 100 ms | 30 |
| [`VCSEC_BLEEndpointInfo`](veh/vcsec/vcsec_bleendpointinfo.md) | VEH | 0x3C9 | 8 | 1000 ms | 93 |
| [`VCSEC_ChildSeatStatus`](veh/vcsec/vcsec_childseatstatus.md) | VEH | 0x25F | 8 | 500 ms | 21 |
| [`VCSEC_DeviceStatus`](veh/vcsec/vcsec_devicestatus.md) | VEH | 0x359 | 8 | 100 ms | 341 |
| [`VCSEC_ecuConfig`](veh/vcsec/vcsec_ecuconfig.md) | VEH | 0x720 | 5 | 10000 ms | 3 |
| [`VCSEC_info`](veh/vcsec/vcsec_info.md) | VEH | 0x319 | 8 | 1000 ms | 19 |
| [`VCSEC_IsoTpPipeRemoteUI`](veh/vcsec/vcsec_isotppiperemoteui.md) | VEH | 0x1DA | 8 |  | 8 |
| [`VCSEC_IsoTpUDPPipeUI`](veh/vcsec/vcsec_isotpudppipeui.md) | VEH | 0x1D9 | 8 |  | 8 |
| [`VCSEC_requests`](veh/vcsec/vcsec_requests.md) | VEH | 0x1F9 | 8 | 100 ms | 19 |
| [`VCSEC_TPMSConnectionData`](veh/vcsec/vcsec_tpmsconnectiondata.md) | VEH | 0x42A | 8 | 100 ms | 20 |
| [`VCSEC_TPMSDisplay`](veh/vcsec/vcsec_tpmsdisplay.md) | VEH | 0x25A | 6 | 1000 ms | 13 |
| [`VCSEC_additionalAuthInfo`](eth/vcsec/vcsec_additionalauthinfo.md) | ETH | 0x2F9 | 8 | 100 ms | 26 |
| [`VCSEC_alertLog`](eth/vcsec/vcsec_alertlog.md) | ETH | 0x530 | 8 |  | 453 |
| [`VCSEC_alertMatrix`](eth/vcsec/vcsec_alertmatrix.md) | ETH | 0x3F9 | 8 | 100 ms | 292 |
| [`VCSEC_debug100ms`](eth/vcsec/vcsec_debug100ms.md) | ETH | 0x719 | 8 | 50 ms | 40 |
| [`VCSEC_IsoTpPipeODIN`](eth/vcsec/vcsec_isotppipeodin.md) | ETH | 0x3B9 | 8 |  | 8 |
| [`VCSEC_TPMSData`](eth/vcsec/vcsec_tpmsdata.md) | ETH | 0x219 | 7 | 100 ms | 39 |
| [`VCSEC_TPMSStatus`](eth/vcsec/vcsec_tpmsstatus.md) | ETH | 0x23A | 8 | 1000 ms | 50 |
| [`VCSEC_udsResponse`](eth/vcsec/vcsec_udsresponse.md) | ETH | 0x7D8 | 8 |  | 1 |
| [`VCSEC_UWBData`](eth/vcsec/vcsec_uwbdata.md) | ETH | 0x42B | 8 | 100 ms | 19 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

