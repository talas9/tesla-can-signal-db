---
layout: default
title: "UI_radarMapData (0x2BA) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: radar map data. Tesla Model 3 / Model Y CAN bus message UI_radarMapData (0x2BA) of Touchscreen user interface computer, firmware 2025.20.8, 6 signals (UI_radarTargetDx, UI_radarTargetDxEnd, UI_radarTargetTrustMap, UI_radarEnableBraking and 2 more). Bit layout, scaling, units and value tables."
---

# UI_radarMapData (0x2BA) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Touchscreen user interface computer message: radar map data; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of UI_radarMapData as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_radarMapData` |
| CAN id | 0x2BA (698) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 6 |

## Signals of UI_radarMapData

Tesla Model 3 / Model Y CAN bus signals in `UI_radarMapData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_radarTargetDx` | Touchscreen user interface computer: radar target dx | 0\|8 | little-endian | unsigned | 1 | -95 | m | -95 to 160 | 255 = `NO_OBJECT` | plausible |
| `UI_radarTargetDxEnd` | Touchscreen user interface computer: radar target dx end | 8\|8 | little-endian | unsigned | 1 | 0 | m | 0 to 255 | 255 = `NO_OBJECT` | plausible |
| `UI_radarTargetTrustMap` | Touchscreen user interface computer: radar target trust map | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_radarEnableBraking` | Touchscreen user interface computer: radar enable braking | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_radarMapDataCounter` | Touchscreen user interface computer: radar map data counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_radarMapDataChecksum` | Touchscreen user interface computer: radar map data checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
