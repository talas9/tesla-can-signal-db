---
layout: default
title: "UI_chargeRequest (0x333) — Touchscreen user interface computer, Tesla Unidentified vehicle 2025.20.8 ETH"
description: "Touchscreen user interface computer message: charge request. Ethernet-side message UI_chargeRequest of Touchscreen user interface computer for Tesla Unidentified vehicle firmware 2025.20.8, 1 signals (UI_dSocAlertEnable). Bit layout, scaling, units and value tables."
---

# UI_chargeRequest (0x333) — Touchscreen user interface computer, Tesla Unidentified vehicle 2025.20.8 ETH

Touchscreen user interface computer message: charge request. This page documents the 1 signals of UI_chargeRequest as defined for Tesla Unidentified vehicle firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_chargeRequest` |
| Ethernet-side id | 0x333 (819) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Unidentified vehicle |
| API name / codename | `GoldenSnitch` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 5 bytes |
| Cycle time | 500 ms |
| Signals | 1 |

## Signals of UI_chargeRequest

Tesla Unidentified vehicle CAN bus signals in `UI_chargeRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_dSocAlertEnable` | Set when the BMS_a117_SW_Delta_SOC_Weak_Short alert for the BMS should have a functional response | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Unidentified vehicle 2025.20.8 ETH DBC file](../../../../../dbc/GoldenSnitch/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/GoldenSnitch/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
