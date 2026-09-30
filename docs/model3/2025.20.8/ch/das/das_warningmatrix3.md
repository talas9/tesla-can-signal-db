---
layout: default
title: "DAS_warningMatrix3 (0x43A) — Driver assistance computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer message: warning matrix3. Tesla Model 3 CAN bus message DAS_warningMatrix3 (0x43A) of Driver assistance computer, firmware 2025.20.8, 40 signals (DAS_w193_camWindshieldUnclean, DAS_w194_accDriverResumeRqrd, DAS_w195_scwUnavailable, DAS_w196_stopSignWarning and 36 more). Bit layout, scaling, units and value tables."
---

# DAS_warningMatrix3 (0x43A) — Driver assistance computer, Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer message: warning matrix3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 40 signals of DAS_warningMatrix3 as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_warningMatrix3` |
| CAN id | 0x43A (1082) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 40 |

## Signals of DAS_warningMatrix3

Tesla Model 3 CAN bus signals in `DAS_warningMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_w193_camWindshieldUnclean` | Driver assistance computer: w193 cam windshield unclean | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w194_accDriverResumeRqrd` | Driver assistance computer: w194 acc driver resume rqrd | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w195_scwUnavailable` | Driver assistance computer: w195 scw unavailable | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w196_stopSignWarning` | Driver assistance computer: w196 stop sign warning | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w197_redLightWarning` | Driver assistance computer: w197 red light warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w198_tsrUnavailable` | Driver assistance computer: w198 tsr unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w199_apcAbort` | Driver assistance computer: w199 apc abort | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w200_lcSlowdown` | Driver assistance computer: w200 lc slowdown | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w201_lcAborting` | Driver assistance computer: w201 lc aborting | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w202_scwNoisyEnvironment` | Driver assistance computer: w202 scw noisy environment | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w203_apcActivation` | Driver assistance computer: w203 apc activation | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w204_apcFinalFront` | Driver assistance computer: w204 apc final front | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w205_apcFinalRear` | Driver assistance computer: w205 apc final rear | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w206_autosteerNotEnabled` | Driver assistance computer: w206 autosteer not enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w207_autosteerUnavailable` | Driver assistance computer: w207 autosteer unavailable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w208_rackDetected` | Driver assistance computer: w208 rack detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w209_autoSummonRequest` | Driver assistance computer: w209 auto summon request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w210_camObstrcted` | Driver assistance computer: w210 cam obstrcted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w211_accNoSeatBelt` | Driver assistance computer: w211 acc no seat belt | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w212_lcUnavailableStrikeOut` | Driver assistance computer: w212 lc unavailable strike out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w213_autosteerStruckOut` | Driver assistance computer: w213 autosteer struck out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w214_driverNotIntracting` | Driver assistance computer: w214 driver not intracting | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w215_contDriverNotIntracting` | Driver assistance computer: w215 cont driver not intracting | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w216_driverOverriding` | Driver assistance computer: w216 driver overriding | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w217_lcUnavailableSpeeding` | Driver assistance computer: w217 lc unavailable speeding | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w218_lcSpeedExceededLimit` | Driver assistance computer: w218 lc speed exceeded limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w219_lcTempUnavailableSpeed` | Driver assistance computer: w219 lc temp unavailable speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w220_lcTempUnavailableRoad` | Driver assistance computer: w220 lc temp unavailable road | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w221_accRadarBlind` | Driver assistance computer: w221 acc radar blind | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w222_accCameraBlind` | Driver assistance computer: w222 acc camera blind | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w223_accObjectInPath` | Driver assistance computer: w223 acc object in path | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w224_accCameraCalibration` | Driver assistance computer: w224 acc camera calibration | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w225_lcDegradedVisSpeedLmt` | Driver assistance computer: w225 lc degraded vis speed lmt | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w226_lcCamCalNeededSpeedLmt` | Driver assistance computer: w226 lc cam cal needed speed lmt | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w227_virtualWallBlocked` | Driver assistance computer: w227 virtual wall blocked | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w228_DEPRECATED` | Driver assistance computer: w228 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w229_alcUltrasoundDamaged` | Driver assistance computer: w229 alc ultrasound damaged | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w230_alcUltrasoundBlocked` | Driver assistance computer: w230 alc ultrasound blocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w231_idfEvent` | Driver assistance computer: w231 idf event | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w232_laneChangeRequested` | Driver assistance computer: w232 lane change requested | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
