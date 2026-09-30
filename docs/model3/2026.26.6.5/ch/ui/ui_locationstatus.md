---
layout: default
title: "UI_locationStatus (0x309) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: location status. Tesla Model 3 CAN bus message UI_locationStatus (0x309) of Touchscreen user interface computer, firmware 2026.26.6.5, 3 signals (UI_latitude, UI_longitude, UI_gpsAccuracy). Bit layout, scaling, units and value tables."
---

# UI_locationStatus (0x309) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN

Touchscreen user interface computer message: location status; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of UI_locationStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_locationStatus` |
| CAN id | 0x309 (777) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_locationStatus

Tesla Model 3 CAN bus signals in `UI_locationStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_latitude` | Touchscreen user interface computer: latitude | 0\|28 | little-endian | signed | 1.0e-06 | 0 | deg | -134.217728 to 134.217727 |  | plausible |
| `UI_longitude` | Touchscreen user interface computer: longitude | 28\|29 | little-endian | signed | 1.0e-06 | 0 | deg | -268.435456 to 268.435455 |  | plausible |
| `UI_gpsAccuracy` | Touchscreen user interface computer: gps accuracy; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 0.2 | 0 | m | 0 to 25.2 | 127 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
