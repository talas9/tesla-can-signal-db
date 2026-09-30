---
layout: default
title: "UI_driverProfileRecall2 (0x28B) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: driver profile recall2. Tesla Model 3 / Model Y CAN bus message UI_driverProfileRecall2 (0x28B) of Touchscreen user interface computer, firmware 2025.20.8, 5 signals (UI_driverProfileLinkedKeySHA1, UI_driverProfileIndex, UI_driverProfileSelectionType, UI_driverProfilePositionAdjusted and 1 more). Bit layout, scaling, units and value tables."
---

# UI_driverProfileRecall2 (0x28B) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: driver profile recall2; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of UI_driverProfileRecall2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverProfileRecall2` |
| CAN id | 0x28B (651) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 5 bytes |
| Cycle time | 500 ms |
| Signals | 5 |

## Signals of UI_driverProfileRecall2

Tesla Model 3 / Model Y CAN bus signals in `UI_driverProfileRecall2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_driverProfileLinkedKeySHA1` | Touchscreen user interface computer: driver profile linked key SHA1; raw 4294967295 = signal not available (SNA) | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967294 | 4294967295 = `SNA` | plausible |
| `UI_driverProfileIndex` | Tracks manual driver profile selection. Shows the linked phonekey / key card / key fob or profile index if not linked | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `UI_driverProfileSelectionType` | Tracks manual driver profile selection. Shows the linked phonekey / key card / key fob or profile index if not linked | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER_PROFILE_SELECTION_TYPE_MANUAL`<br>1 = `DRIVER_PROFILE_SELECTION_TYPE_AUTOMATIC_RESTORE`<br>2 = `DRIVER_PROFILE_SELECTION_TYPE_AUTOMATIC_NO_OP`<br>3 = `DRIVER_PROFILE_SELECTION_TYPE_NONE` | validated |
| `UI_driverProfilePositionAdjusted` | Tracks adjustments to driver profile. Sets when a profile position has been adjusted from what was saved | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_activeKeyRequested` | Tracks manual driver profile selection. Shows the linked phonekey / key card / key fob or profile index if not linked | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
