---
layout: default
title: "VCRIGHT_logging10Hz (0x263) — Right body controller, Tesla Model 3 2025.20.8 ETH"
description: "Right body controller message: logging10 hz. Ethernet-side message VCRIGHT_logging10Hz of Right body controller for Tesla Model 3 firmware 2025.20.8, 34 signals (VCRIGHT_logging10HzIndex, VCRIGHT_hvacLHBleedTarget, VCRIGHT_hvacRHBleedTarget, VCRIGHT_hvacLHVaneTarget and 30 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_logging10Hz (0x263) — Right body controller, Tesla Model 3 2025.20.8 ETH

Right body controller message: logging10 hz. This page documents the 34 signals of VCRIGHT_logging10Hz as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_logging10Hz` |
| Ethernet-side id | 0x263 (611) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 34 |

## Signals of VCRIGHT_logging10Hz

Tesla Model 3 CAN bus signals in `VCRIGHT_logging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_logging10HzIndex` | selector | Right body controller: logging10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_ACTUATOR_TARGETS`<br>1 = `HVAC_ACTUATOR_POSITIONS`<br>2 = `HVAC_ACTUATOR_STATE`<br>3 = `HVAC_ACTUATOR_BRUSHED`<br>4 = `HVAC_ACTUATOR_BRUSHED_DUTY`<br>5 = `END` | plausible |
| `VCRIGHT_hvacLHBleedTarget` | page 0 | Right body controller: hvac LH bleed target | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacRHBleedTarget` | page 0 | Right body controller: hvac RH bleed target | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLHVaneTarget` | page 0 | Right body controller: hvac LH vane target | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacRHVaneTarget` | page 0 | Right body controller: hvac RH vane target | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacUpperModeTarget` | page 0 | Right body controller: hvac upper mode target | 40\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLowerModeTarget` | page 0 | Right body controller: hvac lower mode target | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacIntakeTarget` | page 0 | Right body controller: hvac intake target | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLHBleedPosition` | page 1 | Right body controller: hvac LH bleed position | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacRHBleedPosition` | page 1 | Right body controller: hvac RH bleed position | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLHVanePosition` | page 1 | Right body controller: hvac LH vane position | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacRHVanePosition` | page 1 | Right body controller: hvac RH vane position | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacUpperModePosition` | page 1 | Right body controller: hvac upper mode position | 40\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLowerModePosition` | page 1 | Right body controller: hvac lower mode position | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacIntakePosition` | page 1 | Right body controller: hvac intake position | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_hvacLHBleedActuatorState` | page 2 | Right body controller: hvac LH bleed actuator state | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacRHBleedActuatorState` | page 2 | Right body controller: hvac RH bleed actuator state | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacLHVaneActuatorState` | page 2 | Right body controller: hvac LH vane actuator state | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacRHVaneActuatorState` | page 2 | Right body controller: hvac RH vane actuator state | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacUpperModeActState` | page 2 | Right body controller: hvac upper mode act state | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacLowerModeActState` | page 2 | Right body controller: hvac lower mode act state | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_hvacIntakeActuatorState` | page 2 | Right body controller: hvac intake actuator state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVACACTUATOR_STATE_BRAKING`<br>1 = `HVACACTUATOR_STATE_RUNNING`<br>2 = `HVACACTUATOR_STATE_COASTING` | validated |
| `VCRIGHT_EvapPulldownBiasActive` | page 2 | Indicates if an evap pulldown smell mitigation is active | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_tempDatLeftEst` | page 2 | Right body controller: temp dat left est; raw 255 = signal not available (SNA) | 21\|9 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 200 | 255 = `SNA` | validated |
| `VCRIGHT_tempDatRightEst` | page 2 | Right body controller: temp dat right est; raw 255 = signal not available (SNA) | 30\|9 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 200 | 255 = `SNA` | validated |
| `VCRIGHT_tempDuctLeftEst` | page 2 | Right body controller: temp duct left est; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | validated |
| `VCRIGHT_tempDuctRightEst` | page 2 | Right body controller: temp duct right est; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -22 | degC | -22 to 105 | 255 = `SNA` | validated |
| `VCRIGHT_ptcHeaterBadRodDetectionState` | page 2 | Right body controller: ptc heater bad rod detection state | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `IDLE`<br>2 = `DETECTED`<br>3 = `CHECK_LEFT_OUTER`<br>4 = `CHECK_LEFT_CENTER`<br>5 = `CHECK_LEFT_INNER`<br>6 = `CHECK_RIGHT_OUTER`<br>7 = `CHECK_RIGHT_CENTER`<br>8 = `CHECK_RIGHT_INNER`<br>9 = `CLEAR_FAULT`<br>10 = `CLEAR_FAULT_RESTART`<br>11 = `UNAVAILABLE` | validated |
| `VCRIGHT_leftVerticalActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 8\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_leftLateralActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 16\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_rightVerticalActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 24\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_rightLateralActuatorDuty` | page 4 | Reports the HVAC motor duty cycle | 30\|6 | little-endian | signed | 4 | 0 | % | -100 to 100 |  | validated |
| `VCRIGHT_frontLeftSeatTempTargetQuasiSS` | page 4 | Reports the front left seat heating target temperature. | 36\|6 | little-endian | unsigned | 0.75 | 20 | degC | 20 to 60 | 0 = `OFF` | validated |
| `VCRIGHT_frontRightSeatTempTargetQuasiSS` | page 4 | Reports the front right seat heating target temperature. | 42\|6 | little-endian | unsigned | 1 | 20 | degC | 20 to 60 | 0 = `OFF` | validated |

## Multiplexing

`VCRIGHT_logging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (13 signals), page 4 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
