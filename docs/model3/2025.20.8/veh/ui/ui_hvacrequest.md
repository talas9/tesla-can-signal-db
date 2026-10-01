---
layout: default
title: "UI_hvacRequest (0x2F3) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: hvac request. Tesla Model 3 CAN bus message UI_hvacRequest (0x2F3) of Touchscreen user interface computer, firmware 2025.20.8, 26 signals (UI_hvacReqTempSetpointLeft, UI_hvacReqAutoBlowerLevel, UI_hvacReqTempSetpointRight, UI_hvacReqAirDistributionMode and 22 more). Bit layout, scaling, units and value tables."
---

# UI_hvacRequest (0x2F3) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN

Touchscreen user interface computer message: hvac request; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 26 signals of UI_hvacRequest as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_hvacRequest` |
| CAN id | 0x2F3 (755) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 26 |

## Signals of UI_hvacRequest

Tesla Model 3 CAN bus signals in `UI_hvacRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_hvacReqTempSetpointLeft` | HVAC left set temperature. | 0\|5 | little-endian | unsigned | 0.5 | 15 | degC | 15 to 28 | 0 = `LO`<br>26 = `HI` | plausible |
| `UI_hvacReqAutoBlowerLevel` | Reports the auto Heating, Ventilation, and Air Conditioning (HVAC) speed aggressiveness setting. | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VERY_LOW`<br>1 = `LOW`<br>2 = `MEDIUM`<br>3 = `HIGH`<br>4 = `VERY_HIGH` | plausible |
| `UI_hvacReqTempSetpointRight` | HVAC right set temperature. | 8\|5 | little-endian | unsigned | 0.5 | 15 | degC | 15 to 28 | 0 = `LO`<br>26 = `HI` | plausible |
| `UI_hvacReqAirDistributionMode` | Request for air distribution mode. | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTO`<br>1 = `MANUAL_FLOOR`<br>2 = `MANUAL_PANEL`<br>3 = `MANUAL_PANEL_FLOOR`<br>4 = `MANUAL_DEFROST`<br>5 = `MANUAL_DEFROST_FLOOR`<br>6 = `MANUAL_DEFROST_PANEL`<br>7 = `MANUAL_DEFROST_PANEL_FLOOR` | plausible |
| `UI_hvacReqBlowerSegment` | HVAC manual blower request (GUI_hvacManualBlowerRequest) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7`<br>8 = `8`<br>9 = `9`<br>10 = `10`<br>11 = `AUTO` | plausible |
| `UI_hvacReqRecirc` | HVAC recirculation mode | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTO`<br>1 = `RECIRC`<br>2 = `FRESH` | plausible |
| `UI_hvacReqACDisable` | Request to disable AC. | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTO`<br>1 = `OFF`<br>2 = `ON` | plausible |
| `UI_hvacDefogState` | HVAC defog state. | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `DEFOG`<br>2 = `DEFROST`<br>3 = `AUTO_DEFOG` | plausible |
| `UI_hvacReqUserPowerState` | Reports HVAC power state. | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `ON`<br>2 = `PRECONDITION`<br>3 = `OVERHEAT_PROTECT_FANONLY`<br>4 = `OVERHEAT_PROTECT` | plausible |
| `UI_hvacReqSecondRowState` | HVAC rear fan request speed. | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTO`<br>1 = `OFF`<br>2 = `LOW`<br>3 = `MED`<br>4 = `HIGH` | plausible |
| `UI_hvacUseModeledDuctTemp` | Touchscreen user interface computer: hvac use modeled duct temp | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hvacReqKeepClimateOn` | Request accessory power | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `KEEP_CLIMATE_ON_REQ_OFF`<br>1 = `KEEP_CLIMATE_ON_REQ_ON`<br>2 = `KEEP_CLIMATE_ON_REQ_DOG`<br>3 = `KEEP_CLIMATE_ON_REQ_PARTY` | plausible |
| `UI_hvacReqBioWeaponDefMode` | Request for BioWeapon Defense Mode | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hvacLatchPassengerPresent` | Touchscreen user interface computer: hvac latch passenger present | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacControlsFeatures1` | Touchscreen user interface computer: enable hvac controls features1 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacNotifications` | Touchscreen user interface computer: enable hvac notifications | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hvacPhoneCallAirFlowAdjustEnabled` | Touchscreen user interface computer: hvac phone call air flow adjust enabled | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacVOCPurgeRoutine` | Touchscreen user interface computer: enable hvac VOC purge routine | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCustomerTHSAlerts` | Touchscreen user interface computer: enable customer THS alerts | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_evapDryingSelectiveEnable` | Touchscreen user interface computer: evap drying selective enable | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacWeatherDataBasedHumidityControls` | Touchscreen user interface computer: enable hvac weather data based humidity controls | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hvacReqTempSetpointCOP` | HVAC cabin overheat protection set temperature. | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LOW`<br>1 = `MEDIUM`<br>2 = `HIGH` | plausible |
| `UI_hvacClimateNudgeStatus` | Touchscreen user interface computer: hvac climate nudge status | 58\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CLOSED_NO_NUDGE`<br>1 = `CLOSED_WITH_NUDGE`<br>2 = `OPEN_NO_NUDGE`<br>3 = `OPEN_WITH_NUDGE`<br>4 = `CLOSED_WITH_EXTERIOR_NUDGE` | plausible |
| `UI_enableHvacControlsFeatures2` | Touchscreen user interface computer: enable hvac controls features2 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacAPFoggingMonitor` | Touchscreen user interface computer: enable hvac AP fogging monitor | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableHvacLimpMode` | Touchscreen user interface computer: enable hvac limp mode | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
