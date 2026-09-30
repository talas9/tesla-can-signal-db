---
layout: default
title: "UI_phoneLocationStatus (0x3DB) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: phone location status. Tesla Model Y CAN bus message UI_phoneLocationStatus (0x3DB) of Touchscreen user interface computer, firmware 2026.26.6.5, 3 signals (UI_phoneLatitude, UI_phoneLongitude, UI_phoneGpsAccuracy). Bit layout, scaling, units and value tables."
---

# UI_phoneLocationStatus (0x3DB) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: phone location status; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of UI_phoneLocationStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_phoneLocationStatus` |
| CAN id | 0x3DB (987) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_phoneLocationStatus

Tesla Model Y CAN bus signals in `UI_phoneLocationStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_phoneLatitude` | Touchscreen user interface computer: phone latitude | 0\|28 | little-endian | signed | 1.0e-06 | 0 | deg | -134.217728 to 134.217727 |  | plausible |
| `UI_phoneLongitude` | Touchscreen user interface computer: phone longitude | 28\|29 | little-endian | signed | 1.0e-06 | 0 | deg | -268.435456 to 268.435455 |  | plausible |
| `UI_phoneGpsAccuracy` | Touchscreen user interface computer: phone gps accuracy; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 0.5 | 0 | m | 0 to 63 | 127 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
