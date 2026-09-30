---
layout: default
title: "UI_roadCurvature (0x278) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: road curvature. Tesla Model 3 CAN bus message UI_roadCurvature (0x278) of Touchscreen user interface computer, firmware 2025.20.8, 7 signals (UI_roadCurvC0, UI_roadCurvC1, UI_roadCurvC2, UI_roadCurvC3 and 3 more). Bit layout, scaling, units and value tables."
---

# UI_roadCurvature (0x278) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN

Touchscreen user interface computer message: road curvature; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of UI_roadCurvature as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_roadCurvature` |
| CAN id | 0x278 (632) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 7 |

## Signals of UI_roadCurvature

Tesla Model 3 CAN bus signals in `UI_roadCurvature`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_roadCurvC0` | Touchscreen user interface computer: road curv C0 | 0\|11 | little-endian | signed | 0.02 | 0 | m | -20.48 to 20.46 |  | plausible |
| `UI_roadCurvC1` | Touchscreen user interface computer: road curv C1 | 11\|10 | little-endian | signed | 0.00075 | 0 | 1 | -0.384 to 0.38325 |  | plausible |
| `UI_roadCurvC2` | Touchscreen user interface computer: road curv C2 | 21\|14 | little-endian | signed | 7.5e-06 | 0 | 1/m | -0.06144 to 0.0614325 |  | plausible |
| `UI_roadCurvC3` | Touchscreen user interface computer: road curv C3 | 35\|13 | little-endian | signed | 3.0e-08 | 0 | 1/m2 | -0.00012288 to 0.00012285 |  | plausible |
| `UI_roadCurvRange` | Touchscreen user interface computer: road curv range | 48\|6 | little-endian | unsigned | 4 | 0 | m | 0 to 252 |  | plausible |
| `UI_roadCurvHealth` | Touchscreen user interface computer: road curv health | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `DEGRADED`<br>2 = `AVAILABLE`<br>3 = `DATABASE` | plausible |
| `UI_roadCurvChecksum` | Touchscreen user interface computer: road curv checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
