---
layout: default
title: "VCFRONT_status (0x2E1) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: status. Tesla Model Y CAN bus message VCFRONT_status (0x2E1) of Front body controller, firmware 2026.26.6.5, 86 signals (VCFRONT_statusIndex, VCFRONT_frunkLatchStatus, VCFRONT_wiperSpeed, VCFRONT_wiperPosition and 82 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_status (0x2E1) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: status; frame length observed on a vehicle bus. This page documents the 86 signals of VCFRONT_status as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_status` |
| CAN id | 0x2E1 (737) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 16 ms |
| Signals | 86 |

## Signals of VCFRONT_status

Tesla Model Y CAN bus signals in `VCFRONT_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_statusIndex` | selector | Front body controller: status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BODY_CONTROLS`<br>1 = `VEHICLE_STATE`<br>2 = `REFRIGERANT_SYSTEM`<br>3 = `SYSTEM_HEALTH`<br>4 = `THERMAL`<br>5 = `USER_PRESENCE`<br>6 = `INVALID` | validated |
| `VCFRONT_frunkLatchStatus` | page 0 | Front body controller: frunk latch status; raw 0 = signal not available (SNA) | 3\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `LATCH_SNA`<br>1 = `LATCH_OPENED`<br>2 = `LATCH_CLOSED`<br>3 = `LATCH_CLOSING`<br>4 = `LATCH_OPENING`<br>5 = `LATCH_AJAR`<br>6 = `LATCH_TIMEOUT`<br>7 = `LATCH_DEFAULT`<br>8 = `LATCH_FAULT` | validated |
| `VCFRONT_wiperSpeed` | page 0 | Front body controller: wiper speed; raw 0 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `WIPER_SPEED_SNA`<br>1 = `WIPER_SPEED_OFF`<br>2 = `WIPER_SPEED_1`<br>3 = `WIPER_SPEED_2`<br>4 = `WIPER_SPEED_3`<br>5 = `WIPER_SPEED_4`<br>6 = `WIPER_SPEED_5`<br>7 = `WIPER_SPEED_LOW`<br>8 = `WIPER_SPEED_HIGH`<br>9 = `WIPER_SPEED_NARROW` | validated |
| `VCFRONT_wiperPosition` | page 0 | Wiper position; raw 0 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `WIPER_POSITION_SNA`<br>1 = `WIPER_POSITION_SERVICE`<br>2 = `WIPER_POSITION_DEPRESSED_PARK`<br>3 = `WIPER_POSITION_DELAYED_REST`<br>4 = `WIPER_POSITION_WIPING` | validated |
| `VCFRONT_wiperBlocked` | page 0 | Wiper ECU is reporting a block | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_wiperState` | page 0 | Front body controller: wiper state; raw 0 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `WIPER_STATE_SNA`<br>1 = `WIPER_STATE_SERVICE`<br>2 = `WIPER_STATE_FAULT`<br>3 = `WIPER_STATE_DELAYED_REST`<br>4 = `WIPER_STATE_PARK`<br>5 = `WIPER_STATE_WASH`<br>6 = `WIPER_STATE_MOMENTARY_WIPE`<br>7 = `WIPER_STATE_INTERMITTENT_HIGH`<br>8 = `WIPER_STATE_INTERMITTENT_LOW`<br>9 = `WIPER_STATE_CONT_FAST`<br>10 = `WIPER_STATE_CONT_SLOW`<br>11 = `WIPER_STATE_INT_AUTO_LOW`<br>12 = `WIPER_STATE_INT_AUTO_HIGH`<br>13 = `WIPER_STATE_NARROW_WIPE`<br>14 = `WIPER_STATE_NARROW_WASH` | validated |
| `VCFRONT_crashDetectedType` | page 0 | Front body controller: crash detected type | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CRASH_DETECTED_TYPE_NONE`<br>1 = `CRASH_DETECTED_TYPE_MINOR_1`<br>2 = `CRASH_DETECTED_TYPE_MINOR_2`<br>3 = `CRASH_DETECTED_TYPE_SEVERE` | validated |
| `VCFRONT_crashState` | page 0 | Front body controller: crash state | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CRASH_STATE_IDLE`<br>1 = `CRASH_STATE_MINOR_1`<br>2 = `CRASH_STATE_MINOR_2`<br>3 = `CRASH_STATE_SEVERE` | validated |
| `VCFRONT_crashUnlockOverrideSet` | page 0 | Indication that vehicle lock state has been overridden due to a collision. | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_washPumpState` | page 0 | Front body controller: wash pump state; raw 1 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WASH_PUMP_BIDIRECTIONAL_STATE_OFF`<br>1 = `WASH_PUMP_BIDIRECTIONAL_STATE_DRIVING_PRIMARY`<br>2 = `WASH_PUMP_BIDIRECTIONAL_STATE_DRIVING_SECONDARY`<br>3 = `WASH_PUMP_BIDIRECTIONAL_STATE_SNA` | validated |
| `VCFRONT_turnIndicatorControlType` | page 0 | Turn indicator control hardware variant | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURN_INDICATOR_CONTROL_TYPE_UNKNOWN`<br>1 = `TURN_INDICATOR_CONTROL_TYPE_SINGLE_DETENT_STALK`<br>2 = `TURN_INDICATOR_CONTROL_TYPE_SWS_BUTTON` | validated |
| `VCFRONT_wiperHealth` | page 0 | Health metric to track the power and communication state of the wiper module | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WIPER_HEALTH_OFF`<br>1 = `WIPER_HEALTH_WAIT`<br>2 = `WIPER_HEALTH_OK`<br>3 = `WIPER_HEALTH_TIMEOUT`<br>4 = `WIPER_HEALTH_UPDATING`<br>5 = `WIPER_HEALTH_FAULT`<br>7 = `WIPER_HEALTH_RESERVED` | validated |
| `VCFRONT_wiperLINHealth` | page 0 | Health metric to track the power and communication state of the wiper module | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WIPER_HEALTH_OFF`<br>1 = `WIPER_HEALTH_WAIT`<br>2 = `WIPER_HEALTH_OK`<br>3 = `WIPER_HEALTH_TIMEOUT`<br>4 = `WIPER_HEALTH_UPDATING`<br>5 = `WIPER_HEALTH_FAULT`<br>7 = `WIPER_HEALTH_RESERVED` | validated |
| `VCFRONT_frunkLatchCurrent` | page 0 | Reports the current used by the frunk latch. | 40\|8 | little-endian | signed | 0.157480314374 | 0 | A | -10 to 10 |  | validated |
| `VCFRONT_frunkInteriorRelSwitch` | page 0 | State of the frunk interior release switch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_anyClosureOpen` | page 0 | Front body controller: any closure open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_anyDoorOpen` | page 0 | Front body controller: any door open | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hornOn` | page 0 | Indication that the horn is on | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radarHeaterState` | page 0 | Front body controller: radar heater state; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCFRONT_trunkExteriorWakeSwitch` | page 0 | State of the trunk exterior switch, used for wake only | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_passengerBuckleStatus` | page 0 | State of the passenger's seat belt buckle | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNBUCKLED`<br>1 = `BUCKLED` | validated |
| `VCFRONT_frunkLatchType` | page 0 | Front body controller: frunk latch type | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FRUNK_LATCH_TYPE_UNKNOWN`<br>1 = `FRUNK_LATCH_TYPE_DOUBLE_ACTUATOR`<br>2 = `FRUNK_LATCH_TYPE_DOUBLE_PULL` | validated |
| `VCFRONT_headlampLeftFanStatus` | page 0 | Front body controller: headlamp left fan status | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_headlampRightFanStatus` | page 0 | Front body controller: headlamp right fan status | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_frunkAccessPost` | page 0 | Front body controller: frunk access post | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isActiveHeatingBattery` | page 0 | Front body controller: is active heating battery | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_iBoosterWakeLine` | page 1 | Front body controller: i booster wake line | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_epasWakeLine` | page 1 | Front body controller: epas wake line | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_iBoosterStateDBG` | page 1 | Front body controller: i booster state DBG | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `IBOOSTER_OFF`<br>1 = `IBOOSTER_ON`<br>2 = `IBOOSTER_GOING_DOWN`<br>3 = `IBOOSTER_WRITING_DATA_SHUTDOWN`<br>4 = `IBOOSTER_FORCE_OFF` | validated |
| `VCFRONT_vehicleStatusDBG` | page 1 | Vehicle state machine state debug; raw 18 = signal not available (SNA) | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `VEHICLE_STATUS_INIT`<br>1 = `VEHICLE_STATUS_LOW_POWER_STANDBY`<br>2 = `VEHICLE_STATUS_SILENT_WAKE`<br>3 = `VEHICLE_STATUS_BATTERY_POST_WAKE`<br>4 = `VEHICLE_STATUS_SYSTEM_CHECKS`<br>5 = `VEHICLE_STATUS_SLEEP_SHUTDOWN`<br>6 = `VEHICLE_STATUS_SLEEP_STANDBY`<br>7 = `VEHICLE_STATUS_LV_SHUTDOWN`<br>8 = `VEHICLE_STATUS_LV_AWAKE`<br>9 = `VEHICLE_STATUS_HV_UP_STANDBY`<br>10 = `VEHICLE_STATUS_ACCESSORY`<br>11 = `VEHICLE_STATUS_ACCESSORY_PLUS`<br>12 = `VEHICLE_STATUS_CONDITIONING`<br>13 = `VEHICLE_STATUS_DRIVE`<br>14 = `VEHICLE_STATUS_CRASH`<br>15 = `VEHICLE_STATUS_OTA`<br>16 = `VEHICLE_STATUS_TURN_ON_RAILS`<br>17 = `VEHICLE_STATUS_RESET`<br>18 = `VEHICLE_STATUS_SNA` | validated |
| `VCFRONT_timeSpentSleeping` | page 1 | Measures time elapsed while the vehicle has been sleeping. | 13\|10 | little-endian | unsigned | 1 | 0 | s | 0 to 1023 |  | validated |
| `VCFRONT_sleepCurrent` | page 1 | Calculated electrical current into the 12V battery during VCFRONT sleep; raw 4095 = signal not available (SNA) | 24\|12 | little-endian | unsigned | 0.125 | -511.875 | mA | -511.875 to -0.125 | 4095 = `SNA` | validated |
| `VCFRONT_hibernationState` | page 1 | Front body controller: hibernation state | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_HIBERNATION_STATE_INIT`<br>1 = `VC_HIBERNATION_STATE_NOT_ACTIVE`<br>2 = `VC_HIBERNATION_STATE_ACTIVE`<br>3 = `VC_HIBERNATION_STATE_RECOVERY`<br>4 = `VC_HIBERNATION_STATE_EXIT`<br>5 = `VC_HIBERNATION_STATE_PREP` | validated |
| `VCFRONT_wiperECUType` | page 1 | Wiper ECU type detected | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `WIPER_ECU_TYPE_UNKNOWN`<br>1 = `WIPER_ECU_TYPE_BOSCH`<br>2 = `WIPER_ECU_TYPE_SHB`<br>3 = `WIPER_ECU_TYPE_VALEO` | validated |
| `VCFRONT_wiperHeaterState` | page 1 | Indicates the state of the wiper heater; raw 0 = signal not available (SNA) | 42\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCFRONT_occupantCount` | page 1 | Front body controller: occupant count | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `VCFRONT_closureEasterEggState` | page 1 | Front body controller: closure easter egg state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CLOSURE_EASTEREGG_STATE_IDLE`<br>1 = `CLOSURE_EASTEREGG_STATE_WAITING_FOR_START_CONDITIONS`<br>2 = `CLOSURE_EASTEREGG_STATE_WAITING_FOR_PLAY`<br>3 = `CLOSURE_EASTEREGG_STATE_WAITING_FOR_SYNC_PULSE`<br>4 = `CLOSURE_EASTEREGG_STATE_PLAY`<br>5 = `CLOSURE_EASTEREGG_STATE_SHOW_CLEANUP` | validated |
| `VCFRONT_espWakeLine` | page 1 | Front body controller: esp wake line | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_allowEvapInLowAmbient` | page 1 | Front body controller: allow evap in low ambient | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_potentialRadiatorSteam` | page 1 | Front body controller: potential radiator steam | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_potentialRadiatorSteamUI` | page 1 | Front body controller: potential radiator steam UI | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hvacReqOffForFasterCharge` | page 1 | Reports if turning Heating, Ventilation, and Air Conditioning (HVAC) off may improve supercharging power. | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_limitedSplitTempDeltaEnforced` | page 1 | Front body controller: limited split temp delta enforced | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_batteryDischArbState` | page 1 | Front body controller: battery disch arb state | 57\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | validated |
| `VCFRONT_maxEvapHeatRejection` | page 2 | Front body controller: max evap heat rejection | 8\|8 | little-endian | unsigned | 65 | 0 | W | 0 to 16575 |  | validated |
| `VCFRONT_minEvapHeatRejection` | page 2 | Front body controller: min evap heat rejection | 16\|8 | little-endian | unsigned | 15 | 0 | W | 0 to 3800 |  | validated |
| `VCFRONT_freezeEvapITerm` | page 2 | Front body controller: freeze evap i term | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isEvapOperationAllowed` | page 2 | Front body controller: is evap operation allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chillerDemandActive` | page 2 | Front body controller: chiller demand active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_compPerfRecoveryLimited` | page 2 | Front body controller: comp perf recovery limited | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hvacModeNotAttainable` | page 2 | Front body controller: hvac mode not attainable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hasLowRefrigerant` | page 2 | Front body controller: has low refrigerant | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isColdStartRunning` | page 2 | Front body controller: is cold start running | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isHeatPumpOilPurgeActive` | page 2 | Front body controller: is heat pump oil purge active | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pressureRefrigSuction` | page 2 | Refrigerant system suction pressure; raw 127 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 0.125 | 0 | bar | 0 to 11.5 | 127 = `SNA` | validated |
| `VCFRONT_pressureRefrigDischarge` | page 2 | Refrigerant system discharge pressure; raw 511 = signal not available (SNA) | 40\|9 | little-endian | unsigned | 0.08 | 0 | bar | 0 to 37.25 | 511 = `SNA` | validated |
| `VCFRONT_hvacPerfTestCommand` | page 2 | Front body controller: hvac perf test command | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_STARTED`<br>1 = `INIT`<br>2 = `BLOW`<br>3 = `BLOW_BILEVEL`<br>4 = `STOP`<br>5 = `PRECONDITION` | validated |
| `VCFRONT_coolantFillRoutineStatus` | page 2 | Front body controller: coolant fill routine status | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_READY`<br>1 = `MOVING_TO_FILL_POSITION`<br>2 = `READY_TO_FILL`<br>3 = `FAULTED` | validated |
| `VCFRONT_refrigFillRoutineStatus` | page 2 | Front body controller: refrig fill routine status | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_READY`<br>1 = `MOVING_TO_FILL_POSITION`<br>2 = `READY_TO_FILL`<br>3 = `FAULTED` | validated |
| `VCFRONT_isCOP1Running` | page 2 | Front body controller: is COP1 running | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_closeValvesRoutineStatus` | page 2 | Front body controller: close valves routine status | 57\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_READY`<br>1 = `MOVING_TO_FILL_POSITION`<br>2 = `READY_TO_FILL`<br>3 = `FAULTED` | validated |
| `VCFRONT_thermalPerfTestRunning` | page 2 | Front body controller: thermal perf test running | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_extendedHvacPerfTestCommand` | page 2 | Front body controller: extended hvac perf test command | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `1_CABIN_HEAT_AS`<br>2 = `2_BATT_HEAT_CABIN_REHEAT_AS`<br>3 = `3_SPLIT_REHEAT_COOL_DOMINANT`<br>4 = `4_CABIN_COOL`<br>5 = `5_CABIN_HEAT_COP1`<br>6 = `6_BATTERY_HEAT_COP1`<br>7 = `7_BATTERY_COOL`<br>8 = `8_CABIN_PURGE`<br>9 = `COUNT`<br>10 = `STOP` | validated |
| `VCFRONT_5VARailStable` | page 3 | Front body controller: 5 VA rail stable | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_5VBRailStable` | page 3 | Front body controller: 5 VB rail stable | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_12VARailStable` | page 3 | Front body controller: 12 VA rail stable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_12VBRailStable` | page 3 | Front body controller: 12 VB rail stable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_railAState` | page 3 | Front body controller: rail a state | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_railBState` | page 3 | Front body controller: rail b state | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ChargePumpVoltageStable` | page 3 | Front body controller: charge pump voltage stable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_PEResetLineState` | page 3 | Front body controller: PE reset line state | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_HSDInitCompleteU13` | page 3 | Front body controller: HSD init complete U13 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_HSDInitCompleteU16` | page 3 | Front body controller: HSD init complete U16 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_vbatMonitorVoltage` | page 3 | Front body controller: vbat monitor voltage; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.286409544 | 4095 = `SNA` | validated |
| `VCFRONT_AS8510Voltage` | page 3 | Front body controller: AS8510 voltage; raw 4095 = signal not available (SNA) | 28\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.286409544 | 4095 = `SNA` | validated |
| `VCFRONT_vbatProt` | page 3 | Front body controller: vbat prot | 40\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | validated |
| `VCFRONT_logVerbosity` | page 3 | Front body controller: log verbosity | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `VCFRONT_IBSFault` | page 4 | Indicates that a fault has been diagnosed with the Low Voltage (LV) battery sensor. Position from firmware; message assignment inferred. | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_12VOverchargeCounter` | page 4 | Position from firmware; message assignment inferred. | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `VCFRONT_compPowerSupportingHvac` | page 4 | Front body controller: comp power supporting hvac | 8\|11 | little-endian | unsigned | 10 | 0 | W | 0 to 20470 |  | validated |
| `VCFRONT_compPowerSupportingPT` | page 4 | Front body controller: comp power supporting PT | 19\|11 | little-endian | unsigned | 10 | 0 | W | 0 to 20470 |  | validated |
| `VCFRONT_maxHeatingPowerLeftCC` | page 4 | Front body controller: max heating power left CC | 30\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 12000 |  | validated |
| `VCFRONT_maxHeatingPowerRightCC` | page 4 | Front body controller: max heating power right CC | 37\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 12000 |  | validated |
| `VCFRONT_activeLouverOpenPos` | page 4 | The actual position for the active louver | 44\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_activeLouverState` | page 4 | State of the active louver circuit | 51\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NOT_READY`<br>1 = `UNCALIBRATED`<br>2 = `CALIB_CLOSE`<br>3 = `CALIB_OPEN`<br>4 = `READY`<br>5 = `FAULTED`<br>6 = `FAILSAFE_OPEN`<br>7 = `FAILSAFE_LOCKED`<br>8 = `AUTO_DETECT_BACKOFF`<br>9 = `AUTO_DETECT_PAUSE_1`<br>10 = `AUTO_DETECT_WAIT_1`<br>11 = `AUTO_DETECT_MEASURE_1`<br>12 = `AUTO_DETECT_PAUSE_2`<br>13 = `AUTO_DETECT_WAIT_2`<br>14 = `AUTO_DETECT_MEASURE_2`<br>15 = `AUTO_DETECT_PAUSE_3`<br>16 = `AUTO_DETECT_WAIT_3`<br>17 = `AUTO_DETECT_MEASURE_3` | validated |
| `VCFRONT_windshieldCameraHeaterPower` | page 4 | Front body controller: windshield camera heater power; raw 63 = signal not available (SNA) | 56\|6 | little-endian | unsigned | 2.5 | 0 | W | 0 to 155 | 63 = `SNA` | validated |

## Multiplexing

`VCFRONT_statusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (25 signals), page 1 (18 signals), page 2 (19 signals), page 3 (14 signals), page 4 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
