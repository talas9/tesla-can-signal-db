---
layout: default
title: "UI_telemetryControl (0x428) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: telemetry control. Tesla Model 3 / Model Y CAN bus message UI_telemetryControl (0x428) of Touchscreen user interface computer, firmware 2026.26.6.5, 17 signals (UI_TCR_enable, UI_TCR_moveStateStanding, UI_TCR_moveStateStopped, UI_TCR_moveStateMoving and 13 more). Bit layout, scaling, units and value tables."
---

# UI_telemetryControl (0x428) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: telemetry control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 17 signals of UI_telemetryControl as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_telemetryControl` |
| CAN id | 0x428 (1064) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of UI_telemetryControl

Tesla Model 3 / Model Y CAN bus signals in `UI_telemetryControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_TCR_enable` | Touchscreen user interface computer: TCR enable | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_moveStateStanding` | Touchscreen user interface computer: TCR move state standing | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_moveStateStopped` | Touchscreen user interface computer: TCR move state stopped | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_moveStateMoving` | Touchscreen user interface computer: TCR move state moving | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_moveStateIndeterm` | Touchscreen user interface computer: TCR move state indeterm | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_classConstElem` | Touchscreen user interface computer: TCR class const elem | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_classMovingPed` | Touchscreen user interface computer: TCR class moving ped | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_classMovingTwoWheel` | Touchscreen user interface computer: TCR class moving two wheel | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_classMovingFourWheel` | Touchscreen user interface computer: TCR class moving four wheel | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_classUnknown` | Touchscreen user interface computer: TCR class unknown | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TCR_downSampleFactor` | Touchscreen user interface computer: TCR down sample factor | 10\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_TCR_wExist` | Touchscreen user interface computer: TCR w exist | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_TCR_vehSpeed` | Touchscreen user interface computer: TCR veh speed | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_TCR_minRCS` | Touchscreen user interface computer: TCR min RCS | 40\|8 | little-endian | unsigned | 0.25 | -14 | dB | -14 to 49.75 |  | plausible |
| `UI_TCR_maxDy` | Touchscreen user interface computer: TCR max dy | 48\|5 | little-endian | unsigned | 0.5 | 0 | m | 0 to 15.5 |  | plausible |
| `UI_TCR_maxObjects` | Touchscreen user interface computer: TCR max objects | 56\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `UI_TCR_maxRoadClass` | Touchscreen user interface computer: TCR max road class | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
