---
layout: default
title: "DI_locStatus (0x286) — Drive inverter, Tesla Model Y 2025.20.8 PARTY CAN"
description: "Drive inverter message: loc status. Tesla Model Y CAN bus message DI_locStatus (0x286) of Drive inverter, firmware 2025.20.8, 17 signals (DI_locStatusChecksum, DI_locStatusCounter, DI_cruiseState, DI_cruiseSetSpeed and 13 more). Bit layout, scaling, units and value tables."
---

# DI_locStatus (0x286) — Drive inverter, Tesla Model Y 2025.20.8 PARTY CAN

Drive inverter message: loc status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 17 signals of DI_locStatus as defined for Tesla Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_locStatus` |
| CAN id | 0x286 (646) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 17 |

## Signals of DI_locStatus

Tesla Model Y CAN bus signals in `DI_locStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_locStatusChecksum` | Drive inverter: loc status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DI_locStatusCounter` | Drive inverter: loc status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_cruiseState` | Cruise control state. | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CRS_STATE_UNAVAILABLE`<br>1 = `CRS_STATE_STANDBY`<br>2 = `CRS_STATE_ENABLED`<br>3 = `CRS_STATE_STANDSTILL`<br>4 = `CRS_STATE_OVERRIDE`<br>5 = `CRS_STATE_FAULT`<br>6 = `CRS_STATE_PRE_FAULT`<br>7 = `CRS_STATE_PRE_CANCEL` | validated |
| `DI_cruiseSetSpeed` | Cruise control set point. | 15\|9 | little-endian | unsigned | 0.5 | 0 | speed | 0 to 255.5 |  | validated |
| `DI_cruiseSetSpeedUnits` | Drive inverter: cruise set speed units | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DI_SPEED_MPH`<br>1 = `DI_SPEED_KPH` | validated |
| `DI_autoparkState` | Drive inverter: autopark state; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `DI_APC_UNAVAILABLE`<br>1 = `DI_APC_STANDBY`<br>2 = `DI_APC_STARTED`<br>3 = `DI_APC_ACTIVE`<br>4 = `DI_APC_COMPLETE`<br>5 = `DI_APC_PAUSED`<br>6 = `DI_APC_ABORTED`<br>7 = `DI_APC_RESUMED`<br>8 = `DI_APC_UNPARK_COMPLETE`<br>9 = `DI_APC_SELFPARK_STARTED`<br>15 = `DI_APC_SNA` | validated |
| `DI_parkBrakeState` | DI Park Brake control and EPB interface state; raw 15 = signal not available (SNA) | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `DI_PBRK_UNAVAILABLE`<br>1 = `DI_PBRK_RELEASED`<br>2 = `DI_PBRK_REQUESTED`<br>3 = `DI_PBRK_APPLIED`<br>4 = `DI_PBRK_FAULTED`<br>5 = `DI_PBRK_PANIC_EPB`<br>6 = `DI_PBRK_PANIC_SKID`<br>7 = `DI_PBRK_RELEASING`<br>15 = `DI_PBRK_SNA` | validated |
| `DI_aebState` | Reports the Automatic Emergency Braking (AEB) state; raw 7 = signal not available (SNA) | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `AEB_CAN_STATE_UNAVAILABLE`<br>1 = `AEB_CAN_STATE_STANDBY`<br>2 = `AEB_CAN_STATE_ENABLED`<br>3 = `AEB_CAN_STATE_STANDSTILL`<br>4 = `AEB_CAN_STATE_FAULT`<br>5 = `AEB_CAN_STATE_UNAVAILABLE_ALERT`<br>7 = `AEB_CAN_STATE_SNA` | validated |
| `DI_loncDeactivationReason` | Drive inverter: lonc deactivation reason | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_CANCEL`<br>1 = `USER_CANCEL`<br>2 = `DAS_CANCEL`<br>3 = `ABORT` | validated |
| `DI_vehicleHoldState` | Vehicle hold state. | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_VHLD_STATE_UNAVAILABLE`<br>1 = `DI_VHLD_STATE_STANDBY`<br>2 = `DI_VHLD_STATE_BLEND_IN`<br>3 = `DI_VHLD_STATE_STANDSTILL`<br>4 = `DI_VHLD_STATE_BLEND_OUT`<br>5 = `DI_VHLD_STATE_PARK`<br>6 = `DI_VHLD_STATE_FAULT`<br>7 = `DI_VHLD_STATE_INIT` | validated |
| `DI_summonInPanic` | Drive inverter: summon in panic | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_onePedalDrivingState` | One Pedal Driving State machine state | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DI_OPD_UNAVAILABLE`<br>1 = `DI_OPD_QUICK_BRAKE_RAMP`<br>2 = `DI_OPD_STANDBY`<br>3 = `DI_OPD_NOMINAL`<br>4 = `DI_OPD_MOTOR_BLEND_OUT_PENDING`<br>5 = `DI_OPD_MOTOR_BLEND_OUT_ACTIVE`<br>6 = `DI_OPD_NO_MOTOR`<br>7 = `DI_OPD_MOTOR_BLEND_IN`<br>8 = `DI_OPD_NUM_STATES` | validated |
| `DI_brakeStandActive` | Detects active brake stand. | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_regenBackfillState` | Regen backfill state | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BFILL_UNAVAILABLE`<br>1 = `BFILL_STANDBY`<br>2 = `BFILL_ACTIVE` | validated |
| `DI_cruiseNotAvailableReason` | Drive inverter: cruise not available reason; raw 20 = signal not available (SNA) | 49\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `DI_CRUISE_NOT_AVAILABLE_NONE`<br>1 = `DI_CRUISE_NOT_AVAILABLE_NO_ALERT`<br>2 = `DI_CRUISE_NOT_AVAILABLE_VDC_OR_TC_OFF`<br>3 = `DI_CRUISE_NOT_AVAILABLE_VDC_ACTIVE_OR_DEGRADED`<br>4 = `DI_CRUISE_NOT_AVAILABLE_TC_ACTIVE`<br>5 = `DI_CRUISE_NOT_AVAILABLE_ABS_ACTIVE`<br>6 = `DI_CRUISE_NOT_AVAILABLE_ACC_CANCEL`<br>7 = `DI_CRUISE_NOT_AVAILABLE_CLOSURE_OPEN`<br>8 = `DI_CRUISE_NOT_AVAILABLE_SEAT_BELT_UNBUCKLED`<br>9 = `DI_CRUISE_NOT_AVAILABLE_VALET_MODE`<br>10 = `DI_CRUISE_NOT_AVAILABLE_EBR`<br>11 = `DI_CRUISE_NOT_AVAILABLE_MOTOR_SPEED`<br>12 = `DI_CRUISE_NOT_AVAILABLE_DI_STATE`<br>13 = `DI_CRUISE_NOT_AVAILABLE_CONFIG`<br>14 = `DI_CRUISE_NOT_AVAILABLE_AEB`<br>15 = `DI_CRUISE_NOT_AVAILABLE_MIN_SPEED`<br>16 = `DI_CRUISE_NOT_AVAILABLE_MAX_SPEED`<br>17 = `DI_CRUISE_NOT_AVAILABLE_VEL_EST`<br>18 = `DI_CRUISE_NOT_AVAILABLE_WAIT_INIT`<br>19 = `DI_CRUISE_NOT_AVAILABLE_UI_MIA`<br>20 = `DI_CRUISE_NOT_AVAILABLE_DAS_SNA`<br>21 = `DI_CRUISE_NOT_AVAILABLE_TRACK_MODE_ACTIVE`<br>22 = `DI_CRUISE_NOT_AVAILABLE_CRUISE_FAULTED`<br>23 = `DI_CRUISE_NOT_AVAILABLE_VHLD_UNAVAILABLE`<br>24 = `DI_CRUISE_NOT_AVAILABLE_MOTOR_SPEED_TOO_HIGH_IN_REVERSE`<br>25 = `DI_CRUISE_NOT_AVAILABLE_DAS_SET_SPEED_TOO_HIGH_IN_REVERSE`<br>26 = `DI_CRUISE_NOT_AVAILABLE_ACC_BACKWARD_AT_HIGH_FORWARD_SPEED`<br>27 = `DI_CRUISE_NOT_AVAILABLE_BRAKE_TEMPERATURE`<br>28 = `DI_CRUISE_NOT_AVAILABLE_UNIT0_FAULT`<br>29 = `DI_CRUISE_NOT_AVAILABLE_DAS_CONTROL_MIA`<br>30 = `DI_CRUISE_NOT_AVAILABLE_OFFROAD_MODE_ACTIVE`<br>31 = `DI_CRUISE_NOT_AVAILABLE_SHIFT_TIMEOUT`<br>32 = `DI_CRUISE_NOT_AVAILABLE_SHIFT_OUTSIDE_SPEED_THRESHOLD`<br>33 = `DI_CRUISE_NOT_AVAILABLE_CONTROL_STACK_SWITCH`<br>34 = `DI_CRUISE_NOT_AVAILABLE_CANCEL_ACTIVE`<br>35 = `DI_CRUISE_NOT_AVAILABLE_INTERFACE_NOT_SUPPORTED`<br>36 = `DI_CRUISE_NOT_AVAILABLE_DFLK_ENGAGED`<br>37 = `DI_CRUISE_NOT_AVAILABLE_AEB_STACK_EVENT_INACTIVE`<br>38 = `DI_CRUISE_NOT_AVAILABLE_AEB_STACK_UNAVAILABLE`<br>39 = `DI_CRUISE_NOT_AVAILABLE_EPB_FAULT`<br>40 = `DI_CRUISE_NOT_AVAILABLE_FACTORY_MODE`<br>41 = `DI_CRUISE_NOT_AVAILABLE_LONC_DEGRADED`<br>42 = `DI_CRUISE_NOT_AVAILABLE_ABS_UNAVAILABLE`<br>43 = `DI_CRUISE_NOT_AVAILABLE_REDUNDANT_BRAKES_ACTIVE`<br>44 = `DI_CRUISE_NOT_AVAILABLE_ACCEL_JERK_OUT_OF_ISO_BOUNDS`<br>45 = `DI_CRUISE_NOT_AVAILABLE_VDC_FAULT`<br>46 = `DI_CRUISE_NOT_AVAILABLE_SGS_REQUEST`<br>47 = `DI_CRUISE_NOT_AVAILABLE_EPB_DYNAMIC_APPLY`<br>48 = `DI_CRUISE_NOT_AVAILABLE_DRIVERLESS_AUTONOMY_BEHAVIOR`<br>49 = `DI_CRUISE_NOT_AVAILABLE_ABS_FAULT`<br>50 = `DI_CRUISE_NOT_AVAILABLE_AIR_COMPRESSOR_FAULT` | validated |
| `DI_cruiseFaultReason` | Cruise control fault reason; raw 17 = signal not available (SNA) | 55\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `DI_CRUISE_FAULT_NONE`<br>1 = `DI_CRUISE_FAULT_MOTOR_SPEED_MISMATCH`<br>2 = `DI_CRUISE_FAULT_PM_MIA`<br>3 = `DI_CRUISE_FAULT_PM_REQUEST`<br>4 = `DI_CRUISE_FAULT_STALK`<br>5 = `DI_CRUISE_FAULT_BRAKE_INVALID`<br>6 = `DI_CRUISE_FAULT_CRUISE_SCCM_MIA`<br>7 = `DI_CRUISE_FAULT_ABS_MIA`<br>8 = `DI_CRUISE_FAULT_CRS_STATE_MISM`<br>9 = `DI_CRUISE_FAULT_BRAKE_MIA`<br>10 = `DI_CRUISE_FAULT_EPB_FAULT`<br>11 = `DI_CRUISE_FAULT_VDC_FAULT`<br>12 = `DI_CRUISE_FAULT_ESP_MIA`<br>13 = `DI_CRUISE_FAULT_TC_FAULT`<br>14 = `DI_CRUISE_FAULT_EBR_FAULT`<br>15 = `DI_CRUISE_FAULT_ACCEL_OUT_OF_BOUNDS`<br>16 = `DI_CRUISE_FAULT_VELOCITY_ESTIMATE_NOT_NORMAL`<br>17 = `DI_CRUISE_FAULT_DAS_SNA`<br>19 = `DI_CRUISE_FAULT_ACCEL_JERK_OUT_OF_ISO_BOUNDS`<br>20 = `DI_CRUISE_FAULT_EPB_MIA`<br>21 = `DI_CRUISE_FAULT_CONFIG_MISMATCH`<br>22 = `DI_CRUISE_FAULT_VHLD_FAULTED` | validated |
| `DI_cruiseCancelReason` | Cruise control cancel reason | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DI_CRUISE_CANCEL_NONE`<br>1 = `DI_CRUISE_CANCEL_APC_REQUEST`<br>2 = `DI_CRUISE_CANCEL_SKID`<br>3 = `DI_CRUISE_CANCEL_BRAKE`<br>4 = `DI_CRUISE_CANCEL_STALK`<br>5 = `DI_CRUISE_CANCEL_GEAR`<br>6 = `DI_CRUISE_CANCEL_PARK`<br>7 = `DI_CRUISE_CANCEL_DAS`<br>8 = `DI_CRUISE_CANCEL_ACCEL_OVERRIDE_IN_REVERSE`<br>9 = `DI_CRUISE_CANCEL_SHIFT_REQUEST`<br>10 = `DI_CRUISE_CANCEL_ACC_FSD_EXIT`<br>11 = `DI_CRUISE_CANCEL_DAS_MIA_PEDAL_APPLY` | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/ModelY/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
