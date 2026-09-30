---
layout: default
title: "DAS_bodyControls (0x3E9) — Driver assistance computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Driver assistance computer message: body controls. Tesla Model Y CAN bus message DAS_bodyControls (0x3E9) of Driver assistance computer, firmware 2026.26.6.5, 27 signals (DAS_headlightRequest, DAS_hazardLightRequest, DAS_wiperSpeed, DAS_turnIndicatorRequest and 23 more). Bit layout, scaling, units and value tables."
---

# DAS_bodyControls (0x3E9) — Driver assistance computer, Tesla Model Y 2026.26.6.5 VEH CAN

Driver assistance computer message: body controls; frame length from the layout, not yet observed on a vehicle bus. This page documents the 27 signals of DAS_bodyControls as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_bodyControls` |
| CAN id | 0x3E9 (1001) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 27 |

## Signals of DAS_bodyControls

Tesla Model Y CAN bus signals in `DAS_bodyControls`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_headlightRequest` | The DAS request to the body controls ecu to turn on headlights. | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DAS_HEADLIGHT_REQUEST_OFF`<br>1 = `DAS_HEADLIGHT_REQUEST_ON`<br>2 = `DAS_HEADLIGHT_REQUEST_TAIL_LIGHTS_ONLY`<br>3 = `DAS_HEADLIGHT_REQUEST_INVALID` | validated |
| `DAS_hazardLightRequest` | The command from DAS to body controls to turn on the hazard lights; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DAS_REQUEST_HAZARDS_OFF`<br>1 = `DAS_REQUEST_HAZARDS_ON`<br>2 = `DAS_REQUEST_HAZARDS_ON_FAST`<br>3 = `DAS_REQUEST_HAZARDS_SNA` | validated |
| `DAS_wiperSpeed` | The auto wiper algorithm speed request to the body controller. | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DAS_WIPER_SPEED_OFF`<br>1 = `DAS_WIPER_SPEED_1`<br>2 = `DAS_WIPER_SPEED_2`<br>3 = `DAS_WIPER_SPEED_3`<br>4 = `DAS_WIPER_SPEED_4`<br>5 = `DAS_WIPER_SPEED_5`<br>6 = `DAS_WIPER_SPEED_6`<br>7 = `DAS_WIPER_SPEED_7`<br>8 = `DAS_WIPER_SPEED_8`<br>9 = `DAS_WIPER_SPEED_9`<br>10 = `DAS_WIPER_SPEED_10`<br>11 = `DAS_WIPER_SPEED_11`<br>12 = `DAS_WIPER_SPEED_12`<br>13 = `DAS_WIPER_SPEED_13`<br>14 = `DAS_WIPER_SPEED_14`<br>15 = `DAS_WIPER_SPEED_INVALID` | validated |
| `DAS_turnIndicatorRequest` | Reports Driver Assistance System (DAS) request to body controls to turn on/off the left or right turn indicator. | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DAS_TURN_INDICATOR_NONE`<br>1 = `DAS_TURN_INDICATOR_LEFT`<br>2 = `DAS_TURN_INDICATOR_RIGHT`<br>3 = `DAS_TURN_INDICATOR_CANCEL`<br>4 = `DAS_TURN_INDICATOR_DEFER` | validated |
| `DAS_highLowBeamDecision` | The output of the automatic high beam algorithm, to turn the highbeams on or off; raw 3 = signal not available (SNA) | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DAS_HIGH_BEAM_UNDECIDED`<br>1 = `DAS_HIGH_BEAM_OFF`<br>2 = `DAS_HIGH_BEAM_ON`<br>3 = `DAS_HIGH_BEAM_SNA` | validated |
| `DAS_heaterRequest` | The DAS request to the body controller to turn on the front glass heater in front of the triple camera; raw 0 = signal not available (SNA) | 13\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `DAS_HEATER_SNA`<br>1 = `DAS_HEATER_OFF`<br>2 = `DAS_HEATER_ON` | validated |
| `DAS_highLowBeamOffReason` | The reason why automatic high beams are surpressed; raw 5 = signal not available (SNA) | 15\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HIGH_BEAM_ON`<br>1 = `HIGH_BEAM_OFF_REASON_MOVING_VISION_TARGET`<br>2 = `HIGH_BEAM_OFF_REASON_MOVING_RADAR_TARGET`<br>3 = `HIGH_BEAM_OFF_REASON_AMBIENT_LIGHT`<br>4 = `HIGH_BEAM_OFF_REASON_HEAD_LIGHT`<br>5 = `HIGH_BEAM_OFF_REASON_SNA` | validated |
| `DAS_forwardCamHeaterDutyCycle` | Supplies the requested duty cycle of the front windshield camera heater | 18\|4 | little-endian | unsigned | 0.06666667 | 0 | - | 0 to 1 |  | validated |
| `DAS_dynamicBrakeLightRequest` | Indicates if the dynamic brake light alogirthm is requesting pulsing brake lights. | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_radarHeaterRequest` | Reports the request from Driver Assistance System (DAS) to body controls to turn on heater to clear out fascia in front of the radar. | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_ahlbOverride` | Indicates if body controller should override UI switch and stalk state to allow auto high beam functionality | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_mirrorFoldRequest` | DAS request to fold or present mirrors; raw 3 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DAS_MIRROR_REQUEST_NONE`<br>1 = `DAS_MIRROR_REQUEST_FOLD`<br>2 = `DAS_MIRROR_REQUEST_UNFOLD`<br>3 = `DAS_MIRROR_REQUEST_SNA` | validated |
| `DAS_wiperWashRequest` | Autowiper requests that the windshield be washed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_ulcConfirmationRequestActive` | Driver assistance computer: ulc confirmation request active | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_overrideWiperSetting` | Autopilot wants to override the user's wiper setting to enable auto-wiper | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_autoWiperState` | DAS auto wiper internal state; raw 5 = signal not available (SNA) | 30\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DAS_AUTO_WIPER_STATE_OFF`<br>1 = `DAS_AUTO_WIPER_STATE_SLOW_INTERMITTENT`<br>2 = `DAS_AUTO_WIPER_STATE_FAST_INTERMITTENT`<br>3 = `DAS_AUTO_WIPER_STATE_SLOW_CONTINUOUS`<br>4 = `DAS_AUTO_WIPER_STATE_FAST_CONTINUOUS`<br>5 = `DAS_AUTO_WIPER_STATE_SNA` | validated |
| `DAS_turnIndicatorRequestReason` | Reports the reason that Driver Assistance System (DAS) is requesting a change to the turn indicator state from body controls. | 33\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `DAS_NONE`<br>1 = `DAS_ACTIVE_NAV_LANE_CHANGE`<br>2 = `DAS_ACTIVE_SPEED_LANE_CHANGE`<br>3 = `DAS_ACTIVE_FORK`<br>4 = `DAS_CANCEL_LANE_CHANGE`<br>5 = `DAS_CANCEL_FORK`<br>6 = `DAS_ACTIVE_MERGE`<br>7 = `DAS_CANCEL_MERGE`<br>8 = `DAS_ACTIVE_COMMANDED_LANE_CHANGE`<br>9 = `DAS_ACTIVE_INTERSECTION`<br>10 = `DAS_CANCEL_INTERSECTION`<br>11 = `DAS_ACTIVE_SUMMMON`<br>12 = `DAS_CANCEL_SUMMMON`<br>13 = `DAS_ACTIVE_AUTO_PARK`<br>14 = `DAS_CANCEL_AUTO_PARK`<br>15 = `DAS_CANCEL_MANUAL_BLINKER`<br>17 = `DAS_ACTIVE_STATIC_OBJECT_LANE_CHANGE`<br>18 = `DAS_ACTIVE_INCORRECT_ROAD_SIDE_LANE_CHANGE`<br>19 = `DAS_ACTIVE_EXIT_PASSING_LANE_LANE_CHANGE`<br>20 = `DAS_ACTIVE_EXIT_RIGHT_LANE_LANE_CHANGE`<br>21 = `DAS_ACTIVE_AWAY_FROM_MERGE_LANE_CHANGE`<br>22 = `DAS_ACTIVE_STAY_OUT_OF_RIGHTMOST_LANE_LANE_CHANGE`<br>23 = `DAS_ACTIVE_INFEASIBLE_KINEMATICS_LANE_CHANGE`<br>24 = `DAS_ACTIVE_SIMULTANEOUS_LANE_CHANGE_AVOIDANCE` | validated |
| `DAS_forwardRadarPowerRequest` | Driver assistance computer: forward radar power request | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_driverDomeLightRequest` | DAS requests that driver side dome light be illuminated | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_drivePowerStateRequest` | Reports DAS request for vehicle power state Drive. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_enableIcrDataCollection` | Driver assistance computer: enable icr data collection | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_rPillarCamHeaterDutyCycle` | Supplies the requested duty cycle of the right pillar camera heater | 45\|4 | little-endian | unsigned | 0.06666667 | 0 | - | 0 to 1 |  | validated |
| `DAS_adaptiveHighBeamIsFaulted` | Indicates malfunctioning or unavailable input to the Adaptive High Beam system. | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_restrictDoorReleaseLeft` | Reports requests to inhibit left doors from being released. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RESTRICT_DOOR_RELEASE_INACTIVE`<br>1 = `RESTRICT_DOOR_RELEASE_ACTIVE` | validated |
| `DAS_restrictDoorReleaseRight` | Reports requests to inhibit right doors from being released. | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RESTRICT_DOOR_RELEASE_INACTIVE`<br>1 = `RESTRICT_DOOR_RELEASE_ACTIVE` | validated |
| `DAS_bodyControlsCounter` | Driver assistance computer: body controls counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DAS_bodyControlsChecksum` | Driver assistance computer: body controls checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
