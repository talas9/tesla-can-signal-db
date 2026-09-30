---
layout: default
title: "VCLEFT_alertLog (0x55D) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: alert log. Tesla Model 3 / Model Y CAN bus message VCLEFT_alertLog (0x55D) of Left body controller, firmware 2026.26.6.5, 1427 signals (VCLEFT_alertID, VCLEFT_alertState, VCLEFT_a001_InternalWatchdog, VCLEFT_a010_UnderVoltageDetected and 1423 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_alertLog (0x55D) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left body controller message: alert log; frame length observed on a vehicle bus. This page documents the 1427 signals of VCLEFT_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_alertLog` |
| CAN id | 0x55D (1373) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1427 |

## Signals of VCLEFT_alertLog

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_alertID` | selector | Left body controller: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>10 = `a010_ExtSupplyVoltError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>65 = `a065_emiosIsrRateLimitedDbg`<br>66 = `a066_emiosIsrShortPeriodDetectedDbg`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_ETC_MIA`<br>122 = `a122_ICR_MIA`<br>123 = `a123_AID_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_RCU_MIA`<br>129 = `a129_blowerICLatchFault`<br>130 = `a130_blowerICWarning`<br>131 = `a131_blowerICTransFault`<br>132 = `a132_blowerSoftStall`<br>133 = `a133_blowerLowRPMCBang`<br>134 = `a134_SteerColUpDownUnCal`<br>135 = `a135_SteerColInOutUnCal`<br>136 = `a136_brakeSwitchMismatch`<br>137 = `a137_VCSECPowerCycled`<br>138 = `a138_consoleDoorAssist`<br>139 = `a139_BLERearPowerCycled`<br>140 = `a140_BLELeftPowerCycled`<br>141 = `a141_12VAuxPowerTrip`<br>143 = `a143_mirrorManuallyFolded`<br>145 = `a145_brakeSwitchStuck`<br>148 = `a148_brakePressInputMismatch`<br>150 = `a150_windowPinchFront`<br>151 = `a151_windowPinchRear`<br>152 = `a152_windowUncalFront`<br>153 = `a153_windowUncalRear`<br>154 = `a154_windowThermalFront`<br>155 = `a155_windowThermalRear`<br>156 = `a156_windowNoInputFront`<br>157 = `a157_windowNoInputRear`<br>158 = `a158_windowPinchOverideF`<br>159 = `a159_windowPinchOverideR`<br>160 = `a160_windowUndercurrentF`<br>161 = `a161_windowUndercurrentR`<br>162 = `a162_windowEncoderStallF`<br>163 = `a163_windowEncoderStallR`<br>164 = `a164_windowFactoryTest`<br>165 = `a165_windowFactoryTest2`<br>166 = `a166_windowDebug`<br>167 = `a167_windowDebugPinchF`<br>168 = `a168_windowDebugPinchR`<br>169 = `a169_windowCurrentPeakF`<br>170 = `a170_windowCurrentPeakR`<br>172 = `a172_SPI_MIA`<br>173 = `a173_windowBtnDoorOpen`<br>175 = `a175_windowSealDefectFront`<br>176 = `a176_windowSealDefectRear`<br>180 = `a180_frontDoorLatchRehome`<br>181 = `a181_rearDoorLatchRehome`<br>182 = `a182_emergencyLatchRel`<br>183 = `a183_doorStateFactoryTest`<br>185 = `a185_summonAborted`<br>186 = `a186_latchReleaseFailedF`<br>187 = `a187_latchReleaseFailedR`<br>188 = `a188_latchUnableToRearmF`<br>189 = `a189_latchUnableToRearmR`<br>190 = `a190_eFuseMgmtVbatFused`<br>191 = `a191_TLCOvercurrent`<br>192 = `a192_blowerGeneralFault`<br>193 = `a193_blowerMIA`<br>194 = `a194_blowerUnidentified`<br>195 = `a195_blowerIdentificationFailed`<br>196 = `a196_VEHCANOverterminate`<br>197 = `a197_VEHCANUndertrminate`<br>200 = `a200_motorPhantomEncoder`<br>201 = `a201_motorDutyEncDisabl`<br>202 = `a202_epbmUnderIStatic`<br>203 = `a203_epbmOverIStatic`<br>204 = `a204_epbmUnderIDyn`<br>205 = `a205_epbmOverIDyn`<br>206 = `a206_epbWrongDirection`<br>207 = `a207_epbmEnableWrong`<br>208 = `a208_epbFaulted`<br>209 = `a209_epbStateMisTime`<br>210 = `a210_epbStateTime`<br>211 = `a211_epbmUnderIStaticNew`<br>212 = `a212_epbmOverIStaticNew`<br>213 = `a213_epbmUnderIDynNew`<br>214 = `a214_epbmOverIDynNew`<br>215 = `a215_currentDesyncWarning`<br>216 = `a216_SPI_MIA_debugData1`<br>217 = `a217_SPI_MIA_debugData2`<br>218 = `a218_motorDriverFault`<br>219 = `a219_motorCurrentDropout`<br>220 = `a220_reverseLightFaultUser`<br>221 = `a221_hardwareLoadshedTriggered`<br>223 = `a223_VCBATT1_MIA`<br>224 = `a224_seatEncStallTrack`<br>225 = `a225_seatEncStallBack`<br>226 = `a226_seatEncStallTilt`<br>227 = `a227_seatEncStallLift`<br>228 = `a228_seatEncOverTrack`<br>229 = `a229_seatEncOverBack`<br>230 = `a230_seatEncOverTilt`<br>231 = `a231_seatEncOverLift`<br>232 = `a232_seatCurrUnderTrack`<br>233 = `a233_seatCurrUnderBack`<br>234 = `a234_seatCurrUnderTilt`<br>235 = `a235_seatCurrUnderLift`<br>236 = `a236_lumbarOverPresA`<br>237 = `a237_lumbarOverPresB`<br>238 = `a238_lumbarValveMIA`<br>239 = `a239_seatHeatIFront`<br>240 = `a240_seatHeatShortFront`<br>241 = `a241_seatHeatMIAFront`<br>242 = `a242_seatHeatIRearL`<br>243 = `a243_seatHeatShortRearL`<br>244 = `a244_seatHeatMIARearL`<br>245 = `a245_seatHeatIRearC`<br>246 = `a246_seatHeatShortRearC`<br>247 = `a247_seatHeatMIARearC`<br>248 = `a248_seatHeatIRearR`<br>249 = `a249_seatHeatShortRearR`<br>250 = `a250_seatHeatMIARearR`<br>251 = `a251_seatUncalTrack`<br>252 = `a252_seatUncalBack`<br>253 = `a253_seatUncalTilt`<br>254 = `a254_seatUncalLift`<br>256 = `a256_nxppca9539Fault`<br>257 = `a257_USBMIA`<br>259 = `a259_latchDisarmDelayF`<br>260 = `a260_latchDisarmDelayR`<br>261 = `a261_emergencyLatchRelRear`<br>263 = `a263_seatTrackStallDebug`<br>264 = `a264_seatBackStallDebug`<br>265 = `a265_seatTiltStallDebug`<br>266 = `a266_seatLiftStallDebug`<br>267 = `a267_seatTrackHCEncStlDbg`<br>268 = `a268_seatBackHCEncStlDbg`<br>269 = `a269_seatTiltHCEncStlDbg`<br>270 = `a270_seatLiftHCEncStlDbg`<br>272 = `a272_vhclPwrStateMsmtch`<br>273 = `a273_handleStuckActiveF`<br>274 = `a274_handleStuckActiveR`<br>275 = `a275_leftTurnLightFault`<br>276 = `a276_mirrorDebug`<br>277 = `a277_BLELeftUnderVoltage`<br>278 = `a278_BLERearUnderVoltage`<br>279 = `a279_VCSECUnderVoltage`<br>280 = `a280_latchDidNotDisarmF`<br>281 = `a281_latchDidNotDisarmR`<br>282 = `a282_latchUnexpectedArmF`<br>283 = `a283_latchUnexpectedArmR`<br>284 = `a284_blowerFbkSanity`<br>285 = `a285_blowerChipComms`<br>286 = `a286_windowSpeedInvalidF`<br>287 = `a287_windowSpeedInvalidR`<br>288 = `a288_handlePWMPeriodF`<br>289 = `a289_handlePWMPeriodR`<br>290 = `a290_occupancyFaultedFront`<br>291 = `a291_buckleFaultedFront`<br>292 = `a292_occupancyFaultedRearL`<br>293 = `a293_occupancyFaultedRearC`<br>294 = `a294_occupancyFaultedRearR`<br>295 = `a295_buckleFaultedRearL`<br>296 = `a296_buckleFaultedRearC`<br>297 = `a297_seatBelowMinPumpTmp`<br>299 = `a299_swcMIA`<br>300 = `a300_swcUnderVoltage`<br>301 = `a301_swcOverVoltage`<br>302 = `a302_blowerGeneralFault`<br>303 = `a303_eFuseMgmtWindowLift`<br>304 = `a304_frontIntHandleUnexpectedVoltage`<br>305 = `a305_rearIntHandleUnexpectedVoltage`<br>306 = `a306_handleDisconnectedF`<br>307 = `a307_handleDisconnectedR`<br>308 = `a308_sirenMIA`<br>309 = `a309_brakeSwitchFaulted`<br>310 = `a310_mirrorFoldStall`<br>311 = `a311_leftBrakeLightFault`<br>312 = `a312_leftTailLightFault`<br>313 = `a313_leftFootwellLightFault`<br>314 = `a314_leftMapPocketLightFault`<br>315 = `a315_leftInteriorTrunkLightFault`<br>316 = `a316_mirrorPrematureFoldStall`<br>317 = `a317_epbmLimpModeEnabled`<br>318 = `a318_trailerIncorrectConfig`<br>319 = `a319_brakePressPrimaryInputFaulted`<br>320 = `a320_windowReportCrackedAtTrimClear`<br>321 = `a321_windowRezeroedDebugF`<br>322 = `a322_windowRezeroedDebugR`<br>323 = `a323_mirrorCalibrated`<br>324 = `a324_mirrorHeatFault`<br>325 = `a325_hghtSnsrUnplgdFL`<br>326 = `a326_hghtSnsrUnplgdRL`<br>327 = `a327_hghtSnsrFaultFL`<br>328 = `a328_hghtSnsrFaultRL`<br>329 = `a329_noRideHeightCalib`<br>330 = `a330_shortDropFailedF`<br>331 = `a331_shortDropFailedR`<br>332 = `a332_intrusionSensorMIA`<br>333 = `a333_overheadConsoleMIA`<br>334 = `a334_overheadConsoleInternalFault`<br>335 = `a335_intrusionSensorInternalFault`<br>336 = `a336_windowDropRevThermalF`<br>337 = `a337_windowDropRevThermalR`<br>338 = `a338_trailerLightControllerMIA`<br>339 = `a339_trailerLeftTurnLightNotDetected`<br>340 = `a340_trailerRightTurnLightNotDetected`<br>341 = `a341_trailerLightFault`<br>342 = `a342_trailerLightControllerFault`<br>345 = `a345_chargePortPowerCycling`<br>346 = `a346_eFuseMgmtVbatFused2`<br>347 = `a347_nonContMonitorClearedDBG`<br>348 = `a348_CPSleepOvercurrent`<br>349 = `a349_CPSleepUndervoltage`<br>350 = `a350_ensOutOfRange`<br>351 = `a351_debugLiftgateCurrentSpike`<br>352 = `a352_liftgateClosingLatchEntryFailed`<br>353 = `a353_eFuseMgmtSteeringColumn`<br>354 = `a354_eFuseMgmtLiftGate`<br>355 = `a355_liftgateUnexpectedStop`<br>356 = `a356_liftgateFactoryTest`<br>357 = `a357_liftgateUncalibrated`<br>358 = `a358_debugLiftgateCurrentDropout`<br>359 = `a359_liftgateLatchExitNoPositionChange`<br>360 = `a360_detectedStationaryWhileMoving`<br>361 = `a361_stationaryThresholdsIncorrect`<br>362 = `a362_movingThresholdsIncorrect`<br>363 = `a363_liftgateOpenAngleSetReq`<br>365 = `a365_pitchUnlatchDisabled`<br>366 = `a366_liftgateLatchEntryDBG`<br>370 = `a370_seat2RowPitchUnlatched`<br>371 = `a371_seat2RowTrackUnlatched`<br>372 = `a372_seat2RowBackrestUnlatched`<br>373 = `a373_windowSwOpenReqInDogMode`<br>374 = `a374_trailerLightFaultModelY`<br>375 = `a375_windowPinchOverrideNudge`<br>376 = `a376_seat2RowBridgeCurrentExceeded`<br>380 = `a380_steerColThermalLimited`<br>381 = `a381_pitchEstimation1`<br>382 = `a382_pitchEstimation2`<br>383 = `a383_steerColInOutMotorStallCurrent`<br>384 = `a384_steerColUpDownMotorStallCurrent`<br>385 = `a385_steerColInOutMotorUnderCurrent`<br>386 = `a386_steerColUpDownMotorUnderCurrent`<br>387 = `a387_steerColInOutMotorEncoderStalled`<br>388 = `a388_steerColUpDownMotorEncoderStalled`<br>389 = `a389_steerColInOutEncoderOutOfRange`<br>390 = `a390_steerColUpDownEncoderOutOfRange`<br>391 = `a391_pitchEstimationImplausible`<br>392 = `a392_pitchEstimationGPSImprovedReinit`<br>393 = `a393_pitchEstimationNoGPSFusion`<br>394 = `a394_swsTouchTooNegativeDelta`<br>395 = `a395_swsTouchAdcCheckFail`<br>396 = `a396_swsTouchStuckFault`<br>397 = `a397_swsTouchOutOfRangeFault`<br>398 = `a398_swsTouchNvmFault`<br>399 = `a399_swsTouchNoisyBaselineInitialization`<br>400 = `a400_swsTouchDebouncedProcessingError`<br>401 = `a401_swsForceTestPatternViolation`<br>402 = `a402_swsForceOutOfRange`<br>403 = `a403_swsForceAdcCheckFail`<br>404 = `a404_swsForceI2cError`<br>405 = `a405_swsForceCalibrationFault`<br>406 = `a406_swsForceParametersFault`<br>407 = `a407_swsForceNvmFault`<br>408 = `a408_swsForceTouchSensorFault`<br>409 = `a409_swsScrollWheelPushFault`<br>410 = `a410_swsScrollWheelTiltFault`<br>411 = `a411_swsScrollWheelScrollFault`<br>412 = `a412_leftBrakeTailLightFault`<br>413 = `a413_undervoltageSelfTestFailure`<br>414 = `a414_swsHapticMotorFault`<br>415 = `a415_swsMiscFault`<br>416 = `a416_fohmTouchAdcCheckFail`<br>417 = `a417_fohmTouchOutOfRangeFault`<br>418 = `a418_fohmTouchVarianceFail`<br>419 = `a419_fohmTouchStuck`<br>420 = `a420_fohmTouchSensorsImplausible`<br>421 = `a421_fohmForceOutOfRangeFault`<br>422 = `a422_undervoltageSelfTestStuckOff`<br>423 = `a423_fohmForceI2cError`<br>424 = `a424_fohmAmberLEDFault`<br>425 = `a425_fohmVanityPowerSupplyFault`<br>426 = `a426_seatAbuseMotorWarn`<br>427 = `a427_seatAbuseMotorStop`<br>428 = `a428_seatAbuseBufferWarn`<br>429 = `a429_seatAbuseBufferFull`<br>430 = `a430_fohmRearDomeLightPowerSupplyFault`<br>431 = `a431_fohmVbatFault`<br>432 = `a432_fohmMiscFault`<br>433 = `a433_fohmForceCalibrationInvalid`<br>434 = `a434_swsScrollWheelPushData`<br>435 = `a435_swsNoReasonTouchFault`<br>436 = `a436_swsNoReasonForceFault`<br>437 = `a437_hvacRearLeftVerticalDriverFaulted`<br>438 = `a438_hvacRearLeftLateralDriverFaulted`<br>439 = `a439_hvacRearRightVerticalDriverFaulted`<br>440 = `a440_hvacRearRightLateralDriverFaulted`<br>441 = `a441_prndMIA`<br>442 = `a442_swsLongTouchEvent`<br>444 = `a444_drv8703Fault`<br>445 = `a445_drv8703SpiFaultDBG`<br>446 = `a446_trailerAuxReversePower`<br>447 = `a447_steeringColInOutEndstopCal`<br>448 = `a448_steeringColUpDownEndstopCal`<br>449 = `a449_steerColInOutMotorShadowAlgoResetOffset`<br>450 = `a450_steerColUpDownMotorShadowAlgoResetOffset`<br>451 = `a451_wirelessChargerMIA`<br>453 = `a453_liftgatePinchDetected`<br>454 = `a454_wirelessChargerFault`<br>455 = `a455_liftgateUnexpectedShutfaceSwPressed`<br>460 = `a460_etcDebug`<br>466 = `a466_hvac2RLeftAirwaveVerticalFault`<br>467 = `a467_hvac2RLeftAirwaveVerticalWarning`<br>468 = `a468_hvac2RLeftAirwaveVerticalUncalib`<br>469 = `a469_hvac2RLeftAirwaveLateralFault`<br>470 = `a470_hvac2RLeftAirwaveLateralWarning`<br>471 = `a471_hvac2RLeftAirwaveLateralUncalib`<br>472 = `a472_hvac2RRightAirwaveVerticalFault`<br>473 = `a473_hvac2RRightAirwaveVerticalWarning`<br>474 = `a474_hvac2RRightAirwaveVerticalUncalib`<br>475 = `a475_hvac2RRightAirwaveLateralFault`<br>476 = `a476_hvac2RRightAirwaveLateralWarning`<br>477 = `a477_hvac2RRightAirwaveLateralUncalib`<br>478 = `a478_BPillarCameraHeaterFault`<br>480 = `a480_vnf1048Fault`<br>481 = `a481_vnf1048SelfTestFailure`<br>482 = `a482_NCV77XXFault`<br>483 = `a483_leftTurnLightFaultUser`<br>484 = `a484_leftBrakeLightFaultUser`<br>485 = `a485_uvSelfTestLoadUnattemptedOnDbg`<br>488 = `a488_undervoltageSelfTestStuckOnDebug`<br>489 = `a489_undervoltageSelfTestStuckOn`<br>490 = `a490_vehicleOccupiedOnOTAStart`<br>493 = `a493_12vSocketFrontEFuseTrip`<br>494 = `a494_12vSocketRearEFuseTrip`<br>497 = `a497_CANMsgMACVerificationKeyNotProvisioned`<br>498 = `a498_CANMsgMACVerificationFailure`<br>499 = `a499_epbmInvalidateCdp`<br>500 = `a500_eFuseASICStateMismatch`<br>501 = `a501_vnf1048ConfigurationMismatch`<br>510 = `a510_3RowSeatUncalibrated`<br>511 = `a511_3RowSeatPositionNonsensical`<br>512 = `a512_3RowSeatAbsPosOffsetApplied`<br>513 = `a513_3RowSeatObstacleDetected`<br>514 = `a514_3RowSeatTempHigh`<br>515 = `a515_3RowSeatAbsPosSensorTransitionDbg`<br>516 = `a516_3RowSeatStatsFromLastStateDbg`<br>517 = `a517_3RowSeatRequestWhileUncalibrated`<br>518 = `a518_3RowSeatClashAvoidanceBlocked`<br>519 = `a519_3RowSeatOverfolded`<br>520 = `a520_configMismatch`<br>521 = `a521_seatHeatPadUnexpectedVoltage`<br>522 = `a522_trailerLightUnexpectedVoltage`<br>523 = `a523_eFuseThresholdsIncorrect`<br>525 = `a525_LVBatterySWMisconfiguration`<br>526 = `a526_pcbaOverTemperature`<br>527 = `a527_continuousFeedUnexpectedVoltage`<br>528 = `a528_unableToRunStuckOnTest`<br>536 = `a536_trunkFoldFlatSwitchFault`<br>545 = `a545_LVBatteryTypeUnknown`<br>546 = `a546_mirrorFoldTypeChanged`<br>550 = `a550_ambientTempDelta`<br>551 = `a551_interiorDoorRequestInhibited`<br>554 = `a554_RCM2_MIA`<br>555 = `a555_steeringWheelHeaterCompromised`<br>560 = `a560_2RowSeatUncalibrated`<br>561 = `a561_2RowSeatPositionNonsensical`<br>562 = `a562_2RowSeatAbsPosOffsetApplied`<br>563 = `a563_2RowSeatObstacleDetected`<br>564 = `a564_2RowSeatTempHigh`<br>565 = `a565_2RowSeatAbsPosSensorTransitionDbg`<br>566 = `a566_2RowSeatStatsFromLastStateDbg`<br>567 = `a567_2RowSeatRequestWhileUncalibrated`<br>568 = `a568_2RowSeatClashAvoidanceBlocked`<br>569 = `a569_2RowSeatOverfolded`<br>570 = `a570_seatHeatDisabledF`<br>571 = `a571_seatHeatDisabledRearL`<br>572 = `a572_seatHeatDisabledRearC`<br>573 = `a573_seatHeatDisabledRearR`<br>574 = `a574_2RowSeatStatsFromLastStateDbg2`<br>575 = `a575_3RowSeatStatsFromLastStateDbg2`<br>576 = `a576_liftgateStrutPositionMismatch`<br>577 = `a577_bsiHardwareIssue`<br>578 = `a578_RGBLightFault`<br>579 = `a579_leftSteeringWheelCtrlTypeMismatch`<br>580 = `a580_rightSteeringWheelCtrlTypeMismatch`<br>581 = `a581_reverseLightFault`<br>582 = `a582_seat2RControllerTrip`<br>583 = `a583_doorRemoteUnlatchedFront`<br>584 = `a584_doorRemoteUnlatchedRear`<br>585 = `a585_doorRemoteUnlatchFailedFront`<br>586 = `a586_doorRemoteUnlatchFailedRear`<br>587 = `a587_VCSEAT2L_MIA`<br>589 = `a589_lipcCanFault`<br>590 = `a590_seatEncStallThighSupport`<br>591 = `a591_seatCurrUnderThighSupport`<br>592 = `a592_seatUncalThighSupport`<br>593 = `a593_seatEncOverThighSupport`<br>594 = `a594_seatThighSupportStallDebug`<br>595 = `a595_seatThighSupportHCEncStlDbg`<br>596 = `a596_frontDoorLatchUnexpectedVoltage`<br>597 = `a597_rearDoorLatchUnexpectedVoltage`<br>599 = `a599_LVBatteryTypeUnsupported`<br>601 = `a601_wakeToOpenDoorDbg`<br>605 = `a605_CANMsgMACVerificationKeyMismatch`<br>617 = `a617_APP_MIA` | plausible |
| `VCLEFT_alertState` |  | Left body controller: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCLEFT_a001_InternalWatchdog` | page 1 | Left body controller: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a010_UnderVoltageDetected` | page 10 | Left body controller: a010 under voltage detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a010_UnderVoltageTimeout` | page 10 | Left body controller: a010 under voltage timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a015_NVMMMemOverflow` | page 15 | Left body controller: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a015_NVMMFilesystemError` | page 15 | Left body controller: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a015_NVMMRecordIDError` | page 15 | Left body controller: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a057_VEH_cpControl` | page 57 | Left body controller: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a059_voltageDrop` | page 59 | Left body controller: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCLEFT_a059_resistanceEstimate` | page 59 | Left body controller: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCLEFT_a059_current` | page 59 | Left body controller: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCLEFT_a063_switchChannel` | page 63 | Left body controller: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a063_switchType` | page 63 | Left body controller: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a063_ADCVoltage` | page 63 | Left body controller: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCLEFT_a063_disconnected` | page 63 | Left body controller: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a063_indeterminate` | page 63 | Left body controller: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a063_stuckActive` | page 63 | Left body controller: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a063_faulted` | page 63 | Left body controller: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a082_RIPC_epbPrivateState` | page 82 | Left body controller: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a082_RIPC_remoteHSD` | page 82 | Left body controller: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a082_RIPC_railStatus` | page 82 | Left body controller: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a082_RIPC_remoteMux` | page 82 | Left body controller: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a083_LIPC_epbPrivateState` | page 83 | Left body controller: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a083_LIPC_remoteHSD` | page 83 | Left body controller: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a083_LIPC_railStatus` | page 83 | Left body controller: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a083_LIPC_HSDFaults` | page 83 | Left body controller: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a084_CH_StatusC` | page 84 | Left body controller: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a085_PARTY_buttonStatus` | page 85 | Left body controller: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_LVBMS_statusHigh` | page 86 | Left body controller: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_LVBMS_statusLow` | page 86 | Left body controller: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_status` | page 86 | Left body controller: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_12VBatteryStatus` | page 86 | Left body controller: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_LVPowerState` | page 86 | Left body controller: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_lightStatus` | page 86 | Left body controller: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_systemStatus` | page 86 | Left body controller: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_thermalStatus` | page 86 | Left body controller: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_vehNm` | page 86 | Left body controller: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_BDY_LVSelfTests` | page 86 | Left body controller: a086 BDY LV self tests | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_LVSelfTests` | page 86 | Left body controller: a086 VEH LV self tests | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_VEH_LVHealth` | page 86 | Left body controller: a086 VEH LV health | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a086_BDY_12VBatteryStatus` | page 86 | Left body controller: a086 BDY 12 v battery status | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_VEH_temperature` | page 87 | Left body controller: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_VEH_thermalControl` | page 87 | Left body controller: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_VEH_torque` | page 87 | Left body controller: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_VEH_status` | page 87 | Left body controller: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_PARTY_torque` | page 87 | Left body controller: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_PARTY_status` | page 87 | Left body controller: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_PARTY_temperature` | page 87 | Left body controller: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_PARTY_thermalControl` | page 87 | Left body controller: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a087_VEH_motorStatus` | page 87 | Left body controller: a087 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_VEH_temperature` | page 88 | Left body controller: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_VEH_thermalControl` | page 88 | Left body controller: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_VEH_torque` | page 88 | Left body controller: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_VEH_status` | page 88 | Left body controller: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_PARTY_torque` | page 88 | Left body controller: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_PARTY_status` | page 88 | Left body controller: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_PARTY_temperature` | page 88 | Left body controller: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_PARTY_thermalControl` | page 88 | Left body controller: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a088_VEH_motorStatus` | page 88 | Left body controller: a088 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_PARTY_party1` | page 89 | Left body controller: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_PARTY_status` | page 89 | Left body controller: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_VEH_status` | page 89 | Left body controller: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_BDY_party1` | page 89 | Left body controller: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_BDY_status` | page 89 | Left body controller: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_CH_status` | page 89 | Left body controller: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_CH_party1` | page 89 | Left body controller: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_CH_party3` | page 89 | Left body controller: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_VEH_party1` | page 89 | Left body controller: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a089_VEH_party3` | page 89 | Left body controller: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a091_VEH_faultsAndExtras` | page 91 | Left body controller: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a091_VEH_info` | page 91 | Left body controller: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a091_VEH_state` | page 91 | Left body controller: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a092_VEH_restraintStatus` | page 92 | Left body controller: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a092_VEH_switchStatus` | page 92 | Left body controller: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a092_VEH_seatStatus2` | page 92 | Left body controller: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a092_VEH_vehNm` | page 92 | Left body controller: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a093_VEH_restraintStatus` | page 93 | Left body controller: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a093_VEH_switchStatus` | page 93 | Left body controller: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a093_VEH_seatStatus2` | page 93 | Left body controller: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a093_VEH_vehNm` | page 93 | Left body controller: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a094_VEH_sysStatus` | page 94 | Left body controller: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a094_PARTY_sysStatus` | page 94 | Left body controller: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a094_CH_sysStatus` | page 94 | Left body controller: a094 CH sys status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a095_PT_ptNm` | page 95 | Left body controller: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a095_PT_status` | page 95 | Left body controller: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a096_VEH_status` | page 96 | Left body controller: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a096_CH_status` | page 96 | Left body controller: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a097_VEH_HVStatus` | page 97 | Left body controller: a097 VEH HV status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a097_VEH_state` | page 97 | Left body controller: a097 VEH state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_CH_torque` | page 98 | Left body controller: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_hvStatus` | page 98 | Left body controller: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_status` | page 98 | Left body controller: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_thermalControl` | page 98 | Left body controller: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_temperature` | page 98 | Left body controller: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_torque` | page 98 | Left body controller: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PARTY_status` | page 98 | Left body controller: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PARTY_temperature` | page 98 | Left body controller: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PARTY_thermalControl` | page 98 | Left body controller: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PARTY_torque` | page 98 | Left body controller: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PT_thermalControl` | page 98 | Left body controller: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PT_temperature` | page 98 | Left body controller: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_PARTY_motorStatus` | page 98 | Left body controller: a098 PARTY motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a098_VEH_motorStatus` | page 98 | Left body controller: a098 VEH motor status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a099_VEH_oocStatus` | page 99 | Left body controller: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a100_VEH` | page 100 | Left body controller: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a100_PARTY` | page 100 | Left body controller: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a100_PT` | page 100 | Left body controller: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a100_CH` | page 100 | Left body controller: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a100_OBD` | page 100 | Left body controller: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a101_VEH_state` | page 101 | Left body controller: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a101_PARTY_locState` | page 101 | Left body controller: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a101_LIPC_externalWatchdogHeartBeat` | page 101 | Left body controller: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a101_VEH_locState` | page 101 | Left body controller: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a101_BDY_locState` | page 101 | Left body controller: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a102_VEH_faultsAndExtras` | page 102 | Left body controller: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a102_VEH_feedbackStatus` | page 102 | Left body controller: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a102_VEH_sensorStatus` | page 102 | Left body controller: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a102_VEH_rods` | page 102 | Left body controller: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_VEH_hvsNm` | page 103 | Left body controller: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_VEH_vehNm` | page 103 | Left body controller: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_VEH_status` | page 103 | Left body controller: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_PT_ptNm` | page 103 | Left body controller: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_PT_status` | page 103 | Left body controller: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a103_VEH_evseStatus` | page 103 | Left body controller: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a105_VEH_states` | page 105 | Left body controller: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a105_VEH_chNm` | page 105 | Left body controller: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a105_VEH_dampingStates` | page 105 | Left body controller: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a106_VEH_dcdcStatus` | page 106 | Left body controller: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a106_VEH_thermalControl` | page 106 | Left body controller: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a106_VEH_dcdcRailStatus` | page 106 | Left body controller: a106 VEH dcdc rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a106_CH_dcdcRailStatus` | page 106 | Left body controller: a106 CH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a106_CH_alertMatrix` | page 106 | Left body controller: a106 CH alert matrix | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_hvsNm` | page 107 | Left body controller: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_vehNm` | page 107 | Left body controller: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_status` | page 107 | Left body controller: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_thermalStatus` | page 107 | Left body controller: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_bmbMinMax` | page 107 | Left body controller: a107 VEH bmb min max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_powerAvailable` | page 107 | Left body controller: a107 VEH power available | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_PT_ptNm` | page 107 | Left body controller: a107 PT pt nm | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_PT_status` | page 107 | Left body controller: a107 PT status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_PT_thermalStatus` | page 107 | Left body controller: a107 PT thermal status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_PT_socStatus` | page 107 | Left body controller: a107 PT soc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_socStatus` | page 107 | Left body controller: a107 VEH soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_packConfig` | page 107 | Left body controller: a107 VEH pack config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_energyStatus` | page 107 | Left body controller: a107 VEH energy status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a107_VEH_chargeInfo` | page 107 | Left body controller: a107 VEH charge info | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_hvStatus` | page 108 | Left body controller: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_temperature` | page 108 | Left body controller: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_thermalControl` | page 108 | Left body controller: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_torque` | page 108 | Left body controller: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_status` | page 108 | Left body controller: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PARTY_torque` | page 108 | Left body controller: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PARTY_status` | page 108 | Left body controller: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PARTY_temperature` | page 108 | Left body controller: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PARTY_thermalControl` | page 108 | Left body controller: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PT_temperature` | page 108 | Left body controller: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PT_thermalControl` | page 108 | Left body controller: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_PARTY_motorStatus` | page 108 | Left body controller: a108 PARTY motor status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_VEH_motorStatus` | page 108 | Left body controller: a108 VEH motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a108_CH_torque` | page 108 | Left body controller: a108 CH torque | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_carState` | page 110 | Left body controller: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_carConfig` | page 110 | Left body controller: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_time` | page 110 | Left body controller: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_updateStatus` | page 110 | Left body controller: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_vehNm` | page 110 | Left body controller: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_mismatchFault` | page 110 | Left body controller: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_vin` | page 110 | Left body controller: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_bmpDebug` | page 110 | Left body controller: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_gearControl` | page 110 | Left body controller: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_VEH_canLogAvailability` | page 110 | Left body controller: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_airbagCutoffStatus` | page 110 | Left body controller: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_carConfig` | page 110 | Left body controller: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_carState` | page 110 | Left body controller: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_vin` | page 110 | Left body controller: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_chNm` | page 110 | Left body controller: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_CH_epochTimeGtw` | page 110 | Left body controller: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a110_PARTY_carConfig` | page 110 | Left body controller: a110 PARTY car config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_VEH_internalStatus` | page 111 | Left body controller: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_VEH_status` | page 111 | Left body controller: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_VEH_vehNm` | page 111 | Left body controller: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_RIPC_LVPowerState` | page 111 | Left body controller: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_RIPC_epbPrivateState` | page 111 | Left body controller: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_RIPC_railStatus` | page 111 | Left body controller: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_RIPC_remoteADC` | page 111 | Left body controller: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_RIPC_switchStatus` | page 111 | Left body controller: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_VEH_LVPowerState` | page 111 | Left body controller: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_VEH_seatStatus` | page 111 | Left body controller: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_PARTY_status` | page 111 | Left body controller: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a111_CH_status` | page 111 | Left body controller: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_VEH_internalStatus` | page 112 | Left body controller: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_VEH_status` | page 112 | Left body controller: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_VEH_vehNm` | page 112 | Left body controller: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_LIPC_LVPowerState` | page 112 | Left body controller: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_LIPC_epbPrivateState` | page 112 | Left body controller: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_LIPC_railStatus` | page 112 | Left body controller: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_LIPC_remoteADC` | page 112 | Left body controller: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_LIPC_switchStatus` | page 112 | Left body controller: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_VEH_LVPowerState` | page 112 | Left body controller: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_PARTY_status` | page 112 | Left body controller: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a112_CH_status` | page 112 | Left body controller: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_status` | page 114 | Left body controller: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_wheelSpeeds` | page 114 | Left body controller: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_VEH_wheelSpeeds` | page 114 | Left body controller: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_CH_wheelSpeeds` | page 114 | Left body controller: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_party3` | page 114 | Left body controller: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_VEH_party3` | page 114 | Left body controller: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_VEH_status` | page 114 | Left body controller: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_wheelRotation` | page 114 | Left body controller: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_CH_wheelRotation` | page 114 | Left body controller: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_VEH_wheelRotation` | page 114 | Left body controller: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_brakeTorque` | page 114 | Left body controller: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_PARTY_offsets` | page 114 | Left body controller: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_BDY_offsets` | page 114 | Left body controller: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_BDY_party3` | page 114 | Left body controller: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_BDY_status` | page 114 | Left body controller: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_BDY_wheelRotation` | page 114 | Left body controller: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_BDY_wheelSpeeds` | page 114 | Left body controller: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_CH_party1` | page 114 | Left body controller: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_CH_party3` | page 114 | Left body controller: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a114_CH_status` | page 114 | Left body controller: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_RSSI` | page 115 | Left body controller: a115 VEH RSSI | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_authenticationWithMac` | page 115 | Left body controller: a115 VEH authentication with mac | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_endpointTemp` | page 115 | Left body controller: a115 VEH endpoint temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_ChildSeatStatus` | page 115 | Left body controller: a115 VEH child seat status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_ChildSeatStatus` | page 115 | Left body controller: a115 BDY child seat status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_vehNm` | page 115 | Left body controller: a115 VEH veh nm | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_authentication` | page 115 | Left body controller: a115 VEH authentication | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_BLEResetRequest` | page 115 | Left body controller: a115 VEH BLE reset request | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_requests` | page 115 | Left body controller: a115 VEH requests | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_VEH_requests2` | page 115 | Left body controller: a115 VEH requests2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_REM_authentication` | page 115 | Left body controller: a115 REM authentication | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_UI_corianderVehicleControl` | page 115 | Left body controller: a115 UI coriander vehicle control | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_CH_TPMSDisplay` | page 115 | Left body controller: a115 CH TPMS display | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_BLEResetRequest` | page 115 | Left body controller: a115 BDY BLE reset request | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_RSSI` | page 115 | Left body controller: a115 BDY RSSI | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_authentication` | page 115 | Left body controller: a115 BDY authentication | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_requests` | page 115 | Left body controller: a115 BDY requests | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_requests2` | page 115 | Left body controller: a115 BDY requests2 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_vehNm` | page 115 | Left body controller: a115 BDY veh nm | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a115_BDY_authenticationWithMac` | page 115 | Left body controller: a115 BDY authentication with mac | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_PARTY_epbmStatus` | page 116 | Left body controller: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_vehNm` | page 116 | Left body controller: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_hvacRequest` | page 116 | Left body controller: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_hvacStatus` | page 116 | Left body controller: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_LVPowerState` | page 116 | Left body controller: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_lightStatus` | page 116 | Left body controller: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_seatStatus` | page 116 | Left body controller: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_thsStatus` | page 116 | Left body controller: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_doorStatus` | page 116 | Left body controller: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_seatHeatStatus` | page 116 | Left body controller: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_restraintStatus` | page 116 | Left body controller: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_switchStatus` | page 116 | Left body controller: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_logging1Hz` | page 116 | Left body controller: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_seatStatus2` | page 116 | Left body controller: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_status` | page 116 | Left body controller: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_thermalCommand` | page 116 | Left body controller: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_windowStatus` | page 116 | Left body controller: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_PARTY_restraintStatus` | page 116 | Left body controller: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_PARTY_doorStatus` | page 116 | Left body controller: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_epbmStatus` | page 116 | Left body controller: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_restraintStatus` | page 116 | Left body controller: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_switchStatus` | page 116 | Left body controller: a116 BDY switch status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_status` | page 116 | Left body controller: a116 BDY status | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_logging1Hz` | page 116 | Left body controller: a116 BDY logging1 hz | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_hvacStatus` | page 116 | Left body controller: a116 BDY hvac status | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_BDY_hvacRequest` | page 116 | Left body controller: a116 BDY hvac request | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_liftgateFollowerResponse` | page 116 | Left body controller: a116 VEH liftgate follower response | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_liftgateFollowerStatus` | page 116 | Left body controller: a116 VEH liftgate follower status | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a116_VEH_hvacStatus2` | page 116 | Left body controller: a116 VEH hvac status2 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_BDY_epbmStatus` | page 117 | Left body controller: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_BDY_restraintStatus` | page 117 | Left body controller: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_prndStatus` | page 117 | Left body controller: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_PARTY_epbmStatus` | page 117 | Left body controller: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_vehNm` | page 117 | Left body controller: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_hvacBlowerFdb` | page 117 | Left body controller: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_LVPowerState` | page 117 | Left body controller: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_restraintStatus` | page 117 | Left body controller: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_lightStatus` | page 117 | Left body controller: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_seatStatus` | page 117 | Left body controller: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_BDY_falconSwitchStatus` | page 117 | Left body controller: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_doorStatus` | page 117 | Left body controller: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_doorStatus2` | page 117 | Left body controller: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_windowStatus` | page 117 | Left body controller: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_switchStatus` | page 117 | Left body controller: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_intrusionSensorStatus` | page 117 | Left body controller: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_liftgateStatus` | page 117 | Left body controller: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_seatStatus2` | page 117 | Left body controller: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_PARTY_restraintStatus` | page 117 | Left body controller: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_thermalStatus` | page 117 | Left body controller: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_PARTY_doorStatus` | page 117 | Left body controller: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_VEH_status` | page 117 | Left body controller: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_PARTY_prndStatus` | page 117 | Left body controller: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a117_PARTY_lightingSecondary` | page 117 | Left body controller: a117 PARTY lighting secondary | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_vehNm` | page 118 | Left body controller: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_lighting` | page 118 | Left body controller: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_sensors` | page 118 | Left body controller: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_status` | page 118 | Left body controller: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_okToUseHighPwr` | page 118 | Left body controller: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_LVPowerState` | page 118 | Left body controller: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_coolant` | page 118 | Left body controller: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_vehicleStatus` | page 118 | Left body controller: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_12VBatteryStatus` | page 118 | Left body controller: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_systemStatus` | page 118 | Left body controller: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_LVPowerState` | page 118 | Left body controller: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_outputPowerStatus` | page 118 | Left body controller: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_vehicleTime` | page 118 | Left body controller: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_thermalCommand` | page 118 | Left body controller: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_LVPowerState` | page 118 | Left body controller: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_sensors` | page 118 | Left body controller: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_sensors` | page 118 | Left body controller: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_interNodeResistance` | page 118 | Left body controller: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_lighting` | page 118 | Left body controller: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_VEH_lightStatus` | page 118 | Left body controller: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_vehNm` | page 118 | Left body controller: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_12VBatteryStatus` | page 118 | Left body controller: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_LVBMS_statusHigh` | page 118 | Left body controller: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_CH_alertMatrix` | page 118 | Left body controller: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_BDY_outputPowerStatus` | page 118 | Left body controller: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_BDY_vehicleTime` | page 118 | Left body controller: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | Left body controller: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | Left body controller: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_PARTY_VCFRONT_cameraCleaningStatus` | page 118 | Left body controller: a118 PARTY VCFRONT camera cleaning status | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a118_BDY_LVHealth` | page 118 | Left body controller: a118 BDY LV health | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_VEH_steerAngle` | page 119 | Left body controller: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_VEH_leftStalk` | page 119 | Left body controller: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_VEH_rightStalk` | page 119 | Left body controller: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_PARTY_rightStalk` | page 119 | Left body controller: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_CH_steerAngle` | page 119 | Left body controller: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a119_PARTY_steerAngle` | page 119 | Left body controller: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_chassisCntl` | page 120 | Left body controller: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_systemStatus` | page 120 | Left body controller: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_CH_chassisCntl` | page 120 | Left body controller: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_systemStatus` | page 120 | Left body controller: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_torque` | page 120 | Left body controller: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_torque` | page 120 | Left body controller: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_locStatus` | page 120 | Left body controller: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_speed` | page 120 | Left body controller: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_speed` | page 120 | Left body controller: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_status` | page 120 | Left body controller: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PT_speed` | page 120 | Left body controller: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PT_systemStatus` | page 120 | Left body controller: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_vehicleEstimates` | page 120 | Left body controller: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_aggregatedAxleSpeed` | page 120 | Left body controller: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_aggregatedAxleSpeed` | page 120 | Left body controller: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_systemPower` | page 120 | Left body controller: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_autonomyHealth` | page 120 | Left body controller: a120 PARTY autonomy health | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_autonomyHealth` | page 120 | Left body controller: a120 VEH autonomy health | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PT_systemPower` | page 120 | Left body controller: a120 PT system power | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_stalklessInterfaces` | page 120 | Left body controller: a120 PARTY stalkless interfaces | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_CH_speed` | page 120 | Left body controller: a120 CH speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_estimatedBrakeTemp` | page 120 | Left body controller: a120 VEH estimated brake temp | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_prndControl` | page 120 | Left body controller: a120 PARTY prnd control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_locStatus2` | page 120 | Left body controller: a120 PARTY loc status2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_chassisCntl` | page 120 | Left body controller: a120 VEH chassis cntl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_CH_locStatus2` | page 120 | Left body controller: a120 CH loc status2 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_locStatus` | page 120 | Left body controller: a120 VEH loc status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_locStatus2` | page 120 | Left body controller: a120 VEH loc status2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_prndControl` | page 120 | Left body controller: a120 VEH prnd control | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_vehicleEstimates` | page 120 | Left body controller: a120 VEH vehicle estimates | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_PARTY_motorStatus` | page 120 | Left body controller: a120 PARTY motor status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_VEH_motorStatus` | page 120 | Left body controller: a120 VEH motor status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a120_BDY_speed` | page 120 | Left body controller: a120 BDY speed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a121_OBD_status` | page 121 | Left body controller: a121 OBD status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a123_OBD_alcoholInterlockRequest` | page 123 | Left body controller: a123 OBD alcohol interlock request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a124_PARTY_status` | page 124 | Left body controller: a124 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a124_BDY_status` | page 124 | Left body controller: a124 BDY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a124_VEH_status` | page 124 | Left body controller: a124 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a125_PARTY_actuation` | page 125 | Left body controller: a125 PARTY actuation | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a125_BDY_actuation` | page 125 | Left body controller: a125 BDY actuation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a125_PARTY_status` | page 125 | Left body controller: a125 PARTY status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a125_BDY_status` | page 125 | Left body controller: a125 BDY status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_overCurrentError` | page 129 | Left body controller: a129 over current error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_fetShortCircuit` | page 129 | Left body controller: a129 fet short circuit | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_lockedRotor` | page 129 | Left body controller: a129 locked rotor | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_HA` | page 129 | Left body controller: a129 VDS HA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_LA` | page 129 | Left body controller: a129 VDS LA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_HB` | page 129 | Left body controller: a129 VDS HB | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_LB` | page 129 | Left body controller: a129 VDS LB | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_HC` | page 129 | Left body controller: a129 VDS HC | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VDS_LC` | page 129 | Left body controller: a129 VDS LC | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_SNS_C_OCP` | page 129 | Left body controller: a129 SNS c OCP | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_SNS_B_OCP` | page 129 | Left body controller: a129 SNS b OCP | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_SNS_A_OCP` | page 129 | Left body controller: a129 SNS a OCP | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_PVDD_UVLO2` | page 129 | Left body controller: a129 PVDD UVLO2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_WD_FAULT` | page 129 | Left body controller: a129 WD FAULT | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_OTSD` | page 129 | Left body controller: a129 OTSD | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VREG_UV` | page 129 | Left body controller: a129 VREG UV | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_AVDD_UVLO` | page 129 | Left body controller: a129 AVDD UVLO | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VCP_LSD_UVLO2` | page 129 | Left body controller: a129 VCP LSD UVLO2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VCPH_UVLO2` | page 129 | Left body controller: a129 VCPH UVLO2 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VCPH_UVLO` | page 129 | Left body controller: a129 VCPH UVLO | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VCPH_OVLO_ABS` | page 129 | Left body controller: a129 VCPH OVLO ABS | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_HA` | page 129 | Left body controller: a129 VGS HA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_LA` | page 129 | Left body controller: a129 VGS LA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_HB` | page 129 | Left body controller: a129 VGS HB | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_LB` | page 129 | Left body controller: a129 VGS LB | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_HC` | page 129 | Left body controller: a129 VGS HC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a129_VGS_LC` | page 129 | Left body controller: a129 VGS LC | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_junctionTempWarning` | page 130 | Left body controller: a130 junction temp warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_junctionOverTemp` | page 130 | Left body controller: a130 junction over temp | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_startUpOperation` | page 130 | Left body controller: a130 start up operation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_lossOfSpeedLock` | page 130 | Left body controller: a130 loss of speed lock | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_vccUnderVoltage` | page 130 | Left body controller: a130 vcc under voltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_TEMP_FLAG4` | page 130 | Left body controller: a130 TEMP FLAG4 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_PVDD_UVFL` | page 130 | Left body controller: a130 PVDD UVFL | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_PVDD_OVFL` | page 130 | Left body controller: a130 PVDD OVFL | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_VDS_STATUS` | page 130 | Left body controller: a130 VDS STATUS | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_VCPH_UVFL` | page 130 | Left body controller: a130 VCPH UVFL | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_TEMP_FLAG1` | page 130 | Left body controller: a130 TEMP FLAG1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_TEMP_FLAG2` | page 130 | Left body controller: a130 TEMP FLAG2 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_TEMP_FLAG3` | page 130 | Left body controller: a130 TEMP FLAG3 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a130_OTW` | page 130 | Left body controller: a130 OTW | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a131_vsUnderVoltage` | page 131 | Left body controller: a131 vs under voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a131_vsOverVoltage` | page 131 | Left body controller: a131 vs over voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a131_chpUnderVoltage` | page 131 | Left body controller: a131 chp under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a131_vglUnderVoltage` | page 131 | Left body controller: a131 vgl under voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a131_thOverTemperature` | page 131 | Left body controller: a131 th over temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a132_RPMActual` | page 132 | Left body controller: a132 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCLEFT_a132_RPMTarget` | page 132 | Left body controller: a132 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCLEFT_a133_RPMActual` | page 133 | Left body controller: a133 RPM actual | 16\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCLEFT_a133_RPMTarget` | page 133 | Left body controller: a133 RPM target | 26\|10 | little-endian | unsigned | 10 | 0 | RPM | 0 to 10230 |  | plausible |
| `VCLEFT_a141_outputCurrent` | page 141 | Left body controller: a141 output current | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `VCLEFT_a145_brakeSwitch` | page 145 | Left body controller: a145 brake switch; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a145_ibstRodPosition` | page 145 | Left body controller: a145 ibst rod position | 18\|12 | little-endian | unsigned | 0.015625 | -5 | mm | -5 to 58.984375 |  | plausible |
| `VCLEFT_a145_ibstRodPositionQF` | page 145 | Left body controller: a145 ibst rod position QF | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_INITIALIZED`<br>1 = `NORMAL`<br>2 = `FAULT` | plausible |
| `VCLEFT_a150_windowPosition` | page 150 | Left body controller: a150 window position | 16\|9 | little-endian | signed | 1.43137252331 | 197.529418945 | mm | -168.901947022 to 562.529412389 |  | plausible |
| `VCLEFT_a150_movementTimeMs` | page 150 | Left body controller: a150 movement time ms | 25\|7 | little-endian | unsigned | 50 | 0 | ms | 0 to 6350 |  | plausible |
| `VCLEFT_a150_windowPinchReason` | page 150 | Left body controller: a150 window pinch reason | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `POWER`<br>2 = `POWER_DIV_SPEED`<br>3 = `POWER_CRUDE`<br>4 = `ACCEL_LOOKBACK`<br>5 = `UNUSED` | plausible |
| `VCLEFT_a150_lookbackIndex` | page 150 | Left body controller: a150 lookback index | 35\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a150_absAccelExceedance` | page 150 | Left body controller: a150 abs accel exceedance | 41\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCLEFT_a150_relAccelExceedance` | page 150 | Left body controller: a150 rel accel exceedance | 49\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCLEFT_a150_speedExpScore` | page 150 | Left body controller: a150 speed exp score | 57\|6 | little-endian | signed | 0.0006451613 | -0.009677419 | - | -0.0303225806 to 0.0103225813 |  | plausible |
| `VCLEFT_a150_treatedInGear` | page 150 | Left body controller: a150 treated in gear | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a151_windowPosition` | page 151 | Left body controller: a151 window position | 16\|9 | little-endian | signed | 1.43137252331 | 197.529418945 | mm | -168.901947022 to 562.529412389 |  | plausible |
| `VCLEFT_a151_movementTimeMs` | page 151 | Left body controller: a151 movement time ms | 25\|7 | little-endian | unsigned | 50 | 0 | ms | 0 to 6350 |  | plausible |
| `VCLEFT_a151_windowPinchReason` | page 151 | Left body controller: a151 window pinch reason | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `POWER`<br>2 = `POWER_DIV_SPEED`<br>3 = `POWER_CRUDE`<br>4 = `ACCEL_LOOKBACK`<br>5 = `UNUSED` | plausible |
| `VCLEFT_a151_lookbackIndex` | page 151 | Left body controller: a151 lookback index | 35\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a151_absAccelExceedance` | page 151 | Left body controller: a151 abs accel exceedance | 41\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCLEFT_a151_relAccelExceedance` | page 151 | Left body controller: a151 rel accel exceedance | 49\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCLEFT_a151_speedExpScore` | page 151 | Left body controller: a151 speed exp score | 57\|6 | little-endian | signed | 0.0006451613 | -0.009677419 | - | -0.0303225806 to 0.0103225813 |  | plausible |
| `VCLEFT_a151_treatedInGear` | page 151 | Left body controller: a151 treated in gear | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a152_zeroed` | page 152 | Left body controller: a152 zeroed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a152_endStopTrusted` | page 152 | Left body controller: a152 end stop trusted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a152_speedTableStatus` | page 152 | Left body controller: a152 speed table status; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `EMPTY_SNA`<br>1 = `SENSITIVE_BUILT`<br>2 = `FULLY_BUILT` | plausible |
| `VCLEFT_a152_causedByBackoffs` | page 152 | Left body controller: a152 caused by backoffs | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a153_zeroed` | page 153 | Left body controller: a153 zeroed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a153_endStopTrusted` | page 153 | Left body controller: a153 end stop trusted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a153_speedTableStatus` | page 153 | Left body controller: a153 speed table status; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `EMPTY_SNA`<br>1 = `SENSITIVE_BUILT`<br>2 = `FULLY_BUILT` | plausible |
| `VCLEFT_a153_causedByBackoffs` | page 153 | Left body controller: a153 caused by backoffs | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a154_windowThermalMode` | page 154 | Left body controller: a154 window thermal mode; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NORMAL`<br>2 = `ALERT`<br>3 = `CRITICAL` | plausible |
| `VCLEFT_a154_lightShowActive` | page 154 | Left body controller: a154 light show active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a155_windowThermalMode` | page 155 | Left body controller: a155 window thermal mode; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NORMAL`<br>2 = `ALERT`<br>3 = `CRITICAL` | plausible |
| `VCLEFT_a155_lightShowActive` | page 155 | Left body controller: a155 light show active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a180_intButtonPressed` | page 180 | Left body controller: a180 int button pressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a180_extHandlePWM` | page 180 | Left body controller: a180 ext handle PWM | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_a180_extHandlePulled` | page 180 | Left body controller: a180 ext handle pulled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a180_releasePWM` | page 180 | Left body controller: a180 release PWM | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_a180_latchStatus` | page 180 | Left body controller: a180 latch status; raw 0 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCLEFT_a180_latchClawStatus` | page 180 | Left body controller: a180 latch claw status | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a181_intButtonPressed` | page 181 | Left body controller: a181 int button pressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a181_extHandlePWM` | page 181 | Left body controller: a181 ext handle PWM | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_a181_extHandlePulled` | page 181 | Left body controller: a181 ext handle pulled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a181_releasePWM` | page 181 | Left body controller: a181 release PWM | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_a181_latchStatus` | page 181 | Left body controller: a181 latch status; raw 0 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCLEFT_a181_latchClawStatus` | page 181 | Left body controller: a181 latch claw status | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a186_voltage` | page 186 | Left body controller: a186 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a186_temperature` | page 186 | Left body controller: a186 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a187_voltage` | page 187 | Left body controller: a187 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a187_temperature` | page 187 | Left body controller: a187 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a188_voltage` | page 188 | Left body controller: a188 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a188_temperature` | page 188 | Left body controller: a188 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a189_voltage` | page 189 | Left body controller: a189 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a189_temperature` | page 189 | Left body controller: a189 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a190_eFuseTripCount` | page 190 | Left body controller: a190 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a192_motorFaulted` | page 192 | Left body controller: a192 motor faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorLocked` | page 192 | Left body controller: a192 motor locked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_ecuReset` | page 192 | Left body controller: a192 ecu reset | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_fetTempIrrational` | page 192 | Left body controller: a192 fet temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorControlError` | page 192 | Left body controller: a192 motor control error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_underVoltage` | page 192 | Left body controller: a192 under voltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_overVoltage` | page 192 | Left body controller: a192 over voltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_hardwareOvercurrent` | page 192 | Left body controller: a192 hardware overcurrent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorOpenPhase` | page 192 | Left body controller: a192 motor open phase | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorSoftOpenPhase` | page 192 | Left body controller: a192 motor soft open phase | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorOvertemp` | page 192 | Left body controller: a192 motor overtemp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_dcOvercurrent` | page 192 | Left body controller: a192 dc overcurrent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorStalled` | page 192 | Left body controller: a192 motor stalled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_selfTestFailed` | page 192 | Left body controller: a192 self test failed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_selfTestResult` | page 192 | Left body controller: a192 self test result | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NOT_TESTED`<br>1 = `SHORT_SUPPLY`<br>2 = `SHORT_GROUND`<br>3 = `OPEN_PHASE_U`<br>4 = `OPEN_PHASE_V`<br>5 = `OPEN_PHASE_W`<br>6 = `UNKNOWN`<br>7 = `PASSED` | plausible |
| `VCLEFT_a192_linChecksumError` | page 192 | Left body controller: a192 lin checksum error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_linFramingError` | page 192 | Left body controller: a192 lin framing error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_phaseShorted` | page 192 | Left body controller: a192 phase shorted | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_busVoltageIrrational` | page 192 | Left body controller: a192 bus voltage irrational | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_dcCurrentIrrational` | page 192 | Left body controller: a192 dc current irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorSpeedIrrational` | page 192 | Left body controller: a192 motor speed irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_supplyVoltageIrrational` | page 192 | Left body controller: a192 supply voltage irrational | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorPhaseCurrentIrrational` | page 192 | Left body controller: a192 motor phase current irrational | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_chipOvertemp` | page 192 | Left body controller: a192 chip overtemp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorSpeedTooHigh` | page 192 | Left body controller: a192 motor speed too high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_phaseOvercurrent` | page 192 | Left body controller: a192 phase overcurrent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_vddaOvercurrent` | page 192 | Left body controller: a192 vdda overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_busVoltageUnhealthy` | page 192 | Left body controller: a192 bus voltage unhealthy | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_hsVdsOvervoltage` | page 192 | Left body controller: a192 hs vds overvoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_hsVdsOvervoltageMask` | page 192 | Left body controller: a192 hs vds overvoltage mask | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCLEFT_a192_lsVdsOvervoltage` | page 192 | Left body controller: a192 ls vds overvoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_lsVdsOvervoltageMask` | page 192 | Left body controller: a192 ls vds overvoltage mask | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCLEFT_a192_payloadBitsNotSet` | page 192 | Left body controller: a192 payload bits not set | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorNotIdentified` | page 192 | Left body controller: a192 motor not identified | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a192_motorType` | page 192 | Left body controller: a192 motor type | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `DELTA`<br>2 = `BOSCH` | plausible |
| `VCLEFT_a194_motorTypeUnknown` | page 194 | Left body controller: a194 motor type unknown | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a194_configurationMismatch` | page 194 | Left body controller: a194 configuration mismatch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a194_vcbldcMotorTypeUnknown` | page 194 | Left body controller: a194 vcbldc motor type unknown | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a194_nvramMotorTypeUnknown` | page 194 | Left body controller: a194 nvram motor type unknown | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a194_vcbldcMotorId` | page 194 | Left body controller: a194 vcbldc motor id | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `DELTA`<br>2 = `BOSCH` | plausible |
| `VCLEFT_a194_nvramMotorId` | page 194 | Left body controller: a194 nvram motor id | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `DELTA`<br>2 = `BOSCH` | plausible |
| `VCLEFT_a196_outputState` | page 196 | Left body controller: a196 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a196_NVRAMState` | page 196 | Left body controller: a196 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a196_lockoutState` | page 196 | Left body controller: a196 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a197_outputState` | page 197 | Left body controller: a197 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a197_NVRAMState` | page 197 | Left body controller: a197 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a197_lockoutState` | page 197 | Left body controller: a197 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_unknownAllowed` | page 202 | Left body controller: a202 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_openAllowed` | page 202 | Left body controller: a202 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_dynamicAllowed` | page 202 | Left body controller: a202 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_parkAllowed` | page 202 | Left body controller: a202 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_startAllowed` | page 202 | Left body controller: a202 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_serviceAllowed` | page 202 | Left body controller: a202 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_winchAllowed` | page 202 | Left body controller: a202 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_winchReleaseAllowed` | page 202 | Left body controller: a202 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_parkingAllowed` | page 202 | Left body controller: a202 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_dynApplyAllowed` | page 202 | Left body controller: a202 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_releaseAllowed` | page 202 | Left body controller: a202 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_parkPendingAllowed` | page 202 | Left body controller: a202 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_wenchPendingAllowed` | page 202 | Left body controller: a202 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a202_desyncCount` | page 202 | Left body controller: a202 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a202_current` | page 202 | Left body controller: a202 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCLEFT_a202_epbConfig` | page 202 | Left body controller: a202 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a203_unknownAllowed` | page 203 | Left body controller: a203 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_openAllowed` | page 203 | Left body controller: a203 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_dynamicAllowed` | page 203 | Left body controller: a203 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_parkAllowed` | page 203 | Left body controller: a203 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_startAllowed` | page 203 | Left body controller: a203 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_serviceAllowed` | page 203 | Left body controller: a203 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_winchAllowed` | page 203 | Left body controller: a203 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_winchReleaseAllowed` | page 203 | Left body controller: a203 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_parkingAllowed` | page 203 | Left body controller: a203 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_dynApplyAllowed` | page 203 | Left body controller: a203 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_releaseAllowed` | page 203 | Left body controller: a203 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_parkPendingAllowed` | page 203 | Left body controller: a203 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_wenchPendingAllowed` | page 203 | Left body controller: a203 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a203_desyncCount` | page 203 | Left body controller: a203 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a203_current` | page 203 | Left body controller: a203 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCLEFT_a203_epbConfig` | page 203 | Left body controller: a203 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a204_unknownAllowed` | page 204 | Left body controller: a204 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_openAllowed` | page 204 | Left body controller: a204 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_dynamicAllowed` | page 204 | Left body controller: a204 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_parkAllowed` | page 204 | Left body controller: a204 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_startAllowed` | page 204 | Left body controller: a204 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_serviceAllowed` | page 204 | Left body controller: a204 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_winchAllowed` | page 204 | Left body controller: a204 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_winchReleaseAllowed` | page 204 | Left body controller: a204 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_parkingAllowed` | page 204 | Left body controller: a204 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_dynApplyAllowed` | page 204 | Left body controller: a204 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_releaseAllowed` | page 204 | Left body controller: a204 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_parkPendingAllowed` | page 204 | Left body controller: a204 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_wenchPendingAllowed` | page 204 | Left body controller: a204 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a204_desyncCount` | page 204 | Left body controller: a204 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a204_current` | page 204 | Left body controller: a204 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCLEFT_a204_epbConfig` | page 204 | Left body controller: a204 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a205_unknownAllowed` | page 205 | Left body controller: a205 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_openAllowed` | page 205 | Left body controller: a205 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_dynamicAllowed` | page 205 | Left body controller: a205 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_parkAllowed` | page 205 | Left body controller: a205 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_startAllowed` | page 205 | Left body controller: a205 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_serviceAllowed` | page 205 | Left body controller: a205 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_winchAllowed` | page 205 | Left body controller: a205 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_winchReleaseAllowed` | page 205 | Left body controller: a205 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_parkingAllowed` | page 205 | Left body controller: a205 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_dynApplyAllowed` | page 205 | Left body controller: a205 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_releaseAllowed` | page 205 | Left body controller: a205 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_parkPendingAllowed` | page 205 | Left body controller: a205 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_wenchPendingAllowed` | page 205 | Left body controller: a205 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a205_desyncCount` | page 205 | Left body controller: a205 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a205_current` | page 205 | Left body controller: a205 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCLEFT_a205_epbConfig` | page 205 | Left body controller: a205 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a206_unknownAllowed` | page 206 | Left body controller: a206 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_openAllowed` | page 206 | Left body controller: a206 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_dynamicAllowed` | page 206 | Left body controller: a206 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_parkAllowed` | page 206 | Left body controller: a206 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_startAllowed` | page 206 | Left body controller: a206 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_serviceAllowed` | page 206 | Left body controller: a206 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_winchAllowed` | page 206 | Left body controller: a206 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_winchReleaseAllowed` | page 206 | Left body controller: a206 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_parkingAllowed` | page 206 | Left body controller: a206 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_dynApplyAllowed` | page 206 | Left body controller: a206 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_releaseAllowed` | page 206 | Left body controller: a206 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_parkPendingAllowed` | page 206 | Left body controller: a206 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_wenchPendingAllowed` | page 206 | Left body controller: a206 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a206_unitStatusEPB` | page 206 | Left body controller: a206 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a206_unitStatusEPBM` | page 206 | Left body controller: a206 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a207_unknownAllowed` | page 207 | Left body controller: a207 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_openAllowed` | page 207 | Left body controller: a207 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_dynamicAllowed` | page 207 | Left body controller: a207 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_parkAllowed` | page 207 | Left body controller: a207 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_startAllowed` | page 207 | Left body controller: a207 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_serviceAllowed` | page 207 | Left body controller: a207 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_winchAllowed` | page 207 | Left body controller: a207 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_winchReleaseAllowed` | page 207 | Left body controller: a207 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_parkingAllowed` | page 207 | Left body controller: a207 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_dynApplyAllowed` | page 207 | Left body controller: a207 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_releaseAllowed` | page 207 | Left body controller: a207 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_parkPendingAllowed` | page 207 | Left body controller: a207 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_wenchPendingAllowed` | page 207 | Left body controller: a207 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a207_unitStatusEPB` | page 207 | Left body controller: a207 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a207_unitStatusEPBM` | page 207 | Left body controller: a207 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a208_unknownAllowed` | page 208 | Left body controller: a208 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_openAllowed` | page 208 | Left body controller: a208 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_dynamicAllowed` | page 208 | Left body controller: a208 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_parkAllowed` | page 208 | Left body controller: a208 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_startAllowed` | page 208 | Left body controller: a208 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_serviceAllowed` | page 208 | Left body controller: a208 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_winchAllowed` | page 208 | Left body controller: a208 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_winchReleaseAllowed` | page 208 | Left body controller: a208 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_parkingAllowed` | page 208 | Left body controller: a208 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_dynApplyAllowed` | page 208 | Left body controller: a208 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_releaseAllowed` | page 208 | Left body controller: a208 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_parkPendingAllowed` | page 208 | Left body controller: a208 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_wenchPendingAllowed` | page 208 | Left body controller: a208 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a208_unitStatusEPB` | page 208 | Left body controller: a208 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a208_unitStatusEPBM` | page 208 | Left body controller: a208 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a209_unknownAllowed` | page 209 | Left body controller: a209 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_openAllowed` | page 209 | Left body controller: a209 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_dynamicAllowed` | page 209 | Left body controller: a209 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_parkAllowed` | page 209 | Left body controller: a209 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_startAllowed` | page 209 | Left body controller: a209 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_serviceAllowed` | page 209 | Left body controller: a209 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_winchAllowed` | page 209 | Left body controller: a209 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_winchReleaseAllowed` | page 209 | Left body controller: a209 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_parkingAllowed` | page 209 | Left body controller: a209 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_dynApplyAllowed` | page 209 | Left body controller: a209 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_releaseAllowed` | page 209 | Left body controller: a209 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_parkPendingAllowed` | page 209 | Left body controller: a209 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_wenchPendingAllowed` | page 209 | Left body controller: a209 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a209_unitStatusEPB` | page 209 | Left body controller: a209 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a209_unitStatusEPBM` | page 209 | Left body controller: a209 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a210_unknownAllowed` | page 210 | Left body controller: a210 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_openAllowed` | page 210 | Left body controller: a210 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_dynamicAllowed` | page 210 | Left body controller: a210 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_parkAllowed` | page 210 | Left body controller: a210 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_startAllowed` | page 210 | Left body controller: a210 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_serviceAllowed` | page 210 | Left body controller: a210 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_winchAllowed` | page 210 | Left body controller: a210 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_winchReleaseAllowed` | page 210 | Left body controller: a210 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_parkingAllowed` | page 210 | Left body controller: a210 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_dynApplyAllowed` | page 210 | Left body controller: a210 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_releaseAllowed` | page 210 | Left body controller: a210 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_parkPendingAllowed` | page 210 | Left body controller: a210 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_wenchPendingAllowed` | page 210 | Left body controller: a210 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a210_unitStatusEPB` | page 210 | Left body controller: a210 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a210_unitStatusEPBM` | page 210 | Left body controller: a210 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCLEFT_a221_vbatProtVoltage` | page 221 | Left body controller: a221 vbat prot voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCLEFT_a221_vbatProtCurrent` | page 221 | Left body controller: a221 vbat prot current | 24\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCLEFT_a221_uvLoadshedVoltage` | page 221 | Left body controller: a221 uv loadshed voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCLEFT_a221_loadshedFromBattMonitor` | page 221 | Left body controller: a221 loadshed from batt monitor | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `VCLEFT_a221_faultInjectActive` | page 221 | Left body controller: a221 fault inject active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a221_loadshedResetActive` | page 221 | Left body controller: a221 loadshed reset active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a221_loadshedArmPrimary` | page 221 | Left body controller: a221 loadshed arm primary | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a224_seatMotorCalibrated` | page 224 | Left body controller: a224 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a224_seatMotorCurrent` | page 224 | Left body controller: a224 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a224_seatMotorState` | page 224 | Left body controller: a224 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a224_seatSwitchBack` | page 224 | Left body controller: a224 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a224_seatSwitchForward` | page 224 | Left body controller: a224 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a225_seatMotorCalibrated` | page 225 | Left body controller: a225 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a225_seatMotorCurrent` | page 225 | Left body controller: a225 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a225_seatMotorState` | page 225 | Left body controller: a225 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a225_seatSwitchBack` | page 225 | Left body controller: a225 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a225_seatSwitchForward` | page 225 | Left body controller: a225 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a226_seatMotorCalibrated` | page 226 | Left body controller: a226 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a226_seatMotorCurrent` | page 226 | Left body controller: a226 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a226_seatMotorState` | page 226 | Left body controller: a226 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a226_seatSwitchBack` | page 226 | Left body controller: a226 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a226_seatSwitchForward` | page 226 | Left body controller: a226 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a227_seatMotorCalibrated` | page 227 | Left body controller: a227 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a227_seatMotorCurrent` | page 227 | Left body controller: a227 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a227_seatMotorState` | page 227 | Left body controller: a227 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a227_seatSwitchBack` | page 227 | Left body controller: a227 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a227_seatSwitchForward` | page 227 | Left body controller: a227 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a228_seatMotorCalibrated` | page 228 | Left body controller: a228 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a228_seatMotorCurrent` | page 228 | Left body controller: a228 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a228_seatMotorPosReal` | page 228 | Left body controller: a228 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a228_seatMotorState` | page 228 | Left body controller: a228 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a228_seatSwitchBack` | page 228 | Left body controller: a228 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a228_seatSwitchForward` | page 228 | Left body controller: a228 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a229_seatMotorCalibrated` | page 229 | Left body controller: a229 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a229_seatMotorCurrent` | page 229 | Left body controller: a229 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a229_seatMotorPosReal` | page 229 | Left body controller: a229 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a229_seatMotorState` | page 229 | Left body controller: a229 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a229_seatSwitchBack` | page 229 | Left body controller: a229 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a229_seatSwitchForward` | page 229 | Left body controller: a229 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a230_seatMotorCalibrated` | page 230 | Left body controller: a230 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a230_seatMotorCurrent` | page 230 | Left body controller: a230 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a230_seatMotorPosReal` | page 230 | Left body controller: a230 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a230_seatMotorState` | page 230 | Left body controller: a230 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a230_seatSwitchBack` | page 230 | Left body controller: a230 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a230_seatSwitchForward` | page 230 | Left body controller: a230 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a231_seatMotorCalibrated` | page 231 | Left body controller: a231 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a231_seatMotorCurrent` | page 231 | Left body controller: a231 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a231_seatMotorPosReal` | page 231 | Left body controller: a231 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a231_seatMotorState` | page 231 | Left body controller: a231 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a231_seatSwitchBack` | page 231 | Left body controller: a231 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a231_seatSwitchForward` | page 231 | Left body controller: a231 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a232_seatMotorCurrent` | page 232 | Left body controller: a232 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a232_seatMotorPosReal` | page 232 | Left body controller: a232 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a232_seatMotorState` | page 232 | Left body controller: a232 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a232_seatSwitchBack` | page 232 | Left body controller: a232 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a232_seatSwitchForward` | page 232 | Left body controller: a232 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a233_seatMotorCurrent` | page 233 | Left body controller: a233 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a233_seatMotorPosReal` | page 233 | Left body controller: a233 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a233_seatMotorState` | page 233 | Left body controller: a233 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a233_seatSwitchBack` | page 233 | Left body controller: a233 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a233_seatSwitchForward` | page 233 | Left body controller: a233 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a234_seatMotorCurrent` | page 234 | Left body controller: a234 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a234_seatMotorPosReal` | page 234 | Left body controller: a234 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a234_seatMotorState` | page 234 | Left body controller: a234 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a234_seatSwitchBack` | page 234 | Left body controller: a234 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a234_seatSwitchForward` | page 234 | Left body controller: a234 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a235_seatMotorCurrent` | page 235 | Left body controller: a235 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a235_seatMotorPosReal` | page 235 | Left body controller: a235 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a235_seatMotorState` | page 235 | Left body controller: a235 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a235_seatSwitchBack` | page 235 | Left body controller: a235 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a235_seatSwitchForward` | page 235 | Left body controller: a235 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a236_lumbarAPressureHpa` | page 236 | Left body controller: a236 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a236_lumbarBPressureHpa` | page 236 | Left body controller: a236 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a236_lumbarDiagStatus` | page 236 | Left body controller: a236 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a236_lumbarAState` | page 236 | Left body controller: a236 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a236_lumbarBState` | page 236 | Left body controller: a236 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a237_lumbarAPressureHpa` | page 237 | Left body controller: a237 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a237_lumbarBPressureHpa` | page 237 | Left body controller: a237 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a237_lumbarDiagStatus` | page 237 | Left body controller: a237 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a237_lumbarAState` | page 237 | Left body controller: a237 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a237_lumbarBState` | page 237 | Left body controller: a237 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a238_lumbarAPressureHpa` | page 238 | Left body controller: a238 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a238_lumbarBPressureHpa` | page 238 | Left body controller: a238 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a238_lumbarDiagStatus` | page 238 | Left body controller: a238 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a238_lumbarAState` | page 238 | Left body controller: a238 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a238_lumbarBState` | page 238 | Left body controller: a238 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a239_seatHeatCurrent` | page 239 | Left body controller: a239 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a239_seatHeatTmp` | page 239 | Left body controller: a239 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a239_seatHeatTmpTarget` | page 239 | Left body controller: a239 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCLEFT_a240_seatHeatCurrent` | page 240 | Left body controller: a240 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a240_seatHeatTmp` | page 240 | Left body controller: a240 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a241_seatHeatCurrent` | page 241 | Left body controller: a241 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a241_seatHeatTmp` | page 241 | Left body controller: a241 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a241_cushion` | page 241 | Left body controller: a241 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a241_backrest` | page 241 | Left body controller: a241 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a242_seatHeatCurrent` | page 242 | Left body controller: a242 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a242_seatHeatTmp` | page 242 | Left body controller: a242 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a242_seatHeatTmpTarget` | page 242 | Left body controller: a242 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCLEFT_a243_seatHeatCurrent` | page 243 | Left body controller: a243 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a243_seatHeatTmp` | page 243 | Left body controller: a243 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a244_seatHeatCurrent` | page 244 | Left body controller: a244 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a244_seatHeatTmp` | page 244 | Left body controller: a244 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a244_cushion` | page 244 | Left body controller: a244 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a244_backrest` | page 244 | Left body controller: a244 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a245_seatHeatCurrent` | page 245 | Left body controller: a245 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a245_seatHeatTmp` | page 245 | Left body controller: a245 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a245_seatHeatTmpTarget` | page 245 | Left body controller: a245 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCLEFT_a246_seatHeatCurrent` | page 246 | Left body controller: a246 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a246_seatHeatTmp` | page 246 | Left body controller: a246 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a247_seatHeatCurrent` | page 247 | Left body controller: a247 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a247_seatHeatTmp` | page 247 | Left body controller: a247 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a247_cushion` | page 247 | Left body controller: a247 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a247_backrest` | page 247 | Left body controller: a247 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a248_seatHeatCurrent` | page 248 | Left body controller: a248 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a248_seatHeatTmp` | page 248 | Left body controller: a248 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a248_seatHeatTmpTarget` | page 248 | Left body controller: a248 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCLEFT_a249_seatHeatCurrent` | page 249 | Left body controller: a249 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a249_seatHeatTmp` | page 249 | Left body controller: a249 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a250_seatHeatCurrent` | page 250 | Left body controller: a250 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a250_seatHeatTmp` | page 250 | Left body controller: a250 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a250_cushion` | page 250 | Left body controller: a250 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a250_backrest` | page 250 | Left body controller: a250 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a251_seatMotorCurrent` | page 251 | Left body controller: a251 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a251_seatMotorPosReal` | page 251 | Left body controller: a251 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a251_seatMotorState` | page 251 | Left body controller: a251 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a251_seatSwitchBack` | page 251 | Left body controller: a251 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a251_seatSwitchForward` | page 251 | Left body controller: a251 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a252_seatMotorCurrent` | page 252 | Left body controller: a252 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a252_seatMotorPosReal` | page 252 | Left body controller: a252 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a252_seatMotorState` | page 252 | Left body controller: a252 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a252_seatSwitchBack` | page 252 | Left body controller: a252 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a252_seatSwitchForward` | page 252 | Left body controller: a252 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a253_seatMotorCurrent` | page 253 | Left body controller: a253 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a253_seatMotorPosReal` | page 253 | Left body controller: a253 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a253_seatMotorState` | page 253 | Left body controller: a253 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a253_seatSwitchBack` | page 253 | Left body controller: a253 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a253_seatSwitchForward` | page 253 | Left body controller: a253 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a254_seatMotorCurrent` | page 254 | Left body controller: a254 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a254_seatMotorPosReal` | page 254 | Left body controller: a254 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a254_seatMotorState` | page 254 | Left body controller: a254 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a254_seatSwitchBack` | page 254 | Left body controller: a254 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a254_seatSwitchForward` | page 254 | Left body controller: a254 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a263_seatMotorCurrent` | page 263 | Left body controller: a263 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a263_seatMotorDCurrent` | page 263 | Left body controller: a263 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a263_seatMotorPosReal` | page 263 | Left body controller: a263 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a263_seatMotorState` | page 263 | Left body controller: a263 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a264_seatMotorCurrent` | page 264 | Left body controller: a264 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a264_seatMotorDCurrent` | page 264 | Left body controller: a264 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a264_seatMotorPosReal` | page 264 | Left body controller: a264 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a264_seatMotorState` | page 264 | Left body controller: a264 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a265_seatMotorCurrent` | page 265 | Left body controller: a265 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a265_seatMotorDCurrent` | page 265 | Left body controller: a265 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a265_seatMotorPosReal` | page 265 | Left body controller: a265 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a265_seatMotorState` | page 265 | Left body controller: a265 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a266_seatMotorCurrent` | page 266 | Left body controller: a266 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a266_seatMotorDCurrent` | page 266 | Left body controller: a266 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a266_seatMotorPosReal` | page 266 | Left body controller: a266 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a266_seatMotorState` | page 266 | Left body controller: a266 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a267_seatMotorCurrent` | page 267 | Left body controller: a267 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a267_seatMotorDCurrent` | page 267 | Left body controller: a267 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a267_seatMotorPosReal` | page 267 | Left body controller: a267 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a267_seatMotorState` | page 267 | Left body controller: a267 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a268_seatMotorCurrent` | page 268 | Left body controller: a268 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a268_seatMotorDCurrent` | page 268 | Left body controller: a268 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a268_seatMotorPosReal` | page 268 | Left body controller: a268 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a268_seatMotorState` | page 268 | Left body controller: a268 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a269_seatMotorCurrent` | page 269 | Left body controller: a269 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a269_seatMotorDCurrent` | page 269 | Left body controller: a269 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a269_seatMotorPosReal` | page 269 | Left body controller: a269 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a269_seatMotorState` | page 269 | Left body controller: a269 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a270_seatMotorCurrent` | page 270 | Left body controller: a270 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a270_seatMotorDCurrent` | page 270 | Left body controller: a270 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a270_seatMotorPosReal` | page 270 | Left body controller: a270 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a270_seatMotorState` | page 270 | Left body controller: a270 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a272_expectedState` | page 272 | Left body controller: a272 expected state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCLEFT_a272_actualState` | page 272 | Left body controller: a272 actual state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `VCLEFT_a273_handlePWM` | page 273 | Left body controller: a273 handle PWM | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCLEFT_a273_temperature` | page 273 | Left body controller: a273 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a274_handlePWM` | page 274 | Left body controller: a274 handle PWM | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCLEFT_a274_temperature` | page 274 | Left body controller: a274 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a275_outputFaulted` | page 275 | Left body controller: a275 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a275_currentSenseFaulted` | page 275 | Left body controller: a275 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a275_tempSenseFaulted` | page 275 | Left body controller: a275 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a275_underCurrent` | page 275 | Left body controller: a275 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a275_overCurrent` | page 275 | Left body controller: a275 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a275_overTemperature` | page 275 | Left body controller: a275 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a282_voltage` | page 282 | Left body controller: a282 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a282_temperature` | page 282 | Left body controller: a282 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a283_voltage` | page 283 | Left body controller: a283 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a283_temperature` | page 283 | Left body controller: a283 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a290_isNetworkSwitch` | page 290 | Left body controller: a290 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a290_occupancySensorV` | page 290 | Left body controller: a290 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a290_railVoltage` | page 290 | Left body controller: a290 rail voltage | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a291_buckleSensorVoltage` | page 291 | Left body controller: a291 buckle sensor voltage | 16\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCLEFT_a291_railVoltage` | page 291 | Left body controller: a291 rail voltage | 28\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCLEFT_a292_isNetworkSwitch` | page 292 | Left body controller: a292 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a292_occupancySensorV` | page 292 | Left body controller: a292 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a292_railV` | page 292 | Left body controller: a292 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a293_isNetworkSwitch` | page 293 | Left body controller: a293 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a293_occupancySensorV` | page 293 | Left body controller: a293 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a293_railV` | page 293 | Left body controller: a293 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a294_isNetworkSwitch` | page 294 | Left body controller: a294 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a294_occupancySensorV` | page 294 | Left body controller: a294 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a294_railV` | page 294 | Left body controller: a294 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a295_buckleSensorVoltage` | page 295 | Left body controller: a295 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a295_railV` | page 295 | Left body controller: a295 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a296_buckleSensorVoltage` | page 296 | Left body controller: a296 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a296_railV` | page 296 | Left body controller: a296 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a297_cabinTmp` | page 297 | Left body controller: a297 cabin tmp | 16\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a302_overVoltage` | page 302 | Left body controller: a302 over voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_underVoltage` | page 302 | Left body controller: a302 under voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_motorOverTemperature` | page 302 | Left body controller: a302 motor over temperature | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_moduleOverCurrent` | page 302 | Left body controller: a302 module over current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_overRMSCurrent` | page 302 | Left body controller: a302 over RMS current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_motorStall` | page 302 | Left body controller: a302 motor stall | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_overloadFault` | page 302 | Left body controller: a302 overload fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_motorLostPhase` | page 302 | Left body controller: a302 motor lost phase | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_currentUnbalance` | page 302 | Left body controller: a302 current unbalance | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_overspeedFault` | page 302 | Left body controller: a302 overspeed fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_startupFailed` | page 302 | Left body controller: a302 startup failed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_TMS320OverTempShutDwn` | page 302 | Left body controller: a302 TMS320 over temp shut dwn | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_fetOvertempShutdown` | page 302 | Left body controller: a302 fet overtemp shutdown | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_motorDisconnect` | page 302 | Left body controller: a302 motor disconnect | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_DRV_MIA` | page 302 | Left body controller: a302 DRV MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_overCurrentLatch` | page 302 | Left body controller: a302 over current latch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_CBC_MIA` | page 302 | Left body controller: a302 CBC MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_CBC_UARTReset` | page 302 | Left body controller: a302 CBC UART reset | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a302_DRVFault` | page 302 | Left body controller: a302 DRV fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a303_eFuseTripCount` | page 303 | Left body controller: a303 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a306_disconnectedTime` | page 306 | Left body controller: a306 disconnected time | 16\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | plausible |
| `VCLEFT_a307_disconnectedTime` | page 307 | Left body controller: a307 disconnected time | 16\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | plausible |
| `VCLEFT_a308_tamperDetected` | page 308 | Left body controller: a308 tamper detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a309_5VMainVoltage` | page 309 | Left body controller: a309 5 v main voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a310_mirrorFoldTime` | page 310 | Left body controller: a310 mirror fold time | 16\|9 | little-endian | unsigned | 10 | 0 | ms | 0 to 5110 |  | plausible |
| `VCLEFT_a310_foldingDirection` | page 310 | Left body controller: a310 folding direction | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FOLD`<br>1 = `UNFOLD` | plausible |
| `VCLEFT_a310_mirrorMaxFoldCurrent` | page 310 | Left body controller: a310 mirror max fold current | 32\|7 | little-endian | signed | 0.05 | 0 | A | -3.2 to 3.15 |  | plausible |
| `VCLEFT_a310_ambientTemperature` | page 310 | Left body controller: a310 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCLEFT_a311_outputFaulted` | page 311 | Left body controller: a311 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a311_currentSenseFaulted` | page 311 | Left body controller: a311 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a311_tempSenseFaulted` | page 311 | Left body controller: a311 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a311_underCurrent` | page 311 | Left body controller: a311 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a311_overCurrent` | page 311 | Left body controller: a311 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a311_overTemperature` | page 311 | Left body controller: a311 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_outputFaulted` | page 312 | Left body controller: a312 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_currentSenseFaulted` | page 312 | Left body controller: a312 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_tempSenseFaulted` | page 312 | Left body controller: a312 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_underCurrent` | page 312 | Left body controller: a312 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_overCurrent` | page 312 | Left body controller: a312 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a312_overTemperature` | page 312 | Left body controller: a312 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_outputFaulted` | page 313 | Left body controller: a313 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_currentSenseFaulted` | page 313 | Left body controller: a313 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_tempSenseFaulted` | page 313 | Left body controller: a313 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_underCurrent` | page 313 | Left body controller: a313 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_overCurrent` | page 313 | Left body controller: a313 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a313_overTemperature` | page 313 | Left body controller: a313 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_outputFaulted` | page 314 | Left body controller: a314 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_currentSenseFaulted` | page 314 | Left body controller: a314 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_tempSenseFaulted` | page 314 | Left body controller: a314 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_underCurrent` | page 314 | Left body controller: a314 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_overCurrent` | page 314 | Left body controller: a314 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a314_overTemperature` | page 314 | Left body controller: a314 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_outputFaulted` | page 315 | Left body controller: a315 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_currentSenseFaulted` | page 315 | Left body controller: a315 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_tempSenseFaulted` | page 315 | Left body controller: a315 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_underCurrent` | page 315 | Left body controller: a315 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_overCurrent` | page 315 | Left body controller: a315 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a315_overTemperature` | page 315 | Left body controller: a315 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a316_foldState` | page 316 | Left body controller: a316 fold state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `FOLDED`<br>2 = `UNFOLDED`<br>3 = `FOLDING`<br>4 = `UNFOLDING` | plausible |
| `VCLEFT_a316_actuationDurationMs` | page 316 | Left body controller: a316 actuation duration ms | 19\|10 | little-endian | unsigned | 10 | 0 | ms | 0 to 10230 |  | plausible |
| `VCLEFT_a316_maxCurrentAmps` | page 316 | Left body controller: a316 max current amps | 32\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a316_averageCurrentAmps` | page 316 | Left body controller: a316 average current amps | 44\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a316_ambientTemperatureDegC` | page 316 | Left body controller: a316 ambient temperature deg c; raw 0 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCLEFT_a318_configExpected` | page 318 | Left body controller: a318 config expected | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `TESLA_REV1`<br>2 = `TESLA_REV2` | plausible |
| `VCLEFT_a318_hardwareIdActual` | page 318 | Left body controller: a318 hardware id actual | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a319_IBSTsOutputRodDriver` | page 319 | Left body controller: a319 IBS ts output rod driver | 16\|12 | little-endian | unsigned | 0.015625 | -5 | mm | -5 to 58.984375 |  | plausible |
| `VCLEFT_a319_IBSTsOutputRodDriverQF` | page 319 | Left body controller: a319 IBS ts output rod driver QF | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_INITIALIZED`<br>1 = `NORMAL`<br>2 = `FAULT` | plausible |
| `VCLEFT_a319_fallbackIndex` | page 319 | Left body controller: a319 fallback index | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCLEFT_a324_mirrorHeatCurrent` | page 324 | Left body controller: a324 mirror heat current | 16\|10 | little-endian | unsigned | 0.01 | 0 | A | 0 to 10.23 |  | plausible |
| `VCLEFT_a325_PWMdutyCycleFL` | page 325 | Left body controller: a325 PW mduty cycle FL | 16\|16 | little-endian | unsigned | 0.0025 | 0 | % | 0 to 163.8375 |  | plausible |
| `VCLEFT_a325_PWMfrequencyFL` | page 325 | Left body controller: a325 PW mfrequency FL | 32\|16 | little-endian | unsigned | 0.025 | 0 | Hz | 0 to 1638.375 |  | plausible |
| `VCLEFT_a325_PWMfaultFL` | page 325 | Left body controller: a325 PW mfault FL | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OVER_MAX_DUTY`<br>1 = `UNDER_MIN_DUTY`<br>2 = `OVER_MAX_PERIOD`<br>3 = `UNDER_MIN_PERIOD`<br>4 = `OVER_MAX_DELTA_DUTY`<br>5 = `MIA`<br>6 = `SHORT_CIRCUIT`<br>7 = `OPEN_CIRCUIT`<br>8 = `COUNT`<br>9 = `NONE` | plausible |
| `VCLEFT_a326_PWMdutyCycleRL` | page 326 | Left body controller: a326 PW mduty cycle RL | 16\|16 | little-endian | unsigned | 0.0025 | 0 | % | 0 to 163.8375 |  | plausible |
| `VCLEFT_a326_PWMfrequencyRL` | page 326 | Left body controller: a326 PW mfrequency RL | 32\|16 | little-endian | unsigned | 0.025 | 0 | Hz | 0 to 1638.375 |  | plausible |
| `VCLEFT_a326_PWMfaultRL` | page 326 | Left body controller: a326 PW mfault RL | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OVER_MAX_DUTY`<br>1 = `UNDER_MIN_DUTY`<br>2 = `OVER_MAX_PERIOD`<br>3 = `UNDER_MIN_PERIOD`<br>4 = `OVER_MAX_DELTA_DUTY`<br>5 = `MIA`<br>6 = `SHORT_CIRCUIT`<br>7 = `OPEN_CIRCUIT`<br>8 = `COUNT`<br>9 = `NONE` | plausible |
| `VCLEFT_a327_PWMdutyCycleFL` | page 327 | Left body controller: a327 PW mduty cycle FL | 16\|16 | little-endian | unsigned | 0.0025 | 0 | % | 0 to 163.8375 |  | plausible |
| `VCLEFT_a327_PWMfrequencyFL` | page 327 | Left body controller: a327 PW mfrequency FL | 32\|16 | little-endian | unsigned | 0.025 | 0 | Hz | 0 to 1638.375 |  | plausible |
| `VCLEFT_a327_PWMfaultFL` | page 327 | Left body controller: a327 PW mfault FL | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OVER_MAX_DUTY`<br>1 = `UNDER_MIN_DUTY`<br>2 = `OVER_MAX_PERIOD`<br>3 = `UNDER_MIN_PERIOD`<br>4 = `OVER_MAX_DELTA_DUTY`<br>5 = `MIA`<br>6 = `SHORT_CIRCUIT`<br>7 = `OPEN_CIRCUIT`<br>8 = `COUNT`<br>9 = `NONE` | plausible |
| `VCLEFT_a328_PWMdutyCycleRL` | page 328 | Left body controller: a328 PW mduty cycle RL | 16\|16 | little-endian | unsigned | 0.0025 | 0 | % | 0 to 163.8375 |  | plausible |
| `VCLEFT_a328_PWMfrequencyRL` | page 328 | Left body controller: a328 PW mfrequency RL | 32\|16 | little-endian | unsigned | 0.025 | 0 | Hz | 0 to 1638.375 |  | plausible |
| `VCLEFT_a328_PWMfaultRL` | page 328 | Left body controller: a328 PW mfault RL | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OVER_MAX_DUTY`<br>1 = `UNDER_MIN_DUTY`<br>2 = `OVER_MAX_PERIOD`<br>3 = `UNDER_MIN_PERIOD`<br>4 = `OVER_MAX_DELTA_DUTY`<br>5 = `MIA`<br>6 = `SHORT_CIRCUIT`<br>7 = `OPEN_CIRCUIT`<br>8 = `COUNT`<br>9 = `NONE` | plausible |
| `VCLEFT_a330_voltage` | page 330 | Left body controller: a330 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a330_maxCurrent` | page 330 | Left body controller: a330 max current | 24\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCLEFT_a330_temperature` | page 330 | Left body controller: a330 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a331_voltage` | page 331 | Left body controller: a331 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCLEFT_a331_maxCurrent` | page 331 | Left body controller: a331 max current | 24\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCLEFT_a331_temperature` | page 331 | Left body controller: a331 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCLEFT_a334_OHCDiagnosticMask` | page 334 | Left body controller: a334 OHC diagnostic mask | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCLEFT_a335_USSSelfTestResult` | page 335 | Left body controller: a335 USS self test result | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a335_EEPROMSelfTestResult` | page 335 | Left body controller: a335 EEPROM self test result | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a335_LMSelfTestResult` | page 335 | Left body controller: a335 LM self test result | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a335_SystemError` | page 335 | Left body controller: a335 system error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a335_SelfTestStatus` | page 335 | Left body controller: a335 self test status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_leftTurn` | page 341 | Left body controller: a341 left turn | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_rightTurn` | page 341 | Left body controller: a341 right turn | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_tail` | page 341 | Left body controller: a341 tail | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_stop` | page 341 | Left body controller: a341 stop | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_fog` | page 341 | Left body controller: a341 fog | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a341_reverse` | page 341 | Left body controller: a341 reverse | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a342_OverVoltage` | page 342 | Left body controller: a342 over voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a342_UnderVoltage` | page 342 | Left body controller: a342 under voltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a342_5VRailStatus` | page 342 | Left body controller: a342 5 v rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a342_OverTemperature` | page 342 | Left body controller: a342 over temperature | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a345_secondsSinceWakeUp` | page 345 | Left body controller: a345 seconds since wake up | 16\|32 | little-endian | unsigned | 0.001 | 0 | Seconds | 0 to 4294967.295 |  | plausible |
| `VCLEFT_a345_powerCycleCount` | page 345 | Left body controller: a345 power cycle count | 48\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `VCLEFT_a346_eFuseTripCount` | page 346 | Left body controller: a346 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a348_current` | page 348 | Left body controller: a348 current | 16\|16 | little-endian | unsigned | 0.001 | 0 | mA | 0 to 65.535 |  | plausible |
| `VCLEFT_a349_voltage` | page 349 | Left body controller: a349 voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `VCLEFT_a350_ensPeriod` | page 350 | Left body controller: a350 ens period | 16\|16 | little-endian | unsigned | 0.0001 | 0 | s | 0 to 6.5535 |  | plausible |
| `VCLEFT_a350_ensDuty` | page 350 | Left body controller: a350 ens duty | 32\|10 | little-endian | unsigned | 0.00098 | 0 | % | 0 to 1.00254 |  | plausible |
| `VCLEFT_a350_ensTimedOut` | page 350 | Left body controller: a350 ens timed out | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a352_liftgatePosition` | page 352 | Left body controller: a352 liftgate position | 16\|7 | little-endian | signed | 1 | 43 | deg | -21 to 106 |  | plausible |
| `VCLEFT_a352_liftgateVelocityNearLatch` | page 352 | Left body controller: a352 liftgate velocity near latch | 24\|7 | little-endian | signed | 0.5 | -17 | deg/s | -49 to 14.5 |  | plausible |
| `VCLEFT_a352_liftgateClosingCount` | page 352 | Left body controller: a352 liftgate closing count | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a352_liftgateClosingFailedCount` | page 352 | Left body controller: a352 liftgate closing failed count | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a353_eFuseTripCount` | page 353 | Left body controller: a353 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a354_eFuseTripCount` | page 354 | Left body controller: a354 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a355_liftgateStoppingCondition` | page 355 | Left body controller: a355 liftgate stopping condition | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `PINCH`<br>2 = `OBSTACLE_STALL`<br>3 = `LOW_12V`<br>4 = `STATE_TIMEOUT`<br>5 = `VEHICLE_AT_SPEED`<br>6 = `OBSTACLE_CURRENT`<br>7 = `OBSTACLE_TRAJ_POS`<br>8 = `OBSTACLE_TRAJ_VEL`<br>9 = `UNCALIBRATED`<br>10 = `LATCH_FAULT`<br>11 = `OBSTACLE_CURRENT_SPIKE`<br>12 = `FOLLOWER_REQUEST`<br>13 = `COUNT` | plausible |
| `VCLEFT_a355_liftgateLastState` | page 355 | Left body controller: a355 liftgate last state | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `OFF`<br>2 = `BACKOFF`<br>3 = `OPENING`<br>4 = `CLOSING`<br>5 = `CLOSED`<br>6 = `LATCH_OPENING`<br>7 = `LATCH_CLOSING`<br>8 = `NOT_INSTALLED`<br>9 = `UNKNOWN`<br>10 = `LATCH_EXIT`<br>11 = `END_OF_TRAVEL`<br>12 = `LATCH_ENTRY`<br>13 = `PARTY_DANCE` | plausible |
| `VCLEFT_a355_liftgatePosition` | page 355 | Left body controller: a355 liftgate position | 24\|7 | little-endian | signed | 1 | 43 | deg | -21 to 106 |  | plausible |
| `VCLEFT_a355_liftgateLatchStatus` | page 355 | Left body controller: a355 liftgate latch status; raw 0 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCLEFT_a355_ambientTemperature` | page 355 | Left body controller: a355 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCLEFT_a357_liftgateState` | page 357 | Left body controller: a357 liftgate state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `OFF`<br>2 = `BACKOFF`<br>3 = `OPENING`<br>4 = `CLOSING`<br>5 = `CLOSED`<br>6 = `LATCH_OPENING`<br>7 = `LATCH_CLOSING`<br>8 = `NOT_INSTALLED`<br>9 = `UNKNOWN`<br>10 = `LATCH_EXIT`<br>11 = `END_OF_TRAVEL`<br>12 = `LATCH_ENTRY`<br>13 = `PARTY_DANCE` | plausible |
| `VCLEFT_a357_liftgatePosition` | page 357 | Left body controller: a357 liftgate position | 24\|7 | little-endian | signed | 1 | 43 | deg | -21 to 106 |  | plausible |
| `VCLEFT_a357_liftgateLatchStatus` | page 357 | Left body controller: a357 liftgate latch status; raw 0 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCLEFT_a373_windowChannel` | page 373 | Left body controller: a373 window channel | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `REAR`<br>2 = `FRONT` | plausible |
| `VCLEFT_a374_leftTurn` | page 374 | Left body controller: a374 left turn | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_rightTurn` | page 374 | Left body controller: a374 right turn | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_tail` | page 374 | Left body controller: a374 tail | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_brake` | page 374 | Left body controller: a374 brake | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_fog` | page 374 | Left body controller: a374 fog | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_reverse` | page 374 | Left body controller: a374 reverse | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DETECTED`<br>1 = `DETECTED`<br>2 = `FAULT` | plausible |
| `VCLEFT_a374_trailerMode` | page 374 | Left body controller: a374 trailer mode | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a375_windowFront` | page 375 | Left body controller: a375 window front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a376_2RowSeatTrackActuatorCurrent` | page 376 | Left body controller: a376 2 row seat track actuator current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a376_2RowSeatTrackActuatorDuty` | page 376 | Left body controller: a376 2 row seat track actuator duty | 28\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a376_2RowSeatEasyEntryState` | page 376 | Left body controller: a376 2 row seat easy entry state; raw 6 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRACK_AFT_PITCH_LATCHED`<br>1 = `TRACK_UNLATCHING`<br>2 = `TRACK_FORE_PITCH_LATCHED`<br>3 = `PITCH_UNLATCHING`<br>4 = `TRACK_AFT_PITCH_UNLATCHED`<br>5 = `TRACK_FORE_PITCH_UNLATCHED`<br>6 = `SNA` | plausible |
| `VCLEFT_a376_2RowSeatTrackPositionSwitch` | page 376 | Left body controller: a376 2 row seat track position switch; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a380_inOutAxis` | page 380 | Left body controller: a380 in out axis | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a380_upDownAxis` | page 380 | Left body controller: a380 up down axis | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a391_averageSpeed` | page 391 | Left body controller: a391 average speed | 16\|6 | little-endian | unsigned | 10 | -100 | km/h | -100 to 530 |  | plausible |
| `VCLEFT_a391_averageGrade` | page 391 | Left body controller: a391 average grade | 24\|7 | little-endian | signed | 0.01 | 0 | rad | -0.64 to 0.63 |  | plausible |
| `VCLEFT_a391_averagePower` | page 391 | Left body controller: a391 average power | 32\|7 | little-endian | unsigned | 10 | -200 | kW | -200 to 1070 |  | plausible |
| `VCLEFT_a391_massEstimate` | page 391 | Left body controller: a391 mass estimate | 40\|6 | little-endian | unsigned | 25 | 1900 | kg | 1900 to 3475 |  | plausible |
| `VCLEFT_a391_pitchEstimateIMU` | page 391 | Left body controller: a391 pitch estimate IMU; raw 64 = signal not available (SNA) | 48\|7 | little-endian | signed | 0.001 | 0 | rad | -0.064 to 0.063 | -64 = `SNA` | plausible |
| `VCLEFT_a395_leftSteeringWheelSwitch` | page 395 | Left body controller: a395 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a395_rightSteeringWheelSwitch` | page 395 | Left body controller: a395 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button1Touch` | page 396 | Left body controller: a396 button1 touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button2Touch` | page 396 | Left body controller: a396 button2 touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button3Touch` | page 396 | Left body controller: a396 button3 touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button4Touch` | page 396 | Left body controller: a396 button4 touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button5Touch` | page 396 | Left body controller: a396 button5 touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a396_button6Touch` | page 396 | Left body controller: a396 button6 touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button1Touch` | page 397 | Left body controller: a397 button1 touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button2Touch` | page 397 | Left body controller: a397 button2 touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button3Touch` | page 397 | Left body controller: a397 button3 touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button4Touch` | page 397 | Left body controller: a397 button4 touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button5Touch` | page 397 | Left body controller: a397 button5 touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a397_button6Touch` | page 397 | Left body controller: a397 button6 touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button1Touch` | page 398 | Left body controller: a398 button1 touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button2Touch` | page 398 | Left body controller: a398 button2 touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button3Touch` | page 398 | Left body controller: a398 button3 touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button4Touch` | page 398 | Left body controller: a398 button4 touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button5Touch` | page 398 | Left body controller: a398 button5 touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a398_button6Touch` | page 398 | Left body controller: a398 button6 touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a399_leftSteeringWheelSwitch` | page 399 | Left body controller: a399 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a399_rightSteeringWheelSwitch` | page 399 | Left body controller: a399 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a399_leftNormalizedNoiseValue` | page 399 | Left body controller: a399 left normalized noise value | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a399_rightNormalizedNoiseValue` | page 399 | Left body controller: a399 right normalized noise value | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a401_button1Status` | page 401 | Left body controller: a401 button1 status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a401_button2Status` | page 401 | Left body controller: a401 button2 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a401_button3Status` | page 401 | Left body controller: a401 button3 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a401_button4Status` | page 401 | Left body controller: a401 button4 status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a401_button5Status` | page 401 | Left body controller: a401 button5 status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a401_button6Status` | page 401 | Left body controller: a401 button6 status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button1Status` | page 402 | Left body controller: a402 button1 status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button2Status` | page 402 | Left body controller: a402 button2 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button3Status` | page 402 | Left body controller: a402 button3 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button4Status` | page 402 | Left body controller: a402 button4 status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button5Status` | page 402 | Left body controller: a402 button5 status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a402_button6Status` | page 402 | Left body controller: a402 button6 status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a403_leftSteeringWheelSwitch` | page 403 | Left body controller: a403 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a403_rightSteeringWheelSwitch` | page 403 | Left body controller: a403 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a404_leftSteeringWheelSwitch` | page 404 | Left body controller: a404 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a404_rightSteeringWheelSwitch` | page 404 | Left body controller: a404 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a405_leftSteeringWheelSwitch` | page 405 | Left body controller: a405 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a405_rightSteeringWheelSwitch` | page 405 | Left body controller: a405 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a406_leftSteeringWheelSwitch` | page 406 | Left body controller: a406 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a406_rightSteeringWheelSwitch` | page 406 | Left body controller: a406 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a407_leftSteeringWheelSwitch` | page 407 | Left body controller: a407 left steering wheel switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a407_rightSteeringWheelSwitch` | page 407 | Left body controller: a407 right steering wheel switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a409_leftScrollWheelFault` | page 409 | Left body controller: a409 left scroll wheel fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a409_rightScrollWheelFault` | page 409 | Left body controller: a409 right scroll wheel fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a409_rightScrollWheelPrevious` | page 409 | Left body controller: a409 right scroll wheel previous | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a409_rightScrollWheelChallenge` | page 409 | Left body controller: a409 right scroll wheel challenge | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCLEFT_a409_rightScrollWheelRaw0` | page 409 | Left body controller: a409 right scroll wheel raw0 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a409_rightScrollWheelRaw1` | page 409 | Left body controller: a409 right scroll wheel raw1 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a410_leftScrollWheelFault` | page 410 | Left body controller: a410 left scroll wheel fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a410_rightScrollWheelFault` | page 410 | Left body controller: a410 right scroll wheel fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a411_leftScrollWheelFault` | page 411 | Left body controller: a411 left scroll wheel fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a411_rightScrollWheelFault` | page 411 | Left body controller: a411 right scroll wheel fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_outputFaulted` | page 412 | Left body controller: a412 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_currentSenseFaulted` | page 412 | Left body controller: a412 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_tempSenseFaulted` | page 412 | Left body controller: a412 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_underCurrent` | page 412 | Left body controller: a412 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_overCurrent` | page 412 | Left body controller: a412 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a412_overTemperature` | page 412 | Left body controller: a412 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a413_failureReason` | page 413 | Left body controller: a413 failure reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `DEVICE_STUCK_ON`<br>2 = `BRIDGE`<br>3 = `BRIDGE_AND_DEVICE_STUCK_ON`<br>4 = `LOAD_UNATTEMPTED_ON`<br>8 = `FOLLOWER`<br>16 = `TIMEOUT`<br>32 = `BRIDGE_SYNC` | plausible |
| `VCLEFT_a413_loadUnattemptedOnFailure` | page 413 | Left body controller: a413 load unattempted on failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a413_deviceStuckOnFailure` | page 413 | Left body controller: a413 device stuck on failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a413_uvLoadshedVsenseDigIn` | page 413 | Left body controller: a413 uv loadshed vsense dig in | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a413_uvLoadshedVoltage` | page 413 | Left body controller: a413 uv loadshed voltage | 25\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCLEFT_a414_leftHapticMotorFault` | page 414 | Left body controller: a414 left haptic motor fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a414_rightHapticMotorFault` | page 414 | Left body controller: a414 right haptic motor fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a415_leftVbatUndervoltageFault` | page 415 | Left body controller: a415 left vbat undervoltage fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a415_rightVbatUndervoltageFault` | page 415 | Left body controller: a415 right vbat undervoltage fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a415_leftVbatOvervoltageFault` | page 415 | Left body controller: a415 left vbat overvoltage fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a415_rightVbatOvervoltageFault` | page 415 | Left body controller: a415 right vbat overvoltage fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_leftDomeTouch` | page 417 | Left body controller: a417 left dome touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_parkButtonTouch` | page 417 | Left body controller: a417 park button touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_reverseButtonTouch` | page 417 | Left body controller: a417 reverse button touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_hazardButtonTouch` | page 417 | Left body controller: a417 hazard button touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_neutralButtonTouch` | page 417 | Left body controller: a417 neutral button touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_driveButtonTouch` | page 417 | Left body controller: a417 drive button touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a417_rightDomeTouch` | page 417 | Left body controller: a417 right dome touch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_leftDomeTouch` | page 419 | Left body controller: a419 left dome touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_parkButtonTouch` | page 419 | Left body controller: a419 park button touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_reverseButtonTouch` | page 419 | Left body controller: a419 reverse button touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_hazardButtonTouch` | page 419 | Left body controller: a419 hazard button touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_neutralButtonTouch` | page 419 | Left body controller: a419 neutral button touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_driveButtonTouch` | page 419 | Left body controller: a419 drive button touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a419_rightDomeTouch` | page 419 | Left body controller: a419 right dome touch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_leftDomeTouch` | page 420 | Left body controller: a420 left dome touch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_parkButtonTouch` | page 420 | Left body controller: a420 park button touch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_reverseButtonTouch` | page 420 | Left body controller: a420 reverse button touch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_hazardButtonTouch` | page 420 | Left body controller: a420 hazard button touch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_neutralButtonTouch` | page 420 | Left body controller: a420 neutral button touch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_driveButtonTouch` | page 420 | Left body controller: a420 drive button touch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a420_rightDomeTouch` | page 420 | Left body controller: a420 right dome touch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a421_parkButtonForce` | page 421 | Left body controller: a421 park button force | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a421_reverseButtonForce` | page 421 | Left body controller: a421 reverse button force | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a421_hazardButtonForce` | page 421 | Left body controller: a421 hazard button force | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a421_neutralButtonForce` | page 421 | Left body controller: a421 neutral button force | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a421_driveButtonForce` | page 421 | Left body controller: a421 drive button force | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_seat2RControllerStuckOff` | page 422 | Left body controller: a422 seat2 r controller stuck off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_auxSocketRearStuckOff` | page 422 | Left body controller: a422 aux socket rear stuck off | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_seat2RAllHeatersStuckOff` | page 422 | Left body controller: a422 seat2 r all heaters stuck off | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_trailerLightEcuStuckOff` | page 422 | Left body controller: a422 trailer light ecu stuck off | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_accessoryFeed3StuckOff` | page 422 | Left body controller: a422 accessory feed3 stuck off | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_vbatProtFusedSeatStuckOff` | page 422 | Left body controller: a422 vbat prot fused seat stuck off | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_usbPortsStuckOff` | page 422 | Left body controller: a422 usb ports stuck off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_auxSocketFrontStuckOff` | page 422 | Left body controller: a422 aux socket front stuck off | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_lumbarEcuStuckOff` | page 422 | Left body controller: a422 lumbar ecu stuck off | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_ambientRgbRightStuckOff` | page 422 | Left body controller: a422 ambient rgb right stuck off | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_ambientRgbMiddleStuckOff` | page 422 | Left body controller: a422 ambient rgb middle stuck off | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_ambientRgbLeftStuckOff` | page 422 | Left body controller: a422 ambient rgb left stuck off | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_door1rRgbStuckOff` | page 422 | Left body controller: a422 door1r rgb stuck off | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_door2rRgbStuckOff` | page 422 | Left body controller: a422 door2r rgb stuck off | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_seat1rVentFanBackrestStuckOff` | page 422 | Left body controller: a422 seat1r vent fan backrest stuck off | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_seat1rVentFanCushionStuckOff` | page 422 | Left body controller: a422 seat1r vent fan cushion stuck off | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_trailerBrakeEcuStuckOff` | page 422 | Left body controller: a422 trailer brake ecu stuck off | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_trailerAuxStuckOff` | page 422 | Left body controller: a422 trailer aux stuck off | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a422_vbatFusedStuckOff` | page 422 | Left body controller: a422 vbat fused stuck off | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a424_parkButtonLED` | page 424 | Left body controller: a424 park button LED | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a424_reverseButtonLED` | page 424 | Left body controller: a424 reverse button LED | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a424_neutralButtonLED` | page 424 | Left body controller: a424 neutral button LED | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a424_driveButtonLED` | page 424 | Left body controller: a424 drive button LED | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a424_commonButtonLED` | page 424 | Left body controller: a424 common button LED | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a425_leftVisorLightStatus` | page 425 | Left body controller: a425 left visor light status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a425_rightVisorLightStatus` | page 425 | Left body controller: a425 right visor light status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a426_seatMotorCalibrated` | page 426 | Left body controller: a426 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a426_seatMotorCurrent` | page 426 | Left body controller: a426 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a426_seatMotorPosReal` | page 426 | Left body controller: a426 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a426_seatMotorState` | page 426 | Left body controller: a426 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a426_seatSwitchBack` | page 426 | Left body controller: a426 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a426_seatSwitchForward` | page 426 | Left body controller: a426 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a426_cabinTmp` | page 426 | Left body controller: a426 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a427_seatMotorCalibrated` | page 427 | Left body controller: a427 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a427_seatMotorCurrent` | page 427 | Left body controller: a427 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a427_seatMotorPosReal` | page 427 | Left body controller: a427 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a427_seatMotorState` | page 427 | Left body controller: a427 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a427_seatSwitchBack` | page 427 | Left body controller: a427 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a427_seatSwitchForward` | page 427 | Left body controller: a427 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a427_cabinTmp` | page 427 | Left body controller: a427 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a428_seatMotorCalibrated` | page 428 | Left body controller: a428 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a428_seatMotorCurrent` | page 428 | Left body controller: a428 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a428_seatMotorPosReal` | page 428 | Left body controller: a428 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a428_seatMotorState` | page 428 | Left body controller: a428 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a428_seatSwitchBack` | page 428 | Left body controller: a428 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a428_seatSwitchForward` | page 428 | Left body controller: a428 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a428_cabinTmp` | page 428 | Left body controller: a428 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a429_seatMotorCalibrated` | page 429 | Left body controller: a429 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a429_seatMotorCurrent` | page 429 | Left body controller: a429 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a429_seatMotorPosReal` | page 429 | Left body controller: a429 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a429_seatMotorState` | page 429 | Left body controller: a429 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a429_seatSwitchBack` | page 429 | Left body controller: a429 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a429_seatSwitchForward` | page 429 | Left body controller: a429 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a429_cabinTmp` | page 429 | Left body controller: a429 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCLEFT_a430_leftRearDomeLightPowerSupplyStatus` | page 430 | Left body controller: a430 left rear dome light power supply status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a430_rightRearDomeLightPowerSupplyStatus` | page 430 | Left body controller: a430 right rear dome light power supply status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a431_dcdcVoltageFailure` | page 431 | Left body controller: a431 dcdc voltage failure | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a431_overVoltageDetected` | page 431 | Left body controller: a431 over voltage detected | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a431_underVoltageDetected` | page 431 | Left body controller: a431 under voltage detected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a431_brownoutDetected` | page 431 | Left body controller: a431 brownout detected | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_retriesAvailable` | page 444 | Left body controller: a444 retries available | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a444_channel` | page 444 | Left body controller: a444 channel | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a444_watchdog` | page 444 | Left body controller: a444 watchdog | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_gateDriver` | page 444 | Left body controller: a444 gate driver | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_overcurrent` | page 444 | Left body controller: a444 overcurrent | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_supplyUndervoltage` | page 444 | Left body controller: a444 supply undervoltage | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_cpUndervoltage` | page 444 | Left body controller: a444 cp undervoltage | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_overTempShutdown` | page 444 | Left body controller: a444 over temp shutdown | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_overTempWarning` | page 444 | Left body controller: a444 over temp warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_highSide2GateDriver` | page 444 | Left body controller: a444 high side2 gate driver | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_lowSide2GateDriver` | page 444 | Left body controller: a444 low side2 gate driver | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_highSide1GateDriver` | page 444 | Left body controller: a444 high side1 gate driver | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_lowSide1GateDriver` | page 444 | Left body controller: a444 low side1 gate driver | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_highSide2OverCurent` | page 444 | Left body controller: a444 high side2 over curent | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_lowSide2OverCurent` | page 444 | Left body controller: a444 low side2 over curent | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_highSide1OverCurent` | page 444 | Left body controller: a444 high side1 over curent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_lowSide1OverCurent` | page 444 | Left body controller: a444 low side1 over curent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_spiInit` | page 444 | Left body controller: a444 spi init | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_spiPeriodicCheck` | page 444 | Left body controller: a444 spi periodic check | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_spiFault` | page 444 | Left body controller: a444 spi fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_voltageMonitor` | page 444 | Left body controller: a444 voltage monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a444_enableLow` | page 444 | Left body controller: a444 enable low | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a447_endstopPositionMM` | page 447 | Left body controller: a447 endstop position MM | 16\|16 | little-endian | signed | 0.01 | 0 | mm | -327.68 to 327.67 |  | plausible |
| `VCLEFT_a447_motorType` | page 447 | Left body controller: a447 motor type | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BOSCH`<br>1 = `JE`<br>2 = `BOSCH_COMMON_TO_JE`<br>3 = `NEXTEER` | plausible |
| `VCLEFT_a448_endstopPositionMM` | page 448 | Left body controller: a448 endstop position MM | 16\|16 | little-endian | signed | 0.01 | 0 | mm | -327.68 to 327.67 |  | plausible |
| `VCLEFT_a448_motorType` | page 448 | Left body controller: a448 motor type | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BOSCH`<br>1 = `JE`<br>2 = `BOSCH_COMMON_TO_JE`<br>3 = `NEXTEER` | plausible |
| `VCLEFT_a453_liftgatePosition` | page 453 | Left body controller: a453 liftgate position | 16\|7 | little-endian | signed | 1 | 43 | deg | -21 to 106 |  | plausible |
| `VCLEFT_a455_liftgateState` | page 455 | Left body controller: a455 liftgate state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `OFF`<br>2 = `BACKOFF`<br>3 = `OPENING`<br>4 = `CLOSING`<br>5 = `CLOSED`<br>6 = `LATCH_OPENING`<br>7 = `LATCH_CLOSING`<br>8 = `NOT_INSTALLED`<br>9 = `UNKNOWN`<br>10 = `LATCH_EXIT`<br>11 = `END_OF_TRAVEL`<br>12 = `LATCH_ENTRY`<br>13 = `PARTY_DANCE` | plausible |
| `VCLEFT_a466_hvac2RLeftAirwaveVerticalStall` | page 466 | Left body controller: a466 hvac2 r left airwave vertical stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a469_hvac2RLeftAirwaveLateralStall` | page 469 | Left body controller: a469 hvac2 r left airwave lateral stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a472_hvac2RRightAirwaveVerticalStall` | page 472 | Left body controller: a472 hvac2 r right airwave vertical stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a475_hvac2RRightAirwaveLateralStall` | page 475 | Left body controller: a475 hvac2 r right airwave lateral stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_reset` | page 480 | Left body controller: a480 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_spiError` | page 480 | Left body controller: a480 spi error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_autoOn` | page 480 | Left body controller: a480 auto on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_diagnosticBit` | page 480 | Left body controller: a480 diagnostic bit | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_deviceError` | page 480 | Left body controller: a480 device error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_overcurrent` | page 480 | Left body controller: a480 overcurrent | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_unexpectedLock` | page 480 | Left body controller: a480 unexpected lock | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_disableOutputFault` | page 480 | Left body controller: a480 disable output fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_vsUndervoltage` | page 480 | Left body controller: a480 vs undervoltage | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_hardShort` | page 480 | Left body controller: a480 hard short | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_vdsMax` | page 480 | Left body controller: a480 vds max | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_bypassSaturation` | page 480 | Left body controller: a480 bypass saturation | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_fuseLatch` | page 480 | Left body controller: a480 fuse latch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_deviceOvertemperature` | page 480 | Left body controller: a480 device overtemperature | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_ntcOvertemperature` | page 480 | Left body controller: a480 ntc overtemperature | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_vgsLow` | page 480 | Left body controller: a480 vgs low | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_chargePumpLow` | page 480 | Left body controller: a480 charge pump low | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_watchdog` | page 480 | Left body controller: a480 watchdog | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_spiNotDone` | page 480 | Left body controller: a480 spi not done | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_configIncorrect` | page 480 | Left body controller: a480 config incorrect | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_bufferFull` | page 480 | Left body controller: a480 buffer full | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_hitAlertRateLimit` | page 480 | Left body controller: a480 hit alert rate limit | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_hwlo` | page 480 | Left body controller: a480 hwlo | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a480_enable` | page 480 | Left body controller: a480 enable | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_channel` | page 482 | Left body controller: a482 channel | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCLEFT_a482_spiFault` | page 482 | Left body controller: a482 spi fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_resetBar` | page 482 | Left body controller: a482 reset bar | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_overTempShutdown` | page 482 | Left body controller: a482 over temp shutdown | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_thermalWarning` | page 482 | Left body controller: a482 thermal warning | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_underOrOverVoltageOrOverCurrent` | page 482 | Left body controller: a482 under or over voltage or over current | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a482_underloadDetected` | page 482 | Left body controller: a482 underload detected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_seat2RControllerUnattemptedOn` | page 485 | Left body controller: a485 seat2 r controller unattempted on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_auxSocketRearUnattemptedOn` | page 485 | Left body controller: a485 aux socket rear unattempted on | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_seat2RAllHeatersUnattemptedOn` | page 485 | Left body controller: a485 seat2 r all heaters unattempted on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_trailerLightEcuUnattemptedOn` | page 485 | Left body controller: a485 trailer light ecu unattempted on | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_accessoryFeed3UnattemptedOn` | page 485 | Left body controller: a485 accessory feed3 unattempted on | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_vbatProtFusedSeatUnattemptedOn` | page 485 | Left body controller: a485 vbat prot fused seat unattempted on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_usbPortsUnattemptedOn` | page 485 | Left body controller: a485 usb ports unattempted on | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_auxSocketFrontUnattemptedOn` | page 485 | Left body controller: a485 aux socket front unattempted on | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_lumbarEcuUnattemptedOn` | page 485 | Left body controller: a485 lumbar ecu unattempted on | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_ambientRgbRightUnattemptedOn` | page 485 | Left body controller: a485 ambient rgb right unattempted on | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_ambientRgbMiddleUnattemptedOn` | page 485 | Left body controller: a485 ambient rgb middle unattempted on | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_ambientRgbLeftUnattemptedOn` | page 485 | Left body controller: a485 ambient rgb left unattempted on | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_door1rRgbUnattemptedOn` | page 485 | Left body controller: a485 door1r rgb unattempted on | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_door2rRgbUnattemptedOn` | page 485 | Left body controller: a485 door2r rgb unattempted on | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_seat1rVentFanBackrestUnattemptedOn` | page 485 | Left body controller: a485 seat1r vent fan backrest unattempted on | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_seat1rVentFanCushionUnattemptedOn` | page 485 | Left body controller: a485 seat1r vent fan cushion unattempted on | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_trailerBrakeEcuUnattemptedOn` | page 485 | Left body controller: a485 trailer brake ecu unattempted on | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_trailerAuxUnattemptedOn` | page 485 | Left body controller: a485 trailer aux unattempted on | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a485_vbatFusedUnattemptedOn` | page 485 | Left body controller: a485 vbat fused unattempted on | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a489_seat2RControllerStuckOn` | page 489 | Left body controller: a489 seat2 r controller stuck on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_auxSocketRearStuckOn` | page 489 | Left body controller: a489 aux socket rear stuck on | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON` | plausible |
| `VCLEFT_a489_seat2RAllHeatersStuckOn` | page 489 | Left body controller: a489 seat2 r all heaters stuck on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_trailerLightEcuStuckOn` | page 489 | Left body controller: a489 trailer light ecu stuck on | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_accessoryFeed3StuckOn` | page 489 | Left body controller: a489 accessory feed3 stuck on | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_vbatProtFusedSeatStuckOn` | page 489 | Left body controller: a489 vbat prot fused seat stuck on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON` | plausible |
| `VCLEFT_a489_usbPortsStuckOn` | page 489 | Left body controller: a489 usb ports stuck on | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_auxSocketFrontStuckOn` | page 489 | Left body controller: a489 aux socket front stuck on | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON` | plausible |
| `VCLEFT_a489_lumbarEcuStuckOn` | page 489 | Left body controller: a489 lumbar ecu stuck on | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_ambientRgbRightStuckOn` | page 489 | Left body controller: a489 ambient rgb right stuck on | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_ambientRgbMiddleStuckOn` | page 489 | Left body controller: a489 ambient rgb middle stuck on | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_ambientRgbLeftStuckOn` | page 489 | Left body controller: a489 ambient rgb left stuck on | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_door1rRgbStuckOn` | page 489 | Left body controller: a489 door1r rgb stuck on | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_door2rRgbStuckOn` | page 489 | Left body controller: a489 door2r rgb stuck on | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_seat1rVentFanBackrestStuckOn` | page 489 | Left body controller: a489 seat1r vent fan backrest stuck on | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_seat1rVentFanCushionStuckOn` | page 489 | Left body controller: a489 seat1r vent fan cushion stuck on | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_trailerBrakeEcuStuckOn` | page 489 | Left body controller: a489 trailer brake ecu stuck on | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_trailerAuxStuckOn` | page 489 | Left body controller: a489 trailer aux stuck on | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_vbatFusedStuckOn` | page 489 | Left body controller: a489 vbat fused stuck on | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCLEFT_a489_vbatProtVoltage` | page 489 | Left body controller: a489 vbat prot voltage | 35\|9 | little-endian | unsigned | 0.0391389429569 | 0 | V | 0 to 19.999999851 |  | plausible |
| `VCLEFT_a489_loadshedCommonBusVoltage` | page 489 | Left body controller: a489 loadshed common bus voltage | 44\|9 | little-endian | unsigned | 0.0391389429569 | 0 | V | 0 to 19.999999851 |  | plausible |
| `VCLEFT_a489_loadshedCommonBusMonitorRatio` | page 489 | Left body controller: a489 loadshed common bus monitor ratio | 56\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 127 |  | plausible |
| `VCLEFT_a493_12vSocketFrontEFuseCurrent` | page 493 | Left body controller: a493 12v socket front e fuse current; raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51 | 511 = `SNA` | plausible |
| `VCLEFT_a494_12vSocketRearEFuseCurrent` | page 494 | Left body controller: a494 12v socket rear e fuse current; raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51 | 511 = `SNA` | plausible |
| `VCLEFT_a497_ecuUnprovisioned` | page 497 | Left body controller: a497 ecu unprovisioned | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a500_channel` | page 500 | Left body controller: a500 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a500_mismatchedState` | page 500 | Left body controller: a500 mismatched state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `STANDBY`<br>2 = `WAKEUP`<br>3 = `CONFIGURATION`<br>4 = `UNLOCKED`<br>5 = `LOCKED`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | plausible |
| `VCLEFT_a510_isRearwardEndstopUncalibrated` | page 510 | Left body controller: a510 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a510_isAbsPosSensorUncalibrated` | page 510 | Left body controller: a510 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a510_seatState` | page 510 | Left body controller: a510 seat state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a510_motorType` | page 510 | Left body controller: a510 motor type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCLEFT_a510_absPosSensState` | page 510 | Left body controller: a510 abs pos sens state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAULTED`<br>1 = `REARWARD`<br>2 = `FORWARD`<br>3 = `DISCONNECTED` | plausible |
| `VCLEFT_a513_calibrated` | page 513 | Left body controller: a513 calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a513_angle` | page 513 | Left body controller: a513 angle | 17\|8 | little-endian | signed | 0.5 | 59 | deg | -5 to 122.5 |  | plausible |
| `VCLEFT_a513_seatStatePrev` | page 513 | Left body controller: a513 seat state prev; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a513_obstacleDetectReason` | page 513 | Left body controller: a513 obstacle detect reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `MOTOR_CURRENT_STALL`<br>2 = `MOTOR_ENCODER_STALL`<br>3 = `ACCEL_LOOKBACK_UNCOMP_ABS`<br>4 = `ACCEL_LOOKBACK_UNCOMP_REL`<br>5 = `ACCEL_LOOKBACK_COMP_ABS`<br>6 = `MEDIUM_CURRENT_THRESHOLD`<br>7 = `SPEED_THRESHOLD`<br>8 = `MAX_SPEED_DIFF` | plausible |
| `VCLEFT_a513_accelLookbackTripDepth` | page 513 | Left body controller: a513 accel lookback trip depth | 33\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `VCLEFT_a513_duty` | page 513 | Left body controller: a513 duty | 40\|8 | little-endian | signed | 1 | 0 | % | -128 to 127 |  | plausible |
| `VCLEFT_a513_currentAbsFilt` | page 513 | Left body controller: a513 current abs filt | 48\|8 | little-endian | unsigned | 0.25 | 0 | A | 0 to 63.75 |  | plausible |
| `VCLEFT_a513_motorType` | page 513 | Left body controller: a513 motor type | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCLEFT_a513_absolutePosSensorForward` | page 513 | Left body controller: a513 absolute pos sensor forward | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a513_cabinTemp` | page 513 | Left body controller: a513 cabin temp | 58\|6 | little-endian | signed | 2 | 20 | degC | -44 to 82 |  | plausible |
| `VCLEFT_a517_isRearwardEndstopUncalibrated` | page 517 | Left body controller: a517 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a517_isAbsPosSensorUncalibrated` | page 517 | Left body controller: a517 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a518_seatState` | page 518 | Left body controller: a518 seat state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a520_epbConfig` | page 520 | Left body controller: a520 epb config | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a520_gtwEpbConfig` | page 520 | Left body controller: a520 gtw epb config | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCLEFT_a523_channel` | page 523 | Left body controller: a523 channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a523_control2Byte1` | page 523 | Left body controller: a523 control2 byte1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a523_control2Byte2` | page 523 | Left body controller: a523 control2 byte2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a523_control2Byte3` | page 523 | Left body controller: a523 control2 byte3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a523_control3Byte2` | page 523 | Left body controller: a523 control3 byte2 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a523_control3Byte3` | page 523 | Left body controller: a523 control3 byte3 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a525_GTW_twelveVBatteryType` | page 525 | Left body controller: a525 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCLEFT_a525_newLVBatteryType` | page 525 | Left body controller: a525 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCLEFT_a525_initialLVBatteryType` | page 525 | Left body controller: a525 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCLEFT_a525_serviceMode` | page 525 | Signal reported by Left body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a525_factoryGated` | page 525 | Left body controller: a525 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a525_frunkOpen` | page 525 | Left body controller: a525 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a536_trunkFoldFlatSwitchState` | page 536 | Left body controller: a536 trunk fold flat switch state; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a536_trunkFoldFlatLeftSwitchVoltage` | page 536 | Left body controller: a536 trunk fold flat left switch voltage | 18\|10 | little-endian | unsigned | 0.00488758552819 | 0 | V | 0 to 4.99999999534 |  | plausible |
| `VCLEFT_a545_GTW_twelveVBatteryType` | page 545 | Left body controller: a545 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCLEFT_a545_newLVBatteryType` | page 545 | Left body controller: a545 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCLEFT_a545_serviceMode` | page 545 | Signal reported by Left body controller | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a545_factoryGated` | page 545 | Left body controller: a545 factory gated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a545_frunkOpen` | page 545 | Left body controller: a545 frunk open | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a551_restrictDoorReleaseSignalFront` | page 551 | Left body controller: a551 restrict door release signal front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a551_interiorReleaseReqCountFront` | page 551 | Left body controller: a551 interior release req count front | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a551_lastRequestSourceFront` | page 551 | Left body controller: a551 last request source front | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCLEFT_a551_restrictDoorReleaseSignalRear` | page 551 | Left body controller: a551 restrict door release signal rear | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a551_interiorReleaseReqCountRear` | page 551 | Left body controller: a551 interior release req count rear | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a551_lastRequestSourceRear` | page 551 | Left body controller: a551 last request source rear | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCLEFT_a555_heaterPWMCommand` | page 555 | Left body controller: a555 heater PWM command | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a555_ntcTemperature` | page 555 | Left body controller: a555 ntc temperature | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_a560_isRearwardEndstopUncalibrated` | page 560 | Left body controller: a560 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a560_isAbsPosSensorUncalibrated` | page 560 | Left body controller: a560 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a560_seatState` | page 560 | Left body controller: a560 seat state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a560_motorType` | page 560 | Left body controller: a560 motor type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCLEFT_a560_absPosSensState` | page 560 | Left body controller: a560 abs pos sens state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAULTED`<br>1 = `REARWARD`<br>2 = `FORWARD`<br>3 = `DISCONNECTED` | plausible |
| `VCLEFT_a563_calibrated` | page 563 | Left body controller: a563 calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a563_angle` | page 563 | Left body controller: a563 angle | 17\|8 | little-endian | signed | 0.5 | 59 | deg | -5 to 122.5 |  | plausible |
| `VCLEFT_a563_seatStatePrev` | page 563 | Left body controller: a563 seat state prev; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a563_obstacleDetectReason` | page 563 | Left body controller: a563 obstacle detect reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `MOTOR_CURRENT_STALL`<br>2 = `MOTOR_ENCODER_STALL`<br>3 = `ACCEL_LOOKBACK_UNCOMP_ABS`<br>4 = `ACCEL_LOOKBACK_UNCOMP_REL`<br>5 = `ACCEL_LOOKBACK_COMP_ABS`<br>6 = `MEDIUM_CURRENT_THRESHOLD`<br>7 = `SPEED_THRESHOLD`<br>8 = `MAX_SPEED_DIFF` | plausible |
| `VCLEFT_a563_accelLookbackTripDepth` | page 563 | Left body controller: a563 accel lookback trip depth | 33\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `VCLEFT_a563_duty` | page 563 | Left body controller: a563 duty | 40\|8 | little-endian | signed | 1 | 0 | % | -128 to 127 |  | plausible |
| `VCLEFT_a563_currentAbsFilt` | page 563 | Left body controller: a563 current abs filt | 48\|8 | little-endian | unsigned | 0.25 | 0 | A | 0 to 63.75 |  | plausible |
| `VCLEFT_a563_motorType` | page 563 | Left body controller: a563 motor type | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCLEFT_a563_absolutePosSensorForward` | page 563 | Left body controller: a563 absolute pos sensor forward | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a563_cabinTemp` | page 563 | Left body controller: a563 cabin temp | 58\|6 | little-endian | signed | 2 | 20 | degC | -44 to 82 |  | plausible |
| `VCLEFT_a567_isRearwardEndstopUncalibrated` | page 567 | Left body controller: a567 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a567_isAbsPosSensorUncalibrated` | page 567 | Left body controller: a567 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a568_seatState` | page 568 | Left body controller: a568 seat state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCLEFT_a570_seatHeatCurrent` | page 570 | Left body controller: a570 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a570_seatHeatTmp` | page 570 | Left body controller: a570 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a571_seatHeatCurrent` | page 571 | Left body controller: a571 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a571_seatHeatTmp` | page 571 | Left body controller: a571 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a572_seatHeatCurrent` | page 572 | Left body controller: a572 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a572_seatHeatTmp` | page 572 | Left body controller: a572 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a573_seatHeatCurrent` | page 573 | Left body controller: a573 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCLEFT_a573_seatHeatTmp` | page 573 | Left body controller: a573 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCLEFT_a577_outputFaulted` | page 577 | Left body controller: a577 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a577_currentSenseFaulted` | page 577 | Left body controller: a577 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a577_tempSenseFaulted` | page 577 | Left body controller: a577 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a577_underCurrent` | page 577 | Left body controller: a577 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a577_overCurrent` | page 577 | Left body controller: a577 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a577_overTemperature` | page 577 | Left body controller: a577 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_openCircuitDashFL` | page 578 | Left body controller: a578 open circuit dash FL | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_shortCircuitDashFL` | page 578 | Left body controller: a578 short circuit dash FL | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_miaDashFL` | page 578 | Left body controller: a578 mia dash FL | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_openCircuitDashFR` | page 578 | Left body controller: a578 open circuit dash FR | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_shortCircuitDashFR` | page 578 | Left body controller: a578 short circuit dash FR | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_miaDashFR` | page 578 | Left body controller: a578 mia dash FR | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_openCircuitDoorFL` | page 578 | Left body controller: a578 open circuit door FL | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_shortCircuitDoorFL` | page 578 | Left body controller: a578 short circuit door FL | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_miaDoorFL` | page 578 | Left body controller: a578 mia door FL | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_openCircuitDoorRL` | page 578 | Left body controller: a578 open circuit door RL | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_shortCircuitDoorRL` | page 578 | Left body controller: a578 short circuit door RL | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a578_miaDoorRL` | page 578 | Left body controller: a578 mia door RL | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a579_gtwConfigType` | page 579 | Left body controller: a579 gtw config type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `PREH`<br>2 = `KOSTAL`<br>5 = `TESLA_GEN5` | plausible |
| `VCLEFT_a579_installedHwid` | page 579 | Left body controller: a579 installed hwid | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCLEFT_a580_gtwConfigType` | page 580 | Left body controller: a580 gtw config type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `PREH`<br>2 = `KOSTAL`<br>5 = `TESLA_GEN5` | plausible |
| `VCLEFT_a580_installedHwid` | page 580 | Left body controller: a580 installed hwid | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCLEFT_a581_outputFaulted` | page 581 | Left body controller: a581 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a581_currentSenseFaulted` | page 581 | Left body controller: a581 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a581_tempSenseFaulted` | page 581 | Left body controller: a581 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a581_underCurrent` | page 581 | Left body controller: a581 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a581_overCurrent` | page 581 | Left body controller: a581 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a581_overTemperature` | page 581 | Left body controller: a581 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a582_outputCurrent` | page 582 | Left body controller: a582 output current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCLEFT_a585_ambientTemp` | page 585 | Left body controller: a585 ambient temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCLEFT_a586_ambientTemp` | page 586 | Left body controller: a586 ambient temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCLEFT_a587_VEH_seatStatus2` | page 587 | Left body controller: a587 VEH seat status2 | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a587_VEH_switchStatus` | page 587 | Left body controller: a587 VEH switch status | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a590_seatMotorCalibrated` | page 590 | Left body controller: a590 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a590_seatMotorCurrent` | page 590 | Left body controller: a590 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a590_seatMotorState` | page 590 | Left body controller: a590 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a590_seatSwitchBack` | page 590 | Left body controller: a590 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a590_seatSwitchForward` | page 590 | Left body controller: a590 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a591_seatMotorCurrent` | page 591 | Left body controller: a591 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a591_seatMotorPosReal` | page 591 | Left body controller: a591 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a591_seatMotorState` | page 591 | Left body controller: a591 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a591_seatSwitchBack` | page 591 | Left body controller: a591 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a591_seatSwitchForward` | page 591 | Left body controller: a591 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a592_seatMotorCurrent` | page 592 | Left body controller: a592 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a592_seatMotorPosReal` | page 592 | Left body controller: a592 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a592_seatMotorState` | page 592 | Left body controller: a592 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a592_seatSwitchBack` | page 592 | Left body controller: a592 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a592_seatSwitchForward` | page 592 | Left body controller: a592 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a593_seatMotorCalibrated` | page 593 | Left body controller: a593 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a593_seatMotorCurrent` | page 593 | Left body controller: a593 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a593_seatMotorPosReal` | page 593 | Left body controller: a593 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a593_seatMotorState` | page 593 | Left body controller: a593 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a593_seatSwitchBack` | page 593 | Left body controller: a593 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a593_seatSwitchForward` | page 593 | Left body controller: a593 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCLEFT_a594_seatMotorCurrent` | page 594 | Left body controller: a594 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a594_seatMotorDCurrent` | page 594 | Left body controller: a594 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a594_seatMotorPosReal` | page 594 | Left body controller: a594 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a594_seatMotorState` | page 594 | Left body controller: a594 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a595_seatMotorCurrent` | page 595 | Left body controller: a595 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a595_seatMotorDCurrent` | page 595 | Left body controller: a595 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCLEFT_a595_seatMotorPosReal` | page 595 | Left body controller: a595 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCLEFT_a595_seatMotorState` | page 595 | Left body controller: a595 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCLEFT_a596_frontDoorLatchAjarSwitchVoltage` | page 596 | Left body controller: a596 front door latch ajar switch voltage | 16\|12 | little-endian | unsigned | 1.25 | 0 | mV | 0 to 5118.75 |  | plausible |
| `VCLEFT_a597_rearDoorLatchAjarSwitchVoltage` | page 597 | Left body controller: a597 rear door latch ajar switch voltage | 16\|12 | little-endian | unsigned | 1.25 | 0 | mV | 0 to 5118.75 |  | plausible |
| `VCLEFT_a599_GTW_twelveVBatteryType` | page 599 | Left body controller: a599 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCLEFT_a599_newLVBatteryType` | page 599 | Left body controller: a599 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCLEFT_a599_initialLVBatteryType` | page 599 | Left body controller: a599 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCLEFT_a599_serviceMode` | page 599 | Signal reported by Left body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a599_factoryGated` | page 599 | Left body controller: a599 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a599_frunkOpen` | page 599 | Left body controller: a599 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_a605_excessiveMacFailures` | page 605 | Left body controller: a605 excessive mac failures | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCLEFT_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 10 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (13 signals), page 87 (9 signals), page 88 (9 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (3 signals), page 95 (2 signals), page 96 (2 signals), page 97 (2 signals), page 98 (14 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (5 signals), page 107 (14 signals), page 108 (14 signals), page 110 (17 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (20 signals), page 116 (29 signals), page 117 (24 signals), page 118 (30 signals), page 119 (6 signals), page 120 (33 signals), page 121 (1 signals), page 123 (1 signals), page 124 (3 signals), page 125 (4 signals), page 129 (27 signals), page 130 (14 signals), page 131 (5 signals), page 132 (2 signals), page 133 (2 signals), page 141 (1 signals), page 145 (3 signals), page 150 (8 signals), page 151 (8 signals), page 152 (4 signals), page 153 (4 signals), page 154 (2 signals), page 155 (2 signals), page 180 (6 signals), page 181 (6 signals), page 186 (2 signals), page 187 (2 signals), page 188 (2 signals), page 189 (2 signals), page 190 (1 signals), page 192 (35 signals), page 194 (6 signals), page 196 (3 signals), page 197 (3 signals), page 202 (16 signals), page 203 (16 signals), page 204 (16 signals), page 205 (16 signals), page 206 (15 signals), page 207 (15 signals), page 208 (15 signals), page 209 (15 signals), page 210 (15 signals), page 221 (7 signals), page 224 (5 signals), page 225 (5 signals), page 226 (5 signals), page 227 (5 signals), page 228 (6 signals), page 229 (6 signals), page 230 (6 signals), page 231 (6 signals), page 232 (5 signals), page 233 (5 signals), page 234 (5 signals), page 235 (5 signals), page 236 (5 signals), page 237 (5 signals), page 238 (5 signals), page 239 (3 signals), page 240 (2 signals), page 241 (4 signals), page 242 (3 signals), page 243 (2 signals), page 244 (4 signals), page 245 (3 signals), page 246 (2 signals), page 247 (4 signals), page 248 (3 signals), page 249 (2 signals), page 250 (4 signals), page 251 (5 signals), page 252 (5 signals), page 253 (5 signals), page 254 (5 signals), page 263 (4 signals), page 264 (4 signals), page 265 (4 signals), page 266 (4 signals), page 267 (4 signals), page 268 (4 signals), page 269 (4 signals), page 270 (4 signals), page 272 (2 signals), page 273 (2 signals), page 274 (2 signals), page 275 (6 signals), page 282 (2 signals), page 283 (2 signals), page 290 (3 signals), page 291 (2 signals), page 292 (3 signals), page 293 (3 signals), page 294 (3 signals), page 295 (2 signals), page 296 (2 signals), page 297 (1 signals), page 302 (19 signals), page 303 (1 signals), page 306 (1 signals), page 307 (1 signals), page 308 (1 signals), page 309 (1 signals), page 310 (4 signals), page 311 (6 signals), page 312 (6 signals), page 313 (6 signals), page 314 (6 signals), page 315 (6 signals), page 316 (5 signals), page 318 (2 signals), page 319 (3 signals), page 324 (1 signals), page 325 (3 signals), page 326 (3 signals), page 327 (3 signals), page 328 (3 signals), page 330 (3 signals), page 331 (3 signals), page 334 (1 signals), page 335 (5 signals), page 341 (6 signals), page 342 (4 signals), page 345 (2 signals), page 346 (1 signals), page 348 (1 signals), page 349 (1 signals), page 350 (3 signals), page 352 (4 signals), page 353 (1 signals), page 354 (1 signals), page 355 (5 signals), page 357 (3 signals), page 373 (1 signals), page 374 (7 signals), page 375 (1 signals), page 376 (4 signals), page 380 (2 signals), page 391 (5 signals), page 395 (2 signals), page 396 (6 signals), page 397 (6 signals), page 398 (6 signals), page 399 (4 signals), page 401 (6 signals), page 402 (6 signals), page 403 (2 signals), page 404 (2 signals), page 405 (2 signals), page 406 (2 signals), page 407 (2 signals), page 409 (6 signals), page 410 (2 signals), page 411 (2 signals), page 412 (6 signals), page 413 (5 signals), page 414 (2 signals), page 415 (4 signals), page 417 (7 signals), page 419 (7 signals), page 420 (7 signals), page 421 (5 signals), page 422 (19 signals), page 424 (5 signals), page 425 (2 signals), page 426 (7 signals), page 427 (7 signals), page 428 (7 signals), page 429 (7 signals), page 430 (2 signals), page 431 (4 signals), page 444 (22 signals), page 447 (2 signals), page 448 (2 signals), page 453 (1 signals), page 455 (1 signals), page 466 (1 signals), page 469 (1 signals), page 472 (1 signals), page 475 (1 signals), page 480 (24 signals), page 482 (7 signals), page 485 (19 signals), page 489 (22 signals), page 493 (1 signals), page 494 (1 signals), page 497 (1 signals), page 500 (2 signals), page 510 (5 signals), page 513 (10 signals), page 517 (2 signals), page 518 (1 signals), page 520 (2 signals), page 523 (6 signals), page 525 (6 signals), page 536 (2 signals), page 545 (5 signals), page 551 (6 signals), page 555 (2 signals), page 560 (5 signals), page 563 (10 signals), page 567 (2 signals), page 568 (1 signals), page 570 (2 signals), page 571 (2 signals), page 572 (2 signals), page 573 (2 signals), page 577 (6 signals), page 578 (12 signals), page 579 (2 signals), page 580 (2 signals), page 581 (6 signals), page 582 (1 signals), page 585 (1 signals), page 586 (1 signals), page 587 (2 signals), page 590 (5 signals), page 591 (5 signals), page 592 (5 signals), page 593 (6 signals), page 594 (4 signals), page 595 (4 signals), page 596 (1 signals), page 597 (1 signals), page 599 (6 signals), page 605 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
