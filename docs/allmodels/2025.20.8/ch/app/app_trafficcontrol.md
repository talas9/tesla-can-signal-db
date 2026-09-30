---
layout: default
title: "APP_trafficControl (0x25D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: traffic control. Tesla Model 3 / Model Y CAN bus message APP_trafficControl (0x25D) of Driver assistance computer (primary), firmware 2025.20.8, 14 signals (APP_tcFeatureState, APP_tcStateMachine, APP_tcControlSource, APP_tcControlType and 10 more). Bit layout, scaling, units and value tables."
---

# APP_trafficControl (0x25D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: traffic control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of APP_trafficControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_trafficControl` |
| CAN id | 0x25D (605) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 6 bytes |
| Cycle time | 500 ms |
| Signals | 14 |

## Signals of APP_trafficControl

Tesla Model 3 / Model Y CAN bus signals in `APP_trafficControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_tcFeatureState` | The feature level state of stopping for traffic controls | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TC_DISABLED`<br>1 = `TC_UNAVAILABLE`<br>2 = `TC_AVAILABLE`<br>3 = `TC_ACTIVE` | validated |
| `APP_tcStateMachine` | The traffic control state machine's internal control state. | 2\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TCSM_DISABLED`<br>1 = `TCSM_STANDBY`<br>2 = `TCSM_AWARE`<br>3 = `TCSM_WARNING`<br>4 = `TCSM_STOPPING`<br>5 = `TCSM_STOPPED`<br>6 = `TCSM_CONTINUING` | validated |
| `APP_tcControlSource` | The input data source for the traffic control object | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TC_SOURCE_NONE`<br>1 = `TC_SOURCE_MAP`<br>2 = `TC_SOURCE_VISION`<br>3 = `TC_SOURCE_MAP_AND_VISION` | validated |
| `APP_tcControlType` | The specific type of traffic control, note not all are control worthy. | 11\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `TC_TYPE_INVALID`<br>1 = `TC_TYPE_UNKNOWN`<br>2 = `TC_TYPE_STOP_SIGN`<br>3 = `TC_TYPE_TRAFFIC_LIGHT`<br>4 = `TC_TYPE_YIELD`<br>5 = `TC_TYPE_CROSSWALK`<br>6 = `TC_TYPE_KEEP_CLEAR_ENTER`<br>7 = `TC_TYPE_KEEP_CLEAR_EXIT`<br>8 = `TC_TYPE_SUICIDE_LEFT`<br>9 = `TC_TYPE_PEDESTRIAN_CROSSING`<br>10 = `TC_TYPE_RAMP_METER`<br>11 = `TC_TYPE_SPEED_BUMP`<br>12 = `TC_TYPE_SPEED_HUMP`<br>13 = `TC_TYPE_TRAFFIC_RULE`<br>14 = `TC_TYPE_ALL_WAY_STOP_SIGN`<br>15 = `TC_TYPE_BIKE_MERGE_FROM_LEFT`<br>16 = `TC_TYPE_BIKE_MERGE_FROM_RIGHT`<br>17 = `TC_TYPE_NO_STOP`<br>18 = `TC_TYPE_T_IMPLICIT`<br>19 = `TC_TYPE_T_IMPLICIT_BY_NAME`<br>20 = `TC_TYPE_T_IMPLICIT_BY_GEOM`<br>21 = `TC_TYPE_BEV_JUNCTION`<br>22 = `TC_TYPE_T_ARM` | validated |
| `APP_tcControlDistance` | The distance to the nearest critical traffic control object; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | m | 0 to 254 | 255 = `SNA` | validated |
| `APP_tcControlLightState` | Driver assistance computer (primary): tc control light state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TC_LIGHTSTATE_NONE`<br>1 = `TC_LIGHTSTATE_RED`<br>2 = `TC_LIGHTSTATE_GREEN`<br>3 = `TC_LIGHTSTATE_YELLOW`<br>4 = `TC_LIGHTSTATE_OFF`<br>5 = `TC_LIGHTSTAET_WHITE`<br>6 = `TC_LIGHTSTATE_OTHER` | validated |
| `APP_tcContinuationReason` | The reason the traffic control state machine entered the continue state. | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TC_CONTINUE_NONE`<br>1 = `TC_CONTINUE_GREEN_LIGHT_WITH_CIPV`<br>2 = `TC_CONTINUE_USER_INPUT_ON_GREEN`<br>3 = `TC_CONTINUE_USER_INPUT_ON_RED`<br>4 = `TC_CONTINUE_REQUIRED_DECEL_TOO_HIGH`<br>5 = `TC_CONTINUE_VISION_SIGNALS`<br>6 = `TC_CONTINUE_AP_ACTIVATED_ON_HARD_STOP`<br>7 = `TC_CONTINUE_ASSUMED_DRIVER_STOPPED`<br>8 = `TC_CONTINUE_PASSED_STOP`<br>9 = `TC_CONTINUE_INVALID_MAP_OR_VISION_CONTROL`<br>10 = `TC_CONTINUE_WARNING_TIMEOUT`<br>11 = `TC_CONTINUE_CLEAR_TO_GO`<br>12 = `TC_CONTINUE_SUMMON_TIMEOUT`<br>13 = `TC_CONTINUE_CONTROL_UNAVAILABLE` | validated |
| `APP_tcConfirmationType` | The mechanism of how the driver confirmed the traffic control. | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TC_CONFIRM_NONE`<br>1 = `TC_CONFIRM_STALK`<br>2 = `TC_CONFIRM_PEDAL` | validated |
| `APP_tcWarningSuppressionReason` | The suppression reason for the traffic control warning feature. | 33\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `TC_WARNING_SUPPRESS_NONE`<br>1 = `TC_WARNING_SUPPRESS_FEATURE_DISABLED`<br>2 = `TC_WARNING_SUPPRESS_INSUFFICIENT_DATA`<br>3 = `TC_WARNING_SUPPRESS_SLOWDOWN_PLANNED`<br>4 = `TC_WARNING_SUPPRESS_BELOW_MIN_SPEED`<br>5 = `TC_WARNING_SUPPRESS_DRIVER_SLOWING_DOWN`<br>6 = `TC_WARNING_SUPPRESS_ASSUMED_YELLOW`<br>7 = `TC_WARNING_SUPPRESS_HARD_TURN`<br>8 = `TC_WARNING_SUPPRESS_LOCALIZATION_DEGRADED`<br>9 = `TC_WARNING_SUPPRESS_PEDAL_OVERRIDE`<br>10 = `TC_WARNING_SUPPRESS_CIPV_CONTINUING`<br>11 = `TC_WARNING_SUPPRESS_LIGHT_UNASSOCIATED`<br>12 = `TC_WARNING_SUPPRESS_WRONG_MAP_TYPE`<br>13 = `TC_WARNING_SUPPRESS_STALE_SIGN_DETECTION`<br>14 = `TC_WARNING_SUPPRESS_CIPV_DID_NOT_STOP`<br>15 = `TC_WARNING_SUPPRESS_AMBIGUOUS_VISION_TYPE`<br>16 = `TC_WARNING_SUPPRESS_NO_ASSOCIATED_VISION_LINE`<br>17 = `TC_WARNING_SUPPRESS_NOT_SUPPORTED_BY_MEASUREMENTS`<br>18 = `TC_WARNING_SUPPRESS_TOO_FAR_FROM_PREDICTED_JUNCTION` | validated |
| `APP_tcUnavailableReason` | The reason why the traffic control feature is currently unavailable. | 38\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AP_UNAVAILBLE_NONE`<br>1 = `AP_UNAVAILBLE_MCU_DISABLED`<br>2 = `AP_UNAVAILBLE_LOST_MAP_LOCALIZATION`<br>3 = `AP_UNAVAILBLE_ROAD_CLASS`<br>4 = `AP_UNAVAILBLE_CAMERA_BLINDED`<br>5 = `AP_UNAVAILBLE_SUN_GLARE`<br>6 = `AP_UNAVAILBLE_ROAD_ESTIMATOR_UNHEALTHY`<br>7 = `AP_UNAVAILBLE_GPS_DEGRADED`<br>8 = `AP_UNAVAILBLE_CAMERA_BLINDED_ON_ROAD_RESTRICTED`<br>9 = `AP_UNAVAILBLE_SUN_GLARE_ON_ROAD_RESTRICTED` | validated |
| `APP_tcVisionLight` | Whether or not the traffic light has a vision measurement. | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_tcVisionSign` | Whether or not the traffic sign has a vision measurement. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_tcVisionRoadMarking` | Whether or not the road marking has a vision measurement. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_tcVisionLine` | Whether or not the traffic control line has a vision measurement. | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
