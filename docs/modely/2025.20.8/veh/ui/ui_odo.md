---
layout: default
title: "UI_odo (0x5F3) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: odo. Tesla Model Y CAN bus message UI_odo (0x5F3) of Touchscreen user interface computer, firmware 2025.20.8, 1 signals (UI_odometer). Bit layout, scaling, units and value tables."
---

# UI_odo (0x5F3) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: odo; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 1 signals of UI_odo as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_odo` |
| CAN id | 0x5F3 (1523) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of UI_odo

Tesla Model Y CAN bus signals in `UI_odo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_odometer` | Odometer; raw 16777215 = signal not available (SNA) | 0\|24 | little-endian | unsigned | 0.1 | 0 | km | 0 to 1677721.4 | 16777215 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
