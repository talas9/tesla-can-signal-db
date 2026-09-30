---
layout: default
title: "APP_warningMatrix5 (0x47F) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix5. Tesla Model 3 / Model Y CAN bus message APP_warningMatrix5 (0x47F) of Driver assistance computer (primary), firmware 2026.26.6.5, 64 signals (APP_w321_bmsMia, APP_w322_autoWiperWash, APP_w323_drivableSpaceFCW, APP_w324_adspMia and 60 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix5 (0x47F) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: warning matrix5; frame length from the layout, not yet observed on a vehicle bus. This page documents the 64 signals of APP_warningMatrix5 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix5` |
| CAN id | 0x47F (1151) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of APP_warningMatrix5

Tesla Model 3 / Model Y CAN bus signals in `APP_warningMatrix5`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w321_bmsMia` | Driver assistance computer (primary): w321 bms mia | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w322_autoWiperWash` | Driver assistance computer (primary): w322 auto wiper wash | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w323_drivableSpaceFCW` | Driver assistance computer (primary): w323 drivable space FCW | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w324_adspMia` | Driver assistance computer (primary): w324 adsp mia | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w325_watchdogReset` | Driver assistance computer (primary): w325 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w326_kernelPanic` | Driver assistance computer (primary): w326 kernel panic | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w327_vehicleConfigMismatch` | Driver assistance computer (primary): w327 vehicle config mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w328_autoparkDegraded` | Driver assistance computer (primary): w328 autopark degraded | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w329_evasiveManeuver` | Driver assistance computer (primary): w329 evasive maneuver | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w330_cabinCameraFault` | Driver assistance computer (primary): w330 cabin camera fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w331_fsdDegradedUnavailable` | Driver assistance computer (primary): w331 fsd degraded unavailable | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w332_cameraPositionsSwapped` | Driver assistance computer (primary): w332 camera positions swapped | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w333_fsdUnavailableLocation` | Driver assistance computer (primary): w333 fsd unavailable location | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w334_frontCameraOccluded` | Driver assistance computer (primary): w334 front camera occluded | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w335_tradfcRfSensorError` | Driver assistance computer (primary): w335 tradfc rf sensor error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w336_tradfcLfPmicError` | Driver assistance computer (primary): w336 tradfc lf pmic error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w337_tradfcRfPmicError` | Driver assistance computer (primary): w337 tradfc rf pmic error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w338_tradfcLfTempError` | Driver assistance computer (primary): w338 tradfc lf temp error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w339_tradfcRfTempError` | Driver assistance computer (primary): w339 tradfc rf temp error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w340_tradfcCsiError` | Driver assistance computer (primary): w340 tradfc csi error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w341_tradfcCalibError` | Driver assistance computer (primary): w341 tradfc calib error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w342_tradfcDspHwError` | Driver assistance computer (primary): w342 tradfc dsp hw error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w343_tradfcDspSwError` | Driver assistance computer (primary): w343 tradfc dsp sw error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w344_tradfcDspAlgoTimeout` | Driver assistance computer (primary): w344 tradfc dsp algo timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w345_tradfcPerfDegraded` | Driver assistance computer (primary): w345 tradfc perf degraded | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w346_gpsSwEvent` | Driver assistance computer (primary): w346 gps sw event | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w347_vcbattMiaVehBus` | Driver assistance computer (primary): w347 vcbatt mia veh bus | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w348_cameraSwUpdateRequired` | Driver assistance computer (primary): w348 camera sw update required | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w349_cameraPersistentlyFaulted` | Driver assistance computer (primary): w349 camera persistently faulted | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w350_tradfcSensorMisaligned` | Driver assistance computer (primary): w350 tradfc sensor misaligned | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w351_csiDevice0Down` | Driver assistance computer (primary): w351 csi device0 down | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w352_csiDevice1Down` | Driver assistance computer (primary): w352 csi device1 down | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w353_csiDevice2Down` | Driver assistance computer (primary): w353 csi device2 down | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w354_tradfcMia` | Driver assistance computer (primary): w354 tradfc mia | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w355_camQuadPowerFault` | Driver assistance computer (primary): w355 cam quad power fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w356_driverOverriding` | Driver assistance computer (primary): w356 driver overriding | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w357_ddawSystemFault` | Driver assistance computer (primary): w357 ddaw system fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w358_isaSystemFault` | Driver assistance computer (primary): w358 isa system fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w359_aebDegraded` | Driver assistance computer (primary): w359 aeb degraded | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w360_apImuNoiseDetected` | Driver assistance computer (primary): w360 ap imu noise detected | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w361_cabinCameraLEDFault` | Driver assistance computer (primary): w361 cabin camera LED fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w362_fasciaCamInitFault` | Driver assistance computer (primary): w362 fascia cam init fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w363_fasciaCameraStreamExit` | Driver assistance computer (primary): w363 fascia camera stream exit | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w364_fasciaCameraTypeError` | Driver assistance computer (primary): w364 fascia camera type error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w365_fasciaCamExtNotCal` | Driver assistance computer (primary): w365 fascia cam ext not cal | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w366_fasciaCameraSyncFailed` | Driver assistance computer (primary): w366 fascia camera sync failed | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w367_fasciaCamCalSaved` | Driver assistance computer (primary): w367 fascia cam cal saved | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w368_fasciaCamTypeMismatch` | Driver assistance computer (primary): w368 fascia cam type mismatch | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w369_cruiseWithSingleClick` | Driver assistance computer (primary): w369 cruise with single click | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w370_accApUnavUserSettings` | Driver assistance computer (primary): w370 acc ap unav user settings | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w371_networkLoadingIssue` | Driver assistance computer (primary): w371 network loading issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w372_cabinCameraBlocked` | Driver assistance computer (primary): w372 cabin camera blocked | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w373_gnssUartError` | Driver assistance computer (primary): w373 gnss uart error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w374_gnssDataMia` | Driver assistance computer (primary): w374 gnss data mia | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w375_gnssPpsMia` | Driver assistance computer (primary): w375 gnss pps mia | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w376_wheeltickCountMia` | Driver assistance computer (primary): w376 wheeltick count mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w377_apImuMia` | Driver assistance computer (primary): w377 ap imu mia | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w378_ubloxImuMia` | Driver assistance computer (primary): w378 ublox imu mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w379_positioningEngineMia` | Driver assistance computer (primary): w379 positioning engine mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w380_gnssPpsTimestampIssue` | Driver assistance computer (primary): w380 gnss pps timestamp issue | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w381_apImuTimestampIssue` | Driver assistance computer (primary): w381 ap imu timestamp issue | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w382_ubloxImuTimestampIssue` | Driver assistance computer (primary): w382 ublox imu timestamp issue | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w383_manyApRebootsWhileInP` | Driver assistance computer (primary): w383 many ap reboots while in p | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w384_posEngineInitInMotion` | Driver assistance computer (primary): w384 pos engine init in motion | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
