---
layout: default
title: "UI_locationOffset (0x3D9) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: location offset. Tesla Model 3 / Model Y CAN bus message UI_locationOffset (0x3D9) of Touchscreen user interface computer, firmware 2025.20.8, 2 signals (UI_latitudeOffset, UI_longitudeOffset). Bit layout, scaling, units and value tables."
---

# UI_locationOffset (0x3D9) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Touchscreen user interface computer message: location offset; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of UI_locationOffset as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_locationOffset` |
| CAN id | 0x3D9 (985) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_locationOffset

Tesla Model 3 / Model Y CAN bus signals in `UI_locationOffset`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_latitudeOffset` | Touchscreen user interface computer: latitude offset | 0\|28 | little-endian | signed | 1.0e-06 | 0 | deg | -134.217728 to 134.217727 |  | plausible |
| `UI_longitudeOffset` | Touchscreen user interface computer: longitude offset | 28\|29 | little-endian | signed | 1.0e-06 | 0 | deg | -268.435456 to 268.435455 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
