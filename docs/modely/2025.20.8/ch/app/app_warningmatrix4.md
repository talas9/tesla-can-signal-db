---
layout: default
title: "APP_warningMatrix4 (0x449) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix4. Tesla Model Y CAN bus message APP_warningMatrix4 (0x449) of Driver assistance computer (primary), firmware 2025.20.8, 63 signals (APP_w257_brakeJerkEvent, APP_w258_aebEvent, APP_w259_aebOverrideEvent, APP_w260_collisionWarningEvent and 59 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix4 (0x449) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: warning matrix4; frame length from the layout, not yet observed on a vehicle bus. This page documents the 63 signals of APP_warningMatrix4 as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix4` |
| CAN id | 0x449 (1097) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of APP_warningMatrix4

Tesla Model Y CAN bus signals in `APP_warningMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w257_brakeJerkEvent` | Driver assistance computer (primary): w257 brake jerk event | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w258_aebEvent` | Driver assistance computer (primary): w258 aeb event | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w259_aebOverrideEvent` | Driver assistance computer (primary): w259 aeb override event | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w260_collisionWarningEvent` | Driver assistance computer (primary): w260 collision warning event | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w261_pcieHardwareErrors` | Driver assistance computer (primary): w261 pcie hardware errors | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w262_apeCalibMode` | Driver assistance computer (primary): w262 ape calib mode | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w263_lssAbort` | Driver assistance computer (primary): w263 lss abort | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w264_lssFault` | Driver assistance computer (primary): w264 lss fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w265_drvOnNavUnavailable` | Driver assistance computer (primary): w265 drv on nav unavailable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w266_visionScheduleFallback` | Driver assistance computer (primary): w266 vision schedule fallback | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w267_benchtopEcu` | Driver assistance computer (primary): w267 benchtop ecu | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w268_backupCamExtNotCal` | Driver assistance computer (primary): w268 backup cam ext not cal | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w269_autopilotLimited` | Driver assistance computer (primary): w269 autopilot limited | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w270_blindspotRestricted` | Driver assistance computer (primary): w270 blindspot restricted | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w271_laneChangeAborted` | Driver assistance computer (primary): w271 lane change aborted | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w272_laneChangeUnavailable` | Driver assistance computer (primary): w272 lane change unavailable | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w273_lssEvent` | Driver assistance computer (primary): w273 lss event | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w274_mainCameraStreamErr` | Driver assistance computer (primary): w274 main camera stream err | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w275_narrowCameraStreamErr` | Driver assistance computer (primary): w275 narrow camera stream err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w276_fisheyeCameraStreamErr` | Driver assistance computer (primary): w276 fisheye camera stream err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w277_lPillarCameraStreamErr` | Driver assistance computer (primary): w277 l pillar camera stream err | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w278_rPillarCameraStreamErr` | Driver assistance computer (primary): w278 r pillar camera stream err | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w279_lRepeatCameraStreamErr` | Driver assistance computer (primary): w279 l repeat camera stream err | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w280_rRepeatCameraStreamErr` | Driver assistance computer (primary): w280 r repeat camera stream err | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w281_backupCameraStreamErr` | Driver assistance computer (primary): w281 backup camera stream err | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w282_selfieCameraStreamErr` | Driver assistance computer (primary): w282 selfie camera stream err | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w283_enhancedSummonAbort` | Driver assistance computer (primary): w283 enhanced summon abort | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w284_gpsAntennaDisconnected` | Driver assistance computer (primary): w284 gps antenna disconnected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w285_gpsFaultReset` | Driver assistance computer (primary): w285 gps fault reset | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w286_gpsComIssue` | Driver assistance computer (primary): w286 gps com issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w287_gpsFusionStatus` | Driver assistance computer (primary): w287 gps fusion status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w288_trafficLightWarning` | Driver assistance computer (primary): w288 traffic light warning | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w289_dramCorrEccErrors` | Driver assistance computer (primary): w289 dram corr ecc errors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w290_dramUncorrEccErrors` | Driver assistance computer (primary): w290 dram uncorr ecc errors | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w291_stopSignWarning` | Driver assistance computer (primary): w291 stop sign warning | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w293_mainCameraSyncFailed` | Driver assistance computer (primary): w293 main camera sync failed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w294_narrowCameraSyncFailed` | Driver assistance computer (primary): w294 narrow camera sync failed | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w295_fisheyeCameraSyncFailed` | Driver assistance computer (primary): w295 fisheye camera sync failed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w296_lPillarCameraSyncFailed` | Driver assistance computer (primary): w296 l pillar camera sync failed | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w297_rPillarCameraSyncFailed` | Driver assistance computer (primary): w297 r pillar camera sync failed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w298_lRepeatCameraSyncFailed` | Driver assistance computer (primary): w298 l repeat camera sync failed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w299_rRepeatCameraSyncFailed` | Driver assistance computer (primary): w299 r repeat camera sync failed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w300_backupCameraSyncFailed` | Driver assistance computer (primary): w300 backup camera sync failed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w301_selfieCameraSyncFailed` | Driver assistance computer (primary): w301 selfie camera sync failed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w302_vcfrontMiaPartyBus` | Driver assistance computer (primary): w302 vcfront mia party bus | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w303_imuIrational` | Driver assistance computer (primary): w303 imu irational | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w304_lssCamBlockedStatus` | Driver assistance computer (primary): w304 lss cam blocked status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w305_lssCamStreamExit` | Driver assistance computer (primary): w305 lss cam stream exit | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w306_lssUltrasonicsBlocked` | Driver assistance computer (primary): w306 lss ultrasonics blocked | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w307_lssTurnSignalFault` | Driver assistance computer (primary): w307 lss turn signal fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w308_iboosterMia` | Driver assistance computer (primary): w308 ibooster mia | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w309_selfieDisabledOnCar` | Driver assistance computer (primary): w309 selfie disabled on car | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w310_eth0FrameErrors` | Driver assistance computer (primary): w310 eth0 frame errors | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w311_eth1FrameErrors` | Driver assistance computer (primary): w311 eth1 frame errors | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w312_mainCamTypeMismatch` | Driver assistance computer (primary): w312 main cam type mismatch | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w313_narrowCamTypeMismatch` | Driver assistance computer (primary): w313 narrow cam type mismatch | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w314_fisheyeCamTypeMismatch` | Driver assistance computer (primary): w314 fisheye cam type mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w315_lPillarCamTypeMismatch` | Driver assistance computer (primary): w315 l pillar cam type mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w316_rPillarCamTypeMismatch` | Driver assistance computer (primary): w316 r pillar cam type mismatch | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w317_lRepeatCamTypeMismatch` | Driver assistance computer (primary): w317 l repeat cam type mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w318_rRepeatCamTypeMismatch` | Driver assistance computer (primary): w318 r repeat cam type mismatch | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w319_backupCamTypeMismatch` | Driver assistance computer (primary): w319 backup cam type mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w320_selfieCamTypeMismatch` | Driver assistance computer (primary): w320 selfie cam type mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
