---
layout: default
title: "CP_chargeStatusLog (0x43D) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Charge port controller message: charge status log. Ethernet-side message CP_chargeStatusLog of Charge port controller for Tesla Model 3 / Model Y firmware 2025.20.8, 9 signals (CP_hvChargeStatus_log, CP_chargeShutdownRequest_log, CP_acChargeCurrentLimit_log, CP_internalMaxDcCurrentLimit_log and 5 more). Bit layout, scaling, units and value tables."
---

# CP_chargeStatusLog (0x43D) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Charge port controller message: charge status log. This page documents the 9 signals of CP_chargeStatusLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_chargeStatusLog` |
| Ethernet-side id | 0x43D (1085) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of CP_chargeStatusLog

Tesla Model 3 / Model Y CAN bus signals in `CP_chargeStatusLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_hvChargeStatus_log` | Charge port controller: hv charge status log | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CHARGE_INACTIVE`<br>1 = `CHARGE_CONNECTED`<br>2 = `CHARGE_STANDBY`<br>3 = `EXT_EVSE_TEST_ACTIVE`<br>4 = `EVSE_TEST_PASSED`<br>5 = `CHARGE_ENABLED`<br>6 = `CHARGE_FAULTED` | plausible |
| `CP_chargeShutdownRequest_log` | Charge port controller: charge shutdown request log | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_SHUTDOWN_REQUESTED`<br>1 = `GRACEFUL_SHUTDOWN_REQUESTED`<br>2 = `EMERGENCY_SHUTDOWN_REQUESTED` | plausible |
| `CP_acChargeCurrentLimit_log` | Charge port controller: ac charge current limit log | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | plausible |
| `CP_internalMaxDcCurrentLimit_log` | Charge port controller: internal max dc current limit log | 16\|13 | little-endian | unsigned | 0.25 | 0 | A | 0 to 2047.75 |  | plausible |
| `CP_vehicleIsoCheckRequired_log` | Charge port controller: vehicle iso check required log | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_vehiclePrechargeRequired_log` | Charge port controller: vehicle precharge required log | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_internalMaxAcCurrentLimit_log` | Charge port controller: internal max ac current limit log | 32\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | plausible |
| `CP_evseChargeType_log` | Charge port controller: evse charge type log | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_CHARGER_PRESENT`<br>1 = `DC_CHARGER_PRESENT`<br>2 = `AC_CHARGER_PRESENT` | plausible |
| `CP_chgLimitMode_log` | Charge port controller: chg limit mode log | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HW`<br>1 = `CABLE_UNSECURED`<br>2 = `THERMAL_FOLDBACK`<br>3 = `ADAPTER_FOLDBACK`<br>4 = `DEBUG_OVERRIDE`<br>5 = `NUM` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
