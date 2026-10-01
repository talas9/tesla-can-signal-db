---
layout: default
title: "APSB_status (0x3CB) — APSB ECU, Tesla Model 3 2025.20.8 ETH"
description: "APSB ECU message: status. Ethernet-side message APSB_status of APSB ECU for Tesla Model 3 firmware 2025.20.8, 20 signals (APSB_appStatusMonitorState, APSB_vehBehaviorState, APSB_canMaster, APSB_appGpioState and 16 more). Bit layout, scaling, units and value tables."
---

# APSB_status (0x3CB) — APSB ECU, Tesla Model 3 2025.20.8 ETH

APSB ECU message: status. This page documents the 20 signals of APSB_status as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_status` |
| Ethernet-side id | 0x3CB (971) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 20 |

## Signals of APSB_status

Tesla Model 3 CAN bus signals in `APSB_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_appStatusMonitorState` | APSB ECU: app status monitor state | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_MONITOR_STATE_UNKNOWN`<br>1 = `STATUS_MONITOR_STATE_PWR_OFF`<br>2 = `STATUS_MONITOR_STATE_INIT`<br>3 = `STATUS_MONITOR_STATE_NOMINAL`<br>4 = `STATUS_MONITOR_STATE_CRITICAL`<br>5 = `STATUS_MONITOR_STATE_SHUTTING_DOWN`<br>6 = `STATUS_MONITOR_STATE_RECOVERY`<br>7 = `STATUS_MONITOR_NUM_STATES` | plausible |
| `APSB_vehBehaviorState` | APSB ECU: veh behavior state | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `VEH_BEHAVIOR_STATE_UNKNOWN`<br>1 = `VEH_BEHAVIOR_STATE_APS_AVAILABLE`<br>2 = `VEH_BEHAVIOR_STATE_APS_CONTROL`<br>3 = `VEH_BEHAVIOR_STATE_APS_BRIDGE_APP`<br>4 = `VEH_BEHAVIOR_STATE_APS_BRIDGE_APB`<br>5 = `VEH_BEHAVIOR_STATE_APS_FAIL_SAFE`<br>6 = `VEH_BEHAVIOR_STATE_APS_OVERRIDE`<br>7 = `VEH_BEHAVIOR_STATE_SYSTEM_FAULT`<br>8 = `VEH_BEHAVIOR_NUM_STATES` | plausible |
| `APSB_canMaster` | Indicates which of the autopilot computers is currently controlling outgoing CAN traffic; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CAN_MASTER_APS`<br>1 = `CAN_MASTER_APP`<br>2 = `CAN_MASTER_APB`<br>3 = `CAN_MASTER_SNA` | plausible |
| `APSB_appGpioState` | APSB ECU: app gpio state | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_GPIO_STATE_PWR_DOWN_REBOOT`<br>1 = `AP_GPIO_STATE_DISABLED`<br>2 = `AP_GPIO_STATE_CRITICAL`<br>3 = `AP_GPIO_STATE_HEALTHY` | plausible |
| `APSB_eacInternalState` | APSB ECU: eac internal state | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_EAC_STATE_INIT`<br>1 = `APS_EAC_STATE_MOMENTARY`<br>2 = `APS_EAC_STATE_CONTINUOUS`<br>3 = `APS_EAC_STATE_AUTOPARK`<br>4 = `APS_EAC_STATE_INHIBIT`<br>5 = `APS_EAC_STATE_OVERRIDE`<br>6 = `APS_EAC_STATE_LSS`<br>7 = `APS_EAC_NUM_STATES` | plausible |
| `APSB_switchState` | APSB ECU: switch state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_apbStatusMonitorState` | APSB ECU: apb status monitor state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_MONITOR_STATE_UNKNOWN`<br>1 = `STATUS_MONITOR_STATE_PWR_OFF`<br>2 = `STATUS_MONITOR_STATE_INIT`<br>3 = `STATUS_MONITOR_STATE_NOMINAL`<br>4 = `STATUS_MONITOR_STATE_CRITICAL`<br>5 = `STATUS_MONITOR_STATE_SHUTTING_DOWN`<br>6 = `STATUS_MONITOR_STATE_RECOVERY`<br>7 = `STATUS_MONITOR_NUM_STATES` | plausible |
| `APSB_apbGpioState` | APSB ECU: apb gpio state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_GPIO_STATE_PWR_DOWN_REBOOT`<br>1 = `AP_GPIO_STATE_DISABLED`<br>2 = `AP_GPIO_STATE_CRITICAL`<br>3 = `AP_GPIO_STATE_HEALTHY` | plausible |
| `APSB_statusCounter` | APSB ECU: status counter | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_locLimitReason` | APSB ECU: loc limit reason | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOMINAL_DEFAULT`<br>1 = `NOT_IN_DRIVE`<br>2 = `ACC_AND_AEB_UNAVAILABLE`<br>3 = `PRIMARY_AP_NOT_HEALTHY`<br>4 = `RADAR_NOT_HEALTHY`<br>5 = `NO_RADAR_TARGET`<br>6 = `LOC_MONITOR_UNAVAILABLE`<br>7 = `LOC_LIMITS_EXTENDED` | plausible |
| `APSB_appPowerStateRequest` | APSB ECU: app power state request | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_POWER_STATE_NOMINAL`<br>1 = `AP_POWER_STATE_SENTRY`<br>2 = `AP_POWER_STATE_SUSPEND`<br>3 = `AP_POWER_STATE_SLEEP` | plausible |
| `APSB_appPowerStateReason` | APSB ECU: app power state reason | 31\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UI_POWER_STATE_REQUEST`<br>1 = `AP_WDOG_UNHEALTHY`<br>2 = `AP_NM_REASON_SET`<br>3 = `AP_NOT_IN_PARK`<br>4 = `GTW_GOTO_FULL_POWER`<br>5 = `AP_POWER_REQUEST_HYSTERESIS`<br>6 = `AP_POWER_REQUEST_OVERHEATING`<br>7 = `AP_POWER_REQUEST_OVERRIDE`<br>8 = `VC_POWER_REQUEST`<br>9 = `LOADSHED_POWER_REQUEST_PENDING`<br>10 = `AP_POWER_REQUEST_OVERHEATED`<br>11 = `SLEEP_REQUEST_RECVD`<br>12 = `UI_SUMMON_STANDBY_MODE_ENABLED` | plausible |
| `APSB_apbPowerStateRequest` | APSB ECU: apb power state request | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_POWER_STATE_NOMINAL`<br>1 = `AP_POWER_STATE_SENTRY`<br>2 = `AP_POWER_STATE_SUSPEND`<br>3 = `AP_POWER_STATE_SLEEP` | plausible |
| `APSB_apbPowerStateReason` | APSB ECU: apb power state reason | 38\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UI_POWER_STATE_REQUEST`<br>1 = `AP_WDOG_UNHEALTHY`<br>2 = `AP_NM_REASON_SET`<br>3 = `AP_NOT_IN_PARK`<br>4 = `GTW_GOTO_FULL_POWER`<br>5 = `AP_POWER_REQUEST_HYSTERESIS`<br>6 = `AP_POWER_REQUEST_OVERHEATING`<br>7 = `AP_POWER_REQUEST_OVERRIDE`<br>8 = `VC_POWER_REQUEST`<br>9 = `LOADSHED_POWER_REQUEST_PENDING`<br>10 = `AP_POWER_REQUEST_OVERHEATED`<br>11 = `SLEEP_REQUEST_RECVD`<br>12 = `UI_SUMMON_STANDBY_MODE_ENABLED` | plausible |
| `APSB_heaterStateDebug` | APSB ECU: heater state debug; raw 7 = signal not available (SNA) | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `APS_HEATER_OFF`<br>1 = `APS_HEATER_ON_HEATING`<br>2 = `APS_HEATER_ON_NOT_HEATING`<br>3 = `APS_HEATER_FAULT_OPEN`<br>4 = `APS_HEATER_FAULT_SHORT`<br>7 = `APS_HEATER_SNA` | plausible |
| `APSB_autosummonCounter` | APSB ECU: autosummon counter | 46\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_autosummonAlert` | APSB ECU: autosummon alert | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_gpsAntennaState` | APSB ECU: gps antenna state | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GPS_ANTENNA_DISCONNECTED`<br>1 = `GPS_ANTENNA_UNKNOWN`<br>2 = `GPS_ANTENNA_CONNECTED` | plausible |
| `APSB_arbState` | APSB ECU: arb state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARB_STATE_N_INIT`<br>1 = `ARB_STATE_N_IDLE`<br>2 = `ARB_STATE_N_PRIMARY`<br>3 = `ARB_STATE_N_SECONDARY`<br>4 = `ARB_STATE_N_FAULT`<br>5 = `ARB_STATE_N_MIA`<br>6 = `ARB_STATE_N_UNKNOWN`<br>7 = `ARB_STATE_N_COUNT` | plausible |
| `APSB_socPowerOperatingMode` | APSB ECU: soc power operating mode | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `APS_UNKNOWN`<br>1 = `APS_SINGLE_SOC`<br>2 = `APS_DUAL_SOC` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
