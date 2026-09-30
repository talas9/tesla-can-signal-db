---
layout: default
title: "EPAS3P_sysStatus (0x373) — Electric power steering (primary), Tesla Model Y 2025.20.8 ETH"
description: "Electric power steering (primary) message: sys status. Ethernet-side message EPAS3P_sysStatus of Electric power steering (primary) for Tesla Model Y firmware 2025.20.8, 13 signals (EPAS3P_steeringRackForce, EPAS3P_steeringFault, EPAS3P_steeringReduced, EPAS3P_internalSASQF and 9 more). Bit layout, scaling, units and value tables."
---

# EPAS3P_sysStatus (0x373) — Electric power steering (primary), Tesla Model Y 2025.20.8 ETH

Electric power steering (primary) message: sys status. This page documents the 13 signals of EPAS3P_sysStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3P_sysStatus` |
| Ethernet-side id | 0x373 (883) |
| ECU | [Electric power steering (primary)](../../epas3p.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPAS3P |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 13 |

## Signals of EPAS3P_sysStatus

Tesla Model Y CAN bus signals in `EPAS3P_sysStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3P_steeringRackForce` | The real time, estimated force applied by the steering rack to the tie rods; raw 1023 = signal not available (SNA) | 1\|10 | big-endian | unsigned | 50 | -25575 | N | -25575 to 25525 | 1022 = `NOT_IN_SPEC`<br>1023 = `SNA` | plausible |
| `EPAS3P_steeringFault` | Electric power steering (primary): steering fault | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_FAULT`<br>1 = `FAULT` | plausible |
| `EPAS3P_steeringReduced` | Electric power steering (primary): steering reduced | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NORMAL_ASSIST`<br>1 = `REDUCED_ASSIST` | plausible |
| `EPAS3P_internalSASQF` | This signal identifies the validity of the EPAS3P_internalSAS signal. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `EPAS3P_currentTuneMode` | Electric power steering (primary): current tune mode | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STEERING_TUNE_DM_COMFORT`<br>1 = `STEERING_TUNE_DM_STANDARD`<br>2 = `STEERING_TUNE_DM_SPORT`<br>3 = `STEERING_TUNE_RWD_COMFORT`<br>4 = `STEERING_TUNE_RWD_STANDARD`<br>5 = `STEERING_TUNE_RWD_SPORT` | plausible |
| `EPAS3P_torsionBarTorque` | The measurement of the steering wheel torque input. If the value is positive the steering wheel torque is applied in the clockwise direction; raw 4095 = signal not available (SNA) | 19\|12 | big-endian | unsigned | 0.01 | -20.5 | Nm | -20.5 to 20.44 | 4094 = `UNDEFINABLE_DATA`<br>4095 = `SNA` | plausible |
| `EPAS3P_eacErrorCode` | Electric power steering (primary): eac error code; raw 15 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `EAC_ERROR_IDLE`<br>1 = `EAC_ERROR_MIN_SPEED`<br>2 = `EAC_ERROR_MAX_SPEED`<br>3 = `EAC_ERROR_HANDS_ON`<br>4 = `EAC_ERROR_TMP_FAULT`<br>5 = `EAR_ERROR_MAX_STEER_DELTA`<br>6 = `EAC_ERROR_HIGH_ANGLE_REQ`<br>7 = `EAC_ERROR_HIGH_ANGLE_RATE_REQ`<br>8 = `EAC_ERROR_HIGH_ANGLE_SAFETY`<br>9 = `EAC_ERROR_HIGH_ANGLE_RATE_SAFETY`<br>10 = `EAC_ERROR_HIGH_MMOT_SAFETY`<br>11 = `EAC_ERROR_HIGH_TORSION_SAFETY`<br>12 = `EAC_ERROR_LOW_ASSIST`<br>13 = `EAC_ERROR_PINION_VEL_DIFF`<br>14 = `EAC_EXTERNAL_MONITOR_INHIBIT`<br>15 = `SNA` | plausible |
| `EPAS3P_internalSAS` | The measurement of the steering wheel angle that is calculated by electronic power steering assist steering. Clockwise positive. | 37\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819 |  | plausible |
| `EPAS3P_handsOnLevel` | Electric power steering (primary): hands on level | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEVEL_0`<br>1 = `LEVEL_1`<br>2 = `LEVEL_2`<br>3 = `LEVEL_3` | plausible |
| `EPAS3P_sysStatusCounter` | Electric power steering (primary): sys status counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `EPAS3P_tireIDActive` | Electric power steering (primary): tire ID active | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_eacStatus` | Electric power steering (primary): eac status | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EAC_INHIBITED`<br>1 = `EAC_AVAILABLE`<br>2 = `EAC_ACTIVE`<br>3 = `EAC_FAULT`<br>4 = `EAC_LKA_ELK_AVAILABLE`<br>5 = `EAC_LKA_ACTIVE`<br>6 = `EAC_ELK_AVAILABLE`<br>7 = `EAC_ELK_ACTIVE` | plausible |
| `EPAS3P_sysStatusChecksum` | Electric power steering (primary): sys status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric power steering (primary) messages (EPAS3P)](../../epas3p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
