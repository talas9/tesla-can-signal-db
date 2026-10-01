---
layout: default
title: "BMS_powerAvailable (0x252) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH"
description: "High-voltage battery management system message: power available. Ethernet-side message BMS_powerAvailable of High-voltage battery management system for Tesla Model 3 firmware 2025.20.8, 6 signals (BMS_maxRegenPower, BMS_maxDischargePower, BMS_maxStationaryHeatPower, BMS_powerLimitsState and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_powerAvailable (0x252) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH

High-voltage battery management system message: power available. This page documents the 6 signals of BMS_powerAvailable as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_powerAvailable` |
| Ethernet-side id | 0x252 (594) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of BMS_powerAvailable

Tesla Model 3 CAN bus signals in `BMS_powerAvailable`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_maxRegenPower` | Calculated max regen power | 0\|16 | little-endian | unsigned | 0.01 | 0 | kW | 0 to 655.35 |  | plausible |
| `BMS_maxDischargePower` | Calculated max discharge power possible based on max discharge current and sum of loaded voltages | 16\|16 | little-endian | unsigned | 0.013 | 0 | kW | 0 to 850 |  | plausible |
| `BMS_maxStationaryHeatPower` | Maximum heating power the DI can produce when in stationary heating mode | 32\|10 | little-endian | unsigned | 0.01 | 0 | kW | 0 to 10.23 |  | plausible |
| `BMS_powerLimitsState` | High-voltage battery management system: power limits state | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `POWER_NOT_CALCULATED_FOR_DRIVE`<br>1 = `POWER_CALCULATED_FOR_DRIVE` | plausible |
| `BMS_notEnoughPowerForHeatPump` | Flag indicating the min pack power is lower than specified threshold to support heating with the heat pump | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_instantChargePowerCapability` | Indicates the instantaneous charge power capability of the high voltage battery; raw 65535 = signal not available (SNA) | 48\|16 | little-endian | unsigned | 0.05 | 0 | kW | 0 to 3276.7 | 65535 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
