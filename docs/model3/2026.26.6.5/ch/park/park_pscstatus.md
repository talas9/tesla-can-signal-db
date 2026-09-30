---
layout: default
title: "PARK_pscStatus (0x21E) — Parking assist sensors, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: psc status. Tesla Model 3 CAN bus message PARK_pscStatus (0x21E) of Parking assist sensors, firmware 2026.26.6.5, 15 signals (PARK_pscParkStatus, PARK_pscParkAbortReason, PARK_pscParallelSpace, PARK_pscCrossSpace and 11 more). Bit layout, scaling, units and value tables."
---

# PARK_pscStatus (0x21E) — Parking assist sensors, Tesla Model 3 2026.26.6.5 CH CAN

Parking assist sensors message: psc status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of PARK_pscStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pscStatus` |
| CAN id | 0x21E (542) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 40 ms |
| Signals | 15 |

## Signals of PARK_pscStatus

Tesla Model 3 CAN bus signals in `PARK_pscStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_pscParkStatus` | Parking assist sensors: psc park status; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_AVAILABLE`<br>1 = `SEARCHING`<br>2 = `GUIDANCE_LEFT`<br>3 = `GUIDANCE_RIGHT`<br>4 = `PRE_GUIDANCE`<br>5 = `GUIDANCE_FINISHED`<br>6 = `FAULT`<br>7 = `SNA` | validated |
| `PARK_pscParkAbortReason` | Parking assist sensors: psc park abort reason; raw 31 = signal not available (SNA) | 3\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 30 | 0 = `NONE`<br>1 = `VELOCITY_TOO_HIGH`<br>2 = `MAX_NUM_OF_MOVES`<br>3 = `NO_VALID_PATH`<br>4 = `UNCONTROLLED_TRAVEL_DIST_REACHED`<br>5 = `OFF_TRACK`<br>6 = `MAX_SWA_DEV_EXCEEDED`<br>7 = `MAX_YAW_ANGLE_REACHED`<br>8 = `OBSTACLE_ON_PATH`<br>9 = `PARK_SPACE_TOO_SMALL`<br>10 = `FULL_WARNING_ON_BOTH_SIDES`<br>11 = `HANDS_ON_DETECTED`<br>12 = `VEHICLE_DYNAMICS_INTERVENTION`<br>13 = `EPAS_FAULT`<br>14 = `DAS_ABORT`<br>15 = `ECU_INTERNAL_FAULT`<br>16 = `SYSTEM_FAULT`<br>17 = `SYSTEM_SERVICE`<br>18 = `ERROR`<br>19 = `PSC_ASYNC_CTRL_SYSTEM`<br>20 = `PSC_HIGH_TORQUE`<br>21 = `PSC_VCTL_GENERAL_ABORT`<br>22 = `PSC_PARK_PONR_NOT_REACHED`<br>23 = `PSC_PARK_STC_FAILED`<br>24 = `PSC_MAX_WAY_BEHIND_HINT`<br>25 = `PSC_MOVEMENT_AT_ACTIVATION`<br>31 = `SNA` | validated |
| `PARK_pscParallelSpace` | The existence and type of a parallel parking slot identified by the ultrasonics. | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE_AVAILABLE`<br>1 = `RIGHT_AVAILABLE`<br>2 = `LEFT_AVAILABLE`<br>3 = `BOTH_AVAILABLE` | validated |
| `PARK_pscCrossSpace` | The type and existence of perpendicular parking slot identified through the ultrasonics | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE_AVAILABLE`<br>1 = `RIGHT_AVAILABLE`<br>2 = `LEFT_AVAILABLE`<br>3 = `BOTH_AVAILABLE` | validated |
| `PARK_pscParallelRightParkable` | Whether or not there is a valid path into a parallel parking slot on the right; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `PARKING_SLOT_OK`<br>2 = `PARKING_SLOT_OK_POSITION_OK`<br>3 = `SNA` | validated |
| `PARK_pscParallelLeftParkable` | Whether or not there is a valid path into a parallel parking slot on the left; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `PARKING_SLOT_OK`<br>2 = `PARKING_SLOT_OK_POSITION_OK`<br>3 = `SNA` | validated |
| `PARK_pscCrossRightParkable` | Parking assist sensors: psc cross right parkable; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `PARKING_SLOT_OK`<br>2 = `PARKING_SLOT_OK_POSITION_OK`<br>3 = `SNA` | validated |
| `PARK_pscMaxVelocity` | Parking assist sensors: psc max velocity; raw 63 = signal not available (SNA) | 18\|6 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6.2 | 63 = `SNA` | validated |
| `PARK_pscCrossLeftParkable` | Parking assist sensors: psc cross left parkable; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `PARKING_SLOT_OK`<br>2 = `PARKING_SLOT_OK_POSITION_OK`<br>3 = `SNA` | validated |
| `PARK_pscParkInstruction` | The control request from PARK ECU during autopark manuever; raw 7 = signal not available (SNA) | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NO_MESSAGE`<br>1 = `STOP`<br>2 = `DRIVE_FORWARD`<br>3 = `DRIVE_BACKWARD`<br>4 = `ABORTED`<br>5 = `EXPLORATION`<br>7 = `SNA` | validated |
| `PARK_pscManeuverDistance` | Real time updated path length from center of vehicle reference frame to desired center of vehicle at end of current parking manuever; raw 2047 = signal not available (SNA) | 29\|11 | little-endian | unsigned | 1 | 0 | cm | 0 to 2046 | 2047 = `SNA` | validated |
| `PARK_pscAngleActive` | Parking assist sensors: psc angle active | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INACTIVE`<br>1 = `REQUEST_CONTROL` | validated |
| `PARK_pscAngleRequest` | Parking assist sensors: psc angle request | 41\|15 | little-endian | unsigned | 0.1 | -1638.4 | deg | -1638.4 to 1638.3 |  | validated |
| `PARK_pscStatusCounter` | Parking assist sensors: psc status counter | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `PARK_pscStatusChecksum` | Parking assist sensors: psc status checksum | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
