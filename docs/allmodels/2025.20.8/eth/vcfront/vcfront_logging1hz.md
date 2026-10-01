---
layout: default
title: "VCFRONT_logging1Hz (0x381) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front body controller message: logging1 hz. Ethernet-side message VCFRONT_logging1Hz of Front body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 184 signals (VCFRONT_logging1HzIndex, VCFRONT_modeTransitionID, VCFRONT_modeDesired, VCFRONT_targetPTActiveCool and 180 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_logging1Hz (0x381) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Front body controller message: logging1 hz. This page documents the 184 signals of VCFRONT_logging1Hz as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_logging1Hz` |
| Ethernet-side id | 0x381 (897) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 38 ms |
| Signals | 184 |

## Signals of VCFRONT_logging1Hz

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_logging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_logging1HzIndex` | selector | Front body controller: logging1 hz index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `COOLANT`<br>1 = `FAN_DEMAND_CONDENSER_AND_FET_TEMPS`<br>2 = `COOLANT_VALVE`<br>3 = `MISC_ONE`<br>4 = `HP_EXV_RANGE`<br>5 = `HP_DATA_AND_ACCUMULATORS`<br>6 = `HP_CONTROL_LOOP_AND_STATE`<br>7 = `HP_CYCLE_MODEL`<br>8 = `HP_EXV_CALIBRATION`<br>9 = `HP_DISSIPATION_AND_POWER`<br>10 = `HP_TEMPS_AND_DEMANDS`<br>11 = `HP_PRESSURE_CONTROL`<br>12 = `HP_ARBITRATION`<br>13 = `HP_MODE_SELECT_AND_ESTIMATES`<br>14 = `HP_MODE_OPTIONS_AND_ESTIMATES`<br>15 = `BODY_CONTROL`<br>16 = `COOLANT_2`<br>17 = `HP_PT_TARGETS`<br>18 = `MISC_TWO`<br>19 = `HSD_CURRENTS_1`<br>20 = `HSD_CURRENTS_2`<br>21 = `MISC_THREE`<br>22 = `SLEEP_WAKE`<br>23 = `POWER_RATIONALITY_VCLEFT`<br>24 = `POWER_RATIONALITY_VCRIGHT`<br>25 = `MISC_FOUR`<br>26 = `END` | plausible |
| `VCFRONT_modeTransitionID` | page 0 | Front body controller: mode transition ID | 5\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `PARALLEL_F1_noFlowRequest`<br>1 = `SERIES_F2_faultPumps`<br>2 = `SERIES_F3_faultTempSensors`<br>3 = `SERIES_1_drive_batteryWantsCool`<br>4 = `SERIES_2_drive_batteryNeedsHeat`<br>5 = `SERIES_3_drive_batteryWantsHeat`<br>6 = `PARALLEL_2_drive_batteryWantsHeat`<br>7 = `PARALLEL_3_drive_batteryWantsCool`<br>8 = `PARALLEL_4_drive_batteryNeedsCool`<br>9 = `SERIES_4_charge_batteryNeedsHeat`<br>10 = `SERIES_5_charge_batteryWantsHeat`<br>11 = `PARALLEL_5_charge_batteryWantsHeat`<br>12 = `PARALLEL_6_charge_batteryWantsCool`<br>13 = `SERIES_6_fastCharge_batteryNeedsHeat`<br>14 = `SERIES_7_fastCharge_batteryWantsCool`<br>15 = `PARALLEL_7_fastCharge_batteryWantsCool`<br>16 = `PARALLEL_8_fastCharge_batteryWantsHeat`<br>17 = `SERIES_8_preConditioning_batteryNeedsHeat`<br>18 = `SERIES_9_drive_driveUnitThermalLimiting`<br>19 = `PARALLEL_9_drive_batteryThermalLimiting`<br>20 = `PARALLEL_10_batteryDischarge`<br>21 = `INIT`<br>22 = `OVERRIDE`<br>23 = `UNDEFINED`<br>24 = `ENTER_AMBIENTSOURCE`<br>25 = `EXIT_AMBIENTSOURCE`<br>26 = `SER_1_drive_battNeedsActiveCooling_evapEnabled`<br>27 = `SER_2_drive_battNeedsActiveCooling_evapDisabled`<br>28 = `SER_3_drive_battBelowHotStagnationTemp`<br>29 = `SER_4_drive_chillerPassivelyCools`<br>30 = `SER_5_drive_radPassivelyCoolsBatt`<br>31 = `SER_6_drive_battBelowPassiveOrNeedsHeat`<br>32 = `SER_7_FC_battHeatingNeeded`<br>33 = `SER_8_FC_battNeedsActiveCooling_evapDisabled`<br>34 = `SER_9_FC_battNeedsActiveCooling_evapEnabled`<br>35 = `SER_10_charge_battBelowPassiveTarget`<br>36 = `PAR_1_drive_battNeedsActiveCooling_evapEnabled`<br>37 = `PAR_2_drive_battNeedsActiveCooling_evapDisabled`<br>38 = `PAR_3_drive_ptNeedsActiveCooling`<br>39 = `PAR_4_drive_chillerPassivelyCoolsBatt`<br>40 = `PAR_5_drive_cannotPassivelyCoolBatt`<br>41 = `PAR_6_drive_battAboveHotStagnationTemp`<br>42 = `PAR_7_FC_battNeedsActiveCooling_evapDisabled`<br>43 = `PAR_8_FC_battNeedsActiveCooling_evapEnabled`<br>44 = `PAR_9_FC_battAboveHotStagnationTemp`<br>45 = `PAR_10_charge_battNearPassiveTarget`<br>46 = `SER_11_service_highCoolantFlowReq`<br>47 = `PAR_11_batteryDischarge`<br>48 = `PAR_12_drive_cabinOverheatProtectActive`<br>49 = `SER_12_charge_battNeedsCooling`<br>50 = `PAR_13_charge_battNeedsActiveCooling`<br>51 = `ENTER_SERIES_COP1`<br>52 = `SER_13_driverlessSelfTestActive`<br>53 = `ENTER_AMBIENTSOURCE_DRIVERLESS_SELF_TEST`<br>54 = `SER_14_apInletOvertemp` | plausible |
| `VCFRONT_modeDesired` | page 0 | Front body controller: mode desired | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | plausible |
| `VCFRONT_targetPTActiveCool` | page 0 | Front body controller: target PT active cool | 13\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_targetPtOptionalActiveCool` | page 0 | Front body controller: target pt optional active cool | 20\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_targetPTPassive` | page 0 | Front body controller: target PT passive | 27\|7 | little-endian | unsigned | 1 | -20 | degC | -20 to 80 |  | plausible |
| `VCFRONT_targetBatActiveCool` | page 0 | Front body controller: target bat active cool | 34\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_targetBatOptionalActiveCool` | page 0 | Front body controller: target bat optional active cool | 41\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_targetBatPassive` | page 0 | Front body controller: target bat passive | 48\|7 | little-endian | unsigned | 1 | -20 | degC | -20 to 80 |  | plausible |
| `VCFRONT_targetBatActiveHeat` | page 0 | Active heating temperature target for the battery coolant loop | 55\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 60 |  | plausible |
| `VCFRONT_condenserPressureLimit` | page 1 | Front body controller: condenser pressure limit | 5\|6 | little-endian | unsigned | 0.16 | 10 | bar | 10 to 20 |  | plausible |
| `VCFRONT_fanDemandCondenser` | page 1 | Front body controller: fan demand condenser | 11\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `VCFRONT_fanDemandRadiator` | page 1 | Front body controller: fan demand radiator | 18\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `VCFRONT_tempRefrigSuction` | page 1 | Refrigerant system suction temperature; raw 255 = signal not available (SNA) | 25\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | plausible |
| `VCFRONT_pumpBatteryFETTemp` | page 1 | Front body controller: pump battery FET temp; raw 255 = signal not available (SNA) | 33\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | plausible |
| `VCFRONT_pumpPowertrainFETTemp` | page 1 | Front body controller: pump powertrain FET temp; raw 255 = signal not available (SNA) | 41\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | plausible |
| `VCFRONT_radiatorFanFETTemp` | page 1 | Front body controller: radiator fan FET temp; raw 255 = signal not available (SNA) | 49\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | plausible |
| `VCFRONT_radiatorFanRunReason` | page 1 | Current radiator fan run readon | 57\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `ACTIVE_MANAGER`<br>2 = `AMBIENT_SNIFF`<br>3 = `NVH_MASKING`<br>4 = `HEAT_PUMP`<br>5 = `COAST_MODE`<br>6 = `MIN_ON_GLOBAL`<br>7 = `MIN_ON_NVH`<br>8 = `UDS`<br>9 = `RAD_CLEAR`<br>10 = `DI_BURN_IN`<br>11 = `BATTERY_DISCHARGE`<br>12 = `DRIVERLESS_SELF_TEST`<br>13 = `FACTORY_NO_COOLANT` | plausible |
| `VCFRONT_coolantValveModeWrong` | page 1 | Front body controller: coolant valve mode wrong | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_coolantTempBasedMode` | page 1 | Front body controller: coolant temp based mode | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | plausible |
| `VCFRONT_coolantValveRecalReason` | page 2 | coolant Valve Reason for Recalibration | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNDEFINED`<br>1 = `MAX_TRAVEL`<br>2 = `GENERAL_FAULT`<br>3 = `CALIBRATION_FAULT_NO_TRAVEL`<br>4 = `SELF_TEST`<br>5 = `MOTOR_FEEDBACK_INTERRUPTED`<br>6 = `NVRAM_LOSS` | plausible |
| `VCFRONT_coolantValveCountRange` | page 2 | Range of tick counts of the coolant valve actuator; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 1 | 375 | ticks | 375 to 1375 | 1023 = `SNA` | plausible |
| `VCFRONT_coolantValveAngleDrift` | page 2 | Estimated angular drift of the coolant valve | 18\|10 | little-endian | unsigned | 0.25 | -127 | degrees | -127 to 127 |  | plausible |
| `VCFRONT_coolantValveRecalCount` | page 2 | coolant Valve Calibration Count | 28\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCFRONT_coolantValveWindupEst` | page 2 | Front body controller: coolant valve windup est | 44\|6 | little-endian | unsigned | 2 | 0 | ticks | 0 to 126 |  | plausible |
| `VCFRONT_coolantValveRadBypass` | page 2 | Percent of coolant bypassing the powertrain radiator; raw 127 = signal not available (SNA) | 50\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | plausible |
| `VCFRONT_usingModeledPs` | page 2 | Front body controller: using modeled ps | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_usingModeledPd` | page 2 | Front body controller: using modeled pd | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_usingModeledPl` | page 2 | Front body controller: using modeled pl | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_usingModeledTs` | page 2 | Front body controller: using modeled ts | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_usingModeledTd` | page 2 | Front body controller: using modeled td | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_usingModeledTl` | page 2 | Front body controller: using modeled tl | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpChargeCableType` | page 5 | Front body controller: hp charge cable type | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_CHARGER_PRESENT`<br>1 = `DC_CHARGER_PRESENT`<br>2 = `AC_CHARGER_PRESENT` | plausible |
| `VCFRONT_subcoolActual` | page 5 | Front body controller: subcool actual | 8\|7 | little-endian | signed | 0.4 | 15.2 | degC | -10 to 40 |  | plausible |
| `VCFRONT_hpSubcoolTarget` | page 5 | Front body controller: hp subcool target | 16\|5 | little-endian | unsigned | 1 | 0 | degC | 0 to 31 |  | plausible |
| `VCFRONT_CMPDischargeSuperheat` | page 5 | Front body controller: CMP discharge superheat | 21\|5 | little-endian | signed | 1 | 6 | degC | -10 to 21 |  | plausible |
| `VCFRONT_hpCOP` | page 5 | Front body controller: hp COP | 26\|6 | little-endian | unsigned | 0.1 | 0 | - | 0 to 6 |  | plausible |
| `VCFRONT_lowSideWattsLift` | page 5 | Front body controller: low side watts lift | 32\|7 | little-endian | unsigned | 60 | 0 | W | 0 to 7600 |  | plausible |
| `VCFRONT_tempSuperheatActual` | page 5 | Front body controller: temp superheat actual; raw 1023 = signal not available (SNA) | 39\|10 | little-endian | unsigned | 0.1 | -20 | degC | -20 to 80 | 1023 = `SNA` | plausible |
| `VCFRONT_tempSuperheatTarget` | page 5 | Front body controller: temp superheat target | 49\|10 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 60 |  | plausible |
| `VCFRONT_refrigerantHasBeenFilled` | page 5 | Front body controller: refrigerant has been filled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_refCommissionStatus` | page 5 | Front body controller: ref commission status | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REFRIGERANT_UNKNOWN`<br>1 = `REFRIGERANT_UNCOMMISSIONED`<br>2 = `REFRIGERANT_COMMISSIONED` | plausible |
| `VCFRONT_LCCPurgeActive` | page 5 | Reports if Liquid Cooled Condenser (LCC) refrigerant purge is active on the heat pump. | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_exteriorQuietModeEnabled` | page 6 | Front body controller: exterior quiet mode enabled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_exteriorQuietModeAllowed` | page 6 | Front body controller: exterior quiet mode allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_CCQdotFdFrwrdTarget` | page 6 | Front body controller: CC qdot fd frwrd target | 7\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | plausible |
| `VCFRONT_CCQdotFdbk` | page 6 | Front body controller: CC qdot fdbk | 14\|7 | little-endian | signed | 80 | 0 | W | -5000 to 5000 |  | plausible |
| `VCFRONT_CCQdotActual` | page 6 | Front body controller: CC qdot actual | 21\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | plausible |
| `VCFRONT_evapFdFrwrdTarget` | page 6 | Front body controller: evap fd frwrd target | 28\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | plausible |
| `VCFRONT_evapFdbk` | page 6 | Front body controller: evap fdbk | 35\|7 | little-endian | signed | 100 | -3300 | W | -9700 to 3000 |  | plausible |
| `VCFRONT_DIQdotA` | page 6 | Front body controller: DI qdot a | 42\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10000 |  | plausible |
| `VCFRONT_evapFdFrwrdTargetMinimum` | page 6 | Front body controller: evap fd frwrd target minimum | 49\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10000 |  | plausible |
| `VCFRONT_passiveCoolingState` | page 6 | Front body controller: passive cooling state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ChillerCoolsSeriesLoop`<br>1 = `ChillerCoolsParallelBattLoop`<br>2 = `ChillerAndRadCoolSeriesLoop`<br>3 = `CannotCoolBattery` | plausible |
| `VCFRONT_totalLoadCoolingDominant` | page 6 | Front body controller: total load cooling dominant | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_feedfwdLoadCoolingDominant` | page 6 | Front body controller: feedfwd load cooling dominant | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_modelLoadCoolingDominant` | page 6 | Front body controller: model load cooling dominant | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpPotentialLowRefrig` | page 6 | Front body controller: hp potential low refrig | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpRefrigerantPurgeState` | page 6 | Front body controller: hp refrigerant purge state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `EVAP_PURGE`<br>2 = `COMPLETE` | plausible |
| `VCFRONT_estPressureLiq` | page 7 | Front body controller: est pressure liq | 5\|6 | little-endian | unsigned | 0.5 | 0 | bar | 0 to 31 |  | plausible |
| `VCFRONT_estPressureSuct` | page 7 | Front body controller: est pressure suct | 11\|7 | little-endian | unsigned | 0.125 | 0 | bar | 0 to 11.5 |  | plausible |
| `VCFRONT_estPressureDisch` | page 7 | Front body controller: est pressure disch | 18\|7 | little-endian | unsigned | 0.25 | 0 | bar | 0 to 31.75 |  | plausible |
| `VCFRONT_estTempLiq` | page 7 | Front body controller: est temp liq | 25\|8 | little-endian | signed | 0.8 | 68.8 | degC | -33 to 170 |  | plausible |
| `VCFRONT_estTempSuct` | page 7 | Front body controller: est temp suct | 33\|6 | little-endian | signed | 1 | 2 | degC | -30 to 33 |  | plausible |
| `VCFRONT_estTempDisch` | page 7 | Front body controller: est temp disch | 39\|7 | little-endian | signed | 1.5 | 75 | degC | -20 to 169 |  | plausible |
| `VCFRONT_estCompressorRpm` | page 7 | Front body controller: est compressor rpm | 46\|9 | little-endian | unsigned | 30 | 0 | rpm | 0 to 15000 |  | plausible |
| `VCFRONT_estQLift` | page 7 | Front body controller: est q lift | 55\|6 | little-endian | unsigned | 100 | 0 | W | 0 to 6300 |  | plausible |
| `VCFRONT_cycleModelConverged` | page 7 | Front body controller: cycle model converged | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_compStandbyCoastDownMode` | page 7 | Front body controller: comp standby coast down mode | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_compStandbyShowroomMode` | page 7 | Front body controller: comp standby showroom mode | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_chillerExvCalibOffset` | page 8 | Last calibration offset calculated for the Chiller EXV | 5\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_evapExvCalibOffset` | page 8 | Last calibration offset calculated for the Evaporator EXV | 10\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_recircExvCalibOffset` | page 8 | Last calibration offset calculated for the Recirc EXV | 15\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_lccExvCalibOffset` | page 8 | Last calibration offset calculated for the Liquid Cooled Condenser EXV | 20\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_ccLeftExvCalibOffset` | page 8 | Last calibration offset calculated for the Left Cabin Condenser EXV | 25\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_ccRightExvCalibOffset` | page 8 | Last calibration offset calculated for the Right Cabin Condenser EXV | 30\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | plausible |
| `VCFRONT_chillerEXVControlState` | page 8 | Control State of the chiller electronic expansion valve | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_evapEXVControlState` | page 8 | Control State of the evaporator electronic expansion valve | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_recircEXVControlState` | page 8 | Control State of the recirc electronic expansion valve | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_lccEXVControlState` | page 8 | Control State of the liquid cooled condenser electronic expansion valve | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_cclEXVControlState` | page 8 | Control State of the chiller electronic expansion valve | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_ccrEXVControlState` | page 8 | Control State of the right cabin condenser electronic expansion valve | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | plausible |
| `VCFRONT_chillerExvCalibFailed` | page 8 | State of the last calibration for the Chiller EXV | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_evapExvCalibFailed` | page 8 | State of the last calibration for the Evaporator EXV | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_recircExvCalibFailed` | page 8 | State of the last calibration for the Recirc EXV | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_lccExvCalibFailed` | page 8 | State of the last calibration for the Liquid Cooled Condenser EXV | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ccLeftExvCalibFailed` | page 8 | State of the last calibration for the Left Cabin Condenser EXV | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ccRightExvCalibFailed` | page 8 | State of the last calibration for the Right Cabin Condenser EXV | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientTempSniffActive` | page 8 | Front body controller: ambient temp sniff active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientTempPassiveSniffing` | page 8 | Front body controller: ambient temp passive sniffing | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientTempRadSampling` | page 8 | Front body controller: ambient temp rad sampling | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientTempSpeedSampling` | page 8 | Front body controller: ambient temp speed sampling | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_feedFwdMDotEvaporator` | page 12 | Front body controller: feed fwd m dot evaporator | 5\|8 | little-endian | unsigned | 0.005 | 0 | - | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatBatteryHeatAmbSrc` | page 12 | Front body controller: hp cabin heat battery heat amb src | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatBatteryHeatCOP1` | page 12 | Front body controller: hp cabin heat battery heat COP1 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_feedFwdMDotCabinCondenser` | page 12 | Feed forward MDOT for the cabin condenser controller. | 15\|8 | little-endian | unsigned | 0.005 | 0 | - | 0 to 1 |  | plausible |
| `VCFRONT_feedBackEvapTempController` | page 12 | Evap temperature controller feedback. | 23\|7 | little-endian | unsigned | 0.01 | -0.5 | - | -0.5 to 0.5 |  | plausible |
| `VCFRONT_feedBackDuctTempController` | page 12 | Feedback for the duct temp controller. | 30\|8 | little-endian | unsigned | 0.01 | -1 | - | -1 to 1 |  | plausible |
| `VCFRONT_isSolenoidAllowed` | page 12 | Front body controller: is solenoid allowed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_maxChillerCoolingPower` | page 12 | Front body controller: max chiller cooling power | 39\|8 | little-endian | unsigned | 100 | 0 | W | 0 to 20000 |  | plausible |
| `VCFRONT_fanControlRadCanCool` | page 12 | Front body controller: fan control rad can cool | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_fanControlFeedfwdActive` | page 12 | Front body controller: fan control feedfwd active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_fanControlRadiatorUa` | page 12 | Front body controller: fan control radiator ua | 49\|7 | little-endian | unsigned | 8 | 0 | W/C | 0 to 1000 |  | plausible |
| `VCFRONT_fanControlRadiatorInletTemp` | page 12 | Front body controller: fan control radiator inlet temp | 56\|6 | little-endian | signed | 1.8 | 36 | C | -20 to 90 |  | plausible |
| `VCFRONT_hpASBatteryHeatingAllowed` | page 14 | Front body controller: hp AS battery heating allowed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCOP1BatteryHeatingAllowed` | page 14 | Front body controller: hp COP1 battery heating allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatScavengeOnly` | page 14 | Front body controller: hp cabin heat scavenge only | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatAmbientSource` | page 14 | Front body controller: hp cabin heat ambient source | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatReheatScavenge` | page 14 | Front body controller: hp cabin heat reheat scavenge | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatReheatAmbientSource` | page 14 | Front body controller: hp cabin heat reheat ambient source | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatBlend` | page 14 | Front body controller: hp cabin heat blend | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatCOP1` | page 14 | Front body controller: hp cabin heat COP1 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatBatteryHeatReheatAmbSrc` | page 14 | Front body controller: hp cabin heat battery heat reheat amb src | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinHeatBatteryCoolReheat` | page 14 | Front body controller: hp cabin heat battery cool reheat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinCoolEvaporator` | page 14 | Front body controller: hp cabin cool evaporator | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinCoolEvaporatorReheat` | page 14 | Front body controller: hp cabin cool evaporator reheat | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryHeatAmbientSource` | page 14 | Front body controller: hp battery heat ambient source | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryHeatCOP1` | page 14 | Front body controller: hp battery heat COP1 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryCool` | page 14 | Front body controller: hp battery cool | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryCoolCabinCondenserCD` | page 14 | Front body controller: hp battery cool cabin condenser CD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryCoolCabinCondenserHD` | page 14 | Front body controller: hp battery cool cabin condenser HD | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryCoolCabinReheat` | page 14 | Front body controller: hp battery cool cabin reheat | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpBatteryCoolEvaporator` | page 14 | Front body controller: hp battery cool evaporator | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_suctionSuperheatEstTsSNA` | page 14 | Front body controller: suction superheat est ts SNA | 24\|4 | little-endian | unsigned | 2 | 0 | degC | 0 to 30 |  | plausible |
| `VCFRONT_tempRefrigSuctionEst` | page 14 | Front body controller: temp refrig suction est | 28\|6 | little-endian | signed | 1.2 | 0 | degC | -25 to 37.2 |  | plausible |
| `VCFRONT_hpBattOverTempHvacDisable` | page 14 | Front body controller: hp batt over temp hvac disable | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpDiagLouverCalib` | page 14 | Diagnostics requested a louver calibration. | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpDiagHighSideNotNominal` | page 14 | Front body controller: hp diag high side not nominal | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpForceModeRadClear` | page 14 | Front body controller: hp force mode rad clear | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_estPressureDischargeSat` | page 14 | Front body controller: est pressure discharge sat | 38\|7 | little-endian | unsigned | 0.25 | 0 | bar | 0 to 31.75 |  | plausible |
| `VCFRONT_tempRefrigLiquid` | page 14 | Refrigerant system liquid line temperature; raw 2047 = signal not available (SNA) | 45\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 | 2047 = `SNA` | plausible |
| `VCFRONT_totalBattHeatingPower` | page 14 | Total battery heating power requested | 56\|7 | little-endian | unsigned | 150 | 0 | W | 0 to 19050 |  | plausible |
| `VCFRONT_hpPotentialFrozenRadiator` | page 14 | Front body controller: hp potential frozen radiator | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_passiveSeriesRegOn` | page 16 | Front body controller: passive series reg on | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_passiveDemandRadBypass` | page 16 | Front body controller: passive demand rad bypass | 8\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `VCFRONT_targetLccActiveCoolCap` | page 16 | Front body controller: target lcc active cool cap | 16\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_targetLccActiveCoolEff` | page 16 | Front body controller: target lcc active cool eff | 24\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | plausible |
| `VCFRONT_coolantValveDailyAngleTravel` | page 16 | Running 10-day average of daily angular travel | 32\|7 | little-endian | unsigned | 60 | 0 | degrees | 0 to 7500 |  | plausible |
| `VCFRONT_dischargePressureLimit` | page 16 | Front body controller: discharge pressure limit | 40\|7 | little-endian | unsigned | 0.25 | 0 | bar | 0 to 26 |  | plausible |
| `VCFRONT_radMovementBlockActive` | page 16 | Front body controller: rad movement block active | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_radBypassMoveReason` | page 16 | Front body controller: rad bypass move reason | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT_UNBYPASS`<br>1 = `INIT_BYPASS`<br>2 = `PASSIVE_UNBYPASS`<br>3 = `PASSIVE_BYPASS`<br>4 = `RAD_HEAT_BYPASS`<br>5 = `RAD_HEAT_UNBYPASS`<br>6 = `ACTIVE_PT_UNBYPASS`<br>7 = `ACTIVE_BATT_UNBYPASS`<br>8 = `EXIT_SERIES`<br>9 = `UDS`<br>10 = `HEATPUMP`<br>11 = `DRIVERLESS_SELF_TEST` | plausible |
| `VCFRONT_hpBattHeatingPower` | page 16 | Front body controller: hp batt heating power | 52\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 10000 |  | plausible |
| `VCFRONT_tempCoolantPTInletEstStatus` | page 16 | Front body controller: temp coolant PT inlet est status | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `LOW_CONFIDENCE`<br>2 = `HIGH_CONFIDENCE_OVERPREDICT`<br>3 = `HIGH_CONFIDENCE` | plausible |
| `VCFRONT_hpColdStagnationLimit` | page 17 | Front body controller: hp cold stagnation limit | 8\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 80 |  | plausible |
| `VCFRONT_hpHotStagnationLimit` | page 17 | Front body controller: hp hot stagnation limit | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 80 |  | plausible |
| `VCFRONT_hpCompFlowIndex` | page 17 | Front body controller: hp comp flow index | 23\|8 | little-endian | unsigned | 1 | 0 | - | 30 to 255 |  | plausible |
| `VCFRONT_hpCompFlowIndexFiltered` | page 17 | Front body controller: hp comp flow index filtered | 31\|8 | little-endian | unsigned | 1 | 0 | - | 30 to 255 |  | plausible |
| `VCFRONT_subcoolEstTlSNA` | page 17 | Front body controller: subcool est tl SNA | 39\|6 | little-endian | signed | 2 | 0 | degC | -10 to 53 |  | plausible |
| `VCFRONT_subcoolEstPlSNA` | page 17 | Front body controller: subcool est pl SNA | 45\|6 | little-endian | signed | 2 | 0 | degC | -10 to 53 |  | plausible |
| `VCFRONT_tempRefrigLiquidEst` | page 17 | Front body controller: temp refrig liquid est | 51\|6 | little-endian | unsigned | 2 | 0 | degC | 0 to 125 |  | plausible |
| `VCFRONT_pressureRefrigLiquidEst` | page 17 | Front body controller: pressure refrig liquid est | 57\|6 | little-endian | unsigned | 0.5 | 0 | bar | 0 to 31 |  | plausible |
| `VCFRONT_cmpIsentropicCheckPassed` | page 17 | Front body controller: cmp isentropic check passed | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_louverPosReason` | page 18 | Front body controller: louver pos reason | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `CONDENSOR_MANAGER`<br>2 = `PASSIVE_MANAGER`<br>3 = `SNIFFING`<br>4 = `BOUNDS_CHECK`<br>5 = `FAN_RUN`<br>6 = `FAN_FAULT`<br>7 = `COAST_MODE`<br>8 = `UDS`<br>9 = `HIGH_SPEED`<br>10 = `BATTERY_DISCHARGE`<br>11 = `DRIVERLESS_SELF_TEST` | plausible |
| `VCFRONT_hpEnergyFlowIndex` | page 18 | Front body controller: hp energy flow index | 9\|8 | little-endian | unsigned | 4 | 0 | - | 0 to 1020 |  | plausible |
| `VCFRONT_hpEnergyFlowIndexFiltered` | page 18 | Refrigerant system modeled energy flow index filtered | 17\|8 | little-endian | unsigned | 4 | 0 | - | 0 to 1020 |  | plausible |
| `VCFRONT_ductLeftAtSS` | page 18 | Front body controller: duct left at SS | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ductRightAtSS` | page 18 | Front body controller: duct right at SS | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_minCompressorRPMAllowed` | page 18 | Front body controller: min compressor RPM allowed | 27\|7 | little-endian | unsigned | 90 | 0 | rpm | 0 to 11430 |  | plausible |
| `VCFRONT_ccRefrigerantMassFlow` | page 18 | Front body controller: cc refrigerant mass flow | 34\|6 | little-endian | unsigned | 4 | 0 | g/s | 0 to 251 |  | plausible |
| `VCFRONT_highSideDpResidual` | page 18 | Front body controller: high side dp residual | 40\|7 | little-endian | signed | 0.1 | 0 | bar | -6 to 6 |  | plausible |
| `VCFRONT_abnormalHighSuctionSuperheat` | page 18 | Front body controller: abnormal high suction superheat | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_coolantValveAngleTravel` | page 18 | Total angular travel since last (re)calibration | 48\|10 | little-endian | unsigned | 5 | 0 | degrees | 0 to 5000 |  | plausible |
| `VCFRONT_chargeShuttleType` | page 18 | Front body controller: charge shuttle type | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHARGE_SHUTTLE_NONE`<br>1 = `CHARGE_SHUTTLE_STANDARD`<br>2 = `CHARGE_SHUTTLE_LCCR`<br>3 = `CHARGE_SHUTTLE_COP1` | plausible |
| `VCFRONT_hpRefrigTempSensorCheckCanFire` | page 18 | Front body controller: hp refrig temp sensor check can fire | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpRefrigPressureSensorCheckCanFire` | page 18 | Front body controller: hp refrig pressure sensor check can fire | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_tempSuperheatActFiltered` | page 21 | Front body controller: temp superheat act filtered | 5\|8 | little-endian | signed | 0.25 | 26.5 | degC | -5 to 58 |  | plausible |
| `VCFRONT_tempRefrigDischarge` | page 21 | Refrigerant system discharge temperature; raw 2047 = signal not available (SNA) | 13\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 | 2047 = `SNA` | plausible |
| `VCFRONT_pumpBatteryRPMTarget` | page 21 | Front body controller: pump battery RPM target; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | plausible |
| `VCFRONT_pumpPowertrainRPMTarget` | page 21 | Front body controller: pump powertrain RPM target; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | plausible |
| `VCFRONT_coolantFlowChillerTarget` | page 21 | Front body controller: coolant flow chiller target | 40\|8 | little-endian | unsigned | 0.161 | 0 | LPM | 0 to 25 |  | plausible |
| `VCFRONT_radiatorFanRPMTarget` | page 21 | Front body controller: radiator fan RPM target; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 40 | 0 | rpm | 0 to 10000 | 255 = `SNA` | plausible |
| `VCFRONT_batteryDischArbState` | page 21 | Front body controller: battery disch arb state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | plausible |
| `VCFRONT_preventReEntryTillNexthpResetCOP1` | page 21 | Front body controller: prevent re entry till nexthp reset COP1 | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_chillerBattHeatingPowerAvailable` | page 21 | Front body controller: chiller batt heating power available | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_isExpectedQChillerVeryHighCOP1` | page 21 | Front body controller: is expected q chiller very high COP1 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_superheatProtectionLimit` | page 25 | Front body controller: superheat protection limit | 5\|10 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 60 |  | plausible |
| `VCFRONT_chillerDemandWatts` | page 25 | Front body controller: chiller demand watts | 16\|8 | little-endian | unsigned | 100 | 0 | W | 0 to 20000 |  | plausible |
| `VCFRONT_nominalTevapHWLimit` | page 25 | Front body controller: nominal tevap HW limit | 24\|7 | little-endian | unsigned | 0.5 | 0 | degC | 0 to 60 |  | plausible |
| `VCFRONT_solverIterTotalLoad` | page 25 | Front body controller: solver iter total load | 32\|6 | little-endian | unsigned | 2 | 0 | - | 0 to 126 |  | plausible |
| `VCFRONT_battCoolEvapEnableDelay` | page 25 | Front body controller: batt cool evap enable delay | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_solverIterFeedforward` | page 25 | Front body controller: solver iter feedforward | 40\|6 | little-endian | unsigned | 2 | 0 | - | 0 to 126 |  | plausible |
| `VCFRONT_ambientTempState` | page 25 | Front body controller: ambient temp state | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `MEASUREING`<br>2 = `LATCHED`<br>3 = `SNIFFING` | plausible |
| `VCFRONT_ambientTempUnlatchReason` | page 25 | Front body controller: ambient temp unlatch reason | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `VEHICLE_SPEED`<br>2 = `FAN_AIRFLOW`<br>3 = `LOUVERS_CLOSED`<br>4 = `SNIFF_TIMEBASED`<br>5 = `SNIFF_BLOCKED`<br>6 = `SNIFF_STARTDRIVE` | plausible |
| `VCFRONT_compressorSuctionVaporQuality` | page 25 | Front body controller: compressor suction vapor quality | 51\|5 | little-endian | unsigned | 0.01 | 0.7 | - | 0.7 to 1 |  | plausible |
| `VCFRONT_cabinHeatingCOP1MinActiveRefCharge` | page 25 | Estimation of minimal active refrigerant charge during cabin heating COP1 mode | 56\|7 | little-endian | unsigned | 10 | 0 | - | 0 to 1100 |  | plausible |

## Multiplexing

`VCFRONT_logging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals), page 1 (10 signals), page 2 (12 signals), page 5 (11 signals), page 6 (15 signals), page 7 (11 signals), page 8 (22 signals), page 12 (12 signals), page 14 (29 signals), page 16 (10 signals), page 17 (9 signals), page 18 (13 signals), page 21 (10 signals), page 25 (10 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
