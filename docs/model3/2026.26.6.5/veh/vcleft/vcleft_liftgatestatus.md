---
layout: default
title: "VCLEFT_liftgateStatus (0x142) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: liftgate status. Tesla Model 3 CAN bus message VCLEFT_liftgateStatus (0x142) of Left body controller, firmware 2026.26.6.5, 22 signals (VCLEFT_liftgateStatusIndex, VCLEFT_liftgateState, VCLEFT_liftgateStoppingCondition, VCLEFT_liftgateMvmntNotAllowedCondition and 18 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_liftgateStatus (0x142) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: liftgate status; frame length observed on a vehicle bus. This page documents the 22 signals of VCLEFT_liftgateStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_liftgateStatus` |
| CAN id | 0x142 (322) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 22 |

## Signals of VCLEFT_liftgateStatus

Tesla Model 3 CAN bus signals in `VCLEFT_liftgateStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_liftgateStatusIndex` | selector | Left body controller: liftgate status index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0`<br>1 = `1`<br>2 = `INVALID` | plausible |
| `VCLEFT_liftgateState` | page 0 | State of the power liftgate | 3\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PLG_STATE_INIT`<br>1 = `PLG_STATE_OFF`<br>2 = `PLG_STATE_BACKOFF`<br>3 = `PLG_STATE_OPENING`<br>4 = `PLG_STATE_CLOSING`<br>5 = `PLG_STATE_CLOSED`<br>6 = `PLG_STATE_LATCH_OPENING`<br>7 = `PLG_STATE_LATCH_CLOSING`<br>8 = `PLG_STATE_NOT_INSTALLED`<br>9 = `PLG_STATE_UNKNOWN`<br>10 = `PLG_STATE_LATCH_EXIT`<br>11 = `PLG_STATE_END_OF_TRAVEL`<br>12 = `PLG_STATE_LATCH_ENTRY`<br>13 = `PLG_STATE_PARTY_DANCE` | validated |
| `VCLEFT_liftgateStoppingCondition` | page 0 | Stopping condition for the power liftgate | 10\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PLG_STOPPING_CONDITION_NONE`<br>1 = `PLG_STOPPING_CONDITION_PINCH`<br>2 = `PLG_STOPPING_CONDITION_OBSTACLE_STALL`<br>3 = `PLG_STOPPING_CONDITION_LOW_12V`<br>4 = `PLG_STOPPING_CONDITION_STATE_TIMEOUT`<br>5 = `PLG_STOPPING_CONDITION_VEHICLE_AT_SPEED`<br>6 = `PLG_STOPPING_CONDITION_OBSTACLE_CURRENT`<br>7 = `PLG_STOPPING_CONDITION_OBSTACLE_TRAJ_POS`<br>8 = `PLG_STOPPING_CONDITION_OBSTACLE_TRAJ_VEL`<br>9 = `PLG_STOPPING_CONDITION_UNCALIBRATED`<br>10 = `PLG_STOPPING_CONDITION_LATCH_FAULT`<br>11 = `PLG_STOPPING_CONDITION_OBSTACLE_CURRENT_SPIKE`<br>12 = `PLG_STOPPING_CONDITION_FOLLOWER_REQUEST`<br>13 = `PLG_STOPPING_CONDITION_COUNT` | validated |
| `VCLEFT_liftgateMvmntNotAllowedCondition` | page 0 | Movement not allowed condition for the power liftgate | 14\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PLG_MVMT_NOT_ALLOWED_NONE`<br>1 = `PLG_MVMT_NOT_ALLOWED_LOW_12V`<br>2 = `PLG_MVMT_NOT_ALLOWED_VEHICLE_AT_SPEED`<br>3 = `PLG_MVMT_NOT_ALLOWED_UNCALIBRATED`<br>4 = `PLG_MVMT_NOT_ALLOWED_EXTERIOR_PRESS_AT_MAX_OPEN`<br>5 = `PLG_MVMT_NOT_ALLOWED_LOCKED`<br>6 = `PLG_MVMT_NOT_ALLOWED_STRUT_POSITION_MISMATCH` | validated |
| `VCLEFT_liftgatePositionCalibrated` | page 0 | Liftgate calibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateUIChimeRequest` | page 0 | Request from the liftgate module to sound a UI chime | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `REMOTE_CHIME_REQUEST_NONE`<br>1 = `REMOTE_CHIME_REQUEST_ONE_SHORT`<br>2 = `REMOTE_CHIME_REQUEST_TWO_SHORT`<br>3 = `REMOTE_CHIME_REQUEST_THREE_SHORT`<br>4 = `REMOTE_CHIME_REQUEST_ONE_LONG` | validated |
| `VCLEFT_liftgatePhysicalChimeRequest` | page 0 | Request from the liftgate module to sound a physical chime | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `REMOTE_CHIME_REQUEST_NONE`<br>1 = `REMOTE_CHIME_REQUEST_ONE_SHORT`<br>2 = `REMOTE_CHIME_REQUEST_TWO_SHORT`<br>3 = `REMOTE_CHIME_REQUEST_THREE_SHORT`<br>4 = `REMOTE_CHIME_REQUEST_ONE_LONG` | validated |
| `VCLEFT_liftgateEstimatedStrutTemp` | page 0 | Left body controller: liftgate estimated strut temp | 24\|8 | little-endian | unsigned | 1 | -60 | C | -60 to 195 |  | validated |
| `VCLEFT_liftgateStaticStrutMode` | page 0 | Static strut mode based on its velocity; raw 0 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `PLG_STATIC_STRUT_MODE_UNKNOWN_SNA`<br>1 = `PLG_STATIC_STRUT_MODE_OFF_COAST`<br>2 = `PLG_STATIC_STRUT_MODE_BRAKE_HOLD`<br>3 = `PLG_STATIC_STRUT_MODE_CLOSE_COAST`<br>4 = `PLG_STATIC_STRUT_MODE_OPEN_COAST`<br>5 = `PLG_STATIC_STRUT_MODE_SLAM_BRAKE` | validated |
| `VCLEFT_liftgateRequestSource` | page 0 | Movement request source for the power liftgate | 35\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PLG_REQUEST_SOURCE_NONE`<br>1 = `PLG_REQUEST_SOURCE_MCU_SWITCH`<br>2 = `PLG_REQUEST_SOURCE_EXTERIOR`<br>3 = `PLG_REQUEST_SOURCE_SHUTFACE`<br>4 = `PLG_REQUEST_SOURCE_KEY_TRUNK_BUTTON`<br>5 = `PLG_REQUEST_SOURCE_VCSEC_COMMAND`<br>6 = `PLG_REQUEST_SOURCE_PARTY`<br>7 = `PLG_REQUEST_SOURCE_UDS`<br>8 = `PLG_REQUEST_SOURCE_EMERG_RELEASE`<br>9 = `PLG_REQUEST_SOURCE_DAS` | validated |
| `VCLEFT_liftgateNewHeightNudge` | page 0 | Left body controller: liftgate new height nudge | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateNewSaveHeight` | page 0 | Newly saved height of liftgate tip at max open | 40\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | validated |
| `VCLEFT_liftgateGeofenceState` | page 0 | State of the geofence save process | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PLG_GEOFENCE_STATE_INIT`<br>1 = `PLG_GEOFENCE_STATE_WAITING_TO_TRIGGER`<br>2 = `PLG_GEOFENCE_STATE_SETTING_HEIGHT`<br>3 = `PLG_GEOFENCE_STATE_WAITING_TO_STOP` | validated |
| `VCLEFT_liftgateCloseWarnChimeRequest` | page 0 | Left body controller: liftgate close warn chime request | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateAboveCrossoverAngle` | page 0 | Left body controller: liftgate above crossover angle | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateLatchRequest` | page 0 | Reqeusts the liftgate latch to perform an action | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LATCH_REQUEST_NONE`<br>1 = `LATCH_REQUEST_CINCH`<br>2 = `LATCH_REQUEST_RELEASE_V2`<br>3 = `LATCH_REQUEST_FORCE_RELEASE`<br>4 = `LATCH_REQUEST_RESET` | validated |
| `VCLEFT_liftgateStrutDutyCycle` | page 1 | Left body controller: liftgate strut duty cycle | 3\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_liftgateStrutCurrent` | page 1 | Left body controller: liftgate strut current | 11\|10 | little-endian | signed | 0.1 | 0 | A | -30 to 30 |  | validated |
| `VCLEFT_liftgatePosition` | page 1 | Liftgate position | 21\|7 | little-endian | signed | 1 | 46 | deg | -5 to 95 |  | validated |
| `VCLEFT_liftgateSpeed` | page 1 | Left body controller: liftgate speed | 28\|10 | little-endian | signed | 0.1 | 0 | deg/s | -30 to 30 |  | validated |
| `VCLEFT_liftgateHeight` | page 1 | Height of the liftgate tip above the ground | 38\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | validated |
| `VCLEFT_liftgatePositionDiff` | page 1 | Left body controller: liftgate position diff | 46\|6 | little-endian | signed | 1 | 0 | deg | -30 to 30 |  | validated |

## Multiplexing

`VCLEFT_liftgateStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (15 signals), page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
