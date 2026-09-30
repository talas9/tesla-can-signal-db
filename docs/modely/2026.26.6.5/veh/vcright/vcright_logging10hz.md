---
layout: default
title: "VCRIGHT_logging10Hz (0x263) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: logging10 hz. Tesla Model Y CAN bus message VCRIGHT_logging10Hz (0x263) of Right body controller, firmware 2026.26.6.5, 47 signals (VCRIGHT_logging10HzIndex, VCRIGHT_hvacLHBleedTarget, VCRIGHT_hvacRHBleedTarget, VCRIGHT_hvacLHVaneTarget and 43 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_logging10Hz (0x263) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Right body controller message: logging10 hz; frame length observed on a vehicle bus. This page documents the 47 signals of VCRIGHT_logging10Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_logging10Hz` |
| CAN id | 0x263 (611) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 47 |

## Signals of VCRIGHT_logging10Hz

Tesla Model Y CAN bus signals in `VCRIGHT_logging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_logging10HzIndex` | selector | Right body controller: logging10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_ACTUATOR_TARGETS`<br>1 = `HVAC_ACTUATOR_POSITIONS`<br>2 = `HVAC_ACTUATOR_STATE`<br>3 = `HVAC_ACTUATOR_BRUSHED`<br>4 = `HVAC_ACTUATOR_BRUSHED_DUTY`<br>5 = `END` | plausible |
| `VCRIGHT_hvacLHBleedTarget` | page 0 | Right body controller: hvac LH bleed target | 3\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRHBleedTarget` | page 0 | Right body controller: hvac RH bleed target | 11\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLHVaneTarget` | page 0 | Right body controller: hvac LH vane target | 19\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRHVaneTarget` | page 0 | Right body controller: hvac RH vane target | 27\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacUpperModeTarget` | page 0 | Right body controller: hvac upper mode target | 35\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLowerModeTarget` | page 0 | Right body controller: hvac lower mode target | 45\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacIntakeTarget` | page 0 | Right body controller: hvac intake target | 53\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLHBleedPosition` | page 1 | Right body controller: hvac LH bleed position | 3\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRHBleedPosition` | page 1 | Right body controller: hvac RH bleed position | 11\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLHVanePosition` | page 1 | Right body controller: hvac LH vane position | 19\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRHVanePosition` | page 1 | Right body controller: hvac RH vane position | 27\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacUpperModePosition` | page 1 | Right body controller: hvac upper mode position | 35\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLowerModePosition` | page 1 | Right body controller: hvac lower mode position | 45\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacIntakePosition` | page 1 | Right body controller: hvac intake position | 53\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacLHBleedActuatorState` | page 2 | Right body controller: hvac LH bleed actuator state | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacRHBleedActuatorState` | page 2 | Right body controller: hvac RH bleed actuator state | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacLHVaneActuatorState` | page 2 | Right body controller: hvac LH vane actuator state | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacRHVaneActuatorState` | page 2 | Right body controller: hvac RH vane actuator state | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacUpperModeActState` | page 2 | Right body controller: hvac upper mode act state | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacLowerModeActState` | page 2 | Right body controller: hvac lower mode act state | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacIntakeActuatorState` | page 2 | Right body controller: hvac intake actuator state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacRearActuatorState` | page 2 | Right body controller: hvac rear actuator state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_EvapPulldownBiasActive` | page 2 | Indicates if an evap pulldown smell mitigation is active | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_tempDatLeftEst` | page 2 | Right body controller: temp dat left est; raw 255 = signal not available (SNA) | 21\|9 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 200 | 255 = `SNA` | validated |
| `VCRIGHT_tempDatRightEst` | page 2 | Right body controller: temp dat right est; raw 255 = signal not available (SNA) | 30\|9 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 200 | 255 = `SNA` | validated |
| `VCRIGHT_tempDuctLeftEst` | page 2 | Right body controller: temp duct left est; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | validated |
| `VCRIGHT_tempDuctRightEst` | page 2 | Right body controller: temp duct right est; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | validated |
| `VCRIGHT_ptcHeaterBadRodDetectionState` | page 2 | Right body controller: ptc heater bad rod detection state | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `IDLE`<br>2 = `DETECTED`<br>3 = `CHECK_LEFT_OUTER`<br>4 = `CHECK_LEFT_CENTER`<br>5 = `CHECK_LEFT_INNER`<br>6 = `CHECK_RIGHT_OUTER`<br>7 = `CHECK_RIGHT_CENTER`<br>8 = `CHECK_RIGHT_INNER`<br>9 = `CLEAR_FAULT`<br>10 = `CLEAR_FAULT_RESTART`<br>11 = `UNAVAILABLE` | validated |
| `VCRIGHT_upperModeDrvActuatorState` | page 2 | Reports the HVAC actuator state | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCRIGHT_leftVerticalActuatorStatus` | page 3 | Right body controller: left vertical actuator status | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCRIGHT_leftLateralActuatorStatus` | page 3 | Right body controller: left lateral actuator status | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCRIGHT_rightVerticalActuatorStatus` | page 3 | Right body controller: right vertical actuator status | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCRIGHT_rightLateralActuatorStatus` | page 3 | Right body controller: right lateral actuator status | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCRIGHT_leftVerticalActuatorState` | page 3 | Reports the HVAC actuator state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCRIGHT_leftLateralActuatorState` | page 3 | Reports the HVAC actuator state | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCRIGHT_rightVerticalActuatorState` | page 3 | Reports the HVAC actuator state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCRIGHT_rightLateralActuatorState` | page 3 | Reports the HVAC actuator state | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCRIGHT_windshieldRHExteriorSurface` | page 3 | Right body controller: windshield RH exterior surface; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 | 255 = `SNA` | validated |
| `VCRIGHT_leftVerticalActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 8\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_leftLateralActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 16\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_rightVerticalActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 24\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_rightLateralActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 30\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_frontLeftSeatTempTargetQuasiSS` | page 4 | Reports the front left seat heating target temperature. | 36\|6 | little-endian | unsigned | 0.75 | 20 | degC | 20 to 60 | 0 = `OFF` | validated |
| `VCRIGHT_frontRightSeatTempTargetQuasiSS` | page 4 | Reports the front right seat heating target temperature. | 42\|6 | little-endian | unsigned | 1 | 20 | degC | 20 to 60 | 0 = `OFF` | validated |
| `VCRIGHT_hvacRearPosition` | page 4 | Right body controller: hvac rear position | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRearTarget` | page 4 | Right body controller: hvac rear target | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |

## Multiplexing

`VCRIGHT_logging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (15 signals), page 3 (9 signals), page 4 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
