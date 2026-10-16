---
layout: default
title: "UI_range (0x33A) — Touchscreen user interface computer, Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: range. Tesla Model Y (2025+ / Juniper; community mapping) CAN bus message UI_range (0x33A) of Touchscreen user interface computer, firmware 2025.20.8, 3 signals (UI_ratedRange, UI_soe, UI_uSoe). Bit layout, scaling, units and value tables."
---

# UI_range (0x33A) — Touchscreen user interface computer, Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH CAN

Touchscreen user interface computer message: range; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 3 signals of UI_range as defined for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_range` |
| CAN id | 0x33A (826) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y (2025+ / Juniper; community mapping) |
| API name / codename | `Bayberry` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_range

Tesla Model Y (2025+ / Juniper; community mapping) CAN bus signals in `UI_range`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ratedRange` | Rated range in miles | 0\|10 | little-endian | unsigned | 1 | 0 | mi | 0 to 1023 |  | plausible |
| `UI_soe` | State of energy | 20\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `UI_uSoe` | Usable state of energy | 27\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |

## Download the DBC file

- [Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH DBC file](../../../../../dbc/Bayberry/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Bayberry/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
