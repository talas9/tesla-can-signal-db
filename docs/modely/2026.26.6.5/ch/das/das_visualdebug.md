---
layout: default
title: "DAS_visualDebug (0x24A) — Driver assistance computer, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: visual debug. Tesla Model Y CAN bus message DAS_visualDebug (0x24A) of Driver assistance computer, firmware 2026.26.6.5, 26 signals (DAS_autosteerVehiclesUsage, DAS_autosteerHPPUsage, DAS_autosteerNavigationUsage, DAS_autosteerModelUsage and 22 more). Bit layout, scaling, units and value tables."
---

# DAS_visualDebug (0x24A) — Driver assistance computer, Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer message: visual debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of DAS_visualDebug as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_visualDebug` |
| CAN id | 0x24A (586) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 26 |

## Signals of DAS_visualDebug

Tesla Model Y CAN bus signals in `DAS_visualDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_autosteerVehiclesUsage` | Driver assistance computer: autosteer vehicles usage | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_autosteerHPPUsage` | Driver assistance computer: autosteer HPP usage | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_autosteerNavigationUsage` | Driver assistance computer: autosteer navigation usage | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_autosteerModelUsage` | Driver assistance computer: autosteer model usage | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_autosteerBottsDotsUsage` | Driver assistance computer: autosteer botts dots usage | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_offsetSide` | Driver assistance computer: offset side | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_OFFSET`<br>1 = `OFFSET_RIGHT_OBJECT`<br>2 = `OFFSET_LEFT_OBJECT`<br>3 = `OFFSET_BOTH_OBJECTS` | plausible |
| `DAS_roadSurfaceType` | Driver assistance computer: road surface type; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `ROAD_SURFACE_SNA`<br>1 = `ROAD_SURFACE_NORMAL`<br>2 = `ROAD_SURFACE_ENHANCED` | plausible |
| `DAS_autosteerHealthAnomalyLevel` | Driver assistance computer: autosteer health anomaly level | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DAS_autosteerHealthState` | Driver assistance computer: autosteer health state | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HEALTH_UNAVAILABLE`<br>1 = `HEALTH_NOMINAL`<br>2 = `HEALTH_DEGRADED`<br>3 = `HEALTH_SEVERELY_DEGRADED`<br>4 = `HEALTH_ABORTING`<br>5 = `HEALTH_FAULT` | plausible |
| `DAS_lastLinePreferenceReason` | Driver assistance computer: last line preference reason | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OTHER_LANE_DISAGREES_WITH_MODEL`<br>1 = `AGREEMENT_WITH_NEIGHBOR_LANES`<br>2 = `NEIGHBOR_LANE_PROBABILIY`<br>3 = `NAVIGATION_BRANCH`<br>4 = `AVOID_ONCOMING_LANES`<br>5 = `COUNTRY_DRIVING_SIDE`<br>15 = `NONE` | plausible |
| `DAS_plannerState` | Driver assistance computer: planner state | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TP_EXTSTATE_DISABLED`<br>1 = `TP_EXTSTATE_VL`<br>2 = `TP_EXTSTATE_FOLLOW`<br>3 = `TP_EXTSTATE_LANECHANGE_REQUESTED`<br>4 = `TP_EXTSTATE_LANECHANGE_IN_PROGRESS`<br>5 = `TP_EXTSTATE_LANECHANGE_WAIT_FOR_SIDE_OBSTACLE`<br>6 = `TP_EXTSTATE_LANECHANGE_WAIT_FOR_FWD_OBSTACLE`<br>7 = `TP_EXTSTATE_LANECHANGE_ABORT` | plausible |
| `DAS_lastAutosteerAbortReason` | Driver assistance computer: last autosteer abort reason | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `UI_ABORT_REASON_HM_LANE_VIEW_RANGE`<br>1 = `UI_ABORT_REASON_HM_VIRTUAL_LANE_NO_INPUTS`<br>2 = `UI_ABORT_REASON_HM_STEERING_ERROR`<br>14 = `UI_ABORT_REASON_APP_ME_STATE_NOT_VISION`<br>15 = `UI_ABORT_REASON_ME_MAIN_STATE_NOT_VISION`<br>16 = `UI_ABORT_REASON_CAM_MSG_MIA`<br>17 = `UI_ABORT_REASON_CAM_WATCHDOG`<br>18 = `UI_ABORT_REASON_TRAILER_MODE`<br>19 = `UI_ABORT_REASON_SIDE_COLLISION_IMMINENT`<br>20 = `UI_ABORT_REASON_EPAS_EAC_DENIED`<br>21 = `UI_ABORT_REASON_COMPONENT_MIA`<br>22 = `UI_ABORT_REASON_CRUISE_FAULT`<br>23 = `UI_ABORT_REASON_CID_SWITCH_DISABLED`<br>24 = `UI_ABORT_REASON_DRIVING_OFF_NAV`<br>25 = `UI_ABORT_REASON_VEHICLE_SPEED_ABOVE_MAX`<br>26 = `UI_ABORT_REASON_FOLLOWER_OUTPUT_INVALID`<br>27 = `UI_ABORT_REASON_PLANNER_OUTPUT_INVALID`<br>28 = `UI_ABORT_REASON_EPAS_ERROR_CODE`<br>29 = `UI_ABORT_REASON_ACC_CANCEL`<br>30 = `UI_ABORT_REASON_CAMERA_FAILSAFES`<br>31 = `UI_ABORT_REASON_NO_ABORT`<br>32 = `UI_ABORT_REASON_AEB`<br>33 = `UI_ABORT_REASON_SEATBELT_UNBUCKLED`<br>34 = `UI_ABORT_REASON_USER_OVERRIDE_STRIKEOUT`<br>35 = `UI_ABORT_REASON_DRIVER_NOT_PRESENT`<br>36 = `UI_ABORT_REASON_AHB_MANUAL_OVERRIDE` | plausible |
| `DAS_devAppInterfaceEnabled` | Driver assistance computer: dev app interface enabled | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_navAvailable` | Driver assistance computer: nav available | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS_NAV_UNAVAILABLE`<br>1 = `DAS_NAV_AVAILABLE` | plausible |
| `DAS_navDistance` | Driver assistance computer: nav distance | 40\|8 | little-endian | unsigned | 100 | 0 | km | 0 to 25500 |  | plausible |
| `DAS_accSmartSpeedActive` | Driver assistance computer: acc smart speed active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_accSmartSpeedState` | Driver assistance computer: acc smart speed state; raw 7 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE_OFFRAMP`<br>2 = `ACTIVE_INTEGRATING`<br>3 = `ACTIVE_ONRAMP`<br>4 = `SET_SPEED_SET_REQUESTED`<br>5 = `OFFRAMP_DELAY`<br>7 = `SNA` | plausible |
| `DAS_ulcInProgress` | Reports active lane changes that were not commanded. | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ULC_INACTIVE`<br>1 = `ULC_ACTIVE` | plausible |
| `DAS_trafficAwareSetSpeedInUse` | Indicates that autopilot is using cruise set speed based on flow of traffic | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_isaSystemState` | ISA system state | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ISA_NOMINAL`<br>1 = `ISA_ASSUMED_LIMITS`<br>2 = `ISA_INVALID`<br>3 = `ISA_UNAVAILABLE` | plausible |
| `DAS_behaviorType` | Driver assistance computer: behavior type | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DAS_BEHAVIOR_INVALID`<br>1 = `DAS_BEHAVIOR_IN_LANE`<br>2 = `DAS_BEHAVIOR_LANE_CHANGE_LEFT`<br>3 = `DAS_BEHAVIOR_LANE_CHANGE_RIGHT` | plausible |
| `DAS_ulcType` | Reports the underlying reason for the uncommanded lane change, whether for speed or route. | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ULC_TYPE_NONE`<br>1 = `ULC_TYPE_NAV`<br>2 = `ULC_TYPE_SPEED` | plausible |
| `DAS_rearVehDetectedThisCycle` | Driver assistance computer: rear veh detected this cycle | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VEHICLE_NOT_DETECTED`<br>1 = `VEHICLE_DETECTED` | plausible |
| `DAS_rearLeftVehDetectedCurrent` | Driver assistance computer: rear left veh detected current | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VEHICLE_NOT_DETECTED`<br>1 = `VEHICLE_DETECTED` | plausible |
| `DAS_rearRightVehDetectedTrip` | Driver assistance computer: rear right veh detected trip | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VEHICLE_NOT_DETECTED`<br>1 = `VEHICLE_DETECTED` | plausible |
| `DAS_rearLeftVehDetectedTrip` | Driver assistance computer: rear left veh detected trip | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VEHICLE_NOT_DETECTED`<br>1 = `VEHICLE_DETECTED` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
