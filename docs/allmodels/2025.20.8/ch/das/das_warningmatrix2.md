---
layout: default
title: "DAS_warningMatrix2 (0x349) — Driver assistance computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer message: warning matrix2. Tesla Model 3 / Model Y CAN bus message DAS_warningMatrix2 (0x349) of Driver assistance computer, firmware 2025.20.8, 26 signals (DAS_w129_mainCamExtNotCal, DAS_w130_narrowCamExtNotCal, DAS_w131_mainCamCalSaved, DAS_w132_narrowCamCalSaved and 22 more). Bit layout, scaling, units and value tables."
---

# DAS_warningMatrix2 (0x349) — Driver assistance computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Driver assistance computer message: warning matrix2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of DAS_warningMatrix2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_warningMatrix2` |
| CAN id | 0x349 (841) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 26 |

## Signals of DAS_warningMatrix2

Tesla Model 3 / Model Y CAN bus signals in `DAS_warningMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_w129_mainCamExtNotCal` | Driver assistance computer: w129 main cam ext not cal | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w130_narrowCamExtNotCal` | Driver assistance computer: w130 narrow cam ext not cal | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w131_mainCamCalSaved` | Driver assistance computer: w131 main cam cal saved | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w132_narrowCamCalSaved` | Driver assistance computer: w132 narrow cam cal saved | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w133_mainCamInitFault` | Driver assistance computer: w133 main cam init fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w134_narrowCamInitFault` | Driver assistance computer: w134 narrow cam init fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w135_fisheyeCamInitFault` | Driver assistance computer: w135 fisheye cam init fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w136_lPillarCamInitFault` | Driver assistance computer: w136 l pillar cam init fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w137_rPillarCamInitFault` | Driver assistance computer: w137 r pillar cam init fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w138_lRepeatCamInitFault` | Driver assistance computer: w138 l repeat cam init fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w139_rRepeatCamInitFault` | Driver assistance computer: w139 r repeat cam init fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w140_backupCamInitFault` | Driver assistance computer: w140 backup cam init fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w141_ECU_Thermal_Issue` | Driver assistance computer: w141 ECU thermal issue | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w142_fwdCamPitchProblem` | Driver assistance computer: w142 fwd cam pitch problem | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w143_IDF_event` | Driver assistance computer: w143 IDF event | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w144_selfieCamInitFault` | Driver assistance computer: w144 selfie cam init fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w171_fisheyeCamExtNotCal` | Driver assistance computer: w171 fisheye cam ext not cal | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w172_lPillarCamExtNotCal` | Driver assistance computer: w172 l pillar cam ext not cal | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w173_rPillarCamExtNotCal` | Driver assistance computer: w173 r pillar cam ext not cal | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w174_lRepeatCamExtNotCal` | Driver assistance computer: w174 l repeat cam ext not cal | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w175_rRepeatCamExtNotCal` | Driver assistance computer: w175 r repeat cam ext not cal | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w177_fisheyeCamCalSaved` | Driver assistance computer: w177 fisheye cam cal saved | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w178_lPillarCamCalSaved` | Driver assistance computer: w178 l pillar cam cal saved | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w179_rPillarCamCalSaved` | Driver assistance computer: w179 r pillar cam cal saved | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w180_lRepeatCamCalSaved` | Driver assistance computer: w180 l repeat cam cal saved | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w181_rRepeatCamCalSaved` | Driver assistance computer: w181 r repeat cam cal saved | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
