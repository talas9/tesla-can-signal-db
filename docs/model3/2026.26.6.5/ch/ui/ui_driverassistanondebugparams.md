---
layout: default
title: "UI_driverAssistAnonDebugParams (0x448) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: driver assist anon debug params. Tesla Model 3 CAN bus message UI_driverAssistAnonDebugParams (0x448) of Touchscreen user interface computer, firmware 2026.26.6.5, 12 signals (UI_anonDebugParam1, UI_anonDebugFlag1, UI_anonDebugParam2, UI_anonDebugFlag2 and 8 more). Bit layout, scaling, units and value tables."
---

# UI_driverAssistAnonDebugParams (0x448) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN

Touchscreen user interface computer message: driver assist anon debug params; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of UI_driverAssistAnonDebugParams as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverAssistAnonDebugParams` |
| CAN id | 0x448 (1096) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 12 |

## Signals of UI_driverAssistAnonDebugParams

Tesla Model 3 CAN bus signals in `UI_driverAssistAnonDebugParams`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_anonDebugParam1` | Touchscreen user interface computer: anon debug param1 | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugFlag1` | Touchscreen user interface computer: anon debug flag1 | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_anonDebugParam2` | Touchscreen user interface computer: anon debug param2 | 8\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugFlag2` | Touchscreen user interface computer: anon debug flag2 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_anonDebugParam3` | Touchscreen user interface computer: anon debug param3 | 16\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugFlag3` | Touchscreen user interface computer: anon debug flag3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_anonDebugParam4` | Touchscreen user interface computer: anon debug param4 | 24\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugFlag4` | Touchscreen user interface computer: anon debug flag4 | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_anonDebugParam5` | Touchscreen user interface computer: anon debug param5 | 32\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugParam6` | Touchscreen user interface computer: anon debug param6 | 40\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_anonDebugParam7` | Touchscreen user interface computer: anon debug param7 | 48\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `UI_visionSpeedSlider` | Touchscreen user interface computer: vision speed slider | 56\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
