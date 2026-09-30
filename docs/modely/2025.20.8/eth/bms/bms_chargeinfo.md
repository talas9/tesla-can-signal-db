---
layout: default
title: "BMS_chargeInfo (0x472) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: charge info. Ethernet-side message BMS_chargeInfo of High-voltage battery management system for Tesla Model Y firmware 2025.20.8, 6 signals (BMS_cellChargeDcCurrentLimit, BMS_voltageRegCurrentTarget, BMS_vehicleChargeDcCurrentLimit, BMS_chargeCurrentLimitMode and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_chargeInfo (0x472) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH

High-voltage battery management system message: charge info. This page documents the 6 signals of BMS_chargeInfo as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_chargeInfo` |
| Ethernet-side id | 0x472 (1138) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of BMS_chargeInfo

Tesla Model Y CAN bus signals in `BMS_chargeInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_cellChargeDcCurrentLimit` | DC current target based on cell voltage &amp; temp tables | 0\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | plausible |
| `BMS_voltageRegCurrentTarget` | DC current target based on voltage regulator | 12\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | plausible |
| `BMS_vehicleChargeDcCurrentLimit` | Charge current target after all aggregating all vehicle-side limits, exclude EVSE limits | 24\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | plausible |
| `BMS_chargeCurrentLimitMode` | BMS charging current limiting factor | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CHG_LIMIT_NONE`<br>1 = `CHG_LIMIT_EVSE`<br>2 = `CHG_LIMIT_PCS`<br>3 = `CHG_LIMIT_CP`<br>4 = `CHG_LIMIT_BRICK_TEMP_OPTIMAL_CELL_PROFILE`<br>5 = `CHG_LIMIT_BRICK_TEMP_TOO_HOT`<br>6 = `CHG_LIMIT_BRICK_TEMP_TOO_COLD`<br>7 = `CHG_LIMIT_BRICK_VOLTAGE_REG`<br>8 = `CHG_LIMIT_LEAKY_BUCKET`<br>9 = `CHG_LIMIT_TETHERING`<br>10 = `CHG_LIMIT_CONFIG`<br>11 = `CHG_LIMIT_HV_CHAIN`<br>12 = `CHG_LIMIT_HVAC_COOLING`<br>13 = `CHG_LIMIT_RAMP_UP_PHASE`<br>14 = `CHG_LIMIT_EVSE_IMPLICIT`<br>15 = `CHG_LIMIT_PCS_IMPLICIT`<br>16 = `CHG_LIMIT_CAC_IMBALANCE`<br>17 = `CHG_LIMIT_MISSING_CELL`<br>18 = `CHG_LIMIT_LIMP_MODE`<br>19 = `CHG_LIMIT_NEAR_HWOT_LIMIT`<br>20 = `CHG_LIMIT_RIPPLE_HEAT_ACTIVE` | plausible |
| `BMS_timeToFinishHeatForCharge` | High-voltage battery management system: time to finish heat for charge; raw 127 = signal not available (SNA) | 45\|7 | little-endian | unsigned | 5 | 0 | min | 0 to 600 | 126 = `CALCULATING`<br>127 = `SNA` | plausible |
| `BMS_diNodeModelTemp` | High-voltage battery management system: di node model temp; raw 2047 = signal not available (SNA) | 52\|11 | little-endian | unsigned | 0.1 | -50 | degC | -50 to 154.6 | 2047 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
