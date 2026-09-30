---
layout: default
title: "UI_summonGoal (0x3DC) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: summon goal. Tesla Model 3 CAN bus message UI_summonGoal (0x3DC) of Touchscreen user interface computer, firmware 2026.26.6.5, 3 signals (UI_goalLatitude, UI_goalLongitude, UI_goalOrientation). Bit layout, scaling, units and value tables."
---

# UI_summonGoal (0x3DC) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN

Touchscreen user interface computer message: summon goal; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of UI_summonGoal as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_summonGoal` |
| CAN id | 0x3DC (988) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_summonGoal

Tesla Model 3 CAN bus signals in `UI_summonGoal`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_goalLatitude` | Touchscreen user interface computer: goal latitude | 0\|28 | little-endian | signed | 1.0e-06 | 0 | deg | -134.217728 to 134.217727 |  | plausible |
| `UI_goalLongitude` | Touchscreen user interface computer: goal longitude | 28\|29 | little-endian | signed | 1.0e-06 | 0 | deg | -268.435456 to 268.435455 |  | plausible |
| `UI_goalOrientation` | Touchscreen user interface computer: goal orientation | 57\|7 | little-endian | unsigned | 2.8125 | 0 | deg | 0 to 357.1875 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
