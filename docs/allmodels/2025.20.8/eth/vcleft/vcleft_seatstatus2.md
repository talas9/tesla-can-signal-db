---
layout: default
title: "VCLEFT_seatStatus2 (0x2E2) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Left body controller message: seat status2. Ethernet-side message VCLEFT_seatStatus2 of Left body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 23 signals (VCLEFT_seatStatus2Index, VCLEFT_frontSeatHeatCurrent, VCLEFT_frontSeatHeatDuty, VCLEFT_frontSeatHeatTmp and 19 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_seatStatus2 (0x2E2) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Left body controller message: seat status2. This page documents the 23 signals of VCLEFT_seatStatus2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_seatStatus2` |
| Ethernet-side id | 0x2E2 (738) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 23 |

## Signals of VCLEFT_seatStatus2

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_seatStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_seatStatus2Index` | selector | Left body controller: seat status2 index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SEAT_HEAT_FRONT`<br>1 = `SEAT_HEAT_REARL_BACKREST`<br>2 = `OCCUPANCY`<br>3 = `SEAT_HEAT_REARL`<br>4 = `SEAT_HEAT_REARC`<br>5 = `SEAT_HEAT_REARR_CUSHION`<br>6 = `SEAT_2ROW_ACTUATOR`<br>7 = `SEAT_SWITCH_VOLTAGES_1`<br>8 = `SEAT_SWITCH_VOLTAGES_2`<br>9 = `SEAT_2ROW_EASY_ENTRY`<br>10 = `SEAT_MUX_INDEX_PLACEHOLDER`<br>11 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT`<br>12 = `SEAT_2ROW_ADJUSTABLE_FOLD_FLAT_2` | plausible |
| `VCLEFT_frontSeatHeatCurrent` | page 0 | Left body controller: front seat heat current; raw 12 = signal not available (SNA) | 4\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 | 12 = `SNA` | validated |
| `VCLEFT_frontSeatHeatDuty` | page 0 | Left body controller: front seat heat duty | 16\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCLEFT_frontSeatHeatTmp` | page 0 | Left body controller: front seat heat tmp | 24\|12 | little-endian | signed | 0.05 | 0 | degC | -40 to 80 |  | validated |
| `VCLEFT_frontSeatHeatTmpTarget` | page 0 | Left body controller: front seat heat tmp target | 36\|8 | little-endian | signed | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCLEFT_frontSeatHeatInhibited` | page 0 | Left body controller: front seat heat inhibited | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontSeatHeatPowered` | page 0 | Left body controller: front seat heat powered | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
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

## Multiplexing

`VCLEFT_seatStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 11 (7 signals), page 12 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
