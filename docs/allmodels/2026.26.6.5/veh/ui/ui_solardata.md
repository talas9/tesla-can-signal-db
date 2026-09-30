---
layout: default
title: "UI_solarData (0x2D3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: solar data. Tesla Model 3 / Model Y CAN bus message UI_solarData (0x2D3) of Touchscreen user interface computer, firmware 2026.26.6.5, 7 signals (UI_solarAzimuthAngle, UI_solarAzimuthAngleCarRef, UI_isSunUp, UI_solarElevationAngle and 3 more). Bit layout, scaling, units and value tables."
---

# UI_solarData (0x2D3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: solar data; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 7 signals of UI_solarData as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_solarData` |
| CAN id | 0x2D3 (723) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of UI_solarData

Tesla Model 3 / Model Y CAN bus signals in `UI_solarData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_solarAzimuthAngle` | Touchscreen user interface computer: solar azimuth angle; raw 32768 = signal not available (SNA) | 0\|16 | little-endian | signed | 1 | 0 | degrees | -32768 to 32767 | -32768 = `SNA` | plausible |
| `UI_solarAzimuthAngleCarRef` | Touchscreen user interface computer: solar azimuth angle car ref; raw 255 = signal not available (SNA) | 16\|9 | little-endian | signed | 1 | 0 | degrees | -256 to 254 | 255 = `SNA` | plausible |
| `UI_isSunUp` | is sun up; raw 3 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SUN_DOWN`<br>1 = `SUN_UP`<br>3 = `SUN_SNA` | validated |
| `UI_solarElevationAngle` | Solar Elevation Angle; raw 127 = signal not available (SNA) | 32\|8 | little-endian | signed | 1 | 0 | degrees | -128 to 126 | 127 = `SNA` | validated |
| `UI_screenPCBTemperature` | Temperature of display PCB | 40\|8 | little-endian | signed | 0.5 | 40 | degC | -20 to 100 |  | validated |
| `UI_minsToSunset` | time until to sunset | 48\|8 | little-endian | unsigned | 10 | 0 | min | 0 to 2550 |  | validated |
| `UI_minsToSunrise` | time until to sunrise | 56\|8 | little-endian | unsigned | 10 | 0 | min | 0 to 2550 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
