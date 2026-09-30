---
layout: default
title: "APP_warningMatrix2 (0x429) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix2. Tesla Model Y CAN bus message APP_warningMatrix2 (0x429) of Driver assistance computer (primary), firmware 2025.20.8, 64 signals (APP_w129_mainCamExtNotCal, APP_w130_narrowCamExtNotCal, APP_w131_mainCamCalSaved, APP_w132_narrowCamCalSaved and 60 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix2 (0x429) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: warning matrix2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 64 signals of APP_warningMatrix2 as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix2` |
| CAN id | 0x429 (1065) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of APP_warningMatrix2

Tesla Model Y CAN bus signals in `APP_warningMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w129_mainCamExtNotCal` | Driver assistance computer (primary): w129 main cam ext not cal | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w130_narrowCamExtNotCal` | Driver assistance computer (primary): w130 narrow cam ext not cal | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w131_mainCamCalSaved` | Driver assistance computer (primary): w131 main cam cal saved | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w132_narrowCamCalSaved` | Driver assistance computer (primary): w132 narrow cam cal saved | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w133_mainCamInitFault` | Driver assistance computer (primary): w133 main cam init fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w134_narrowCamInitFault` | Driver assistance computer (primary): w134 narrow cam init fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w135_fisheyeCamInitFault` | Driver assistance computer (primary): w135 fisheye cam init fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w136_lPillarCamInitFault` | Driver assistance computer (primary): w136 l pillar cam init fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w137_rPillarCamInitFault` | Driver assistance computer (primary): w137 r pillar cam init fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w138_lRepeatCamInitFault` | Driver assistance computer (primary): w138 l repeat cam init fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w139_rRepeatCamInitFault` | Driver assistance computer (primary): w139 r repeat cam init fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w140_backupCamInitFault` | Driver assistance computer (primary): w140 backup cam init fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w141_ECU_Thermal_Issue` | Driver assistance computer (primary): w141 ECU thermal issue | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w142_fwdCamPitchProblem` | Driver assistance computer (primary): w142 fwd cam pitch problem | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w143_IDF_event` | Driver assistance computer (primary): w143 IDF event | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w144_fanctrldError` | Driver assistance computer (primary): w144 fanctrld error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w145_camSelfCalIssue` | Driver assistance computer (primary): w145 cam self cal issue | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w146_telemetryProblem` | Driver assistance computer (primary): w146 telemetry problem | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w147_selfieCamInitFault` | Driver assistance computer (primary): w147 selfie cam init fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w148_overlayActive` | Driver assistance computer (primary): w148 overlay active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w149_diskFull` | Driver assistance computer (primary): w149 disk full | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w150_diMiaPartyBus` | Driver assistance computer (primary): w150 di mia party bus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w151_epasMiaPartyBus` | Driver assistance computer (primary): w151 epas mia party bus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w152_espMiaPartyBus` | Driver assistance computer (primary): w152 esp mia party bus | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w153_rcmMiaPartyBus` | Driver assistance computer (primary): w153 rcm mia party bus | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w154_vcleftMiaPartyBus` | Driver assistance computer (primary): w154 vcleft mia party bus | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w155_vcrightMiaPartyBus` | Driver assistance computer (primary): w155 vcright mia party bus | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w156_epblMiaVehBus` | Driver assistance computer (primary): w156 epbl mia veh bus | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w157_sccmMiaVehBus` | Driver assistance computer (primary): w157 sccm mia veh bus | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w158_vcfrontMiaVehBus` | Driver assistance computer (primary): w158 vcfront mia veh bus | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w159_vcleftMiaVehBus` | Driver assistance computer (primary): w159 vcleft mia veh bus | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w160_vcrightMiaVehBus` | Driver assistance computer (primary): w160 vcright mia veh bus | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w161_backupCameraUnavailable` | Driver assistance computer (primary): w161 backup camera unavailable | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w162_mainCameraTypeError` | Driver assistance computer (primary): w162 main camera type error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w163_narrowCameraTypeError` | Driver assistance computer (primary): w163 narrow camera type error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w164_fisheyeCameraTypeError` | Driver assistance computer (primary): w164 fisheye camera type error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w165_lPillarCameraTypeError` | Driver assistance computer (primary): w165 l pillar camera type error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w166_rPillarCameraTypeError` | Driver assistance computer (primary): w166 r pillar camera type error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w167_lRepeatCameraTypeError` | Driver assistance computer (primary): w167 l repeat camera type error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w168_rRepeatCameraTypeError` | Driver assistance computer (primary): w168 r repeat camera type error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w169_backupCameraTypeError` | Driver assistance computer (primary): w169 backup camera type error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w170_selfieCameraTypeError` | Driver assistance computer (primary): w170 selfie camera type error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w171_appHighCoolantFlowReq` | Driver assistance computer (primary): w171 app high coolant flow req | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w172_fisheyeCamExtNotCal` | Driver assistance computer (primary): w172 fisheye cam ext not cal | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w173_lPillarCamExtNotCal` | Driver assistance computer (primary): w173 l pillar cam ext not cal | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w174_rPillarCamExtNotCal` | Driver assistance computer (primary): w174 r pillar cam ext not cal | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w175_lRepeatCamExtNotCal` | Driver assistance computer (primary): w175 l repeat cam ext not cal | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w176_rRepeatCamExtNotCal` | Driver assistance computer (primary): w176 r repeat cam ext not cal | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w177_fisheyeCamCalSaved` | Driver assistance computer (primary): w177 fisheye cam cal saved | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w178_lPillarCamCalSaved` | Driver assistance computer (primary): w178 l pillar cam cal saved | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w179_rPillarCamCalSaved` | Driver assistance computer (primary): w179 r pillar cam cal saved | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w180_lRepeatCamCalSaved` | Driver assistance computer (primary): w180 l repeat cam cal saved | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w181_rRepeatCamCalSaved` | Driver assistance computer (primary): w181 r repeat cam cal saved | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w182_mainCameraStreamExit` | Driver assistance computer (primary): w182 main camera stream exit | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w183_narrowCameraStreamExit` | Driver assistance computer (primary): w183 narrow camera stream exit | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w184_fisheyeCameraStreamExit` | Driver assistance computer (primary): w184 fisheye camera stream exit | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w185_lPillarCameraStreamExit` | Driver assistance computer (primary): w185 l pillar camera stream exit | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w186_rPillarCameraStreamExit` | Driver assistance computer (primary): w186 r pillar camera stream exit | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w187_lRepeatCameraStreamExit` | Driver assistance computer (primary): w187 l repeat camera stream exit | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w188_rRepeatCameraStreamExit` | Driver assistance computer (primary): w188 r repeat camera stream exit | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w189_backupCameraStreamExit` | Driver assistance computer (primary): w189 backup camera stream exit | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w190_selfieCameraStreamExit` | Driver assistance computer (primary): w190 selfie camera stream exit | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w191_autopilotAborting` | Driver assistance computer (primary): w191 autopilot aborting | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w192_emergencySpeakerFail` | Driver assistance computer (primary): w192 emergency speaker fail | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
