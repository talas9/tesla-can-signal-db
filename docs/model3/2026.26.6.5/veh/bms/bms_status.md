---
layout: default
title: "BMS_status (0x212) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: status. Tesla Model 3 CAN bus message BMS_status (0x212) of High-voltage battery management system, firmware 2026.26.6.5, 20 signals (BMS_hvacPowerRequest, BMS_notEnoughPowerForDrive, BMS_notEnoughPowerForSupport, BMS_preconditionAllowed and 16 more). Bit layout, scaling, units and value tables."
---

# BMS_status (0x212) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: status; frame length observed on a vehicle bus. This page documents the 20 signals of BMS_status as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_status` |
| CAN id | 0x212 (530) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 20 |

## Signals of BMS_status

Tesla Model 3 CAN bus signals in `BMS_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_hvacPowerRequest` | High-voltage battery management system: hvac power request | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_notEnoughPowerForDrive` | Flag indicating the min pack power is lower than specified threshold to support drive | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_notEnoughPowerForSupport` | Flag indicating if the system can support a new request for 12V battery support | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_preconditionAllowed` | High-voltage battery management system: precondition allowed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_updateAllowed` | High-voltage battery management system: update allowed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cpMiaOnHvs` | Flag indicating that BMS is no longer receiving comms from CP on HVS bus | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_pcsPwmEnabled` | Reports the state of the PCS_PWM_ENABLE input on the HVBMS, which is derived from the P1-12-DCDC-ENABLE input, which comes from VCFRONT | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_contactorState` | BMS Contactor Status; raw 0 = signal not available (SNA) | 8\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `BMS_CTRSET_SNA`<br>1 = `BMS_CTRSET_OPEN`<br>2 = `BMS_CTRSET_OPENING`<br>3 = `BMS_CTRSET_CLOSING`<br>4 = `BMS_CTRSET_CLOSED`<br>5 = `BMS_CTRSET_WELDED`<br>6 = `BMS_CTRSET_BLOCKED` | validated |
| `BMS_userChargeStatus` | BMS charge status for UI display. Renamed from BMS_uiChargeStatus | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BMS_DISCONNECTED`<br>1 = `BMS_NO_POWER`<br>2 = `BMS_ABOUT_TO_CHARGE`<br>3 = `BMS_CHARGING`<br>4 = `BMS_CHARGE_COMPLETE`<br>5 = `BMS_CHARGE_STOPPED`<br>6 = `BMS_CALIBRATING` | validated |
| `BMS_batteryInputPower` | High-voltage battery management system: battery input power; raw 65535 = signal not available (SNA) | 14\|16 | little-endian | unsigned | 0.05 | 0 | kW | 0 to 3276.7 | 65535 = `SNA` | validated |
| `BMS_chargeRequest` | Indicates charge is available and charge is desired | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_state` | BMS operating state; raw 9 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BMS_STANDBY`<br>1 = `BMS_DRIVE`<br>2 = `BMS_SUPPORT`<br>3 = `BMS_CHARGE`<br>4 = `BMS_FEIM`<br>5 = `BMS_CLEAR_FAULT`<br>6 = `BMS_FAULT`<br>7 = `BMS_WELD`<br>8 = `BMS_TEST`<br>9 = `BMS_SNA`<br>10 = `BMS_DIAG` | validated |
| `BMS_diLimpRequest` | BMS request to DI to enter limp mode | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LIMP_REQUEST_NONE`<br>1 = `LIMP_REQUEST_WELDED` | validated |
| `BMS_okToShipByAir` | High-voltage battery management system: ok to ship by air | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_okToShipByLand` | High-voltage battery management system: ok to ship by land | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_chgPowerAvailable` | BMS available charge power; raw 4095 = signal not available (SNA) | 39\|12 | little-endian | unsigned | 0.125 | 0 | kW | 0 to 511.75 | 4095 = `SNA` | validated |
| `BMS_acManagerState` | High-voltage battery management system: ac manager state | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INACTIVE`<br>1 = `STANDBY`<br>2 = `REQUEST_POWER_TRANSFER`<br>3 = `ENABLE_FC_LINK_FOR_AC`<br>4 = `ENABLE_PCS`<br>5 = `CHARGING_ACTIVE`<br>6 = `TETHERING_ACTIVE`<br>7 = `GRID_FOLLOW_ACTIVE`<br>8 = `GRID_FORM_ACTIVE`<br>9 = `DISABLE_PCS`<br>10 = `OPEN_AC_RELAYS`<br>11 = `FAULTED` | validated |
| `BMS_conditioningRequest` | BMS request to enable conditioning so it can attempt FEIM recovery | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_smStateRequest` | BMS high level state request; raw 9 = signal not available (SNA) | 57\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BMS_STANDBY`<br>1 = `BMS_DRIVE`<br>2 = `BMS_SUPPORT`<br>3 = `BMS_CHARGE`<br>4 = `BMS_FEIM`<br>5 = `BMS_CLEAR_FAULT`<br>6 = `BMS_FAULT`<br>7 = `BMS_WELD`<br>8 = `BMS_TEST`<br>9 = `BMS_SNA`<br>10 = `BMS_DIAG` | validated |
| `BMS_hvState` | BMS high voltage state | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HV_DOWN`<br>1 = `HV_COMING_UP`<br>2 = `HV_GOING_DOWN`<br>3 = `HV_UP_FOR_DRIVE`<br>4 = `HV_UP_FOR_CHARGE`<br>5 = `HV_UP_FOR_DC_CHARGE`<br>6 = `HV_UP` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
