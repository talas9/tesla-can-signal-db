---
layout: default
title: "VCLEFT_hvacBlowerFeedback (0x282) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: hvac blower feedback. Tesla Model 3 / Model Y CAN bus message VCLEFT_hvacBlowerFeedback (0x282) of Left body controller, firmware 2025.20.8, 13 signals (VCLEFT_hvacBlowerFeedbackIndex, VCLEFT_hvacBlowerEnabled, VCLEFT_hvacBlowerOutputDuty, VCLEFT_hvacBlowerRPMTarget and 9 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_hvacBlowerFeedback (0x282) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Left body controller message: hvac blower feedback; frame length observed on a vehicle bus. This page documents the 13 signals of VCLEFT_hvacBlowerFeedback as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_hvacBlowerFeedback` |
| CAN id | 0x282 (642) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 13 |

## Signals of VCLEFT_hvacBlowerFeedback

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_hvacBlowerFeedback`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_hvacBlowerFeedbackIndex` | selector | Left body controller: hvac blower feedback index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVAC_FEEDBACK_SIGNALS`<br>1 = `END` | plausible |
| `VCLEFT_hvacBlowerEnabled` | page 0 | Left body controller: hvac blower enabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_hvacBlowerOutputDuty` | page 0 | Left body controller: hvac blower output duty; raw 127 = signal not available (SNA) | 3\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | plausible |
| `VCLEFT_hvacBlowerRPMTarget` | page 0 | Left body controller: hvac blower RPM target; raw 1023 = signal not available (SNA) | 10\|10 | little-endian | unsigned | 10 | 0 | rpm | 0 to 10000 | 1023 = `SNA` | plausible |
| `VCLEFT_hvacBlowerRPMActual` | page 0 | Blower speed feedback | 20\|10 | little-endian | unsigned | 10 | 0 | rpm | 0 to 10000 |  | plausible |
| `VCLEFT_hvacBlowerTorque` | page 0 | Left body controller: hvac blower torque; raw 1023 = signal not available (SNA) | 34\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | plausible |
| `VCLEFT_hvacBlowerFETTemp` | page 0 | Left body controller: hvac blower FET temp; raw 127 = signal not available (SNA) | 44\|7 | little-endian | unsigned | 2 | -50 | degC | -50 to 180 | 127 = `SNA` | plausible |
| `VCLEFT_hvacBlowerIDc` | page 0 | Left body controller: hvac blower i dc; raw 127 = signal not available (SNA) | 51\|7 | little-endian | unsigned | 0.5 | 0 | A | 0 to 63 | 127 = `SNA` | plausible |
| `VCLEFT_hvacBlowerInitd` | page 0 | Left body controller: hvac blower initd | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_hvacBlowerFault` | page 0 | Left body controller: hvac blower fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_hvacBlowerLimitFETTemps` | page 0 | Left body controller: hvac blower limit FET temps | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_hvacBlowerPowerOn` | page 0 | Left body controller: hvac blower power on | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_hvacBlowerMotorID` | page 0 | Reports the ID of the HVAC blower motor | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_MOTOR_ID_UNKNOWN`<br>1 = `VC_MOTOR_ID_DELTA`<br>2 = `VC_MOTOR_ID_BOSCH` | plausible |

## Multiplexing

`VCLEFT_hvacBlowerFeedbackIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
