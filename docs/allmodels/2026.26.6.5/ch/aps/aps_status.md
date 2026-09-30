---
layout: default
title: "APS_status (0x3C9) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: status. Tesla Model 3 / Model Y CAN bus message APS_status (0x3C9) of Driver assistance computer (secondary), firmware 2026.26.6.5, 23 signals (APS_appStatusMonitorState, APS_vehBehaviorState, APS_canMaster, APS_appGpioState and 19 more). Bit layout, scaling, units and value tables."
---

# APS_status (0x3C9) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 23 signals of APS_status as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_status` |
| CAN id | 0x3C9 (969) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 23 |

## Signals of APS_status

Tesla Model 3 / Model Y CAN bus signals in `APS_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_appStatusMonitorState` | The current status of APE, indicates the health of the stack on the APE | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_MONITOR_STATE_UNKNOWN`<br>1 = `STATUS_MONITOR_STATE_PWR_OFF`<br>2 = `STATUS_MONITOR_STATE_INIT`<br>3 = `STATUS_MONITOR_STATE_NOMINAL`<br>4 = `STATUS_MONITOR_STATE_CRITICAL`<br>5 = `STATUS_MONITOR_STATE_SHUTTING_DOWN`<br>6 = `STATUS_MONITOR_STATE_RECOVERY`<br>7 = `STATUS_MONITOR_NUM_STATES` | validated |
| `APS_vehBehaviorState` | Driver assistance computer (secondary): veh behavior state | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `VEH_BEHAVIOR_STATE_UNKNOWN`<br>1 = `VEH_BEHAVIOR_STATE_APS_AVAILABLE`<br>2 = `VEH_BEHAVIOR_STATE_APS_CONTROL`<br>3 = `VEH_BEHAVIOR_STATE_APS_BRIDGE_APP`<br>4 = `VEH_BEHAVIOR_STATE_APS_BRIDGE_APB`<br>5 = `VEH_BEHAVIOR_STATE_APS_FAIL_SAFE`<br>6 = `VEH_BEHAVIOR_STATE_APS_OVERRIDE`<br>7 = `VEH_BEHAVIOR_STATE_SYSTEM_FAULT`<br>8 = `VEH_BEHAVIOR_NUM_STATES` | validated |
| `APS_canMaster` | Indicates which of the autopilot computers is currently controlling outgoing CAN traffic; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CAN_MASTER_APS`<br>1 = `CAN_MASTER_APP`<br>2 = `CAN_MASTER_APB`<br>3 = `CAN_MASTER_SNA` | validated |
| `APS_appGpioState` | The GPIO state of APEA, indicates the health of the primary Parker (HW2 and HW2.5) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_GPIO_STATE_PWR_DOWN_REBOOT`<br>1 = `AP_GPIO_STATE_DISABLED`<br>2 = `AP_GPIO_STATE_CRITICAL`<br>3 = `AP_GPIO_STATE_HEALTHY` | validated |
| `APS_eacInternalState` | Indicates the internal state of the external angle control monitor running on Aurix. | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_EAC_STATE_INIT`<br>1 = `APS_EAC_STATE_MOMENTARY`<br>2 = `APS_EAC_STATE_CONTINUOUS`<br>3 = `APS_EAC_STATE_AUTOPARK`<br>4 = `APS_EAC_STATE_INHIBIT`<br>5 = `APS_EAC_STATE_OVERRIDE`<br>6 = `APS_EAC_STATE_LSS`<br>7 = `APS_EAC_NUM_STATES` | validated |
| `APS_switchState` | Driver assistance computer (secondary): switch state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APS_apbStatusMonitorState` | The current status of APEB, indicates the health of the stack on the APEB | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_MONITOR_STATE_UNKNOWN`<br>1 = `STATUS_MONITOR_STATE_PWR_OFF`<br>2 = `STATUS_MONITOR_STATE_INIT`<br>3 = `STATUS_MONITOR_STATE_NOMINAL`<br>4 = `STATUS_MONITOR_STATE_CRITICAL`<br>5 = `STATUS_MONITOR_STATE_SHUTTING_DOWN`<br>6 = `STATUS_MONITOR_STATE_RECOVERY`<br>7 = `STATUS_MONITOR_NUM_STATES` | validated |
| `APS_apbGpioState` | The GPIO state of APEB, indicates the health of the secondary Parker (HW2.5 only) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_GPIO_STATE_PWR_DOWN_REBOOT`<br>1 = `AP_GPIO_STATE_DISABLED`<br>2 = `AP_GPIO_STATE_CRITICAL`<br>3 = `AP_GPIO_STATE_HEALTHY` | validated |
| `APS_statusCounter` | Driver assistance computer (secondary): status counter | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `APS_locLimitReason` | Indicates why longitudinal control limits are currently not relaxed | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOMINAL_DEFAULT`<br>1 = `NOT_IN_DRIVE`<br>2 = `ACC_AND_AEB_UNAVAILABLE`<br>3 = `PRIMARY_AP_NOT_HEALTHY`<br>4 = `RADAR_NOT_HEALTHY`<br>5 = `NO_RADAR_TARGET`<br>6 = `LOC_MONITOR_UNAVAILABLE`<br>7 = `LOC_LIMITS_EXTENDED` | validated |
| `APS_appPowerStateRequest` | Indicates ap primary power state request | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_POWER_STATE_NOMINAL`<br>1 = `AP_POWER_STATE_SENTRY`<br>2 = `AP_POWER_STATE_SUSPEND`<br>3 = `AP_POWER_STATE_SLEEP` | validated |
| `APS_appPowerStateReason` | Indicates ap primary power state reason | 31\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UI_POWER_STATE_REQUEST`<br>1 = `AP_WDOG_UNHEALTHY`<br>2 = `AP_NM_REASON_SET`<br>3 = `AP_NOT_IN_PARK`<br>4 = `GTW_GOTO_FULL_POWER`<br>5 = `AP_POWER_REQUEST_HYSTERESIS`<br>6 = `AP_POWER_REQUEST_OVERHEATING`<br>7 = `AP_POWER_REQUEST_OVERRIDE`<br>8 = `VC_POWER_REQUEST`<br>9 = `LOADSHED_POWER_REQUEST_PENDING`<br>10 = `AP_POWER_REQUEST_OVERHEATED`<br>11 = `SLEEP_REQUEST_RECVD`<br>12 = `UI_SUMMON_STANDBY_MODE_ENABLED` | validated |
| `APS_apbPowerStateRequest` | Indicates ap backup power state request | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AP_POWER_STATE_NOMINAL`<br>1 = `AP_POWER_STATE_SENTRY`<br>2 = `AP_POWER_STATE_SUSPEND`<br>3 = `AP_POWER_STATE_SLEEP` | validated |
| `APS_apbPowerStateReason` | Indicates ap backup power state reason | 37\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UI_POWER_STATE_REQUEST`<br>1 = `AP_WDOG_UNHEALTHY`<br>2 = `AP_NM_REASON_SET`<br>3 = `AP_NOT_IN_PARK`<br>4 = `GTW_GOTO_FULL_POWER`<br>5 = `AP_POWER_REQUEST_HYSTERESIS`<br>6 = `AP_POWER_REQUEST_OVERHEATING`<br>7 = `AP_POWER_REQUEST_OVERRIDE`<br>8 = `VC_POWER_REQUEST`<br>9 = `LOADSHED_POWER_REQUEST_PENDING`<br>10 = `AP_POWER_REQUEST_OVERHEATED`<br>11 = `SLEEP_REQUEST_RECVD`<br>12 = `UI_SUMMON_STANDBY_MODE_ENABLED` | validated |
| `APS_heaterStateDebug` | Driver assistance computer (secondary): heater state debug; raw 7 = signal not available (SNA) | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `APS_HEATER_OFF`<br>1 = `APS_HEATER_ON_HEATING`<br>2 = `APS_HEATER_ON_NOT_HEATING`<br>3 = `APS_HEATER_FAULT_OPEN`<br>4 = `APS_HEATER_FAULT_SHORT`<br>7 = `APS_HEATER_SNA` | validated |
| `APS_autosummonCounter` | Driver assistance computer (secondary): autosummon counter | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `APS_autosummonAlert` | Driver assistance computer (secondary): autosummon alert | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APS_gpsAntennaState` | Driver assistance computer (secondary): gps antenna state | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GPS_ANTENNA_DISCONNECTED`<br>1 = `GPS_ANTENNA_UNKNOWN`<br>2 = `GPS_ANTENNA_CONNECTED` | validated |
| `APS_arbState` | Reports the state of the arbitration state machine of this System on Chip (SoC). | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARB_STATE_N_INIT`<br>1 = `ARB_STATE_N_IDLE`<br>2 = `ARB_STATE_N_PRIMARY`<br>3 = `ARB_STATE_N_SECONDARY`<br>4 = `ARB_STATE_N_FAULT`<br>5 = `ARB_STATE_N_MIA`<br>6 = `ARB_STATE_N_UNKNOWN`<br>7 = `ARB_STATE_N_COUNT` | validated |
| `APS_socPowerOperatingMode` | Reports the total number of System on Chips (SoCs) that are powered on to provide support for active Autopilot features. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `APS_UNKNOWN`<br>1 = `APS_SINGLE_SOC`<br>2 = `APS_DUAL_SOC` | validated |
| `APS_otherArbState` | Reports the state of the arbitration state machine of the other System on Chip (SoC). Lets the current SoC know the state of the other SoC to achieve safer operations. | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARB_STATE_N_INIT`<br>1 = `ARB_STATE_N_IDLE`<br>2 = `ARB_STATE_N_PRIMARY`<br>3 = `ARB_STATE_N_SECONDARY`<br>4 = `ARB_STATE_N_FAULT`<br>5 = `ARB_STATE_N_MIA`<br>6 = `ARB_STATE_N_UNKNOWN`<br>7 = `ARB_STATE_N_COUNT` | validated |
| `APS_appActivePlannerType` | Driver assistance computer (secondary): app active planner type | 58\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_PLANNER`<br>1 = `AUTOSTEER_MON`<br>2 = `FIXED_PLANNER`<br>3 = `EMERGENCY_PLANNER`<br>4 = `BOOT_FIXED_PLANNER` | validated |
| `APS_apbActivePlannerType` | Driver assistance computer (secondary): apb active planner type | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_PLANNER`<br>1 = `AUTOSTEER_MON`<br>2 = `FIXED_PLANNER`<br>3 = `EMERGENCY_PLANNER`<br>4 = `BOOT_FIXED_PLANNER` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
