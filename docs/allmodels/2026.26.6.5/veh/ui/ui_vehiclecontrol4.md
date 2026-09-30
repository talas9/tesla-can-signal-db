---
layout: default
title: "UI_vehicleControl4 (0x4A9) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: vehicle control4. Tesla Model 3 / Model Y CAN bus message UI_vehicleControl4 (0x4A9) of Touchscreen user interface computer, firmware 2026.26.6.5, 7 signals (UI_firstRowLeftDomeLightRequest, UI_firstRowRightDomeLightRequest, UI_secondRowLeftDomeLightRequest, UI_secondRowCenterDomeLightRequest and 3 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleControl4 (0x4A9) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: vehicle control4; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of UI_vehicleControl4 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleControl4` |
| CAN id | 0x4A9 (1193) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 1 bytes |
| Cycle time | 500 ms |
| Signals | 7 |

## Signals of UI_vehicleControl4

Tesla Model 3 / Model Y CAN bus signals in `UI_vehicleControl4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_firstRowLeftDomeLightRequest` | Monitors the dome light switch for first row left side | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_firstRowRightDomeLightRequest` | Monitors the dome light switch for first row right side | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_secondRowLeftDomeLightRequest` | Monitors the dome light switch for second row left side | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_secondRowCenterDomeLightRequest` | Monitors the dome light switch for second row center side | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_secondRowRightDomeLightRequest` | Monitors the dome light switch for second row right side | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_thirdRowLeftDomeLightRequest` | Monitors the dome light switch for third row left side | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |
| `UI_thirdRowRightDomeLightRequest` | Monitors the dome light switch for third row right side | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOME_LIGHT_REQUEST_NONE`<br>1 = `DOME_LIGHT_REQUEST_ACTIVE` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
