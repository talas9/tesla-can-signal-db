---
layout: default
title: "CP_chargeStatus (0x13D) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: charge status. Tesla Model Y CAN bus message CP_chargeStatus (0x13D) of Charge port controller, firmware 2026.26.6.5, 13 signals (CP_powerTransferStatus, CP_powerTransferShutdownRequest, CP_evseAcControlMode, CP_v2xCapable and 9 more). Bit layout, scaling, units and value tables."
---

# CP_chargeStatus (0x13D) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN

Charge port controller message: charge status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of CP_chargeStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_chargeStatus` |
| CAN id | 0x13D (317) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 13 |

## Signals of CP_chargeStatus

Tesla Model Y CAN bus signals in `CP_chargeStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_powerTransferStatus` | Indicates the state of the charge port power transfer interface. | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_POWER_TRANSFER_INACTIVE`<br>1 = `CP_POWER_TRANSFER_CONNECTED`<br>2 = `CP_POWER_TRANSFER_STANDBY`<br>3 = `CP_EXT_EVSE_TEST_ACTIVE`<br>4 = `CP_EVSE_TEST_PASSED`<br>5 = `CP_POWER_TRANSFER_ENABLED`<br>6 = `CP_POWER_TRANSFER_FAULTED` | validated |
| `CP_powerTransferShutdownRequest` | Reports the request from the charge port to end a charge session. | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_SHUTDOWN_REQUESTED`<br>1 = `GRACEFUL_SHUTDOWN_REQUESTED`<br>2 = `ESCALATED_SHUTDOWN_REQUESTED`<br>3 = `EMERGENCY_SHUTDOWN_REQUESTED` | validated |
| `CP_evseAcControlMode` | Charge port controller: evse ac control mode | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AC_CTRL_MODE_NONE`<br>1 = `AC_CTRL_MODE_CHARGE_ONLY`<br>2 = `AC_CTRL_MODE_GRID_FORM`<br>3 = `AC_CTRL_MODE_GRID_FOLLOW` | validated |
| `CP_v2xCapable` | Indicates whether the charge port ECU supports Powershare (V2X) features. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_evseAcCurrentLimit` | Measures the maximum current the AC EVSE can allow per conductor. | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | validated |
| `CP_internalMaxDcCurrentLimit` | Measures the maximum current the charge port can allow while DC charging. | 16\|13 | little-endian | unsigned | 0.25 | 0 | A | 0 to 2047.75 |  | validated |
| `CP_vehicleIsoCheckRequired` | Indicates whether the vehicle is expected to perform isolation monitoring while charging is active. | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_vehiclePrechargeRequired` | Indicates whether the vehicle is expected to perform precharge for the DC charge session. | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_internalMaxAcCurrentLimit` | Measures the maximum current the charge port can allow while AC charging. | 32\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | validated |
| `CP_evseChargeType` | Reports the type of EVSE connected. | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_CHARGER_PRESENT`<br>1 = `DC_CHARGER_PRESENT`<br>2 = `AC_CHARGER_PRESENT` | validated |
| `CP_chgLimitMode` | Reports the reason the charge port is attempting to limit the charge current. | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_CHG_LIMIT_HW`<br>1 = `CP_CHG_LIMIT_CABLE_UNSECURED`<br>2 = `CP_CHG_LIMIT_THERMAL_FOLDBACK`<br>3 = `CP_CHG_LIMIT_ADAPTER_FOLDBACK`<br>4 = `CP_CHG_LIMIT_DEBUG_OVERRIDE`<br>5 = `CP_CHG_LIMIT_ADAPTER_HW`<br>6 = `CP_CHG_LIMIT_NUM` | validated |
| `CP_dcHvInletExposed` | Indicates whether the direct current (DC) charge port inlet pins are exposed to human touch. | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_acHvInletExposed` | Indicates whether the alternating current (AC) charge port inlet pins are exposed to human touch. | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
