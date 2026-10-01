---
layout: default
title: "BMS_log1 (0x372) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: log1. Tesla Model 3 CAN bus message BMS_log1 (0x372) of High-voltage battery management system, firmware 2026.26.6.5, 30 signals (BMS_log1MuxId, BMS_powerTransferStatus, BMS_extDcPrechargeVoltageLimit, BMS_dcChargeCurrentRequest and 26 more). Bit layout, scaling, units and value tables."
---

# BMS_log1 (0x372) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: log1; frame length observed on a vehicle bus. This page documents the 30 signals of BMS_log1 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_log1` |
| CAN id | 0x372 (882) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 30 |

## Signals of BMS_log1

Tesla Model 3 CAN bus signals in `BMS_log1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_log1MuxId` | selector | High-voltage battery management system: log1 mux id | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `CPU_USAGE1`<br>1 = `CPU_USAGE2`<br>2 = `CPU_USAGE3`<br>4 = `CHARGE_INTERFACE_1`<br>5 = `CHARGE_INTERFACE_2`<br>6 = `BANDOLIER_MODEL_PACK_TEMPS`<br>7 = `RAW_CDCR_1`<br>8 = `RAW_CDCR_2`<br>9 = `CHARGE_TERMINATION`<br>10 = `CHARGE_REGULATION`<br>11 = `PACK_DATA`<br>12 = `SLEEP_CURRENT_1_STATES_AND_BOOLS`<br>13 = `CHARGE_ENERGY_3_AND_PACK_VOLTAGE`<br>14 = `CHARGE_ENERGY_4` | validated |
| `BMS_powerTransferStatus` | page 4 | Reports the Battery Management System (BMS) power transfer interface state. | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BMS_POWER_TRANSFER_STANDBY`<br>1 = `BMS_EXT_EVSE_TEST_ALLOWED`<br>2 = `BMS_EXT_PRECHARGE_ALLOWED`<br>3 = `BMS_POWER_TRANSFER_ENABLING`<br>4 = `BMS_POWER_TRANSFER_ENABLED`<br>5 = `BMS_GRACEFUL_SHUTDOWN`<br>6 = `BMS_EMERGENCY_SHUTDOWN`<br>7 = `BMS_POWER_TRANSFER_FAULTED`<br>8 = `BMS_POWER_TRANSFER_BLOCKED` | validated |
| `BMS_extDcPrechargeVoltageLimit` | page 4 | High-voltage battery management system: ext dc precharge voltage limit | 20\|12 | little-endian | unsigned | 0.146502256393 | 0 | V | 0 to 599.926739929 |  | validated |
| `BMS_dcChargeCurrentRequest` | page 4 | The BMS's instantaneous DC charge current request to the EVSE | 32\|14 | little-endian | signed | 0.25 | 0 | A | -2048 to 2047.75 |  | validated |
| `BMS_dcChargeCurrentLimit` | page 4 | The vehicle's charge current limit on a DC EVSE's output | 46\|13 | little-endian | signed | 0.5 | 0 | A | -2048 to 2047.5 |  | validated |
| `BMS_dcDischargeEnabled` | page 4 | High-voltage battery management system: dc discharge enabled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_rippleChargeRetryCount` | page 4 | High-voltage battery management system: ripple charge retry count | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `BMS_dcChargeVoltageLimit` | page 5 | The vehicle's charge voltage limit on a DC EVSE's output | 8\|12 | little-endian | unsigned | 0.146502256393 | 0 | V | 0 to 599.926739929 |  | validated |
| `BMS_dcChargePowerLimit` | page 5 | Max power limit for pack during DC charging | 20\|12 | little-endian | signed | 1 | 0 | kW | -2048 to 2047 |  | validated |
| `BMS_acRealPowerRequest` | page 5 | Reports the instantaneous real AC power command during active power transfer. | 32\|16 | little-endian | signed | 0.002 | 0 | kW | -40 to 40 |  | validated |
| `BMS_maxExtIsoFcLinkV` | page 5 | The max voltage read on the FC link during the external isolation check | 48\|13 | little-endian | unsigned | 0.134293735027 | 0 | V | 0 to 1099.99998361 |  | validated |
| `BMS_minModeledPackTemp` | page 6 | High-voltage battery management system: min modeled pack temp | 8\|11 | little-endian | unsigned | 0.1 | -50 | C | -50 to 154.7 |  | plausible |
| `BMS_maxModeledPackTemp` | page 6 | High-voltage battery management system: max modeled pack temp | 19\|11 | little-endian | unsigned | 0.1 | -50 | C | -50 to 154.7 |  | plausible |
| `BMS_energyMaxPredictedBrickTemp` | page 13 | High-voltage battery management system: energy max predicted brick temp | 8\|8 | little-endian | unsigned | 1 | -50 | C | -50 to 205 |  | validated |
| `BMS_energyTempGradientAtMaxTemp` | page 13 | High-voltage battery management system: energy temp gradient at max temp | 16\|9 | little-endian | unsigned | 0.1 | 0 | C | 0 to 51.1 |  | validated |
| `BMS_energyWalkMaxSoc` | page 13 | High-voltage battery management system: energy walk max soc | 25\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | validated |
| `BMS_energyWalkMinSoc` | page 13 | High-voltage battery management system: energy walk min soc | 35\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | validated |
| `BMS_chargeEnergyWalkState` | page 13 | High-voltage battery management system: charge energy walk state | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ENERGY_WALK_INIT`<br>1 = `ENERGY_WALK_RUNNING`<br>2 = `ENERGY_WALK_COMPLETE`<br>3 = `ENERGY_WALK_STOPPED` | validated |
| `BMS_packVoltage` | page 13 | Measures voltage on the battery side of the High Voltage (HV) contactors. | 48\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | validated |
| `BMS_energyWalkMaxPackCurrent` | page 14 | High-voltage battery management system: energy walk max pack current; raw 32768 = signal not available (SNA) | 8\|16 | little-endian | signed | 0.1 | 0 | A | -3276.7 to 3276.7 | -32768 = `SNA` | validated |
| `BMS_energyWalkMaxVehiclePower` | page 14 | High-voltage battery management system: energy walk max vehicle power | 24\|11 | little-endian | signed | 1 | 500 | kW | -524 to 1523 |  | validated |
| `BMS_battTempPct` | page 14 | High-voltage battery management system: batt temp pct; raw 255 = signal not available (SNA) | 35\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 | 255 = `SNA` | validated |
| `BMS_powerTransferDisableType` | page 14 | High-voltage battery management system: power transfer disable type | 43\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `CANCELED`<br>2 = `ABORTED`<br>3 = `FAULTED` | validated |
| `BMS_powerTransferDisableReason` | page 14 | High-voltage battery management system: power transfer disable reason | 45\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `COND_NONE`<br>1 = `CP_MIA`<br>2 = `PCS_MIA`<br>3 = `CP_EMERGENCY_SHUTDOWN_REQUESTED`<br>4 = `PCS_EMERGENCY_SHUTDOWN_REQUESTED`<br>5 = `CP_FAULT_LINE_ASSERTED`<br>6 = `SYSTEM_DIRECTOR_FAULT_REQUESTED`<br>7 = `POWERSHARE_PROTECTION_TRIPPED`<br>10 = `CP_ESCALATED_SHUTDOWN_REQUESTED`<br>11 = `PCS_ESCALATED_SHUTDOWN_REQUESTED`<br>12 = `ABORT_CHARGE_ALERT_SET`<br>13 = `ABORT_SUPERDISCHARGE_ALERT_SET`<br>14 = `FC_LINK_NOT_ALLOWED_TO_ENERGIZE`<br>15 = `EVSE_NOT_COMPATIBLE`<br>16 = `FC_CONTACTORS_NOT_OPEN`<br>17 = `FC_CONTACTORS_NOT_CLOSED`<br>18 = `FC_LINK_NOT_READY`<br>19 = `STATE_TIMEOUT_EXPIRED`<br>20 = `EVSE_NOT_PRESENT`<br>21 = `EVSE_NOT_READY`<br>22 = `NOT_NEEDED_OR_WANTED`<br>23 = `CP_GRACEFUL_SHUTDOWN_REQUESTED`<br>24 = `PCS_GRACEFUL_SHUTDOWN_REQUESTED`<br>25 = `SYSTEM_NOT_POSSIBLE`<br>26 = `SYSTEM_NOT_ALLOWED`<br>27 = `CP_DISALLOWS`<br>28 = `PCS_DISALLOWS`<br>29 = `SYSTEM_NOT_ENABLED`<br>30 = `CP_NOT_READY`<br>31 = `CP_NOT_ENABLED`<br>32 = `PCS_NOT_ENABLED`<br>33 = `CP_INLET_STILL_ENERGIZED`<br>34 = `PCS_NOT_DISABLED`<br>35 = `AC_RELAYS_NOT_OPEN`<br>36 = `SOE_TOO_LOW`<br>37 = `FEATURE_DISABLED`<br>38 = `TEMP_TOO_LOW`<br>39 = `ALL_RETRIES_EXHAUSTED`<br>40 = `EVSE_OUTPUT_CURRENT_NOT_LOW`<br>41 = `PRECHARGE_NOT_COMPLETE` | validated |
| `BMS_powerTransferWaitCondition` | page 14 | High-voltage battery management system: power transfer wait condition | 51\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `COND_NONE`<br>1 = `CP_MIA`<br>2 = `PCS_MIA`<br>3 = `CP_EMERGENCY_SHUTDOWN_REQUESTED`<br>4 = `PCS_EMERGENCY_SHUTDOWN_REQUESTED`<br>5 = `CP_FAULT_LINE_ASSERTED`<br>6 = `SYSTEM_DIRECTOR_FAULT_REQUESTED`<br>7 = `POWERSHARE_PROTECTION_TRIPPED`<br>10 = `CP_ESCALATED_SHUTDOWN_REQUESTED`<br>11 = `PCS_ESCALATED_SHUTDOWN_REQUESTED`<br>12 = `ABORT_CHARGE_ALERT_SET`<br>13 = `ABORT_SUPERDISCHARGE_ALERT_SET`<br>14 = `FC_LINK_NOT_ALLOWED_TO_ENERGIZE`<br>15 = `EVSE_NOT_COMPATIBLE`<br>16 = `FC_CONTACTORS_NOT_OPEN`<br>17 = `FC_CONTACTORS_NOT_CLOSED`<br>18 = `FC_LINK_NOT_READY`<br>19 = `STATE_TIMEOUT_EXPIRED`<br>20 = `EVSE_NOT_PRESENT`<br>21 = `EVSE_NOT_READY`<br>22 = `NOT_NEEDED_OR_WANTED`<br>23 = `CP_GRACEFUL_SHUTDOWN_REQUESTED`<br>24 = `PCS_GRACEFUL_SHUTDOWN_REQUESTED`<br>25 = `SYSTEM_NOT_POSSIBLE`<br>26 = `SYSTEM_NOT_ALLOWED`<br>27 = `CP_DISALLOWS`<br>28 = `PCS_DISALLOWS`<br>29 = `SYSTEM_NOT_ENABLED`<br>30 = `CP_NOT_READY`<br>31 = `CP_NOT_ENABLED`<br>32 = `PCS_NOT_ENABLED`<br>33 = `CP_INLET_STILL_ENERGIZED`<br>34 = `PCS_NOT_DISABLED`<br>35 = `AC_RELAYS_NOT_OPEN`<br>36 = `SOE_TOO_LOW`<br>37 = `FEATURE_DISABLED`<br>38 = `TEMP_TOO_LOW`<br>39 = `ALL_RETRIES_EXHAUSTED`<br>40 = `EVSE_OUTPUT_CURRENT_NOT_LOW`<br>41 = `PRECHARGE_NOT_COMPLETE` | validated |
| `BMS_dischargeRetryCount` | page 14 | High-voltage battery management system: discharge retry count | 57\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `BMS_acChargeDesired` | page 14 | High-voltage battery management system: ac charge desired | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_tetheringDesired` | page 14 | High-voltage battery management system: tethering desired | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_gridFormDesired` | page 14 | High-voltage battery management system: grid form desired | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_gridFollowDesired` | page 14 | High-voltage battery management system: grid follow desired | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`BMS_log1MuxId` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 4 (6 signals), page 5 (4 signals), page 6 (2 signals), page 13 (6 signals), page 14 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
