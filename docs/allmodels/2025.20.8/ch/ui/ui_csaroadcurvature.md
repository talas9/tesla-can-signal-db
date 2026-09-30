---
layout: default
title: "UI_csaRoadCurvature (0x2A7) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: csa road curvature. Tesla Model 3 / Model Y CAN bus message UI_csaRoadCurvature (0x2A7) of Touchscreen user interface computer, firmware 2025.20.8, 7 signals (UI_csaRoadCurvC2, UI_csaRoadCurvC3, UI_csaRoadCurvRange, UI_csaRoadCurvCounter and 3 more). Bit layout, scaling, units and value tables."
---

# UI_csaRoadCurvature (0x2A7) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Touchscreen user interface computer message: csa road curvature; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of UI_csaRoadCurvature as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_csaRoadCurvature` |
| CAN id | 0x2A7 (679) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 7 |

## Signals of UI_csaRoadCurvature

Tesla Model 3 / Model Y CAN bus signals in `UI_csaRoadCurvature`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_csaRoadCurvC2` | Touchscreen user interface computer: csa road curv C2 | 0\|16 | little-endian | signed | 1.0e-06 | 0 | 1/m | -0.032768 to 0.032767 |  | plausible |
| `UI_csaRoadCurvC3` | Touchscreen user interface computer: csa road curv C3 | 16\|16 | little-endian | signed | 4.0e-09 | 0 | 1/m2 | -0.000131072 to 0.000131068 |  | plausible |
| `UI_csaRoadCurvRange` | Touchscreen user interface computer: csa road curv range | 32\|8 | little-endian | unsigned | 2 | 0 | m | 0 to 510 |  | plausible |
| `UI_csaRoadCurvCounter` | Touchscreen user interface computer: csa road curv counter | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_csaRoadCurvUsingTspline` | Touchscreen user interface computer: csa road curv using tspline | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_csaRoadCurvReserved` | Touchscreen user interface computer: csa road curv reserved | 49\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_csaRoadCurvChecksum` | Touchscreen user interface computer: csa road curv checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
