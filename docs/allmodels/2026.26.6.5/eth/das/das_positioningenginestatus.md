---
layout: default
title: "DAS_positioningEngineStatus (0x30D) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Driver assistance computer message: positioning engine status. Ethernet-side message DAS_positioningEngineStatus of Driver assistance computer for Tesla Model 3 / Model Y firmware 2026.26.6.5, 25 signals (DAS_positioningEngineStatusMultiplexer, DAS_meoSolverNumRuns, DAS_meoSolverReportTerminationType, DAS_meoSolverReportTotalTimeS and 21 more). Bit layout, scaling, units and value tables."
---

# DAS_positioningEngineStatus (0x30D) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Driver assistance computer message: positioning engine status. This page documents the 25 signals of DAS_positioningEngineStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_positioningEngineStatus` |
| Ethernet-side id | 0x30D (781) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 250 ms |
| Signals | 25 |

## Signals of DAS_positioningEngineStatus

Tesla Model 3 / Model Y CAN bus signals in `DAS_positioningEngineStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_positioningEngineStatusMultiplexer` | selector | Driver assistance computer: positioning engine status multiplexer | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3` | plausible |
| `DAS_meoSolverNumRuns` | page 2 | Driver assistance computer: meo solver num runs | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0`<br>1 = `1_TO_10`<br>2 = `11_TO_100`<br>3 = `101_AND_ABOVE` | validated |
| `DAS_meoSolverReportTerminationType` | page 2 | Driver assistance computer: meo solver report termination type | 6\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CONVERGENCE`<br>1 = `FAILURE`<br>2 = `NO_CONVERGENCE`<br>3 = `USER_FAILURE`<br>4 = `USER_SUCCESS` | validated |
| `DAS_meoSolverReportTotalTimeS` | page 2 | Driver assistance computer: meo solver report total time s | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `0`<br>1 = `0_TO_0_1`<br>2 = `0_1_TO_0_2`<br>3 = `0_2_TO_0_3`<br>4 = `0_3_TO_0_4`<br>5 = `0_4_TO_0_5`<br>6 = `0_5_AND_ABOVE` | validated |
| `DAS_meoHorizontalAccuracyM` | page 2 | Driver assistance computer: meo horizontal accuracy m | 12\|6 | little-endian | unsigned | 1 | 0 | m | 0 to 63 |  | validated |
| `DAS_meoVerticalAccuracyM` | page 2 | Driver assistance computer: meo vertical accuracy m | 18\|6 | little-endian | unsigned | 1 | 0 | m | 0 to 63 |  | validated |
| `DAS_meoHeadingAccuracyDeg` | page 2 | Driver assistance computer: meo heading accuracy deg | 24\|3 | little-endian | unsigned | 1 | 0 | deg | 0 to 7 |  | validated |
| `DAS_meoHeadingValid` | page 2 | Driver assistance computer: meo heading valid | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_meoNumSatellitesUsed` | page 2 | Driver assistance computer: meo num satellites used | 28\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `DAS_meoGpsQualityLevel` | page 2 | Driver assistance computer: meo gps quality level | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `GPS_NO_COMMUNICATION`<br>1 = `GPS_OUTPUT_UNAVAILABLE`<br>2 = `GPS_QUALITY_UNKNOWN`<br>3 = `GPS_QUALITY_POOR`<br>4 = `GPS_QUALITY_ROAD`<br>5 = `GPS_QUALITY_LANE`<br>6 = `GPS_QUALITY_SUB_LANE` | validated |
| `DAS_meoFixType` | page 2 | Driver assistance computer: meo fix type | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_FIX`<br>1 = `DEAD_RECKONING_ONLY`<br>2 = `FIX_2D`<br>3 = `FIX_3D`<br>4 = `GNSS_DEAD_RECKONING_COMBINED`<br>5 = `TIME_ONLY_FIX` | validated |
| `DAS_meoResetCount` | page 2 | Driver assistance computer: meo reset count | 39\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `DAS_lastMeoResetReason` | page 2 | Driver assistance computer: last meo reset reason | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `INITIALIZE_STATE_FROM_CONTEXT_FAILED`<br>2 = `SLAM_ANCHOR_NODE_OUT_OF_ORDER`<br>3 = `EXTRAPOLATION_DEVIATES_FROM_SPP` | validated |
| `DAS_vioMultiGpsSelectedSource` | page 3 | Driver assistance computer: vio multi gps selected source | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `RAW_GPS`<br>2 = `BLUEFIN_MEO`<br>3 = `BLUEFIN_SPP_TDCP`<br>4 = `RELOCALIZATION`<br>5 = `SEEDED_ORIGIN` | validated |
| `DAS_vioMultiGpsPeCooldownActive` | page 3 | Driver assistance computer: vio multi gps pe cooldown active | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_vioMultiGpsPeSppTdcpConsistentWithRawGps` | page 3 | Driver assistance computer: vio multi gps pe spp tdcp consistent with raw gps | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_vioMultiGpsPeMeoConsistentWithRawGps` | page 3 | Driver assistance computer: vio multi gps pe meo consistent with raw gps | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_vioMultiGpsPeSppTdcpVsRawGpsTransDiscrepM` | page 3 | Driver assistance computer: vio multi gps pe spp tdcp vs raw gps trans discrep m | 10\|4 | little-endian | unsigned | 1 | 0 | m | 0 to 15 |  | validated |
| `DAS_vioMultiGpsPeMeoVsRawGpsTransDiscrepM` | page 3 | Driver assistance computer: vio multi gps pe meo vs raw gps trans discrep m | 14\|4 | little-endian | unsigned | 1 | 0 | m | 0 to 15 |  | validated |
| `DAS_vioMultiGpsPeSppTdcpVsRawGpsRotDiscrepDeg` | page 3 | Driver assistance computer: vio multi gps pe spp tdcp vs raw gps rot discrep deg | 18\|3 | little-endian | unsigned | 1 | 0 | deg | 0 to 7 |  | validated |
| `DAS_vioMultiGpsPeMeoVsRawGpsRotDiscrepDeg` | page 3 | Driver assistance computer: vio multi gps pe meo vs raw gps rot discrep deg | 21\|3 | little-endian | unsigned | 1 | 0 | deg | 0 to 7 |  | validated |
| `DAS_publishedGpsSource` | page 3 | Driver assistance computer: published gps source | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `RAW_GPS_PASSTHROUGH`<br>2 = `VIO_GEODETIC_POSE`<br>3 = `VIO_MULTI_GPS` | validated |
| `DAS_bluefinEnabled` | page 3 | Driver assistance computer: bluefin enabled | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_orioleDisabled` | page 3 | Driver assistance computer: oriole disabled | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_disableMonarch` | page 3 | Indicates the state of the Autopilot (AP) monarch positioning engine. | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |

## Multiplexing

`DAS_positioningEngineStatusMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (12 signals), page 3 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
