---
layout: default
title: "VCBATT2_alertLog (0x54E) — VCBATT2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT2 ECU message: alert log. Tesla Model Y CAN bus message VCBATT2_alertLog (0x54E) of VCBATT2 ECU, firmware 2026.26.6.5, 217 signals (VCBATT2_alertID, VCBATT2_alertState, VCBATT2_a001_InternalWatchdog, VCBATT2_a015_NVMMMemOverflow and 213 more). Bit layout, scaling, units and value tables."
---

# VCBATT2_alertLog (0x54E) — VCBATT2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT2 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 217 signals of VCBATT2_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT2_alertLog` |
| CAN id | 0x54E (1358) |
| ECU | [VCBATT2 ECU](../../vcbatt2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT2 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 217 |

## Signals of VCBATT2_alertLog

Tesla Model Y CAN bus signals in `VCBATT2_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT2_alertID` | selector | VCBATT2 ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>18 = `a018_HardFault`<br>19 = `a019_BusFault`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>28 = `a028_UsageFault`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>36 = `a036_UnknownIrq`<br>37 = `a037_MemManageFault`<br>38 = `a038_ProtFaultInfo`<br>39 = `a039_ProtFaultAddress`<br>40 = `a040_Backtrace`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>77 = `a077_VCBATT0_MIA`<br>78 = `a078_VCBATT1_MIA`<br>79 = `a079_VCBATT2_MIA`<br>80 = `a080_VCFRONT0_MIA`<br>81 = `a081_VCFRONT1_MIA`<br>82 = `a082_VCFRONT2_MIA`<br>86 = `a086_VCBATT_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>96 = `a096_OCS1P_MIA`<br>98 = `a098_DIR_MIA`<br>100 = `a100_CANbus_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>122 = `a122_ICR_MIA`<br>123 = `a123_VC_SECONDARY_LIGHTING_LEADER_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_SCCM_MIA`<br>126 = `a126_EPAS3P_MIA`<br>131 = `a131_PCSCOMMON_MIA`<br>133 = `a133_BRAKE_MIA`<br>143 = `a143_powerLossDuringSleep`<br>144 = `a144_EPAS3S_MIA`<br>156 = `a156_louverBlockage`<br>157 = `a157_louverBreakage`<br>158 = `a158_louverDisconnected`<br>166 = `a166_rightHCMMIA`<br>181 = `a181_homelinkMIA`<br>185 = `a185_washerFluidLow`<br>186 = `a186_washerFluidLowFasciaAndRepeater`<br>187 = `a187_washerFluidLowPassengerWiper`<br>188 = `a188_sleepFailed`<br>192 = `a192_vehicleLoadShed`<br>208 = `a208_brakeFluidLow`<br>209 = `a209_brakeFluidSNA`<br>211 = `a211_I2CFault`<br>227 = `a227_radFanCompromised`<br>241 = `a241_radFanMIA`<br>290 = `a290_leftFogLightFault`<br>291 = `a291_rightFogLightFault`<br>292 = `a292_sideMarkerLightPipeFault`<br>295 = `a295_rightSideRepeaterLightFault`<br>299 = `a299_homelinkConfigurationFailed`<br>300 = `a300_louverActuatorSwapDetected`<br>303 = `a303_frunkAccessPostActive`<br>304 = `a304_frunkReleaseFailed`<br>305 = `a305_frunkPriOverCurrent`<br>306 = `a306_frunkPriUnderCurrent`<br>309 = `a309_frunkEmergencyReleasePressed`<br>353 = `a353_wiperHeaterUndercurrent`<br>354 = `a354_windshieldCameraHeaterUndercurrent`<br>361 = `a361_washerFluidLowMomentary`<br>364 = `a364_heaterTypeEstimationChanged`<br>389 = `a389_frunkInhibitingReleaseAtSpeed`<br>391 = `a391_frunkLatchSwitchFault`<br>399 = `a399_frunkNeverReportedOpen`<br>423 = `a423_rtosSleepFailed`<br>463 = `a463_frunkSensorService`<br>471 = `a471_emergencyFrunkButtonPressIgnored`<br>475 = `a475_rightHeadlampInternalError`<br>485 = `a485_mcuGamingEFuseFault`<br>486 = `a486_sleepPowerDebug`<br>516 = `a516_hibernationActive`<br>517 = `a517_hibernationRecovery`<br>520 = `a520_rightHeadlampInternalErrorV2`<br>522 = `a522_hibernationActiveLogCapture`<br>524 = `a524_rightHeadlampAimingFault`<br>547 = `a547_postCrashLoadShed`<br>548 = `a548_HVFaultLoadShed`<br>557 = `a557_rightHeadlampInternalErrorV3`<br>558 = `a558_rightHeadlampAimingDebug`<br>567 = `a567_rightFrontTurnLightFault`<br>569 = `a569_rightDaytimeRunningLightFault`<br>575 = `a575_frontOilPumpEFuseTrip`<br>578 = `a578_vbattFusedLowCurrentFeedEFuseTrip`<br>583 = `a583_frunkSwitchGroupDisagreementDebug`<br>584 = `a584_frunkSwitchGroupDebug`<br>586 = `a586_rightLowOrHighBeamLightCondition`<br>610 = `a610_frunkOpenFailureMetricSet`<br>617 = `a617_APP_MIA`<br>619 = `a619_frunkSwitchReleaseTimeDBG`<br>624 = `a624_rightHeadlampInternalErrorV4`<br>631 = `a631_rightHeadlampFactoryFault`<br>634 = `a634_indeterminateSwitchTransitionDetectedDbg`<br>643 = `a643_rightHeadlampUartCondition`<br>644 = `a644_washPumpHealthCalculationDbg0`<br>645 = `a645_washPumpHealthCalculationDbg1`<br>646 = `a646_washPumpHealthCalculationDbg2`<br>649 = `a649_persistAccPortPowerReqOverridden`<br>650 = `a650_powerConsumptionInfo`<br>662 = `a662_mculessRightHeadlampCurrentAlertDbg`<br>664 = `a664_rightHeadlampUartWaterMarkWarning`<br>666 = `a666_rightHeadlampRetryInfo`<br>668 = `a668_rightHeadlampRegionOrSideMismatch`<br>698 = `a698_rightHeadlampNotAimed`<br>702 = `a702_dynamicHeadlightLevelingUnavailable` | plausible |
| `VCBATT2_alertState` |  | VCBATT2 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCBATT2_a001_InternalWatchdog` | page 1 | VCBATT2 ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a015_NVMMMemOverflow` | page 15 | VCBATT2 ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a015_NVMMFilesystemError` | page 15 | VCBATT2 ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a015_NVMMRecordIDError` | page 15 | VCBATT2 ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a059_voltageDrop` | page 59 | VCBATT2 ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT2_a059_resistanceEstimate` | page 59 | VCBATT2 ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCBATT2_a059_current` | page 59 | VCBATT2 ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCBATT2_a063_switchChannel` | page 63 | VCBATT2 ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT2_a063_switchType` | page 63 | VCBATT2 ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT2_a063_ADCVoltage` | page 63 | VCBATT2 ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCBATT2_a063_disconnected` | page 63 | VCBATT2 ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a063_indeterminate` | page 63 | VCBATT2 ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a063_stuckActive` | page 63 | VCBATT2 ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a063_faulted` | page 63 | VCBATT2 ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a091_FRONTIPC_faultsAndExtras` | page 91 | VCBATT2 ECU: a091 FRONTIPC faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a091_FRONTIPC_state` | page 91 | VCBATT2 ECU: a091 FRONTIPC state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a096_FRONTIPC_status` | page 96 | VCBATT2 ECU: a096 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a098_FRONTIPC_temperature` | page 98 | VCBATT2 ECU: a098 FRONTIPC temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a098_FRONTIPC_thermalControl` | page 98 | VCBATT2 ECU: a098 FRONTIPC thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_BATTIPC_dcdcRailStatus` | page 106 | VCBATT2 ECU: a106 BATTIPC dcdc rail status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_BATTIPC_dcdcStatus` | page 106 | VCBATT2 ECU: a106 BATTIPC dcdc status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_VEH_dcdcStatus` | page 106 | VCBATT2 ECU: a106 VEH dcdc status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_VEH_thermalControl` | page 106 | VCBATT2 ECU: a106 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_VEH_dcdcRailStatus` | page 106 | VCBATT2 ECU: a106 VEH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_CH_dcdcRailStatus` | page 106 | VCBATT2 ECU: a106 CH dcdc rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_CH_alertMatrix` | page 106 | VCBATT2 ECU: a106 CH alert matrix | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_FRONTIPC_thermalControl` | page 106 | VCBATT2 ECU: a106 FRONTIPC thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_FRONTIPC_dcdcRailStatus` | page 106 | VCBATT2 ECU: a106 FRONTIPC dcdc rail status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_FRONTIPC_dcdcStatus` | page 106 | VCBATT2 ECU: a106 FRONTIPC dcdc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a108_FRONTIPC_status` | page 108 | VCBATT2 ECU: a108 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a108_FRONTIPC_temperature` | page 108 | VCBATT2 ECU: a108 FRONTIPC temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a108_FRONTIPC_thermalControl` | page 108 | VCBATT2 ECU: a108 FRONTIPC thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a108_FRONTIPC_motorStatus` | page 108 | VCBATT2 ECU: a108 FRONTIPC motor status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_BATTIPC_speed` | page 120 | VCBATT2 ECU: a120 BATTIPC speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_speed` | page 120 | VCBATT2 ECU: a120 FRONTIPC speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_systemStatus` | page 120 | VCBATT2 ECU: a120 FRONTIPC system status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_BATTIPC_systemStatus` | page 120 | VCBATT2 ECU: a120 BATTIPC system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_systemPower` | page 120 | VCBATT2 ECU: a120 FRONTIPC system power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_autonomyHealth` | page 120 | VCBATT2 ECU: a120 FRONTIPC autonomy health | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_BATTIPC_chassisControl2` | page 120 | VCBATT2 ECU: a120 BATTIPC chassis control2 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_chassisControl2` | page 120 | VCBATT2 ECU: a120 FRONTIPC chassis control2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_FRONTIPC_odometerStatus` | page 120 | VCBATT2 ECU: a120 FRONTIPC odometer status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a124_FRONTIPC_status` | page 124 | VCBATT2 ECU: a124 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a124_BATTIPC_status` | page 124 | VCBATT2 ECU: a124 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a125_FRONTIPC_leftStalk` | page 125 | VCBATT2 ECU: a125 FRONTIPC left stalk | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a125_FRONTIPC_steerAngle` | page 125 | VCBATT2 ECU: a125 FRONTIPC steer angle | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a125_FRONTIPC_info` | page 125 | VCBATT2 ECU: a125 FRONTIPC info | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a126_FRONTIPC_sysStatus` | page 126 | VCBATT2 ECU: a126 FRONTIPC sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a126_BATTIPC_sysStatus` | page 126 | VCBATT2 ECU: a126 BATTIPC sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a126_FRONTIPC_status` | page 126 | VCBATT2 ECU: a126 FRONTIPC status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a126_BATTIPC_status` | page 126 | VCBATT2 ECU: a126 BATTIPC status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a131_FRONTIPC_power` | page 131 | VCBATT2 ECU: a131 FRONTIPC power | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a131_BATTIPC_power` | page 131 | VCBATT2 ECU: a131 BATTIPC power | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a133_BATTIPC_primaryActuator` | page 133 | VCBATT2 ECU: a133 BATTIPC primary actuator | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a133_FRONTIPC_secondaryActuator` | page 133 | VCBATT2 ECU: a133 FRONTIPC secondary actuator | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a144_FRONTIPC_status` | page 144 | VCBATT2 ECU: a144 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a144_BATTIPC_status` | page 144 | VCBATT2 ECU: a144 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a156_motorCounts` | page 156 | VCBATT2 ECU: a156 motor counts | 16\|11 | little-endian | unsigned | 1 | -100 | ticks | -100 to 1947 |  | plausible |
| `VCBATT2_a157_motorCounts` | page 157 | VCBATT2 ECU: a157 motor counts | 16\|11 | little-endian | unsigned | 1 | -100 | ticks | -100 to 1947 |  | plausible |
| `VCBATT2_a181_vehicleState` | page 181 | VCBATT2 ECU: a181 vehicle state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT2_a188_sleepBypassCurrent` | page 188 | VCBATT2 ECU: a188 sleep bypass current | 16\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 51 |  | plausible |
| `VCBATT2_a188_sleepShutdownStep` | page 188 | VCBATT2 ECU: a188 sleep shutdown step; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FRONTPRIV_ASLEEP`<br>1 = `TURN_OFF_SILENT_WAKE_FEED`<br>2 = `DONE`<br>3 = `SNA` | plausible |
| `VCBATT2_a188_vehiclePowerState` | page 188 | VCBATT2 ECU: a188 vehicle power state | 26\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `LOW_POWER_AWAKE`<br>2 = `CONDITIONING`<br>3 = `ACCESSORY`<br>4 = `ACCESSORY_PLUS`<br>5 = `DRIVE`<br>6 = `OTA`<br>7 = `WAIT_FOR_HIGH_POWER`<br>8 = `TURN_ON_LV`<br>9 = `SYSTEM_CHECKS`<br>10 = `LV_ON`<br>11 = `JUMP_START`<br>12 = `LV_SHUTDOWN`<br>13 = `GO_QUIET`<br>14 = `SLEEP_SHUTDOWN`<br>15 = `LOW_POWER_STANDBY`<br>16 = `RESET` | plausible |
| `VCBATT2_a188_timeNotSleeping` | page 188 | VCBATT2 ECU: a188 time not sleeping | 32\|6 | little-endian | unsigned | 1 | 0 | sec | 0 to 63 |  | plausible |
| `VCBATT2_a188_CANAfterQuiet` | page 188 | VCBATT2 ECU: a188 CAN after quiet | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_vehiclePowerState` | page 192 | VCBATT2 ECU: a192 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT2_a192_hvState` | page 192 | VCBATT2 ECU: a192 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT2_a192_notEnoughPowerForSupport` | page 192 | VCBATT2 ECU: a192 not enough power for support | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_pcsEFuseStable` | page 192 | VCBATT2 ECU: a192 pcs e fuse stable | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_vcrightEFuseStable` | page 192 | VCBATT2 ECU: a192 vcright e fuse stable | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_contactorEFuseStable` | page 192 | VCBATT2 ECU: a192 contactor e fuse stable | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_hvcEFuseStable` | page 192 | VCBATT2 ECU: a192 hvc e fuse stable | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_replaceLVBattery` | page 192 | VCBATT2 ECU: a192 replace LV battery | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_BMS_MIA` | page 192 | VCBATT2 ECU: a192 BMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_PCS_MIA` | page 192 | VCBATT2 ECU: a192 PCS MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_HVBlockingMismatch` | page 192 | VCBATT2 ECU: a192 HV blocking mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_disconnected12V` | page 192 | VCBATT2 ECU: a192 disconnected12 v | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_LVBatteryCannotSupportVehicle` | page 192 | VCBATT2 ECU: a192 LV battery cannot support vehicle | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_DI_gear` | page 192 | VCBATT2 ECU: a192 DI gear; raw 7 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCBATT2_a192_GTW_factoryGated` | page 192 | VCBATT2 ECU: a192 GTW factory gated | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_GTW_updateStarted` | page 192 | VCBATT2 ECU: a192 GTW update started | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_serviceMode` | page 192 | Signal reported by VCBATT2 ECU | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_frunkOpen` | page 192 | VCBATT2 ECU: a192 frunk open | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_IBSCurrent` | page 192 | VCBATT2 ECU: a192 IBS current | 40\|8 | little-endian | unsigned | 0.5 | -63 | A | -63 to 64.5 |  | plausible |
| `VCBATT2_a192_PCSCurrent` | page 192 | VCBATT2 ECU: a192 PCS current | 48\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCBATT2_a192_HVFaultLoadShedActive` | page 192 | VCBATT2 ECU: a192 HV fault load shed active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_postCrashLoadShedActive` | page 192 | VCBATT2 ECU: a192 post crash load shed active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorFaulted` | page 227 | VCBATT2 ECU: a227 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorLocked` | page 227 | VCBATT2 ECU: a227 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_ecuReset` | page 227 | VCBATT2 ECU: a227 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_fetTempIrrational` | page 227 | VCBATT2 ECU: a227 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorControlError` | page 227 | VCBATT2 ECU: a227 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_underVoltage` | page 227 | VCBATT2 ECU: a227 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_overVoltage` | page 227 | VCBATT2 ECU: a227 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_hardwareOvercurrent` | page 227 | VCBATT2 ECU: a227 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorOpenPhase` | page 227 | VCBATT2 ECU: a227 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorSoftOpenPhase` | page 227 | VCBATT2 ECU: a227 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorOvertemp` | page 227 | VCBATT2 ECU: a227 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_dcOvercurrent` | page 227 | VCBATT2 ECU: a227 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorStalled` | page 227 | VCBATT2 ECU: a227 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_selfTestFailed` | page 227 | VCBATT2 ECU: a227 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_selfTestResult` | page 227 | VCBATT2 ECU: a227 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCBATT2_a227_linChecksumError` | page 227 | VCBATT2 ECU: a227 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_linFramingError` | page 227 | VCBATT2 ECU: a227 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_phaseShorted` | page 227 | VCBATT2 ECU: a227 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_busVoltageIrrational` | page 227 | VCBATT2 ECU: a227 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_dcCurrentIrrational` | page 227 | VCBATT2 ECU: a227 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorSpeedIrrational` | page 227 | VCBATT2 ECU: a227 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_supplyVoltageIrrational` | page 227 | VCBATT2 ECU: a227 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorPhaseCurrentIrrational` | page 227 | VCBATT2 ECU: a227 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_chipOvertemp` | page 227 | VCBATT2 ECU: a227 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_motorSpeedTooHigh` | page 227 | VCBATT2 ECU: a227 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_phaseOvercurrent` | page 227 | VCBATT2 ECU: a227 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_vddaOvercurrent` | page 227 | VCBATT2 ECU: a227 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_busVoltageUnhealthy` | page 227 | VCBATT2 ECU: a227 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_hsVdsOvervoltage` | page 227 | VCBATT2 ECU: a227 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_hsVdsOvervoltageMask` | page 227 | VCBATT2 ECU: a227 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCBATT2_a227_lsVdsOvervoltage` | page 227 | VCBATT2 ECU: a227 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_lsVdsOvervoltageMask` | page 227 | VCBATT2 ECU: a227 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCBATT2_a227_payloadBitsNotSet` | page 227 | VCBATT2 ECU: a227 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a300_oldType` | page 300 | VCBATT2 ECU: a300 old type | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMDM`<br>1 = `KEBODA`<br>3 = `UNKOWN` | plausible |
| `VCBATT2_a300_newType` | page 300 | VCBATT2 ECU: a300 new type | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMDM`<br>1 = `KEBODA`<br>3 = `UNKOWN` | plausible |
| `VCBATT2_a303_vehicleSpeed` | page 303 | VCBATT2 ECU: a303 vehicle speed | 16\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCBATT2_a303_postVoltage` | page 303 | VCBATT2 ECU: a303 post voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT2_a303_lockStatus` | page 303 | VCBATT2 ECU: a303 lock status; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `UNLOCKED`<br>2 = `LOCKED` | plausible |
| `VCBATT2_a304_voltage` | page 304 | VCBATT2 ECU: a304 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCBATT2_a304_temperature` | page 304 | VCBATT2 ECU: a304 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCBATT2_a305_voltage` | page 305 | VCBATT2 ECU: a305 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCBATT2_a305_temperature` | page 305 | VCBATT2 ECU: a305 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCBATT2_a305_actuatorCurrent` | page 305 | VCBATT2 ECU: a305 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCBATT2_a306_voltage` | page 306 | VCBATT2 ECU: a306 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCBATT2_a306_temperature` | page 306 | VCBATT2 ECU: a306 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCBATT2_a306_actuatorCurrent` | page 306 | VCBATT2 ECU: a306 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCBATT2_a309_vehicleSpeed` | page 309 | VCBATT2 ECU: a309 vehicle speed | 16\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCBATT2_a309_switchVoltage` | page 309 | VCBATT2 ECU: a309 switch voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT2_a309_lockStatus` | page 309 | VCBATT2 ECU: a309 lock status; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `UNLOCKED`<br>2 = `LOCKED` | plausible |
| `VCBATT2_a353_wiperHeaterCurrent` | page 353 | VCBATT2 ECU: a353 wiper heater current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCBATT2_a353_batteryVoltage` | page 353 | VCBATT2 ECU: a353 battery voltage | 24\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCBATT2_a353_ambientTemperature` | page 353 | VCBATT2 ECU: a353 ambient temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCBATT2_a354_windshieldCameraHeaterCurrent` | page 354 | VCBATT2 ECU: a354 windshield camera heater current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCBATT2_a354_batteryVoltage` | page 354 | VCBATT2 ECU: a354 battery voltage | 24\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCBATT2_a354_ambientTemperature` | page 354 | VCBATT2 ECU: a354 ambient temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCBATT2_a389_closedAtSpeed` | page 389 | VCBATT2 ECU: a389 closed at speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a389_faultedWhileOpenAtSpeed` | page 389 | VCBATT2 ECU: a389 faulted while open at speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a389_possiblyStuckClosed` | page 389 | VCBATT2 ECU: a389 possibly stuck closed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a389_vehicleSpeed` | page 389 | VCBATT2 ECU: a389 vehicle speed | 19\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCBATT2_a389_temperature` | page 389 | VCBATT2 ECU: a389 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCBATT2_a389_latchStatus` | page 389 | VCBATT2 ECU: a389 latch status; raw 0 = signal not available (SNA) | 40\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCBATT2_a391_switchMismatch` | page 391 | VCBATT2 ECU: a391 switch mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_switch1Shorted` | page 391 | VCBATT2 ECU: a391 switch1 shorted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_switch1Disconnected` | page 391 | VCBATT2 ECU: a391 switch1 disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_switch2Shorted` | page 391 | VCBATT2 ECU: a391 switch2 shorted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_switch2Disconnected` | page 391 | VCBATT2 ECU: a391 switch2 disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_switch1VoltageAverage` | page 391 | VCBATT2 ECU: a391 switch1 voltage average | 21\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a391_switch1VoltageInstant` | page 391 | VCBATT2 ECU: a391 switch1 voltage instant | 32\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a391_switch2VoltageAverage` | page 391 | VCBATT2 ECU: a391 switch2 voltage average | 42\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a391_switch2VoltageInstant` | page 391 | VCBATT2 ECU: a391 switch2 voltage instant | 52\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a463_switchMismatch` | page 463 | VCBATT2 ECU: a463 switch mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_switch1Shorted` | page 463 | VCBATT2 ECU: a463 switch1 shorted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_switch1Disconnected` | page 463 | VCBATT2 ECU: a463 switch1 disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_switch2Shorted` | page 463 | VCBATT2 ECU: a463 switch2 shorted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_switch2Disconnected` | page 463 | VCBATT2 ECU: a463 switch2 disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_switch1VoltageAverage` | page 463 | VCBATT2 ECU: a463 switch1 voltage average | 21\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a463_switch1VoltageInstant` | page 463 | VCBATT2 ECU: a463 switch1 voltage instant | 32\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a463_switch2VoltageAverage` | page 463 | VCBATT2 ECU: a463 switch2 voltage average | 42\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a463_switch2VoltageInstant` | page 463 | VCBATT2 ECU: a463 switch2 voltage instant | 52\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCBATT2_a485_mcuGamingEFuseCurrent` | page 485 | VCBATT2 ECU: a485 mcu gaming e fuse current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCBATT2_a516_IBSVoltage` | page 516 | VCBATT2 ECU: a516 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT2_a516_HVSoc` | page 516 | VCBATT2 ECU: a516 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCBATT2_a516_contactorsPermanentlyClosed` | page 516 | VCBATT2 ECU: a516 contactors permanently closed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a516_LVBatteryDisconnected` | page 516 | VCBATT2 ECU: a516 LV battery disconnected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a516_reverseBatteryFault` | page 516 | VCBATT2 ECU: a516 reverse battery fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a516_LVBatteryCannotSupportVehicle` | page 516 | VCBATT2 ECU: a516 LV battery cannot support vehicle | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a517_IBSVoltage` | page 517 | VCBATT2 ECU: a517 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT2_a517_HVSoc` | page 517 | VCBATT2 ECU: a517 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCBATT2_a522_IBSVoltage` | page 522 | VCBATT2 ECU: a522 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT2_a522_HVSoc` | page 522 | VCBATT2 ECU: a522 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCBATT2_a522_contactorsPermanentlyClosed` | page 522 | VCBATT2 ECU: a522 contactors permanently closed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a522_LVBatteryDisconnected` | page 522 | VCBATT2 ECU: a522 LV battery disconnected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a522_reverseBatteryFault` | page 522 | VCBATT2 ECU: a522 reverse battery fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a522_LVBatteryCannotSupportVehicle` | page 522 | VCBATT2 ECU: a522 LV battery cannot support vehicle | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a547_serviceMode` | page 547 | Signal reported by VCBATT2 ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a547_frunkOpen` | page 547 | VCBATT2 ECU: a547 frunk open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_vehiclePowerState` | page 548 | VCBATT2 ECU: a548 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT2_a548_notEnoughPowerForSupport` | page 548 | VCBATT2 ECU: a548 not enough power for support | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_HVBlockingMismatch` | page 548 | VCBATT2 ECU: a548 HV blocking mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_LVBatteryCannotSupportVehicle` | page 548 | VCBATT2 ECU: a548 LV battery cannot support vehicle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_DI_gear` | page 548 | VCBATT2 ECU: a548 DI gear; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCBATT2_a548_backstopBucketCount` | page 548 | VCBATT2 ECU: a548 backstop bucket count | 24\|5 | little-endian | unsigned | 0.035 | 0 | Ah | 0 to 1.085 |  | plausible |
| `VCBATT2_a548_hvState` | page 548 | VCBATT2 ECU: a548 hv state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT2_a548_BMS_MIA` | page 548 | VCBATT2 ECU: a548 BMS MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_PCS_MIA` | page 548 | VCBATT2 ECU: a548 PCS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_ampHourBucketCount` | page 548 | VCBATT2 ECU: a548 amp hour bucket count | 34\|6 | little-endian | unsigned | 0.01 | 0 | Ah | 0 to 0.63 |  | plausible |
| `VCBATT2_a548_LVBMSSOC` | page 548 | VCBATT2 ECU: a548 LVBMSSOC | 40\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCBATT2_a548_serviceMode` | page 548 | Signal reported by VCBATT2 ECU | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_frunkOpen` | page 548 | VCBATT2 ECU: a548 frunk open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_PCSTargetVoltage` | page 548 | VCBATT2 ECU: a548 PCS target voltage | 48\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT2_a548_ampHourBucketFilled` | page 548 | VCBATT2 ECU: a548 amp hour bucket filled | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_HVNotConfirmedUpTrigger` | page 548 | VCBATT2 ECU: a548 HV not confirmed up trigger | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_PCSNotMeetingTargetTrigger` | page 548 | VCBATT2 ECU: a548 PCS not meeting target trigger | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_PCSMIATrigger` | page 548 | VCBATT2 ECU: a548 PCSMIA trigger | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_PCSSaturatedTrigger` | page 548 | VCBATT2 ECU: a548 PCS saturated trigger | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_backstopHit` | page 548 | VCBATT2 ECU: a548 backstop hit | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a610_switch1State` | page 610 | VCBATT2 ECU: a610 switch1 state; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCBATT2_a610_switch2State` | page 610 | VCBATT2 ECU: a610 switch2 state; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCBATT2_a610_dataBufferBits` | page 610 | VCBATT2 ECU: a610 data buffer bits | 20\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `VCBATT2_a610_temperature` | page 610 | VCBATT2 ECU: a610 temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCBATT2_a668_hcmRegionAndSide` | page 668 | VCBATT2 ECU: a668 hcm region and side; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `SAE_LEFT`<br>2 = `SAE_RIGHT`<br>3 = `ECE_LHD_LEFT`<br>4 = `ECE_LHD_RIGHT`<br>5 = `ECE_RHD_LEFT`<br>6 = `ECE_RHD_RIGHT` | plausible |
| `VCBATT2_a668_country` | page 668 | VCBATT2 ECU: a668 country | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT2_a668_homologationRegionOverride` | page 668 | VCBATT2 ECU: a668 homologation region override | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT_FOR_COUNTRY_CODE`<br>1 = `KR_UNECE`<br>2 = `MX_UNECE` | plausible |
| `VCBATT2_a668_isRightHandDrive` | page 668 | VCBATT2 ECU: a668 is right hand drive | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a698_isGlobalHeadlamps` | page 698 | VCBATT2 ECU: a698 is global headlamps | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a698_isVirtualPitchSensor` | page 698 | VCBATT2 ECU: a698 is virtual pitch sensor | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a698_calibratedVerticalPositionHCMR` | page 698 | VCBATT2 ECU: a698 calibrated vertical position HCMR; raw 1023 = signal not available (SNA) | 18\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCBATT2_a698_calibratedHorizontalPositionHCMR` | page 698 | VCBATT2 ECU: a698 calibrated horizontal position HCMR; raw 1023 = signal not available (SNA) | 28\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |

## Multiplexing

`VCBATT2_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals), page 91 (2 signals), page 96 (1 signals), page 98 (2 signals), page 106 (10 signals), page 108 (4 signals), page 120 (9 signals), page 124 (2 signals), page 125 (3 signals), page 126 (4 signals), page 131 (2 signals), page 133 (2 signals), page 144 (2 signals), page 156 (1 signals), page 157 (1 signals), page 181 (1 signals), page 188 (5 signals), page 192 (22 signals), page 227 (33 signals), page 300 (2 signals), page 303 (3 signals), page 304 (2 signals), page 305 (3 signals), page 306 (3 signals), page 309 (3 signals), page 353 (3 signals), page 354 (3 signals), page 389 (6 signals), page 391 (9 signals), page 463 (9 signals), page 485 (1 signals), page 516 (6 signals), page 517 (2 signals), page 522 (6 signals), page 547 (2 signals), page 548 (20 signals), page 610 (4 signals), page 668 (4 signals), page 698 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT2 ECU messages (VCBATT2)](../../vcbatt2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
