---
layout: default
title: "VCSEAT2L_seatStatus2 (0x7C2) — VCSEAT2L ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCSEAT2L ECU message: seat status2. Tesla Model Y CAN bus message VCSEAT2L_seatStatus2 (0x7C2) of VCSEAT2L ECU, firmware 2026.26.6.5, 13 signals (VCSEAT2L_seatStatus2Index, VCSEAT2L_choreography2RState, VCSEAT2L_choreography3RState, VCSEAT2L_choreography1RIsAllowedToMove and 9 more). Bit layout, scaling, units and value tables."
---

# VCSEAT2L_seatStatus2 (0x7C2) — VCSEAT2L ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCSEAT2L ECU message: seat status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of VCSEAT2L_seatStatus2 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEAT2L_seatStatus2` |
| CAN id | 0x7C2 (1986) |
| ECU | [VCSEAT2L ECU](../../vcseat2l.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEAT2L |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 13 |

## Signals of VCSEAT2L_seatStatus2

Tesla Model Y CAN bus signals in `VCSEAT2L_seatStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEAT2L_seatStatus2Index` | selector | VCSEAT2L ECU: seat status2 index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_HEAT_FRONT`<br>1 = `SEAT_VOLTAGES`<br>2 = `OCCUPANCY`<br>3 = `VENTILATION`<br>4 = `CHOREOGRAPHY`<br>5 = `LOADSHED` | plausible |
| `VCSEAT2L_choreography2RState` | page 4 | VCSEAT2L ECU: choreography2 r state | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_CHOREOGRAPHY_ROW_STATE_IDLE`<br>1 = `SEAT_CHOREOGRAPHY_ROW_STATE_FOLDING`<br>2 = `SEAT_CHOREOGRAPHY_ROW_STATE_UNFOLDING` | plausible |
| `VCSEAT2L_choreography3RState` | page 4 | VCSEAT2L ECU: choreography3 r state | 7\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_CHOREOGRAPHY_ROW_STATE_IDLE`<br>1 = `SEAT_CHOREOGRAPHY_ROW_STATE_FOLDING`<br>2 = `SEAT_CHOREOGRAPHY_ROW_STATE_UNFOLDING` | plausible |
| `VCSEAT2L_choreography1RIsAllowedToMove` | page 4 | VCSEAT2L ECU: choreography1 r is allowed to move | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2L_choreography2RIsAllowedToMove` | page 4 | VCSEAT2L ECU: choreography2 r is allowed to move | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2L_choreography1RTrackVelocityType` | page 4 | VCSEAT2L ECU: choreography1 r track velocity type | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOTOR_VELOCITY_TYPE_STOP`<br>1 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_FORWARD`<br>2 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_BACKWARD`<br>3 = `SEAT_MOTOR_VELOCITY_TYPE_MID_FORWARD`<br>4 = `SEAT_MOTOR_VELOCITY_TYPE_MID_BACKWARD`<br>5 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_FORWARD`<br>6 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_BACKWARD` | plausible |
| `VCSEAT2L_choreography1RBackrestVelocityType` | page 4 | VCSEAT2L ECU: choreography1 r backrest velocity type | 15\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOTOR_VELOCITY_TYPE_STOP`<br>1 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_FORWARD`<br>2 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_BACKWARD`<br>3 = `SEAT_MOTOR_VELOCITY_TYPE_MID_FORWARD`<br>4 = `SEAT_MOTOR_VELOCITY_TYPE_MID_BACKWARD`<br>5 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_FORWARD`<br>6 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_BACKWARD` | plausible |
| `VCSEAT2L_choreography2RTrackVelocityType` | page 4 | VCSEAT2L ECU: choreography2 r track velocity type | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOTOR_VELOCITY_TYPE_STOP`<br>1 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_FORWARD`<br>2 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_BACKWARD`<br>3 = `SEAT_MOTOR_VELOCITY_TYPE_MID_FORWARD`<br>4 = `SEAT_MOTOR_VELOCITY_TYPE_MID_BACKWARD`<br>5 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_FORWARD`<br>6 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_BACKWARD` | plausible |
| `VCSEAT2L_choreography2RBackrestVelocityType` | page 4 | VCSEAT2L ECU: choreography2 r backrest velocity type | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOTOR_VELOCITY_TYPE_STOP`<br>1 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_FORWARD`<br>2 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_BACKWARD`<br>3 = `SEAT_MOTOR_VELOCITY_TYPE_MID_FORWARD`<br>4 = `SEAT_MOTOR_VELOCITY_TYPE_MID_BACKWARD`<br>5 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_FORWARD`<br>6 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_BACKWARD` | plausible |
| `VCSEAT2L_choreography3RBackrestVelocityType` | page 4 | VCSEAT2L ECU: choreography3 r backrest velocity type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOTOR_VELOCITY_TYPE_STOP`<br>1 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_FORWARD`<br>2 = `SEAT_MOTOR_VELOCITY_TYPE_LOW_BACKWARD`<br>3 = `SEAT_MOTOR_VELOCITY_TYPE_MID_FORWARD`<br>4 = `SEAT_MOTOR_VELOCITY_TYPE_MID_BACKWARD`<br>5 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_FORWARD`<br>6 = `SEAT_MOTOR_VELOCITY_TYPE_HIGH_BACKWARD` | plausible |
| `VCSEAT2L_choreographyState` | page 4 | VCSEAT2L ECU: choreography state | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SEAT_CHOREO_STATE_INVALID`<br>1 = `SEAT_CHOREO_STATE_1R_STOP_2R_FAST_OUT_OF_KEEPOUT_ZONE`<br>2 = `SEAT_CHOREO_STATE_1R_CLEAR_2R_FAST_OUT_OF_KEEPOUT_ZONE`<br>3 = `SEAT_CHOREO_STATE_1R_CLEAR_2R_MID_OUT_OF_KEEPOUT_ZONE`<br>4 = `SEAT_CHOREO_STATE_1R_CLEAR_2R_STOP_OUT_OF_KEEPOUT_ZONE`<br>5 = `SEAT_CHOREO_STATE_2R_STOP_3R_FAST`<br>6 = `SEAT_CHOREO_STATE_1R_STOP_2R_FAST_OUT_OF_KEEPOUT_ZONE_3R_FAST`<br>7 = `SEAT_CHOREO_STATE_1R_STOP_2R_FAST_OUT_OF_KEEPOUT_ZONE_3R_MID`<br>8 = `SEAT_CHOREO_STATE_1R_CLEAR_2R_FAST_OUT_OF_KEEPOUT_ZONE_3R_MID`<br>9 = `SEAT_CHOREO_STATE_1R_CLEAR_2R_MID_OUT_OF_KEEPOUT_ZONE_3R_MID`<br>10 = `SEAT_CHOREO_STATE_1R_RESTORE` | plausible |
| `VCSEAT2L_choreographyCollisionPair` | page 4 | VCSEAT2L ECU: choreography collision pair | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_CHOREOGRAPHY_COLLISION_PAIR_NONE`<br>1 = `SEAT_CHOREOGRAPHY_COLLISION_PAIR_1R_BACKREST_2R_CUSHION`<br>2 = `SEAT_CHOREOGRAPHY_COLLISION_PAIR_1R_BACKREST_2R_BACKREST`<br>3 = `SEAT_CHOREOGRAPHY_COLLISION_PAIR_2R_CUSHION_3R_BACKREST`<br>4 = `SEAT_CHOREOGRAPHY_COLLISION_PAIR_2R_BACKREST_3R_BACKREST` | plausible |
| `VCSEAT2L_2rMovingForChoreography` | page 4 | VCSEAT2L ECU: 2r moving for choreography | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCSEAT2L_seatStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 4 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCSEAT2L ECU messages (VCSEAT2L)](../../vcseat2l.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
