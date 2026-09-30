---
layout: default
title: "FC_alertMatrix5 (0x3BE) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: alert matrix5. Tesla Model 3 CAN bus message FC_alertMatrix5 (0x3BE) of FC ECU, firmware 2025.20.8, 57 signals (FC_a257_GB_bmsMia, FC_a258_GB_evseMia, FC_a259_GB_vehTxBufOvf, FC_a260_GB_vehRxBufOvf and 53 more). Bit layout, scaling, units and value tables."
---

# FC_alertMatrix5 (0x3BE) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: alert matrix5; frame length from the layout, not yet observed on a vehicle bus. This page documents the 57 signals of FC_alertMatrix5 as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_alertMatrix5` |
| CAN id | 0x3BE (958) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 57 |

## Signals of FC_alertMatrix5

Tesla Model 3 CAN bus signals in `FC_alertMatrix5`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_a257_GB_bmsMia` | FC ECU: a257 GB bms mia | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a258_GB_evseMia` | FC ECU: a258 GB evse mia | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a259_GB_vehTxBufOvf` | FC ECU: a259 GB veh tx buf ovf | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a260_GB_vehRxBufOvf` | FC ECU: a260 GB veh rx buf ovf | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a261_GB_evseTxBufOvf` | FC ECU: a261 GB evse tx buf ovf | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a262_GB_evseRxBufOvf` | FC ECU: a262 GB evse rx buf ovf | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a263_GB_hwProxTrip` | FC ECU: a263 GB hw prox trip | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a264_GB_timeoutCHM` | FC ECU: a264 GB timeout CHM | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a265_GB_bmsIncompatible` | FC ECU: a265 GB bms incompatible | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a266_GB_negPin_OT` | FC ECU: a266 GB neg pin OT | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a267_GB_posPin_OT` | FC ECU: a267 GB pos pin OT | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a268_GB_pcb_OT` | FC ECU: a268 GB pcb OT | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a269_GB_timeoutCRM` | FC ECU: a269 GB timeout CRM | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a270_GB_timeoutCML` | FC ECU: a270 GB timeout CML | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a271_GB_timeoutCRO` | FC ECU: a271 GB timeout CRO | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a272_GB_negToPosDeltaHi` | FC ECU: a272 GB neg to pos delta hi | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a273_GB_negToPosDeltaLo` | FC ECU: a273 GB neg to pos delta lo | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a274_GB_negToPcbDeltaHi` | FC ECU: a274 GB neg to pcb delta hi | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a275_GB_posToPcbDeltaHi` | FC ECU: a275 GB pos to pcb delta hi | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a276_GB_negToPcbDeltaLo` | FC ECU: a276 GB neg to pcb delta lo | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a277_GB_posToPcbDeltaLo` | FC ECU: a277 GB pos to pcb delta lo | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a278_GB_timeoutCCS` | FC ECU: a278 GB timeout CCS | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a279_GB_evseOverCurrent` | FC ECU: a279 GB evse over current | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a280_GB_retryLimitExceeded` | FC ECU: a280 GB retry limit exceeded | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a281_GB_evseOutOfService` | FC ECU: a281 GB evse out of service | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a282_GB_negTempHiFoldBk` | FC ECU: a282 GB neg temp hi fold bk | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a283_GB_posTempHiFoldBk` | FC ECU: a283 GB pos temp hi fold bk | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a284_GB_pcbTempHiFoldBk` | FC ECU: a284 GB pcb temp hi fold bk | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a285_GB_proxDisconnected` | FC ECU: a285 GB prox disconnected | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a286_GB_evseConnUnlocked` | FC ECU: a286 GB evse conn unlocked | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a287_GB_vehConnUnlocked` | FC ECU: a287 GB veh conn unlocked | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a288_GB_evseAbnormalStopReq` | FC ECU: a288 GB evse abnormal stop req | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a289_GB_proxTimeout` | FC ECU: a289 GB prox timeout | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a290_GB_pilotAcceptTimeout` | FC ECU: a290 GB pilot accept timeout | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a291_GB_vehDataTimeout` | FC ECU: a291 GB veh data timeout | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a292_GB_vehConLockTimeout` | FC ECU: a292 GB veh con lock timeout | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a293_GB_proxRationality` | FC ECU: a293 GB prox rationality | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a294_GB_unused` | FC ECU: a294 GB unused | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a295_GB_pilotRationality` | FC ECU: a295 GB pilot rationality | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a296_GB_invalidPilotTransitio` | FC ECU: a296 GB invalid pilot transitio | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a297_GB_unused` | FC ECU: a297 GB unused | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a298_GB_bmsCtrCloseTimeout` | FC ECU: a298 GB bms ctr close timeout | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a299_GB_evseReadyTimeout` | FC ECU: a299 GB evse ready timeout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a300_GB_unused` | FC ECU: a300 GB unused | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a301_GB_unused` | FC ECU: a301 GB unused | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a302_GB_unused` | FC ECU: a302 GB unused | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a303_GB_negRecogTimeout` | FC ECU: a303 GB neg recog timeout | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a304_GB_unused` | FC ECU: a304 GB unused | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a305_GB_posRecogTimeout` | FC ECU: a305 GB pos recog timeout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a306_GB_vehReadyDeasserted` | FC ECU: a306 GB veh ready deasserted | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a307_GB_fcContOpenTimeout` | FC ECU: a307 GB fc cont open timeout | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a308_GB_evseConLockTimeout` | FC ECU: a308 GB evse con lock timeout | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a309_GB_unused` | FC ECU: a309 GB unused | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a310_GB_unused` | FC ECU: a310 GB unused | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a311_GB_battParamsTimeout` | FC ECU: a311 GB batt params timeout | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a312_GB_evseLimitsTimeout` | FC ECU: a312 GB evse limits timeout | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a313_GB_inputVoltageRailOv` | FC ECU: a313 GB input voltage rail ov | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
