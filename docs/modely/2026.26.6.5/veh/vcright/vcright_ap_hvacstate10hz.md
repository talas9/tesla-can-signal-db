---
layout: default
title: "VCRIGHT_AP_hvacState10Hz (0x45A) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: AP hvac state10 hz. Tesla Model Y CAN bus message VCRIGHT_AP_hvacState10Hz (0x45A) of Right body controller, firmware 2026.26.6.5, 23 signals (VCRIGHT_AP_hvacState10HzIndex, VCRIGHT_AP_autoDefogAvailable, VCRIGHT_AP_hvacFlashFoggingDetected, VCRIGHT_AP_hvacModelInitStatus and 19 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_AP_hvacState10Hz (0x45A) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Right body controller message: AP hvac state10 hz; frame length observed on a vehicle bus. This page documents the 23 signals of VCRIGHT_AP_hvacState10Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_AP_hvacState10Hz` |
| CAN id | 0x45A (1114) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 23 |

## Signals of VCRIGHT_AP_hvacState10Hz

Tesla Model Y CAN bus signals in `VCRIGHT_AP_hvacState10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_AP_hvacState10HzIndex` | selector | Right body controller: AP hvac state10 hz index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MUX_0`<br>1 = `MUX_1`<br>2 = `END` | validated |
| `VCRIGHT_AP_autoDefogAvailable` | page 0 | Right body controller: AP auto defog available | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_AP_hvacFlashFoggingDetected` | page 0 | Right body controller: AP hvac flash fogging detected | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_AP_hvacModelInitStatus` | page 0 | Right body controller: AP hvac model init status | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_INIT_WAIT_FOR_SENSORS`<br>1 = `NOT_INIT_WAIT_FOR_GTW`<br>2 = `INIT_FROM_SENSORS`<br>3 = `INIT_FROM_SENSORS_PREDICTION_ERROR`<br>4 = `INIT_FORWARD_CALC`<br>5 = `INIT_WAITING_FOR_SENSORS` | validated |
| `VCRIGHT_AP_cabinTempWindshield` | page 0 | Right body controller: AP cabin temp windshield; raw 255 = signal not available (SNA) | 7\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_AP_cabinTempSideGlassRight` | page 0 | Right body controller: AP cabin temp side glass right; raw 255 = signal not available (SNA) | 15\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_AP_cabinTempSideGlassLeft` | page 0 | Right body controller: AP cabin temp side glass left; raw 255 = signal not available (SNA) | 23\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_AP_hvacRecircDoorPercent` | page 0 | Right body controller: AP hvac recirc door percent | 31\|6 | little-endian | unsigned | 1.6 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_AP_hvacAirDistributionMode` | page 0 | Right body controller: AP hvac air distribution mode | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `FLOOR`<br>2 = `PANEL`<br>3 = `PANEL_FLOOR`<br>4 = `DEFROST`<br>5 = `DEFROST_FLOOR`<br>6 = `DEFROST_PANEL`<br>7 = `DEFROST_PANEL_FLOOR` | validated |
| `VCRIGHT_AP_hvacEstimateWindshieldRH` | page 0 | Right body controller: AP hvac estimate windshield RH | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 |  | validated |
| `VCRIGHT_AP_hvacMassflowTarget` | page 0 | Right body controller: AP hvac massflow target | 48\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 200 |  | validated |
| `VCRIGHT_AP_tempDuctDefrost` | page 0 | Right body controller: AP temp duct defrost; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | validated |
| `VCRIGHT_AP_cameraTurnOnTime` | page 1 | Reports the time duration requested to run the Autopilot (AP) cameras for defogging purposes; raw 511 = signal not available (SNA) | 2\|9 | little-endian | unsigned | 5 | 0 | min | 0 to 2540 | 511 = `SNA` | validated |
| `VCRIGHT_AP_cameraDefogType` | page 1 | Right body controller: AP camera defog type | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `CAMERA`<br>2 = `CMD`<br>3 = `GLARESHIELD_HEATER_PLUS_FAN`<br>4 = `TWO_CAMERA_PLUS_FAN` | validated |
| `VCRIGHT_ah_hvacFaultSurvivabilityTime` | page 1 | Right body controller: ah hvac fault survivability time; raw 31 = signal not available (SNA) | 14\|5 | little-endian | unsigned | 10 | 0 | sec | 0 to 300 | 31 = `SNA` | validated |
| `VCRIGHT_ah_defoggingTimeNeeded` | page 1 | Right body controller: ah defogging time needed; raw 31 = signal not available (SNA) | 19\|5 | little-endian | unsigned | 1 | 0 | min | 0 to 30 | 31 = `SNA` | validated |
| `VCRIGHT_AP_cameraFanDutyRequest` | page 1 | Right body controller: AP camera fan duty request; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | validated |
| `VCRIGHT_ah_defogSystemState` | page 1 | Right body controller: ah defog system state; raw 7 = signal not available (SNA) | 31\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `DEFOG_SYS_INIT`<br>1 = `DEFOG_SYS_EVALUATING_HARDWARE`<br>2 = `DEFOG_SYS_EVALUATING_PRECONDITIONING`<br>3 = `DEFOG_SYS_HEALTHY_REEVALUATING`<br>4 = `DEFOG_SYS_HEALTHY`<br>5 = `DEFOG_SYS_HEALTHY_DEGRADED`<br>6 = `DEFOG_SYS_UNHEALTHY`<br>7 = `DEFOG_SYS_SNA` | validated |
| `VCRIGHT_AP_turnForwardCameraHeaterOnReason` | page 1 | Right body controller: AP turn forward camera heater on reason | 34\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TURN_ON_REASON_NONE`<br>1 = `TURN_ON_REASON_EVAP_JUST_TURNED_OFF`<br>2 = `TURN_ON_REASON_EVAP_UNAVAILABLE`<br>3 = `TURN_ON_REASON_RADIATOR_STEAMING`<br>4 = `TURN_ON_REASON_START_OF_COLD_DRIVE`<br>5 = `TURN_ON_REASON_COMPRESSOR_OFF`<br>6 = `TURN_ON_REASON_FLASH_FOGGING`<br>7 = `TURN_ON_REASON_EXTERNAL_DEW_LIKELY`<br>8 = `TURN_ON_REASON_LOSS_OF_DEHUMIDIFICATION`<br>9 = `TURN_ON_REASON_ROBOTAXI_PRECONDITIONING`<br>10 = `TURN_ON_REASON_GLARESHIELD_PRECONDITIONING`<br>11 = `TURN_ON_REASON_WET_EVAP_STARTUP`<br>12 = `TURN_ON_REASON_HVAC_SYSTEM_NOT_NOMINAL`<br>13 = `TURN_ON_REASON_MANUAL_HVAC_CONTROL`<br>14 = `TURN_ON_REASON_MANUAL_DEFOG_DEFROST`<br>15 = `TURN_ON_REASON_MANUAL_FOGGING_HAMMER` | validated |
| `VCRIGHT_AP_turnCameraFanOffReason` | page 1 | Reports the reason for requesting the triple camera fan to turn off. | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TURN_OFF_REASON_NONE`<br>1 = `TURN_OFF_REASON_EVAP_JUST_TURNED_OFF`<br>2 = `TURN_OFF_REASON_RADIATOR_STEAMING`<br>3 = `TURN_OFF_REASON_START_OF_COLD_DRIVE`<br>4 = `TURN_OFF_REASON_VOC_CONCENTRATION_HIGH`<br>5 = `TURN_OFF_REASON_FLASH_FOGGING`<br>6 = `TURN_OFF_REASON_EVAP_CONTROLS_COMPROMISED`<br>7 = `TURN_OFF_REASON_CABIN_HUMIDITY` | validated |
| `VCRIGHT_AP_forwardCameraIntegratedHeaterRequest` | page 1 | Request to run forward camera heating. | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_AP_solarFluxOnRightWindow` | page 1 | Right body controller: AP solar flux on right window; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1150 | 255 = `SNA` | validated |
| `VCRIGHT_AP_solarFluxOnLeftWindow` | page 1 | Right body controller: AP solar flux on left window; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1150 | 255 = `SNA` | validated |

## Multiplexing

`VCRIGHT_AP_hvacState10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (11 signals), page 1 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
