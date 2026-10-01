---
layout: default
title: "VCRIGHT_windowStatus (0x2C3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Right body controller message: window status. Tesla Model 3 / Model Y CAN bus message VCRIGHT_windowStatus (0x2C3) of Right body controller, firmware 2025.20.8, 31 signals (VCRIGHT_windowStatusIndex, VCRIGHT_windowStateRF, VCRIGHT_windowTrimClearMoveRequest, VCRIGHT_windowDutyRF and 27 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_windowStatus (0x2C3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Right body controller message: window status; frame length observed on a vehicle bus. This page documents the 31 signals of VCRIGHT_windowStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_windowStatus` |
| CAN id | 0x2C3 (707) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 31 |

## Signals of VCRIGHT_windowStatus

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_windowStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_windowStatusIndex` | selector | Right body controller: window status index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `VCRIGHT_windowStateRF` | page 0 | Status of right front window motor | 1\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STATE_STOPPED`<br>1 = `WINDOW_STATE_MOVING_UP`<br>2 = `WINDOW_STATE_MOVING_DOWN`<br>3 = `WINDOW_STATE_BACKOFF`<br>4 = `WINDOW_STATE_SHORT_DROP`<br>5 = `WINDOW_STATE_SHORT_DROP_REVERSE`<br>6 = `WINDOW_STATE_MOVING_AUTO_UP`<br>7 = `WINDOW_STATE_MOVING_AUTO_DOWN`<br>8 = `WINDOW_STATE_BACKDRIVE`<br>9 = `WINDOW_STATE_SHORT_RISE`<br>10 = `WINDOW_STATE_SHORT_RISE_REVERSE` | plausible |
| `VCRIGHT_windowTrimClearMoveRequest` | page 0 | Reports a request for whether windows should enter or exit trim clear mode. Signal is only valid if Vehicle Controller Left (VCLEFT) is on driver side. | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_SNA`<br>1 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_IDLE`<br>2 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_RESEAL`<br>3 = `WINDOW_TRIM_CLEAR_MOVE_REQUEST_BACKDRIVE` | plausible |
| `VCRIGHT_windowDutyRF` | page 0 | Right body controller: window duty RF | 8\|6 | little-endian | signed | 5 | 0 | % | -100 to 100 |  | plausible |
| `VCRIGHT_windowTrimClearActiveRequest` | page 0 | Reports whether window trim clear is active. Signal is only valid if Vehicle Controller Left (VCLEFT) is on driver side; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_SNA`<br>1 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_INACTIVE`<br>2 = `WINDOW_TRIM_CLEAR_ACTIVE_REQUEST_ACTIVE` | plausible |
| `VCRIGHT_windowCurrentRF` | page 0 | Current drawn by left front window regulator | 16\|6 | little-endian | signed | 0.5 | 0 | A | -15 to 15 |  | plausible |
| `VCRIGHT_windowPositionRF` | page 0 | Right body controller: window position RF; raw 1 = signal not available (SNA) | 22\|9 | little-endian | signed | 1.25 | 265 | mm | -50 to 580 | 1 = `SNA` | plausible |
| `VCRIGHT_windowCalibratedRF` | page 0 | Calibration status of right front window motor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_windowStateRR` | page 0 | Status of right rear window motor | 33\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STATE_STOPPED`<br>1 = `WINDOW_STATE_MOVING_UP`<br>2 = `WINDOW_STATE_MOVING_DOWN`<br>3 = `WINDOW_STATE_BACKOFF`<br>4 = `WINDOW_STATE_SHORT_DROP`<br>5 = `WINDOW_STATE_SHORT_DROP_REVERSE`<br>6 = `WINDOW_STATE_MOVING_AUTO_UP`<br>7 = `WINDOW_STATE_MOVING_AUTO_DOWN`<br>8 = `WINDOW_STATE_BACKDRIVE`<br>9 = `WINDOW_STATE_SHORT_RISE`<br>10 = `WINDOW_STATE_SHORT_RISE_REVERSE` | plausible |
| `VCRIGHT_windowDutyRR` | page 0 | Right body controller: window duty RR | 40\|6 | little-endian | signed | 5 | 0 | % | -100 to 100 |  | plausible |
| `VCRIGHT_windowCurrentRR` | page 0 | Current drawn by left rear window regulator | 48\|6 | little-endian | signed | 0.5 | 0 | A | -15 to 15 |  | plausible |
| `VCRIGHT_windowPositionRR` | page 0 | Right body controller: window position RR | 54\|9 | little-endian | signed | 1.25 | 265 | mm | -50 to 580 |  | plausible |
| `VCRIGHT_windowCalibratedRR` | page 0 | Calibration status of right rear window motor | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_windowThermalTCRF` | page 1 | Right body controller: window thermal TCRF | 1\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 255 |  | plausible |
| `VCRIGHT_windowThermalModeRF` | page 1 | Right body controller: window thermal mode RF; raw 0 = signal not available (SNA) | 9\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_THERMAL_MODE_SNA`<br>1 = `WINDOW_THERMAL_MODE_NORMAL`<br>2 = `WINDOW_THERMAL_MODE_ALERT`<br>3 = `WINDOW_THERMAL_MODE_CRITICAL` | plausible |
| `VCRIGHT_windowStopReasonRF` | page 1 | Reason for right front window stopping motion | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_STOP_REASON_NONE`<br>1 = `WINDOW_STOP_REASON_DOOR_OPEN_TRIM_PROTECT`<br>2 = `WINDOW_STOP_REASON_NEW_REQUEST`<br>3 = `WINDOW_STOP_REASON_TARGET_REACHED`<br>4 = `WINDOW_STOP_REASON_STOP_REQUEST`<br>5 = `WINDOW_STOP_REASON_FULL_OPEN_SOFT_STOP`<br>6 = `WINDOW_STOP_REASON_STATE_TIMEOUT` | plausible |
| `VCRIGHT_windowStopReqReasonRF` | page 1 | Reason for right front window stopping motion | 14\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STOP_REQUEST_REASON_NONE`<br>1 = `WINDOW_STOP_REQUEST_REASON_SWITCH_CANCEL_AUTO_MOVEMENT`<br>2 = `WINDOW_STOP_REQUEST_REASON_SWITCH_RELEASED`<br>3 = `WINDOW_STOP_REQUEST_REASON_REAR_LOCKOUT`<br>4 = `WINDOW_STOP_REQUEST_REASON_THERMAL`<br>5 = `WINDOW_STOP_REQUEST_REASON_STALL`<br>6 = `WINDOW_STOP_REQUEST_REASON_STATE_TIMEOUT`<br>7 = `WINDOW_STOP_REQUEST_REASON_FULL_OPEN_SOFT_STOP`<br>8 = `WINDOW_STOP_REQUEST_REASON_EXTERNAL_REQUEST` | plausible |
| `VCRIGHT_windowThermalTCRR` | page 1 | Right body controller: window thermal TCRR | 18\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 255 |  | plausible |
| `VCRIGHT_windowThermalModeRR` | page 1 | Right body controller: window thermal mode RR; raw 0 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_THERMAL_MODE_SNA`<br>1 = `WINDOW_THERMAL_MODE_NORMAL`<br>2 = `WINDOW_THERMAL_MODE_ALERT`<br>3 = `WINDOW_THERMAL_MODE_CRITICAL` | plausible |
| `VCRIGHT_windowStopReasonRR` | page 1 | Reason for right rear window stopping motion | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_STOP_REASON_NONE`<br>1 = `WINDOW_STOP_REASON_DOOR_OPEN_TRIM_PROTECT`<br>2 = `WINDOW_STOP_REASON_NEW_REQUEST`<br>3 = `WINDOW_STOP_REASON_TARGET_REACHED`<br>4 = `WINDOW_STOP_REASON_STOP_REQUEST`<br>5 = `WINDOW_STOP_REASON_FULL_OPEN_SOFT_STOP`<br>6 = `WINDOW_STOP_REASON_STATE_TIMEOUT` | plausible |
| `VCRIGHT_windowStopReqReasonRR` | page 1 | Reason for right rear window stopping motion | 31\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WINDOW_STOP_REQUEST_REASON_NONE`<br>1 = `WINDOW_STOP_REQUEST_REASON_SWITCH_CANCEL_AUTO_MOVEMENT`<br>2 = `WINDOW_STOP_REQUEST_REASON_SWITCH_RELEASED`<br>3 = `WINDOW_STOP_REQUEST_REASON_REAR_LOCKOUT`<br>4 = `WINDOW_STOP_REQUEST_REASON_THERMAL`<br>5 = `WINDOW_STOP_REQUEST_REASON_STALL`<br>6 = `WINDOW_STOP_REQUEST_REASON_STATE_TIMEOUT`<br>7 = `WINDOW_STOP_REQUEST_REASON_FULL_OPEN_SOFT_STOP`<br>8 = `WINDOW_STOP_REQUEST_REASON_EXTERNAL_REQUEST` | plausible |
| `VCRIGHT_windowControlStateRF` | page 1 | Window control state | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_CONTROL_STATE_IDLE`<br>1 = `WINDOW_CONTROL_STATE_CLOSING`<br>2 = `WINDOW_CONTROL_STATE_GOING_TO_POSITION` | plausible |
| `VCRIGHT_windowCtrlUnavailableRF` | page 1 | Window control unavailable reason | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_CONTROL_UNAVAILABLE_REASON_NONE`<br>1 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNEXPECTED`<br>2 = `WINDOW_CONTROL_UNAVAILABLE_REASON_SWITCH_PRESSED`<br>3 = `WINDOW_CONTROL_UNAVAILABLE_REASON_PINCH`<br>4 = `WINDOW_CONTROL_UNAVAILABLE_REASON_THERMAL_LIMIT`<br>5 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNCALIBRATED`<br>6 = `WINDOW_CONTROL_UNAVAILABLE_REASON_VEHICLE_IN_DRIVE`<br>7 = `WINDOW_CONTROL_UNAVAILABLE_REASON_WINDOW_MOVING` | plausible |
| `VCRIGHT_windowControlStateRR` | page 1 | Window control state | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WINDOW_CONTROL_STATE_IDLE`<br>1 = `WINDOW_CONTROL_STATE_CLOSING`<br>2 = `WINDOW_CONTROL_STATE_GOING_TO_POSITION` | plausible |
| `VCRIGHT_windowCtrlUnavailableRR` | page 1 | Window control unavailable reason | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_CONTROL_UNAVAILABLE_REASON_NONE`<br>1 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNEXPECTED`<br>2 = `WINDOW_CONTROL_UNAVAILABLE_REASON_SWITCH_PRESSED`<br>3 = `WINDOW_CONTROL_UNAVAILABLE_REASON_PINCH`<br>4 = `WINDOW_CONTROL_UNAVAILABLE_REASON_THERMAL_LIMIT`<br>5 = `WINDOW_CONTROL_UNAVAILABLE_REASON_UNCALIBRATED`<br>6 = `WINDOW_CONTROL_UNAVAILABLE_REASON_VEHICLE_IN_DRIVE`<br>7 = `WINDOW_CONTROL_UNAVAILABLE_REASON_WINDOW_MOVING` | plausible |
| `VCRIGHT_windowPositionStateRF` | page 1 | Reports the window position state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_POSITION_UNKNOWN`<br>1 = `WINDOW_POSITION_CLOSED`<br>2 = `WINDOW_POSITION_CRACKED`<br>3 = `WINDOW_POSITION_VENT`<br>4 = `WINDOW_POSITION_DAS_LIMITED`<br>5 = `WINDOW_POSITION_PARTIAL_OPEN`<br>6 = `WINDOW_POSITION_FULL_OPEN`<br>7 = `WINDOW_POSITION_CLOSED_TRIM_CLEAR` | plausible |
| `VCRIGHT_windowPositionStateRR` | page 1 | Window position state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_POSITION_UNKNOWN`<br>1 = `WINDOW_POSITION_CLOSED`<br>2 = `WINDOW_POSITION_CRACKED`<br>3 = `WINDOW_POSITION_VENT`<br>4 = `WINDOW_POSITION_DAS_LIMITED`<br>5 = `WINDOW_POSITION_PARTIAL_OPEN`<br>6 = `WINDOW_POSITION_FULL_OPEN`<br>7 = `WINDOW_POSITION_CLOSED_TRIM_CLEAR` | plausible |
| `VCRIGHT_windowVehGearStateRF` | page 1 | Window's interpretation of vehicle gear state; raw 0 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_VEHICLE_GEAR_STATE_UNKNOWN_SNA`<br>1 = `WINDOW_VEHICLE_GEAR_STATE_PARK`<br>2 = `WINDOW_VEHICLE_GEAR_STATE_IN_GEAR` | plausible |
| `VCRIGHT_windowVehGearStateRR` | page 1 | Window's interpretation of vehicle gear state; raw 0 = signal not available (SNA) | 58\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_VEHICLE_GEAR_STATE_UNKNOWN_SNA`<br>1 = `WINDOW_VEHICLE_GEAR_STATE_PARK`<br>2 = `WINDOW_VEHICLE_GEAR_STATE_IN_GEAR` | plausible |
| `VCRIGHT_windowSpeedTableStatusRF` | page 1 | Speed table build status of right front window; raw 0 = signal not available (SNA) | 60\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_SPEED_TABLE_STATUS_EMPTY_SNA`<br>1 = `WINDOW_SPEED_TABLE_STATUS_SENSITIVE_BUILT`<br>2 = `WINDOW_SPEED_TABLE_STATUS_FULLY_BUILT` | plausible |
| `VCRIGHT_windowSpeedTableStatusRR` | page 1 | Speed table build status of right rear window; raw 0 = signal not available (SNA) | 62\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `WINDOW_SPEED_TABLE_STATUS_EMPTY_SNA`<br>1 = `WINDOW_SPEED_TABLE_STATUS_SENSITIVE_BUILT`<br>2 = `WINDOW_SPEED_TABLE_STATUS_FULLY_BUILT` | plausible |

## Multiplexing

`VCRIGHT_windowStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals), page 1 (18 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
