---
layout: default
title: "UI_tripPlanning3 (0x495) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: trip planning3. Ethernet-side message UI_tripPlanning3 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 4 signals (UI_predictedEnergy, UI_predictedEnergyLearned, UI_hindsightEnergy, UI_hindsightEnergyLearned). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning3 (0x495) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: trip planning3. This page documents the 4 signals of UI_tripPlanning3 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning3` |
| Ethernet-side id | 0x495 (1173) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of UI_tripPlanning3

Tesla Model Y CAN bus signals in `UI_tripPlanning3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_predictedEnergy` | initially predicted energy in kWh for current location along navigation route; raw 32768 = signal not available (SNA) | 0\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.67 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |
| `UI_predictedEnergyLearned` | Touchscreen user interface computer: predicted energy learned; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.68 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |
| `UI_hindsightEnergy` | hindsight energy, the model predicted energy based on measured speed and acceleration for the current location along navigation route; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.67 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |
| `UI_hindsightEnergyLearned` | Touchscreen user interface computer: hindsight energy learned; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.68 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
