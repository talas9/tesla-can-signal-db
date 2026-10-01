---
layout: default
title: "UI_seatControl (0x29A) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: seat control. Tesla Model Y CAN bus message UI_seatControl (0x29A) of Touchscreen user interface computer, firmware 2026.26.6.5, 13 signals (UI_seatControlIndex, UI_3RSeatChildLock, UI_2RowLeftSeatTrackBack, UI_2RowLeftSeatTrackForward and 9 more). Bit layout, scaling, units and value tables."
---

# UI_seatControl (0x29A) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: seat control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of UI_seatControl as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_seatControl` |
| CAN id | 0x29A (666) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 13 |

## Signals of UI_seatControl

Tesla Model Y CAN bus signals in `UI_seatControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_seatControlIndex` | selector | Touchscreen user interface computer: seat control index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3` | plausible |
| `UI_3RSeatChildLock` | page 0 | Reports the state of 3rd row seat fold flat child lock from the UI | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_LEFT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_RIGHT`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_BOTH` | plausible |
| `UI_2RowLeftSeatTrackBack` | page 0 | Touchscreen user interface computer: 2 row left seat track back | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_2RowLeftSeatTrackForward` | page 0 | Touchscreen user interface computer: 2 row left seat track forward | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_2RowRightSeatTrackBack` | page 0 | Touchscreen user interface computer: 2 row right seat track back | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_2RowRightSeatTrackForward` | page 0 | Touchscreen user interface computer: 2 row right seat track forward | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_left3RowSeatAdjustmentRequest` | page 0 | Reports request from the touchscreen User Interface (UI) to actuate the left third row seat. | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_COMFORT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_FAST`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_COMFORT`<br>4 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_FAST`<br>5 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_TOGGLE_FOLD`<br>6 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_STOP` | plausible |
| `UI_right3RowSeatAdjustmentRequest` | page 0 | Reports request from the touchscreen User Interface (UI) to actuate the right third row seat. | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_COMFORT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_FAST`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_COMFORT`<br>4 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_FAST`<br>5 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_TOGGLE_FOLD`<br>6 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_STOP` | plausible |
| `UI_2RLeftSeatFanReq` | page 0 | Request for second row left seat ventilation | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | plausible |
| `UI_2RRightSeatFanReq` | page 0 | Request for second row right seat ventilation | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | plausible |
| `UI_leftThirdRowSeatRequestFromRearDisplay` | page 0 | Touchscreen user interface computer: left third row seat request from rear display | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_rightThirdRowSeatRequestFromRearDisplay` | page 0 | Touchscreen user interface computer: right third row seat request from rear display | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_seatChoreographyStopRequest` | page 0 | Reports if the UI requests to stop the seat choreography | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`UI_seatControlIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
