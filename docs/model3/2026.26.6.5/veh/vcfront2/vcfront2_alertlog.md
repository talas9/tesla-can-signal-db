---
layout: default
title: "VCFRONT2_alertLog (0x547) — VCFRONT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "VCFRONT2 ECU message: alert log. Tesla Model 3 CAN bus message VCFRONT2_alertLog (0x547) of VCFRONT2 ECU, firmware 2026.26.6.5, 454 signals (VCFRONT2_alertID, VCFRONT2_alertState, VCFRONT2_a001_InternalWatchdog, VCFRONT2_a015_NVMMMemOverflow and 450 more). Bit layout, scaling, units and value tables."
---

# VCFRONT2_alertLog (0x547) — VCFRONT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN

VCFRONT2 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 454 signals of VCFRONT2_alertLog as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT2_alertLog` |
| CAN id | 0x547 (1351) |
| ECU | [VCFRONT2 ECU](../../vcfront2.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT2 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 454 |

## Signals of VCFRONT2_alertLog

Tesla Model 3 CAN bus signals in `VCFRONT2_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT2_alertID` | selector | VCFRONT2 ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>4 = `a004_adaptiveHeadlightsUnavailable`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>8 = `a008_adaptiveHeadlightsUnavailableStalk`<br>9 = `a009_LCCPurgeAttempted`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>18 = `a018_HardFault`<br>19 = `a019_BusFault`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>28 = `a028_UsageFault`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>36 = `a036_UnknownIrq`<br>37 = `a037_MemManageFault`<br>38 = `a038_ProtFaultInfo`<br>39 = `a039_ProtFaultAddress`<br>40 = `a040_Backtrace`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>53 = `a053_wiperCommErrorUser`<br>54 = `a054_compressorLowFlowUserFacing`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>77 = `a077_VCBATT0_MIA`<br>78 = `a078_VCBATT1_MIA`<br>79 = `a079_VCBATT2_MIA`<br>80 = `a080_VCFRONT0_MIA`<br>81 = `a081_VCFRONT1_MIA`<br>82 = `a082_VCFRONT2_MIA`<br>86 = `a086_VCBATT_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>96 = `a096_OCS1P_MIA`<br>98 = `a098_DIR_MIA`<br>100 = `a100_CANbus_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>122 = `a122_ICR_MIA`<br>123 = `a123_VC_SECONDARY_LIGHTING_LEADER_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_SCCM_MIA`<br>126 = `a126_EPAS3P_MIA`<br>131 = `a131_PCSCOMMON_MIA`<br>133 = `a133_BRAKE_MIA`<br>135 = `a135_coolantLevelLow`<br>136 = `a136_refrigDischTempSns`<br>137 = `a137_refrigDischPresSns`<br>138 = `a138_refrigSuctTempSns`<br>139 = `a139_refrigSuctPresSns`<br>140 = `a140_coolantTempPtSns`<br>141 = `a141_coolantTempBatSns`<br>142 = `a142_exvMotorFault`<br>143 = `a143_powerLossDuringSleep`<br>144 = `a144_EPAS3S_MIA`<br>150 = `a150_pumpBatLowRPMCBang`<br>153 = `a153_userPresenceDisplayMismatchClrd`<br>155 = `a155_autopilotDriveNotAuthed`<br>159 = `a159_coolantValveFault`<br>160 = `a160_compressorInhibited`<br>161 = `a161_compressorSelfFault`<br>162 = `a162_compressorInhibitedContext`<br>163 = `a163_compressorDisabledFSR`<br>167 = `a167_leftHCMMIA`<br>171 = `a171_driveBlckdByMsmtch`<br>172 = `a172_wsteHtBlckdByMsmtch`<br>173 = `a173_HVBlckdByMsmtch`<br>174 = `a174_driveNotAuthed`<br>176 = `a176_vehicleInSelfTest`<br>178 = `a178_compLiquidPumpOut`<br>184 = `a184_cabinCoolingPerformanceAbnormal`<br>186 = `a186_noDriveChgCableCon`<br>187 = `a187_busesNotSleeping`<br>188 = `a188_sleepFailed`<br>195 = `a195_drveBlckdVltgeTooHgh`<br>210 = `a210_coolantValveCalib`<br>214 = `a214_ptPumpCompromised`<br>215 = `a215_ptPumpMIA`<br>217 = `a217_battPumpCompromised`<br>218 = `a218_socMonitorDetectedThresholdSoc`<br>225 = `a225_driveBlckdByShowroom`<br>226 = `a226_battPumpMIA`<br>232 = `a232_lowSideControllerHighFdbk`<br>235 = `a235_ptTempSnsIrrational`<br>236 = `a236_batTempSnsIrrational`<br>240 = `a240_lowSideCompromised`<br>247 = `a247_evapSolenoidFault`<br>249 = `a249_coolantValveBadMode`<br>250 = `a250_headlampsNotAimed`<br>251 = `a251_UIWakeupTrigger`<br>254 = `a254_pumpBatStopped`<br>273 = `a273_wiperFrictionModelFault`<br>279 = `a279_refrigLiquidTempSns`<br>280 = `a280_refrigLiquidPresSns`<br>281 = `a281_alcoholInterlockBlockingDrive`<br>282 = `a282_coolantLevelSensorFault`<br>283 = `a283_thmlFanLimitedByCurrent`<br>284 = `a284_chillerExvFault`<br>285 = `a285_evaporatorExvFault`<br>286 = `a286_recircExvFault`<br>287 = `a287_lccExvFault`<br>288 = `a288_ccLeftExvFault`<br>289 = `a289_ccRightExvFault`<br>294 = `a294_leftSideRepeaterLightFault`<br>298 = `a298_radiatorLowAirFlowDetected`<br>301 = `a301_wipersFactoryDisabled`<br>302 = `a302_wiperCommError`<br>355 = `a355_coolantSysLockout`<br>356 = `a356_refrigSysLockout`<br>360 = `a360_ungracefulAccPlusExit`<br>365 = `a365_burnInRoutineEntered`<br>366 = `a366_burnInRoutineExited`<br>367 = `a367_dischargeRoutineEntered`<br>368 = `a368_dischargeRoutineExited`<br>369 = `a369_reducedPowerDischarge`<br>374 = `a374_lccInletSolenoidFault`<br>377 = `a377_wiperParkFault`<br>378 = `a378_wiperECUDebug`<br>380 = `a380_chillerExvWarning`<br>381 = `a381_evaporatorExvWarning`<br>382 = `a382_recircExvWarning`<br>383 = `a383_lccExvWarning`<br>384 = `a384_ccLeftExvWarning`<br>385 = `a385_ccRightExvWarning`<br>386 = `a386_exvMotorWarning`<br>393 = `a393_ambientTempNetworkSna`<br>394 = `a394_pressureSensorCheckFault`<br>395 = `a395_pressureSensorCheckInconclusive`<br>396 = `a396_coolantLevelLowUserFacing`<br>397 = `a397_temperatureSensorCheckFault`<br>398 = `a398_tempSensorCheckInconclusive`<br>409 = `a409_invalidConfiguration`<br>420 = `a420_holidayParty`<br>421 = `a421_leftHeadlampUartCondition`<br>423 = `a423_rtosSleepFailed`<br>446 = `a446_cabinHVACUnavailableContext`<br>447 = `a447_cabinHVACUnavailable`<br>451 = `a451_refrigerantNotCommissioned`<br>452 = `a452_dischargePresSensIntermittent`<br>453 = `a453_dischargeTempSensIntermittent`<br>454 = `a454_suctionPresSensIntermittent`<br>455 = `a455_suctionTempSensIntermittent`<br>456 = `a456_liquidPresSensIntermittent`<br>457 = `a457_liquidTempSensIntermittent`<br>458 = `a458_grosslyLowRefrigerant`<br>459 = `a459_thermalFillAndDrive`<br>460 = `a460_hardIsentropicTdFailed`<br>464 = `a464_highFlowIndexHighSubcoolFlagged`<br>465 = `a465_lowFlowIndexHighSubcoolFlagged`<br>466 = `a466_highFlowIndexLowSubcoolFlagged`<br>467 = `a467_lowPowerIndexFlagged`<br>468 = `a468_highPowerIndexFlagged`<br>469 = `a469_prvPopDetected`<br>470 = `a470_implausiblePdPlDetected`<br>471 = `a471_hcm5Debug`<br>474 = `a474_leftHeadlampInternalError`<br>489 = `a489_ValveStuckFlagged`<br>490 = `a490_coolantPumpsNotIdentified`<br>499 = `a499_loadShedPumpFlowRequest`<br>504 = `a504_airInRefrigerantDetected`<br>506 = `a506_invalidRefrigerantSystemConfig`<br>507 = `a507_leftHeadlampAimingFault`<br>511 = `a511_DCDCSaturationLoadShed`<br>519 = `a519_leftHeadlampInternalErrorV2`<br>531 = `a531_lowPowerIndexFlaggedUserFacing`<br>534 = `a534_chillerExvCalibInitDebug`<br>535 = `a535_evapExvCalibInitDebug`<br>536 = `a536_recircExvCalibInitDebug`<br>537 = `a537_lccExvCalibInitDebug`<br>538 = `a538_cclExvCalibInitDebug`<br>539 = `a539_ccrExvCalibInitDebug`<br>540 = `a540_radiatorSteamDetected`<br>542 = `a542_refrigerantReclaim`<br>543 = `a543_compressorLowFlowDeliveryDetected`<br>546 = `a546_leftLowOrHighBeamLightCondition`<br>549 = `a549_leftHeadlampInternalErrorV3`<br>560 = `a560_compressorHighSuperheat`<br>563 = `a563_chargePortDoorOpenBlockedByBrake`<br>564 = `a564_leftHeadlampAimingDebug`<br>565 = `a565_userPresenceDisplayStateMismatch`<br>566 = `a566_leftFrontTurnLightFault`<br>568 = `a568_leftDaytimeRunningLightFault`<br>570 = `a570_headlampsAdaptedToLeftHandTraffic`<br>571 = `a571_headlampsAdaptedToRightHandTraffic`<br>572 = `a572_hvacCompressorEFuseTrip`<br>578 = `a578_vbusFusedLowCurrentFeedEFuseTrip`<br>585 = `a585_bothHeadlampsInternalError`<br>601 = `a601_autopilotAirPurgeLimitReached`<br>602 = `a602_unknownTurnIndicatorConfig`<br>603 = `a603_unexpectedTurnIndicatorConfigChange`<br>604 = `a604_turnIndicatorConfigInputMismatch`<br>606 = `a606_chillerBattHeatingExit`<br>610 = `a610_driveEntryDelayed`<br>611 = `a611_poorRadiatorHeatRejection`<br>612 = `a612_selfTestsBlockingDrive`<br>614 = `a614_coolantSysDriverlessSelfTest`<br>615 = `a615_VCSEAT2L_MIA`<br>616 = `a616_VCSEAT2R_MIA`<br>617 = `a617_APP_MIA`<br>618 = `a618_cabinCoolingCapacityLimited`<br>620 = `a620_pumpAirLock`<br>621 = `a621_coolantAirPurgeIncomplete`<br>622 = `a622_pumpDetectsLowCoolantFlow`<br>625 = `a625_leftHeadlampInternalErrorV4`<br>630 = `a630_leftHeadlampFactoryFault`<br>636 = `d636_ptCoolantPumpDetectsAirInSystem`<br>637 = `d637_battCoolantPumpDetectsAirInSystem`<br>638 = `d638_ptCoolantTempSensorIssue`<br>639 = `d639_batteryCoolantTempSensorIssue`<br>640 = `d640_firmwareVersionMismatch`<br>641 = `d641_ptCoolantPumpCircuitOpen`<br>642 = `d642_batteryCoolantPumpCircuitOpen`<br>647 = `d647_louverCommLost`<br>648 = `d648_louverBlocked`<br>650 = `d650_lowCoolantLevel`<br>651 = `d651_ptCoolantPumpStall`<br>652 = `d652_ptCoolantPumpCircuitIssue`<br>653 = `d653_ptCoolantPumpCommLost`<br>654 = `d654_batteryCoolantPumpStall`<br>655 = `d655_batteryCoolantPumpCircuitIssue`<br>656 = `d656_batteryCoolantPumpCommLost`<br>657 = `d657_radiatorFanOperationIssue`<br>658 = `d658_radiatorFanCircuitIssue`<br>659 = `d659_radiatorFanCommLost`<br>660 = `d660_coolantValveCircuitIssue`<br>661 = `a661_mculessLeftHeadlampCurrentAlertDbg`<br>662 = `a662_driveExitBlockedIndefinitelyBySelfTestRequest`<br>663 = `a663_leftHeadlampUartWaterMarkWarning`<br>665 = `a665_leftHeadlampRetryInfo`<br>667 = `a667_leftHeadlampRegionOrSideMismatch`<br>669 = `a669_thermalHVPowerBudgetActive`<br>697 = `a697_leftHeadlampNotAimed`<br>702 = `a702_dynamicHeadlightLevelingUnavailable` | plausible |
| `VCFRONT2_alertState` |  | VCFRONT2 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCFRONT2_a001_InternalWatchdog` | page 1 | VCFRONT2 ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a015_NVMMMemOverflow` | page 15 | VCFRONT2 ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a015_NVMMFilesystemError` | page 15 | VCFRONT2 ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a015_NVMMRecordIDError` | page 15 | VCFRONT2 ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a059_voltageDrop` | page 59 | VCFRONT2 ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT2_a059_resistanceEstimate` | page 59 | VCFRONT2 ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCFRONT2_a059_current` | page 59 | VCFRONT2 ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCFRONT2_a063_switchChannel` | page 63 | VCFRONT2 ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT2_a063_switchType` | page 63 | VCFRONT2 ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT2_a063_ADCVoltage` | page 63 | VCFRONT2 ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCFRONT2_a063_disconnected` | page 63 | VCFRONT2 ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a063_indeterminate` | page 63 | VCFRONT2 ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a063_stuckActive` | page 63 | VCFRONT2 ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a063_faulted` | page 63 | VCFRONT2 ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a091_FRONTIPC_faultsAndExtras` | page 91 | VCFRONT2 ECU: a091 FRONTIPC faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a091_FRONTIPC_state` | page 91 | VCFRONT2 ECU: a091 FRONTIPC state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a096_FRONTIPC_status` | page 96 | VCFRONT2 ECU: a096 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a098_FRONTIPC_temperature` | page 98 | VCFRONT2 ECU: a098 FRONTIPC temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a098_FRONTIPC_thermalControl` | page 98 | VCFRONT2 ECU: a098 FRONTIPC thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_BATTIPC_dcdcRailStatus` | page 106 | VCFRONT2 ECU: a106 BATTIPC dcdc rail status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_BATTIPC_dcdcStatus` | page 106 | VCFRONT2 ECU: a106 BATTIPC dcdc status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_VEH_dcdcStatus` | page 106 | VCFRONT2 ECU: a106 VEH dcdc status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_VEH_thermalControl` | page 106 | VCFRONT2 ECU: a106 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_VEH_dcdcRailStatus` | page 106 | VCFRONT2 ECU: a106 VEH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_CH_dcdcRailStatus` | page 106 | VCFRONT2 ECU: a106 CH dcdc rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_CH_alertMatrix` | page 106 | VCFRONT2 ECU: a106 CH alert matrix | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_FRONTIPC_thermalControl` | page 106 | VCFRONT2 ECU: a106 FRONTIPC thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_FRONTIPC_dcdcRailStatus` | page 106 | VCFRONT2 ECU: a106 FRONTIPC dcdc rail status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_FRONTIPC_dcdcStatus` | page 106 | VCFRONT2 ECU: a106 FRONTIPC dcdc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a108_FRONTIPC_status` | page 108 | VCFRONT2 ECU: a108 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a108_FRONTIPC_temperature` | page 108 | VCFRONT2 ECU: a108 FRONTIPC temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a108_FRONTIPC_thermalControl` | page 108 | VCFRONT2 ECU: a108 FRONTIPC thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a108_FRONTIPC_motorStatus` | page 108 | VCFRONT2 ECU: a108 FRONTIPC motor status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_BATTIPC_speed` | page 120 | VCFRONT2 ECU: a120 BATTIPC speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_speed` | page 120 | VCFRONT2 ECU: a120 FRONTIPC speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_systemStatus` | page 120 | VCFRONT2 ECU: a120 FRONTIPC system status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_BATTIPC_systemStatus` | page 120 | VCFRONT2 ECU: a120 BATTIPC system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_systemPower` | page 120 | VCFRONT2 ECU: a120 FRONTIPC system power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_autonomyHealth` | page 120 | VCFRONT2 ECU: a120 FRONTIPC autonomy health | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_BATTIPC_chassisControl2` | page 120 | VCFRONT2 ECU: a120 BATTIPC chassis control2 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_chassisControl2` | page 120 | VCFRONT2 ECU: a120 FRONTIPC chassis control2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_FRONTIPC_odometerStatus` | page 120 | VCFRONT2 ECU: a120 FRONTIPC odometer status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a124_FRONTIPC_status` | page 124 | VCFRONT2 ECU: a124 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a124_BATTIPC_status` | page 124 | VCFRONT2 ECU: a124 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a125_FRONTIPC_leftStalk` | page 125 | VCFRONT2 ECU: a125 FRONTIPC left stalk | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a125_FRONTIPC_steerAngle` | page 125 | VCFRONT2 ECU: a125 FRONTIPC steer angle | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a125_FRONTIPC_info` | page 125 | VCFRONT2 ECU: a125 FRONTIPC info | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a126_FRONTIPC_sysStatus` | page 126 | VCFRONT2 ECU: a126 FRONTIPC sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a126_BATTIPC_sysStatus` | page 126 | VCFRONT2 ECU: a126 BATTIPC sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a126_FRONTIPC_status` | page 126 | VCFRONT2 ECU: a126 FRONTIPC status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a126_BATTIPC_status` | page 126 | VCFRONT2 ECU: a126 BATTIPC status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a131_FRONTIPC_power` | page 131 | VCFRONT2 ECU: a131 FRONTIPC power | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a131_BATTIPC_power` | page 131 | VCFRONT2 ECU: a131 BATTIPC power | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a133_BATTIPC_primaryActuator` | page 133 | VCFRONT2 ECU: a133 BATTIPC primary actuator | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a133_FRONTIPC_secondaryActuator` | page 133 | VCFRONT2 ECU: a133 FRONTIPC secondary actuator | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_driverState` | page 142 | VCFRONT2 ECU: a142 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a142_driverThermWarn` | page 142 | VCFRONT2 ECU: a142 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_driverThermShutdown` | page 142 | VCFRONT2 ECU: a142 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_undervoltage` | page 142 | VCFRONT2 ECU: a142 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_chargePumpUndervoltage` | page 142 | VCFRONT2 ECU: a142 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilOpenX` | page 142 | VCFRONT2 ECU: a142 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilOpenY` | page 142 | VCFRONT2 ECU: a142 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortXPGnd` | page 142 | VCFRONT2 ECU: a142 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortXPVbb` | page 142 | VCFRONT2 ECU: a142 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortXNGnd` | page 142 | VCFRONT2 ECU: a142 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortXNVbb` | page 142 | VCFRONT2 ECU: a142 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortYPGnd` | page 142 | VCFRONT2 ECU: a142 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortYPVbb` | page 142 | VCFRONT2 ECU: a142 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortYNGnd` | page 142 | VCFRONT2 ECU: a142 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_isCoilShortYNVbb` | page 142 | VCFRONT2 ECU: a142 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_driverHasCommError` | page 142 | VCFRONT2 ECU: a142 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a144_FRONTIPC_status` | page 144 | VCFRONT2 ECU: a144 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a144_BATTIPC_status` | page 144 | VCFRONT2 ECU: a144 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a150_RPMActual` | page 150 | VCFRONT2 ECU: a150 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT2_a150_RPMTarget` | page 150 | VCFRONT2 ECU: a150 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT2_a159_stall` | page 159 | VCFRONT2 ECU: a159 stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a159_angleActual` | page 159 | VCFRONT2 ECU: a159 angle actual | 17\|10 | little-endian | unsigned | 0.25 | -70 | deg | -70 to 185.75 |  | plausible |
| `VCFRONT2_a159_angleTarget` | page 159 | VCFRONT2 ECU: a159 angle target | 27\|10 | little-endian | unsigned | 0.25 | -10 | deg | -10 to 245.75 |  | plausible |
| `VCFRONT2_a171_VCFRONT` | page 171 | VCFRONT2 ECU: a171 VCFRONT | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_VCRIGHT` | page 171 | VCFRONT2 ECU: a171 VCRIGHT | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_VCLEFT` | page 171 | VCFRONT2 ECU: a171 VCLEFT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_VCBATT` | page 171 | VCFRONT2 ECU: a171 VCBATT | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_BMS` | page 171 | VCFRONT2 ECU: a171 BMS | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_HVP` | page 171 | VCFRONT2 ECU: a171 HVP | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_GTW` | page 171 | VCFRONT2 ECU: a171 GTW | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_CP` | page 171 | VCFRONT2 ECU: a171 CP | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_PCS` | page 171 | VCFRONT2 ECU: a171 PCS | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_PCSCPU2` | page 171 | VCFRONT2 ECU: a171 PCSCPU2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_DI` | page 171 | VCFRONT2 ECU: a171 DI | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_DIS` | page 171 | VCFRONT2 ECU: a171 DIS | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_PM` | page 171 | VCFRONT2 ECU: a171 PM | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_PMS` | page 171 | VCFRONT2 ECU: a171 PMS | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_EPBR` | page 171 | VCFRONT2 ECU: a171 EPBR | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_EPBL` | page 171 | VCFRONT2 ECU: a171 EPBL | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_IBST` | page 171 | VCFRONT2 ECU: a171 IBST | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_IBSTCAL` | page 171 | VCFRONT2 ECU: a171 IBSTCAL | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_ESP` | page 171 | VCFRONT2 ECU: a171 ESP | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_ESPCAL` | page 171 | VCFRONT2 ECU: a171 ESPCAL | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_OPC` | page 171 | VCFRONT2 ECU: a171 OPC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_OPCS` | page 171 | VCFRONT2 ECU: a171 OPCS | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_SCCM` | page 171 | VCFRONT2 ECU: a171 SCCM | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_LVBMS` | page 171 | VCFRONT2 ECU: a171 LVBMS | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_IDB` | page 171 | VCFRONT2 ECU: a171 IDB | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_IDB1` | page 171 | VCFRONT2 ECU: a171 IDB1 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_IDBCAL` | page 171 | VCFRONT2 ECU: a171 IDBCAL | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_RCU` | page 171 | VCFRONT2 ECU: a171 RCU | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_RCUCAL` | page 171 | VCFRONT2 ECU: a171 RCUCAL | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_DPB` | page 171 | VCFRONT2 ECU: a171 DPB | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_DPBCAL` | page 171 | VCFRONT2 ECU: a171 DPBCAL | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_serviceMode` | page 171 | Signal reported by VCFRONT2 ECU | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a172_ECUMismatchBits` | page 172 | VCFRONT2 ECU: a172 ECU mismatch bits | 16\|47 | little-endian | unsigned | 1 | 0 |  | 0 to 140737488355327 |  | layout-only |
| `VCFRONT2_a172_serviceMode` | page 172 | Signal reported by VCFRONT2 ECU | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a173_ECUMismatchBits` | page 173 | VCFRONT2 ECU: a173 ECU mismatch bits | 16\|47 | little-endian | unsigned | 1 | 0 |  | 0 to 140737488355327 |  | layout-only |
| `VCFRONT2_a173_serviceMode` | page 173 | Signal reported by VCFRONT2 ECU | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a176_vehicleState` | page 176 | VCFRONT2 ECU: a176 vehicle state | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `LOW_POWER_AWAKE`<br>2 = `CONDITIONING`<br>3 = `ACCESSORY`<br>4 = `ACCESSORY_PLUS`<br>5 = `DRIVE`<br>6 = `OTA`<br>7 = `WAIT_FOR_HIGH_POWER`<br>8 = `TURN_ON_LV`<br>9 = `SYSTEM_CHECKS`<br>10 = `LV_ON`<br>11 = `JUMP_START`<br>12 = `LV_SHUTDOWN`<br>13 = `GO_QUIET`<br>14 = `SLEEP_SHUTDOWN`<br>15 = `LOW_POWER_STANDBY`<br>16 = `RESET` | plausible |
| `VCFRONT2_a186_noDriveChgCableConX` | page 186 | VCFRONT2 ECU: a186 no drive chg cable con x | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a187_vehBusRetryCount` | page 187 | VCFRONT2 ECU: a187 veh bus retry count | 16\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT2_a187_partyBusRetryCount` | page 187 | VCFRONT2 ECU: a187 party bus retry count | 25\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT2_a187_hvsBusRetryCount` | page 187 | VCFRONT2 ECU: a187 hvs bus retry count | 34\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT2_a187_ethBusRetryCount` | page 187 | VCFRONT2 ECU: a187 eth bus retry count | 43\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT2_a187_chBusRetryCount` | page 187 | VCFRONT2 ECU: a187 ch bus retry count | 52\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT2_a195_LVVoltage` | page 195 | VCFRONT2 ECU: a195 LV voltage | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT2_a195_serviceMode` | page 195 | Signal reported by VCFRONT2 ECU | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a195_frunkOpen` | page 195 | VCFRONT2 ECU: a195 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a210_valveUnderTravel` | page 210 | VCFRONT2 ECU: a210 valve under travel | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a210_valveOverTravel` | page 210 | VCFRONT2 ECU: a210 valve over travel | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a210_valveNoTravel` | page 210 | VCFRONT2 ECU: a210 valve no travel | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorFaulted` | page 214 | VCFRONT2 ECU: a214 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorLocked` | page 214 | VCFRONT2 ECU: a214 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_ecuReset` | page 214 | VCFRONT2 ECU: a214 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_fetTempIrrational` | page 214 | VCFRONT2 ECU: a214 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorControlError` | page 214 | VCFRONT2 ECU: a214 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_underVoltage` | page 214 | VCFRONT2 ECU: a214 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_overVoltage` | page 214 | VCFRONT2 ECU: a214 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_hardwareOvercurrent` | page 214 | VCFRONT2 ECU: a214 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorOpenPhase` | page 214 | VCFRONT2 ECU: a214 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorSoftOpenPhase` | page 214 | VCFRONT2 ECU: a214 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorOvertemp` | page 214 | VCFRONT2 ECU: a214 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_dcOvercurrent` | page 214 | VCFRONT2 ECU: a214 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorStalled` | page 214 | VCFRONT2 ECU: a214 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_selfTestFailed` | page 214 | VCFRONT2 ECU: a214 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_selfTestResult` | page 214 | VCFRONT2 ECU: a214 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCFRONT2_a214_linChecksumError` | page 214 | VCFRONT2 ECU: a214 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_linFramingError` | page 214 | VCFRONT2 ECU: a214 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_phaseShorted` | page 214 | VCFRONT2 ECU: a214 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_busVoltageIrrational` | page 214 | VCFRONT2 ECU: a214 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_dcCurrentIrrational` | page 214 | VCFRONT2 ECU: a214 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorSpeedIrrational` | page 214 | VCFRONT2 ECU: a214 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_supplyVoltageIrrational` | page 214 | VCFRONT2 ECU: a214 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorPhaseCurrentIrrational` | page 214 | VCFRONT2 ECU: a214 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_chipOvertemp` | page 214 | VCFRONT2 ECU: a214 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_motorSpeedTooHigh` | page 214 | VCFRONT2 ECU: a214 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_phaseOvercurrent` | page 214 | VCFRONT2 ECU: a214 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_vddaOvercurrent` | page 214 | VCFRONT2 ECU: a214 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_busVoltageUnhealthy` | page 214 | VCFRONT2 ECU: a214 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_hsVdsOvervoltage` | page 214 | VCFRONT2 ECU: a214 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_hsVdsOvervoltageMask` | page 214 | VCFRONT2 ECU: a214 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT2_a214_lsVdsOvervoltage` | page 214 | VCFRONT2 ECU: a214 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_lsVdsOvervoltageMask` | page 214 | VCFRONT2 ECU: a214 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT2_a214_payloadBitsNotSet` | page 214 | VCFRONT2 ECU: a214 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorFaulted` | page 217 | VCFRONT2 ECU: a217 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorLocked` | page 217 | VCFRONT2 ECU: a217 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_ecuReset` | page 217 | VCFRONT2 ECU: a217 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_fetTempIrrational` | page 217 | VCFRONT2 ECU: a217 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorControlError` | page 217 | VCFRONT2 ECU: a217 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_underVoltage` | page 217 | VCFRONT2 ECU: a217 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_overVoltage` | page 217 | VCFRONT2 ECU: a217 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_hardwareOvercurrent` | page 217 | VCFRONT2 ECU: a217 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorOpenPhase` | page 217 | VCFRONT2 ECU: a217 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorSoftOpenPhase` | page 217 | VCFRONT2 ECU: a217 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorOvertemp` | page 217 | VCFRONT2 ECU: a217 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_dcOvercurrent` | page 217 | VCFRONT2 ECU: a217 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorStalled` | page 217 | VCFRONT2 ECU: a217 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_selfTestFailed` | page 217 | VCFRONT2 ECU: a217 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_selfTestResult` | page 217 | VCFRONT2 ECU: a217 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCFRONT2_a217_linChecksumError` | page 217 | VCFRONT2 ECU: a217 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_linFramingError` | page 217 | VCFRONT2 ECU: a217 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_phaseShorted` | page 217 | VCFRONT2 ECU: a217 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_busVoltageIrrational` | page 217 | VCFRONT2 ECU: a217 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_dcCurrentIrrational` | page 217 | VCFRONT2 ECU: a217 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorSpeedIrrational` | page 217 | VCFRONT2 ECU: a217 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_supplyVoltageIrrational` | page 217 | VCFRONT2 ECU: a217 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorPhaseCurrentIrrational` | page 217 | VCFRONT2 ECU: a217 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_chipOvertemp` | page 217 | VCFRONT2 ECU: a217 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_motorSpeedTooHigh` | page 217 | VCFRONT2 ECU: a217 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_phaseOvercurrent` | page 217 | VCFRONT2 ECU: a217 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_vddaOvercurrent` | page 217 | VCFRONT2 ECU: a217 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_busVoltageUnhealthy` | page 217 | VCFRONT2 ECU: a217 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_hsVdsOvervoltage` | page 217 | VCFRONT2 ECU: a217 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_hsVdsOvervoltageMask` | page 217 | VCFRONT2 ECU: a217 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT2_a217_lsVdsOvervoltage` | page 217 | VCFRONT2 ECU: a217 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_lsVdsOvervoltageMask` | page 217 | VCFRONT2 ECU: a217 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT2_a217_payloadBitsNotSet` | page 217 | VCFRONT2 ECU: a217 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a235_ptSensorTemp` | page 235 | VCFRONT2 ECU: a235 pt sensor temp | 16\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT2_a236_batSensorTemp` | page 236 | VCFRONT2 ECU: a236 bat sensor temp | 16\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT2_a247_solenoidISense` | page 247 | VCFRONT2 ECU: a247 solenoid i sense | 16\|8 | little-endian | signed | 0.01 | 0 | A | -1.28 to 1.27 |  | plausible |
| `VCFRONT2_a249_tempCoolantBatInlet` | page 249 | VCFRONT2 ECU: a249 temp coolant bat inlet | 16\|10 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 87.875 |  | plausible |
| `VCFRONT2_a249_tempCoolantPTInlet` | page 249 | VCFRONT2 ECU: a249 temp coolant PT inlet | 26\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT2_a254_RPMActual` | page 254 | VCFRONT2 ECU: a254 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT2_a254_RPMTarget` | page 254 | VCFRONT2 ECU: a254 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT2_a283_thmlFanDisabled` | page 283 | VCFRONT2 ECU: a283 thml fan disabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a283_thmlFanLimited` | page 283 | VCFRONT2 ECU: a283 thml fan limited | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a283_thmlFanDemand` | page 283 | VCFRONT2 ECU: a283 thml fan demand | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT2_a283_thmlFanDemandLimit` | page 283 | VCFRONT2 ECU: a283 thml fan demand limit | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT2_a283_thmlFanPhaseI` | page 283 | VCFRONT2 ECU: a283 thml fan phase i | 40\|7 | little-endian | unsigned | 0.25 | 5 | A | 5 to 36.75 |  | plausible |
| `VCFRONT2_a283_thmlFanPhaseILimit` | page 283 | VCFRONT2 ECU: a283 thml fan phase i limit | 48\|7 | little-endian | unsigned | 0.25 | 5 | A | 5 to 36.75 |  | plausible |
| `VCFRONT2_a284_driverState` | page 284 | VCFRONT2 ECU: a284 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a284_driverThermWarn` | page 284 | VCFRONT2 ECU: a284 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_driverThermShutdown` | page 284 | VCFRONT2 ECU: a284 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_undervoltage` | page 284 | VCFRONT2 ECU: a284 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_chargePumpUndervoltage` | page 284 | VCFRONT2 ECU: a284 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilOpenX` | page 284 | VCFRONT2 ECU: a284 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilOpenY` | page 284 | VCFRONT2 ECU: a284 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortXPGnd` | page 284 | VCFRONT2 ECU: a284 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortXPVbb` | page 284 | VCFRONT2 ECU: a284 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortXNGnd` | page 284 | VCFRONT2 ECU: a284 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortXNVbb` | page 284 | VCFRONT2 ECU: a284 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortYPGnd` | page 284 | VCFRONT2 ECU: a284 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortYPVbb` | page 284 | VCFRONT2 ECU: a284 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortYNGnd` | page 284 | VCFRONT2 ECU: a284 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_isCoilShortYNVbb` | page 284 | VCFRONT2 ECU: a284 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_driverHasCommError` | page 284 | VCFRONT2 ECU: a284 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_driverState` | page 285 | VCFRONT2 ECU: a285 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a285_driverThermWarn` | page 285 | VCFRONT2 ECU: a285 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_driverThermShutdown` | page 285 | VCFRONT2 ECU: a285 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_undervoltage` | page 285 | VCFRONT2 ECU: a285 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_chargePumpUndervoltage` | page 285 | VCFRONT2 ECU: a285 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilOpenX` | page 285 | VCFRONT2 ECU: a285 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilOpenY` | page 285 | VCFRONT2 ECU: a285 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortXPGnd` | page 285 | VCFRONT2 ECU: a285 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortXPVbb` | page 285 | VCFRONT2 ECU: a285 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortXNGnd` | page 285 | VCFRONT2 ECU: a285 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortXNVbb` | page 285 | VCFRONT2 ECU: a285 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortYPGnd` | page 285 | VCFRONT2 ECU: a285 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortYPVbb` | page 285 | VCFRONT2 ECU: a285 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortYNGnd` | page 285 | VCFRONT2 ECU: a285 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_isCoilShortYNVbb` | page 285 | VCFRONT2 ECU: a285 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_driverHasCommError` | page 285 | VCFRONT2 ECU: a285 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_driverState` | page 286 | VCFRONT2 ECU: a286 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a286_driverThermWarn` | page 286 | VCFRONT2 ECU: a286 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_driverThermShutdown` | page 286 | VCFRONT2 ECU: a286 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_undervoltage` | page 286 | VCFRONT2 ECU: a286 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_chargePumpUndervoltage` | page 286 | VCFRONT2 ECU: a286 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilOpenX` | page 286 | VCFRONT2 ECU: a286 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilOpenY` | page 286 | VCFRONT2 ECU: a286 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortXPGnd` | page 286 | VCFRONT2 ECU: a286 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortXPVbb` | page 286 | VCFRONT2 ECU: a286 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortXNGnd` | page 286 | VCFRONT2 ECU: a286 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortXNVbb` | page 286 | VCFRONT2 ECU: a286 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortYPGnd` | page 286 | VCFRONT2 ECU: a286 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortYPVbb` | page 286 | VCFRONT2 ECU: a286 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortYNGnd` | page 286 | VCFRONT2 ECU: a286 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_isCoilShortYNVbb` | page 286 | VCFRONT2 ECU: a286 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_driverHasCommError` | page 286 | VCFRONT2 ECU: a286 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_driverState` | page 287 | VCFRONT2 ECU: a287 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a287_driverThermWarn` | page 287 | VCFRONT2 ECU: a287 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_driverThermShutdown` | page 287 | VCFRONT2 ECU: a287 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_undervoltage` | page 287 | VCFRONT2 ECU: a287 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_chargePumpUndervoltage` | page 287 | VCFRONT2 ECU: a287 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilOpenX` | page 287 | VCFRONT2 ECU: a287 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilOpenY` | page 287 | VCFRONT2 ECU: a287 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortXPGnd` | page 287 | VCFRONT2 ECU: a287 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortXPVbb` | page 287 | VCFRONT2 ECU: a287 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortXNGnd` | page 287 | VCFRONT2 ECU: a287 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortXNVbb` | page 287 | VCFRONT2 ECU: a287 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortYPGnd` | page 287 | VCFRONT2 ECU: a287 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortYPVbb` | page 287 | VCFRONT2 ECU: a287 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortYNGnd` | page 287 | VCFRONT2 ECU: a287 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_isCoilShortYNVbb` | page 287 | VCFRONT2 ECU: a287 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_driverHasCommError` | page 287 | VCFRONT2 ECU: a287 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_driverState` | page 288 | VCFRONT2 ECU: a288 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a288_driverThermWarn` | page 288 | VCFRONT2 ECU: a288 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_driverThermShutdown` | page 288 | VCFRONT2 ECU: a288 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_undervoltage` | page 288 | VCFRONT2 ECU: a288 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_chargePumpUndervoltage` | page 288 | VCFRONT2 ECU: a288 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilOpenX` | page 288 | VCFRONT2 ECU: a288 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilOpenY` | page 288 | VCFRONT2 ECU: a288 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortXPGnd` | page 288 | VCFRONT2 ECU: a288 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortXPVbb` | page 288 | VCFRONT2 ECU: a288 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortXNGnd` | page 288 | VCFRONT2 ECU: a288 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortXNVbb` | page 288 | VCFRONT2 ECU: a288 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortYPGnd` | page 288 | VCFRONT2 ECU: a288 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortYPVbb` | page 288 | VCFRONT2 ECU: a288 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortYNGnd` | page 288 | VCFRONT2 ECU: a288 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_isCoilShortYNVbb` | page 288 | VCFRONT2 ECU: a288 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_driverHasCommError` | page 288 | VCFRONT2 ECU: a288 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_driverState` | page 289 | VCFRONT2 ECU: a289 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT2_a289_driverThermWarn` | page 289 | VCFRONT2 ECU: a289 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_driverThermShutdown` | page 289 | VCFRONT2 ECU: a289 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_undervoltage` | page 289 | VCFRONT2 ECU: a289 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_chargePumpUndervoltage` | page 289 | VCFRONT2 ECU: a289 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilOpenX` | page 289 | VCFRONT2 ECU: a289 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilOpenY` | page 289 | VCFRONT2 ECU: a289 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortXPGnd` | page 289 | VCFRONT2 ECU: a289 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortXPVbb` | page 289 | VCFRONT2 ECU: a289 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortXNGnd` | page 289 | VCFRONT2 ECU: a289 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortXNVbb` | page 289 | VCFRONT2 ECU: a289 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortYPGnd` | page 289 | VCFRONT2 ECU: a289 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortYPVbb` | page 289 | VCFRONT2 ECU: a289 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortYNGnd` | page 289 | VCFRONT2 ECU: a289 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_isCoilShortYNVbb` | page 289 | VCFRONT2 ECU: a289 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_driverHasCommError` | page 289 | VCFRONT2 ECU: a289 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a302_LINFrameStatus` | page 302 | VCFRONT2 ECU: a302 LIN frame status | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `OK`<br>2 = `TIMEOUT`<br>3 = `ERROR`<br>4 = `NA` | plausible |
| `VCFRONT2_a355_fluidNotFilled` | page 355 | VCFRONT2 ECU: a355 fluid not filled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a355_systemNotCommissioned` | page 355 | VCFRONT2 ECU: a355 system not commissioned | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a355_serviceLockout` | page 355 | VCFRONT2 ECU: a355 service lockout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a355_factoryGated` | page 355 | VCFRONT2 ECU: a355 factory gated | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_fluidNotFilled` | page 356 | VCFRONT2 ECU: a356 fluid not filled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_systemNotCommissioned` | page 356 | VCFRONT2 ECU: a356 system not commissioned | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_serviceLockout` | page 356 | VCFRONT2 ECU: a356 service lockout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_factoryGated` | page 356 | VCFRONT2 ECU: a356 factory gated | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_refCommissionStatus` | page 356 | VCFRONT2 ECU: a356 ref commission status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a360_vehicleLoadShedActive` | page 360 | VCFRONT2 ECU: a360 vehicle load shed active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a360_notEnoughPowerForSupport` | page 360 | VCFRONT2 ECU: a360 not enough power for support | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a367_bmsSoc` | page 367 | VCFRONT2 ECU: a367 bms soc | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT2_a368_bmsRequestRemoved` | page 368 | VCFRONT2 ECU: a368 bms request removed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_enteringState` | page 368 | VCFRONT2 ECU: a368 entering state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | plausible |
| `VCFRONT2_a368_exitingState` | page 368 | VCFRONT2 ECU: a368 exiting state | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | plausible |
| `VCFRONT2_a368_bmsSoc` | page 368 | VCFRONT2 ECU: a368 bms soc | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT2_a368_systemFaulted` | page 368 | VCFRONT2 ECU: a368 system faulted | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_coolantTempSensorsFaulted` | page 368 | VCFRONT2 ECU: a368 coolant temp sensors faulted | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_coolantValveFaulted` | page 368 | VCFRONT2 ECU: a368 coolant valve faulted | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_louverFaulted` | page 368 | VCFRONT2 ECU: a368 louver faulted | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_fansFaulted` | page 368 | VCFRONT2 ECU: a368 fans faulted | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_coolantNotFilled` | page 368 | VCFRONT2 ECU: a368 coolant not filled | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_coolantPumpsFaulted` | page 368 | VCFRONT2 ECU: a368 coolant pumps faulted | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_preconditionsNotMet` | page 368 | VCFRONT2 ECU: a368 preconditions not met | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_belowSocMin` | page 368 | VCFRONT2 ECU: a368 below soc min | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a369_powerGenerationLimited` | page 369 | VCFRONT2 ECU: a369 power generation limited | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a369_heatRejectionLimited` | page 369 | VCFRONT2 ECU: a369 heat rejection limited | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a369_bmsSoc` | page 369 | VCFRONT2 ECU: a369 bms soc | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT2_a369_wasteHeatPower` | page 369 | VCFRONT2 ECU: a369 waste heat power | 32\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 12700 |  | plausible |
| `VCFRONT2_a374_lccInletSolenoidISense` | page 374 | VCFRONT2 ECU: a374 lcc inlet solenoid i sense | 16\|8 | little-endian | signed | 0.01 | 0 | A | -1.28 to 1.27 |  | plausible |
| `VCFRONT2_a377_wiperStuckOutOfPark` | page 377 | VCFRONT2 ECU: a377 wiper stuck out of park | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a377_wiperStuckInPark` | page 377 | VCFRONT2 ECU: a377 wiper stuck in park | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a397_discharge` | page 397 | VCFRONT2 ECU: a397 discharge | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a397_suction` | page 397 | VCFRONT2 ECU: a397 suction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a397_liquid` | page 397 | VCFRONT2 ECU: a397 liquid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a397_offsetError` | page 397 | VCFRONT2 ECU: a397 offset error | 19\|10 | little-endian | signed | 0.2 | 0 | C | -102.4 to 102.2 |  | plausible |
| `VCFRONT2_a397_runTimeOffSetDetected` | page 397 | VCFRONT2 ECU: a397 run time off set detected | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a409_brushlessMotorConfigurationInvalid` | page 409 | VCFRONT2 ECU: a409 brushless motor configuration invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compFaultRefrigerant` | page 446 | VCFRONT2 ECU: a446 comp fault refrigerant | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compFaultTdHigh` | page 446 | VCFRONT2 ECU: a446 comp fault td high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compFaultPdLow` | page 446 | VCFRONT2 ECU: a446 comp fault pd low | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compFaultPdHigh` | page 446 | VCFRONT2 ECU: a446 comp fault pd high | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compFaultPsLow` | page 446 | VCFRONT2 ECU: a446 comp fault ps low | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyLowAmbient` | page 446 | VCFRONT2 ECU: a446 comp standby low ambient | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyLowDischPress` | page 446 | VCFRONT2 ECU: a446 comp standby low disch press | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyHVNotReady` | page 446 | VCFRONT2 ECU: a446 comp standby HV not ready | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyCommunication` | page 446 | VCFRONT2 ECU: a446 comp standby communication | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbySelfNotReady` | page 446 | VCFRONT2 ECU: a446 comp standby self not ready | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyRefrigNotOk` | page 446 | VCFRONT2 ECU: a446 comp standby refrig not ok | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyCoastDownMode` | page 446 | VCFRONT2 ECU: a446 comp standby coast down mode | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyMultiplePdCutouts` | page 446 | VCFRONT2 ECU: a446 comp standby multiple pd cutouts | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyShowroomMode` | page 446 | VCFRONT2 ECU: a446 comp standby showroom mode | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_compStandbyMultipleTdCutouts` | page 446 | VCFRONT2 ECU: a446 comp standby multiple td cutouts | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_hpCabinLoadType` | page 446 | VCFRONT2 ECU: a446 hp cabin load type | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `CC`<br>2 = `REHEAT`<br>3 = `EVAP` | plausible |
| `VCFRONT2_a446_hpBatteryLoadType` | page 446 | VCFRONT2 ECU: a446 hp battery load type | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `BATT_HEAT`<br>2 = `BATT_COOL` | plausible |
| `VCFRONT2_a446_usingModeledPs` | page 446 | VCFRONT2 ECU: a446 using modeled ps | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_usingModeledPd` | page 446 | VCFRONT2 ECU: a446 using modeled pd | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_usingModeledPl` | page 446 | VCFRONT2 ECU: a446 using modeled pl | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_usingModeledTs` | page 446 | VCFRONT2 ECU: a446 using modeled ts | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_usingModeledTd` | page 446 | VCFRONT2 ECU: a446 using modeled td | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_usingModeledTl` | page 446 | VCFRONT2 ECU: a446 using modeled tl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorHasOffsetTd` | page 446 | VCFRONT2 ECU: a446 sensor has offset td | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorHasOffsetPd` | page 446 | VCFRONT2 ECU: a446 sensor has offset pd | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorDroopPd` | page 446 | VCFRONT2 ECU: a446 sensor droop pd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorHasOffsetTl` | page 446 | VCFRONT2 ECU: a446 sensor has offset tl | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentPs` | page 446 | VCFRONT2 ECU: a446 sensor intermittent ps | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentPd` | page 446 | VCFRONT2 ECU: a446 sensor intermittent pd | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentPl` | page 446 | VCFRONT2 ECU: a446 sensor intermittent pl | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentTs` | page 446 | VCFRONT2 ECU: a446 sensor intermittent ts | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentTd` | page 446 | VCFRONT2 ECU: a446 sensor intermittent td | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_sensorIntermittentTl` | page 446 | VCFRONT2 ECU: a446 sensor intermittent tl | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_highSuctionSuperheat` | page 446 | VCFRONT2 ECU: a446 high suction superheat | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_evapLowPsCutout` | page 446 | VCFRONT2 ECU: a446 evap low ps cutout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_batteryOverTemp` | page 446 | VCFRONT2 ECU: a446 battery over temp | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_hvacSystemFault` | page 446 | VCFRONT2 ECU: a446 hvac system fault | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_coolantSysLockedOut` | page 446 | VCFRONT2 ECU: a446 coolant sys locked out | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_refSysLockedOut` | page 446 | VCFRONT2 ECU: a446 ref sys locked out | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_chillerEXVNotReady` | page 446 | VCFRONT2 ECU: a446 chiller EXV not ready | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_CCLEXVNotReady` | page 446 | VCFRONT2 ECU: a446 CCLEXV not ready | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_CCREXVNotReady` | page 446 | VCFRONT2 ECU: a446 CCREXV not ready | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_LCCEXVNotReady` | page 446 | VCFRONT2 ECU: a446 LCCEXV not ready | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_evapEXVNotReady` | page 446 | VCFRONT2 ECU: a446 evap EXV not ready | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_recircEXVNotReady` | page 446 | VCFRONT2 ECU: a446 recirc EXV not ready | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_checkA447Alert` | page 446 | VCFRONT2 ECU: a446 check A447 alert | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_caseHVACUnavailable` | page 447 | VCFRONT2 ECU: a447 case HVAC unavailable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_heatPumpHVACUnavailable` | page 447 | VCFRONT2 ECU: a447 heat pump HVAC unavailable | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_activeLouverCompromised` | page 447 | VCFRONT2 ECU: a447 active louver compromised | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_coolantValveCompromised` | page 447 | VCFRONT2 ECU: a447 coolant valve compromised | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_ambientSourcingCompromised` | page 447 | VCFRONT2 ECU: a447 ambient sourcing compromised | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_scavengeLoopCompromised` | page 447 | VCFRONT2 ECU: a447 scavenge loop compromised | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_coolantSystemCompromised` | page 447 | VCFRONT2 ECU: a447 coolant system compromised | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_hvBattActiveDischgCompromised` | page 447 | VCFRONT2 ECU: a447 hv batt active dischg compromised | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_hvBatteryDischargingCompromised` | page 447 | VCFRONT2 ECU: a447 hv battery discharging compromised | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_lccSolenoidCompromised` | page 447 | VCFRONT2 ECU: a447 lcc solenoid compromised | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigerantSystemCompromised` | page 447 | VCFRONT2 ECU: a447 refrigerant system compromised | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_powertrainThermalFansCompromised` | page 447 | VCFRONT2 ECU: a447 powertrain thermal fans compromised | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigDischargePressCompromised` | page 447 | VCFRONT2 ECU: a447 refrig discharge press compromised | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigeDischargeTempCompromised` | page 447 | VCFRONT2 ECU: a447 refrige discharge temp compromised | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigSuctionPressCompromised` | page 447 | VCFRONT2 ECU: a447 refrig suction press compromised | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigSuctionTempCompromised` | page 447 | VCFRONT2 ECU: a447 refrig suction temp compromised | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigLiquidPressCompromised` | page 447 | VCFRONT2 ECU: a447 refrig liquid press compromised | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_refrigLiquidTempCompromised` | page 447 | VCFRONT2 ECU: a447 refrig liquid temp compromised | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a459_coolantFillActive` | page 459 | VCFRONT2 ECU: a459 coolant fill active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a459_refrigerantFillActive` | page 459 | VCFRONT2 ECU: a459 refrigerant fill active | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a464_flowIndex` | page 464 | VCFRONT2 ECU: a464 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a464_flowIndexFiltered` | page 464 | VCFRONT2 ECU: a464 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a464_subcool` | page 464 | VCFRONT2 ECU: a464 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a464_subcoolFiltered` | page 464 | VCFRONT2 ECU: a464 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a465_flowIndex` | page 465 | VCFRONT2 ECU: a465 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a465_flowIndexFiltered` | page 465 | VCFRONT2 ECU: a465 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a465_subcool` | page 465 | VCFRONT2 ECU: a465 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a465_subcoolFiltered` | page 465 | VCFRONT2 ECU: a465 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a465_flaggedAtSteadyState` | page 465 | VCFRONT2 ECU: a465 flagged at steady state | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a465_flaggedAtUnsteadyState` | page 465 | VCFRONT2 ECU: a465 flagged at unsteady state | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a466_flowIndex` | page 466 | VCFRONT2 ECU: a466 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a466_flowIndexFiltered` | page 466 | VCFRONT2 ECU: a466 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT2_a466_subcool` | page 466 | VCFRONT2 ECU: a466 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a466_subcoolFiltered` | page 466 | VCFRONT2 ECU: a466 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT2_a467_powerIndexFiltered` | page 467 | VCFRONT2 ECU: a467 power index filtered | 16\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 127 |  | plausible |
| `VCFRONT2_a470_pressureLiquid` | page 470 | VCFRONT2 ECU: a470 pressure liquid | 16\|8 | little-endian | unsigned | 0.2 | 0 | bar | 0 to 51 |  | plausible |
| `VCFRONT2_a470_pressureDischarge` | page 470 | VCFRONT2 ECU: a470 pressure discharge | 24\|8 | little-endian | unsigned | 0.2 | 0 | bar | 0 to 51 |  | plausible |
| `VCFRONT2_a490_coolantPumpType` | page 490 | VCFRONT2 ECU: a490 coolant pump type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DUAL`<br>1 = `SINGLE_PUMP_BATT`<br>2 = `DUAL_SAN_P4`<br>4 = `DUAL_SAN_P4_LUB`<br>5 = `DUAL_MIX` | plausible |
| `VCFRONT2_a511_PCSEFuseCurrent` | page 511 | VCFRONT2 ECU: a511 PCSE fuse current | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT2_a511_DCDCMaxOutputCurrentAllowed` | page 511 | VCFRONT2 ECU: a511 DCDC max output current allowed | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT2_a511_hvState` | page 511 | VCFRONT2 ECU: a511 hv state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT2_a511_DCDCOutputIsLimited` | page 511 | VCFRONT2 ECU: a511 DCDC output is limited | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_PCSSignalsAreValid` | page 511 | VCFRONT2 ECU: a511 PCS signals are valid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_factoryGated` | page 511 | VCFRONT2 ECU: a511 factory gated | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_vehicleIsUpdating` | page 511 | VCFRONT2 ECU: a511 vehicle is updating | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_serviceMode` | page 511 | Signal reported by VCFRONT2 ECU | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_frunkOpen` | page 511 | VCFRONT2 ECU: a511 frunk open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a531_powerIndexFiltered` | page 531 | VCFRONT2 ECU: a531 power index filtered | 16\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 127 |  | plausible |
| `VCFRONT2_a560_highSHCOP1` | page 560 | VCFRONT2 ECU: a560 high SHCOP1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHBattConditioning` | page 560 | VCFRONT2 ECU: a560 high SH batt conditioning | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHCabinReheatCD` | page 560 | VCFRONT2 ECU: a560 high SH cabin reheat CD | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHCabinReheatHD` | page 560 | VCFRONT2 ECU: a560 high SH cabin reheat HD | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHCabinCooling` | page 560 | VCFRONT2 ECU: a560 high SH cabin cooling | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHCabinHeating` | page 560 | VCFRONT2 ECU: a560 high SH cabin heating | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_highSHCatchAll` | page 560 | VCFRONT2 ECU: a560 high SH catch all | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a615_FRONTIPC_switchStatus` | page 615 | VCFRONT2 ECU: a615 FRONTIPC switch status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a616_FRONTIPC_switchStatus` | page 616 | VCFRONT2 ECU: a616 FRONTIPC switch status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a667_hcmRegionAndSide` | page 667 | VCFRONT2 ECU: a667 hcm region and side; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `SAE_LEFT`<br>2 = `SAE_RIGHT`<br>3 = `ECE_LHD_LEFT`<br>4 = `ECE_LHD_RIGHT`<br>5 = `ECE_RHD_LEFT`<br>6 = `ECE_RHD_RIGHT` | plausible |
| `VCFRONT2_a667_country` | page 667 | VCFRONT2 ECU: a667 country | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT2_a667_homologationRegionOverride` | page 667 | VCFRONT2 ECU: a667 homologation region override | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT_FOR_COUNTRY_CODE`<br>1 = `KR_UNECE`<br>2 = `MX_UNECE` | plausible |
| `VCFRONT2_a667_isRightHandDrive` | page 667 | VCFRONT2 ECU: a667 is right hand drive | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a697_isGlobalHeadlamps` | page 697 | VCFRONT2 ECU: a697 is global headlamps | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a697_isVirtualPitchSensor` | page 697 | VCFRONT2 ECU: a697 is virtual pitch sensor | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a697_calibratedVerticalPositionHCML` | page 697 | VCFRONT2 ECU: a697 calibrated vertical position HCML; raw 1023 = signal not available (SNA) | 18\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCFRONT2_a697_calibratedHorizontalPositionHCML` | page 697 | VCFRONT2 ECU: a697 calibrated horizontal position HCML; raw 1023 = signal not available (SNA) | 28\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |

## Multiplexing

`VCFRONT2_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals), page 91 (2 signals), page 96 (1 signals), page 98 (2 signals), page 106 (10 signals), page 108 (4 signals), page 120 (9 signals), page 124 (2 signals), page 125 (3 signals), page 126 (4 signals), page 131 (2 signals), page 133 (2 signals), page 142 (16 signals), page 144 (2 signals), page 150 (2 signals), page 159 (3 signals), page 171 (32 signals), page 172 (2 signals), page 173 (2 signals), page 176 (1 signals), page 186 (1 signals), page 187 (5 signals), page 195 (3 signals), page 210 (3 signals), page 214 (33 signals), page 217 (33 signals), page 235 (1 signals), page 236 (1 signals), page 247 (1 signals), page 249 (2 signals), page 254 (2 signals), page 283 (6 signals), page 284 (16 signals), page 285 (16 signals), page 286 (16 signals), page 287 (16 signals), page 288 (16 signals), page 289 (16 signals), page 302 (1 signals), page 355 (4 signals), page 356 (5 signals), page 360 (2 signals), page 367 (1 signals), page 368 (13 signals), page 369 (4 signals), page 374 (1 signals), page 377 (2 signals), page 397 (5 signals), page 409 (1 signals), page 446 (46 signals), page 447 (18 signals), page 459 (2 signals), page 464 (4 signals), page 465 (6 signals), page 466 (4 signals), page 467 (1 signals), page 470 (2 signals), page 490 (1 signals), page 511 (9 signals), page 531 (1 signals), page 560 (7 signals), page 615 (1 signals), page 616 (1 signals), page 667 (4 signals), page 697 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT2 ECU messages (VCFRONT2)](../../vcfront2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
