---
layout: default
title: "VCFRONT_partyDebug (0x104) — Front body controller, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "Front body controller message: party debug. Tesla Model 3 CAN bus message VCFRONT_partyDebug (0x104) of Front body controller, firmware 2026.26.6.5, 18 signals (VCFRONT_vcleftHighPower, VCFRONT_vcrightHighPower, VCFRONT_uiHighPower, VCFRONT_5VAStable and 14 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_partyDebug (0x104) — Front body controller, Tesla Model 3 2026.26.6.5 PARTY CAN

Front body controller message: party debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of VCFRONT_partyDebug as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_partyDebug` |
| CAN id | 0x104 (260) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCFRONT |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 18 |

## Signals of VCFRONT_partyDebug

Tesla Model 3 CAN bus signals in `VCFRONT_partyDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_vcleftHighPower` | Front body controller: vcleft high power | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_vcrightHighPower` | Front body controller: vcright high power | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_uiHighPower` | Front body controller: ui high power | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_5VAStable` | Front body controller: 5 VA stable | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_5VBStable` | Front body controller: 5 VB stable | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_12VAStable` | Front body controller: 12 VA stable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_12VBStable` | Front body controller: 12 VB stable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_railA` | Front body controller: rail a | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_railB` | Front body controller: rail b | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_chargePumpStable` | Front body controller: charge pump stable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_vehicleSM` | Vehicle state machine state; raw 18 = signal not available (SNA) | 10\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `VEHICLE_STATUS_INIT`<br>1 = `VEHICLE_STATUS_LOW_POWER_STANDBY`<br>2 = `VEHICLE_STATUS_SILENT_WAKE`<br>3 = `VEHICLE_STATUS_BATTERY_POST_WAKE`<br>4 = `VEHICLE_STATUS_SYSTEM_CHECKS`<br>5 = `VEHICLE_STATUS_SLEEP_SHUTDOWN`<br>6 = `VEHICLE_STATUS_SLEEP_STANDBY`<br>7 = `VEHICLE_STATUS_LV_SHUTDOWN`<br>8 = `VEHICLE_STATUS_LV_AWAKE`<br>9 = `VEHICLE_STATUS_HV_UP_STANDBY`<br>10 = `VEHICLE_STATUS_ACCESSORY`<br>11 = `VEHICLE_STATUS_ACCESSORY_PLUS`<br>12 = `VEHICLE_STATUS_CONDITIONING`<br>13 = `VEHICLE_STATUS_DRIVE`<br>14 = `VEHICLE_STATUS_CRASH`<br>15 = `VEHICLE_STATUS_OTA`<br>16 = `VEHICLE_STATUS_TURN_ON_RAILS`<br>17 = `VEHICLE_STATUS_RESET`<br>18 = `VEHICLE_STATUS_SNA` | plausible |
| `VCFRONT_revBattFault` | Front body controller: rev batt fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_battSM` | Front body controller: batt SM | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BATTERY_SM_STATE_INIT`<br>1 = `BATTERY_SM_STATE_CHARGE`<br>2 = `BATTERY_SM_STATE_DISCHARGE`<br>3 = `BATTERY_SM_STATE_STANDBY`<br>4 = `BATTERY_SM_STATE_RESISTANCE_ESTIMATION`<br>5 = `BATTERY_SM_STATE_OTA_STANDBY`<br>6 = `BATTERY_SM_STATE_DISCONNECTED_BATTERY_TEST`<br>7 = `BATTERY_SM_STATE_SHORTED_CELL_TEST`<br>8 = `BATTERY_SM_STATE_FAULT`<br>9 = `BATTERY_SM_STATE_RECOVERY`<br>10 = `BATTERY_SM_STATE_EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_U13Init` | Front body controller: U13 init | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_U16Init` | Front body controller: U16 init | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_anyVehLoadShedActiveDBG` | Front body controller: any veh load shed active DBG | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_battVoltage` | Front body controller: batt voltage | 24\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_battCurrent` | Front body controller: batt current | 40\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
