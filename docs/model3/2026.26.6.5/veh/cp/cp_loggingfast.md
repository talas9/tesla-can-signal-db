---
layout: default
title: "CP_loggingFast (0x75D) — Charge port controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Charge port controller message: logging fast. Tesla Model 3 CAN bus message CP_loggingFast (0x75D) of Charge port controller, firmware 2026.26.6.5, 26 signals (CP_loggingFastSelect, CP_inductiveSensor_raw, CP_doorOpenActuationTime, CP_doorCloseActuationTime and 22 more). Bit layout, scaling, units and value tables."
---

# CP_loggingFast (0x75D) — Charge port controller, Tesla Model 3 2026.26.6.5 VEH CAN

Charge port controller message: logging fast; frame length observed on a vehicle bus. This page documents the 26 signals of CP_loggingFast as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_loggingFast` |
| CAN id | 0x75D (1885) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 26 |

## Signals of CP_loggingFast

Tesla Model 3 CAN bus signals in `CP_loggingFast`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_loggingFastSelect` | selector | Charge port controller: logging fast select | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6` | plausible |
| `CP_inductiveSensor_raw` | page 0 | Charge port controller: inductive sensor raw | 4\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | validated |
| `CP_doorOpenActuationTime` | page 0 | Charge port controller: door open actuation time | 32\|14 | little-endian | unsigned | 1 | 0 | ms | 0 to 16383 |  | validated |
| `CP_doorCloseActuationTime` | page 0 | Charge port controller: door close actuation time | 46\|14 | little-endian | unsigned | 1 | 0 | ms | 0 to 16383 |  | validated |
| `CP_chargeCableSecured` | page 0 | Indicates whether a charge cable is secured in any inlet | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_chargeCablePresent` | page 0 | Indicates whether a charge cable is present in any inlet | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CABLE_NOT_PRESENT`<br>1 = `CABLE_PRESENT` | validated |
| `CP_latchCheckAvailable` | page 0 | Charge port controller: latch check available | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_UHF_controlState` | page 2 | Control state of UHF receiver | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CP_UHF_INIT`<br>1 = `CP_UHF_CONFIG`<br>2 = `CP_UHF_IDLE`<br>3 = `CP_UHF_CALIBRATE`<br>4 = `CP_UHF_PREPARE_RX`<br>5 = `CP_UHF_RX`<br>6 = `CP_UHF_CHECK_RX`<br>7 = `CP_UHF_READ_RXFIFO`<br>8 = `CP_UHF_HANDLE_FOUND`<br>9 = `CP_UHF_SLEEP`<br>10 = `CP_UHF_FAULT` | validated |
| `CP_proximityV` | page 2 | Charge port controller: proximity v | 8\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 6.5535 |  | validated |
| `CP_proximityV_GBCC1` | page 2 | Sensed voltage of GB DC inlet CC1 connection | 24\|14 | little-endian | unsigned | 0.001 | 0 | V | 0 to 13.3 |  | validated |
| `CP_proximityV_GBCC2` | page 2 | Sensed voltage of GB DC inlet CC2 connection | 38\|14 | little-endian | unsigned | 0.001 | 0 | V | 0 to 13.3 |  | validated |
| `CP_doorPot` | page 2 | Position of the charge port door potentiometer | 52\|12 | little-endian | unsigned | 0.025 | 0 | % | 0 to 100 |  | validated |
| `CP_doorPresenceSensorV` | page 3 | Reports voltage value read by the charge port door's presence sensor. | 4\|12 | little-endian | unsigned | 0.001221 | 0 | V | 0 to 4.999995 |  | validated |
| `CP_doorOpenRequest` | page 3 | Door open request trigger | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CPD_OPEN_REQ_NONE`<br>1 = `CPD_OPEN_REQ_UI`<br>2 = `CPD_OPEN_REQ_SEC`<br>3 = `CPD_OPEN_REQ_UHF`<br>4 = `CPD_OPEN_REQ_PUSH_TO_OPEN`<br>5 = `CPD_OPEN_REQ_CLOSING_FAILED`<br>6 = `CPD_OPEN_REQ_VCFRONT`<br>7 = `CPD_OPEN_REQ_CABLE_RECONNECTED`<br>8 = `CPD_OPEN_REQ_NUM` | validated |
| `CP_doorOpenEndOfDriveReason` | page 3 | Reason why the door stopped moving in the open direction | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_STOP_DRIVE_REASON_NONE`<br>1 = `CP_STOP_DRIVE_REASON_STALLED`<br>2 = `CP_STOP_DRIVE_REASON_STOPPED_MOVING_TIMEOUT`<br>3 = `CP_STOP_DRIVE_REASON_REACHED_STOP`<br>4 = `CP_STOP_DRIVE_REASON_MAX_TARGET_V`<br>5 = `CP_STOP_DRIVE_REASON_ABSOLUTE_TIMEOUT`<br>6 = `CP_STOP_DRIVE_REASON_REQ_OVERRIDE`<br>7 = `CP_STOP_DRIVE_REASON_OVERCURRENT` | validated |
| `CP_coverClosed` | page 3 | Charge port controller: cover closed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_doorCloseEndOfDriveReason` | page 3 | Reason why the door stopped moving in the closing direction | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_STOP_DRIVE_REASON_NONE`<br>1 = `CP_STOP_DRIVE_REASON_STALLED`<br>2 = `CP_STOP_DRIVE_REASON_STOPPED_MOVING_TIMEOUT`<br>3 = `CP_STOP_DRIVE_REASON_REACHED_STOP`<br>4 = `CP_STOP_DRIVE_REASON_MAX_TARGET_V`<br>5 = `CP_STOP_DRIVE_REASON_ABSOLUTE_TIMEOUT`<br>6 = `CP_STOP_DRIVE_REASON_REQ_OVERRIDE`<br>7 = `CP_STOP_DRIVE_REASON_OVERCURRENT` | validated |
| `CP_doorCloseRequest` | page 3 | Door close request trigger | 27\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CPD_CLOSE_REQ_NONE`<br>1 = `CPD_CLOSE_REQ_CABLE_UNPLUGGED`<br>2 = `CPD_CLOSE_REQ_DOOR_OPEN_TIMEOUT`<br>3 = `CPD_CLOSE_REQ_UI`<br>4 = `CPD_CLOSE_REQ_SEC`<br>5 = `CPD_CLOSE_REQ_PUSH_TO_CLOSE`<br>6 = `CPD_CLOSE_REQ_CAR_WASH`<br>7 = `CPD_CLOSE_REQ_FAULT_LINE`<br>8 = `CPD_CLOSE_REQ_ENTER_DRIVE`<br>9 = `CPD_CLOSE_REQ_OPENED_IN_DRIVE_STATE`<br>10 = `CPD_CLOSE_REQ_INITIAL_CINCH`<br>11 = `CPD_CLOSE_REQ_SENSOR_MISMATCH`<br>12 = `CPD_CLOSE_REQ_SENSOR_COMMS_RECOVERED`<br>13 = `CPD_CLOSE_REQ_OPEN_ON_WAKE`<br>14 = `CPD_CLOSE_REQ_VCFRONT`<br>15 = `CPD_CLOSE_REQ_COVER_OPEN`<br>16 = `CPD_CLOSE_REQ_NUM` | validated |
| `CP_latchDisengagingTime` | page 3 | Charge port controller: latch disengaging time | 32\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | validated |
| `CP_latchEngagingTime` | page 3 | Charge port controller: latch engaging time | 42\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | validated |
| `CP_latchDisengagingStopReason` | page 3 | Reason why the latch stopped moving in the engaged direction | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_STOP_DRIVE_REASON_NONE`<br>1 = `CP_STOP_DRIVE_REASON_STALLED`<br>2 = `CP_STOP_DRIVE_REASON_STOPPED_MOVING_TIMEOUT`<br>3 = `CP_STOP_DRIVE_REASON_REACHED_STOP`<br>4 = `CP_STOP_DRIVE_REASON_MAX_TARGET_V`<br>5 = `CP_STOP_DRIVE_REASON_ABSOLUTE_TIMEOUT`<br>6 = `CP_STOP_DRIVE_REASON_REQ_OVERRIDE`<br>7 = `CP_STOP_DRIVE_REASON_OVERCURRENT` | validated |
| `CP_latchEngagingStopReason` | page 3 | Reason why the latch stopped moving in the engaged direction | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_STOP_DRIVE_REASON_NONE`<br>1 = `CP_STOP_DRIVE_REASON_STALLED`<br>2 = `CP_STOP_DRIVE_REASON_STOPPED_MOVING_TIMEOUT`<br>3 = `CP_STOP_DRIVE_REASON_REACHED_STOP`<br>4 = `CP_STOP_DRIVE_REASON_MAX_TARGET_V`<br>5 = `CP_STOP_DRIVE_REASON_ABSOLUTE_TIMEOUT`<br>6 = `CP_STOP_DRIVE_REASON_REQ_OVERRIDE`<br>7 = `CP_STOP_DRIVE_REASON_OVERCURRENT` | validated |
| `CP_pilotUnlatchRequestActive` | page 3 | Reports whether the Charge Port (CP) pilot unlatch request is active. | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_doorIdDetectionState` | page 3 | Charge port controller: door id detection state; raw 0 = signal not available (SNA) | 59\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `DOOR_ID_UNKNOWN_SNA`<br>1 = `DOOR_ID_INVALID`<br>2 = `DOOR_ID_VALID` | validated |
| `CP_doorIdDetectedBin` | page 3 | Charge port controller: door id detected bin | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DOOR_ID_BIN_UNKNOWN`<br>1 = `DOOR_ID_BIN_NMB`<br>2 = `DOOR_ID_BIN_HMC`<br>3 = `DOOR_ID_BIN_OPAL` | validated |
| `CP_semiV2LatchNonLinear` | page 3 | Reports whether the Charge Port (CP) SemiV2 latch potentiometer reading is non-linear. | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`CP_loggingFastSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 2 (5 signals), page 3 (14 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
