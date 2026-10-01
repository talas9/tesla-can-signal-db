---
layout: default
title: "EPBL_internalStatus (0x288) — Left electric parking brake, Tesla Model Y 2025.20.8 VEH CAN"
description: "Left electric parking brake message: internal status. Tesla Model Y CAN bus message EPBL_internalStatus (0x288) of Left electric parking brake, firmware 2025.20.8, 19 signals (EPBL_unitStatus, EPBL_unitFaultStatus, EPBL_summonState, EPBL_disconnected and 15 more). Bit layout, scaling, units and value tables."
---

# EPBL_internalStatus (0x288) — Left electric parking brake, Tesla Model Y 2025.20.8 VEH CAN

Left electric parking brake message: internal status; frame length observed on a vehicle bus. This page documents the 19 signals of EPBL_internalStatus as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBL_internalStatus` |
| CAN id | 0x288 (648) |
| ECU | [Left electric parking brake](../../epbl.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBL |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 19 |

## Signals of EPBL_internalStatus

Tesla Model Y CAN bus signals in `EPBL_internalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBL_unitStatus` | Electronic Parking Brake's unit state. | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_STATUS_UNKNOWN`<br>1 = `EPB_STATUS_OPEN`<br>2 = `EPB_STATUS_DYNAMIC`<br>3 = `EPB_STATUS_PARK`<br>4 = `EPB_STATUS_START`<br>5 = `EPB_STATUS_SERVICE`<br>6 = `EPB_STATUS_WINCHMODE`<br>7 = `EPB_STATUS_WINCHMODE_RELEASING`<br>8 = `EPB_STATUS_PARKING`<br>9 = `EPB_STATUS_DYNAMIC_APPLYING`<br>10 = `EPB_STATUS_RELEASING`<br>11 = `EPB_STATUS_SERVICE_RELEASING`<br>12 = `EPB_STATUS_PARK_PENDING`<br>13 = `EPB_STATUS_WINCHMODE_PENDING`<br>14 = `EPB_STATUS_SUMMON`<br>15 = `EPB_STATUS_SUMMON_RELEASING`<br>16 = `EPB_STATUS_SUMMON_PARKING`<br>17 = `EPB_STATUS_EXTERNAL_DYNAMIC`<br>18 = `EPB_STATUS_RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EPB_STATUS_EXTERNAL_PARKING`<br>20 = `EPB_STATUS_DYNAMIC_PARKING`<br>21 = `EPB_STATUS_FREE_ROLL_MODE`<br>22 = `EPB_STATUS_AUTONOMY_OPEN`<br>23 = `EPB_STATUS_COUNT` | plausible |
| `EPBL_unitFaultStatus` | Left electric parking brake: unit fault status | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_STATUS_NOMINAL`<br>1 = `EPB_STATUS_RETRY`<br>2 = `EPB_STATUS_FAULT`<br>3 = `EPB_STATUS_FAULT_IDLE` | plausible |
| `EPBL_summonState` | Left electric parking brake: summon state | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_SUMMON_INIT`<br>1 = `EPB_SUMMON_IDLE`<br>2 = `EPB_SUMMON_ARMED`<br>3 = `EPB_SUMMON_ACTIVE`<br>4 = `EPB_SUMMON_COMPLETE`<br>5 = `EPB_SUMMON_FAULT`<br>6 = `EPB_SUMMON_UNAVAILABLE` | plausible |
| `EPBL_disconnected` | Left electric parking brake: disconnected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBL_pistonTouchingRotor` | Left electric parking brake: piston touching rotor | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBL_csmFaultReason` | Left electric parking brake: csm fault reason | 13\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CSM_FAULT_NONE`<br>1 = `CSM_FAULT_EPBM_DISABLED`<br>2 = `CSM_FAULT_EPBM_FAULTED`<br>3 = `CSM_FAULT_STATE_MISMATCH`<br>4 = `CSM_FAULT_TIMEOUT_CALIBRATE`<br>5 = `CSM_FAULT_APPLY_BLOCKED`<br>6 = `CSM_FAULT_RELEASE_BLOCKED`<br>7 = `CSM_FAULT_TIMEOUT_APPLY_COMPLETE`<br>8 = `CSM_FAULT_TIMEOUT_APPLY_INRUSH`<br>9 = `CSM_FAULT_TIMEOUT_EPB_WAIT_FOR_CLAMP`<br>10 = `CSM_FAULT_TIMEOUT_EPBM_WAIT_FOR_CLAMP`<br>11 = `CSM_FAULT_TIMEOUT_RELEASE_INRUSH`<br>12 = `CSM_FAULT_TIMEOUT_RELEASE_WAIT_FOR_ENDSTOP`<br>13 = `CSM_FAULT_TIMEOUT_RELEASE_NO_LOAD`<br>14 = `CSM_FAULT_TIMEOUT_RELEASE_COMPLETE`<br>15 = `CSM_FAULT_TIMEOUT_EPBM_CUTOFF`<br>16 = `CSM_FAULT_TIMEOUT_NO_RAMP`<br>17 = `CSM_FAULT_TIMEOUT_EPBM_START`<br>18 = `CSM_FAULT_MOTOR_IDLE_FAULT`<br>19 = `CSM_FAULT_MOTOR_ACTIVE_FAULT`<br>20 = `CSM_FAULT_MOTOR_NOT_READY`<br>21 = `CSM_FAULT_EPBM_MIA`<br>22 = `CSM_FAULT_NVM_MISMATCH`<br>23 = `CSM_FAULT_REMOTE_MIA` | plausible |
| `EPBL_esmOperationTrigger` | Left electric parking brake: esm operation trigger | 18\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `EPB_TRIGGER_PBUTTON_PRESSED_STOPPED`<br>1 = `EPB_TRIGGER_PBUTTON_PRESSED_OKTOPARK`<br>2 = `EPB_TRIGGER_PBUTTON_PRESSED_FAST`<br>3 = `EPB_TRIGGER_PBUTTON_PRESSED_UNKNOWN`<br>4 = `EPB_TRIGGER_PBUTTON_RELEASED`<br>5 = `EPB_TRIGGER_ACTIVE_PARK_REQUEST`<br>6 = `EPB_TRIGGER_DI_UNPARK`<br>7 = `EPB_TRIGGER_TOUCHSCREEN`<br>8 = `EPB_TRIGGER_WINCHMODE_EXIT`<br>9 = `EPB_TRIGGER_WINCHMODE_ENTER`<br>10 = `EPB_TRIGGER_WINCHMODE_UNAVAILABLE`<br>11 = `EPB_TRIGGER_SERVICE`<br>12 = `EPB_TRIGGER_DIAG_CLOSE`<br>13 = `EPB_TRIGGER_DIAG_OPEN`<br>14 = `EPB_TRIGGER_DIAG_EXIT`<br>15 = `EPB_TRIGGER_USER_CONFIRMED`<br>16 = `EPB_TRIGGER_USER_CANCEL`<br>17 = `EPB_TRIGGER_SPEED_STOPPED`<br>18 = `EPB_TRIGGER_SPEED_OKAYTOPARK`<br>19 = `EPB_TRIGGER_SPEED_FAST`<br>20 = `EPB_TRIGGER_TIMEOUT`<br>21 = `EPB_TRIGGER_SAVESTATE_ON_BOOT`<br>22 = `EPB_TRIGGER_REAPPLY`<br>23 = `EPB_TRIGGER_SUMMON_COMPLETE`<br>24 = `EPB_TRIGGER_FAULT`<br>25 = `EPB_TRIGGER_SUMMON_FAULT`<br>26 = `EPB_TRIGGER_DISQUALIFIED`<br>27 = `EPB_TRIGGER_EPBM_DISQUALIFIED`<br>28 = `EPB_TRIGGER_ACCELERATION`<br>29 = `EPB_TRIGGER_SYSTEM_APPLY`<br>30 = `EPB_TRIGGER_DRIVER_IS_LEAVING`<br>31 = `EPB_TRIGGER_AUTOPARK_END`<br>32 = `EPB_TRIGGER_UI_DOOR_OPEN_REQUEST`<br>33 = `EPB_TRIGGER_TOUCHSCREEN_INVALID`<br>34 = `EPB_TRIGGER_STATIONARY_DETECT`<br>35 = `EPB_TRIGGER_LOW_BRAKE_FLUID_MODE_PARK`<br>36 = `EPB_TRIGGER_LOW_BRAKE_FLUID_MODE_DYNAMIC_PARK`<br>37 = `EPB_TRIGGER_LOW_BRAKE_FLUID_MODE_DYNAMIC`<br>38 = `EPB_TRIGGER_FREE_ROLL_PARK_FOR_HANDLE_PULLED`<br>39 = `EPB_TRIGGER_DI_PARK`<br>40 = `EPB_TRIGGER_CDP_PANIC_MODE_TIMEOUT`<br>41 = `EPB_TRIGGER_CDP_PANIC_MODE_READY`<br>42 = `EPB_TRIGGER_LV_ACTIVE_DECEL`<br>43 = `EPB_TRIGGER_STEERING_ACTIVE_DECEL`<br>44 = `EPB_TRIGGER_ACTIVE_DECEL_FAST`<br>45 = `EPB_TRIGGER_ACTIVE_DECEL_OKTOPARK`<br>46 = `EPB_TRIGGER_SPEED_SOURCES_LOST`<br>47 = `EPB_TRIGGER_RECOVERY_PARK`<br>48 = `EPB_TRIGGER_AP_IS_LEAVING`<br>49 = `EPB_TRIGGER_ACTIVE_DECEL_CDP_DOWN`<br>50 = `EPB_TRIGGER_ACTIVE_DECEL_DAS_STATIC` | plausible |
| `EPBL_summonFaultReason` | Error code associated with previous summon failure. | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_SUMMONFAULT_NONE`<br>1 = `EPB_SUMMONFAULT_DI_MIA`<br>2 = `EPB_SUMMONFAULT_DAS_MIA`<br>3 = `EPB_SUMMONFAULT_ESP_MIA`<br>4 = `EPB_SUMMONFAULT_EPBM_MIA`<br>5 = `EPB_SUMMONFAULT_DI_FAULT`<br>6 = `EPB_SUMMONFAULT_DI_APC_FAULT`<br>7 = `EPB_SUMMONFAULT_DAS_FAULT`<br>8 = `EPB_SUMMONFAULT_ESP_FAULT`<br>9 = `EPB_SUMMONFAULT_VEH_CAN_FAULT`<br>10 = `EPB_SUMMONFAULT_EAC_NOT_ALLOWED`<br>11 = `EPB_SUMMONFAULT_EPBM_REQUEST`<br>12 = `EPB_SUMMONFAULT_SPEED`<br>13 = `EPB_SUMMONFAULT_EXTERNAL`<br>14 = `EPB_SUMMONFAULT_PARK_MIA`<br>15 = `EPB_SUMMONFAULT_PM_MIA`<br>16 = `EPB_SUMMONFAULT_PM_REQUEST`<br>17 = `EPB_SUMMONFAULT_OOC`<br>18 = `EPB_SUMMONFAULT_MISMATCH`<br>19 = `EPB_SUMMONFAULT_EPB_FAULT`<br>20 = `EPB_SUMMONFAULT_DI_STATE_INVALID`<br>21 = `EPB_SUMMONFAULT_PASSIVE_REQUEST`<br>22 = `EPB_SUMMONFAULT_EPBREMOTE_MIA`<br>23 = `EPB_SUMMONFAULT_REMOTE_SUMMON_FAULTED`<br>24 = `EPB_SUMMONFAULT_LOCAL_UNIT_FAULTED`<br>25 = `EPB_SUMMONFAULT_REMOTE_UNIT_FAULTED`<br>26 = `EPB_SUMMONFAULT_START_IN_UNAVAILABLE`<br>27 = `EPB_SUMMONFAULT_INVALID_REMOTE_STATE`<br>28 = `EPB_SUMMONFAULT_REMOTE_DID_NOT_START`<br>29 = `EPB_SUMMONFAULT_AP_MONITOR`<br>30 = `EPB_SUMMONFAULT_MONITOR_TYPE_UNKNOWN` | plausible |
| `EPBL_localServiceModeActive` | Signal reported by Left electric parking brake | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBL_localCdpState` | Left electric parking brake: local cdp state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_CDP_STATE_UNKNOWN`<br>1 = `EPB_CDP_STATE_VALID`<br>2 = `EPB_CDP_STATE_FAULT` | plausible |
| `EPBL_chimeRequestLocal` | Left electric parking brake: chime request local | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_CHIME_REQUEST_NONE`<br>1 = `EPB_CHIME_REQUEST_GENERAL`<br>2 = `EPB_CHIME_REQUEST_GPO`<br>3 = `EPB_CHIME_REQUEST_ABOUT_TO_ACTIVE_DECEL`<br>4 = `EPB_CHIME_REQUEST_ACTIVE_DECEL` | plausible |
| `EPBL_telltaleLocal` | Left electric parking brake: telltale local; raw 7 = signal not available (SNA) | 39\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `EPB_TELLTALE_LAMP_OFF`<br>1 = `EPB_TELLTALE_LAMP_RED_PARKED`<br>2 = `EPB_TELLTALE_LAMP_RED_ON`<br>3 = `EPB_TELLTALE_LAMP_AMBER_ON`<br>4 = `EPB_TELLTALE_LAMP_RED_FLASH`<br>7 = `EPB_TELLTALE_SNA` | plausible |
| `EPBL_driverIsLeavingLocal` | Left electric parking brake: driver is leaving local | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBL_driverIsLeavingAnySpeedLocal` | Left electric parking brake: driver is leaving any speed local | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBL_internalCDPRequest` | Left electric parking brake: internal CDP request | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPB_CDP_NOT_REQUESTED`<br>1 = `EPB_CDP_REQUESTED` | plausible |
| `EPBL_esmSpeedClass` | Left electric parking brake: esm speed class | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ESM_SPEED_CLASS_STOPPED`<br>1 = `ESM_SPEED_CLASS_SYSTEM_APPLY_OK`<br>2 = `ESM_SPEED_CLASS_USER_APPLY_OK`<br>3 = `ESM_SPEED_CLASS_FAST`<br>4 = `ESM_SPEED_CLASS_UNKNOWN` | plausible |
| `EPBL_learnedEpbConfig` | Left electric parking brake: learned epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `EPB_CONFIG_UNKNOWN`<br>1 = `EPB_CONFIG_MODEL3_BASE`<br>2 = `EPB_CONFIG_MODEL3_PERFORMANCE`<br>3 = `EPB_CONFIG_MODELS_BASE`<br>4 = `EPB_CONFIG_MODELY_BASE`<br>5 = `EPB_CONFIG_MODELY_PERFORMANCE`<br>6 = `EPB_CONFIG_MODELX_BASE`<br>7 = `EPB_CONFIG_MODEL3_PERFORMANCE_V2`<br>8 = `EPB_CONFIG_MODELY_PERFORMANCE_V2`<br>9 = `EPB_CONFIG_MODELS_CERAMIC`<br>10 = `EPB_CONFIG_MODEL3_ZF`<br>11 = `EPB_CONFIG_CT_MANDO` | plausible |
| `EPBL_internalStatusCounter` | Left electric parking brake: internal status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `EPBL_internalStatusChecksum` | Left electric parking brake: internal status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Left electric parking brake messages (EPBL)](../../epbl.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
