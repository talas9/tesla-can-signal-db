---
layout: default
title: "VCBATT1_alertLog (0x53B) — VCBATT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: alert log. Tesla Model 3 / Model Y CAN bus message VCBATT1_alertLog (0x53B) of VCBATT1 ECU, firmware 2026.26.6.5, 829 signals (VCBATT1_alertID, VCBATT1_alertState, VCBATT1_a001_InternalWatchdog, VCBATT1_a015_NVMMMemOverflow and 825 more). Bit layout, scaling, units and value tables."
---

# VCBATT1_alertLog (0x53B) — VCBATT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 829 signals of VCBATT1_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_alertLog` |
| CAN id | 0x53B (1339) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 829 |

## Signals of VCBATT1_alertLog

Tesla Model 3 / Model Y CAN bus signals in `VCBATT1_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_alertID` | selector | VCBATT1 ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>18 = `a018_HardFault`<br>19 = `a019_BusFault`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>28 = `a028_UsageFault`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>36 = `a036_UnknownIrq`<br>37 = `a037_MemManageFault`<br>38 = `a038_ProtFaultInfo`<br>39 = `a039_ProtFaultAddress`<br>40 = `a040_Backtrace`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>77 = `a077_VCBATT0_MIA`<br>78 = `a078_VCBATT1_MIA`<br>79 = `a079_VCBATT2_MIA`<br>80 = `a080_VCFRONT0_MIA`<br>81 = `a081_VCFRONT1_MIA`<br>82 = `a082_VCFRONT2_MIA`<br>86 = `a086_VCBATT_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>96 = `a096_OCS1P_MIA`<br>98 = `a098_DIR_MIA`<br>100 = `a100_CANbus_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>122 = `a122_ICR_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_SCCM_MIA`<br>126 = `a126_EPAS3P_MIA`<br>127 = `a127_vcleftEFuseTrip`<br>129 = `a129_epas1EFuseTrip`<br>130 = `a130_autopilot1EFuseTrip`<br>131 = `a131_PCSCOMMON_MIA`<br>132 = `a132_iBoosterEFuseTrip`<br>133 = `a133_BRAKE_MIA`<br>134 = `a134_hvContactorsEFuseTrip`<br>144 = `a144_EPAS3S_MIA`<br>164 = `a164_eFuseLckoutMissing`<br>165 = `a165_unxpctdEFuseLckout`<br>180 = `a180_DCDCNotSupportingLVBus`<br>182 = `a182_replaceLVBattery`<br>183 = `a183_replaceLVBattery2`<br>188 = `a188_sleepFailed`<br>189 = `a189_IBSMIA`<br>191 = `a191_exitDriveLowLVBusVoltage`<br>196 = `a196_discnctdLVBattery`<br>204 = `a204_undervoltageLoadshedTriggered`<br>205 = `a205_overvoltageProtectionTriggered`<br>212 = `a212_IBSOverTemp`<br>213 = `a213_LVOvercharge`<br>215 = `a215_selfTestOrchestratorDebug`<br>216 = `a216_powerCutoffImminent`<br>217 = `a217_LVProtectionSelfTestInvalid`<br>219 = `a219_LVVoltFloorRchd`<br>220 = `a220_LVUnhealthy`<br>221 = `a221_reverseBatteryFault`<br>223 = `a223_bridgeOvervoltageSelfTestFailure`<br>224 = `a224_overcurrentLoadshedTriggered`<br>225 = `a225_overcurrentSelfTestFailure`<br>226 = `a226_overcurrentSelfTestChannelFastDBG`<br>227 = `a227_overcurrentSelfTestChannelMediumDBG`<br>228 = `a228_overcurrentSelfTestChannelSlowDBG`<br>229 = `a229_LVHealthCompromised`<br>230 = `a230_ingoingOvercurrentSelfTestFailure`<br>231 = `a231_autopilot1EFuseTripDuringOTA`<br>235 = `a235_dualPowerLoadsSelfTestFailure`<br>236 = `a236_hvcDualPowerSelfTestDebug`<br>243 = `a243_LVOverchargeInstc`<br>244 = `a244_brakeValveECUEFuseTrip`<br>245 = `a245_sleepBypassFault`<br>252 = `a252_controllerWakeup`<br>253 = `a253_maxChrgeSssionTmeout`<br>256 = `a256_nxppca9539Fault`<br>258 = `a258_resistanceEstimationRun`<br>259 = `a259_LVVoltageDropOnHighLoadCurrent`<br>260 = `a260_deadLVBattery`<br>275 = `a275_TLVBMS_BmbCommunication`<br>276 = `a276_TLVBMS_BmbDataIntegrityLoss`<br>277 = `a277_TLVBMS_BmbStatusRegError`<br>278 = `a278_TLVBMS_BmbHwOverCurrentFault`<br>297 = `a297_TLVBMS_BmbHwOverTemperatureFault`<br>359 = `a359_postPORExcessiveAh`<br>362 = `a362_TLVBMS_AllSocCorrectionTimeout`<br>363 = `a363_TLVBMS_BleedBasedWeakShort`<br>370 = `a370_noLVSupportSocTooLow`<br>371 = `a371_failureToPrechargeRisk`<br>372 = `a372_TLVBMS_BmbHwOverVoltageFault`<br>376 = `a376_controllerWakeupDebug`<br>379 = `a379_shortedCellTestRunDebug`<br>387 = `a387_shortedCellInstc`<br>388 = `a388_shortedCell`<br>392 = `a392_TLVBMS_BmbHwUnderVoltageFault`<br>400 = `a400_TLVBMS_BmbVrefBad`<br>401 = `a401_deadLVMinimalAhDischarged`<br>402 = `a402_LVBatteryCannotSupportVehicle`<br>403 = `a403_chargeExitHardCurrentLimit`<br>404 = `a404_resistanceEstimationHardFailure`<br>405 = `a405_dcrData1`<br>406 = `a406_dcrData2`<br>407 = `a407_dcrMilliOhmsAboveThreshold`<br>408 = `a408_standbyChargeProfileHardExit`<br>410 = `a410_LVBatteryDataCollection1`<br>411 = `a411_LVBatteryDataCollection2`<br>412 = `a412_dcrData3`<br>413 = `a413_TLVBMS_BmbVrefWarning`<br>414 = `a414_undervoltageSelfTestFailure`<br>415 = `a415_undervoltageSelfTestStuckOff`<br>416 = `a416_TLVBMS_BrickOverDischarged`<br>417 = `a417_TLVBMS_BrickOverVoltageFault`<br>418 = `a418_TLVBMS_BrickOverVoltageWarning`<br>419 = `a419_TLVBMS_BrickSocLow`<br>421 = `a421_LVBatteryHealthTestInterrupted`<br>422 = `a422_rtosSleepFailed`<br>423 = `a423_TLVBMS_BrickUnderVoltageFault`<br>424 = `a424_TLVBMS_BrickUnderVoltageOcv`<br>425 = `a425_TLVBMS_BusVoltageTooHigh`<br>426 = `a426_TLVBMS_BusVoltageTooLow`<br>427 = `a427_TLVBMS_CacChange`<br>428 = `a428_TLVBMS_CacImbalance`<br>429 = `a429_TLVBMS_CapacityTestResults`<br>430 = `a430_TLVBMS_ChargeCurrentLimitExceeded`<br>431 = `a431_TLVBMS_ChargeOverCurrent`<br>432 = `a432_TLVBMS_ChargeRegulationFault`<br>433 = `a433_TLVBMS_ConfigFromBmbModIdFailed`<br>434 = `a434_TLVBMS_ConfigInitFailed`<br>435 = `a435_TLVBMS_DchgCurrentLimitExceeded`<br>436 = `a436_TLVBMS_DischargeOverCurrent`<br>437 = `a437_TLVBMS_NvmRegistrationError`<br>438 = `a438_TLVBMS_PackOverTemperatureFault`<br>439 = `a439_TLVBMS_PackOverTemperatureWarning`<br>440 = `a440_TLVBMS_PackSNInvalidForNvm`<br>441 = `a441_TLVBMS_ResetNeededForNvmPackSwap`<br>442 = `a442_TLVBMS_SocChange`<br>443 = `a443_TLVBMS_BmbDieOverTemperature`<br>446 = `a446_LVBatteryUnrecoverableByAnyDevice`<br>450 = `a450_doorWakeToOpenDBG`<br>461 = `a461_TLVBMS_SocHighAhError`<br>462 = `a462_LVBMSFault`<br>475 = `a475_vnf1248Fault`<br>476 = `a476_LVBMSMIA`<br>477 = `a477_LVBatteryUnrecoverableByVehicle`<br>478 = `a478_LVBMS_MOSFET_Open`<br>479 = `a479_LVBMS_ECPA_NotClosed`<br>480 = `a480_vnf1048Fault`<br>481 = `a481_LVBridgeCloseDBG`<br>482 = `a482_lvBridgeEFuseTrip`<br>483 = `a483_vnf1048SelfTestFailure`<br>484 = `a484_undervoltageSelfTestStuckOn`<br>485 = `a485_uvSelfTestLoadUnattemptedOnDbg`<br>486 = `a486_undervoltageSelfTestBridgeSyncFailure`<br>489 = `a489_vnf1248SelfTestDebug`<br>490 = `a490_vnf1248SelfTestFailure`<br>491 = `a491_vnf1248ConfigurationMismatch`<br>492 = `a492_TLVBMS_SocImbalance`<br>493 = `a493_TLVBMS_SocImbalanceWarning`<br>494 = `a494_LVBatteryTempBlockingOTA`<br>495 = `a495_LVBatteryRecoveryBlocked`<br>496 = `a496_LVBatteryExitDriveWarning`<br>497 = `a497_LVBatteryWarnDisconnect`<br>498 = `a498_TLVBMS_ImpedanceTestResults`<br>500 = `a500_eFuseASICStateMismatch`<br>501 = `a501_vnf1048ConfigurationMismatch`<br>502 = `a502_TLVBMS_WeakShortImpedance`<br>503 = `a503_TLVBMS_BrickExtendedOvFault`<br>508 = `a508_TLVBMS_ImpedanceGrowth`<br>509 = `a509_eFuseASICManagerStateMismatch`<br>510 = `a510_LVBatteryRecoveryTimeout`<br>512 = `a512_LVBMSFault_MOS_Open_hardwareOC`<br>513 = `a513_LVBMSFault_MOS_Open_chgOC`<br>514 = `a514_LVBMSFault_MOS_Open_cellUV`<br>515 = `a515_LVBMSFault_MOS_Open_cellOV`<br>518 = `a518_LVBMSFault_MOS_Open_packOV`<br>521 = `a521_vcleftEFuseLoadShed`<br>523 = `a523_eFuseThresholdsIncorrect`<br>525 = `a525_LVBatterySWMisconfiguration`<br>527 = `a527_LVBatteryCellImbalance`<br>528 = `a528_LVBatteryCommsDiscnctd`<br>529 = `a529_discnctdBatteryStateUnknown`<br>533 = `a533_TLVBMS_MosfetOverTemperatureFault`<br>541 = `a541_LVBatteryChargeOCLevel1`<br>544 = `a544_LVBatteryCommsBusTurnedOff`<br>545 = `a545_LVBatteryTypeUnknown`<br>548 = `a548_HVFaultLoadShed`<br>555 = `a555_LVBatteryCellRebalancing`<br>556 = `a556_falseTriggerOfDiscnctdBatteryTest`<br>559 = `a559_LVBatteryLowSOC`<br>561 = `a561_LVBMSEFuseOvertemperature`<br>562 = `a562_LVBMSModuleOvertemperature`<br>573 = `a573_radarEFuseTrip`<br>575 = `a575_vbatFusedLoadShedEFuseTrip`<br>576 = `a576_mcuLogicEFuseTrip`<br>580 = `a580_rightHeadlightEFuseTrip`<br>581 = `a581_harnessResistanceInfo`<br>582 = `a582_goodForPCSPowerCycle`<br>585 = `a585_lvBatteryHealthTestRequired`<br>587 = `a587_externalLVPowerSupply`<br>588 = `a588_vcleftPwrRationalityCurve`<br>589 = `a589_vcleftFastBlowDetection`<br>592 = `a592_vcleftCurvePowerCutoff`<br>593 = `a593_vcleftFastBlowPowerCutoff`<br>595 = `a595_voltageSensorMismatch`<br>597 = `a597_LVBMBeFuseSelfTestNotReady`<br>598 = `a598_LVBMBeFuseSelfTestFailed`<br>599 = `a599_LVBatteryTypeUnsupported`<br>600 = `a600_currentSensorMismatch`<br>601 = `a601_LVBatteryHeaterNotPresent`<br>608 = `a608_TLVBMS_BleedFetFailure`<br>615 = `a615_TLVBMS_BatteryHeaterFault`<br>617 = `a617_APP_MIA`<br>628 = `a628_TLVBMS_BmbThermistorFault`<br>629 = `a629_TLVBMS_PackTemperatureIrrational`<br>670 = `a670_TLVBMS_EfuseStateIrrational`<br>672 = `a672_LVBatteryVitals` | plausible |
| `VCBATT1_alertState` |  | VCBATT1 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCBATT1_a001_InternalWatchdog` | page 1 | VCBATT1 ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a015_NVMMMemOverflow` | page 15 | VCBATT1 ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a015_NVMMFilesystemError` | page 15 | VCBATT1 ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a015_NVMMRecordIDError` | page 15 | VCBATT1 ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a059_voltageDrop` | page 59 | VCBATT1 ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a059_resistanceEstimate` | page 59 | VCBATT1 ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCBATT1_a059_current` | page 59 | VCBATT1 ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCBATT1_a063_switchChannel` | page 63 | VCBATT1 ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a063_switchType` | page 63 | VCBATT1 ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a063_ADCVoltage` | page 63 | VCBATT1 ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCBATT1_a063_disconnected` | page 63 | VCBATT1 ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a063_indeterminate` | page 63 | VCBATT1 ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a063_stuckActive` | page 63 | VCBATT1 ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a063_faulted` | page 63 | VCBATT1 ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a091_FRONTIPC_faultsAndExtras` | page 91 | VCBATT1 ECU: a091 FRONTIPC faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a091_FRONTIPC_state` | page 91 | VCBATT1 ECU: a091 FRONTIPC state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a096_FRONTIPC_status` | page 96 | VCBATT1 ECU: a096 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a098_FRONTIPC_temperature` | page 98 | VCBATT1 ECU: a098 FRONTIPC temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a098_FRONTIPC_thermalControl` | page 98 | VCBATT1 ECU: a098 FRONTIPC thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_BATTIPC_dcdcRailStatus` | page 106 | VCBATT1 ECU: a106 BATTIPC dcdc rail status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_BATTIPC_dcdcStatus` | page 106 | VCBATT1 ECU: a106 BATTIPC dcdc status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_VEH_dcdcStatus` | page 106 | VCBATT1 ECU: a106 VEH dcdc status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_VEH_thermalControl` | page 106 | VCBATT1 ECU: a106 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_VEH_dcdcRailStatus` | page 106 | VCBATT1 ECU: a106 VEH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_CH_dcdcRailStatus` | page 106 | VCBATT1 ECU: a106 CH dcdc rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_CH_alertMatrix` | page 106 | VCBATT1 ECU: a106 CH alert matrix | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_FRONTIPC_thermalControl` | page 106 | VCBATT1 ECU: a106 FRONTIPC thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_FRONTIPC_dcdcRailStatus` | page 106 | VCBATT1 ECU: a106 FRONTIPC dcdc rail status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_FRONTIPC_dcdcStatus` | page 106 | VCBATT1 ECU: a106 FRONTIPC dcdc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a108_FRONTIPC_status` | page 108 | VCBATT1 ECU: a108 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a108_FRONTIPC_temperature` | page 108 | VCBATT1 ECU: a108 FRONTIPC temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a108_FRONTIPC_thermalControl` | page 108 | VCBATT1 ECU: a108 FRONTIPC thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a108_FRONTIPC_motorStatus` | page 108 | VCBATT1 ECU: a108 FRONTIPC motor status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_BATTIPC_speed` | page 120 | VCBATT1 ECU: a120 BATTIPC speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_speed` | page 120 | VCBATT1 ECU: a120 FRONTIPC speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_systemStatus` | page 120 | VCBATT1 ECU: a120 FRONTIPC system status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_BATTIPC_systemStatus` | page 120 | VCBATT1 ECU: a120 BATTIPC system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_systemPower` | page 120 | VCBATT1 ECU: a120 FRONTIPC system power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_autonomyHealth` | page 120 | VCBATT1 ECU: a120 FRONTIPC autonomy health | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_BATTIPC_chassisControl2` | page 120 | VCBATT1 ECU: a120 BATTIPC chassis control2 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_chassisControl2` | page 120 | VCBATT1 ECU: a120 FRONTIPC chassis control2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_FRONTIPC_odometerStatus` | page 120 | VCBATT1 ECU: a120 FRONTIPC odometer status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a124_FRONTIPC_status` | page 124 | VCBATT1 ECU: a124 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a124_BATTIPC_status` | page 124 | VCBATT1 ECU: a124 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a125_FRONTIPC_leftStalk` | page 125 | VCBATT1 ECU: a125 FRONTIPC left stalk | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a125_FRONTIPC_steerAngle` | page 125 | VCBATT1 ECU: a125 FRONTIPC steer angle | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a125_FRONTIPC_info` | page 125 | VCBATT1 ECU: a125 FRONTIPC info | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a126_FRONTIPC_sysStatus` | page 126 | VCBATT1 ECU: a126 FRONTIPC sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a126_BATTIPC_sysStatus` | page 126 | VCBATT1 ECU: a126 BATTIPC sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a126_FRONTIPC_status` | page 126 | VCBATT1 ECU: a126 FRONTIPC status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a126_BATTIPC_status` | page 126 | VCBATT1 ECU: a126 BATTIPC status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a127_vcleftEFuseCurrent` | page 127 | VCBATT1 ECU: a127 vcleft e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a127_vcleftEFuseVoltage` | page 127 | VCBATT1 ECU: a127 vcleft e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a127_vcleftEFuseTemp` | page 127 | VCBATT1 ECU: a127 vcleft e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCBATT1_a127_vcleftEFuseRemainingRetries` | page 127 | VCBATT1 ECU: a127 vcleft e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCBATT1_a129_epas1EFuseCurrent` | page 129 | VCBATT1 ECU: a129 epas1 e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a129_epas1EFuseVoltage` | page 129 | VCBATT1 ECU: a129 epas1 e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a129_epas1EFuseTemp` | page 129 | VCBATT1 ECU: a129 epas1 e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCBATT1_a130_autopilot1EFuseCurrent` | page 130 | VCBATT1 ECU: a130 autopilot1 e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a130_autopilot1EFuseVoltage` | page 130 | VCBATT1 ECU: a130 autopilot1 e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a130_autopilot1EFuseTemp` | page 130 | VCBATT1 ECU: a130 autopilot1 e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCBATT1_a130_autopilot1EFuseRemainingRetries` | page 130 | VCBATT1 ECU: a130 autopilot1 e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCBATT1_a131_FRONTIPC_power` | page 131 | VCBATT1 ECU: a131 FRONTIPC power | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a131_BATTIPC_power` | page 131 | VCBATT1 ECU: a131 BATTIPC power | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a132_iBoosterCurrent` | page 132 | VCBATT1 ECU: a132 i booster current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a132_iBoosterVoltage` | page 132 | VCBATT1 ECU: a132 i booster voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a132_iBoosterEFuseTemp` | page 132 | VCBATT1 ECU: a132 i booster e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCBATT1_a133_BATTIPC_primaryActuator` | page 133 | VCBATT1 ECU: a133 BATTIPC primary actuator | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a133_FRONTIPC_secondaryActuator` | page 133 | VCBATT1 ECU: a133 FRONTIPC secondary actuator | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a144_FRONTIPC_status` | page 144 | VCBATT1 ECU: a144 FRONTIPC status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a144_BATTIPC_status` | page 144 | VCBATT1 ECU: a144 BATTIPC status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a164_lockoutVoltage` | page 164 | VCBATT1 ECU: a164 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a165_lockoutVoltage` | page 165 | VCBATT1 ECU: a165 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a180_vehiclePowerState` | page 180 | VCBATT1 ECU: a180 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a180_hvState` | page 180 | VCBATT1 ECU: a180 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT1_a180_bmsState` | page 180 | VCBATT1 ECU: a180 bms state; raw 9 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a180_notEnoughPowerForSupport` | page 180 | VCBATT1 ECU: a180 not enough power for support | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_pcsEFuseStable` | page 180 | VCBATT1 ECU: a180 pcs e fuse stable | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_vcrightEFuseStable` | page 180 | VCBATT1 ECU: a180 vcright e fuse stable | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_contactorEFuseStable` | page 180 | VCBATT1 ECU: a180 contactor e fuse stable | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_hvcEFuseStable` | page 180 | VCBATT1 ECU: a180 hvc e fuse stable | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_replaceLVBattery` | page 180 | VCBATT1 ECU: a180 replace LV battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_BMS_MIA` | page 180 | VCBATT1 ECU: a180 BMS MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_PCS_MIA` | page 180 | VCBATT1 ECU: a180 PCS MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_HVBlockingMismatch` | page 180 | VCBATT1 ECU: a180 HV blocking mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_serviceMode` | page 180 | Signal reported by VCBATT1 ECU | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_transportMode` | page 180 | VCBATT1 ECU: a180 transport mode | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_frunkOpen` | page 180 | VCBATT1 ECU: a180 frunk open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_dcdcLVSupportStatus` | page 180 | VCBATT1 ECU: a180 dcdc LV support status | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCBATT1_a180_IBSVoltage` | page 180 | VCBATT1 ECU: a180 IBS voltage | 48\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCBATT1_a180_targetPCSVoltage` | page 180 | VCBATT1 ECU: a180 target PCS voltage | 56\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a182_deadLV` | page 182 | VCBATT1 ECU: a182 dead LV | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_voltageDrop` | page 182 | VCBATT1 ECU: a182 voltage drop | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_overcharge` | page 182 | VCBATT1 ECU: a182 overcharge | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_LVFloorReached` | page 182 | VCBATT1 ECU: a182 LV floor reached | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_shortedCell` | page 182 | VCBATT1 ECU: a182 shorted cell | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_postPORExcessiveAh` | page 182 | VCBATT1 ECU: a182 post POR excessive ah | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_resistanceEstimationHardFailure` | page 182 | VCBATT1 ECU: a182 resistance estimation hard failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_dcrMilliOhmsAboveThreshold` | page 182 | VCBATT1 ECU: a182 dcr milli ohms above threshold | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_prechargeLVLoadReduction` | page 182 | VCBATT1 ECU: a182 precharge LV load reduction | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_factoryMode` | page 182 | VCBATT1 ECU: a182 factory mode | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_serviceMode` | page 182 | Signal reported by VCBATT1 ECU | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_transportMode` | page 182 | VCBATT1 ECU: a182 transport mode | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_frunkOpen` | page 182 | VCBATT1 ECU: a182 frunk open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_packOverDischarged` | page 182 | VCBATT1 ECU: a182 pack over discharged | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_cellImbalance` | page 182 | VCBATT1 ECU: a182 cell imbalance | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_instantPrechargeDCRTooHigh` | page 182 | VCBATT1 ECU: a182 instant precharge DCR too high | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_ambientTemp` | page 182 | VCBATT1 ECU: a182 ambient temp; raw 0 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 1 | -40 | degC | -39 to 87 | 0 = `SNA` | plausible |
| `VCBATT1_a182_dischargedAmpHours` | page 182 | VCBATT1 ECU: a182 discharged amp hours | 39\|8 | little-endian | unsigned | 60 | 0 | Ah | 0 to 15300 |  | plausible |
| `VCBATT1_a182_chargedAmpHours` | page 182 | VCBATT1 ECU: a182 charged amp hours | 47\|8 | little-endian | unsigned | 60 | 0 | Ah | 0 to 15300 |  | plausible |
| `VCBATT1_a182_calibrationLostFault` | page 182 | VCBATT1 ECU: a182 calibration lost fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_samplingHWError` | page 182 | VCBATT1 ECU: a182 sampling HW error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_brickOverDischarged` | page 182 | VCBATT1 ECU: a182 brick over discharged | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_impedanceGrowth` | page 182 | VCBATT1 ECU: a182 impedance growth | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_batteryType` | page 182 | VCBATT1 ECU: a182 battery type | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a182_bleedFetTestFailure` | page 182 | VCBATT1 ECU: a182 bleed fet test failure | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_weakShort` | page 182 | VCBATT1 ECU: a182 weak short | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a188_sleepBypassCurrent` | page 188 | VCBATT1 ECU: a188 sleep bypass current | 16\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 51 |  | plausible |
| `VCBATT1_a188_IBSCurrent` | page 188 | VCBATT1 ECU: a188 IBS current | 24\|10 | little-endian | signed | 0.08 | 0 | A | -40.96 to 40.88 |  | plausible |
| `VCBATT1_a188_LVSupport` | page 188 | VCBATT1 ECU: a188 LV support | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a188_bridgeEFuseState` | page 188 | VCBATT1 ECU: a188 bridge e fuse state | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCBATT1_a188_bridgeState` | page 188 | VCBATT1 ECU: a188 bridge state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `WAIT_FOR_COMMS`<br>2 = `PRECHARGING_BRIDGE`<br>3 = `WAIT_FOR_BRIDGE_CLOSE`<br>4 = `COMMS_SYNC`<br>5 = `VOLTAGE_MATCH`<br>6 = `CONNECTING`<br>7 = `CONNECTED`<br>8 = `OPEN` | plausible |
| `VCBATT1_a188_frontPrivBusAwake` | page 188 | VCBATT1 ECU: a188 front priv bus awake | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a188_sleepShutdownStep` | page 188 | VCBATT1 ECU: a188 sleep shutdown step; raw 7 = signal not available (SNA) | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SUITABLE_BYPASS_CURRENT`<br>1 = `TURN_OFF_HIGH_POWER_FEEDS`<br>2 = `WAIT_FOR_FRONTPRIV_ASLEEP`<br>3 = `TURN_OFF_BRIDGE`<br>4 = `TURN_OFF_SW_EN`<br>5 = `WAIT_FOR_SLEEPABLE_CURRENT`<br>6 = `DONE`<br>7 = `SNA` | plausible |
| `VCBATT1_a188_vehiclePowerState` | page 188 | VCBATT1 ECU: a188 vehicle power state | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `LOW_POWER_AWAKE`<br>2 = `CONDITIONING`<br>3 = `ACCESSORY`<br>4 = `ACCESSORY_PLUS`<br>5 = `DRIVE`<br>6 = `OTA`<br>7 = `WAIT_FOR_HIGH_POWER`<br>8 = `TURN_ON_LV`<br>9 = `SYSTEM_CHECKS`<br>10 = `LV_ON`<br>11 = `JUMP_START`<br>12 = `LV_SHUTDOWN`<br>13 = `GO_QUIET`<br>14 = `SLEEP_SHUTDOWN`<br>15 = `LOW_POWER_STANDBY`<br>16 = `RESET` | plausible |
| `VCBATT1_a188_timeNotSleeping` | page 188 | VCBATT1 ECU: a188 time not sleeping | 56\|6 | little-endian | unsigned | 1 | 0 | sec | 0 to 63 |  | plausible |
| `VCBATT1_a188_CANAfterQuiet` | page 188 | VCBATT1 ECU: a188 CAN after quiet | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_vehiclePowerState` | page 191 | VCBATT1 ECU: a191 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a191_hvState` | page 191 | VCBATT1 ECU: a191 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT1_a191_reverseBatteryEFuseFault` | page 191 | VCBATT1 ECU: a191 reverse battery e fuse fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_vehicleLoadShedActive` | page 191 | VCBATT1 ECU: a191 vehicle load shed active | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_vehicleLoadShedHvFaultActive` | page 191 | VCBATT1 ECU: a191 vehicle load shed hv fault active | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_vehicleLoadShedPostCrashActive` | page 191 | VCBATT1 ECU: a191 vehicle load shed post crash active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_IBSVoltage` | page 191 | VCBATT1 ECU: a191 IBS voltage | 25\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCBATT1_a191_a180_DCDCNotSupportingLVBus` | page 191 | VCBATT1 ECU: a191 a180 DCDC not supporting LV bus | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_MOSState` | page 191 | VCBATT1 ECU: a191 MOS state; raw 3 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a191_LVBMSVoltage` | page 191 | VCBATT1 ECU: a191 LVBMS voltage | 36\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCBATT1_a191_ECPAState` | page 191 | VCBATT1 ECU: a191 ECPA state; raw 3 = signal not available (SNA) | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a191_LVBMSCurrentTargetValid` | page 191 | VCBATT1 ECU: a191 LVBMS current target valid | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_LVBMSVoltageTargetValid` | page 191 | VCBATT1 ECU: a191 LVBMS voltage target valid | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_serviceMode` | page 191 | Signal reported by VCBATT1 ECU | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_frunkOpen` | page 191 | VCBATT1 ECU: a191 frunk open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_vehicleLoadShedStage` | page 191 | VCBATT1 ECU: a191 vehicle load shed stage | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE_OR_UNDEFINED`<br>1 = `1`<br>2 = `2`<br>3 = `3` | plausible |
| `VCBATT1_a191_exitDriveWarningTimerExpired` | page 191 | VCBATT1 ECU: a191 exit drive warning timer expired | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_LVBMSMIA` | page 191 | VCBATT1 ECU: a191 LVBMSMIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_PCS_MIA` | page 191 | VCBATT1 ECU: a191 PCS MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_NotEnoughPowerForSupport` | page 191 | VCBATT1 ECU: a191 not enough power for support | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_bmsState` | page 191 | VCBATT1 ECU: a191 bms state; raw 9 = signal not available (SNA) | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a196_factoryMode` | page 196 | VCBATT1 ECU: a196 factory mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a196_serviceMode` | page 196 | Signal reported by VCBATT1 ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a196_transportMode` | page 196 | VCBATT1 ECU: a196 transport mode | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a196_frunkOpen` | page 196 | VCBATT1 ECU: a196 frunk open | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a196_vehiclePowerState` | page 196 | VCBATT1 ECU: a196 vehicle power state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a196_batterySMState` | page 196 | VCBATT1 ECU: a196 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a196_disconnectedBatteryTestCurrent` | page 196 | VCBATT1 ECU: a196 disconnected battery test current | 28\|12 | little-endian | unsigned | 0.004884005 | -10 | A | -10 to 10.000000475 |  | plausible |
| `VCBATT1_a196_disconnectedBatteryTestVoltage` | page 196 | VCBATT1 ECU: a196 disconnected battery test voltage | 40\|8 | little-endian | unsigned | 0.0392156876624 | 6 | V | 6 to 16.0000003539 |  | plausible |
| `VCBATT1_a196_disconnectedBatteryTestPrevVoltage` | page 196 | VCBATT1 ECU: a196 disconnected battery test prev voltage | 48\|8 | little-endian | unsigned | 0.0392156876624 | 6 | V | 6 to 16.0000003539 |  | plausible |
| `VCBATT1_a196_ECPAState` | page 196 | VCBATT1 ECU: a196 ECPA state; raw 3 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a204_vbusVoltage` | page 204 | VCBATT1 ECU: a204 vbus voltage | 16\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCBATT1_a204_ARailLocked` | page 204 | VCBATT1 ECU: a204 a rail locked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a204_uvLoadshedFaultInject` | page 204 | VCBATT1 ECU: a204 uv loadshed fault inject | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a204_batBridgeCurrent` | page 204 | VCBATT1 ECU: a204 bat bridge current | 32\|16 | little-endian | signed | 0.0625 | 0 | A | -2048 to 2047.9375 |  | plausible |
| `VCBATT1_a205_busVoltage` | page 205 | VCBATT1 ECU: a205 bus voltage | 16\|10 | little-endian | unsigned | 0.025 | 0 | V | 0 to 25.575 |  | plausible |
| `VCBATT1_a205_ARailLocked` | page 205 | VCBATT1 ECU: a205 a rail locked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a205_ovLoadshedFaultInject` | page 205 | VCBATT1 ECU: a205 ov loadshed fault inject | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a205_batBridgeCurrent` | page 205 | VCBATT1 ECU: a205 bat bridge current | 32\|16 | little-endian | signed | 0.0625 | 0 | A | -2048 to 2047.9375 |  | plausible |
| `VCBATT1_a212_IBSTemp` | page 212 | VCBATT1 ECU: a212 IBS temp | 16\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCBATT1_a213_IBSVolts` | page 213 | VCBATT1 ECU: a213 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a213_IBSAh` | page 213 | VCBATT1 ECU: a213 IBS ah | 32\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCBATT1_a213_LVBatteryTemp` | page 213 | VCBATT1 ECU: a213 LV battery temp; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 | -32768 = `SNA` | plausible |
| `VCBATT1_a216_inDrive` | page 216 | VCBATT1 ECU: a216 in drive | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a216_hvState` | page 216 | VCBATT1 ECU: a216 hv state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT1_a216_vcleftFastBlowImminent` | page 216 | VCBATT1 ECU: a216 vcleft fast blow imminent | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a216_vcleftFastBlowDebounceImminent` | page 216 | VCBATT1 ECU: a216 vcleft fast blow debounce imminent | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a216_vcleftStaticImminent` | page 216 | VCBATT1 ECU: a216 vcleft static imminent | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a216_vcleftDynamicImminent` | page 216 | VCBATT1 ECU: a216 vcleft dynamic imminent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a219_IBSVolts` | page 219 | VCBATT1 ECU: a219 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a219_IBSAh` | page 219 | VCBATT1 ECU: a219 IBS ah | 32\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCBATT1_a219_IBSCurrent` | page 219 | VCBATT1 ECU: a219 IBS current | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a220_DI_gear` | page 220 | VCBATT1 ECU: a220 DI gear; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCBATT1_a220_redundancyRequired` | page 220 | VCBATT1 ECU: a220 redundancy required | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a220_vehicleSpeed` | page 220 | VCBATT1 ECU: a220 vehicle speed | 20\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCBATT1_a220_lvHealthStatus` | page 220 | VCBATT1 ECU: a220 lv health status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOMAIN_HEALTHY`<br>1 = `HEALTHY_LIMITED`<br>2 = `LATENT_FAULT`<br>3 = `BACKUP_COMPROMISED`<br>4 = `ENERGY_RESERVE_COMPROMISED`<br>5 = `ENERGY_RESERVE_CRITICAL`<br>6 = `POWER_SUPPLY_COMPROMISED` | plausible |
| `VCBATT1_a220_factoryMode` | page 220 | VCBATT1 ECU: a220 factory mode | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a220_serviceMode` | page 220 | Signal reported by VCBATT1 ECU | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a220_unhealthyReason` | page 220 | VCBATT1 ECU: a220 unhealthy reason | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `BRIDGE_STATE`<br>2 = `BRIDGE_EFUSE_SELF_TEST`<br>3 = `VCFRONT_COMMS`<br>4 = `UNDERVOLTAGE_TRIP_STATE`<br>5 = `UNDERVOLTAGE_SELF_TEST`<br>6 = `OVERVOLTAGE_TRIP_STATE`<br>7 = `OVERVOLTAGE_SELF_TEST`<br>8 = `OVERCURRENT_TRIP_STATE`<br>9 = `OVERCURRENT_SELF_TEST`<br>10 = `PROTECTIONS_LOCKOUT_STATE`<br>11 = `EFUSE_CONFIGURATION`<br>12 = `REVERSE_BATTERY_EFUSE_STATE`<br>13 = `LV_BATTERY_ELECTRICAL_CONNECTION`<br>14 = `LV_BATTERY_ELECTRICAL_CONNECTION_CONFIDENCE`<br>15 = `LV_BATTERY_COMMS`<br>16 = `LV_BATTERY_EFUSE_STATE`<br>17 = `LV_BATTERY_SENSOR_COMMS`<br>18 = `LV_BATTERY_VOLTAGE_SENSOR_RATIONALITY`<br>19 = `LV_BATTERY_CURRENT_SENSOR_RATIONALITY`<br>20 = `LV_BATTERY_ENERGY_CAPABILITY_ACTIVE_DECEL`<br>21 = `LV_BATTERY_POWER_CAPABILITY_ACTIVE_DECEL`<br>22 = `LV_BATTERY_ENERGY_CAPABILITY_CRITICAL_PULLOVER`<br>23 = `LV_BATTERY_CAPABILITY_CONFIDENCE`<br>24 = `LV_BATTERY_CONFIGURATION`<br>25 = `LV_BATTERY_IMPEDANCE`<br>26 = `LV_BATTERY_ENERGY_CAPABILITY_URGENT_PULLOVER`<br>27 = `DUAL_POWER_LOADS_SELF_TEST`<br>28 = `LV_BATTERY_CRITICAL_HARNESS_RESISTANCE`<br>29 = `HVC_RIGHT_DOMAIN_POWER_SELF_TEST`<br>30 = `PROTECTIONS_ARM_STATE` | plausible |
| `VCBATT1_a221_IBSCurrent` | page 221 | VCBATT1 ECU: a221 IBS current | 16\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a221_PCSCurrent` | page 221 | VCBATT1 ECU: a221 PCS current | 32\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCBATT1_a221_serviceMode` | page 221 | Signal reported by VCBATT1 ECU | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a221_frunkOpen` | page 221 | VCBATT1 ECU: a221 frunk open | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_failedArmingSetup` | page 223 | VCBATT1 ECU: a223 failed arming setup | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_failedFaultInject` | page 223 | VCBATT1 ECU: a223 failed fault inject | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_overvoltageFaultActive` | page 223 | VCBATT1 ECU: a223 overvoltage fault active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_sharedBridgeShutdownActive` | page 223 | VCBATT1 ECU: a223 shared bridge shutdown active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_timedOut` | page 223 | VCBATT1 ECU: a223 timed out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_ocSenseAmpCurrent` | page 224 | VCBATT1 ECU: a224 oc sense amp current | 16\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCBATT1_a224_hardwareLoadshedFaultActive` | page 224 | VCBATT1 ECU: a224 hardware loadshed fault active | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_ocLoadshedFaultActive` | page 224 | VCBATT1 ECU: a224 oc loadshed fault active | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_faultChannelPinActiveSlow` | page 224 | VCBATT1 ECU: a224 fault channel pin active slow | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_faultChannelPinActiveMedium` | page 224 | VCBATT1 ECU: a224 fault channel pin active medium | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_faultChannelPinActiveFast` | page 224 | VCBATT1 ECU: a224 fault channel pin active fast | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_faultChannelPinActiveIngoing` | page 224 | VCBATT1 ECU: a224 fault channel pin active ingoing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_hardwareLoadshedFaultActiveIngoing` | page 224 | VCBATT1 ECU: a224 hardware loadshed fault active ingoing | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_bridgeOpened` | page 229 | VCBATT1 ECU: a229 bridge opened | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_lvBatteryElecDisc` | page 229 | VCBATT1 ECU: a229 lv battery elec disc | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_lvBatteryEFuseOff` | page 229 | VCBATT1 ECU: a229 lv battery e fuse off | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_lvBatteryActiveDecelEnergy` | page 229 | VCBATT1 ECU: a229 lv battery active decel energy | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_lvBatteryRevEfuseOff` | page 229 | VCBATT1 ECU: a229 lv battery rev efuse off | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_lvBatteryComms` | page 229 | VCBATT1 ECU: a229 lv battery comms | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a235_hvcRightDomainFailureReason` | page 235 | VCBATT1 ECU: a235 hvc right domain failure reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_FAILURE`<br>1 = `EFUSE_OPEN_FAILURE`<br>2 = `DIODE_OPEN_FAILURE`<br>3 = `EFUSE_OR_DIODE_SHORT_FAILURE`<br>4 = `EFUSE_AND_DIODE_FAILURE` | plausible |
| `VCBATT1_a235_hvcLeftDomainFailureReason` | page 235 | VCBATT1 ECU: a235 hvc left domain failure reason | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_FAILURE`<br>1 = `EFUSE_OPEN_FAILURE`<br>2 = `DIODE_OPEN_FAILURE`<br>3 = `EFUSE_OR_DIODE_SHORT_FAILURE`<br>4 = `EFUSE_AND_DIODE_FAILURE` | plausible |
| `VCBATT1_a235_timedOut` | page 235 | VCBATT1 ECU: a235 timed out | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a243_IBSVolts` | page 243 | VCBATT1 ECU: a243 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a243_IBSCurrent` | page 243 | VCBATT1 ECU: a243 IBS current | 32\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a243_LVBatteryTemp` | page 243 | VCBATT1 ECU: a243 LV battery temp; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 | -32768 = `SNA` | plausible |
| `VCBATT1_a244_brakeValveECUEFuseCurrent` | page 244 | VCBATT1 ECU: a244 brake valve ECUE fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a244_brakeValveECUEFuseVoltage` | page 244 | VCBATT1 ECU: a244 brake valve ECUE fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a245_current` | page 245 | VCBATT1 ECU: a245 current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a245_voltage` | page 245 | VCBATT1 ECU: a245 voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a245_vbatProtVoltage` | page 245 | VCBATT1 ECU: a245 vbat prot voltage | 48\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a253_currentNotTapered` | page 253 | VCBATT1 ECU: a253 current not tapered | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_ampHourTargetNotReached` | page 253 | VCBATT1 ECU: a253 amp hour target not reached | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_IBSCurrent` | page 253 | VCBATT1 ECU: a253 IBS current | 18\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a253_IBSAmpHours` | page 253 | VCBATT1 ECU: a253 IBS amp hours | 34\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCBATT1_a253_LVBatteryTemp` | page 253 | VCBATT1 ECU: a253 LV battery temp; raw 127 = signal not available (SNA) | 48\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCBATT1_a253_firstChargeOTA` | page 253 | VCBATT1 ECU: a253 first charge OTA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_firstChargePOR` | page 253 | VCBATT1 ECU: a253 first charge POR | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_serviceMode` | page 253 | Signal reported by VCBATT1 ECU | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_frunkOpen` | page 253 | VCBATT1 ECU: a253 frunk open | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a259_serviceMode` | page 259 | Signal reported by VCBATT1 ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a259_voltageDropCounter` | page 259 | VCBATT1 ECU: a259 voltage drop counter | 17\|3 | little-endian | unsigned | 2 | 0 | - | 0 to 14 |  | plausible |
| `VCBATT1_a259_minVoltageReached` | page 259 | VCBATT1 ECU: a259 min voltage reached | 20\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a259_IBSTemp` | page 259 | VCBATT1 ECU: a259 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCBATT1_a259_maxCurrentReached` | page 259 | VCBATT1 ECU: a259 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a260_IBSVolts` | page 260 | VCBATT1 ECU: a260 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a260_IBSAh` | page 260 | VCBATT1 ECU: a260 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a260_vehiclePowerState` | page 260 | VCBATT1 ECU: a260 vehicle power state | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a260_batterySMState` | page 260 | VCBATT1 ECU: a260 battery SM state | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a260_HV_UP` | page 260 | VCBATT1 ECU: a260 HV UP | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_notEnoughPowerForSupport` | page 260 | VCBATT1 ECU: a260 not enough power for support | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_coolantHasBeenFilled` | page 260 | VCBATT1 ECU: a260 coolant has been filled | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_ampHourTrigger` | page 260 | VCBATT1 ECU: a260 amp hour trigger | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_voltageTrigger` | page 260 | VCBATT1 ECU: a260 voltage trigger | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_crashDetected` | page 260 | VCBATT1 ECU: a260 crash detected | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_BMS_MIA` | page 260 | VCBATT1 ECU: a260 BMS MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_PCS_MIA` | page 260 | VCBATT1 ECU: a260 PCS MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_HVBlockingMismatch` | page 260 | VCBATT1 ECU: a260 HV blocking mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_serviceMode` | page 260 | Signal reported by VCBATT1 ECU | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_dcdcLVSupportStatus` | page 260 | VCBATT1 ECU: a260 dcdc LV support status | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCBATT1_a260_PCSAndVCREFuseStable` | page 260 | VCBATT1 ECU: a260 PCS and VCRE fuse stable | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_bmsState` | page 260 | VCBATT1 ECU: a260 bms state; raw 9 = signal not available (SNA) | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a297_bmbDeviceId` | page 297 | VCBATT1 ECU: a297 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCBATT1_a297_bmbDeviceFaultTempMask` | page 297 | VCBATT1 ECU: a297 bmb device fault temp mask | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a359_IBSVolts` | page 359 | VCBATT1 ECU: a359 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a359_IBSAh` | page 359 | VCBATT1 ECU: a359 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a359_vehiclePowerState` | page 359 | VCBATT1 ECU: a359 vehicle power state | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a359_batterySMState` | page 359 | VCBATT1 ECU: a359 battery SM state | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a359_hvState` | page 359 | VCBATT1 ECU: a359 hv state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT1_a359_coolantHasBeenFilled` | page 359 | VCBATT1 ECU: a359 coolant has been filled | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_crashDetected` | page 359 | VCBATT1 ECU: a359 crash detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_BMS_MIA` | page 359 | VCBATT1 ECU: a359 BMS MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_PCS_MIA` | page 359 | VCBATT1 ECU: a359 PCS MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_serviceMode` | page 359 | Signal reported by VCBATT1 ECU | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_dcdcLVSupportStatus` | page 359 | VCBATT1 ECU: a359 dcdc LV support status | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCBATT1_a359_bmsState` | page 359 | VCBATT1 ECU: a359 bms state; raw 9 = signal not available (SNA) | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a363_minBleedCharge` | page 363 | VCBATT1 ECU: a363 min bleed charge | 16\|15 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 32.767 |  | plausible |
| `VCBATT1_a363_avgBleedCharge` | page 363 | VCBATT1 ECU: a363 avg bleed charge | 32\|15 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 32.767 |  | plausible |
| `VCBATT1_a363_checkIntervalDays` | page 363 | VCBATT1 ECU: a363 check interval days | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCBATT1_a363_minBleedChargeBrickId` | page 363 | VCBATT1 ECU: a363 min bleed charge brick id; raw 31 = signal not available (SNA) | 56\|5 | little-endian | unsigned | 1 | 1 |  | 1 to 31 | 31 = `SNA` | plausible |
| `VCBATT1_a363_setFromNvm` | page 363 | VCBATT1 ECU: a363 set from nvm | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a370_IBSVolts` | page 370 | VCBATT1 ECU: a370 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a370_IBSAh` | page 370 | VCBATT1 ECU: a370 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a370_notEnoughPowerForSupport` | page 370 | VCBATT1 ECU: a370 not enough power for support | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a370_serviceMode` | page 370 | Signal reported by VCBATT1 ECU | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a370_sleepCurrent` | page 370 | VCBATT1 ECU: a370 sleep current | 42\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCBATT1_a370_SOC` | page 370 | VCBATT1 ECU: a370 SOC; raw 7 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 2.5 | 5 | PCT | 5 to 20 | 7 = `SNA` | plausible |
| `VCBATT1_a371_shortedCellTestTrigger` | page 371 | VCBATT1 ECU: a371 shorted cell test trigger | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_voltDropOnHighCurrentTrigger` | page 371 | VCBATT1 ECU: a371 volt drop on high current trigger | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_deadLVMinimalAhDischargedTrigger` | page 371 | VCBATT1 ECU: a371 dead LV minimal ah discharged trigger | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_resistanceEstimationHardFailTrigger` | page 371 | VCBATT1 ECU: a371 resistance estimation hard fail trigger | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_dcrMilliOhmsAboveThresholdTrigger` | page 371 | VCBATT1 ECU: a371 dcr milli ohms above threshold trigger | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_prechargeLVLoadReductionTrigger` | page 371 | VCBATT1 ECU: a371 precharge LV load reduction trigger | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_instantPrechargeDCRTooHighTrigger` | page 371 | VCBATT1 ECU: a371 instant precharge DCR too high trigger | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a372_bmbDeviceId` | page 372 | VCBATT1 ECU: a372 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCBATT1_a372_bmbDeviceFaultBrickMask` | page 372 | VCBATT1 ECU: a372 bmb device fault brick mask | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a387_shortedCellFaultCounter` | page 387 | VCBATT1 ECU: a387 shorted cell fault counter | 16\|3 | little-endian | unsigned | 1 | 0 | - | 0 to 7 |  | plausible |
| `VCBATT1_a387_minVoltageReached` | page 387 | VCBATT1 ECU: a387 min voltage reached | 19\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a387_opportunisticTest` | page 387 | VCBATT1 ECU: a387 opportunistic test | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a387_IBSTemp` | page 387 | VCBATT1 ECU: a387 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCBATT1_a387_maxCurrentReached` | page 387 | VCBATT1 ECU: a387 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a388_shortedCellFaultCounter` | page 388 | VCBATT1 ECU: a388 shorted cell fault counter | 16\|3 | little-endian | unsigned | 1 | 0 | - | 0 to 7 |  | plausible |
| `VCBATT1_a388_minVoltageReached` | page 388 | VCBATT1 ECU: a388 min voltage reached | 19\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a388_opportunisticTest` | page 388 | VCBATT1 ECU: a388 opportunistic test | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a388_IBSTemp` | page 388 | VCBATT1 ECU: a388 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCBATT1_a388_maxCurrentReached` | page 388 | VCBATT1 ECU: a388 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a392_bmbDeviceId` | page 392 | VCBATT1 ECU: a392 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCBATT1_a392_bmbDeviceFaultBrickMask` | page 392 | VCBATT1 ECU: a392 bmb device fault brick mask | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a401_LVBatteryTemp` | page 401 | VCBATT1 ECU: a401 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCBATT1_a401_IBSCurrent` | page 401 | VCBATT1 ECU: a401 IBS current | 24\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a401_IBSVoltage` | page 401 | VCBATT1 ECU: a401 IBS voltage | 36\|11 | little-endian | unsigned | 0.0108873518184 | 0 | V | 0 to 22.2864091723 |  | plausible |
| `VCBATT1_a401_IBSAmpHours` | page 401 | VCBATT1 ECU: a401 IBS amp hours | 48\|8 | little-endian | unsigned | 0.01 | -2.55 | Ah | -2.55 to 4.4408920985e-16 |  | plausible |
| `VCBATT1_a402_LVBatteryTemp` | page 402 | VCBATT1 ECU: a402 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCBATT1_a402_batterySMState` | page 402 | VCBATT1 ECU: a402 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a402_failureToPrechargeRisk` | page 402 | VCBATT1 ECU: a402 failure to precharge risk | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_electricalDisconnectLVBattery` | page 402 | VCBATT1 ECU: a402 electrical disconnect LV battery | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_communicationDisconnectLVBattery` | page 402 | VCBATT1 ECU: a402 communication disconnect LV battery | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_reverseBatteryFault` | page 402 | VCBATT1 ECU: a402 reverse battery fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_MOSOpen` | page 402 | VCBATT1 ECU: a402 MOS open | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_serviceMode` | page 402 | Signal reported by VCBATT1 ECU | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_frunkOpen` | page 402 | VCBATT1 ECU: a402 frunk open | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a404_minVoltageReached` | page 404 | VCBATT1 ECU: a404 min voltage reached | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT1_a404_IBSTemp` | page 404 | VCBATT1 ECU: a404 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCBATT1_a404_maxCurrentReached` | page 404 | VCBATT1 ECU: a404 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCBATT1_a407_dcrMilliOhms` | page 407 | VCBATT1 ECU: a407 dcr milli ohms | 16\|8 | little-endian | unsigned | 0.2 | 0 | mOhms | 0 to 51 |  | plausible |
| `VCBATT1_a407_dcr12VThreshold` | page 407 | VCBATT1 ECU: a407 dcr12 v threshold | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `40_MILLIOHMS`<br>2 = `35_MILLIOHMS`<br>3 = `30_MILLIOHMS`<br>4 = `27_MILLIOHMS`<br>5 = `24_MILLIOHMS`<br>6 = `22_MILLIOHMS`<br>7 = `20_MILLIOHMS`<br>8 = `19_MILLIOHMS`<br>9 = `18_MILLIOHMS`<br>10 = `17_MILLIOHMS`<br>11 = `16_MILLIOHMS`<br>12 = `15_MILLIOHMS` | plausible |
| `VCBATT1_a407_avgIntervalCurrent` | page 407 | VCBATT1 ECU: a407 avg interval current | 28\|5 | little-endian | unsigned | 1 | -31 | A | -31 to 0 |  | plausible |
| `VCBATT1_a407_intervalCurrentVariance` | page 407 | VCBATT1 ECU: a407 interval current variance | 33\|6 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6.3 |  | plausible |
| `VCBATT1_a407_avgPulseCurrent` | page 407 | VCBATT1 ECU: a407 avg pulse current | 39\|7 | little-endian | unsigned | 1 | -127 | A | -127 to 0 |  | plausible |
| `VCBATT1_a407_pulseCurrentVarianceShifted` | page 407 | VCBATT1 ECU: a407 pulse current variance shifted | 46\|6 | little-endian | unsigned | 0.25 | 0 | A | 0 to 15.75 |  | plausible |
| `VCBATT1_a407_IBSTemperature` | page 407 | VCBATT1 ECU: a407 IBS temperature | 52\|8 | little-endian | unsigned | 0.5 | -30 | degC | -30 to 97.5 |  | plausible |
| `VCBATT1_a407_testCounter` | page 407 | VCBATT1 ECU: a407 test counter | 60\|2 | little-endian | unsigned | 1 | 0 | - | 0 to 3 |  | plausible |
| `VCBATT1_a407_testingExpended` | page 407 | VCBATT1 ECU: a407 testing expended | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a407_opportunisticTest` | page 407 | VCBATT1 ECU: a407 opportunistic test | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_failureReason` | page 414 | VCBATT1 ECU: a414 failure reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `DEVICE_STUCK_ON`<br>2 = `BRIDGE`<br>3 = `BRIDGE_AND_DEVICE_STUCK_ON`<br>4 = `LOAD_UNATTEMPTED_ON`<br>8 = `FOLLOWER`<br>16 = `TIMEOUT`<br>32 = `BRIDGE_SYNC` | plausible |
| `VCBATT1_a414_loadUnattemptedOnFailure` | page 414 | VCBATT1 ECU: a414 load unattempted on failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_deviceStuckOnFailure` | page 414 | VCBATT1 ECU: a414 device stuck on failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_followerVCLeftSelfTestFailure` | page 414 | VCBATT1 ECU: a414 follower VC left self test failure | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_bridgeFailedToOpen` | page 414 | VCBATT1 ECU: a414 bridge failed to open | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_uvLoadshedVsenseDigIn` | page 414 | VCBATT1 ECU: a414 uv loadshed vsense dig in | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a415_upstreamEFuseStuckOff` | page 415 | VCBATT1 ECU: a415 upstream e fuse stuck off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a416_brickVoltageMin` | page 416 | VCBATT1 ECU: a416 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a416_brickVoltageMax` | page 416 | VCBATT1 ECU: a416 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a416_packCurrent` | page 416 | VCBATT1 ECU: a416 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a416_socMin` | page 416 | VCBATT1 ECU: a416 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a416_brickId` | page 416 | VCBATT1 ECU: a416 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a417_brickVoltageMin` | page 417 | VCBATT1 ECU: a417 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a417_brickVoltageMax` | page 417 | VCBATT1 ECU: a417 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a417_packCurrent` | page 417 | VCBATT1 ECU: a417 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a417_socMax` | page 417 | VCBATT1 ECU: a417 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a417_brickId` | page 417 | VCBATT1 ECU: a417 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a418_brickVoltageMin` | page 418 | VCBATT1 ECU: a418 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a418_brickVoltageMax` | page 418 | VCBATT1 ECU: a418 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a418_packCurrent` | page 418 | VCBATT1 ECU: a418 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a418_socMax` | page 418 | VCBATT1 ECU: a418 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a418_brickId` | page 418 | VCBATT1 ECU: a418 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a419_brickVoltageMin` | page 419 | VCBATT1 ECU: a419 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a419_brickVoltageMax` | page 419 | VCBATT1 ECU: a419 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a419_packCurrent` | page 419 | VCBATT1 ECU: a419 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a419_socMin` | page 419 | VCBATT1 ECU: a419 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a419_brickId` | page 419 | VCBATT1 ECU: a419 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a421_vehiclePowerState` | page 421 | VCBATT1 ECU: a421 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a421_LVBMSSOC` | page 421 | VCBATT1 ECU: a421 LVBMSSOC | 18\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCBATT1_a421_capacityTestUrgency` | page 421 | VCBATT1 ECU: a421 capacity test urgency | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `REFRESH_DESIRED`<br>2 = `REFRESH_STALLED`<br>3 = `RESULTS_EXPIRED`<br>4 = `NO_RESULTS_FOR_NEW_PACK`<br>5 = `FAULTED_LOSS_OF_TIME` | plausible |
| `VCBATT1_a421_energyActiveDecel` | page 421 | VCBATT1 ECU: a421 energy active decel | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a421_energyCriticalPullover` | page 421 | VCBATT1 ECU: a421 energy critical pullover | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a421_powerActiveDecel` | page 421 | VCBATT1 ECU: a421 power active decel | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a423_brickVoltageMin` | page 423 | VCBATT1 ECU: a423 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a423_brickVoltageMax` | page 423 | VCBATT1 ECU: a423 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a423_packCurrent` | page 423 | VCBATT1 ECU: a423 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a423_socMin` | page 423 | VCBATT1 ECU: a423 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a423_brickId` | page 423 | VCBATT1 ECU: a423 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a424_brickVoltageMin` | page 424 | VCBATT1 ECU: a424 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a424_brickVoltageMax` | page 424 | VCBATT1 ECU: a424 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a424_packCurrent` | page 424 | VCBATT1 ECU: a424 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a424_socMin` | page 424 | VCBATT1 ECU: a424 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a424_brickId` | page 424 | VCBATT1 ECU: a424 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a431_netPackCurrent` | page 431 | VCBATT1 ECU: a431 net pack current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a431_maxChargeCurrentLimit` | page 431 | VCBATT1 ECU: a431 max charge current limit; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a431_hvjbCurrentLimit` | page 431 | VCBATT1 ECU: a431 hvjb current limit; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a432_targetCurrent` | page 432 | VCBATT1 ECU: a432 target current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a432_packCurrent` | page 432 | VCBATT1 ECU: a432 pack current; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a433_bmbModuleId` | page 433 | VCBATT1 ECU: a433 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a433_packTypeData` | page 433 | VCBATT1 ECU: a433 pack type data | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a433_cellTypeData` | page 433 | VCBATT1 ECU: a433 cell type data | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a433_bmbModuleIdValid` | page 433 | VCBATT1 ECU: a433 bmb module id valid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a433_useBmbModuleId` | page 433 | VCBATT1 ECU: a433 use bmb module id | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a434_bmbModuleId` | page 434 | VCBATT1 ECU: a434 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a434_packTypeData` | page 434 | VCBATT1 ECU: a434 pack type data | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a434_cellTypeData` | page 434 | VCBATT1 ECU: a434 cell type data | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a434_bmbModuleIdValid` | page 434 | VCBATT1 ECU: a434 bmb module id valid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a434_useBmbModuleId` | page 434 | VCBATT1 ECU: a434 use bmb module id | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a436_netPackCurrent` | page 436 | VCBATT1 ECU: a436 net pack current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a436_maxDischargeCurrentLimit` | page 436 | VCBATT1 ECU: a436 max discharge current limit; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a436_hvjbCurrentLimit` | page 436 | VCBATT1 ECU: a436 hvjb current limit; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCBATT1_a437_nvmDataMissingA` | page 437 | VCBATT1 ECU: a437 nvm data missing a | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a437_nvmDataMissingB` | page 437 | VCBATT1 ECU: a437 nvm data missing b | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a438_temperature` | page 438 | VCBATT1 ECU: a438 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCBATT1_a438_sensorId` | page 438 | VCBATT1 ECU: a438 sensor id | 32\|6 | little-endian | unsigned | 1 | 1 |  | 1 to 64 |  | layout-only |
| `VCBATT1_a439_temperature` | page 439 | VCBATT1 ECU: a439 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCBATT1_a439_sensorId` | page 439 | VCBATT1 ECU: a439 sensor id | 32\|6 | little-endian | unsigned | 1 | 1 |  | 1 to 64 |  | layout-only |
| `VCBATT1_a441_bmbModuleId` | page 441 | VCBATT1 ECU: a441 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a441_bmbModuleIdPrev` | page 441 | VCBATT1 ECU: a441 bmb module id prev | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a446_cell1Voltage` | page 446 | VCBATT1 ECU: a446 cell1 voltage | 16\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a446_cell2Voltage` | page 446 | VCBATT1 ECU: a446 cell2 voltage | 25\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a446_cell3Voltage` | page 446 | VCBATT1 ECU: a446 cell3 voltage | 34\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a446_cell4Voltage` | page 446 | VCBATT1 ECU: a446 cell4 voltage | 43\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a446_sumCellVoltage` | page 446 | VCBATT1 ECU: a446 sum cell voltage | 52\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a446_deepDischargeFlag` | page 446 | VCBATT1 ECU: a446 deep discharge flag | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a446_serviceMode` | page 446 | Signal reported by VCBATT1 ECU | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a446_frunkOpen` | page 446 | VCBATT1 ECU: a446 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CellOVLevel1` | page 462 | VCBATT1 ECU: a462 cell OV level1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CellOVLevel2` | page 462 | VCBATT1 ECU: a462 cell OV level2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CellOVLevel3` | page 462 | VCBATT1 ECU: a462 cell OV level3 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CellUVLevel1` | page 462 | VCBATT1 ECU: a462 cell UV level1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CellUVLevel2` | page 462 | VCBATT1 ECU: a462 cell UV level2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_ModuleOTLevel1` | page 462 | VCBATT1 ECU: a462 module OT level1 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_PackOVLevel1` | page 462 | VCBATT1 ECU: a462 pack OV level1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_PackOVLevel2` | page 462 | VCBATT1 ECU: a462 pack OV level2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_DischrgOCLevel1` | page 462 | VCBATT1 ECU: a462 dischrg OC level1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_HardwareOCLevel2` | page 462 | VCBATT1 ECU: a462 hardware OC level2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_ChrgOCLevel1` | page 462 | VCBATT1 ECU: a462 chrg OC level1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_ChrgOCLevel2` | page 462 | VCBATT1 ECU: a462 chrg OC level2 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_MOSFETOTLevel1` | page 462 | VCBATT1 ECU: a462 MOSFETOT level1 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_CPA_State` | page 462 | VCBATT1 ECU: a462 CPA state | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_NTCTempDiffWarnLevel1` | page 462 | VCBATT1 ECU: a462 NTC temp diff warn level1 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_KBValueLostFault` | page 462 | VCBATT1 ECU: a462 KB value lost fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_BalanceCircuitFault` | page 462 | VCBATT1 ECU: a462 balance circuit fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_MOSOpenFault` | page 462 | VCBATT1 ECU: a462 MOS open fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_DeepDischarge` | page 462 | VCBATT1 ECU: a462 deep discharge | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_SamplingError` | page 462 | VCBATT1 ECU: a462 sampling error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_MOSFETStuckClose` | page 462 | VCBATT1 ECU: a462 MOSFET stuck close | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_MOSFETStuckOpen` | page 462 | VCBATT1 ECU: a462 MOSFET stuck open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_Imbalance` | page 462 | VCBATT1 ECU: a462 imbalance | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_serviceMode` | page 462 | Signal reported by VCBATT1 ECU | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_frunkOpen` | page 462 | VCBATT1 ECU: a462 frunk open | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_channel` | page 475 | VCBATT1 ECU: a475 channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `BRAKE_MOTOR_ECU_1`<br>2 = `LOADSHED`<br>3 = `AUTOPILOT_1`<br>4 = `BRIDGE`<br>5 = `EPAS1`<br>6 = `LEFT_CONTROLLER` | plausible |
| `VCBATT1_a475_reset` | page 475 | VCBATT1 ECU: a475 reset | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_spiError` | page 475 | VCBATT1 ECU: a475 spi error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_autoOn` | page 475 | VCBATT1 ECU: a475 auto on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_diagnosticBit` | page 475 | VCBATT1 ECU: a475 diagnostic bit | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_deviceError` | page 475 | VCBATT1 ECU: a475 device error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_unexpectedLock` | page 475 | VCBATT1 ECU: a475 unexpected lock | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_unexpectedFailSafe` | page 475 | VCBATT1 ECU: a475 unexpected fail safe | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_disableOutputFault` | page 475 | VCBATT1 ECU: a475 disable output fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_vsUndervoltage` | page 475 | VCBATT1 ECU: a475 vs undervoltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_hardShort` | page 475 | VCBATT1 ECU: a475 hard short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_prechargeFailure` | page 475 | VCBATT1 ECU: a475 precharge failure | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_vdsMax` | page 475 | VCBATT1 ECU: a475 vds max | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_bypassSaturation` | page 475 | VCBATT1 ECU: a475 bypass saturation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_fuseLatch` | page 475 | VCBATT1 ECU: a475 fuse latch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_deviceOvertemperature` | page 475 | VCBATT1 ECU: a475 device overtemperature | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_ntcOvertemperature` | page 475 | VCBATT1 ECU: a475 ntc overtemperature | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_vgsLow` | page 475 | VCBATT1 ECU: a475 vgs low | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_chargePumpLow` | page 475 | VCBATT1 ECU: a475 charge pump low | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_watchdog` | page 475 | VCBATT1 ECU: a475 watchdog | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_spiNotDone` | page 475 | VCBATT1 ECU: a475 spi not done | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_csUndervoltage` | page 475 | VCBATT1 ECU: a475 cs undervoltage | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_configIncorrect` | page 475 | VCBATT1 ECU: a475 config incorrect | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_bufferFull` | page 475 | VCBATT1 ECU: a475 buffer full | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_hitAlertRateLimit` | page 475 | VCBATT1 ECU: a475 hit alert rate limit | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_hwlo` | page 475 | VCBATT1 ECU: a475 hwlo | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_dinState` | page 475 | VCBATT1 ECU: a475 din state | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_enable` | page 475 | VCBATT1 ECU: a475 enable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM1_timedOut` | page 476 | VCBATT1 ECU: a476 FRM1 timed out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM2_timedOut` | page 476 | VCBATT1 ECU: a476 FRM2 timed out | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM3_timedOut` | page 476 | VCBATT1 ECU: a476 FRM3 timed out | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM4_timedOut` | page 476 | VCBATT1 ECU: a476 FRM4 timed out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM5_timedOut` | page 476 | VCBATT1 ECU: a476 FRM5 timed out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM6_timedOut` | page 476 | VCBATT1 ECU: a476 FRM6 timed out | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM7_timedOut` | page 476 | VCBATT1 ECU: a476 FRM7 timed out | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM8_timedOut` | page 476 | VCBATT1 ECU: a476 FRM8 timed out | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM9_timedOut` | page 476 | VCBATT1 ECU: a476 FRM9 timed out | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM10_timedOut` | page 476 | VCBATT1 ECU: a476 FRM10 timed out | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM11_timedOut` | page 476 | VCBATT1 ECU: a476 FRM11 timed out | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_FRM12_timedOut` | page 476 | VCBATT1 ECU: a476 FRM12 timed out | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_factoryMode` | page 476 | VCBATT1 ECU: a476 factory mode | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_serviceMode` | page 476 | Signal reported by VCBATT1 ECU | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_transportMode` | page 476 | VCBATT1 ECU: a476 transport mode | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_frunkOpen` | page 476 | VCBATT1 ECU: a476 frunk open | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_vehiclePowerState` | page 476 | VCBATT1 ECU: a476 vehicle power state | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a476_batterySMState` | page 476 | VCBATT1 ECU: a476 battery SM state | 34\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a476_ECPAState` | page 476 | VCBATT1 ECU: a476 ECPA state; raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a477_cell1Voltage` | page 477 | VCBATT1 ECU: a477 cell1 voltage | 16\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a477_cell2Voltage` | page 477 | VCBATT1 ECU: a477 cell2 voltage | 25\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a477_cell3Voltage` | page 477 | VCBATT1 ECU: a477 cell3 voltage | 34\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a477_cell4Voltage` | page 477 | VCBATT1 ECU: a477 cell4 voltage | 43\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCBATT1_a477_sumCellVoltage` | page 477 | VCBATT1 ECU: a477 sum cell voltage | 52\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a477_deepDischargeFlag` | page 477 | VCBATT1 ECU: a477 deep discharge flag | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a477_serviceMode` | page 477 | Signal reported by VCBATT1 ECU | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a477_frunkOpen` | page 477 | VCBATT1 ECU: a477 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_battFaultPackOverVoltage` | page 478 | VCBATT1 ECU: a478 batt fault pack over voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_battFaultHardwareOverCurrent` | page 478 | VCBATT1 ECU: a478 batt fault hardware over current | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_battFaultChargeOverCurrent` | page 478 | VCBATT1 ECU: a478 batt fault charge over current | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_battFaultCellUnderVoltage` | page 478 | VCBATT1 ECU: a478 batt fault cell under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_battFaultCellOverVoltage` | page 478 | VCBATT1 ECU: a478 batt fault cell over voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_vehiclePowerState` | page 478 | VCBATT1 ECU: a478 vehicle power state | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a478_batterySMState` | page 478 | VCBATT1 ECU: a478 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a478_bmsState` | page 478 | VCBATT1 ECU: a478 bms state; raw 9 = signal not available (SNA) | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a478_dcdcLVSupportStatus` | page 478 | VCBATT1 ECU: a478 dcdc LV support status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCBATT1_a478_factoryMode` | page 478 | VCBATT1 ECU: a478 factory mode | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_serviceMode` | page 478 | Signal reported by VCBATT1 ECU | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_transportMode` | page 478 | VCBATT1 ECU: a478 transport mode | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_notEnoughPowerForSupport` | page 478 | VCBATT1 ECU: a478 not enough power for support | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_crashDetected` | page 478 | VCBATT1 ECU: a478 crash detected | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_BMS_MIA` | page 478 | VCBATT1 ECU: a478 BMS MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_PCS_MIA` | page 478 | VCBATT1 ECU: a478 PCS MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_HVBlockingMismatch` | page 478 | VCBATT1 ECU: a478 HV blocking mismatch | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_HV_UP` | page 478 | VCBATT1 ECU: a478 HV UP | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_pcsEFuseStable` | page 478 | VCBATT1 ECU: a478 pcs e fuse stable | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_vcrightEFuseStable` | page 478 | VCBATT1 ECU: a478 vcright e fuse stable | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_contactorEFuseStable` | page 478 | VCBATT1 ECU: a478 contactor e fuse stable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_hvcEFuseStable` | page 478 | VCBATT1 ECU: a478 hvc e fuse stable | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_frunkOpen` | page 478 | VCBATT1 ECU: a478 frunk open | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_FRM3_timedOut` | page 479 | VCBATT1 ECU: a479 FRM3 timed out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_ECPAState` | page 479 | VCBATT1 ECU: a479 ECPA state; raw 3 = signal not available (SNA) | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a479_factoryMode` | page 479 | VCBATT1 ECU: a479 factory mode | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_serviceMode` | page 479 | Signal reported by VCBATT1 ECU | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_transportMode` | page 479 | VCBATT1 ECU: a479 transport mode | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_frunkLatchStatus` | page 479 | VCBATT1 ECU: a479 frunk latch status; raw 0 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCBATT1_a479_vehiclePowerState` | page 479 | VCBATT1 ECU: a479 vehicle power state | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a479_batterySMState` | page 479 | VCBATT1 ECU: a479 battery SM state | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a480_channel` | page 480 | VCBATT1 ECU: a480 channel | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `AUTOPILOT_1`<br>2 = `EPAS1`<br>3 = `LEFT_CONTROLLER` | plausible |
| `VCBATT1_a480_reset` | page 480 | VCBATT1 ECU: a480 reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_spiError` | page 480 | VCBATT1 ECU: a480 spi error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_autoOn` | page 480 | VCBATT1 ECU: a480 auto on | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_diagnosticBit` | page 480 | VCBATT1 ECU: a480 diagnostic bit | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_deviceError` | page 480 | VCBATT1 ECU: a480 device error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_overcurrent` | page 480 | VCBATT1 ECU: a480 overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_unexpectedLock` | page 480 | VCBATT1 ECU: a480 unexpected lock | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_disableOutputFault` | page 480 | VCBATT1 ECU: a480 disable output fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_vsUndervoltage` | page 480 | VCBATT1 ECU: a480 vs undervoltage | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_hardShort` | page 480 | VCBATT1 ECU: a480 hard short | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_vdsMax` | page 480 | VCBATT1 ECU: a480 vds max | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_bypassSaturation` | page 480 | VCBATT1 ECU: a480 bypass saturation | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_fuseLatch` | page 480 | VCBATT1 ECU: a480 fuse latch | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_deviceOvertemperature` | page 480 | VCBATT1 ECU: a480 device overtemperature | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_ntcOvertemperature` | page 480 | VCBATT1 ECU: a480 ntc overtemperature | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_vgsLow` | page 480 | VCBATT1 ECU: a480 vgs low | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_chargePumpLow` | page 480 | VCBATT1 ECU: a480 charge pump low | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_watchdog` | page 480 | VCBATT1 ECU: a480 watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_spiNotDone` | page 480 | VCBATT1 ECU: a480 spi not done | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_configIncorrect` | page 480 | VCBATT1 ECU: a480 config incorrect | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_bufferFull` | page 480 | VCBATT1 ECU: a480 buffer full | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_hitAlertRateLimit` | page 480 | VCBATT1 ECU: a480 hit alert rate limit | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_hwlo` | page 480 | VCBATT1 ECU: a480 hwlo | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_enable` | page 480 | VCBATT1 ECU: a480 enable | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a482_lvBridgeEFuseCurrent` | page 482 | VCBATT1 ECU: a482 lv bridge e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a482_lvBridgeEFuseVoltage` | page 482 | VCBATT1 ECU: a482 lv bridge e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCBATT1_a482_lvBridgeEFuseTemp` | page 482 | VCBATT1 ECU: a482 lv bridge e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCBATT1_a482_lvBridgeEFuseRemainingRetries` | page 482 | VCBATT1 ECU: a482 lv bridge e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCBATT1_a484_upstreamEFuseStuckOn` | page 484 | VCBATT1 ECU: a484 upstream e fuse stuck on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a484_upstreamEFuseVoltage` | page 484 | VCBATT1 ECU: a484 upstream e fuse voltage | 17\|6 | little-endian | unsigned | 1 | 0 | V | 0 to 63 |  | plausible |
| `VCBATT1_a484_vbusVoltage` | page 484 | VCBATT1 ECU: a484 vbus voltage | 24\|6 | little-endian | unsigned | 1 | 0 | V | 0 to 63 |  | plausible |
| `VCBATT1_a484_upstreamEFuseRatio` | page 484 | VCBATT1 ECU: a484 upstream e fuse ratio | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCBATT1_a485_upstreamEfuseUnattemptedOn` | page 485 | VCBATT1 ECU: a485 upstream efuse unattempted on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_bridgeFailedArmingSetup` | page 486 | VCBATT1 ECU: a486 bridge failed arming setup | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_bridgeFailedSyncCheck` | page 486 | VCBATT1 ECU: a486 bridge failed sync check | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_localBridgeOutputOn` | page 486 | VCBATT1 ECU: a486 local bridge output on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_localBridgeSyncArmed` | page 486 | VCBATT1 ECU: a486 local bridge sync armed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_localBridgeDinState` | page 486 | VCBATT1 ECU: a486 local bridge din state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeOutputOn` | page 486 | VCBATT1 ECU: a486 remote bridge output on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeOutputOnValid` | page 486 | VCBATT1 ECU: a486 remote bridge output on valid | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeSyncArmed` | page 486 | VCBATT1 ECU: a486 remote bridge sync armed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeSyncArmedValid` | page 486 | VCBATT1 ECU: a486 remote bridge sync armed valid | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeDinState` | page 486 | VCBATT1 ECU: a486 remote bridge din state | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_remoteBridgeDinStateValid` | page 486 | VCBATT1 ECU: a486 remote bridge din state valid | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a493_minBrickSocId` | page 493 | VCBATT1 ECU: a493 min brick soc id | 16\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | layout-only |
| `VCBATT1_a493_minBrickSocByOcvMax` | page 493 | VCBATT1 ECU: a493 min brick soc by ocv max | 24\|8 | little-endian | unsigned | 0.5 | 0 | PCT | 0 to 127.5 |  | plausible |
| `VCBATT1_a493_maxBrickSocId` | page 493 | VCBATT1 ECU: a493 max brick soc id | 32\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | layout-only |
| `VCBATT1_a493_maxBrickSocByOcvMin` | page 493 | VCBATT1 ECU: a493 max brick soc by ocv min | 40\|8 | little-endian | unsigned | 0.5 | 0 | PCT | 0 to 127.5 |  | plausible |
| `VCBATT1_a493_maxBrickSoc` | page 493 | VCBATT1 ECU: a493 max brick soc | 48\|7 | little-endian | unsigned | 1 | 0 | PCT | 0 to 127 |  | plausible |
| `VCBATT1_a493_avgBrickSoc` | page 493 | VCBATT1 ECU: a493 avg brick soc | 56\|7 | little-endian | unsigned | 1 | 0 | PCT | 0 to 127 |  | plausible |
| `VCBATT1_a495_SoCUnrecoverable` | page 495 | VCBATT1 ECU: a495 so c unrecoverable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_SocTooLow` | page 495 | VCBATT1 ECU: a495 soc too low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_retryExpended` | page 495 | VCBATT1 ECU: a495 retry expended | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_LVBMSMIA` | page 495 | VCBATT1 ECU: a495 LVBMSMIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_reverseBatteryEFuseFault` | page 495 | VCBATT1 ECU: a495 reverse battery e fuse fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_DCDCOff` | page 495 | VCBATT1 ECU: a495 DCDC off | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_HVOff` | page 495 | VCBATT1 ECU: a495 HV off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_externalInteraction` | page 495 | VCBATT1 ECU: a495 external interaction | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_serviceMode` | page 495 | Signal reported by VCBATT1 ECU | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_frunkOpen` | page 495 | VCBATT1 ECU: a495 frunk open | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_externalPowerSupply` | page 495 | VCBATT1 ECU: a495 external power supply | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_reverseBatteryEFuseFault` | page 496 | VCBATT1 ECU: a496 reverse battery e fuse fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_vehicleLoadShedActive` | page 496 | VCBATT1 ECU: a496 vehicle load shed active | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_MOSState` | page 496 | VCBATT1 ECU: a496 MOS state; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCBATT1_a496_serviceMode` | page 496 | Signal reported by VCBATT1 ECU | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_frunkOpen` | page 496 | VCBATT1 ECU: a496 frunk open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_PCS_MIA` | page 496 | VCBATT1 ECU: a496 PCS MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_NotEnoughPowerForSupport` | page 496 | VCBATT1 ECU: a496 not enough power for support | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_bmsState` | page 496 | VCBATT1 ECU: a496 bms state; raw 9 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a497_serviceMode` | page 497 | Signal reported by VCBATT1 ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a497_FactoryMode` | page 497 | VCBATT1 ECU: a497 factory mode | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a497_SOC` | page 497 | VCBATT1 ECU: a497 SOC | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCBATT1_a497_PackCurrent` | page 497 | VCBATT1 ECU: a497 pack current | 32\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCBATT1_a497_SumCellVoltage` | page 497 | VCBATT1 ECU: a497 sum cell voltage | 48\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a497_frunkOpen` | page 497 | VCBATT1 ECU: a497 frunk open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a500_channel` | page 500 | VCBATT1 ECU: a500 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a500_mismatchedState` | page 500 | VCBATT1 ECU: a500 mismatched state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCBATT1_a503_brickVoltageMin` | page 503 | VCBATT1 ECU: a503 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a503_brickVoltageMax` | page 503 | VCBATT1 ECU: a503 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCBATT1_a503_packCurrent` | page 503 | VCBATT1 ECU: a503 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCBATT1_a503_socMax` | page 503 | VCBATT1 ECU: a503 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCBATT1_a503_brickId` | page 503 | VCBATT1 ECU: a503 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCBATT1_a509_channel` | page 509 | VCBATT1 ECU: a509 channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `BRAKE_MOTOR_ECU_1`<br>2 = `LOADSHED`<br>3 = `AUTOPILOT_1`<br>4 = `BRIDGE`<br>5 = `EPAS1`<br>6 = `LEFT_CONTROLLER` | plausible |
| `VCBATT1_a509_state` | page 509 | VCBATT1 ECU: a509 state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCBATT1_a509_expectedState` | page 509 | VCBATT1 ECU: a509 expected state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCBATT1_a509_hardwareLockout` | page 509 | VCBATT1 ECU: a509 hardware lockout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a509_unlocksRemaining` | page 509 | VCBATT1 ECU: a509 unlocks remaining | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a510_sumCellVoltage` | page 510 | VCBATT1 ECU: a510 sum cell voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a510_packVoltage` | page 510 | VCBATT1 ECU: a510 pack voltage | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a510_targetPCSVoltage` | page 510 | VCBATT1 ECU: a510 target PCS voltage | 32\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a510_serviceMode` | page 510 | Signal reported by VCBATT1 ECU | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a510_frunkOpen` | page 510 | VCBATT1 ECU: a510 frunk open | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a512_packVoltageIntervalMin` | page 512 | VCBATT1 ECU: a512 pack voltage interval min | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a512_packVoltageIntervalMax` | page 512 | VCBATT1 ECU: a512 pack voltage interval max | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a512_packTemperature` | page 512 | VCBATT1 ECU: a512 pack temperature | 32\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 215 |  | plausible |
| `VCBATT1_a512_sumCellVoltage` | page 512 | VCBATT1 ECU: a512 sum cell voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a512_overcurrentDirection` | page 512 | VCBATT1 ECU: a512 overcurrent direction | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INCONCLUSIVE`<br>1 = `CHARGE`<br>2 = `DISCHARGE` | plausible |
| `VCBATT1_a512_serviceMode` | page 512 | Signal reported by VCBATT1 ECU | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a512_frunkOpen` | page 512 | VCBATT1 ECU: a512 frunk open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a512_vehiclePowerState` | page 512 | VCBATT1 ECU: a512 vehicle power state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a513_packCurrent` | page 513 | VCBATT1 ECU: a513 pack current | 16\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCBATT1_a513_packTemperature` | page 513 | VCBATT1 ECU: a513 pack temperature | 32\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 215 |  | plausible |
| `VCBATT1_a513_packVoltage` | page 513 | VCBATT1 ECU: a513 pack voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a513_packSOC` | page 513 | VCBATT1 ECU: a513 pack SOC | 48\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCBATT1_a513_serviceMode` | page 513 | Signal reported by VCBATT1 ECU | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a513_frunkOpen` | page 513 | VCBATT1 ECU: a513 frunk open | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a513_vehiclePowerState` | page 513 | VCBATT1 ECU: a513 vehicle power state | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a514_cell1Voltage` | page 514 | VCBATT1 ECU: a514 cell1 voltage | 16\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a514_cell2Voltage` | page 514 | VCBATT1 ECU: a514 cell2 voltage | 23\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a514_cell3Voltage` | page 514 | VCBATT1 ECU: a514 cell3 voltage | 30\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a514_cell4Voltage` | page 514 | VCBATT1 ECU: a514 cell4 voltage | 37\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a514_packVoltage` | page 514 | VCBATT1 ECU: a514 pack voltage | 44\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a514_packSOC` | page 514 | VCBATT1 ECU: a514 pack SOC | 52\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `VCBATT1_a514_serviceMode` | page 514 | Signal reported by VCBATT1 ECU | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a514_frunkOpen` | page 514 | VCBATT1 ECU: a514 frunk open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a514_vehiclePowerState` | page 514 | VCBATT1 ECU: a514 vehicle power state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a515_cell1Voltage` | page 515 | VCBATT1 ECU: a515 cell1 voltage | 16\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a515_cell2Voltage` | page 515 | VCBATT1 ECU: a515 cell2 voltage | 23\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a515_cell3Voltage` | page 515 | VCBATT1 ECU: a515 cell3 voltage | 30\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a515_cell4Voltage` | page 515 | VCBATT1 ECU: a515 cell4 voltage | 37\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCBATT1_a515_packVoltage` | page 515 | VCBATT1 ECU: a515 pack voltage | 44\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a515_packSOC` | page 515 | VCBATT1 ECU: a515 pack SOC | 52\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `VCBATT1_a515_serviceMode` | page 515 | Signal reported by VCBATT1 ECU | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a515_frunkOpen` | page 515 | VCBATT1 ECU: a515 frunk open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a515_vehiclePowerState` | page 515 | VCBATT1 ECU: a515 vehicle power state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a518_packVoltage` | page 518 | VCBATT1 ECU: a518 pack voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a518_IBSVoltage` | page 518 | VCBATT1 ECU: a518 IBS voltage | 24\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCBATT1_a518_targetPCSVoltage` | page 518 | VCBATT1 ECU: a518 target PCS voltage | 33\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a518_outputVoltageAtPCS` | page 518 | VCBATT1 ECU: a518 output voltage at PCS | 41\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a518_packSOC` | page 518 | VCBATT1 ECU: a518 pack SOC | 49\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCBATT1_a518_serviceMode` | page 518 | Signal reported by VCBATT1 ECU | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a518_frunkOpen` | page 518 | VCBATT1 ECU: a518 frunk open | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a518_vehiclePowerState` | page 518 | VCBATT1 ECU: a518 vehicle power state | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a521_vcleftEFuseCurrent` | page 521 | VCBATT1 ECU: a521 vcleft e fuse current | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCBATT1_a521_vcleftEFuseTemp` | page 521 | VCBATT1 ECU: a521 vcleft e fuse temp | 32\|8 | little-endian | unsigned | 0.75 | 0 | degC | 0 to 191.25 |  | plausible |
| `VCBATT1_a521_ambientTemp` | page 521 | VCBATT1 ECU: a521 ambient temp | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCBATT1_a521_serviceMode` | page 521 | Signal reported by VCBATT1 ECU | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a521_frunkOpen` | page 521 | VCBATT1 ECU: a521 frunk open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a523_channel` | page 523 | VCBATT1 ECU: a523 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a523_control2Byte1` | page 523 | VCBATT1 ECU: a523 control2 byte1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a523_control2Byte2` | page 523 | VCBATT1 ECU: a523 control2 byte2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a523_control2Byte3` | page 523 | VCBATT1 ECU: a523 control2 byte3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a523_control3Byte2` | page 523 | VCBATT1 ECU: a523 control3 byte2 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a523_control3Byte3` | page 523 | VCBATT1 ECU: a523 control3 byte3 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT1_a525_GTW_twelveVBatteryType` | page 525 | VCBATT1 ECU: a525 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCBATT1_a525_newLVBatteryType` | page 525 | VCBATT1 ECU: a525 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a525_initialLVBatteryType` | page 525 | VCBATT1 ECU: a525 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a525_serviceMode` | page 525 | Signal reported by VCBATT1 ECU | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a525_factoryGated` | page 525 | VCBATT1 ECU: a525 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a525_frunkOpen` | page 525 | VCBATT1 ECU: a525 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a527_cell1Voltage` | page 527 | VCBATT1 ECU: a527 cell1 voltage | 16\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a527_cell2Voltage` | page 527 | VCBATT1 ECU: a527 cell2 voltage | 26\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a527_cell3Voltage` | page 527 | VCBATT1 ECU: a527 cell3 voltage | 36\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a527_cell4Voltage` | page 527 | VCBATT1 ECU: a527 cell4 voltage | 46\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a527_serviceMode` | page 527 | Signal reported by VCBATT1 ECU | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a527_frunkOpen` | page 527 | VCBATT1 ECU: a527 frunk open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_ECPAStateSNA` | page 528 | VCBATT1 ECU: a528 ECPA state SNA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_ECPAFrameTimeout` | page 528 | VCBATT1 ECU: a528 ECPA frame timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_currentSenseFaulted` | page 528 | VCBATT1 ECU: a528 current sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_serviceMode` | page 528 | Signal reported by VCBATT1 ECU | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_frunkOpen` | page 528 | VCBATT1 ECU: a528 frunk open | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a533_temperature` | page 533 | VCBATT1 ECU: a533 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCBATT1_a541_PackTemperature` | page 541 | VCBATT1 ECU: a541 pack temperature | 16\|9 | little-endian | unsigned | 0.5 | -50 | degC | -50 to 205.5 |  | plausible |
| `VCBATT1_a541_ChargeCurrentLimit` | page 541 | VCBATT1 ECU: a541 charge current limit | 25\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCBATT1_a541_PeakCurrent` | page 541 | VCBATT1 ECU: a541 peak current | 35\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCBATT1_a541_AverageCurrent` | page 541 | VCBATT1 ECU: a541 average current | 45\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCBATT1_a541_SOC` | page 541 | VCBATT1 ECU: a541 SOC | 56\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCBATT1_a544_serviceMode` | page 544 | Signal reported by VCBATT1 ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a544_frunkOpen` | page 544 | VCBATT1 ECU: a544 frunk open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a544_LVBMSSOC` | page 544 | VCBATT1 ECU: a544 LVBMSSOC | 18\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCBATT1_a545_GTW_twelveVBatteryType` | page 545 | VCBATT1 ECU: a545 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCBATT1_a545_newLVBatteryType` | page 545 | VCBATT1 ECU: a545 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a545_serviceMode` | page 545 | Signal reported by VCBATT1 ECU | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a545_factoryGated` | page 545 | VCBATT1 ECU: a545 factory gated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a545_frunkOpen` | page 545 | VCBATT1 ECU: a545 frunk open | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_vehiclePowerState` | page 548 | VCBATT1 ECU: a548 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a548_notEnoughPowerForSupport` | page 548 | VCBATT1 ECU: a548 not enough power for support | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_HVBlockingMismatch` | page 548 | VCBATT1 ECU: a548 HV blocking mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_LVBatteryCannotSupportVehicle` | page 548 | VCBATT1 ECU: a548 LV battery cannot support vehicle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_DI_gear` | page 548 | VCBATT1 ECU: a548 DI gear; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCBATT1_a548_backstopBucketCount` | page 548 | VCBATT1 ECU: a548 backstop bucket count | 24\|5 | little-endian | unsigned | 0.035 | 0 | Ah | 0 to 1.085 |  | plausible |
| `VCBATT1_a548_hvState` | page 548 | VCBATT1 ECU: a548 hv state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCBATT1_a548_BMS_MIA` | page 548 | VCBATT1 ECU: a548 BMS MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_PCS_MIA` | page 548 | VCBATT1 ECU: a548 PCS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_ampHourBucketCount` | page 548 | VCBATT1 ECU: a548 amp hour bucket count | 34\|6 | little-endian | unsigned | 0.01 | 0 | Ah | 0 to 0.63 |  | plausible |
| `VCBATT1_a548_LVBMSSOC` | page 548 | VCBATT1 ECU: a548 LVBMSSOC | 40\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCBATT1_a548_serviceMode` | page 548 | Signal reported by VCBATT1 ECU | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_frunkOpen` | page 548 | VCBATT1 ECU: a548 frunk open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_PCSTargetVoltage` | page 548 | VCBATT1 ECU: a548 PCS target voltage | 48\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a548_ampHourBucketFilled` | page 548 | VCBATT1 ECU: a548 amp hour bucket filled | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_HVNotConfirmedUpTrigger` | page 548 | VCBATT1 ECU: a548 HV not confirmed up trigger | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_PCSNotMeetingTargetTrigger` | page 548 | VCBATT1 ECU: a548 PCS not meeting target trigger | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_PCSMIATrigger` | page 548 | VCBATT1 ECU: a548 PCSMIA trigger | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_PCSSaturatedTrigger` | page 548 | VCBATT1 ECU: a548 PCS saturated trigger | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_backstopHit` | page 548 | VCBATT1 ECU: a548 backstop hit | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a555_cell1Voltage` | page 555 | VCBATT1 ECU: a555 cell1 voltage | 16\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a555_cell2Voltage` | page 555 | VCBATT1 ECU: a555 cell2 voltage | 26\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a555_cell3Voltage` | page 555 | VCBATT1 ECU: a555 cell3 voltage | 36\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a555_cell4Voltage` | page 555 | VCBATT1 ECU: a555 cell4 voltage | 46\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCBATT1_a559_SOC` | page 559 | VCBATT1 ECU: a559 SOC | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCBATT1_a559_PackCurrent` | page 559 | VCBATT1 ECU: a559 pack current | 24\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCBATT1_a559_vehiclePowerState` | page 559 | VCBATT1 ECU: a559 vehicle power state | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a559_batterySMState` | page 559 | VCBATT1 ECU: a559 battery SM state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a559_bmsState` | page 559 | VCBATT1 ECU: a559 bms state; raw 9 = signal not available (SNA) | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCBATT1_a559_dcdcLVSupportStatus` | page 559 | VCBATT1 ECU: a559 dcdc LV support status | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCBATT1_a559_factoryMode` | page 559 | VCBATT1 ECU: a559 factory mode | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_serviceMode` | page 559 | Signal reported by VCBATT1 ECU | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_transportMode` | page 559 | VCBATT1 ECU: a559 transport mode | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_notEnoughPowerForSupport` | page 559 | VCBATT1 ECU: a559 not enough power for support | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_crashDetected` | page 559 | VCBATT1 ECU: a559 crash detected | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_BMS_MIA` | page 559 | VCBATT1 ECU: a559 BMS MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_PCS_MIA` | page 559 | VCBATT1 ECU: a559 PCS MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_HVBlockingMismatch` | page 559 | VCBATT1 ECU: a559 HV blocking mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_HV_UP` | page 559 | VCBATT1 ECU: a559 HV UP | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_pcsEFuseStable` | page 559 | VCBATT1 ECU: a559 pcs e fuse stable | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_vcrightEFuseStable` | page 559 | VCBATT1 ECU: a559 vcright e fuse stable | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_contactorEFuseStable` | page 559 | VCBATT1 ECU: a559 contactor e fuse stable | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_hvcEFuseStable` | page 559 | VCBATT1 ECU: a559 hvc e fuse stable | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_frunkOpen` | page 559 | VCBATT1 ECU: a559 frunk open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a561_efuseTemperature` | page 561 | VCBATT1 ECU: a561 efuse temperature | 16\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCBATT1_a561_packTemperature` | page 561 | VCBATT1 ECU: a561 pack temperature | 21\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCBATT1_a561_ambientTemperature` | page 561 | VCBATT1 ECU: a561 ambient temperature | 26\|6 | little-endian | unsigned | 4 | 0 | C | 0 to 252 |  | plausible |
| `VCBATT1_a561_cell1Voltage` | page 561 | VCBATT1 ECU: a561 cell1 voltage | 32\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a561_cell2Voltage` | page 561 | VCBATT1 ECU: a561 cell2 voltage | 39\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a561_cell3Voltage` | page 561 | VCBATT1 ECU: a561 cell3 voltage | 46\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a561_cell4Voltage` | page 561 | VCBATT1 ECU: a561 cell4 voltage | 53\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a561_factoryMode` | page 561 | VCBATT1 ECU: a561 factory mode | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a561_serviceMode` | page 561 | Signal reported by VCBATT1 ECU | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a561_frunkOpen` | page 561 | VCBATT1 ECU: a561 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a562_efuseTemperature` | page 562 | VCBATT1 ECU: a562 efuse temperature | 16\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCBATT1_a562_packTemperature` | page 562 | VCBATT1 ECU: a562 pack temperature | 21\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCBATT1_a562_ambientTemperature` | page 562 | VCBATT1 ECU: a562 ambient temperature | 26\|6 | little-endian | unsigned | 4 | 0 | C | 0 to 252 |  | plausible |
| `VCBATT1_a562_cell1Voltage` | page 562 | VCBATT1 ECU: a562 cell1 voltage | 32\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a562_cell2Voltage` | page 562 | VCBATT1 ECU: a562 cell2 voltage | 39\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a562_cell3Voltage` | page 562 | VCBATT1 ECU: a562 cell3 voltage | 46\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a562_cell4Voltage` | page 562 | VCBATT1 ECU: a562 cell4 voltage | 53\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCBATT1_a562_factoryMode` | page 562 | VCBATT1 ECU: a562 factory mode | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a562_serviceMode` | page 562 | Signal reported by VCBATT1 ECU | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a562_frunkOpen` | page 562 | VCBATT1 ECU: a562 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a580_rightHeadlightCurrent` | page 580 | VCBATT1 ECU: a580 right headlight current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCBATT1_a582_batterySMState` | page 582 | VCBATT1 ECU: a582 battery SM state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a582_PCSCurrent` | page 582 | VCBATT1 ECU: a582 PCS current | 24\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCBATT1_a582_LVBusVoltage` | page 582 | VCBATT1 ECU: a582 LV bus voltage | 32\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCBATT1_a582_LVBusVoltageSource` | page 582 | VCBATT1 ECU: a582 LV bus voltage source | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `IBS`<br>2 = `VBAT_MONITOR`<br>3 = `LVBMS` | plausible |
| `VCBATT1_a582_batteryType` | page 582 | VCBATT1 ECU: a582 battery type | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a582_inFactoryMode` | page 582 | VCBATT1 ECU: a582 in factory mode | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a582_frunkOpen` | page 582 | VCBATT1 ECU: a582 frunk open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_daysSincePreviousTest` | page 585 | VCBATT1 ECU: a585 days since previous test; raw 16383 = signal not available (SNA) | 16\|14 | little-endian | unsigned | 0.1 | -0.1 | days | -0.1 to 1638.1 | 0 = `BELOW_RANGE`<br>16382 = `ABOVE_RANGE`<br>16383 = `SNA` | plausible |
| `VCBATT1_a585_testUrgency` | page 585 | VCBATT1 ECU: a585 test urgency | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `REFRESH_DESIRED`<br>2 = `REFRESH_STALLED`<br>3 = `RESULTS_EXPIRED`<br>4 = `NO_RESULTS_FOR_NEW_PACK`<br>5 = `FAULTED_LOSS_OF_TIME` | plausible |
| `VCBATT1_a585_hoursSinceUserPresenceUpdate` | page 585 | VCBATT1 ECU: a585 hours since user presence update; raw 4095 = signal not available (SNA) | 35\|12 | little-endian | unsigned | 0.1 | -0.1 | hours | -0.1 to 409.3 | 0 = `BELOW_RANGE`<br>4094 = `ABOVE_RANGE`<br>4095 = `SNA` | plausible |
| `VCBATT1_a585_userPresenceState` | page 585 | VCBATT1 ECU: a585 user presence state | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT`<br>3 = `TIMED_OUT` | plausible |
| `VCBATT1_a585_periodicTriggerActive` | page 585 | VCBATT1 ECU: a585 periodic trigger active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_developmentCar` | page 585 | VCBATT1 ECU: a585 development car | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_updateStarted` | page 585 | VCBATT1 ECU: a585 update started | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_factoryMode` | page 585 | VCBATT1 ECU: a585 factory mode | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_serviceMode` | page 585 | Signal reported by VCBATT1 ECU | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_factoryMode` | page 587 | VCBATT1 ECU: a587 factory mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_serviceMode` | page 587 | Signal reported by VCBATT1 ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_transportMode` | page 587 | VCBATT1 ECU: a587 transport mode | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_frunkOpen` | page 587 | VCBATT1 ECU: a587 frunk open | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_LVBMS_packCurrent_valid` | page 587 | VCBATT1 ECU: a587 LVBMS pack current valid | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_vehiclePowerState` | page 587 | VCBATT1 ECU: a587 vehicle power state | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a587_batterySMState` | page 587 | VCBATT1 ECU: a587 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a587_LVBMS_packCurrent` | page 587 | VCBATT1 ECU: a587 LVBMS pack current | 28\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCBATT1_a587_IBSCurrent` | page 587 | VCBATT1 ECU: a587 IBS current | 40\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a592_vcleftCutoffEFuseCurveType` | page 592 | VCBATT1 ECU: a592 vcleft cutoff e fuse curve type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STATIC_EFUSE_CURVE`<br>1 = `DYNAMIC_EFUSE_CURVE` | plausible |
| `VCBATT1_a592_vcleftCutoffCurveOffsetChannel` | page 592 | VCBATT1 ECU: a592 vcleft cutoff curve offset channel | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCBATT1_a592_vcleftCutoffATerm` | page 592 | VCBATT1 ECU: a592 vcleft cutoff a term; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 50 | 0 | - | 0 to 3276700 | 65535 = `SNA` | plausible |
| `VCBATT1_a592_vcleftCutoffBTerm` | page 592 | VCBATT1 ECU: a592 vcleft cutoff b term; raw 128 = signal not available (SNA) | 40\|8 | little-endian | signed | 1 | -78 | - | -206 to 49 | -128 = `SNA` | plausible |
| `VCBATT1_a592_vcleftCutoffCTerm` | page 592 | VCBATT1 ECU: a592 vcleft cutoff c term; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 50 | 0 | - | -1638400 to 1638350 | -32768 = `SNA` | plausible |
| `VCBATT1_a593_vcleftCutoffEFuseFastBlowType` | page 593 | VCBATT1 ECU: a593 vcleft cutoff e fuse fast blow type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TIMING`<br>1 = `DEBOUNCE` | plausible |
| `VCBATT1_a593_vcleftCutoffCurrentThreshold` | page 593 | VCBATT1 ECU: a593 vcleft cutoff current threshold | 17\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCBATT1_a593_vcleftCutoffTimingThresholdMs` | page 593 | VCBATT1 ECU: a593 vcleft cutoff timing threshold ms | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT1_a593_vcleftCutoffMaxCount` | page 593 | VCBATT1 ECU: a593 vcleft cutoff max count | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCBATT1_a597_EPBReleased` | page 597 | VCBATT1 ECU: a597 EPB released | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_LVNotBeingSupported` | page 597 | VCBATT1 ECU: a597 LV not being supported | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_LVBMB_currentInvalid` | page 597 | VCBATT1 ECU: a597 LVBMB current invalid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_IBSCurrentInvalid` | page 597 | VCBATT1 ECU: a597 IBS current invalid | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_LVBMB_eFuseOpen` | page 597 | VCBATT1 ECU: a597 LVBMB e fuse open | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_vehicleIsUpdating` | page 597 | VCBATT1 ECU: a597 vehicle is updating | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_LVBusVoltageNotControllable` | page 597 | VCBATT1 ECU: a597 LV bus voltage not controllable | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_lostLVBusControl` | page 597 | VCBATT1 ECU: a597 lost LV bus control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_externalPowerSupply` | page 597 | VCBATT1 ECU: a597 external power supply | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_lvBatteryLowCharge` | page 597 | VCBATT1 ECU: a597 lv battery low charge | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_closedDChgResult` | page 597 | VCBATT1 ECU: a597 closed d chg result | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCBATT1_a597_closedChgResult` | page 597 | VCBATT1 ECU: a597 closed chg result | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCBATT1_a597_selfTestState` | page 597 | VCBATT1 ECU: a597 self test state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INACTIVE`<br>1 = `CLOSED_DISCHARGE`<br>2 = `CLOSED_CHARGE` | plausible |
| `VCBATT1_a598_LVBMS_packCurrent` | page 598 | VCBATT1 ECU: a598 LVBMS pack current | 16\|12 | little-endian | unsigned | 0.0025 | 0 | A | 0 to 10.2375 |  | plausible |
| `VCBATT1_a598_IBSCurrent` | page 598 | VCBATT1 ECU: a598 IBS current | 28\|12 | little-endian | signed | 0.0025 | 0 | A | -5.12 to 5.1175 |  | plausible |
| `VCBATT1_a598_closedChgIBSCurrentCount` | page 598 | VCBATT1 ECU: a598 closed chg IBS current count | 40\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `VCBATT1_a598_closedChgPackCurrentCount` | page 598 | VCBATT1 ECU: a598 closed chg pack current count | 44\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `VCBATT1_a598_closedDChgIBSCurrentCount` | page 598 | VCBATT1 ECU: a598 closed d chg IBS current count | 48\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `VCBATT1_a598_closedDChgPackCurrentCount` | page 598 | VCBATT1 ECU: a598 closed d chg pack current count | 52\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `VCBATT1_a598_closedDChgResult` | page 598 | VCBATT1 ECU: a598 closed d chg result | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCBATT1_a598_closedChgResult` | page 598 | VCBATT1 ECU: a598 closed chg result | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `FAILED`<br>2 = `PASSED` | plausible |
| `VCBATT1_a599_GTW_twelveVBatteryType` | page 599 | VCBATT1 ECU: a599 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCBATT1_a599_newLVBatteryType` | page 599 | VCBATT1 ECU: a599 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a599_initialLVBatteryType` | page 599 | VCBATT1 ECU: a599 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCBATT1_a599_serviceMode` | page 599 | Signal reported by VCBATT1 ECU | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a599_factoryGated` | page 599 | VCBATT1 ECU: a599 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a599_frunkOpen` | page 599 | VCBATT1 ECU: a599 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_factoryMode` | page 600 | VCBATT1 ECU: a600 factory mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_serviceMode` | page 600 | Signal reported by VCBATT1 ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_transportMode` | page 600 | VCBATT1 ECU: a600 transport mode | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_frunkOpen` | page 600 | VCBATT1 ECU: a600 frunk open | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_vehiclePowerState` | page 600 | VCBATT1 ECU: a600 vehicle power state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCBATT1_a600_batterySMState` | page 600 | VCBATT1 ECU: a600 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCBATT1_a600_LVBMS_packCurrent` | page 600 | VCBATT1 ECU: a600 LVBMS pack current | 28\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCBATT1_a600_IBSCurrent` | page 600 | VCBATT1 ECU: a600 IBS current | 40\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCBATT1_a600_version` | page 600 | VCBATT1 ECU: a600 version | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCBATT1_a601_subUsageId` | page 601 | VCBATT1 ECU: a601 sub usage id; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65534 | 65535 = `SNA` | plausible |
| `VCBATT1_a608_deltaV` | page 608 | VCBATT1 ECU: a608 delta v | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 6.5535 |  | plausible |
| `VCBATT1_a608_bleedFetFailureBrickId` | page 608 | VCBATT1 ECU: a608 bleed fet failure brick id; raw 31 = signal not available (SNA) | 32\|5 | little-endian | unsigned | 1 | 1 |  | 1 to 31 | 31 = `SNA` | plausible |
| `VCBATT1_a608_retryCount` | page 608 | VCBATT1 ECU: a608 retry count | 40\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `VCBATT1_a608_setFromNvm` | page 608 | VCBATT1 ECU: a608 set from nvm | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCBATT1_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals), page 91 (2 signals), page 96 (1 signals), page 98 (2 signals), page 106 (10 signals), page 108 (4 signals), page 120 (9 signals), page 124 (2 signals), page 125 (3 signals), page 126 (4 signals), page 127 (4 signals), page 129 (3 signals), page 130 (4 signals), page 131 (2 signals), page 132 (3 signals), page 133 (2 signals), page 144 (2 signals), page 164 (1 signals), page 165 (1 signals), page 180 (18 signals), page 182 (26 signals), page 188 (10 signals), page 191 (21 signals), page 196 (10 signals), page 204 (4 signals), page 205 (4 signals), page 212 (1 signals), page 213 (3 signals), page 216 (6 signals), page 219 (3 signals), page 220 (7 signals), page 221 (4 signals), page 223 (5 signals), page 224 (8 signals), page 229 (6 signals), page 235 (3 signals), page 243 (3 signals), page 244 (2 signals), page 245 (3 signals), page 253 (9 signals), page 259 (5 signals), page 260 (17 signals), page 297 (2 signals), page 359 (12 signals), page 363 (5 signals), page 370 (6 signals), page 371 (7 signals), page 372 (2 signals), page 387 (5 signals), page 388 (5 signals), page 392 (2 signals), page 401 (4 signals), page 402 (9 signals), page 404 (3 signals), page 407 (10 signals), page 414 (6 signals), page 415 (1 signals), page 416 (5 signals), page 417 (5 signals), page 418 (5 signals), page 419 (5 signals), page 421 (6 signals), page 423 (5 signals), page 424 (5 signals), page 431 (3 signals), page 432 (2 signals), page 433 (5 signals), page 434 (5 signals), page 436 (3 signals), page 437 (2 signals), page 438 (2 signals), page 439 (2 signals), page 441 (2 signals), page 446 (8 signals), page 462 (25 signals), page 475 (28 signals), page 476 (19 signals), page 477 (8 signals), page 478 (23 signals), page 479 (8 signals), page 480 (25 signals), page 482 (4 signals), page 484 (4 signals), page 485 (1 signals), page 486 (11 signals), page 493 (6 signals), page 495 (11 signals), page 496 (8 signals), page 497 (6 signals), page 500 (2 signals), page 503 (5 signals), page 509 (5 signals), page 510 (5 signals), page 512 (8 signals), page 513 (7 signals), page 514 (9 signals), page 515 (9 signals), page 518 (8 signals), page 521 (5 signals), page 523 (6 signals), page 525 (6 signals), page 527 (6 signals), page 528 (5 signals), page 533 (1 signals), page 541 (5 signals), page 544 (3 signals), page 545 (5 signals), page 548 (20 signals), page 555 (4 signals), page 559 (20 signals), page 561 (10 signals), page 562 (10 signals), page 580 (1 signals), page 582 (7 signals), page 585 (9 signals), page 587 (9 signals), page 592 (5 signals), page 593 (4 signals), page 597 (13 signals), page 598 (8 signals), page 599 (6 signals), page 600 (9 signals), page 601 (1 signals), page 608 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
