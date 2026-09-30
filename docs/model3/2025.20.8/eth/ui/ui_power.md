---
layout: default
title: "UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH"
description: "Touchscreen user interface computer message: power. Ethernet-side message UI_power of Touchscreen user interface computer for Tesla Model 3 firmware 2025.20.8, 2 signals (UI_powerExpected, UI_powerIdeal). Bit layout, scaling, units and value tables."
---

# UI_power (0x3BB) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH

Touchscreen user interface computer message: power. This page documents the 2 signals of UI_power as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_power` |
| Ethernet-side id | 0x3BB (955) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 2 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_power

Tesla Model 3 CAN bus signals in `UI_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_powerExpected` | Touchscreen user interface computer: power expected | 0\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |
| `UI_powerIdeal` | Touchscreen user interface computer: power ideal | 8\|8 | little-endian | unsigned | 1 | 0 | kW | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
