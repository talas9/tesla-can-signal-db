---
layout: default
title: "DAS_status (0x399) — Driver assistance computer, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: status. Tesla Model Y CAN bus message DAS_status (0x399) of Driver assistance computer, firmware 2026.26.6.5, 26 signals (DAS_autopilotState, DAS_blindSpotRearLeft, DAS_blindSpotRearRight, DAS_fusedSpeedLimit and 22 more). Bit layout, scaling, units and value tables."
---

# DAS_status (0x399) — Driver assistance computer, Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of DAS_status as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_status` |
| CAN id | 0x399 (921) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 26 |

## Signals of DAS_status

Tesla Model Y CAN bus signals in `DAS_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_autopilotState` | Reports the high level autopilot state; raw 15 = signal not available (SNA) | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `DISABLED`<br>1 = `UNAVAILABLE`<br>2 = `AVAILABLE`<br>3 = `ACTIVE_NOMINAL`<br>4 = `ACTIVE_RESTRICTED`<br>5 = `ACTIVE_NAV`<br>6 = `ACTIVE_FSD`<br>8 = `ABORTING`<br>9 = `ABORTED`<br>14 = `FAULT`<br>15 = `SNA` | validated |
| `DAS_blindSpotRearLeft` | Reports rear left blind spot warning level; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_WARNING`<br>1 = `WARNING_LEVEL_1`<br>2 = `WARNING_LEVEL_2`<br>3 = `SNA` | validated |
| `DAS_blindSpotRearRight` | Reports rear right blind spot warning level; raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_WARNING`<br>1 = `WARNING_LEVEL_1`<br>2 = `WARNING_LEVEL_2`<br>3 = `SNA` | validated |
| `DAS_fusedSpeedLimit` | Driver assistance computer: fused speed limit; raw 0 = signal not available (SNA) | 8\|5 | little-endian | unsigned | 5 | 0 | kph/mph | 5 to 150 | 0 = `UNKNOWN_SNA`<br>31 = `NONE` | validated |
| `DAS_suppressSpeedWarning` | Driver assistance computer: suppress speed warning | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `Do_Not_Suppress`<br>1 = `Suppress_Speed_Warning` | validated |
| `DAS_summonObstacle` | Driver assistance computer: summon obstacle | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_summonClearedGate` | Driver assistance computer: summon cleared gate | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_visionOnlySpeedLimit` | Driver assistance computer: vision only speed limit; raw 0 = signal not available (SNA) | 16\|5 | little-endian | unsigned | 5 | 0 | kph/mph | 5 to 150 | 0 = `UNKNOWN_SNA`<br>31 = `NONE` | validated |
| `DAS_heaterState` | The state of the app which runs the front glass heater; raw 0 = signal not available (SNA) | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HEATER_OFF_SNA`<br>1 = `HEATER_ON` | validated |
| `DAS_forwardCollisionWarning` | Driver assistance computer: forward collision warning; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `FORWARD_COLLISION_WARNING`<br>3 = `SNA` | validated |
| `DAS_autoparkReady` | Indicates if all the conditions for Autopark are met. | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `AUTOPARK_UNAVAILABLE`<br>1 = `AUTOPARK_READY` | validated |
| `DAS_autoParked` | Driver assistance computer: auto parked | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_autoparkActive` | Reports whether Autopark is currently active. | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_summonFwdLeashReached` | Driver assistance computer: summon fwd leash reached | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_summonRvsLeashReached` | Driver assistance computer: summon rvs leash reached | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_lssState` | Tracks lane support system state and whether it is controlling steering angle requests for LKA / ELKA. | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LSS_STATE_FAULT`<br>1 = `LSS_STATE_LDW`<br>2 = `LSS_STATE_LKA`<br>3 = `LSS_STATE_ELK`<br>4 = `LSS_STATE_MONITOR`<br>5 = `LSS_STATE_BLINDSPOT`<br>6 = `LSS_STATE_ABORT`<br>7 = `LSS_STATE_OFF` | validated |
| `DAS_sideCollisionAvoid` | Reports if the side collision avoidance function is active on the left or right; raw 3 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `AVOID_LEFT`<br>2 = `AVOID_RIGHT`<br>3 = `SNA` | validated |
| `DAS_sideCollisionWarning` | Reports if the side collision warning function is active in the left or right. | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `WARN_LEFT`<br>2 = `WARN_RIGHT`<br>3 = `WARN_LEFT_RIGHT` | validated |
| `DAS_sideCollisionInhibit` | Driver assistance computer: side collision inhibit | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_INHIBIT`<br>1 = `INHIBIT` | validated |
| `DAS_laneDepartureWarning` | Driver assistance computer: lane departure warning; raw 5 = signal not available (SNA) | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LEFT_WARNING`<br>2 = `RIGHT_WARNING`<br>3 = `LEFT_WARNING_SEVERE`<br>4 = `RIGHT_WARNING_SEVERE`<br>5 = `SNA` | validated |
| `DAS_fleetSpeedState` | The state of the fleet speed algorithm. | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FLEETSPEED_UNAVAILABLE`<br>1 = `FLEETSPEED_AVAILABLE`<br>2 = `FLEETSPEED_ACTIVE`<br>3 = `FLEETSPEED_HOLD` | validated |
| `DAS_autopilotHandsOnState` | Reports the state of the hands on state machine; raw 15 = signal not available (SNA) | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `LC_HANDS_ON_NOT_REQD`<br>1 = `LC_HANDS_ON_REQD_DETECTED`<br>2 = `LC_HANDS_ON_REQD_NOT_DETECTED`<br>3 = `LC_HANDS_ON_REQD_VISUAL`<br>4 = `LC_HANDS_ON_REQD_CHIME_1`<br>5 = `LC_HANDS_ON_REQD_CHIME_2`<br>6 = `LC_HANDS_ON_REQD_SLOWING`<br>7 = `LC_HANDS_ON_REQD_STRUCK_OUT`<br>8 = `LC_HANDS_ON_SUSPENDED`<br>9 = `LC_HANDS_ON_REQD_ESCALATED_CHIME_1`<br>10 = `LC_HANDS_ON_REQD_ESCALATED_CHIME_2`<br>15 = `LC_HANDS_ON_SNA` | validated |
| `DAS_autoLaneChangeState` | Reports the legacy Automatic Lane Change (ALC) state used to drive the instrument cluster User Interface (UI); raw 31 = signal not available (SNA) | 46\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 30 | 0 = `ALC_UNAVAILABLE_DISABLED`<br>1 = `ALC_UNAVAILABLE_NO_LANES`<br>2 = `ALC_UNAVAILABLE_SONICS_INVALID`<br>3 = `ALC_UNAVAILABLE_TP_FOLLOW`<br>4 = `ALC_UNAVAILABLE_EXITING_HIGHWAY`<br>5 = `ALC_UNAVAILABLE_VEHICLE_SPEED`<br>6 = `ALC_AVAILABLE_ONLY_L`<br>7 = `ALC_AVAILABLE_ONLY_R`<br>8 = `ALC_AVAILABLE_BOTH`<br>9 = `ALC_IN_PROGRESS_L`<br>10 = `ALC_IN_PROGRESS_R`<br>11 = `ALC_WAITING_FOR_SIDE_OBST_TO_PASS_L`<br>12 = `ALC_WAITING_FOR_SIDE_OBST_TO_PASS_R`<br>13 = `ALC_WAITING_FOR_FWD_OBST_TO_PASS_L`<br>14 = `ALC_WAITING_FOR_FWD_OBST_TO_PASS_R`<br>15 = `ALC_ABORT_SIDE_OBSTACLE_PRESENT_L`<br>16 = `ALC_ABORT_SIDE_OBSTACLE_PRESENT_R`<br>17 = `ALC_ABORT_POOR_VIEW_RANGE`<br>18 = `ALC_ABORT_LC_HEALTH_BAD`<br>19 = `ALC_ABORT_BLINKER_TURNED_OFF`<br>20 = `ALC_ABORT_OTHER_REASON`<br>21 = `ALC_UNAVAILABLE_SOLID_LANE_LINE`<br>22 = `ALC_BLOCKED_VEH_TTC_L`<br>23 = `ALC_BLOCKED_VEH_TTC_AND_USS_L`<br>24 = `ALC_BLOCKED_VEH_TTC_R`<br>25 = `ALC_BLOCKED_VEH_TTC_AND_USS_R`<br>26 = `ALC_BLOCKED_LANE_TYPE_L`<br>27 = `ALC_BLOCKED_LANE_TYPE_R`<br>28 = `ALC_WAITING_HANDS_ON`<br>29 = `ALC_ABORT_TIMEOUT`<br>30 = `ALC_ABORT_MISSION_PLAN_INVALID`<br>31 = `ALC_SNA` | validated |
| `DAS_summonAvailable` | Driver assistance computer: summon available | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_statusCounter` | Driver assistance computer: status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_statusChecksum` | Driver assistance computer: status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
