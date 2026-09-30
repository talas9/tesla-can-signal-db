---
layout: default
title: "UI_tripPlanning4 (0x496) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: trip planning4. Ethernet-side message UI_tripPlanning4 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 4 signals (UI_longTermEnergyModelError, UI_longTermRmsSpeedRatio, UI_gradeCorrectedEnergy, UI_gradeCorrectedEnergyLearned). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning4 (0x496) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: trip planning4. This page documents the 4 signals of UI_tripPlanning4 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning4` |
| Ethernet-side id | 0x496 (1174) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of UI_tripPlanning4

Tesla Model Y CAN bus signals in `UI_tripPlanning4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_longTermEnergyModelError` | Touchscreen user interface computer: long term energy model error; raw 128 = signal not available (SNA) | 0\|8 | little-endian | signed | 0.5 | 0 | whpm | -64 to 63.5 | -128 = `SNA`<br>127 = `MAXVAL` | plausible |
| `UI_longTermRmsSpeedRatio` | Touchscreen user interface computer: long term rms speed ratio; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.01 | 0 | 1 | 0 to 2.54 | 254 = `MAXVAL`<br>255 = `SNA` | plausible |
| `UI_gradeCorrectedEnergy` | Touchscreen user interface computer: grade corrected energy; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.68 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |
| `UI_gradeCorrectedEnergyLearned` | Touchscreen user interface computer: grade corrected energy learned; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.68 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
