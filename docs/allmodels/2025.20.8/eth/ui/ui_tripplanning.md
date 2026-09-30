---
layout: default
title: "UI_tripPlanning (0x82) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: trip planning. Ethernet-side message UI_tripPlanning of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 9 signals (UI_tripPlanningActive, UI_navToSupercharger, UI_navFastchargerType, UI_battPreconditionOnNavState and 5 more). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning (0x82) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: trip planning. This page documents the 9 signals of UI_tripPlanning as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning` |
| Ethernet-side id | 0x82 (130) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of UI_tripPlanning

Tesla Model 3 / Model Y CAN bus signals in `UI_tripPlanning`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_tripPlanningActive` | Indicates that there is active route in navigation with a valid energy at destination prediction. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_navToSupercharger` | Navigation destination is a supercharger | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_navFastchargerType` | when navigation is turned on, this enum identifies the type of fastcharger the car is navigating to based on the rated power from sc_locations | 2\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LOW_POWER`<br>2 = `V2`<br>3 = `V3`<br>4 = `V4` | validated |
| `UI_battPreconditionOnNavState` | Indicates to battery and thermal systems whether the battery should be actively heated, passively heated, actively cooled, or passively cooled | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASSIVE_HEAT`<br>1 = `ACTIVE_HEAT`<br>2 = `PASSIVE_COOL`<br>3 = `ACTIVE_COOL` | validated |
| `UI_requestActiveBatteryHeating` | Flag to request BMS enable active battery heating | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_battPreconditionOnNavPowerReq` | The preconditioning power that Trip Planner is requesting from the thermal system to use for battery preconditioning (cooling or heating); raw 127 = signal not available (SNA) | 8\|8 | little-endian | signed | 125 | 0 | W | -16000 to 15750 | -126 = `MIN`<br>126 = `MAX`<br>127 = `SNA` | validated |
| `UI_battPreconditionOnNavTargetT` | The pack temperature that Trip Planner is targeting upon arriving to a fast charger; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.25 | 0 | degC | 0 to 63.5 | 0 = `MIN`<br>254 = `MAX`<br>255 = `SNA` | validated |
| `UI_ambientTempAtDestination` | Touchscreen user interface computer: ambient temp at destination; raw 128 = signal not available (SNA) | 32\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 | -128 = `SNA` | plausible |
| `UI_energyAtDestination` | expected energy at destination in kWh for current navigation route; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | kWh | -327.67 to 327.67 | -32768 = `SNA`<br>-32767 = `TRIP_TOO_LONG` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
