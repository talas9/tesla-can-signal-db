---
layout: default
title: "VCRIGHT_seatStatus (0x4E3) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: seat status. Tesla Model Y CAN bus message VCRIGHT_seatStatus (0x4E3) of Right body controller, firmware 2026.26.6.5, 60 signals (VCRIGHT_seatStatusIndex, VC_AH_1RowRightSeatMovementHealth, VCRIGHT_frontSeatTrackPos, VCRIGHT_frontSeatTrackCurrent and 56 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_seatStatus (0x4E3) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Right body controller message: seat status; frame length observed on a vehicle bus. This page documents the 60 signals of VCRIGHT_seatStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_seatStatus` |
| CAN id | 0x4E3 (1251) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 60 |

## Signals of VCRIGHT_seatStatus

Tesla Model Y CAN bus signals in `VCRIGHT_seatStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_seatStatusIndex` | selector | Right body controller: seat status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRACK`<br>1 = `BACK`<br>2 = `LIFT`<br>3 = `TILT`<br>4 = `LUMBAR`<br>5 = `POSITION`<br>6 = `OFFSETS`<br>7 = `RELATIVE_POSITION` | validated |
| `VC_AH_1RowRightSeatMovementHealth` | page 0 | Right body controller: AH 1 row right seat movement health | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_MOVEMENT_HEALTH_UNKNOWN`<br>1 = `SEAT_MOVEMENT_HEALTHY`<br>2 = `SEAT_CANNOT_MOVE`<br>3 = `SEAT_IN_NON_USE_POSITION`<br>4 = `SEAT_CALIBRATION_REQUIRED` | validated |
| `VCRIGHT_frontSeatTrackPos` | page 0 | Motor encoder value representing front left seat track position | 8\|16 | little-endian | signed | 1 | 0 |  | -32768 to 32767 |  | validated |
| `VCRIGHT_frontSeatTrackCurrent` | page 0 | Current drawn by front left seat track motor | 24\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | validated |
| `VCRIGHT_frontSeatTrackDuty` | page 0 | Front left seat track motor duty cycle | 36\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatTrackState` | page 0 | State of front right seat track motor | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_frontSeatTrackCalibrated` | page 0 | Right body controller: front seat track calibrated | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTrackLog` | page 0 | Right body controller: front seat track log | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTrackBridgeSt` | page 0 | Bridge state | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IO_BRIDGE_STATE_DISABLED`<br>1 = `IO_BRIDGE_STATE_ENABLED`<br>2 = `IO_BRIDGE_STATE_BRAKE`<br>3 = `IO_BRIDGE_STATE_COAST` | validated |
| `VCRIGHT_frontSeatTrackPercentage` | page 0 | Communicates position of front seat track as percentage of its total range | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_frontSeatBackPos` | page 1 | Motor encoder value representing front right seat backrest position | 8\|16 | little-endian | signed | 1 | 0 |  | -32768 to 32767 |  | validated |
| `VCRIGHT_frontSeatBackCurrent` | page 1 | Current drawn by front right seat backrest motor | 24\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | validated |
| `VCRIGHT_frontSeatBackDuty` | page 1 | Front right seat backrest motor duty cycle | 36\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatBackState` | page 1 | Active state of front right seat backrest | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_frontSeatBackCalibrated` | page 1 | Right body controller: front seat back calibrated | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatBackLog` | page 1 | Right body controller: front seat back log | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatBackBridgeSt` | page 1 | Bridge state | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IO_BRIDGE_STATE_DISABLED`<br>1 = `IO_BRIDGE_STATE_ENABLED`<br>2 = `IO_BRIDGE_STATE_BRAKE`<br>3 = `IO_BRIDGE_STATE_COAST` | validated |
| `VCRIGHT_frontSeatBackPercentage` | page 1 | Communicates position of front seat backrest recline as percentage of its total range | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_frontSeatLiftPos` | page 2 | Motor encoder value representing front left seat lift position | 8\|16 | little-endian | signed | 1 | 0 |  | -32768 to 32767 |  | validated |
| `VCRIGHT_frontSeatLiftCurrent` | page 2 | Current drawn by front left seat lift motor | 24\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | validated |
| `VCRIGHT_frontSeatLiftDuty` | page 2 | Front left seat lift motor duty cycle | 36\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatLiftState` | page 2 | Status of front left seat motor | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_frontSeatLiftCalibrated` | page 2 | Right body controller: front seat lift calibrated | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatLiftLog` | page 2 | Right body controller: front seat lift log | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatLiftBridgeSt` | page 2 | Bridge state | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IO_BRIDGE_STATE_DISABLED`<br>1 = `IO_BRIDGE_STATE_ENABLED`<br>2 = `IO_BRIDGE_STATE_BRAKE`<br>3 = `IO_BRIDGE_STATE_COAST` | validated |
| `VCRIGHT_frontSeatLiftPercentage` | page 2 | Communicates position of front seat lift as percentage of its total range | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_frontSeatTiltPos` | page 3 | Motor encoder value representing front left seat tilt position | 8\|16 | little-endian | signed | 1 | 0 |  | -32768 to 32767 |  | validated |
| `VCRIGHT_frontSeatTiltCurrent` | page 3 | Current drawn by front left seat tilt motor | 24\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | validated |
| `VCRIGHT_frontSeatTiltDuty` | page 3 | Front left seat tilt motor duty cycle | 36\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatTiltState` | page 3 | State of front right seat tilt motor | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_frontSeatTiltCalibrated` | page 3 | Right body controller: front seat tilt calibrated | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTiltLog` | page 3 | Right body controller: front seat tilt log | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTiltBridgeSt` | page 3 | Bridge state | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IO_BRIDGE_STATE_DISABLED`<br>1 = `IO_BRIDGE_STATE_ENABLED`<br>2 = `IO_BRIDGE_STATE_BRAKE`<br>3 = `IO_BRIDGE_STATE_COAST` | validated |
| `VCRIGHT_frontSeatTiltPercentage` | page 3 | Communicates position of front seat tilt as percentage of its total range | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_lumbarAState` | page 4 | State of front right seat lumbar bladder A | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_lumbarBState` | page 4 | State of front right lumbar bladder B | 6\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SEAT_STATE_STOPPED`<br>1 = `SEAT_STATE_MOVING_UP`<br>2 = `SEAT_STATE_MOVING_DOWN`<br>3 = `SEAT_STATE_RECALLING`<br>4 = `SEAT_STATE_CALIBRATING`<br>5 = `SEAT_STATE_UNDEFINED` | validated |
| `VCRIGHT_lumbarAPressureHpa` | page 4 | Right body controller: lumbar a pressure hpa | 9\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |
| `VCRIGHT_lumbarAPressureHpaFilt` | page 4 | logs filtered pressure of right seat lumbar bladder A | 21\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | validated |
| `VCRIGHT_lumbarBPressureHpa` | page 4 | Right body controller: lumbar b pressure hpa | 31\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |
| `VCRIGHT_lumbarBPressureHpaFilt` | page 4 | logs filtered pressure of right seat lumbar bladder B | 43\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | validated |
| `VCRIGHT_lumbarActiveTooLongErr` | page 4 | Error reported by lumbar ECU: Valve activated too long | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarMaxPErr` | page 4 | Error reported by lumbar ECU: max bladder pressure reached | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarOvercurrentErr` | page 4 | Error reported by lumbar ECU: pump overcurrent | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarMaxOperatingPErr` | page 4 | Error reported by lumbar ECU: max bladder operating pressure reached | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarMinPErr` | page 4 | Error reported by lumbar ECU: min bladder pressure reached | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarGeneralErr` | page 4 | Error reported by lumbar ECU: general error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarDevMaxPumpPressA` | page 4 | System has reached Tesla specified maximum pressure for lumbar bladder A | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_lumbarDevMaxPumpPressB` | page 4 | System has reached Tesla specified maximum pressure for lumbar bladder B | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_frontSeatTrackPosReal` | page 5 | Front right seat track position in millimeters | 3\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_frontSeatBackPosReal` | page 5 | Front right seat backrest position in degrees | 16\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatLiftPosReal` | page 5 | Front right seat lift position in millimeters | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_frontSeatTiltPosReal` | page 5 | Front right seat tilt position in degrees | 40\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatThighSupportPosReal` | page 5 | Position of front seat thigh support in a physical unit | 52\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_frontSeatTrackPosOffset` | page 6 | Communicates post calibration position offset of front right seat track in a physical unit | 3\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_frontSeatBackPosOffset` | page 6 | Communicates post calibration position offset of front right seat backrest in a physical unit | 16\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatLiftPosOffset` | page 6 | Communicates post calibration position offset of front right seat lift in a physical unit | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_frontSeatTiltPosOffset` | page 6 | Communicates post calibration position offset of front right seat tilt in a physical unit | 40\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | validated |
| `VCRIGHT_frontSeatThighSupportPosOffset` | page 6 | Post calibration position offset of front seat thigh support in a physical unit | 52\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | validated |
| `VCRIGHT_lumbarAPressurePercentage` | page 7 | Percentage of lumbar bladder A pressure relative to maximum pressure | 3\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_lumbarBPressurePercentage` | page 7 | Percentage of lumbar bladder B pressure relative to maximum pressure | 10\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |

## Multiplexing

`VCRIGHT_seatStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals), page 1 (8 signals), page 2 (8 signals), page 3 (8 signals), page 4 (14 signals), page 5 (5 signals), page 6 (5 signals), page 7 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
