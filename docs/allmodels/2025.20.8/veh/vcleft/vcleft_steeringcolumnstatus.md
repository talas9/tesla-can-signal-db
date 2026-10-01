---
layout: default
title: "VCLEFT_steeringColumnStatus (0x262) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: steering column status. Tesla Model 3 / Model Y CAN bus message VCLEFT_steeringColumnStatus (0x262) of Left body controller, firmware 2025.20.8, 12 signals (VCLEFT_steeringColumnSMState, VCLEFT_steeringColumnLastRequest, VCLEFT_steeringColumnUpDownDuty, VCLEFT_steeringColumnInOutDuty and 8 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_steeringColumnStatus (0x262) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Left body controller message: steering column status; frame length observed on a vehicle bus. This page documents the 12 signals of VCLEFT_steeringColumnStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_steeringColumnStatus` |
| CAN id | 0x262 (610) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 12 |

## Signals of VCLEFT_steeringColumnStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_steeringColumnStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_steeringColumnSMState` | Status of steering column state machine; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `STEERING_COLUMN_STATE_SNA`<br>1 = `STEERING_COLUMN_STATE_RECALL`<br>2 = `STEERING_COLUMN_STATE_CALIBRATE`<br>3 = `STEERING_COLUMN_STATE_MANUAL_CONTROL` | plausible |
| `VCLEFT_steeringColumnLastRequest` | Left body controller: steering column last request; raw 0 = signal not available (SNA) | 3\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `STEERING_COLUMN_REQUEST_SNA`<br>1 = `STEERING_COLUMN_REQUEST_NONE`<br>2 = `STEERING_COLUMN_REQUEST_UP`<br>3 = `STEERING_COLUMN_REQUEST_DOWN`<br>4 = `STEERING_COLUMN_REQUEST_IN`<br>5 = `STEERING_COLUMN_REQUEST_OUT` | plausible |
| `VCLEFT_steeringColumnUpDownDuty` | Steering column tilt motor duty cycle | 6\|5 | little-endian | signed | 7 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_steeringColumnInOutDuty` | Steering column telescope motor duty cycle | 11\|5 | little-endian | signed | 7 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_steeringColumnUpDownPos` | Motor encoder value representing steering column tilt position | 16\|8 | little-endian | signed | 1 | 103 | mm | -25 to 230 |  | plausible |
| `VCLEFT_steeringColumnInOutPos` | Motor encoder value representing steering column telescope position | 24\|8 | little-endian | signed | 1 | 103 | mm | -25 to 230 |  | plausible |
| `VCLEFT_steeringColumnUpDownAmps` | Measures current used by the steering column tilt motor. | 32\|6 | little-endian | signed | 0.63 | 0 | A | -20 to 19.53 |  | plausible |
| `VCLEFT_steeringColumnInOutAmps` | Measures current used by the steering column telescope motor. | 38\|6 | little-endian | signed | 0.63 | 0 | A | -20 to 19.53 |  | plausible |
| `VCLEFT_steeringColumnUpDownCalib` | Left body controller: steering column up down calib | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_steeringColumnInOutCalib` | Left body controller: steering column in out calib | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_steeringColumnUpDownTC` | Left body controller: steering column up down TC | 46\|8 | little-endian | unsigned | 0.5 | -10 | s | -10 to 117.5 |  | plausible |
| `VCLEFT_steeringColumnInOutTC` | Left body controller: steering column in out TC | 54\|8 | little-endian | unsigned | 0.5 | -10 | s | -10 to 117.5 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
