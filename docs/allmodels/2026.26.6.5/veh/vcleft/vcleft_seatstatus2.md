---
layout: default
title: "VCLEFT_seatStatus2 (0x2E2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: seat status2. Tesla Model 3 / Model Y CAN bus message VCLEFT_seatStatus2 (0x2E2) of Left body controller, firmware 2026.26.6.5, 51 signals (VCLEFT_seatStatus2Index, VCLEFT_frontSeatHeatCurrent, VCLEFT_frontSeatHeatDuty, VCLEFT_frontSeatHeatTmp and 47 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_seatStatus2 (0x2E2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left body controller message: seat status2; frame length observed on a vehicle bus. This page documents the 51 signals of VCLEFT_seatStatus2 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_seatStatus2` |
| CAN id | 0x2E2 (738) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 51 |

## Signals of VCLEFT_seatStatus2

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_seatStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_seatStatus2Index` | selector | Left body controller: seat status2 index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SEAT_HEAT_FRONT`<br>1 = `SEAT_HEAT_REARL_BACKREST`<br>2 = `OCCUPANCY`<br>3 = `SEAT_HEAT_REARL`<br>4 = `SEAT_HEAT_REARC`<br>5 = `SEAT_HEAT_REARR_CUSHION`<br>6 = `SEAT_2ROW_ACTUATOR`<br>7 = `SEAT_SWITCH_VOLTAGES_1`<br>8 = `SEAT_SWITCH_VOLTAGES_2`<br>9 = `SEAT_2ROW_EASY_ENTRY`<br>10 = `SEAT_HEAT_3R_LEFT`<br>11 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT`<br>12 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT_2`<br>13 = `FRONT_SEAT_THIGH_SUPPORT`<br>14 = `SEAT_3ROW_ADJUSTABLE_FOLD_FLAT`<br>15 = `SEAT_HEAT_3R_RIGHT_CUSHION` | plausible |
| `VCLEFT_frontSeatHeatCurrent` | page 0 | Left body controller: front seat heat current; raw 12 = signal not available (SNA) | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 | 12 = `SNA` | validated |
| `VCLEFT_frontSeatHeatDuty` | page 0 | Left body controller: front seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCLEFT_frontSeatHeatTmp` | page 0 | Left body controller: front seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCLEFT_frontSeatHeatTmpTarget` | page 0 | Left body controller: front seat heat tmp target | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | contradicted |
| `VCLEFT_frontSeatHeatInhibited` | page 0 | Left body controller: front seat heat inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontSeatHeatPowered` | page 0 | Left body controller: front seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeatFoldLeftSwitch` | page 0 | Reports status of the left seat fold switch in the second row; raw 0 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_2RowSeatUnfoldLeftSwitch` | page 0 | Reports status of the left seat unfold switch in the second row; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_2RowSeatFoldRightSwitch` | page 0 | Reports status of the right seat fold switch in the second row; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_2RowSeatUnfoldRightSwitch` | page 0 | Reports status of the right seat unfold switch in the second row; raw 0 = signal not available (SNA) | 52\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_3RowSeatFoldLeftSwitch` | page 0 | Reports status of the left seat fold switch in the third row; raw 0 = signal not available (SNA) | 54\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_3RowSeatUnfoldLeftSwitch` | page 0 | Reports status of the left seat unfold switch in the third row; raw 0 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_3RowSeatFoldRightSwitch` | page 0 | Reports status of the right seat fold switch in the third row; raw 0 = signal not available (SNA) | 58\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_3RowSeatUnfoldRightSwitch` | page 0 | Reports status of the right seat unfold switch in the third row; raw 0 = signal not available (SNA) | 60\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VC_AH_1RowLeftSeatHeatVentHealth` | page 0 | Left body controller: AH 1 row left seat heat vent health | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_HEAT_VENT_HEALTH_UNKNOWN`<br>1 = `SEAT_HEAT_VENT_HEALTHY`<br>2 = `SEAT_HEAT_VENT_UNAVAILABLE` | validated |
| `VCLEFT_2RowSeatReclineState` | page 11 | Reports the active state of the 2nd row seat recliner; raw 15 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_STOPPED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_COMFORT`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_COMFORT`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_FAST`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_FAST`<br>5 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_FOLDING`<br>6 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_UNFOLDING`<br>7 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_FORWARD_TO_POSITION`<br>8 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_REARWARD_TO_POSITION`<br>9 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ZERO_POSITION`<br>12 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_SNA` | validated |
| `VCLEFT_2RowSeatReclineDuty` | page 11 | Reports the 2nd row seat recliner motor duty cycle | 8\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_2RowSeatReclineCurrent` | page 11 | Reports the 2nd row seat recliner motor current | 16\|12 | little-endian | signed | 0.05 | 0 | A | -100 to 100 |  | validated |
| `VCLEFT_2RowSeatReclineCalibrated` | page 11 | Reports calibration status of the 2nd row seat recliner | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeatReclinePositionRaw` | page 11 | Reports the 2nd row seat recliner raw encoder count | 29\|12 | little-endian | signed | 1 | 0 |  | -2048 to 2047 |  | validated |
| `VCLEFT_2RowSeatReclineAngle` | page 11 | Reports the position of the 2nd row seat recliner in degrees | 41\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCLEFT_2RowSeatReclineAbsPosSwitchState` | page 11 | Reports the status of 2nd row seat recline absolute position (comfort zone) switch; raw 0 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCLEFT_2RowSeatReclinePositionState` | page 12 | Reports the active position state of the 2nd row seat recliner; raw 4 = signal not available (SNA) | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_FOLDED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNFOLDED`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNSAFE_INTERMEDIATE`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNKNOWN`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_SNA` | validated |
| `VCLEFT_2RowSeatReclineAdjustmentAllowed` | page 12 | Indicates whether adjustment requests are currently permitted for the rear seat recliner | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeatReclineFoldAllowed` | page 12 | Indicates whether auto-fold requests are currently permitted for the rear seat recliner | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeatReclineUnfoldAllowed` | page 12 | Indicates whether auto-unfold requests are currently permitted for the rear seat recliner | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeatReclineNextToggleDirection` | page 12 | Left body controller: 2 row seat recline next toggle direction; raw 2 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_FOLD`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_UNFOLD`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_SNA` | validated |
| `VCLEFT_2RowSeatReclineChoreoBlockedByOccupancy` | page 12 | Left body controller: 2 row seat recline choreo blocked by occupancy | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_2RowSeat1RClashAvoidanceBlockedReason` | page 12 | Left body controller: 2 row seat1 r clash avoidance blocked reason | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_NONE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_VEHICLE_IN_MOTION`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_UNCALIBRATED`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_REAR_SEAT_UNCALIBRATED`<br>4 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_PROFILE_RECALL`<br>5 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_MOVING`<br>6 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_OCCUPANCY` | validated |
| `VCLEFT_2RowSeat1RClashAvoidanceState` | page 12 | Left body controller: 2 row seat1 r clash avoidance state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_IDLE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_FRONT_SEAT_CLEARING`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_WAITING_TO_RESTORE_FRONT_SEAT`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_RESTORING_FRONT_SEAT` | validated |
| `VCLEFT_2RowSeatReclineAbsPosSwitchTransPoint` | page 12 | Left body controller: 2 row seat recline abs pos switch trans point | 18\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VC_AH_2RowLeftSeatMovementHealth` | page 12 | Left body controller: AH 2 row left seat movement health | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOVEMENT_HEALTH_UNKNOWN`<br>1 = `SEAT_MOVEMENT_HEALTHY`<br>2 = `SEAT_CANNOT_MOVE`<br>3 = `SEAT_IN_NON_USE_POSITION`<br>4 = `SEAT_CALIBRATION_REQUIRED` | validated |
| `VCLEFT_3RowSeatReclineState` | page 14 | Reports active state of the rear seat recliner; raw 15 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_STOPPED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_COMFORT`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_COMFORT`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_FAST`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_FAST`<br>5 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_FOLDING`<br>6 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_UNFOLDING`<br>7 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_FORWARD_TO_POSITION`<br>8 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_REARWARD_TO_POSITION`<br>9 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ZERO_POSITION`<br>12 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_SNA` | validated |
| `VCLEFT_3RowSeatReclineDuty` | page 14 | Reports the third row seat recliner motor duty cycle | 8\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_3RowSeatReclineCurrent` | page 14 | Reports the third row seat recliner motor current | 16\|12 | little-endian | signed | 0.05 | 0 | A | -100 to 100 |  | validated |
| `VCLEFT_3RowSeatReclineCalibrated` | page 14 | Reports calibration status of the third row seat recliner | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclinePositionRaw` | page 14 | Reports the third row seat recliner raw encoder count | 29\|12 | little-endian | signed | 1 | 0 |  | -2048 to 2047 |  | validated |
| `VCLEFT_3RowSeatReclineAngle` | page 14 | Reports position of the 3rd row seat recliner in degrees | 41\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCLEFT_3RowSeatReclineNextToggleDirection` | page 14 | Left body controller: 3 row seat recline next toggle direction; raw 2 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_FOLD`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_UNFOLD`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_SNA` | validated |
| `VCLEFT_3RRightCushionHeatCurrent` | page 15 | Current drawn by 3rd row right seat heater | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `VCLEFT_3RRightCushionHeatDuty` | page 15 | 3rd row right seat heater duty cycle | 16\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_3RRightCushionHeatTmp` | page 15 | Left body controller: 3 r right cushion heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCLEFT_3RRightCushionHeatTmpTarget` | page 15 | Target temperature for 3rd row right seat heater | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCLEFT_3RRightCushionHeatInhibited` | page 15 | Status describing whether 3rd row right seat heat is inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclinePositionState` | page 15 | Reports active position state of the rear seat recliner; raw 4 = signal not available (SNA) | 46\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_FOLDED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNFOLDED`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNSAFE_INTERMEDIATE`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNKNOWN`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_SNA` | validated |
| `VCLEFT_3RowSeatReclineAdjustmentAllowed` | page 15 | Indicates whether adjustment requests are currently permitted for the rear seat recliner | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclineFoldAllowed` | page 15 | Indicates whether auto-fold requests are currently permitted for the rear seat recliner | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclineUnfoldAllowed` | page 15 | Indicates whether auto-unfold requests are currently permitted for the rear seat recliner | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclineChoreoBlockedByOccupancy` | page 15 | Left body controller: 3 row seat recline choreo blocked by occupancy | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_3RowSeatReclineAbsPosSwitchState` | page 15 | Reports status of 2R seat recline absolute position (comfort zone) switch; raw 0 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |

## Multiplexing

`VCLEFT_seatStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (15 signals), page 11 (7 signals), page 12 (10 signals), page 14 (7 signals), page 15 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
