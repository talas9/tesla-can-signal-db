---
layout: default
title: "DAS_status2 (0x389) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: status2. Tesla Model 3 CAN bus message DAS_status2 (0x389) of Driver assistance computer, firmware 2026.26.6.5, 19 signals (DAS_accSpeedLimit, DAS_versionIdentifier, DAS_pmmObstacleSeverity, DAS_pmmLoggingRequest and 15 more). Bit layout, scaling, units and value tables."
---

# DAS_status2 (0x389) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer message: status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of DAS_status2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_status2` |
| CAN id | 0x389 (905) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 19 |

## Signals of DAS_status2

Tesla Model 3 CAN bus signals in `DAS_status2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_accSpeedLimit` | Reports the Adaptive Cruise Control (ACC) speed limit, which is derived from speed limits embedded in maps; raw 511 = signal not available (SNA) | 0\|9 | little-endian | unsigned | 0.4 | 0 | mph | 0 to 200 | 0 = `NONE`<br>511 = `SNA` | validated |
| `DAS_versionIdentifier` | Driver assistance computer: version identifier | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_pmmObstacleSeverity` | Detects the output of the Pedal Misapplication Mitigation (PMM) function, which limits torque or applies the brake; raw 7 = signal not available (SNA) | 10\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `PMM_NONE`<br>1 = `PMM_IMMINENT_REAR`<br>2 = `PMM_IMMINENT_FRONT`<br>3 = `PMM_BRAKE_REQUEST`<br>4 = `PMM_CRASH_REAR`<br>5 = `PMM_CRASH_FRONT`<br>6 = `PMM_ACCEL_LIMIT`<br>7 = `PMM_SNA` | validated |
| `DAS_pmmLoggingRequest` | Driver assistance computer: pmm logging request | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DAS_activationFailureStatus` | Driver assistance computer: activation failure status | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LC_ACTIVATION_IDLE`<br>1 = `LC_ACTIVATION_FAILED_1`<br>2 = `LC_ACTIVATION_FAILED_2` | validated |
| `DAS_pmmUltrasonicsFaultReason` | Reports if there is a reason Pedal Misapplication Mitigation (PMM) is disabled due to a condition with the ultrasonics. | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PMM_ULTRASONICS_NO_FAULT`<br>1 = `PMM_ULTRASONICS_BLOCKED_FRONT`<br>2 = `PMM_ULTRASONICS_BLOCKED_REAR`<br>3 = `PMM_ULTRASONICS_BLOCKED_BOTH`<br>4 = `PMM_ULTRASONICS_INVALID_MIA` | validated |
| `DAS_pmmRadarFaultReason` | Reports if there is a reason Pedal Misapplication Mitigation (PMM) is disabled due to a radar issue. | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMM_RADAR_NO_FAULT`<br>1 = `PMM_RADAR_BLOCKED_FRONT`<br>2 = `PMM_RADAR_INVALID_MIA` | validated |
| `DAS_pmmSysFaultReason` | Reports if there is a reason Pedal Misapplication Mitigation (PMM) is disabled due to a system malfunction. | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PMM_FAULT_NONE`<br>1 = `PMM_FAULT_DAS_DISABLED`<br>2 = `PMM_FAULT_SPEED`<br>3 = `PMM_FAULT_DI_FAULT`<br>4 = `PMM_FAULT_STEERING_ANGLE_RATE`<br>5 = `PMM_FAULT_DISABLED_BY_USER`<br>6 = `PMM_FAULT_ROAD_TYPE`<br>7 = `PMM_FAULT_BRAKE_PEDAL_INHIBIT` | validated |
| `DAS_pmmCameraFaultReason` | Reports if there is a reason Pedal Misapplication Mitigation (PMM) is disabled due to camera issues. | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMM_CAMERA_NO_FAULT`<br>1 = `PMM_CAMERA_BLOCKED_FRONT`<br>2 = `PMM_CAMERA_INVALID_MIA` | validated |
| `DAS_ACC_report` | Indicates what control target Traffic-Aware Cruise Control (TACC) is controlling for. Only relevant during TACC (not Autosteer). | 26\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `ACC_REPORT_TARGET_NONE`<br>1 = `ACC_REPORT_TARGET_CIPV`<br>2 = `ACC_REPORT_TARGET_IN_FRONT_OF_CIPV`<br>3 = `ACC_REPORT_TARGET_MCVL`<br>4 = `ACC_REPORT_TARGET_MCVR`<br>5 = `ACC_REPORT_TARGET_CUTIN`<br>6 = `ACC_REPORT_TARGET_TYPE_STOP_SIGN`<br>7 = `ACC_REPORT_TARGET_TYPE_TRAFFIC_LIGHT`<br>8 = `ACC_REPORT_TARGET_TYPE_IPSO`<br>9 = `ACC_REPORT_TARGET_TYPE_FAULT`<br>10 = `ACC_REPORT_CSA`<br>11 = `ACC_REPORT_LC_HANDS_ON_REQD_STRUCK_OUT`<br>12 = `ACC_REPORT_LC_EXTERNAL_STATE_ABORTING`<br>13 = `ACC_REPORT_LC_EXTERNAL_STATE_ABORTED`<br>14 = `ACC_REPORT_LC_EXTERNAL_STATE_ACTIVE_RESTRICTED`<br>15 = `ACC_REPORT_RADAR_OBJ_ONE`<br>16 = `ACC_REPORT_RADAR_OBJ_TWO`<br>17 = `ACC_REPORT_TARGET_MCP`<br>18 = `ACC_REPORT_FLEET_SPEEDS`<br>19 = `ACC_REPORT_MCVLR_DPP`<br>20 = `ACC_REPORT_MCVLR_IN_PATH`<br>21 = `ACC_REPORT_CIPV_CUTTING_OUT`<br>22 = `ACC_REPORT_RADAR_OBJ_FIVE`<br>23 = `ACC_REPORT_CAMERA_ONLY`<br>24 = `ACC_REPORT_BEHAVIOR_REPORT` | validated |
| `DAS_relaxCruiseLimits` | Indicates whether DI should relax accel limits | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_csaState` | Reports the state of the curve speed adaption algorithm. | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CSA_EXTERNAL_STATE_UNAVAILABLE`<br>1 = `CSA_EXTERNAL_STATE_AVAILABLE`<br>2 = `CSA_EXTERNAL_STATE_ENABLE`<br>3 = `CSA_EXTERNAL_STATE_HOLD` | validated |
| `DAS_radarTelemetry` | Driver assistance computer: radar telemetry | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RADAR_TELEMETRY_IDLE`<br>1 = `RADAR_TELEMETRY_NORMAL`<br>2 = `RADAR_TELEMETRY_URGENT` | validated |
| `DAS_robState` | Driver assistance computer: rob state | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ROB_STATE_INHIBITED`<br>1 = `ROB_STATE_MEASURE`<br>2 = `ROB_STATE_ACTIVE`<br>3 = `ROB_STATE_MAPLESS` | validated |
| `DAS_driverInteractionLevel` | Driver assistance computer: driver interaction level | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER_INTERACTING`<br>1 = `DRIVER_NOT_INTERACTING`<br>2 = `CONTINUED_DRIVER_NOT_INTERACTING` | validated |
| `DAS_ppOffsetDesiredRamp` | Driver assistance computer: pp offset desired ramp | 40\|8 | little-endian | unsigned | 0.01 | -1.28 | m | -1.28 to 1.27 | 128 = `PP_NO_OFFSET` | validated |
| `DAS_longCollisionWarning` | Driver assistance computer: long collision warning; raw 15 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `FCM_LONG_COLLISION_WARNING_NONE`<br>1 = `FCM_LONG_COLLISION_WARNING_VEHICLE_UNKNOWN`<br>2 = `FCM_LONG_COLLISION_WARNING_PEDESTRIAN`<br>3 = `FCM_LONG_COLLISION_WARNING_IPSO`<br>4 = `FCM_LONG_COLLISION_WARNING_STOPSIGN_STOPLINE`<br>5 = `FCM_LONG_COLLISION_WARNING_TFL_STOPLINE`<br>6 = `FCM_LONG_COLLISION_WARNING_VEHICLE_CIPV`<br>7 = `FCM_LONG_COLLISION_WARNING_VEHICLE_CUTIN`<br>8 = `FCM_LONG_COLLISION_WARNING_VEHICLE_MCVL`<br>9 = `FCM_LONG_COLLISION_WARNING_VEHICLE_MCVL2`<br>10 = `FCM_LONG_COLLISION_WARNING_VEHICLE_MCVR`<br>11 = `FCM_LONG_COLLISION_WARNING_VEHICLE_MCVR2`<br>12 = `FCM_LONG_COLLISION_WARNING_VEHICLE_CIPV2`<br>15 = `FCM_LONG_COLLISION_WARNING_SNA` | validated |
| `DAS_status2Counter` | Driver assistance computer: status2 counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_status2Checksum` | Driver assistance computer: status2 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
