---
layout: default
title: "UI_vehicleControl (0x273) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: vehicle control. Tesla Model 3 / Model Y CAN bus message UI_vehicleControl (0x273) of Touchscreen user interface computer, firmware 2025.20.8, 39 signals (UI_powerStateRequest, UI_childDoorLockOnRight, UI_frontFogSwitch, UI_summonActive and 35 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleControl (0x273) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: vehicle control; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 39 signals of UI_vehicleControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleControl` |
| CAN id | 0x273 (627) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 39 |

## Signals of UI_vehicleControl

Tesla Model 3 / Model Y CAN bus signals in `UI_vehicleControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_powerStateRequest` | Request accessory power | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACCESSORY`<br>2 = `ACCESSORY_PLUS`<br>3 = `DRIVE_SUMMON` | plausible |
| `UI_childDoorLockOnRight` | UI child door lock request status. | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontFogSwitch` | Request for front fog lights to be on | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_summonActive` | Summon is active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frunkRequest` | Request open frunk | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_wiperMode` | Wiper mode state; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WIPER_MODE_SNA`<br>1 = `WIPER_MODE_SERVICE`<br>2 = `WIPER_MODE_NORMAL`<br>3 = `WIPER_MODE_PARK` | plausible |
| `UI_steeringBacklightEnabled` | Touchscreen user interface computer: steering backlight enabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `UI_steeringButtonMode` | Steering wheel control mode | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STEERING_BUTTON_MODE_OFF`<br>1 = `STEERING_BUTTON_MODE_STEERING_COLUMN_ADJ`<br>2 = `STEERING_BUTTON_MODE_MIRROR_LEFT`<br>3 = `STEERING_BUTTON_MODE_MIRROR_RIGHT`<br>4 = `STEERING_BUTTON_MODE_HEADLIGHT_LEFT`<br>5 = `STEERING_BUTTON_MODE_HEADLIGHT_RIGHT`<br>6 = `STEERING_BUTTON_MODE_WIPERS`<br>7 = `STEERING_BUTTON_MODE_SEATS` | plausible |
| `UI_walkUpUnlock` | Walk up unlock request (datavalue defaults to false) | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_walkAwayLock` | Walk away door lock setting. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_unlockOnPark` | Unlock on park setting | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_globalUnlockOn` | Global Unlock Setting | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_childDoorLockOnLeft` | UI child door lock request status. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_lockRequest` | Lock or unlock request; raw 7 = signal not available (SNA) | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `UI_LOCK_REQUEST_IDLE`<br>1 = `UI_LOCK_REQUEST_LOCK`<br>2 = `UI_LOCK_REQUEST_UNLOCK`<br>3 = `UI_LOCK_REQUEST_REMOTE_UNLOCK`<br>4 = `UI_LOCK_REQUEST_REMOTE_LOCK`<br>7 = `UI_LOCK_REQUEST_SNA` | plausible |
| `UI_alarmEnabled` | UI customer level request to enable alarm. | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_intrusionSensorOn` | Touchscreen user interface computer: intrusion sensor on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_stop12vSupport` | UI request to stop rails as 12v support | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rearFogSwitch` | Request for rear fog lights to be on | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_mirrorFoldRequest` | Fold the mirrors; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `MIRROR_FOLD_REQUEST_IDLE`<br>1 = `MIRROR_FOLD_REQUEST_RETRACT`<br>2 = `MIRROR_FOLD_REQUEST_PRESENT`<br>3 = `MIRROR_FOLD_REQUEST_SNA` | plausible |
| `UI_mirrorHeatRequest` | Customer usage of mirror heater and rear defrost | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_remoteStartRequest` | remote start or self park request; raw 4 = signal not available (SNA) | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI_REMOTE_START_REQUEST_IDLE`<br>1 = `UI_REMOTE_START_REQUEST_START`<br>4 = `UI_REMOTE_START_REQUEST_SNA` | plausible |
| `UI_seeYouHomeLightingOn` | Headlights after exit | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_powerOff` | power off rails request. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_displayBrightnessLevel` | UI brightness; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127 | 255 = `SNA` | plausible |
| `UI_ambientLightingEnabled` | Touchscreen user interface computer: ambient lighting enabled | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autoHighBeamEnabled` | Enable Automatic High/Low Beams | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatHeatReq` | Request for front left seat heat | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `UI_frontRightSeatHeatReq` | Request for front left seat heat | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `UI_rearLeftSeatHeatReq` | UI request for second row left seat heater | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `UI_rearCenterSeatHeatReq` | UI request for second row middle seat heater | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `UI_rearRightSeatHeatReq` | UI request for second row right seat heater | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `UI_autoFoldMirrorsOn` | Enable Automatic Mirror Fold/Unfold | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_mirrorDipOnReverse` | Enable Mirror Dip On Reverse | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_remoteClosureRequest` | remote actuate trunk; raw 3 = signal not available (SNA) | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `UI_REMOTE_CLOSURE_REQUEST_IDLE`<br>1 = `UI_REMOTE_CLOSURE_REQUEST_REAR_TRUNK_MOVE`<br>2 = `UI_REMOTE_CLOSURE_REQUEST_FRONT_TRUNK_MOVE`<br>3 = `UI_REMOTE_CLOSURE_REQUEST_SNA` | plausible |
| `UI_wiperRequest` | Wiper speed; raw 0 = signal not available (SNA) | 56\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `WIPER_REQUEST_SNA`<br>1 = `WIPER_REQUEST_OFF`<br>2 = `WIPER_REQUEST_AUTO`<br>3 = `WIPER_REQUEST_SLOW_INTERMITTENT`<br>4 = `WIPER_REQUEST_FAST_INTERMITTENT`<br>5 = `WIPER_REQUEST_SLOW_CONTINUOUS`<br>6 = `WIPER_REQUEST_FAST_CONTINUOUS` | plausible |
| `UI_domeLightSwitch` | Dome light switch | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DOME_LIGHT_SWITCH_OFF`<br>1 = `DOME_LIGHT_SWITCH_ON`<br>2 = `DOME_LIGHT_SWITCH_AUTO` | plausible |
| `UI_honkHorn` | Touchscreen user interface computer: honk horn | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_driveStateRequest` | Touchscreen user interface computer: drive state request | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `IDLE`<br>1 = `START` | plausible |
| `UI_rearWindowLockout` | Touchscreen user interface computer: rear window lockout | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
