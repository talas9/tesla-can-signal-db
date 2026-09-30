---
layout: default
title: "TRCM_alertLog (0x512) — TRCM ECU, Tesla Model 3 2026.26.6.5 CH CAN"
description: "TRCM ECU message: alert log. Tesla Model 3 CAN bus message TRCM_alertLog (0x512) of TRCM ECU, firmware 2026.26.6.5, 657 signals (TRCM_alertID, TRCM_alertState, TRCM_a015_NVMMMemOverflow, TRCM_a015_NVMMFilesystemError and 653 more). Bit layout, scaling, units and value tables."
---

# TRCM_alertLog (0x512) — TRCM ECU, Tesla Model 3 2026.26.6.5 CH CAN

TRCM ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 657 signals of TRCM_alertLog as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TRCM_alertLog` |
| CAN id | 0x512 (1298) |
| ECU | [TRCM ECU](../../trcm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TRCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 657 |

## Signals of TRCM_alertLog

Tesla Model 3 CAN bus signals in `TRCM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TRCM_alertID` | selector | TRCM ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_airbagsDisabled`<br>2 = `a002_systemDisabled`<br>3 = `a003_SWAssertion`<br>4 = `a004_internalFailure`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>7 = `a007_chassisChecksumError`<br>8 = `a008_chassisCounterError`<br>9 = `a009_partyChecksumError`<br>10 = `a010_partyCounterError`<br>11 = `a011_edrDataLocked`<br>12 = `a012_asm5TemperatureOutsideSignalRange`<br>13 = `a013_AlertManagerFault`<br>14 = `a014_asm3TemperatureOutsideSignalRange`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_asm5TemperatureOutsideOperatingRange`<br>18 = `a018_asm3TemperatureOutsideOperatingRange`<br>19 = `a019_Task500usError`<br>20 = `a020_asm3ComStatusError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>23 = `a023_asm3ArsStatusXError`<br>24 = `a024_asm3AccStatusError`<br>25 = `a025_CHCANBusFaults`<br>26 = `a026_airbagAsicDiagnosticFault`<br>27 = `a027_airbagAsicDeploymentDiagnosticFault`<br>28 = `a028_chassisLengthError`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>32 = `a032_ScrollCreated`<br>33 = `a033_HercLogCreated`<br>34 = `a034_apClipTrigger`<br>35 = `a035_hvDisconnectCommanded`<br>36 = `a036_crashDetected`<br>37 = `a037_nearDeploy`<br>38 = `a038_ens1Degraded`<br>39 = `a039_ens2Degraded`<br>40 = `a040_task500usOverrunDebug`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>47 = `a047_vinNotLearned`<br>48 = `a048_vinMismatch`<br>49 = `a049_nvmDebugInfo`<br>50 = `a050_partyLengthError`<br>51 = `a051_systemSelfTestTimeout`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>65 = `a065_vSafingFetUnderVoltage`<br>66 = `a066_leftPowerIssue`<br>67 = `a067_rightPowerIssue`<br>68 = `a068_vBusCUnderVoltage`<br>69 = `a069_swAppBoot`<br>70 = `a070_asm3StatusError`<br>71 = `a071_asm3DeviceFaulted`<br>72 = `a072_ais2120StatusError`<br>73 = `a073_ais2120DeviceFaulted`<br>74 = `a074_ais2120SelfTestXPositiveFailed`<br>75 = `a075_ais2120SelfTestXNegativeFailed`<br>76 = `a076_ais2120SelfTestYPositiveFailed`<br>77 = `a077_ais2120SelfTestYNegativeFailed`<br>78 = `a078_imuSensorSignalMonitor`<br>81 = `a081_powerLossDetected`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_buckleStatusFrontLeftSignalNotOkay`<br>122 = `a122_buckleStatusFrontRightSignalNotOkay`<br>123 = `a123_buckleStatusRearLeftSignalNotOkay`<br>124 = `a124_buckleStatusRearRightSignalNotOkay`<br>125 = `a125_occupantClassificationSignalNotOkay`<br>126 = `a126_seatTrackPositionLeftSignalNotOkay`<br>127 = `a127_seatTrackPositionRightSignalNotOkay`<br>135 = `a135_asm5StatusError`<br>136 = `a136_asm5DeviceFaulted`<br>137 = `a137_ext1AsicSnoopTestFailed`<br>138 = `a138_ext2AsicSnoopTestFailed`<br>145 = `a145_frontCenterAccelReportedError`<br>146 = `a146_frontCenterAccelGeneralIssue`<br>147 = `a147_frontCenterAccelElectricalIssue`<br>148 = `a148_frontCenterAccelConfigError`<br>149 = `a149_frontCenterAccelSignalMonitor`<br>150 = `a150_frontLeftAccelReportedError`<br>151 = `a151_frontLeftAccelGeneralIssue`<br>152 = `a152_frontLeftAccelElectricalIssue`<br>153 = `a153_frontLeftAccelConfigError`<br>154 = `a154_frontLeftAccelSignalMonitor`<br>155 = `a155_frontLeftDoorPressureReportedError`<br>156 = `a156_frontLeftDoorPressureGeneralIssue`<br>157 = `a157_frontLeftDoorPressureElectricalIssue`<br>158 = `a158_frontLeftDoorPressureConfigError`<br>159 = `a159_frontLeftDoorPressureSignalMonitor`<br>160 = `a160_frontRightAccelReportedError`<br>161 = `a161_frontRightAccelGeneralIssue`<br>162 = `a162_frontRightAccelElectricalIssue`<br>163 = `a163_frontRightAccelConfigError`<br>164 = `a164_frontRightAccelSignalMonitor`<br>165 = `a165_frontRightDoorPressureReportedError`<br>166 = `a166_frontRightDoorPressureGeneralIssue`<br>167 = `a167_frontRightDoorPressureElectricalIssue`<br>168 = `a168_frontRightDoorPressureConfigError`<br>169 = `a169_frontRightDoorPressureSignalMonitor`<br>170 = `a170_leftBPillarAccelReportedError`<br>171 = `a171_leftBPillarAccelGeneralIssue`<br>172 = `a172_leftBPillarAccelElectricalIssue`<br>173 = `a173_leftBPillarAccelConfigError`<br>174 = `a174_leftBPillarAccelSignalMonitor`<br>175 = `a175_leftCPillarAccelReportedError`<br>176 = `a176_leftCPillarAccelGeneralIssue`<br>177 = `a177_leftCPillarAccelElectricalIssue`<br>178 = `a178_leftCPillarAccelConfigError`<br>179 = `a179_leftCPillarAccelSignalMonitor`<br>190 = `a190_rearLeftDoorPressureReportedError`<br>191 = `a191_rearLeftDoorPressureGeneralIssue`<br>192 = `a192_rearLeftDoorPressureElectricalIssue`<br>193 = `a193_rearLeftDoorPressureConfigError`<br>194 = `a194_rearLeftDoorPressureSignalMonitor`<br>195 = `a195_rearRightDoorPressureReportedError`<br>196 = `a196_rearRightDoorPressureGeneralIssue`<br>197 = `a197_rearRightDoorPressureElectricalIssue`<br>198 = `a198_rearRightDoorPressureConfigError`<br>199 = `a199_rearRightDoorPressureSignalMonitor`<br>200 = `a200_rightBPillarAccelReportedError`<br>201 = `a201_rightBPillarAccelGeneralIssue`<br>202 = `a202_rightBPillarAccelElectricalIssue`<br>203 = `a203_rightBPillarAccelConfigError`<br>204 = `a204_rightBPillarAccelSignalMonitor`<br>205 = `a205_rightCPillarAccelReportedError`<br>206 = `a206_rightCPillarAccelGeneralIssue`<br>207 = `a207_rightCPillarAccelElectricalIssue`<br>208 = `a208_rightCPillarAccelConfigError`<br>209 = `a209_rightCPillarAccelSignalMonitor`<br>272 = `a272_asm5ComStatusError`<br>273 = `a273_asm5ArsStatusXError`<br>274 = `a274_asm5ArsStatusZError`<br>275 = `a275_asm5AccStatusError`<br>276 = `a276_watchdogStatus`<br>278 = `a278_safingEngine0Armed`<br>279 = `a279_safingEngine1Armed`<br>280 = `a280_safingEngine2Armed`<br>281 = `a281_safingEngine3Armed`<br>282 = `a282_safingEngine4Armed`<br>283 = `a283_safingEngine5Armed`<br>284 = `a284_safingEngine6Armed`<br>285 = `a285_safingEngine7Armed`<br>286 = `a286_safingEngine8Armed`<br>287 = `a287_safingEngine9Armed`<br>288 = `a288_safingEngine10Armed`<br>289 = `a289_safingEngine11Armed`<br>290 = `a290_safingEngine12Armed`<br>291 = `a291_safingEngine13Armed`<br>292 = `a292_safingEngine14Armed`<br>293 = `a293_safingEngine15Armed`<br>294 = `a294_safingEngine16Armed`<br>295 = `a295_safingEngine17Armed`<br>296 = `a296_safingEngine18Armed`<br>297 = `a297_safingEngine19Armed`<br>298 = `a298_safingEngine20Armed`<br>299 = `a299_safingEngine21Armed`<br>300 = `a300_driverAirbagStage1Suppressed`<br>301 = `a301_passengerAirbagStage1Suppressed`<br>302 = `a302_driverAirbagStage2Suppressed`<br>303 = `a303_driverAirbagActiveVentSuppressed`<br>304 = `a304_passengerAirbagStage2Suppressed`<br>305 = `a305_passengerAirbagActiveVentSuppressed`<br>306 = `a306_inboardSeatAirbagSuppressed`<br>308 = `a308_kneeAirbagLeftSuppressed`<br>309 = `a309_kneeAirbagRightSuppressed`<br>310 = `a310_curtainAirbagLeftSuppressed`<br>311 = `a311_curtainAirbagRightSuppressed`<br>312 = `a312_seatbeltLoadLimiterFrontLeftSuppressed`<br>313 = `a313_seatbeltLoadLimiterFrontRightSuppressed`<br>314 = `a314_seatbeltShoulderPretensionerFrontLeftSuppressed`<br>315 = `a315_seatbeltShoulderPretensionerFrontRightSuppressed`<br>316 = `a316_seatbeltLapPretensionerFrontLeftSuppressed`<br>317 = `a317_seatbeltLapPretensionerFrontRightSuppressed`<br>318 = `a318_outboardSeatAirbagLeftSuppressed`<br>319 = `a319_outboardSeatAirbagRightSuppressed`<br>320 = `a320_hoodLifterLeftSuppressed`<br>321 = `a321_hoodLifterRightSuppressed`<br>322 = `a322_seatbeltShoulderPretensionerRearLeftSuppressed`<br>323 = `a323_seatbeltShoulderPretensionerRearRightSuppressed`<br>332 = `a332_driverAirbagStage1Deployed`<br>333 = `a333_passengerAirbagStage1Deployed`<br>334 = `a334_driverAirbagStage2Deployed`<br>335 = `a335_driverAirbagActiveVentDeployed`<br>336 = `a336_passengerAirbagStage2Deployed`<br>337 = `a337_passengerAirbagActiveVentDeployed`<br>338 = `a338_inboardSeatAirbagDeployed`<br>340 = `a340_kneeAirbagLeftDeployed`<br>341 = `a341_kneeAirbagRightDeployed`<br>342 = `a342_curtainAirbagLeftDeployed`<br>343 = `a343_curtainAirbagRightDeployed`<br>344 = `a344_seatbeltLoadLimiterFrontLeftDeployed`<br>345 = `a345_seatbeltLoadLimiterFrontRightDeployed`<br>346 = `a346_seatbeltShoulderPretensionerFrontLeftDeployed`<br>347 = `a347_seatbeltShoulderPretensionerFrontRightDeployed`<br>348 = `a348_seatbeltLapPretensionerFrontLeftDeployed`<br>349 = `a349_seatbeltLapPretensionerFrontRightDeployed`<br>350 = `a350_outboardSeatAirbagLeftDeployed`<br>351 = `a351_outboardSeatAirbagRightDeployed`<br>352 = `a352_hoodLifterLeftDeployed`<br>353 = `a353_hoodLifterRightDeployed`<br>354 = `a354_seatbeltShoulderPretensionerRearLeftDeployed`<br>355 = `a355_seatbeltShoulderPretensionerRearRightDeployed`<br>364 = `a364_safingEngine0NoValidData`<br>365 = `a365_safingEngine1NoValidData`<br>366 = `a366_safingEngine2NoValidData`<br>367 = `a367_safingEngine3NoValidData`<br>368 = `a368_safingEngine4NoValidData`<br>369 = `a369_safingEngine5NoValidData`<br>370 = `a370_safingEngine6NoValidData`<br>371 = `a371_safingEngine7NoValidData`<br>372 = `a372_safingEngine8NoValidData`<br>373 = `a373_safingEngine9NoValidData`<br>374 = `a374_safingEngine10NoValidData`<br>375 = `a375_safingEngine11NoValidData`<br>376 = `a376_safingEngine12NoValidData`<br>377 = `a377_safingEngine13NoValidData`<br>378 = `a378_safingEngine14NoValidData`<br>379 = `a379_safingEngine15NoValidData`<br>380 = `a380_safingEngine16NoValidData`<br>381 = `a381_safingEngine17NoValidData`<br>382 = `a382_safingEngine18NoValidData`<br>383 = `a383_safingEngine19NoValidData`<br>384 = `a384_safingEngine20NoValidData`<br>385 = `a385_safingEngine21NoValidData`<br>387 = `a387_primaryAsicResetSource`<br>388 = `a388_cpuLoadHigh`<br>389 = `a389_asicPwrStatusError`<br>390 = `a390_systemAsicClockOrOperatingStateError`<br>391 = `a391_extAsic1ClockOrOperatingStateError`<br>392 = `a392_extAsic2ClockOrOperatingStateError`<br>393 = `a393_depAdcConvertRatioError`<br>394 = `a394_gspiGlobalStatusWordError`<br>395 = `a395_imuUncalibrated`<br>396 = `a396_spiCommunicationProgramError`<br>397 = `a397_safingMonitorError`<br>398 = `a398_asicNvmReprogrammed`<br>399 = `a399_imuCalibrationComplete`<br>400 = `a400_driverAirbagStage1Issue`<br>401 = `a401_passengerAirbagStage1Issue`<br>402 = `a402_driverAirbagStage2Issue`<br>403 = `a403_driverAirbagActiveVentIssue`<br>404 = `a404_passengerAirbagStage2Issue`<br>405 = `a405_passengerAirbagActiveVentIssue`<br>406 = `a406_inboardSeatAirbagIssue`<br>408 = `a408_kneeAirbagLeftIssue`<br>409 = `a409_kneeAirbagRightIssue`<br>410 = `a410_curtainAirbagLeftIssue`<br>411 = `a411_curtainAirbagRightIssue`<br>412 = `a412_seatbeltLoadLimiterFrontLeftIssue`<br>413 = `a413_seatbeltLoadLimiterFrontRightIssue`<br>414 = `a414_seatbeltShoulderPretensionerFrontLeftIssue`<br>415 = `a415_seatbeltShoulderPretensionerFrontRightIssue`<br>416 = `a416_seatbeltLapPretensionerFrontLeftIssue`<br>417 = `a417_seatbeltLapPretensionerFrontRightIssue`<br>418 = `a418_outboardSeatAirbagLeftIssue`<br>419 = `a419_outboardSeatAirbagRightIssue`<br>420 = `a420_hoodLifterLeftIssue`<br>421 = `a421_hoodLifterRightIssue`<br>422 = `a422_seatbeltShoulderPretensionerRearLeftIssue`<br>423 = `a423_seatbeltShoulderPretensionerRearRightIssue`<br>432 = `a432_driverAirbagStage1ConfigError`<br>433 = `a433_passengerAirbagStage1ConfigError`<br>434 = `a434_driverAirbagStage2ConfigError`<br>435 = `a435_driverAirbagActiveVentConfigError`<br>436 = `a436_passengerAirbagStage2ConfigError`<br>437 = `a437_passengerAirbagActiveVentConfigError`<br>438 = `a438_inboardSeatAirbagConfigError`<br>440 = `a440_kneeAirbagLeftConfigError`<br>441 = `a441_kneeAirbagRightConfigError`<br>442 = `a442_curtainAirbagLeftConfigError`<br>443 = `a443_curtainAirbagRightConfigError`<br>444 = `a444_seatbeltLoadLimiterFrontLeftConfigError`<br>445 = `a445_seatbeltLoadLimiterFrontRightConfigError`<br>446 = `a446_seatbeltShoulderPretensionerFrontLeftConfigError`<br>447 = `a447_seatbeltShoulderPretensionerFrontRightConfigError`<br>448 = `a448_seatbeltLapPretensionerFrontLeftConfigError`<br>449 = `a449_seatbeltLapPretensionerFrontRightConfigError`<br>450 = `a450_outboardSeatAirbagLeftConfigError`<br>451 = `a451_outboardSeatAirbagRightConfigError`<br>452 = `a452_hoodLifterLeftConfigError`<br>453 = `a453_hoodLifterRightConfigError`<br>454 = `a454_seatbeltShoulderPretensionerRearLeftConfigError`<br>455 = `a455_seatbeltShoulderPretensionerRearRightConfigError`<br>544 = `a544_erCapDiagnosticsFailed`<br>545 = `a545_erCapBelowAutarkyThreshold`<br>546 = `a546_sensorValuesFaultedBySmart`<br>550 = `a550_AlgoWake_RCM_WAKE_FRONT`<br>551 = `a551_AlgoWake_RCM_WAKE_REAR`<br>552 = `a552_AlgoWake_RCM_WAKE_LEFT`<br>553 = `a553_AlgoWake_RCM_WAKE_RIGHT`<br>554 = `a554_AlgoWake_PAS_LH_PLAUSI_FRONT`<br>555 = `a555_AlgoWake_PAS_LH_PLAUSI_REAR`<br>557 = `a557_AlgoWake_PAS_RH_PLAUSI_FRONT`<br>558 = `a558_AlgoWake_PAS_RH_PLAUSI_REAR`<br>560 = `a560_AlgoWake_RCM_WAKE_ROLL_LEFT`<br>561 = `a561_AlgoWake_RCM_WAKE_ROLL_RIGHT`<br>562 = `a562_AlgoWake_RCM_AWAKE_FRONT`<br>563 = `a563_AlgoWake_RCM_AWAKE_REAR`<br>564 = `a564_AlgoWake_RCM_AWAKE_LEFT`<br>565 = `a565_AlgoWake_RCM_AWAKE_RIGHT`<br>566 = `a566_AlgoWake_RCM_AWAKE_ROLL`<br>567 = `a567_AlgoWake_RCM_AWAKE_X`<br>568 = `a568_AlgoWake_RCM_AWAKE_Y`<br>569 = `a569_AlgoWake_PAS_WAKE_LEFT`<br>570 = `a570_AlgoWake_PAS_WAKE_RIGHT`<br>576 = `a576_AlgoWake_IMPACT_FINISH_X`<br>577 = `a577_AlgoWake_IMPACT_FINISH_Y`<br>578 = `a578_AlgoWake_IMPACT_FINISH_ROLL`<br>579 = `a579_AlgoWake_RCM_ENABLED_X`<br>580 = `a580_AlgoWake_RCM_ENABLED_Y`<br>581 = `a581_AlgoWake_RCM_ENABLED_ROLL`<br>582 = `a582_AlgoWake_RCM_AWAKE`<br>588 = `a588_yawRateOffsetPosLimit`<br>589 = `a589_yawRateOffsetNegLimit`<br>590 = `a590_pitchRateOffsetPosLimit`<br>591 = `a591_pitchRateOffsetNegLimit`<br>592 = `a592_rollRateOffsetPosLimit`<br>593 = `a593_rollRateOffsetNegLimit`<br>594 = `a594_longitudinalAccelOffsetPosLimit`<br>595 = `a595_longitudinalAccelOffsetNegLimit`<br>596 = `a596_lateralAccelOffsetPosLimit`<br>597 = `a597_lateralAccelOffsetNegLimit`<br>598 = `a598_verticalAccelOffsetPosLimit`<br>599 = `a599_verticalAccelOffsetNegLimit`<br>600 = `a600_airbagAsicStartupFailure`<br>601 = `a601_loop0AsicStartupDiagnosticFailure`<br>602 = `a602_loop1AsicStartupDiagnosticFailure`<br>603 = `a603_loop2AsicStartupDiagnosticFailure`<br>604 = `a604_loop3AsicStartupDiagnosticFailure`<br>605 = `a605_loop4AsicStartupDiagnosticFailure`<br>606 = `a606_loop5AsicStartupDiagnosticFailure`<br>607 = `a607_loop6AsicStartupDiagnosticFailure`<br>608 = `a608_loop7AsicStartupDiagnosticFailure`<br>609 = `a609_loop8AsicStartupDiagnosticFailure`<br>610 = `a610_loop9AsicStartupDiagnosticFailure`<br>611 = `a611_loop10AsicStartupDiagnosticFailure`<br>612 = `a612_loop11AsicStartupDiagnosticFailure`<br>613 = `a613_loop12AsicStartupDiagnosticFailure`<br>614 = `a614_loop13AsicStartupDiagnosticFailure`<br>615 = `a615_loop14AsicStartupDiagnosticFailure`<br>616 = `a616_loop15AsicStartupDiagnosticFailure`<br>617 = `a617_loop16AsicStartupDiagnosticFailure`<br>618 = `a618_loop17AsicStartupDiagnosticFailure`<br>619 = `a619_loop18AsicStartupDiagnosticFailure`<br>620 = `a620_loop19AsicStartupDiagnosticFailure`<br>621 = `a621_loop20AsicStartupDiagnosticFailure`<br>622 = `a622_loop21AsicStartupDiagnosticFailure`<br>623 = `a623_loop22AsicStartupDiagnosticFailure`<br>624 = `a624_loop23AsicStartupDiagnosticFailure`<br>625 = `a625_loop24AsicStartupDiagnosticFailure`<br>626 = `a626_loop25AsicStartupDiagnosticFailure`<br>627 = `a627_loop26AsicStartupDiagnosticFailure`<br>628 = `a628_loop27AsicStartupDiagnosticFailure`<br>629 = `a629_loop28AsicStartupDiagnosticFailure`<br>630 = `a630_loop29AsicStartupDiagnosticFailure`<br>631 = `a631_loop30AsicStartupDiagnosticFailure`<br>632 = `a632_loop31AsicStartupDiagnosticFailure`<br>633 = `a633_glacierInitialStatusFailure`<br>634 = `a634_glacierTraceabilityReadoutA0A0Failure`<br>635 = `a635_glacierTraceabilityReadoutB0B0Failure`<br>636 = `a636_glacierRegisterPatternWriteFailure`<br>637 = `a637_glacierFixedPatternSelfTestFailure`<br>638 = `a638_glacierSelfTestEFailure`<br>639 = `a639_glacierSelfTestFFailure`<br>640 = `a640_glacierAnalogSelfTestFailure`<br>641 = `a641_glacierOscillatorVerificationFailure`<br>642 = `a642_glacierFinalStatusFailure`<br>643 = `a643_glacierOffsetVerificationFailure`<br>644 = `a644_glacierNormalOperationFailure`<br>645 = `a645_glacierDeviceReset`<br>646 = `a646_glacierDeviceFaulted` | plausible |
| `TRCM_alertState` |  | TRCM ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `TRCM_a015_NVMMMemOverflow` | page 15 | TRCM ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a015_NVMMFilesystemError` | page 15 | TRCM ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a015_NVMMRecordIDError` | page 15 | TRCM ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a017_tempData` | page 17 | TRCM ECU: a017 temp data | 16\|16 | little-endian | signed | 0.06897 | 25 | degC | -2235.00896 to 2284.93999 |  | plausible |
| `TRCM_a018_tempData` | page 18 | TRCM ECU: a018 temp data | 16\|16 | little-endian | signed | 0.06897 | 25 | degC | -2235.00896 to 2284.93999 |  | plausible |
| `TRCM_a035_eventArmStatus` | page 35 | TRCM ECU: a035 event arm status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `TRCM_a035_eventFrontLeftSeatbelt` | page 35 | TRCM ECU: a035 event front left seatbelt | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a035_eventFrontRightSeatbelt` | page 35 | TRCM ECU: a035 event front right seatbelt | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a035_eventVehicleSpeed` | page 35 | TRCM ECU: a035 event vehicle speed | 32\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `TRCM_a035_eventDriverBrakeApply` | page 35 | TRCM ECU: a035 event driver brake apply; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `TRCM_a035_eventAccelPedalPos` | page 35 | TRCM ECU: a035 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `TRCM_a036_collisionType` | page 36 | TRCM ECU: a036 collision type; raw 8 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_CLASSIFIED`<br>1 = `FRONT`<br>2 = `LEFTSIDE`<br>3 = `RIGHTSIDE`<br>5 = `REAR`<br>6 = `ROLLOVER`<br>7 = `PEDPRO`<br>8 = `SNA` | plausible |
| `TRCM_a036_collisionSeverity` | page 36 | TRCM ECU: a036 collision severity | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PRETENSIONER`<br>1 = `FIRST_STAGE`<br>2 = `SECOND_STAGE`<br>3 = `PEDPRO_EVENT` | plausible |
| `TRCM_a036_eventArmStatus` | page 36 | TRCM ECU: a036 event arm status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `TRCM_a036_eventFrontLeftSeatbelt` | page 36 | TRCM ECU: a036 event front left seatbelt | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a036_eventFrontRightSeatbelt` | page 36 | TRCM ECU: a036 event front right seatbelt | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a036_eventVehicleSpeed` | page 36 | TRCM ECU: a036 event vehicle speed | 32\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `TRCM_a036_eventDriverBrakeApply` | page 36 | TRCM ECU: a036 event driver brake apply; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `TRCM_a036_eventAccelPedalPos` | page 36 | TRCM ECU: a036 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `TRCM_a037_nearDeployFront` | page 37 | TRCM ECU: a037 near deploy front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_nearDeployRear` | page 37 | TRCM ECU: a037 near deploy rear | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_nearDeployLeft` | page 37 | TRCM ECU: a037 near deploy left | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_nearDeployRight` | page 37 | TRCM ECU: a037 near deploy right | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_nearDeployRoll` | page 37 | TRCM ECU: a037 near deploy roll | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_eventArmStatus` | page 37 | TRCM ECU: a037 event arm status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `TRCM_a037_eventFrontLeftSeatbelt` | page 37 | TRCM ECU: a037 event front left seatbelt | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a037_eventFrontRightSeatbelt` | page 37 | TRCM ECU: a037 event front right seatbelt | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a037_eventVehicleSpeed` | page 37 | TRCM ECU: a037 event vehicle speed | 32\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `TRCM_a037_eventDriverBrakeApply` | page 37 | TRCM ECU: a037 event driver brake apply; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `TRCM_a037_eventAccelPedalPos` | page 37 | TRCM ECU: a037 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `TRCM_a038_stuckLowOrOpenCircuit` | page 38 | TRCM ECU: a038 stuck low or open circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a038_stuckHigh` | page 38 | TRCM ECU: a038 stuck high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a038_overCurrent` | page 38 | TRCM ECU: a038 over current | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a038_driverOverTemperature` | page 38 | TRCM ECU: a038 driver over temperature | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a039_stuckLowOrOpenCircuit` | page 39 | TRCM ECU: a039 stuck low or open circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a039_stuckHigh` | page 39 | TRCM ECU: a039 stuck high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a039_overCurrent` | page 39 | TRCM ECU: a039 over current | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a039_driverOverTemperature` | page 39 | TRCM ECU: a039 driver over temperature | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a057_VEH_cpControl` | page 57 | TRCM ECU: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a059_voltageDrop` | page 59 | TRCM ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `TRCM_a059_resistanceEstimate` | page 59 | TRCM ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `TRCM_a059_current` | page 59 | TRCM ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `TRCM_a063_switchChannel` | page 63 | TRCM ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `TRCM_a063_switchType` | page 63 | TRCM ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `TRCM_a063_ADCVoltage` | page 63 | TRCM ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `TRCM_a063_disconnected` | page 63 | TRCM ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a063_indeterminate` | page 63 | TRCM ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a063_stuckActive` | page 63 | TRCM ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a063_faulted` | page 63 | TRCM ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a065_vsafingFetVoltage` | page 65 | TRCM ECU: a065 vsafing fet voltage | 16\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `TRCM_a066_busVoltage` | page 66 | TRCM ECU: a066 bus voltage | 16\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `TRCM_a078_channelIndex` | page 78 | TRCM ECU: a078 channel index | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `TRCM_a078_value` | page 78 | TRCM ECU: a078 value | 24\|16 | little-endian | signed | 1 | 0 |  | -32768 to 32767 |  | layout-only |
| `TRCM_a081_eventArmStatus` | page 81 | TRCM ECU: a081 event arm status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `TRCM_a081_eventFrontLeftSeatbelt` | page 81 | TRCM ECU: a081 event front left seatbelt | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a081_eventFrontRightSeatbelt` | page 81 | TRCM ECU: a081 event front right seatbelt | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `TRCM_a081_eventVehicleSpeed` | page 81 | TRCM ECU: a081 event vehicle speed | 32\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `TRCM_a081_eventDriverBrakeApply` | page 81 | TRCM ECU: a081 event driver brake apply; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `TRCM_a081_eventAccelPedalPos` | page 81 | TRCM ECU: a081 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `TRCM_a082_RIPC_epbPrivateState` | page 82 | TRCM ECU: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a082_RIPC_remoteHSD` | page 82 | TRCM ECU: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a082_RIPC_railStatus` | page 82 | TRCM ECU: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a082_RIPC_remoteMux` | page 82 | TRCM ECU: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a083_LIPC_epbPrivateState` | page 83 | TRCM ECU: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a083_LIPC_remoteHSD` | page 83 | TRCM ECU: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a083_LIPC_railStatus` | page 83 | TRCM ECU: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a083_LIPC_HSDFaults` | page 83 | TRCM ECU: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a084_CH_StatusC` | page 84 | TRCM ECU: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a085_PARTY_buttonStatus` | page 85 | TRCM ECU: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_LVBMS_statusHigh` | page 86 | TRCM ECU: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_LVBMS_statusLow` | page 86 | TRCM ECU: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_status` | page 86 | TRCM ECU: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_12VBatteryStatus` | page 86 | TRCM ECU: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_LVPowerState` | page 86 | TRCM ECU: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_lightStatus` | page 86 | TRCM ECU: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_systemStatus` | page 86 | TRCM ECU: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_thermalStatus` | page 86 | TRCM ECU: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VEH_vehNm` | page 86 | TRCM ECU: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_VEH_temperature` | page 87 | TRCM ECU: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_VEH_thermalControl` | page 87 | TRCM ECU: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_VEH_torque` | page 87 | TRCM ECU: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_VEH_status` | page 87 | TRCM ECU: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_PARTY_torque` | page 87 | TRCM ECU: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_PARTY_status` | page 87 | TRCM ECU: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_PARTY_temperature` | page 87 | TRCM ECU: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_PARTY_thermalControl` | page 87 | TRCM ECU: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_VEH_motorStatus` | page 87 | TRCM ECU: a087 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_temperature` | page 88 | TRCM ECU: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_thermalControl` | page 88 | TRCM ECU: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_torque` | page 88 | TRCM ECU: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_status` | page 88 | TRCM ECU: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_torque` | page 88 | TRCM ECU: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_status` | page 88 | TRCM ECU: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_temperature` | page 88 | TRCM ECU: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_thermalControl` | page 88 | TRCM ECU: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_motorStatus` | page 88 | TRCM ECU: a088 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_PARTY_party1` | page 89 | TRCM ECU: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_PARTY_status` | page 89 | TRCM ECU: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_VEH_status` | page 89 | TRCM ECU: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_BDY_party1` | page 89 | TRCM ECU: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_BDY_status` | page 89 | TRCM ECU: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_CH_status` | page 89 | TRCM ECU: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_CH_party1` | page 89 | TRCM ECU: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_CH_party3` | page 89 | TRCM ECU: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_VEH_party1` | page 89 | TRCM ECU: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_VEH_party3` | page 89 | TRCM ECU: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a091_VEH_faultsAndExtras` | page 91 | TRCM ECU: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a091_VEH_info` | page 91 | TRCM ECU: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a091_VEH_state` | page 91 | TRCM ECU: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a092_VEH_restraintStatus` | page 92 | TRCM ECU: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a092_VEH_switchStatus` | page 92 | TRCM ECU: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a092_VEH_seatStatus2` | page 92 | TRCM ECU: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a092_VEH_vehNm` | page 92 | TRCM ECU: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a093_VEH_restraintStatus` | page 93 | TRCM ECU: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a093_VEH_switchStatus` | page 93 | TRCM ECU: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a093_VEH_seatStatus2` | page 93 | TRCM ECU: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a093_VEH_vehNm` | page 93 | TRCM ECU: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a094_VEH_sysStatus` | page 94 | TRCM ECU: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a094_PARTY_sysStatus` | page 94 | TRCM ECU: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a094_CH_sysStatus` | page 94 | TRCM ECU: a094 CH sys status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a095_PT_ptNm` | page 95 | TRCM ECU: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a095_PT_status` | page 95 | TRCM ECU: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a096_VEH_status` | page 96 | TRCM ECU: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a096_CH_status` | page 96 | TRCM ECU: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a097_VEH_HVStatus` | page 97 | TRCM ECU: a097 VEH HV status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a097_VEH_state` | page 97 | TRCM ECU: a097 VEH state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_CH_torque` | page 98 | TRCM ECU: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_hvStatus` | page 98 | TRCM ECU: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_status` | page 98 | TRCM ECU: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_thermalControl` | page 98 | TRCM ECU: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_temperature` | page 98 | TRCM ECU: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_torque` | page 98 | TRCM ECU: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PARTY_status` | page 98 | TRCM ECU: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PARTY_temperature` | page 98 | TRCM ECU: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PARTY_thermalControl` | page 98 | TRCM ECU: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PARTY_torque` | page 98 | TRCM ECU: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PT_thermalControl` | page 98 | TRCM ECU: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PT_temperature` | page 98 | TRCM ECU: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_PARTY_motorStatus` | page 98 | TRCM ECU: a098 PARTY motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_VEH_motorStatus` | page 98 | TRCM ECU: a098 VEH motor status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a099_VEH_oocStatus` | page 99 | TRCM ECU: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_VEH` | page 100 | TRCM ECU: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_PARTY` | page 100 | TRCM ECU: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_PT` | page 100 | TRCM ECU: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_CH` | page 100 | TRCM ECU: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_OBD` | page 100 | TRCM ECU: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_VEH_state` | page 101 | TRCM ECU: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_PARTY_locState` | page 101 | TRCM ECU: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_LIPC_externalWatchdogHeartBeat` | page 101 | TRCM ECU: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_VEH_locState` | page 101 | TRCM ECU: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_BDY_locState` | page 101 | TRCM ECU: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a102_VEH_faultsAndExtras` | page 102 | TRCM ECU: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a102_VEH_feedbackStatus` | page 102 | TRCM ECU: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a102_VEH_sensorStatus` | page 102 | TRCM ECU: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a102_VEH_rods` | page 102 | TRCM ECU: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_VEH_hvsNm` | page 103 | TRCM ECU: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_VEH_vehNm` | page 103 | TRCM ECU: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_VEH_status` | page 103 | TRCM ECU: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_PT_ptNm` | page 103 | TRCM ECU: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_PT_status` | page 103 | TRCM ECU: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_VEH_evseStatus` | page 103 | TRCM ECU: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a105_VEH_states` | page 105 | TRCM ECU: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a105_VEH_chNm` | page 105 | TRCM ECU: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a105_VEH_dampingStates` | page 105 | TRCM ECU: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_VEH_dcdcStatus` | page 106 | TRCM ECU: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_VEH_thermalControl` | page 106 | TRCM ECU: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_VEH_dcdcRailStatus` | page 106 | TRCM ECU: a106 VEH dcdc rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_CH_dcdcRailStatus` | page 106 | TRCM ECU: a106 CH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_CH_alertMatrix` | page 106 | TRCM ECU: a106 CH alert matrix | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_hvsNm` | page 107 | TRCM ECU: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_vehNm` | page 107 | TRCM ECU: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_status` | page 107 | TRCM ECU: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_thermalStatus` | page 107 | TRCM ECU: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_bmbMinMax` | page 107 | TRCM ECU: a107 VEH bmb min max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_powerAvailable` | page 107 | TRCM ECU: a107 VEH power available | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_ptNm` | page 107 | TRCM ECU: a107 PT pt nm | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_status` | page 107 | TRCM ECU: a107 PT status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_thermalStatus` | page 107 | TRCM ECU: a107 PT thermal status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_socStatus` | page 107 | TRCM ECU: a107 PT soc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_socStatus` | page 107 | TRCM ECU: a107 VEH soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_packConfig` | page 107 | TRCM ECU: a107 VEH pack config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_energyStatus` | page 107 | TRCM ECU: a107 VEH energy status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_chargeInfo` | page 107 | TRCM ECU: a107 VEH charge info | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_hvStatus` | page 108 | TRCM ECU: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_temperature` | page 108 | TRCM ECU: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_thermalControl` | page 108 | TRCM ECU: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_torque` | page 108 | TRCM ECU: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_status` | page 108 | TRCM ECU: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PARTY_torque` | page 108 | TRCM ECU: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PARTY_status` | page 108 | TRCM ECU: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PARTY_temperature` | page 108 | TRCM ECU: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PARTY_thermalControl` | page 108 | TRCM ECU: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PT_temperature` | page 108 | TRCM ECU: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PT_thermalControl` | page 108 | TRCM ECU: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_PARTY_motorStatus` | page 108 | TRCM ECU: a108 PARTY motor status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_VEH_motorStatus` | page 108 | TRCM ECU: a108 VEH motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_CH_torque` | page 108 | TRCM ECU: a108 CH torque | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_carState` | page 110 | TRCM ECU: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_carConfig` | page 110 | TRCM ECU: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_time` | page 110 | TRCM ECU: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_updateStatus` | page 110 | TRCM ECU: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_vehNm` | page 110 | TRCM ECU: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_mismatchFault` | page 110 | TRCM ECU: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_vin` | page 110 | TRCM ECU: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_bmpDebug` | page 110 | TRCM ECU: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_gearControl` | page 110 | TRCM ECU: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_VEH_canLogAvailability` | page 110 | TRCM ECU: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_airbagCutoffStatus` | page 110 | TRCM ECU: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_carConfig` | page 110 | TRCM ECU: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_carState` | page 110 | TRCM ECU: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_vin` | page 110 | TRCM ECU: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_chNm` | page 110 | TRCM ECU: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_CH_epochTimeGtw` | page 110 | TRCM ECU: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_PARTY_carConfig` | page 110 | TRCM ECU: a110 PARTY car config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_VEH_internalStatus` | page 111 | TRCM ECU: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_VEH_status` | page 111 | TRCM ECU: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_VEH_vehNm` | page 111 | TRCM ECU: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_RIPC_LVPowerState` | page 111 | TRCM ECU: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_RIPC_epbPrivateState` | page 111 | TRCM ECU: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_RIPC_railStatus` | page 111 | TRCM ECU: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_RIPC_remoteADC` | page 111 | TRCM ECU: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_RIPC_switchStatus` | page 111 | TRCM ECU: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_VEH_LVPowerState` | page 111 | TRCM ECU: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_VEH_seatStatus` | page 111 | TRCM ECU: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_PARTY_status` | page 111 | TRCM ECU: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_CH_status` | page 111 | TRCM ECU: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_VEH_internalStatus` | page 112 | TRCM ECU: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_VEH_status` | page 112 | TRCM ECU: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_VEH_vehNm` | page 112 | TRCM ECU: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_LIPC_LVPowerState` | page 112 | TRCM ECU: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_LIPC_epbPrivateState` | page 112 | TRCM ECU: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_LIPC_railStatus` | page 112 | TRCM ECU: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_LIPC_remoteADC` | page 112 | TRCM ECU: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_LIPC_switchStatus` | page 112 | TRCM ECU: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_VEH_LVPowerState` | page 112 | TRCM ECU: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_PARTY_status` | page 112 | TRCM ECU: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_CH_status` | page 112 | TRCM ECU: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_status` | page 114 | TRCM ECU: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_wheelSpeeds` | page 114 | TRCM ECU: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_VEH_wheelSpeeds` | page 114 | TRCM ECU: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_CH_wheelSpeeds` | page 114 | TRCM ECU: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_party3` | page 114 | TRCM ECU: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_VEH_party3` | page 114 | TRCM ECU: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_VEH_status` | page 114 | TRCM ECU: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_wheelRotation` | page 114 | TRCM ECU: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_CH_wheelRotation` | page 114 | TRCM ECU: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_VEH_wheelRotation` | page 114 | TRCM ECU: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_brakeTorque` | page 114 | TRCM ECU: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_PARTY_offsets` | page 114 | TRCM ECU: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_BDY_offsets` | page 114 | TRCM ECU: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_BDY_party3` | page 114 | TRCM ECU: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_BDY_status` | page 114 | TRCM ECU: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_BDY_wheelRotation` | page 114 | TRCM ECU: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_BDY_wheelSpeeds` | page 114 | TRCM ECU: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_CH_party1` | page 114 | TRCM ECU: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_CH_party3` | page 114 | TRCM ECU: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_CH_status` | page 114 | TRCM ECU: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VEH_vehNm` | page 115 | TRCM ECU: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VEH_authentication` | page 115 | TRCM ECU: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VEH_BLEResetRequest` | page 115 | TRCM ECU: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VEH_requests` | page 115 | TRCM ECU: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VEH_requests2` | page 115 | TRCM ECU: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_REM_authentication` | page 115 | TRCM ECU: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_UI_corianderVehicleControl` | page 115 | TRCM ECU: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_CH_TPMSDisplay` | page 115 | TRCM ECU: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_PARTY_epbmStatus` | page 116 | TRCM ECU: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_vehNm` | page 116 | TRCM ECU: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_hvacRequest` | page 116 | TRCM ECU: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_hvacStatus` | page 116 | TRCM ECU: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_LVPowerState` | page 116 | TRCM ECU: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_lightStatus` | page 116 | TRCM ECU: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_seatStatus` | page 116 | TRCM ECU: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_thsStatus` | page 116 | TRCM ECU: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_doorStatus` | page 116 | TRCM ECU: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_seatHeatStatus` | page 116 | TRCM ECU: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_restraintStatus` | page 116 | TRCM ECU: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_switchStatus` | page 116 | TRCM ECU: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_logging1Hz` | page 116 | TRCM ECU: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_seatStatus2` | page 116 | TRCM ECU: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_status` | page 116 | TRCM ECU: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_thermalCommand` | page 116 | TRCM ECU: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VEH_windowStatus` | page 116 | TRCM ECU: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_PARTY_restraintStatus` | page 116 | TRCM ECU: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_PARTY_doorStatus` | page 116 | TRCM ECU: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_BDY_epbmStatus` | page 116 | TRCM ECU: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_BDY_restraintStatus` | page 116 | TRCM ECU: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_BDY_switchStatus` | page 116 | TRCM ECU: a116 BDY switch status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_BDY_epbmStatus` | page 117 | TRCM ECU: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_BDY_restraintStatus` | page 117 | TRCM ECU: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_prndStatus` | page 117 | TRCM ECU: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_PARTY_epbmStatus` | page 117 | TRCM ECU: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_vehNm` | page 117 | TRCM ECU: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_hvacBlowerFdb` | page 117 | TRCM ECU: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_LVPowerState` | page 117 | TRCM ECU: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_restraintStatus` | page 117 | TRCM ECU: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_lightStatus` | page 117 | TRCM ECU: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_seatStatus` | page 117 | TRCM ECU: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_BDY_falconSwitchStatus` | page 117 | TRCM ECU: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_doorStatus` | page 117 | TRCM ECU: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_doorStatus2` | page 117 | TRCM ECU: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_windowStatus` | page 117 | TRCM ECU: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_switchStatus` | page 117 | TRCM ECU: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_intrusionSensorStatus` | page 117 | TRCM ECU: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_liftgateStatus` | page 117 | TRCM ECU: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_seatStatus2` | page 117 | TRCM ECU: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_PARTY_restraintStatus` | page 117 | TRCM ECU: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_thermalStatus` | page 117 | TRCM ECU: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_PARTY_doorStatus` | page 117 | TRCM ECU: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VEH_status` | page 117 | TRCM ECU: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_PARTY_prndStatus` | page 117 | TRCM ECU: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_PARTY_lightingSecondary` | page 117 | TRCM ECU: a117 PARTY lighting secondary | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_vehNm` | page 118 | TRCM ECU: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_lighting` | page 118 | TRCM ECU: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_sensors` | page 118 | TRCM ECU: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_status` | page 118 | TRCM ECU: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_okToUseHighPwr` | page 118 | TRCM ECU: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_LVPowerState` | page 118 | TRCM ECU: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_coolant` | page 118 | TRCM ECU: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_vehicleStatus` | page 118 | TRCM ECU: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_12VBatteryStatus` | page 118 | TRCM ECU: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_systemStatus` | page 118 | TRCM ECU: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_LVPowerState` | page 118 | TRCM ECU: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_outputPowerStatus` | page 118 | TRCM ECU: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_vehicleTime` | page 118 | TRCM ECU: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_thermalCommand` | page 118 | TRCM ECU: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_LVPowerState` | page 118 | TRCM ECU: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_sensors` | page 118 | TRCM ECU: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_sensors` | page 118 | TRCM ECU: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_interNodeResistance` | page 118 | TRCM ECU: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_lighting` | page 118 | TRCM ECU: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VEH_lightStatus` | page 118 | TRCM ECU: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_vehNm` | page 118 | TRCM ECU: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_12VBatteryStatus` | page 118 | TRCM ECU: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_LVBMS_statusHigh` | page 118 | TRCM ECU: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_CH_alertMatrix` | page 118 | TRCM ECU: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_BDY_outputPowerStatus` | page 118 | TRCM ECU: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_BDY_vehicleTime` | page 118 | TRCM ECU: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | TRCM ECU: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | TRCM ECU: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_PARTY_VCFRONT_cameraCleaningStatus` | page 118 | TRCM ECU: a118 PARTY VCFRONT camera cleaning status | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_VEH_steerAngle` | page 119 | TRCM ECU: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_VEH_leftStalk` | page 119 | TRCM ECU: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_VEH_rightStalk` | page 119 | TRCM ECU: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_PARTY_rightStalk` | page 119 | TRCM ECU: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_CH_steerAngle` | page 119 | TRCM ECU: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_PARTY_steerAngle` | page 119 | TRCM ECU: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_chassisCntl` | page 120 | TRCM ECU: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_systemStatus` | page 120 | TRCM ECU: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_CH_chassisCntl` | page 120 | TRCM ECU: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_systemStatus` | page 120 | TRCM ECU: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_torque` | page 120 | TRCM ECU: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_torque` | page 120 | TRCM ECU: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_locStatus` | page 120 | TRCM ECU: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_speed` | page 120 | TRCM ECU: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_speed` | page 120 | TRCM ECU: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_status` | page 120 | TRCM ECU: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PT_speed` | page 120 | TRCM ECU: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PT_systemStatus` | page 120 | TRCM ECU: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_vehicleEstimates` | page 120 | TRCM ECU: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_aggregatedAxleSpeed` | page 120 | TRCM ECU: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_aggregatedAxleSpeed` | page 120 | TRCM ECU: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_systemPower` | page 120 | TRCM ECU: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_autonomyHealth` | page 120 | TRCM ECU: a120 PARTY autonomy health | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_autonomyHealth` | page 120 | TRCM ECU: a120 VEH autonomy health | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PT_systemPower` | page 120 | TRCM ECU: a120 PT system power | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_stalklessInterfaces` | page 120 | TRCM ECU: a120 PARTY stalkless interfaces | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_CH_speed` | page 120 | TRCM ECU: a120 CH speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_estimatedBrakeTemp` | page 120 | TRCM ECU: a120 VEH estimated brake temp | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_prndControl` | page 120 | TRCM ECU: a120 PARTY prnd control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_locStatus2` | page 120 | TRCM ECU: a120 PARTY loc status2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_chassisCntl` | page 120 | TRCM ECU: a120 VEH chassis cntl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_CH_locStatus2` | page 120 | TRCM ECU: a120 CH loc status2 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_locStatus` | page 120 | TRCM ECU: a120 VEH loc status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_locStatus2` | page 120 | TRCM ECU: a120 VEH loc status2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_prndControl` | page 120 | TRCM ECU: a120 VEH prnd control | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_vehicleEstimates` | page 120 | TRCM ECU: a120 VEH vehicle estimates | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_motorStatus` | page 120 | TRCM ECU: a120 PARTY motor status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_motorStatus` | page 120 | TRCM ECU: a120 VEH motor status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_BDY_speed` | page 120 | TRCM ECU: a120 BDY speed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_groundLossError` | page 332 | TRCM ECU: a332 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_overcurrentError` | page 332 | TRCM ECU: a332 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_overvoltageError` | page 332 | TRCM ECU: a332 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_currentMonitorTimer` | page 332 | TRCM ECU: a332 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a333_groundLossError` | page 333 | TRCM ECU: a333 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a333_overcurrentError` | page 333 | TRCM ECU: a333 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a333_overvoltageError` | page 333 | TRCM ECU: a333 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a333_currentMonitorTimer` | page 333 | TRCM ECU: a333 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a334_groundLossError` | page 334 | TRCM ECU: a334 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a334_overcurrentError` | page 334 | TRCM ECU: a334 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a334_overvoltageError` | page 334 | TRCM ECU: a334 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a334_currentMonitorTimer` | page 334 | TRCM ECU: a334 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a335_groundLossError` | page 335 | TRCM ECU: a335 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a335_overcurrentError` | page 335 | TRCM ECU: a335 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a335_overvoltageError` | page 335 | TRCM ECU: a335 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a335_currentMonitorTimer` | page 335 | TRCM ECU: a335 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a336_groundLossError` | page 336 | TRCM ECU: a336 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a336_overcurrentError` | page 336 | TRCM ECU: a336 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a336_overvoltageError` | page 336 | TRCM ECU: a336 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a336_currentMonitorTimer` | page 336 | TRCM ECU: a336 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a337_groundLossError` | page 337 | TRCM ECU: a337 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a337_overcurrentError` | page 337 | TRCM ECU: a337 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a337_overvoltageError` | page 337 | TRCM ECU: a337 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a337_currentMonitorTimer` | page 337 | TRCM ECU: a337 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a338_groundLossError` | page 338 | TRCM ECU: a338 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a338_overcurrentError` | page 338 | TRCM ECU: a338 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a338_overvoltageError` | page 338 | TRCM ECU: a338 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a338_currentMonitorTimer` | page 338 | TRCM ECU: a338 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a340_groundLossError` | page 340 | TRCM ECU: a340 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a340_overcurrentError` | page 340 | TRCM ECU: a340 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a340_overvoltageError` | page 340 | TRCM ECU: a340 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a340_currentMonitorTimer` | page 340 | TRCM ECU: a340 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a341_groundLossError` | page 341 | TRCM ECU: a341 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a341_overcurrentError` | page 341 | TRCM ECU: a341 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a341_overvoltageError` | page 341 | TRCM ECU: a341 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a341_currentMonitorTimer` | page 341 | TRCM ECU: a341 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a342_groundLossError` | page 342 | TRCM ECU: a342 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a342_overcurrentError` | page 342 | TRCM ECU: a342 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a342_overvoltageError` | page 342 | TRCM ECU: a342 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a342_currentMonitorTimer` | page 342 | TRCM ECU: a342 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a343_groundLossError` | page 343 | TRCM ECU: a343 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a343_overcurrentError` | page 343 | TRCM ECU: a343 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a343_overvoltageError` | page 343 | TRCM ECU: a343 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a343_currentMonitorTimer` | page 343 | TRCM ECU: a343 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a344_groundLossError` | page 344 | TRCM ECU: a344 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a344_overcurrentError` | page 344 | TRCM ECU: a344 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a344_overvoltageError` | page 344 | TRCM ECU: a344 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a344_currentMonitorTimer` | page 344 | TRCM ECU: a344 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a345_groundLossError` | page 345 | TRCM ECU: a345 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a345_overcurrentError` | page 345 | TRCM ECU: a345 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a345_overvoltageError` | page 345 | TRCM ECU: a345 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a345_currentMonitorTimer` | page 345 | TRCM ECU: a345 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a346_groundLossError` | page 346 | TRCM ECU: a346 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a346_overcurrentError` | page 346 | TRCM ECU: a346 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a346_overvoltageError` | page 346 | TRCM ECU: a346 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a346_currentMonitorTimer` | page 346 | TRCM ECU: a346 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a347_groundLossError` | page 347 | TRCM ECU: a347 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a347_overcurrentError` | page 347 | TRCM ECU: a347 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a347_overvoltageError` | page 347 | TRCM ECU: a347 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a347_currentMonitorTimer` | page 347 | TRCM ECU: a347 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a348_groundLossError` | page 348 | TRCM ECU: a348 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a348_overcurrentError` | page 348 | TRCM ECU: a348 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a348_overvoltageError` | page 348 | TRCM ECU: a348 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a348_currentMonitorTimer` | page 348 | TRCM ECU: a348 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a349_groundLossError` | page 349 | TRCM ECU: a349 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a349_overcurrentError` | page 349 | TRCM ECU: a349 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a349_overvoltageError` | page 349 | TRCM ECU: a349 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a349_currentMonitorTimer` | page 349 | TRCM ECU: a349 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a350_groundLossError` | page 350 | TRCM ECU: a350 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a350_overcurrentError` | page 350 | TRCM ECU: a350 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a350_overvoltageError` | page 350 | TRCM ECU: a350 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a350_currentMonitorTimer` | page 350 | TRCM ECU: a350 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a351_groundLossError` | page 351 | TRCM ECU: a351 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a351_overcurrentError` | page 351 | TRCM ECU: a351 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a351_overvoltageError` | page 351 | TRCM ECU: a351 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a351_currentMonitorTimer` | page 351 | TRCM ECU: a351 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a352_groundLossError` | page 352 | TRCM ECU: a352 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a352_overcurrentError` | page 352 | TRCM ECU: a352 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a352_overvoltageError` | page 352 | TRCM ECU: a352 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a352_currentMonitorTimer` | page 352 | TRCM ECU: a352 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a353_groundLossError` | page 353 | TRCM ECU: a353 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a353_overcurrentError` | page 353 | TRCM ECU: a353 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a353_overvoltageError` | page 353 | TRCM ECU: a353 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a353_currentMonitorTimer` | page 353 | TRCM ECU: a353 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a354_groundLossError` | page 354 | TRCM ECU: a354 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a354_overcurrentError` | page 354 | TRCM ECU: a354 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a354_overvoltageError` | page 354 | TRCM ECU: a354 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a354_currentMonitorTimer` | page 354 | TRCM ECU: a354 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a355_groundLossError` | page 355 | TRCM ECU: a355 ground loss error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a355_overcurrentError` | page 355 | TRCM ECU: a355 overcurrent error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a355_overvoltageError` | page 355 | TRCM ECU: a355 overvoltage error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a355_currentMonitorTimer` | page 355 | TRCM ECU: a355 current monitor timer | 24\|8 | little-endian | unsigned | 16 | 0 | us | 0 to 4080 |  | plausible |
| `TRCM_a400_deploymentLoopNumber` | page 400 | TRCM ECU: a400 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a400_resistance` | page 400 | TRCM ECU: a400 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a400_shortToGround` | page 400 | TRCM ECU: a400 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_shortToBattery` | page 400 | TRCM ECU: a400 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_shortToSelf` | page 400 | TRCM ECU: a400 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_openCircuit` | page 400 | TRCM ECU: a400 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_crossCoupled` | page 400 | TRCM ECU: a400 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_resistanceOutOfSpec` | page 400 | TRCM ECU: a400 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_deploymentLoopNumber` | page 401 | TRCM ECU: a401 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a401_resistance` | page 401 | TRCM ECU: a401 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a401_shortToGround` | page 401 | TRCM ECU: a401 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_shortToBattery` | page 401 | TRCM ECU: a401 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_shortToSelf` | page 401 | TRCM ECU: a401 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_openCircuit` | page 401 | TRCM ECU: a401 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_crossCoupled` | page 401 | TRCM ECU: a401 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_resistanceOutOfSpec` | page 401 | TRCM ECU: a401 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_deploymentLoopNumber` | page 402 | TRCM ECU: a402 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a402_resistance` | page 402 | TRCM ECU: a402 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a402_shortToGround` | page 402 | TRCM ECU: a402 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_shortToBattery` | page 402 | TRCM ECU: a402 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_shortToSelf` | page 402 | TRCM ECU: a402 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_openCircuit` | page 402 | TRCM ECU: a402 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_crossCoupled` | page 402 | TRCM ECU: a402 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_resistanceOutOfSpec` | page 402 | TRCM ECU: a402 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_deploymentLoopNumber` | page 403 | TRCM ECU: a403 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a403_resistance` | page 403 | TRCM ECU: a403 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a403_shortToGround` | page 403 | TRCM ECU: a403 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_shortToBattery` | page 403 | TRCM ECU: a403 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_shortToSelf` | page 403 | TRCM ECU: a403 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_openCircuit` | page 403 | TRCM ECU: a403 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_crossCoupled` | page 403 | TRCM ECU: a403 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_resistanceOutOfSpec` | page 403 | TRCM ECU: a403 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_deploymentLoopNumber` | page 404 | TRCM ECU: a404 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a404_resistance` | page 404 | TRCM ECU: a404 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a404_shortToGround` | page 404 | TRCM ECU: a404 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_shortToBattery` | page 404 | TRCM ECU: a404 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_shortToSelf` | page 404 | TRCM ECU: a404 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_openCircuit` | page 404 | TRCM ECU: a404 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_crossCoupled` | page 404 | TRCM ECU: a404 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_resistanceOutOfSpec` | page 404 | TRCM ECU: a404 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_deploymentLoopNumber` | page 405 | TRCM ECU: a405 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a405_resistance` | page 405 | TRCM ECU: a405 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a405_shortToGround` | page 405 | TRCM ECU: a405 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_shortToBattery` | page 405 | TRCM ECU: a405 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_shortToSelf` | page 405 | TRCM ECU: a405 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_openCircuit` | page 405 | TRCM ECU: a405 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_crossCoupled` | page 405 | TRCM ECU: a405 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_resistanceOutOfSpec` | page 405 | TRCM ECU: a405 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_deploymentLoopNumber` | page 406 | TRCM ECU: a406 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a406_resistance` | page 406 | TRCM ECU: a406 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a406_shortToGround` | page 406 | TRCM ECU: a406 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_shortToBattery` | page 406 | TRCM ECU: a406 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_shortToSelf` | page 406 | TRCM ECU: a406 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_openCircuit` | page 406 | TRCM ECU: a406 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_crossCoupled` | page 406 | TRCM ECU: a406 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_resistanceOutOfSpec` | page 406 | TRCM ECU: a406 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_deploymentLoopNumber` | page 408 | TRCM ECU: a408 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a408_resistance` | page 408 | TRCM ECU: a408 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a408_shortToGround` | page 408 | TRCM ECU: a408 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_shortToBattery` | page 408 | TRCM ECU: a408 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_shortToSelf` | page 408 | TRCM ECU: a408 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_openCircuit` | page 408 | TRCM ECU: a408 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_crossCoupled` | page 408 | TRCM ECU: a408 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_resistanceOutOfSpec` | page 408 | TRCM ECU: a408 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_deploymentLoopNumber` | page 409 | TRCM ECU: a409 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a409_resistance` | page 409 | TRCM ECU: a409 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a409_shortToGround` | page 409 | TRCM ECU: a409 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_shortToBattery` | page 409 | TRCM ECU: a409 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_shortToSelf` | page 409 | TRCM ECU: a409 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_openCircuit` | page 409 | TRCM ECU: a409 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_crossCoupled` | page 409 | TRCM ECU: a409 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_resistanceOutOfSpec` | page 409 | TRCM ECU: a409 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_deploymentLoopNumber` | page 410 | TRCM ECU: a410 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a410_resistance` | page 410 | TRCM ECU: a410 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a410_shortToGround` | page 410 | TRCM ECU: a410 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_shortToBattery` | page 410 | TRCM ECU: a410 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_shortToSelf` | page 410 | TRCM ECU: a410 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_openCircuit` | page 410 | TRCM ECU: a410 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_crossCoupled` | page 410 | TRCM ECU: a410 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_resistanceOutOfSpec` | page 410 | TRCM ECU: a410 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_deploymentLoopNumber` | page 411 | TRCM ECU: a411 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a411_resistance` | page 411 | TRCM ECU: a411 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a411_shortToGround` | page 411 | TRCM ECU: a411 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_shortToBattery` | page 411 | TRCM ECU: a411 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_shortToSelf` | page 411 | TRCM ECU: a411 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_openCircuit` | page 411 | TRCM ECU: a411 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_crossCoupled` | page 411 | TRCM ECU: a411 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_resistanceOutOfSpec` | page 411 | TRCM ECU: a411 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_deploymentLoopNumber` | page 412 | TRCM ECU: a412 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a412_resistance` | page 412 | TRCM ECU: a412 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a412_shortToGround` | page 412 | TRCM ECU: a412 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_shortToBattery` | page 412 | TRCM ECU: a412 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_shortToSelf` | page 412 | TRCM ECU: a412 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_openCircuit` | page 412 | TRCM ECU: a412 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_crossCoupled` | page 412 | TRCM ECU: a412 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_resistanceOutOfSpec` | page 412 | TRCM ECU: a412 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_deploymentLoopNumber` | page 413 | TRCM ECU: a413 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a413_resistance` | page 413 | TRCM ECU: a413 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a413_shortToGround` | page 413 | TRCM ECU: a413 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_shortToBattery` | page 413 | TRCM ECU: a413 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_shortToSelf` | page 413 | TRCM ECU: a413 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_openCircuit` | page 413 | TRCM ECU: a413 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_crossCoupled` | page 413 | TRCM ECU: a413 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_resistanceOutOfSpec` | page 413 | TRCM ECU: a413 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_deploymentLoopNumber` | page 414 | TRCM ECU: a414 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a414_resistance` | page 414 | TRCM ECU: a414 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a414_shortToGround` | page 414 | TRCM ECU: a414 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_shortToBattery` | page 414 | TRCM ECU: a414 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_shortToSelf` | page 414 | TRCM ECU: a414 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_openCircuit` | page 414 | TRCM ECU: a414 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_crossCoupled` | page 414 | TRCM ECU: a414 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_resistanceOutOfSpec` | page 414 | TRCM ECU: a414 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_deploymentLoopNumber` | page 415 | TRCM ECU: a415 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a415_resistance` | page 415 | TRCM ECU: a415 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a415_shortToGround` | page 415 | TRCM ECU: a415 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_shortToBattery` | page 415 | TRCM ECU: a415 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_shortToSelf` | page 415 | TRCM ECU: a415 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_openCircuit` | page 415 | TRCM ECU: a415 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_crossCoupled` | page 415 | TRCM ECU: a415 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_resistanceOutOfSpec` | page 415 | TRCM ECU: a415 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_deploymentLoopNumber` | page 416 | TRCM ECU: a416 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a416_resistance` | page 416 | TRCM ECU: a416 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a416_shortToGround` | page 416 | TRCM ECU: a416 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_shortToBattery` | page 416 | TRCM ECU: a416 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_shortToSelf` | page 416 | TRCM ECU: a416 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_openCircuit` | page 416 | TRCM ECU: a416 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_crossCoupled` | page 416 | TRCM ECU: a416 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_resistanceOutOfSpec` | page 416 | TRCM ECU: a416 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_deploymentLoopNumber` | page 417 | TRCM ECU: a417 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a417_resistance` | page 417 | TRCM ECU: a417 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a417_shortToGround` | page 417 | TRCM ECU: a417 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_shortToBattery` | page 417 | TRCM ECU: a417 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_shortToSelf` | page 417 | TRCM ECU: a417 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_openCircuit` | page 417 | TRCM ECU: a417 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_crossCoupled` | page 417 | TRCM ECU: a417 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_resistanceOutOfSpec` | page 417 | TRCM ECU: a417 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_deploymentLoopNumber` | page 418 | TRCM ECU: a418 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a418_resistance` | page 418 | TRCM ECU: a418 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a418_shortToGround` | page 418 | TRCM ECU: a418 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_shortToBattery` | page 418 | TRCM ECU: a418 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_shortToSelf` | page 418 | TRCM ECU: a418 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_openCircuit` | page 418 | TRCM ECU: a418 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_crossCoupled` | page 418 | TRCM ECU: a418 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_resistanceOutOfSpec` | page 418 | TRCM ECU: a418 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_deploymentLoopNumber` | page 419 | TRCM ECU: a419 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a419_resistance` | page 419 | TRCM ECU: a419 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a419_shortToGround` | page 419 | TRCM ECU: a419 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_shortToBattery` | page 419 | TRCM ECU: a419 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_shortToSelf` | page 419 | TRCM ECU: a419 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_openCircuit` | page 419 | TRCM ECU: a419 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_crossCoupled` | page 419 | TRCM ECU: a419 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_resistanceOutOfSpec` | page 419 | TRCM ECU: a419 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_deploymentLoopNumber` | page 420 | TRCM ECU: a420 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a420_resistance` | page 420 | TRCM ECU: a420 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a420_shortToGround` | page 420 | TRCM ECU: a420 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_shortToBattery` | page 420 | TRCM ECU: a420 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_shortToSelf` | page 420 | TRCM ECU: a420 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_openCircuit` | page 420 | TRCM ECU: a420 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_crossCoupled` | page 420 | TRCM ECU: a420 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_resistanceOutOfSpec` | page 420 | TRCM ECU: a420 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_deploymentLoopNumber` | page 421 | TRCM ECU: a421 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a421_resistance` | page 421 | TRCM ECU: a421 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a421_shortToGround` | page 421 | TRCM ECU: a421 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_shortToBattery` | page 421 | TRCM ECU: a421 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_shortToSelf` | page 421 | TRCM ECU: a421 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_openCircuit` | page 421 | TRCM ECU: a421 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_crossCoupled` | page 421 | TRCM ECU: a421 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_resistanceOutOfSpec` | page 421 | TRCM ECU: a421 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_deploymentLoopNumber` | page 422 | TRCM ECU: a422 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a422_resistance` | page 422 | TRCM ECU: a422 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a422_shortToGround` | page 422 | TRCM ECU: a422 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_shortToBattery` | page 422 | TRCM ECU: a422 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_shortToSelf` | page 422 | TRCM ECU: a422 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_openCircuit` | page 422 | TRCM ECU: a422 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_crossCoupled` | page 422 | TRCM ECU: a422 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_resistanceOutOfSpec` | page 422 | TRCM ECU: a422 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_deploymentLoopNumber` | page 423 | TRCM ECU: a423 deployment loop number | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `TRCM_a423_resistance` | page 423 | TRCM ECU: a423 resistance; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | 0 | Ohms | 0 to 12.7 | 255 = `SNA` | plausible |
| `TRCM_a423_shortToGround` | page 423 | TRCM ECU: a423 short to ground | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_shortToBattery` | page 423 | TRCM ECU: a423 short to battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_shortToSelf` | page 423 | TRCM ECU: a423 short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_openCircuit` | page 423 | TRCM ECU: a423 open circuit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_crossCoupled` | page 423 | TRCM ECU: a423 cross coupled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_resistanceOutOfSpec` | page 423 | TRCM ECU: a423 resistance out of spec | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`TRCM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 15 (3 signals), page 17 (1 signals), page 18 (1 signals), page 35 (6 signals), page 36 (8 signals), page 37 (11 signals), page 38 (4 signals), page 39 (4 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 65 (1 signals), page 66 (1 signals), page 78 (2 signals), page 81 (6 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (9 signals), page 88 (9 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (3 signals), page 95 (2 signals), page 96 (2 signals), page 97 (2 signals), page 98 (14 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (5 signals), page 107 (14 signals), page 108 (14 signals), page 110 (17 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (22 signals), page 117 (24 signals), page 118 (29 signals), page 119 (6 signals), page 120 (33 signals), page 332 (4 signals), page 333 (4 signals), page 334 (4 signals), page 335 (4 signals), page 336 (4 signals), page 337 (4 signals), page 338 (4 signals), page 340 (4 signals), page 341 (4 signals), page 342 (4 signals), page 343 (4 signals), page 344 (4 signals), page 345 (4 signals), page 346 (4 signals), page 347 (4 signals), page 348 (4 signals), page 349 (4 signals), page 350 (4 signals), page 351 (4 signals), page 352 (4 signals), page 353 (4 signals), page 354 (4 signals), page 355 (4 signals), page 400 (8 signals), page 401 (8 signals), page 402 (8 signals), page 403 (8 signals), page 404 (8 signals), page 405 (8 signals), page 406 (8 signals), page 408 (8 signals), page 409 (8 signals), page 410 (8 signals), page 411 (8 signals), page 412 (8 signals), page 413 (8 signals), page 414 (8 signals), page 415 (8 signals), page 416 (8 signals), page 417 (8 signals), page 418 (8 signals), page 419 (8 signals), page 420 (8 signals), page 421 (8 signals), page 422 (8 signals), page 423 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All TRCM ECU messages (TRCM)](../../trcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
