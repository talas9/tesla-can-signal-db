---
layout: default
title: "VCFRONT_logging1Hz (0x381) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: logging1 hz. Tesla Model 3 / Model Y CAN bus message VCFRONT_logging1Hz (0x381) of Front body controller, firmware 2026.26.6.5, 205 signals (VCFRONT_logging1HzIndex, VCFRONT_modeTransitionID, VCFRONT_modeDesired, VCFRONT_targetPTActiveCool and 201 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_logging1Hz (0x381) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front body controller message: logging1 hz; frame length observed on a vehicle bus. This page documents the 205 signals of VCFRONT_logging1Hz as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_logging1Hz` |
| CAN id | 0x381 (897) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 36 ms |
| Signals | 205 |

## Signals of VCFRONT_logging1Hz

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_logging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_logging1HzIndex` | selector | Front body controller: logging1 hz index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `COOLANT`<br>1 = `FAN_DEMAND_CONDENSER_AND_FET_TEMPS`<br>2 = `COOLANT_VALVE`<br>3 = `MISC_ONE`<br>4 = `HP_EXV_RANGE`<br>5 = `HP_DATA_AND_ACCUMULATORS`<br>6 = `HP_CONTROL_LOOP_AND_STATE`<br>7 = `HP_CYCLE_MODEL`<br>8 = `HP_EXV_CALIBRATION`<br>9 = `HP_DISSIPATION_AND_POWER`<br>10 = `HP_TEMPS_AND_DEMANDS`<br>11 = `HP_PRESSURE_CONTROL`<br>12 = `HP_ARBITRATION`<br>13 = `HP_MODE_SELECT_AND_ESTIMATES`<br>14 = `HP_MODE_OPTIONS_AND_ESTIMATES`<br>15 = `BODY_CONTROL`<br>16 = `COOLANT_2`<br>17 = `HP_PT_TARGETS`<br>18 = `MISC_TWO`<br>19 = `HSD_CURRENTS_1`<br>20 = `HSD_CURRENTS_2`<br>21 = `MISC_THREE`<br>22 = `SLEEP_WAKE`<br>23 = `POWER_RATIONALITY_VCLEFT`<br>24 = `POWER_RATIONALITY_VCRIGHT`<br>25 = `MISC_FOUR`<br>26 = `MISC_FIVE`<br>27 = `END` | plausible |
| `VCFRONT_modeTransitionID` | page 0 | Front body controller: mode transition ID | 5\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `PARALLEL_F1_noFlowRequest`<br>1 = `SERIES_F2_faultPumps`<br>2 = `SERIES_F3_faultTempSensors`<br>3 = `SERIES_1_drive_batteryWantsCool`<br>4 = `SERIES_2_drive_batteryNeedsHeat`<br>5 = `SERIES_3_drive_batteryWantsHeat`<br>6 = `PARALLEL_2_drive_batteryWantsHeat`<br>7 = `PARALLEL_3_drive_batteryWantsCool`<br>8 = `PARALLEL_4_drive_batteryNeedsCool`<br>9 = `SERIES_4_charge_batteryNeedsHeat`<br>10 = `SERIES_5_charge_batteryWantsHeat`<br>11 = `PARALLEL_5_charge_batteryWantsHeat`<br>12 = `PARALLEL_6_charge_batteryWantsCool`<br>13 = `SERIES_6_fastCharge_batteryNeedsHeat`<br>14 = `SERIES_7_fastCharge_batteryWantsCool`<br>15 = `PARALLEL_7_fastCharge_batteryWantsCool`<br>16 = `PARALLEL_8_fastCharge_batteryWantsHeat`<br>17 = `SERIES_8_preConditioning_batteryNeedsHeat`<br>18 = `SERIES_9_drive_driveUnitThermalLimiting`<br>19 = `PARALLEL_9_drive_batteryThermalLimiting`<br>20 = `PARALLEL_10_batteryDischarge`<br>21 = `INIT`<br>22 = `OVERRIDE`<br>23 = `UNDEFINED`<br>24 = `ENTER_AMBIENTSOURCE`<br>25 = `EXIT_AMBIENTSOURCE`<br>26 = `SER_1_drive_battNeedsActiveCooling_evapEnabled`<br>27 = `SER_2_drive_battNeedsActiveCooling_evapDisabled`<br>28 = `SER_3_drive_battBelowHotStagnationTemp`<br>29 = `SER_4_drive_chillerPassivelyCools`<br>30 = `SER_5_drive_radPassivelyCoolsBatt`<br>31 = `SER_6_drive_battBelowPassiveOrNeedsHeat`<br>32 = `SER_7_FC_battHeatingNeeded`<br>33 = `SER_8_FC_battNeedsActiveCooling_evapDisabled`<br>34 = `SER_9_FC_battNeedsActiveCooling_evapEnabled`<br>35 = `SER_10_charge_battBelowPassiveTarget`<br>36 = `PAR_1_drive_battNeedsActiveCooling_evapEnabled`<br>37 = `PAR_2_drive_battNeedsActiveCooling_evapDisabled`<br>38 = `PAR_3_drive_ptNeedsActiveCooling`<br>39 = `PAR_4_drive_chillerPassivelyCoolsBatt`<br>40 = `PAR_5_drive_cannotPassivelyCoolBatt`<br>41 = `PAR_6_drive_battAboveHotStagnationTemp`<br>42 = `PAR_7_FC_battNeedsActiveCooling_evapDisabled`<br>43 = `PAR_8_FC_battNeedsActiveCooling_evapEnabled`<br>44 = `PAR_9_FC_battAboveHotStagnationTemp`<br>45 = `PAR_10_charge_battNearPassiveTarget`<br>46 = `SER_11_service_highCoolantFlowReq`<br>47 = `PAR_11_batteryDischarge`<br>48 = `PAR_12_drive_cabinOverheatProtectActive`<br>49 = `SER_12_charge_battNeedsCooling`<br>50 = `PAR_13_charge_battNeedsActiveCooling`<br>51 = `ENTER_SERIES_COP1`<br>52 = `SER_13_driverlessSelfTestActive`<br>53 = `ENTER_AMBIENTSOURCE_DRIVERLESS_SELF_TEST`<br>54 = `SER_14_apInletOvertemp` | validated |
| `VCFRONT_modeDesired` | page 0 | Front body controller: mode desired | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | validated |
| `VCFRONT_targetPTActiveCool` | page 0 | Front body controller: target PT active cool | 13\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | validated |
| `VCFRONT_targetPtOptionalActiveCool` | page 0 | Front body controller: target pt optional active cool | 20\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | validated |
| `VCFRONT_targetPTPassive` | page 0 | Front body controller: target PT passive | 27\|7 | little-endian | unsigned | 1 | -20 | degC | -20 to 80 |  | validated |
| `VCFRONT_targetBatActiveCool` | page 0 | Front body controller: target bat active cool | 34\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | validated |
| `VCFRONT_targetBatOptionalActiveCool` | page 0 | Front body controller: target bat optional active cool | 41\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | validated |
| `VCFRONT_targetBatPassive` | page 0 | Front body controller: target bat passive | 48\|7 | little-endian | unsigned | 1 | -20 | degC | -20 to 80 |  | validated |
| `VCFRONT_targetBatActiveHeat` | page 0 | Active heating temperature target for the battery coolant loop | 55\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 60 |  | validated |
| `VCFRONT_condenserPressureLimit` | page 1 | Front body controller: condenser pressure limit | 5\|6 | little-endian | unsigned | 0.16 | 10 | bar | 10 to 20 |  | validated |
| `VCFRONT_fanDemandCondenser` | page 1 | Front body controller: fan demand condenser | 11\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_fanDemandRadiator` | page 1 | Front body controller: fan demand radiator | 18\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_tempRefrigSuction` | page 1 | Refrigerant system suction temperature; raw 255 = signal not available (SNA) | 25\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | validated |
| `VCFRONT_pumpBatteryFETTemp` | page 1 | Front body controller: pump battery FET temp; raw 255 = signal not available (SNA) | 33\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | validated |
| `VCFRONT_pumpPowertrainFETTemp` | page 1 | Front body controller: pump powertrain FET temp; raw 255 = signal not available (SNA) | 41\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | validated |
| `VCFRONT_radiatorFanFETTemp` | page 1 | Front body controller: radiator fan FET temp; raw 255 = signal not available (SNA) | 49\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | validated |
| `VCFRONT_radiatorFanRunReason` | page 1 | Current radiator fan run readon | 57\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `ACTIVE_MANAGER`<br>2 = `AMBIENT_SNIFF`<br>3 = `NVH_MASKING`<br>4 = `HEAT_PUMP`<br>5 = `COAST_MODE`<br>6 = `MIN_ON_GLOBAL`<br>7 = `MIN_ON_NVH`<br>8 = `UDS`<br>9 = `RAD_CLEAR`<br>10 = `DI_BURN_IN`<br>11 = `BATTERY_DISCHARGE`<br>12 = `DRIVERLESS_SELF_TEST`<br>13 = `FACTORY_NO_COOLANT` | validated |
| `VCFRONT_coolantValveModeWrong` | page 1 | Front body controller: coolant valve mode wrong | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_coolantTempBasedMode` | page 1 | Front body controller: coolant temp based mode | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | validated |
| `VCFRONT_coolantValveRecalReason` | page 2 | coolant Valve Reason for Recalibration | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNDEFINED`<br>1 = `MAX_TRAVEL`<br>2 = `GENERAL_FAULT`<br>3 = `CALIBRATION_FAULT_NO_TRAVEL`<br>4 = `SELF_TEST`<br>5 = `MOTOR_FEEDBACK_INTERRUPTED`<br>6 = `NVRAM_LOSS` | validated |
| `VCFRONT_coolantValveCountRange` | page 2 | Range of tick counts of the coolant valve actuator; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 1 | 375 | ticks | 375 to 1375 | 1023 = `SNA` | validated |
| `VCFRONT_coolantValveAngleDrift` | page 2 | Estimated angular drift of the coolant valve | 18\|10 | little-endian | unsigned | 0.25 | -127 | degrees | -127 to 127 |  | validated |
| `VCFRONT_coolantValveRecalCount` | page 2 | coolant Valve Calibration Count | 28\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_coolantValveWindupEst` | page 2 | Front body controller: coolant valve windup est | 44\|6 | little-endian | unsigned | 2 | 0 | ticks | 0 to 126 |  | validated |
| `VCFRONT_coolantValveRadBypass` | page 2 | Percent of coolant bypassing the powertrain radiator; raw 127 = signal not available (SNA) | 50\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | validated |
| `VCFRONT_usingModeledPs` | page 2 | Front body controller: using modeled ps | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_usingModeledPd` | page 2 | Front body controller: using modeled pd | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_usingModeledPl` | page 2 | Front body controller: using modeled pl | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_usingModeledTs` | page 2 | Front body controller: using modeled ts | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_usingModeledTd` | page 2 | Front body controller: using modeled td | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_usingModeledTl` | page 2 | Front body controller: using modeled tl | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_HCML_lowBeamSpotTemp` | page 3 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 8\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCML_highBeamTemp` | page 3 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 16\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCML_turnTemp` | page 3 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 24\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCML_bladeTemp` | page 3 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 32\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCML_diffuseTemp` | page 3 | Position from firmware; message assignment inferred. | 40\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCMR_lowBeamSpotTemp` | page 4 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 8\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCMR_highBeamTemp` | page 4 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 16\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCMR_turnTemp` | page 4 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 24\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCMR_bladeTemp` | page 4 | Temperature of the left low beam LED board. Position from firmware; message assignment inferred. | 32\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_HCMR_diffuseTemp` | page 4 | Position from firmware; message assignment inferred. | 40\|8 | little-endian | signed | 1 | 67 | degC | -60 to 194 |  | plausible |
| `VCFRONT_homelinkRegionCode` | page 5 | Homelink Region Code. Position from firmware; message assignment inferred. | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HOMELINK_REGION_CODE_UNKNOWN`<br>1 = `HOMELINK_REGION_CODE_EUROPE`<br>5 = `HOMELINK_REGION_CODE_AMERICAS`<br>8 = `HOMELINK_REGION_CODE_REST_OF_WORLD`<br>9 = `HOMELINK_REGION_CODE_CHINA` | plausible |
| `VCFRONT_hpSubcoolTarget` | page 5 | Front body controller: hp subcool target | 16\|5 | little-endian | unsigned | 1 | 0 | degC | 0 to 31 |  | validated |
| `VCFRONT_CMPDischargeSuperheat` | page 5 | Front body controller: CMP discharge superheat | 21\|5 | little-endian | signed | 1 | 6 | degC | -10 to 21 |  | validated |
| `VCFRONT_hpCOP` | page 5 | Front body controller: hp COP | 26\|6 | little-endian | unsigned | 0.1 | 0 | - | 0 to 6 |  | validated |
| `VCFRONT_lowSideWattsLift` | page 5 | Front body controller: low side watts lift | 32\|7 | little-endian | unsigned | 60 | 0 | W | 0 to 7600 |  | validated |
| `VCFRONT_tempSuperheatActual` | page 5 | Front body controller: temp superheat actual; raw 1023 = signal not available (SNA) | 39\|10 | little-endian | unsigned | 0.1 | -20 | degC | -20 to 80 | 1023 = `SNA` | validated |
| `VCFRONT_tempSuperheatTarget` | page 5 | Front body controller: temp superheat target | 49\|10 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 60 |  | validated |
| `VCFRONT_refrigerantHasBeenFilled` | page 5 | Front body controller: refrigerant has been filled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_refCommissionStatus` | page 5 | Front body controller: ref commission status | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REFRIGERANT_UNKNOWN`<br>1 = `REFRIGERANT_UNCOMMISSIONED`<br>2 = `REFRIGERANT_COMMISSIONED` | validated |
| `VCFRONT_LCCPurgeActive` | page 5 | Reports if Liquid Cooled Condenser (LCC) refrigerant purge is active on the heat pump. | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_exteriorQuietModeEnabled` | page 6 | Front body controller: exterior quiet mode enabled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_exteriorQuietModeAllowed` | page 6 | Front body controller: exterior quiet mode allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_CCQdotFdFrwrdTarget` | page 6 | Front body controller: CC qdot fd frwrd target | 7\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | validated |
| `VCFRONT_CCQdotFdbk` | page 6 | Front body controller: CC qdot fdbk | 14\|7 | little-endian | signed | 80 | 0 | W | -5000 to 5000 |  | validated |
| `VCFRONT_CCQdotActual` | page 6 | Front body controller: CC qdot actual | 21\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | validated |
| `VCFRONT_evapFdFrwrdTarget` | page 6 | Front body controller: evap fd frwrd target | 28\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10100 |  | validated |
| `VCFRONT_evapFdbk` | page 6 | Front body controller: evap fdbk | 35\|7 | little-endian | signed | 100 | -3300 | W | -9700 to 3000 |  | validated |
| `VCFRONT_DIQdotA` | page 6 | Front body controller: DI qdot a | 42\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10000 |  | validated |
| `VCFRONT_evapFdFrwrdTargetMinimum` | page 6 | Front body controller: evap fd frwrd target minimum | 49\|7 | little-endian | unsigned | 80 | 0 | W | 0 to 10000 |  | validated |
| `VCFRONT_passiveCoolingState` | page 6 | Front body controller: passive cooling state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ChillerCoolsSeriesLoop`<br>1 = `ChillerCoolsParallelBattLoop`<br>2 = `ChillerAndRadCoolSeriesLoop`<br>3 = `CannotCoolBattery` | validated |
| `VCFRONT_totalLoadCoolingDominant` | page 6 | Front body controller: total load cooling dominant | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_feedfwdLoadCoolingDominant` | page 6 | Front body controller: feedfwd load cooling dominant | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_modelLoadCoolingDominant` | page 6 | Front body controller: model load cooling dominant | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpPotentialLowRefrig` | page 6 | Front body controller: hp potential low refrig | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpRefrigerantPurgeState` | page 6 | Front body controller: hp refrigerant purge state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `EVAP_PURGE`<br>2 = `COMPLETE` | validated |
| `VCFRONT_estPressureLiq` | page 7 | Front body controller: est pressure liq | 5\|6 | little-endian | unsigned | 0.5 | 0 | bar | 0 to 31 |  | validated |
| `VCFRONT_estPressureSuct` | page 7 | Front body controller: est pressure suct | 11\|7 | little-endian | unsigned | 0.125 | 0 | bar | 0 to 11.5 |  | validated |
| `VCFRONT_estPressureDisch` | page 7 | Front body controller: est pressure disch | 18\|7 | little-endian | unsigned | 0.25 | 0 | bar | 0 to 31.75 |  | validated |
| `VCFRONT_estTempLiq` | page 7 | Front body controller: est temp liq | 25\|8 | little-endian | signed | 0.8 | 68.8 | degC | -33 to 170 |  | validated |
| `VCFRONT_estTempSuct` | page 7 | Front body controller: est temp suct | 33\|6 | little-endian | signed | 1 | 2 | degC | -30 to 33 |  | validated |
| `VCFRONT_estTempDisch` | page 7 | Front body controller: est temp disch | 39\|7 | little-endian | signed | 1.5 | 75 | degC | -20 to 169 |  | validated |
| `VCFRONT_estCompressorRpm` | page 7 | Front body controller: est compressor rpm | 46\|9 | little-endian | unsigned | 30 | 0 | rpm | 0 to 15000 |  | validated |
| `VCFRONT_estQLift` | page 7 | Front body controller: est q lift | 55\|6 | little-endian | unsigned | 100 | 0 | W | 0 to 6300 |  | validated |
| `VCFRONT_cycleModelConverged` | page 7 | Front body controller: cycle model converged | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_compStandbyCoastDownMode` | page 7 | Front body controller: comp standby coast down mode | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_compStandbyShowroomMode` | page 7 | Front body controller: comp standby showroom mode | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chillerExvCalibOffset` | page 8 | Last calibration offset calculated for the Chiller EXV | 5\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_evapExvCalibOffset` | page 8 | Last calibration offset calculated for the Evaporator EXV | 10\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_recircExvCalibOffset` | page 8 | Last calibration offset calculated for the Recirc EXV | 15\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_lccExvCalibOffset` | page 8 | Last calibration offset calculated for the Liquid Cooled Condenser EXV | 20\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_ccLeftExvCalibOffset` | page 8 | Last calibration offset calculated for the Left Cabin Condenser EXV | 25\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_ccRightExvCalibOffset` | page 8 | Last calibration offset calculated for the Right Cabin Condenser EXV | 30\|5 | little-endian | signed | 8 | 0 | ticks | -127 to 120 |  | validated |
| `VCFRONT_chillerEXVControlState` | page 8 | Control State of the chiller electronic expansion valve | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_evapEXVControlState` | page 8 | Control State of the evaporator electronic expansion valve | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_recircEXVControlState` | page 8 | Control State of the recirc electronic expansion valve | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_lccEXVControlState` | page 8 | Control State of the liquid cooled condenser electronic expansion valve | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_cclEXVControlState` | page 8 | Control State of the chiller electronic expansion valve | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_ccrEXVControlState` | page 8 | Control State of the right cabin condenser electronic expansion valve | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `ACTIVE`<br>2 = `DISCHARGE`<br>3 = `CALIBRATING`<br>4 = `CALIBRATING_TIMEOUT`<br>5 = `PARKED` | validated |
| `VCFRONT_chillerExvCalibFailed` | page 8 | State of the last calibration for the Chiller EXV | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_evapExvCalibFailed` | page 8 | State of the last calibration for the Evaporator EXV | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_recircExvCalibFailed` | page 8 | State of the last calibration for the Recirc EXV | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_lccExvCalibFailed` | page 8 | State of the last calibration for the Liquid Cooled Condenser EXV | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ccLeftExvCalibFailed` | page 8 | State of the last calibration for the Left Cabin Condenser EXV | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ccRightExvCalibFailed` | page 8 | State of the last calibration for the Right Cabin Condenser EXV | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientTempSniffActive` | page 8 | Front body controller: ambient temp sniff active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientTempPassiveSniffing` | page 8 | Front body controller: ambient temp passive sniffing | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientTempRadSampling` | page 8 | Front body controller: ambient temp rad sampling | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientTempSpeedSampling` | page 8 | Front body controller: ambient temp speed sampling | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_feedFwdMDotEvaporator` | page 12 | Front body controller: feed fwd m dot evaporator | 5\|8 | little-endian | unsigned | 0.005 | 0 | - | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatBatteryHeatAmbSrc` | page 12 | Front body controller: hp cabin heat battery heat amb src | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatBatteryHeatCOP1` | page 12 | Front body controller: hp cabin heat battery heat COP1 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_feedFwdMDotCabinCondenser` | page 12 | Feed forward MDOT for the cabin condenser controller. | 15\|8 | little-endian | unsigned | 0.005 | 0 | - | 0 to 1 |  | validated |
| `VCFRONT_feedBackEvapTempController` | page 12 | Evap temperature controller feedback. | 23\|7 | little-endian | unsigned | 0.01 | -0.5 | - | -0.5 to 0.5 |  | validated |
| `VCFRONT_feedBackDuctTempController` | page 12 | Feedback for the duct temp controller. | 30\|8 | little-endian | unsigned | 0.01 | -1 | - | -1 to 1 |  | validated |
| `VCFRONT_isSolenoidAllowed` | page 12 | Front body controller: is solenoid allowed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_maxChillerCoolingPower` | page 12 | Front body controller: max chiller cooling power | 39\|8 | little-endian | unsigned | 100 | 0 | W | 0 to 20000 |  | validated |
| `VCFRONT_fanControlRadCanCool` | page 12 | Front body controller: fan control rad can cool | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_fanControlFeedfwdActive` | page 12 | Front body controller: fan control feedfwd active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_fanControlRadiatorUa` | page 12 | Front body controller: fan control radiator ua | 49\|7 | little-endian | unsigned | 8 | 0 | W/C | 0 to 1000 |  | validated |
| `VCFRONT_fanControlRadiatorInletTemp` | page 12 | Front body controller: fan control radiator inlet temp | 56\|6 | little-endian | signed | 1.8 | 36 | C | -20 to 90 |  | validated |
| `VCFRONT_hpASBatteryHeatingAllowed` | page 14 | Front body controller: hp AS battery heating allowed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCOP1BatteryHeatingAllowed` | page 14 | Front body controller: hp COP1 battery heating allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatScavengeOnly` | page 14 | Front body controller: hp cabin heat scavenge only | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatAmbientSource` | page 14 | Front body controller: hp cabin heat ambient source | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatReheatScavenge` | page 14 | Front body controller: hp cabin heat reheat scavenge | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatReheatAmbientSource` | page 14 | Front body controller: hp cabin heat reheat ambient source | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatBlend` | page 14 | Front body controller: hp cabin heat blend | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatCOP1` | page 14 | Front body controller: hp cabin heat COP1 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatBatteryHeatReheatAmbSrc` | page 14 | Front body controller: hp cabin heat battery heat reheat amb src | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinHeatBatteryCoolReheat` | page 14 | Front body controller: hp cabin heat battery cool reheat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_evapDisabledLowPsCutout` | page 14 | Position from firmware; message assignment inferred. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpCabinCoolEvaporatorReheat` | page 14 | Front body controller: hp cabin cool evaporator reheat | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryHeatAmbientSource` | page 14 | Front body controller: hp battery heat ambient source | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryHeatCOP1` | page 14 | Front body controller: hp battery heat COP1 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryCool` | page 14 | Front body controller: hp battery cool | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryCoolCabinCondenserCD` | page 14 | Front body controller: hp battery cool cabin condenser CD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryCoolCabinCondenserHD` | page 14 | Front body controller: hp battery cool cabin condenser HD | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryCoolCabinReheat` | page 14 | Front body controller: hp battery cool cabin reheat | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBatteryCoolEvaporator` | page 14 | Front body controller: hp battery cool evaporator | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_suctionSuperheatEstTsSNA` | page 14 | Front body controller: suction superheat est ts SNA | 24\|4 | little-endian | unsigned | 2 | 0 | degC | 0 to 30 |  | validated |
| `VCFRONT_tempRefrigSuctionEst` | page 14 | Front body controller: temp refrig suction est | 28\|6 | little-endian | signed | 1.2 | 7.2 | degC | -25 to 37.2 |  | contradicted |
| `VCFRONT_hpBattOverTempHvacDisable` | page 14 | Front body controller: hp batt over temp hvac disable | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpDiagLouverCalib` | page 14 | Diagnostics requested a louver calibration. | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpDiagHighSideNotNominal` | page 14 | Front body controller: hp diag high side not nominal | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpForceModeRadClear` | page 14 | Front body controller: hp force mode rad clear | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientSourcingDisabled` | page 14 | Position from firmware; message assignment inferred. | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_chillerLiftDisabledLowPs` | page 14 | Position from firmware; message assignment inferred. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_tempRefrigLiquid` | page 14 | Refrigerant system liquid line temperature; raw 2047 = signal not available (SNA) | 45\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 | 2047 = `SNA` | validated |
| `VCFRONT_maxCompressorRPMAllowed` | page 14 | Position from firmware; message assignment inferred. | 56\|7 | little-endian | unsigned | 90 | 0 | rpm | 0 to 11430 |  | plausible |
| `VCFRONT_hpPotentialFrozenRadiator` | page 14 | Front body controller: hp potential frozen radiator | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpForceScavenge` | page 16 | Position from firmware; message assignment inferred. | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_battOverStagUpperLimit` | page 16 | Position from firmware; message assignment inferred. | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_battUnderStagUpperLimit` | page 16 | Position from firmware; message assignment inferred. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientColderThanBatt` | page 16 | Position from firmware; message assignment inferred. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ambientSourcingAvailable` | page 16 | Position from firmware; message assignment inferred. | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_hpMode` | page 16 | Position from firmware; message assignment inferred. | 10\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `GENERAL`<br>2 = `AMBIENT_SOURCE`<br>3 = `CABIN_HEAT_SCAVENGE_ONLY`<br>4 = `CABIN_HEAT_AMBIENT_SOURCE`<br>5 = `CABIN_HEAT_REHEAT_SCAVENGE`<br>6 = `CABIN_HEAT_REHEAT_AMBIENT_SOURCE`<br>7 = `CABIN_HEAT_BLEND`<br>8 = `CABIN_HEAT_COP1`<br>9 = `CABIN_HEAT_BATTERY_HEAT_REHEAT_AMBIENT_SOURCE`<br>10 = `CABIN_HEAT_BATTERY_COOL_REHEAT`<br>11 = `CABIN_COOL_EVAPORATOR`<br>12 = `CABIN_COOL_EVAPORATOR_REHEAT`<br>13 = `BATTERY_HEAT_AMBIENT_SOURCE`<br>14 = `BATTERY_HEAT_COP1`<br>15 = `BATTERY_COOL`<br>16 = `BATTERY_COOL_CC_HEATING_DOMINANT`<br>17 = `BATTERY_COOL_CC_COOLING_DOMINANT`<br>18 = `BATTERY_COOL_CABIN_REHEAT`<br>19 = `BATTERY_COOL_EVAPORATOR`<br>20 = `BATTERY_HEAT_CABIN_HEAT_AMBIENT_SOURCE`<br>21 = `BATTERY_HEAT_CABIN_HEAT_COP1`<br>22 = `CABIN_COOL_EVAPORATOR_BATTERY_HEAT_AMBIENT_SOURCE`<br>23 = `BATTERY_HEAT_CABIN_HEAT_COP1_CHILLER` | plausible |
| `VCFRONT_battLoopWorthCooling` | page 16 | Position from firmware; message assignment inferred. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ptLoopWorthCooling` | page 16 | Position from firmware; message assignment inferred. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_estCompRefrigMassflow` | page 16 | Position from firmware; message assignment inferred. | 17\|6 | little-endian | unsigned | 4 | 0 | g/s | 0 to 251 |  | plausible |
| `VCFRONT_pressureRefrigDischEst` | page 16 | Position from firmware; message assignment inferred. | 23\|5 | little-endian | unsigned | 1 | 0 | bar | 0 to 31 |  | plausible |
| `VCFRONT_coolantValveDailyAngleTravel` | page 16 | Running 10-day average of daily angular travel | 30\|7 | little-endian | unsigned | 60 | 0 | degrees | 0 to 7500 |  | validated |
| `VCFRONT_dischargePressureLimit` | page 16 | Front body controller: discharge pressure limit | 37\|7 | little-endian | unsigned | 0.25 | 0 | bar | 0 to 26 |  | validated |
| `VCFRONT_radMovementBlockActive` | page 16 | Front body controller: rad movement block active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radBypassMoveReason` | page 16 | Front body controller: rad bypass move reason | 45\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT_UNBYPASS`<br>1 = `INIT_BYPASS`<br>2 = `PASSIVE_UNBYPASS`<br>3 = `PASSIVE_BYPASS`<br>4 = `RAD_HEAT_BYPASS`<br>5 = `RAD_HEAT_UNBYPASS`<br>6 = `ACTIVE_PT_UNBYPASS`<br>7 = `ACTIVE_BATT_UNBYPASS`<br>8 = `EXIT_SERIES`<br>9 = `UDS`<br>10 = `HEATPUMP`<br>11 = `DRIVERLESS_SELF_TEST` | validated |
| `VCFRONT_hpAtSteadyState` | page 16 | Position from firmware; message assignment inferred. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_suctionSuperheatEstPsSNA` | page 16 | Position from firmware; message assignment inferred. | 57\|4 | little-endian | unsigned | 2 | 0 | degC | 0 to 30 |  | plausible |
| `VCFRONT_targetPTActiveCoolSource` | page 16 | Front body controller: target PT active cool source | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BMS`<br>1 = `UI`<br>2 = `DAS`<br>3 = `PCS`<br>4 = `LCC`<br>5 = `DIF`<br>6 = `DIR`<br>7 = `OVERRIDE` | validated |
| `VCFRONT_hpColdStagnationLimit` | page 17 | Front body controller: hp cold stagnation limit | 8\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 80 |  | validated |
| `VCFRONT_hpHotStagnationLimit` | page 17 | Front body controller: hp hot stagnation limit | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 80 |  | validated |
| `VCFRONT_hpCompFlowIndex` | page 17 | Front body controller: hp comp flow index | 23\|8 | little-endian | unsigned | 1 | 30 | - | 30 to 255 |  | validated |
| `VCFRONT_hpCompFlowIndexFiltered` | page 17 | Front body controller: hp comp flow index filtered | 31\|8 | little-endian | unsigned | 1 | 30 | - | 30 to 255 |  | validated |
| `VCFRONT_subcoolEstTlSNA` | page 17 | Front body controller: subcool est tl SNA | 39\|6 | little-endian | signed | 2 | 0 | degC | -10 to 53 |  | validated |
| `VCFRONT_subcoolEstPlSNA` | page 17 | Front body controller: subcool est pl SNA | 45\|6 | little-endian | signed | 2 | 0 | degC | -10 to 53 |  | validated |
| `VCFRONT_tempRefrigLiquidEst` | page 17 | Front body controller: temp refrig liquid est | 51\|6 | little-endian | unsigned | 2 | 0 | degC | 0 to 125 |  | validated |
| `VCFRONT_pressureRefrigLiquidEst` | page 17 | Front body controller: pressure refrig liquid est | 57\|6 | little-endian | unsigned | 0.5 | 0 | bar | 0 to 31 |  | validated |
| `VCFRONT_cmpIsentropicCheckPassed` | page 17 | Front body controller: cmp isentropic check passed | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_louverPosReason` | page 18 | Front body controller: louver pos reason | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `CONDENSOR_MANAGER`<br>2 = `PASSIVE_MANAGER`<br>3 = `SNIFFING`<br>4 = `BOUNDS_CHECK`<br>5 = `FAN_RUN`<br>6 = `FAN_FAULT`<br>7 = `COAST_MODE`<br>8 = `UDS`<br>9 = `HIGH_SPEED`<br>10 = `BATTERY_DISCHARGE`<br>11 = `DRIVERLESS_SELF_TEST` | validated |
| `VCFRONT_hpEnergyFlowIndex` | page 18 | Front body controller: hp energy flow index | 9\|8 | little-endian | unsigned | 4 | 0 | - | 0 to 1020 |  | validated |
| `VCFRONT_hpEnergyFlowIndexFiltered` | page 18 | Refrigerant system modeled energy flow index filtered | 17\|8 | little-endian | unsigned | 4 | 0 | - | 0 to 1020 |  | validated |
| `VCFRONT_ductLeftAtSS` | page 18 | Front body controller: duct left at SS | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ductRightAtSS` | page 18 | Front body controller: duct right at SS | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_minCompressorRPMAllowed` | page 18 | Front body controller: min compressor RPM allowed | 27\|7 | little-endian | unsigned | 90 | 0 | rpm | 0 to 11430 |  | validated |
| `VCFRONT_ccRefrigerantMassFlow` | page 18 | Front body controller: cc refrigerant mass flow | 34\|6 | little-endian | unsigned | 4 | 0 | g/s | 0 to 251 |  | validated |
| `VCFRONT_highSideDpResidual` | page 18 | Front body controller: high side dp residual | 40\|7 | little-endian | signed | 0.1 | 0 | bar | -6 to 6 |  | validated |
| `VCFRONT_abnormalHighSuctionSuperheat` | page 18 | Front body controller: abnormal high suction superheat | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_coolantValveAngleTravel` | page 18 | Total angular travel since last (re)calibration | 48\|10 | little-endian | unsigned | 5 | 0 | degrees | 0 to 5000 |  | validated |
| `VCFRONT_chargeShuttleType` | page 18 | Front body controller: charge shuttle type | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHARGE_SHUTTLE_NONE`<br>1 = `CHARGE_SHUTTLE_STANDARD`<br>2 = `CHARGE_SHUTTLE_LCCR`<br>3 = `CHARGE_SHUTTLE_COP1` | validated |
| `VCFRONT_hpRefrigTempSensorCheckCanFire` | page 18 | Front body controller: hp refrig temp sensor check can fire | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpRefrigPressureSensorCheckCanFire` | page 18 | Front body controller: hp refrig pressure sensor check can fire | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_tempSuperheatActFiltered` | page 21 | Front body controller: temp superheat act filtered | 8\|8 | little-endian | signed | 0.25 | 26.5 | degC | -5 to 58 |  | validated |
| `VCFRONT_tempRefrigDischarge` | page 21 | Refrigerant system discharge temperature; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 | 2047 = `SNA` | validated |
| `VCFRONT_pumpBatteryRPMTarget` | page 21 | Front body controller: pump battery RPM target; raw 255 = signal not available (SNA) | 27\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | validated |
| `VCFRONT_pumpPowertrainRPMTarget` | page 21 | Front body controller: pump powertrain RPM target; raw 255 = signal not available (SNA) | 35\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | validated |
| `VCFRONT_coolantFlowChillerTarget` | page 21 | Front body controller: coolant flow chiller target | 43\|8 | little-endian | unsigned | 0.161 | 0 | LPM | 0 to 25 |  | validated |
| `VCFRONT_radiatorFanRPMTarget` | page 21 | Front body controller: radiator fan RPM target; raw 255 = signal not available (SNA) | 51\|8 | little-endian | unsigned | 40 | 0 | rpm | 0 to 10000 | 255 = `SNA` | validated |
| `VCFRONT_preventReEntryTillNexthpResetCOP1` | page 21 | Front body controller: prevent re entry till nexthp reset COP1 | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chillerBattHeatingPowerAvailable` | page 21 | Front body controller: chiller batt heating power available | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isExpectedQChillerVeryHighCOP1` | page 21 | Front body controller: is expected q chiller very high COP1 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_autopilotAirPurgeRoutineCounter` | page 21 | Front body controller: autopilot air purge routine counter | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `VCFRONT_superheatProtectionLimit` | page 25 | Front body controller: superheat protection limit | 5\|10 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 60 |  | validated |
| `VCFRONT_chillerDemandWatts` | page 25 | Front body controller: chiller demand watts | 16\|8 | little-endian | unsigned | 100 | 0 | W | 0 to 20000 |  | validated |
| `VCFRONT_nominalTevapHWLimit` | page 25 | Front body controller: nominal tevap HW limit | 24\|7 | little-endian | unsigned | 0.5 | 0 | degC | 0 to 60 |  | validated |
| `VCFRONT_battCoolEvapEnableDelay` | page 25 | Front body controller: batt cool evap enable delay | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ambientTempState` | page 25 | Front body controller: ambient temp state | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `MEASUREING`<br>2 = `LATCHED`<br>3 = `SNIFFING` | validated |
| `VCFRONT_ambientTempUnlatchReason` | page 25 | Front body controller: ambient temp unlatch reason | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `VEHICLE_SPEED`<br>2 = `FAN_AIRFLOW`<br>3 = `LOUVERS_CLOSED`<br>4 = `SNIFF_TIMEBASED`<br>5 = `SNIFF_BLOCKED`<br>6 = `SNIFF_STARTDRIVE` | validated |
| `VCFRONT_compressorSuctionVaporQuality` | page 25 | Front body controller: compressor suction vapor quality | 40\|5 | little-endian | unsigned | 0.01 | 0.7 | - | 0.7 to 1 |  | validated |
| `VCFRONT_cabinHeatingCOP1MinActiveRefCharge` | page 25 | Estimation of minimal active refrigerant charge during cabin heating COP1 mode | 48\|7 | little-endian | unsigned | 10 | 0 | - | 0 to 1100 |  | validated |
| `VCFRONT_hpDuctTargetLeft` | page 26 | Front body controller: hp duct target left | 8\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 65 |  | validated |
| `VCFRONT_hpDuctTargetRight` | page 26 | Front body controller: hp duct target right | 16\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 65 |  | validated |
| `VCFRONT_radiatorUAIndex` | page 26 | Reports the radiator UA index in percentage defined as actual calculated UA divided by the expected nominal UA. | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCFRONT_maxBatInletCoolantTempAllowed` | page 26 | Front body controller: max bat inlet coolant temp allowed | 32\|5 | little-endian | unsigned | 1 | 40 | degC | 40 to 65 |  | validated |
| `VCFRONT_coolantTempInBypassDelta` | page 26 | Front body controller: coolant temp in bypass delta | 40\|5 | little-endian | unsigned | 1 | -20 | degC | -20 to 11 |  | validated |
| `VCFRONT_targetAPPActiveCool` | page 26 | Front body controller: target APP active cool | 48\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 100 |  | validated |

## Multiplexing

`VCFRONT_logging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals), page 1 (10 signals), page 2 (12 signals), page 3 (5 signals), page 4 (5 signals), page 5 (10 signals), page 6 (15 signals), page 7 (11 signals), page 8 (22 signals), page 12 (12 signals), page 14 (30 signals), page 16 (17 signals), page 17 (9 signals), page 18 (13 signals), page 21 (10 signals), page 25 (8 signals), page 26 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
