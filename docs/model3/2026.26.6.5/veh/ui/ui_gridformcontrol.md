---
layout: default
title: "UI_gridFormControl (0x390) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: grid form control. Tesla Model 3 CAN bus message UI_gridFormControl (0x390) of Touchscreen user interface computer, firmware 2026.26.6.5, 3 signals (UI_dischargeTerminationPct, UI_v2lFeatureRequest, UI_powershareRequest). Bit layout, scaling, units and value tables."
---

# UI_gridFormControl (0x390) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: grid form control; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 3 signals of UI_gridFormControl as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_gridFormControl` |
| CAN id | 0x390 (912) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 2 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_gridFormControl

Tesla Model 3 CAN bus signals in `UI_gridFormControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_dischargeTerminationPct` | Reports the minimum State of Energy (SOE) to which the vehicle will discharge for powering outlets, Vehicle to Load (V2L), or Vehicle to Home (V2H). | 0\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `UI_v2lFeatureRequest` | Touchscreen user interface computer: v2l feature request | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_powershareRequest` | Controls the start and stop of powersharing. | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `POWERSHARE_REQUEST_DISABLE`<br>1 = `POWERSHARE_REQUEST_STANDARD_VEHICLE`<br>2 = `POWERSHARE_REQUEST_AUTHENTICATED` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
