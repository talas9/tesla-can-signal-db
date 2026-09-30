---
layout: default
title: "UI_range (0x33A) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: range. Tesla Model 3 CAN bus message UI_range (0x33A) of Touchscreen user interface computer, firmware 2025.20.8, 6 signals (UI_ratedRange, UI_whpm, UI_soe, UI_uSoe and 2 more). Bit layout, scaling, units and value tables."
---

# UI_range (0x33A) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN

Touchscreen user interface computer message: range; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 6 signals of UI_range as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_range` |
| CAN id | 0x33A (826) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of UI_range

Tesla Model 3 CAN bus signals in `UI_range`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ratedRange` | Rated range in miles | 0\|10 | little-endian | unsigned | 1 | 0 | mi | 0 to 1023 |  | validated |
| `UI_whpm` | Touchscreen user interface computer: whpm | 10\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | plausible |
| `UI_soe` | State of energy | 20\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `UI_uSoe` | Usable state of energy | 27\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `UI_softPackLimitPct` | Touchscreen user interface computer: soft pack limit pct | 34\|15 | little-endian | unsigned | 0.003051851 | 0 | % | 0 to 100.000001717 |  | plausible |
| `UI_targetFullPackEnergy` | Touchscreen user interface computer: target full pack energy | 49\|15 | little-endian | unsigned | 0.006103702 | 0 | kWh | 0 to 200.000003434 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
