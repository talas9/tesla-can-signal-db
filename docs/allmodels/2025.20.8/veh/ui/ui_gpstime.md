---
layout: default
title: "UI_gpsTime (0x324) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: gps time. Tesla Model 3 / Model Y CAN bus message UI_gpsTime (0x324) of Touchscreen user interface computer, firmware 2025.20.8, 1 signals (UI_gpsTime). Bit layout, scaling, units and value tables."
---

# UI_gpsTime (0x324) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: gps time; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 1 signals of UI_gpsTime as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_gpsTime` |
| CAN id | 0x324 (804) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of UI_gpsTime

Tesla Model 3 / Model Y CAN bus signals in `UI_gpsTime`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_gpsTime` | Touchscreen user interface computer: gps time | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
