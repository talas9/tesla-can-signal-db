---
layout: default
title: "VCFRONT_alertLog (0x534) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front body controller message: alert log. Ethernet-side message VCFRONT_alertLog of Front body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 2145 signals (VCFRONT_alertID, VCFRONT_alertState, VCFRONT_a001_InternalWatchdog, VCFRONT_a002_CPUUndervoltage and 2141 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_alertLog (0x534) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Front body controller message: alert log. This page documents the 2145 signals of VCFRONT_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_alertLog` |
| Ethernet-side id | 0x534 (1332) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2145 |

## Signals of VCFRONT_alertLog

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_alertID` | selector | Front body controller: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>4 = `a004_adaptiveHeadlightsUnavailable`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>7 = `a007_coolantLevelLowDTC`<br>8 = `a008_adaptiveHeadlightsUnavailableStalk`<br>9 = `a009_LCCPurgeAttempted`<br>10 = `a010_ExtSupplyVoltError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>54 = `a054_compressorLowFlowUserFacing`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_pumpBatICLatchFault`<br>122 = `a122_pumpBatICWarning`<br>123 = `a123_pumpPtICLatchFault`<br>124 = `a124_pumpPtICWarning`<br>125 = `a125_thmlFanICLatchFault`<br>126 = `a126_thmlFanICWarning`<br>127 = `a127_vcleftEFuseTrip`<br>128 = `a128_vcrightEFuseTrip`<br>129 = `a129_pcsEFuseTrip`<br>130 = `a130_epas3pEFuseTrip`<br>131 = `a131_epas3sEFuseTrip`<br>132 = `a132_iBoosterEFuseTrip`<br>133 = `a133_espEFuseTrip`<br>134 = `a134_fusedHighEFuseTrip`<br>135 = `a135_coolantLevelLow`<br>136 = `a136_refrigDischTempSns`<br>137 = `a137_refrigDischPresSns`<br>138 = `a138_refrigSuctTempSns`<br>139 = `a139_refrigSuctPresSns`<br>140 = `a140_coolantTempPtSns`<br>141 = `a141_coolantTempBatSns`<br>142 = `a142_exvMotorFault`<br>143 = `a143_pumpBatICTransFault`<br>144 = `a144_pumpPtICTransFault`<br>145 = `a145_thmlFanICTransFault`<br>146 = `a146_pumpBatSoftStall`<br>147 = `a147_pumpPtSoftStall`<br>148 = `a148_thmlFanSoftStall`<br>149 = `a149_BLEFrontPowerCycled`<br>150 = `a150_pumpBatLowRPMCBang`<br>151 = `a151_pumpPtLowRPMCBang`<br>152 = `a152_thmlFanLowRPMCBang`<br>153 = `a153_userPresenceDisplayMismatchClrd`<br>154 = `a154_prechargeDCRData1`<br>155 = `a155_prechargeDCRData2`<br>156 = `a156_louverBlockage`<br>157 = `a157_louverBreakage`<br>158 = `a158_louverDisconnected`<br>159 = `a159_coolantValveFault`<br>160 = `a160_compressorInhibited`<br>161 = `a161_compressorSelfFault`<br>162 = `a162_compressorInhibitedContext`<br>163 = `a163_compressorDisabledFSR`<br>164 = `a164_eFuseLckoutMissing`<br>165 = `a165_unxpctdEFuseLckout`<br>166 = `a166_rightHCMMIA`<br>167 = `a167_leftHCMMIA`<br>168 = `a168_hcmShortToVBAT`<br>169 = `a169_hcmPhaseEnableFail`<br>170 = `a170_hcmUnderVoltage`<br>171 = `a171_driveBlckdByMsmtch`<br>172 = `a172_wsteHtBlckdByMsmtch`<br>173 = `a173_HVBlckdByMsmtch`<br>174 = `a174_driveNotAuthed`<br>175 = `a175_ambientTempSns`<br>176 = `a176_vehicleInSelfTest`<br>177 = `a177_mcuAudioEFuseFault`<br>178 = `a178_compLiquidPumpOut`<br>179 = `a179_highLVAmpsIntoPCS`<br>180 = `a180_DCDCNotSupportingLVBus`<br>181 = `a181_homelinkMIA`<br>182 = `a182_replaceLVBattery`<br>183 = `a183_replaceLVBattery2`<br>184 = `a184_cabinCoolingPerformanceAbnormal`<br>185 = `a185_washerFluidLow`<br>186 = `a186_noDriveChgCableCon`<br>187 = `a187_busesNotSleeping`<br>188 = `a188_sleepFailed`<br>189 = `a189_IBSMIA`<br>190 = `a190_linSchedulingInfo`<br>191 = `a191_exitDriveLowLVBusVoltage`<br>192 = `a192_vehicleLoadShed`<br>193 = `a193_mcuAudioRetry`<br>194 = `a194_iBoosterRetry`<br>195 = `a195_drveBlckdVltgeTooHgh`<br>196 = `a196_discnctdLVBattery`<br>197 = `a197_prechargeDCRData3`<br>198 = `a198_PRVCANOverterminate`<br>199 = `a199_PRVCANUndertrminate`<br>200 = `a200_vcleftSelfTestFail`<br>201 = `a201_vcrightSelfTestFail`<br>202 = `a202_pcsSelfTestFail`<br>203 = `a203_epas3pSelfTestFail`<br>204 = `a204_epas3sSelfTestFail`<br>205 = `a205_iBoosterSelfTestFail`<br>206 = `a206_espSelfTestFail`<br>207 = `a207_vbatFusdSelfTestFail`<br>208 = `a208_brakeFluidLow`<br>209 = `a209_brakeFluidSNA`<br>210 = `a210_coolantValveCalib`<br>211 = `a211_I2CFault`<br>212 = `a212_IBSOverTemp`<br>213 = `a213_LVOvercharge`<br>214 = `a214_ptPumpCompromised`<br>215 = `a215_ptPumpMIA`<br>216 = `a216_powerCutoffImminent`<br>217 = `a217_battPumpCompromised`<br>218 = `a218_socMonitorDetectedThresholdSoc`<br>219 = `a219_LVVoltFloorRchd`<br>220 = `a220_reverseBatteryFault`<br>221 = `a221_leftTurnLightFault`<br>222 = `a222_rightTurnLightFault`<br>223 = `a223_12VTempSensDiscnect`<br>224 = `a224_revBatChrgPmpFault`<br>225 = `a225_driveBlckdByShowroom`<br>226 = `a226_battPumpMIA`<br>227 = `a227_radFanCompromised`<br>228 = `a228_pumpBatFbkSanity`<br>229 = `a229_pumpPtFbkSanity`<br>230 = `a230_thmlFanFbkSanity`<br>231 = `a231_12VTempSensShort`<br>232 = `a232_lowSideControllerHighFdbk`<br>233 = `a233_autopilot1EFuseFault`<br>234 = `a234_autopilot2EFuseFault`<br>235 = `a235_ptTempSnsIrrational`<br>236 = `a236_batTempSnsIrrational`<br>237 = `a237_pumpBatChipComms`<br>238 = `a238_pumpPtChipComms`<br>239 = `a239_thmlFanChipComms`<br>240 = `a240_lowSideCompromised`<br>241 = `a241_radFanMIA`<br>242 = `a242_drveBlckdVltgeTooLow`<br>243 = `a243_LVOverchargeInstc`<br>244 = `a244_sleepBypassFault`<br>245 = `a245_pump1EFuseFault`<br>246 = `a246_pump2EFuseFault`<br>247 = `a247_evapSolenoidFault`<br>248 = `a248_voltageOutOfSpec`<br>249 = `a249_coolantValveBadMode`<br>250 = `a250_headlampsNotAimed`<br>251 = `a251_UIWakeupTrigger`<br>252 = `a252_controllerWakeup`<br>253 = `a253_maxChrgeSssionTmeout`<br>254 = `a254_pumpBatStopped`<br>255 = `a255_pumpPtStopped`<br>256 = `a256_compTornShaftSeal`<br>257 = `a257_portExpanderVOR`<br>258 = `a258_resistanceEstimationRun`<br>259 = `a259_LVVoltageDropOnHighLoadCurrent`<br>260 = `a260_deadLVBattery`<br>261 = `a261_vcleftVoltageMismatch`<br>262 = `a262_vcrightVoltageMismatch`<br>263 = `a263_pcsVoltageMismatch`<br>264 = `a264_iBoosterVoltageMismatch`<br>265 = `a265_ESPVoltageMismatch`<br>266 = `a266_EPAS3pVoltageMismatch`<br>267 = `a267_EPAS3sVoltageMismatch`<br>268 = `a268_vbatFusedVoltageMismatch`<br>269 = `a269_drveBlckdVltgeTooLow2`<br>270 = `a270_prechargeFailed`<br>271 = `a271_LVBatteryPermSupported`<br>273 = `a273_wiperFrictionModelFault`<br>274 = `a274_failureToPrechargeRisk2`<br>275 = `a275_TLVBMS_BmbCommunication`<br>276 = `a276_TLVBMS_BmbDataIntegrityLoss`<br>277 = `a277_TLVBMS_BmbStatusRegError`<br>278 = `a278_TLVBMS_BmbHwOverCurrentFault`<br>279 = `a279_refrigLiquidTempSns`<br>280 = `a280_refrigLiquidPresSns`<br>281 = `a281_alcoholInterlockBlockingDrive`<br>282 = `a282_coolantLevelSensorFault`<br>283 = `a283_thmlFanLimitedByCurrent`<br>284 = `a284_chillerExvFault`<br>285 = `a285_evaporatorExvFault`<br>286 = `a286_recircExvFault`<br>287 = `a287_lccExvFault`<br>288 = `a288_ccLeftExvFault`<br>289 = `a289_ccRightExvFault`<br>290 = `a290_leftFogLightFault`<br>291 = `a291_rightFogLightFault`<br>292 = `a292_sideMarkerLightPipeFault`<br>293 = `a293_interiorFrunkLightFault`<br>294 = `a294_leftSideRepeaterLightFault`<br>295 = `a295_rightSideRepeaterLightFault`<br>296 = `a296_turnSignalIssue`<br>297 = `a297_TLVBMS_BmbHwOverTemperatureFault`<br>298 = `a298_radiatorLowAirFlowDetected`<br>299 = `a299_homelinkConfigurationFailed`<br>300 = `a300_louverActuatorSwapDetected`<br>301 = `a301_wipersFactoryDisabled`<br>302 = `a302_wiperCommError`<br>303 = `a303_frunkAccessPostActive`<br>304 = `a304_frunkReleaseFailed`<br>305 = `a305_frunkPriOverCurrent`<br>306 = `a306_frunkPriUnderCurrent`<br>307 = `a307_frunkSecOverCurrent`<br>308 = `a308_frunkSecUnderCurrent`<br>309 = `a309_frunkEmergencyReleasePressed`<br>310 = `a310_vcleftOvertempSlope`<br>311 = `a311_vcrightOvertempSlope`<br>312 = `a312_pcsOvertempSlope`<br>313 = `a313_epas3pOvertempSlope`<br>314 = `a314_epas3sOvertempSlope`<br>315 = `a315_iboosterOvertempSlope`<br>316 = `a316_espOvertempSlope`<br>317 = `a317_vbatFusedOvertempSlope`<br>318 = `a318_vcleftOvertempMax`<br>319 = `a319_vcrightOvertempMax`<br>320 = `a320_pcsOvertempMax`<br>321 = `a321_epas3pOvertempMax`<br>322 = `a322_epas3sOvertempMax`<br>323 = `a323_iboosterOvertempMax`<br>324 = `a324_espOvertempMax`<br>325 = `a325_vbatFusedOvertempMax`<br>326 = `a326_vcleftSlowTripOC`<br>327 = `a327_vcrightSlowTripOC`<br>328 = `a328_pcsSlowTripOC`<br>329 = `a329_epas3pSlowTripOC`<br>330 = `a330_epas3sSlowTripOC`<br>331 = `a331_iboosterSlowTripOC`<br>332 = `a332_espSlowTripOC`<br>333 = `a333_vbatFusedSlowTripOC`<br>334 = `a334_vcleftFastTripOCMax`<br>335 = `a335_vcrightFastTripOCMax`<br>336 = `a336_pcsFastTripOCMax`<br>337 = `a337_epas3pFastTripOCMax`<br>338 = `a338_epas3sFastTripOCMax`<br>339 = `a339_iboosterFastTripOCMax`<br>340 = `a340_espFastTripOCMax`<br>341 = `a341_vbatFusedFastTripOCMax`<br>342 = `a342_vcleftFastTripSlope`<br>343 = `a343_vcrightFastTripSlope`<br>344 = `a344_pcsFastTripSlope`<br>345 = `a345_epas3pFastTripSlope`<br>346 = `a346_epas3sFastTripSlope`<br>347 = `a347_iboosterFastTripSlope`<br>348 = `a348_espFastTripSlope`<br>349 = `a349_vbatFusedFastTripSlope`<br>350 = `a350_espValveCurrentSenseSaturated`<br>351 = `a351_emergencyFrunkButtonPressIgnored`<br>352 = `a352_audioCurrentSpikeData`<br>353 = `a353_wiperHeaterUndercurrent`<br>354 = `a354_windshieldCameraHeaterUndercurrent`<br>355 = `a355_coolantSysLockout`<br>356 = `a356_refrigSysLockout`<br>357 = `a357_hornUndercurrent`<br>358 = `a358_hornOvercurrent`<br>359 = `a359_postPORExcessiveAh`<br>360 = `a360_ungracefulAccPlusExit`<br>361 = `a361_washerFluidLowMomentary`<br>362 = `a362_TLVBMS_AllSocCorrectionTimeout`<br>363 = `a363_TLVBMS_BleedBasedWeakShort`<br>364 = `a364_heaterTypeEstimationChanged`<br>365 = `a365_burnInRoutineEntered`<br>366 = `a366_burnInRoutineExited`<br>367 = `a367_dischargeRoutineEntered`<br>368 = `a368_dischargeRoutineExited`<br>369 = `a369_reducedPowerDischarge`<br>370 = `a370_noLVSupportSocTooLow`<br>371 = `a371_failureToPrechargeRisk`<br>372 = `a372_TLVBMS_BmbHwOverVoltageFault`<br>373 = `a373_chillerControlFlooding`<br>374 = `a374_lccInletSolenoidFault`<br>375 = `a375_refVoltageOutOfSpec`<br>376 = `a376_controllerWakeupDebug`<br>377 = `a377_wiperParkFault`<br>378 = `a378_wiperECUDebug`<br>379 = `a379_shortedCellTestRunDebug`<br>380 = `a380_chillerExvWarning`<br>381 = `a381_evaporatorExvWarning`<br>382 = `a382_recircExvWarning`<br>383 = `a383_lccExvWarning`<br>384 = `a384_ccLeftExvWarning`<br>385 = `a385_ccRightExvWarning`<br>386 = `a386_exvMotorWarning`<br>387 = `a387_shortedCellInstc`<br>388 = `a388_shortedCell`<br>389 = `a389_frunkInhibitingReleaseAtSpeed`<br>390 = `a390_heatPumpModeConvergence`<br>391 = `a391_frunkLatchSwitchFault`<br>392 = `a392_TLVBMS_BmbHwUnderVoltageFault`<br>393 = `a393_ambientTempNetworkSna`<br>394 = `a394_pressureSensorCheckFault`<br>395 = `a395_pressureSensorCheckInconclusive`<br>396 = `a396_coolantLevelLowUserFacing`<br>397 = `a397_temperatureSensorCheckFault`<br>398 = `a398_tempSensorCheckInconclusive`<br>399 = `a399_frunkNeverReportedOpen`<br>400 = `a400_TLVBMS_BmbVrefBad`<br>401 = `a401_deadLVMinimalAhDischarged`<br>402 = `a402_LVBatteryCannotSupportVehicle`<br>403 = `a403_chargeExitHardCurrentLimit`<br>404 = `a404_resistanceEstimationHardFailure`<br>405 = `a405_dcrData1`<br>406 = `a406_dcrData2`<br>407 = `a407_dcrMilliOhmsAboveThreshold`<br>408 = `a408_standbyChargeProfileHardExit`<br>409 = `a409_invalidConfiguration`<br>410 = `a410_LVBatteryDataCollection1`<br>411 = `a411_LVBatteryDataCollection2`<br>412 = `a412_dcrData3`<br>413 = `a413_TLVBMS_BmbVrefWarning`<br>414 = `a414_prechargeLVLoadReduction`<br>415 = `a415_prechargeLVLoadReduction2`<br>416 = `a416_TLVBMS_BrickOverDischarged`<br>417 = `a417_TLVBMS_BrickOverVoltageFault`<br>418 = `a418_TLVBMS_BrickOverVoltageWarning`<br>419 = `a419_TLVBMS_BrickSocLow`<br>420 = `a420_holidayParty`<br>421 = `a421_holidayPartyUserGenerated`<br>422 = `a422_waitForSyncTimedOut`<br>423 = `a423_TLVBMS_BrickUnderVoltageFault`<br>424 = `a424_TLVBMS_BrickUnderVoltageOcv`<br>425 = `a425_TLVBMS_BusVoltageTooHigh`<br>426 = `a426_TLVBMS_BusVoltageTooLow`<br>427 = `a427_TLVBMS_CacChange`<br>428 = `a428_TLVBMS_CacImbalance`<br>429 = `a429_TLVBMS_CapacityTestResults`<br>430 = `a430_TLVBMS_ChargeCurrentLimitExceeded`<br>431 = `a431_TLVBMS_ChargeOverCurrent`<br>432 = `a432_TLVBMS_ChargeRegulationFault`<br>433 = `a433_TLVBMS_ConfigFromBmbModIdFailed`<br>434 = `a434_TLVBMS_ConfigInitFailed`<br>435 = `a435_TLVBMS_DchgCurrentLimitExceeded`<br>436 = `a436_TLVBMS_DischargeOverCurrent`<br>437 = `a437_TLVBMS_NvmRegistrationError`<br>438 = `a438_TLVBMS_PackOverTemperatureFault`<br>439 = `a439_TLVBMS_PackOverTemperatureWarning`<br>440 = `a440_TLVBMS_PackSNInvalidForNvm`<br>441 = `a441_TLVBMS_ResetNeededForNvmPackSwap`<br>442 = `a442_TLVBMS_SocChange`<br>443 = `a443_TLVBMS_BmbDieOverTemperature`<br>444 = `a444_drv8703Fault`<br>445 = `a445_drv8703SpiFaultDBG`<br>446 = `a446_cabinHVACUnavailableContext`<br>447 = `a447_cabinHVACUnavailable`<br>448 = `a448_gtwSteeringBtnReset`<br>449 = `a449_hornSwitchStuckOn`<br>450 = `a450_hornSwitchNotPressedFactory`<br>451 = `a451_refrigerantNotCommissioned`<br>452 = `a452_dischargePresSensIntermittent`<br>453 = `a453_dischargeTempSensIntermittent`<br>454 = `a454_suctionPresSensIntermittent`<br>455 = `a455_suctionTempSensIntermittent`<br>456 = `a456_liquidPresSensIntermittent`<br>457 = `a457_liquidTempSensIntermittent`<br>458 = `a458_grosslyLowRefrigerant`<br>459 = `a459_thermalFillAndDrive`<br>460 = `a460_hardIsentropicTdFailed`<br>461 = `a461_TLVBMS_SocHighAhError`<br>462 = `a462_LVBMSFault`<br>463 = `a463_frunkSensorService`<br>464 = `a464_highFlowIndexHighSubcoolFlagged`<br>465 = `a465_lowFlowIndexHighSubcoolFlagged`<br>466 = `a466_highFlowIndexLowSubcoolFlagged`<br>467 = `a467_lowPowerIndexFlagged`<br>468 = `a468_highPowerIndexFlagged`<br>469 = `a469_prvPopDetected`<br>470 = `a470_implausiblePdPlDetected`<br>471 = `a471_hcm5Debug`<br>472 = `a472_leftHeadlampRangeUpdate`<br>473 = `a473_rightHeadlampRangeUpdate`<br>474 = `a474_leftHeadlampInternalError`<br>475 = `a475_rightHeadlampInternalError`<br>476 = `a476_LVBMSMIA`<br>477 = `a477_LVBatteryUnrecoverableByVehicle`<br>478 = `a478_LVBMS_MOSFET_Open`<br>479 = `a479_LVBMS_ECPA_NotClosed`<br>480 = `a480_vnf1048Fault`<br>481 = `a481_vnf1048SelfTestFailure`<br>482 = `a482_rightHeadlampMigrationDebug`<br>483 = `a483_leftHeadlampStepperMotorFault`<br>484 = `a484_headlampLevelingRideHeightDebug`<br>485 = `a485_leftHeadlampMigrationDebug`<br>486 = `a486_mcuGraphicsEFuseFault`<br>487 = `a487_leftHeadlampLastPositionUpdate`<br>488 = `a488_rightHeadlampStepperMotorFault`<br>489 = `a489_ValveStuckFlagged`<br>490 = `a490_coolantPumpsNotIdentified`<br>491 = `a491_rightHeadlampLastPositionUpdate`<br>492 = `a492_TLVBMS_SocImbalance`<br>493 = `a493_TLVBMS_SocImbalanceWarning`<br>494 = `a494_LVBatteryTempBlockingOTA`<br>495 = `a495_LVBatteryRecoveryBlocked`<br>496 = `a496_LVBatteryExitDriveWarning`<br>497 = `a497_LVBatteryWarnDisconnect`<br>498 = `a498_TLVBMS_ImpedanceTestResults`<br>499 = `a499_loadShedPumpFlowRequest`<br>500 = `a500_eFuseASICStateMismatch`<br>501 = `a501_vnf1048ConfigurationMismatch`<br>502 = `a502_TLVBMS_WeakShortImpedance`<br>503 = `a503_TLVBMS_BrickExtendedOvFault`<br>504 = `a504_airInRefrigerantDetected`<br>505 = `a505_BLEFrontUnderVoltage`<br>506 = `a506_invalidRefrigerantSystemConfig`<br>507 = `a507_leftHeadlampAimingFault`<br>508 = `a508_TLVBMS_ImpedanceGrowth`<br>509 = `a509_vcrightEFuseLoadShed`<br>510 = `a510_LVBatteryRecoveryTimeout`<br>511 = `a511_DCDCSaturationLoadShed`<br>512 = `a512_LVBMSFault_MOS_Open_hardwareOC`<br>513 = `a513_LVBMSFault_MOS_Open_chgOC`<br>514 = `a514_LVBMSFault_MOS_Open_cellUV`<br>515 = `a515_LVBMSFault_MOS_Open_cellOV`<br>516 = `a516_hibernationActive`<br>517 = `a517_hibernationRecovery`<br>518 = `a518_LVBMSFault_MOS_Open_packOV`<br>519 = `a519_leftHeadlampInternalErrorV2`<br>520 = `a520_rightHeadlampInternalErrorV2`<br>521 = `a521_vcleftEFuseLoadShed`<br>522 = `a522_hibernationActiveLogCapture`<br>523 = `a523_eFuseThresholdsIncorrect`<br>524 = `a524_rightHeadlampAimingFault`<br>525 = `a525_LVBatterySWMisconfiguration`<br>526 = `a526_pcbaOverTemperature`<br>527 = `a527_LVBatteryCellImbalance`<br>528 = `a528_LVBatteryCommsDiscnctd`<br>529 = `a529_discnctdBatteryStateUnknown`<br>530 = `a530_sharpCurrentRise`<br>531 = `a531_lowPowerIndexFlaggedUserFacing`<br>532 = `a532_gtwMIAInDrive`<br>533 = `a533_TLVBMS_MosfetOverTemperatureFault`<br>534 = `a534_chillerExvCalibInitDebug`<br>535 = `a535_evapExvCalibInitDebug`<br>536 = `a536_recircExvCalibInitDebug`<br>537 = `a537_lccExvCalibInitDebug`<br>538 = `a538_cclExvCalibInitDebug`<br>539 = `a539_ccrExvCalibInitDebug`<br>540 = `a540_radiatorSteamDetected`<br>541 = `a541_LVBatteryChargeOCLevel1`<br>542 = `a542_refrigerantReclaim`<br>543 = `a543_compressorLowFlowDeliveryDetected`<br>544 = `a544_LVBatteryCommsBusTurnedOff`<br>545 = `a545_LVBatteryTypeUnknown`<br>546 = `a546_leftLowOrHighBeamLightCondition`<br>547 = `a547_postCrashLoadShed`<br>548 = `a548_HVFaultLoadShed`<br>549 = `a549_leftHeadlampInternalErrorV3`<br>550 = `a550_ambientTempDelta`<br>551 = `a551_leftHeadlampSoftShort`<br>552 = `a552_eFuseSelfTestFailure`<br>553 = `a553_rightHeadlampSoftShort`<br>555 = `a555_LVBatteryCellRebalancing`<br>556 = `a556_falseTriggerOfDiscnctdBatteryTest`<br>557 = `a557_rightHeadlampInternalErrorV3`<br>558 = `a558_rightHeadlampAimingDebug`<br>559 = `a559_LVBatteryLowSOC`<br>560 = `a560_compressorHighSuperheat`<br>561 = `a561_LVBMSEFuseOvertemperature`<br>562 = `a562_LVBMSModuleOvertemperature`<br>563 = `a563_chargePortDoorOpenBlockedByBrake`<br>564 = `a564_leftHeadlampAimingDebug`<br>565 = `a565_userPresenceDisplayStateMismatch`<br>566 = `a566_leftFrontTurnLightFault`<br>567 = `a567_rightFrontTurnLightFault`<br>568 = `a568_leftDaytimeRunningLightFault`<br>569 = `a569_rightDaytimeRunningLightFault`<br>570 = `a570_headlampsAdaptedToLeftHandTraffic`<br>571 = `a571_headlampsAdaptedToRightHandTraffic`<br>572 = `a572_hvacCompressorEFuseTrip`<br>573 = `a573_radarEFuseTrip`<br>574 = `a574_frontDriveInverterEFuseTrip`<br>575 = `a575_frontOilPumpEFuseTrip`<br>576 = `a576_mcuLogicEFuseTrip`<br>577 = `a577_tasEFuseTrip`<br>578 = `a578_vbatFusedLowCurrentFeedEFuseTrip`<br>579 = `a579_leftHeadlightEFuseTrip`<br>580 = `a580_rightHeadlightEFuseTrip`<br>581 = `a581_windshieldWiperEFuseTrip`<br>582 = `a582_goodForPCSPowerCycle`<br>583 = `a583_frunkSwitchGroupDisagreementDebug`<br>584 = `a584_frunkSwitchGroupDebug`<br>585 = `a585_bothHeadlampsInternalError`<br>586 = `a586_rightLowOrHighBeamLightCondition`<br>587 = `a587_externalLVPowerSupply`<br>588 = `a588_vcleftPwrRationalityCurve`<br>589 = `a589_vcleftFastBlowDetection`<br>590 = `a590_vcrightPwrRationalityCurve`<br>591 = `a591_vcrightFastBlowDetection`<br>592 = `a592_vcleftCurvePowerCutoff`<br>593 = `a593_vcleftFastBlowPowerCutoff`<br>594 = `a594_virtualPitchConversionDebug`<br>595 = `a595_voltageSensorMismatch`<br>596 = `a596_vcrightCurvePowerCutoff`<br>597 = `a597_vcrightFastBlowPowerCutoff`<br>598 = `a598_eFuseSelfTestFailureService`<br>599 = `a599_LVBatteryTypeUnsupported`<br>600 = `a600_currentSensorMismatch`<br>601 = `a601_headlampRetryInfo`<br>605 = `a605_sleepBypassPowerOff`<br>606 = `a606_chillerBattHeatingExit`<br>607 = `a607_sleepPowerDebug`<br>608 = `a608_TLVBMS_BleedFetTest`<br>609 = `a609_autopilotDriveNotAuthed`<br>610 = `a610_frunkOpenFailureMetricSet`<br>611 = `a611_poorRadiatorHeatRejection`<br>612 = `a612_LVUnhealthyLoadShed`<br>613 = `a613_selfTestsBlockingDrive`<br>615 = `a615_TLVBMS_BatteryHeaterFault`<br>618 = `a618_cabinCoolingCapacityLimited`<br>619 = `a619_frunkSwitchReleaseTimeDBG`<br>620 = `a620_pumpAirLock`<br>621 = `a621_coolantAirPurgeIncomplete`<br>622 = `a622_pumpDetectsLowCoolantFlow`<br>623 = `a623_LVUnhealthy`<br>624 = `a624_rightHeadlampInternalErrorV4`<br>625 = `a625_leftHeadlampInternalErrorV4`<br>626 = `a626_LVBatteryResistanceIncrease`<br>627 = `a627_LVBatteryUnrecoverableByAnyDevice`<br>630 = `a630_leftHeadlampFactoryFault`<br>631 = `a631_rightHeadlampFactoryFault`<br>649 = `a649_persistAccPortPowerReqOverridden` | plausible |
| `VCFRONT_alertState` |  | Front body controller: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCFRONT_a001_InternalWatchdog` | page 1 | Front body controller: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a002_CPUUndervoltage` | page 2 | Front body controller: a002 CPU undervoltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a002_PowerOnReset` | page 2 | Front body controller: a002 power on reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_APPWatchdogFaultOrMIA` | page 4 | Front body controller: a004 APP watchdog fault or MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_DASHighLowBeamDecisionSNA` | page 4 | Front body controller: a004 DAS high low beam decision SNA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_DASAdaptiveHighBeamFault` | page 4 | Front body controller: a004 DAS adaptive high beam fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_DASMatrixColumnMsgMIA` | page 4 | Front body controller: a004 DAS matrix column msg MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_DASBendAngleMsgMIA` | page 4 | Front body controller: a004 DAS bend angle msg MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a004_EPAS3PNotInSpecOrMIA` | page 4 | Front body controller: a004 EPAS3 p not in spec or MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_APPWatchdogFaultOrMIA` | page 8 | Front body controller: a008 APP watchdog fault or MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_DASHighLowBeamDecisionSNA` | page 8 | Front body controller: a008 DAS high low beam decision SNA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_DASAdaptiveHighBeamFault` | page 8 | Front body controller: a008 DAS adaptive high beam fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_DASMatrixColumnMsgMIA` | page 8 | Front body controller: a008 DAS matrix column msg MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_DASBendAngleMsgMIA` | page 8 | Front body controller: a008 DAS bend angle msg MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a008_EPAS3PNotInSpecOrMIA` | page 8 | Front body controller: a008 EPAS3 p not in spec or MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a010_UnderVoltageDetected` | page 10 | Front body controller: a010 under voltage detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a010_UnderVoltageTimeout` | page 10 | Front body controller: a010 under voltage timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a015_NVMMMemOverflow` | page 15 | Front body controller: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a015_NVMMFilesystemError` | page 15 | Front body controller: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a015_NVMMRecordIDError` | page 15 | Front body controller: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a057_VEH_cpControl` | page 57 | Front body controller: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a059_voltageDrop` | page 59 | Front body controller: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a059_resistanceEstimate` | page 59 | Front body controller: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCFRONT_a059_current` | page 59 | Front body controller: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCFRONT_a063_switchChannel` | page 63 | Front body controller: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a063_switchType` | page 63 | Front body controller: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a063_ADCVoltage` | page 63 | Front body controller: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCFRONT_a063_disconnected` | page 63 | Front body controller: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a063_indeterminate` | page 63 | Front body controller: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a063_stuckActive` | page 63 | Front body controller: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a063_faulted` | page 63 | Front body controller: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a082_RIPC_epbPrivateState` | page 82 | Front body controller: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a082_RIPC_remoteHSD` | page 82 | Front body controller: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a082_RIPC_railStatus` | page 82 | Front body controller: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a082_RIPC_remoteMux` | page 82 | Front body controller: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a083_LIPC_epbPrivateState` | page 83 | Front body controller: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a083_LIPC_remoteHSD` | page 83 | Front body controller: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a083_LIPC_railStatus` | page 83 | Front body controller: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a083_LIPC_HSDFaults` | page 83 | Front body controller: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a084_CH_StatusC` | page 84 | Front body controller: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a085_PARTY_buttonStatus` | page 85 | Front body controller: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_LVBMS_statusHigh` | page 86 | Front body controller: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_LVBMS_statusLow` | page 86 | Front body controller: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_status` | page 86 | Front body controller: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_12VBatteryStatus` | page 86 | Front body controller: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_LVPowerState` | page 86 | Front body controller: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_lightStatus` | page 86 | Front body controller: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_systemStatus` | page 86 | Front body controller: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_thermalStatus` | page 86 | Front body controller: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a086_VEH_vehNm` | page 86 | Front body controller: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_VEH_temperature` | page 87 | Front body controller: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_VEH_thermalControl` | page 87 | Front body controller: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_VEH_torque` | page 87 | Front body controller: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_VEH_status` | page 87 | Front body controller: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_PARTY_torque` | page 87 | Front body controller: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_PARTY_status` | page 87 | Front body controller: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_PARTY_temperature` | page 87 | Front body controller: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a087_PARTY_thermalControl` | page 87 | Front body controller: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_VEH_temperature` | page 88 | Front body controller: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_VEH_thermalControl` | page 88 | Front body controller: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_VEH_torque` | page 88 | Front body controller: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_VEH_status` | page 88 | Front body controller: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_PARTY_torque` | page 88 | Front body controller: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_PARTY_status` | page 88 | Front body controller: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_PARTY_temperature` | page 88 | Front body controller: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a088_PARTY_thermalControl` | page 88 | Front body controller: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_PARTY_party1` | page 89 | Front body controller: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_PARTY_status` | page 89 | Front body controller: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_VEH_status` | page 89 | Front body controller: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_BDY_party1` | page 89 | Front body controller: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_BDY_status` | page 89 | Front body controller: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_CH_status` | page 89 | Front body controller: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_CH_party1` | page 89 | Front body controller: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_CH_party3` | page 89 | Front body controller: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_VEH_party1` | page 89 | Front body controller: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a089_VEH_party3` | page 89 | Front body controller: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a091_VEH_faultsAndExtras` | page 91 | Front body controller: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a091_VEH_info` | page 91 | Front body controller: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a091_VEH_state` | page 91 | Front body controller: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a092_VEH_restraintStatus` | page 92 | Front body controller: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a092_VEH_switchStatus` | page 92 | Front body controller: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a092_VEH_seatStatus2` | page 92 | Front body controller: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a092_VEH_vehNm` | page 92 | Front body controller: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a093_VEH_restraintStatus` | page 93 | Front body controller: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a093_VEH_switchStatus` | page 93 | Front body controller: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a093_VEH_seatStatus2` | page 93 | Front body controller: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a093_VEH_vehNm` | page 93 | Front body controller: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a094_VEH_sysStatus` | page 94 | Front body controller: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a094_PARTY_sysStatus` | page 94 | Front body controller: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a095_PT_ptNm` | page 95 | Front body controller: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a095_PT_status` | page 95 | Front body controller: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a096_VEH_status` | page 96 | Front body controller: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a096_CH_status` | page 96 | Front body controller: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_CH_torque` | page 98 | Front body controller: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_VEH_hvStatus` | page 98 | Front body controller: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_VEH_status` | page 98 | Front body controller: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_VEH_thermalControl` | page 98 | Front body controller: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_VEH_temperature` | page 98 | Front body controller: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_VEH_torque` | page 98 | Front body controller: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PARTY_status` | page 98 | Front body controller: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PARTY_temperature` | page 98 | Front body controller: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PARTY_thermalControl` | page 98 | Front body controller: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PARTY_torque` | page 98 | Front body controller: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PT_thermalControl` | page 98 | Front body controller: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a098_PT_temperature` | page 98 | Front body controller: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a099_VEH_oocStatus` | page 99 | Front body controller: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a100_VEH` | page 100 | Front body controller: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a100_PARTY` | page 100 | Front body controller: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a100_PT` | page 100 | Front body controller: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a100_CH` | page 100 | Front body controller: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a100_OBD` | page 100 | Front body controller: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a101_VEH_state` | page 101 | Front body controller: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a101_PARTY_locState` | page 101 | Front body controller: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a101_LIPC_externalWatchdogHeartBeat` | page 101 | Front body controller: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a101_VEH_locState` | page 101 | Front body controller: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a101_BDY_locState` | page 101 | Front body controller: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a102_VEH_faultsAndExtras` | page 102 | Front body controller: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a102_VEH_feedbackStatus` | page 102 | Front body controller: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a102_VEH_sensorStatus` | page 102 | Front body controller: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a102_VEH_rods` | page 102 | Front body controller: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_VEH_hvsNm` | page 103 | Front body controller: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_VEH_vehNm` | page 103 | Front body controller: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_VEH_status` | page 103 | Front body controller: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_PT_ptNm` | page 103 | Front body controller: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_PT_status` | page 103 | Front body controller: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a103_VEH_evseStatus` | page 103 | Front body controller: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a105_VEH_states` | page 105 | Front body controller: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a105_VEH_chNm` | page 105 | Front body controller: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a105_VEH_dampingStates` | page 105 | Front body controller: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_VEH_dcdcStatus` | page 106 | Front body controller: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_VEH_thermalControl` | page 106 | Front body controller: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_VEH_thermalInterface` | page 106 | Front body controller: a106 VEH thermal interface | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_VEH_dcdcRailStatus` | page 106 | Front body controller: a106 VEH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_CH_dcdcRailStatus` | page 106 | Front body controller: a106 CH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a106_CH_alertMatrix` | page 106 | Front body controller: a106 CH alert matrix | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_hvsNm` | page 107 | Front body controller: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_vehNm` | page 107 | Front body controller: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_status` | page 107 | Front body controller: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_thermalStatus` | page 107 | Front body controller: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_thermalStatus2` | page 107 | Front body controller: a107 VEH thermal status2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_bmbMinMax` | page 107 | Front body controller: a107 VEH bmb min max | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_powerAvailable` | page 107 | Front body controller: a107 VEH power available | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_PT_ptNm` | page 107 | Front body controller: a107 PT pt nm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_PT_status` | page 107 | Front body controller: a107 PT status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_PT_thermalStatus` | page 107 | Front body controller: a107 PT thermal status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_PT_socStatus` | page 107 | Front body controller: a107 PT soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_socStatus` | page 107 | Front body controller: a107 VEH soc status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_packConfig` | page 107 | Front body controller: a107 VEH pack config | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_energyStatus` | page 107 | Front body controller: a107 VEH energy status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a107_VEH_chargeInfo` | page 107 | Front body controller: a107 VEH charge info | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_VEH_hvStatus` | page 108 | Front body controller: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_VEH_temperature` | page 108 | Front body controller: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_VEH_thermalControl` | page 108 | Front body controller: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_VEH_torque` | page 108 | Front body controller: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_VEH_status` | page 108 | Front body controller: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PARTY_torque` | page 108 | Front body controller: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PARTY_status` | page 108 | Front body controller: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PARTY_temperature` | page 108 | Front body controller: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PARTY_thermalControl` | page 108 | Front body controller: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PT_temperature` | page 108 | Front body controller: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a108_PT_thermalControl` | page 108 | Front body controller: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_PARTY_status` | page 109 | Front body controller: a109 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_PARTY_inertial2` | page 109 | Front body controller: a109 PARTY inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_PARTY_nearDeploy` | page 109 | Front body controller: a109 PARTY near deploy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_PARTY_collision` | page 109 | Front body controller: a109 PARTY collision | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_VEH_status` | page 109 | Front body controller: a109 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_VEH_imuOffsets` | page 109 | Front body controller: a109 VEH imu offsets | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_PARTY_inertial1` | page 109 | Front body controller: a109 PARTY inertial1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_BDY_imuOffsets` | page 109 | Front body controller: a109 BDY imu offsets | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_BDY_inertial1` | page 109 | Front body controller: a109 BDY inertial1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_BDY_inertial2` | page 109 | Front body controller: a109 BDY inertial2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_BDY_status` | page 109 | Front body controller: a109 BDY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_VEH_inertial1` | page 109 | Front body controller: a109 VEH inertial1 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_VEH_inertial2` | page 109 | Front body controller: a109 VEH inertial2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_CH_inertial1` | page 109 | Front body controller: a109 CH inertial1 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_CH_inertial2` | page 109 | Front body controller: a109 CH inertial2 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a109_CH_status` | page 109 | Front body controller: a109 CH status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a110_VEH_status` | page 110 | Front body controller: a110 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_carState` | page 110 | Front body controller: a110 VEH car state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_carConfig` | page 110 | Front body controller: a110 VEH car config | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_time` | page 110 | Front body controller: a110 VEH time | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_updateStatus` | page 110 | Front body controller: a110 VEH update status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_vehNm` | page 110 | Front body controller: a110 VEH veh nm | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_mismatchFault` | page 110 | Front body controller: a110 VEH mismatch fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_vin` | page 110 | Front body controller: a110 VEH vin | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_bmpDebug` | page 110 | Front body controller: a110 VEH bmp debug | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_gearControl` | page 110 | Front body controller: a110 VEH gear control | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_VEH_canLogAvailability` | page 110 | Front body controller: a110 VEH can log availability | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_airbagCutoffStatus` | page 110 | Front body controller: a110 CH airbag cutoff status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_carConfig` | page 110 | Front body controller: a110 CH car config | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_carState` | page 110 | Front body controller: a110 CH car state | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_vin` | page 110 | Front body controller: a110 CH vin | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_chNm` | page 110 | Front body controller: a110 CH ch nm | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_CH_epochTimeGtw` | page 110 | Front body controller: a110 CH epoch time gtw | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a111_VEH_internalStatus` | page 111 | Front body controller: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_VEH_status` | page 111 | Front body controller: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_VEH_vehNm` | page 111 | Front body controller: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_RIPC_LVPowerState` | page 111 | Front body controller: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_RIPC_epbPrivateState` | page 111 | Front body controller: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_RIPC_railStatus` | page 111 | Front body controller: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_RIPC_remoteADC` | page 111 | Front body controller: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_RIPC_switchStatus` | page 111 | Front body controller: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_VEH_LVPowerState` | page 111 | Front body controller: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_VEH_seatStatus` | page 111 | Front body controller: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_PARTY_status` | page 111 | Front body controller: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a111_CH_status` | page 111 | Front body controller: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_VEH_internalStatus` | page 112 | Front body controller: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_VEH_status` | page 112 | Front body controller: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_VEH_vehNm` | page 112 | Front body controller: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_LIPC_LVPowerState` | page 112 | Front body controller: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_LIPC_epbPrivateState` | page 112 | Front body controller: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_LIPC_railStatus` | page 112 | Front body controller: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_LIPC_remoteADC` | page 112 | Front body controller: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_LIPC_switchStatus` | page 112 | Front body controller: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_VEH_LVPowerState` | page 112 | Front body controller: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_PARTY_status` | page 112 | Front body controller: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a112_CH_status` | page 112 | Front body controller: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_status` | page 114 | Front body controller: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_wheelSpeeds` | page 114 | Front body controller: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_VEH_wheelSpeeds` | page 114 | Front body controller: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_CH_wheelSpeeds` | page 114 | Front body controller: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_party3` | page 114 | Front body controller: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_VEH_party3` | page 114 | Front body controller: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_VEH_status` | page 114 | Front body controller: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_wheelRotation` | page 114 | Front body controller: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_CH_wheelRotation` | page 114 | Front body controller: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_VEH_wheelRotation` | page 114 | Front body controller: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_brakeTorque` | page 114 | Front body controller: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_PARTY_offsets` | page 114 | Front body controller: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_BDY_offsets` | page 114 | Front body controller: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_BDY_party3` | page 114 | Front body controller: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_BDY_status` | page 114 | Front body controller: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_BDY_wheelRotation` | page 114 | Front body controller: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_BDY_wheelSpeeds` | page 114 | Front body controller: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_CH_party1` | page 114 | Front body controller: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_CH_party3` | page 114 | Front body controller: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a114_CH_status` | page 114 | Front body controller: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_VEH_vehNm` | page 115 | Front body controller: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_VEH_authentication` | page 115 | Front body controller: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_VEH_BLEResetRequest` | page 115 | Front body controller: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_VEH_requests` | page 115 | Front body controller: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_VEH_requests2` | page 115 | Front body controller: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_REM_authentication` | page 115 | Front body controller: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_UI_corianderVehicleControl` | page 115 | Front body controller: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a115_CH_TPMSDisplay` | page 115 | Front body controller: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_PARTY_epbmStatus` | page 116 | Front body controller: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_vehNm` | page 116 | Front body controller: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_hvacRequest` | page 116 | Front body controller: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_hvacStatus` | page 116 | Front body controller: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_LVPowerState` | page 116 | Front body controller: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_lightStatus` | page 116 | Front body controller: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_seatStatus` | page 116 | Front body controller: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_thsStatus` | page 116 | Front body controller: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_doorStatus` | page 116 | Front body controller: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_seatHeatStatus` | page 116 | Front body controller: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_restraintStatus` | page 116 | Front body controller: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_switchStatus` | page 116 | Front body controller: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_logging1Hz` | page 116 | Front body controller: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_seatStatus2` | page 116 | Front body controller: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_status` | page 116 | Front body controller: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_thermalCommand` | page 116 | Front body controller: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_VEH_windowStatus` | page 116 | Front body controller: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_PARTY_restraintStatus` | page 116 | Front body controller: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_PARTY_doorStatus` | page 116 | Front body controller: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_BDY_epbmStatus` | page 116 | Front body controller: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a116_BDY_restraintStatus` | page 116 | Front body controller: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_BDY_epbmStatus` | page 117 | Front body controller: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_BDY_restraintStatus` | page 117 | Front body controller: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_prndStatus` | page 117 | Front body controller: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_PARTY_epbmStatus` | page 117 | Front body controller: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_vehNm` | page 117 | Front body controller: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_hvacBlowerFdb` | page 117 | Front body controller: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_LVPowerState` | page 117 | Front body controller: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_restraintStatus` | page 117 | Front body controller: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_lightStatus` | page 117 | Front body controller: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_seatStatus` | page 117 | Front body controller: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_BDY_falconSwitchStatus` | page 117 | Front body controller: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_doorStatus` | page 117 | Front body controller: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_doorStatus2` | page 117 | Front body controller: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_windowStatus` | page 117 | Front body controller: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_switchStatus` | page 117 | Front body controller: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_intrusionSensorStatus` | page 117 | Front body controller: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_liftgateStatus` | page 117 | Front body controller: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_seatStatus2` | page 117 | Front body controller: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_PARTY_restraintStatus` | page 117 | Front body controller: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_thermalStatus` | page 117 | Front body controller: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_PARTY_doorStatus` | page 117 | Front body controller: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_VEH_status` | page 117 | Front body controller: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a117_PARTY_prndStatus` | page 117 | Front body controller: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_vehNm` | page 118 | Front body controller: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_lighting` | page 118 | Front body controller: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_sensors` | page 118 | Front body controller: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_status` | page 118 | Front body controller: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_okToUseHighPwr` | page 118 | Front body controller: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_LVPowerState` | page 118 | Front body controller: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_coolant` | page 118 | Front body controller: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_vehicleStatus` | page 118 | Front body controller: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_12VBatteryStatus` | page 118 | Front body controller: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_systemStatus` | page 118 | Front body controller: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_LVPowerState` | page 118 | Front body controller: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_outputPowerStatus` | page 118 | Front body controller: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_vehicleTime` | page 118 | Front body controller: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_thermalCommand` | page 118 | Front body controller: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_LVPowerState` | page 118 | Front body controller: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_sensors` | page 118 | Front body controller: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_sensors` | page 118 | Front body controller: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_interNodeResistance` | page 118 | Front body controller: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_lighting` | page 118 | Front body controller: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_VEH_lightStatus` | page 118 | Front body controller: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_vehNm` | page 118 | Front body controller: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_12VBatteryStatus` | page 118 | Front body controller: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_LVBMS_statusHigh` | page 118 | Front body controller: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_CH_alertMatrix` | page 118 | Front body controller: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_BDY_outputPowerStatus` | page 118 | Front body controller: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_BDY_vehicleTime` | page 118 | Front body controller: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | Front body controller: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | Front body controller: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_VEH_steerAngle` | page 119 | Front body controller: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_VEH_leftStalk` | page 119 | Front body controller: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_VEH_rightStalk` | page 119 | Front body controller: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_PARTY_rightStalk` | page 119 | Front body controller: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_CH_steerAngle` | page 119 | Front body controller: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a119_PARTY_steerAngle` | page 119 | Front body controller: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_chassisCntl` | page 120 | Front body controller: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_systemStatus` | page 120 | Front body controller: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_CH_chassisCntl` | page 120 | Front body controller: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_systemStatus` | page 120 | Front body controller: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_torque` | page 120 | Front body controller: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_torque` | page 120 | Front body controller: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_locStatus` | page 120 | Front body controller: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_speed` | page 120 | Front body controller: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_speed` | page 120 | Front body controller: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_status` | page 120 | Front body controller: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PT_speed` | page 120 | Front body controller: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PT_systemStatus` | page 120 | Front body controller: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_vehicleEstimates` | page 120 | Front body controller: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_aggregatedAxleSpeed` | page 120 | Front body controller: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_aggregatedAxleSpeed` | page 120 | Front body controller: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_systemPower` | page 120 | Front body controller: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PT_systemPower` | page 120 | Front body controller: a120 PT system power | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_stalklessInterfaces` | page 120 | Front body controller: a120 PARTY stalkless interfaces | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_CH_speed` | page 120 | Front body controller: a120 CH speed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_estimatedBrakeTemp` | page 120 | Front body controller: a120 VEH estimated brake temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_prndControl` | page 120 | Front body controller: a120 PARTY prnd control | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_PARTY_locStatus2` | page 120 | Front body controller: a120 PARTY loc status2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_chassisCntl` | page 120 | Front body controller: a120 VEH chassis cntl | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_locStatus` | page 120 | Front body controller: a120 VEH loc status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_locStatus2` | page 120 | Front body controller: a120 VEH loc status2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_prndControl` | page 120 | Front body controller: a120 VEH prnd control | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a120_VEH_vehicleEstimates` | page 120 | Front body controller: a120 VEH vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a121_overCurrentError` | page 121 | Front body controller: a121 over current error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a121_fetShortCircuit` | page 121 | Front body controller: a121 fet short circuit | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a121_lockedRotor` | page 121 | Front body controller: a121 locked rotor | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a122_junctionTempWarning` | page 122 | Front body controller: a122 junction temp warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a122_junctionOverTemp` | page 122 | Front body controller: a122 junction over temp | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a122_startUpOperation` | page 122 | Front body controller: a122 start up operation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a122_lossOfSpeedLock` | page 122 | Front body controller: a122 loss of speed lock | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a122_vccUnderVoltage` | page 122 | Front body controller: a122 vcc under voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a123_overCurrentError` | page 123 | Front body controller: a123 over current error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a123_fetShortCircuit` | page 123 | Front body controller: a123 fet short circuit | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a123_lockedRotor` | page 123 | Front body controller: a123 locked rotor | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a124_junctionTempWarning` | page 124 | Front body controller: a124 junction temp warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a124_junctionOverTemp` | page 124 | Front body controller: a124 junction over temp | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a124_startUpOperation` | page 124 | Front body controller: a124 start up operation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a124_lossOfSpeedLock` | page 124 | Front body controller: a124 loss of speed lock | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a124_vccUnderVoltage` | page 124 | Front body controller: a124 vcc under voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a125_overCurrentError` | page 125 | Front body controller: a125 over current error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a125_fetShortCircuit` | page 125 | Front body controller: a125 fet short circuit | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a125_lockedRotor` | page 125 | Front body controller: a125 locked rotor | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a126_junctionTempWarning` | page 126 | Front body controller: a126 junction temp warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a126_junctionOverTemp` | page 126 | Front body controller: a126 junction over temp | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a126_startUpOperation` | page 126 | Front body controller: a126 start up operation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a126_lossOfSpeedLock` | page 126 | Front body controller: a126 loss of speed lock | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a126_vccUnderVoltage` | page 126 | Front body controller: a126 vcc under voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a127_vcleftEFuseCurrent` | page 127 | Front body controller: a127 vcleft e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a127_vcleftEFuseVoltage` | page 127 | Front body controller: a127 vcleft e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a127_vcleftEFuseTemp` | page 127 | Front body controller: a127 vcleft e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a127_vcleftEFuseRemainingRetries` | page 127 | Front body controller: a127 vcleft e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a128_vcrightEFuseCurrent` | page 128 | Front body controller: a128 vcright e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a128_vcrightEFuseVoltage` | page 128 | Front body controller: a128 vcright e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a128_vcrightEFuseTemp` | page 128 | Front body controller: a128 vcright e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a128_vcrightEFuseRemainingRetries` | page 128 | Front body controller: a128 vcright e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a129_pcsEFuseCurrent` | page 129 | Front body controller: a129 pcs e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a129_pcsEFuseVoltage` | page 129 | Front body controller: a129 pcs e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a129_pcsEFuseTemp` | page 129 | Front body controller: a129 pcs e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a129_pcsEFuseRemainingRetries` | page 129 | Front body controller: a129 pcs e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a130_epas3pEFuseCurrent` | page 130 | Front body controller: a130 epas3p e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a130_epas3pEFuseVoltage` | page 130 | Front body controller: a130 epas3p e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a130_epas3pEFuseTemp` | page 130 | Front body controller: a130 epas3p e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a131_epas3sEFuseCurrent` | page 131 | Front body controller: a131 epas3s e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a131_epas3sEFuseVoltage` | page 131 | Front body controller: a131 epas3s e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a131_epas3sEFuseTemp` | page 131 | Front body controller: a131 epas3s e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a132_iBoosterCurrent` | page 132 | Front body controller: a132 i booster current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a132_iBoosterVoltage` | page 132 | Front body controller: a132 i booster voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a132_iBoosterEFuseTemp` | page 132 | Front body controller: a132 i booster e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a133_espEFuseCurrent` | page 133 | Front body controller: a133 esp e fuse current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a133_espEFuseVoltage` | page 133 | Front body controller: a133 esp e fuse voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a133_espEFuseTemp` | page 133 | Front body controller: a133 esp e fuse temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a134_fusedHighCurrent` | page 134 | Front body controller: a134 fused high current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a134_fusedHighVoltage` | page 134 | Front body controller: a134 fused high voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a134_fusedHighTemp` | page 134 | Front body controller: a134 fused high temp | 48\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a134_vbatFusedEFuseRemainingRetries` | page 134 | Front body controller: a134 vbat fused e fuse remaining retries | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a136_snsShortCircuit` | page 136 | Front body controller: a136 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a136_snsDisconnect` | page 136 | Front body controller: a136 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a136_snsRateChangeUp` | page 136 | Front body controller: a136 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a136_snsRateChangeDown` | page 136 | Front body controller: a136 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a137_snsShortCircuit` | page 137 | Front body controller: a137 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a137_snsDisconnect` | page 137 | Front body controller: a137 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a137_snsRateChangeUp` | page 137 | Front body controller: a137 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a137_snsRateChangeDown` | page 137 | Front body controller: a137 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a138_snsShortCircuit` | page 138 | Front body controller: a138 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a138_snsDisconnect` | page 138 | Front body controller: a138 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a138_snsRateChangeUp` | page 138 | Front body controller: a138 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a138_snsRateChangeDown` | page 138 | Front body controller: a138 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a139_snsShortCircuit` | page 139 | Front body controller: a139 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a139_snsDisconnect` | page 139 | Front body controller: a139 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a139_snsRateChangeUp` | page 139 | Front body controller: a139 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a139_snsRateChangeDown` | page 139 | Front body controller: a139 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a140_snsShortCircuit` | page 140 | Front body controller: a140 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a140_snsDisconnect` | page 140 | Front body controller: a140 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a140_snsRateChangeUp` | page 140 | Front body controller: a140 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a140_snsRateChangeDown` | page 140 | Front body controller: a140 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a141_snsShortCircuit` | page 141 | Front body controller: a141 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a141_snsDisconnect` | page 141 | Front body controller: a141 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a141_snsRateChangeUp` | page 141 | Front body controller: a141 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a141_snsRateChangeDown` | page 141 | Front body controller: a141 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_driverState` | page 142 | Front body controller: a142 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a142_driverThermWarn` | page 142 | Front body controller: a142 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_driverThermShutdown` | page 142 | Front body controller: a142 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_undervoltage` | page 142 | Front body controller: a142 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_chargePumpUndervoltage` | page 142 | Front body controller: a142 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilOpenX` | page 142 | Front body controller: a142 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilOpenY` | page 142 | Front body controller: a142 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortXPGnd` | page 142 | Front body controller: a142 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortXPVbb` | page 142 | Front body controller: a142 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortXNGnd` | page 142 | Front body controller: a142 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortXNVbb` | page 142 | Front body controller: a142 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortYPGnd` | page 142 | Front body controller: a142 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortYPVbb` | page 142 | Front body controller: a142 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortYNGnd` | page 142 | Front body controller: a142 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_isCoilShortYNVbb` | page 142 | Front body controller: a142 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a142_driverHasCommError` | page 142 | Front body controller: a142 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a143_vsUnderVoltage` | page 143 | Front body controller: a143 vs under voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a143_vsOverVoltage` | page 143 | Front body controller: a143 vs over voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a143_chpUnderVoltage` | page 143 | Front body controller: a143 chp under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a143_vglUnderVoltage` | page 143 | Front body controller: a143 vgl under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a143_thOverTemperature` | page 143 | Front body controller: a143 th over temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a144_vsUnderVoltage` | page 144 | Front body controller: a144 vs under voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a144_vsOverVoltage` | page 144 | Front body controller: a144 vs over voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a144_chpUnderVoltage` | page 144 | Front body controller: a144 chp under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a144_vglUnderVoltage` | page 144 | Front body controller: a144 vgl under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a144_thOverTemperature` | page 144 | Front body controller: a144 th over temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a145_vsUnderVoltage` | page 145 | Front body controller: a145 vs under voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a145_vsOverVoltage` | page 145 | Front body controller: a145 vs over voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a145_chpUnderVoltage` | page 145 | Front body controller: a145 chp under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a145_vglUnderVoltage` | page 145 | Front body controller: a145 vgl under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a145_thOverTemperature` | page 145 | Front body controller: a145 th over temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a146_RPMActual` | page 146 | Front body controller: a146 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a146_RPMTarget` | page 146 | Front body controller: a146 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a147_RPMActual` | page 147 | Front body controller: a147 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a147_RPMTarget` | page 147 | Front body controller: a147 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a148_RPMActual` | page 148 | Front body controller: a148 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a148_RPMTarget` | page 148 | Front body controller: a148 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a150_RPMActual` | page 150 | Front body controller: a150 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a150_RPMTarget` | page 150 | Front body controller: a150 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a151_RPMActual` | page 151 | Front body controller: a151 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a151_RPMTarget` | page 151 | Front body controller: a151 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a152_RPMActual` | page 152 | Front body controller: a152 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a152_RPMTarget` | page 152 | Front body controller: a152 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a156_motorCounts` | page 156 | Front body controller: a156 motor counts | 16\|11 | little-endian | unsigned | 1 | -100 | ticks | -100 to 1947 |  | plausible |
| `VCFRONT_a157_motorCounts` | page 157 | Front body controller: a157 motor counts | 16\|11 | little-endian | unsigned | 1 | -100 | ticks | -100 to 1947 |  | plausible |
| `VCFRONT_a159_stall` | page 159 | Front body controller: a159 stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a159_angleActual` | page 159 | Front body controller: a159 angle actual | 17\|10 | little-endian | unsigned | 0.25 | -70 | deg | -70 to 185.75 |  | plausible |
| `VCFRONT_a159_angleTarget` | page 159 | Front body controller: a159 angle target | 27\|10 | little-endian | unsigned | 0.25 | -10 | deg | -10 to 245.75 |  | plausible |
| `VCFRONT_a160_highDischTemp` | page 160 | Front body controller: a160 high disch temp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_lowDischPressure` | page 160 | Front body controller: a160 low disch pressure | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_highDischPressure` | page 160 | Front body controller: a160 high disch pressure | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_lowSuctionPressure` | page 160 | Front body controller: a160 low suction pressure | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultSnsDischPress` | page 160 | Front body controller: a160 fault sns disch press | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultSnsDischTemp` | page 160 | Front body controller: a160 fault sns disch temp | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultSnsSuctPress` | page 160 | Front body controller: a160 fault sns suct press | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultSnsSuctTemp` | page 160 | Front body controller: a160 fault sns suct temp | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultSnsAmbientTemp` | page 160 | Front body controller: a160 fault sns ambient temp | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultValveEXV` | page 160 | Front body controller: a160 fault valve EXV | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_faultValveEvapSol` | page 160 | Front body controller: a160 fault valve evap sol | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_highDischargePressureCutouts` | page 160 | Front body controller: a160 high discharge pressure cutouts | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_highDischargeTempCutouts` | page 160 | Front body controller: a160 high discharge temp cutouts | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a160_compressorRpm` | page 160 | Front body controller: a160 compressor rpm | 32\|7 | little-endian | unsigned | 90 | 0 | RPM | 0 to 11430 |  | plausible |
| `VCFRONT_a161_failedStart` | page 161 | Front body controller: a161 failed start | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_HVOverVoltage` | page 161 | Front body controller: a161 HV over voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_HVUnderVoltage` | page 161 | Front body controller: a161 HV under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_overCurrent` | page 161 | Front body controller: a161 over current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_overTemperature` | page 161 | Front body controller: a161 over temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_shortCircuit` | page 161 | Front body controller: a161 short circuit | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_underTemperature` | page 161 | Front body controller: a161 under temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_LVUnderVoltage` | page 161 | Front body controller: a161 LV under voltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_LVOverVoltage` | page 161 | Front body controller: a161 LV over voltage | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_tempSnsFaultIPM1` | page 161 | Front body controller: a161 temp sns fault IPM1 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_tempSnsFaultIPM2` | page 161 | Front body controller: a161 temp sns fault IPM2 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_tempSnsFaultCPU` | page 161 | Front body controller: a161 temp sns fault CPU | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_currentSnsError` | page 161 | Front body controller: a161 current sns error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_selfTestFailCPU` | page 161 | Front body controller: a161 self test fail CPU | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_internalPowerSupplyFault` | page 161 | Front body controller: a161 internal power supply fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_inverterOpenCircuit` | page 161 | Front body controller: a161 inverter open circuit | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_warnOverTemperature` | page 161 | Front body controller: a161 warn over temperature | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_failedStartRepeated` | page 161 | Front body controller: a161 failed start repeated | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a161_overload` | page 161 | Front body controller: a161 overload | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a162_dischargePressure` | page 162 | Front body controller: a162 discharge pressure | 16\|6 | little-endian | unsigned | 0.5 | 0 | bar | 0 to 31.5 |  | plausible |
| `VCFRONT_a162_chillerExvFlow` | page 162 | Front body controller: a162 chiller exv flow | 22\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a162_lccExvFlow` | page 162 | Front body controller: a162 lcc exv flow | 29\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a162_ccLeftExvFlow` | page 162 | Front body controller: a162 cc left exv flow | 36\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a162_ccRightExvFlow` | page 162 | Front body controller: a162 cc right exv flow | 43\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a162_evapExvFlow` | page 162 | Front body controller: a162 evap exv flow | 50\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a162_recircExvFlow` | page 162 | Front body controller: a162 recirc exv flow | 57\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a164_lockoutVoltage` | page 164 | Front body controller: a164 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a165_lockoutVoltage` | page 165 | Front body controller: a165 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a168_leftECU` | page 168 | Front body controller: a168 left ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a168_rightECU` | page 168 | Front body controller: a168 right ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a169_leftECU` | page 169 | Front body controller: a169 left ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a169_rightECU` | page 169 | Front body controller: a169 right ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a170_leftECU` | page 170 | Front body controller: a170 left ECU | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a170_rightECU` | page 170 | Front body controller: a170 right ECU | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_VCFRONT` | page 171 | Front body controller: a171 VCFRONT | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_VCRIGHT` | page 171 | Front body controller: a171 VCRIGHT | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_VCLEFT` | page 171 | Front body controller: a171 VCLEFT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_BMS` | page 171 | Front body controller: a171 BMS | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_HVP` | page 171 | Front body controller: a171 HVP | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_GTW` | page 171 | Front body controller: a171 GTW | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_CP` | page 171 | Front body controller: a171 CP | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_PCS` | page 171 | Front body controller: a171 PCS | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_PCSCPU2` | page 171 | Front body controller: a171 PCSCPU2 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_DI` | page 171 | Front body controller: a171 DI | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_DIS` | page 171 | Front body controller: a171 DIS | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_PM` | page 171 | Front body controller: a171 PM | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_PMS` | page 171 | Front body controller: a171 PMS | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_EPBR` | page 171 | Front body controller: a171 EPBR | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_EPBL` | page 171 | Front body controller: a171 EPBL | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_IBST` | page 171 | Front body controller: a171 IBST | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_IBSTCAL` | page 171 | Front body controller: a171 IBSTCAL | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_ESP` | page 171 | Front body controller: a171 ESP | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_ESPCAL` | page 171 | Front body controller: a171 ESPCAL | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_OPC` | page 171 | Front body controller: a171 OPC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_OPCS` | page 171 | Front body controller: a171 OPCS | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_SCCM` | page 171 | Front body controller: a171 SCCM | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_LVBMS` | page 171 | Front body controller: a171 LVBMS | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_IDB` | page 171 | Front body controller: a171 IDB | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_IDB1` | page 171 | Front body controller: a171 IDB1 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_IDBCAL` | page 171 | Front body controller: a171 IDBCAL | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_RCU` | page 171 | Front body controller: a171 RCU | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_RCUCAL` | page 171 | Front body controller: a171 RCUCAL | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_DPB` | page 171 | Front body controller: a171 DPB | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_DPBCAL` | page 171 | Front body controller: a171 DPBCAL | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a171_serviceMode` | page 171 | Signal reported by Front body controller | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a172_ECUMismatchBits` | page 172 | Front body controller: a172 ECU mismatch bits | 16\|47 | little-endian | unsigned | 1 | 0 |  | 0 to 140737488355327 |  | layout-only |
| `VCFRONT_a172_serviceMode` | page 172 | Signal reported by Front body controller | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a173_ECUMismatchBits` | page 173 | Front body controller: a173 ECU mismatch bits | 16\|47 | little-endian | unsigned | 1 | 0 |  | 0 to 140737488355327 |  | layout-only |
| `VCFRONT_a173_serviceMode` | page 173 | Signal reported by Front body controller | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a175_snsShortCircuit` | page 175 | Front body controller: a175 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a175_snsDisconnect` | page 175 | Front body controller: a175 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a175_snsRateChangeUp` | page 175 | Front body controller: a175 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a175_snsRateChangeDown` | page 175 | Front body controller: a175 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a176_vehicleState` | page 176 | Front body controller: a176 vehicle state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `ACCESSORY_PLUS`<br>4 = `DRIVE` | plausible |
| `VCFRONT_a177_mcuAudioCurrent` | page 177 | Front body controller: a177 mcu audio current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a179_highLVAmpsIntoPCSLog` | page 179 | Front body controller: a179 high LV amps into PCS log | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_vehiclePowerState` | page 180 | Front body controller: a180 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a180_hvState` | page 180 | Front body controller: a180 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a180_bmsState` | page 180 | Front body controller: a180 bms state; raw 9 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a180_notEnoughPowerForSupport` | page 180 | Front body controller: a180 not enough power for support | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_pcsEFuseStable` | page 180 | Front body controller: a180 pcs e fuse stable | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_vcrightEFuseStable` | page 180 | Front body controller: a180 vcright e fuse stable | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_contactorEFuseStable` | page 180 | Front body controller: a180 contactor e fuse stable | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_hvcEFuseStable` | page 180 | Front body controller: a180 hvc e fuse stable | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_replaceLVBattery` | page 180 | Front body controller: a180 replace LV battery | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_BMS_MIA` | page 180 | Front body controller: a180 BMS MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_PCS_MIA` | page 180 | Front body controller: a180 PCS MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_HVBlockingMismatch` | page 180 | Front body controller: a180 HV blocking mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_serviceMode` | page 180 | Signal reported by Front body controller | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_transportMode` | page 180 | Front body controller: a180 transport mode | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_frunkOpen` | page 180 | Front body controller: a180 frunk open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a180_dcdcLVSupportStatus` | page 180 | Front body controller: a180 dcdc LV support status | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCFRONT_a181_vehicleState` | page 181 | Front body controller: a181 vehicle state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a182_deadLV` | page 182 | Front body controller: a182 dead LV | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_voltageDrop` | page 182 | Front body controller: a182 voltage drop | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_overcharge` | page 182 | Front body controller: a182 overcharge | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_LVFloorReached` | page 182 | Front body controller: a182 LV floor reached | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_shortedCell` | page 182 | Front body controller: a182 shorted cell | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_postPORExcessiveAh` | page 182 | Front body controller: a182 post POR excessive ah | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_resistanceEstimationHardFailure` | page 182 | Front body controller: a182 resistance estimation hard failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_dcrMilliOhmsAboveThreshold` | page 182 | Front body controller: a182 dcr milli ohms above threshold | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_prechargeLVLoadReduction` | page 182 | Front body controller: a182 precharge LV load reduction | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_factoryMode` | page 182 | Front body controller: a182 factory mode | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_serviceMode` | page 182 | Signal reported by Front body controller | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_transportMode` | page 182 | Front body controller: a182 transport mode | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_frunkOpen` | page 182 | Front body controller: a182 frunk open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_packOverDischarged` | page 182 | Front body controller: a182 pack over discharged | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_cellImbalance` | page 182 | Front body controller: a182 cell imbalance | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_instantPrechargeDCRTooHigh` | page 182 | Front body controller: a182 instant precharge DCR too high | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_ambientTemp` | page 182 | Front body controller: a182 ambient temp; raw 0 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 1 | -40 | degC | -39 to 87 | 0 = `SNA` | plausible |
| `VCFRONT_a182_dischargedAmpHours` | page 182 | Front body controller: a182 discharged amp hours | 40\|8 | little-endian | unsigned | 60 | 0 | Ah | 0 to 15300 |  | plausible |
| `VCFRONT_a182_chargedAmpHours` | page 182 | Front body controller: a182 charged amp hours | 48\|8 | little-endian | unsigned | 60 | 0 | Ah | 0 to 15300 |  | plausible |
| `VCFRONT_a182_calibrationLostFault` | page 182 | Front body controller: a182 calibration lost fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_samplingHWError` | page 182 | Front body controller: a182 sampling HW error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_brickOverDischarged` | page 182 | Front body controller: a182 brick over discharged | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a182_batteryType` | page 182 | Front body controller: a182 battery type | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a186_noDriveChgCableConX` | page 186 | Front body controller: a186 no drive chg cable con x | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a187_vehBusRetryCount` | page 187 | Front body controller: a187 veh bus retry count | 16\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT_a187_partyBusRetryCount` | page 187 | Front body controller: a187 party bus retry count | 25\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT_a187_hvsBusRetryCount` | page 187 | Front body controller: a187 hvs bus retry count | 34\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT_a187_ethBusRetryCount` | page 187 | Front body controller: a187 eth bus retry count | 43\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT_a187_chBusRetryCount` | page 187 | Front body controller: a187 ch bus retry count | 52\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | layout-only |
| `VCFRONT_a188_sleepBypassCurrent` | page 188 | Front body controller: a188 sleep bypass current | 16\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 51 |  | plausible |
| `VCFRONT_a188_IBSCurrent` | page 188 | Front body controller: a188 IBS current | 24\|12 | little-endian | signed | 0.02 | 0 | A | -40.96 to 40.94 |  | plausible |
| `VCFRONT_a188_vehicleState` | page 188 | Front body controller: a188 vehicle state; raw 18 = signal not available (SNA) | 36\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `LOW_POWER_STANDBY`<br>2 = `SILENT_WAKE`<br>3 = `BATTERY_POST_WAKE`<br>4 = `SYSTEM_CHECKS`<br>5 = `SLEEP_SHUTDOWN`<br>6 = `SLEEP_STANDBY`<br>7 = `LV_SHUTDOWN`<br>8 = `LV_AWAKE`<br>9 = `HV_UP_STANDBY`<br>10 = `ACCESSORY`<br>11 = `ACCESSORY_PLUS`<br>12 = `CONDITIONING`<br>13 = `DRIVE`<br>14 = `CRASH`<br>15 = `OTA`<br>16 = `TURN_ON_RAILS`<br>17 = `RESET`<br>18 = `SNA` | plausible |
| `VCFRONT_a188_timeNotSleeping` | page 188 | Front body controller: a188 time not sleeping | 41\|6 | little-endian | unsigned | 1 | 0 | sec | 0 to 63 |  | plausible |
| `VCFRONT_a188_chargeRequest` | page 188 | Front body controller: a188 charge request | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_12VSupport` | page 188 | Front body controller: a188 12 v support | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_ThermalSupport` | page 188 | Front body controller: a188 thermal support | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_accessoryRequest` | page 188 | Front body controller: a188 accessory request | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_CANAfterQuiet` | page 188 | Front body controller: a188 CAN after quiet | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_SleepRequestTimeout` | page 188 | Front body controller: a188 sleep request timeout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a188_wakeUpMsgID` | page 188 | Front body controller: a188 wake up msg ID | 53\|11 | little-endian | unsigned | 1 | 0 |  | 0 to 2047 |  | layout-only |
| `VCFRONT_a191_vehiclePowerState` | page 191 | Front body controller: a191 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a191_hvState` | page 191 | Front body controller: a191 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a191_reverseBatteryEFuseFault` | page 191 | Front body controller: a191 reverse battery e fuse fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_vehicleLoadShedActive` | page 191 | Front body controller: a191 vehicle load shed active | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_vehicleLoadShedHvFaultActive` | page 191 | Front body controller: a191 vehicle load shed hv fault active | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_vehicleLoadShedPostCrashActive` | page 191 | Front body controller: a191 vehicle load shed post crash active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_IBSVoltage` | page 191 | Front body controller: a191 IBS voltage | 25\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCFRONT_a191_a180_DCDCNotSupportingLVBus` | page 191 | Front body controller: a191 a180 DCDC not supporting LV bus | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_MOSState` | page 191 | Front body controller: a191 MOS state; raw 3 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a191_LVBMSVoltage` | page 191 | Front body controller: a191 LVBMS voltage | 36\|8 | little-endian | unsigned | 0.08741903 | 0 | V | 0 to 22.29185265 |  | plausible |
| `VCFRONT_a191_ECPAState` | page 191 | Front body controller: a191 ECPA state; raw 3 = signal not available (SNA) | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a191_LVBMSCurrentTargetValid` | page 191 | Front body controller: a191 LVBMS current target valid | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_LVBMSVoltageTargetValid` | page 191 | Front body controller: a191 LVBMS voltage target valid | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_serviceMode` | page 191 | Signal reported by Front body controller | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_frunkOpen` | page 191 | Front body controller: a191 frunk open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_vehicleLoadShedStage` | page 191 | Front body controller: a191 vehicle load shed stage | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE_OR_UNDEFINED`<br>1 = `1`<br>2 = `2`<br>3 = `3` | plausible |
| `VCFRONT_a191_exitDriveWarningTimerExpired` | page 191 | Front body controller: a191 exit drive warning timer expired | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_LVBMSMIA` | page 191 | Front body controller: a191 LVBMSMIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_PCS_MIA` | page 191 | Front body controller: a191 PCS MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_NotEnoughPowerForSupport` | page 191 | Front body controller: a191 not enough power for support | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a191_bmsState` | page 191 | Front body controller: a191 bms state; raw 9 = signal not available (SNA) | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a192_vehiclePowerState` | page 192 | Front body controller: a192 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a192_hvState` | page 192 | Front body controller: a192 hv state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a192_notEnoughPowerForSupport` | page 192 | Front body controller: a192 not enough power for support | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_pcsEFuseStable` | page 192 | Front body controller: a192 pcs e fuse stable | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_vcrightEFuseStable` | page 192 | Front body controller: a192 vcright e fuse stable | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_contactorEFuseStable` | page 192 | Front body controller: a192 contactor e fuse stable | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_hvcEFuseStable` | page 192 | Front body controller: a192 hvc e fuse stable | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_replaceLVBattery` | page 192 | Front body controller: a192 replace LV battery | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_BMS_MIA` | page 192 | Front body controller: a192 BMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_PCS_MIA` | page 192 | Front body controller: a192 PCS MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_HVBlockingMismatch` | page 192 | Front body controller: a192 HV blocking mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_disconnected12V` | page 192 | Front body controller: a192 disconnected12 v | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_LVBatteryCannotSupportVehicle` | page 192 | Front body controller: a192 LV battery cannot support vehicle | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_DI_gear` | page 192 | Front body controller: a192 DI gear; raw 7 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCFRONT_a192_GTW_factoryGated` | page 192 | Front body controller: a192 GTW factory gated | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_GTW_updateStarted` | page 192 | Front body controller: a192 GTW update started | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_serviceMode` | page 192 | Signal reported by Front body controller | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_frunkOpen` | page 192 | Front body controller: a192 frunk open | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_IBSCurrent` | page 192 | Front body controller: a192 IBS current | 40\|8 | little-endian | unsigned | 0.5 | -63 | A | -63 to 64.5 |  | plausible |
| `VCFRONT_a192_PCSCurrent` | page 192 | Front body controller: a192 PCS current | 48\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCFRONT_a192_HVFaultLoadShedActive` | page 192 | Front body controller: a192 HV fault load shed active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a192_postCrashLoadShedActive` | page 192 | Front body controller: a192 post crash load shed active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a195_IBSVoltage` | page 195 | Front body controller: a195 IBS voltage | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a195_serviceMode` | page 195 | Signal reported by Front body controller | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a195_frunkOpen` | page 195 | Front body controller: a195 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a196_factoryMode` | page 196 | Front body controller: a196 factory mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a196_serviceMode` | page 196 | Signal reported by Front body controller | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a196_transportMode` | page 196 | Front body controller: a196 transport mode | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a196_frunkOpen` | page 196 | Front body controller: a196 frunk open | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a196_vehiclePowerState` | page 196 | Front body controller: a196 vehicle power state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a196_batterySMState` | page 196 | Front body controller: a196 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a196_disconnectedBatteryTestCurrent` | page 196 | Front body controller: a196 disconnected battery test current | 28\|12 | little-endian | unsigned | 0.004884005 | -10 | A | -10 to 10.000000475 |  | plausible |
| `VCFRONT_a196_disconnectedBatteryTestVoltage` | page 196 | Front body controller: a196 disconnected battery test voltage | 40\|8 | little-endian | unsigned | 0.0392156876624 | 6 | V | 6 to 16.0000003539 |  | plausible |
| `VCFRONT_a196_disconnectedBatteryTestPrevVoltage` | page 196 | Front body controller: a196 disconnected battery test prev voltage | 48\|8 | little-endian | unsigned | 0.0392156876624 | 6 | V | 6 to 16.0000003539 |  | plausible |
| `VCFRONT_a196_ECPAState` | page 196 | Front body controller: a196 ECPA state; raw 3 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a198_outputState` | page 198 | Front body controller: a198 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a198_NVRAMState` | page 198 | Front body controller: a198 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a198_lockoutState` | page 198 | Front body controller: a198 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a199_outputState` | page 199 | Front body controller: a199 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a199_NVRAMState` | page 199 | Front body controller: a199 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a199_lockoutState` | page 199 | Front body controller: a199 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a200_vcleftSelfTest` | page 200 | Front body controller: a200 vcleft self test; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a201_vcrightSelfTest` | page 201 | Front body controller: a201 vcright self test; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a202_pcsSelfTest` | page 202 | Front body controller: a202 pcs self test; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a207_vbatFusedSelfTest` | page 207 | Front body controller: a207 vbat fused self test; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a210_valveUnderTravel` | page 210 | Front body controller: a210 valve under travel | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a210_valveOverTravel` | page 210 | Front body controller: a210 valve over travel | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a210_valveNoTravel` | page 210 | Front body controller: a210 valve no travel | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a212_IBSTemp` | page 212 | Front body controller: a212 IBS temp | 16\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCFRONT_a213_IBSVolts` | page 213 | Front body controller: a213 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a213_IBSAh` | page 213 | Front body controller: a213 IBS ah | 32\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCFRONT_a213_LVBatteryTemp` | page 213 | Front body controller: a213 LV battery temp; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 | -32768 = `SNA` | plausible |
| `VCFRONT_a214_motorFaulted` | page 214 | Front body controller: a214 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorLocked` | page 214 | Front body controller: a214 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_ecuReset` | page 214 | Front body controller: a214 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_fetTempIrrational` | page 214 | Front body controller: a214 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorControlError` | page 214 | Front body controller: a214 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_underVoltage` | page 214 | Front body controller: a214 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_overVoltage` | page 214 | Front body controller: a214 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_hardwareOvercurrent` | page 214 | Front body controller: a214 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorOpenPhase` | page 214 | Front body controller: a214 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorSoftOpenPhase` | page 214 | Front body controller: a214 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorOvertemp` | page 214 | Front body controller: a214 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_dcOvercurrent` | page 214 | Front body controller: a214 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorStalled` | page 214 | Front body controller: a214 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_selfTestFailed` | page 214 | Front body controller: a214 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_selfTestResult` | page 214 | Front body controller: a214 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCFRONT_a214_linChecksumError` | page 214 | Front body controller: a214 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_linFramingError` | page 214 | Front body controller: a214 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_phaseShorted` | page 214 | Front body controller: a214 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_busVoltageIrrational` | page 214 | Front body controller: a214 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_dcCurrentIrrational` | page 214 | Front body controller: a214 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorSpeedIrrational` | page 214 | Front body controller: a214 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_supplyVoltageIrrational` | page 214 | Front body controller: a214 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorPhaseCurrentIrrational` | page 214 | Front body controller: a214 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_chipOvertemp` | page 214 | Front body controller: a214 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_motorSpeedTooHigh` | page 214 | Front body controller: a214 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_phaseOvercurrent` | page 214 | Front body controller: a214 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_vddaOvercurrent` | page 214 | Front body controller: a214 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_busVoltageUnhealthy` | page 214 | Front body controller: a214 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_hsVdsOvervoltage` | page 214 | Front body controller: a214 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_hsVdsOvervoltageMask` | page 214 | Front body controller: a214 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a214_lsVdsOvervoltage` | page 214 | Front body controller: a214 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a214_lsVdsOvervoltageMask` | page 214 | Front body controller: a214 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a214_payloadBitsNotSet` | page 214 | Front body controller: a214 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_inDrive` | page 216 | Front body controller: a216 in drive | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_hvState` | page 216 | Front body controller: a216 hv state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a216_vcleftFastBlowImminent` | page 216 | Front body controller: a216 vcleft fast blow imminent | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcleftFastBlowDebounceImminent` | page 216 | Front body controller: a216 vcleft fast blow debounce imminent | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcleftStaticImminent` | page 216 | Front body controller: a216 vcleft static imminent | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcleftDynamicImminent` | page 216 | Front body controller: a216 vcleft dynamic imminent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcrightFastBlowImminent` | page 216 | Front body controller: a216 vcright fast blow imminent | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcrightFastBlowDebounceImminent` | page 216 | Front body controller: a216 vcright fast blow debounce imminent | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcrightStaticImminent` | page 216 | Front body controller: a216 vcright static imminent | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a216_vcrightDynamicImminent` | page 216 | Front body controller: a216 vcright dynamic imminent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorFaulted` | page 217 | Front body controller: a217 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorLocked` | page 217 | Front body controller: a217 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_ecuReset` | page 217 | Front body controller: a217 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_fetTempIrrational` | page 217 | Front body controller: a217 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorControlError` | page 217 | Front body controller: a217 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_underVoltage` | page 217 | Front body controller: a217 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_overVoltage` | page 217 | Front body controller: a217 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_hardwareOvercurrent` | page 217 | Front body controller: a217 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorOpenPhase` | page 217 | Front body controller: a217 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorSoftOpenPhase` | page 217 | Front body controller: a217 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorOvertemp` | page 217 | Front body controller: a217 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_dcOvercurrent` | page 217 | Front body controller: a217 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorStalled` | page 217 | Front body controller: a217 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_selfTestFailed` | page 217 | Front body controller: a217 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_selfTestResult` | page 217 | Front body controller: a217 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCFRONT_a217_linChecksumError` | page 217 | Front body controller: a217 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_linFramingError` | page 217 | Front body controller: a217 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_phaseShorted` | page 217 | Front body controller: a217 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_busVoltageIrrational` | page 217 | Front body controller: a217 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_dcCurrentIrrational` | page 217 | Front body controller: a217 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorSpeedIrrational` | page 217 | Front body controller: a217 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_supplyVoltageIrrational` | page 217 | Front body controller: a217 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorPhaseCurrentIrrational` | page 217 | Front body controller: a217 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_chipOvertemp` | page 217 | Front body controller: a217 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_motorSpeedTooHigh` | page 217 | Front body controller: a217 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_phaseOvercurrent` | page 217 | Front body controller: a217 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_vddaOvercurrent` | page 217 | Front body controller: a217 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_busVoltageUnhealthy` | page 217 | Front body controller: a217 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_hsVdsOvervoltage` | page 217 | Front body controller: a217 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_hsVdsOvervoltageMask` | page 217 | Front body controller: a217 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a217_lsVdsOvervoltage` | page 217 | Front body controller: a217 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a217_lsVdsOvervoltageMask` | page 217 | Front body controller: a217 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a217_payloadBitsNotSet` | page 217 | Front body controller: a217 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a219_IBSVolts` | page 219 | Front body controller: a219 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a219_IBSAh` | page 219 | Front body controller: a219 IBS ah | 32\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCFRONT_a219_IBSCurrent` | page 219 | Front body controller: a219 IBS current | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a220_IBSCurrent` | page 220 | Front body controller: a220 IBS current | 16\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a220_PCSCurrent` | page 220 | Front body controller: a220 PCS current | 32\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCFRONT_a220_serviceMode` | page 220 | Signal reported by Front body controller | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a220_frunkOpen` | page 220 | Front body controller: a220 frunk open | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_outputFaulted` | page 221 | Front body controller: a221 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_currentSenseFaulted` | page 221 | Front body controller: a221 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_tempSenseFaulted` | page 221 | Front body controller: a221 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_underCurrent` | page 221 | Front body controller: a221 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_overCurrent` | page 221 | Front body controller: a221 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a221_overTemperature` | page 221 | Front body controller: a221 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_outputFaulted` | page 222 | Front body controller: a222 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_currentSenseFaulted` | page 222 | Front body controller: a222 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_tempSenseFaulted` | page 222 | Front body controller: a222 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_underCurrent` | page 222 | Front body controller: a222 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_overCurrent` | page 222 | Front body controller: a222 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a222_overTemperature` | page 222 | Front body controller: a222 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a223_12VTemperature` | page 223 | Front body controller: a223 12 v temperature | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a227_motorFaulted` | page 227 | Front body controller: a227 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorLocked` | page 227 | Front body controller: a227 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_ecuReset` | page 227 | Front body controller: a227 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_fetTempIrrational` | page 227 | Front body controller: a227 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorControlError` | page 227 | Front body controller: a227 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_underVoltage` | page 227 | Front body controller: a227 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_overVoltage` | page 227 | Front body controller: a227 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_hardwareOvercurrent` | page 227 | Front body controller: a227 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorOpenPhase` | page 227 | Front body controller: a227 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorSoftOpenPhase` | page 227 | Front body controller: a227 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorOvertemp` | page 227 | Front body controller: a227 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_dcOvercurrent` | page 227 | Front body controller: a227 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorStalled` | page 227 | Front body controller: a227 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_selfTestFailed` | page 227 | Front body controller: a227 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_selfTestResult` | page 227 | Front body controller: a227 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCFRONT_a227_linChecksumError` | page 227 | Front body controller: a227 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_linFramingError` | page 227 | Front body controller: a227 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_phaseShorted` | page 227 | Front body controller: a227 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_busVoltageIrrational` | page 227 | Front body controller: a227 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_dcCurrentIrrational` | page 227 | Front body controller: a227 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorSpeedIrrational` | page 227 | Front body controller: a227 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_supplyVoltageIrrational` | page 227 | Front body controller: a227 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorPhaseCurrentIrrational` | page 227 | Front body controller: a227 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_chipOvertemp` | page 227 | Front body controller: a227 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_motorSpeedTooHigh` | page 227 | Front body controller: a227 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_phaseOvercurrent` | page 227 | Front body controller: a227 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_vddaOvercurrent` | page 227 | Front body controller: a227 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_busVoltageUnhealthy` | page 227 | Front body controller: a227 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_hsVdsOvervoltage` | page 227 | Front body controller: a227 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_hsVdsOvervoltageMask` | page 227 | Front body controller: a227 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a227_lsVdsOvervoltage` | page 227 | Front body controller: a227 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a227_lsVdsOvervoltageMask` | page 227 | Front body controller: a227 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a227_payloadBitsNotSet` | page 227 | Front body controller: a227 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a231_12VTemperature` | page 231 | Front body controller: a231 12 v temperature | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a233_current` | page 233 | Front body controller: a233 current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a234_current` | page 234 | Front body controller: a234 current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a235_ptSensorTemp` | page 235 | Front body controller: a235 pt sensor temp | 16\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a236_batSensorTemp` | page 236 | Front body controller: a236 bat sensor temp | 16\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a242_LVBatteryTemp` | page 242 | Front body controller: a242 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a242_IBSCurrent` | page 242 | Front body controller: a242 IBS current | 24\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a242_IBSVoltage` | page 242 | Front body controller: a242 IBS voltage | 36\|11 | little-endian | unsigned | 0.0108873518184 | 0 | V | 0 to 22.2864091723 |  | plausible |
| `VCFRONT_a242_IBSAmpHours` | page 242 | Front body controller: a242 IBS amp hours | 48\|8 | little-endian | unsigned | 0.01 | -2.55 | Ah | -2.55 to 4.4408920985e-16 |  | plausible |
| `VCFRONT_a242_vehiclePowerState` | page 242 | Front body controller: a242 vehicle power state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a243_IBSVolts` | page 243 | Front body controller: a243 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a243_IBSCurrent` | page 243 | Front body controller: a243 IBS current | 32\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a243_LVBatteryTemp` | page 243 | Front body controller: a243 LV battery temp; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 | -32768 = `SNA` | plausible |
| `VCFRONT_a244_current` | page 244 | Front body controller: a244 current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a244_voltage` | page 244 | Front body controller: a244 voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a244_vbatProtVoltage` | page 244 | Front body controller: a244 vbat prot voltage | 48\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a245_current` | page 245 | Front body controller: a245 current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a245_voltage` | page 245 | Front body controller: a245 voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a245_eFuseRemainingRetries` | page 245 | Front body controller: a245 e fuse remaining retries | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a246_current` | page 246 | Front body controller: a246 current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a246_voltage` | page 246 | Front body controller: a246 voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a246_eFuseRemainingRetries` | page 246 | Front body controller: a246 e fuse remaining retries | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a247_solenoidISense` | page 247 | Front body controller: a247 solenoid i sense | 16\|8 | little-endian | signed | 0.01 | 0 | A | -1.28 to 1.27 |  | plausible |
| `VCFRONT_a248_AS8510Voltage` | page 248 | Front body controller: a248 AS8510 voltage | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a248_IBSVoltage` | page 248 | Front body controller: a248 IBS voltage | 28\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a248_vbatMonitor` | page 248 | Front body controller: a248 vbat monitor | 40\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a248_voltageCalScaling` | page 248 | Front body controller: a248 voltage cal scaling | 52\|12 | little-endian | unsigned | 0.025 | 0 | % | 0 to 102.375 |  | plausible |
| `VCFRONT_a249_tempCoolantBatInlet` | page 249 | Front body controller: a249 temp coolant bat inlet | 16\|10 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 87.875 |  | plausible |
| `VCFRONT_a249_tempCoolantPTInlet` | page 249 | Front body controller: a249 temp coolant PT inlet | 26\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 215.875 |  | plausible |
| `VCFRONT_a250_isGlobalHeadlamps` | page 250 | Front body controller: a250 is global headlamps | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a250_isVirtualPitchSensor` | page 250 | Front body controller: a250 is virtual pitch sensor | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a250_isAimedHCML` | page 250 | Front body controller: a250 is aimed HCML | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a250_isAimedHCMR` | page 250 | Front body controller: a250 is aimed HCMR | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a250_calibratedVerticalPositionHCML` | page 250 | Front body controller: a250 calibrated vertical position HCML; raw 1023 = signal not available (SNA) | 20\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCFRONT_a250_calibratedVerticalPositionHCMR` | page 250 | Front body controller: a250 calibrated vertical position HCMR; raw 1023 = signal not available (SNA) | 30\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCFRONT_a250_calibratedHorizontalPositionHCML` | page 250 | Front body controller: a250 calibrated horizontal position HCML; raw 1023 = signal not available (SNA) | 40\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCFRONT_a250_calibratedHorizontalPositionHCMR` | page 250 | Front body controller: a250 calibrated horizontal position HCMR; raw 1023 = signal not available (SNA) | 50\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VCFRONT_a253_currentNotTapered` | page 253 | Front body controller: a253 current not tapered | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a253_ampHourTargetNotReached` | page 253 | Front body controller: a253 amp hour target not reached | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a253_IBSCurrent` | page 253 | Front body controller: a253 IBS current | 18\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a253_IBSAmpHours` | page 253 | Front body controller: a253 IBS amp hours | 34\|14 | little-endian | signed | 0.01 | 0 | Ah | -81.92 to 81.91 |  | plausible |
| `VCFRONT_a253_LVBatteryTemp` | page 253 | Front body controller: a253 LV battery temp; raw 127 = signal not available (SNA) | 48\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a253_firstChargeOTA` | page 253 | Front body controller: a253 first charge OTA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a253_firstChargePOR` | page 253 | Front body controller: a253 first charge POR | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a253_serviceMode` | page 253 | Signal reported by Front body controller | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a253_frunkOpen` | page 253 | Front body controller: a253 frunk open | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a254_RPMActual` | page 254 | Front body controller: a254 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a254_RPMTarget` | page 254 | Front body controller: a254 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a255_RPMActual` | page 255 | Front body controller: a255 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a255_RPMTarget` | page 255 | Front body controller: a255 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCFRONT_a257_lockoutVoltage` | page 257 | Front body controller: a257 lockout voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a257_vcrightLockoutStatus` | page 257 | Front body controller: a257 vcright lockout status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `PENDING`<br>2 = `ACTIVE` | plausible |
| `VCFRONT_a257_vcleftFault` | page 257 | Front body controller: a257 vcleft fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_vcrightFault` | page 257 | Front body controller: a257 vcright fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_pcsFault` | page 257 | Front body controller: a257 pcs fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_vbatFusedFault` | page 257 | Front body controller: a257 vbat fused fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_iBoosterFault` | page 257 | Front body controller: a257 i booster fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_espFault` | page 257 | Front body controller: a257 esp fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_epas3pFault` | page 257 | Front body controller: a257 epas3p fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_epas3sFault` | page 257 | Front body controller: a257 epas3s fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_revBattFault` | page 257 | Front body controller: a257 rev batt fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a257_vehicleState` | page 257 | Front body controller: a257 vehicle state; raw 18 = signal not available (SNA) | 43\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `LOW_POWER_STANDBY`<br>2 = `SILENT_WAKE`<br>3 = `BATTERY_POST_WAKE`<br>4 = `SYSTEM_CHECKS`<br>5 = `SLEEP_SHUTDOWN`<br>6 = `SLEEP_STANDBY`<br>7 = `LV_SHUTDOWN`<br>8 = `LV_AWAKE`<br>9 = `HV_UP_STANDBY`<br>10 = `ACCESSORY`<br>11 = `ACCESSORY_PLUS`<br>12 = `CONDITIONING`<br>13 = `DRIVE`<br>14 = `CRASH`<br>15 = `OTA`<br>16 = `TURN_ON_RAILS`<br>17 = `RESET`<br>18 = `SNA` | plausible |
| `VCFRONT_a259_serviceMode` | page 259 | Signal reported by Front body controller | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a259_voltageDropCounter` | page 259 | Front body controller: a259 voltage drop counter | 17\|3 | little-endian | unsigned | 2 | 0 | - | 0 to 14 |  | plausible |
| `VCFRONT_a259_minVoltageReached` | page 259 | Front body controller: a259 min voltage reached | 20\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a259_IBSTemp` | page 259 | Front body controller: a259 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCFRONT_a259_maxCurrentReached` | page 259 | Front body controller: a259 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a260_IBSVolts` | page 260 | Front body controller: a260 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a260_IBSAh` | page 260 | Front body controller: a260 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a260_vehiclePowerState` | page 260 | Front body controller: a260 vehicle power state | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a260_batterySMState` | page 260 | Front body controller: a260 battery SM state | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a260_HV_UP` | page 260 | Front body controller: a260 HV UP | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_notEnoughPowerForSupport` | page 260 | Front body controller: a260 not enough power for support | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_coolantHasBeenFilled` | page 260 | Front body controller: a260 coolant has been filled | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_ampHourTrigger` | page 260 | Front body controller: a260 amp hour trigger | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_voltageTrigger` | page 260 | Front body controller: a260 voltage trigger | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_crashDetected` | page 260 | Front body controller: a260 crash detected | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_BMS_MIA` | page 260 | Front body controller: a260 BMS MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_PCS_MIA` | page 260 | Front body controller: a260 PCS MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_HVBlockingMismatch` | page 260 | Front body controller: a260 HV blocking mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_serviceMode` | page 260 | Signal reported by Front body controller | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_dcdcLVSupportStatus` | page 260 | Front body controller: a260 dcdc LV support status | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCFRONT_a260_PCSAndVCREFuseStable` | page 260 | Front body controller: a260 PCS and VCRE fuse stable | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a260_bmsState` | page 260 | Front body controller: a260 bms state; raw 9 = signal not available (SNA) | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a261_eFuseVoltage` | page 261 | Front body controller: a261 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a261_vbatProtVoltage` | page 261 | Front body controller: a261 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a262_eFuseVoltage` | page 262 | Front body controller: a262 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a262_vbatProtVoltage` | page 262 | Front body controller: a262 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a263_eFuseVoltage` | page 263 | Front body controller: a263 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a263_vbatProtVoltage` | page 263 | Front body controller: a263 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a264_eFuseVoltage` | page 264 | Front body controller: a264 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a264_vbatProtVoltage` | page 264 | Front body controller: a264 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a265_eFuseVoltage` | page 265 | Front body controller: a265 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a265_vbatProtVoltage` | page 265 | Front body controller: a265 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a266_eFuseVoltage` | page 266 | Front body controller: a266 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a266_vbatProtVoltage` | page 266 | Front body controller: a266 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a267_eFuseVoltage` | page 267 | Front body controller: a267 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a267_vbatProtVoltage` | page 267 | Front body controller: a267 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a268_eFuseVoltage` | page 268 | Front body controller: a268 e fuse voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a268_vbatProtVoltage` | page 268 | Front body controller: a268 vbat prot voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a269_LVBatteryTemp` | page 269 | Front body controller: a269 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a269_IBSCurrent` | page 269 | Front body controller: a269 IBS current | 24\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a269_IBSVoltage` | page 269 | Front body controller: a269 IBS voltage | 36\|11 | little-endian | unsigned | 0.0108873518184 | 0 | V | 0 to 22.2864091723 |  | plausible |
| `VCFRONT_a269_IBSAmpHours` | page 269 | Front body controller: a269 IBS amp hours | 48\|8 | little-endian | unsigned | 0.01 | -2.55 | Ah | -2.55 to 4.4408920985e-16 |  | plausible |
| `VCFRONT_a269_vehiclePowerState` | page 269 | Front body controller: a269 vehicle power state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a270_prechargeChannel` | page 270 | Front body controller: a270 precharge channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `LEFT_CONTROLLER`<br>2 = `AUTOPILOT_1`<br>3 = `AUTOPILOT_2`<br>4 = `RIGHT_CONTROLLER`<br>5 = `MCU_LOGIC` | plausible |
| `VCFRONT_a270_sourceVoltage` | page 270 | Front body controller: a270 source voltage | 19\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 |  | plausible |
| `VCFRONT_a270_loadVoltage` | page 270 | Front body controller: a270 load voltage | 29\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 |  | plausible |
| `VCFRONT_a270_timeout` | page 270 | Front body controller: a270 timeout | 40\|12 | little-endian | unsigned | 1 | 0 | ms | 0 to 4095 |  | plausible |
| `VCFRONT_a271_shortedCellTestTrigger` | page 271 | Front body controller: a271 shorted cell test trigger | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_voltDropOnHighCurrentTrigger` | page 271 | Front body controller: a271 volt drop on high current trigger | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_deadLVMinimalAhDischargedTrigger` | page 271 | Front body controller: a271 dead LV minimal ah discharged trigger | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_resistanceEstimationHardFailTrigger` | page 271 | Front body controller: a271 resistance estimation hard fail trigger | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_dcrMilliOhmsAboveThresholdTrigger` | page 271 | Front body controller: a271 dcr milli ohms above threshold trigger | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_prechargeLVLoadReductionTrigger` | page 271 | Front body controller: a271 precharge LV load reduction trigger | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a271_instantPrechargeDCRTooHighTrigger` | page 271 | Front body controller: a271 instant precharge DCR too high trigger | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a279_snsShortCircuit` | page 279 | Front body controller: a279 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a279_snsDisconnect` | page 279 | Front body controller: a279 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a279_snsRateChangeUp` | page 279 | Front body controller: a279 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a279_snsRateChangeDown` | page 279 | Front body controller: a279 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a280_snsShortCircuit` | page 280 | Front body controller: a280 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a280_snsDisconnect` | page 280 | Front body controller: a280 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a280_snsRateChangeUp` | page 280 | Front body controller: a280 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a280_snsRateChangeDown` | page 280 | Front body controller: a280 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a283_thmlFanDisabled` | page 283 | Front body controller: a283 thml fan disabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a283_thmlFanLimited` | page 283 | Front body controller: a283 thml fan limited | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a283_thmlFanDemand` | page 283 | Front body controller: a283 thml fan demand | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a283_thmlFanDemandLimit` | page 283 | Front body controller: a283 thml fan demand limit | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a283_thmlFanPhaseI` | page 283 | Front body controller: a283 thml fan phase i | 40\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCFRONT_a283_thmlFanPhaseILimit` | page 283 | Front body controller: a283 thml fan phase i limit | 48\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCFRONT_a284_driverState` | page 284 | Front body controller: a284 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a284_driverThermWarn` | page 284 | Front body controller: a284 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_driverThermShutdown` | page 284 | Front body controller: a284 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_undervoltage` | page 284 | Front body controller: a284 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_chargePumpUndervoltage` | page 284 | Front body controller: a284 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilOpenX` | page 284 | Front body controller: a284 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilOpenY` | page 284 | Front body controller: a284 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortXPGnd` | page 284 | Front body controller: a284 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortXPVbb` | page 284 | Front body controller: a284 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortXNGnd` | page 284 | Front body controller: a284 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortXNVbb` | page 284 | Front body controller: a284 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortYPGnd` | page 284 | Front body controller: a284 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortYPVbb` | page 284 | Front body controller: a284 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortYNGnd` | page 284 | Front body controller: a284 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_isCoilShortYNVbb` | page 284 | Front body controller: a284 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a284_driverHasCommError` | page 284 | Front body controller: a284 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_driverState` | page 285 | Front body controller: a285 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a285_driverThermWarn` | page 285 | Front body controller: a285 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_driverThermShutdown` | page 285 | Front body controller: a285 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_undervoltage` | page 285 | Front body controller: a285 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_chargePumpUndervoltage` | page 285 | Front body controller: a285 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilOpenX` | page 285 | Front body controller: a285 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilOpenY` | page 285 | Front body controller: a285 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortXPGnd` | page 285 | Front body controller: a285 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortXPVbb` | page 285 | Front body controller: a285 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortXNGnd` | page 285 | Front body controller: a285 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortXNVbb` | page 285 | Front body controller: a285 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortYPGnd` | page 285 | Front body controller: a285 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortYPVbb` | page 285 | Front body controller: a285 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortYNGnd` | page 285 | Front body controller: a285 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_isCoilShortYNVbb` | page 285 | Front body controller: a285 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a285_driverHasCommError` | page 285 | Front body controller: a285 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_driverState` | page 286 | Front body controller: a286 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a286_driverThermWarn` | page 286 | Front body controller: a286 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_driverThermShutdown` | page 286 | Front body controller: a286 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_undervoltage` | page 286 | Front body controller: a286 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_chargePumpUndervoltage` | page 286 | Front body controller: a286 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilOpenX` | page 286 | Front body controller: a286 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilOpenY` | page 286 | Front body controller: a286 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortXPGnd` | page 286 | Front body controller: a286 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortXPVbb` | page 286 | Front body controller: a286 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortXNGnd` | page 286 | Front body controller: a286 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortXNVbb` | page 286 | Front body controller: a286 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortYPGnd` | page 286 | Front body controller: a286 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortYPVbb` | page 286 | Front body controller: a286 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortYNGnd` | page 286 | Front body controller: a286 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_isCoilShortYNVbb` | page 286 | Front body controller: a286 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a286_driverHasCommError` | page 286 | Front body controller: a286 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_driverState` | page 287 | Front body controller: a287 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a287_driverThermWarn` | page 287 | Front body controller: a287 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_driverThermShutdown` | page 287 | Front body controller: a287 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_undervoltage` | page 287 | Front body controller: a287 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_chargePumpUndervoltage` | page 287 | Front body controller: a287 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilOpenX` | page 287 | Front body controller: a287 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilOpenY` | page 287 | Front body controller: a287 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortXPGnd` | page 287 | Front body controller: a287 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortXPVbb` | page 287 | Front body controller: a287 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortXNGnd` | page 287 | Front body controller: a287 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortXNVbb` | page 287 | Front body controller: a287 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortYPGnd` | page 287 | Front body controller: a287 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortYPVbb` | page 287 | Front body controller: a287 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortYNGnd` | page 287 | Front body controller: a287 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_isCoilShortYNVbb` | page 287 | Front body controller: a287 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a287_driverHasCommError` | page 287 | Front body controller: a287 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_driverState` | page 288 | Front body controller: a288 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a288_driverThermWarn` | page 288 | Front body controller: a288 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_driverThermShutdown` | page 288 | Front body controller: a288 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_undervoltage` | page 288 | Front body controller: a288 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_chargePumpUndervoltage` | page 288 | Front body controller: a288 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilOpenX` | page 288 | Front body controller: a288 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilOpenY` | page 288 | Front body controller: a288 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortXPGnd` | page 288 | Front body controller: a288 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortXPVbb` | page 288 | Front body controller: a288 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortXNGnd` | page 288 | Front body controller: a288 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortXNVbb` | page 288 | Front body controller: a288 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortYPGnd` | page 288 | Front body controller: a288 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortYPVbb` | page 288 | Front body controller: a288 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortYNGnd` | page 288 | Front body controller: a288 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_isCoilShortYNVbb` | page 288 | Front body controller: a288 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a288_driverHasCommError` | page 288 | Front body controller: a288 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_driverState` | page 289 | Front body controller: a289 driver state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `UNPOWERED`<br>2 = `RESET`<br>3 = `INIT_COMM`<br>4 = `COMM_ERROR`<br>5 = `ENABLE_MOTOR`<br>6 = `READY`<br>7 = `STALL`<br>8 = `FAULT_SHORT_COIL`<br>9 = `FAULT_OPEN_COIL`<br>10 = `DRIVER_FAULT` | plausible |
| `VCFRONT_a289_driverThermWarn` | page 289 | Front body controller: a289 driver therm warn | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_driverThermShutdown` | page 289 | Front body controller: a289 driver therm shutdown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_undervoltage` | page 289 | Front body controller: a289 undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_chargePumpUndervoltage` | page 289 | Front body controller: a289 charge pump undervoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilOpenX` | page 289 | Front body controller: a289 is coil open x | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilOpenY` | page 289 | Front body controller: a289 is coil open y | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortXPGnd` | page 289 | Front body controller: a289 is coil short XP gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortXPVbb` | page 289 | Front body controller: a289 is coil short XP vbb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortXNGnd` | page 289 | Front body controller: a289 is coil short XN gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortXNVbb` | page 289 | Front body controller: a289 is coil short XN vbb | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortYPGnd` | page 289 | Front body controller: a289 is coil short YP gnd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortYPVbb` | page 289 | Front body controller: a289 is coil short YP vbb | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortYNGnd` | page 289 | Front body controller: a289 is coil short YN gnd | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_isCoilShortYNVbb` | page 289 | Front body controller: a289 is coil short YN vbb | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a289_driverHasCommError` | page 289 | Front body controller: a289 driver has comm error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_outputFaulted` | page 290 | Front body controller: a290 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_currentSenseFaulted` | page 290 | Front body controller: a290 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_tempSenseFaulted` | page 290 | Front body controller: a290 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_underCurrent` | page 290 | Front body controller: a290 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_overCurrent` | page 290 | Front body controller: a290 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a290_overTemperature` | page 290 | Front body controller: a290 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_outputFaulted` | page 291 | Front body controller: a291 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_currentSenseFaulted` | page 291 | Front body controller: a291 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_tempSenseFaulted` | page 291 | Front body controller: a291 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_underCurrent` | page 291 | Front body controller: a291 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_overCurrent` | page 291 | Front body controller: a291 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a291_overTemperature` | page 291 | Front body controller: a291 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_outputFaulted` | page 292 | Front body controller: a292 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_currentSenseFaulted` | page 292 | Front body controller: a292 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_tempSenseFaulted` | page 292 | Front body controller: a292 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_underCurrent` | page 292 | Front body controller: a292 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_overCurrent` | page 292 | Front body controller: a292 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a292_overTemperature` | page 292 | Front body controller: a292 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_outputFaulted` | page 293 | Front body controller: a293 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_currentSenseFaulted` | page 293 | Front body controller: a293 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_tempSenseFaulted` | page 293 | Front body controller: a293 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_underCurrent` | page 293 | Front body controller: a293 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_overCurrent` | page 293 | Front body controller: a293 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a293_overTemperature` | page 293 | Front body controller: a293 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_outputFaulted` | page 294 | Front body controller: a294 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_currentSenseFaulted` | page 294 | Front body controller: a294 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_tempSenseFaulted` | page 294 | Front body controller: a294 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_underCurrent` | page 294 | Front body controller: a294 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_overCurrent` | page 294 | Front body controller: a294 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a294_overTemperature` | page 294 | Front body controller: a294 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_outputFaulted` | page 295 | Front body controller: a295 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_currentSenseFaulted` | page 295 | Front body controller: a295 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_tempSenseFaulted` | page 295 | Front body controller: a295 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_underCurrent` | page 295 | Front body controller: a295 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_overCurrent` | page 295 | Front body controller: a295 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a295_overTemperature` | page 295 | Front body controller: a295 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a297_bmbDeviceId` | page 297 | Front body controller: a297 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCFRONT_a297_bmbDeviceFaultTempMask` | page 297 | Front body controller: a297 bmb device fault temp mask | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a300_oldType` | page 300 | Front body controller: a300 old type | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMDM`<br>1 = `KEBODA`<br>3 = `UNKOWN` | plausible |
| `VCFRONT_a300_newType` | page 300 | Front body controller: a300 new type | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PMDM`<br>1 = `KEBODA`<br>3 = `UNKOWN` | plausible |
| `VCFRONT_a302_LINFrameStatus` | page 302 | Front body controller: a302 LIN frame status | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `OK`<br>2 = `TIMEOUT`<br>3 = `ERROR`<br>4 = `NA` | plausible |
| `VCFRONT_a303_vehicleSpeed` | page 303 | Front body controller: a303 vehicle speed | 16\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT_a303_postVoltage` | page 303 | Front body controller: a303 post voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a303_lockStatus` | page 303 | Front body controller: a303 lock status; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `UNLOCKED`<br>2 = `LOCKED` | plausible |
| `VCFRONT_a304_voltage` | page 304 | Front body controller: a304 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a304_temperature` | page 304 | Front body controller: a304 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a305_voltage` | page 305 | Front body controller: a305 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a305_temperature` | page 305 | Front body controller: a305 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a305_actuatorCurrent` | page 305 | Front body controller: a305 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a306_voltage` | page 306 | Front body controller: a306 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a306_temperature` | page 306 | Front body controller: a306 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a306_actuatorCurrent` | page 306 | Front body controller: a306 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a307_voltage` | page 307 | Front body controller: a307 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a307_temperature` | page 307 | Front body controller: a307 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a307_actuatorCurrent` | page 307 | Front body controller: a307 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a308_voltage` | page 308 | Front body controller: a308 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a308_temperature` | page 308 | Front body controller: a308 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a308_actuatorCurrent` | page 308 | Front body controller: a308 actuator current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a309_vehicleSpeed` | page 309 | Front body controller: a309 vehicle speed | 16\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT_a309_switchVoltage` | page 309 | Front body controller: a309 switch voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a309_lockStatus` | page 309 | Front body controller: a309 lock status; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `UNLOCKED`<br>2 = `LOCKED` | plausible |
| `VCFRONT_a334_maxSlope` | page 334 | Front body controller: a334 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a334_avgCurrent` | page 334 | Front body controller: a334 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a334_maxCurrent` | page 334 | Front body controller: a334 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a334_vehicleState` | page 334 | Front body controller: a334 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a335_maxSlope` | page 335 | Front body controller: a335 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a335_avgCurrent` | page 335 | Front body controller: a335 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a335_maxCurrent` | page 335 | Front body controller: a335 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a335_vehicleState` | page 335 | Front body controller: a335 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a336_maxSlope` | page 336 | Front body controller: a336 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a336_avgCurrent` | page 336 | Front body controller: a336 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a336_maxCurrent` | page 336 | Front body controller: a336 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a336_vehicleState` | page 336 | Front body controller: a336 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a337_maxSlope` | page 337 | Front body controller: a337 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a337_avgCurrent` | page 337 | Front body controller: a337 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a337_maxCurrent` | page 337 | Front body controller: a337 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a337_vehicleState` | page 337 | Front body controller: a337 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a338_maxSlope` | page 338 | Front body controller: a338 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a338_avgCurrent` | page 338 | Front body controller: a338 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a338_maxCurrent` | page 338 | Front body controller: a338 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a338_vehicleState` | page 338 | Front body controller: a338 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a339_maxSlope` | page 339 | Front body controller: a339 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a339_avgCurrent` | page 339 | Front body controller: a339 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a339_maxCurrent` | page 339 | Front body controller: a339 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a339_vehicleState` | page 339 | Front body controller: a339 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a340_maxSlope` | page 340 | Front body controller: a340 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a340_avgCurrent` | page 340 | Front body controller: a340 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a340_maxCurrent` | page 340 | Front body controller: a340 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a340_vehicleState` | page 340 | Front body controller: a340 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a341_maxSlope` | page 341 | Front body controller: a341 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a341_avgCurrent` | page 341 | Front body controller: a341 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a341_maxCurrent` | page 341 | Front body controller: a341 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a341_vehicleState` | page 341 | Front body controller: a341 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a342_maxSlope` | page 342 | Front body controller: a342 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a342_avgCurrent` | page 342 | Front body controller: a342 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a342_maxCurrent` | page 342 | Front body controller: a342 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a342_vehicleState` | page 342 | Front body controller: a342 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a343_maxSlope` | page 343 | Front body controller: a343 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a343_avgCurrent` | page 343 | Front body controller: a343 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a343_maxCurrent` | page 343 | Front body controller: a343 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a343_vehicleState` | page 343 | Front body controller: a343 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a344_maxSlope` | page 344 | Front body controller: a344 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a344_avgCurrent` | page 344 | Front body controller: a344 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a344_maxCurrent` | page 344 | Front body controller: a344 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a344_vehicleState` | page 344 | Front body controller: a344 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a345_maxSlope` | page 345 | Front body controller: a345 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a345_avgCurrent` | page 345 | Front body controller: a345 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a345_maxCurrent` | page 345 | Front body controller: a345 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a345_vehicleState` | page 345 | Front body controller: a345 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a346_maxSlope` | page 346 | Front body controller: a346 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a346_avgCurrent` | page 346 | Front body controller: a346 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a346_maxCurrent` | page 346 | Front body controller: a346 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a346_vehicleState` | page 346 | Front body controller: a346 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a347_maxSlope` | page 347 | Front body controller: a347 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a347_avgCurrent` | page 347 | Front body controller: a347 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a347_maxCurrent` | page 347 | Front body controller: a347 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a347_vehicleState` | page 347 | Front body controller: a347 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a348_maxSlope` | page 348 | Front body controller: a348 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a348_avgCurrent` | page 348 | Front body controller: a348 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a348_maxCurrent` | page 348 | Front body controller: a348 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a348_vehicleState` | page 348 | Front body controller: a348 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a349_maxSlope` | page 349 | Front body controller: a349 max slope | 16\|12 | little-endian | unsigned | 0.1 | 0 | A/ms | 0 to 409.5 |  | plausible |
| `VCFRONT_a349_avgCurrent` | page 349 | Front body controller: a349 avg current | 28\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a349_maxCurrent` | page 349 | Front body controller: a349 max current | 40\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a349_vehicleState` | page 349 | Front body controller: a349 vehicle state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a350_espValveCurrent` | page 350 | Front body controller: a350 esp valve current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a353_wiperHeaterCurrent` | page 353 | Front body controller: a353 wiper heater current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a353_batteryVoltage` | page 353 | Front body controller: a353 battery voltage | 24\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a353_ambientTemperature` | page 353 | Front body controller: a353 ambient temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCFRONT_a354_windshieldCameraHeaterCurrent` | page 354 | Front body controller: a354 windshield camera heater current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a354_batteryVoltage` | page 354 | Front body controller: a354 battery voltage | 24\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCFRONT_a354_ambientTemperature` | page 354 | Front body controller: a354 ambient temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCFRONT_a355_fluidNotFilled` | page 355 | Front body controller: a355 fluid not filled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a355_systemNotCommissioned` | page 355 | Front body controller: a355 system not commissioned | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a355_serviceLockout` | page 355 | Front body controller: a355 service lockout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a355_factoryGated` | page 355 | Front body controller: a355 factory gated | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a356_fluidNotFilled` | page 356 | Front body controller: a356 fluid not filled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a356_systemNotCommissioned` | page 356 | Front body controller: a356 system not commissioned | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a356_serviceLockout` | page 356 | Front body controller: a356 service lockout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a356_factoryGated` | page 356 | Front body controller: a356 factory gated | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a356_refCommissionStatus` | page 356 | Front body controller: a356 ref commission status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a357_maxTransientCurrent` | page 357 | Front body controller: a357 max transient current | 16\|10 | little-endian | unsigned | 0.02 | 0 | A | 0 to 20.46 |  | plausible |
| `VCFRONT_a358_maxTransientCurrent` | page 358 | Front body controller: a358 max transient current | 16\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCFRONT_a359_IBSVolts` | page 359 | Front body controller: a359 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a359_IBSAh` | page 359 | Front body controller: a359 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a359_vehiclePowerState` | page 359 | Front body controller: a359 vehicle power state | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a359_batterySMState` | page 359 | Front body controller: a359 battery SM state | 42\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a359_hvState` | page 359 | Front body controller: a359 hv state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a359_coolantHasBeenFilled` | page 359 | Front body controller: a359 coolant has been filled | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a359_crashDetected` | page 359 | Front body controller: a359 crash detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a359_BMS_MIA` | page 359 | Front body controller: a359 BMS MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a359_PCS_MIA` | page 359 | Front body controller: a359 PCS MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a359_serviceMode` | page 359 | Signal reported by Front body controller | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a359_dcdcLVSupportStatus` | page 359 | Front body controller: a359 dcdc LV support status | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCFRONT_a359_bmsState` | page 359 | Front body controller: a359 bms state; raw 9 = signal not available (SNA) | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a360_vehicleLoadShedActive` | page 360 | Front body controller: a360 vehicle load shed active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a360_notEnoughPowerForSupport` | page 360 | Front body controller: a360 not enough power for support | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a367_bmsSoc` | page 367 | Front body controller: a367 bms soc | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a368_bmsRequestRemoved` | page 368 | Front body controller: a368 bms request removed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_enteringState` | page 368 | Front body controller: a368 entering state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | plausible |
| `VCFRONT_a368_exitingState` | page 368 | Front body controller: a368 exiting state | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_READY`<br>1 = `READY`<br>2 = `BATTERY_HEATING`<br>3 = `BATTERY_DISCHARGE`<br>4 = `INHIBIT_FOR_REST`<br>5 = `FAULTED` | plausible |
| `VCFRONT_a368_bmsSoc` | page 368 | Front body controller: a368 bms soc | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a368_systemFaulted` | page 368 | Front body controller: a368 system faulted | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_coolantTempSensorsFaulted` | page 368 | Front body controller: a368 coolant temp sensors faulted | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_coolantValveFaulted` | page 368 | Front body controller: a368 coolant valve faulted | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_louverFaulted` | page 368 | Front body controller: a368 louver faulted | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_fansFaulted` | page 368 | Front body controller: a368 fans faulted | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_coolantNotFilled` | page 368 | Front body controller: a368 coolant not filled | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_coolantPumpsFaulted` | page 368 | Front body controller: a368 coolant pumps faulted | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_preconditionsNotMet` | page 368 | Front body controller: a368 preconditions not met | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a368_belowSocMin` | page 368 | Front body controller: a368 below soc min | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a369_powerGenerationLimited` | page 369 | Front body controller: a369 power generation limited | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a369_heatRejectionLimited` | page 369 | Front body controller: a369 heat rejection limited | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a369_bmsSoc` | page 369 | Front body controller: a369 bms soc | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a369_wasteHeatPower` | page 369 | Front body controller: a369 waste heat power | 32\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 12700 |  | plausible |
| `VCFRONT_a370_IBSVolts` | page 370 | Front body controller: a370 IBS volts | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a370_IBSAh` | page 370 | Front body controller: a370 IBS ah | 28\|12 | little-endian | signed | 0.1 | 0 | Ah | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a370_notEnoughPowerForSupport` | page 370 | Front body controller: a370 not enough power for support | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a370_serviceMode` | page 370 | Signal reported by Front body controller | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a370_sleepCurrent` | page 370 | Front body controller: a370 sleep current | 42\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a370_SOC` | page 370 | Front body controller: a370 SOC; raw 7 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 2.5 | 5 | PCT | 5 to 20 | 7 = `SNA` | plausible |
| `VCFRONT_a371_shortedCellTestTrigger` | page 371 | Front body controller: a371 shorted cell test trigger | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_voltDropOnHighCurrentTrigger` | page 371 | Front body controller: a371 volt drop on high current trigger | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_deadLVMinimalAhDischargedTrigger` | page 371 | Front body controller: a371 dead LV minimal ah discharged trigger | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_resistanceEstimationHardFailTrigger` | page 371 | Front body controller: a371 resistance estimation hard fail trigger | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_dcrMilliOhmsAboveThresholdTrigger` | page 371 | Front body controller: a371 dcr milli ohms above threshold trigger | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_prechargeLVLoadReductionTrigger` | page 371 | Front body controller: a371 precharge LV load reduction trigger | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a371_instantPrechargeDCRTooHighTrigger` | page 371 | Front body controller: a371 instant precharge DCR too high trigger | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a372_bmbDeviceId` | page 372 | Front body controller: a372 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCFRONT_a372_bmbDeviceFaultBrickMask` | page 372 | Front body controller: a372 bmb device fault brick mask | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a373_tempSuperheatActual` | page 373 | Front body controller: a373 temp superheat actual; raw 1023 = signal not available (SNA) | 16\|10 | little-endian | unsigned | 0.1 | -20 | degC | -20 to 82.2 | 1023 = `SNA` | plausible |
| `VCFRONT_a373_tempSuperheatTarget` | page 373 | Front body controller: a373 temp superheat target | 26\|10 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 102.3 |  | plausible |
| `VCFRONT_a373_compDemandChiller` | page 373 | Front body controller: a373 comp demand chiller | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a374_lccInletSolenoidISense` | page 374 | Front body controller: a374 lcc inlet solenoid i sense | 16\|8 | little-endian | signed | 0.01 | 0 | A | -1.28 to 1.27 |  | plausible |
| `VCFRONT_a377_wiperStuckOutOfPark` | page 377 | Front body controller: a377 wiper stuck out of park | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a377_wiperStuckInPark` | page 377 | Front body controller: a377 wiper stuck in park | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a378_wiperBlocked` | page 378 | Front body controller: a378 wiper blocked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a378_wiperOverload` | page 378 | Front body controller: a378 wiper overload | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NORMAL`<br>1 = `TQLIMIT1`<br>2 = `TQLIMIT2` | plausible |
| `VCFRONT_a378_wiperFault` | page 378 | Front body controller: a378 wiper fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a378_wiperOvertemperature` | page 378 | Front body controller: a378 wiper overtemperature | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NORMAL`<br>1 = `TLIMIT1`<br>2 = `TLIMIT2`<br>3 = `TLIMIT3` | plausible |
| `VCFRONT_a378_wiperUndervoltage` | page 378 | Front body controller: a378 wiper undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a378_wiperOvervoltage` | page 378 | Front body controller: a378 wiper overvoltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a378_wiperLINError` | page 378 | Front body controller: a378 wiper LIN error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a387_shortedCellFaultCounter` | page 387 | Front body controller: a387 shorted cell fault counter | 16\|3 | little-endian | unsigned | 1 | 0 | - | 0 to 7 |  | plausible |
| `VCFRONT_a387_minVoltageReached` | page 387 | Front body controller: a387 min voltage reached | 19\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a387_opportunisticTest` | page 387 | Front body controller: a387 opportunistic test | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a387_IBSTemp` | page 387 | Front body controller: a387 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCFRONT_a387_maxCurrentReached` | page 387 | Front body controller: a387 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a388_shortedCellFaultCounter` | page 388 | Front body controller: a388 shorted cell fault counter | 16\|3 | little-endian | unsigned | 1 | 0 | - | 0 to 7 |  | plausible |
| `VCFRONT_a388_minVoltageReached` | page 388 | Front body controller: a388 min voltage reached | 19\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a388_opportunisticTest` | page 388 | Front body controller: a388 opportunistic test | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a388_IBSTemp` | page 388 | Front body controller: a388 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCFRONT_a388_maxCurrentReached` | page 388 | Front body controller: a388 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a389_closedAtSpeed` | page 389 | Front body controller: a389 closed at speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a389_faultedWhileOpenAtSpeed` | page 389 | Front body controller: a389 faulted while open at speed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a389_possiblyStuckClosed` | page 389 | Front body controller: a389 possibly stuck closed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a389_vehicleSpeed` | page 389 | Front body controller: a389 vehicle speed | 19\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT_a389_temperature` | page 389 | Front body controller: a389 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a389_latchStatus` | page 389 | Front body controller: a389 latch status; raw 0 = signal not available (SNA) | 40\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCFRONT_a391_switchMismatch` | page 391 | Front body controller: a391 switch mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a391_switch1Shorted` | page 391 | Front body controller: a391 switch1 shorted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a391_switch1Disconnected` | page 391 | Front body controller: a391 switch1 disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a391_switch2Shorted` | page 391 | Front body controller: a391 switch2 shorted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a391_switch2Disconnected` | page 391 | Front body controller: a391 switch2 disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a391_switch1Voltage` | page 391 | Front body controller: a391 switch1 voltage | 21\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCFRONT_a391_switch2Voltage` | page 391 | Front body controller: a391 switch2 voltage | 32\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCFRONT_a392_bmbDeviceId` | page 392 | Front body controller: a392 bmb device id | 16\|4 | little-endian | unsigned | 1 | 1 |  | 1 to 16 |  | layout-only |
| `VCFRONT_a392_bmbDeviceFaultBrickMask` | page 392 | Front body controller: a392 bmb device fault brick mask | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a397_discharge` | page 397 | Front body controller: a397 discharge | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a397_suction` | page 397 | Front body controller: a397 suction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a397_liquid` | page 397 | Front body controller: a397 liquid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a397_offsetError` | page 397 | Front body controller: a397 offset error | 19\|10 | little-endian | signed | 0.2 | 0 | C | -102.4 to 102.2 |  | plausible |
| `VCFRONT_a397_runTimeOffSetDetected` | page 397 | Front body controller: a397 run time off set detected | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a401_LVBatteryTemp` | page 401 | Front body controller: a401 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a401_IBSCurrent` | page 401 | Front body controller: a401 IBS current | 24\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a401_IBSVoltage` | page 401 | Front body controller: a401 IBS voltage | 36\|11 | little-endian | unsigned | 0.0108873518184 | 0 | V | 0 to 22.2864091723 |  | plausible |
| `VCFRONT_a401_IBSAmpHours` | page 401 | Front body controller: a401 IBS amp hours | 48\|8 | little-endian | unsigned | 0.01 | -2.55 | Ah | -2.55 to 4.4408920985e-16 |  | plausible |
| `VCFRONT_a402_LVBatteryTemp` | page 402 | Front body controller: a402 LV battery temp; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a402_batterySMState` | page 402 | Front body controller: a402 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a402_failureToPrechargeRisk` | page 402 | Front body controller: a402 failure to precharge risk | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_electricalDisconnectLVBattery` | page 402 | Front body controller: a402 electrical disconnect LV battery | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_communicationDisconnectLVBattery` | page 402 | Front body controller: a402 communication disconnect LV battery | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_reverseBatteryFault` | page 402 | Front body controller: a402 reverse battery fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_MOSOpen` | page 402 | Front body controller: a402 MOS open | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_serviceMode` | page 402 | Signal reported by Front body controller | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a402_frunkOpen` | page 402 | Front body controller: a402 frunk open | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a404_minVoltageReached` | page 404 | Front body controller: a404 min voltage reached | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCFRONT_a404_IBSTemp` | page 404 | Front body controller: a404 IBS temp | 32\|16 | little-endian | signed | 0.01 | 0 | degC | -327.68 to 327.67 |  | plausible |
| `VCFRONT_a404_maxCurrentReached` | page 404 | Front body controller: a404 max current reached | 48\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | plausible |
| `VCFRONT_a407_dcrMilliOhms` | page 407 | Front body controller: a407 dcr milli ohms | 16\|8 | little-endian | unsigned | 0.2 | 0 | mOhms | 0 to 51 |  | plausible |
| `VCFRONT_a407_dcr12VThreshold` | page 407 | Front body controller: a407 dcr12 v threshold | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `40_MILLIOHMS`<br>2 = `35_MILLIOHMS`<br>3 = `30_MILLIOHMS`<br>4 = `27_MILLIOHMS`<br>5 = `24_MILLIOHMS`<br>6 = `22_MILLIOHMS`<br>7 = `20_MILLIOHMS`<br>8 = `19_MILLIOHMS`<br>9 = `18_MILLIOHMS`<br>10 = `17_MILLIOHMS`<br>11 = `16_MILLIOHMS`<br>12 = `15_MILLIOHMS` | plausible |
| `VCFRONT_a407_avgIntervalCurrent` | page 407 | Front body controller: a407 avg interval current | 28\|5 | little-endian | unsigned | 1 | -31 | A | -31 to 0 |  | plausible |
| `VCFRONT_a407_intervalCurrentVariance` | page 407 | Front body controller: a407 interval current variance | 33\|6 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6.3 |  | plausible |
| `VCFRONT_a407_avgPulseCurrent` | page 407 | Front body controller: a407 avg pulse current | 39\|7 | little-endian | unsigned | 1 | -127 | A | -127 to 0 |  | plausible |
| `VCFRONT_a407_pulseCurrentVariance` | page 407 | Front body controller: a407 pulse current variance | 46\|6 | little-endian | unsigned | 0.25 | 0 | A | 0 to 15.75 |  | plausible |
| `VCFRONT_a407_IBSTemperature` | page 407 | Front body controller: a407 IBS temperature | 52\|8 | little-endian | unsigned | 0.5 | -30 | degC | -30 to 97.5 |  | plausible |
| `VCFRONT_a407_testCounter` | page 407 | Front body controller: a407 test counter | 60\|2 | little-endian | unsigned | 1 | 0 | - | 0 to 3 |  | plausible |
| `VCFRONT_a407_testingExpended` | page 407 | Front body controller: a407 testing expended | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a407_opportunisticTest` | page 407 | Front body controller: a407 opportunistic test | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a409_brushlessMotorConfigurationInvalid` | page 409 | Front body controller: a409 brushless motor configuration invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a414_dcrMilliOhms` | page 414 | Front body controller: a414 dcr milli ohms | 16\|6 | little-endian | unsigned | 1 | 0 | mOhms | 0 to 63 |  | plausible |
| `VCFRONT_a414_LVBatteryTemp` | page 414 | Front body controller: a414 LV battery temp; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a414_IBSCurrent` | page 414 | Front body controller: a414 IBS current | 31\|12 | little-endian | signed | 0.1 | 0 | A | -204.8 to 204.7 |  | plausible |
| `VCFRONT_a414_IBSVoltage` | page 414 | Front body controller: a414 IBS voltage | 43\|11 | little-endian | unsigned | 0.0108873518184 | 0 | V | 0 to 22.2864091723 |  | plausible |
| `VCFRONT_a414_IBSAmpHours` | page 414 | Front body controller: a414 IBS amp hours | 54\|8 | little-endian | unsigned | 0.01 | -2.55 | Ah | -2.55 to 4.4408920985e-16 |  | plausible |
| `VCFRONT_a414_vehiclePowerState` | page 414 | Front body controller: a414 vehicle power state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a415_dcrMilliOhms` | page 415 | Front body controller: a415 dcr milli ohms | 16\|6 | little-endian | unsigned | 1 | 0 | mOhms | 0 to 63 |  | plausible |
| `VCFRONT_a415_LVBatteryTemp` | page 415 | Front body controller: a415 LV battery temp; raw 127 = signal not available (SNA) | 22\|7 | little-endian | unsigned | 1 | -40 | degC | -40 to 86 | 127 = `SNA` | plausible |
| `VCFRONT_a415_IBSCurrent` | page 415 | Front body controller: a415 IBS current | 29\|9 | little-endian | signed | 0.5 | 0 | A | -128 to 127.5 |  | plausible |
| `VCFRONT_a415_IBSVoltage` | page 415 | Front body controller: a415 IBS voltage | 38\|9 | little-endian | unsigned | 0.04 | 0 | V | 0 to 20.44 |  | plausible |
| `VCFRONT_a415_IBSAmpHours` | page 415 | Front body controller: a415 IBS amp hours | 47\|7 | little-endian | unsigned | 0.02 | -2.55 | Ah | -2.55 to -0.01 |  | plausible |
| `VCFRONT_a415_vehiclePowerState` | page 415 | Front body controller: a415 vehicle power state | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a415_HV_UP` | page 415 | Front body controller: a415 HV UP | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_hvUpFirstTrigger` | page 415 | Front body controller: a415 hv up first trigger | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_hvUpAnyTrigger` | page 415 | Front body controller: a415 hv up any trigger | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_pcsEFuseUnstable` | page 415 | Front body controller: a415 pcs e fuse unstable | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_vcrightEfuseUnstable` | page 415 | Front body controller: a415 vcright efuse unstable | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_vcleftEfuseUnstable` | page 415 | Front body controller: a415 vcleft efuse unstable | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_contactorEFuseUnstable` | page 415 | Front body controller: a415 contactor e fuse unstable | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a415_hvcEFuseUnstable` | page 415 | Front body controller: a415 hvc e fuse unstable | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a416_brickVoltageMin` | page 416 | Front body controller: a416 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a416_brickVoltageMax` | page 416 | Front body controller: a416 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a416_packCurrent` | page 416 | Front body controller: a416 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a416_socMin` | page 416 | Front body controller: a416 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a416_brickId` | page 416 | Front body controller: a416 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a417_brickVoltageMin` | page 417 | Front body controller: a417 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a417_brickVoltageMax` | page 417 | Front body controller: a417 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a417_packCurrent` | page 417 | Front body controller: a417 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a417_socMax` | page 417 | Front body controller: a417 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a417_brickId` | page 417 | Front body controller: a417 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a418_brickVoltageMin` | page 418 | Front body controller: a418 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a418_brickVoltageMax` | page 418 | Front body controller: a418 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a418_packCurrent` | page 418 | Front body controller: a418 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a418_socMax` | page 418 | Front body controller: a418 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a418_brickId` | page 418 | Front body controller: a418 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a419_brickVoltageMin` | page 419 | Front body controller: a419 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a419_brickVoltageMax` | page 419 | Front body controller: a419 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a419_packCurrent` | page 419 | Front body controller: a419 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a419_socMin` | page 419 | Front body controller: a419 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a419_brickId` | page 419 | Front body controller: a419 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a423_brickVoltageMin` | page 423 | Front body controller: a423 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a423_brickVoltageMax` | page 423 | Front body controller: a423 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a423_packCurrent` | page 423 | Front body controller: a423 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a423_socMin` | page 423 | Front body controller: a423 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a423_brickId` | page 423 | Front body controller: a423 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a424_brickVoltageMin` | page 424 | Front body controller: a424 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a424_brickVoltageMax` | page 424 | Front body controller: a424 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a424_packCurrent` | page 424 | Front body controller: a424 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a424_socMin` | page 424 | Front body controller: a424 soc min | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a424_brickId` | page 424 | Front body controller: a424 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a431_netPackCurrent` | page 431 | Front body controller: a431 net pack current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a431_maxChargeCurrentLimit` | page 431 | Front body controller: a431 max charge current limit; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a431_hvjbCurrentLimit` | page 431 | Front body controller: a431 hvjb current limit; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a432_targetCurrent` | page 432 | Front body controller: a432 target current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a432_packCurrent` | page 432 | Front body controller: a432 pack current; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a433_bmbModuleId` | page 433 | Front body controller: a433 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a433_packTypeData` | page 433 | Front body controller: a433 pack type data | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a433_cellTypeData` | page 433 | Front body controller: a433 cell type data | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a433_bmbModuleIdValid` | page 433 | Front body controller: a433 bmb module id valid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a433_useBmbModuleId` | page 433 | Front body controller: a433 use bmb module id | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a434_bmbModuleId` | page 434 | Front body controller: a434 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a434_packTypeData` | page 434 | Front body controller: a434 pack type data | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a434_cellTypeData` | page 434 | Front body controller: a434 cell type data | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a434_bmbModuleIdValid` | page 434 | Front body controller: a434 bmb module id valid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a434_useBmbModuleId` | page 434 | Front body controller: a434 use bmb module id | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a436_netPackCurrent` | page 436 | Front body controller: a436 net pack current; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a436_maxDischargeCurrentLimit` | page 436 | Front body controller: a436 max discharge current limit; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a436_hvjbCurrentLimit` | page 436 | Front body controller: a436 hvjb current limit; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 | -32768 = `SNA` | plausible |
| `VCFRONT_a437_nvmDataMissingA` | page 437 | Front body controller: a437 nvm data missing a | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a437_nvmDataMissingB` | page 437 | Front body controller: a437 nvm data missing b | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a438_temperature` | page 438 | Front body controller: a438 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCFRONT_a438_sensorId` | page 438 | Front body controller: a438 sensor id | 32\|6 | little-endian | unsigned | 1 | 1 |  | 1 to 64 |  | layout-only |
| `VCFRONT_a439_temperature` | page 439 | Front body controller: a439 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCFRONT_a439_sensorId` | page 439 | Front body controller: a439 sensor id | 32\|6 | little-endian | unsigned | 1 | 1 |  | 1 to 64 |  | layout-only |
| `VCFRONT_a441_bmbModuleId` | page 441 | Front body controller: a441 bmb module id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a441_bmbModuleIdPrev` | page 441 | Front body controller: a441 bmb module id prev | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a444_retriesAvailable` | page 444 | Front body controller: a444 retries available | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a444_channel` | page 444 | Front body controller: a444 channel | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a444_watchdog` | page 444 | Front body controller: a444 watchdog | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_gateDriver` | page 444 | Front body controller: a444 gate driver | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_overcurrent` | page 444 | Front body controller: a444 overcurrent | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_supplyUndervoltage` | page 444 | Front body controller: a444 supply undervoltage | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_cpUndervoltage` | page 444 | Front body controller: a444 cp undervoltage | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_overTempShutdown` | page 444 | Front body controller: a444 over temp shutdown | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_overTempWarning` | page 444 | Front body controller: a444 over temp warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_highSide2GateDriver` | page 444 | Front body controller: a444 high side2 gate driver | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_lowSide2GateDriver` | page 444 | Front body controller: a444 low side2 gate driver | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_highSide1GateDriver` | page 444 | Front body controller: a444 high side1 gate driver | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_lowSide1GateDriver` | page 444 | Front body controller: a444 low side1 gate driver | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_highSide2OverCurent` | page 444 | Front body controller: a444 high side2 over curent | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_lowSide2OverCurent` | page 444 | Front body controller: a444 low side2 over curent | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_highSide1OverCurent` | page 444 | Front body controller: a444 high side1 over curent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_lowSide1OverCurent` | page 444 | Front body controller: a444 low side1 over curent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_spiInit` | page 444 | Front body controller: a444 spi init | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_spiPeriodicCheck` | page 444 | Front body controller: a444 spi periodic check | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_spiFault` | page 444 | Front body controller: a444 spi fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_voltageMonitor` | page 444 | Front body controller: a444 voltage monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a444_enableLow` | page 444 | Front body controller: a444 enable low | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compFaultRefrigerant` | page 446 | Front body controller: a446 comp fault refrigerant | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compFaultTdHigh` | page 446 | Front body controller: a446 comp fault td high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compFaultPdLow` | page 446 | Front body controller: a446 comp fault pd low | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compFaultPdHigh` | page 446 | Front body controller: a446 comp fault pd high | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compFaultPsLow` | page 446 | Front body controller: a446 comp fault ps low | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyLowAmbient` | page 446 | Front body controller: a446 comp standby low ambient | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyLowDischPress` | page 446 | Front body controller: a446 comp standby low disch press | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyHVNotReady` | page 446 | Front body controller: a446 comp standby HV not ready | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyCommunication` | page 446 | Front body controller: a446 comp standby communication | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbySelfNotReady` | page 446 | Front body controller: a446 comp standby self not ready | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyRefrigNotOk` | page 446 | Front body controller: a446 comp standby refrig not ok | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyCoastDownMode` | page 446 | Front body controller: a446 comp standby coast down mode | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyMultiplePdCutouts` | page 446 | Front body controller: a446 comp standby multiple pd cutouts | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyShowroomMode` | page 446 | Front body controller: a446 comp standby showroom mode | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_compStandbyMultipleTdCutouts` | page 446 | Front body controller: a446 comp standby multiple td cutouts | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_hpCabinLoadType` | page 446 | Front body controller: a446 hp cabin load type | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `CC`<br>2 = `REHEAT`<br>3 = `EVAP` | plausible |
| `VCFRONT_a446_hpBatteryLoadType` | page 446 | Front body controller: a446 hp battery load type | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `BATT_HEAT`<br>2 = `BATT_COOL` | plausible |
| `VCFRONT_a446_usingModeledPs` | page 446 | Front body controller: a446 using modeled ps | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_usingModeledPd` | page 446 | Front body controller: a446 using modeled pd | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_usingModeledPl` | page 446 | Front body controller: a446 using modeled pl | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_usingModeledTs` | page 446 | Front body controller: a446 using modeled ts | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_usingModeledTd` | page 446 | Front body controller: a446 using modeled td | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_usingModeledTl` | page 446 | Front body controller: a446 using modeled tl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorHasOffsetTd` | page 446 | Front body controller: a446 sensor has offset td | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorHasOffsetPd` | page 446 | Front body controller: a446 sensor has offset pd | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorDroopPd` | page 446 | Front body controller: a446 sensor droop pd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorHasOffsetTl` | page 446 | Front body controller: a446 sensor has offset tl | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentPs` | page 446 | Front body controller: a446 sensor intermittent ps | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentPd` | page 446 | Front body controller: a446 sensor intermittent pd | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentPl` | page 446 | Front body controller: a446 sensor intermittent pl | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentTs` | page 446 | Front body controller: a446 sensor intermittent ts | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentTd` | page 446 | Front body controller: a446 sensor intermittent td | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_sensorIntermittentTl` | page 446 | Front body controller: a446 sensor intermittent tl | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_highSuctionSuperheat` | page 446 | Front body controller: a446 high suction superheat | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_evapLowPsCutout` | page 446 | Front body controller: a446 evap low ps cutout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_batteryOverTemp` | page 446 | Front body controller: a446 battery over temp | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_hvacSystemFault` | page 446 | Front body controller: a446 hvac system fault | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_coolantSysLockedOut` | page 446 | Front body controller: a446 coolant sys locked out | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_refSysLockedOut` | page 446 | Front body controller: a446 ref sys locked out | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_chillerEXVNotReady` | page 446 | Front body controller: a446 chiller EXV not ready | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_CCLEXVNotReady` | page 446 | Front body controller: a446 CCLEXV not ready | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_CCREXVNotReady` | page 446 | Front body controller: a446 CCREXV not ready | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_LCCEXVNotReady` | page 446 | Front body controller: a446 LCCEXV not ready | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_evapEXVNotReady` | page 446 | Front body controller: a446 evap EXV not ready | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_recircEXVNotReady` | page 446 | Front body controller: a446 recirc EXV not ready | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a446_checkA447Alert` | page 446 | Front body controller: a446 check A447 alert | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_caseHVACUnavailable` | page 447 | Front body controller: a447 case HVAC unavailable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_heatPumpHVACUnavailable` | page 447 | Front body controller: a447 heat pump HVAC unavailable | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_activeLouverCompromised` | page 447 | Front body controller: a447 active louver compromised | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_coolantValveCompromised` | page 447 | Front body controller: a447 coolant valve compromised | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_ambientSourcingCompromised` | page 447 | Front body controller: a447 ambient sourcing compromised | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_scavengeLoopCompromised` | page 447 | Front body controller: a447 scavenge loop compromised | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_coolantSystemCompromised` | page 447 | Front body controller: a447 coolant system compromised | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_hvBattActiveDischgCompromised` | page 447 | Front body controller: a447 hv batt active dischg compromised | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_hvBatteryDischargingCompromised` | page 447 | Front body controller: a447 hv battery discharging compromised | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_lccSolenoidCompromised` | page 447 | Front body controller: a447 lcc solenoid compromised | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigerantSystemCompromised` | page 447 | Front body controller: a447 refrigerant system compromised | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_powertrainThermalFansCompromised` | page 447 | Front body controller: a447 powertrain thermal fans compromised | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigDischargePressCompromised` | page 447 | Front body controller: a447 refrig discharge press compromised | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigeDischargeTempCompromised` | page 447 | Front body controller: a447 refrige discharge temp compromised | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigSuctionPressCompromised` | page 447 | Front body controller: a447 refrig suction press compromised | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigSuctionTempCompromised` | page 447 | Front body controller: a447 refrig suction temp compromised | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigLiquidPressCompromised` | page 447 | Front body controller: a447 refrig liquid press compromised | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a447_refrigLiquidTempCompromised` | page 447 | Front body controller: a447 refrig liquid temp compromised | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a459_coolantFillActive` | page 459 | Front body controller: a459 coolant fill active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a459_refrigerantFillActive` | page 459 | Front body controller: a459 refrigerant fill active | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CellOVLevel1` | page 462 | Front body controller: a462 cell OV level1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CellOVLevel2` | page 462 | Front body controller: a462 cell OV level2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CellOVLevel3` | page 462 | Front body controller: a462 cell OV level3 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CellUVLevel1` | page 462 | Front body controller: a462 cell UV level1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CellUVLevel2` | page 462 | Front body controller: a462 cell UV level2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_ModuleOTLevel1` | page 462 | Front body controller: a462 module OT level1 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_PackOVLevel1` | page 462 | Front body controller: a462 pack OV level1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_PackOVLevel2` | page 462 | Front body controller: a462 pack OV level2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_DischrgOCLevel1` | page 462 | Front body controller: a462 dischrg OC level1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_HardwareOCLevel2` | page 462 | Front body controller: a462 hardware OC level2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_ChrgOCLevel1` | page 462 | Front body controller: a462 chrg OC level1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_ChrgOCLevel2` | page 462 | Front body controller: a462 chrg OC level2 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_MOSFETOTLevel1` | page 462 | Front body controller: a462 MOSFETOT level1 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_CPA_State` | page 462 | Front body controller: a462 CPA state | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_NTCTempDiffWarnLevel1` | page 462 | Front body controller: a462 NTC temp diff warn level1 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_KBValueLostFault` | page 462 | Front body controller: a462 KB value lost fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_BalanceCircuitFault` | page 462 | Front body controller: a462 balance circuit fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_MOSOpenFault` | page 462 | Front body controller: a462 MOS open fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_DeepDischarge` | page 462 | Front body controller: a462 deep discharge | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_SamplingError` | page 462 | Front body controller: a462 sampling error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_MOSFETStuckClose` | page 462 | Front body controller: a462 MOSFET stuck close | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_MOSFETStuckOpen` | page 462 | Front body controller: a462 MOSFET stuck open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_Imbalance` | page 462 | Front body controller: a462 imbalance | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_serviceMode` | page 462 | Signal reported by Front body controller | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a462_frunkOpen` | page 462 | Front body controller: a462 frunk open | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switchMismatch` | page 463 | Front body controller: a463 switch mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switch1Shorted` | page 463 | Front body controller: a463 switch1 shorted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switch1Disconnected` | page 463 | Front body controller: a463 switch1 disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switch2Shorted` | page 463 | Front body controller: a463 switch2 shorted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switch2Disconnected` | page 463 | Front body controller: a463 switch2 disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a463_switch1Voltage` | page 463 | Front body controller: a463 switch1 voltage | 21\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCFRONT_a463_switch2Voltage` | page 463 | Front body controller: a463 switch2 voltage | 32\|10 | little-endian | unsigned | 5 | 0 | mV | 0 to 5115 |  | plausible |
| `VCFRONT_a464_flowIndex` | page 464 | Front body controller: a464 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a464_flowIndexFiltered` | page 464 | Front body controller: a464 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a464_subcool` | page 464 | Front body controller: a464 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a464_subcoolFiltered` | page 464 | Front body controller: a464 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a465_flowIndex` | page 465 | Front body controller: a465 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a465_flowIndexFiltered` | page 465 | Front body controller: a465 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a465_subcool` | page 465 | Front body controller: a465 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a465_subcoolFiltered` | page 465 | Front body controller: a465 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a465_flaggedAtSteadyState` | page 465 | Front body controller: a465 flagged at steady state | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a465_flaggedAtUnsteadyState` | page 465 | Front body controller: a465 flagged at unsteady state | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a466_flowIndex` | page 466 | Front body controller: a466 flow index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a466_flowIndexFiltered` | page 466 | Front body controller: a466 flow index filtered | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `VCFRONT_a466_subcool` | page 466 | Front body controller: a466 subcool | 32\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a466_subcoolFiltered` | page 466 | Front body controller: a466 subcool filtered | 40\|7 | little-endian | unsigned | 0.4 | -10 | degC | -10 to 40.8 |  | plausible |
| `VCFRONT_a467_powerIndexFiltered` | page 467 | Front body controller: a467 power index filtered | 16\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 127 |  | plausible |
| `VCFRONT_a470_pressureLiquid` | page 470 | Front body controller: a470 pressure liquid | 16\|8 | little-endian | unsigned | 0.2 | 0 | bar | 0 to 51 |  | plausible |
| `VCFRONT_a470_pressureDischarge` | page 470 | Front body controller: a470 pressure discharge | 24\|8 | little-endian | unsigned | 0.2 | 0 | bar | 0 to 51 |  | plausible |
| `VCFRONT_a474_ssl100Bank1Status` | page 474 | Front body controller: a474 ssl100 bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank2Status` | page 474 | Front body controller: a474 ssl100 bank2 status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank3Status` | page 474 | Front body controller: a474 ssl100 bank3 status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank4Status` | page 474 | Front body controller: a474 ssl100 bank4 status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank5Status` | page 474 | Front body controller: a474 ssl100 bank5 status | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank6Status` | page 474 | Front body controller: a474 ssl100 bank6 status | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank7Status` | page 474 | Front body controller: a474 ssl100 bank7 status | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank8Status` | page 474 | Front body controller: a474 ssl100 bank8 status | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_ssl100Bank9Status` | page 474 | Front body controller: a474 ssl100 bank9 status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a474_lowBeamPrefieldStatus` | page 474 | Front body controller: a474 low beam prefield status | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a474_drl1Status` | page 474 | Front body controller: a474 drl1 status | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a474_drl2Status` | page 474 | Front body controller: a474 drl2 status | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a474_drl3Status` | page 474 | Front body controller: a474 drl3 status | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a474_turnStatus` | page 474 | Front body controller: a474 turn status | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a474_fanStatus` | page 474 | Front body controller: a474 fan status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_TPS92520_COMPOV` | page 474 | Front body controller: a474 TPS92520 COMPOV | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_TPS92520_HSILIM` | page 474 | Front body controller: a474 TPS92520 HSILIM | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_TPS92520_BSTUV` | page 474 | Front body controller: a474 TPS92520 BSTUV | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_BoostRailStatus` | page 474 | Front body controller: a474 boost rail status | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_EEPROM_DataStatus` | page 474 | Front body controller: a474 EEPROM data status | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a474_LMMVariant` | page 474 | Front body controller: a474 LMM variant; raw 0 = signal not available (SNA) | 57\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NOT_LMM4_OR_UNKNOWN`<br>2 = `LMM4` | plausible |
| `VCFRONT_a474_headlampECURevision` | page 474 | Front body controller: a474 headlamp ECU revision | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a475_ssl100Bank1Status` | page 475 | Front body controller: a475 ssl100 bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank2Status` | page 475 | Front body controller: a475 ssl100 bank2 status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank3Status` | page 475 | Front body controller: a475 ssl100 bank3 status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank4Status` | page 475 | Front body controller: a475 ssl100 bank4 status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank5Status` | page 475 | Front body controller: a475 ssl100 bank5 status | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank6Status` | page 475 | Front body controller: a475 ssl100 bank6 status | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank7Status` | page 475 | Front body controller: a475 ssl100 bank7 status | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank8Status` | page 475 | Front body controller: a475 ssl100 bank8 status | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_ssl100Bank9Status` | page 475 | Front body controller: a475 ssl100 bank9 status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a475_lowBeamPrefieldStatus` | page 475 | Front body controller: a475 low beam prefield status | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a475_drl1Status` | page 475 | Front body controller: a475 drl1 status | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a475_drl2Status` | page 475 | Front body controller: a475 drl2 status | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a475_drl3Status` | page 475 | Front body controller: a475 drl3 status | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a475_turnStatus` | page 475 | Front body controller: a475 turn status | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a475_fanStatus` | page 475 | Front body controller: a475 fan status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_TPS92520_COMPOV` | page 475 | Front body controller: a475 TPS92520 COMPOV | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_TPS92520_HSILIM` | page 475 | Front body controller: a475 TPS92520 HSILIM | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_TPS92520_BSTUV` | page 475 | Front body controller: a475 TPS92520 BSTUV | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_BoostRailStatus` | page 475 | Front body controller: a475 boost rail status | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_EEPROM_DataStatus` | page 475 | Front body controller: a475 EEPROM data status | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a475_LMMVariant` | page 475 | Front body controller: a475 LMM variant; raw 0 = signal not available (SNA) | 57\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NOT_LMM4_OR_UNKNOWN`<br>2 = `LMM4` | plausible |
| `VCFRONT_a475_headlampECURevision` | page 475 | Front body controller: a475 headlamp ECU revision | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a476_FRM1_timedOut` | page 476 | Front body controller: a476 FRM1 timed out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM2_timedOut` | page 476 | Front body controller: a476 FRM2 timed out | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM3_timedOut` | page 476 | Front body controller: a476 FRM3 timed out | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM4_timedOut` | page 476 | Front body controller: a476 FRM4 timed out | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM5_timedOut` | page 476 | Front body controller: a476 FRM5 timed out | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM6_timedOut` | page 476 | Front body controller: a476 FRM6 timed out | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM7_timedOut` | page 476 | Front body controller: a476 FRM7 timed out | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM8_timedOut` | page 476 | Front body controller: a476 FRM8 timed out | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM9_timedOut` | page 476 | Front body controller: a476 FRM9 timed out | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM10_timedOut` | page 476 | Front body controller: a476 FRM10 timed out | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM11_timedOut` | page 476 | Front body controller: a476 FRM11 timed out | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_FRM12_timedOut` | page 476 | Front body controller: a476 FRM12 timed out | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_factoryMode` | page 476 | Front body controller: a476 factory mode | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_serviceMode` | page 476 | Signal reported by Front body controller | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_transportMode` | page 476 | Front body controller: a476 transport mode | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_frunkOpen` | page 476 | Front body controller: a476 frunk open | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a476_vehiclePowerState` | page 476 | Front body controller: a476 vehicle power state | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a476_batterySMState` | page 476 | Front body controller: a476 battery SM state | 34\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a476_ECPAState` | page 476 | Front body controller: a476 ECPA state; raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a477_cell1Voltage` | page 477 | Front body controller: a477 cell1 voltage | 16\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a477_cell2Voltage` | page 477 | Front body controller: a477 cell2 voltage | 25\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a477_cell3Voltage` | page 477 | Front body controller: a477 cell3 voltage | 34\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a477_cell4Voltage` | page 477 | Front body controller: a477 cell4 voltage | 43\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a477_sumCellVoltage` | page 477 | Front body controller: a477 sum cell voltage | 52\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a477_deepDischargeFlag` | page 477 | Front body controller: a477 deep discharge flag | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a477_serviceMode` | page 477 | Signal reported by Front body controller | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a477_frunkOpen` | page 477 | Front body controller: a477 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_battFaultPackOverVoltage` | page 478 | Front body controller: a478 batt fault pack over voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_battFaultHardwareOverCurrent` | page 478 | Front body controller: a478 batt fault hardware over current | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_battFaultChargeOverCurrent` | page 478 | Front body controller: a478 batt fault charge over current | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_battFaultCellUnderVoltage` | page 478 | Front body controller: a478 batt fault cell under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_battFaultCellOverVoltage` | page 478 | Front body controller: a478 batt fault cell over voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_vehiclePowerState` | page 478 | Front body controller: a478 vehicle power state | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a478_batterySMState` | page 478 | Front body controller: a478 battery SM state | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a478_bmsState` | page 478 | Front body controller: a478 bms state; raw 9 = signal not available (SNA) | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a478_dcdcLVSupportStatus` | page 478 | Front body controller: a478 dcdc LV support status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCFRONT_a478_factoryMode` | page 478 | Front body controller: a478 factory mode | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_serviceMode` | page 478 | Signal reported by Front body controller | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_transportMode` | page 478 | Front body controller: a478 transport mode | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_notEnoughPowerForSupport` | page 478 | Front body controller: a478 not enough power for support | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_crashDetected` | page 478 | Front body controller: a478 crash detected | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_BMS_MIA` | page 478 | Front body controller: a478 BMS MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_PCS_MIA` | page 478 | Front body controller: a478 PCS MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_HVBlockingMismatch` | page 478 | Front body controller: a478 HV blocking mismatch | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_HV_UP` | page 478 | Front body controller: a478 HV UP | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_pcsEFuseStable` | page 478 | Front body controller: a478 pcs e fuse stable | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_vcrightEFuseStable` | page 478 | Front body controller: a478 vcright e fuse stable | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_contactorEFuseStable` | page 478 | Front body controller: a478 contactor e fuse stable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_hvcEFuseStable` | page 478 | Front body controller: a478 hvc e fuse stable | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a478_frunkOpen` | page 478 | Front body controller: a478 frunk open | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a479_FRM3_timedOut` | page 479 | Front body controller: a479 FRM3 timed out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a479_ECPAState` | page 479 | Front body controller: a479 ECPA state; raw 3 = signal not available (SNA) | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a479_factoryMode` | page 479 | Front body controller: a479 factory mode | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a479_serviceMode` | page 479 | Signal reported by Front body controller | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a479_transportMode` | page 479 | Front body controller: a479 transport mode | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a479_frunkLatchStatus` | page 479 | Front body controller: a479 frunk latch status; raw 0 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCFRONT_a479_vehiclePowerState` | page 479 | Front body controller: a479 vehicle power state | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a479_batterySMState` | page 479 | Front body controller: a479 battery SM state | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a480_channel` | page 480 | Front body controller: a480 channel | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PCS`<br>1 = `LEFT_CONTROLLER`<br>2 = `RIGHT_CONTROLLER`<br>3 = `EPAS_1`<br>4 = `EPAS_2`<br>5 = `HCU_ESP_ABS`<br>6 = `IBOOSTER`<br>7 = `INVALID` | plausible |
| `VCFRONT_a480_reset` | page 480 | Front body controller: a480 reset | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_spiError` | page 480 | Front body controller: a480 spi error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_autoOn` | page 480 | Front body controller: a480 auto on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_diagnosticBit` | page 480 | Front body controller: a480 diagnostic bit | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_deviceError` | page 480 | Front body controller: a480 device error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_overcurrent` | page 480 | Front body controller: a480 overcurrent | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_unexpectedLock` | page 480 | Front body controller: a480 unexpected lock | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_disableOutputFault` | page 480 | Front body controller: a480 disable output fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_vsUndervoltage` | page 480 | Front body controller: a480 vs undervoltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_hardShort` | page 480 | Front body controller: a480 hard short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_vdsMax` | page 480 | Front body controller: a480 vds max | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_bypassSaturation` | page 480 | Front body controller: a480 bypass saturation | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_fuseLatch` | page 480 | Front body controller: a480 fuse latch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_deviceOvertemperature` | page 480 | Front body controller: a480 device overtemperature | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_ntcOvertemperature` | page 480 | Front body controller: a480 ntc overtemperature | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_vgsLow` | page 480 | Front body controller: a480 vgs low | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_chargePumpLow` | page 480 | Front body controller: a480 charge pump low | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_watchdog` | page 480 | Front body controller: a480 watchdog | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_spiNotDone` | page 480 | Front body controller: a480 spi not done | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_configIncorrect` | page 480 | Front body controller: a480 config incorrect | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_bufferFull` | page 480 | Front body controller: a480 buffer full | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_hitAlertRateLimit` | page 480 | Front body controller: a480 hit alert rate limit | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_hwlo` | page 480 | Front body controller: a480 hwlo | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a480_enable` | page 480 | Front body controller: a480 enable | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a486_mcuGraphicsEFuseCurrent` | page 486 | Front body controller: a486 mcu graphics e fuse current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a490_coolantPumpType` | page 490 | Front body controller: a490 coolant pump type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DUAL`<br>1 = `SINGLE_PUMP_BATT`<br>2 = `DUAL_SAN_P4`<br>4 = `DUAL_SAN_P4_LUB`<br>5 = `DUAL_MIX` | plausible |
| `VCFRONT_a493_minBrickSocId` | page 493 | Front body controller: a493 min brick soc id | 16\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | layout-only |
| `VCFRONT_a493_minBrickSocByOcvMax` | page 493 | Front body controller: a493 min brick soc by ocv max | 24\|8 | little-endian | unsigned | 0.5 | 0 | PCT | 0 to 127.5 |  | plausible |
| `VCFRONT_a493_maxBrickSocId` | page 493 | Front body controller: a493 max brick soc id | 32\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | layout-only |
| `VCFRONT_a493_maxBrickSocByOcvMin` | page 493 | Front body controller: a493 max brick soc by ocv min | 40\|8 | little-endian | unsigned | 0.5 | 0 | PCT | 0 to 127.5 |  | plausible |
| `VCFRONT_a493_maxBrickSoc` | page 493 | Front body controller: a493 max brick soc | 48\|7 | little-endian | unsigned | 1 | 0 | PCT | 0 to 127 |  | plausible |
| `VCFRONT_a493_avgBrickSoc` | page 493 | Front body controller: a493 avg brick soc | 56\|7 | little-endian | unsigned | 1 | 0 | PCT | 0 to 127 |  | plausible |
| `VCFRONT_a495_SoCUnrecoverable` | page 495 | Front body controller: a495 so c unrecoverable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_SocTooLow` | page 495 | Front body controller: a495 soc too low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_retryExpended` | page 495 | Front body controller: a495 retry expended | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_LVBMSMIA` | page 495 | Front body controller: a495 LVBMSMIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_reverseBatteryEFuseFault` | page 495 | Front body controller: a495 reverse battery e fuse fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_DCDCOff` | page 495 | Front body controller: a495 DCDC off | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_HVOff` | page 495 | Front body controller: a495 HV off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_externalInteraction` | page 495 | Front body controller: a495 external interaction | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_serviceMode` | page 495 | Signal reported by Front body controller | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_frunkOpen` | page 495 | Front body controller: a495 frunk open | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a495_externalPowerSupply` | page 495 | Front body controller: a495 external power supply | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_reverseBatteryEFuseFault` | page 496 | Front body controller: a496 reverse battery e fuse fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_vehicleLoadShedActive` | page 496 | Front body controller: a496 vehicle load shed active | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_MOSState` | page 496 | Front body controller: a496 MOS state; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OPEN`<br>1 = `CLOSED`<br>2 = `INVALID`<br>3 = `SNA` | plausible |
| `VCFRONT_a496_serviceMode` | page 496 | Signal reported by Front body controller | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_frunkOpen` | page 496 | Front body controller: a496 frunk open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_PCS_MIA` | page 496 | Front body controller: a496 PCS MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_NotEnoughPowerForSupport` | page 496 | Front body controller: a496 not enough power for support | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a496_bmsState` | page 496 | Front body controller: a496 bms state; raw 9 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a497_serviceMode` | page 497 | Signal reported by Front body controller | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a497_FactoryMode` | page 497 | Front body controller: a497 factory mode | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a497_SOC` | page 497 | Front body controller: a497 SOC | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a497_PackCurrent` | page 497 | Front body controller: a497 pack current | 32\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCFRONT_a497_SumCellVoltage` | page 497 | Front body controller: a497 sum cell voltage | 48\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a497_frunkOpen` | page 497 | Front body controller: a497 frunk open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a500_channel` | page 500 | Front body controller: a500 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a500_mismatchedState` | page 500 | Front body controller: a500 mismatched state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCFRONT_a503_brickVoltageMin` | page 503 | Front body controller: a503 brick voltage min | 16\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a503_brickVoltageMax` | page 503 | Front body controller: a503 brick voltage max | 26\|10 | little-endian | unsigned | 0.005 | 0 | V | 0 to 5.115 |  | plausible |
| `VCFRONT_a503_packCurrent` | page 503 | Front body controller: a503 pack current | 36\|10 | little-endian | signed | 5 | 0 | A | -2560 to 2555 |  | plausible |
| `VCFRONT_a503_socMax` | page 503 | Front body controller: a503 soc max | 46\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCFRONT_a503_brickId` | page 503 | Front body controller: a503 brick id | 54\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | layout-only |
| `VCFRONT_a509_vcrightEFuseCurrent` | page 509 | Front body controller: a509 vcright e fuse current | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a509_vcrightEFuseTemp` | page 509 | Front body controller: a509 vcright e fuse temp | 32\|8 | little-endian | unsigned | 0.75 | 0 | degC | 0 to 191.25 |  | plausible |
| `VCFRONT_a509_ambientTemp` | page 509 | Front body controller: a509 ambient temp | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a509_serviceMode` | page 509 | Signal reported by Front body controller | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a509_frunkOpen` | page 509 | Front body controller: a509 frunk open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a510_sumCellVoltage` | page 510 | Front body controller: a510 sum cell voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a510_packVoltage` | page 510 | Front body controller: a510 pack voltage | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a510_targetPCSVoltage` | page 510 | Front body controller: a510 target PCS voltage | 32\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a510_serviceMode` | page 510 | Signal reported by Front body controller | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a510_frunkOpen` | page 510 | Front body controller: a510 frunk open | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_PCSEFuseCurrent` | page 511 | Front body controller: a511 PCSE fuse current | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a511_DCDCMaxOutputCurrentAllowed` | page 511 | Front body controller: a511 DCDC max output current allowed | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a511_hvState` | page 511 | Front body controller: a511 hv state | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a511_DCDCOutputIsLimited` | page 511 | Front body controller: a511 DCDC output is limited | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_PCSSignalsAreValid` | page 511 | Front body controller: a511 PCS signals are valid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_factoryGated` | page 511 | Front body controller: a511 factory gated | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_vehicleIsUpdating` | page 511 | Front body controller: a511 vehicle is updating | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_serviceMode` | page 511 | Signal reported by Front body controller | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a511_frunkOpen` | page 511 | Front body controller: a511 frunk open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a512_packVoltageIntervalMin` | page 512 | Front body controller: a512 pack voltage interval min | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a512_packVoltageIntervalMax` | page 512 | Front body controller: a512 pack voltage interval max | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a512_packTemperature` | page 512 | Front body controller: a512 pack temperature | 32\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 215 |  | plausible |
| `VCFRONT_a512_sumCellVoltage` | page 512 | Front body controller: a512 sum cell voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a512_overcurrentDirection` | page 512 | Front body controller: a512 overcurrent direction | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INCONCLUSIVE`<br>1 = `CHARGE`<br>2 = `DISCHARGE` | plausible |
| `VCFRONT_a512_serviceMode` | page 512 | Signal reported by Front body controller | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a512_frunkOpen` | page 512 | Front body controller: a512 frunk open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a512_vehiclePowerState` | page 512 | Front body controller: a512 vehicle power state | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a513_packCurrent` | page 513 | Front body controller: a513 pack current | 16\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCFRONT_a513_packTemperature` | page 513 | Front body controller: a513 pack temperature | 32\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 215 |  | plausible |
| `VCFRONT_a513_packVoltage` | page 513 | Front body controller: a513 pack voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a513_packSOC` | page 513 | Front body controller: a513 pack SOC | 48\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCFRONT_a513_serviceMode` | page 513 | Signal reported by Front body controller | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a513_frunkOpen` | page 513 | Front body controller: a513 frunk open | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a513_vehiclePowerState` | page 513 | Front body controller: a513 vehicle power state | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a514_cell1Voltage` | page 514 | Front body controller: a514 cell1 voltage | 16\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a514_cell2Voltage` | page 514 | Front body controller: a514 cell2 voltage | 23\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a514_cell3Voltage` | page 514 | Front body controller: a514 cell3 voltage | 30\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a514_cell4Voltage` | page 514 | Front body controller: a514 cell4 voltage | 37\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a514_packVoltage` | page 514 | Front body controller: a514 pack voltage | 44\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a514_packSOC` | page 514 | Front body controller: a514 pack SOC | 52\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `VCFRONT_a514_serviceMode` | page 514 | Signal reported by Front body controller | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a514_frunkOpen` | page 514 | Front body controller: a514 frunk open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a514_vehiclePowerState` | page 514 | Front body controller: a514 vehicle power state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a515_cell1Voltage` | page 515 | Front body controller: a515 cell1 voltage | 16\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a515_cell2Voltage` | page 515 | Front body controller: a515 cell2 voltage | 23\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a515_cell3Voltage` | page 515 | Front body controller: a515 cell3 voltage | 30\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a515_cell4Voltage` | page 515 | Front body controller: a515 cell4 voltage | 37\|7 | little-endian | unsigned | 0.08 | 0 | V | 0 to 10.16 |  | plausible |
| `VCFRONT_a515_packVoltage` | page 515 | Front body controller: a515 pack voltage | 44\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a515_packSOC` | page 515 | Front body controller: a515 pack SOC | 52\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `VCFRONT_a515_serviceMode` | page 515 | Signal reported by Front body controller | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a515_frunkOpen` | page 515 | Front body controller: a515 frunk open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a515_vehiclePowerState` | page 515 | Front body controller: a515 vehicle power state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a516_IBSVoltage` | page 516 | Front body controller: a516 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a516_HVSoc` | page 516 | Front body controller: a516 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCFRONT_a516_contactorsPermanentlyClosed` | page 516 | Front body controller: a516 contactors permanently closed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a516_LVBatteryDisconnected` | page 516 | Front body controller: a516 LV battery disconnected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a516_reverseBatteryFault` | page 516 | Front body controller: a516 reverse battery fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a516_LVBatteryCannotSupportVehicle` | page 516 | Front body controller: a516 LV battery cannot support vehicle | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a517_IBSVoltage` | page 517 | Front body controller: a517 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a517_HVSoc` | page 517 | Front body controller: a517 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCFRONT_a518_packVoltage` | page 518 | Front body controller: a518 pack voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a518_IBSVoltage` | page 518 | Front body controller: a518 IBS voltage | 24\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCFRONT_a518_targetPCSVoltage` | page 518 | Front body controller: a518 target PCS voltage | 33\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a518_outputVoltageAtPCS` | page 518 | Front body controller: a518 output voltage at PCS | 41\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a518_packSOC` | page 518 | Front body controller: a518 pack SOC | 49\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCFRONT_a518_serviceMode` | page 518 | Signal reported by Front body controller | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a518_frunkOpen` | page 518 | Front body controller: a518 frunk open | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a518_vehiclePowerState` | page 518 | Front body controller: a518 vehicle power state | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a519_MatrixBank1Status` | page 519 | Front body controller: a519 matrix bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a519_MatrixBank2Status` | page 519 | Front body controller: a519 matrix bank2 status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a519_MatrixBank3Status` | page 519 | Front body controller: a519 matrix bank3 status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a519_MatrixBank4Status` | page 519 | Front body controller: a519 matrix bank4 status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a519_TurnSignalStatus` | page 519 | Front body controller: a519 turn signal status | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a519_SideMarkerStatus` | page 519 | Front body controller: a519 side marker status | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `UNDERCURRENT_FAULT`<br>2 = `OVERCURRENT_FAULT` | plausible |
| `VCFRONT_a519_DRLStatus` | page 519 | Front body controller: a519 DRL status | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a519_AmbientStatus` | page 519 | Front body controller: a519 ambient status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a519_LBFlatSAEStatus` | page 519 | Front body controller: a519 LB flat SAE status | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a519_LBFlatECEStatus` | page 519 | Front body controller: a519 LB flat ECE status | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a519_TPS92520_COMPOV` | page 519 | Front body controller: a519 TPS92520 COMPOV | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_TPS92520_HSILIM` | page 519 | Front body controller: a519 TPS92520 HSILIM | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_TPS92520_BSTUV` | page 519 | Front body controller: a519 TPS92520 BSTUV | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_CoolingFanStatus` | page 519 | Front body controller: a519 cooling fan status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_BoostRailStatus` | page 519 | Front body controller: a519 boost rail status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_EEPROMCurrentBinStatus` | page 519 | Front body controller: a519 EEPROM current bin status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_EEPROMCalCurrentStatus` | page 519 | Front body controller: a519 EEPROM cal current status | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_HeadlampECURevision` | page 519 | Front body controller: a519 headlamp ECU revision | 50\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a519_NonzeroEEPROMRetries` | page 519 | Front body controller: a519 nonzero EEPROM retries | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a519_MaxEEPROMRetries` | page 519 | Front body controller: a519 max EEPROM retries | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_MatrixBank1Status` | page 520 | Front body controller: a520 matrix bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a520_MatrixBank2Status` | page 520 | Front body controller: a520 matrix bank2 status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a520_MatrixBank3Status` | page 520 | Front body controller: a520 matrix bank3 status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a520_MatrixBank4Status` | page 520 | Front body controller: a520 matrix bank4 status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a520_TurnSignalStatus` | page 520 | Front body controller: a520 turn signal status | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a520_SideMarkerStatus` | page 520 | Front body controller: a520 side marker status | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `UNDERCURRENT_FAULT`<br>2 = `OVERCURRENT_FAULT` | plausible |
| `VCFRONT_a520_DRLStatus` | page 520 | Front body controller: a520 DRL status | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a520_AmbientStatus` | page 520 | Front body controller: a520 ambient status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a520_LBFlatSAEStatus` | page 520 | Front body controller: a520 LB flat SAE status | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a520_LBFlatECEStatus` | page 520 | Front body controller: a520 LB flat ECE status | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a520_TPS92520_COMPOV` | page 520 | Front body controller: a520 TPS92520 COMPOV | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_TPS92520_HSILIM` | page 520 | Front body controller: a520 TPS92520 HSILIM | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_TPS92520_BSTUV` | page 520 | Front body controller: a520 TPS92520 BSTUV | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_CoolingFanStatus` | page 520 | Front body controller: a520 cooling fan status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_BoostRailStatus` | page 520 | Front body controller: a520 boost rail status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_EEPROMCurrentBinStatus` | page 520 | Front body controller: a520 EEPROM current bin status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_EEPROMCalCurrentStatus` | page 520 | Front body controller: a520 EEPROM cal current status | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_HeadlampECURevision` | page 520 | Front body controller: a520 headlamp ECU revision | 50\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a520_NonzeroEEPROMRetries` | page 520 | Front body controller: a520 nonzero EEPROM retries | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a520_MaxEEPROMRetries` | page 520 | Front body controller: a520 max EEPROM retries | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a521_vcleftEFuseCurrent` | page 521 | Front body controller: a521 vcleft e fuse current | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `VCFRONT_a521_vcleftEFuseTemp` | page 521 | Front body controller: a521 vcleft e fuse temp | 32\|8 | little-endian | unsigned | 0.75 | 0 | degC | 0 to 191.25 |  | plausible |
| `VCFRONT_a521_ambientTemp` | page 521 | Front body controller: a521 ambient temp | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCFRONT_a521_serviceMode` | page 521 | Signal reported by Front body controller | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a521_frunkOpen` | page 521 | Front body controller: a521 frunk open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a522_IBSVoltage` | page 522 | Front body controller: a522 IBS voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a522_HVSoc` | page 522 | Front body controller: a522 HV soc | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.3 |  | plausible |
| `VCFRONT_a522_contactorsPermanentlyClosed` | page 522 | Front body controller: a522 contactors permanently closed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a522_LVBatteryDisconnected` | page 522 | Front body controller: a522 LV battery disconnected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a522_reverseBatteryFault` | page 522 | Front body controller: a522 reverse battery fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a522_LVBatteryCannotSupportVehicle` | page 522 | Front body controller: a522 LV battery cannot support vehicle | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a523_channel` | page 523 | Front body controller: a523 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a523_control2Byte1` | page 523 | Front body controller: a523 control2 byte1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a523_control2Byte2` | page 523 | Front body controller: a523 control2 byte2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a523_control2Byte3` | page 523 | Front body controller: a523 control2 byte3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a523_control3Byte2` | page 523 | Front body controller: a523 control3 byte2 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a523_control3Byte3` | page 523 | Front body controller: a523 control3 byte3 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCFRONT_a525_GTW_twelveVBatteryType` | page 525 | Front body controller: a525 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCFRONT_a525_newLVBatteryType` | page 525 | Front body controller: a525 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a525_initialLVBatteryType` | page 525 | Front body controller: a525 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a525_serviceMode` | page 525 | Signal reported by Front body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a525_factoryGated` | page 525 | Front body controller: a525 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a525_frunkOpen` | page 525 | Front body controller: a525 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a527_cell1Voltage` | page 527 | Front body controller: a527 cell1 voltage | 16\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a527_cell2Voltage` | page 527 | Front body controller: a527 cell2 voltage | 26\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a527_cell3Voltage` | page 527 | Front body controller: a527 cell3 voltage | 36\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a527_cell4Voltage` | page 527 | Front body controller: a527 cell4 voltage | 46\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a527_serviceMode` | page 527 | Signal reported by Front body controller | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a527_frunkOpen` | page 527 | Front body controller: a527 frunk open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a528_ECPAStateSNA` | page 528 | Front body controller: a528 ECPA state SNA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a528_ECPAFrameTimeout` | page 528 | Front body controller: a528 ECPA frame timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a528_currentSenseFaulted` | page 528 | Front body controller: a528 current sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a528_serviceMode` | page 528 | Signal reported by Front body controller | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a528_frunkOpen` | page 528 | Front body controller: a528 frunk open | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a531_powerIndexFiltered` | page 531 | Front body controller: a531 power index filtered | 16\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 127 |  | plausible |
| `VCFRONT_a532_eFuseFault` | page 532 | Front body controller: a532 e fuse fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a533_temperature` | page 533 | Front body controller: a533 temperature | 16\|16 | little-endian | unsigned | 0.01 | 0 | C | 0 to 655.35 |  | plausible |
| `VCFRONT_a541_PackTemperature` | page 541 | Front body controller: a541 pack temperature | 16\|9 | little-endian | unsigned | 0.5 | -50 | degC | -50 to 205.5 |  | plausible |
| `VCFRONT_a541_ChargeCurrentLimit` | page 541 | Front body controller: a541 charge current limit | 25\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCFRONT_a541_PeakCurrent` | page 541 | Front body controller: a541 peak current | 35\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCFRONT_a541_AverageCurrent` | page 541 | Front body controller: a541 average current | 45\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCFRONT_a541_SOC` | page 541 | Front body controller: a541 SOC | 56\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a544_serviceMode` | page 544 | Signal reported by Front body controller | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a544_frunkOpen` | page 544 | Front body controller: a544 frunk open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a544_LVBMSSOC` | page 544 | Front body controller: a544 LVBMSSOC | 18\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCFRONT_a545_GTW_twelveVBatteryType` | page 545 | Front body controller: a545 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCFRONT_a545_newLVBatteryType` | page 545 | Front body controller: a545 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a545_serviceMode` | page 545 | Signal reported by Front body controller | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a545_factoryGated` | page 545 | Front body controller: a545 factory gated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a545_frunkOpen` | page 545 | Front body controller: a545 frunk open | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a547_serviceMode` | page 547 | Signal reported by Front body controller | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a547_frunkOpen` | page 547 | Front body controller: a547 frunk open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_vehiclePowerState` | page 548 | Front body controller: a548 vehicle power state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a548_notEnoughPowerForSupport` | page 548 | Front body controller: a548 not enough power for support | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_HVBlockingMismatch` | page 548 | Front body controller: a548 HV blocking mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_LVBatteryCannotSupportVehicle` | page 548 | Front body controller: a548 LV battery cannot support vehicle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_DI_gear` | page 548 | Front body controller: a548 DI gear; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCFRONT_a548_backstopBucketCount` | page 548 | Front body controller: a548 backstop bucket count | 24\|5 | little-endian | unsigned | 0.035 | 0 | Ah | 0 to 1.085 |  | plausible |
| `VCFRONT_a548_hvState` | page 548 | Front body controller: a548 hv state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOWN`<br>1 = `COMING_UP`<br>2 = `GOING_DOWN`<br>3 = `UP_FOR_DRIVE`<br>4 = `UP_FOR_CHARGE`<br>5 = `UP_FOR_DC_CHARGE`<br>6 = `UP` | plausible |
| `VCFRONT_a548_BMS_MIA` | page 548 | Front body controller: a548 BMS MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_PCS_MIA` | page 548 | Front body controller: a548 PCS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_ampHourBucketCount` | page 548 | Front body controller: a548 amp hour bucket count | 34\|6 | little-endian | unsigned | 0.01 | 0 | Ah | 0 to 0.63 |  | plausible |
| `VCFRONT_a548_LVBMSSOC` | page 548 | Front body controller: a548 LVBMSSOC | 40\|5 | little-endian | unsigned | 3 | 0 | % | 0 to 93 |  | plausible |
| `VCFRONT_a548_serviceMode` | page 548 | Signal reported by Front body controller | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_frunkOpen` | page 548 | Front body controller: a548 frunk open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_PCSTargetVoltage` | page 548 | Front body controller: a548 PCS target voltage | 48\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a548_ampHourBucketFilled` | page 548 | Front body controller: a548 amp hour bucket filled | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_HVNotConfirmedUpTrigger` | page 548 | Front body controller: a548 HV not confirmed up trigger | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_PCSNotMeetingTargetTrigger` | page 548 | Front body controller: a548 PCS not meeting target trigger | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_PCSMIATrigger` | page 548 | Front body controller: a548 PCSMIA trigger | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_PCSSaturatedTrigger` | page 548 | Front body controller: a548 PCS saturated trigger | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a548_backstopHit` | page 548 | Front body controller: a548 backstop hit | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a549_MatrixBank1Status` | page 549 | Front body controller: a549 matrix bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a549_SideMarkerStatus` | page 549 | Front body controller: a549 side marker status | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_TurnSignalStatus` | page 549 | Front body controller: a549 turn signal status | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_DRL1Status` | page 549 | Front body controller: a549 DRL1 status | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_DRL2Status` | page 549 | Front body controller: a549 DRL2 status | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_DRL3Status` | page 549 | Front body controller: a549 DRL3 status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_LowBeamStatus` | page 549 | Front body controller: a549 low beam status | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a549_TPS92520_COMPOV` | page 549 | Front body controller: a549 TPS92520 COMPOV | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a549_TPS92520_HSILIM` | page 549 | Front body controller: a549 TPS92520 HSILIM | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a549_TPS92520_BSTUV` | page 549 | Front body controller: a549 TPS92520 BSTUV | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a549_BoostRailStatus` | page 549 | Front body controller: a549 boost rail status | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a549_EEPROMDataStatus` | page 549 | Front body controller: a549 EEPROM data status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a549_HeadlampECURevision` | page 549 | Front body controller: a549 headlamp ECU revision | 43\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a551_headlampCurrent` | page 551 | Front body controller: a551 headlamp current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a552_vcrightSelfTestResult` | page 552 | Front body controller: a552 vcright self test result; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a552_epas3pSelfTestResult` | page 552 | Front body controller: a552 epas3p self test result; raw 12 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a552_epas3sSelfTestResult` | page 552 | Front body controller: a552 epas3s self test result; raw 12 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a553_headlampCurrent` | page 553 | Front body controller: a553 headlamp current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCFRONT_a555_cell1Voltage` | page 555 | Front body controller: a555 cell1 voltage | 16\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a555_cell2Voltage` | page 555 | Front body controller: a555 cell2 voltage | 26\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a555_cell3Voltage` | page 555 | Front body controller: a555 cell3 voltage | 36\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a555_cell4Voltage` | page 555 | Front body controller: a555 cell4 voltage | 46\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | plausible |
| `VCFRONT_a557_MatrixBank1Status` | page 557 | Front body controller: a557 matrix bank1 status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `CRC_ERROR`<br>2 = `PIXEL_ERROR`<br>3 = `UNRESPONSIVE` | plausible |
| `VCFRONT_a557_SideMarkerStatus` | page 557 | Front body controller: a557 side marker status | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_TurnSignalStatus` | page 557 | Front body controller: a557 turn signal status | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_DRL1Status` | page 557 | Front body controller: a557 DRL1 status | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_DRL2Status` | page 557 | Front body controller: a557 DRL2 status | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_DRL3Status` | page 557 | Front body controller: a557 DRL3 status | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_CenterStatus` | page 557 | Front body controller: a557 center status | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_LowBeamStatus` | page 557 | Front body controller: a557 low beam status | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OK`<br>1 = `OVERVOLTAGE_FAULT`<br>2 = `UNDERVOLTAGE_FAULT`<br>3 = `DRIVER_STATUS_FAULT`<br>4 = `OVERVOLTAGE_FALSE_TRIGGER`<br>5 = `UNDERVOLTAGE_FALSE_TRIGGER`<br>6 = `DRIVER_STATUS_FALSE_TRIGGER` | plausible |
| `VCFRONT_a557_TPS92520_COMPOV` | page 557 | Front body controller: a557 TPS92520 COMPOV | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a557_TPS92520_HSILIM` | page 557 | Front body controller: a557 TPS92520 HSILIM | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a557_TPS92520_BSTUV` | page 557 | Front body controller: a557 TPS92520 BSTUV | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a557_BoostRailStatus` | page 557 | Front body controller: a557 boost rail status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a557_EEPROMDataStatus` | page 557 | Front body controller: a557 EEPROM data status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a557_HeadlampECURevision` | page 557 | Front body controller: a557 headlamp ECU revision | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GEN_3_REV_C`<br>2 = `GEN_3_REV_D`<br>3 = `GEN_3_REV_E`<br>4 = `GEN_3_REV_F`<br>5 = `GEN_5_REV_A`<br>6 = `GEN_5_REV_C`<br>7 = `GEN_5_REV_D`<br>8 = `GEN_5_REV_E`<br>15 = `RESERVED` | plausible |
| `VCFRONT_a559_SOC` | page 559 | Front body controller: a559 SOC | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCFRONT_a559_PackCurrent` | page 559 | Front body controller: a559 pack current | 24\|12 | little-endian | unsigned | 0.2 | -600 | A | -600 to 219 |  | plausible |
| `VCFRONT_a559_vehiclePowerState` | page 559 | Front body controller: a559 vehicle power state | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCFRONT_a559_batterySMState` | page 559 | Front body controller: a559 battery SM state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a559_bmsState` | page 559 | Front body controller: a559 bms state; raw 9 = signal not available (SNA) | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `STANDBY`<br>1 = `DRIVE`<br>2 = `SUPPORT`<br>3 = `CHARGE`<br>4 = `FEIM`<br>5 = `CLEAR_FAULT`<br>6 = `FAULT`<br>7 = `WELD`<br>8 = `TEST`<br>9 = `SNA`<br>10 = `DIAG` | plausible |
| `VCFRONT_a559_dcdcLVSupportStatus` | page 559 | Front body controller: a559 dcdc LV support status | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `ACTIVE`<br>2 = `FAULTED` | plausible |
| `VCFRONT_a559_factoryMode` | page 559 | Front body controller: a559 factory mode | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_serviceMode` | page 559 | Signal reported by Front body controller | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_transportMode` | page 559 | Front body controller: a559 transport mode | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_notEnoughPowerForSupport` | page 559 | Front body controller: a559 not enough power for support | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_crashDetected` | page 559 | Front body controller: a559 crash detected | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_BMS_MIA` | page 559 | Front body controller: a559 BMS MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_PCS_MIA` | page 559 | Front body controller: a559 PCS MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_HVBlockingMismatch` | page 559 | Front body controller: a559 HV blocking mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_HV_UP` | page 559 | Front body controller: a559 HV UP | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_pcsEFuseStable` | page 559 | Front body controller: a559 pcs e fuse stable | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_vcrightEFuseStable` | page 559 | Front body controller: a559 vcright e fuse stable | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_contactorEFuseStable` | page 559 | Front body controller: a559 contactor e fuse stable | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_hvcEFuseStable` | page 559 | Front body controller: a559 hvc e fuse stable | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a559_frunkOpen` | page 559 | Front body controller: a559 frunk open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCOP1` | page 560 | Front body controller: a560 high SHCOP1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHBattConditioning` | page 560 | Front body controller: a560 high SH batt conditioning | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCabinReheatCD` | page 560 | Front body controller: a560 high SH cabin reheat CD | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCabinReheatHD` | page 560 | Front body controller: a560 high SH cabin reheat HD | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCabinCooling` | page 560 | Front body controller: a560 high SH cabin cooling | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCabinHeating` | page 560 | Front body controller: a560 high SH cabin heating | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a560_highSHCatchAll` | page 560 | Front body controller: a560 high SH catch all | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a561_efuseTemperature` | page 561 | Front body controller: a561 efuse temperature | 16\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCFRONT_a561_packTemperature` | page 561 | Front body controller: a561 pack temperature | 21\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCFRONT_a561_ambientTemperature` | page 561 | Front body controller: a561 ambient temperature | 26\|6 | little-endian | unsigned | 4 | 0 | C | 0 to 252 |  | plausible |
| `VCFRONT_a561_cell1Voltage` | page 561 | Front body controller: a561 cell1 voltage | 32\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a561_cell2Voltage` | page 561 | Front body controller: a561 cell2 voltage | 39\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a561_cell3Voltage` | page 561 | Front body controller: a561 cell3 voltage | 46\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a561_cell4Voltage` | page 561 | Front body controller: a561 cell4 voltage | 53\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a561_factoryMode` | page 561 | Front body controller: a561 factory mode | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a561_serviceMode` | page 561 | Signal reported by Front body controller | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a561_frunkOpen` | page 561 | Front body controller: a561 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a562_efuseTemperature` | page 562 | Front body controller: a562 efuse temperature | 16\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCFRONT_a562_packTemperature` | page 562 | Front body controller: a562 pack temperature | 21\|5 | little-endian | unsigned | 4 | 0 | C | 0 to 124 |  | plausible |
| `VCFRONT_a562_ambientTemperature` | page 562 | Front body controller: a562 ambient temperature | 26\|6 | little-endian | unsigned | 4 | 0 | C | 0 to 252 |  | plausible |
| `VCFRONT_a562_cell1Voltage` | page 562 | Front body controller: a562 cell1 voltage | 32\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a562_cell2Voltage` | page 562 | Front body controller: a562 cell2 voltage | 39\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a562_cell3Voltage` | page 562 | Front body controller: a562 cell3 voltage | 46\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a562_cell4Voltage` | page 562 | Front body controller: a562 cell4 voltage | 53\|7 | little-endian | unsigned | 0.04 | 0 | V | 0 to 5.08 |  | plausible |
| `VCFRONT_a562_factoryMode` | page 562 | Front body controller: a562 factory mode | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a562_serviceMode` | page 562 | Signal reported by Front body controller | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a562_frunkOpen` | page 562 | Front body controller: a562 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a579_leftHeadlightCurrent` | page 579 | Front body controller: a579 left headlight current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a579_leftHeadlightVoltage` | page 579 | Front body controller: a579 left headlight voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a579_leftHeadlightRemainingRetries` | page 579 | Front body controller: a579 left headlight remaining retries | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a580_rightHeadlightCurrent` | page 580 | Front body controller: a580 right headlight current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCFRONT_a580_rightHeadlightVoltage` | page 580 | Front body controller: a580 right headlight voltage | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCFRONT_a580_rightHeadlightRemainingRetries` | page 580 | Front body controller: a580 right headlight remaining retries | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_a582_batterySMState` | page 582 | Front body controller: a582 battery SM state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `CHARGE`<br>2 = `DISCHARGE`<br>3 = `STANDBY`<br>4 = `RESISTANCE_ESTIMATION`<br>5 = `OTA_STANDBY`<br>6 = `DISCONNECTED_BATTERY_TEST`<br>7 = `SHORTED_CELL_TEST`<br>8 = `FAULT`<br>9 = `RECOVERY`<br>10 = `EXTERNAL_LV_BUS_CONTROL` | plausible |
| `VCFRONT_a582_PCSCurrent` | page 582 | Front body controller: a582 PCS current | 24\|8 | little-endian | unsigned | 0.5 | -127 | A | -127 to 0.5 |  | plausible |
| `VCFRONT_a582_LVBusVoltage` | page 582 | Front body controller: a582 LV bus voltage | 32\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a582_LVBusVoltageSource` | page 582 | Front body controller: a582 LV bus voltage source | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `IBS`<br>2 = `VBAT_MONITOR`<br>3 = `LVBMS` | plausible |
| `VCFRONT_a582_batteryType` | page 582 | Front body controller: a582 battery type | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a582_inFactoryMode` | page 582 | Front body controller: a582 in factory mode | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a582_frunkOpen` | page 582 | Front body controller: a582 frunk open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_leftHeadlampInternalErrorMask` | page 585 | Front body controller: a585 left headlamp internal error mask | 16\|20 | little-endian | unsigned | 1 | 0 |  | 0 to 1048575 |  | layout-only |
| `VCFRONT_a585_rightHeadlampInternalErrorMask` | page 585 | Front body controller: a585 right headlamp internal error mask | 36\|20 | little-endian | unsigned | 1 | 0 |  | 0 to 1048575 |  | layout-only |
| `VCFRONT_a585_inFactoryMode` | page 585 | Front body controller: a585 in factory mode | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_inServiceMode` | page 585 | Signal reported by Front body controller | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_inTransportMode` | page 585 | Front body controller: a585 in transport mode | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_uiMia` | page 585 | Front body controller: a585 ui mia | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_frunkOpen` | page 585 | Front body controller: a585 frunk open | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_leftRailVoltageLow` | page 585 | Front body controller: a585 left rail voltage low | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a585_rightRailVoltageLow` | page 585 | Front body controller: a585 right rail voltage low | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a592_vcleftCutoffEFuseCurveType` | page 592 | Front body controller: a592 vcleft cutoff e fuse curve type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STATIC_EFUSE_CURVE`<br>1 = `DYNAMIC_EFUSE_CURVE` | plausible |
| `VCFRONT_a592_vcleftCutoffCurveOffsetChannel` | page 592 | Front body controller: a592 vcleft cutoff curve offset channel | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a592_vcleftCutoffATerm` | page 592 | Front body controller: a592 vcleft cutoff a term; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 50 | 0 | - | 0 to 3276700 | 65535 = `SNA` | plausible |
| `VCFRONT_a592_vcleftCutoffBTerm` | page 592 | Front body controller: a592 vcleft cutoff b term; raw 128 = signal not available (SNA) | 40\|8 | little-endian | signed | 1 | -78 | - | -206 to 49 | -128 = `SNA` | plausible |
| `VCFRONT_a592_vcleftCutoffCTerm` | page 592 | Front body controller: a592 vcleft cutoff c term; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 50 | 0 | - | -1638400 to 1638350 | -32768 = `SNA` | plausible |
| `VCFRONT_a593_vcleftCutoffEFuseFastBlowType` | page 593 | Front body controller: a593 vcleft cutoff e fuse fast blow type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TIMING`<br>1 = `DEBOUNCE` | plausible |
| `VCFRONT_a593_vcleftCutoffCurrentThreshold` | page 593 | Front body controller: a593 vcleft cutoff current threshold | 17\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a593_vcleftCutoffTimingThresholdMs` | page 593 | Front body controller: a593 vcleft cutoff timing threshold ms | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a593_vcleftCutoffMaxCount` | page 593 | Front body controller: a593 vcleft cutoff max count | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCFRONT_a596_vcrightCutoffEFuseCurveType` | page 596 | Front body controller: a596 vcright cutoff e fuse curve type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STATIC_EFUSE_CURVE`<br>1 = `DYNAMIC_EFUSE_CURVE` | plausible |
| `VCFRONT_a596_vcrightCutoffCurveOffsetChannel` | page 596 | Front body controller: a596 vcright cutoff curve offset channel | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCFRONT_a596_vcrightCutoffATerm` | page 596 | Front body controller: a596 vcright cutoff a term; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 50 | 0 | - | 0 to 3276700 | 65535 = `SNA` | plausible |
| `VCFRONT_a596_vcrightCutoffBTerm` | page 596 | Front body controller: a596 vcright cutoff b term; raw 128 = signal not available (SNA) | 40\|8 | little-endian | signed | 1 | -78 | - | -206 to 49 | -128 = `SNA` | plausible |
| `VCFRONT_a596_vcrightCutoffCTerm` | page 596 | Front body controller: a596 vcright cutoff c term; raw 32768 = signal not available (SNA) | 48\|16 | little-endian | signed | 50 | 0 | - | -1638400 to 1638350 | -32768 = `SNA` | plausible |
| `VCFRONT_a597_vcrightCutoffEFuseFastBlowType` | page 597 | Front body controller: a597 vcright cutoff e fuse fast blow type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TIMING`<br>1 = `DEBOUNCE` | plausible |
| `VCFRONT_a597_vcrightCutoffCurrentThreshold` | page 597 | Front body controller: a597 vcright cutoff current threshold | 17\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 409.5 |  | plausible |
| `VCFRONT_a597_vcrightCutoffTimingThresholdMs` | page 597 | Front body controller: a597 vcright cutoff timing threshold ms | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCFRONT_a597_vcrightCutoffMaxCount` | page 597 | Front body controller: a597 vcright cutoff max count | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCFRONT_a598_vcleftSelfTestResult` | page 598 | Front body controller: a598 vcleft self test result; raw 12 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_RUN`<br>1 = `RUNNING`<br>2 = `PASSED`<br>3 = `FAILED_RAILS_UNSTABLE`<br>4 = `FAILED_EFUSE_OUTPUT_SHORT`<br>5 = `FAILED_POWER_FET_STUCK_ON`<br>6 = `FAILED_ENABLE_LOW_MALFUNCTION`<br>7 = `FAILED_POWER_FET_CHANNEL_OPEN`<br>8 = `FAILED_ENABLE_HIGH_MALFUNCTION`<br>9 = `FAILED_TURN_OFF_PATH_TOO_SLOW`<br>10 = `FAILED_NOT_LATCHED`<br>11 = `SKIPPED`<br>12 = `SNA` | plausible |
| `VCFRONT_a599_GTW_twelveVBatteryType` | page 599 | Front body controller: a599 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCFRONT_a599_newLVBatteryType` | page 599 | Front body controller: a599 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a599_initialLVBatteryType` | page 599 | Front body controller: a599 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCFRONT_a599_serviceMode` | page 599 | Signal reported by Front body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a599_factoryGated` | page 599 | Front body controller: a599 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a599_frunkOpen` | page 599 | Front body controller: a599 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a605_vbatProtVoltage` | page 605 | Front body controller: a605 vbat prot voltage | 16\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 |  | plausible |
| `VCFRONT_a605_sleepBypassVoltage` | page 605 | Front body controller: a605 sleep bypass voltage | 26\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 |  | plausible |
| `VCFRONT_a605_sleepBypassCurrent` | page 605 | Front body controller: a605 sleep bypass current | 36\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCFRONT_a610_switch1State` | page 610 | Front body controller: a610 switch1 state; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCFRONT_a610_switch2State` | page 610 | Front body controller: a610 switch2 state; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCFRONT_a610_dataBufferBits` | page 610 | Front body controller: a610 data buffer bits | 20\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `VCFRONT_a610_temperature` | page 610 | Front body controller: a610 temperature; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCFRONT_a611_tempCoolantPTInlet` | page 611 | Front body controller: a611 temp coolant PT inlet | 16\|6 | little-endian | unsigned | 1 | 20 | degC | 20 to 83 |  | plausible |
| `VCFRONT_a611_tempCoolantPTInletEst` | page 611 | Front body controller: a611 temp coolant PT inlet est | 22\|6 | little-endian | unsigned | 1 | 20 | degC | 20 to 83 |  | plausible |
| `VCFRONT_a611_tempAmbientRaw` | page 611 | Front body controller: a611 temp ambient raw | 28\|6 | little-endian | unsigned | 1 | 20 | degC | 20 to 83 |  | plausible |
| `VCFRONT_a611_radFanAvgSpeed` | page 611 | Front body controller: a611 rad fan avg speed | 34\|6 | little-endian | unsigned | 100 | 0 | RPM | 0 to 6300 |  | plausible |
| `VCFRONT_a611_ptLoopCoolantFlow` | page 611 | Front body controller: a611 pt loop coolant flow | 40\|6 | little-endian | unsigned | 0.5 | 0 | LPM | 0 to 31.5 |  | plausible |
| `VCFRONT_a611_compressorPower` | page 611 | Front body controller: a611 compressor power | 46\|6 | little-endian | unsigned | 200 | 0 | W | 0 to 12600 |  | plausible |
| `VCFRONT_a611_heatGenTotal` | page 611 | Front body controller: a611 heat gen total | 52\|6 | little-endian | unsigned | 500 | 0 | W | 0 to 31500 |  | plausible |
| `VCFRONT_a611_radCoolantToAirUAEst` | page 611 | Front body controller: a611 rad coolant to air UA est | 58\|6 | little-endian | unsigned | 20 | 0 | W/degC | 0 to 1260 |  | plausible |
| `VCFRONT_a612_DI_gear` | page 612 | Front body controller: a612 DI gear; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCFRONT_a612_manualDrivingProhibited` | page 612 | Front body controller: a612 manual driving prohibited | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a612_vehicleSpeed` | page 612 | Front body controller: a612 vehicle speed | 20\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT_a612_lvHealthStatus` | page 612 | Front body controller: a612 lv health status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DOMAIN_HEALTHY`<br>1 = `BACKUP_COMPROMISED`<br>2 = `ENERGY_RESERVE_CRITICAL`<br>3 = `POWER_SUPPLY_COMPROMISED` | plausible |
| `VCFRONT_a620_powertrainIsDryRunDetected` | page 620 | Front body controller: a620 powertrain is dry run detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a620_powertrainPumpRpm` | page 620 | Front body controller: a620 powertrain pump rpm; raw 255 = signal not available (SNA) | 17\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7620 | 255 = `SNA` | plausible |
| `VCFRONT_a620_powertrainPumpIPhaseFiltered` | page 620 | Front body controller: a620 powertrain pump i phase filtered; raw 255 = signal not available (SNA) | 25\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `VCFRONT_a620_powertrainPumpIPhaseMinFilt` | page 620 | Front body controller: a620 powertrain pump i phase min filt; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 0.1 | 0 | A | 0 to 12.6 | 127 = `SNA` | plausible |
| `VCFRONT_a620_chillerIsDryRunDetected` | page 620 | Front body controller: a620 chiller is dry run detected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a620_chillerPumpRpm` | page 620 | Front body controller: a620 chiller pump rpm; raw 255 = signal not available (SNA) | 41\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7620 | 255 = `SNA` | plausible |
| `VCFRONT_a620_chillerPumpIPhaseFiltered` | page 620 | Front body controller: a620 chiller pump i phase filtered; raw 255 = signal not available (SNA) | 49\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `VCFRONT_a620_chillerPumpIPhaseMinFilt` | page 620 | Front body controller: a620 chiller pump i phase min filt; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 0.1 | 0 | A | 0 to 12.6 | 127 = `SNA` | plausible |
| `VCFRONT_a622_pumpChLowCoolantFlow` | page 622 | Front body controller: a622 pump ch low coolant flow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a622_pumpPtLowCoolantFlow` | page 622 | Front body controller: a622 pump pt low coolant flow | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a622_coolantMode` | page 622 | Front body controller: a622 coolant mode | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | plausible |
| `VCFRONT_a622_isRadiatorBypassed` | page 622 | Front body controller: a622 is radiator bypassed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_DI_gear` | page 623 | Front body controller: a623 DI gear; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `VCFRONT_a623_manualDrivingProhibited` | page 623 | Front body controller: a623 manual driving prohibited | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_vehicleSpeed` | page 623 | Front body controller: a623 vehicle speed | 20\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `VCFRONT_a623_lvHealthStatus` | page 623 | Front body controller: a623 lv health status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DOMAIN_HEALTHY`<br>1 = `BACKUP_COMPROMISED`<br>2 = `ENERGY_RESERVE_CRITICAL`<br>3 = `POWER_SUPPLY_COMPROMISED` | plausible |
| `VCFRONT_a623_unhealthyReason` | page 623 | Front body controller: a623 unhealthy reason | 34\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `LV_BATTERY_CAPABILITY_LOW_ACCURACY`<br>2 = `LV_BATTERY_POWER_ACTIVE_DECEL`<br>3 = `PCS_OPEN_CIRCUIT`<br>4 = `PCS_MIA`<br>5 = `PCS_NOT_ACTIVE`<br>6 = `PCS_EFUSE_OFF`<br>7 = `LV_BATTERY_ELECTRICAL_CONNECTION_UNKNOWN`<br>8 = `LV_BATTERY_ELECTRICAL_CONNECTION`<br>9 = `LV_BATTERY_SENSOR_IBS_MIA`<br>10 = `LV_BATTERY_COMMS`<br>11 = `LVBMB_EFUSE_OPEN`<br>12 = `REVERSE_BATTERY_EFUSE_OFF`<br>13 = `LV_BATTERY_ENERGY_CRITICAL_PULLOVER`<br>14 = `LV_BATTERY_ENERGY_ACTIVE_DECEL`<br>15 = `LV_BATTERY_CONFIGURATION`<br>16 = `LV_BATTERY_IMPEDANCE` | plausible |
| `VCFRONT_a623_failureLvBatteryEnergyActiveDecel` | page 623 | Front body controller: a623 failure lv battery energy active decel | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryEnergyCritical` | page 623 | Front body controller: a623 failure lv battery energy critical | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureReverseBatteryEfuseOff` | page 623 | Front body controller: a623 failure reverse battery efuse off | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvbmbEfuseOpen` | page 623 | Front body controller: a623 failure lvbmb efuse open | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryComms` | page 623 | Front body controller: a623 failure lv battery comms | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatterySensorIbsMia` | page 623 | Front body controller: a623 failure lv battery sensor ibs mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryConnection` | page 623 | Front body controller: a623 failure lv battery connection | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryConnectionUnknown` | page 623 | Front body controller: a623 failure lv battery connection unknown | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failurePcsEfuseOff` | page 623 | Front body controller: a623 failure pcs efuse off | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failurePcsNotActive` | page 623 | Front body controller: a623 failure pcs not active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failurePcsMia` | page 623 | Front body controller: a623 failure pcs mia | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failurePcsOpenCircuit` | page 623 | Front body controller: a623 failure pcs open circuit | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryPowerActiveDecel` | page 623 | Front body controller: a623 failure lv battery power active decel | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryCapabilityLowAccuracy` | page 623 | Front body controller: a623 failure lv battery capability low accuracy | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryConfiguration` | page 623 | Front body controller: a623 failure lv battery configuration | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_failureLvBatteryHighImpedance` | page 623 | Front body controller: a623 failure lv battery high impedance | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_factoryMode` | page 623 | Front body controller: a623 factory mode | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a623_serviceMode` | page 623 | Signal reported by Front body controller | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a624_HighBeam_OV` | page 624 | Front body controller: a624 high beam OV | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_HighBeam_UV` | page 624 | Front body controller: a624 high beam UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_HighBeam_short` | page 624 | Front body controller: a624 high beam short | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_HighBeam_compov` | page 624 | Front body controller: a624 high beam compov | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_HighBeam_bootuv` | page 624 | Front body controller: a624 high beam bootuv | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_HighBeam_binStatus` | page 624 | Front body controller: a624 high beam bin status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_OV` | page 624 | Front body controller: a624 low beam OV | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_UV` | page 624 | Front body controller: a624 low beam UV | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_short` | page 624 | Front body controller: a624 low beam short | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_compov` | page 624 | Front body controller: a624 low beam compov | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_bootuv` | page 624 | Front body controller: a624 low beam bootuv | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_LowBeam_binStatus` | page 624 | Front body controller: a624 low beam bin status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_OV` | page 624 | Front body controller: a624 DRL OV | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_UV` | page 624 | Front body controller: a624 DRL UV | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_short` | page 624 | Front body controller: a624 DRL short | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_compov` | page 624 | Front body controller: a624 DRL compov | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_bootuv` | page 624 | Front body controller: a624 DRL bootuv | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_DRL_binStatus` | page 624 | Front body controller: a624 DRL bin status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_OV` | page 624 | Front body controller: a624 turn signal OV | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_UV` | page 624 | Front body controller: a624 turn signal UV | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_short` | page 624 | Front body controller: a624 turn signal short | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_compov` | page 624 | Front body controller: a624 turn signal compov | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_bootuv` | page 624 | Front body controller: a624 turn signal bootuv | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_TurnSignal_binStatus` | page 624 | Front body controller: a624 turn signal bin status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_OV` | page 624 | Front body controller: a624 side marker OV | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_UV` | page 624 | Front body controller: a624 side marker UV | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_short` | page 624 | Front body controller: a624 side marker short | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_compov` | page 624 | Front body controller: a624 side marker compov | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_bootuv` | page 624 | Front body controller: a624 side marker bootuv | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_SideMarker_binStatus` | page 624 | Front body controller: a624 side marker bin status | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_boost_OV` | page 624 | Front body controller: a624 boost OV | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_boost_BOOTUV` | page 624 | Front body controller: a624 boost BOOTUV | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_boost_ILIM` | page 624 | Front body controller: a624 boost ILIM | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_boost_ISPUV` | page 624 | Front body controller: a624 boost ISPUV | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_EEPROM_status` | page 624 | Front body controller: a624 EEPROM status | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a624_EEPROM_region` | page 624 | Front body controller: a624 EEPROM region; raw 0 = signal not available (SNA) | 51\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `SAE_LEFT`<br>2 = `SAE_RIGHT`<br>3 = `ECE_LHD_LEFT`<br>4 = `ECE_LHD_RIGHT`<br>5 = `ECE_RHD_LEFT`<br>6 = `ECE_RHD_RIGHT` | plausible |
| `VCFRONT_a625_HighBeam_OV` | page 625 | Front body controller: a625 high beam OV | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_HighBeam_UV` | page 625 | Front body controller: a625 high beam UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_HighBeam_short` | page 625 | Front body controller: a625 high beam short | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_HighBeam_compov` | page 625 | Front body controller: a625 high beam compov | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_HighBeam_bootuv` | page 625 | Front body controller: a625 high beam bootuv | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_HighBeam_binStatus` | page 625 | Front body controller: a625 high beam bin status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_OV` | page 625 | Front body controller: a625 low beam OV | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_UV` | page 625 | Front body controller: a625 low beam UV | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_short` | page 625 | Front body controller: a625 low beam short | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_compov` | page 625 | Front body controller: a625 low beam compov | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_bootuv` | page 625 | Front body controller: a625 low beam bootuv | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_LowBeam_binStatus` | page 625 | Front body controller: a625 low beam bin status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_OV` | page 625 | Front body controller: a625 DRL OV | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_UV` | page 625 | Front body controller: a625 DRL UV | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_short` | page 625 | Front body controller: a625 DRL short | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_compov` | page 625 | Front body controller: a625 DRL compov | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_bootuv` | page 625 | Front body controller: a625 DRL bootuv | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_DRL_binStatus` | page 625 | Front body controller: a625 DRL bin status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_OV` | page 625 | Front body controller: a625 turn signal OV | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_UV` | page 625 | Front body controller: a625 turn signal UV | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_short` | page 625 | Front body controller: a625 turn signal short | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_compov` | page 625 | Front body controller: a625 turn signal compov | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_bootuv` | page 625 | Front body controller: a625 turn signal bootuv | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_TurnSignal_binStatus` | page 625 | Front body controller: a625 turn signal bin status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_OV` | page 625 | Front body controller: a625 side marker OV | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_UV` | page 625 | Front body controller: a625 side marker UV | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_short` | page 625 | Front body controller: a625 side marker short | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_compov` | page 625 | Front body controller: a625 side marker compov | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_bootuv` | page 625 | Front body controller: a625 side marker bootuv | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_SideMarker_binStatus` | page 625 | Front body controller: a625 side marker bin status | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_boost_OV` | page 625 | Front body controller: a625 boost OV | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_boost_BOOTUV` | page 625 | Front body controller: a625 boost BOOTUV | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_boost_ILIM` | page 625 | Front body controller: a625 boost ILIM | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_boost_ISPUV` | page 625 | Front body controller: a625 boost ISPUV | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_EEPROM_status` | page 625 | Front body controller: a625 EEPROM status | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VCFRONT_a625_EEPROM_region` | page 625 | Front body controller: a625 EEPROM region; raw 0 = signal not available (SNA) | 51\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `SAE_LEFT`<br>2 = `SAE_RIGHT`<br>3 = `ECE_LHD_LEFT`<br>4 = `ECE_LHD_RIGHT`<br>5 = `ECE_RHD_LEFT`<br>6 = `ECE_RHD_RIGHT` | plausible |
| `VCFRONT_a626_dcrMilliOhms` | page 626 | Front body controller: a626 dcr milli ohms | 16\|8 | little-endian | unsigned | 0.2 | 0 | mOhms | 0 to 51 |  | plausible |
| `VCFRONT_a626_elevatedDcrThreshold` | page 626 | Front body controller: a626 elevated dcr threshold | 24\|4 | little-endian | unsigned | 0.5 | 12 | mOhms | 12 to 19.5 |  | plausible |
| `VCFRONT_a626_avgIntervalCurrent` | page 626 | Front body controller: a626 avg interval current | 28\|5 | little-endian | unsigned | 1 | -31 | A | -31 to 0 |  | plausible |
| `VCFRONT_a626_intervalCurrentVariance` | page 626 | Front body controller: a626 interval current variance | 33\|6 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6.3 |  | plausible |
| `VCFRONT_a626_avgPulseCurrent` | page 626 | Front body controller: a626 avg pulse current | 39\|7 | little-endian | unsigned | 1 | -127 | A | -127 to 0 |  | plausible |
| `VCFRONT_a626_pulseCurrentVariance` | page 626 | Front body controller: a626 pulse current variance | 46\|6 | little-endian | unsigned | 0.25 | 0 | A | 0 to 15.75 |  | plausible |
| `VCFRONT_a626_IBSTemperature` | page 626 | Front body controller: a626 IBS temperature | 52\|8 | little-endian | unsigned | 0.5 | -30 | degC | -30 to 97.5 |  | plausible |
| `VCFRONT_a626_testCounter` | page 626 | Front body controller: a626 test counter | 60\|2 | little-endian | unsigned | 1 | 0 | - | 0 to 3 |  | plausible |
| `VCFRONT_a626_testingExpended` | page 626 | Front body controller: a626 testing expended | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a626_opportunisticTest` | page 626 | Front body controller: a626 opportunistic test | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a627_cell1Voltage` | page 627 | Front body controller: a627 cell1 voltage | 16\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a627_cell2Voltage` | page 627 | Front body controller: a627 cell2 voltage | 25\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a627_cell3Voltage` | page 627 | Front body controller: a627 cell3 voltage | 34\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a627_cell4Voltage` | page 627 | Front body controller: a627 cell4 voltage | 43\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `VCFRONT_a627_sumCellVoltage` | page 627 | Front body controller: a627 sum cell voltage | 52\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCFRONT_a627_deepDischargeFlag` | page 627 | Front body controller: a627 deep discharge flag | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a627_serviceMode` | page 627 | Signal reported by Front body controller | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT_a627_frunkOpen` | page 627 | Front body controller: a627 frunk open | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCFRONT_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (2 signals), page 4 (6 signals), page 8 (6 signals), page 10 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (8 signals), page 88 (8 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (2 signals), page 95 (2 signals), page 96 (2 signals), page 98 (12 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (6 signals), page 107 (15 signals), page 108 (11 signals), page 109 (16 signals), page 110 (17 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (21 signals), page 117 (23 signals), page 118 (28 signals), page 119 (6 signals), page 120 (27 signals), page 121 (3 signals), page 122 (5 signals), page 123 (3 signals), page 124 (5 signals), page 125 (3 signals), page 126 (5 signals), page 127 (4 signals), page 128 (4 signals), page 129 (4 signals), page 130 (3 signals), page 131 (3 signals), page 132 (3 signals), page 133 (3 signals), page 134 (4 signals), page 136 (4 signals), page 137 (4 signals), page 138 (4 signals), page 139 (4 signals), page 140 (4 signals), page 141 (4 signals), page 142 (16 signals), page 143 (5 signals), page 144 (5 signals), page 145 (5 signals), page 146 (2 signals), page 147 (2 signals), page 148 (2 signals), page 150 (2 signals), page 151 (2 signals), page 152 (2 signals), page 156 (1 signals), page 157 (1 signals), page 159 (3 signals), page 160 (14 signals), page 161 (19 signals), page 162 (7 signals), page 164 (1 signals), page 165 (1 signals), page 168 (2 signals), page 169 (2 signals), page 170 (2 signals), page 171 (31 signals), page 172 (2 signals), page 173 (2 signals), page 175 (4 signals), page 176 (1 signals), page 177 (1 signals), page 179 (1 signals), page 180 (16 signals), page 181 (1 signals), page 182 (23 signals), page 186 (1 signals), page 187 (5 signals), page 188 (11 signals), page 191 (21 signals), page 192 (22 signals), page 195 (3 signals), page 196 (10 signals), page 198 (3 signals), page 199 (3 signals), page 200 (1 signals), page 201 (1 signals), page 202 (1 signals), page 207 (1 signals), page 210 (3 signals), page 212 (1 signals), page 213 (3 signals), page 214 (33 signals), page 216 (10 signals), page 217 (33 signals), page 219 (3 signals), page 220 (4 signals), page 221 (6 signals), page 222 (6 signals), page 223 (1 signals), page 227 (33 signals), page 231 (1 signals), page 233 (1 signals), page 234 (1 signals), page 235 (1 signals), page 236 (1 signals), page 242 (5 signals), page 243 (3 signals), page 244 (3 signals), page 245 (3 signals), page 246 (3 signals), page 247 (1 signals), page 248 (4 signals), page 249 (2 signals), page 250 (8 signals), page 253 (9 signals), page 254 (2 signals), page 255 (2 signals), page 257 (12 signals), page 259 (5 signals), page 260 (17 signals), page 261 (2 signals), page 262 (2 signals), page 263 (2 signals), page 264 (2 signals), page 265 (2 signals), page 266 (2 signals), page 267 (2 signals), page 268 (2 signals), page 269 (5 signals), page 270 (4 signals), page 271 (7 signals), page 279 (4 signals), page 280 (4 signals), page 283 (6 signals), page 284 (16 signals), page 285 (16 signals), page 286 (16 signals), page 287 (16 signals), page 288 (16 signals), page 289 (16 signals), page 290 (6 signals), page 291 (6 signals), page 292 (6 signals), page 293 (6 signals), page 294 (6 signals), page 295 (6 signals), page 297 (2 signals), page 300 (2 signals), page 302 (1 signals), page 303 (3 signals), page 304 (2 signals), page 305 (3 signals), page 306 (3 signals), page 307 (3 signals), page 308 (3 signals), page 309 (3 signals), page 334 (4 signals), page 335 (4 signals), page 336 (4 signals), page 337 (4 signals), page 338 (4 signals), page 339 (4 signals), page 340 (4 signals), page 341 (4 signals), page 342 (4 signals), page 343 (4 signals), page 344 (4 signals), page 345 (4 signals), page 346 (4 signals), page 347 (4 signals), page 348 (4 signals), page 349 (4 signals), page 350 (1 signals), page 353 (3 signals), page 354 (3 signals), page 355 (4 signals), page 356 (5 signals), page 357 (1 signals), page 358 (1 signals), page 359 (12 signals), page 360 (2 signals), page 367 (1 signals), page 368 (13 signals), page 369 (4 signals), page 370 (6 signals), page 371 (7 signals), page 372 (2 signals), page 373 (3 signals), page 374 (1 signals), page 377 (2 signals), page 378 (7 signals), page 387 (5 signals), page 388 (5 signals), page 389 (6 signals), page 391 (7 signals), page 392 (2 signals), page 397 (5 signals), page 401 (4 signals), page 402 (9 signals), page 404 (3 signals), page 407 (10 signals), page 409 (1 signals), page 414 (6 signals), page 415 (14 signals), page 416 (5 signals), page 417 (5 signals), page 418 (5 signals), page 419 (5 signals), page 423 (5 signals), page 424 (5 signals), page 431 (3 signals), page 432 (2 signals), page 433 (5 signals), page 434 (5 signals), page 436 (3 signals), page 437 (2 signals), page 438 (2 signals), page 439 (2 signals), page 441 (2 signals), page 444 (22 signals), page 446 (46 signals), page 447 (18 signals), page 459 (2 signals), page 462 (25 signals), page 463 (7 signals), page 464 (4 signals), page 465 (6 signals), page 466 (4 signals), page 467 (1 signals), page 470 (2 signals), page 474 (22 signals), page 475 (22 signals), page 476 (19 signals), page 477 (8 signals), page 478 (23 signals), page 479 (8 signals), page 480 (25 signals), page 486 (1 signals), page 490 (1 signals), page 493 (6 signals), page 495 (11 signals), page 496 (8 signals), page 497 (6 signals), page 500 (2 signals), page 503 (5 signals), page 509 (5 signals), page 510 (5 signals), page 511 (9 signals), page 512 (8 signals), page 513 (7 signals), page 514 (9 signals), page 515 (9 signals), page 516 (6 signals), page 517 (2 signals), page 518 (8 signals), page 519 (20 signals), page 520 (20 signals), page 521 (5 signals), page 522 (6 signals), page 523 (6 signals), page 525 (6 signals), page 527 (6 signals), page 528 (5 signals), page 531 (1 signals), page 532 (1 signals), page 533 (1 signals), page 541 (5 signals), page 544 (3 signals), page 545 (5 signals), page 547 (2 signals), page 548 (20 signals), page 549 (13 signals), page 551 (1 signals), page 552 (3 signals), page 553 (1 signals), page 555 (4 signals), page 557 (14 signals), page 559 (20 signals), page 560 (7 signals), page 561 (10 signals), page 562 (10 signals), page 579 (3 signals), page 580 (3 signals), page 582 (7 signals), page 585 (9 signals), page 592 (5 signals), page 593 (4 signals), page 596 (5 signals), page 597 (4 signals), page 598 (1 signals), page 599 (6 signals), page 605 (3 signals), page 610 (4 signals), page 611 (8 signals), page 612 (4 signals), page 620 (8 signals), page 622 (4 signals), page 623 (23 signals), page 624 (36 signals), page 625 (36 signals), page 626 (10 signals), page 627 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
