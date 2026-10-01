---
layout: default
title: "VCRIGHT_hvacStatus (0x243) — Right body controller, Tesla Model Y 2025.20.8 ETH"
description: "Right body controller message: hvac status. Ethernet-side message VCRIGHT_hvacStatus of Right body controller for Tesla Model Y firmware 2025.20.8, 61 signals (VCRIGHT_hvacStatusIndex, VCRIGHT_childModeHVACState, VCRIGHT_dogModeState, VCRIGHT_hvacCabinTempEstValid and 57 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_hvacStatus (0x243) — Right body controller, Tesla Model Y 2025.20.8 ETH

Right body controller message: hvac status. This page documents the 61 signals of VCRIGHT_hvacStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_hvacStatus` |
| Ethernet-side id | 0x243 (579) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 61 |

## Signals of VCRIGHT_hvacStatus

Tesla Model Y CAN bus signals in `VCRIGHT_hvacStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_hvacStatusIndex` | selector | Right body controller: hvac status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI`<br>1 = `VCFRONT`<br>2 = `VCFRONT2`<br>3 = `MISC`<br>4 = `MISC2`<br>5 = `MISC3` | plausible |
| `VCRIGHT_childModeHVACState` | page 0 | Right body controller: child mode HVAC state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `ACTIVE_COMPROMISED` | plausible |
| `VCRIGHT_dogModeState` | page 0 | Reports the state of Dog Mode. | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DOG_MODE_UNAVAILABLE_MODEL_DEVICE_FAULT`<br>1 = `DOG_MODE_UNAVAILABLE_CABIN_TOO_HOT`<br>2 = `DOG_MODE_INITIALIZING`<br>3 = `DOG_MODE_AVAILABLE`<br>4 = `DOG_MODE_RUNNING`<br>5 = `DOG_MODE_RUNNING_DEVICE_OR_MODEL_FAULT`<br>6 = `DOG_MODE_RUNNING_TEMP_MONITOR_TRIP`<br>15 = `DOG_MODE_INVALID` | plausible |
| `VCRIGHT_hvacCabinTempEstValid` | page 0 | Right body controller: hvac cabin temp est valid | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_COPNotRunningReasonFiltered` | page 0 | Reports the reason cabin overheat protection is not running for User Interface (UI). | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `DISABLED`<br>2 = `USER_INTERACTION`<br>3 = `ENERGY_CONSUMPTION_LIMIT`<br>4 = `TIMEOUT`<br>5 = `LOW_SOLAR_LOAD`<br>6 = `WAITING`<br>7 = `CABIN_BELOW_THRESHOLD` | plausible |
| `VCRIGHT_hvacCabinTempEst` | page 0 | Estimated temperature of the cabin | 30\|11 | little-endian | unsigned | 0.1 | -40 | degC | -40 to 164 |  | plausible |
| `VCRIGHT_hvacAirDistributionMode` | page 0 | Cabin airflow distribution | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `FLOOR`<br>2 = `PANEL`<br>3 = `PANEL_FLOOR`<br>4 = `DEFROST`<br>5 = `DEFROST_FLOOR`<br>6 = `DEFROST_PANEL`<br>7 = `DEFROST_PANEL_FLOOR` | plausible |
| `VCRIGHT_hvacBlowerSegment` | page 0 | Cabin airflow blower set speed segment | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7`<br>8 = `8`<br>9 = `9`<br>10 = `10`<br>11 = `11` | plausible |
| `VCRIGHT_hvacRecirc` | page 0 | UI airflow recirculation request state | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTO`<br>1 = `RECIRC`<br>2 = `FRESH` | plausible |
| `VCRIGHT_hvacACRunning` | page 0 | Air conditioning is active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `VCRIGHT_hvacPowerState` | page 0 | Commanded HVAC power state from UI | 51\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `ON`<br>2 = `PRECONDITION`<br>3 = `OVERHEAT_PROTECT_FANONLY`<br>4 = `OVERHEAT_PROTECT` | plausible |
| `VCRIGHT_hvacVentStatus` | page 0 | HVAC vent status | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BOTH`<br>1 = `LEFT`<br>2 = `RIGHT`<br>3 = `OFF` | plausible |
| `VCRIGHT_hvacSecondRowState` | page 0 | Right body controller: hvac second row state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTO`<br>1 = `OFF`<br>2 = `LOW`<br>3 = `MED`<br>4 = `HIGH` | plausible |
| `VCRIGHT_hvacSystemNominal` | page 0 | HVAC system state | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacModelInitStatus` | page 0 | Right body controller: hvac model init status | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_INIT_WAIT_FOR_SENSORS`<br>1 = `NOT_INIT_WAIT_FOR_GTW`<br>2 = `INIT_FROM_SENSORS`<br>3 = `INIT_FROM_SENSORS_PREDICTION_ERROR`<br>4 = `INIT_FORWARD_CALC`<br>5 = `INIT_WAITING_FOR_SENSORS`<br>6 = `INIT_FROM_SENSORS_LIMP`<br>7 = `INIT_FROM_SENSORS_PREDICTION_ERROR_LIMP`<br>8 = `INIT_FORWARD_CALC_LIMP`<br>9 = `NOT_INIT_CAMERA_POCKET_BEING_INITIALIZED` | plausible |
| `VCRIGHT_hvacMassflowRefrigSysRight` | page 1 | Right body controller: hvac massflow refrig sys right | 3\|7 | little-endian | unsigned | 1 | 0 | g/s | 0 to 125 |  | plausible |
| `VCRIGHT_hvacRecircDoorPercent` | page 1 | Reports the HVAC air recirculation massflow fraction target. | 10\|6 | little-endian | unsigned | 1.6 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_tempDuctLeft` | page 1 | Fusion of upper and lower left duct temp sensor values for Heat Pump HVAC case, Raw left/right duct temp sensor value for the legacy HVAC case; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacMassflowRefrigSystem` | page 1 | Right body controller: hvac massflow refrig system | 24\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 250 |  | plausible |
| `VCRIGHT_tempDuctRight` | page 1 | Fusion of upper and lower right duct temp sensor values for Heat Pump HVAC case, Raw left/right duct temp sensor value for the legacy HVAC case; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacMassflowRefrigSysLeft` | page 1 | Right body controller: hvac massflow refrig sys left | 40\|7 | little-endian | unsigned | 1 | 0 | g/s | 0 to 125 |  | plausible |
| `VCRIGHT_hvacDuctTargetLeft` | page 1 | Left airflow duct temperature target; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacDuctTargetRight` | page 1 | Right airflow duct temperature target; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_enableTripleCameraFanPowerInSleep` | page 2 | Right body controller: enable triple camera fan power in sleep | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_tempDuctRightUpper` | page 2 | Right body controller: temp duct right upper; raw 255 = signal not available (SNA) | 10\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_hpSplitTempsEnabled` | page 2 | Right body controller: hp split temps enabled | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacEvapInletTempEstimate` | page 2 | Right body controller: hvac evap inlet temp estimate; raw 1023 = signal not available (SNA) | 19\|10 | little-endian | unsigned | 0.13 | -40 | degC | -40 to 90 | 1023 = `SNA` | plausible |
| `VCRIGHT_tempMonitorNotNominal` | page 2 | Right body controller: temp monitor not nominal | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacCabinAtTempTarget` | page 2 | Cabin has reached target temp, send signal to UI | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacReqSecondRow` | page 2 | Right body controller: hvac req second row | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacAirflowReason` | page 2 | Reason for cabin airflow | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | plausible |
| `VCRIGHT_autoHvacBlowerShouldLimit` | page 2 | Cabin airflow blower auto set speed recommendation based on NVH | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_solarLoadOnVehicle` | page 2 | Right body controller: solar load on vehicle; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 4 | 0 | W/m2 | 0 to 1016 | 255 = `SNA` | plausible |
| `VCRIGHT_refrigDistCommanded` | page 2 | The HVAC system has set its settings to run the refrigerant distribution routine | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacFrontRightSeatFanStatus` | page 2 | Right body controller: hvac front right seat fan status | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | plausible |
| `VCRIGHT_hvacFrontLeftSeatFanStatus` | page 2 | Right body controller: hvac front left seat fan status | 51\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | plausible |
| `VCRIGHT_hvacFrontRightSeatHeatStatus` | page 3 | Right body controller: hvac front right seat heat status | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `VCRIGHT_hvacSeatFrontLeftTempTarget` | page 3 | Front left seat heating target temperature | 6\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 0 = `OFF` | plausible |
| `VCRIGHT_hvacManualToAutoNotify` | page 3 | Right body controller: hvac manual to auto notify | 14\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `COMFORT`<br>2 = `FOGGING`<br>3 = `FOGGING_COMFORT`<br>4 = `COMFORT_FORWARD_LOOK`<br>5 = `MISC2`<br>6 = `MISC3` | plausible |
| `VCRIGHT_hvacRequestsFullAuto` | page 3 | Request that the UI go to full auto HVAC mode | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_ALLOWED`<br>1 = `HIGH_BLOWER_SPEED`<br>2 = `MANUAL_HVAC_HIGH_FOGGING_RISK`<br>3 = `HVAC_OFF_FOGGING_RISK`<br>4 = `MISC1`<br>5 = `MISC2`<br>6 = `MISC3`<br>7 = `MISC4` | plausible |
| `VCRIGHT_passengerPresentHvacCycle` | page 3 | Right body controller: passenger present hvac cycle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacRequestsAutoIntake` | page 3 | Request that the UI go to auto intake HVAC mode | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_steeringWheelHeatStatus` | page 3 | Right body controller: steering wheel heat status | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STEERING_WHEEL_HEAT_OFF`<br>1 = `STEERING_WHEEL_HEAT_LEVEL1`<br>2 = `STEERING_WHEEL_HEAT_LEVEL2`<br>3 = `STEERING_WHEEL_HEAT_LEVEL3` | plausible |
| `VCRIGHT_autoDefogStatus` | page 3 | Indicates defog status of auto HVAC, used for providing messaging to the user | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `DEFOG`<br>2 = `INTERMEDIATE_DEFOG` | plausible |
| `VCRIGHT_solarElevation` | page 3 | Right body controller: solar elevation; raw 256 = signal not available (SNA) | 31\|9 | little-endian | signed | 0.5 | 0 | deg | -127.5 to 127.5 | -256 = `SNA` | plausible |
| `VCRIGHT_minsToSunrise` | page 3 | Right body controller: mins to sunrise; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 10 | 0 | min | 0 to 2540 | 255 = `SNA` | plausible |
| `VCRIGHT_minsToSunset` | page 3 | Right body controller: mins to sunset; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 10 | 0 | min | 0 to 2540 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacLimitedReasonRight` | page 3 | Right body controller: hvac limited reason right | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_LIMITING_NONE`<br>1 = `HVAC_LIMITING_HOT_DUCT_LOCKOUT`<br>2 = `HVAC_LIMITING_COLD_DUCT_LOCKOUT`<br>3 = `HVAC_LIMITING_QDOT_LIMITED_COOLING`<br>4 = `HVAC_LIMITING_QDOT_LIMITED_HEATING`<br>5 = `HVAC_LIMITING_HDL_AND_QDLC`<br>6 = `HVAC_LIMITING_CDL_AND_QDLH`<br>7 = `HVAC_LIMITING_MANUAL_BLOWER` | plausible |
| `VCRIGHT_hvacLimitedReasonLeft` | page 3 | Right body controller: hvac limited reason left | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_LIMITING_NONE`<br>1 = `HVAC_LIMITING_HOT_DUCT_LOCKOUT`<br>2 = `HVAC_LIMITING_COLD_DUCT_LOCKOUT`<br>3 = `HVAC_LIMITING_QDOT_LIMITED_COOLING`<br>4 = `HVAC_LIMITING_QDOT_LIMITED_HEATING`<br>5 = `HVAC_LIMITING_HDL_AND_QDLC`<br>6 = `HVAC_LIMITING_CDL_AND_QDLH`<br>7 = `HVAC_LIMITING_MANUAL_BLOWER` | plausible |
| `VCRIGHT_hvacOverheatProtActive` | page 3 | Status of cabin overheat protection | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_tempDuctLeftUpper` | page 4 | Right body controller: temp duct left upper; raw 255 = signal not available (SNA) | 10\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacFrontLeftSeatHeatStatus` | page 4 | Right body controller: hvac front left seat heat status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_REQUEST_OFF`<br>1 = `HEATER_REQUEST_LEVEL1`<br>2 = `HEATER_REQUEST_LEVEL2`<br>3 = `HEATER_REQUEST_LEVEL3` | plausible |
| `VCRIGHT_hvacQdotLeft` | page 4 | Right body controller: hvac qdot left | 20\|14 | little-endian | unsigned | 1 | -8191 | W | -8191 to 8191 |  | plausible |
| `VCRIGHT_hvacQdotRight` | page 4 | Right body controller: hvac qdot right | 34\|14 | little-endian | unsigned | 1 | -8191 | W | -8191 to 8191 |  | plausible |
| `VCRIGHT_tempDuctLeftLower` | page 4 | Right body controller: temp duct left lower; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_tempDuctRightLower` | page 4 | Right body controller: temp duct right lower; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_modeledCabinPressure` | page 5 | Right body controller: modeled cabin pressure | 24\|8 | little-endian | unsigned | 1 | 0 | Pa | 0 to 255 |  | plausible |
| `VCRIGHT_blowerTorqueIndex` | page 5 | Right body controller: blower torque index | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_autoSwingLeftPosX` | page 5 | Right body controller: auto swing left pos x | 39\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_autoSwingRightPositionX` | page 5 | Right body controller: auto swing right position x | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_autoSwingAvailable` | page 5 | Right body controller: auto swing available | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCRIGHT_hvacStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (14 signals), page 1 (8 signals), page 2 (13 signals), page 3 (14 signals), page 4 (6 signals), page 5 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
