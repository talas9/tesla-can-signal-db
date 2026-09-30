---
layout: default
title: "UI_csaOfframpCurvature (0x298) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: csa offramp curvature. Tesla Model Y CAN bus message UI_csaOfframpCurvature (0x298) of Touchscreen user interface computer, firmware 2025.20.8, 7 signals (UI_csaOfframpCurvC2, UI_csaOfframpCurvC3, UI_csaOfframpCurvRange, UI_csaOfframpCurvCounter and 3 more). Bit layout, scaling, units and value tables."
---

# UI_csaOfframpCurvature (0x298) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 CH CAN

Touchscreen user interface computer message: csa offramp curvature; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of UI_csaOfframpCurvature as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_csaOfframpCurvature` |
| CAN id | 0x298 (664) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 7 |

## Signals of UI_csaOfframpCurvature

Tesla Model Y CAN bus signals in `UI_csaOfframpCurvature`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_csaOfframpCurvC2` | Touchscreen user interface computer: csa offramp curv C2 | 0\|16 | little-endian | signed | 1.0e-06 | 0 | 1/m | -0.032768 to 0.032767 |  | plausible |
| `UI_csaOfframpCurvC3` | Touchscreen user interface computer: csa offramp curv C3 | 16\|16 | little-endian | signed | 4.0e-09 | 0 | 1/m2 | -0.000131072 to 0.000131068 |  | plausible |
| `UI_csaOfframpCurvRange` | Touchscreen user interface computer: csa offramp curv range | 32\|8 | little-endian | unsigned | 2 | 0 | m | 0 to 510 |  | plausible |
| `UI_csaOfframpCurvCounter` | Touchscreen user interface computer: csa offramp curv counter | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_csaOfframpCurvUsingTspline` | Touchscreen user interface computer: csa offramp curv using tspline | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_csaOfframpCurvReserved` | Touchscreen user interface computer: csa offramp curv reserved | 49\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_csaOfframpCurvChecksum` | Touchscreen user interface computer: csa offramp curv checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
