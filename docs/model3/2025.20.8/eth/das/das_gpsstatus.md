---
layout: default
title: "DAS_gpsStatus (0x7F9) — Driver assistance computer, Tesla Model 3 2025.20.8 ETH"
description: "Driver assistance computer message: gps status. Ethernet-side message DAS_gpsStatus of Driver assistance computer for Tesla Model 3 firmware 2025.20.8, 52 signals (DAS_gpsStatusMultiplexer, DAS_gpsTransportModeState, DAS_gpsSatsInUseHardware, DAS_gpsWheeltickCounter and 48 more). Bit layout, scaling, units and value tables."
---

# DAS_gpsStatus (0x7F9) — Driver assistance computer, Tesla Model 3 2025.20.8 ETH

Driver assistance computer message: gps status. This page documents the 52 signals of DAS_gpsStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_gpsStatus` |
| Ethernet-side id | 0x7F9 (2041) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 52 |

## Signals of DAS_gpsStatus

Tesla Model 3 CAN bus signals in `DAS_gpsStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_gpsStatusMultiplexer` | selector | Driver assistance computer: gps status multiplexer | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3` | plausible |
| `DAS_gpsTransportModeState` | page 0 | Indicates if the transport mode algorithm detects the car is in transport mode. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS_GPS_TRANSPORT_MODE_OFF`<br>1 = `DAS_GPS_TRANSPORT_MODE_ON` | validated |
| `DAS_gpsSatsInUseHardware` | page 0 | The number of GPS satellites currently in use by hardware solution. | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_gpsWheeltickCounter` | page 0 | Driver assistance computer: gps wheeltick counter | 9\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_gpsWheeltickPulsePeriod` | page 0 | Driver assistance computer: gps wheeltick pulse period | 25\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `DAS_gpsRejectingSatData` | page 0 | Indicates whether or not the GPS is rejecting satellites due to poor signal. | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsWheelsOffMotionDetected` | page 0 | Indicates that wheels-off acceleration detected | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS_GPS_MOTION_DETECTED_OFF`<br>1 = `DAS_GPS_MOTION_DETECTED_ON` | validated |
| `DAS_gpsFixTypeHardware` | page 0 | The fix type of the GPS receiver, see u-blox M8 spec, section 33.13.1.1 | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID_FIX`<br>1 = `GPS_FIX`<br>2 = `DGPS_FIX`<br>3 = `PPS_FIX`<br>4 = `REAL_TIME_KINEMATICS_FIX`<br>5 = `FLOAT_RTK_FIX`<br>6 = `DEAD_RECOCKONING_FIX` | validated |
| `DAS_gpsRawxEnabled` | page 0 | GPS receiver has raw messages enabled | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsRxmRawxMia` | page 1 | Driver assistance computer: gps rxm rawx mia | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsRxmSfrbxMia` | page 1 | Driver assistance computer: gps rxm sfrbx mia | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsEsfMeasMia` | page 1 | AP is not receiving EsfMeas message from GPS receiver | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsEsfRawMia` | page 1 | AP is not receiving EsfRaw message from GPS receiver | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsNavStatusMia` | page 1 | AP is not receiving NavStatus message from GPS receiver | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsSoftwareConfigured` | page 1 | Software GPS solution is allowed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsSoftwareUsed` | page 1 | Software GPS solution is actively used | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsSoftwareFastStartReady` | page 1 | Software GPS solution could use fast start mechanism at boot-up | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsSatsInUseSoftware` | page 1 | The number of GPS satellites currently in use by software solution on SOC-A. | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_gpsFixTypeSoftware` | page 1 | The fix type of the GPS software solution on SOC-A. | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID_FIX`<br>1 = `GPS_FIX`<br>2 = `DGPS_FIX`<br>3 = `PPS_FIX`<br>4 = `REAL_TIME_KINEMATICS_FIX`<br>5 = `FLOAT_RTK_FIX`<br>6 = `DEAD_RECOCKONING_FIX` | validated |
| `DAS_gpsCWJammingInidcator` | page 1 | Level of continuous wave jamming detected by GPS hardware | 19\|5 | little-endian | unsigned | 8 | 0 | - | 0 to 248 |  | validated |
| `DAS_gpsJammingState` | page 1 | State of GPS jamming monitor | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GPS_JAMMING_STATE_UNKNOWN`<br>1 = `GPS_JAMMING_STATE_NOMINAL`<br>2 = `GPS_JAMMING_STATE_WARNING`<br>3 = `GPS_JAMMING_STATE_CRITICAL` | validated |
| `DAS_gpsSpoofDetectorState` | page 1 | Instantaneous state of GPS spoofing detector. Detection only triggers at the transition from real to suspected spoof signal. | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GPS_SPOOFING_UNKNOWN`<br>1 = `GPS_SPOOFING_NO_ACTIVE_INDICATION`<br>2 = `GPS_SPOOFING_INDICATION_PRESENT`<br>3 = `GPS_SPOOFING_MULTIPLE_INDICATIONS` | validated |
| `DAS_gpsInvalidMsgPercentage` | page 1 | Percentage of messages received by AP from GPS receiver that were invalid. Calculated over up-to 10s window. | 28\|4 | little-endian | unsigned | 6 | 0 | % | 0 to 90 |  | validated |
| `DAS_gnssConstellationsState` | page 1 | Indicates if GNSS constellations match expected configuration. | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONSTELLATIONS_STATE_UNKNOWN`<br>1 = `CONSTELLATIONS_STATE_INVALID`<br>2 = `CONSTELLATIONS_STATE_VALID` | validated |
| `DAS_gpsReceiverNoiseLevel` | page 1 | General noise level of GPS receiver. | 34\|6 | little-endian | unsigned | 8 | 0 | - | 0 to 504 |  | validated |
| `DAS_gpsAutomaticGainControl` | page 1 | Automatic Gain Control of GPS receiver. | 40\|8 | little-endian | unsigned | 32 | 0 | - | 0 to 8160 |  | validated |
| `DAS_gpsPreviousPositionDeltaHw` | page 1 | Change in position of two consecutive location outputs from GPS hardware solution. | 48\|6 | little-endian | unsigned | 3 | 0 | m | 0 to 189 |  | validated |
| `DAS_gpsPreviousPositionDeltaSw` | page 1 | Change in position of two consecutive location outputs from GPS software solution. | 54\|6 | little-endian | unsigned | 3 | 0 | m | 0 to 189 |  | validated |
| `DAS_gpsNmeaDispatchFailureCount` | page 1 | Number of GPS messages dropped by AP without sending over to UI. Calculated over up-to 10s window. | 60\|4 | little-endian | unsigned | 5 | 0 | - | 0 to 75 |  | validated |
| `DAS_gnssMaxInstantaneousCnorGps` | page 2 | Maximum carrier-to-noise ratio among all satellites from GPS constellation. | 4\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssMaxInstantaneousCnorGal` | page 2 | Maximum carrier-to-noise ratio among all satellites from GALILEO constellation. | 10\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssMaxInstantaneousCnorBds` | page 2 | Maximum carrier-to-noise ratio among all satellites from BEIDOU constellation. | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gpsResetReason` | page 2 | When AP resets GPS receiver, this signal indicates the reason why | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `GPS_RESET_NONE`<br>1 = `GPS_RESET_DATA_MISSING`<br>2 = `GPS_RESET_DATA_CORRUPTED`<br>3 = `GPS_RESET_UBX_MISSING`<br>4 = `GPS_RESET_GNSS_DATA_MISSING`<br>5 = `GPS_RESET_EXIT_TRANSPORT_MODE`<br>6 = `GPS_RESET_ENTER_TRANSPORT_MODE`<br>7 = `GPS_RESET_SATELLITE_REJECTION_TIMEOUT`<br>8 = `GPS_RESET_SUSPEND_CONFIGURATION_FAULT`<br>9 = `GPS_RESET_RESUME_CONFIGURATION_FAULT`<br>10 = `GPS_RESET_GNSS_CFG_CHANGE`<br>11 = `GPS_RESET_MANUAL_COLD_RESET`<br>12 = `GPS_RESET_SOLUTION_INCONSISTENCY`<br>13 = `GPS_RESET_PPS_MISSING` | validated |
| `DAS_gpsAccuracyHorizontal` | page 2 | Self-reported horizontal GPS accuracy | 26\|6 | little-endian | unsigned | 1 | 0 | m | 0 to 63 |  | validated |
| `DAS_gpsAccuracyVertical` | page 2 | Self-reported vertical GPS accuracy | 32\|6 | little-endian | unsigned | 1 | 0 | m | 0 to 63 |  | validated |
| `DAS_gpsSolutionFallback` | page 2 | GPS solution falling back from software to hardware | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsToMcuSource` | page 2 | This signal exposes which localization solution is being sent to the MCU. | 39\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `GPS_TO_MCU_SOURCE_UNKNOWN`<br>1 = `GPS_TO_MCU_SOURCE_HARDWARE_SOLUTION`<br>2 = `GPS_TO_MCU_SOURCE_SOFTWARE_SOLUTION`<br>3 = `GPS_TO_MCU_SOURCE_TESLA_VIO_SOLUTION`<br>4 = `GPS_TO_MCU_SOURCE_BLUEFIN_SOLUTION` | validated |
| `DAS_gpsSolutionSoc` | page 2 | Reports which System on Chip (SOC) is producing the GPS localization solution. | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GPS_SOLUTION_SOC_UNKNOWN`<br>1 = `GPS_SOLUTION_SOC_A`<br>2 = `GPS_SOLUTION_SOC_B` | validated |
| `DAS_gpsRedundancyActive` | page 2 | Reports whether the GPS Redundancy feature is active on the Autopilot (AP) board. This feature enables either System on Chip (SOC) to publish the Global Navigation Satellite System (GNSS) solution. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_gpsFixTypeSoftwareSocB` | page 2 | Reports the fix type of the GPS software solution on System on Chip B (SOC-B). | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID_FIX`<br>1 = `GPS_FIX`<br>2 = `DGPS_FIX`<br>3 = `PPS_FIX`<br>4 = `REAL_TIME_KINEMATICS_FIX`<br>5 = `FLOAT_RTK_FIX`<br>6 = `DEAD_RECOCKONING_FIX` | validated |
| `DAS_gpsSatsInUseSoftwareSocB` | page 2 | Reports the number of GPS satellites currently in use by software solution on System on Chip B (SOC-B). | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_gnssNumSatsGps` | page 3 | Number of satellites visible from GPS constellation. | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 15 = `FIFTEEN_OR_MORE_SATELLITES` | validated |
| `DAS_gnssNumSatsGal` | page 3 | Number of satellites visible from GALILEO constellation. | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 15 = `FIFTEEN_OR_MORE_SATELLITES` | validated |
| `DAS_gnssNumSatsBds` | page 3 | Number of satellites visible from BEIDOU constellation. | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 15 = `FIFTEEN_OR_MORE_SATELLITES` | validated |
| `DAS_gnssAvgInstantaneousCnorGps` | page 3 | Average carrier-to-noise ratio among all satellites from GPS constellation on the high band as reported by the Positioning Engine on SOC-A. | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssAvgInstantaneousCnorGal` | page 3 | Average carrier-to-noise ratio among all satellites from GALILEO constellation on the high band. | 22\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssAvgInstantaneousCnorBds` | page 3 | Average carrier-to-noise ratio among all satellites from BEIDOU constellation on the high band as reported by the Positioning Engine on SOC-A. | 28\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssAvgInstantCnorGpsSocB` | page 3 | Driver assistance computer: gnss avg instant cnor gps soc b | 34\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `DAS_gnssAvgInstantCnorBdsSocB` | page 3 | Driver assistance computer: gnss avg instant cnor bds soc b | 40\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `DAS_gnssAvgInstantaneousCnorGpsLowBand` | page 3 | Measures the average carrier-to-noise ratio among all satellites from GPS constellation on the low band as reported by the Positioning Engine on System on Chip A (SOC-A). | 46\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssAvgInstantaneousCnorGalLowBand` | page 3 | Measures the average carrier-to-noise ratio among all satellites from GALILEO constellation on the low band. | 52\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `DAS_gnssAvgInstantaneousCnorBdsLowBand` | page 3 | Measures the average carrier-to-noise ratio among all satellites from BEIDOU constellation on the low band as reported by the Positioning Engine on System on Chip A (SOC-A). | 58\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |

## Multiplexing

`DAS_gpsStatusMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (8 signals), page 1 (20 signals), page 2 (12 signals), page 3 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
