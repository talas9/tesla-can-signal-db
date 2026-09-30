---
layout: default
title: "UI_tpmsRCPsetting (0x3B8) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: tpms RC psetting. Ethernet-side message UI_tpmsRCPsetting of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (UI_setRCPFront, UI_setRCPRear). Bit layout, scaling, units and value tables."
---

# UI_tpmsRCPsetting (0x3B8) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: tpms RC psetting. This page documents the 2 signals of UI_tpmsRCPsetting as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tpmsRCPsetting` |
| Ethernet-side id | 0x3B8 (952) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_tpmsRCPsetting

Tesla Model 3 / Model Y CAN bus signals in `UI_tpmsRCPsetting`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_setRCPFront` | Touchscreen user interface computer: set RCP front | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `UI_setRCPRear` | Touchscreen user interface computer: set RCP rear | 24\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
