---
layout: default
title: "UI_powerEstimates (0x33B) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: power estimates. Tesla Model 3 CAN bus message UI_powerEstimates (0x33B) of Touchscreen user interface computer, firmware 2025.20.8, 4 signals (UI_idlePowerConsumption, UI_chargeTimeUntilTerminationPct, UI_isTripChargingActive, UI_chargeTimeUntilReadyToDepart). Bit layout, scaling, units and value tables."
---

# UI_powerEstimates (0x33B) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 VEH CAN

Touchscreen user interface computer message: power estimates; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 4 signals of UI_powerEstimates as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_powerEstimates` |
| CAN id | 0x33B (827) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of UI_powerEstimates

Tesla Model 3 CAN bus signals in `UI_powerEstimates`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_idlePowerConsumption` | Power consumption when idle | 0\|16 | little-endian | unsigned | 0.001 | 0 | kW | 0 to 50 |  | plausible |
| `UI_chargeTimeUntilTerminationPct` | Charge time minutes until reached uSoe target; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 1 | 0 | min | 0 to 2046 | 1440 = `MAXVAL`<br>2047 = `SNA` | plausible |
| `UI_isTripChargingActive` | Touchscreen user interface computer: is trip charging active | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_chargeTimeUntilReadyToDepart` | Charge time minutes until enough energy to depart for rest of trip; raw 2047 = signal not available (SNA) | 32\|11 | little-endian | unsigned | 1 | 0 | min | 0 to 2046 | 1440 = `MAXVAL`<br>2047 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
