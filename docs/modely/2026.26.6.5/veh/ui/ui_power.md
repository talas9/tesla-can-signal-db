---
layout: default
title: "UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: power. Tesla Model Y CAN bus message UI_power (0x3BB) of Touchscreen user interface computer, firmware 2026.26.6.5, 2 signals (UI_powerExpected, UI_powerIdeal). Bit layout, scaling, units and value tables."
---

# UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: power; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 2 signals of UI_power as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_power` |
| CAN id | 0x3BB (955) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 2 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_power

Tesla Model Y CAN bus signals in `UI_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_powerExpected` | Touchscreen user interface computer: power expected | 0\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |
| `UI_powerIdeal` | Touchscreen user interface computer: power ideal | 8\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
