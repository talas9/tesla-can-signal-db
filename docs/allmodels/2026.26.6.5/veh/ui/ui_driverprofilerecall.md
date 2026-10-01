---
layout: default
title: "UI_driverProfileRecall (0x285) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: driver profile recall. Tesla Model 3 / Model Y CAN bus message UI_driverProfileRecall (0x285) of Touchscreen user interface computer, firmware 2026.26.6.5, 24 signals (UI_driverProfileRecallIndex, UI_driverProfileRecallStop, UI_frontSeatRecallActive, UI_frontSeatTrackPos and 20 more). Bit layout, scaling, units and value tables."
---

# UI_driverProfileRecall (0x285) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: driver profile recall; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 24 signals of UI_driverProfileRecall as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverProfileRecall` |
| CAN id | 0x285 (645) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 24 |

## Signals of UI_driverProfileRecall

Tesla Model 3 / Model Y CAN bus signals in `UI_driverProfileRecall`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_driverProfileRecallIndex` | selector | Touchscreen user interface computer: driver profile recall index; raw 0 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5` | validated |
| `UI_driverProfileRecallStop` |  | notifies controller to stop profile recall action | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_frontSeatRecallActive` | page 1 | signals when driver seat presets are being recalled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_frontSeatTrackPos` | page 1 | Touchscreen user interface computer: front seat track pos | 5\|10 | little-endian | signed | 4 | 0 | mm | -2048 to 2044 |  | plausible |
| `UI_frontSeatBackPos` | page 1 | Touchscreen user interface computer: front seat back pos | 16\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | plausible |
| `UI_frontSeatLiftPos` | page 1 | Touchscreen user interface computer: front seat lift pos | 32\|10 | little-endian | signed | 4 | 0 | mm | -2048 to 2044 |  | plausible |
| `UI_frontSeatTiltPos` | page 1 | Touchscreen user interface computer: front seat tilt pos | 48\|12 | little-endian | signed | 0.1 | 0 | deg | -204.8 to 204.7 |  | plausible |
| `UI_columnAndLumbarRecallActive` | page 2 | Touchscreen user interface computer: column and lumbar recall active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_steeringColumnUpDownPos` | page 2 | Touchscreen user interface computer: steering column up down pos | 8\|8 | little-endian | signed | 1 | 103 | mm | -25 to 230 |  | plausible |
| `UI_lumbarAPressurePercentage` | page 2 | Touchscreen user interface computer: lumbar a pressure percentage; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | plausible |
| `UI_lumbarBPressurePercentage` | page 2 | Touchscreen user interface computer: lumbar b pressure percentage; raw 127 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | plausible |
| `UI_steeringColumnInOutPos` | page 2 | Touchscreen user interface computer: steering column in out pos | 48\|8 | little-endian | signed | 1 | 103 | mm | -25 to 230 |  | plausible |
| `UI_leftMirrorTiltXPosition` | page 3 | signal from ui to command mirror X tilt position | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `UI_leftMirrorTiltYPosition` | page 3 | signal from ui to command mirror Y tilt position | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `UI_rightMirrorTiltXPosition` | page 3 | Touchscreen user interface computer: right mirror tilt x position | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `UI_rightMirrorTiltYPosition` | page 3 | Touchscreen user interface computer: right mirror tilt y position | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `UI_frontSeatThighSupportPos` | page 3 | Touchscreen user interface computer: front seat thigh support pos | 40\|8 | little-endian | signed | 1 | 0 | mm | -128 to 127 |  | plausible |
| `UI_mirrorRecallActive` | page 4 | Touchscreen user interface computer: mirror recall active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_customMirrorDipPositionsSet` | page 4 | Reports whether custom mirror dip positions are set. | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_leftMirrorDipXPosition` | page 4 | signal from ui to command left mirror X dip position | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `UI_leftMirrorDipYPosition` | page 4 | signal from ui to command mirror Y dip position | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `UI_rightMirrorDipXPosition` | page 4 | Touchscreen user interface computer: right mirror dip x position | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | validated |
| `UI_rightMirrorDipYPosition` | page 4 | Touchscreen user interface computer: right mirror dip y position | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | validated |
| `UI_modifyMirrorDipRequest` | page 4 | Reports that a user is trying to modify the mirrors in the dipped position. | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MODIFY_MIRROR_DIP_REQUEST_NONE`<br>1 = `MODIFY_MIRROR_DIP_REQUEST_UNDIPPED`<br>2 = `MODIFY_MIRROR_DIP_REQUEST_DIPPED` | validated |

## Multiplexing

`UI_driverProfileRecallIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals), page 2 (5 signals), page 3 (5 signals), page 4 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
