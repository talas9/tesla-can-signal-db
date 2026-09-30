---
layout: default
title: "APP_status (0x259) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: status. Ethernet-side message APP_status of Driver assistance computer (primary) for Tesla Model Y firmware 2025.20.8, 24 signals (APP_watchdogState, APP_fusedState, APP_cameraHeaterRequest, APP_factorySummonStatus and 20 more). Bit layout, scaling, units and value tables."
---

# APP_status (0x259) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: status. This page documents the 24 signals of APP_status as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_status` |
| Ethernet-side id | 0x259 (601) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 24 |

## Signals of APP_status

Tesla Model Y CAN bus signals in `APP_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_watchdogState` | State of system watchdog on ParkerB; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `AP_WDOG_STATE_UNKNOWN`<br>1 = `AP_WDOG_STATE_DEGRADED`<br>2 = `AP_WDOG_STATE_CRITICAL`<br>3 = `AP_WDOG_STATE_HEALTHY`<br>4 = `AP_WDOG_STATE_SHUTTING_DOWN`<br>7 = `AP_WDOG_STATE_SNA` | validated |
| `APP_fusedState` | Driver assistance computer (primary): fused state; raw 3 = signal not available (SNA) | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `APP_FUSE_UNKNOWN`<br>1 = `APP_FUSE_UNFUSED`<br>2 = `APP_FUSE_FUSED`<br>3 = `APP_FUSE_SNA` | validated |
| `APP_cameraHeaterRequest` | Indicates if heater grid is active because of request from AP cameras. | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_factorySummonStatus` | Driver assistance computer (primary): factory summon status; raw 0 = signal not available (SNA) | 6\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `FACTORY_SUMMON_SNA`<br>1 = `FACTORY_SUMMON_ACTIVE`<br>2 = `FACTORY_SUMMON_AVAILABLE`<br>3 = `FACTORY_SUMMON_UNAVAILABLE_NO_QR_INSTRUCTION`<br>4 = `FACTORY_SUMMON_UNAVAILABLE_GOAL_TOO_FAR`<br>5 = `FACTORY_SUMMON_UNAVAILABLE_NO_GPS`<br>6 = `FACTORY_SUMMON_UNAVAILABLE_VEHICLE_SPEED_INVALID`<br>7 = `FACTORY_SUMMON_UNAVAILABLE_HEADING_NOT_INITIALIZED`<br>8 = `FACTORY_SUMMON_END_OF_ROUTE` | validated |
| `APP_clipRecordingStatus` | Driver assistance computer (primary): clip recording status | 10\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APP_CLIP_NO_DRIVE`<br>1 = `APP_CLIP_IDLE`<br>2 = `APP_CLIP_RECORDING`<br>3 = `APP_CLIP_TRIGGERED`<br>4 = `APP_CLIP_FAULTED` | validated |
| `APP_allowApActivationWithBrake` | Indicates whether Autopilot (AP) activation while brake pressed is allowed. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_summonUnavailableReason` | The reason why smart summon is currently unavailable. | 14\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `SMART_SUMMON_UNAVAILABLE_UNKNOWN`<br>1 = `SMART_SUMMON_UNAVAILABLE_NONE`<br>2 = `SMART_SUMMON_UNAVAILABLE_NOT_IN_PARK`<br>3 = `SMART_SUMMON_UNAVAILABLE_CAMERA_STREAM`<br>4 = `SMART_SUMMON_UNAVAILABLE_CAMERA_BLOCKED`<br>5 = `SMART_SUMMON_UNAVAILABLE_ULTRASONIC_BLOCKED`<br>6 = `SMART_SUMMON_UNAVAILABLE_ULTRASONIC_FAULT`<br>7 = `SMART_SUMMON_UNAVAILABLE_CRUISE_UNAVAILABLE`<br>8 = `SMART_SUMMON_UNAVAILABLE_EAC_UNAVAILABLE`<br>9 = `SMART_SUMMON_UNAVAILABLE_PUBLIC_ROAD`<br>10 = `SMART_SUMMON_UNAVAILABLE_POOR_CONNECTION`<br>11 = `SMART_SUMMON_UNAVAILABLE_PHONE_GPS_UNAVAILABLE`<br>12 = `SMART_SUMMON_UNAVAILABLE_EGO_GPS_UNAVAILABLE`<br>13 = `SMART_SUMMON_UNAVAILABLE_PHONE_IS_TOO_FAR`<br>14 = `SMART_SUMMON_UNAVAILABLE_END_OF_LEASH`<br>15 = `SMART_SUMMON_UNAVAILABLE_CAMERA_NOT_CALIBRATED`<br>16 = `SMART_SUMMON_UNAVAILABLE_VISION_HEALTH_CRITICAL`<br>17 = `SMART_SUMMON_UNAVAILABLE_ULTRASONIC_STALE`<br>18 = `SMART_SUMMON_UNAVAILABLE_ALL_SENSORS_OCCLUDED`<br>19 = `SMART_SUMMON_UNAVAILABLE_PUBLIC_ROAD_BOUNDARIES_NOT_VALID`<br>20 = `SMART_SUMMON_UNAVAILABLE_NO_CONTEXT`<br>21 = `SMART_SUMMON_UNAVAILABLE_HIGH_GRADE`<br>22 = `SMART_SUMMON_UNAVAILABLE_EXTENDED_COMPUTE_INACTIVE`<br>23 = `SMART_SUMMON_UNAVAILABLE_LOW_TIRE_PRESSURE`<br>24 = `SMART_SUMMON_UNAVAILABLE_CLOSURE_OPEN`<br>25 = `SMART_SUMMON_UNAVAILABLE_REMOTE_STOP_OR_ABORT_REQUEST_ACTIVE`<br>26 = `SMART_SUMMON_UNAVAILABLE_BRAKE_PEDAL_PRESSED`<br>27 = `SMART_SUMMON_UNAVAILABLE_ACCEL_PEDAL_PRESSED`<br>28 = `SMART_SUMMON_UNAVAILABLE_OUTSIDE_GEOFENCE` | validated |
| `APP_fsdSuspendState` | If FSD feature is suspended on this car; raw 3 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_SUSPENDED`<br>1 = `SUSPENDED`<br>3 = `SNA` | validated |
| `APP_fsdRevokeStrikeoutCount` | Reports the number of strikeouts counted towards revoking Full Self-Driving (FSD) feature; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 7 = `SNA` | validated |
| `APP_teslaVisionSupported` | Whether autopilot can support tesla vision; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_SUPPORTED`<br>1 = `SUPPORTED`<br>3 = `SNA` | validated |
| `APP_teslaVisionUnsupportedReason` | Reason for vehicle not supporting tesla vision | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `NONE`<br>2 = `AP_HARDWARE`<br>3 = `UNSUPPORTED_CAMERA`<br>4 = `VEHICLE_LOCATION` | validated |
| `APP_fsdRevokeCount` | Reports the number of times the car has had Full Self-Driving (FSD) revoked; raw 7 = signal not available (SNA) | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 7 = `SNA` | validated |
| `APP_excessiveAccelPedalWarning` | Indicates that driver is using acceleration pedal continously and excessively | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_unifiedObjectStackSupported` | Whether autopilot can support unified objects stack for tesla vision; raw 3 = signal not available (SNA) | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_SUPPORTED`<br>1 = `SUPPORTED`<br>3 = `SNA` | validated |
| `APP_unifiedObjsUnsupportedReason` | Driver assistance computer (primary): unified objs unsupported reason | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `NONE`<br>2 = `AP_HARDWARE`<br>3 = `UNSUPPORTED_CAMERA`<br>4 = `VEHICLE_LOCATION` | plausible |
| `APP_DDAWSystemStatus` | DDAW system status; raw 4 = signal not available (SNA) | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DDAW_SYSTEM_NOMINAL`<br>1 = `DDAW_SYSTEM_DRIVER_DROWSY`<br>2 = `DDAW_SYSTEM_FAILURE`<br>3 = `DDAW_SYSTEM_INVALID`<br>4 = `DDAW_SYSTEM_SNA` | plausible |
| `APP_socOperatingMode` | Operating Mode of the SOC | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_UNKNOWN`<br>1 = `AP_SINGLE_SOC`<br>2 = `AP_DUAL_SOC` | plausible |
| `APP_summonVersionIdentifier` | Driver assistance computer (primary): summon version identifier | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEGACY_SMART_SUMMON`<br>1 = `ACTUALLY_SMART_SUMMON` | plausible |
| `APP_sentryState` | Reports the Sentry mode state on Gen. 4 Hardware (HW4) and later vehicles; raw 6 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENTRY_OFF`<br>1 = `SENTRY_IDLE`<br>2 = `SENTRY_ARMED`<br>3 = `SENTRY_AWARE`<br>4 = `SENTRY_PANIC`<br>5 = `SENTRY_QUIET`<br>6 = `SENTRY_SNA` | validated |
| `APP_autoparkVersionIdentifier` | Driver assistance computer (primary): autopark version identifier | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEGACY_AUTOPARK`<br>1 = `V3_VISION_AUTOPARK`<br>2 = `ACTUALLY_SMART_AUTOPARK` | validated |
| `APP_setSpeedMode` | Driver assistance computer (primary): set speed mode | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TARGET_SPEED`<br>1 = `MAX_SPEED`<br>2 = `AUTO` | plausible |
| `APP_suspendResumeAvailable` | Driver assistance computer (primary): suspend resume available | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_statusCounter` | Driver assistance computer (primary): status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `APP_statusChecksum` | Driver assistance computer (primary): status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
