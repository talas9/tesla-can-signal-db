---
layout: default
title: "APP_warningMatrix6 (0x47D) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix6. Tesla Model Y CAN bus message APP_warningMatrix6 (0x47D) of Driver assistance computer (primary), firmware 2026.26.6.5, 63 signals (APP_w385_posEngineUnhealthy, APP_w386_radarOnlyBrakingEvent, APP_w387_radarBlockageDetected, APP_w388_windshieldCameraHeaterFaulted and 59 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix6 (0x47D) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: warning matrix6; frame length from the layout, not yet observed on a vehicle bus. This page documents the 63 signals of APP_warningMatrix6 as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix6` |
| CAN id | 0x47D (1149) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of APP_warningMatrix6

Tesla Model Y CAN bus signals in `APP_warningMatrix6`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w385_posEngineUnhealthy` | Driver assistance computer (primary): w385 pos engine unhealthy | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w386_radarOnlyBrakingEvent` | Driver assistance computer (primary): w386 radar only braking event | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w387_radarBlockageDetected` | Driver assistance computer (primary): w387 radar blockage detected | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w388_windshieldCameraHeaterFaulted` | Driver assistance computer (primary): w388 windshield camera heater faulted | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w389_camFovResidueDetected` | Driver assistance computer (primary): w389 cam fov residue detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w390_cabinCamVisDegraded` | Driver assistance computer (primary): w390 cabin cam vis degraded | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w391_cabinCameraBlockedonAP` | Driver assistance computer (primary): w391 cabin camera blockedon AP | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w392_fsdSuspended` | Driver assistance computer (primary): w392 fsd suspended | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w393_attnMntrUnavailable` | Driver assistance computer (primary): w393 attn mntr unavailable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w394_apImuGrossErrors` | Driver assistance computer (primary): w394 ap imu gross errors | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w395_cabinCameraLEDFaultSvc` | Driver assistance computer (primary): w395 cabin camera LED fault svc | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w396_severeResidueDetected` | Driver assistance computer (primary): w396 severe residue detected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w397_apFeatDisabledPermanent` | Driver assistance computer (primary): w397 ap feat disabled permanent | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w398_imuOutputUnhealthy` | Driver assistance computer (primary): w398 imu output unhealthy | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w399_brakeboosterMia` | Driver assistance computer (primary): w399 brakebooster mia | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w400_selfieCameraFanFault` | Driver assistance computer (primary): w400 selfie camera fan fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w401_leftPillarCameraHeaterFaulted` | Driver assistance computer (primary): w401 left pillar camera heater faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w402_rightPillarCameraHeaterFaulted` | Driver assistance computer (primary): w402 right pillar camera heater faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w403_notifyCameraSelfCleanAction` | Driver assistance computer (primary): w403 notify camera self clean action | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w404_epbrMiaVehBus` | Driver assistance computer (primary): w404 epbr mia veh bus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w405_apsMia` | Driver assistance computer (primary): w405 aps mia | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w406_gnssHWHealthDegraded` | Driver assistance computer (primary): w406 gnss HW health degraded | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w407_autonomyDegraded1` | Driver assistance computer (primary): w407 autonomy degraded1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w408_autonomyDegraded2` | Driver assistance computer (primary): w408 autonomy degraded2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w409_autonomyDegraded3` | Driver assistance computer (primary): w409 autonomy degraded3 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w410_autonomyDegraded4` | Driver assistance computer (primary): w410 autonomy degraded4 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w411_backupCameraOccluded` | Driver assistance computer (primary): w411 backup camera occluded | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w412_abortBackupCamOccluded` | Driver assistance computer (primary): w412 abort backup cam occluded | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w413_autonomyDegraded5` | Driver assistance computer (primary): w413 autonomy degraded5 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w415_autonomyUnavailableSystem` | Driver assistance computer (primary): w415 autonomy unavailable system | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w416_autonomyDegradedSystem` | Driver assistance computer (primary): w416 autonomy degraded system | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w417_autonomyUnavailableVisibility` | Driver assistance computer (primary): w417 autonomy unavailable visibility | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w418_autonomyDegradedVisibility` | Driver assistance computer (primary): w418 autonomy degraded visibility | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w419_autonomyUnavailableApSystem` | Driver assistance computer (primary): w419 autonomy unavailable ap system | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w420_autonomyDegradedApSystem` | Driver assistance computer (primary): w420 autonomy degraded ap system | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w421_autonomyUnavailableUser` | Driver assistance computer (primary): w421 autonomy unavailable user | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w422_autonomyDegradedUser` | Driver assistance computer (primary): w422 autonomy degraded user | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w423_cameraVisPopUpForward` | Driver assistance computer (primary): w423 camera vis pop up forward | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w424_cameraVisPopUpLPillar` | Driver assistance computer (primary): w424 camera vis pop up l pillar | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w425_cameraVisPopUpRPillar` | Driver assistance computer (primary): w425 camera vis pop up r pillar | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w426_cameraVisPopUpLRepeater` | Driver assistance computer (primary): w426 camera vis pop up l repeater | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w427_cameraVisPopUpRRepeater` | Driver assistance computer (primary): w427 camera vis pop up r repeater | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w428_cameraVisPopUpBackup` | Driver assistance computer (primary): w428 camera vis pop up backup | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w429_cameraVisPopUpFascia` | Driver assistance computer (primary): w429 camera vis pop up fascia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w430_frontVisibilityDegraded_LOW` | Driver assistance computer (primary): w430 front visibility degraded LOW | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w431_frontVisibilityDegraded_MEDIUM` | Driver assistance computer (primary): w431 front visibility degraded MEDIUM | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w432_frontVisibilityDegraded_HIGH` | Driver assistance computer (primary): w432 front visibility degraded HIGH | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w433_leftRepeaterDowngradeDetected` | Driver assistance computer (primary): w433 left repeater downgrade detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w434_rightRepeaterDowngradeDetected` | Driver assistance computer (primary): w434 right repeater downgrade detected | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w435_repeaterAeroRibInfoMismatched` | Driver assistance computer (primary): w435 repeater aero rib info mismatched | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w436_camCsiError` | Driver assistance computer (primary): w436 cam csi error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w437_missingCloudEepromData` | Driver assistance computer (primary): w437 missing cloud eeprom data | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w438_rcuMia` | Driver assistance computer (primary): w438 rcu mia | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w439_ethernetCommFailure` | Driver assistance computer (primary): w439 ethernet comm failure | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w440_lensHoodOcclusion` | Driver assistance computer (primary): w440 lens hood occlusion | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w441_cabinCamLEDRailOff` | Driver assistance computer (primary): w441 cabin cam LED rail off | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w442_autonomyCancelMethod` | Driver assistance computer (primary): w442 autonomy cancel method | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w443_mainImagerConfigMismatch` | Driver assistance computer (primary): w443 main imager config mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w444_narrowImagerConfigMismatch` | Driver assistance computer (primary): w444 narrow imager config mismatch | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w445_fisheyeImagerConfigMismatch` | Driver assistance computer (primary): w445 fisheye imager config mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w446_leftPillarImagerConfigMismatch` | Driver assistance computer (primary): w446 left pillar imager config mismatch | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w447_rightPillarImagerConfigMismatch` | Driver assistance computer (primary): w447 right pillar imager config mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w448_leftRepeaterImagerConfigMismatch` | Driver assistance computer (primary): w448 left repeater imager config mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
