---
layout: default
title: "UI_airbagCutoffStatus (0x3D3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: airbag cutoff status. Ethernet-side message UI_airbagCutoffStatus of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (UI_airbagCutoffSwState, UI_warningIndicatorStatus). Bit layout, scaling, units and value tables."
---

# UI_airbagCutoffStatus (0x3D3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: airbag cutoff status. This page documents the 2 signals of UI_airbagCutoffStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_airbagCutoffStatus` |
| Ethernet-side id | 0x3D3 (979) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 1 bytes |
| Cycle time | 500 ms |
| Signals | 2 |

## Signals of UI_airbagCutoffStatus

Tesla Model 3 / Model Y CAN bus signals in `UI_airbagCutoffStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_airbagCutoffSwState` | Reports the front passenger airbag cutoff switch request; raw 2 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASSENGER_AIRBAG_ON`<br>1 = `PASSENGER_AIRBAG_OFF`<br>2 = `SNA` | validated |
| `UI_warningIndicatorStatus` | Touchscreen user interface computer: warning indicator status; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `WARNING_LAMP_OFF`<br>1 = `WARNING_LAMP_ON`<br>3 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
