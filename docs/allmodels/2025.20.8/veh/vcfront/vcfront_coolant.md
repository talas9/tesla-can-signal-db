---
layout: default
title: "VCFRONT_coolant (0x241) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: coolant. Tesla Model 3 / Model Y CAN bus message VCFRONT_coolant (0x241) of Front body controller, firmware 2025.20.8, 12 signals (VCFRONT_coolantFlowBatActual, VCFRONT_coolantFlowBatTarget, VCFRONT_coolantFlowBatReason, VCFRONT_coolantFlowPTActual and 8 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_coolant (0x241) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Front body controller message: coolant; frame length observed on a vehicle bus. This page documents the 12 signals of VCFRONT_coolant as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_coolant` |
| CAN id | 0x241 (577) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 12 |

## Signals of VCFRONT_coolant

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_coolant`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_coolantFlowBatActual` | Front body controller: coolant flow bat actual | 0\|9 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 40 |  | validated |
| `VCFRONT_coolantFlowBatTarget` | Front body controller: coolant flow bat target | 9\|8 | little-endian | unsigned | 0.2 | 0 | LPM | 0 to 40 |  | validated |
| `VCFRONT_coolantFlowBatReason` | Front body controller: coolant flow bat reason | 17\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `COOLANT_AIR_PURGE`<br>2 = `NO_FLOW_REQ`<br>3 = `OVERRIDE_BATT`<br>4 = `ACTIVE_MANAGER_BATT`<br>5 = `PASSIVE_MANAGER_BATT`<br>6 = `BMS_FLOW_REQ`<br>7 = `DAS_FLOW_REQ`<br>8 = `OVERRIDE_PT`<br>9 = `ACTIVE_MANAGER_PT`<br>10 = `PASSIVE_MANAGER_PT`<br>11 = `PCS_FLOW_REQ`<br>12 = `DI_FLOW_REQ`<br>13 = `DIS_FLOW_REQ`<br>14 = `HP_FLOW_REQ`<br>15 = `BMS_PPR_FLOW_REQ`<br>16 = `DI_PPR_FLOW_REQ`<br>17 = `UI_FLOW_REQ`<br>18 = `DI_BURN_IN_FLOW_REQ`<br>19 = `BATTERY_DISCHARGE_FLOW_REQ`<br>20 = `DRIVERLESS_SELF_TEST`<br>21 = `AP_AIR_PURGE` | validated |
| `VCFRONT_coolantFlowPTActual` | Front body controller: coolant flow PT actual | 22\|9 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 40 |  | validated |
| `VCFRONT_coolantFlowPTTarget` | Front body controller: coolant flow PT target | 31\|8 | little-endian | unsigned | 0.2 | 0 | LPM | 0 to 40 |  | validated |
| `VCFRONT_coolantFlowPTReason` | Front body controller: coolant flow PT reason | 39\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `COOLANT_AIR_PURGE`<br>2 = `NO_FLOW_REQ`<br>3 = `OVERRIDE_BATT`<br>4 = `ACTIVE_MANAGER_BATT`<br>5 = `PASSIVE_MANAGER_BATT`<br>6 = `BMS_FLOW_REQ`<br>7 = `DAS_FLOW_REQ`<br>8 = `OVERRIDE_PT`<br>9 = `ACTIVE_MANAGER_PT`<br>10 = `PASSIVE_MANAGER_PT`<br>11 = `PCS_FLOW_REQ`<br>12 = `DI_FLOW_REQ`<br>13 = `DIS_FLOW_REQ`<br>14 = `HP_FLOW_REQ`<br>15 = `BMS_PPR_FLOW_REQ`<br>16 = `DI_PPR_FLOW_REQ`<br>17 = `UI_FLOW_REQ`<br>18 = `DI_BURN_IN_FLOW_REQ`<br>19 = `BATTERY_DISCHARGE_FLOW_REQ`<br>20 = `DRIVERLESS_SELF_TEST`<br>21 = `AP_AIR_PURGE` | validated |
| `VCFRONT_wasteHeatRequestType` | Front body controller: waste heat request type | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WASTE_TYPE_NONE`<br>1 = `WASTE_TYPE_PARTIAL`<br>2 = `WASTE_TYPE_FULL`<br>3 = `WASTE_TYPE_BURN_IN` | validated |
| `VCFRONT_coolantHasBeenFilled` | Front body controller: coolant has been filled | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radiatorIneffective` | Indication that the efficiency of the radiator is reduced | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_coolantAirPurgeBatState` | Front body controller: coolant air purge bat state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AIR_PURGE_STATE_INACTIVE`<br>1 = `AIR_PURGE_STATE_ACTIVE`<br>2 = `AIR_PURGE_STATE_COMPLETE`<br>3 = `AIR_PURGE_STATE_INTERRUPTED`<br>4 = `AIR_PURGE_STATE_PENDING` | validated |
| `VCFRONT_coolantFlowTableConfig` | Front body controller: coolant flow table config | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FLOW_TABLE_CONFIG_DEFAULT`<br>1 = `FLOW_TABLE_CONFIG_BMS_TYPE_5` | validated |
| `VCFRONT_coolantLevelContinuouslyLow` | Front body controller: coolant level continuously low | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
