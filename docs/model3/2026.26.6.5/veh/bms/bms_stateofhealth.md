---
layout: default
title: "BMS_stateOfHealth (0x492) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: state of health. Tesla Model 3 CAN bus message BMS_stateOfHealth (0x492) of High-voltage battery management system, firmware 2026.26.6.5, 9 signals (BMS_sohEnergyPercent, BMS_userFacingSohTestState, BMS_userFacingSohTestEndMode, BMS_timeSinceSohUpdate and 5 more). Bit layout, scaling, units and value tables."
---

# BMS_stateOfHealth (0x492) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: state of health; frame length observed on a vehicle bus. This page documents the 9 signals of BMS_stateOfHealth as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_stateOfHealth` |
| CAN id | 0x492 (1170) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of BMS_stateOfHealth

Tesla Model 3 CAN bus signals in `BMS_stateOfHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_sohEnergyPercent` | Estimate of battery SOH Energy % based on the most accurate capacity estimates the BMS has available; raw 1023 = signal not available (SNA) | 0\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 | 1023 = `SNA` | validated |
| `BMS_userFacingSohTestState` | High-voltage battery management system: user facing soh test state | 10\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_RUNNING`<br>1 = `HEAT_PACK`<br>2 = `DISCHARGE`<br>3 = `DISCHARGE_REST`<br>4 = `CHARGE`<br>5 = `CHARGE_REST` | validated |
| `BMS_userFacingSohTestEndMode` | High-voltage battery management system: user facing soh test end mode | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `RUNNING`<br>2 = `REQUEST_DROPPED`<br>3 = `FAILED`<br>4 = `TEST_COMPLETE`<br>5 = `TEST_COMPLETE_WITH_SOC_IMBALANCE` | validated |
| `BMS_timeSinceSohUpdate` | Days since last successful SOH test; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 1 | 0 | days | 0 to 3650 | 4095 = `SNA` | validated |
| `BMS_sohTestCycleFlag` | Flag that is True from the start of an SOH test until it ends and all relevant signals have been logged | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_sohTestIsBlocked` | High-voltage battery management system: soh test is blocked | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_calibratedSohAvailable` | SOH Energy is based on valid results from the SOH capacity test | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_requiredEvsePowerForSoh` | High-voltage battery management system: required evse power for soh; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.125 | 0 | kW | 0 to 31.75 | 255 = `SNA` | validated |
| `BMS_distanceSinceSohUpdate` | Distance since the last State of Health update in km; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 1 | 0 | km | 0 to 65534 | 65535 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
