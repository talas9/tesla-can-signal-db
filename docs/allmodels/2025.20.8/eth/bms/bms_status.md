---
layout: default
title: "BMS_status (0x212) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: status. Ethernet-side message BMS_status of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 21 signals (BMS_hvacPowerRequest, BMS_notEnoughPowerForDrive, BMS_notEnoughPowerForSupport, BMS_preconditionAllowed and 17 more). Bit layout, scaling, units and value tables."
---

# BMS_status (0x212) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: status. This page documents the 21 signals of BMS_status as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_status` |
| Ethernet-side id | 0x212 (530) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 21 |

## Signals of BMS_status

Tesla Model 3 / Model Y CAN bus signals in `BMS_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_hvacPowerRequest` | High-voltage battery management system: hvac power request | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_notEnoughPowerForDrive` | Flag indicating the min pack power is lower than specified threshold to support drive | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_notEnoughPowerForSupport` | Flag indicating if the system can support a new request for 12V battery support | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_preconditionAllowed` | High-voltage battery management system: precondition allowed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_updateAllowed` | High-voltage battery management system: update allowed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_activeHeatingWorthwhile` | Determination by the Battery Management System (BMS) if active heating is worthwhile | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_cpMiaOnHvs` | Flag indicating that BMS is no longer receiving comms from CP on HVS bus | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_pcsPwmEnabled` | Reports the state of the PCS_PWM_ENABLE input on the HVBMS, which is derived from the P1-12-DCDC-ENABLE input, which comes from VCFRONT | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_contactorState` | BMS Contactor Status; raw 0 = signal not available (SNA) | 8\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `BMS_CTRSET_SNA`<br>1 = `BMS_CTRSET_OPEN`<br>2 = `BMS_CTRSET_OPENING`<br>3 = `BMS_CTRSET_CLOSING`<br>4 = `BMS_CTRSET_CLOSED`<br>5 = `BMS_CTRSET_WELDED`<br>6 = `BMS_CTRSET_BLOCKED` | validated |
| `BMS_userChargeStatus` | BMS charge status for UI display. Renamed from BMS_uiChargeStatus | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BMS_DISCONNECTED`<br>1 = `BMS_NO_POWER`<br>2 = `BMS_ABOUT_TO_CHARGE`<br>3 = `BMS_CHARGING`<br>4 = `BMS_CHARGE_COMPLETE`<br>5 = `BMS_CHARGE_STOPPED`<br>6 = `BMS_CALIBRATING` | validated |
| `BMS_totalBatteryPower` | High-voltage battery management system: total battery power; raw 65536 = signal not available (SNA) | 14\|17 | little-endian | signed | 0.05 | 0 | kW | -3276.8 to 3276.75 | -65536 = `SNA` | plausible |
| `BMS_chargeRequest` | Indicates charge is available and charge is desired | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_state` | BMS operating state; raw 9 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BMS_STANDBY`<br>1 = `BMS_DRIVE`<br>2 = `BMS_SUPPORT`<br>3 = `BMS_CHARGE`<br>4 = `BMS_FEIM`<br>5 = `BMS_CLEAR_FAULT`<br>6 = `BMS_FAULT`<br>7 = `BMS_WELD`<br>8 = `BMS_TEST`<br>9 = `BMS_SNA`<br>10 = `BMS_DIAG` | validated |
| `BMS_diLimpRequest` | BMS request to DI to enter limp mode | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LIMP_REQUEST_NONE`<br>1 = `LIMP_REQUEST_WELDED` | plausible |
| `BMS_okToShipByAir` | High-voltage battery management system: ok to ship by air | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_okToShipByLand` | High-voltage battery management system: ok to ship by land | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_chgPowerAvailable` | BMS available charge power; raw 4095 = signal not available (SNA) | 40\|12 | little-endian | unsigned | 0.125 | 0 | kW | 0 to 511.75 | 4095 = `SNA` | plausible |
| `BMS_chargeRetryCount` | Number of retries remaining to enable charge | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | plausible |
| `BMS_conditioningRequest` | BMS request to enable conditioning so it can attempt FEIM recovery | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_smStateRequest` | BMS high level state request; raw 9 = signal not available (SNA) | 57\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BMS_STANDBY`<br>1 = `BMS_DRIVE`<br>2 = `BMS_SUPPORT`<br>3 = `BMS_CHARGE`<br>4 = `BMS_FEIM`<br>5 = `BMS_CLEAR_FAULT`<br>6 = `BMS_FAULT`<br>7 = `BMS_WELD`<br>8 = `BMS_TEST`<br>9 = `BMS_SNA`<br>10 = `BMS_DIAG` | plausible |
| `BMS_hvState` | BMS high voltage state | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HV_DOWN`<br>1 = `HV_COMING_UP`<br>2 = `HV_GOING_DOWN`<br>3 = `HV_UP_FOR_DRIVE`<br>4 = `HV_UP_FOR_CHARGE`<br>5 = `HV_UP_FOR_DC_CHARGE`<br>6 = `HV_UP` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
