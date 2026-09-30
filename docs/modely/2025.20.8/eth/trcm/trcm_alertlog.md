---
layout: default
title: "TRCM_alertLog (0x512) — TRCM ECU, Tesla Model Y 2025.20.8 ETH"
description: "TRCM ECU message: alert log. Ethernet-side message TRCM_alertLog of TRCM ECU for Tesla Model Y firmware 2025.20.8, 334 signals (TRCM_alertID, TRCM_alertState, TRCM_a015_NVMMMemOverflow, TRCM_a015_NVMMFilesystemError and 330 more). Bit layout, scaling, units and value tables."
---

# TRCM_alertLog (0x512) — TRCM ECU, Tesla Model Y 2025.20.8 ETH

TRCM ECU message: alert log. This page documents the 334 signals of TRCM_alertLog as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TRCM_alertLog` |
| Ethernet-side id | 0x512 (1298) |
| ECU | [TRCM ECU](../../trcm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TRCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 334 |

## Signals of TRCM_alertLog

Tesla Model Y CAN bus signals in `TRCM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TRCM_alertID` | selector | TRCM ECU: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>7 = `a007_chassisChecksumError`<br>8 = `a008_chassisCounterError`<br>9 = `a009_partyChecksumError`<br>10 = `a010_partyCounterError`<br>12 = `a012_asm5TemperatureOutsideSignalRange`<br>13 = `a013_AlertManagerFault`<br>14 = `a014_asm3TemperatureOutsideSignalRange`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_asm5TemperatureOutsideOperatingRange`<br>18 = `a018_asm3TemperatureOutsideOperatingRange`<br>19 = `a019_Task500usError`<br>20 = `a020_asm3ComStatusError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>23 = `a023_asm3ArsStatusXError`<br>24 = `a024_asm3AccStatusError`<br>25 = `a025_CHCANBusFaults`<br>26 = `a026_airbagAsicDiagnosticFault`<br>27 = `a027_airbagAsicDeploymentDiagnosticFault`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>33 = `a033_HercLogCreated`<br>34 = `a034_apClipTrigger`<br>35 = `a035_hvDisconnectCommanded`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>65 = `a065_vSafingFetUnderVoltage`<br>66 = `a066_vBusAUnderVoltage`<br>67 = `a067_vBusBUnderVoltage`<br>68 = `a068_vBusCUnderVoltage`<br>69 = `a069_swAppBoot`<br>70 = `a070_asm3StatusError`<br>71 = `a071_asm3DeviceFaulted`<br>72 = `a072_ais2120StatusError`<br>73 = `a073_ais2120DeviceFaulted`<br>74 = `a074_ais2120SelfTestXPositiveFailed`<br>75 = `a075_ais2120SelfTestXNegativeFailed`<br>76 = `a076_ais2120SelfTestYPositiveFailed`<br>77 = `a077_ais2120SelfTestYNegativeFailed`<br>81 = `a081_autarkyActive`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_glacierInitialStatusFailure`<br>122 = `a122_glacierTraceabilityReadoutA0A0Failure`<br>123 = `a123_glacierTraceabilityReadoutB0B0Failure`<br>124 = `a124_glacierRegisterPatternWriteFailure`<br>125 = `a125_glacierFixedPatternSelfTestFailure`<br>126 = `a126_glacierSelfTestEFailure`<br>127 = `a127_glacierSelfTestFFailure`<br>128 = `a128_glacierAnalogSelfTestFailure`<br>129 = `a129_glacierOscillatorVerificationFailure`<br>130 = `a130_glacierFinalStatusFailure`<br>131 = `a131_glacierOffsetVerificationFailure`<br>132 = `a132_glacierNormalOperationFailure`<br>133 = `a133_glacierDeviceReset`<br>134 = `a134_glacierDeviceFaulted`<br>135 = `a135_asm5StatusError`<br>136 = `a136_asm5DeviceFaulted`<br>137 = `a137_ext1AsicSnoopTestFailed`<br>138 = `a138_ext2AsicSnoopTestFailed`<br>139 = `a139_disarmed`<br>140 = `a140_frontRightAccelInitFailure`<br>141 = `a141_frontRightAccelShortToGround`<br>142 = `a142_frontRightAccelShortToBattery`<br>143 = `a143_frontRightAccelConfigError`<br>144 = `a144_frontRightAccelOpen`<br>145 = `a145_frontRightAccelCommError`<br>146 = `a146_frontRightAccelSensorDefect`<br>147 = `a147_frontRightAccelSignalMonitor`<br>150 = `a150_rightFrontDoorPressureInitFailure`<br>151 = `a151_rightFrontDoorPressureShortToGround`<br>152 = `a152_rightFrontDoorPressureShortToBattery`<br>153 = `a153_rightFrontDoorPressureConfigError`<br>154 = `a154_rightFrontDoorPressureOpen`<br>155 = `a155_rightFrontDoorPressureCommError`<br>156 = `a156_rightFrontDoorPressureSensorDefect`<br>157 = `a157_rightFrontDoorPressureSignalMonitor`<br>160 = `a160_frontLeftAccelInitFailure`<br>161 = `a161_frontLeftAccelShortToGround`<br>162 = `a162_frontLeftAccelShortToBattery`<br>163 = `a163_frontLeftAccelConfigError`<br>164 = `a164_frontLeftAccelOpen`<br>165 = `a165_frontLeftAccelCommError`<br>166 = `a166_frontLeftAccelSensorDefect`<br>167 = `a167_frontLeftAccelSignalMonitor`<br>170 = `a170_leftFrontDoorPressureInitFailure`<br>171 = `a171_leftFrontDoorPressureShortToGround`<br>172 = `a172_leftFrontDoorPressureShortToBattery`<br>173 = `a173_leftFrontDoorPressureConfigError`<br>174 = `a174_leftFrontDoorPressureOpen`<br>175 = `a175_leftFrontDoorPressureCommError`<br>176 = `a176_leftFrontDoorPressureSensorDefect`<br>177 = `a177_leftFrontDoorPressureSignalMonitor`<br>180 = `a180_rightBPillarAccelInitFailure`<br>181 = `a181_rightBPillarAccelShortToGround`<br>182 = `a182_rightBPillarAccelShortToBattery`<br>183 = `a183_rightBPillarAccelConfigError`<br>184 = `a184_rightBPillarAccelOpen`<br>185 = `a185_rightBPillarAccelCommError`<br>186 = `a186_rightBPillarAccelSensorDefect`<br>187 = `a187_rightBPillarAccelSignalMonitor`<br>190 = `a190_leftBPillarAccelInitFailure`<br>191 = `a191_leftBPillarAccelShortToGround`<br>192 = `a192_leftBPillarAccelShortToBattery`<br>193 = `a193_leftBPillarAccelConfigError`<br>194 = `a194_leftBPillarAccelOpen`<br>195 = `a195_leftBPillarAccelCommError`<br>196 = `a196_leftBPillarAccelSensorDefect`<br>197 = `a197_leftBPillarAccelSignalMonitor`<br>200 = `a200_frontCenterAccelInitFailure`<br>201 = `a201_frontCenterAccelShortToGround`<br>202 = `a202_frontCenterAccelShortToBattery`<br>203 = `a203_frontCenterAccelConfigError`<br>204 = `a204_frontCenterAccelOpen`<br>205 = `a205_frontCenterAccelCommError`<br>206 = `a206_frontCenterAccelSensorDefect`<br>207 = `a207_frontCenterAccelSignalMonitor`<br>210 = `a210_leftCPillarAccelInitFailure`<br>211 = `a211_leftCPillarAccelShortToGround`<br>212 = `a212_leftCPillarAccelShortToBattery`<br>213 = `a213_leftCPillarAccelConfigError`<br>214 = `a214_leftCPillarAccelOpen`<br>215 = `a215_leftCPillarAccelCommError`<br>216 = `a216_leftCPillarAccelSensorDefect`<br>217 = `a217_leftCPillarAccelSignalMonitor`<br>220 = `a220_rightCPillarAccelInitFailure`<br>221 = `a221_rightCPillarAccelShortToGround`<br>222 = `a222_rightCPillarAccelShortToBattery`<br>223 = `a223_rightCPillarAccelConfigError`<br>224 = `a224_rightCPillarAccelOpen`<br>225 = `a225_rightCPillarAccelCommError`<br>226 = `a226_rightCPillarAccelSensorDefect`<br>227 = `a227_rightCPillarAccelSignalMonitor`<br>230 = `a230_leftRearDoorPressureInitFailure`<br>231 = `a231_leftRearDoorPressureShortToGround`<br>232 = `a232_leftRearDoorPressureShortToBattery`<br>233 = `a233_leftRearDoorPressureConfigError`<br>234 = `a234_leftRearDoorPressureOpen`<br>235 = `a235_leftRearDoorPressureCommError`<br>236 = `a236_leftRearDoorPressureSensorDefect`<br>237 = `a237_leftRearDoorPressureSignalMonitor`<br>240 = `a240_rightRearDoorPressureInitFailure`<br>241 = `a241_rightRearDoorPressureShortToGround`<br>242 = `a242_rightRearDoorPressureShortToBattery`<br>243 = `a243_rightRearDoorPressureConfigError`<br>244 = `a244_rightRearDoorPressureOpen`<br>245 = `a245_rightRearDoorPressureCommError`<br>246 = `a246_rightRearDoorPressureSensorDefect`<br>247 = `a247_rightRearDoorPressureSignalMonitor`<br>250 = `a250_frontCenterAccelXInitFailure`<br>251 = `a251_frontCenterAccelXShortToGround`<br>252 = `a252_frontCenterAccelXShortToBattery`<br>253 = `a253_frontCenterAccelXConfigError`<br>254 = `a254_frontCenterAccelXOpen`<br>255 = `a255_frontCenterAccelXCommError`<br>256 = `a256_frontCenterAccelXSensorDefect`<br>257 = `a257_frontCenterAccelXSignalMonitor`<br>260 = `a260_frontCenterAccelYInitFailure`<br>261 = `a261_frontCenterAccelYShortToGround`<br>262 = `a262_frontCenterAccelYShortToBattery`<br>263 = `a263_frontCenterAccelYConfigError`<br>264 = `a264_frontCenterAccelYOpen`<br>265 = `a265_frontCenterAccelYCommError`<br>266 = `a266_frontCenterAccelYSensorDefect`<br>267 = `a267_frontCenterAccelYSignalMonitor`<br>272 = `a272_asm5ComStatusError`<br>273 = `a273_asm5ArsStatusXError`<br>274 = `a274_asm5ArsStatusZError`<br>275 = `a275_asm5AccStatusError`<br>276 = `a276_watchdogStatus`<br>278 = `a278_safingEngine0Armed`<br>279 = `a279_safingEngine1Armed`<br>280 = `a280_safingEngine2Armed`<br>281 = `a281_safingEngine3Armed`<br>282 = `a282_safingEngine4Armed`<br>283 = `a283_safingEngine5Armed`<br>284 = `a284_safingEngine6Armed`<br>285 = `a285_safingEngine7Armed`<br>286 = `a286_safingEngine8Armed`<br>287 = `a287_safingEngine9Armed`<br>288 = `a288_safingEngine10Armed`<br>289 = `a289_safingEngine11Armed`<br>290 = `a290_safingEngine12Armed`<br>291 = `a291_safingEngine13Armed`<br>292 = `a292_safingEngine14Armed`<br>293 = `a293_safingEngine15Armed`<br>294 = `a294_safingEngine16Armed`<br>295 = `a295_safingEngine17Armed`<br>296 = `a296_safingEngine18Armed`<br>297 = `a297_safingEngine19Armed`<br>298 = `a298_safingEngine20Armed`<br>299 = `a299_safingEngine21Armed`<br>300 = `a300_unarmedAB1FPDeployCommand`<br>301 = `a301_unarmedAB1FDDeployCommand`<br>302 = `a302_unarmedAV1FPDeployCommand`<br>303 = `a303_unarmedFSABDeployCommand`<br>304 = `a304_unarmedAB2FPDeployCommand`<br>305 = `a305_unarmedAB2FDDeployCommand`<br>306 = `a306_unarmedAV1FDDeployCommand`<br>307 = `a307_unarmedLoop7DeployCommand`<br>308 = `a308_unarmedKA1FPDeployCommand`<br>309 = `a309_unarmedKA1FDDeployCommand`<br>310 = `a310_unarmedALLFRDeployCommand`<br>311 = `a311_unarmedALLFLDeployCommand`<br>312 = `a312_unarmedBT2FRDeployCommand`<br>313 = `a313_unarmedBT2FLDeployCommand`<br>314 = `a314_unarmedSA1FLDeployCommand`<br>315 = `a315_unarmedSA1FRDeployCommand`<br>316 = `a316_unarmedBT1RRDeployCommand`<br>317 = `a317_unarmedBT1RLDeployCommand`<br>318 = `a318_unarmedBT1FRDeployCommand`<br>319 = `a319_unarmedBT1FLDeployCommand`<br>320 = `a320_unarmedLoop20DeployCommand`<br>321 = `a321_unarmedLoop21DeployCommand`<br>322 = `a322_unarmedIC1FRDeployCommand`<br>323 = `a323_unarmedIC1FLDeployCommand`<br>324 = `a324_unarmedLoop24DeployCommand`<br>325 = `a325_unarmedLoop25DeployCommand`<br>326 = `a326_unarmedLoop26DeployCommand`<br>327 = `a327_unarmedLoop27DeployCommand`<br>328 = `a328_unarmedLoop28DeployCommand`<br>329 = `a329_unarmedLoop29DeployCommand`<br>330 = `a330_unarmedLoop30DeployCommand`<br>331 = `a331_unarmedLoop31DeployCommand`<br>332 = `a332_AB1FPDeployment`<br>333 = `a333_AB1FDDeployment`<br>334 = `a334_AV1FPDeployment`<br>335 = `a335_Loop3Deployment`<br>336 = `a336_AB2FPDeployment`<br>337 = `a337_AB2FDDeployment`<br>338 = `a338_AV1FDDeployment`<br>339 = `a339_Loop7Deployment`<br>340 = `a340_KA1FPDeployment`<br>341 = `a341_KA1FDDeployment`<br>342 = `a342_ALLFRDeployment`<br>343 = `a343_ALLFLDeployment`<br>344 = `a344_BT2FRDeployment`<br>345 = `a345_BT2FLDeployment`<br>346 = `a346_SA1FLDeployment`<br>347 = `a347_SA1FRDeployment`<br>348 = `a348_BT1RRDeployment`<br>349 = `a349_BT1RLDeployment`<br>350 = `a350_BT1FRDeployment`<br>351 = `a351_BT1FLDeployment`<br>352 = `a352_Loop20Deployment`<br>353 = `a353_Loop21Deployment`<br>354 = `a354_IC1FRDeployment`<br>355 = `a355_IC1FLDeployment`<br>356 = `a356_Loop24Deployment`<br>357 = `a357_Loop25Deployment`<br>358 = `a358_Loop26Deployment`<br>359 = `a359_Loop27Deployment`<br>360 = `a360_Loop28Deployment`<br>361 = `a361_Loop29Deployment`<br>362 = `a362_Loop30Deployment`<br>363 = `a363_Loop31Deployment`<br>364 = `a364_safingEngine0NoValidData`<br>365 = `a365_safingEngine1NoValidData`<br>366 = `a366_safingEngine2NoValidData`<br>367 = `a367_safingEngine3NoValidData`<br>368 = `a368_safingEngine4NoValidData`<br>369 = `a369_safingEngine5NoValidData`<br>370 = `a370_safingEngine6NoValidData`<br>371 = `a371_safingEngine7NoValidData`<br>372 = `a372_safingEngine8NoValidData`<br>373 = `a373_safingEngine9NoValidData`<br>374 = `a374_safingEngine10NoValidData`<br>375 = `a375_safingEngine11NoValidData`<br>376 = `a376_safingEngine12NoValidData`<br>377 = `a377_safingEngine13NoValidData`<br>378 = `a378_safingEngine14NoValidData`<br>379 = `a379_safingEngine15NoValidData`<br>380 = `a380_safingEngine16NoValidData`<br>381 = `a381_safingEngine17NoValidData`<br>382 = `a382_safingEngine18NoValidData`<br>383 = `a383_safingEngine19NoValidData`<br>384 = `a384_safingEngine20NoValidData`<br>385 = `a385_safingEngine21NoValidData`<br>387 = `a387_primaryAsicResetSource`<br>388 = `a388_cpuLoadHigh`<br>389 = `a389_asicPwrStatusError`<br>390 = `a390_systemAsicClockOrOperatingStateError`<br>391 = `a391_extAsic1ClockOrOperatingStateError`<br>392 = `a392_extAsic2ClockOrOperatingStateError`<br>393 = `a393_depAdcConvertRatioError`<br>394 = `a394_gspiGlobalStatusWordError`<br>395 = `a395_imuCalibrationNotDone`<br>396 = `a396_spiCommunicationProgramError`<br>397 = `a397_safingMonitorError`<br>398 = `a398_asicNvmReprogrammed`<br>400 = `a400_AB1FPShortToGround`<br>401 = `a401_AB1FPShortToBattery`<br>402 = `a402_AB1FPOpen`<br>403 = `a403_AB1FPShortToSelf`<br>404 = `a404_AB1FPCrossCoupled`<br>405 = `a405_AB1FPConfigError`<br>406 = `a406_AB1FDShortToGround`<br>407 = `a407_AB1FDShortToBattery`<br>408 = `a408_AB1FDOpen`<br>409 = `a409_AB1FDShortToSelf`<br>410 = `a410_AB1FDCrossCoupled`<br>411 = `a411_AB1FDConfigError`<br>412 = `a412_PAVShortToGround`<br>413 = `a413_PAVShortToBattery`<br>414 = `a414_PAVOpen`<br>415 = `a415_PAVShortToSelf`<br>416 = `a416_PAVCrossCoupled`<br>417 = `a417_PAVConfigError`<br>418 = `a418_AB2FPShortToGround`<br>419 = `a419_AB2FPShortToBattery`<br>420 = `a420_AB2FPOpen`<br>421 = `a421_AB2FPShortToSelf`<br>422 = `a422_AB2FPCrossCoupled`<br>423 = `a423_AB2FPConfigError`<br>424 = `a424_AB2FDShortToGround`<br>425 = `a425_AB2FDShortToBattery`<br>426 = `a426_AB2FDOpen`<br>427 = `a427_AB2FDShortToSelf`<br>428 = `a428_AB2FDCrossCoupled`<br>429 = `a429_AB2FDConfigError`<br>430 = `a430_DAVShortToGround`<br>431 = `a431_DAVShortToBattery`<br>432 = `a432_DAVOpen`<br>433 = `a433_DAVShortToSelf`<br>434 = `a434_DAVCrossCoupled`<br>435 = `a435_DAVConfigError`<br>436 = `a436_IKBFPShortToGround`<br>437 = `a437_IKBFPShortToBattery`<br>438 = `a438_IKBFPOpen`<br>439 = `a439_IKBFPShortToSelf`<br>440 = `a440_IKBFPCrossCoupled`<br>441 = `a441_IKBFPConfigError`<br>442 = `a442_IKBFDShortToGround`<br>443 = `a443_IKBFDShortToBattery`<br>444 = `a444_IKBFDOpen`<br>445 = `a445_IKBFDShortToSelf`<br>446 = `a446_IKBFDCrossCoupled`<br>447 = `a447_IKBFDConfigError`<br>448 = `a448_PLLShortToGround`<br>449 = `a449_PLLShortToBattery`<br>450 = `a450_PLLOpen`<br>451 = `a451_PLLShortToSelf`<br>452 = `a452_PLLCrossCoupled`<br>453 = `a453_PLLConfigError`<br>454 = `a454_DLLShortToGround`<br>455 = `a455_DLLShortToBattery`<br>456 = `a456_DLLOpen`<br>457 = `a457_DLLShortToSelf`<br>458 = `a458_DLLCrossCoupled`<br>459 = `a459_DLLConfigError`<br>460 = `a460_BTRP_RetractorShortToGround`<br>461 = `a461_BTRP_RetractorShortToBattery`<br>462 = `a462_BTRP_RetractorOpen`<br>463 = `a463_BTRP_RetractorShortToSelf`<br>464 = `a464_BTRP_RetractorCrossCoupled`<br>465 = `a465_BTRP_RetractorConfigError`<br>466 = `a466_BTRD_RetractorShortToGround`<br>467 = `a467_BTRD_RetractorShortToBattery`<br>468 = `a468_BTRD_RetractorOpen`<br>469 = `a469_BTRD_RetractorShortToSelf`<br>470 = `a470_BTRD_RetractorCrossCoupled`<br>471 = `a471_BTRD_RetractorConfigError`<br>472 = `a472_SA1FLShortToGround`<br>473 = `a473_SA1FLShortToBattery`<br>474 = `a474_SA1FLOpen`<br>475 = `a475_SA1FLShortToSelf`<br>476 = `a476_SA1FLCrossCoupled`<br>477 = `a477_SA1FLConfigError`<br>478 = `a478_SA1FRShortToGround`<br>479 = `a479_SA1FRShortToBattery`<br>480 = `a480_SA1FROpen`<br>481 = `a481_SA1FRShortToSelf`<br>482 = `a482_SA1FRCrossCoupled`<br>483 = `a483_SA1FRConfigError`<br>484 = `a484_BTRRShortToGround`<br>485 = `a485_BTRRShortToBattery`<br>486 = `a486_BTRROpen`<br>487 = `a487_BTRRShortToSelf`<br>488 = `a488_BTRRCrossCoupled`<br>489 = `a489_BTRRConfigError`<br>490 = `a490_BTRLShortToGround`<br>491 = `a491_BTRLShortToBattery`<br>492 = `a492_BTRLOpen`<br>493 = `a493_BTRLShortToSelf`<br>494 = `a494_BTRLCrossCoupled`<br>495 = `a495_BTRLConfigError`<br>496 = `a496_BTRP_AnchorShortToGround`<br>497 = `a497_BTRP_AnchorShortToBattery`<br>498 = `a498_BTRP_AnchorOpen`<br>499 = `a499_BTRP_AnchorShortToSelf`<br>500 = `a500_BTRP_AnchorCrossCoupled`<br>501 = `a501_BTRP_AnchorConfigError`<br>502 = `a502_BTRD_AnchorShortToGround`<br>503 = `a503_BTRD_AnchorShortToBattery`<br>504 = `a504_BTRD_AnchorOpen`<br>505 = `a505_BTRD_AnchorShortToSelf`<br>506 = `a506_BTRD_AnchorCrossCoupled`<br>507 = `a507_BTRD_AnchorConfigError`<br>508 = `a508_IC1FRShortToGround`<br>509 = `a509_IC1FRShortToBattery`<br>510 = `a510_IC1FROpen`<br>511 = `a511_IC1FRShortToSelf`<br>512 = `a512_IC1FRCrossCoupled`<br>513 = `a513_IC1FRConfigError`<br>514 = `a514_IC1FLShortToGround`<br>515 = `a515_IC1FLShortToBattery`<br>516 = `a516_IC1FLOpen`<br>517 = `a517_IC1FLShortToSelf`<br>518 = `a518_IC1FLCrossCoupled`<br>519 = `a519_IC1FLConfigError`<br>520 = `a520_FSABShortToGround`<br>521 = `a521_FSABShortToBattery`<br>522 = `a522_FSABOpen`<br>523 = `a523_FSABShortToSelf`<br>524 = `a524_FSABCrossCoupled`<br>525 = `a525_FSABConfigError`<br>544 = `a544_erCapDiagnosticsFailed`<br>545 = `a545_erCapBelowAutarkyThreshold`<br>546 = `a546_sensorValuesFaultedBySmart`<br>550 = `a550_AlgoWake_RCM_WAKE_FRONT`<br>551 = `a551_AlgoWake_RCM_WAKE_REAR`<br>552 = `a552_AlgoWake_RCM_WAKE_LEFT`<br>553 = `a553_AlgoWake_RCM_WAKE_RIGHT`<br>554 = `a554_AlgoWake_PAS_LH_PLAUSI_FRONT`<br>555 = `a555_AlgoWake_PAS_LH_PLAUSI_REAR`<br>556 = `a556_AlgoWake_PAS_LH_PLAUSI`<br>557 = `a557_AlgoWake_PAS_RH_PLAUSI_FRONT`<br>558 = `a558_AlgoWake_PAS_RH_PLAUSI_REAR`<br>559 = `a559_AlgoWake_PAS_RH_PLAUSI`<br>560 = `a560_AlgoWake_RCM_WAKE_ROLL_LEFT`<br>561 = `a561_AlgoWake_RCM_WAKE_ROLL_RIGHT`<br>562 = `a562_AlgoWake_RCM_AWAKE_FRONT`<br>563 = `a563_AlgoWake_RCM_AWAKE_REAR`<br>564 = `a564_AlgoWake_RCM_AWAKE_LEFT`<br>565 = `a565_AlgoWake_RCM_AWAKE_RIGHT`<br>566 = `a566_AlgoWake_RCM_AWAKE_ROLL`<br>567 = `a567_AlgoWake_RCM_AWAKE_X`<br>568 = `a568_AlgoWake_RCM_AWAKE_Y`<br>569 = `a569_AlgoWake_IMPACT_FINISH_X_FRONT`<br>570 = `a570_AlgoWake_IMPACT_FINISH_X_REAR`<br>571 = `a571_AlgoWake_IMPACT_FINISH_Y_RCM_POS`<br>572 = `a572_AlgoWake_IMPACT_FINISH_Y_RCM_NEG`<br>573 = `a573_AlgoWake_IMPACT_FINISH_Y_RCM`<br>574 = `a574_AlgoWake_IMPACT_FINISH_ROLL_RIGHT`<br>575 = `a575_AlgoWake_IMPACT_FINISH_ROLL_LEFT`<br>576 = `a576_AlgoWake_IMPACT_FINISH_X`<br>577 = `a577_AlgoWake_IMPACT_FINISH_Y`<br>578 = `a578_AlgoWake_IMPACT_FINISH_ROLL`<br>579 = `a579_AlgoWake_RCM_ENABLED_X`<br>580 = `a580_AlgoWake_RCM_ENABLED_Y`<br>581 = `a581_AlgoWake_RCM_ENABLED_ROLL`<br>582 = `a582_AlgoWake_RCM_AWAKE`<br>588 = `a588_yawRateOffsetPosLimit`<br>589 = `a589_yawRateOffsetNegLimit`<br>590 = `a590_pitchRateOffsetPosLimit`<br>591 = `a591_pitchRateOffsetNegLimit`<br>592 = `a592_rollRateOffsetPosLimit`<br>593 = `a593_rollRateOffsetNegLimit`<br>594 = `a594_longitudinalAccelOffsetPosLimit`<br>595 = `a595_longitudinalAccelOffsetNegLimit`<br>596 = `a596_lateralAccelOffsetPosLimit`<br>597 = `a597_lateralAccelOffsetNegLimit`<br>598 = `a598_verticalAccelOffsetPosLimit`<br>599 = `a599_verticalAccelOffsetNegLimit`<br>600 = `a600_airbagAsicStartupFailure`<br>601 = `a601_loop0AsicStartupDiagnosticFailure`<br>602 = `a602_loop1AsicStartupDiagnosticFailure`<br>603 = `a603_loop2AsicStartupDiagnosticFailure`<br>604 = `a604_loop3AsicStartupDiagnosticFailure`<br>605 = `a605_loop4AsicStartupDiagnosticFailure`<br>606 = `a606_loop5AsicStartupDiagnosticFailure`<br>607 = `a607_loop6AsicStartupDiagnosticFailure`<br>608 = `a608_loop7AsicStartupDiagnosticFailure`<br>609 = `a609_loop8AsicStartupDiagnosticFailure`<br>610 = `a610_loop9AsicStartupDiagnosticFailure`<br>611 = `a611_loop10AsicStartupDiagnosticFailure`<br>612 = `a612_loop11AsicStartupDiagnosticFailure`<br>613 = `a613_loop12AsicStartupDiagnosticFailure`<br>614 = `a614_loop13AsicStartupDiagnosticFailure`<br>615 = `a615_loop14AsicStartupDiagnosticFailure`<br>616 = `a616_loop15AsicStartupDiagnosticFailure`<br>617 = `a617_loop16AsicStartupDiagnosticFailure`<br>618 = `a618_loop17AsicStartupDiagnosticFailure`<br>619 = `a619_loop18AsicStartupDiagnosticFailure`<br>620 = `a620_loop19AsicStartupDiagnosticFailure`<br>621 = `a621_loop20AsicStartupDiagnosticFailure`<br>622 = `a622_loop21AsicStartupDiagnosticFailure`<br>623 = `a623_loop22AsicStartupDiagnosticFailure`<br>624 = `a624_loop23AsicStartupDiagnosticFailure`<br>625 = `a625_loop24AsicStartupDiagnosticFailure`<br>626 = `a626_loop25AsicStartupDiagnosticFailure`<br>627 = `a627_loop26AsicStartupDiagnosticFailure`<br>628 = `a628_loop27AsicStartupDiagnosticFailure`<br>629 = `a629_loop28AsicStartupDiagnosticFailure`<br>630 = `a630_loop29AsicStartupDiagnosticFailure`<br>631 = `a631_loop30AsicStartupDiagnosticFailure`<br>632 = `a632_loop31AsicStartupDiagnosticFailure` | plausible |
| `TRCM_alertState` |  | TRCM ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `TRCM_a015_NVMMMemOverflow` | page 15 | TRCM ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a015_NVMMFilesystemError` | page 15 | TRCM ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a015_NVMMRecordIDError` | page 15 | TRCM ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a088_VEH_temperature` | page 88 | TRCM ECU: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_thermalControl` | page 88 | TRCM ECU: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_torque` | page 88 | TRCM ECU: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_VEH_status` | page 88 | TRCM ECU: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_torque` | page 88 | TRCM ECU: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_status` | page 88 | TRCM ECU: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_temperature` | page 88 | TRCM ECU: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_PARTY_thermalControl` | page 88 | TRCM ECU: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a095_PT_ptNm` | page 95 | TRCM ECU: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a095_PT_status` | page 95 | TRCM ECU: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a096_VEH_status` | page 96 | TRCM ECU: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a096_CH_status` | page 96 | TRCM ECU: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a106_VEH_thermalInterface` | page 106 | TRCM ECU: a106 VEH thermal interface | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_VEH_dcdcRailStatus` | page 106 | TRCM ECU: a106 VEH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_CH_dcdcRailStatus` | page 106 | TRCM ECU: a106 CH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_CH_alertMatrix` | page 106 | TRCM ECU: a106 CH alert matrix | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_hvsNm` | page 107 | TRCM ECU: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_vehNm` | page 107 | TRCM ECU: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_status` | page 107 | TRCM ECU: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_thermalStatus` | page 107 | TRCM ECU: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_thermalStatus2` | page 107 | TRCM ECU: a107 VEH thermal status2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_bmbMinMax` | page 107 | TRCM ECU: a107 VEH bmb min max | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_powerAvailable` | page 107 | TRCM ECU: a107 VEH power available | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_ptNm` | page 107 | TRCM ECU: a107 PT pt nm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_status` | page 107 | TRCM ECU: a107 PT status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_thermalStatus` | page 107 | TRCM ECU: a107 PT thermal status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_PT_socStatus` | page 107 | TRCM ECU: a107 PT soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_socStatus` | page 107 | TRCM ECU: a107 VEH soc status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_packConfig` | page 107 | TRCM ECU: a107 VEH pack config | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_energyStatus` | page 107 | TRCM ECU: a107 VEH energy status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_VEH_chargeInfo` | page 107 | TRCM ECU: a107 VEH charge info | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a109_PARTY_status` | page 109 | TRCM ECU: a109 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_PARTY_inertial2` | page 109 | TRCM ECU: a109 PARTY inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_PARTY_nearDeploy` | page 109 | TRCM ECU: a109 PARTY near deploy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_PARTY_collision` | page 109 | TRCM ECU: a109 PARTY collision | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_VEH_status` | page 109 | TRCM ECU: a109 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_VEH_imuOffsets` | page 109 | TRCM ECU: a109 VEH imu offsets | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_PARTY_inertial1` | page 109 | TRCM ECU: a109 PARTY inertial1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_BDY_imuOffsets` | page 109 | TRCM ECU: a109 BDY imu offsets | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_BDY_inertial1` | page 109 | TRCM ECU: a109 BDY inertial1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_BDY_inertial2` | page 109 | TRCM ECU: a109 BDY inertial2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_BDY_status` | page 109 | TRCM ECU: a109 BDY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_VEH_inertial1` | page 109 | TRCM ECU: a109 VEH inertial1 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_VEH_inertial2` | page 109 | TRCM ECU: a109 VEH inertial2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_CH_inertial1` | page 109 | TRCM ECU: a109 CH inertial1 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_CH_inertial2` | page 109 | TRCM ECU: a109 CH inertial2 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_CH_status` | page 109 | TRCM ECU: a109 CH status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a120_PT_systemPower` | page 120 | TRCM ECU: a120 PT system power | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_stalklessInterfaces` | page 120 | TRCM ECU: a120 PARTY stalkless interfaces | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_CH_speed` | page 120 | TRCM ECU: a120 CH speed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_estimatedBrakeTemp` | page 120 | TRCM ECU: a120 VEH estimated brake temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_prndControl` | page 120 | TRCM ECU: a120 PARTY prnd control | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_PARTY_locStatus2` | page 120 | TRCM ECU: a120 PARTY loc status2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_chassisCntl` | page 120 | TRCM ECU: a120 VEH chassis cntl | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_locStatus` | page 120 | TRCM ECU: a120 VEH loc status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_locStatus2` | page 120 | TRCM ECU: a120 VEH loc status2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_prndControl` | page 120 | TRCM ECU: a120 VEH prnd control | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_VEH_vehicleEstimates` | page 120 | TRCM ECU: a120 VEH vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`TRCM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (8 signals), page 88 (8 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (2 signals), page 95 (2 signals), page 96 (2 signals), page 98 (12 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (6 signals), page 107 (15 signals), page 108 (11 signals), page 109 (16 signals), page 110 (16 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (21 signals), page 117 (23 signals), page 118 (28 signals), page 119 (6 signals), page 120 (27 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TRCM ECU messages (TRCM)](../../trcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
