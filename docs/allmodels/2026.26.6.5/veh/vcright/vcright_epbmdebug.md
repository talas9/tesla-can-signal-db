---
layout: default
title: "VCRIGHT_epbmDebug (0x393) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: epbm debug. Tesla Model 3 / Model Y CAN bus message VCRIGHT_epbmDebug (0x393) of Right body controller, firmware 2026.26.6.5, 14 signals (VCRIGHT_epbmDebugIndex, VCRIGHT_epbmCaliperState, VCRIGHT_epbmMotorEnabled, VCRIGHT_epbMotorCurrent and 10 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_epbmDebug (0x393) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Right body controller message: epbm debug; frame length observed on a vehicle bus. This page documents the 14 signals of VCRIGHT_epbmDebug as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_epbmDebug` |
| CAN id | 0x393 (915) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of VCRIGHT_epbmDebug

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_epbmDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_epbmDebugIndex` | selector | Right body controller: epbm debug index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STATES`<br>1 = `TRANSITIONS` | validated |
| `VCRIGHT_epbmCaliperState` | page 0 | Right body controller: epbm caliper state | 1\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_SAVED_CALIPERSTATE_UNSAVED`<br>1 = `EPB_SAVED_CALIPERSTATE_UNKNOWN`<br>2 = `EPB_SAVED_CALIPERSTATE_REAPPLY`<br>3 = `EPB_SAVED_CALIPERSTATE_PARK`<br>4 = `EPB_SAVED_CALIPERSTATE_OPEN`<br>5 = `EPB_SAVED_CALIPERSTATE_SERVICE`<br>6 = `EPB_SAVED_CALIPERSTATE_WINCHMODE` | validated |
| `VCRIGHT_epbmMotorEnabled` | page 0 | Right body controller: epbm motor enabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_epbMotorCurrent` | page 0 | Right body controller: epb motor current | 5\|11 | little-endian | unsigned | 0.01 | 0 | A | 0 to 20.47 |  | validated |
| `VCRIGHT_epbmApplyVoltage` | page 0 | Right body controller: epbm apply voltage | 16\|11 | little-endian | unsigned | 0.01 | 0 | A | 0 to 20.47 |  | validated |
| `VCRIGHT_epbmReleaseVoltage` | page 0 | Right body controller: epbm release voltage | 27\|11 | little-endian | unsigned | 0.01 | 0 | A | 0 to 20.47 |  | validated |
| `VCRIGHT_summonFaultReason` | page 0 | Electronic Parking Brake Monitors error code associated with previous summon failure. | 38\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_SUMMONFAULT_NONE`<br>1 = `EPB_SUMMONFAULT_DI_MIA`<br>2 = `EPB_SUMMONFAULT_DAS_MIA`<br>3 = `EPB_SUMMONFAULT_ESP_MIA`<br>4 = `EPB_SUMMONFAULT_EPBM_MIA`<br>5 = `EPB_SUMMONFAULT_DI_FAULT`<br>6 = `EPB_SUMMONFAULT_DI_APC_FAULT`<br>7 = `EPB_SUMMONFAULT_DAS_FAULT`<br>8 = `EPB_SUMMONFAULT_ESP_FAULT`<br>9 = `EPB_SUMMONFAULT_VEH_CAN_FAULT`<br>10 = `EPB_SUMMONFAULT_EAC_NOT_ALLOWED`<br>11 = `EPB_SUMMONFAULT_EPBM_REQUEST`<br>12 = `EPB_SUMMONFAULT_SPEED`<br>13 = `EPB_SUMMONFAULT_EXTERNAL`<br>14 = `EPB_SUMMONFAULT_PARK_MIA`<br>15 = `EPB_SUMMONFAULT_PM_MIA`<br>16 = `EPB_SUMMONFAULT_PM_REQUEST`<br>17 = `EPB_SUMMONFAULT_OOC`<br>18 = `EPB_SUMMONFAULT_MISMATCH`<br>19 = `EPB_SUMMONFAULT_EPB_FAULT`<br>20 = `EPB_SUMMONFAULT_DI_STATE_INVALID`<br>21 = `EPB_SUMMONFAULT_PASSIVE_REQUEST`<br>22 = `EPB_SUMMONFAULT_EPBREMOTE_MIA`<br>23 = `EPB_SUMMONFAULT_REMOTE_SUMMON_FAULTED`<br>24 = `EPB_SUMMONFAULT_LOCAL_UNIT_FAULTED`<br>25 = `EPB_SUMMONFAULT_REMOTE_UNIT_FAULTED`<br>26 = `EPB_SUMMONFAULT_START_IN_UNAVAILABLE`<br>27 = `EPB_SUMMONFAULT_INVALID_REMOTE_STATE`<br>28 = `EPB_SUMMONFAULT_REMOTE_DID_NOT_START`<br>29 = `EPB_SUMMONFAULT_AP_MONITOR`<br>30 = `EPB_SUMMONFAULT_MONITOR_TYPE_UNKNOWN` | validated |
| `VCRIGHT_epbSummonState` | page 0 | Electronic Parking Brake Monitors reading of Electronic Parking Brake's summon state. | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_SUMMON_INIT`<br>1 = `EPB_SUMMON_IDLE`<br>2 = `EPB_SUMMON_ARMED`<br>3 = `EPB_SUMMON_ACTIVE`<br>4 = `EPB_SUMMON_COMPLETE`<br>5 = `EPB_SUMMON_FAULT`<br>6 = `EPB_SUMMON_UNAVAILABLE` | validated |
| `VCRIGHT_epbmSummonState` | page 0 | Electronic Parking Brake Monitors summon state. | 46\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_SUMMON_INIT`<br>1 = `EPB_SUMMON_IDLE`<br>2 = `EPB_SUMMON_ARMED`<br>3 = `EPB_SUMMON_ACTIVE`<br>4 = `EPB_SUMMON_COMPLETE`<br>5 = `EPB_SUMMON_FAULT`<br>6 = `EPB_SUMMON_UNAVAILABLE` | validated |
| `VCRIGHT_epbUnitStatus` | page 0 | Electronic Parking Brake Monitors reading of Electronic Parking Brake's state. | 49\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_STATUS_UNKNOWN`<br>1 = `EPB_STATUS_OPEN`<br>2 = `EPB_STATUS_DYNAMIC`<br>3 = `EPB_STATUS_PARK`<br>4 = `EPB_STATUS_START`<br>5 = `EPB_STATUS_SERVICE`<br>6 = `EPB_STATUS_WINCHMODE`<br>7 = `EPB_STATUS_WINCHMODE_RELEASING`<br>8 = `EPB_STATUS_PARKING`<br>9 = `EPB_STATUS_DYNAMIC_APPLYING`<br>10 = `EPB_STATUS_RELEASING`<br>11 = `EPB_STATUS_SERVICE_RELEASING`<br>12 = `EPB_STATUS_PARK_PENDING`<br>13 = `EPB_STATUS_WINCHMODE_PENDING`<br>14 = `EPB_STATUS_SUMMON`<br>15 = `EPB_STATUS_SUMMON_RELEASING`<br>16 = `EPB_STATUS_SUMMON_PARKING`<br>17 = `EPB_STATUS_EXTERNAL_DYNAMIC`<br>18 = `EPB_STATUS_RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EPB_STATUS_EXTERNAL_PARKING`<br>20 = `EPB_STATUS_DYNAMIC_PARKING`<br>21 = `EPB_STATUS_FREE_ROLL_MODE`<br>22 = `EPB_STATUS_AUTONOMY_OPEN`<br>23 = `EPB_STATUS_COUNT` | validated |
| `VCRIGHT_epbmFaultStatus` | page 0 | Electronic Parking Brake Monitors fault state. | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_STATUS_NOMINAL`<br>1 = `EPB_STATUS_RETRY`<br>2 = `EPB_STATUS_FAULT`<br>3 = `EPB_STATUS_FAULT_IDLE` | validated |
| `VCRIGHT_epbFaultStatus` | page 0 | Electronic Parking Brake Monitors reading of Electronic Parking Brake's fault state. | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_STATUS_NOMINAL`<br>1 = `EPB_STATUS_RETRY`<br>2 = `EPB_STATUS_FAULT`<br>3 = `EPB_STATUS_FAULT_IDLE` | validated |
| `VCRIGHT_epbmSystemStatus` | page 0 | Electronic Parking Brake Monitors reading of Electronic Parking Brake's state. | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `EPB_VEHICLE_STATUS_UNKNOWN`<br>1 = `EPB_VEHICLE_STATUS_RELEASED`<br>2 = `EPB_VEHICLE_STATUS_PARKED`<br>3 = `EPB_VEHICLE_STATUS_DYNAMIC`<br>4 = `EPB_VEHICLE_STATUS_PARKING`<br>5 = `EPB_VEHICLE_STATUS_RELEASING`<br>6 = `EPB_VEHICLE_STATUS_FAULT`<br>7 = `EPB_VEHICLE_STATUS_FAULT_SECURE`<br>8 = `EPB_VEHICLE_STATUS_MISMATCH` | validated |
| `VCRIGHT_epbmAutonomyBehavior` | page 0 | Right body controller: epbm autonomy behavior | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER` | validated |

## Multiplexing

`VCRIGHT_epbmDebugIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (13 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
