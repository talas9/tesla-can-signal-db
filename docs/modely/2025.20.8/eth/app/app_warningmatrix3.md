---
layout: default
title: "APP_warningMatrix3 (0x439) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: warning matrix3. Ethernet-side message APP_warningMatrix3 of Driver assistance computer (primary) for Tesla Model Y firmware 2025.20.8, 41 signals (APP_w193_camWindshieldUnclean, APP_w194_accDriverResumeRqrd, APP_w195_scwUnavailable, APP_w196_stopSignWarning and 37 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix3 (0x439) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: warning matrix3. This page documents the 41 signals of APP_warningMatrix3 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix3` |
| Ethernet-side id | 0x439 (1081) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 41 |

## Signals of APP_warningMatrix3

Tesla Model Y CAN bus signals in `APP_warningMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w193_camWindshieldUnclean` | Driver assistance computer (primary): w193 cam windshield unclean | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w194_accDriverResumeRqrd` | Driver assistance computer (primary): w194 acc driver resume rqrd | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w195_scwUnavailable` | Driver assistance computer (primary): w195 scw unavailable | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w196_stopSignWarning` | Driver assistance computer (primary): w196 stop sign warning | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w197_redLightWarning` | Driver assistance computer (primary): w197 red light warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w198_tsrUnavailable` | Driver assistance computer (primary): w198 tsr unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w199_apcAbort` | Driver assistance computer (primary): w199 apc abort | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w200_lcSlowdown` | Driver assistance computer (primary): w200 lc slowdown | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w201_lcAborting` | Driver assistance computer (primary): w201 lc aborting | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w202_scwNoisyEnvironment` | Driver assistance computer (primary): w202 scw noisy environment | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w203_apcActivation` | Driver assistance computer (primary): w203 apc activation | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w204_apcFinalFront` | Driver assistance computer (primary): w204 apc final front | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w205_apcFinalRear` | Driver assistance computer (primary): w205 apc final rear | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w206_autosteerNotEnabled` | Driver assistance computer (primary): w206 autosteer not enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w207_autosteerUnavailable` | Driver assistance computer (primary): w207 autosteer unavailable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w208_rackDetected` | Driver assistance computer (primary): w208 rack detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w209_autoSummonRequest` | Driver assistance computer (primary): w209 auto summon request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w210_camObstrcted` | Driver assistance computer (primary): w210 cam obstrcted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w211_accNoSeatBelt` | Driver assistance computer (primary): w211 acc no seat belt | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w212_lcUnavailableStrikeOut` | Driver assistance computer (primary): w212 lc unavailable strike out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w213_autosteerStruckOut` | Driver assistance computer (primary): w213 autosteer struck out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w214_driverNotIntracting` | Driver assistance computer (primary): w214 driver not intracting | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w215_contDriverNotIntracting` | Driver assistance computer (primary): w215 cont driver not intracting | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w216_driverOverriding` | Driver assistance computer (primary): w216 driver overriding | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w217_lcUnavailableSpeeding` | Driver assistance computer (primary): w217 lc unavailable speeding | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w218_lcSpeedExceededLimit` | Driver assistance computer (primary): w218 lc speed exceeded limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w219_lcTempUnavailableSpeed` | Driver assistance computer (primary): w219 lc temp unavailable speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w220_lcTempUnavailableRoad` | Driver assistance computer (primary): w220 lc temp unavailable road | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w221_accRadarBlind` | Driver assistance computer (primary): w221 acc radar blind | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w222_accCameraBlind` | Driver assistance computer (primary): w222 acc camera blind | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w223_accObjectInPath` | Driver assistance computer (primary): w223 acc object in path | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w224_accCameraCalibration` | Driver assistance computer (primary): w224 acc camera calibration | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w225_lcDegradedVisSpeedLmt` | Driver assistance computer (primary): w225 lc degraded vis speed lmt | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w226_lcCamCalNeededSpeedLmt` | Driver assistance computer (primary): w226 lc cam cal needed speed lmt | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w227_virtualWallBlocked` | Driver assistance computer (primary): w227 virtual wall blocked | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w228_DEPRECATED` | Driver assistance computer (primary): w228 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w229_alcUltrasoundDamaged` | Driver assistance computer (primary): w229 alc ultrasound damaged | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w230_alcUltrasoundBlocked` | Driver assistance computer (primary): w230 alc ultrasound blocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w231_idfEvent` | Driver assistance computer (primary): w231 idf event | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w232_laneChangeRequested` | Driver assistance computer (primary): w232 lane change requested | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w234_activeSafetyTelemetry` | Driver assistance computer (primary): w234 active safety telemetry | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
