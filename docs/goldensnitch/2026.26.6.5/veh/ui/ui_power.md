---
layout: default
title: "UI_power (0x3BB) — Touchscreen user interface computer, Tesla Unidentified vehicle 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: power. Tesla Unidentified vehicle CAN bus message UI_power (0x3BB) of Touchscreen user interface computer, firmware 2026.26.6.5, 1 signals (UI_dSocAlertEnable). Bit layout, scaling, units and value tables."
---

# UI_power (0x3BB) — Touchscreen user interface computer, Tesla Unidentified vehicle 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: power; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 1 signals of UI_power as defined for Tesla Unidentified vehicle firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_power` |
| CAN id | 0x3BB (955) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Unidentified vehicle |
| API name / codename | `GoldenSnitch` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of UI_power

Tesla Unidentified vehicle CAN bus signals in `UI_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_dSocAlertEnable` | Set when the BMS_a117_SW_Delta_SOC_Weak_Short alert for the BMS should have a functional response | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Unidentified vehicle 2026.26.6.5 VEH DBC file](../../../../../dbc/GoldenSnitch/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/GoldenSnitch/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
