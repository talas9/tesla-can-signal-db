---
layout: default
title: "APSB_warningMatrix3 (0x3D0) — APSB ECU, Tesla Model 3 2026.26.6.5 ETH"
description: "APSB ECU message: warning matrix3. Ethernet-side message APSB_warningMatrix3 of APSB ECU for Tesla Model 3 firmware 2026.26.6.5, 59 signals (APSB_w193_camWindshieldUnclean, APSB_w194_accDriverResumeRqrd, APSB_w195_scwUnavailable, APSB_w196_stopSignWarning and 55 more). Bit layout, scaling, units and value tables."
---

# APSB_warningMatrix3 (0x3D0) — APSB ECU, Tesla Model 3 2026.26.6.5 ETH

APSB ECU message: warning matrix3. This page documents the 59 signals of APSB_warningMatrix3 as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_warningMatrix3` |
| Ethernet-side id | 0x3D0 (976) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 59 |

## Signals of APSB_warningMatrix3

Tesla Model 3 CAN bus signals in `APSB_warningMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_w193_camWindshieldUnclean` | APSB ECU: w193 cam windshield unclean | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w194_accDriverResumeRqrd` | APSB ECU: w194 acc driver resume rqrd | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w195_scwUnavailable` | APSB ECU: w195 scw unavailable | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w196_stopSignWarning` | APSB ECU: w196 stop sign warning | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w197_redLightWarning` | APSB ECU: w197 red light warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w198_tsrUnavailable` | APSB ECU: w198 tsr unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w199_apcAbort` | APSB ECU: w199 apc abort | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w200_lcSlowdown` | APSB ECU: w200 lc slowdown | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w201_lcAborting` | APSB ECU: w201 lc aborting | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w202_scwNoisyEnvironment` | APSB ECU: w202 scw noisy environment | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w203_apcActivation` | APSB ECU: w203 apc activation | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w204_apcFinalFront` | APSB ECU: w204 apc final front | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w205_apcFinalRear` | APSB ECU: w205 apc final rear | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w206_autosteerNotEnabled` | APSB ECU: w206 autosteer not enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w207_autosteerUnavailable` | APSB ECU: w207 autosteer unavailable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w208_rackDetected` | APSB ECU: w208 rack detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w209_autoSummonRequest` | APSB ECU: w209 auto summon request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w210_camObstrcted` | APSB ECU: w210 cam obstrcted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w211_accNoSeatBelt` | APSB ECU: w211 acc no seat belt | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w212_lcUnavailableStrikeOut` | APSB ECU: w212 lc unavailable strike out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w213_autosteerStruckOut` | APSB ECU: w213 autosteer struck out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w214_driverNotIntracting` | APSB ECU: w214 driver not intracting | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w215_contDriverNotIntracting` | APSB ECU: w215 cont driver not intracting | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w216_driverOverriding` | APSB ECU: w216 driver overriding | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w217_lcUnavailableSpeeding` | APSB ECU: w217 lc unavailable speeding | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w218_lcSpeedExceededLimit` | APSB ECU: w218 lc speed exceeded limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w219_lcTempUnavailableSpeed` | APSB ECU: w219 lc temp unavailable speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w220_lcTempUnavailableRoad` | APSB ECU: w220 lc temp unavailable road | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w221_accRadarBlind` | APSB ECU: w221 acc radar blind | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w222_accCameraBlind` | APSB ECU: w222 acc camera blind | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w223_accObjectInPath` | APSB ECU: w223 acc object in path | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w224_accCameraCalibration` | APSB ECU: w224 acc camera calibration | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w225_lcDegradedVisSpeedLmt` | APSB ECU: w225 lc degraded vis speed lmt | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w226_lcCamCalNeededSpeedLmt` | APSB ECU: w226 lc cam cal needed speed lmt | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w227_virtualWallBlocked` | APSB ECU: w227 virtual wall blocked | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w228_DEPRECATED` | APSB ECU: w228 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w229_alcUltrasoundDamaged` | APSB ECU: w229 alc ultrasound damaged | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w230_alcUltrasoundBlocked` | APSB ECU: w230 alc ultrasound blocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w231_idfEvent` | APSB ECU: w231 idf event | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w232_laneChangeRequested` | APSB ECU: w232 lane change requested | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w235_a72LoopDetected` | APSB ECU: w235 a72 loop detected | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w236_canSharedMemError` | APSB ECU: w236 can shared mem error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w237_faultMgrEventDetected` | APSB ECU: w237 fault mgr event detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w238_resetReason` | APSB ECU: w238 reset reason | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w241_ddrInitFailures` | APSB ECU: w241 ddr init failures | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w242_tripMBISTFailure` | APSB ECU: w242 trip MBIST failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w243_tripHWErrorStatus` | APSB ECU: w243 trip HW error status | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w244_gpuHWFaultStatus` | APSB ECU: w244 gpu HW fault status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w245_eloopRxFromUnexpectedSourceMAC` | APSB ECU: w245 eloop rx from unexpected source MAC | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w246_ethloopSwitchPortLinkDown` | APSB ECU: w246 ethloop switch port link down | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w247_ethernetFrameError` | APSB ECU: w247 ethernet frame error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w248_ethloopSwitchPoorSqi` | APSB ECU: w248 ethloop switch poor sqi | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w249_ufsFailures` | APSB ECU: w249 ufs failures | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w250_ethloopSwitchMemUsageTooHighPort2` | APSB ECU: w250 ethloop switch mem usage too high port2 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w251_ethloopSwitchMemUsageTooHighPort3` | APSB ECU: w251 ethloop switch mem usage too high port3 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w252_ethSwitchPortLinkDown` | APSB ECU: w252 eth switch port link down | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w253_powerStateTimeout` | APSB ECU: w253 power state timeout | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w254_sleepStateTimeout` | APSB ECU: w254 sleep state timeout | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w255_bootHealth` | APSB ECU: w255 boot health | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
