---
layout: default
title: "UI_elevationStatus (0x3D8) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: elevation status. Tesla Model 3 CAN bus message UI_elevationStatus (0x3D8) of Touchscreen user interface computer, firmware 2025.20.8, 2 signals (UI_elevation, UI_navElevation). Bit layout, scaling, units and value tables."
---

# UI_elevationStatus (0x3D8) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN

Touchscreen user interface computer message: elevation status; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 2 signals of UI_elevationStatus as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_elevationStatus` |
| CAN id | 0x3D8 (984) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_elevationStatus

Tesla Model 3 CAN bus signals in `UI_elevationStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_elevation` | Touchscreen user interface computer: elevation; raw 8191 = signal not available (SNA) | 0\|14 | little-endian | signed | 1 | 0 | m | -8192 to 8190 | 8191 = `SNA` | plausible |
| `UI_navElevation` | Touchscreen user interface computer: nav elevation; raw 8191 = signal not available (SNA) | 16\|14 | little-endian | signed | 1 | 0 | m | -8192 to 8190 | 8191 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
