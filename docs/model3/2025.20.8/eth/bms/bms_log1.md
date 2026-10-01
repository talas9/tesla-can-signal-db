---
layout: default
title: "BMS_log1 (0x374) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH"
description: "High-voltage battery management system message: log1. Ethernet-side message BMS_log1 of High-voltage battery management system for Tesla Model 3 firmware 2025.20.8, 19 signals (BMS_log1MuxId, BMS_hvChargeStatus, BMS_extDcPrechargeVoltageLimit, BMS_dcChargeCurrentRequest and 15 more). Bit layout, scaling, units and value tables."
---

# BMS_log1 (0x374) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH

High-voltage battery management system message: log1. This page documents the 19 signals of BMS_log1 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_log1` |
| Ethernet-side id | 0x374 (884) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 19 |

## Signals of BMS_log1

Tesla Model 3 CAN bus signals in `BMS_log1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_log1MuxId` | selector | High-voltage battery management system: log1 mux id | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `CPU_USAGE1`<br>1 = `CPU_USAGE2`<br>2 = `CPU_USAGE3`<br>3 = `STATES_AND_BOOLS`<br>4 = `POS_CTR_HEALTH_1`<br>5 = `POS_CTR_HEALTH_2`<br>6 = `NEG_CTR_HEALTH_1`<br>7 = `NEG_CTR_HEALTH_2`<br>8 = `CHARGE_INTERFACE_1`<br>9 = `CHARGE_INTERFACE_2`<br>10 = `BANDOLIER_MODEL_PACK_TEMPS`<br>11 = `BANDOLIER_MODEL_THERMISTOR_TEMPS_1`<br>12 = `BANDOLIER_MODEL_THERMISTOR_TEMPS_2`<br>13 = `CHARGE_TERMINATION`<br>14 = `CHARGE_REGULATION`<br>15 = `SOC_BY_DELTA_V_1`<br>16 = `SOC_BY_DELTA_V_2`<br>17 = `IMPEDANCE_DEVIATION_1`<br>18 = `IMPEDANCE_DEVIATION_2`<br>19 = `PACK_DATA`<br>20 = `CHARGE_ENERGY_1`<br>21 = `CHARGE_ENERGY_2`<br>22 = `CHARGE_ENERGY_3`<br>23 = `CHARGE_ENERGY_4`<br>24 = `CHARGE_LIMIT_1`<br>25 = `CHARGE_LIMIT_2`<br>26 = `SLEEP_CURRENT_1`<br>27 = `SLEEP_CURRENT_2` | plausible |
| `BMS_hvChargeStatus` | page 8 | High-voltage battery management system: hv charge status | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CHARGE_STANDBY`<br>1 = `EXT_EVSE_TEST_ALLOWED`<br>2 = `EXT_PRECHARGE_ALLOWED`<br>3 = `CHARGE_ENABLING`<br>4 = `CHARGE_ENABLED`<br>5 = `GRACEFUL_SHUTDOWN`<br>6 = `EMERGENCY_SHUTDOWN`<br>7 = `CHARGE_FAULTED`<br>8 = `CHARGE_BLOCKED` | plausible |
| `BMS_extDcPrechargeVoltageLimit` | page 8 | High-voltage battery management system: ext dc precharge voltage limit | 20\|12 | little-endian | unsigned | 0.146502256393 | 0 | V | 0 to 599.926739929 |  | plausible |
| `BMS_dcChargeCurrentRequest` | page 8 | The BMS's instantaneous DC charge current request to the EVSE | 32\|14 | little-endian | signed | 0.25 | 0 | A | -2048 to 2047.75 |  | plausible |
| `BMS_dcChargeCurrentLimit` | page 8 | The vehicle's charge current limit on a DC EVSE's output | 46\|13 | little-endian | signed | 0.5 | 0 | A | -2048 to 2047.5 |  | plausible |
| `BMS_dcDischargeEnabled` | page 8 | High-voltage battery management system: dc discharge enabled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_rippleChargeRetryCount` | page 8 | High-voltage battery management system: ripple charge retry count | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `BMS_dcChargeVoltageLimit` | page 9 | The vehicle's charge voltage limit on a DC EVSE's output | 8\|12 | little-endian | unsigned | 0.146502256393 | 0 | V | 0 to 599.926739929 |  | plausible |
| `BMS_dcChargePowerLimit` | page 9 | Max power limit for pack during DC charging | 20\|12 | little-endian | signed | 1 | 0 | kW | -2048 to 2047 |  | plausible |
| `BMS_acChargePowerRequest` | page 9 | High-voltage battery management system: ac charge power request | 32\|16 | little-endian | unsigned | 0.001 | 0 | kW | 0 to 65.535 |  | plausible |
| `BMS_maxExtIsoFcLinkV` | page 9 | The max voltage read on the FC link during the external isolation check | 48\|13 | little-endian | unsigned | 0.134293735027 | 0 | V | 0 to 1099.99998361 |  | plausible |
| `BMS_minModeledPackTemp` | page 10 | High-voltage battery management system: min modeled pack temp | 8\|11 | little-endian | unsigned | 0.1 | -50 | C | -50 to 154.7 |  | plausible |
| `BMS_maxModeledPackTemp` | page 10 | High-voltage battery management system: max modeled pack temp | 19\|11 | little-endian | unsigned | 0.1 | -50 | C | -50 to 154.7 |  | plausible |
| `BMS_socByDeltaVEnabled` | page 15 | High-voltage battery management system: soc by delta v enabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_socByDvMaxSocLimit` | page 15 | High-voltage battery management system: soc by dv max soc limit | 9\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | plausible |
| `BMS_socByDvVoltageChangeOverAh` | page 15 | High-voltage battery management system: soc by dv voltage change over ah | 19\|9 | little-endian | unsigned | 0.002 | 0 | V | 0 to 1 |  | plausible |
| `BMS_socByDvMaxSocByAhCorrected` | page 15 | High-voltage battery management system: soc by dv max soc by ah corrected | 28\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | plausible |
| `BMS_socByDvMaxBrickVoltage` | page 15 | High-voltage battery management system: soc by dv max brick voltage | 40\|12 | little-endian | unsigned | 0.002 | 0 | V | 0 to 5 |  | plausible |
| `BMS_socByDvMaxBrickId` | page 15 | High-voltage battery management system: soc by dv max brick id | 56\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |

## Multiplexing

`BMS_log1MuxId` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 8 (6 signals), page 9 (4 signals), page 10 (2 signals), page 15 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
