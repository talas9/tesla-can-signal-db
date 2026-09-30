---
layout: default
title: "VCFRONT1_alertLog (0x537) — VCFRONT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCFRONT1 ECU message: alert log. Tesla Model 3 / Model Y CAN bus message VCFRONT1_alertLog (0x537) of VCFRONT1 ECU, firmware 2026.26.6.5, 272 signals (VCFRONT1_alertID, VCFRONT1_alertState, VCFRONT1_a001_InternalWatchdog, VCFRONT1_a015_NVMMMemOverflow and 268 more). Bit layout, scaling, units and value tables."
---

# VCFRONT1_alertLog (0x537) — VCFRONT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCFRONT1 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 272 signals of VCFRONT1_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT1_alertLog` |
| CAN id | 0x537 (1335) |
| ECU | [VCFRONT1 ECU](../../vcfront1.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT1 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 272 |

## Signals of VCFRONT1_alertLog

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT1_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT1_alertID` | selector | VCFRONT1 ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>18 = `a018_HardFault`<br>19 = `a019_BusFault`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>28 = `a028_UsageFault`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>36 = `a036_UnknownIrq`<br>37 = `a037_MemManageFault`<br>38 = `a038_ProtFaultInfo`<br>39 = `a039_ProtFaultAddress`<br>40 = `a040_Backtrace`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>77 = `a077_VCBATT0_MIA`<br>78 = `a078_VCBATT1_MIA`<br>79 = `a079_VCBATT2_MIA`<br>80 = `a080_VCFRONT0_MIA`<br>81 = `a081_VCFRONT1_MIA`<br>82 = `a082_VCFRONT2_MIA`<br>86 = `a086_VCBATT_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>96 = `a096_OCS1P_MIA`<br>98 = `a098_DIR_MIA`<br>100 = `a100_CANbus_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>122 = `a122_ICR_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_SCCM_MIA`<br>126 = `a126_EPAS3P_MIA`<br>127 = `a127_iBoosterEFuseTrip`<br>128 = `a128_vcrightEFuseTrip`<br>129 = `a129_pcsEFuseTrip`<br>130 = `a130_autopilot2EFuseTrip`<br>131 = `a131_PCSCOMMON_MIA`<br>132 = `a132_epas2EFuseTrip`<br>133 = `a133_BRAKE_MIA`<br>134 = `a134_hvContactorsEFuseTrip`<br>135 = `a135_leftHeadlightEFuseTrip`<br>144 = `a144_EPAS3S_MIA`<br>164 = `a164_eFuseLckoutMissing`<br>165 = `a165_unxpctdEFuseLckout`<br>177 = `a177_mcuAudioEFuseTrip`<br>188 = `a188_sleepFailed`<br>191 = `a191_exitDriveDomainDown`<br>204 = `a204_undervoltageLoadshedTriggered`<br>205 = `a205_overvoltageProtectionTriggered`<br>214 = `a214_openCircuitDetected`<br>216 = `a216_powerCutoffImminent`<br>220 = `a220_LVUnhealthy`<br>223 = `a223_bridgeOvervoltageSelfTestFailure`<br>229 = `a229_LVHealthCompromised`<br>230 = `a230_autopilot2EFuseTripDuringOTA`<br>249 = `a249_pcsOvClampTripped`<br>250 = `a250_pcsOvShutdownTripped`<br>251 = `a251_pcsOvShutdownSelfTestFailure`<br>252 = `a252_pcsOvShutdownSelfTestStageFailure`<br>253 = `a253_pcsOvShutdownHighSideSelfTestDebug`<br>256 = `a256_nxppca9539Fault`<br>262 = `a262_vcrightVoltageMismatch`<br>263 = `a263_pcsVoltageMismatch`<br>264 = `a264_iBoosterVoltageMismatch`<br>266 = `a266_EPAS2VoltageMismatch`<br>414 = `a414_undervoltageSelfTestFailure`<br>415 = `a415_undervoltageSelfTestStuckOff`<br>423 = `a423_rtosSleepFailed`<br>450 = `a450_doorWakeToOpenDBG`<br>475 = `a475_vnf1248Fault`<br>480 = `a480_vnf1048Fault`<br>482 = `a482_lvBridgeEFuseTrip`<br>483 = `a483_vnf1048SelfTestFailure`<br>484 = `a484_undervoltageSelfTestStuckOn`<br>485 = `a485_uvSelfTestLoadUnattemptedOnDbg`<br>486 = `a486_undervoltageSelfTestBridgeSyncFailure`<br>489 = `a489_vnf1248SelfTestDebug`<br>490 = `a490_vnf1248SelfTestFailure`<br>491 = `a491_vnf1248ConfigurationMismatch`<br>496 = `a496_exitDriveWarningDomainDown`<br>500 = `a500_eFuseASICStateMismatch`<br>501 = `a501_vnf1048ConfigurationMismatch`<br>509 = `a509_eFuseASICManagerStateMismatch`<br>523 = `a523_eFuseThresholdsIncorrect`<br>574 = `a574_frontDriveInverterEFuseTrip`<br>575 = `a575_frontDriveInverterEFuseTripDBG`<br>578 = `a578_vbusFusedLoadShedEFuseTrip`<br>581 = `a581_harnessResistanceInfo`<br>590 = `a590_vcrightPwrRationalityCurve`<br>591 = `a591_vcrightFastBlowDetection`<br>596 = `a596_vcrightCurvePowerCutoff`<br>597 = `a597_vcrightFastBlowPowerCutoff`<br>617 = `a617_APP_MIA` | plausible |
| `VCFRONT1_alertState` |  | VCFRONT1 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCFRONT1_a001_InternalWatchdog` | page 1 | VCFRONT1 ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a015_NVMMMemOverflow` | page 15 | VCFRONT1 ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a015_NVMMFilesystemError` | page 15 | VCFRONT1 ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a015_NVMMRecordIDError` | page 15 | VCFRONT1 ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a059_voltageDrop` | page 59 | VCFRONT1 ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT1_a059_resistanceEstimate` | page 59 | VCFRONT1 ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCFRONT1_a059_current` | page 59 | VCFRONT1 ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCFRONT1_a063_switchChannel` | page 63 | VCFRONT1 ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a063_switchType` | page 63 | VCFRONT1 ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a063_ADCVoltage` | page 63 | VCFRONT1 ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCFRONT1_a063_disconnected` | page 63 | VCFRONT1 ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a063_indeterminate` | page 63 | VCFRONT1 ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a063_stuckActive` | page 63 | VCFRONT1 ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a063_faulted` | page 63 | VCFRONT1 ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a091_FRONTIPC_faultsAndExtras` | page 91 | VCFRONT1 ECU: a091 FRONTIPC faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a091_FRONTIPC_state` | page 91 | VCFRONT1 ECU: a091 FRONTIPC state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a096_FRONTIPC_status` | page 96 | VCFRONT1 ECU: a096 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a098_FRONTIPC_temperature` | page 98 | VCFRONT1 ECU: a098 FRONTIPC temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a098_FRONTIPC_thermalControl` | page 98 | VCFRONT1 ECU: a098 FRONTIPC thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_BATTIPC_dcdcRailStatus` | page 106 | VCFRONT1 ECU: a106 BATTIPC dcdc rail status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_BATTIPC_dcdcStatus` | page 106 | VCFRONT1 ECU: a106 BATTIPC dcdc status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_VEH_dcdcStatus` | page 106 | VCFRONT1 ECU: a106 VEH dcdc status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_VEH_thermalControl` | page 106 | VCFRONT1 ECU: a106 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_VEH_dcdcRailStatus` | page 106 | VCFRONT1 ECU: a106 VEH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_CH_dcdcRailStatus` | page 106 | VCFRONT1 ECU: a106 CH dcdc rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_CH_alertMatrix` | page 106 | VCFRONT1 ECU: a106 CH alert matrix | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_FRONTIPC_thermalControl` | page 106 | VCFRONT1 ECU: a106 FRONTIPC thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_FRONTIPC_dcdcRailStatus` | page 106 | VCFRONT1 ECU: a106 FRONTIPC dcdc rail status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_FRONTIPC_dcdcStatus` | page 106 | VCFRONT1 ECU: a106 FRONTIPC dcdc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a108_FRONTIPC_status` | page 108 | VCFRONT1 ECU: a108 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a108_FRONTIPC_temperature` | page 108 | VCFRONT1 ECU: a108 FRONTIPC temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a108_FRONTIPC_thermalControl` | page 108 | VCFRONT1 ECU: a108 FRONTIPC thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a108_FRONTIPC_motorStatus` | page 108 | VCFRONT1 ECU: a108 FRONTIPC motor status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_BATTIPC_speed` | page 120 | VCFRONT1 ECU: a120 BATTIPC speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_speed` | page 120 | VCFRONT1 ECU: a120 FRONTIPC speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_systemStatus` | page 120 | VCFRONT1 ECU: a120 FRONTIPC system status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_BATTIPC_systemStatus` | page 120 | VCFRONT1 ECU: a120 BATTIPC system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_systemPower` | page 120 | VCFRONT1 ECU: a120 FRONTIPC system power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_autonomyHealth` | page 120 | VCFRONT1 ECU: a120 FRONTIPC autonomy health | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_BATTIPC_chassisControl2` | page 120 | VCFRONT1 ECU: a120 BATTIPC chassis control2 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_chassisControl2` | page 120 | VCFRONT1 ECU: a120 FRONTIPC chassis control2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_FRONTIPC_odometerStatus` | page 120 | VCFRONT1 ECU: a120 FRONTIPC odometer status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a124_FRONTIPC_status` | page 124 | VCFRONT1 ECU: a124 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a124_BATTIPC_status` | page 124 | VCFRONT1 ECU: a124 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a125_FRONTIPC_leftStalk` | page 125 | VCFRONT1 ECU: a125 FRONTIPC left stalk | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a125_FRONTIPC_steerAngle` | page 125 | VCFRONT1 ECU: a125 FRONTIPC steer angle | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a125_FRONTIPC_info` | page 125 | VCFRONT1 ECU: a125 FRONTIPC info | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a126_FRONTIPC_sysStatus` | page 126 | VCFRONT1 ECU: a126 FRONTIPC sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a126_BATTIPC_sysStatus` | page 126 | VCFRONT1 ECU: a126 BATTIPC sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a126_FRONTIPC_status` | page 126 | VCFRONT1 ECU: a126 FRONTIPC status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a126_BATTIPC_status` | page 126 | VCFRONT1 ECU: a126 BATTIPC status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a127_iBoosterEFuseCurrent` | page 127 | VCFRONT1 ECU: a127 i booster e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a127_iBoosterEFuseVoltage` | page 127 | VCFRONT1 ECU: a127 i booster e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a127_iBoosterEFuseTemp` | page 127 | VCFRONT1 ECU: a127 i booster e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a128_vcrightEFuseCurrent` | page 128 | VCFRONT1 ECU: a128 vcright e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a128_vcrightEFuseVoltage` | page 128 | VCFRONT1 ECU: a128 vcright e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a128_vcrightEFuseTemp` | page 128 | VCFRONT1 ECU: a128 vcright e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a128_vcrightEFuseRemainingRetries` | page 128 | VCFRONT1 ECU: a128 vcright e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT1_a129_pcsEFuseCurrent` | page 129 | VCFRONT1 ECU: a129 pcs e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a129_pcsEFuseVoltage` | page 129 | VCFRONT1 ECU: a129 pcs e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a129_pcsEFuseTemp` | page 129 | VCFRONT1 ECU: a129 pcs e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a129_pcsEFuseRemainingRetries` | page 129 | VCFRONT1 ECU: a129 pcs e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT1_a130_autopilot2EFuseCurrent` | page 130 | VCFRONT1 ECU: a130 autopilot2 e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a130_autopilot2EFuseVoltage` | page 130 | VCFRONT1 ECU: a130 autopilot2 e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a130_autopilot2EFuseTemp` | page 130 | VCFRONT1 ECU: a130 autopilot2 e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a130_autopilot2EFuseRemainingRetries` | page 130 | VCFRONT1 ECU: a130 autopilot2 e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT1_a131_FRONTIPC_power` | page 131 | VCFRONT1 ECU: a131 FRONTIPC power | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a131_BATTIPC_power` | page 131 | VCFRONT1 ECU: a131 BATTIPC power | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a132_epas2EFuseCurrent` | page 132 | VCFRONT1 ECU: a132 epas2 e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a132_epas2EFuseVoltage` | page 132 | VCFRONT1 ECU: a132 epas2 e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a132_epas2EFuseTemp` | page 132 | VCFRONT1 ECU: a132 epas2 e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a133_BATTIPC_primaryActuator` | page 133 | VCFRONT1 ECU: a133 BATTIPC primary actuator | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a133_FRONTIPC_secondaryActuator` | page 133 | VCFRONT1 ECU: a133 FRONTIPC secondary actuator | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a135_leftHeadlightEFuseCurrent` | page 135 | VCFRONT1 ECU: a135 left headlight e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a144_FRONTIPC_status` | page 144 | VCFRONT1 ECU: a144 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a144_BATTIPC_status` | page 144 | VCFRONT1 ECU: a144 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a164_lockoutVoltage` | page 164 | VCFRONT1 ECU: a164 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a165_lockoutVoltage` | page 165 | VCFRONT1 ECU: a165 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a177_mcuAudioEFuseCurrent` | page 177 | VCFRONT1 ECU: a177 mcu audio e fuse current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT1_a177_mcuAudioEFuseVoltage` | page 177 | VCFRONT1 ECU: a177 mcu audio e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a191_vehiclePowerState` | page 191 | VCFRONT1 ECU: a191 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT1_a191_hvState` | page 191 | VCFRONT1 ECU: a191 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT1_a191_busVoltage` | page 191 | VCFRONT1 ECU: a191 bus voltage | 24\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCFRONT1_a191_serviceMode` | page 191 | Signal reported by VCFRONT1 ECU | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a191_frunkOpen` | page 191 | VCFRONT1 ECU: a191 frunk open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a191_exitDriveWarningTimerExpired` | page 191 | VCFRONT1 ECU: a191 exit drive warning timer expired | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a191_NotEnoughPowerForSupport` | page 191 | VCFRONT1 ECU: a191 not enough power for support | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a191_bmsState` | page 191 | VCFRONT1 ECU: a191 bms state; raw 9 = signal not available (SNA) | 36\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT1_a204_vbusVoltage` | page 204 | VCFRONT1 ECU: a204 vbus voltage | 16\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a204_BRailLocked` | page 204 | VCFRONT1 ECU: a204 b rail locked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a204_uvLoadshedFaultInject` | page 204 | VCFRONT1 ECU: a204 uv loadshed fault inject | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a204_pcsBridgeCurrent` | page 204 | VCFRONT1 ECU: a204 pcs bridge current | 32\|16 | little-endian | signed | 0.0625 | 0 | A | -2048 to 2047.9375 |  | plausible |
| `VCFRONT1_a205_busVoltage` | page 205 | VCFRONT1 ECU: a205 bus voltage | 16\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a205_BRailLocked` | page 205 | VCFRONT1 ECU: a205 b rail locked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a205_ovLoadshedFaultInject` | page 205 | VCFRONT1 ECU: a205 ov loadshed fault inject | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a205_pcsBridgeCurrent` | page 205 | VCFRONT1 ECU: a205 pcs bridge current | 32\|16 | little-endian | signed | 0.0625 | 0 | A | -2048 to 2047.9375 |  | plausible |
| `VCFRONT1_a216_inDrive` | page 216 | VCFRONT1 ECU: a216 in drive | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a216_hvState` | page 216 | VCFRONT1 ECU: a216 hv state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT1_a216_vcrightFastBlowImminent` | page 216 | VCFRONT1 ECU: a216 vcright fast blow imminent | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a216_vcrightFastBlowDebounceImminent` | page 216 | VCFRONT1 ECU: a216 vcright fast blow debounce imminent | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a216_vcrightStaticImminent` | page 216 | VCFRONT1 ECU: a216 vcright static imminent | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a216_vcrightDynamicImminent` | page 216 | VCFRONT1 ECU: a216 vcright dynamic imminent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a220_DI_gear` | page 220 | VCFRONT1 ECU: a220 DI gear; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCFRONT1_a220_redundancyRequired` | page 220 | VCFRONT1 ECU: a220 redundancy required | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a220_vehicleSpeed` | page 220 | VCFRONT1 ECU: a220 vehicle speed | 20\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT1_a220_lvHealthStatus` | page 220 | VCFRONT1 ECU: a220 lv health status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOMAIN_HEALTHY`<br>1 = `HEALTHY_LIMITED`<br>2 = `LATENT_FAULT`<br>3 = `BACKUP_COMPROMISED`<br>4 = `ENERGY_RESERVE_COMPROMISED`<br>5 = `ENERGY_RESERVE_CRITICAL`<br>6 = `POWER_SUPPLY_COMPROMISED` | plausible |
| `VCFRONT1_a220_factoryMode` | page 220 | VCFRONT1 ECU: a220 factory mode | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a220_serviceMode` | page 220 | Signal reported by VCFRONT1 ECU | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a220_unhealthyReason` | page 220 | VCFRONT1 ECU: a220 unhealthy reason | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `BRIDGE_STATE`<br>2 = `BRIDGE_EFUSE_SELF_TEST`<br>3 = `VCBATT_COMMS`<br>4 = `UNDERVOLTAGE_TRIP_STATE`<br>5 = `UNDERVOLTAGE_SELF_TEST`<br>6 = `OVERVOLTAGE_TRIP_STATE`<br>7 = `OVERVOLTAGE_SELF_TEST`<br>8 = `PROTECTIONS_LOCKOUT_STATE`<br>9 = `PCS_SHUTDOWN_TRIP_STATE`<br>10 = `PCS_SHUTDOWN_SELF_TEST`<br>11 = `PCS_SHUTDOWN_ARM_STATE`<br>12 = `EFUSE_CONFIGURATION`<br>13 = `PCS_EFUSE_STATE`<br>14 = `PCS_ELECTRICAL_CONNECTION`<br>15 = `PCS_ELECTRICAL_CONNECTION_CONFIDENCE`<br>16 = `PCS_COMMS`<br>17 = `PCS_POWER_CAPABILITY`<br>18 = `PCS_SUPPORT_STATUS`<br>19 = `PCS_OVERVOLTAGE_CLAMP_REFERENCE_RATIONALITY`<br>20 = `PCS_OVERVOLTAGE_CLAMP_BUS_RATIONALITY`<br>21 = `PCS_OVERVOLTAGE_CLAMP_TRIP_STATE`<br>22 = `PCS_OVERVOLTAGE_CLAMP_ARM_STATE`<br>23 = `HVC_EFUSE_STATE`<br>24 = `PCS_CRITICAL_HARNESS_RESISTANCE`<br>25 = `PROTECTIONS_ARM_STATE` | plausible |
| `VCFRONT1_a223_failedArmingSetup` | page 223 | VCFRONT1 ECU: a223 failed arming setup | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a223_failedFaultInject` | page 223 | VCFRONT1 ECU: a223 failed fault inject | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a223_overvoltageFaultActive` | page 223 | VCFRONT1 ECU: a223 overvoltage fault active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a223_sharedBridgeShutdownActive` | page 223 | VCFRONT1 ECU: a223 shared bridge shutdown active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a223_timedOut` | page 223 | VCFRONT1 ECU: a223 timed out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a229_bridgeOpened` | page 229 | VCFRONT1 ECU: a229 bridge opened | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a229_pcsMIA` | page 229 | VCFRONT1 ECU: a229 pcs MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a229_pcsNotSupporting` | page 229 | VCFRONT1 ECU: a229 pcs not supporting | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a250_pcsOvShutdownFaultPinActive` | page 250 | VCFRONT1 ECU: a250 pcs ov shutdown fault pin active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a250_pcsOvShutdownArmed` | page 250 | VCFRONT1 ECU: a250 pcs ov shutdown armed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a250_battDomainHealthy` | page 250 | VCFRONT1 ECU: a250 batt domain healthy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a250_busVoltage` | page 250 | VCFRONT1 ECU: a250 bus voltage | 19\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a250_dcdcEnableLineVoltage` | page 250 | VCFRONT1 ECU: a250 dcdc enable line voltage | 29\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCFRONT1_a250_ovClampBusVoltage` | page 250 | VCFRONT1 ECU: a250 ov clamp bus voltage | 38\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a250_ovClampReferenceVoltage` | page 250 | VCFRONT1 ECU: a250 ov clamp reference voltage | 48\|7 | little-endian | unsigned | 0.025 | 0 | V | 0 to 3.175 |  | plausible |
| `VCFRONT1_a250_ovClampMonitorVoltage1` | page 250 | VCFRONT1 ECU: a250 ov clamp monitor voltage1 | 55\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCFRONT1_a251_rationalitySetupCheckResult` | page 251 | VCFRONT1 ECU: a251 rationality setup check result | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCFRONT1_a251_rationalitySetupFailureReason` | page 251 | VCFRONT1 ECU: a251 rationality setup failure reason | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INCORRECT_PIN_CONFIGURATION`<br>2 = `INCORRECT_CLAMP_MONITOR_VOLTAGE`<br>3 = `INCORRECT_PCS_ENABLE_LINE_VOLTAGE`<br>4 = `INCORRECT_PCS_TRIP_STATE`<br>5 = `INCORRECT_PCS_SUPPORT_STATUS`<br>6 = `INCORRECT_PCS_DCDC_ENABLE_FEEDBACK`<br>7 = `MULTIPLE` | plausible |
| `VCFRONT1_a251_clampLowSideCheckResult` | page 251 | VCFRONT1 ECU: a251 clamp low side check result | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCFRONT1_a251_clampLowSideFailureReason` | page 251 | VCFRONT1 ECU: a251 clamp low side failure reason | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INCORRECT_PIN_CONFIGURATION`<br>2 = `INCORRECT_CLAMP_MONITOR_VOLTAGE`<br>3 = `INCORRECT_PCS_ENABLE_LINE_VOLTAGE`<br>4 = `INCORRECT_PCS_TRIP_STATE`<br>5 = `INCORRECT_PCS_SUPPORT_STATUS`<br>6 = `INCORRECT_PCS_DCDC_ENABLE_FEEDBACK`<br>7 = `MULTIPLE` | plausible |
| `VCFRONT1_a251_rationalityShutdownArmedCheckResult` | page 251 | VCFRONT1 ECU: a251 rationality shutdown armed check result | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCFRONT1_a251_rationalityShutdownArmedFailureReason` | page 251 | VCFRONT1 ECU: a251 rationality shutdown armed failure reason | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INCORRECT_PIN_CONFIGURATION`<br>2 = `INCORRECT_CLAMP_MONITOR_VOLTAGE`<br>3 = `INCORRECT_PCS_ENABLE_LINE_VOLTAGE`<br>4 = `INCORRECT_PCS_TRIP_STATE`<br>5 = `INCORRECT_PCS_SUPPORT_STATUS`<br>6 = `INCORRECT_PCS_DCDC_ENABLE_FEEDBACK`<br>7 = `MULTIPLE` | plausible |
| `VCFRONT1_a251_clampHighSideCheckResult` | page 251 | VCFRONT1 ECU: a251 clamp high side check result | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCFRONT1_a251_clampHighSideFailureReason` | page 251 | VCFRONT1 ECU: a251 clamp high side failure reason | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INCORRECT_PIN_CONFIGURATION`<br>2 = `INCORRECT_CLAMP_MONITOR_VOLTAGE`<br>3 = `INCORRECT_PCS_ENABLE_LINE_VOLTAGE`<br>4 = `INCORRECT_PCS_TRIP_STATE`<br>5 = `INCORRECT_PCS_SUPPORT_STATUS`<br>6 = `INCORRECT_PCS_DCDC_ENABLE_FEEDBACK`<br>7 = `MULTIPLE` | plausible |
| `VCFRONT1_a251_rationalityPcsShutdownCheckResult` | page 251 | VCFRONT1 ECU: a251 rationality pcs shutdown check result | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCFRONT1_a251_rationalityPcsShutdownFailureReason` | page 251 | VCFRONT1 ECU: a251 rationality pcs shutdown failure reason | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INCORRECT_PIN_CONFIGURATION`<br>2 = `INCORRECT_CLAMP_MONITOR_VOLTAGE`<br>3 = `INCORRECT_PCS_ENABLE_LINE_VOLTAGE`<br>4 = `INCORRECT_PCS_TRIP_STATE`<br>5 = `INCORRECT_PCS_SUPPORT_STATUS`<br>6 = `INCORRECT_PCS_DCDC_ENABLE_FEEDBACK`<br>7 = `MULTIPLE` | plausible |
| `VCFRONT1_a251_testTimedOut` | page 251 | VCFRONT1 ECU: a251 test timed out | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_stage` | page 252 | VCFRONT1 ECU: a252 stage | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNDEFINED`<br>1 = `RATIONALITY_SETUP_CHECK`<br>2 = `CLAMP_LOW_SIDE_CHECK`<br>3 = `RATIONALITY_SHUTDOWN_ARMED_CHECK`<br>4 = `CLAMP_HIGH_SIDE_CHECK`<br>5 = `RATIONALITY_PCS_SHUTDOWN_CHECK` | plausible |
| `VCFRONT1_a252_incorrectPinConfiguration` | page 252 | VCFRONT1 ECU: a252 incorrect pin configuration | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectClampMonitor1Voltage` | page 252 | VCFRONT1 ECU: a252 incorrect clamp monitor1 voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectClampMonitor2Voltage` | page 252 | VCFRONT1 ECU: a252 incorrect clamp monitor2 voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectClampMonitor3Voltage` | page 252 | VCFRONT1 ECU: a252 incorrect clamp monitor3 voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectPcsEnableLineVoltage` | page 252 | VCFRONT1 ECU: a252 incorrect pcs enable line voltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectPcsTripState` | page 252 | VCFRONT1 ECU: a252 incorrect pcs trip state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectPcsSupportStatus` | page 252 | VCFRONT1 ECU: a252 incorrect pcs support status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_incorrectPcsDcdcEnableFeedback` | page 252 | VCFRONT1 ECU: a252 incorrect pcs dcdc enable feedback | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsOvShutdownFaultPinActive` | page 252 | VCFRONT1 ECU: a252 pcs ov shutdown fault pin active | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsOvShutdownArmed` | page 252 | VCFRONT1 ECU: a252 pcs ov shutdown armed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsSupporting` | page 252 | VCFRONT1 ECU: a252 pcs supporting | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsDcdcEnableFeedback` | page 252 | VCFRONT1 ECU: a252 pcs dcdc enable feedback | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsOvClampArmed` | page 252 | VCFRONT1 ECU: a252 pcs ov clamp armed | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsOvSelfTestEnabled` | page 252 | VCFRONT1 ECU: a252 pcs ov self test enabled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_busVoltage` | page 252 | VCFRONT1 ECU: a252 bus voltage | 33\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a252_dcdcEnableLineVoltage` | page 252 | VCFRONT1 ECU: a252 dcdc enable line voltage | 43\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCFRONT1_a252_ovClampMonitorChannel` | page 252 | VCFRONT1 ECU: a252 ov clamp monitor channel | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `VCFRONT1_a252_ovClampMonitorVoltage` | page 252 | VCFRONT1 ECU: a252 ov clamp monitor voltage | 55\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCFRONT1_a262_eFuseVoltage` | page 262 | VCFRONT1 ECU: a262 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a262_vbatProtVoltage` | page 262 | VCFRONT1 ECU: a262 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a263_eFuseVoltage` | page 263 | VCFRONT1 ECU: a263 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a263_vbatProtVoltage` | page 263 | VCFRONT1 ECU: a263 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a264_eFuseVoltage` | page 264 | VCFRONT1 ECU: a264 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a264_vbatProtVoltage` | page 264 | VCFRONT1 ECU: a264 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a266_eFuseVoltage` | page 266 | VCFRONT1 ECU: a266 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a266_vbatProtVoltage` | page 266 | VCFRONT1 ECU: a266 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a414_failureReason` | page 414 | VCFRONT1 ECU: a414 failure reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `DEVICE_STUCK_ON`<br>2 = `BRIDGE`<br>3 = `BRIDGE_AND_DEVICE_STUCK_ON`<br>4 = `LOAD_UNATTEMPTED_ON`<br>8 = `FOLLOWER`<br>16 = `TIMEOUT`<br>32 = `BRIDGE_SYNC` | plausible |
| `VCFRONT1_a414_loadUnattemptedOnFailure` | page 414 | VCFRONT1 ECU: a414 load unattempted on failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a414_deviceStuckOnFailure` | page 414 | VCFRONT1 ECU: a414 device stuck on failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a414_followerVCRightSelfTestFailure` | page 414 | VCFRONT1 ECU: a414 follower VC right self test failure | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a414_bridgeFailedToOpen` | page 414 | VCFRONT1 ECU: a414 bridge failed to open | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a414_uvLoadshedVsenseDigIn` | page 414 | VCFRONT1 ECU: a414 uv loadshed vsense dig in | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a415_upstreamEFuseStuckOff` | page 415 | VCFRONT1 ECU: a415 upstream e fuse stuck off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_channel` | page 475 | VCFRONT1 ECU: a475 channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `EPAS2`<br>2 = `RIGHT_CONTROLLER`<br>3 = `PCS`<br>4 = `AUTOPILOT_2`<br>5 = `BRAKE_MOTOR_ECU_2`<br>6 = `BRIDGE` | plausible |
| `VCFRONT1_a475_reset` | page 475 | VCFRONT1 ECU: a475 reset | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_spiError` | page 475 | VCFRONT1 ECU: a475 spi error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_autoOn` | page 475 | VCFRONT1 ECU: a475 auto on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_diagnosticBit` | page 475 | VCFRONT1 ECU: a475 diagnostic bit | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_deviceError` | page 475 | VCFRONT1 ECU: a475 device error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_unexpectedLock` | page 475 | VCFRONT1 ECU: a475 unexpected lock | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_unexpectedFailSafe` | page 475 | VCFRONT1 ECU: a475 unexpected fail safe | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_disableOutputFault` | page 475 | VCFRONT1 ECU: a475 disable output fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_vsUndervoltage` | page 475 | VCFRONT1 ECU: a475 vs undervoltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_hardShort` | page 475 | VCFRONT1 ECU: a475 hard short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_prechargeFailure` | page 475 | VCFRONT1 ECU: a475 precharge failure | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_vdsMax` | page 475 | VCFRONT1 ECU: a475 vds max | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_bypassSaturation` | page 475 | VCFRONT1 ECU: a475 bypass saturation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_fuseLatch` | page 475 | VCFRONT1 ECU: a475 fuse latch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_deviceOvertemperature` | page 475 | VCFRONT1 ECU: a475 device overtemperature | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_ntcOvertemperature` | page 475 | VCFRONT1 ECU: a475 ntc overtemperature | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_vgsLow` | page 475 | VCFRONT1 ECU: a475 vgs low | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_chargePumpLow` | page 475 | VCFRONT1 ECU: a475 charge pump low | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_watchdog` | page 475 | VCFRONT1 ECU: a475 watchdog | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_spiNotDone` | page 475 | VCFRONT1 ECU: a475 spi not done | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_csUndervoltage` | page 475 | VCFRONT1 ECU: a475 cs undervoltage | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_configIncorrect` | page 475 | VCFRONT1 ECU: a475 config incorrect | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_bufferFull` | page 475 | VCFRONT1 ECU: a475 buffer full | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_hitAlertRateLimit` | page 475 | VCFRONT1 ECU: a475 hit alert rate limit | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_hwlo` | page 475 | VCFRONT1 ECU: a475 hwlo | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_dinState` | page 475 | VCFRONT1 ECU: a475 din state | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_enable` | page 475 | VCFRONT1 ECU: a475 enable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_channel` | page 480 | VCFRONT1 ECU: a480 channel | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `AUTOPILOT_2`<br>2 = `EPAS2`<br>3 = `RIGHT_CONTROLLER` | plausible |
| `VCFRONT1_a480_reset` | page 480 | VCFRONT1 ECU: a480 reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_spiError` | page 480 | VCFRONT1 ECU: a480 spi error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_autoOn` | page 480 | VCFRONT1 ECU: a480 auto on | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_diagnosticBit` | page 480 | VCFRONT1 ECU: a480 diagnostic bit | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_deviceError` | page 480 | VCFRONT1 ECU: a480 device error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_overcurrent` | page 480 | VCFRONT1 ECU: a480 overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_unexpectedLock` | page 480 | VCFRONT1 ECU: a480 unexpected lock | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_disableOutputFault` | page 480 | VCFRONT1 ECU: a480 disable output fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_vsUndervoltage` | page 480 | VCFRONT1 ECU: a480 vs undervoltage | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_hardShort` | page 480 | VCFRONT1 ECU: a480 hard short | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_vdsMax` | page 480 | VCFRONT1 ECU: a480 vds max | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_bypassSaturation` | page 480 | VCFRONT1 ECU: a480 bypass saturation | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_fuseLatch` | page 480 | VCFRONT1 ECU: a480 fuse latch | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_deviceOvertemperature` | page 480 | VCFRONT1 ECU: a480 device overtemperature | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_ntcOvertemperature` | page 480 | VCFRONT1 ECU: a480 ntc overtemperature | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_vgsLow` | page 480 | VCFRONT1 ECU: a480 vgs low | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_chargePumpLow` | page 480 | VCFRONT1 ECU: a480 charge pump low | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_watchdog` | page 480 | VCFRONT1 ECU: a480 watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_spiNotDone` | page 480 | VCFRONT1 ECU: a480 spi not done | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_configIncorrect` | page 480 | VCFRONT1 ECU: a480 config incorrect | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_bufferFull` | page 480 | VCFRONT1 ECU: a480 buffer full | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_hitAlertRateLimit` | page 480 | VCFRONT1 ECU: a480 hit alert rate limit | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_hwlo` | page 480 | VCFRONT1 ECU: a480 hwlo | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_enable` | page 480 | VCFRONT1 ECU: a480 enable | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a482_lvBridgeEFuseCurrent` | page 482 | VCFRONT1 ECU: a482 lv bridge e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a482_lvBridgeEFuseVoltage` | page 482 | VCFRONT1 ECU: a482 lv bridge e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a482_lvBridgeEFuseTemp` | page 482 | VCFRONT1 ECU: a482 lv bridge e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT1_a484_upstreamEFuseStuckOn` | page 484 | VCFRONT1 ECU: a484 upstream e fuse stuck on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a484_upstreamEFuseVoltage` | page 484 | VCFRONT1 ECU: a484 upstream e fuse voltage | 17\|6 | little-endian | unsigned | 1 | 0 | V | 0 to 63 |  | plausible |
| `VCFRONT1_a484_vbusVoltage` | page 484 | VCFRONT1 ECU: a484 vbus voltage | 24\|6 | little-endian | unsigned | 1 | 0 | V | 0 to 63 |  | plausible |
| `VCFRONT1_a484_upstreamEFuseRatio` | page 484 | VCFRONT1 ECU: a484 upstream e fuse ratio | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT1_a485_upstreamEfuseUnattemptedOn` | page 485 | VCFRONT1 ECU: a485 upstream efuse unattempted on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_bridgeFailedArmingSetup` | page 486 | VCFRONT1 ECU: a486 bridge failed arming setup | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_bridgeFailedSyncCheck` | page 486 | VCFRONT1 ECU: a486 bridge failed sync check | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_localBridgeOutputOn` | page 486 | VCFRONT1 ECU: a486 local bridge output on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_localBridgeSyncArmed` | page 486 | VCFRONT1 ECU: a486 local bridge sync armed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_localBridgeDinState` | page 486 | VCFRONT1 ECU: a486 local bridge din state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeOutputOn` | page 486 | VCFRONT1 ECU: a486 remote bridge output on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeOutputOnValid` | page 486 | VCFRONT1 ECU: a486 remote bridge output on valid | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeSyncArmed` | page 486 | VCFRONT1 ECU: a486 remote bridge sync armed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeSyncArmedValid` | page 486 | VCFRONT1 ECU: a486 remote bridge sync armed valid | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeDinState` | page 486 | VCFRONT1 ECU: a486 remote bridge din state | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_remoteBridgeDinStateValid` | page 486 | VCFRONT1 ECU: a486 remote bridge din state valid | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a496_serviceMode` | page 496 | Signal reported by VCFRONT1 ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a496_frunkOpen` | page 496 | VCFRONT1 ECU: a496 frunk open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a496_NotEnoughPowerForSupport` | page 496 | VCFRONT1 ECU: a496 not enough power for support | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a496_bmsState` | page 496 | VCFRONT1 ECU: a496 bms state; raw 9 = signal not available (SNA) | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT1_a500_channel` | page 500 | VCFRONT1 ECU: a500 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a500_mismatchedState` | page 500 | VCFRONT1 ECU: a500 mismatched state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCFRONT1_a509_channel` | page 509 | VCFRONT1 ECU: a509 channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `EPAS2`<br>2 = `RIGHT_CONTROLLER`<br>3 = `PCS`<br>4 = `AUTOPILOT_2`<br>5 = `BRAKE_MOTOR_ECU_2`<br>6 = `BRIDGE` | plausible |
| `VCFRONT1_a509_state` | page 509 | VCFRONT1 ECU: a509 state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCFRONT1_a509_expectedState` | page 509 | VCFRONT1 ECU: a509 expected state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCFRONT1_a509_hardwareLockout` | page 509 | VCFRONT1 ECU: a509 hardware lockout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a509_unlocksRemaining` | page 509 | VCFRONT1 ECU: a509 unlocks remaining | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_channel` | page 523 | VCFRONT1 ECU: a523 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_control2Byte1` | page 523 | VCFRONT1 ECU: a523 control2 byte1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_control2Byte2` | page 523 | VCFRONT1 ECU: a523 control2 byte2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_control2Byte3` | page 523 | VCFRONT1 ECU: a523 control2 byte3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_control3Byte2` | page 523 | VCFRONT1 ECU: a523 control3 byte2 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a523_control3Byte3` | page 523 | VCFRONT1 ECU: a523 control3 byte3 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a574_frontDriveInverterCurrent` | page 574 | VCFRONT1 ECU: a574 front drive inverter current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT1_a574_frontDriveInverterRemainingRetries` | page 574 | VCFRONT1 ECU: a574 front drive inverter remaining retries | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT1_a596_vcrightCutoffEFuseCurveType` | page 596 | VCFRONT1 ECU: a596 vcright cutoff e fuse curve type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STATIC_EFUSE_CURVE`<br>1 = `DYNAMIC_EFUSE_CURVE` | plausible |
| `VCFRONT1_a596_vcrightCutoffCurveOffsetChannel` | page 596 | VCFRONT1 ECU: a596 vcright cutoff curve offset channel | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT1_a596_vcrightCutoffATerm` | page 596 | VCFRONT1 ECU: a596 vcright cutoff a term; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 50 | 0 | - | 0 to 3276700 | 65535 = `SNA` | plausible |
| `VCFRONT1_a596_vcrightCutoffBTerm` | page 596 | VCFRONT1 ECU: a596 vcright cutoff b term; raw 128 = signal not available (SNA) | 40\|8 | little-endian | signed | 1 | -78 | - | -206 to 49 | -128 = `SNA` | plausible |
| `VCFRONT1_a596_vcrightCutoffCTerm` | page 596 | VCFRONT1 ECU: a596 vcright cutoff c term; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 50 | 0 | - | -1638400 to 1638350 | -32768 = `SNA` | plausible |
| `VCFRONT1_a597_vcrightCutoffEFuseFastBlowType` | page 597 | VCFRONT1 ECU: a597 vcright cutoff e fuse fast blow type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TIMING`<br>1 = `DEBOUNCE` | plausible |
| `VCFRONT1_a597_vcrightCutoffCurrentThreshold` | page 597 | VCFRONT1 ECU: a597 vcright cutoff current threshold | 17\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT1_a597_vcrightCutoffTimingThresholdMs` | page 597 | VCFRONT1 ECU: a597 vcright cutoff timing threshold ms | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT1_a597_vcrightCutoffMaxCount` | page 597 | VCFRONT1 ECU: a597 vcright cutoff max count | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |

## Multiplexing

`VCFRONT1_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals), page 91 (2 signals), page 96 (1 signals), page 98 (2 signals), page 106 (10 signals), page 108 (4 signals), page 120 (9 signals), page 124 (2 signals), page 125 (3 signals), page 126 (4 signals), page 127 (3 signals), page 128 (4 signals), page 129 (4 signals), page 130 (4 signals), page 131 (2 signals), page 132 (3 signals), page 133 (2 signals), page 135 (1 signals), page 144 (2 signals), page 164 (1 signals), page 165 (1 signals), page 177 (2 signals), page 191 (8 signals), page 204 (4 signals), page 205 (4 signals), page 216 (6 signals), page 220 (7 signals), page 223 (5 signals), page 229 (3 signals), page 250 (8 signals), page 251 (11 signals), page 252 (19 signals), page 262 (2 signals), page 263 (2 signals), page 264 (2 signals), page 266 (2 signals), page 414 (6 signals), page 415 (1 signals), page 475 (28 signals), page 480 (25 signals), page 482 (3 signals), page 484 (4 signals), page 485 (1 signals), page 486 (11 signals), page 496 (4 signals), page 500 (2 signals), page 509 (5 signals), page 523 (6 signals), page 574 (2 signals), page 596 (5 signals), page 597 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT1 ECU messages (VCFRONT1)](../../vcfront1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
