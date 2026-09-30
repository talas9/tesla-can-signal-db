---
layout: default
title: "UI_dynamicTriggersCampaignFired (0x7B3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: dynamic triggers campaign fired. Tesla Model 3 / Model Y CAN bus message UI_dynamicTriggersCampaignFired (0x7B3) of Touchscreen user interface computer, firmware 2026.26.6.5, 1 signals (UI_campaignFired). Bit layout, scaling, units and value tables."
---

# UI_dynamicTriggersCampaignFired (0x7B3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: dynamic triggers campaign fired; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UI_dynamicTriggersCampaignFired as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_dynamicTriggersCampaignFired` |
| CAN id | 0x7B3 (1971) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 1 |

## Signals of UI_dynamicTriggersCampaignFired

Tesla Model 3 / Model Y CAN bus signals in `UI_dynamicTriggersCampaignFired`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_campaignFired` | Touchscreen user interface computer: campaign fired | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
