---
layout: default
title: "BMS_chargeInfo (0x472) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: charge info. Tesla Model 3 / Model Y CAN bus message BMS_chargeInfo (0x472) of High-voltage battery management system, firmware 2026.26.6.5, 8 signals (BMS_acChargePowerSample, BMS_voltageRegCurrentTarget, BMS_vehicleChargeDcCurrentLimit, BMS_userChargeCurrentLimitMode and 4 more). Bit layout, scaling, units and value tables."
---

# BMS_chargeInfo (0x472) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: charge info; frame length observed on a vehicle bus. This page documents the 8 signals of BMS_chargeInfo as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_chargeInfo` |
| CAN id | 0x472 (1138) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of BMS_chargeInfo

Tesla Model 3 / Model Y CAN bus signals in `BMS_chargeInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_acChargePowerSample` | High-voltage battery management system: ac charge power sample; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 25 | 255 = `SNA` | validated |
| `BMS_voltageRegCurrentTarget` | DC current target based on voltage regulator | 8\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | validated |
| `BMS_vehicleChargeDcCurrentLimit` | Charge current target after all aggregating all vehicle-side limits, exclude EVSE limits | 20\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | validated |
| `BMS_userChargeCurrentLimitMode` | BMS' user-facing reason for charge being either limited or not limited | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `USR_CHG_LIMIT_NONE`<br>1 = `USR_CHG_LIMIT_EVSE`<br>2 = `USR_CHG_LIMIT_BATT_TEMP_LOW`<br>3 = `USR_CHG_LIMIT_HIGH_SOC`<br>4 = `USR_CHG_LIMIT_EVSE_RELOCATION_RECOMMENDED` | validated |
| `BMS_chargeCurrentLimitMode` | BMS charging current limiting factor | 35\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CHG_LIMIT_NONE`<br>1 = `CHG_LIMIT_EVSE`<br>2 = `CHG_LIMIT_PCS`<br>3 = `CHG_LIMIT_CP`<br>4 = `CHG_LIMIT_BRICK_TEMP_OPTIMAL_CELL_PROFILE`<br>5 = `CHG_LIMIT_BRICK_TEMP_TOO_HOT`<br>6 = `CHG_LIMIT_BRICK_TEMP_TOO_COLD`<br>7 = `CHG_LIMIT_BRICK_VOLTAGE_REG`<br>8 = `CHG_LIMIT_LEAKY_BUCKET`<br>9 = `CHG_LIMIT_TETHERING`<br>10 = `CHG_LIMIT_CONFIG`<br>11 = `CHG_LIMIT_HV_CHAIN`<br>12 = `CHG_LIMIT_HVAC_COOLING`<br>13 = `CHG_LIMIT_RAMP_UP_PHASE`<br>14 = `CHG_LIMIT_EVSE_IMPLICIT`<br>15 = `CHG_LIMIT_PCS_IMPLICIT`<br>16 = `CHG_LIMIT_CAC_IMBALANCE`<br>17 = `CHG_LIMIT_MISSING_CELL`<br>18 = `CHG_LIMIT_LIMP_MODE`<br>19 = `CHG_LIMIT_NEAR_HWOT_LIMIT`<br>20 = `CHG_LIMIT_RIPPLE_HEAT_ACTIVE` | validated |
| `BMS_timeToFinishHeatForCharge` | High-voltage battery management system: time to finish heat for charge; raw 127 = signal not available (SNA) | 40\|7 | little-endian | unsigned | 5 | 0 | min | 0 to 600 | 126 = `CALCULATING`<br>127 = `SNA` | validated |
| `BMS_timeToTripPlanChargingTarget` | High-voltage battery management system: time to trip plan charging target; raw 2047 = signal not available (SNA) | 48\|11 | little-endian | unsigned | 1 | 0 | min | 0 to 2046 | 2047 = `SNA` | validated |
| `BMS_useChargeTimeEstimate` | High-voltage battery management system: use charge time estimate | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
