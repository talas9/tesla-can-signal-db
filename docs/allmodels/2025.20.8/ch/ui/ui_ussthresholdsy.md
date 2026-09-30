---
layout: default
title: "UI_ussThresholdsY (0x725) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: uss thresholds y. Tesla Model 3 / Model Y CAN bus message UI_ussThresholdsY (0x725) of Touchscreen user interface computer, firmware 2025.20.8, 14 signals (UI_ussSensorIdY, UI_ussThresholdY0, UI_ussThresholdY1, UI_ussThresholdY2 and 10 more). Bit layout, scaling, units and value tables."
---

# UI_ussThresholdsY (0x725) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Touchscreen user interface computer message: uss thresholds y; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of UI_ussThresholdsY as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_ussThresholdsY` |
| CAN id | 0x725 (1829) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 14 |

## Signals of UI_ussThresholdsY

Tesla Model 3 / Model Y CAN bus signals in `UI_ussThresholdsY`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ussSensorIdY` | Touchscreen user interface computer: uss sensor id y | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `REAR_INNER`<br>1 = `REAR_CORNER`<br>2 = `REAR_SIDE`<br>3 = `FRONT_INNER`<br>4 = `FRONT_CORNER`<br>5 = `FRONT_SIDE` | plausible |
| `UI_ussThresholdY0` | Touchscreen user interface computer: uss threshold Y0 | 3\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY1` | Touchscreen user interface computer: uss threshold Y1 | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY2` | Touchscreen user interface computer: uss threshold Y2 | 13\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY3` | Touchscreen user interface computer: uss threshold Y3 | 18\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY4` | Touchscreen user interface computer: uss threshold Y4 | 23\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY5` | Touchscreen user interface computer: uss threshold Y5 | 28\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY6` | Touchscreen user interface computer: uss threshold Y6 | 33\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY7` | Touchscreen user interface computer: uss threshold Y7 | 38\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY8` | Touchscreen user interface computer: uss threshold Y8 | 43\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY9` | Touchscreen user interface computer: uss threshold Y9 | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY10` | Touchscreen user interface computer: uss threshold Y10 | 53\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdY11` | Touchscreen user interface computer: uss threshold Y11 | 58\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdYControl` | Touchscreen user interface computer: uss threshold y control | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
