---
layout: default
title: "BMS_powerAvailable (0x252) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: power available. Tesla Model 3 / Model Y CAN bus message BMS_powerAvailable (0x252) of High-voltage battery management system, firmware 2026.26.6.5, 6 signals (BMS_maxRegenPower, BMS_maxDischargePower, BMS_maxStationaryHeatPower, BMS_powerLimitsState and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_powerAvailable (0x252) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: power available; frame length observed on a vehicle bus. This page documents the 6 signals of BMS_powerAvailable as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_powerAvailable` |
| CAN id | 0x252 (594) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of BMS_powerAvailable

Tesla Model 3 / Model Y CAN bus signals in `BMS_powerAvailable`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_maxRegenPower` | Calculated max regen power | 0\|16 | little-endian | unsigned | 0.01 | 0 | kW | 0 to 655.35 |  | validated |
| `BMS_maxDischargePower` | Calculated max discharge power possible based on max discharge current and sum of loaded voltages | 16\|16 | little-endian | unsigned | 0.013 | 0 | kW | 0 to 850 |  | validated |
| `BMS_maxStationaryHeatPower` | Maximum heating power the DI can produce when in stationary heating mode | 32\|10 | little-endian | unsigned | 0.01 | 0 | kW | 0 to 10.23 |  | validated |
| `BMS_powerLimitsState` | High-voltage battery management system: power limits state | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `POWER_NOT_CALCULATED_FOR_DRIVE`<br>1 = `POWER_CALCULATED_FOR_DRIVE` | validated |
| `BMS_totalHvPowerBudget` | Maximum total power that the High Voltage (HV) battery and Electric Vehicle Supply Equipment (EVSE) (if present) can safely produce | 43\|9 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 51.1 |  | validated |
| `BMS_notEnoughPowerForHeatPump` | Flag indicating the min pack power is lower than specified threshold to support heating with the heat pump | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
