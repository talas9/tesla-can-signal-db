---
layout: default
title: "UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: power. Tesla Model 3 / Model Y CAN bus message UI_power (0x3BB) of Touchscreen user interface computer, firmware 2026.26.6.5, 4 signals (UI_powerExpected, UI_powerIdeal, UI_dSocAlertEnable, UI_dSocAlertThreshold). Bit layout, scaling, units and value tables."
---

# UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: power; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 4 signals of UI_power as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_power` |
| CAN id | 0x3BB (955) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of UI_power

Tesla Model 3 / Model Y CAN bus signals in `UI_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_powerExpected` | Touchscreen user interface computer: power expected | 0\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |
| `UI_powerIdeal` | Touchscreen user interface computer: power ideal | 8\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |
| `UI_dSocAlertEnable` | Set when the BMS_a117_SW_Delta_SOC_Weak_Short alert for the BMS should have a functional response | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_dSocAlertThreshold` | Touchscreen user interface computer: d soc alert threshold | 17\|5 | little-endian | unsigned | 0.1 | -3 | % | -3 to 0.1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
