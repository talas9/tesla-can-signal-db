---
layout: default
title: "VCRIGHT_seatStatus2 (0x2E3) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: seat status2. Tesla Model Y CAN bus message VCRIGHT_seatStatus2 (0x2E3) of Right body controller, firmware 2026.26.6.5, 61 signals (VCRIGHT_seatStatus2Index, VCRIGHT_frontSeatHeatCurrent, VCRIGHT_frontSeatHeatDuty, VCRIGHT_frontSeatHeatTmp and 57 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_seatStatus2 (0x2E3) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Right body controller message: seat status2; frame length observed on a vehicle bus. This page documents the 61 signals of VCRIGHT_seatStatus2 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_seatStatus2` |
| CAN id | 0x2E3 (739) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 61 |

## Signals of VCRIGHT_seatStatus2

Tesla Model Y CAN bus signals in `VCRIGHT_seatStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_seatStatus2Index` | selector | Right body controller: seat status2 index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SEAT_HEAT_FRONT`<br>1 = `SEAT_HEAT_REARL_CUSHION`<br>2 = `SEAT_HEAT_REARC`<br>3 = `SEAT_HEAT_REARR`<br>4 = `OCCUPANCY`<br>5 = `SEAT_HEAT_REARR_BACKREST`<br>6 = `SEAT_2ROW_ACTUATOR`<br>7 = `SEAT_SWITCH_VOLTAGES_1`<br>8 = `SEAT_SWITCH_VOLTAGES_2`<br>9 = `SEAT_2ROW_EASY_ENTRY`<br>10 = `OCS_IEE`<br>11 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT`<br>12 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT_2`<br>13 = `FRONT_SEAT_THIGH_SUPPORT`<br>14 = `SEAT_3ROW_ADJUSTABLE_FOLD_FLAT`<br>15 = `SEAT_HEAT_3R_RIGHT` | plausible |
| `VCRIGHT_frontSeatHeatCurrent` | page 0 | Right body controller: front seat heat current; raw 12 = signal not available (SNA) | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 | 12 = `SNA` | validated |
| `VCRIGHT_frontSeatHeatDuty` | page 0 | Right body controller: front seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCRIGHT_frontSeatHeatTmp` | page 0 | Right body controller: front seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCRIGHT_frontSeatHeatTmpTarget` | page 0 | Target temperature for front right seat heater | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | contradicted |
| `VCRIGHT_frontSeatHeatInhibited` | page 0 | Front right seat heater duty cycle | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatHeatPowered` | page 0 | Right body controller: front seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_AH_1RowRightSeatHeatVentHealth` | page 0 | Right body controller: AH 1 row right seat heat vent health | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_HEAT_VENT_HEALTH_UNKNOWN`<br>1 = `SEAT_HEAT_VENT_HEALTHY`<br>2 = `SEAT_HEAT_VENT_UNAVAILABLE` | validated |
| `VCRIGHT_rearLSeatHeatCurrent` | page 1 | Current drawn by rear center seat heater | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `VCRIGHT_rearLSeatHeatDuty` | page 1 | Right body controller: rear l seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCRIGHT_rearLSeatHeatTmp` | page 1 | Right body controller: rear l seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCRIGHT_rearLSeatHeatTmpTarget` | page 1 | Right body controller: rear l seat heat tmp target | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCRIGHT_rearLSeatHeatInhibited` | page 1 | Right body controller: rear l seat heat inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rearLSeatHeatPowered` | page 1 | Right body controller: rear l seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rearCSeatHeatCurrent` | page 2 | Right body controller: rear c seat heat current | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `VCRIGHT_rearCSeatHeatDuty` | page 2 | Right body controller: rear c seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCRIGHT_rearCSeatHeatTmp` | page 2 | Right body controller: rear c seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCRIGHT_rearCSeatHeatTmpTarget` | page 2 | Right body controller: rear c seat heat tmp target | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCRIGHT_rearCSeatHeatInhibited` | page 2 | Right body controller: rear c seat heat inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rearCSeatHeatPowered` | page 2 | Right body controller: rear c seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rearRSeatHeatCurrent` | page 3 | Right body controller: rear r seat heat current | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `VCRIGHT_rearRSeatHeatDuty` | page 3 | Right body controller: rear r seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCRIGHT_rearRSeatHeatTmp` | page 3 | Right body controller: rear r seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCRIGHT_rearRSeatHeatTmpTarget` | page 3 | Right body controller: rear r seat heat tmp target | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | contradicted |
| `VCRIGHT_rearRSeatHeatInhibited` | page 3 | Right body controller: rear r seat heat inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rearRSeatHeatPowered` | page 3 | Right body controller: rear r seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeatReclineState` | page 11 | Reports the active state of the 2nd row seat recliner; raw 15 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_STOPPED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_COMFORT`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_COMFORT`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_FAST`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_FAST`<br>5 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_FOLDING`<br>6 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_UNFOLDING`<br>7 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_FORWARD_TO_POSITION`<br>8 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_REARWARD_TO_POSITION`<br>9 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ZERO_POSITION`<br>12 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_SNA` | validated |
| `VCRIGHT_2RowSeatReclineDuty` | page 11 | Reports the 2nd row seat recliner motor duty cycle | 8\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_2RowSeatReclineCurrent` | page 11 | Reports the 2nd row seat recliner motor current | 16\|12 | little-endian | signed | 0.05 | 0 | A | -100 to 100 |  | validated |
| `VCRIGHT_2RowSeatReclineCalibrated` | page 11 | Reports calibration status of the 2nd row seat recliner | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeatReclinePositionRaw` | page 11 | Reports the 2nd row seat recliner raw encoder count | 29\|12 | little-endian | signed | 1 | 0 |  | -2048 to 2047 |  | validated |
| `VCRIGHT_2RowSeatReclineAngle` | page 11 | Reports the position of the 2nd row seat recliner in degrees | 41\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_2RowSeatReclineAbsPosSwitchState` | page 11 | Reports the status of 2nd row seat recline absolute position (comfort zone) switch; raw 0 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCRIGHT_2RowSeatReclinePositionState` | page 12 | Reports the active position state of the 2nd row seat recliner; raw 4 = signal not available (SNA) | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_FOLDED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNFOLDED`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNSAFE_INTERMEDIATE`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNKNOWN`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_SNA` | validated |
| `VCRIGHT_2RowSeatReclineAdjustmentAllowed` | page 12 | Indicates whether adjustment requests are currently permitted for the rear seat recliner | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeatReclineFoldAllowed` | page 12 | Indicates whether auto-fold requests are currently permitted for the rear seat recliner | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeatReclineUnfoldAllowed` | page 12 | Indicates whether auto-unfold requests are currently permitted for the rear seat recliner | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeatReclineNextToggleDirection` | page 12 | Right body controller: 2 row seat recline next toggle direction; raw 2 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_FOLD`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_UNFOLD`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_SNA` | validated |
| `VCRIGHT_2RowSeatReclineChoreoBlockedByOccupancy` | page 12 | Right body controller: 2 row seat recline choreo blocked by occupancy | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_2RowSeat1RClashAvoidanceBlockedReason` | page 12 | Right body controller: 2 row seat1 r clash avoidance blocked reason | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_NONE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_VEHICLE_IN_MOTION`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_UNCALIBRATED`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_REAR_SEAT_UNCALIBRATED`<br>4 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_PROFILE_RECALL`<br>5 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_MOVING`<br>6 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_OCCUPANCY` | validated |
| `VCRIGHT_2RowSeat1RClashAvoidanceState` | page 12 | Right body controller: 2 row seat1 r clash avoidance state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_IDLE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_FRONT_SEAT_CLEARING`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_WAITING_TO_RESTORE_FRONT_SEAT`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_RESTORING_FRONT_SEAT` | validated |
| `VCRIGHT_2RowSeatReclineAbsPosSwitchTransPoint` | page 12 | Right body controller: 2 row seat recline abs pos switch trans point | 18\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VC_AH_2RowRightSeatMovementHealth` | page 12 | Right body controller: AH 2 row right seat movement health | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOVEMENT_HEALTH_UNKNOWN`<br>1 = `SEAT_MOVEMENT_HEALTHY`<br>2 = `SEAT_CANNOT_MOVE`<br>3 = `SEAT_IN_NON_USE_POSITION`<br>4 = `SEAT_CALIBRATION_REQUIRED` | validated |
| `VCRIGHT_3RowSeatReclineState` | page 14 | Reports active state of the rear seat recliner; raw 15 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_STOPPED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_COMFORT`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_COMFORT`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_FAST`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_FAST`<br>5 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_FOLDING`<br>6 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_UNFOLDING`<br>7 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_FORWARD_TO_POSITION`<br>8 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_REARWARD_TO_POSITION`<br>9 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ZERO_POSITION`<br>12 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_SNA` | validated |
| `VCRIGHT_3RowSeatReclineDuty` | page 14 | Reports the third row seat recliner motor duty cycle | 8\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_3RowSeatReclineCurrent` | page 14 | Reports the third row seat recliner motor current | 16\|12 | little-endian | signed | 0.05 | 0 | A | -100 to 100 |  | validated |
| `VCRIGHT_3RowSeatReclineCalibrated` | page 14 | Reports calibration status of the third row seat recliner | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclinePositionRaw` | page 14 | Reports the third row seat recliner raw encoder count | 29\|12 | little-endian | signed | 1 | 0 |  | -2048 to 2047 |  | validated |
| `VCRIGHT_3RowSeatReclineAngle` | page 14 | Reports position of the 3rd row seat recliner in degrees | 41\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_3RowSeatReclineNextToggleDirection` | page 14 | Right body controller: 3 row seat recline next toggle direction; raw 2 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_FOLD`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_UNFOLD`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_SNA` | validated |
| `VCRIGHT_3RRightSeatHeatCurrent` | page 15 | Current drawn by 3rd row right seat heater | 5\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `VCRIGHT_3RRightSeatHeatDuty` | page 15 | 3rd row right seat heater duty cycle | 17\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_3RRightSeatHeatTmp` | page 15 | Temperature of 3rd row right seat heater as reported by NTC | 25\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCRIGHT_3RRightSeatHeatTmpTarget` | page 15 | Target temperature for 3rd row right seat heater | 37\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCRIGHT_3RRightSeatHeatInhibited` | page 15 | Status describing whether 3rd row right seat heat is inhibited | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclinePositionState` | page 15 | Reports active position state of the rear seat recliner; raw 4 = signal not available (SNA) | 46\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_FOLDED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNFOLDED`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNSAFE_INTERMEDIATE`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNKNOWN`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_SNA` | validated |
| `VCRIGHT_3RowSeatReclineAdjustmentAllowed` | page 15 | Indicates whether adjustment requests are currently permitted for the rear seat recliner | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclineFoldAllowed` | page 15 | Indicates whether auto-fold requests are currently permitted for the rear seat recliner | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclineUnfoldAllowed` | page 15 | Indicates whether auto-unfold requests are currently permitted for the rear seat recliner | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclineChoreoBlockedByOccupancy` | page 15 | Right body controller: 3 row seat recline choreo blocked by occupancy | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_3RowSeatReclineAbsPosSwitchState` | page 15 | Reports status of 2R seat recline absolute position (comfort zone) switch; raw 0 = signal not available (SNA) | 53\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |

## Multiplexing

`VCRIGHT_seatStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (6 signals), page 2 (6 signals), page 3 (6 signals), page 11 (7 signals), page 12 (10 signals), page 14 (7 signals), page 15 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
