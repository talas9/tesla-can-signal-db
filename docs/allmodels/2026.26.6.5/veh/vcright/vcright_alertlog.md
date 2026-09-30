---
layout: default
title: "VCRIGHT_alertLog (0x550) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: alert log. Tesla Model 3 / Model Y CAN bus message VCRIGHT_alertLog (0x550) of Right body controller, firmware 2026.26.6.5, 1366 signals (VCRIGHT_alertID, VCRIGHT_alertState, VCRIGHT_a001_InternalWatchdog, VCRIGHT_a010_UnderVoltageDetected and 1362 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_alertLog (0x550) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Right body controller message: alert log; frame length observed on a vehicle bus. This page documents the 1366 signals of VCRIGHT_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_alertLog` |
| CAN id | 0x550 (1360) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1366 |

## Signals of VCRIGHT_alertLog

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_alertID` | selector | Right body controller: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>10 = `a010_ExtSupplyVoltError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>65 = `a065_emiosIsrRateLimitedDbg`<br>66 = `a066_emiosIsrShortPeriodDetectedDbg`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_ETC_MIA`<br>122 = `a122_ICR_MIA`<br>123 = `a123_VC_SECONDARY_LIGHTING_LEADER_MIA`<br>124 = `a124_BB_MIA`<br>125 = `a125_RCU_MIA`<br>126 = `a126_hvacActOpenLoadDBG`<br>127 = `a127_hvacActOvercurrentDBG`<br>128 = `a128_hvacActDrvFaultDBG`<br>129 = `a129_hvacIntakeUncalib`<br>130 = `a130_hvacLHBleedUncalib`<br>131 = `a131_hvacRHBleedUncalib`<br>132 = `a132_hvacLHVaneUncalib`<br>133 = `a133_hvacRHVaneUncalib`<br>134 = `a134_hvacUpprModeUncalib`<br>135 = `a135_hvacLowrModeUncalib`<br>136 = `a136_hvacIntakeFault`<br>137 = `a137_hvacLHBleedFault`<br>138 = `a138_hvacRHBleedFault`<br>139 = `a139_hvacLHVaneFault`<br>140 = `a140_hvacRHVaneFault`<br>141 = `a141_hvacUpperModeFault`<br>142 = `a142_hvacLowerModeFault`<br>143 = `a143_mirrorManuallyFolded`<br>144 = `a144_evaporatorTempSns`<br>145 = `a145_ductLeftTempSns`<br>146 = `a146_ductRightTempSns`<br>147 = `a147_incarProbeTempSns`<br>148 = `a148_incarMidTempSns`<br>149 = `a149_incarDeepTempSns`<br>150 = `a150_windowPinchFront`<br>151 = `a151_windowPinchRear`<br>152 = `a152_windowUncalFront`<br>153 = `a153_windowUncalRear`<br>154 = `a154_windowThermalFront`<br>155 = `a155_windowThermalRear`<br>156 = `a156_windowNoInputFront`<br>157 = `a157_windowNoInputRear`<br>158 = `a158_windowPinchOverideF`<br>159 = `a159_windowPinchOverideR`<br>160 = `a160_windowUndercurrentF`<br>161 = `a161_windowUndercurrentR`<br>162 = `a162_windowEncoderStallF`<br>163 = `a163_windowEncoderStallR`<br>164 = `a164_windowFactoryTest`<br>165 = `a165_windowFactoryTest2`<br>166 = `a166_windowDebug`<br>167 = `a167_windowDebugPinchF`<br>168 = `a168_windowDebugPinchR`<br>169 = `a169_windowCurrentPeakF`<br>170 = `a170_windowCurrentPeakR`<br>171 = `a171_hvacRearUncalib`<br>172 = `a172_SPI_MIA`<br>173 = `a173_windowBtnDoorOpen`<br>174 = `a174_BLERightPowerCycled`<br>175 = `a175_windowSealDefectFront`<br>176 = `a176_windowSealDefectRear`<br>177 = `a177_hvacRearFault`<br>178 = `a178_trunkSwitchVCBATTMIA`<br>179 = `a179_trunkSwitchVCFRONTMIA`<br>180 = `a180_frontDoorLatchRehome`<br>181 = `a181_rearDoorLatchRehome`<br>182 = `a182_emergencyLatchRel`<br>183 = `a183_doorStateFactoryTest`<br>184 = `a184_trunkFailedOpening`<br>185 = `a185_summonAborted`<br>186 = `a186_latchReleaseFailedF`<br>187 = `a187_latchReleaseFailedR`<br>188 = `a188_latchUnableToRearmF`<br>189 = `a189_latchUnableToRearmR`<br>190 = `a190_eFuseMgmtVbatFused`<br>191 = `a191_gloveboxPower`<br>192 = `a192_gloveboxLatchRel`<br>193 = `a193_amplifierEFuseFault`<br>194 = `a194_cntctrPwrEFuseFault`<br>195 = `a195_hvcEFuseFault`<br>196 = `a196_VEHCANOverterminate`<br>197 = `a197_VEHCANUndertrminate`<br>198 = `a198_PRVCANOverterminate`<br>199 = `a199_PRVCANUndertrminate`<br>200 = `a200_motorPhantomEncoder`<br>201 = `a201_motorDutyEncDisabl`<br>202 = `a202_epbmUnderIStatic`<br>203 = `a203_epbmOverIStatic`<br>204 = `a204_epbmUnderIDyn`<br>205 = `a205_epbmOverIDyn`<br>206 = `a206_epbWrongDirection`<br>207 = `a207_epbmEnableWrong`<br>208 = `a208_epbFaulted`<br>209 = `a209_epbStateMisTime`<br>210 = `a210_epbStateTime`<br>211 = `a211_epbmUnderIStaticNew`<br>212 = `a212_epbmOverIStaticNew`<br>213 = `a213_epbmUnderIDynNew`<br>214 = `a214_epbmOverIDynNew`<br>215 = `a215_currentDesyncWarning`<br>216 = `a216_SPI_MIA_debugData1`<br>217 = `a217_SPI_MIA_debugData2`<br>218 = `a218_motorDriverFault`<br>219 = `a219_motorCurrentDropout`<br>220 = `a220_reverseLightFaultUser`<br>221 = `a221_undervoltageLoadshedTriggered`<br>222 = `a222_rearFasciaFogLightFaultUser`<br>223 = `a223_VCBATT1_MIA`<br>224 = `a224_seatEncStallTrack`<br>225 = `a225_seatEncStallBack`<br>226 = `a226_seatEncStallTilt`<br>227 = `a227_seatEncStallLift`<br>228 = `a228_seatEncOverTrack`<br>229 = `a229_seatEncOverBack`<br>230 = `a230_seatEncOverTilt`<br>231 = `a231_seatEncOverLift`<br>232 = `a232_seatCurrUnderTrack`<br>233 = `a233_seatCurrUnderBack`<br>234 = `a234_seatCurrUnderTilt`<br>235 = `a235_seatCurrUnderLift`<br>236 = `a236_lumbarOverPresA`<br>237 = `a237_lumbarOverPresB`<br>238 = `a238_lumbarValveMIA`<br>239 = `a239_seatHeatIFront`<br>240 = `a240_seatHeatShortFront`<br>241 = `a241_seatHeatMIAFront`<br>242 = `a242_seatHeatIRearL`<br>243 = `a243_seatHeatShortRearL`<br>244 = `a244_seatHeatMIARearL`<br>245 = `a245_seatHeatIRearC`<br>246 = `a246_seatHeatShortRearC`<br>247 = `a247_seatHeatMIARearC`<br>248 = `a248_seatHeatIRearR`<br>249 = `a249_seatHeatShortRearR`<br>250 = `a250_seatHeatMIARearR`<br>251 = `a251_seatUncalTrack`<br>252 = `a252_seatUncalBack`<br>253 = `a253_seatUncalTilt`<br>254 = `a254_seatUncalLift`<br>255 = `a255_PTCOverTemp`<br>256 = `a256_PTCCurrentDrawNoReq`<br>257 = `a257_THSMIA`<br>258 = `a258_PTCStuckInBoot`<br>259 = `a259_latchDisarmDelayF`<br>260 = `a260_latchDisarmDelayR`<br>261 = `a261_emergencyLatchRelRear`<br>262 = `a262_PTCFaulted`<br>263 = `a263_seatTrackStallDebug`<br>264 = `a264_seatBackStallDebug`<br>265 = `a265_seatTiltStallDebug`<br>266 = `a266_seatLiftStallDebug`<br>267 = `a267_seatTrackHCEncStlDbg`<br>268 = `a268_seatBackHCEncStlDbg`<br>269 = `a269_seatTiltHCEncStlDbg`<br>270 = `a270_seatLiftHCEncStlDbg`<br>271 = `a271_THSSensorFault`<br>272 = `a272_vhclPwrStateMsmtch`<br>273 = `a273_handleStuckActiveF`<br>274 = `a274_handleStuckActiveR`<br>275 = `a275_rightTurnLightFault`<br>276 = `a276_mirrorDebug`<br>277 = `a277_BLERightUnderVoltage`<br>278 = `a278_hvacPtcHeatingUnavailable`<br>279 = `a279_trunkFailedToClose`<br>280 = `a280_latchDidNotDisarmF`<br>281 = `a281_latchDidNotDisarmR`<br>282 = `a282_latchUnexpectedArmF`<br>283 = `a283_latchUnexpectedArmR`<br>284 = `a284_gloveboxUnderCurrentDetected`<br>285 = `a285_gloveboxOverCurrentDetected`<br>286 = `a286_windowSpeedInvalidF`<br>287 = `a287_windowSpeedInvalidR`<br>288 = `a288_handlePWMPeriodF`<br>289 = `a289_handlePWMPeriodR`<br>290 = `a290_occupancyFaultedFront`<br>291 = `a291_buckleFaultedFront`<br>292 = `a292_buckleFaultedRearC`<br>293 = `a293_buckleFaultedRearR`<br>294 = `a294_occupancyFaultedRearR`<br>295 = `a295_occupancyFaulted3RowL`<br>296 = `a296_occupancyFaulted3RowR`<br>297 = `a297_seatBelowMinPumpTmp`<br>298 = `a298_buckleFaulted3RowL`<br>299 = `a299_buckleFaulted3RowR`<br>300 = `a300_VCFRONT1_MIA`<br>301 = `a301_airwaveRightVerticalWarning`<br>302 = `a302_airwaveRightVerticalUnavailable`<br>303 = `a303_eFuseMgmtWindowLift`<br>304 = `a304_frontIntHandleUnexpectedVoltage`<br>305 = `a305_rearIntHandleUnexpectedVoltage`<br>306 = `a306_handleDisconnectedF`<br>307 = `a307_handleDisconnectedR`<br>308 = `a308_airwaveRightLateralUnavailable`<br>310 = `a310_mirrorFoldStall`<br>311 = `a311_rightBrakeLightFault`<br>312 = `a312_rightTailLightFault`<br>313 = `a313_rightFootwellLightFault`<br>314 = `a314_rightMapPocketLightFault`<br>315 = `a315_rightInteriorTrunkLightFault`<br>316 = `a316_mirrorPrematureFoldStall`<br>317 = `a317_epbmLimpModeEnabled`<br>318 = `a318_leftExteriorTrunkLightFault`<br>319 = `a319_rightExteriorTrunkLightFault`<br>320 = `a320_windowReportCrackedAtTrimClear`<br>321 = `a321_windowRezeroedDebugF`<br>322 = `a322_windowRezeroedDebugR`<br>323 = `a323_mirrorCalibrated`<br>324 = `a324_mirrorHeatFault`<br>325 = `a325_airwaveLeftVerticalUnavailable`<br>326 = `a326_airwaveLeftLateralUnavailable`<br>327 = `a327_airwaveLeftLateralWarning`<br>328 = `a328_airwaveLeftVerticalWarning`<br>329 = `a329_airwaveRightLateralWarning`<br>330 = `a330_shortDropFailedF`<br>331 = `a331_shortDropFailedR`<br>336 = `a336_windowDropRevThermalF`<br>337 = `a337_windowDropRevThermalR`<br>342 = `a342_rearDefrostDisabled`<br>343 = `a343_rearDefrostUndercurrent`<br>344 = `a344_rearDefrostOvercurrent`<br>345 = `a345_HVACPTCHeaterPwrEFuseFault`<br>346 = `a346_cabinRadarEFuseFault`<br>347 = `a347_nonContMonitorClearedDBG`<br>352 = `a352_audioCurrentSpikeData`<br>355 = `a355_hvacLHBleedWarning`<br>356 = `a356_hvacRHBleedWarning`<br>357 = `a357_hvacLHVaneWarning`<br>358 = `a358_hvacRHVaneWarning`<br>359 = `a359_hvacUpperModeWarning`<br>360 = `a360_detectedStationaryWhileMoving`<br>361 = `a361_stationaryThresholdsIncorrect`<br>362 = `a362_movingThresholdsIncorrect`<br>363 = `a363_hvacLowerModeWarning`<br>364 = `a364_hvacIntakeWarning`<br>365 = `a365_pitchUnlatchDisabled`<br>366 = `a366_trunkLatchUnhomed`<br>367 = `a367_trunkLatchSwFault`<br>368 = `a368_ductLeftLowerTempSns`<br>369 = `a369_ductRightLowerTempSns`<br>370 = `a370_seat2RowPitchUnlatched`<br>371 = `a371_seat2RowTrackUnlatched`<br>372 = `a372_seat2RowBackrestUnlatched`<br>373 = `a373_windowSwOpenReqInDogMode`<br>375 = `a375_windowPinchOverrideNudge`<br>376 = `a376_seat2RowBridgeCurrentExceeded`<br>377 = `a377_ambientTempSns`<br>378 = `a378_ductLeftUpperTempSns`<br>379 = `a379_ductRightUpperTempSns`<br>380 = `a380_reverseLightFault`<br>381 = `a381_rearFogLightFault`<br>382 = `a382_leftLiftgateTailLightFault`<br>383 = `a383_hvacRearWarning`<br>385 = `a385_glareShieldHeaterUnavailable`<br>406 = `a406_aptivOCSMIA`<br>407 = `a407_aptivOCSInterfaceError`<br>408 = `a408_aptivOCSDeviceError`<br>409 = `a409_aptivOCSDeviceErrorDebug`<br>411 = `a411_undervoltageSelfTestFailure`<br>412 = `a412_rightBrakeTailLightFault`<br>413 = `a413_centerHighMountStopLightFault`<br>414 = `a414_rearFasciaReverseLightFault`<br>415 = `a415_rearFasciaFogLightFault`<br>416 = `a416_rearFasciaTailLightFault`<br>417 = `a417_rearFasciaLeftTurnLightFault`<br>418 = `a418_rearFasciaRightTurnLightFault`<br>419 = `a419_tailFasciaLeftLightFault`<br>420 = `a420_tailFasciaRightLightFault`<br>421 = `a421_leftTailLightFault`<br>422 = `a422_undervoltageSelfTestStuckOff`<br>426 = `a426_seatAbuseMotorWarn`<br>427 = `a427_seatAbuseMotorStop`<br>428 = `a428_seatAbuseBufferWarn`<br>429 = `a429_seatAbuseBufferFull`<br>444 = `a444_drv8703Fault`<br>445 = `a445_drv8703SpiFaultDBG`<br>446 = `a446_cabinHVACUnavailableContext`<br>448 = `a448_manualHVACAlert`<br>450 = `a450_ptcForcedOutOfSeqRod`<br>451 = `a451_ptcSeqRodOutOfRetries`<br>454 = `a454_ptcHeaterBadRodDetected`<br>482 = `a482_NCV77XXFault`<br>483 = `a483_rightTurnLightFaultUser`<br>484 = `a484_rightBrakeLightFaultUser`<br>485 = `a485_leftTailLightFaultUser`<br>486 = `a486_rightTailLightFaultUser`<br>487 = `a487_centerHighMountStopLightFaultUser`<br>488 = `a488_undervoltageSelfTestStuckOnDebug`<br>489 = `a489_undervoltageSelfTestStuckOn`<br>490 = `a490_vehicleOccupiedOnOTAStart`<br>491 = `a491_BPillarCameraHeaterFault`<br>492 = `a492_uvSelfTestLoadUnattemptedOnDbg`<br>496 = `a496_gloveboxOpenFailed`<br>497 = `a497_CANMsgMACVerificationKeyNotProvisioned`<br>498 = `a498_CANMsgMACVerificationFailure`<br>499 = `a499_epbmInvalidateCdp`<br>510 = `a510_3RowSeatUncalibrated`<br>511 = `a511_3RowSeatPositionNonsensical`<br>512 = `a512_3RowSeatAbsPosOffsetApplied`<br>513 = `a513_3RowSeatObstacleDetected`<br>514 = `a514_3RowSeatTempHigh`<br>515 = `a515_3RowSeatAbsPosSensorTransitionDbg`<br>516 = `a516_3RowSeatStatsFromLastStateDbg`<br>517 = `a517_3RowSeatRequestWhileUncalibrated`<br>518 = `a518_3RowSeatClashAvoidanceBlocked`<br>519 = `a519_3RowSeatOverfolded`<br>520 = `a520_configMismatch`<br>525 = `a525_LVBatterySWMisconfiguration`<br>526 = `a526_pcbaOverTemperature`<br>527 = `a527_continuousFeedUnexpectedVoltage`<br>528 = `a528_unableToRunStuckOnTest`<br>529 = `a529_airflowFeedBackModelError`<br>531 = `a531_airflowModelTmpCompDisabled`<br>532 = `a532_airflowModelFeedForwardError`<br>533 = `a533_cabinModelDebug`<br>537 = `a537_solarCalcsNotNominal`<br>538 = `a538_hvacSystemNotNominal`<br>539 = `a539_dogModeMonitorTrip`<br>540 = `a540_hvacActuatorDitherDebug`<br>542 = `a542_steeringWheelHeatingInhibited`<br>545 = `a545_LVBatteryTypeUnknown`<br>546 = `a546_mirrorFoldTypeChanged`<br>550 = `a550_ambientTempDelta`<br>551 = `a551_interiorDoorRequestInhibited`<br>555 = `a555_RCM2_MIA`<br>556 = `a556_rcmReportedOCSError`<br>560 = `a560_2RowSeatUncalibrated`<br>561 = `a561_2RowSeatPositionNonsensical`<br>562 = `a562_2RowSeatAbsPosOffsetApplied`<br>563 = `a563_2RowSeatObstacleDetected`<br>564 = `a564_2RowSeatTempHigh`<br>565 = `a565_2RowSeatAbsPosSensorTransitionDbg`<br>566 = `a566_2RowSeatStatsFromLastStateDbg`<br>567 = `a567_2RowSeatRequestWhileUncalibrated`<br>568 = `a568_2RowSeatClashAvoidanceBlocked`<br>569 = `a569_2RowSeatOverfolded`<br>570 = `a570_seatHeatDisabledF`<br>571 = `a571_seatHeatDisabledRearL`<br>572 = `a572_seatHeatDisabledRearC`<br>573 = `a573_seatHeatDisabledRearR`<br>574 = `a574_2RowSeatStatsFromLastStateDbg2`<br>575 = `a575_3RowSeatStatsFromLastStateDbg2`<br>577 = `a577_bsiHardwareIssue`<br>578 = `a578_RGBLightFault`<br>579 = `a579_liftgateFollowerUnexpectedStop`<br>580 = `a580_debugLiftgateFollowerCurrentSpike`<br>583 = `a583_doorRemoteUnlatchedFront`<br>584 = `a584_doorRemoteUnlatchedRear`<br>585 = `a585_doorRemoteUnlatchFailedFront`<br>586 = `a586_doorRemoteUnlatchFailedRear`<br>587 = `a587_VCSEAT2L_MIA`<br>588 = `a588_VCSEAT2R_MIA`<br>589 = `a589_defogSysDriverlessSelfTest`<br>590 = `a590_seatEncStallThighSupport`<br>591 = `a591_seatCurrUnderThighSupport`<br>592 = `a592_seatUncalThighSupport`<br>593 = `a593_seatEncOverThighSupport`<br>594 = `a594_seatThighSupportStallDebug`<br>595 = `a595_seatThighSupportHCEncStlDbg`<br>596 = `a596_frontDoorLatchUnexpectedVoltage`<br>597 = `a597_rearDoorLatchUnexpectedVoltage`<br>598 = `a598_childModeMonitorTrip`<br>599 = `a599_LVBatteryTypeUnsupported`<br>601 = `a601_wakeToOpenDoorDbg`<br>605 = `a605_CANMsgMACVerificationKeyMismatch`<br>617 = `a617_APP_MIA` | plausible |
| `VCRIGHT_alertState` |  | Right body controller: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCRIGHT_a001_InternalWatchdog` | page 1 | Right body controller: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a010_UnderVoltageDetected` | page 10 | Right body controller: a010 under voltage detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a010_UnderVoltageTimeout` | page 10 | Right body controller: a010 under voltage timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a015_NVMMMemOverflow` | page 15 | Right body controller: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a015_NVMMFilesystemError` | page 15 | Right body controller: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a015_NVMMRecordIDError` | page 15 | Right body controller: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a057_VEH_cpControl` | page 57 | Right body controller: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a059_voltageDrop` | page 59 | Right body controller: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCRIGHT_a059_resistanceEstimate` | page 59 | Right body controller: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCRIGHT_a059_current` | page 59 | Right body controller: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCRIGHT_a063_switchChannel` | page 63 | Right body controller: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a063_switchType` | page 63 | Right body controller: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a063_ADCVoltage` | page 63 | Right body controller: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCRIGHT_a063_disconnected` | page 63 | Right body controller: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a063_indeterminate` | page 63 | Right body controller: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a063_stuckActive` | page 63 | Right body controller: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a063_faulted` | page 63 | Right body controller: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a082_RIPC_epbPrivateState` | page 82 | Right body controller: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a082_RIPC_remoteHSD` | page 82 | Right body controller: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a082_RIPC_railStatus` | page 82 | Right body controller: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a082_RIPC_remoteMux` | page 82 | Right body controller: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a083_LIPC_epbPrivateState` | page 83 | Right body controller: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a083_LIPC_remoteHSD` | page 83 | Right body controller: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a083_LIPC_railStatus` | page 83 | Right body controller: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a083_LIPC_HSDFaults` | page 83 | Right body controller: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a084_CH_StatusC` | page 84 | Right body controller: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a085_PARTY_buttonStatus` | page 85 | Right body controller: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_LVBMS_statusHigh` | page 86 | Right body controller: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_LVBMS_statusLow` | page 86 | Right body controller: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_status` | page 86 | Right body controller: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_12VBatteryStatus` | page 86 | Right body controller: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_LVPowerState` | page 86 | Right body controller: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_lightStatus` | page 86 | Right body controller: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_systemStatus` | page 86 | Right body controller: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_thermalStatus` | page 86 | Right body controller: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_vehNm` | page 86 | Right body controller: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_BDY_LVSelfTests` | page 86 | Right body controller: a086 BDY LV self tests | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_LVSelfTests` | page 86 | Right body controller: a086 VEH LV self tests | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_VEH_LVHealth` | page 86 | Right body controller: a086 VEH LV health | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a086_BDY_12VBatteryStatus` | page 86 | Right body controller: a086 BDY 12 v battery status | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_VEH_temperature` | page 87 | Right body controller: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_VEH_thermalControl` | page 87 | Right body controller: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_VEH_torque` | page 87 | Right body controller: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_VEH_status` | page 87 | Right body controller: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_PARTY_torque` | page 87 | Right body controller: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_PARTY_status` | page 87 | Right body controller: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_PARTY_temperature` | page 87 | Right body controller: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_PARTY_thermalControl` | page 87 | Right body controller: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a087_VEH_motorStatus` | page 87 | Right body controller: a087 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_VEH_temperature` | page 88 | Right body controller: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_VEH_thermalControl` | page 88 | Right body controller: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_VEH_torque` | page 88 | Right body controller: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_VEH_status` | page 88 | Right body controller: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_PARTY_torque` | page 88 | Right body controller: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_PARTY_status` | page 88 | Right body controller: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_PARTY_temperature` | page 88 | Right body controller: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_PARTY_thermalControl` | page 88 | Right body controller: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a088_VEH_motorStatus` | page 88 | Right body controller: a088 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_PARTY_party1` | page 89 | Right body controller: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_PARTY_status` | page 89 | Right body controller: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_VEH_status` | page 89 | Right body controller: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_BDY_party1` | page 89 | Right body controller: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_BDY_status` | page 89 | Right body controller: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_CH_status` | page 89 | Right body controller: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_CH_party1` | page 89 | Right body controller: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_CH_party3` | page 89 | Right body controller: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_VEH_party1` | page 89 | Right body controller: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a089_VEH_party3` | page 89 | Right body controller: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a091_VEH_faultsAndExtras` | page 91 | Right body controller: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a091_VEH_info` | page 91 | Right body controller: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a091_VEH_state` | page 91 | Right body controller: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a092_VEH_restraintStatus` | page 92 | Right body controller: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a092_VEH_switchStatus` | page 92 | Right body controller: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a092_VEH_seatStatus2` | page 92 | Right body controller: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a092_VEH_vehNm` | page 92 | Right body controller: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a093_VEH_restraintStatus` | page 93 | Right body controller: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a093_VEH_switchStatus` | page 93 | Right body controller: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a093_VEH_seatStatus2` | page 93 | Right body controller: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a093_VEH_vehNm` | page 93 | Right body controller: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a094_VEH_sysStatus` | page 94 | Right body controller: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a094_PARTY_sysStatus` | page 94 | Right body controller: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a094_CH_sysStatus` | page 94 | Right body controller: a094 CH sys status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a095_PT_ptNm` | page 95 | Right body controller: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a095_PT_status` | page 95 | Right body controller: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a096_VEH_status` | page 96 | Right body controller: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a096_CH_status` | page 96 | Right body controller: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a097_VEH_HVStatus` | page 97 | Right body controller: a097 VEH HV status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a097_VEH_state` | page 97 | Right body controller: a097 VEH state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_CH_torque` | page 98 | Right body controller: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_hvStatus` | page 98 | Right body controller: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_status` | page 98 | Right body controller: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_thermalControl` | page 98 | Right body controller: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_temperature` | page 98 | Right body controller: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_torque` | page 98 | Right body controller: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PARTY_status` | page 98 | Right body controller: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PARTY_temperature` | page 98 | Right body controller: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PARTY_thermalControl` | page 98 | Right body controller: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PARTY_torque` | page 98 | Right body controller: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PT_thermalControl` | page 98 | Right body controller: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PT_temperature` | page 98 | Right body controller: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_PARTY_motorStatus` | page 98 | Right body controller: a098 PARTY motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a098_VEH_motorStatus` | page 98 | Right body controller: a098 VEH motor status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a099_VEH_oocStatus` | page 99 | Right body controller: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a100_VEH` | page 100 | Right body controller: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a100_PARTY` | page 100 | Right body controller: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a100_PT` | page 100 | Right body controller: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a100_CH` | page 100 | Right body controller: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a100_OBD` | page 100 | Right body controller: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a101_VEH_state` | page 101 | Right body controller: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a101_PARTY_locState` | page 101 | Right body controller: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a101_LIPC_externalWatchdogHeartBeat` | page 101 | Right body controller: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a101_VEH_locState` | page 101 | Right body controller: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a101_BDY_locState` | page 101 | Right body controller: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a102_VEH_faultsAndExtras` | page 102 | Right body controller: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a102_VEH_feedbackStatus` | page 102 | Right body controller: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a102_VEH_sensorStatus` | page 102 | Right body controller: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a102_VEH_rods` | page 102 | Right body controller: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_VEH_hvsNm` | page 103 | Right body controller: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_VEH_vehNm` | page 103 | Right body controller: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_VEH_status` | page 103 | Right body controller: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_PT_ptNm` | page 103 | Right body controller: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_PT_status` | page 103 | Right body controller: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a103_VEH_evseStatus` | page 103 | Right body controller: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a105_VEH_states` | page 105 | Right body controller: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a105_VEH_chNm` | page 105 | Right body controller: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a105_VEH_dampingStates` | page 105 | Right body controller: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a106_VEH_dcdcStatus` | page 106 | Right body controller: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a106_VEH_thermalControl` | page 106 | Right body controller: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a106_VEH_dcdcRailStatus` | page 106 | Right body controller: a106 VEH dcdc rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a106_CH_dcdcRailStatus` | page 106 | Right body controller: a106 CH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a106_CH_alertMatrix` | page 106 | Right body controller: a106 CH alert matrix | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_hvsNm` | page 107 | Right body controller: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_vehNm` | page 107 | Right body controller: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_status` | page 107 | Right body controller: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_thermalStatus` | page 107 | Right body controller: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_bmbMinMax` | page 107 | Right body controller: a107 VEH bmb min max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_powerAvailable` | page 107 | Right body controller: a107 VEH power available | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_PT_ptNm` | page 107 | Right body controller: a107 PT pt nm | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_PT_status` | page 107 | Right body controller: a107 PT status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_PT_thermalStatus` | page 107 | Right body controller: a107 PT thermal status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_PT_socStatus` | page 107 | Right body controller: a107 PT soc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_socStatus` | page 107 | Right body controller: a107 VEH soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_packConfig` | page 107 | Right body controller: a107 VEH pack config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_energyStatus` | page 107 | Right body controller: a107 VEH energy status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a107_VEH_chargeInfo` | page 107 | Right body controller: a107 VEH charge info | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_hvStatus` | page 108 | Right body controller: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_temperature` | page 108 | Right body controller: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_thermalControl` | page 108 | Right body controller: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_torque` | page 108 | Right body controller: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_status` | page 108 | Right body controller: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PARTY_torque` | page 108 | Right body controller: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PARTY_status` | page 108 | Right body controller: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PARTY_temperature` | page 108 | Right body controller: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PARTY_thermalControl` | page 108 | Right body controller: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PT_temperature` | page 108 | Right body controller: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PT_thermalControl` | page 108 | Right body controller: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_PARTY_motorStatus` | page 108 | Right body controller: a108 PARTY motor status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_VEH_motorStatus` | page 108 | Right body controller: a108 VEH motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a108_CH_torque` | page 108 | Right body controller: a108 CH torque | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_carState` | page 110 | Right body controller: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_carConfig` | page 110 | Right body controller: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_time` | page 110 | Right body controller: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_updateStatus` | page 110 | Right body controller: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_vehNm` | page 110 | Right body controller: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_mismatchFault` | page 110 | Right body controller: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_vin` | page 110 | Right body controller: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_bmpDebug` | page 110 | Right body controller: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_gearControl` | page 110 | Right body controller: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_VEH_canLogAvailability` | page 110 | Right body controller: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_airbagCutoffStatus` | page 110 | Right body controller: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_carConfig` | page 110 | Right body controller: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_carState` | page 110 | Right body controller: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_vin` | page 110 | Right body controller: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_chNm` | page 110 | Right body controller: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_CH_epochTimeGtw` | page 110 | Right body controller: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a110_PARTY_carConfig` | page 110 | Right body controller: a110 PARTY car config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_VEH_internalStatus` | page 111 | Right body controller: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_VEH_status` | page 111 | Right body controller: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_VEH_vehNm` | page 111 | Right body controller: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_RIPC_LVPowerState` | page 111 | Right body controller: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_RIPC_epbPrivateState` | page 111 | Right body controller: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_RIPC_railStatus` | page 111 | Right body controller: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_RIPC_remoteADC` | page 111 | Right body controller: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_RIPC_switchStatus` | page 111 | Right body controller: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_VEH_LVPowerState` | page 111 | Right body controller: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_VEH_seatStatus` | page 111 | Right body controller: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_PARTY_status` | page 111 | Right body controller: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a111_CH_status` | page 111 | Right body controller: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_VEH_internalStatus` | page 112 | Right body controller: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_VEH_status` | page 112 | Right body controller: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_VEH_vehNm` | page 112 | Right body controller: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_LIPC_LVPowerState` | page 112 | Right body controller: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_LIPC_epbPrivateState` | page 112 | Right body controller: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_LIPC_railStatus` | page 112 | Right body controller: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_LIPC_remoteADC` | page 112 | Right body controller: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_LIPC_switchStatus` | page 112 | Right body controller: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_VEH_LVPowerState` | page 112 | Right body controller: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_PARTY_status` | page 112 | Right body controller: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a112_CH_status` | page 112 | Right body controller: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_status` | page 114 | Right body controller: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_wheelSpeeds` | page 114 | Right body controller: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_VEH_wheelSpeeds` | page 114 | Right body controller: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_CH_wheelSpeeds` | page 114 | Right body controller: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_party3` | page 114 | Right body controller: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_VEH_party3` | page 114 | Right body controller: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_VEH_status` | page 114 | Right body controller: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_wheelRotation` | page 114 | Right body controller: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_CH_wheelRotation` | page 114 | Right body controller: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_VEH_wheelRotation` | page 114 | Right body controller: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_brakeTorque` | page 114 | Right body controller: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_PARTY_offsets` | page 114 | Right body controller: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_BDY_offsets` | page 114 | Right body controller: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_BDY_party3` | page 114 | Right body controller: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_BDY_status` | page 114 | Right body controller: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_BDY_wheelRotation` | page 114 | Right body controller: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_BDY_wheelSpeeds` | page 114 | Right body controller: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_CH_party1` | page 114 | Right body controller: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_CH_party3` | page 114 | Right body controller: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a114_CH_status` | page 114 | Right body controller: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_vehNm` | page 115 | Right body controller: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_authentication` | page 115 | Right body controller: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_BLEResetRequest` | page 115 | Right body controller: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_requests` | page 115 | Right body controller: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_requests2` | page 115 | Right body controller: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_REM_authentication` | page 115 | Right body controller: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_UI_corianderVehicleControl` | page 115 | Right body controller: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_CH_TPMSDisplay` | page 115 | Right body controller: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_RSSI` | page 115 | Right body controller: a115 VEH RSSI | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_authenticationWithMac` | page 115 | Right body controller: a115 VEH authentication with mac | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_endpointTemp` | page 115 | Right body controller: a115 VEH endpoint temp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_VEH_ChildSeatStatus` | page 115 | Right body controller: a115 VEH child seat status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_ChildSeatStatus` | page 115 | Right body controller: a115 BDY child seat status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_endpointTemp` | page 115 | Right body controller: a115 BDY endpoint temp | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_BLEResetRequest` | page 115 | Right body controller: a115 BDY BLE reset request | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_RSSI` | page 115 | Right body controller: a115 BDY RSSI | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_authentication` | page 115 | Right body controller: a115 BDY authentication | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_requests` | page 115 | Right body controller: a115 BDY requests | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_requests2` | page 115 | Right body controller: a115 BDY requests2 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_vehNm` | page 115 | Right body controller: a115 BDY veh nm | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a115_BDY_authenticationWithMac` | page 115 | Right body controller: a115 BDY authentication with mac | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_PARTY_epbmStatus` | page 116 | Right body controller: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_vehNm` | page 116 | Right body controller: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_hvacRequest` | page 116 | Right body controller: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_hvacStatus` | page 116 | Right body controller: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_LVPowerState` | page 116 | Right body controller: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_lightStatus` | page 116 | Right body controller: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_seatStatus` | page 116 | Right body controller: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_thsStatus` | page 116 | Right body controller: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_doorStatus` | page 116 | Right body controller: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_seatHeatStatus` | page 116 | Right body controller: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_restraintStatus` | page 116 | Right body controller: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_switchStatus` | page 116 | Right body controller: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_logging1Hz` | page 116 | Right body controller: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_seatStatus2` | page 116 | Right body controller: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_status` | page 116 | Right body controller: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_thermalCommand` | page 116 | Right body controller: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_VEH_windowStatus` | page 116 | Right body controller: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_PARTY_restraintStatus` | page 116 | Right body controller: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_PARTY_doorStatus` | page 116 | Right body controller: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_BDY_epbmStatus` | page 116 | Right body controller: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_BDY_restraintStatus` | page 116 | Right body controller: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a116_BDY_switchStatus` | page 116 | Right body controller: a116 BDY switch status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_epbmStatus` | page 117 | Right body controller: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_restraintStatus` | page 117 | Right body controller: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_prndStatus` | page 117 | Right body controller: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_PARTY_epbmStatus` | page 117 | Right body controller: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_vehNm` | page 117 | Right body controller: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_hvacBlowerFdb` | page 117 | Right body controller: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_LVPowerState` | page 117 | Right body controller: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_restraintStatus` | page 117 | Right body controller: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_lightStatus` | page 117 | Right body controller: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_seatStatus` | page 117 | Right body controller: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_falconSwitchStatus` | page 117 | Right body controller: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_doorStatus` | page 117 | Right body controller: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_doorStatus2` | page 117 | Right body controller: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_windowStatus` | page 117 | Right body controller: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_switchStatus` | page 117 | Right body controller: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_intrusionSensorStatus` | page 117 | Right body controller: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_liftgateStatus` | page 117 | Right body controller: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_seatStatus2` | page 117 | Right body controller: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_PARTY_restraintStatus` | page 117 | Right body controller: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_thermalStatus` | page 117 | Right body controller: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_PARTY_doorStatus` | page 117 | Right body controller: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_status` | page 117 | Right body controller: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_PARTY_prndStatus` | page 117 | Right body controller: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_PARTY_lightingSecondary` | page 117 | Right body controller: a117 PARTY lighting secondary | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_lightingSecondary` | page 117 | Right body controller: a117 BDY lighting secondary | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_hvacBlowerFdb` | page 117 | Right body controller: a117 BDY hvac blower fdb | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_thermalStatus` | page 117 | Right body controller: a117 BDY thermal status | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_BDY_status` | page 117 | Right body controller: a117 BDY status | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a117_VEH_liftgateLeaderRequest` | page 117 | Right body controller: a117 VEH liftgate leader request | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_vehNm` | page 118 | Right body controller: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_lighting` | page 118 | Right body controller: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_sensors` | page 118 | Right body controller: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_status` | page 118 | Right body controller: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_okToUseHighPwr` | page 118 | Right body controller: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_LVPowerState` | page 118 | Right body controller: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_coolant` | page 118 | Right body controller: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_vehicleStatus` | page 118 | Right body controller: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_12VBatteryStatus` | page 118 | Right body controller: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_systemStatus` | page 118 | Right body controller: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_LVPowerState` | page 118 | Right body controller: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_outputPowerStatus` | page 118 | Right body controller: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_vehicleTime` | page 118 | Right body controller: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_thermalCommand` | page 118 | Right body controller: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_LVPowerState` | page 118 | Right body controller: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_sensors` | page 118 | Right body controller: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_sensors` | page 118 | Right body controller: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_interNodeResistance` | page 118 | Right body controller: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_lighting` | page 118 | Right body controller: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_lightStatus` | page 118 | Right body controller: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_vehNm` | page 118 | Right body controller: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_12VBatteryStatus` | page 118 | Right body controller: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_LVBMS_statusHigh` | page 118 | Right body controller: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_CH_alertMatrix` | page 118 | Right body controller: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_BDY_outputPowerStatus` | page 118 | Right body controller: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_BDY_vehicleTime` | page 118 | Right body controller: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | Right body controller: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | Right body controller: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_PARTY_VCFRONT_cameraCleaningStatus` | page 118 | Right body controller: a118 PARTY VCFRONT camera cleaning status | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_VEH_LVHealth` | page 118 | Right body controller: a118 VEH LV health | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a118_BDY_LVHealth` | page 118 | Right body controller: a118 BDY LV health | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_VEH_steerAngle` | page 119 | Right body controller: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_VEH_leftStalk` | page 119 | Right body controller: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_VEH_rightStalk` | page 119 | Right body controller: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_PARTY_rightStalk` | page 119 | Right body controller: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_CH_steerAngle` | page 119 | Right body controller: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a119_PARTY_steerAngle` | page 119 | Right body controller: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_chassisCntl` | page 120 | Right body controller: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_systemStatus` | page 120 | Right body controller: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_CH_chassisCntl` | page 120 | Right body controller: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_systemStatus` | page 120 | Right body controller: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_torque` | page 120 | Right body controller: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_torque` | page 120 | Right body controller: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_locStatus` | page 120 | Right body controller: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_speed` | page 120 | Right body controller: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_speed` | page 120 | Right body controller: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_status` | page 120 | Right body controller: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PT_speed` | page 120 | Right body controller: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PT_systemStatus` | page 120 | Right body controller: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_vehicleEstimates` | page 120 | Right body controller: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_aggregatedAxleSpeed` | page 120 | Right body controller: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_aggregatedAxleSpeed` | page 120 | Right body controller: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_systemPower` | page 120 | Right body controller: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_autonomyHealth` | page 120 | Right body controller: a120 PARTY autonomy health | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_autonomyHealth` | page 120 | Right body controller: a120 VEH autonomy health | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PT_systemPower` | page 120 | Right body controller: a120 PT system power | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_stalklessInterfaces` | page 120 | Right body controller: a120 PARTY stalkless interfaces | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_CH_speed` | page 120 | Right body controller: a120 CH speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_estimatedBrakeTemp` | page 120 | Right body controller: a120 VEH estimated brake temp | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_prndControl` | page 120 | Right body controller: a120 PARTY prnd control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_locStatus2` | page 120 | Right body controller: a120 PARTY loc status2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_chassisCntl` | page 120 | Right body controller: a120 VEH chassis cntl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_CH_locStatus2` | page 120 | Right body controller: a120 CH loc status2 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_locStatus` | page 120 | Right body controller: a120 VEH loc status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_locStatus2` | page 120 | Right body controller: a120 VEH loc status2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_prndControl` | page 120 | Right body controller: a120 VEH prnd control | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_vehicleEstimates` | page 120 | Right body controller: a120 VEH vehicle estimates | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_PARTY_motorStatus` | page 120 | Right body controller: a120 PARTY motor status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_VEH_motorStatus` | page 120 | Right body controller: a120 VEH motor status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a120_BDY_speed` | page 120 | Right body controller: a120 BDY speed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a121_OBD_status` | page 121 | Right body controller: a121 OBD status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a124_PARTY_status` | page 124 | Right body controller: a124 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a124_BDY_status` | page 124 | Right body controller: a124 BDY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a124_VEH_status` | page 124 | Right body controller: a124 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a125_PARTY_actuation` | page 125 | Right body controller: a125 PARTY actuation | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a125_BDY_actuation` | page 125 | Right body controller: a125 BDY actuation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a125_PARTY_status` | page 125 | Right body controller: a125 PARTY status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a125_BDY_status` | page 125 | Right body controller: a125 BDY status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a136_hvacIntakeStall` | page 136 | Right body controller: a136 hvac intake stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a137_hvacLHBleedStall` | page 137 | Right body controller: a137 hvac LH bleed stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a138_hvacRHBleedStall` | page 138 | Right body controller: a138 hvac RH bleed stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a139_hvacLHVaneStall` | page 139 | Right body controller: a139 hvac LH vane stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a140_hvacRHVaneStall` | page 140 | Right body controller: a140 hvac RH vane stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a141_hvacUpperModeStall` | page 141 | Right body controller: a141 hvac upper mode stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a142_hvacLowerModeStall` | page 142 | Right body controller: a142 hvac lower mode stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a144_snsShortCircuit` | page 144 | Right body controller: a144 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a144_snsDisconnect` | page 144 | Right body controller: a144 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a144_snsRateChangeUp` | page 144 | Right body controller: a144 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a144_snsRateChangeDown` | page 144 | Right body controller: a144 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a145_snsShortCircuit` | page 145 | Right body controller: a145 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a145_snsDisconnect` | page 145 | Right body controller: a145 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a145_snsRateChangeUp` | page 145 | Right body controller: a145 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a145_snsRateChangeDown` | page 145 | Right body controller: a145 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a146_snsShortCircuit` | page 146 | Right body controller: a146 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a146_snsDisconnect` | page 146 | Right body controller: a146 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a146_snsRateChangeUp` | page 146 | Right body controller: a146 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a146_snsRateChangeDown` | page 146 | Right body controller: a146 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a147_snsShortCircuit` | page 147 | Right body controller: a147 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a147_snsDisconnect` | page 147 | Right body controller: a147 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a147_snsRateChangeUp` | page 147 | Right body controller: a147 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a147_snsRateChangeDown` | page 147 | Right body controller: a147 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a148_snsShortCircuit` | page 148 | Right body controller: a148 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a148_snsDisconnect` | page 148 | Right body controller: a148 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a148_snsRateChangeUp` | page 148 | Right body controller: a148 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a148_snsRateChangeDown` | page 148 | Right body controller: a148 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a149_snsShortCircuit` | page 149 | Right body controller: a149 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a149_snsDisconnect` | page 149 | Right body controller: a149 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a149_snsRateChangeUp` | page 149 | Right body controller: a149 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a149_snsRateChangeDown` | page 149 | Right body controller: a149 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a150_windowPosition` | page 150 | Right body controller: a150 window position | 16\|9 | little-endian | signed | 1.43137252331 | 197.529418945 | mm | -168.901947022 to 562.529412389 |  | plausible |
| `VCRIGHT_a150_movementTimeMs` | page 150 | Right body controller: a150 movement time ms | 25\|7 | little-endian | unsigned | 50 | 0 | ms | 0 to 6350 |  | plausible |
| `VCRIGHT_a150_windowPinchReason` | page 150 | Right body controller: a150 window pinch reason | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `POWER`<br>2 = `POWER_DIV_SPEED`<br>3 = `POWER_CRUDE`<br>4 = `ACCEL_LOOKBACK`<br>5 = `UNUSED` | plausible |
| `VCRIGHT_a150_lookbackIndex` | page 150 | Right body controller: a150 lookback index | 35\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a150_absAccelExceedance` | page 150 | Right body controller: a150 abs accel exceedance | 41\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCRIGHT_a150_relAccelExceedance` | page 150 | Right body controller: a150 rel accel exceedance | 49\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCRIGHT_a150_speedExpScore` | page 150 | Right body controller: a150 speed exp score | 57\|6 | little-endian | signed | 0.0006451613 | -0.009677419 | - | -0.0303225806 to 0.0103225813 |  | plausible |
| `VCRIGHT_a150_treatedInGear` | page 150 | Right body controller: a150 treated in gear | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a151_windowPosition` | page 151 | Right body controller: a151 window position | 16\|9 | little-endian | signed | 1.43137252331 | 197.529418945 | mm | -168.901947022 to 562.529412389 |  | plausible |
| `VCRIGHT_a151_movementTimeMs` | page 151 | Right body controller: a151 movement time ms | 25\|7 | little-endian | unsigned | 50 | 0 | ms | 0 to 6350 |  | plausible |
| `VCRIGHT_a151_windowPinchReason` | page 151 | Right body controller: a151 window pinch reason | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `POWER`<br>2 = `POWER_DIV_SPEED`<br>3 = `POWER_CRUDE`<br>4 = `ACCEL_LOOKBACK`<br>5 = `UNUSED` | plausible |
| `VCRIGHT_a151_lookbackIndex` | page 151 | Right body controller: a151 lookback index | 35\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a151_absAccelExceedance` | page 151 | Right body controller: a151 abs accel exceedance | 41\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCRIGHT_a151_relAccelExceedance` | page 151 | Right body controller: a151 rel accel exceedance | 49\|8 | little-endian | unsigned | 0.09803922 | 0 | % | 0 to 25.0000011 |  | plausible |
| `VCRIGHT_a151_speedExpScore` | page 151 | Right body controller: a151 speed exp score | 57\|6 | little-endian | signed | 0.0006451613 | -0.009677419 | - | -0.0303225806 to 0.0103225813 |  | plausible |
| `VCRIGHT_a151_treatedInGear` | page 151 | Right body controller: a151 treated in gear | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a152_zeroed` | page 152 | Right body controller: a152 zeroed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a152_endStopTrusted` | page 152 | Right body controller: a152 end stop trusted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a152_speedTableStatus` | page 152 | Right body controller: a152 speed table status; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `EMPTY_SNA`<br>1 = `SENSITIVE_BUILT`<br>2 = `FULLY_BUILT` | plausible |
| `VCRIGHT_a152_causedByBackoffs` | page 152 | Right body controller: a152 caused by backoffs | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a153_zeroed` | page 153 | Right body controller: a153 zeroed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a153_endStopTrusted` | page 153 | Right body controller: a153 end stop trusted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a153_speedTableStatus` | page 153 | Right body controller: a153 speed table status; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `EMPTY_SNA`<br>1 = `SENSITIVE_BUILT`<br>2 = `FULLY_BUILT` | plausible |
| `VCRIGHT_a153_causedByBackoffs` | page 153 | Right body controller: a153 caused by backoffs | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a154_windowThermalMode` | page 154 | Right body controller: a154 window thermal mode; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NORMAL`<br>2 = `ALERT`<br>3 = `CRITICAL` | plausible |
| `VCRIGHT_a154_lightShowActive` | page 154 | Right body controller: a154 light show active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a155_windowThermalMode` | page 155 | Right body controller: a155 window thermal mode; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NORMAL`<br>2 = `ALERT`<br>3 = `CRITICAL` | plausible |
| `VCRIGHT_a155_lightShowActive` | page 155 | Right body controller: a155 light show active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a177_hvacRearStall` | page 177 | Right body controller: a177 hvac rear stall | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a180_intButtonPressed` | page 180 | Right body controller: a180 int button pressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a180_extHandlePWM` | page 180 | Right body controller: a180 ext handle PWM | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCRIGHT_a180_extHandlePulled` | page 180 | Right body controller: a180 ext handle pulled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a180_releasePWM` | page 180 | Right body controller: a180 release PWM | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCRIGHT_a180_latchStatus` | page 180 | Right body controller: a180 latch status; raw 0 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCRIGHT_a180_latchClawStatus` | page 180 | Right body controller: a180 latch claw status | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a181_intButtonPressed` | page 181 | Right body controller: a181 int button pressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a181_extHandlePWM` | page 181 | Right body controller: a181 ext handle PWM | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCRIGHT_a181_extHandlePulled` | page 181 | Right body controller: a181 ext handle pulled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a181_releasePWM` | page 181 | Right body controller: a181 release PWM | 40\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCRIGHT_a181_latchStatus` | page 181 | Right body controller: a181 latch status; raw 0 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCRIGHT_a181_latchClawStatus` | page 181 | Right body controller: a181 latch claw status | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a184_voltage` | page 184 | Right body controller: a184 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a184_temperature` | page 184 | Right body controller: a184 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a184_trunkCurrent` | page 184 | Right body controller: a184 trunk current | 32\|8 | little-endian | unsigned | 0.05 | 0 | A | 0 to 12.75 |  | plausible |
| `VCRIGHT_a186_voltage` | page 186 | Right body controller: a186 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a186_temperature` | page 186 | Right body controller: a186 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a187_voltage` | page 187 | Right body controller: a187 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a187_temperature` | page 187 | Right body controller: a187 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a188_voltage` | page 188 | Right body controller: a188 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a188_temperature` | page 188 | Right body controller: a188 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a189_voltage` | page 189 | Right body controller: a189 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a189_temperature` | page 189 | Right body controller: a189 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a190_eFuseTripCount` | page 190 | Right body controller: a190 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a193_amplifierCurrent` | page 193 | Right body controller: a193 amplifier current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCRIGHT_a194_cntctrPwrCurrent` | page 194 | Right body controller: a194 cntctr pwr current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCRIGHT_a195_hvcCurrent` | page 195 | Right body controller: a195 hvc current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCRIGHT_a196_outputState` | page 196 | Right body controller: a196 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a196_NVRAMState` | page 196 | Right body controller: a196 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a196_lockoutState` | page 196 | Right body controller: a196 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a197_outputState` | page 197 | Right body controller: a197 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a197_NVRAMState` | page 197 | Right body controller: a197 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a197_lockoutState` | page 197 | Right body controller: a197 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a198_outputState` | page 198 | Right body controller: a198 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a198_NVRAMState` | page 198 | Right body controller: a198 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a198_lockoutState` | page 198 | Right body controller: a198 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a199_outputState` | page 199 | Right body controller: a199 output state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a199_NVRAMState` | page 199 | Right body controller: a199 NVRAM state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a199_lockoutState` | page 199 | Right body controller: a199 lockout state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_unknownAllowed` | page 202 | Right body controller: a202 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_openAllowed` | page 202 | Right body controller: a202 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_dynamicAllowed` | page 202 | Right body controller: a202 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_parkAllowed` | page 202 | Right body controller: a202 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_startAllowed` | page 202 | Right body controller: a202 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_serviceAllowed` | page 202 | Right body controller: a202 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_winchAllowed` | page 202 | Right body controller: a202 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_winchReleaseAllowed` | page 202 | Right body controller: a202 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_parkingAllowed` | page 202 | Right body controller: a202 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_dynApplyAllowed` | page 202 | Right body controller: a202 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_releaseAllowed` | page 202 | Right body controller: a202 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_parkPendingAllowed` | page 202 | Right body controller: a202 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_wenchPendingAllowed` | page 202 | Right body controller: a202 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a202_desyncCount` | page 202 | Right body controller: a202 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a202_current` | page 202 | Right body controller: a202 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCRIGHT_a202_epbConfig` | page 202 | Right body controller: a202 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a203_unknownAllowed` | page 203 | Right body controller: a203 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_openAllowed` | page 203 | Right body controller: a203 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_dynamicAllowed` | page 203 | Right body controller: a203 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_parkAllowed` | page 203 | Right body controller: a203 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_startAllowed` | page 203 | Right body controller: a203 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_serviceAllowed` | page 203 | Right body controller: a203 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_winchAllowed` | page 203 | Right body controller: a203 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_winchReleaseAllowed` | page 203 | Right body controller: a203 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_parkingAllowed` | page 203 | Right body controller: a203 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_dynApplyAllowed` | page 203 | Right body controller: a203 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_releaseAllowed` | page 203 | Right body controller: a203 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_parkPendingAllowed` | page 203 | Right body controller: a203 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_wenchPendingAllowed` | page 203 | Right body controller: a203 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a203_desyncCount` | page 203 | Right body controller: a203 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a203_current` | page 203 | Right body controller: a203 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCRIGHT_a203_epbConfig` | page 203 | Right body controller: a203 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a204_unknownAllowed` | page 204 | Right body controller: a204 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_openAllowed` | page 204 | Right body controller: a204 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_dynamicAllowed` | page 204 | Right body controller: a204 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_parkAllowed` | page 204 | Right body controller: a204 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_startAllowed` | page 204 | Right body controller: a204 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_serviceAllowed` | page 204 | Right body controller: a204 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_winchAllowed` | page 204 | Right body controller: a204 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_winchReleaseAllowed` | page 204 | Right body controller: a204 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_parkingAllowed` | page 204 | Right body controller: a204 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_dynApplyAllowed` | page 204 | Right body controller: a204 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_releaseAllowed` | page 204 | Right body controller: a204 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_parkPendingAllowed` | page 204 | Right body controller: a204 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_wenchPendingAllowed` | page 204 | Right body controller: a204 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a204_desyncCount` | page 204 | Right body controller: a204 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a204_current` | page 204 | Right body controller: a204 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCRIGHT_a204_epbConfig` | page 204 | Right body controller: a204 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a205_unknownAllowed` | page 205 | Right body controller: a205 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_openAllowed` | page 205 | Right body controller: a205 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_dynamicAllowed` | page 205 | Right body controller: a205 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_parkAllowed` | page 205 | Right body controller: a205 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_startAllowed` | page 205 | Right body controller: a205 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_serviceAllowed` | page 205 | Right body controller: a205 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_winchAllowed` | page 205 | Right body controller: a205 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_winchReleaseAllowed` | page 205 | Right body controller: a205 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_parkingAllowed` | page 205 | Right body controller: a205 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_dynApplyAllowed` | page 205 | Right body controller: a205 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_releaseAllowed` | page 205 | Right body controller: a205 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_parkPendingAllowed` | page 205 | Right body controller: a205 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_wenchPendingAllowed` | page 205 | Right body controller: a205 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a205_desyncCount` | page 205 | Right body controller: a205 desync count | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a205_current` | page 205 | Right body controller: a205 current | 38\|10 | little-endian | unsigned | 0.05 | 0 | A | 0 to 51.15 |  | plausible |
| `VCRIGHT_a205_epbConfig` | page 205 | Right body controller: a205 epb config | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a206_unknownAllowed` | page 206 | Right body controller: a206 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_openAllowed` | page 206 | Right body controller: a206 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_dynamicAllowed` | page 206 | Right body controller: a206 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_parkAllowed` | page 206 | Right body controller: a206 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_startAllowed` | page 206 | Right body controller: a206 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_serviceAllowed` | page 206 | Right body controller: a206 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_winchAllowed` | page 206 | Right body controller: a206 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_winchReleaseAllowed` | page 206 | Right body controller: a206 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_parkingAllowed` | page 206 | Right body controller: a206 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_dynApplyAllowed` | page 206 | Right body controller: a206 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_releaseAllowed` | page 206 | Right body controller: a206 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_parkPendingAllowed` | page 206 | Right body controller: a206 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_wenchPendingAllowed` | page 206 | Right body controller: a206 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a206_unitStatusEPB` | page 206 | Right body controller: a206 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a206_unitStatusEPBM` | page 206 | Right body controller: a206 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a207_unknownAllowed` | page 207 | Right body controller: a207 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_openAllowed` | page 207 | Right body controller: a207 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_dynamicAllowed` | page 207 | Right body controller: a207 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_parkAllowed` | page 207 | Right body controller: a207 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_startAllowed` | page 207 | Right body controller: a207 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_serviceAllowed` | page 207 | Right body controller: a207 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_winchAllowed` | page 207 | Right body controller: a207 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_winchReleaseAllowed` | page 207 | Right body controller: a207 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_parkingAllowed` | page 207 | Right body controller: a207 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_dynApplyAllowed` | page 207 | Right body controller: a207 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_releaseAllowed` | page 207 | Right body controller: a207 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_parkPendingAllowed` | page 207 | Right body controller: a207 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_wenchPendingAllowed` | page 207 | Right body controller: a207 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a207_unitStatusEPB` | page 207 | Right body controller: a207 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a207_unitStatusEPBM` | page 207 | Right body controller: a207 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a208_unknownAllowed` | page 208 | Right body controller: a208 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_openAllowed` | page 208 | Right body controller: a208 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_dynamicAllowed` | page 208 | Right body controller: a208 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_parkAllowed` | page 208 | Right body controller: a208 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_startAllowed` | page 208 | Right body controller: a208 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_serviceAllowed` | page 208 | Right body controller: a208 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_winchAllowed` | page 208 | Right body controller: a208 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_winchReleaseAllowed` | page 208 | Right body controller: a208 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_parkingAllowed` | page 208 | Right body controller: a208 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_dynApplyAllowed` | page 208 | Right body controller: a208 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_releaseAllowed` | page 208 | Right body controller: a208 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_parkPendingAllowed` | page 208 | Right body controller: a208 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_wenchPendingAllowed` | page 208 | Right body controller: a208 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a208_unitStatusEPB` | page 208 | Right body controller: a208 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a208_unitStatusEPBM` | page 208 | Right body controller: a208 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a209_unknownAllowed` | page 209 | Right body controller: a209 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_openAllowed` | page 209 | Right body controller: a209 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_dynamicAllowed` | page 209 | Right body controller: a209 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_parkAllowed` | page 209 | Right body controller: a209 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_startAllowed` | page 209 | Right body controller: a209 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_serviceAllowed` | page 209 | Right body controller: a209 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_winchAllowed` | page 209 | Right body controller: a209 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_winchReleaseAllowed` | page 209 | Right body controller: a209 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_parkingAllowed` | page 209 | Right body controller: a209 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_dynApplyAllowed` | page 209 | Right body controller: a209 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_releaseAllowed` | page 209 | Right body controller: a209 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_parkPendingAllowed` | page 209 | Right body controller: a209 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_wenchPendingAllowed` | page 209 | Right body controller: a209 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a209_unitStatusEPB` | page 209 | Right body controller: a209 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a209_unitStatusEPBM` | page 209 | Right body controller: a209 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a210_unknownAllowed` | page 210 | Right body controller: a210 unknown allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_openAllowed` | page 210 | Right body controller: a210 open allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_dynamicAllowed` | page 210 | Right body controller: a210 dynamic allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_parkAllowed` | page 210 | Right body controller: a210 park allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_startAllowed` | page 210 | Right body controller: a210 start allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_serviceAllowed` | page 210 | Right body controller: a210 service allowed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_winchAllowed` | page 210 | Right body controller: a210 winch allowed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_winchReleaseAllowed` | page 210 | Right body controller: a210 winch release allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_parkingAllowed` | page 210 | Right body controller: a210 parking allowed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_dynApplyAllowed` | page 210 | Right body controller: a210 dyn apply allowed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_releaseAllowed` | page 210 | Right body controller: a210 release allowed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_parkPendingAllowed` | page 210 | Right body controller: a210 park pending allowed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_wenchPendingAllowed` | page 210 | Right body controller: a210 wench pending allowed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a210_unitStatusEPB` | page 210 | Right body controller: a210 unit status EPB | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a210_unitStatusEPBM` | page 210 | Right body controller: a210 unit status EPBM | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `OPEN`<br>2 = `DYNAMIC`<br>3 = `PARK`<br>4 = `START`<br>5 = `SERVICE`<br>6 = `WINCHMODE`<br>7 = `WINCHMODE_RELEASING`<br>8 = `PARKING`<br>9 = `DYNAMIC_APPLYING`<br>10 = `RELEASING`<br>11 = `SERVICE_RELEASING`<br>12 = `PARK_PENDING`<br>13 = `WINCHMODE_PENDING`<br>14 = `SUMMON`<br>15 = `SUMMON_RELEASING`<br>16 = `SUMMON_PARKING`<br>17 = `EXTERNAL_DYNAMIC`<br>18 = `RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EXTERNAL_PARKING`<br>20 = `DYNAMIC_PARKING`<br>21 = `FREE_ROLL_MODE`<br>22 = `AUTONOMY_OPEN`<br>23 = `COUNT` | plausible |
| `VCRIGHT_a221_vbatProtVoltage` | page 221 | Right body controller: a221 vbat prot voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCRIGHT_a221_vbatProtCurrent` | page 221 | Right body controller: a221 vbat prot current | 24\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCRIGHT_a221_uvLoadshedVoltage` | page 221 | Right body controller: a221 uv loadshed voltage | 40\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCRIGHT_a221_uvLoadshedFromFrontMonitor` | page 221 | Right body controller: a221 uv loadshed from front monitor | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `VCRIGHT_a221_faultInjectActive` | page 221 | Right body controller: a221 fault inject active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a221_uvResetActive` | page 221 | Right body controller: a221 uv reset active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a221_uvLoadshedArmPrimary` | page 221 | Right body controller: a221 uv loadshed arm primary | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a224_seatMotorCalibrated` | page 224 | Right body controller: a224 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a224_seatMotorCurrent` | page 224 | Right body controller: a224 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a224_seatMotorState` | page 224 | Right body controller: a224 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a224_seatSwitchBack` | page 224 | Right body controller: a224 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a224_seatSwitchForward` | page 224 | Right body controller: a224 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a225_seatMotorCalibrated` | page 225 | Right body controller: a225 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a225_seatMotorCurrent` | page 225 | Right body controller: a225 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a225_seatMotorState` | page 225 | Right body controller: a225 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a225_seatSwitchBack` | page 225 | Right body controller: a225 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a225_seatSwitchForward` | page 225 | Right body controller: a225 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a226_seatMotorCalibrated` | page 226 | Right body controller: a226 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a226_seatMotorCurrent` | page 226 | Right body controller: a226 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a226_seatMotorState` | page 226 | Right body controller: a226 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a226_seatSwitchBack` | page 226 | Right body controller: a226 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a226_seatSwitchForward` | page 226 | Right body controller: a226 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a227_seatMotorCalibrated` | page 227 | Right body controller: a227 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a227_seatMotorCurrent` | page 227 | Right body controller: a227 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a227_seatMotorState` | page 227 | Right body controller: a227 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a227_seatSwitchBack` | page 227 | Right body controller: a227 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a227_seatSwitchForward` | page 227 | Right body controller: a227 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a228_seatMotorCalibrated` | page 228 | Right body controller: a228 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a228_seatMotorCurrent` | page 228 | Right body controller: a228 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a228_seatMotorPosReal` | page 228 | Right body controller: a228 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a228_seatMotorState` | page 228 | Right body controller: a228 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a228_seatSwitchBack` | page 228 | Right body controller: a228 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a228_seatSwitchForward` | page 228 | Right body controller: a228 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a229_seatMotorCalibrated` | page 229 | Right body controller: a229 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a229_seatMotorCurrent` | page 229 | Right body controller: a229 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a229_seatMotorPosReal` | page 229 | Right body controller: a229 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a229_seatMotorState` | page 229 | Right body controller: a229 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a229_seatSwitchBack` | page 229 | Right body controller: a229 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a229_seatSwitchForward` | page 229 | Right body controller: a229 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a230_seatMotorCalibrated` | page 230 | Right body controller: a230 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a230_seatMotorCurrent` | page 230 | Right body controller: a230 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a230_seatMotorPosReal` | page 230 | Right body controller: a230 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a230_seatMotorState` | page 230 | Right body controller: a230 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a230_seatSwitchBack` | page 230 | Right body controller: a230 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a230_seatSwitchForward` | page 230 | Right body controller: a230 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a231_seatMotorCalibrated` | page 231 | Right body controller: a231 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a231_seatMotorCurrent` | page 231 | Right body controller: a231 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a231_seatMotorPosReal` | page 231 | Right body controller: a231 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a231_seatMotorState` | page 231 | Right body controller: a231 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a231_seatSwitchBack` | page 231 | Right body controller: a231 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a231_seatSwitchForward` | page 231 | Right body controller: a231 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a232_seatMotorCurrent` | page 232 | Right body controller: a232 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a232_seatMotorPosReal` | page 232 | Right body controller: a232 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a232_seatMotorState` | page 232 | Right body controller: a232 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a232_seatSwitchBack` | page 232 | Right body controller: a232 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a232_seatSwitchForward` | page 232 | Right body controller: a232 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a233_seatMotorCurrent` | page 233 | Right body controller: a233 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a233_seatMotorPosReal` | page 233 | Right body controller: a233 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a233_seatMotorState` | page 233 | Right body controller: a233 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a233_seatSwitchBack` | page 233 | Right body controller: a233 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a233_seatSwitchForward` | page 233 | Right body controller: a233 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a234_seatMotorCurrent` | page 234 | Right body controller: a234 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a234_seatMotorPosReal` | page 234 | Right body controller: a234 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a234_seatMotorState` | page 234 | Right body controller: a234 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a234_seatSwitchBack` | page 234 | Right body controller: a234 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a234_seatSwitchForward` | page 234 | Right body controller: a234 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a235_seatMotorCurrent` | page 235 | Right body controller: a235 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a235_seatMotorPosReal` | page 235 | Right body controller: a235 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a235_seatMotorState` | page 235 | Right body controller: a235 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a235_seatSwitchBack` | page 235 | Right body controller: a235 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a235_seatSwitchForward` | page 235 | Right body controller: a235 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a236_lumbarAPressureHpa` | page 236 | Right body controller: a236 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a236_lumbarBPressureHpa` | page 236 | Right body controller: a236 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a236_lumbarDiagStatus` | page 236 | Right body controller: a236 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a236_lumbarAState` | page 236 | Right body controller: a236 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a236_lumbarBState` | page 236 | Right body controller: a236 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a237_lumbarAPressureHpa` | page 237 | Right body controller: a237 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a237_lumbarBPressureHpa` | page 237 | Right body controller: a237 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a237_lumbarDiagStatus` | page 237 | Right body controller: a237 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a237_lumbarAState` | page 237 | Right body controller: a237 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a237_lumbarBState` | page 237 | Right body controller: a237 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a238_lumbarAPressureHpa` | page 238 | Right body controller: a238 lumbar a pressure hpa | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a238_lumbarBPressureHpa` | page 238 | Right body controller: a238 lumbar b pressure hpa | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCRIGHT_a238_lumbarDiagStatus` | page 238 | Right body controller: a238 lumbar diag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a238_lumbarAState` | page 238 | Right body controller: a238 lumbar a state | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a238_lumbarBState` | page 238 | Right body controller: a238 lumbar b state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a239_seatHeatCurrent` | page 239 | Right body controller: a239 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a239_seatHeatTmp` | page 239 | Right body controller: a239 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a239_seatHeatTmpTarget` | page 239 | Right body controller: a239 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCRIGHT_a240_seatHeatCurrent` | page 240 | Right body controller: a240 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a240_seatHeatTmp` | page 240 | Right body controller: a240 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a241_seatHeatCurrent` | page 241 | Right body controller: a241 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a241_seatHeatTmp` | page 241 | Right body controller: a241 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a241_cushion` | page 241 | Right body controller: a241 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a241_backrest` | page 241 | Right body controller: a241 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a242_seatHeatCurrent` | page 242 | Right body controller: a242 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a242_seatHeatTmp` | page 242 | Right body controller: a242 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a242_seatHeatTmpTarget` | page 242 | Right body controller: a242 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCRIGHT_a243_seatHeatCurrent` | page 243 | Right body controller: a243 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a243_seatHeatTmp` | page 243 | Right body controller: a243 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a244_seatHeatCurrent` | page 244 | Right body controller: a244 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a244_seatHeatTmp` | page 244 | Right body controller: a244 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a244_cushion` | page 244 | Right body controller: a244 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a244_backrest` | page 244 | Right body controller: a244 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a245_seatHeatCurrent` | page 245 | Right body controller: a245 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a245_seatHeatTmp` | page 245 | Right body controller: a245 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a245_seatHeatTmpTarget` | page 245 | Right body controller: a245 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCRIGHT_a246_seatHeatCurrent` | page 246 | Right body controller: a246 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a246_seatHeatTmp` | page 246 | Right body controller: a246 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a247_seatHeatCurrent` | page 247 | Right body controller: a247 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a247_seatHeatTmp` | page 247 | Right body controller: a247 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a247_cushion` | page 247 | Right body controller: a247 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a247_backrest` | page 247 | Right body controller: a247 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a248_seatHeatCurrent` | page 248 | Right body controller: a248 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a248_seatHeatTmp` | page 248 | Right body controller: a248 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a248_seatHeatTmpTarget` | page 248 | Right body controller: a248 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCRIGHT_a249_seatHeatCurrent` | page 249 | Right body controller: a249 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a249_seatHeatTmp` | page 249 | Right body controller: a249 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a250_seatHeatCurrent` | page 250 | Right body controller: a250 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a250_seatHeatTmp` | page 250 | Right body controller: a250 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a250_cushion` | page 250 | Right body controller: a250 cushion | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a250_backrest` | page 250 | Right body controller: a250 backrest | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a251_seatMotorCurrent` | page 251 | Right body controller: a251 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a251_seatMotorPosReal` | page 251 | Right body controller: a251 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a251_seatMotorState` | page 251 | Right body controller: a251 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a251_seatSwitchBack` | page 251 | Right body controller: a251 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a251_seatSwitchForward` | page 251 | Right body controller: a251 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a252_seatMotorCurrent` | page 252 | Right body controller: a252 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a252_seatMotorPosReal` | page 252 | Right body controller: a252 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a252_seatMotorState` | page 252 | Right body controller: a252 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a252_seatSwitchBack` | page 252 | Right body controller: a252 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a252_seatSwitchForward` | page 252 | Right body controller: a252 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a253_seatMotorCurrent` | page 253 | Right body controller: a253 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a253_seatMotorPosReal` | page 253 | Right body controller: a253 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a253_seatMotorState` | page 253 | Right body controller: a253 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a253_seatSwitchBack` | page 253 | Right body controller: a253 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a253_seatSwitchForward` | page 253 | Right body controller: a253 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a254_seatMotorCurrent` | page 254 | Right body controller: a254 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a254_seatMotorPosReal` | page 254 | Right body controller: a254 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a254_seatMotorState` | page 254 | Right body controller: a254 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a254_seatSwitchBack` | page 254 | Right body controller: a254 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a254_seatSwitchForward` | page 254 | Right body controller: a254 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a255_leftIGBTTemp` | page 255 | Right body controller: a255 left IGBT temp | 16\|8 | little-endian | signed | 1 | 80 | degC | -48 to 207 |  | plausible |
| `VCRIGHT_a255_rightIGBTTemp` | page 255 | Right body controller: a255 right IGBT temp | 24\|8 | little-endian | signed | 1 | 80 | degC | -48 to 207 |  | plausible |
| `VCRIGHT_a255_OCPTemp` | page 255 | Right body controller: a255 OCP temp | 32\|8 | little-endian | signed | 1 | 80 | degC | -48 to 207 |  | plausible |
| `VCRIGHT_a255_PCBTemp` | page 255 | Right body controller: a255 PCB temp | 40\|8 | little-endian | signed | 1 | 80 | degC | -48 to 207 |  | plausible |
| `VCRIGHT_a256_leftCurrent` | page 256 | Right body controller: a256 left current | 16\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 51 |  | plausible |
| `VCRIGHT_a256_rightCurrent` | page 256 | Right body controller: a256 right current | 24\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 51 |  | plausible |
| `VCRIGHT_a257_MIAStatus` | page 257 | Right body controller: a257 MIA status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a258_bootIdFreq` | page 258 | Right body controller: a258 boot id freq | 16\|8 | little-endian | unsigned | 0.02 | 0 | Hz | 0 to 5.1 |  | plausible |
| `VCRIGHT_a262_LVLow` | page 262 | Right body controller: a262 LV low | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LVHigh` | page 262 | Right body controller: a262 LV high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_HVLow` | page 262 | Right body controller: a262 HV low | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_HVHigh` | page 262 | Right body controller: a262 HV high | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftOverCurrent` | page 262 | Right body controller: a262 left over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightOverCurrent` | page 262 | Right body controller: a262 right over current | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftShutOutlet` | page 262 | Right body controller: a262 left shut outlet | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightShutOutlet` | page 262 | Right body controller: a262 right shut outlet | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_ThermalShutPCB` | page 262 | Right body controller: a262 thermal shut PCB | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftThermalShutIGBT` | page 262 | Right body controller: a262 left thermal shut IGBT | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightThermalShutIGBT` | page 262 | Right body controller: a262 right thermal shut IGBT | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_CANTimeout` | page 262 | Right body controller: a262 CAN timeout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LowVoltageSensor` | page 262 | Right body controller: a262 low voltage sensor | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_HighVoltageSensor` | page 262 | Right body controller: a262 high voltage sensor | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftCurrentHVSensor` | page 262 | Right body controller: a262 left current HV sensor | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightCurrentHVSensor` | page 262 | Right body controller: a262 right current HV sensor | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftTempIGBT` | page 262 | Right body controller: a262 left temp IGBT | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_TempOCP` | page 262 | Right body controller: a262 temp OCP | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightTempIGBT` | page 262 | Right body controller: a262 right temp IGBT | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_TempPCB` | page 262 | Right body controller: a262 temp PCB | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftIGBTShort` | page 262 | Right body controller: a262 left IGBT short | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightIGBTShort` | page 262 | Right body controller: a262 right IGBT short | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_IGBTDriverTemporary` | page 262 | Right body controller: a262 IGBT driver temporary | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_IGBTDriverPermanent` | page 262 | Right body controller: a262 IGBT driver permanent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_LeftIGBTOpen` | page 262 | Right body controller: a262 left IGBT open | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a262_RightIGBTOpen` | page 262 | Right body controller: a262 right IGBT open | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a263_seatMotorCurrent` | page 263 | Right body controller: a263 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a263_seatMotorDCurrent` | page 263 | Right body controller: a263 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a263_seatMotorPosReal` | page 263 | Right body controller: a263 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a263_seatMotorState` | page 263 | Right body controller: a263 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a264_seatMotorCurrent` | page 264 | Right body controller: a264 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a264_seatMotorDCurrent` | page 264 | Right body controller: a264 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a264_seatMotorPosReal` | page 264 | Right body controller: a264 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a264_seatMotorState` | page 264 | Right body controller: a264 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a265_seatMotorCurrent` | page 265 | Right body controller: a265 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a265_seatMotorDCurrent` | page 265 | Right body controller: a265 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a265_seatMotorPosReal` | page 265 | Right body controller: a265 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a265_seatMotorState` | page 265 | Right body controller: a265 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a266_seatMotorCurrent` | page 266 | Right body controller: a266 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a266_seatMotorDCurrent` | page 266 | Right body controller: a266 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a266_seatMotorPosReal` | page 266 | Right body controller: a266 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a266_seatMotorState` | page 266 | Right body controller: a266 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a267_seatMotorCurrent` | page 267 | Right body controller: a267 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a267_seatMotorDCurrent` | page 267 | Right body controller: a267 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a267_seatMotorPosReal` | page 267 | Right body controller: a267 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a267_seatMotorState` | page 267 | Right body controller: a267 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a268_seatMotorCurrent` | page 268 | Right body controller: a268 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a268_seatMotorDCurrent` | page 268 | Right body controller: a268 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a268_seatMotorPosReal` | page 268 | Right body controller: a268 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a268_seatMotorState` | page 268 | Right body controller: a268 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a269_seatMotorCurrent` | page 269 | Right body controller: a269 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a269_seatMotorDCurrent` | page 269 | Right body controller: a269 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a269_seatMotorPosReal` | page 269 | Right body controller: a269 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a269_seatMotorState` | page 269 | Right body controller: a269 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a270_seatMotorCurrent` | page 270 | Right body controller: a270 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a270_seatMotorDCurrent` | page 270 | Right body controller: a270 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a270_seatMotorPosReal` | page 270 | Right body controller: a270 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a270_seatMotorState` | page 270 | Right body controller: a270 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a271_humiditySensorSNA` | page 271 | Right body controller: a271 humidity sensor SNA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a271_temperatureSensorSNA` | page 271 | Right body controller: a271 temperature sensor SNA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a271_solarVisSensorSNA` | page 271 | Right body controller: a271 solar vis sensor SNA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a271_solarInfSensorSNA` | page 271 | Right body controller: a271 solar inf sensor SNA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a273_handlePWM` | page 273 | Right body controller: a273 handle PWM | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_a273_temperature` | page 273 | Right body controller: a273 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a274_handlePWM` | page 274 | Right body controller: a274 handle PWM | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_a274_temperature` | page 274 | Right body controller: a274 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a275_outputFaulted` | page 275 | Right body controller: a275 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a275_currentSenseFaulted` | page 275 | Right body controller: a275 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a275_tempSenseFaulted` | page 275 | Right body controller: a275 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a275_underCurrent` | page 275 | Right body controller: a275 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a275_overCurrent` | page 275 | Right body controller: a275 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a275_overTemperature` | page 275 | Right body controller: a275 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a278_HVLow` | page 278 | Right body controller: a278 HV low | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a278_PTCMIA` | page 278 | Right body controller: a278 PTCMIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a282_voltage` | page 282 | Right body controller: a282 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a282_temperature` | page 282 | Right body controller: a282 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a283_voltage` | page 283 | Right body controller: a283 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a283_temperature` | page 283 | Right body controller: a283 temperature | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a284_gloveboxMinCurrent` | page 284 | Right body controller: a284 glovebox min current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCRIGHT_a284_gloveboxMaxCurrent` | page 284 | Right body controller: a284 glovebox max current | 24\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCRIGHT_a284_cabinTempInterior` | page 284 | Right body controller: a284 cabin temp interior; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87 | 255 = `SNA` | plausible |
| `VCRIGHT_a285_gloveboxMinCurrent` | page 285 | Right body controller: a285 glovebox min current | 16\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCRIGHT_a285_gloveboxMaxCurrent` | page 285 | Right body controller: a285 glovebox max current | 24\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCRIGHT_a285_cabinTempInterior` | page 285 | Right body controller: a285 cabin temp interior; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87 | 255 = `SNA` | plausible |
| `VCRIGHT_a290_isNetworkSwitch` | page 290 | Right body controller: a290 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a290_occupancySensorV` | page 290 | Right body controller: a290 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a290_railVoltage` | page 290 | Right body controller: a290 rail voltage | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a291_buckleSensorVoltage` | page 291 | Right body controller: a291 buckle sensor voltage | 16\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCRIGHT_a291_railVoltage` | page 291 | Right body controller: a291 rail voltage | 28\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCRIGHT_a292_buckleSensorVoltage` | page 292 | Right body controller: a292 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a292_railV` | page 292 | Right body controller: a292 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a293_buckleSensorVoltage` | page 293 | Right body controller: a293 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a293_railV` | page 293 | Right body controller: a293 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a294_isNetworkSwitch` | page 294 | Right body controller: a294 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a294_occupancySensorV` | page 294 | Right body controller: a294 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a294_railV` | page 294 | Right body controller: a294 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a295_isNetworkSwitch` | page 295 | Right body controller: a295 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a295_occupancySensorV` | page 295 | Right body controller: a295 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a295_railV` | page 295 | Right body controller: a295 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a296_isNetworkSwitch` | page 296 | Right body controller: a296 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a296_occupancySensorV` | page 296 | Right body controller: a296 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a296_railV` | page 296 | Right body controller: a296 rail v | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a297_cabinTmp` | page 297 | Right body controller: a297 cabin tmp | 16\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a298_buckleSensorVoltage` | page 298 | Right body controller: a298 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a298_railV` | page 298 | Right body controller: a298 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a299_buckleSensorVoltage` | page 299 | Right body controller: a299 buckle sensor voltage | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a299_railV` | page 299 | Right body controller: a299 rail v | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a302_calibrationPositiveDirection` | page 302 | Right body controller: a302 calibration positive direction | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_calibrationNegativeDirection` | page 302 | Right body controller: a302 calibration negative direction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_uncalibrated` | page 302 | Right body controller: a302 uncalibrated | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_driverFault` | page 302 | Right body controller: a302 driver fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_connected` | page 302 | Right body controller: a302 connected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_targetMissed` | page 302 | Right body controller: a302 target missed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a302_positionTarget` | page 302 | Right body controller: a302 position target | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a302_positionActual` | page 302 | Right body controller: a302 position actual | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a303_eFuseTripCount` | page 303 | Right body controller: a303 e fuse trip count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a306_disconnectedTime` | page 306 | Right body controller: a306 disconnected time | 16\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | plausible |
| `VCRIGHT_a307_disconnectedTime` | page 307 | Right body controller: a307 disconnected time | 16\|10 | little-endian | unsigned | 1 | 0 | ms | 0 to 1023 |  | plausible |
| `VCRIGHT_a308_calibrationPositiveDirection` | page 308 | Right body controller: a308 calibration positive direction | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_calibrationNegativeDirection` | page 308 | Right body controller: a308 calibration negative direction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_uncalibrated` | page 308 | Right body controller: a308 uncalibrated | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_driverFault` | page 308 | Right body controller: a308 driver fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_connected` | page 308 | Right body controller: a308 connected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_targetMissed` | page 308 | Right body controller: a308 target missed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a308_positionTarget` | page 308 | Right body controller: a308 position target | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a308_positionActual` | page 308 | Right body controller: a308 position actual | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a310_mirrorFoldTime` | page 310 | Right body controller: a310 mirror fold time | 16\|9 | little-endian | unsigned | 10 | 0 | ms | 0 to 5110 |  | plausible |
| `VCRIGHT_a310_foldingDirection` | page 310 | Right body controller: a310 folding direction | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FOLD`<br>1 = `UNFOLD` | plausible |
| `VCRIGHT_a310_mirrorMaxFoldCurrent` | page 310 | Right body controller: a310 mirror max fold current | 32\|7 | little-endian | signed | 0.05 | 0 | A | -3.2 to 3.15 |  | plausible |
| `VCRIGHT_a310_ambientTemperature` | page 310 | Right body controller: a310 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCRIGHT_a311_outputFaulted` | page 311 | Right body controller: a311 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a311_currentSenseFaulted` | page 311 | Right body controller: a311 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a311_tempSenseFaulted` | page 311 | Right body controller: a311 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a311_underCurrent` | page 311 | Right body controller: a311 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a311_overCurrent` | page 311 | Right body controller: a311 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a311_overTemperature` | page 311 | Right body controller: a311 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_outputFaulted` | page 312 | Right body controller: a312 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_currentSenseFaulted` | page 312 | Right body controller: a312 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_tempSenseFaulted` | page 312 | Right body controller: a312 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_underCurrent` | page 312 | Right body controller: a312 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_overCurrent` | page 312 | Right body controller: a312 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a312_overTemperature` | page 312 | Right body controller: a312 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_outputFaulted` | page 313 | Right body controller: a313 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_currentSenseFaulted` | page 313 | Right body controller: a313 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_tempSenseFaulted` | page 313 | Right body controller: a313 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_underCurrent` | page 313 | Right body controller: a313 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_overCurrent` | page 313 | Right body controller: a313 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a313_overTemperature` | page 313 | Right body controller: a313 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_outputFaulted` | page 314 | Right body controller: a314 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_currentSenseFaulted` | page 314 | Right body controller: a314 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_tempSenseFaulted` | page 314 | Right body controller: a314 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_underCurrent` | page 314 | Right body controller: a314 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_overCurrent` | page 314 | Right body controller: a314 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a314_overTemperature` | page 314 | Right body controller: a314 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_outputFaulted` | page 315 | Right body controller: a315 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_currentSenseFaulted` | page 315 | Right body controller: a315 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_tempSenseFaulted` | page 315 | Right body controller: a315 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_underCurrent` | page 315 | Right body controller: a315 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_overCurrent` | page 315 | Right body controller: a315 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a315_overTemperature` | page 315 | Right body controller: a315 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a316_foldState` | page 316 | Right body controller: a316 fold state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `FOLDED`<br>2 = `UNFOLDED`<br>3 = `FOLDING`<br>4 = `UNFOLDING` | plausible |
| `VCRIGHT_a316_actuationDurationMs` | page 316 | Right body controller: a316 actuation duration ms | 19\|10 | little-endian | unsigned | 10 | 0 | ms | 0 to 10230 |  | plausible |
| `VCRIGHT_a316_maxCurrentAmps` | page 316 | Right body controller: a316 max current amps | 32\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a316_averageCurrentAmps` | page 316 | Right body controller: a316 average current amps | 44\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a316_ambientTemperatureDegC` | page 316 | Right body controller: a316 ambient temperature deg c; raw 0 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCRIGHT_a318_outputFaulted` | page 318 | Right body controller: a318 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a318_currentSenseFaulted` | page 318 | Right body controller: a318 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a318_tempSenseFaulted` | page 318 | Right body controller: a318 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a318_underCurrent` | page 318 | Right body controller: a318 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a318_overCurrent` | page 318 | Right body controller: a318 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a318_overTemperature` | page 318 | Right body controller: a318 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_outputFaulted` | page 319 | Right body controller: a319 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_currentSenseFaulted` | page 319 | Right body controller: a319 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_tempSenseFaulted` | page 319 | Right body controller: a319 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_underCurrent` | page 319 | Right body controller: a319 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_overCurrent` | page 319 | Right body controller: a319 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a319_overTemperature` | page 319 | Right body controller: a319 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a324_mirrorHeatCurrent` | page 324 | Right body controller: a324 mirror heat current | 16\|10 | little-endian | unsigned | 0.01 | 0 | A | 0 to 10.23 |  | plausible |
| `VCRIGHT_a325_calibrationPositiveDirection` | page 325 | Right body controller: a325 calibration positive direction | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_calibrationNegativeDirection` | page 325 | Right body controller: a325 calibration negative direction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_uncalibrated` | page 325 | Right body controller: a325 uncalibrated | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_driverFault` | page 325 | Right body controller: a325 driver fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_connected` | page 325 | Right body controller: a325 connected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_targetMissed` | page 325 | Right body controller: a325 target missed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a325_positionTarget` | page 325 | Right body controller: a325 position target | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a325_positionActual` | page 325 | Right body controller: a325 position actual | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a326_calibrationPositiveDirection` | page 326 | Right body controller: a326 calibration positive direction | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_calibrationNegativeDirection` | page 326 | Right body controller: a326 calibration negative direction | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_uncalibrated` | page 326 | Right body controller: a326 uncalibrated | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_driverFault` | page 326 | Right body controller: a326 driver fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_connected` | page 326 | Right body controller: a326 connected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_targetMissed` | page 326 | Right body controller: a326 target missed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a326_positionTarget` | page 326 | Right body controller: a326 position target | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a326_positionActual` | page 326 | Right body controller: a326 position actual | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `VCRIGHT_a330_voltage` | page 330 | Right body controller: a330 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a330_maxCurrent` | page 330 | Right body controller: a330 max current | 24\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCRIGHT_a330_temperature` | page 330 | Right body controller: a330 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a331_voltage` | page 331 | Right body controller: a331 voltage | 16\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a331_maxCurrent` | page 331 | Right body controller: a331 max current | 24\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.75 |  | plausible |
| `VCRIGHT_a331_temperature` | page 331 | Right body controller: a331 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a343_rearDefrostCurrent` | page 343 | Right body controller: a343 rear defrost current | 16\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51.1 |  | plausible |
| `VCRIGHT_a343_batteryVoltage` | page 343 | Right body controller: a343 battery voltage | 25\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a343_ambientTemperature` | page 343 | Right body controller: a343 ambient temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a344_rearDefrostCurrent` | page 344 | Right body controller: a344 rear defrost current | 16\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51.1 |  | plausible |
| `VCRIGHT_a344_batteryVoltage` | page 344 | Right body controller: a344 battery voltage | 25\|7 | little-endian | unsigned | 0.15 | 0 | V | 0 to 19.05 |  | plausible |
| `VCRIGHT_a344_ambientTemperature` | page 344 | Right body controller: a344 ambient temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87.5 |  | plausible |
| `VCRIGHT_a345_PTCTHSGBPwrCurrent` | page 345 | Right body controller: a345 PTCTHSGB pwr current | 16\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |
| `VCRIGHT_a368_snsShortCircuit` | page 368 | Right body controller: a368 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a368_snsDisconnect` | page 368 | Right body controller: a368 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a368_snsRateChangeUp` | page 368 | Right body controller: a368 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a368_snsRateChangeDown` | page 368 | Right body controller: a368 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a369_snsShortCircuit` | page 369 | Right body controller: a369 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a369_snsDisconnect` | page 369 | Right body controller: a369 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a369_snsRateChangeUp` | page 369 | Right body controller: a369 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a369_snsRateChangeDown` | page 369 | Right body controller: a369 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a373_windowChannel` | page 373 | Right body controller: a373 window channel | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `REAR`<br>2 = `FRONT` | plausible |
| `VCRIGHT_a375_windowFront` | page 375 | Right body controller: a375 window front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a376_2RowSeatTrackActuatorCurrent` | page 376 | Right body controller: a376 2 row seat track actuator current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a376_2RowSeatTrackActuatorDuty` | page 376 | Right body controller: a376 2 row seat track actuator duty | 28\|12 | little-endian | signed | 0.1 | 0 | % | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a376_2RowSeatEasyEntryState` | page 376 | Right body controller: a376 2 row seat easy entry state; raw 6 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRACK_AFT_PITCH_LATCHED`<br>1 = `TRACK_UNLATCHING`<br>2 = `TRACK_FORE_PITCH_LATCHED`<br>3 = `PITCH_UNLATCHING`<br>4 = `TRACK_AFT_PITCH_UNLATCHED`<br>5 = `TRACK_FORE_PITCH_UNLATCHED`<br>6 = `SNA` | plausible |
| `VCRIGHT_a376_2RowSeatTrackPositionSwitch` | page 376 | Right body controller: a376 2 row seat track position switch; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a377_snsShortCircuit` | page 377 | Right body controller: a377 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a377_snsDisconnect` | page 377 | Right body controller: a377 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a377_snsRateChangeUp` | page 377 | Right body controller: a377 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a377_snsRateChangeDown` | page 377 | Right body controller: a377 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a378_snsShortCircuit` | page 378 | Right body controller: a378 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a378_snsDisconnect` | page 378 | Right body controller: a378 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a378_snsRateChangeUp` | page 378 | Right body controller: a378 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a378_snsRateChangeDown` | page 378 | Right body controller: a378 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a379_snsShortCircuit` | page 379 | Right body controller: a379 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a379_snsDisconnect` | page 379 | Right body controller: a379 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a379_snsRateChangeUp` | page 379 | Right body controller: a379 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a379_snsRateChangeDown` | page 379 | Right body controller: a379 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_outputFaulted` | page 380 | Right body controller: a380 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_currentSenseFaulted` | page 380 | Right body controller: a380 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_tempSenseFaulted` | page 380 | Right body controller: a380 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_underCurrent` | page 380 | Right body controller: a380 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_overCurrent` | page 380 | Right body controller: a380 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a380_overTemperature` | page 380 | Right body controller: a380 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_outputFaulted` | page 381 | Right body controller: a381 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_currentSenseFaulted` | page 381 | Right body controller: a381 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_tempSenseFaulted` | page 381 | Right body controller: a381 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_underCurrent` | page 381 | Right body controller: a381 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_overCurrent` | page 381 | Right body controller: a381 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a381_overTemperature` | page 381 | Right body controller: a381 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_outputFaulted` | page 382 | Right body controller: a382 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_currentSenseFaulted` | page 382 | Right body controller: a382 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_tempSenseFaulted` | page 382 | Right body controller: a382 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_underCurrent` | page 382 | Right body controller: a382 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_overCurrent` | page 382 | Right body controller: a382 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a382_overTemperature` | page 382 | Right body controller: a382 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a385_current` | page 385 | Right body controller: a385 current | 16\|11 | little-endian | unsigned | 0.001 | 0 | A | 0 to 2.047 |  | plausible |
| `VCRIGHT_a385_voltage` | page 385 | Right body controller: a385 voltage | 32\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCRIGHT_a385_resistance` | page 385 | Right body controller: a385 resistance | 40\|8 | little-endian | unsigned | 1 | 0 | ohm | 0 to 255 |  | plausible |
| `VCRIGHT_a385_reason` | page 385 | Right body controller: a385 reason | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `UNRESPONSIVE`<br>2 = `RESISTANCE_LOW`<br>3 = `RESISTANCE_HIGH` | plausible |
| `VCRIGHT_a406_frame1MIA` | page 406 | Right body controller: a406 frame1 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a406_frame2MIA` | page 406 | Right body controller: a406 frame2 MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a407_configMismatch` | page 407 | Right body controller: a407 config mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a407_counterError` | page 407 | Right body controller: a407 counter error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a407_checksumError` | page 407 | Right body controller: a407 checksum error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a407_linResponseError` | page 407 | Right body controller: a407 lin response error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_generalError` | page 408 | Right body controller: a408 general error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_seatbeltError` | page 408 | Right body controller: a408 seatbelt error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_doorError` | page 408 | Right body controller: a408 door error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_ALRError` | page 408 | Right body controller: a408 ALR error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_pressureError` | page 408 | Right body controller: a408 pressure error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_fluidLevelError` | page 408 | Right body controller: a408 fluid level error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_temperatureError` | page 408 | Right body controller: a408 temperature error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_hardwareInternalError` | page 408 | Right body controller: a408 hardware internal error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_overvoltageError` | page 408 | Right body controller: a408 overvoltage error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_overcurrentError` | page 408 | Right body controller: a408 overcurrent error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_ignitionError` | page 408 | Right body controller: a408 ignition error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_calibrationError` | page 408 | Right body controller: a408 calibration error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a408_trimError` | page 408 | Right body controller: a408 trim error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a411_failureReason` | page 411 | Right body controller: a411 failure reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `DEVICE_STUCK_ON`<br>2 = `BRIDGE`<br>3 = `BRIDGE_AND_DEVICE_STUCK_ON`<br>4 = `LOAD_UNATTEMPTED_ON`<br>8 = `FOLLOWER`<br>16 = `TIMEOUT`<br>32 = `BRIDGE_SYNC` | plausible |
| `VCRIGHT_a411_loadUnattemptedOnFailure` | page 411 | Right body controller: a411 load unattempted on failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a411_deviceStuckOnFailure` | page 411 | Right body controller: a411 device stuck on failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a411_uvLoadshedVsenseDigIn` | page 411 | Right body controller: a411 uv loadshed vsense dig in | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a411_uvLoadshedVoltage` | page 411 | Right body controller: a411 uv loadshed voltage | 25\|9 | little-endian | unsigned | 0.05 | 0 | V | 0 to 25.55 |  | plausible |
| `VCRIGHT_a412_outputFaulted` | page 412 | Right body controller: a412 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a412_currentSenseFaulted` | page 412 | Right body controller: a412 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a412_tempSenseFaulted` | page 412 | Right body controller: a412 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a412_underCurrent` | page 412 | Right body controller: a412 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a412_overCurrent` | page 412 | Right body controller: a412 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a412_overTemperature` | page 412 | Right body controller: a412 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_outputFaulted` | page 413 | Right body controller: a413 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_currentSenseFaulted` | page 413 | Right body controller: a413 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_tempSenseFaulted` | page 413 | Right body controller: a413 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_underCurrent` | page 413 | Right body controller: a413 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_overCurrent` | page 413 | Right body controller: a413 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a413_overTemperature` | page 413 | Right body controller: a413 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_outputFaulted` | page 414 | Right body controller: a414 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_currentSenseFaulted` | page 414 | Right body controller: a414 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_tempSenseFaulted` | page 414 | Right body controller: a414 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_underCurrent` | page 414 | Right body controller: a414 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_overCurrent` | page 414 | Right body controller: a414 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a414_overTemperature` | page 414 | Right body controller: a414 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_outputFaulted` | page 415 | Right body controller: a415 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_currentSenseFaulted` | page 415 | Right body controller: a415 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_tempSenseFaulted` | page 415 | Right body controller: a415 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_underCurrent` | page 415 | Right body controller: a415 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_overCurrent` | page 415 | Right body controller: a415 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a415_overTemperature` | page 415 | Right body controller: a415 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_outputFaulted` | page 416 | Right body controller: a416 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_currentSenseFaulted` | page 416 | Right body controller: a416 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_tempSenseFaulted` | page 416 | Right body controller: a416 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_underCurrent` | page 416 | Right body controller: a416 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_overCurrent` | page 416 | Right body controller: a416 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a416_overTemperature` | page 416 | Right body controller: a416 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_outputFaulted` | page 417 | Right body controller: a417 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_currentSenseFaulted` | page 417 | Right body controller: a417 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_tempSenseFaulted` | page 417 | Right body controller: a417 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_underCurrent` | page 417 | Right body controller: a417 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_overCurrent` | page 417 | Right body controller: a417 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a417_overTemperature` | page 417 | Right body controller: a417 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_outputFaulted` | page 418 | Right body controller: a418 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_currentSenseFaulted` | page 418 | Right body controller: a418 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_tempSenseFaulted` | page 418 | Right body controller: a418 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_underCurrent` | page 418 | Right body controller: a418 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_overCurrent` | page 418 | Right body controller: a418 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a418_overTemperature` | page 418 | Right body controller: a418 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_outputFaulted` | page 419 | Right body controller: a419 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_currentSenseFaulted` | page 419 | Right body controller: a419 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_tempSenseFaulted` | page 419 | Right body controller: a419 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_underCurrent` | page 419 | Right body controller: a419 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_overCurrent` | page 419 | Right body controller: a419 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a419_overTemperature` | page 419 | Right body controller: a419 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_outputFaulted` | page 420 | Right body controller: a420 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_currentSenseFaulted` | page 420 | Right body controller: a420 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_tempSenseFaulted` | page 420 | Right body controller: a420 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_underCurrent` | page 420 | Right body controller: a420 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_overCurrent` | page 420 | Right body controller: a420 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a420_overTemperature` | page 420 | Right body controller: a420 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_outputFaulted` | page 421 | Right body controller: a421 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_currentSenseFaulted` | page 421 | Right body controller: a421 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_tempSenseFaulted` | page 421 | Right body controller: a421 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_underCurrent` | page 421 | Right body controller: a421 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_overCurrent` | page 421 | Right body controller: a421 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a421_overTemperature` | page 421 | Right body controller: a421 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_3rUsbPortsStuckOff` | page 422 | Right body controller: a422 3r usb ports stuck off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_lumbarEcuStuckOff` | page 422 | Right body controller: a422 lumbar ecu stuck off | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_oilPumpStuckOff` | page 422 | Right body controller: a422 oil pump stuck off | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_vbusProtFusedMiscStuckOff` | page 422 | Right body controller: a422 vbus prot fused misc stuck off | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_vbusProtFusedSeatStuckOff` | page 422 | Right body controller: a422 vbus prot fused seat stuck off | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_seatFrontVentFanCushionStuckOff` | page 422 | Right body controller: a422 seat front vent fan cushion stuck off | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_seatFrontVentFanBackrestStuckOff` | page 422 | Right body controller: a422 seat front vent fan backrest stuck off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_doorRearRgbStuckOff` | page 422 | Right body controller: a422 door rear rgb stuck off | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_radioTunerStuckOff` | page 422 | Right body controller: a422 radio tuner stuck off | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_seat2rControllerStuckOff` | page 422 | Right body controller: a422 seat2r controller stuck off | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_premiumAmpStuckOff` | page 422 | Right body controller: a422 premium amp stuck off | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a422_rearGlassHeaterStuckOff` | page 422 | Right body controller: a422 rear glass heater stuck off | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a426_seatMotorCalibrated` | page 426 | Right body controller: a426 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a426_seatMotorCurrent` | page 426 | Right body controller: a426 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a426_seatMotorPosReal` | page 426 | Right body controller: a426 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a426_seatMotorState` | page 426 | Right body controller: a426 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a426_seatSwitchBack` | page 426 | Right body controller: a426 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a426_seatSwitchForward` | page 426 | Right body controller: a426 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a426_cabinTmp` | page 426 | Right body controller: a426 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a427_seatMotorCalibrated` | page 427 | Right body controller: a427 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a427_seatMotorCurrent` | page 427 | Right body controller: a427 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a427_seatMotorPosReal` | page 427 | Right body controller: a427 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a427_seatMotorState` | page 427 | Right body controller: a427 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a427_seatSwitchBack` | page 427 | Right body controller: a427 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a427_seatSwitchForward` | page 427 | Right body controller: a427 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a427_cabinTmp` | page 427 | Right body controller: a427 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a428_seatMotorCalibrated` | page 428 | Right body controller: a428 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a428_seatMotorCurrent` | page 428 | Right body controller: a428 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a428_seatMotorPosReal` | page 428 | Right body controller: a428 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a428_seatMotorState` | page 428 | Right body controller: a428 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a428_seatSwitchBack` | page 428 | Right body controller: a428 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a428_seatSwitchForward` | page 428 | Right body controller: a428 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a428_cabinTmp` | page 428 | Right body controller: a428 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a429_seatMotorCalibrated` | page 429 | Right body controller: a429 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a429_seatMotorCurrent` | page 429 | Right body controller: a429 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a429_seatMotorPosReal` | page 429 | Right body controller: a429 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a429_seatMotorState` | page 429 | Right body controller: a429 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a429_seatSwitchBack` | page 429 | Right body controller: a429 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a429_seatSwitchForward` | page 429 | Right body controller: a429 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a429_cabinTmp` | page 429 | Right body controller: a429 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCRIGHT_a444_retriesAvailable` | page 444 | Right body controller: a444 retries available | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a444_channel` | page 444 | Right body controller: a444 channel | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a444_watchdog` | page 444 | Right body controller: a444 watchdog | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_gateDriver` | page 444 | Right body controller: a444 gate driver | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_overcurrent` | page 444 | Right body controller: a444 overcurrent | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_supplyUndervoltage` | page 444 | Right body controller: a444 supply undervoltage | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_cpUndervoltage` | page 444 | Right body controller: a444 cp undervoltage | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_overTempShutdown` | page 444 | Right body controller: a444 over temp shutdown | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_overTempWarning` | page 444 | Right body controller: a444 over temp warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_highSide2GateDriver` | page 444 | Right body controller: a444 high side2 gate driver | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_lowSide2GateDriver` | page 444 | Right body controller: a444 low side2 gate driver | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_highSide1GateDriver` | page 444 | Right body controller: a444 high side1 gate driver | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_lowSide1GateDriver` | page 444 | Right body controller: a444 low side1 gate driver | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_highSide2OverCurent` | page 444 | Right body controller: a444 high side2 over curent | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_lowSide2OverCurent` | page 444 | Right body controller: a444 low side2 over curent | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_highSide1OverCurent` | page 444 | Right body controller: a444 high side1 over curent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_lowSide1OverCurent` | page 444 | Right body controller: a444 low side1 over curent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_spiInit` | page 444 | Right body controller: a444 spi init | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_spiPeriodicCheck` | page 444 | Right body controller: a444 spi periodic check | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_spiFault` | page 444 | Right body controller: a444 spi fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_voltageMonitor` | page 444 | Right body controller: a444 voltage monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_enableLow` | page 444 | Right body controller: a444 enable low | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_highCurrentFeedEnabled` | page 444 | Right body controller: a444 high current feed enabled | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_supplyVoltageEnabled` | page 444 | Right body controller: a444 supply voltage enabled | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a444_supplyVoltage` | page 444 | Right body controller: a444 supply voltage | 54\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `VCRIGHT_a446_caseTempHVACUnavailable` | page 446 | Right body controller: a446 case temp HVAC unavailable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_evapHVACUnavailable` | page 446 | Right body controller: a446 evap HVAC unavailable | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_evapTempInvalid` | page 446 | Right body controller: a446 evap temp invalid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_hvacBlowerFaulted` | page 446 | Right body controller: a446 hvac blower faulted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_evapOperationNotAllowed` | page 446 | Right body controller: a446 evap operation not allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_allAirPathsBlocked` | page 446 | Right body controller: a446 all air paths blocked | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_rawDuctTempInvalidLeft` | page 446 | Right body controller: a446 raw duct temp invalid left | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a446_rawDuctTempInvalidRight` | page 446 | Right body controller: a446 raw duct temp invalid right | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manACOFFComfortCoolNudge` | page 448 | Right body controller: a448 man ACOFF comfort cool nudge | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manAirflowComfortHeatNudge` | page 448 | Right body controller: a448 man airflow comfort heat nudge | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manAirflowFwdLkComfortHeatNudge` | page 448 | Right body controller: a448 man airflow fwd lk comfort heat nudge | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manAirflowFwdLkComfortCoolNudge` | page 448 | Right body controller: a448 man airflow fwd lk comfort cool nudge | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manACOffFwdLkComfortCoolNudge` | page 448 | Right body controller: a448 man AC off fwd lk comfort cool nudge | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manFreshComfortHeatManualHVACIntvn` | page 448 | Right body controller: a448 man fresh comfort heat manual HVAC intvn | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manFreshComfortCoolManualHVACIntvn` | page 448 | Right body controller: a448 man fresh comfort cool manual HVAC intvn | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manFreshComfortCoolAutoHVACIntvn` | page 448 | Right body controller: a448 man fresh comfort cool auto HVAC intvn | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manFreshComfortHeatAutoHVACIntvn` | page 448 | Right body controller: a448 man fresh comfort heat auto HVAC intvn | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manRecircRHAutoHVACIntvn` | page 448 | Right body controller: a448 man recirc RH auto HVAC intvn | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manRecircFlashFogGenericHVACIntvn` | page 448 | Right body controller: a448 man recirc flash fog generic HVAC intvn | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manRecircFlashFogWetAirHVACIntvn` | page 448 | Right body controller: a448 man recirc flash fog wet air HVAC intvn | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manRecircRHManualHVACNudge` | page 448 | Right body controller: a448 man recirc RH manual HVAC nudge | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manACoffRHManualHVACNudge` | page 448 | Right body controller: a448 man a coff RH manual HVAC nudge | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manHvacOffAutoSteerFogIntvn` | page 448 | Right body controller: a448 man hvac off auto steer fog intvn | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manHvacOffAutoSteerFogNudge` | page 448 | Right body controller: a448 man hvac off auto steer fog nudge | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manHvacAutoSteerFogIntvn` | page 448 | Right body controller: a448 man hvac auto steer fog intvn | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manHvacAutoSteerFogNudge` | page 448 | Right body controller: a448 man hvac auto steer fog nudge | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a448_manualHighBlowerSpeedAutoHVACIntvn` | page 448 | Right body controller: a448 manual high blower speed auto HVAC intvn | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_channel` | page 482 | Right body controller: a482 channel | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `VCRIGHT_a482_spiFault` | page 482 | Right body controller: a482 spi fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_resetBar` | page 482 | Right body controller: a482 reset bar | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_overTempShutdown` | page 482 | Right body controller: a482 over temp shutdown | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_thermalWarning` | page 482 | Right body controller: a482 thermal warning | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_underOrOverVoltageOrOverCurrent` | page 482 | Right body controller: a482 under or over voltage or over current | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a482_underloadDetected` | page 482 | Right body controller: a482 underload detected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a489_vbatProtVoltage` | page 489 | Right body controller: a489 vbat prot voltage | 16\|9 | little-endian | unsigned | 0.0391389429569 | 0 | V | 0 to 19.999999851 |  | plausible |
| `VCRIGHT_a489_3rUsbPortsStuckOn` | page 489 | Right body controller: a489 3r usb ports stuck on | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_lumbarEcuStuckOn` | page 489 | Right body controller: a489 lumbar ecu stuck on | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_oilPumpStuckOn` | page 489 | Right body controller: a489 oil pump stuck on | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_vbusProtFusedMiscStuckOn` | page 489 | Right body controller: a489 vbus prot fused misc stuck on | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON` | plausible |
| `VCRIGHT_a489_vbusProtFusedSeatStuckOn` | page 489 | Right body controller: a489 vbus prot fused seat stuck on | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON` | plausible |
| `VCRIGHT_a489_seatFrontVentFanCushionStuckOn` | page 489 | Right body controller: a489 seat front vent fan cushion stuck on | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_seatFrontVentFanBackrestStuckOn` | page 489 | Right body controller: a489 seat front vent fan backrest stuck on | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_doorRearRgbStuckOn` | page 489 | Right body controller: a489 door rear rgb stuck on | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_radioTunerStuckOn` | page 489 | Right body controller: a489 radio tuner stuck on | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_seat2rControllerStuckOn` | page 489 | Right body controller: a489 seat2r controller stuck on | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_premiumAmpStuckOn` | page 489 | Right body controller: a489 premium amp stuck on | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a489_rearGlassHeaterStuckOn` | page 489 | Right body controller: a489 rear glass heater stuck on | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PASS_OR_NOT_APPLICABLE`<br>1 = `STUCK_ON_SHARED_MONITOR` | plausible |
| `VCRIGHT_a492_3rUsbPortsUnattemptedOn` | page 492 | Right body controller: a492 3r usb ports unattempted on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_lumbarEcuUnattemptedOn` | page 492 | Right body controller: a492 lumbar ecu unattempted on | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_oilPumpUnattemptedOn` | page 492 | Right body controller: a492 oil pump unattempted on | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_vbusProtFusedMiscUnattemptedOn` | page 492 | Right body controller: a492 vbus prot fused misc unattempted on | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_vbusProtFusedSeatUnattemptedOn` | page 492 | Right body controller: a492 vbus prot fused seat unattempted on | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_seatFrontVentFanCushionUnattemptedOn` | page 492 | Right body controller: a492 seat front vent fan cushion unattempted on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_seatFrontVentFanBackrestUnattemptedOn` | page 492 | Right body controller: a492 seat front vent fan backrest unattempted on | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_doorRearRgbUnattemptedOn` | page 492 | Right body controller: a492 door rear rgb unattempted on | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_radioTunerUnattemptedOn` | page 492 | Right body controller: a492 radio tuner unattempted on | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_seat2rControllerUnattemptedOn` | page 492 | Right body controller: a492 seat2r controller unattempted on | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_premiumAmpUnattemptedOn` | page 492 | Right body controller: a492 premium amp unattempted on | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a492_rearGlassHeaterUnattemptedOn` | page 492 | Right body controller: a492 rear glass heater unattempted on | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a496_cabinTempInterior` | page 496 | Right body controller: a496 cabin temp interior; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87 | 255 = `SNA` | plausible |
| `VCRIGHT_a497_ecuUnprovisioned` | page 497 | Right body controller: a497 ecu unprovisioned | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a510_isRearwardEndstopUncalibrated` | page 510 | Right body controller: a510 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a510_isAbsPosSensorUncalibrated` | page 510 | Right body controller: a510 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a510_seatState` | page 510 | Right body controller: a510 seat state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a510_motorType` | page 510 | Right body controller: a510 motor type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCRIGHT_a510_absPosSensState` | page 510 | Right body controller: a510 abs pos sens state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAULTED`<br>1 = `REARWARD`<br>2 = `FORWARD`<br>3 = `DISCONNECTED` | plausible |
| `VCRIGHT_a513_calibrated` | page 513 | Right body controller: a513 calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a513_angle` | page 513 | Right body controller: a513 angle | 17\|8 | little-endian | signed | 0.5 | 59 | deg | -5 to 122.5 |  | plausible |
| `VCRIGHT_a513_seatStatePrev` | page 513 | Right body controller: a513 seat state prev; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a513_obstacleDetectReason` | page 513 | Right body controller: a513 obstacle detect reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `MOTOR_CURRENT_STALL`<br>2 = `MOTOR_ENCODER_STALL`<br>3 = `ACCEL_LOOKBACK_UNCOMP_ABS`<br>4 = `ACCEL_LOOKBACK_UNCOMP_REL`<br>5 = `ACCEL_LOOKBACK_COMP_ABS`<br>6 = `MEDIUM_CURRENT_THRESHOLD`<br>7 = `SPEED_THRESHOLD`<br>8 = `MAX_SPEED_DIFF` | plausible |
| `VCRIGHT_a513_accelLookbackTripDepth` | page 513 | Right body controller: a513 accel lookback trip depth | 33\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `VCRIGHT_a513_duty` | page 513 | Right body controller: a513 duty | 40\|8 | little-endian | signed | 1 | 0 | % | -128 to 127 |  | plausible |
| `VCRIGHT_a513_currentAbsFilt` | page 513 | Right body controller: a513 current abs filt | 48\|8 | little-endian | unsigned | 0.25 | 0 | A | 0 to 63.75 |  | plausible |
| `VCRIGHT_a513_motorType` | page 513 | Right body controller: a513 motor type | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCRIGHT_a513_absolutePosSensorForward` | page 513 | Right body controller: a513 absolute pos sensor forward | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a513_cabinTemp` | page 513 | Right body controller: a513 cabin temp | 58\|6 | little-endian | signed | 2 | 20 | degC | -44 to 82 |  | plausible |
| `VCRIGHT_a517_isRearwardEndstopUncalibrated` | page 517 | Right body controller: a517 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a517_isAbsPosSensorUncalibrated` | page 517 | Right body controller: a517 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a518_seatState` | page 518 | Right body controller: a518 seat state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a520_epbConfig` | page 520 | Right body controller: a520 epb config | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a520_gtwEpbConfig` | page 520 | Right body controller: a520 gtw epb config | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `MODEL3_BASE`<br>2 = `MODEL3_PERFORMANCE`<br>3 = `MODELS_BASE`<br>4 = `MODELY_BASE`<br>5 = `MODELY_PERFORMANCE`<br>6 = `MODELX_BASE`<br>7 = `MODEL3_PERFORMANCE_V2`<br>8 = `MODELY_PERFORMANCE_V2`<br>9 = `MODELS_CERAMIC`<br>10 = `MODEL3_ZF`<br>11 = `CT_MANDO` | plausible |
| `VCRIGHT_a525_GTW_twelveVBatteryType` | page 525 | Right body controller: a525 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCRIGHT_a525_newLVBatteryType` | page 525 | Right body controller: a525 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_a525_initialLVBatteryType` | page 525 | Right body controller: a525 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_a525_serviceMode` | page 525 | Signal reported by Right body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a525_factoryGated` | page 525 | Right body controller: a525 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a525_frunkOpen` | page 525 | Right body controller: a525 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_ptcHeaterFault` | page 538 | Right body controller: a538 ptc heater fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_ductTempSensorFault` | page 538 | Right body controller: a538 duct temp sensor fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_evapTempSensorFault` | page 538 | Right body controller: a538 evap temp sensor fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_cabinTempSensorFault` | page 538 | Right body controller: a538 cabin temp sensor fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_cabinModelNotInitialized` | page 538 | Right body controller: a538 cabin model not initialized | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_airpathsBlocked` | page 538 | Right body controller: a538 airpaths blocked | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_blowerFaultOrStopped` | page 538 | Right body controller: a538 blower fault or stopped | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_compressorFaultOrStandby` | page 538 | Right body controller: a538 compressor fault or standby | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_heatPumpModeNotAttainable` | page 538 | Right body controller: a538 heat pump mode not attainable | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_thsVersionMismatch` | page 538 | Right body controller: a538 ths version mismatch | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_thsMia` | page 538 | Right body controller: a538 ths mia | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_hvOn` | page 538 | Right body controller: a538 hv on | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_hvacPowerOn` | page 538 | Right body controller: a538 hvac power on | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a538_limpMode` | page 538 | Right body controller: a538 limp mode | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_hvacSystemNotNominal` | page 539 | Right body controller: a539 hvac system not nominal | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_modeledCabinTempOutOfRange` | page 539 | Right body controller: a539 modeled cabin temp out of range | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_modeledCabinTempExceedingSetTemp` | page 539 | Right body controller: a539 modeled cabin temp exceeding set temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_cabinTempSensorFault` | page 539 | Right body controller: a539 cabin temp sensor fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_cabinTempSensorOutOfRange` | page 539 | Right body controller: a539 cabin temp sensor out of range | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a539_modeledCabinTempDeviation` | page 539 | Right body controller: a539 modeled cabin temp deviation | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a545_GTW_twelveVBatteryType` | page 545 | Right body controller: a545 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCRIGHT_a545_newLVBatteryType` | page 545 | Right body controller: a545 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_a545_serviceMode` | page 545 | Signal reported by Right body controller | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a545_factoryGated` | page 545 | Right body controller: a545 factory gated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a545_frunkOpen` | page 545 | Right body controller: a545 frunk open | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a551_restrictDoorReleaseSignalFront` | page 551 | Right body controller: a551 restrict door release signal front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a551_interiorReleaseReqCountFront` | page 551 | Right body controller: a551 interior release req count front | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a551_lastRequestSourceFront` | page 551 | Right body controller: a551 last request source front | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCRIGHT_a551_restrictDoorReleaseSignalRear` | page 551 | Right body controller: a551 restrict door release signal rear | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a551_interiorReleaseReqCountRear` | page 551 | Right body controller: a551 interior release req count rear | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCRIGHT_a551_lastRequestSourceRear` | page 551 | Right body controller: a551 last request source rear | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `VCRIGHT_a560_isRearwardEndstopUncalibrated` | page 560 | Right body controller: a560 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a560_isAbsPosSensorUncalibrated` | page 560 | Right body controller: a560 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a560_seatState` | page 560 | Right body controller: a560 seat state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a560_motorType` | page 560 | Right body controller: a560 motor type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCRIGHT_a560_absPosSensState` | page 560 | Right body controller: a560 abs pos sens state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAULTED`<br>1 = `REARWARD`<br>2 = `FORWARD`<br>3 = `DISCONNECTED` | plausible |
| `VCRIGHT_a563_calibrated` | page 563 | Right body controller: a563 calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a563_angle` | page 563 | Right body controller: a563 angle | 17\|8 | little-endian | signed | 0.5 | 59 | deg | -5 to 122.5 |  | plausible |
| `VCRIGHT_a563_seatStatePrev` | page 563 | Right body controller: a563 seat state prev; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a563_obstacleDetectReason` | page 563 | Right body controller: a563 obstacle detect reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `MOTOR_CURRENT_STALL`<br>2 = `MOTOR_ENCODER_STALL`<br>3 = `ACCEL_LOOKBACK_UNCOMP_ABS`<br>4 = `ACCEL_LOOKBACK_UNCOMP_REL`<br>5 = `ACCEL_LOOKBACK_COMP_ABS`<br>6 = `MEDIUM_CURRENT_THRESHOLD`<br>7 = `SPEED_THRESHOLD`<br>8 = `MAX_SPEED_DIFF` | plausible |
| `VCRIGHT_a563_accelLookbackTripDepth` | page 563 | Right body controller: a563 accel lookback trip depth | 33\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `VCRIGHT_a563_duty` | page 563 | Right body controller: a563 duty | 40\|8 | little-endian | signed | 1 | 0 | % | -128 to 127 |  | plausible |
| `VCRIGHT_a563_currentAbsFilt` | page 563 | Right body controller: a563 current abs filt | 48\|8 | little-endian | unsigned | 0.25 | 0 | A | 0 to 63.75 |  | plausible |
| `VCRIGHT_a563_motorType` | page 563 | Right body controller: a563 motor type | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCRIGHT_a563_absolutePosSensorForward` | page 563 | Right body controller: a563 absolute pos sensor forward | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a563_cabinTemp` | page 563 | Right body controller: a563 cabin temp | 58\|6 | little-endian | signed | 2 | 20 | degC | -44 to 82 |  | plausible |
| `VCRIGHT_a567_isRearwardEndstopUncalibrated` | page 567 | Right body controller: a567 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a567_isAbsPosSensorUncalibrated` | page 567 | Right body controller: a567 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a568_seatState` | page 568 | Right body controller: a568 seat state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCRIGHT_a570_seatHeatCurrent` | page 570 | Right body controller: a570 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a570_seatHeatTmp` | page 570 | Right body controller: a570 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a571_seatHeatCurrent` | page 571 | Right body controller: a571 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a571_seatHeatTmp` | page 571 | Right body controller: a571 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a572_seatHeatCurrent` | page 572 | Right body controller: a572 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a572_seatHeatTmp` | page 572 | Right body controller: a572 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a573_seatHeatCurrent` | page 573 | Right body controller: a573 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCRIGHT_a573_seatHeatTmp` | page 573 | Right body controller: a573 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCRIGHT_a577_outputFaulted` | page 577 | Right body controller: a577 output faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a577_currentSenseFaulted` | page 577 | Right body controller: a577 current sense faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a577_tempSenseFaulted` | page 577 | Right body controller: a577 temp sense faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a577_underCurrent` | page 577 | Right body controller: a577 under current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a577_overCurrent` | page 577 | Right body controller: a577 over current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a577_overTemperature` | page 577 | Right body controller: a577 over temperature | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_openCircuitDoorFR` | page 578 | Right body controller: a578 open circuit door FR | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_shortCircuitDoorFR` | page 578 | Right body controller: a578 short circuit door FR | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_miaDoorFR` | page 578 | Right body controller: a578 mia door FR | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_openCircuitDoorRR` | page 578 | Right body controller: a578 open circuit door RR | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_shortCircuitDoorRR` | page 578 | Right body controller: a578 short circuit door RR | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a578_miaDoorRR` | page 578 | Right body controller: a578 mia door RR | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a579_liftgateFollowerStoppingCondition` | page 579 | Right body controller: a579 liftgate follower stopping condition | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `OBSTACLE_CURRENT`<br>2 = `OBSTACLE_CURRENT_SPIKE`<br>3 = `PINCH_SENSITIVE` | plausible |
| `VCRIGHT_a579_liftgateFollowerPosition` | page 579 | Right body controller: a579 liftgate follower position | 24\|7 | little-endian | signed | 1 | 43 | deg | -21 to 106 |  | plausible |
| `VCRIGHT_a579_liftgateFollowerLatchStatus` | page 579 | Right body controller: a579 liftgate follower latch status; raw 0 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `OPENED`<br>2 = `CLOSED`<br>3 = `CLOSING`<br>4 = `OPENING`<br>5 = `AJAR`<br>6 = `TIMEOUT`<br>7 = `DEFAULT`<br>8 = `FAULT` | plausible |
| `VCRIGHT_a585_ambientTemp` | page 585 | Right body controller: a585 ambient temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCRIGHT_a586_ambientTemp` | page 586 | Right body controller: a586 ambient temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `VCRIGHT_a587_VEH_switchStatus` | page 587 | Right body controller: a587 VEH switch status | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a588_VEH_seatStatus2` | page 588 | Right body controller: a588 VEH seat status2 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a588_VEH_switchStatus` | page 588 | Right body controller: a588 VEH switch status | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a588_VEH_restraintStatus` | page 588 | Right body controller: a588 VEH restraint status | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a590_seatMotorCalibrated` | page 590 | Right body controller: a590 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a590_seatMotorCurrent` | page 590 | Right body controller: a590 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a590_seatMotorState` | page 590 | Right body controller: a590 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a590_seatSwitchBack` | page 590 | Right body controller: a590 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a590_seatSwitchForward` | page 590 | Right body controller: a590 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a591_seatMotorCurrent` | page 591 | Right body controller: a591 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a591_seatMotorPosReal` | page 591 | Right body controller: a591 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a591_seatMotorState` | page 591 | Right body controller: a591 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a591_seatSwitchBack` | page 591 | Right body controller: a591 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a591_seatSwitchForward` | page 591 | Right body controller: a591 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a592_seatMotorCurrent` | page 592 | Right body controller: a592 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a592_seatMotorPosReal` | page 592 | Right body controller: a592 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a592_seatMotorState` | page 592 | Right body controller: a592 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a592_seatSwitchBack` | page 592 | Right body controller: a592 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a592_seatSwitchForward` | page 592 | Right body controller: a592 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a593_seatMotorCalibrated` | page 593 | Right body controller: a593 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a593_seatMotorCurrent` | page 593 | Right body controller: a593 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a593_seatMotorPosReal` | page 593 | Right body controller: a593 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a593_seatMotorState` | page 593 | Right body controller: a593 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a593_seatSwitchBack` | page 593 | Right body controller: a593 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a593_seatSwitchForward` | page 593 | Right body controller: a593 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCRIGHT_a594_seatMotorCurrent` | page 594 | Right body controller: a594 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a594_seatMotorDCurrent` | page 594 | Right body controller: a594 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a594_seatMotorPosReal` | page 594 | Right body controller: a594 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a594_seatMotorState` | page 594 | Right body controller: a594 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a595_seatMotorCurrent` | page 595 | Right body controller: a595 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a595_seatMotorDCurrent` | page 595 | Right body controller: a595 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCRIGHT_a595_seatMotorPosReal` | page 595 | Right body controller: a595 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCRIGHT_a595_seatMotorState` | page 595 | Right body controller: a595 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCRIGHT_a596_frontDoorLatchAjarSwitchVoltage` | page 596 | Right body controller: a596 front door latch ajar switch voltage | 16\|12 | little-endian | unsigned | 1.25 | 0 | mV | 0 to 5118.75 |  | plausible |
| `VCRIGHT_a597_rearDoorLatchAjarSwitchVoltage` | page 597 | Right body controller: a597 rear door latch ajar switch voltage | 16\|12 | little-endian | unsigned | 1.25 | 0 | mV | 0 to 5118.75 |  | plausible |
| `VCRIGHT_a599_GTW_twelveVBatteryType` | page 599 | Right body controller: a599 GTW twelve v battery type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | plausible |
| `VCRIGHT_a599_newLVBatteryType` | page 599 | Right body controller: a599 new LV battery type | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_a599_initialLVBatteryType` | page 599 | Right body controller: a599 initial LV battery type | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `ATLASBX_B24_FLOODED`<br>2 = `CLARIOS_B24_FLOODED`<br>3 = `CATL_LI_ION`<br>4 = `TESLA_16V_LI_ION`<br>5 = `TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_a599_serviceMode` | page 599 | Signal reported by Right body controller | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a599_factoryGated` | page 599 | Right body controller: a599 factory gated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a599_frunkOpen` | page 599 | Right body controller: a599 frunk open | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_a605_excessiveMacFailures` | page 605 | Right body controller: a605 excessive mac failures | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCRIGHT_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 10 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (13 signals), page 87 (9 signals), page 88 (9 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (3 signals), page 95 (2 signals), page 96 (2 signals), page 97 (2 signals), page 98 (14 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (5 signals), page 107 (14 signals), page 108 (14 signals), page 110 (17 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (21 signals), page 116 (22 signals), page 117 (29 signals), page 118 (31 signals), page 119 (6 signals), page 120 (33 signals), page 121 (1 signals), page 124 (3 signals), page 125 (4 signals), page 136 (1 signals), page 137 (1 signals), page 138 (1 signals), page 139 (1 signals), page 140 (1 signals), page 141 (1 signals), page 142 (1 signals), page 144 (4 signals), page 145 (4 signals), page 146 (4 signals), page 147 (4 signals), page 148 (4 signals), page 149 (4 signals), page 150 (8 signals), page 151 (8 signals), page 152 (4 signals), page 153 (4 signals), page 154 (2 signals), page 155 (2 signals), page 177 (1 signals), page 180 (6 signals), page 181 (6 signals), page 184 (3 signals), page 186 (2 signals), page 187 (2 signals), page 188 (2 signals), page 189 (2 signals), page 190 (1 signals), page 193 (1 signals), page 194 (1 signals), page 195 (1 signals), page 196 (3 signals), page 197 (3 signals), page 198 (3 signals), page 199 (3 signals), page 202 (16 signals), page 203 (16 signals), page 204 (16 signals), page 205 (16 signals), page 206 (15 signals), page 207 (15 signals), page 208 (15 signals), page 209 (15 signals), page 210 (15 signals), page 221 (7 signals), page 224 (5 signals), page 225 (5 signals), page 226 (5 signals), page 227 (5 signals), page 228 (6 signals), page 229 (6 signals), page 230 (6 signals), page 231 (6 signals), page 232 (5 signals), page 233 (5 signals), page 234 (5 signals), page 235 (5 signals), page 236 (5 signals), page 237 (5 signals), page 238 (5 signals), page 239 (3 signals), page 240 (2 signals), page 241 (4 signals), page 242 (3 signals), page 243 (2 signals), page 244 (4 signals), page 245 (3 signals), page 246 (2 signals), page 247 (4 signals), page 248 (3 signals), page 249 (2 signals), page 250 (4 signals), page 251 (5 signals), page 252 (5 signals), page 253 (5 signals), page 254 (5 signals), page 255 (4 signals), page 256 (2 signals), page 257 (1 signals), page 258 (1 signals), page 262 (26 signals), page 263 (4 signals), page 264 (4 signals), page 265 (4 signals), page 266 (4 signals), page 267 (4 signals), page 268 (4 signals), page 269 (4 signals), page 270 (4 signals), page 271 (4 signals), page 273 (2 signals), page 274 (2 signals), page 275 (6 signals), page 278 (2 signals), page 282 (2 signals), page 283 (2 signals), page 284 (3 signals), page 285 (3 signals), page 290 (3 signals), page 291 (2 signals), page 292 (2 signals), page 293 (2 signals), page 294 (3 signals), page 295 (3 signals), page 296 (3 signals), page 297 (1 signals), page 298 (2 signals), page 299 (2 signals), page 302 (8 signals), page 303 (1 signals), page 306 (1 signals), page 307 (1 signals), page 308 (8 signals), page 310 (4 signals), page 311 (6 signals), page 312 (6 signals), page 313 (6 signals), page 314 (6 signals), page 315 (6 signals), page 316 (5 signals), page 318 (6 signals), page 319 (6 signals), page 324 (1 signals), page 325 (8 signals), page 326 (8 signals), page 330 (3 signals), page 331 (3 signals), page 343 (3 signals), page 344 (3 signals), page 345 (1 signals), page 368 (4 signals), page 369 (4 signals), page 373 (1 signals), page 375 (1 signals), page 376 (4 signals), page 377 (4 signals), page 378 (4 signals), page 379 (4 signals), page 380 (6 signals), page 381 (6 signals), page 382 (6 signals), page 385 (4 signals), page 406 (2 signals), page 407 (4 signals), page 408 (13 signals), page 411 (5 signals), page 412 (6 signals), page 413 (6 signals), page 414 (6 signals), page 415 (6 signals), page 416 (6 signals), page 417 (6 signals), page 418 (6 signals), page 419 (6 signals), page 420 (6 signals), page 421 (6 signals), page 422 (12 signals), page 426 (7 signals), page 427 (7 signals), page 428 (7 signals), page 429 (7 signals), page 444 (25 signals), page 446 (8 signals), page 448 (19 signals), page 482 (7 signals), page 489 (13 signals), page 492 (12 signals), page 496 (1 signals), page 497 (1 signals), page 510 (5 signals), page 513 (10 signals), page 517 (2 signals), page 518 (1 signals), page 520 (2 signals), page 525 (6 signals), page 538 (14 signals), page 539 (6 signals), page 545 (5 signals), page 551 (6 signals), page 560 (5 signals), page 563 (10 signals), page 567 (2 signals), page 568 (1 signals), page 570 (2 signals), page 571 (2 signals), page 572 (2 signals), page 573 (2 signals), page 577 (6 signals), page 578 (6 signals), page 579 (3 signals), page 585 (1 signals), page 586 (1 signals), page 587 (1 signals), page 588 (3 signals), page 590 (5 signals), page 591 (5 signals), page 592 (5 signals), page 593 (6 signals), page 594 (4 signals), page 595 (4 signals), page 596 (1 signals), page 597 (1 signals), page 599 (6 signals), page 605 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
