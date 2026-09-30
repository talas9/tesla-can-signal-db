---
layout: default
title: "EPAS3S_sysStatus (0x370) — Electric power steering (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Electric power steering (secondary) message: sys status. Tesla Model 3 / Model Y CAN bus message EPAS3S_sysStatus (0x370) of Electric power steering (secondary), firmware 2026.26.6.5, 13 signals (EPAS3S_steeringRackForce, EPAS3S_steeringFault, EPAS3S_steeringReduced, EPAS3S_internalSASQF and 9 more). Bit layout, scaling, units and value tables."
---

# EPAS3S_sysStatus (0x370) — Electric power steering (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Electric power steering (secondary) message: sys status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of EPAS3S_sysStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3S_sysStatus` |
| CAN id | 0x370 (880) |
| ECU | [Electric power steering (secondary)](../../epas3s.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | EPAS3S |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 13 |

## Signals of EPAS3S_sysStatus

Tesla Model 3 / Model Y CAN bus signals in `EPAS3S_sysStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3S_steeringRackForce` | The real time, estimated force applied by the steering rack to the tie rods; raw 1023 = signal not available (SNA) | 1\|10 | big-endian | unsigned | 50 | -25575 | N | -25575 to 25525 | 1022 = `NOT_IN_SPEC`<br>1023 = `SNA` | plausible |
| `EPAS3S_steeringFault` | Electric power steering (secondary): steering fault | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_FAULT`<br>1 = `FAULT` | plausible |
| `EPAS3S_steeringReduced` | Electric power steering (secondary): steering reduced | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NORMAL_ASSIST`<br>1 = `REDUCED_ASSIST` | plausible |
| `EPAS3S_internalSASQF` | This signal identifies the validity of the EPAS3P_internalSAS signal. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `EPAS3S_currentTuneMode` | Electric power steering (secondary): current tune mode | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STEERING_TUNE_DM_COMFORT`<br>1 = `STEERING_TUNE_DM_STANDARD`<br>2 = `STEERING_TUNE_DM_SPORT`<br>3 = `STEERING_TUNE_RWD_COMFORT`<br>4 = `STEERING_TUNE_RWD_STANDARD`<br>5 = `STEERING_TUNE_RWD_SPORT` | plausible |
| `EPAS3S_torsionBarTorque` | The measurement of the steering wheel torque input. If the value is positive the steering wheel torque is applied in the clockwise direction; raw 4095 = signal not available (SNA) | 19\|12 | big-endian | unsigned | 0.01 | -20.5 | Nm | -20.5 to 20.44 | 4094 = `UNDEFINABLE_DATA`<br>4095 = `SNA` | plausible |
| `EPAS3S_eacErrorCode` | Electric power steering (secondary): eac error code; raw 15 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `EAC_ERROR_IDLE`<br>1 = `EAC_ERROR_MIN_SPEED`<br>2 = `EAC_ERROR_MAX_SPEED`<br>3 = `EAC_ERROR_HANDS_ON`<br>4 = `EAC_ERROR_TMP_FAULT`<br>5 = `EAR_ERROR_MAX_STEER_DELTA`<br>6 = `EAC_ERROR_HIGH_ANGLE_REQ`<br>7 = `EAC_ERROR_HIGH_ANGLE_RATE_REQ`<br>8 = `EAC_ERROR_HIGH_ANGLE_SAFETY`<br>9 = `EAC_ERROR_HIGH_ANGLE_RATE_SAFETY`<br>10 = `EAC_ERROR_HIGH_MMOT_SAFETY`<br>11 = `EAC_ERROR_HIGH_TORSION_SAFETY`<br>12 = `EAC_ERROR_LOW_ASSIST`<br>13 = `EAC_ERROR_PINION_VEL_DIFF`<br>14 = `EAC_EXTERNAL_MONITOR_INHIBIT`<br>15 = `SNA` | plausible |
| `EPAS3S_internalSAS` | The measurement of the steering wheel angle that is calculated by electronic power steering assist steering. Clockwise positive. | 37\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819 |  | plausible |
| `EPAS3S_handsOnLevel` | Electric power steering (secondary): hands on level | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEVEL_0`<br>1 = `LEVEL_1`<br>2 = `LEVEL_2`<br>3 = `LEVEL_3` | plausible |
| `EPAS3S_sysStatusCounter` | Electric power steering (secondary): sys status counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `EPAS3S_driverlessState` | Electric power steering (secondary): driverless state | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EAC_DRIVERLESS_INACTIVE`<br>1 = `EAC_DRIVERLESS_ACTIVE` | plausible |
| `EPAS3S_eacStatus` | Electric power steering (secondary): eac status | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EAC_INHIBITED`<br>1 = `EAC_AVAILABLE`<br>2 = `EAC_ACTIVE`<br>3 = `EAC_FAULT`<br>4 = `EAC_LKA_ELK_AVAILABLE`<br>5 = `EAC_LKA_ACTIVE`<br>6 = `EAC_ELK_AVAILABLE`<br>7 = `EAC_ELK_ACTIVE` | plausible |
| `EPAS3S_sysStatusChecksum` | Electric power steering (secondary): sys status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Electric power steering (secondary) messages (EPAS3S)](../../epas3s.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
