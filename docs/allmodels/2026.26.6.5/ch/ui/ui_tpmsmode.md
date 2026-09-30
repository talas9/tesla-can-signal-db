---
layout: default
title: "UI_tpmsMode (0x358) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: tpms mode. Tesla Model 3 / Model Y CAN bus message UI_tpmsMode (0x358) of Touchscreen user interface computer, firmware 2026.26.6.5, 4 signals (UI_TPMSMode, UI_TPMSLearnIDMode, UI_sizeOfWheelSelect, UI_sizeOfReqCANAutoLearn). Bit layout, scaling, units and value tables."
---

# UI_tpmsMode (0x358) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: tpms mode; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of UI_tpmsMode as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tpmsMode` |
| CAN id | 0x358 (856) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 4 bytes |
| Cycle time | not cyclic or not known |
| Signals | 4 |

## Signals of UI_tpmsMode

Tesla Model 3 / Model Y CAN bus signals in `UI_tpmsMode`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_TPMSMode` | Touchscreen user interface computer: TPMS mode | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNUSED_MODE`<br>1 = `NORMAL_MODE`<br>2 = `PERFORMANCE_MODE` | plausible |
| `UI_TPMSLearnIDMode` | Touchscreen user interface computer: TPMS learn ID mode | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ID_LEARN_FUNCTION`<br>1 = `AUTO_LEARN_ACTIVE_BY_MANUAL`<br>2 = `AUTO_LOCATION_ACTIVE_BY_MANUAL`<br>3 = `AUTO_LEARN_ACTIVE_AFTER_PWR`<br>4 = `AUTO_LOCATION_ACTIVE_AFTER_PWR` | plausible |
| `UI_sizeOfWheelSelect` | Touchscreen user interface computer: size of wheel select | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNUSED`<br>1 = `18_INCH_WHEEL`<br>2 = `19_INCH_WHEEL` | plausible |
| `UI_sizeOfReqCANAutoLearn` | Touchscreen user interface computer: size of req CAN auto learn | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
