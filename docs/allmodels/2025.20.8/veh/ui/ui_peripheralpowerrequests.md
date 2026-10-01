---
layout: default
title: "UI_peripheralPowerRequests (0x3B4) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: peripheral power requests. Tesla Model 3 / Model Y CAN bus message UI_peripheralPowerRequests (0x3B4) of Touchscreen user interface computer, firmware 2025.20.8, 1 signals (UI_usbFrontHubPowerStateRequest). Bit layout, scaling, units and value tables."
---

# UI_peripheralPowerRequests (0x3B4) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: peripheral power requests; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 1 signals of UI_peripheralPowerRequests as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_peripheralPowerRequests` |
| CAN id | 0x3B4 (948) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 1 bytes |
| Cycle time | 500 ms |
| Signals | 1 |

## Signals of UI_peripheralPowerRequests

Tesla Model 3 / Model Y CAN bus signals in `UI_peripheralPowerRequests`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_usbFrontHubPowerStateRequest` | Reports the Universal Serial Bus (USB) Hub power request; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `POWER_REQUEST_SNA`<br>1 = `POWER_NO_PREFERENCE`<br>2 = `POWER_ON` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
