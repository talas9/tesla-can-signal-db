---
layout: default
title: "VCSEAT2L_seatStatus (0x2FC) — VCSEAT2L ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCSEAT2L ECU message: seat status. Tesla Model Y CAN bus message VCSEAT2L_seatStatus (0x2FC) of VCSEAT2L ECU, firmware 2026.26.6.5, 15 signals (VCSEAT2L_row2SeatStatusIndex, VCSEAT2L_seatTrackPosReal, VCSEAT2L_seatTrackPosOffset, VCSEAT2L_seatReclineState and 11 more). Bit layout, scaling, units and value tables."
---

# VCSEAT2L_seatStatus (0x2FC) — VCSEAT2L ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCSEAT2L ECU message: seat status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of VCSEAT2L_seatStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEAT2L_seatStatus` |
| CAN id | 0x2FC (764) |
| ECU | [VCSEAT2L ECU](../../vcseat2l.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEAT2L |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 15 |

## Signals of VCSEAT2L_seatStatus

Tesla Model Y CAN bus signals in `VCSEAT2L_seatStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEAT2L_row2SeatStatusIndex` | selector | VCSEAT2L ECU: row2 seat status index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK`<br>1 = `POSITION`<br>2 = `ADJUSTABLE_FOLD_FLAT`<br>3 = `ARMREST` | plausible |
| `VCSEAT2L_seatTrackPosReal` | page 1 | Reports real position of seat track | 4\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCSEAT2L_seatTrackPosOffset` | page 1 | VCSEAT2L ECU: seat track pos offset | 16\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCSEAT2L_seatReclineState` | page 1 | Reports the active state of the 2nd row seat recliner; raw 15 = signal not available (SNA) | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_STOPPED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_COMFORT`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_COMFORT`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_FORWARD_FAST`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_ADJUSTING_REARWARD_FAST`<br>5 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_FOLDING`<br>6 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_UNFOLDING`<br>7 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_FORWARD_TO_POSITION`<br>8 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_MOVING_REARWARD_TO_POSITION`<br>9 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ZERO_POSITION`<br>12 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SEAT_ADJUSTABLE_FOLD_FLAT_STATE_SNA` | validated |
| `VCSEAT2L_seatReclineCalibrated` | page 1 | Reports calibration status of the 2nd row seat recliner | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEAT2L_seatReclinePositionState` | page 1 | Reports the active position state of the 2nd row seat recliner; raw 4 = signal not available (SNA) | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_FOLDED`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNFOLDED`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNSAFE_INTERMEDIATE`<br>3 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_UNKNOWN`<br>4 = `SEAT_ADJUSTABLE_FOLD_FLAT_POSITION_STATE_SNA` | validated |
| `VCSEAT2L_seatReclineAbsPosSwitchTransPoint` | page 1 | VCSEAT2L ECU: seat recline abs pos switch trans point | 36\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCSEAT2L_seatReclineAbsPosSwitchState` | page 1 | Reports the status of 2nd row seat recline absolute position (comfort zone) switch; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | validated |
| `VCSEAT2L_seatReclineFoldAllowed` | page 1 | VCSEAT2L ECU: seat recline fold allowed | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEAT2L_seatReclineUnfoldAllowed` | page 1 | VCSEAT2L ECU: seat recline unfold allowed | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEAT2L_seatReclineAdjustmentAllowed` | page 1 | VCSEAT2L ECU: seat recline adjustment allowed | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEAT2L_seat1RClashAvoidanceBlockedReason` | page 1 | VCSEAT2L ECU: seat1 r clash avoidance blocked reason | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_NONE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_VEHICLE_IN_MOTION`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_UNCALIBRATED`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_REAR_SEAT_UNCALIBRATED`<br>4 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_PROFILE_RECALL`<br>5 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_MOVING`<br>6 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_REASON_FRONT_SEAT_OCCUPANCY` | validated |
| `VCSEAT2L_seat1RClashAvoidanceState` | page 1 | VCSEAT2L ECU: seat1 r clash avoidance state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_IDLE`<br>1 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_FRONT_SEAT_CLEARING`<br>2 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_WAITING_TO_RESTORE_FRONT_SEAT`<br>3 = `SEAT_FOLD_FLAT_CLASH_AVOIDANCE_STATE_RESTORING_FRONT_SEAT` | validated |
| `VCSEAT2L_seatReclineChoreoBlockedByOccupancy` | page 1 | VCSEAT2L ECU: seat recline choreo blocked by occupancy | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEAT2L_seatReclineNextToggleDirection` | page 1 | VCSEAT2L ECU: seat recline next toggle direction; raw 2 = signal not available (SNA) | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_FOLD`<br>1 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_UNFOLD`<br>2 = `SEAT_ADJUSTABLE_FOLD_FLAT_NEXT_TOGGLE_DIRECTION_SNA` | validated |

## Multiplexing

`VCSEAT2L_row2SeatStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (14 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCSEAT2L ECU messages (VCSEAT2L)](../../vcseat2l.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
