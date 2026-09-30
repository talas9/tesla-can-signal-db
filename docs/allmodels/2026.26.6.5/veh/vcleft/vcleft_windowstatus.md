---
layout: default
title: "VCLEFT_windowStatus (0x2C2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: window status. Tesla Model 3 / Model Y CAN bus message VCLEFT_windowStatus (0x2C2) of Left body controller, firmware 2026.26.6.5, 31 signals (VCLEFT_windowStatusIndex, VCLEFT_windowStateLF, VCLEFT_windowTrimClearMoveRequest, VCLEFT_windowDutyLF and 27 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_windowStatus (0x2C2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left body controller message: window status; frame length observed on a vehicle bus. This page documents the 31 signals of VCLEFT_windowStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_windowStatus` |
| CAN id | 0x2C2 (706) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 31 |

## Signals of VCLEFT_windowStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_windowStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_windowStatusIndex` | selector | Left body controller: window status index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `VCLEFT_windowStateLF` | page 0 | Status of left front window motor | 1\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STATE_STOPPED`<br>1 = `WINDOW_STATE_MOVING_UP`<br>2 = `WINDOW_STATE_MOVING_DOWN`<br>3 = `WINDOW_STATE_BACKOFF`<br>4 = `WINDOW_STATE_SHORT_DROP`<br>5 = `WINDOW_STATE_SHORT_DROP_REVERSE`<br>6 = `WINDOW_STATE_MOVING_AUTO_UP`<br>7 = `WINDOW_STATE_MOVING_AUTO_DOWN`<br>8 = `WINDOW_STATE_BACKDRIVE`<br>9 = `WINDOW_STATE_SHORT_RISE`<br>10 = `WINDOW_STATE_SHORT_RISE_REVERSE` | validated |
| `VCLEFT_windowTrimClearMoveRequest` | page 0 | Requests whether windows should enter or exit trim clear. Signal only valid if Vehicle Controller Left (VCLEFT) is on driver side. | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_SNA`<br>1 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_IDLE`<br>2 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_RESEAL`<br>3 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_BACKDRIVE` | validated |
| `VCLEFT_windowDutyLF` | page 0 | Left body controller: window duty LF | 8\|6 | little-endian | signed | 5 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_windowTrimClearActiveRequest` | page 0 | Reports whether window trim clear is active. Signal is only valid if Vehicle Controller Left (VCLEFT) is on driver side; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_SNA`<br>1 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_INACTIVE`<br>2 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_ACTIVE` | validated |
| `VCLEFT_windowCurrentLF` | page 0 | Current drawn by left front window regulator | 16\|6 | little-endian | signed | 0.5 | 0 | A | -15 to 15 |  | validated |
| `VCLEFT_windowPositionLF` | page 0 | Left body controller: window position LF; raw 1 = signal not available (SNA) | 22\|9 | little-endian | signed | 1.25 | 265 | mm | -50 to 580 | 1 = `SNA` | validated |
| `VCLEFT_windowCalibratedLF` | page 0 | Calibration status of left front window motor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_windowStateLR` | page 0 | Status of left rear window motor | 33\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STATE_STOPPED`<br>1 = `WINDOW_STATE_MOVING_UP`<br>2 = `WINDOW_STATE_MOVING_DOWN`<br>3 = `WINDOW_STATE_BACKOFF`<br>4 = `WINDOW_STATE_SHORT_DROP`<br>5 = `WINDOW_STATE_SHORT_DROP_REVERSE`<br>6 = `WINDOW_STATE_MOVING_AUTO_UP`<br>7 = `WINDOW_STATE_MOVING_AUTO_DOWN`<br>8 = `WINDOW_STATE_BACKDRIVE`<br>9 = `WINDOW_STATE_SHORT_RISE`<br>10 = `WINDOW_STATE_SHORT_RISE_REVERSE` | validated |
| `VCLEFT_windowDutyLR` | page 0 | Left body controller: window duty LR | 40\|6 | little-endian | signed | 5 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_windowCurrentLR` | page 0 | Current drawn by left rear window regulator | 48\|6 | little-endian | signed | 0.5 | 0 | A | -15 to 15 |  | validated |
| `VCLEFT_windowPositionLR` | page 0 | Left body controller: window position LR | 54\|9 | little-endian | signed | 1.25 | 265 | mm | -50 to 580 |  | validated |
| `VCLEFT_windowCalibratedLR` | page 0 | Calibraiton status of left rear window motor | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_windowThermalTCLF` | page 1 | Left body controller: window thermal TCLF | 1\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 255 |  | validated |
| `VCLEFT_windowThermalModeLF` | page 1 | Left body controller: window thermal mode LF; raw 0 = signal not available (SNA) | 9\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_THERMAL_MODE_SNA`<br>1 = `WINDOW_THERMAL_MODE_NORMAL`<br>2 = `WINDOW_THERMAL_MODE_ALERT`<br>3 = `WINDOW_THERMAL_MODE_CRITICAL` | validated |
| `VCLEFT_windowStopReasonLF` | page 1 | Reason for left front window stopping motion | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_STOP_REASON_NONE`<br>1 = `WINDOW_STOP_REASON_DOOR_OPEN_TRIM_PROTECT`<br>2 = `WINDOW_STOP_REASON_NEW_REQUEST`<br>3 = `WINDOW_STOP_REASON_TARGET_REACHED`<br>4 = `WINDOW_STOP_REASON_STOP_REQUEST`<br>5 = `WINDOW_STOP_REASON_FULL_OPEN_SOFT_STOP`<br>6 = `WINDOW_STOP_REASON_STATE_TIMEOUT` | validated |
| `VCLEFT_windowStopReqReasonLF` | page 1 | Reason for left front window stopping motion | 14\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STOP_REQUEST_REASON_NONE`<br>1 = `WINDOW_STOP_REQUEST_REASON_SWITCH_CANCEL_AUTO_MOVEMENT`<br>2 = `WINDOW_STOP_REQUEST_REASON_SWITCH_RELEASED`<br>3 = `WINDOW_STOP_REQUEST_REASON_REAR_LOCKOUT`<br>4 = `WINDOW_STOP_REQUEST_REASON_THERMAL`<br>5 = `WINDOW_STOP_REQUEST_REASON_STALL`<br>6 = `WINDOW_STOP_REQUEST_REASON_STATE_TIMEOUT`<br>7 = `WINDOW_STOP_REQUEST_REASON_FULL_OPEN_SOFT_STOP`<br>8 = `WINDOW_STOP_REQUEST_REASON_EXTERNAL_REQUEST` | validated |
| `VCLEFT_windowThermalTCLR` | page 1 | Left body controller: window thermal TCLR | 18\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 255 |  | validated |
| `VCLEFT_windowThermalModeLR` | page 1 | Left body controller: window thermal mode LR; raw 0 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_THERMAL_MODE_SNA`<br>1 = `WINDOW_THERMAL_MODE_NORMAL`<br>2 = `WINDOW_THERMAL_MODE_ALERT`<br>3 = `WINDOW_THERMAL_MODE_CRITICAL` | validated |
| `VCLEFT_windowStopReasonLR` | page 1 | Reason for left rear window stopping motion | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_STOP_REASON_NONE`<br>1 = `WINDOW_STOP_REASON_DOOR_OPEN_TRIM_PROTECT`<br>2 = `WINDOW_STOP_REASON_NEW_REQUEST`<br>3 = `WINDOW_STOP_REASON_TARGET_REACHED`<br>4 = `WINDOW_STOP_REASON_STOP_REQUEST`<br>5 = `WINDOW_STOP_REASON_FULL_OPEN_SOFT_STOP`<br>6 = `WINDOW_STOP_REASON_STATE_TIMEOUT` | validated |
| `VCLEFT_windowStopReqReasonLR` | page 1 | Reason for left rear window stopping motion | 31\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STOP_REQUEST_REASON_NONE`<br>1 = `WINDOW_STOP_REQUEST_REASON_SWITCH_CANCEL_AUTO_MOVEMENT`<br>2 = `WINDOW_STOP_REQUEST_REASON_SWITCH_RELEASED`<br>3 = `WINDOW_STOP_REQUEST_REASON_REAR_LOCKOUT`<br>4 = `WINDOW_STOP_REQUEST_REASON_THERMAL`<br>5 = `WINDOW_STOP_REQUEST_REASON_STALL`<br>6 = `WINDOW_STOP_REQUEST_REASON_STATE_TIMEOUT`<br>7 = `WINDOW_STOP_REQUEST_REASON_FULL_OPEN_SOFT_STOP`<br>8 = `WINDOW_STOP_REQUEST_REASON_EXTERNAL_REQUEST` | validated |
| `VCLEFT_windowControlStateLF` | page 1 | Window control state | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_CONTROL_STATE_IDLE`<br>1 = `WINDOW_CONTROL_STATE_CLOSING`<br>2 = `WINDOW_CONTROL_STATE_GOING_TO_POSITION` | validated |
| `VCLEFT_windowCtrlUnavailableLF` | page 1 | Window control unavailable reason | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_CONTROL_UNAVAILABLE_REASON_NONE`<br>1 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNEXPECTED`<br>2 = `WINDOW_CONTROL_UNAVAILABLE_REASON_SWITCH_PRESSED`<br>3 = `WINDOW_CONTROL_UNAVAILABLE_REASON_PINCH`<br>4 = `WINDOW_CONTROL_UNAVAILABLE_REASON_THERMAL_LIMIT`<br>5 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNCALIBRATED`<br>6 = `WINDOW_CONTROL_UNAVAILABLE_REASON_VEHICLE_IN_DRIVE`<br>7 = `WINDOW_CONTROL_UNAVAILABLE_REASON_WINDOW_MOVING` | validated |
| `VCLEFT_windowControlStateLR` | page 1 | Window control state | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_CONTROL_STATE_IDLE`<br>1 = `WINDOW_CONTROL_STATE_CLOSING`<br>2 = `WINDOW_CONTROL_STATE_GOING_TO_POSITION` | validated |
| `VCLEFT_windowCtrlUnavailableLR` | page 1 | Window control unavailable reason | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_CONTROL_UNAVAILABLE_REASON_NONE`<br>1 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNEXPECTED`<br>2 = `WINDOW_CONTROL_UNAVAILABLE_REASON_SWITCH_PRESSED`<br>3 = `WINDOW_CONTROL_UNAVAILABLE_REASON_PINCH`<br>4 = `WINDOW_CONTROL_UNAVAILABLE_REASON_THERMAL_LIMIT`<br>5 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNCALIBRATED`<br>6 = `WINDOW_CONTROL_UNAVAILABLE_REASON_VEHICLE_IN_DRIVE`<br>7 = `WINDOW_CONTROL_UNAVAILABLE_REASON_WINDOW_MOVING` | validated |
| `VCLEFT_windowPositionStateLF` | page 1 | Window position state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_POSITION_UNKNOWN`<br>1 = `WINDOW_POSITION_CLOSED`<br>2 = `WINDOW_POSITION_CRACKED`<br>3 = `WINDOW_POSITION_VENT`<br>4 = `WINDOW_POSITION_DAS_LIMITED`<br>5 = `WINDOW_POSITION_PARTIAL_OPEN`<br>6 = `WINDOW_POSITION_FULL_OPEN`<br>7 = `WINDOW_POSITION_CLOSED_TRIM_CLEAR` | validated |
| `VCLEFT_windowPositionStateLR` | page 1 | Window position state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_POSITION_UNKNOWN`<br>1 = `WINDOW_POSITION_CLOSED`<br>2 = `WINDOW_POSITION_CRACKED`<br>3 = `WINDOW_POSITION_VENT`<br>4 = `WINDOW_POSITION_DAS_LIMITED`<br>5 = `WINDOW_POSITION_PARTIAL_OPEN`<br>6 = `WINDOW_POSITION_FULL_OPEN`<br>7 = `WINDOW_POSITION_CLOSED_TRIM_CLEAR` | validated |
| `VCLEFT_windowVehGearStateLF` | page 1 | Window's interpretation of vehicle gear state; raw 0 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_VEHICLE_GEAR_STATE_UNKNOWN_SNA`<br>1 = `WINDOW_VEHICLE_GEAR_STATE_PARK`<br>2 = `WINDOW_VEHICLE_GEAR_STATE_IN_GEAR` | validated |
| `VCLEFT_windowVehGearStateLR` | page 1 | Window's interpretation of vehicle gear state; raw 0 = signal not available (SNA) | 58\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_VEHICLE_GEAR_STATE_UNKNOWN_SNA`<br>1 = `WINDOW_VEHICLE_GEAR_STATE_PARK`<br>2 = `WINDOW_VEHICLE_GEAR_STATE_IN_GEAR` | validated |
| `VCLEFT_windowSpeedTableStatusLF` | page 1 | Speed table build status of left front window; raw 0 = signal not available (SNA) | 60\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_SPEED_TABLE_STATUS_EMPTY_SNA`<br>1 = `WINDOW_SPEED_TABLE_STATUS_SENSITIVE_BUILT`<br>2 = `WINDOW_SPEED_TABLE_STATUS_FULLY_BUILT` | validated |
| `VCLEFT_windowSpeedTableStatusLR` | page 1 | Speed table build status of left rear window; raw 0 = signal not available (SNA) | 62\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_SPEED_TABLE_STATUS_EMPTY_SNA`<br>1 = `WINDOW_SPEED_TABLE_STATUS_SENSITIVE_BUILT`<br>2 = `WINDOW_SPEED_TABLE_STATUS_FULLY_BUILT` | validated |

## Multiplexing

`VCLEFT_windowStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals), page 1 (18 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
