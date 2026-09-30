---
layout: default
title: "APS_warningMatrix3 (0x350) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (secondary) message: warning matrix3. Tesla Model 3 CAN bus message APS_warningMatrix3 (0x350) of Driver assistance computer (secondary), firmware 2025.20.8, 59 signals (APS_w193_camWindshieldUnclean, APS_w194_accDriverResumeRqrd, APS_w195_scwUnavailable, APS_w196_stopSignWarning and 55 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix3 (0x350) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (secondary) message: warning matrix3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 59 signals of APS_warningMatrix3 as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix3` |
| CAN id | 0x350 (848) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 59 |

## Signals of APS_warningMatrix3

Tesla Model 3 CAN bus signals in `APS_warningMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_w193_camWindshieldUnclean` | Driver assistance computer (secondary): w193 cam windshield unclean | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w194_accDriverResumeRqrd` | Driver assistance computer (secondary): w194 acc driver resume rqrd | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w195_scwUnavailable` | Driver assistance computer (secondary): w195 scw unavailable | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w196_stopSignWarning` | Driver assistance computer (secondary): w196 stop sign warning | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w197_redLightWarning` | Driver assistance computer (secondary): w197 red light warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w198_tsrUnavailable` | Driver assistance computer (secondary): w198 tsr unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w199_apcAbort` | Driver assistance computer (secondary): w199 apc abort | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w200_lcSlowdown` | Driver assistance computer (secondary): w200 lc slowdown | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w201_lcAborting` | Driver assistance computer (secondary): w201 lc aborting | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w202_scwNoisyEnvironment` | Driver assistance computer (secondary): w202 scw noisy environment | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w203_apcActivation` | Driver assistance computer (secondary): w203 apc activation | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w204_apcFinalFront` | Driver assistance computer (secondary): w204 apc final front | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w205_apcFinalRear` | Driver assistance computer (secondary): w205 apc final rear | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w206_autosteerNotEnabled` | Driver assistance computer (secondary): w206 autosteer not enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w207_autosteerUnavailable` | Driver assistance computer (secondary): w207 autosteer unavailable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w208_rackDetected` | Driver assistance computer (secondary): w208 rack detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w209_autoSummonRequest` | Driver assistance computer (secondary): w209 auto summon request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w210_camObstrcted` | Driver assistance computer (secondary): w210 cam obstrcted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w211_accNoSeatBelt` | Driver assistance computer (secondary): w211 acc no seat belt | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w212_lcUnavailableStrikeOut` | Driver assistance computer (secondary): w212 lc unavailable strike out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w213_autosteerStruckOut` | Driver assistance computer (secondary): w213 autosteer struck out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w214_driverNotIntracting` | Driver assistance computer (secondary): w214 driver not intracting | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w215_contDriverNotIntracting` | Driver assistance computer (secondary): w215 cont driver not intracting | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w216_driverOverriding` | Driver assistance computer (secondary): w216 driver overriding | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w217_lcUnavailableSpeeding` | Driver assistance computer (secondary): w217 lc unavailable speeding | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w218_lcSpeedExceededLimit` | Driver assistance computer (secondary): w218 lc speed exceeded limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w219_lcTempUnavailableSpeed` | Driver assistance computer (secondary): w219 lc temp unavailable speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w220_lcTempUnavailableRoad` | Driver assistance computer (secondary): w220 lc temp unavailable road | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w221_accRadarBlind` | Driver assistance computer (secondary): w221 acc radar blind | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w222_accCameraBlind` | Driver assistance computer (secondary): w222 acc camera blind | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w223_accObjectInPath` | Driver assistance computer (secondary): w223 acc object in path | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w224_accCameraCalibration` | Driver assistance computer (secondary): w224 acc camera calibration | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w225_lcDegradedVisSpeedLmt` | Driver assistance computer (secondary): w225 lc degraded vis speed lmt | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w226_lcCamCalNeededSpeedLmt` | Driver assistance computer (secondary): w226 lc cam cal needed speed lmt | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w227_virtualWallBlocked` | Driver assistance computer (secondary): w227 virtual wall blocked | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w228_DEPRECATED` | Driver assistance computer (secondary): w228 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w229_alcUltrasoundDamaged` | Driver assistance computer (secondary): w229 alc ultrasound damaged | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w230_alcUltrasoundBlocked` | Driver assistance computer (secondary): w230 alc ultrasound blocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w231_idfEvent` | Driver assistance computer (secondary): w231 idf event | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w232_laneChangeRequested` | Driver assistance computer (secondary): w232 lane change requested | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w235_a72LoopDetected` | Driver assistance computer (secondary): w235 a72 loop detected | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w236_canSharedMemError` | Driver assistance computer (secondary): w236 can shared mem error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w237_faultMgrEventDetected` | Driver assistance computer (secondary): w237 fault mgr event detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w238_resetReason` | Driver assistance computer (secondary): w238 reset reason | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w241_ddrInitFailures` | Driver assistance computer (secondary): w241 ddr init failures | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w242_tripMBISTFailure` | Driver assistance computer (secondary): w242 trip MBIST failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w243_tripHWErrorStatus` | Driver assistance computer (secondary): w243 trip HW error status | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w244_gpuHWFaultStatus` | Driver assistance computer (secondary): w244 gpu HW fault status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w245_eloopRxFromUnexpectedSourceMAC` | Driver assistance computer (secondary): w245 eloop rx from unexpected source MAC | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w246_ethloopSwitchPortLinkDown` | Driver assistance computer (secondary): w246 ethloop switch port link down | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w247_ethernetFrameError` | Driver assistance computer (secondary): w247 ethernet frame error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w248_ethloopSwitchPoorSqi` | Driver assistance computer (secondary): w248 ethloop switch poor sqi | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w249_ufsFailures` | Driver assistance computer (secondary): w249 ufs failures | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w250_ethloopSwitchMemUsageTooHighPort2` | Driver assistance computer (secondary): w250 ethloop switch mem usage too high port2 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w251_ethloopSwitchMemUsageTooHighPort3` | Driver assistance computer (secondary): w251 ethloop switch mem usage too high port3 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w252_ethSwitchPortLinkDown` | Driver assistance computer (secondary): w252 eth switch port link down | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w253_powerStateTimeout` | Driver assistance computer (secondary): w253 power state timeout | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w254_sleepStateTimeout` | Driver assistance computer (secondary): w254 sleep state timeout | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w255_bootHealth` | Driver assistance computer (secondary): w255 boot health | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
