---
layout: default
title: "UI_tpmsRCPsetting (0x3BC) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: tpms RC psetting. Tesla Model 3 / Model Y CAN bus message UI_tpmsRCPsetting (0x3BC) of Touchscreen user interface computer, firmware 2026.26.6.5, 3 signals (UI_sendCalibrateTireRequest, UI_setRCPFront, UI_setRCPRear). Bit layout, scaling, units and value tables."
---

# UI_tpmsRCPsetting (0x3BC) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: tpms RC psetting; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 3 signals of UI_tpmsRCPsetting as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tpmsRCPsetting` |
| CAN id | 0x3BC (956) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_tpmsRCPsetting

Tesla Model 3 / Model Y CAN bus signals in `UI_tpmsRCPsetting`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_sendCalibrateTireRequest` | Reports UI requests for PMDI to start the tire pressure calibration routine. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_setRCPFront` | Touchscreen user interface computer: set RCP front | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `UI_setRCPRear` | Touchscreen user interface computer: set RCP rear | 24\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
