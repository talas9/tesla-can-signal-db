---
layout: default
title: "UI_ussThresholdsX (0x723) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: uss thresholds x. Tesla Model 3 CAN bus message UI_ussThresholdsX (0x723) of Touchscreen user interface computer, firmware 2025.20.8, 14 signals (UI_ussSensorIdX, UI_ussThresholdX0, UI_ussThresholdX1, UI_ussThresholdX2 and 10 more). Bit layout, scaling, units and value tables."
---

# UI_ussThresholdsX (0x723) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN

Touchscreen user interface computer message: uss thresholds x; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of UI_ussThresholdsX as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_ussThresholdsX` |
| CAN id | 0x723 (1827) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 14 |

## Signals of UI_ussThresholdsX

Tesla Model 3 CAN bus signals in `UI_ussThresholdsX`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ussSensorIdX` | Touchscreen user interface computer: uss sensor id x | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `REAR_INNER`<br>1 = `REAR_CORNER`<br>2 = `REAR_SIDE`<br>3 = `FRONT_INNER`<br>4 = `FRONT_CORNER`<br>5 = `FRONT_SIDE` | plausible |
| `UI_ussThresholdX0` | Touchscreen user interface computer: uss threshold X0 | 3\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX1` | Touchscreen user interface computer: uss threshold X1 | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX2` | Touchscreen user interface computer: uss threshold X2 | 13\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX3` | Touchscreen user interface computer: uss threshold X3 | 18\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX4` | Touchscreen user interface computer: uss threshold X4 | 23\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX5` | Touchscreen user interface computer: uss threshold X5 | 28\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX6` | Touchscreen user interface computer: uss threshold X6 | 33\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX7` | Touchscreen user interface computer: uss threshold X7 | 38\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX8` | Touchscreen user interface computer: uss threshold X8 | 43\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX9` | Touchscreen user interface computer: uss threshold X9 | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX10` | Touchscreen user interface computer: uss threshold X10 | 53\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdX11` | Touchscreen user interface computer: uss threshold X11 | 58\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_ussThresholdXControl` | Touchscreen user interface computer: uss threshold x control | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
