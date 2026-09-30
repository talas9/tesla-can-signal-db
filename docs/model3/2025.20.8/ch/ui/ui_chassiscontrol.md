---
layout: default
title: "UI_chassisControl (0x293) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: chassis control. Tesla Model 3 CAN bus message UI_chassisControl (0x293) of Touchscreen user interface computer, firmware 2025.20.8, 28 signals (UI_steeringTuneRequest, UI_tractionControlMode, UI_parkBrakeRequest, UI_narrowGarages and 24 more). Bit layout, scaling, units and value tables."
---

# UI_chassisControl (0x293) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN

Touchscreen user interface computer message: chassis control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 28 signals of UI_chassisControl as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_chassisControl` |
| CAN id | 0x293 (659) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 28 |

## Signals of UI_chassisControl

Tesla Model 3 CAN bus signals in `UI_chassisControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_steeringTuneRequest` | UI customer level request for steering feel. MS had comfort, normal, sport. M3 intent is Normal, sport see SW-95934 | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STEERING_TUNE_COMFORT`<br>1 = `STEERING_TUNE_STANDARD`<br>2 = `STEERING_TUNE_SPORT` | validated |
| `UI_tractionControlMode` | Transport user selected traction control modes | 2\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TC_NORMAL_SELECTED`<br>1 = `TC_SLIP_START_SELECTED`<br>2 = `TC_DEV_MODE_1_SELECTED`<br>3 = `TC_DEV_MODE_2_SELECTED`<br>4 = `TC_ROLLS_MODE_SELECTED`<br>5 = `TC_DYNO_MODE_SELECTED`<br>6 = `TC_OFFROAD_ASSIST_SELECTED`<br>7 = `TC_SLIPPERY_SURFACE_SELECTED` | validated |
| `UI_parkBrakeRequest` | User selection for Park brake; raw 3 = signal not available (SNA) | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `PARK_BRAKE_REQUEST_IDLE`<br>1 = `PARK_BRAKE_REQUEST_PRESSED`<br>3 = `PARK_BRAKE_REQUEST_SNA` | validated |
| `UI_narrowGarages` | Touchscreen user interface computer: narrow garages | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_winchModeRequest` | Winch mode (towing) request | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINCH_MODE_IDLE`<br>1 = `WINCH_MODE_ENTER`<br>2 = `WINCH_MODE_EXIT`<br>3 = `WINCH_MODE_DIALOGUE_OPEN` | validated |
| `UI_zeroSpeedConfirmed` | Touchscreen user interface computer: zero speed confirmed; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CANCELED`<br>1 = `CONFIRMED`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `UI_trailerMode` | Indicates whether trailer mode is selected. To be used when towing a trailer. | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TRAILER_MODE_OFF`<br>1 = `TRAILER_MODE_ON` | validated |
| `UI_distanceUnits` | Touchscreen user interface computer: distance units | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `KM`<br>1 = `MILES` | plausible |
| `UI_dasDebugEnable` | Touchscreen user interface computer: das debug enable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_accOvertakeEnable` | Enable ACC Overtake assistance (reduce follow distance when the turn signal is on), UI firmware only sets datavalue to True; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `ACC_OVERTAKE_OFF`<br>1 = `ACC_OVERTAKE_ON`<br>3 = `SNA` | validated |
| `UI_aebEnable` | Enable Autonomous Emergency Brakes; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AEB_OFF`<br>1 = `AEB_ON`<br>3 = `SNA` | validated |
| `UI_aesEnable` | Enable Automatic Emergency Steering (associated datavalue set to true and never changed by UI firmware); raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AES_OFF`<br>1 = `AES_ON`<br>3 = `SNA` | validated |
| `UI_ahlbEnable` | Enable Automatic High/Low Beams; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AHLB_OFF`<br>1 = `AHLB_ON`<br>3 = `SNA` | validated |
| `UI_autoLaneChangeEnable` | Enable Automatic Lane Change; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OFF`<br>1 = `ON`<br>3 = `SNA` | validated |
| `UI_winchProxUserOverride` | User feedback from tow mode panel confirming that charge cable is disconnected when vehicle is unable to determine cable status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rebootAutopilot` | Touchscreen user interface computer: reboot autopilot | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autoParkRequest` | Request Automatic Parking; raw 15 = signal not available (SNA) | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `NONE`<br>1 = `PARK_LEFT_PARALLEL`<br>2 = `PARK_LEFT_CROSS`<br>3 = `PARK_RIGHT_PARALLEL`<br>4 = `PARK_RIGHT_CROSS`<br>5 = `PARALLEL_PULL_OUT_TO_LEFT`<br>6 = `PARALLEL_PULL_OUT_TO_RIGHT`<br>7 = `ABORT`<br>8 = `COMPLETE`<br>9 = `SEARCH`<br>10 = `PAUSE`<br>11 = `RESUME`<br>12 = `BEGIN_PARKING`<br>15 = `SNA` | validated |
| `UI_bsdEnable` | Enable Blind Spot Detection (datavalue defaults to true and not changed by UI firmware); raw 3 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `BSD_OFF`<br>1 = `BSD_ON`<br>3 = `SNA` | validated |
| `UI_fcwEnable` | Enable Forward Collision Warning; raw 3 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FCW_OFF`<br>1 = `FCW_ON`<br>3 = `SNA` | validated |
| `UI_fcwSensitivity` | Forward Collision Warning Level; raw 3 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AEB_SENSITIVITY_EARLY`<br>1 = `AEB_SENSITIVITY_AVERAGE`<br>2 = `AEB_SENSITIVITY_LATE`<br>3 = `SNA` | validated |
| `UI_latControlEnable` | Enable Lateral Control (lane centering, lane keeping, lane changing); raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LATERAL_CONTROL_OFF`<br>1 = `LATERAL_CONTROL_ON`<br>2 = `LATERAL_CONTROL_UNAVAILABLE`<br>3 = `LATERAL_CONTROL_SNA` | validated |
| `UI_ldwEnable` | Enable Lane Departure Warning; raw 3 = signal not available (SNA) | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_HAPTIC`<br>1 = `LDW_TRIGGERS_HAPTIC`<br>3 = `SNA` | validated |
| `UI_pedalSafetyEnable` | Touchscreen user interface computer: pedal safety enable; raw 3 = signal not available (SNA) | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `PEDAL_SAFETY_OFF`<br>1 = `PEDAL_SAFETY_ON`<br>3 = `SNA` | plausible |
| `UI_pedalMap_epas` | Touchscreen user interface computer: pedal map epas | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHILL`<br>1 = `SPORT`<br>2 = `PERFORMANCE` | plausible |
| `UI_redLightStopSignEnable` | Touchscreen user interface computer: red light stop sign enable; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RLSSW_OFF`<br>1 = `RLSSW_ON`<br>3 = `SNA` | plausible |
| `UI_selfParkTune` | Touchscreen user interface computer: self park tune; raw 15 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 15 = `SNA` | plausible |
| `UI_chassisControlCounter` | Touchscreen user interface computer: chassis control counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_chassisControlChecksum` | Touchscreen user interface computer: chassis control checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
