---
layout: default
title: "UI_frontSeatRequests (0x4F3) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: front seat requests. Tesla Model Y CAN bus message UI_frontSeatRequests (0x4F3) of Touchscreen user interface computer, firmware 2026.26.6.5, 24 signals (UI_frontRightSeatTrackForward, UI_frontRightSeatTrackBack, UI_frontLeftSeatTrackForward, UI_frontLeftSeatTrackBack and 20 more). Bit layout, scaling, units and value tables."
---

# UI_frontSeatRequests (0x4F3) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: front seat requests; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 24 signals of UI_frontSeatRequests as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_frontSeatRequests` |
| CAN id | 0x4F3 (1267) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 24 |

## Signals of UI_frontSeatRequests

Tesla Model Y CAN bus signals in `UI_frontSeatRequests`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_frontRightSeatTrackForward` | Touchscreen user interface computer: front right seat track forward | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatTrackBack` | Touchscreen user interface computer: front right seat track back | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTrackForward` | Touchscreen user interface computer: front left seat track forward | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTrackBack` | Touchscreen user interface computer: front left seat track back | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatBackrestBack` | Touchscreen user interface computer: front right seat backrest back | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatBackrestForward` | Touchscreen user interface computer: front right seat backrest forward | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatBackrestBack` | Touchscreen user interface computer: front left seat backrest back | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatBackrestForward` | Touchscreen user interface computer: front left seat backrest forward | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatTiltUp` | Touchscreen user interface computer: front right seat tilt up | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatTiltDown` | Touchscreen user interface computer: front right seat tilt down | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTiltUp` | Touchscreen user interface computer: front left seat tilt up | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTiltDown` | Touchscreen user interface computer: front left seat tilt down | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLiftUp` | Touchscreen user interface computer: front right seat lift up | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLiftDown` | Touchscreen user interface computer: front right seat lift down | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLiftUp` | Touchscreen user interface computer: front left seat lift up | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLiftDown` | Touchscreen user interface computer: front left seat lift down | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLumbarUp` | Touchscreen user interface computer: front left seat lumbar up | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLumbarDown` | Touchscreen user interface computer: front left seat lumbar down | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLumbarUp` | Touchscreen user interface computer: front right seat lumbar up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLumbarDown` | Touchscreen user interface computer: front right seat lumbar down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLumbarIn` | Touchscreen user interface computer: front left seat lumbar in | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatLumbarOut` | Touchscreen user interface computer: front left seat lumbar out | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLumbarIn` | Touchscreen user interface computer: front right seat lumbar in | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatLumbarOut` | Touchscreen user interface computer: front right seat lumbar out | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
