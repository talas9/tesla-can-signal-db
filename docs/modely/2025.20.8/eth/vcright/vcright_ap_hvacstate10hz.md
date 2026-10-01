---
layout: default
title: "VCRIGHT_AP_hvacState10Hz (0x45A) — Right body controller, Tesla Model Y 2025.20.8 ETH"
description: "Right body controller message: AP hvac state10 hz. Ethernet-side message VCRIGHT_AP_hvacState10Hz of Right body controller for Tesla Model Y firmware 2025.20.8, 17 signals (VCRIGHT_AP_hvacState10HzIndex, VCRIGHT_AP_autoDefogAvailable, VCRIGHT_AP_hvacFlashFoggingDetected, VCRIGHT_AP_hvacModelInitStatus and 13 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_AP_hvacState10Hz (0x45A) — Right body controller, Tesla Model Y 2025.20.8 ETH

Right body controller message: AP hvac state10 hz. This page documents the 17 signals of VCRIGHT_AP_hvacState10Hz as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_AP_hvacState10Hz` |
| Ethernet-side id | 0x45A (1114) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 17 |

## Signals of VCRIGHT_AP_hvacState10Hz

Tesla Model Y CAN bus signals in `VCRIGHT_AP_hvacState10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_AP_hvacState10HzIndex` | selector | Right body controller: AP hvac state10 hz index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MUX_0`<br>1 = `MUX_1`<br>2 = `END` | plausible |
| `VCRIGHT_AP_autoDefogAvailable` | page 0 | Right body controller: AP auto defog available | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_AP_hvacFlashFoggingDetected` | page 0 | Right body controller: AP hvac flash fogging detected | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_AP_hvacModelInitStatus` | page 0 | Right body controller: AP hvac model init status | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_INIT_WAIT_FOR_SENSORS`<br>1 = `NOT_INIT_WAIT_FOR_GTW`<br>2 = `INIT_FROM_SENSORS`<br>3 = `INIT_FROM_SENSORS_PREDICTION_ERROR`<br>4 = `INIT_FORWARD_CALC`<br>5 = `INIT_WAITING_FOR_SENSORS` | plausible |
| `VCRIGHT_AP_cabinTempWindshield` | page 0 | Right body controller: AP cabin temp windshield; raw 255 = signal not available (SNA) | 7\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_cabinTempSideGlassRight` | page 0 | Right body controller: AP cabin temp side glass right; raw 255 = signal not available (SNA) | 15\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_cabinTempSideGlassLeft` | page 0 | Right body controller: AP cabin temp side glass left; raw 255 = signal not available (SNA) | 23\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_hvacRecircDoorPercent` | page 0 | Right body controller: AP hvac recirc door percent | 31\|6 | little-endian | unsigned | 1.6 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_AP_hvacAirDistributionMode` | page 0 | Right body controller: AP hvac air distribution mode | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `FLOOR`<br>2 = `PANEL`<br>3 = `PANEL_FLOOR`<br>4 = `DEFROST`<br>5 = `DEFROST_FLOOR`<br>6 = `DEFROST_PANEL`<br>7 = `DEFROST_PANEL_FLOOR` | plausible |
| `VCRIGHT_AP_hvacEstimateWindshieldRH` | page 0 | Right body controller: AP hvac estimate windshield RH | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 |  | plausible |
| `VCRIGHT_AP_hvacMassflowTarget` | page 0 | Right body controller: AP hvac massflow target | 48\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 200 |  | plausible |
| `VCRIGHT_AP_tempDuctDefrost` | page 0 | Right body controller: AP temp duct defrost; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_cameraFanDutyRequest` | page 1 | Right body controller: AP camera fan duty request; raw 127 = signal not available (SNA) | 30\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | plausible |
| `VCRIGHT_AP_turnCameraFanOffReason` | page 1 | Reports the reason for requesting the triple camera fan to turn off. | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TURN_OFF_REASON_NONE`<br>1 = `TURN_OFF_REASON_EVAP_JUST_TURNED_OFF`<br>2 = `TURN_OFF_REASON_RADIATOR_STEAMING`<br>3 = `TURN_OFF_REASON_START_OF_COLD_DRIVE`<br>4 = `TURN_OFF_REASON_VOC_CONCENTRATION_HIGH`<br>5 = `TURN_OFF_REASON_FLASH_FOGGING`<br>6 = `TURN_OFF_REASON_EVAP_CONTROLS_COMPROMISED`<br>7 = `TURN_OFF_REASON_CABIN_HUMIDITY` | plausible |
| `VCRIGHT_AP_cameraTurnOnTime` | page 1 | Reports the time duration requested to run the Autopilot (AP) cameras for defogging purposes; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 10 | 0 | min | 0 to 2540 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_solarFluxOnRightWindow` | page 1 | Right body controller: AP solar flux on right window; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1150 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_solarFluxOnLeftWindow` | page 1 | Right body controller: AP solar flux on left window; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1150 | 255 = `SNA` | plausible |

## Multiplexing

`VCRIGHT_AP_hvacState10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (11 signals), page 1 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
