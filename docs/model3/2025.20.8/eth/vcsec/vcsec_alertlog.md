---
layout: default
title: "VCSEC_alertLog (0x530) — Vehicle security controller, Tesla Model 3 2025.20.8 ETH"
description: "Vehicle security controller message: alert log. Ethernet-side message VCSEC_alertLog of Vehicle security controller for Tesla Model 3 firmware 2025.20.8, 453 signals (VCSEC_alertID, VCSEC_alertState, VCSEC_a001_InternalWatchdog, VCSEC_a002_CPUUndervoltage and 449 more). Bit layout, scaling, units and value tables."
---

# VCSEC_alertLog (0x530) — Vehicle security controller, Tesla Model 3 2025.20.8 ETH

Vehicle security controller message: alert log. This page documents the 453 signals of VCSEC_alertLog as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_alertLog` |
| Ethernet-side id | 0x530 (1328) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 453 |

## Signals of VCSEC_alertLog

Tesla Model 3 CAN bus signals in `VCSEC_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_alertID` | selector | Vehicle security controller: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>10 = `a010_ExtSupplyVoltError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>17 = `a017_NVMMStatusDbg`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>121 = `a121_ICR_MIA`<br>133 = `a133_alarmTriggered`<br>134 = `a134_noVINLoaded`<br>135 = `a135_centerEndpointBusy`<br>136 = `a136_leftEndpointBusy`<br>137 = `a137_rightEndpointBusy`<br>138 = `a138_rearEndpointBusy`<br>140 = `a140_nfcAuthentication`<br>141 = `a141_tooFewKeysOnWhitelist`<br>142 = `a142_bleGattAlertC`<br>143 = `a143_bleGattAlertL`<br>144 = `a144_bleGattAlertR`<br>145 = `a145_bleGattAlertRe`<br>147 = `a147_protobufRXTimeout`<br>148 = `a148_keyWhitelistFull`<br>149 = `a149_attrsWentMissingL`<br>150 = `a150_attrsWentMissingR`<br>151 = `a151_attrsWentMissingRe`<br>153 = `a153_srvcCmdTimeoutC`<br>154 = `a154_srvcCmdTimeoutL`<br>155 = `a155_srvcCmdTimeoutR`<br>156 = `a156_srvcCmdTimeoutRe`<br>158 = `a158_hciDebugC`<br>159 = `a159_hciDebugL`<br>161 = `a161_hciDebugR`<br>162 = `a162_hciDebugRe`<br>164 = `a164_attrsWentMissingC`<br>165 = `a165_ephemeralKeyGenerated`<br>166 = `a166_BLECenterPowerCycled`<br>167 = `a167_BLECenterSoftReset`<br>168 = `a168_BLELeftSoftReset`<br>169 = `a169_BLERightSoftReset`<br>170 = `a170_BLERearSoftReset`<br>172 = `a172_BLEUnexpectedResetC`<br>173 = `a173_BLEUnexpectedResetL`<br>174 = `a174_BLEUnexpectedResetRi`<br>175 = `a175_BLEUnexpectedResetRe`<br>177 = `a177_whitelistAddedKey`<br>178 = `a178_whitelistRemovedKey`<br>179 = `a179_wlistChangedRole`<br>180 = `a180_wlistRemovedPermission`<br>181 = `a181_signedMessageFault`<br>182 = `a182_cryptoHighStackUsage`<br>183 = `a183_centerEndpointRFMia`<br>184 = `a184_driverEndpointRFMia`<br>185 = `a185_passengerEndpointRFMia`<br>186 = `a186_rearEndpointRFMia`<br>187 = `a187_badConnectionDropped`<br>188 = `a188_protobufDecodeError`<br>189 = `a189_protoExpLengthTooLarge`<br>190 = `a190_protoTooManyBytes`<br>191 = `a191_macIDWlistingFailedC`<br>192 = `a192_macIDWlistingFailedL`<br>193 = `a193_macIDWlistingFailedRi`<br>194 = `a194_macIDWlistingFailedRe`<br>195 = `a195_keyMissingInDrive`<br>196 = `a196_protobufTXTimeout`<br>197 = `a197_indicationFault`<br>198 = `a198_BPillarNFCReaderMIA`<br>199 = `a199_CenterNFCReaderMIA`<br>200 = `a200_centerEndpointLostComm`<br>201 = `a201_leftEndpointLostComm`<br>202 = `a202_rightEndpointLostComm`<br>203 = `a203_rearEndpointLostComm`<br>204 = `a204_SharedSecretsWritten`<br>205 = `a205_MTUUpdateNotConfirmed`<br>206 = `a206_BLELeftAssertFailure`<br>207 = `a207_BLERightAssertFailure`<br>208 = `a208_BLERearAssertFailure`<br>209 = `a209_BLECenterAssertFailure`<br>210 = `a210_keyDeviceBatteryLow`<br>211 = `a211_handlePullWithoutAuth`<br>212 = `a212_snifferRSSIMIA`<br>213 = `a213_gattTimeoutWithExptdCount`<br>214 = `a214_gattServFalseWaitToBoot`<br>215 = `a215_TPMSUnexpectedDisconnectSensor0`<br>216 = `a216_TPMSUnexpectedDisconnectSensor1`<br>217 = `a217_TPMSUnexpectedDisconnectSensor2`<br>218 = `a218_TPMSUnexpectedDisconnectSensor3`<br>219 = `a219_TPMSSensorPairingRemoved`<br>220 = `a220_TPMSSensorPairingNotCompleted`<br>221 = `a221_TPMSSoftWarning`<br>222 = `a222_TPMSSystemMalfunction`<br>223 = `a223_TPMSFaultSensor0`<br>224 = `a224_TPMSFaultSensor1`<br>225 = `a225_TPMSFaultSensor2`<br>226 = `a226_TPMSFaultSensor3`<br>227 = `a227_connectionWithoutLinkEvent`<br>228 = `a228_TPMSHardWarning`<br>235 = `a235_presentWithoutHandlePull`<br>236 = `a236_keyIdentificationMaxAttemptReached`<br>237 = `a237_keyNotReadyToReceiveIDRequests`<br>238 = `a238_TPMSLocationsUpdated`<br>239 = `a239_TPMSIdleConnection`<br>240 = `a240_noKeysPaired`<br>241 = `a241_TPMSUpdateStartedSensor0`<br>242 = `a242_TPMSUpdateStartedSensor1`<br>243 = `a243_TPMSUpdateStartedSensor2`<br>244 = `a244_TPMSUpdateStartedSensor3`<br>245 = `a245_TPMSUpdateInterruptedSensor0`<br>246 = `a246_TPMSUpdateInterruptedSensor1`<br>247 = `a247_TPMSUpdateInterruptedSensor2`<br>248 = `a248_TPMSUpdateInterruptedSensor3`<br>249 = `a249_TPMSUpdateCompleteSensor0`<br>250 = `a250_TPMSUpdateCompleteSensor1`<br>251 = `a251_TPMSUpdateCompleteSensor2`<br>252 = `a252_TPMSUpdateCompleteSensor3`<br>253 = `a253_TPMSLowBattery`<br>254 = `a254_whitelistUpdatedKey`<br>255 = `a255_wlistUpdatedPermission`<br>256 = `a256_whitelistOperationFail`<br>257 = `a257_connectedKeyIsExpiring`<br>258 = `a258_keyIsExpiring`<br>260 = `a260_prsntPhoneKeyDisconnected`<br>261 = `a261_TPMSFactoryLearnActive`<br>262 = `a262_flowControlBackedUp`<br>263 = `a263_dispatchCouldNotBeCompleted`<br>264 = `a264_noOnePopulatedMessage`<br>265 = `a265_tooManyPopulatedMessage`<br>266 = `a266_TPMSSoftWarningFrontLeft`<br>267 = `a267_TPMSSoftWarningFrontRight`<br>268 = `a268_TPMSSoftWarningRearLeft`<br>269 = `a269_TPMSSoftWarningRearRight`<br>270 = `a270_TPMSHardWarningFrontLeft`<br>271 = `a271_TPMSHardWarningFrontRight`<br>272 = `a272_TPMSHardWarningRearLeft`<br>273 = `a273_TPMSHardWarningRearRight`<br>274 = `a274_handlePullWithoutAuth2`<br>275 = `a275_childSeatNotConnectedAtStartOfDrive`<br>276 = `a276_childSeatNotConnectedAtEndOfDrive`<br>277 = `a277_childSeatBatteryIsLow`<br>300 = `a300_scheduleItKeyAdded`<br>301 = `a301_imposterDetected`<br>302 = `a302_unfused`<br>303 = `a303_KeyfobUpdateInterrupted`<br>304 = `a304_KeyfobUpdateComplete`<br>305 = `a305_ATTFlowControlViolatedC`<br>306 = `a306_KeyfobAdvReceivedWhileConnected`<br>307 = `a307_ATTTimeout`<br>308 = `a308_NonConnectableAdvReceived`<br>309 = `a309_serviceKeyConditionsNotMet`<br>310 = `a310_uhfChargePortFilterFalsePositive`<br>311 = `a311_moreThanThreeKeysPresent`<br>312 = `a312_unexpectedBLEDisconnect`<br>315 = `a315_bleBondingEvent`<br>316 = `a316_ltkRequestRejected`<br>401 = `a401_rearLeftEndpointLostComm`<br>402 = `a402_rearRightEndpointLostComm`<br>404 = `a404_NFCCradleEndpointLostComm`<br>406 = `a406_hciDebugRL`<br>407 = `a407_hciDebugRR`<br>408 = `a408_hciDebugNFCC`<br>411 = `a411_leftRearEndpointBusy`<br>412 = `a412_rightRearEndpointBusy`<br>413 = `a413_NFCCradleEndpointBusy`<br>416 = `a416_BLECradleNFCSoftReset`<br>417 = `a417_BLERearLeftSoftReset`<br>418 = `a418_BLERearRightSoftReset`<br>420 = `a420_BLEUnexpectedResetNFCCradle`<br>421 = `a421_BLEUnexpectedResetRL`<br>422 = `a422_BLEUnexpectedResetRR`<br>425 = `a425_BLENFCCradleAssertFailure`<br>426 = `a426_BLERearLeftAssertFailure`<br>427 = `a427_BLERearRightAssertFailure`<br>428 = `a428_UWBCenterUpdateInterrupted`<br>429 = `a429_UWBLeftUpdateInterrupted`<br>430 = `a430_UWBRightUpdateInterrupted`<br>432 = `a432_UWBRearLeftUpdateInterrupted`<br>433 = `a433_UWBRearRightUpdateInterrupted`<br>434 = `a434_UWBRadioConfigUpdated`<br>435 = `a435_NFCCardPresentWhileCharging`<br>436 = `a436_uhfHWDoesNotMatchCountry`<br>437 = `a437_NearbyInteractionFailure`<br>438 = `a438_UWBRearUpdateInterrupted`<br>453 = `a453_passiveDisabled`<br>454 = `a454_TPMSOverPressureWarning`<br>455 = `a455_TPMSOverPressureWarningFrontLeft`<br>456 = `a456_TPMSOverPressureWarningFrontRight`<br>457 = `a457_TPMSOverPressureWarningRearLeft`<br>458 = `a458_TPMSOverPressureWarningRearRight`<br>459 = `a459_TPMSCertCheckFailedSensor0`<br>460 = `a460_TPMSCertCheckFailedSensor1`<br>461 = `a461_TPMSCertCheckFailedSensor2`<br>462 = `a462_TPMSCertCheckFailedSensor3`<br>465 = `a465_UWBRearLeftKeyVerificationFailure`<br>466 = `a466_UWBRearRightKeyVerificationFailure`<br>467 = `a467_UWBCenterKeyVerificationFailure`<br>468 = `a468_UWBRearKeyVerificationFailure`<br>469 = `a469_UWBLeftKeyVerificationFailure`<br>470 = `a470_UWBRightKeyVerificationFailure`<br>472 = `a472_peerRemovedInformation`<br>473 = `a473_handlePullWithoutAuth3`<br>474 = `a474_handlePullWithoutAuth4`<br>475 = `a475_handlePullWithoutAuth5`<br>476 = `a476_handlePullWithoutAuth6`<br>477 = `a477_phoneStartedBonding`<br>478 = `a478_handlePullWithoutAuth7`<br>479 = `a479_handlePullWithoutAuthNIStateDev0`<br>480 = `a480_handlePullWithoutAuthNIStateDev1`<br>481 = `a481_handlePullWithoutAuthNIStateDev2`<br>482 = `a482_VINChanged`<br>483 = `a483_highThermalGradiantDetected`<br>484 = `a484_UWBLeftUpdateTriggered`<br>485 = `a485_UWBCenterUpdateTriggered`<br>486 = `a486_UWBRightUpdateTriggered`<br>487 = `a487_unrecognizedProto`<br>488 = `a488_FiraRangingRejected`<br>489 = `a489_UWBRearLeftUpdateTriggered`<br>490 = `a490_UWBRearRightUpdateTriggered`<br>494 = `a494_UWBRearUpdateTriggered`<br>495 = `a495_handlePullWithoutAuth_iOS`<br>496 = `a496_handlePullWithoutAuth_Android`<br>497 = `a497_incorrectEndpointInstallation`<br>498 = `a498_TPMSFeature0Reached`<br>499 = `a499_TPMSAssertFailure0`<br>500 = `a500_TPMSAssertFailure1`<br>501 = `a501_TPMSAssertFailure2`<br>502 = `a502_TPMSAssertFailure3`<br>503 = `a503_canAuthenticationFailure`<br>510 = `a510_watchKeyOffWrist`<br>511 = `a511_phoneKeyStationary`<br>512 = `a512_dummyAlertMax` | plausible |
| `VCSEC_alertState` |  | Vehicle security controller: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCSEC_a001_InternalWatchdog` | page 1 | Vehicle security controller: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a002_CPUUndervoltage` | page 2 | Vehicle security controller: a002 CPU undervoltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a002_PowerOnReset` | page 2 | Vehicle security controller: a002 power on reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a010_UnderVoltageDetected` | page 10 | Vehicle security controller: a010 under voltage detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a010_UnderVoltageTimeout` | page 10 | Vehicle security controller: a010 under voltage timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a015_NVMMMemOverflow` | page 15 | Vehicle security controller: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a015_NVMMFilesystemError` | page 15 | Vehicle security controller: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a015_NVMMRecordIDError` | page 15 | Vehicle security controller: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a057_VEH_cpControl` | page 57 | Vehicle security controller: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a059_voltageDrop` | page 59 | Vehicle security controller: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCSEC_a059_resistanceEstimate` | page 59 | Vehicle security controller: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCSEC_a059_current` | page 59 | Vehicle security controller: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCSEC_a063_switchChannel` | page 63 | Vehicle security controller: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a063_switchType` | page 63 | Vehicle security controller: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a063_ADCVoltage` | page 63 | Vehicle security controller: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCSEC_a063_disconnected` | page 63 | Vehicle security controller: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a063_indeterminate` | page 63 | Vehicle security controller: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a063_stuckActive` | page 63 | Vehicle security controller: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a063_faulted` | page 63 | Vehicle security controller: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a082_RIPC_epbPrivateState` | page 82 | Vehicle security controller: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a082_RIPC_remoteHSD` | page 82 | Vehicle security controller: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a082_RIPC_railStatus` | page 82 | Vehicle security controller: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a082_RIPC_remoteMux` | page 82 | Vehicle security controller: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a083_LIPC_epbPrivateState` | page 83 | Vehicle security controller: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a083_LIPC_remoteHSD` | page 83 | Vehicle security controller: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a083_LIPC_railStatus` | page 83 | Vehicle security controller: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a083_LIPC_HSDFaults` | page 83 | Vehicle security controller: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a084_CH_StatusC` | page 84 | Vehicle security controller: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a085_PARTY_buttonStatus` | page 85 | Vehicle security controller: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_LVBMS_statusHigh` | page 86 | Vehicle security controller: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_LVBMS_statusLow` | page 86 | Vehicle security controller: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_status` | page 86 | Vehicle security controller: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_12VBatteryStatus` | page 86 | Vehicle security controller: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_LVPowerState` | page 86 | Vehicle security controller: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_lightStatus` | page 86 | Vehicle security controller: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_systemStatus` | page 86 | Vehicle security controller: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_thermalStatus` | page 86 | Vehicle security controller: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VEH_vehNm` | page 86 | Vehicle security controller: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_VEH_temperature` | page 87 | Vehicle security controller: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_VEH_thermalControl` | page 87 | Vehicle security controller: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_VEH_torque` | page 87 | Vehicle security controller: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_VEH_status` | page 87 | Vehicle security controller: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_PARTY_torque` | page 87 | Vehicle security controller: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_PARTY_status` | page 87 | Vehicle security controller: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_PARTY_temperature` | page 87 | Vehicle security controller: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_PARTY_thermalControl` | page 87 | Vehicle security controller: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_VEH_temperature` | page 88 | Vehicle security controller: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_VEH_thermalControl` | page 88 | Vehicle security controller: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_VEH_torque` | page 88 | Vehicle security controller: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_VEH_status` | page 88 | Vehicle security controller: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_PARTY_torque` | page 88 | Vehicle security controller: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_PARTY_status` | page 88 | Vehicle security controller: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_PARTY_temperature` | page 88 | Vehicle security controller: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_PARTY_thermalControl` | page 88 | Vehicle security controller: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_PARTY_party1` | page 89 | Vehicle security controller: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_PARTY_status` | page 89 | Vehicle security controller: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_VEH_status` | page 89 | Vehicle security controller: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_BDY_party1` | page 89 | Vehicle security controller: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_BDY_status` | page 89 | Vehicle security controller: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_CH_status` | page 89 | Vehicle security controller: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_CH_party1` | page 89 | Vehicle security controller: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_CH_party3` | page 89 | Vehicle security controller: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_VEH_party1` | page 89 | Vehicle security controller: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_VEH_party3` | page 89 | Vehicle security controller: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a091_VEH_faultsAndExtras` | page 91 | Vehicle security controller: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a091_VEH_info` | page 91 | Vehicle security controller: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a091_VEH_state` | page 91 | Vehicle security controller: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a092_VEH_restraintStatus` | page 92 | Vehicle security controller: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a092_VEH_switchStatus` | page 92 | Vehicle security controller: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a092_VEH_seatStatus2` | page 92 | Vehicle security controller: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a092_VEH_vehNm` | page 92 | Vehicle security controller: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a093_VEH_restraintStatus` | page 93 | Vehicle security controller: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a093_VEH_switchStatus` | page 93 | Vehicle security controller: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a093_VEH_seatStatus2` | page 93 | Vehicle security controller: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a093_VEH_vehNm` | page 93 | Vehicle security controller: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a094_VEH_sysStatus` | page 94 | Vehicle security controller: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a094_PARTY_sysStatus` | page 94 | Vehicle security controller: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a095_PT_ptNm` | page 95 | Vehicle security controller: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a095_PT_status` | page 95 | Vehicle security controller: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a096_VEH_status` | page 96 | Vehicle security controller: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a096_CH_status` | page 96 | Vehicle security controller: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_CH_torque` | page 98 | Vehicle security controller: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_VEH_hvStatus` | page 98 | Vehicle security controller: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_VEH_status` | page 98 | Vehicle security controller: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_VEH_thermalControl` | page 98 | Vehicle security controller: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_VEH_temperature` | page 98 | Vehicle security controller: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_VEH_torque` | page 98 | Vehicle security controller: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PARTY_status` | page 98 | Vehicle security controller: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PARTY_temperature` | page 98 | Vehicle security controller: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PARTY_thermalControl` | page 98 | Vehicle security controller: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PARTY_torque` | page 98 | Vehicle security controller: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PT_thermalControl` | page 98 | Vehicle security controller: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_PT_temperature` | page 98 | Vehicle security controller: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a099_VEH_oocStatus` | page 99 | Vehicle security controller: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_VEH` | page 100 | Vehicle security controller: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_PARTY` | page 100 | Vehicle security controller: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_PT` | page 100 | Vehicle security controller: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_CH` | page 100 | Vehicle security controller: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_OBD` | page 100 | Vehicle security controller: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_VEH_state` | page 101 | Vehicle security controller: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_PARTY_locState` | page 101 | Vehicle security controller: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_LIPC_externalWatchdogHeartBeat` | page 101 | Vehicle security controller: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_VEH_locState` | page 101 | Vehicle security controller: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_BDY_locState` | page 101 | Vehicle security controller: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a102_VEH_faultsAndExtras` | page 102 | Vehicle security controller: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a102_VEH_feedbackStatus` | page 102 | Vehicle security controller: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a102_VEH_sensorStatus` | page 102 | Vehicle security controller: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a102_VEH_rods` | page 102 | Vehicle security controller: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_VEH_hvsNm` | page 103 | Vehicle security controller: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_VEH_vehNm` | page 103 | Vehicle security controller: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_VEH_status` | page 103 | Vehicle security controller: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_PT_ptNm` | page 103 | Vehicle security controller: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_PT_status` | page 103 | Vehicle security controller: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_VEH_evseStatus` | page 103 | Vehicle security controller: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a105_VEH_states` | page 105 | Vehicle security controller: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a105_VEH_chNm` | page 105 | Vehicle security controller: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a105_VEH_dampingStates` | page 105 | Vehicle security controller: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_VEH_dcdcStatus` | page 106 | Vehicle security controller: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_VEH_thermalControl` | page 106 | Vehicle security controller: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_VEH_thermalInterface` | page 106 | Vehicle security controller: a106 VEH thermal interface | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_VEH_dcdcRailStatus` | page 106 | Vehicle security controller: a106 VEH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_CH_dcdcRailStatus` | page 106 | Vehicle security controller: a106 CH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_CH_alertMatrix` | page 106 | Vehicle security controller: a106 CH alert matrix | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_hvsNm` | page 107 | Vehicle security controller: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_vehNm` | page 107 | Vehicle security controller: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_status` | page 107 | Vehicle security controller: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_thermalStatus` | page 107 | Vehicle security controller: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_thermalStatus2` | page 107 | Vehicle security controller: a107 VEH thermal status2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_bmbMinMax` | page 107 | Vehicle security controller: a107 VEH bmb min max | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_powerAvailable` | page 107 | Vehicle security controller: a107 VEH power available | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_PT_ptNm` | page 107 | Vehicle security controller: a107 PT pt nm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_PT_status` | page 107 | Vehicle security controller: a107 PT status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_PT_thermalStatus` | page 107 | Vehicle security controller: a107 PT thermal status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_PT_socStatus` | page 107 | Vehicle security controller: a107 PT soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_socStatus` | page 107 | Vehicle security controller: a107 VEH soc status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_packConfig` | page 107 | Vehicle security controller: a107 VEH pack config | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_energyStatus` | page 107 | Vehicle security controller: a107 VEH energy status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_VEH_chargeInfo` | page 107 | Vehicle security controller: a107 VEH charge info | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_VEH_hvStatus` | page 108 | Vehicle security controller: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_VEH_temperature` | page 108 | Vehicle security controller: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_VEH_thermalControl` | page 108 | Vehicle security controller: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_VEH_torque` | page 108 | Vehicle security controller: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_VEH_status` | page 108 | Vehicle security controller: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PARTY_torque` | page 108 | Vehicle security controller: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PARTY_status` | page 108 | Vehicle security controller: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PARTY_temperature` | page 108 | Vehicle security controller: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PARTY_thermalControl` | page 108 | Vehicle security controller: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PT_temperature` | page 108 | Vehicle security controller: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_PT_thermalControl` | page 108 | Vehicle security controller: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_PARTY_status` | page 109 | Vehicle security controller: a109 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_PARTY_inertial2` | page 109 | Vehicle security controller: a109 PARTY inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_PARTY_nearDeploy` | page 109 | Vehicle security controller: a109 PARTY near deploy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_PARTY_collision` | page 109 | Vehicle security controller: a109 PARTY collision | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_VEH_status` | page 109 | Vehicle security controller: a109 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_VEH_imuOffsets` | page 109 | Vehicle security controller: a109 VEH imu offsets | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_PARTY_inertial1` | page 109 | Vehicle security controller: a109 PARTY inertial1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_BDY_imuOffsets` | page 109 | Vehicle security controller: a109 BDY imu offsets | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_BDY_inertial1` | page 109 | Vehicle security controller: a109 BDY inertial1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_BDY_inertial2` | page 109 | Vehicle security controller: a109 BDY inertial2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_BDY_status` | page 109 | Vehicle security controller: a109 BDY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_VEH_inertial1` | page 109 | Vehicle security controller: a109 VEH inertial1 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_VEH_inertial2` | page 109 | Vehicle security controller: a109 VEH inertial2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_CH_inertial1` | page 109 | Vehicle security controller: a109 CH inertial1 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_CH_inertial2` | page 109 | Vehicle security controller: a109 CH inertial2 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_CH_status` | page 109 | Vehicle security controller: a109 CH status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_carState` | page 110 | Vehicle security controller: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_carConfig` | page 110 | Vehicle security controller: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_time` | page 110 | Vehicle security controller: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_updateStatus` | page 110 | Vehicle security controller: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_vehNm` | page 110 | Vehicle security controller: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_mismatchFault` | page 110 | Vehicle security controller: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_vin` | page 110 | Vehicle security controller: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_bmpDebug` | page 110 | Vehicle security controller: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_gearControl` | page 110 | Vehicle security controller: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_VEH_canLogAvailability` | page 110 | Vehicle security controller: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_airbagCutoffStatus` | page 110 | Vehicle security controller: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_carConfig` | page 110 | Vehicle security controller: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_carState` | page 110 | Vehicle security controller: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_vin` | page 110 | Vehicle security controller: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_chNm` | page 110 | Vehicle security controller: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_CH_epochTimeGtw` | page 110 | Vehicle security controller: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_VEH_internalStatus` | page 111 | Vehicle security controller: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_VEH_status` | page 111 | Vehicle security controller: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_VEH_vehNm` | page 111 | Vehicle security controller: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_RIPC_LVPowerState` | page 111 | Vehicle security controller: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_RIPC_epbPrivateState` | page 111 | Vehicle security controller: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_RIPC_railStatus` | page 111 | Vehicle security controller: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_RIPC_remoteADC` | page 111 | Vehicle security controller: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_RIPC_switchStatus` | page 111 | Vehicle security controller: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_VEH_LVPowerState` | page 111 | Vehicle security controller: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_VEH_seatStatus` | page 111 | Vehicle security controller: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_PARTY_status` | page 111 | Vehicle security controller: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_CH_status` | page 111 | Vehicle security controller: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_VEH_internalStatus` | page 112 | Vehicle security controller: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_VEH_status` | page 112 | Vehicle security controller: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_VEH_vehNm` | page 112 | Vehicle security controller: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_LIPC_LVPowerState` | page 112 | Vehicle security controller: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_LIPC_epbPrivateState` | page 112 | Vehicle security controller: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_LIPC_railStatus` | page 112 | Vehicle security controller: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_LIPC_remoteADC` | page 112 | Vehicle security controller: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_LIPC_switchStatus` | page 112 | Vehicle security controller: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_VEH_LVPowerState` | page 112 | Vehicle security controller: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_PARTY_status` | page 112 | Vehicle security controller: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_CH_status` | page 112 | Vehicle security controller: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_status` | page 114 | Vehicle security controller: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_wheelSpeeds` | page 114 | Vehicle security controller: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_VEH_wheelSpeeds` | page 114 | Vehicle security controller: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_CH_wheelSpeeds` | page 114 | Vehicle security controller: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_party3` | page 114 | Vehicle security controller: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_VEH_party3` | page 114 | Vehicle security controller: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_VEH_status` | page 114 | Vehicle security controller: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_wheelRotation` | page 114 | Vehicle security controller: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_CH_wheelRotation` | page 114 | Vehicle security controller: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_VEH_wheelRotation` | page 114 | Vehicle security controller: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_brakeTorque` | page 114 | Vehicle security controller: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_PARTY_offsets` | page 114 | Vehicle security controller: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_BDY_offsets` | page 114 | Vehicle security controller: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_BDY_party3` | page 114 | Vehicle security controller: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_BDY_status` | page 114 | Vehicle security controller: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_BDY_wheelRotation` | page 114 | Vehicle security controller: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_BDY_wheelSpeeds` | page 114 | Vehicle security controller: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_CH_party1` | page 114 | Vehicle security controller: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_CH_party3` | page 114 | Vehicle security controller: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_CH_status` | page 114 | Vehicle security controller: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VEH_vehNm` | page 115 | Vehicle security controller: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VEH_authentication` | page 115 | Vehicle security controller: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VEH_BLEResetRequest` | page 115 | Vehicle security controller: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VEH_requests` | page 115 | Vehicle security controller: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VEH_requests2` | page 115 | Vehicle security controller: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_REM_authentication` | page 115 | Vehicle security controller: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_UI_corianderVehicleControl` | page 115 | Vehicle security controller: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_CH_TPMSDisplay` | page 115 | Vehicle security controller: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_PARTY_epbmStatus` | page 116 | Vehicle security controller: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_vehNm` | page 116 | Vehicle security controller: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_hvacRequest` | page 116 | Vehicle security controller: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_hvacStatus` | page 116 | Vehicle security controller: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_LVPowerState` | page 116 | Vehicle security controller: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_lightStatus` | page 116 | Vehicle security controller: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_seatStatus` | page 116 | Vehicle security controller: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_thsStatus` | page 116 | Vehicle security controller: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_doorStatus` | page 116 | Vehicle security controller: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_seatHeatStatus` | page 116 | Vehicle security controller: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_restraintStatus` | page 116 | Vehicle security controller: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_switchStatus` | page 116 | Vehicle security controller: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_logging1Hz` | page 116 | Vehicle security controller: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_seatStatus2` | page 116 | Vehicle security controller: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_status` | page 116 | Vehicle security controller: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_thermalCommand` | page 116 | Vehicle security controller: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VEH_windowStatus` | page 116 | Vehicle security controller: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_PARTY_restraintStatus` | page 116 | Vehicle security controller: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_PARTY_doorStatus` | page 116 | Vehicle security controller: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_BDY_epbmStatus` | page 116 | Vehicle security controller: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_BDY_restraintStatus` | page 116 | Vehicle security controller: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_BDY_epbmStatus` | page 117 | Vehicle security controller: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_BDY_restraintStatus` | page 117 | Vehicle security controller: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_prndStatus` | page 117 | Vehicle security controller: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_PARTY_epbmStatus` | page 117 | Vehicle security controller: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_vehNm` | page 117 | Vehicle security controller: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_hvacBlowerFdb` | page 117 | Vehicle security controller: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_LVPowerState` | page 117 | Vehicle security controller: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_restraintStatus` | page 117 | Vehicle security controller: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_lightStatus` | page 117 | Vehicle security controller: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_seatStatus` | page 117 | Vehicle security controller: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_BDY_falconSwitchStatus` | page 117 | Vehicle security controller: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_doorStatus` | page 117 | Vehicle security controller: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_doorStatus2` | page 117 | Vehicle security controller: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_windowStatus` | page 117 | Vehicle security controller: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_switchStatus` | page 117 | Vehicle security controller: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_intrusionSensorStatus` | page 117 | Vehicle security controller: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_liftgateStatus` | page 117 | Vehicle security controller: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_seatStatus2` | page 117 | Vehicle security controller: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_PARTY_restraintStatus` | page 117 | Vehicle security controller: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_thermalStatus` | page 117 | Vehicle security controller: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_PARTY_doorStatus` | page 117 | Vehicle security controller: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VEH_status` | page 117 | Vehicle security controller: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_PARTY_prndStatus` | page 117 | Vehicle security controller: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_vehNm` | page 118 | Vehicle security controller: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_lighting` | page 118 | Vehicle security controller: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_sensors` | page 118 | Vehicle security controller: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_status` | page 118 | Vehicle security controller: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_okToUseHighPwr` | page 118 | Vehicle security controller: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_LVPowerState` | page 118 | Vehicle security controller: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_coolant` | page 118 | Vehicle security controller: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_vehicleStatus` | page 118 | Vehicle security controller: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_12VBatteryStatus` | page 118 | Vehicle security controller: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_systemStatus` | page 118 | Vehicle security controller: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_LVPowerState` | page 118 | Vehicle security controller: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_outputPowerStatus` | page 118 | Vehicle security controller: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_vehicleTime` | page 118 | Vehicle security controller: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_thermalCommand` | page 118 | Vehicle security controller: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_LVPowerState` | page 118 | Vehicle security controller: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_sensors` | page 118 | Vehicle security controller: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_sensors` | page 118 | Vehicle security controller: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_interNodeResistance` | page 118 | Vehicle security controller: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_lighting` | page 118 | Vehicle security controller: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VEH_lightStatus` | page 118 | Vehicle security controller: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_vehNm` | page 118 | Vehicle security controller: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_12VBatteryStatus` | page 118 | Vehicle security controller: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_LVBMS_statusHigh` | page 118 | Vehicle security controller: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_CH_alertMatrix` | page 118 | Vehicle security controller: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_BDY_outputPowerStatus` | page 118 | Vehicle security controller: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_BDY_vehicleTime` | page 118 | Vehicle security controller: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | Vehicle security controller: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | Vehicle security controller: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_VEH_steerAngle` | page 119 | Vehicle security controller: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_VEH_leftStalk` | page 119 | Vehicle security controller: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_VEH_rightStalk` | page 119 | Vehicle security controller: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_PARTY_rightStalk` | page 119 | Vehicle security controller: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_CH_steerAngle` | page 119 | Vehicle security controller: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_PARTY_steerAngle` | page 119 | Vehicle security controller: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_chassisCntl` | page 120 | Vehicle security controller: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_systemStatus` | page 120 | Vehicle security controller: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_CH_chassisCntl` | page 120 | Vehicle security controller: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_systemStatus` | page 120 | Vehicle security controller: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_torque` | page 120 | Vehicle security controller: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_torque` | page 120 | Vehicle security controller: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_locStatus` | page 120 | Vehicle security controller: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_speed` | page 120 | Vehicle security controller: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_speed` | page 120 | Vehicle security controller: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_status` | page 120 | Vehicle security controller: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PT_speed` | page 120 | Vehicle security controller: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PT_systemStatus` | page 120 | Vehicle security controller: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_vehicleEstimates` | page 120 | Vehicle security controller: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_aggregatedAxleSpeed` | page 120 | Vehicle security controller: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_aggregatedAxleSpeed` | page 120 | Vehicle security controller: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_systemPower` | page 120 | Vehicle security controller: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PT_systemPower` | page 120 | Vehicle security controller: a120 PT system power | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_stalklessInterfaces` | page 120 | Vehicle security controller: a120 PARTY stalkless interfaces | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_CH_speed` | page 120 | Vehicle security controller: a120 CH speed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_estimatedBrakeTemp` | page 120 | Vehicle security controller: a120 VEH estimated brake temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_prndControl` | page 120 | Vehicle security controller: a120 PARTY prnd control | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_PARTY_locStatus2` | page 120 | Vehicle security controller: a120 PARTY loc status2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_chassisCntl` | page 120 | Vehicle security controller: a120 VEH chassis cntl | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_locStatus` | page 120 | Vehicle security controller: a120 VEH loc status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_locStatus2` | page 120 | Vehicle security controller: a120 VEH loc status2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_prndControl` | page 120 | Vehicle security controller: a120 VEH prnd control | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_VEH_vehicleEstimates` | page 120 | Vehicle security controller: a120 VEH vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a121_VEH_status` | page 121 | Vehicle security controller: a121 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a121_VEH_occupancy` | page 121 | Vehicle security controller: a121 VEH occupancy | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a133_alarmTriggerReason` | page 133 | Vehicle security controller: a133 alarm trigger reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `FRONT_DRIVER_DOOR`<br>1 = `FRONT_PASSENGER_DOOR`<br>2 = `REAR_DRIVER_DOOR`<br>3 = `REAR_PASSENGER_DOOR`<br>4 = `FRONT_TRUNK`<br>5 = `REAR_TRUNK`<br>6 = `ULTRASONIC`<br>7 = `TILT_SENSOR`<br>8 = `SENTRY_REQUEST`<br>9 = `NOT_TRIGGERED`<br>10 = `POWERED_UP_TRIGGERED`<br>11 = `RADAR`<br>12 = `TONNEAU`<br>13 = `TRAILER_DISCONNECT`<br>14 = `TAILGATE` | plausible |
| `VCSEC_a177_newWhitelistSlot` | page 177 | Vehicle security controller: a177 new whitelist slot | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a177_signingKeySlot` | page 177 | Vehicle security controller: a177 signing key slot | 21\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a177_newKeyPublicKey` | page 177 | Vehicle security controller: a177 new key public key | 26\|20 | little-endian | unsigned | 1 | 0 |  | 0 to 1048575 |  | layout-only |
| `VCSEC_a177_keyActiveTime` | page 177 | Vehicle security controller: a177 key active time | 46\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `VCSEC_a177_keyRole` | page 177 | Vehicle security controller: a177 key role | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `SERVICE_KEY`<br>2 = `OWNER_KEY`<br>3 = `DRIVER_KEY`<br>4 = `FM_KEY`<br>5 = `VEHICLE_MONITOR_KEY`<br>6 = `CHARGING_MANAGER_KEY`<br>7 = `SERVICE_TECH_KEY`<br>8 = `GUEST_KEY`<br>9 = `RIDER_KEY`<br>10 = `PREDELIVERY_KEY` | plausible |
| `VCSEC_a178_publicKey` | page 178 | Vehicle security controller: a178 public key | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_a178_signingKeySlot` | page 178 | Vehicle security controller: a178 signing key slot | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a178_removedKeySlot` | page 178 | Vehicle security controller: a178 removed key slot | 53\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a178_removedKeyRole` | page 178 | Vehicle security controller: a178 removed key role | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `SERVICE_KEY`<br>2 = `OWNER_KEY`<br>3 = `DRIVER_KEY`<br>4 = `FM_KEY`<br>5 = `VEHICLE_MONITOR_KEY`<br>6 = `CHARGING_MANAGER_KEY`<br>7 = `SERVICE_TECH_KEY`<br>8 = `GUEST_KEY`<br>9 = `RIDER_KEY`<br>10 = `PREDELIVERY_KEY` | plausible |
| `VCSEC_a191_clearWlist` | page 191 | Vehicle security controller: a191 clear wlist | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a191_WlistingDevice` | page 191 | Vehicle security controller: a191 wlisting device | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a191_failedToSendWlist` | page 191 | Vehicle security controller: a191 failed to send wlist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a192_clearWlist` | page 192 | Vehicle security controller: a192 clear wlist | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a192_WlistingDevice` | page 192 | Vehicle security controller: a192 wlisting device | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a192_failedToSendWlist` | page 192 | Vehicle security controller: a192 failed to send wlist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a193_clearWlist` | page 193 | Vehicle security controller: a193 clear wlist | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a193_WlistingDevice` | page 193 | Vehicle security controller: a193 wlisting device | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a193_failedToSendWlist` | page 193 | Vehicle security controller: a193 failed to send wlist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a194_clearWlist` | page 194 | Vehicle security controller: a194 clear wlist | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a194_WlistingDevice` | page 194 | Vehicle security controller: a194 wlisting device | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a194_failedToSendWlist` | page 194 | Vehicle security controller: a194 failed to send wlist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a197_connectionChannel` | page 197 | Vehicle security controller: a197 connection channel | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a197_connHandleMismatch` | page 197 | Vehicle security controller: a197 conn handle mismatch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a197_confrmtnTimeout` | page 197 | Vehicle security controller: a197 confrmtn timeout | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a197_errorInconfrmtn` | page 197 | Vehicle security controller: a197 error inconfrmtn | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a210_whiteListChannel` | page 210 | Vehicle security controller: a210 white list channel | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a211_handlePulled` | page 211 | Vehicle security controller: a211 handle pulled | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `FRONTDRIVER`<br>1 = `FRONTPASSENGER`<br>2 = `REARDRIVER`<br>3 = `REARPASSENGER`<br>4 = `TRUNK`<br>5 = `CHARGEPORT`<br>6 = `FRUNK`<br>7 = `AUTOPRESENT_DRIVER`<br>8 = `AUTOPRESENT_PASSENGER`<br>10 = `UNKNOWN` | plausible |
| `VCSEC_a211_connectionCount` | page 211 | Vehicle security controller: a211 connection count | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a211_RSSIValidMatrix` | page 211 | Vehicle security controller: a211 RSSI valid matrix | 24\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `VCSEC_a211_DevicePresentCount` | page 211 | Vehicle security controller: a211 device present count | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `VCSEC_a211_UnknownDevicePresent` | page 211 | Vehicle security controller: a211 unknown device present | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a211_AuthRequested` | page 211 | Vehicle security controller: a211 auth requested | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a211_MaximumRSSI` | page 211 | Vehicle security controller: a211 maximum RSSI | 52\|8 | little-endian | signed | 1 | 0 |  | -128 to 127 |  | layout-only |
| `VCSEC_a211_MaximumRSSIAntenna` | page 211 | Vehicle security controller: a211 maximum RSSI antenna | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LEFT`<br>1 = `RIGHT`<br>2 = `REAR`<br>3 = `CENTER`<br>4 = `FRONT`<br>5 = `SECONDARY`<br>6 = `NFCCRADLE`<br>7 = `REARLEFT`<br>8 = `REARRIGHT`<br>9 = `FRONTLEFT`<br>10 = `FRONTRIGHT`<br>11 = `NONE` | plausible |
| `VCSEC_a212_snifferChannelMissing` | page 212 | Vehicle security controller: a212 sniffer channel missing | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `UNKNOWN` | plausible |
| `VCSEC_a212_snifferMIALeft` | page 212 | Vehicle security controller: a212 sniffer MIA left | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIARight` | page 212 | Vehicle security controller: a212 sniffer MIA right | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIARear` | page 212 | Vehicle security controller: a212 sniffer MIA rear | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_accessAddressInvalid` | page 212 | Vehicle security controller: a212 access address invalid | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIAFront` | page 212 | Vehicle security controller: a212 sniffer MIA front | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIASecondary` | page 212 | Vehicle security controller: a212 sniffer MIA secondary | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIACradle` | page 212 | Vehicle security controller: a212 sniffer MIA cradle | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIARearLeft` | page 212 | Vehicle security controller: a212 sniffer MIA rear left | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIARearRight` | page 212 | Vehicle security controller: a212 sniffer MIA rear right | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIAFrontLeft` | page 212 | Vehicle security controller: a212 sniffer MIA front left | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferMIAFrontRight` | page 212 | Vehicle security controller: a212 sniffer MIA front right | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a219_pairingRemovedSensor0` | page 219 | Vehicle security controller: a219 pairing removed sensor0 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a219_pairingRemovedSensor1` | page 219 | Vehicle security controller: a219 pairing removed sensor1 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a219_pairingRemovedSensor2` | page 219 | Vehicle security controller: a219 pairing removed sensor2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a219_pairingRemovedSensor3` | page 219 | Vehicle security controller: a219 pairing removed sensor3 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a221_countryCode` | page 221 | Vehicle security controller: a221 country code | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_a221_homologationRegion` | page 221 | Vehicle security controller: a221 homologation region | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `NORTHAMERICA`<br>2 = `EUROPE`<br>3 = `CHINA` | plausible |
| `VCSEC_a223_connParamsNotSet` | page 223 | Vehicle security controller: a223 conn params not set | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a223_sensorDataStale` | page 223 | Vehicle security controller: a223 sensor data stale | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a223_PTDataNotReceived` | page 223 | Vehicle security controller: a223 PT data not received | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a223_invalidPressureDataReceived` | page 223 | Vehicle security controller: a223 invalid pressure data received | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a224_connParamsNotSet` | page 224 | Vehicle security controller: a224 conn params not set | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a224_sensorDataStale` | page 224 | Vehicle security controller: a224 sensor data stale | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a224_PTDataNotReceived` | page 224 | Vehicle security controller: a224 PT data not received | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a224_invalidPressureDataReceived` | page 224 | Vehicle security controller: a224 invalid pressure data received | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a225_connParamsNotSet` | page 225 | Vehicle security controller: a225 conn params not set | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a225_sensorDataStale` | page 225 | Vehicle security controller: a225 sensor data stale | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a225_PTDataNotReceived` | page 225 | Vehicle security controller: a225 PT data not received | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a225_invalidPressureDataReceived` | page 225 | Vehicle security controller: a225 invalid pressure data received | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a226_connParamsNotSet` | page 226 | Vehicle security controller: a226 conn params not set | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a226_sensorDataStale` | page 226 | Vehicle security controller: a226 sensor data stale | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a226_PTDataNotReceived` | page 226 | Vehicle security controller: a226 PT data not received | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a226_invalidPressureDataReceived` | page 226 | Vehicle security controller: a226 invalid pressure data received | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a236_connectionChannel` | page 236 | Vehicle security controller: a236 connection channel | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a253_lowBatterySensor0` | page 253 | Vehicle security controller: a253 low battery sensor0 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a253_lowBatterySensor1` | page 253 | Vehicle security controller: a253 low battery sensor1 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a253_lowBatterySensor2` | page 253 | Vehicle security controller: a253 low battery sensor2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a253_lowBatterySensor3` | page 253 | Vehicle security controller: a253 low battery sensor3 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a256_whitelistOperation` | page 256 | Vehicle security controller: a256 whitelist operation | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `IDLE`<br>1 = `ADD_PUBLIC_KEY`<br>2 = `REMOVE_PUBLIC_KEY`<br>8 = `AWAIT_LOCAL_ENTITY_AUTH_COMPLETE`<br>9 = `ADD_IMPERMANENT_KEY`<br>10 = `REPLACE_IMPERMANENT_KEYS`<br>11 = `REMOVE_IMPERMANENT_KEYS`<br>12 = `REPLACE_KEY` | plausible |
| `VCSEC_a256_failureReason` | page 256 | Vehicle security controller: a256 failure reason | 24\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `INVALID_KEY`<br>2 = `NO_PERMISSION_TO_ADD`<br>3 = `NO_PERMISSION_TO_REMOVE`<br>4 = `NO_PERMISSION_TO_CHANGE_PERMISSIONS`<br>5 = `NO_PERMISSION_TO_REMOVE_ONESELF`<br>6 = `ATTEMPTING_TO_ELEVATE_OTHER_ABOVE_ONSELF`<br>7 = `ATTEMPTING_TO_REMOVE_OWN_PERMISSIONS`<br>8 = `ATTEMPTING_TO_DEMOTE_OTHER_TO_ONESELF`<br>9 = `KEY_NOT_ON_WHITELIST`<br>10 = `KEYCHAN_FULL`<br>11 = `COMPONENT_SPECIFIC`<br>12 = `COULD_NOT_START_TIMER`<br>13 = `TIMER_NOT_RUNNING`<br>14 = `ATTEMPTING_TO_UPDATE_TIME_ON_OWN_PERMISSIONS`<br>15 = `ATTEMPTING_TO_ADD_KEY_THAT_IS_ALREADY_ON_THE_WHITELIST`<br>16 = `ATTEMPTING_TO_ADD_KEY_THAT_IS_NOT_ON_READER`<br>17 = `FM_ATTEMPTING_TO_REMOVE_PERMANENT_KEY`<br>18 = `FM_ATTEMPTING_TO_ADD_PERMANENT_KEY`<br>19 = `FM_MODIFYING_OUTSIDE_OF_F_MODE`<br>20 = `KEYCHAIN_WHILE_FS_FULL`<br>21 = `ATTEMPTING_TO_ADD_KEY_WITHOUT_ROLE`<br>22 = `ATTEMPTING_TO_ADD_KEY_WITH_SERVICE_ROLE`<br>23 = `SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH_OUTSIDE_SERVICE_MODE`<br>24 = `NON_SERVICE_KEY_ATTEMPTING_TO_ADD_SERVICE_TECH`<br>25 = `COULD_NOT_START_LOCAL_ENTITY_AUTH`<br>26 = `LOCAL_ENTITY_AUTH_FAILED_UI_DENIED`<br>27 = `LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_TAP`<br>28 = `LOCAL_ENTITY_AUTH_FAILED_TIMED_OUT_WAITING_FOR_UI_ACK`<br>29 = `LOCAL_ENTITY_AUTH_FAILED_VALET_MODE`<br>30 = `LOCAL_ENTITY_AUTH_FAILED_CANCELLED`<br>31 = `NON_SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY`<br>32 = `ATTEMPTING_TO_ADD_RIDER_KEY_OUTSIDE_FLEET_MODE`<br>33 = `NON_SERVICE_KEY_ATTEMPTING_TO_ADD_RIDER_KEY`<br>34 = `SERVICE_KEY_ATTEMPTING_TO_ADD_PREDELIVERY_KEY_WHEN_ALREADY_DELIVERED`<br>63 = `UNKNOWN` | plausible |
| `VCSEC_a256_whitelistSlot` | page 256 | Vehicle security controller: a256 whitelist slot | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a256_signingKeySlot` | page 256 | Vehicle security controller: a256 signing key slot | 40\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a256_keyActiveTime` | page 256 | Vehicle security controller: a256 key active time | 45\|18 | little-endian | unsigned | 1 | 0 |  | 0 to 262143 |  | layout-only |
| `VCSEC_a257_whitelistSlot` | page 257 | Vehicle security controller: a257 whitelist slot | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a257_keyID` | page 257 | Vehicle security controller: a257 key ID | 24\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `VCSEC_a257_keyActiveTime` | page 257 | Vehicle security controller: a257 key active time | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a257_permissionActiveTime` | page 257 | Vehicle security controller: a257 permission active time | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a266_pressure` | page 266 | Vehicle security controller: a266 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a267_pressure` | page 267 | Vehicle security controller: a267 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a268_pressure` | page 268 | Vehicle security controller: a268 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a269_pressure` | page 269 | Vehicle security controller: a269 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a270_pressure` | page 270 | Vehicle security controller: a270 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a271_pressure` | page 271 | Vehicle security controller: a271 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a272_pressure` | page 272 | Vehicle security controller: a272 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a273_pressure` | page 273 | Vehicle security controller: a273 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a311_whitelistChannel` | page 311 | Vehicle security controller: a311 whitelist channel | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_a436_currentUHFHardware` | page 436 | Vehicle security controller: a436 current UHF hardware | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a436_expectedUHFHardware` | page 436 | Vehicle security controller: a436 expected UHF hardware | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a436_countryCode` | page 436 | Vehicle security controller: a436 country code | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_a455_pressure` | page 455 | Vehicle security controller: a455 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a456_pressure` | page 456 | Vehicle security controller: a456 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a457_pressure` | page 457 | Vehicle security controller: a457 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a458_pressure` | page 458 | Vehicle security controller: a458 pressure | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | plausible |
| `VCSEC_a497_centerEndpointMismatch` | page 497 | Vehicle security controller: a497 center endpoint mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_cradleEndpointMismatch` | page 497 | Vehicle security controller: a497 cradle endpoint mismatch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_leftEndpointMismatch` | page 497 | Vehicle security controller: a497 left endpoint mismatch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_rightEndpointMismatch` | page 497 | Vehicle security controller: a497 right endpoint mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_rearLeftEndpointMismatch` | page 497 | Vehicle security controller: a497 rear left endpoint mismatch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_rearRightEndpointMismatch` | page 497 | Vehicle security controller: a497 rear right endpoint mismatch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_endpointLocationToFix` | page 497 | Vehicle security controller: a497 endpoint location to fix | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LEFT`<br>1 = `RIGHT`<br>2 = `REAR`<br>3 = `CENTER`<br>4 = `FRONT`<br>5 = `SECONDARY`<br>6 = `NFCCRADLE`<br>7 = `REARLEFT`<br>8 = `REARRIGHT`<br>9 = `FRONTLEFT`<br>10 = `FRONTRIGHT`<br>11 = `NONE` | plausible |
| `VCSEC_a497_endpointExpectedPcbaId` | page 497 | Vehicle security controller: a497 endpoint expected pcba id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a497_endpointExpectedAssemblyId` | page 497 | Vehicle security controller: a497 endpoint expected assembly id | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a497_endpointExpectedUsageId` | page 497 | Vehicle security controller: a497 endpoint expected usage id | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a497_endpointActualPcbaId` | page 497 | Vehicle security controller: a497 endpoint actual pcba id | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_a497_endpointActualAssemblyId` | page 497 | Vehicle security controller: a497 endpoint actual assembly id | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCSEC_a497_endpointActualUsageId` | page 497 | Vehicle security controller: a497 endpoint actual usage id | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |

## Multiplexing

`VCSEC_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (2 signals), page 10 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (8 signals), page 88 (8 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (2 signals), page 95 (2 signals), page 96 (2 signals), page 98 (12 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (6 signals), page 107 (15 signals), page 108 (11 signals), page 109 (16 signals), page 110 (16 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (21 signals), page 117 (23 signals), page 118 (28 signals), page 119 (6 signals), page 120 (27 signals), page 121 (2 signals), page 133 (1 signals), page 177 (5 signals), page 178 (4 signals), page 191 (3 signals), page 192 (3 signals), page 193 (3 signals), page 194 (3 signals), page 197 (4 signals), page 210 (1 signals), page 211 (8 signals), page 212 (12 signals), page 219 (4 signals), page 221 (2 signals), page 223 (4 signals), page 224 (4 signals), page 225 (4 signals), page 226 (4 signals), page 236 (1 signals), page 253 (4 signals), page 256 (5 signals), page 257 (4 signals), page 266 (1 signals), page 267 (1 signals), page 268 (1 signals), page 269 (1 signals), page 270 (1 signals), page 271 (1 signals), page 272 (1 signals), page 273 (1 signals), page 311 (1 signals), page 436 (3 signals), page 455 (1 signals), page 456 (1 signals), page 457 (1 signals), page 458 (1 signals), page 497 (13 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
