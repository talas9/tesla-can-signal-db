---
layout: default
title: "EPASTS_alertLog (0x594) — EPASTS ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "EPASTS ECU message: alert log. Tesla Model 3 / Model Y CAN bus message EPASTS_alertLog (0x594) of EPASTS ECU, firmware 2026.26.6.5, 276 signals (EPASTS_alertID, EPASTS_alertState, EPASTS_a001_debugInfo, EPASTS_a002_debugInfo and 272 more). Bit layout, scaling, units and value tables."
---

# EPASTS_alertLog (0x594) — EPASTS ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

EPASTS ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 276 signals of EPASTS_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPASTS_alertLog` |
| CAN id | 0x594 (1428) |
| ECU | [EPASTS ECU](../../epasts.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | EPASTS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 276 |

## Signals of EPASTS_alertLog

Tesla Model 3 / Model Y CAN bus signals in `EPASTS_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPASTS_alertID` | selector | EPASTS ECU: alert ID | 0\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_adcCalibrationOrInitFail`<br>2 = `a002_adcMuxErr`<br>3 = `a003_pspInvalidParamset`<br>4 = `a004_scpInputMia`<br>5 = `a005_scpUnknownResetSource`<br>6 = `a006_swrhResetByInvalidErrid`<br>7 = `a007_tsmcCoreTempDiff`<br>8 = `a008_psdcPlatformShutdown`<br>9 = `a009_mcusscLbistPermanentFail`<br>10 = `a010_svcIncompatibleSwVersions`<br>11 = `a011_mcusscMonbistErr`<br>12 = `a012_mcusscMbistEccErr`<br>13 = `a013_mcusscSffMonitoringFailed`<br>14 = `a014_mcusscSffMonitoringMia`<br>15 = `a015_mcusscCsErrorCheckFail`<br>16 = `a016_mcufcCsErrorCheckFail`<br>17 = `a017_stmdStmPlausibilityCheckErr`<br>18 = `a018_exchCsErrorCheck`<br>19 = `a019_rsthHwResetInfoCorruptionCheck`<br>20 = `a020_mcusscEolEcuIdIntegritiyFail`<br>21 = `a021_osehCsErrorCheck`<br>22 = `a022_swrhSwResetInfoCorruptionCheck`<br>23 = `a023_btarcCorruptionCheck`<br>24 = `a024_srhCsErrorCheckFail`<br>25 = `a025_btarcCorruptionCheck`<br>26 = `a026_mrccCsErrorCheckFail`<br>27 = `a027_mcusscDmuHfErr`<br>28 = `a028_smuhNonInitDataCorruption`<br>29 = `a029_smuhSmuCoreCntErrorTestFail`<br>30 = `a030_rsthClockReset`<br>31 = `a031_pmsProductionModeFailed`<br>32 = `a032_eolpEolCheckFailed`<br>33 = `a033_icsvcPswVersionMismatch`<br>34 = `a034_sbchReadbackRegFail`<br>35 = `a035_sbchChipIdFail`<br>36 = `a036_sbcmSbcBistFailed`<br>37 = `a037_epmV5P2Fail`<br>38 = `a038_csohCh1CsErrorErrAtReset`<br>39 = `a039_csohCh2CsErrorErrAtReset`<br>40 = `a040_swrhLimitedResetRetriesExpired`<br>41 = `a041_imcmCoreConfigurationMismatch`<br>42 = `a042_wdhWdTestFail`<br>43 = `a043_sbcmWdStateDisabled`<br>44 = `a044_sbcmSbcEepromFail`<br>45 = `a045_psumSbcBandgapVoltErr`<br>46 = `a046_mcusscOscillatorNotReliable`<br>47 = `a047_epmVregVoltFail`<br>48 = `a048_epmVcpVoltFail`<br>49 = `a049_epmLgFail`<br>50 = `a050_erlErr`<br>51 = `a051_ermMessageErr`<br>52 = `a052_ermSdcInputBufferOverflow`<br>53 = `a053_adcUnexpectedNumOfData`<br>54 = `a054_adcUnexpectedData`<br>55 = `a055_amExtendedGduTest`<br>56 = `a056_amGduConfigCsErrorCheck`<br>57 = `a057_amGduVds`<br>58 = `a058_amIntVgsUndervtgErr`<br>59 = `a059_amStartupTestFailed`<br>60 = `a060_amGduFail`<br>61 = `a061_amIntSerialErr`<br>62 = `a062_amPhaseBridgeCheck`<br>63 = `a063_amIntRegulatorErr`<br>64 = `a064_amBridgeShort`<br>65 = `a065_amGduJuncTemp`<br>66 = `a066_amVoltQfErr`<br>67 = `a067_tspmPowermoduleTempImplausible`<br>68 = `a068_rsthCoreRedundancyErr`<br>69 = `a069_rsthCoreTempOutOfRangeHwCheck`<br>70 = `a070_rsthInternalLowVolt`<br>71 = `a071_rsthInternalHighVolt`<br>72 = `a072_rsthFlashUncorrEccOrOvfl`<br>73 = `a073_rsthOtherEdcEcc`<br>74 = `a074_rsthUnexpectedAlarm`<br>75 = `a075_rsthUnusedOtherModuleAlarm`<br>76 = `a076_exchGeneralException`<br>77 = `a077_dmDeadlineViolation`<br>78 = `a078_dmDeadlineViolation`<br>79 = `a079_gduhComErr`<br>80 = `a080_pwmTimerSyncCheck`<br>81 = `a081_exchFloatingPointException`<br>82 = `a082_adcTriggerTimeChk`<br>83 = `a083_tdaDclinkcapacitorTempChecker`<br>84 = `a084_adcTriggerCheck`<br>85 = `a085_amGduSwitchOffTestByMcu`<br>86 = `a086_rsthRamUncorrEcc`<br>87 = `a087_rsthFlashConfigErr`<br>88 = `a088_tedMainboardTempChecker`<br>89 = `a089_tedRevercebattfetjunctionTempChecker`<br>90 = `a090_etsmWarning`<br>91 = `a091_bvpBattVoltCrossChkFailed`<br>92 = `a092_amGduSwitchOffTestBySbc`<br>93 = `a093_sctpTsuSingleStaticFail`<br>94 = `a094_sctpTsuMultipleStaticFail`<br>95 = `a095_mdModelBasedMotorIntegrityCheck`<br>96 = `a096_rppRpsSingleStaticFail`<br>97 = `a097_rppRpsMultipleStaticFail`<br>98 = `a098_invErr`<br>99 = `a099_mcdTorqueMismatchFault`<br>100 = `a100_amVbrgLssFault`<br>101 = `a101_sdrvSpcIdMismatch`<br>102 = `a102_amPhasecurrentQosErr`<br>103 = `a103_exhaUnusedInterruptCallException`<br>104 = `a104_exhaBusMpuException`<br>105 = `a105_exhaSriBusErrException`<br>106 = `a106_exhaSpbBusErrException`<br>107 = `a107_exhaOtherNmiException`<br>108 = `a108_exhaInternalProtectionException`<br>109 = `a109_exhaSysBusOrPeriphErrException`<br>110 = `a110_amPhaseRelaySwitchOffTest`<br>111 = `a111_amCurrentSensingDisconnection`<br>112 = `a112_rsthSafetyFlipflopErr`<br>113 = `a113_rsthUncorrectableEndToEndBusErr`<br>114 = `a114_osehOsErr`<br>115 = `a115_mcusscLbistSingleFail`<br>116 = `a116_mrccStartupRegCsErrorStaticErr`<br>117 = `a117_mrccStartupRegCsErrorTransientErr`<br>118 = `a118_mcusscFlashCsErrorErr`<br>119 = `a119_mcusscFlashEccCriticalErr`<br>120 = `a120_mcusscFlashEccLatentErr`<br>121 = `a121_mcusscMbistEccErr`<br>122 = `a122_pcpBridgeFetShort`<br>123 = `a123_imcmCommErr`<br>124 = `a124_mcusscMbistEccTransientErr`<br>125 = `a125_mcusscMbistMiaErr`<br>126 = `a126_mcusscMonbistMiaErr`<br>127 = `a127_exchAdditionalExceptionAfterRst`<br>128 = `a128_exchExceptionStopRestart`<br>129 = `a129_exchAdditionalExceptionStopRestart`<br>130 = `a130_mrccConfigCsErrorErr`<br>131 = `a131_exchGuardedResetAfterPartitionStop`<br>132 = `a132_mcusscNotSupportedMcu`<br>133 = `a133_mcusscLbistEcuIdIsNotSupported`<br>134 = `a134_osehGuardedResetAfterErrWithoutReset`<br>135 = `a135_tmpsfetjCalculationOverflowErr`<br>136 = `a136_ftElectricalAngleQf`<br>137 = `a137_osehErrWithoutImmediateReset`<br>138 = `a138_osehAdditionalErrWithoutImmReset`<br>139 = `a139_osehAdditionalOsErr`<br>140 = `a140_imcmConfigurationErr`<br>141 = `a141_amFetShortTest`<br>142 = `a142_tedEmifilterDmcTempChecker`<br>143 = `a143_tedEmifilterCmcTempChecker`<br>144 = `a144_mriCoreRaminitFailed`<br>145 = `a145_mriPeripheralRaminitFailed`<br>146 = `a146_btarcRcCircuitCheck`<br>147 = `a147_amDcLinkShortedFail`<br>148 = `a148_mrccExitFromStandbyDetected`<br>149 = `a149_amReversibleEmergencyOffRequested`<br>150 = `a150_amExternalEmergencyOffRequested`<br>151 = `a151_amPermanentEmergencyOffRequested`<br>152 = `a152_exchFlashEccException`<br>153 = `a153_sdsmBlockSelectorInvalid`<br>154 = `a154_sdsmCsErrorInvalidPrimary`<br>155 = `a155_sdsmDataInvalidAll`<br>156 = `a156_amIntSerialErrSafetyReset`<br>157 = `a157_mcudcpInvalidEcuId`<br>158 = `a158_amGduFailDuringRecovery`<br>159 = `a159_exchFlashWordlineTransientErr`<br>160 = `a160_rsthCpu1UnexpectedAlarm`<br>161 = `a161_tdaRelayfetjunctionTempChecker`<br>162 = `a162_tdaBridgefetjunctionTempChecker`<br>163 = `a163_tdaPowermoduleTempChecker`<br>164 = `a164_tdaBattfetjunctionTempChecker`<br>165 = `a165_tdaDcbusshuntTempChecker`<br>166 = `a166_tdaPhasecurrentshuntTempChecker`<br>167 = `a167_iccd1ErrQueueOverflow`<br>168 = `a168_c1csInvalidC1App`<br>169 = `a169_scpSafetyReset`<br>170 = `a170_pmpDcvoltAge`<br>171 = `a171_pmpKgvalueAge`<br>172 = `a172_pmpElangMotorcurrentAge`<br>173 = `a173_pmpRotorspeedAge`<br>174 = `a174_pmpPhasecurrentAge`<br>175 = `a175_exchFlashStoredConfigErr`<br>176 = `a176_exchCpu1ExceptionReset`<br>177 = `a177_etsrInvalidated`<br>178 = `a178_exchWdtException`<br>179 = `a179_tedMotorcoilTempChecker`<br>180 = `a180_dmDeadlineViolationC1`<br>181 = `a181_dmDeadlineViolationC1`<br>182 = `a182_mcdInputMia`<br>183 = `a183_sbchCommErrSbcToMcu`<br>184 = `a184_sbcmCommBufferOverflow`<br>185 = `a185_sbcscpQAWatchdogReset`<br>186 = `a186_wdhCommBufferOverflow`<br>187 = `a187_epmVoltFail`<br>188 = `a188_epmCommBufferOverflow`<br>189 = `a189_sbchCommErrMcuToSbc`<br>190 = `a190_sbchCommBufferOverflow`<br>191 = `a191_sbcscpVcp2VucVoltFail`<br>192 = `a192_osumC0CsaNearFull`<br>193 = `a193_osumC0StackNearFull`<br>194 = `a194_amNvdataLoss`<br>195 = `a195_imcmCommErrC1`<br>196 = `a196_topEolTasOffsetInvalid`<br>197 = `a197_difpDifactorInvalid`<br>198 = `a198_osumC1CsaNearFull`<br>199 = `a199_osumC1StackNearFull`<br>200 = `a200_ammInputBufferOverflow`<br>201 = `a201_ammOutputBufferOverflow`<br>202 = `a202_ohnvmpStoredOffsetLost`<br>203 = `a203_ctcInterfaceErr`<br>204 = `a204_fdpPrevTrqErr`<br>205 = `a205_fdrOclFail`<br>206 = `a206_fdrOclPartialBlocking`<br>207 = `a207_fdrOclFreezing`<br>208 = `a208_fdrLowSeverityBlocking`<br>209 = `a209_fdrLowSeverityFreezing`<br>210 = `a210_fdrTotalBlocking`<br>211 = `a211_frmInternalErr`<br>212 = `a212_frmDataLost`<br>213 = `a213_frmHighFrictionDetected`<br>214 = `a214_velInterfaceErr`<br>215 = `a215_vsgSafeViolErr`<br>216 = `a216_isdgImproperShutdown`<br>217 = `a217_msdMasterSilentErr`<br>218 = `a218_aadApplicationStateErr`<br>219 = `a219_frhFastRestartFailed`<br>220 = `a220_transceiverInputqueueOverflow`<br>221 = `a221_apsCntError`<br>222 = `a222_apsCsError`<br>223 = `a223_apsMia`<br>224 = `a224_dasCntError`<br>225 = `a225_dasCsError`<br>226 = `a226_dasMia`<br>227 = `a227_dirTorqueCntError`<br>228 = `a228_dirTorqueCsError`<br>229 = `a229_dirTorqueMia`<br>230 = `a230_diSpdCntError`<br>231 = `a231_diSpdCsError`<br>232 = `a232_diSpdMia`<br>233 = `a233_ecu1StatCntError`<br>234 = `a234_ecu1StatCsError`<br>235 = `a235_ecu1StatMia`<br>236 = `a236_espWrCntError`<br>237 = `a237_espWrCsError`<br>238 = `a238_espWrMia`<br>239 = `a239_espWsCntError`<br>240 = `a240_espWsCsError`<br>241 = `a241_espWsMia`<br>242 = `a242_gtwConfigMia`<br>243 = `a243_rcmCntError`<br>244 = `a244_rcmCsError`<br>245 = `a245_rcmMia`<br>246 = `a246_sccmCntError`<br>247 = `a247_sccmCsError`<br>248 = `a248_sccmMia`<br>249 = `a249_uiTuneReqCntError`<br>250 = `a250_uiTuneReqCsError`<br>251 = `a251_uiTuneReqMia`<br>252 = `a252_vcFrontCntError`<br>253 = `a253_vcFrontCsError`<br>254 = `a254_vcFrontMia`<br>255 = `a255_pmState2Mia`<br>256 = `a256_dcvmOverVolt`<br>257 = `a257_dcvmUnderVolt`<br>258 = `a258_pspInvalidProjectParamset`<br>259 = `a259_scoCanBusOff`<br>260 = `a260_scoPrivateBusOff`<br>261 = `a261_sccmStatusError`<br>262 = `a262_yawRateStatus`<br>263 = `a263_espWsStatus`<br>264 = `a264_assistTorqueLimited`<br>265 = `a265_overheatProtect`<br>266 = `a266_overloadProtect`<br>267 = `a267_safeSpeedAssist`<br>268 = `a268_eacCancelled`<br>269 = `a269_assistTorqueDisabled`<br>270 = `a270_oscillationCompTrqLimReached` | plausible |
| `EPASTS_alertState` |  | EPASTS ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `EPASTS_a001_debugInfo` | page 1 | EPASTS ECU: a001 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a002_debugInfo` | page 2 | EPASTS ECU: a002 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a003_debugInfo` | page 3 | EPASTS ECU: a003 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a004_debugInfo` | page 4 | EPASTS ECU: a004 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a005_debugInfo` | page 5 | EPASTS ECU: a005 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a006_debugInfo` | page 6 | EPASTS ECU: a006 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a007_debugInfo` | page 7 | EPASTS ECU: a007 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a009_debugInfo` | page 9 | EPASTS ECU: a009 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a010_debugInfo` | page 10 | EPASTS ECU: a010 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a011_debugInfo` | page 11 | EPASTS ECU: a011 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a012_debugInfo` | page 12 | EPASTS ECU: a012 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a013_debugInfo` | page 13 | EPASTS ECU: a013 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a014_debugInfo` | page 14 | EPASTS ECU: a014 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a015_debugInfo` | page 15 | EPASTS ECU: a015 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a016_debugInfo` | page 16 | EPASTS ECU: a016 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a017_debugInfo` | page 17 | EPASTS ECU: a017 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a018_debugInfo` | page 18 | EPASTS ECU: a018 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a019_debugInfo` | page 19 | EPASTS ECU: a019 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a020_debugInfo` | page 20 | EPASTS ECU: a020 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a021_debugInfo` | page 21 | EPASTS ECU: a021 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a022_debugInfo` | page 22 | EPASTS ECU: a022 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a023_debugInfo` | page 23 | EPASTS ECU: a023 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a024_debugInfo` | page 24 | EPASTS ECU: a024 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a025_debugInfo` | page 25 | EPASTS ECU: a025 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a026_debugInfo` | page 26 | EPASTS ECU: a026 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a027_debugInfo` | page 27 | EPASTS ECU: a027 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a028_debugInfo` | page 28 | EPASTS ECU: a028 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a029_debugInfo` | page 29 | EPASTS ECU: a029 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a030_debugInfo` | page 30 | EPASTS ECU: a030 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a031_debugInfo` | page 31 | EPASTS ECU: a031 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a032_debugInfo` | page 32 | EPASTS ECU: a032 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a033_debugInfo` | page 33 | EPASTS ECU: a033 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a034_debugInfo` | page 34 | EPASTS ECU: a034 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a035_debugInfo` | page 35 | EPASTS ECU: a035 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a036_debugInfo` | page 36 | EPASTS ECU: a036 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a037_debugInfo` | page 37 | EPASTS ECU: a037 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a038_debugInfo` | page 38 | EPASTS ECU: a038 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a039_debugInfo` | page 39 | EPASTS ECU: a039 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a040_debugInfo` | page 40 | EPASTS ECU: a040 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a041_debugInfo` | page 41 | EPASTS ECU: a041 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a042_debugInfo` | page 42 | EPASTS ECU: a042 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a043_debugInfo` | page 43 | EPASTS ECU: a043 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a044_debugInfo` | page 44 | EPASTS ECU: a044 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a045_debugInfo` | page 45 | EPASTS ECU: a045 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a046_debugInfo` | page 46 | EPASTS ECU: a046 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a047_debugInfo` | page 47 | EPASTS ECU: a047 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a048_debugInfo` | page 48 | EPASTS ECU: a048 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a049_debugInfo` | page 49 | EPASTS ECU: a049 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a050_debugInfo` | page 50 | EPASTS ECU: a050 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a051_debugInfo` | page 51 | EPASTS ECU: a051 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a052_debugInfo` | page 52 | EPASTS ECU: a052 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a053_debugInfo` | page 53 | EPASTS ECU: a053 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a054_debugInfo` | page 54 | EPASTS ECU: a054 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a055_debugInfo` | page 55 | EPASTS ECU: a055 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a056_debugInfo` | page 56 | EPASTS ECU: a056 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a057_debugInfo` | page 57 | EPASTS ECU: a057 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a058_debugInfo` | page 58 | EPASTS ECU: a058 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a059_debugInfo` | page 59 | EPASTS ECU: a059 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a060_debugInfo` | page 60 | EPASTS ECU: a060 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a061_debugInfo` | page 61 | EPASTS ECU: a061 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a062_debugInfo` | page 62 | EPASTS ECU: a062 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a063_debugInfo` | page 63 | EPASTS ECU: a063 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a064_debugInfo` | page 64 | EPASTS ECU: a064 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a065_debugInfo` | page 65 | EPASTS ECU: a065 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a066_debugInfo` | page 66 | EPASTS ECU: a066 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a067_debugInfo` | page 67 | EPASTS ECU: a067 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a068_debugInfo` | page 68 | EPASTS ECU: a068 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a069_debugInfo` | page 69 | EPASTS ECU: a069 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a070_debugInfo` | page 70 | EPASTS ECU: a070 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a071_debugInfo` | page 71 | EPASTS ECU: a071 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a072_debugInfo` | page 72 | EPASTS ECU: a072 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a073_debugInfo` | page 73 | EPASTS ECU: a073 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a074_debugInfo` | page 74 | EPASTS ECU: a074 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a075_debugInfo` | page 75 | EPASTS ECU: a075 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a076_debugInfo` | page 76 | EPASTS ECU: a076 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a077_debugInfo` | page 77 | EPASTS ECU: a077 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a078_debugInfo` | page 78 | EPASTS ECU: a078 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a079_debugInfo` | page 79 | EPASTS ECU: a079 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a080_debugInfo` | page 80 | EPASTS ECU: a080 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a081_debugInfo` | page 81 | EPASTS ECU: a081 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a082_debugInfo` | page 82 | EPASTS ECU: a082 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a083_debugInfo` | page 83 | EPASTS ECU: a083 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a084_debugInfo` | page 84 | EPASTS ECU: a084 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a085_debugInfo` | page 85 | EPASTS ECU: a085 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a086_debugInfo` | page 86 | EPASTS ECU: a086 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a087_debugInfo` | page 87 | EPASTS ECU: a087 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a088_debugInfo` | page 88 | EPASTS ECU: a088 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a089_debugInfo` | page 89 | EPASTS ECU: a089 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a090_debugInfo` | page 90 | EPASTS ECU: a090 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a091_debugInfo` | page 91 | EPASTS ECU: a091 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a092_debugInfo` | page 92 | EPASTS ECU: a092 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a093_debugInfo` | page 93 | EPASTS ECU: a093 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a094_debugInfo` | page 94 | EPASTS ECU: a094 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a095_debugInfo` | page 95 | EPASTS ECU: a095 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a096_debugInfo` | page 96 | EPASTS ECU: a096 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a097_debugInfo` | page 97 | EPASTS ECU: a097 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a098_debugInfo` | page 98 | EPASTS ECU: a098 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a099_debugInfo` | page 99 | EPASTS ECU: a099 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a100_debugInfo` | page 100 | EPASTS ECU: a100 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a101_debugInfo` | page 101 | EPASTS ECU: a101 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a102_debugInfo` | page 102 | EPASTS ECU: a102 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a103_debugInfo` | page 103 | EPASTS ECU: a103 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a104_debugInfo` | page 104 | EPASTS ECU: a104 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a105_debugInfo` | page 105 | EPASTS ECU: a105 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a106_debugInfo` | page 106 | EPASTS ECU: a106 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a107_debugInfo` | page 107 | EPASTS ECU: a107 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a108_debugInfo` | page 108 | EPASTS ECU: a108 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a109_debugInfo` | page 109 | EPASTS ECU: a109 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a110_debugInfo` | page 110 | EPASTS ECU: a110 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a111_debugInfo` | page 111 | EPASTS ECU: a111 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a112_debugInfo` | page 112 | EPASTS ECU: a112 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a113_debugInfo` | page 113 | EPASTS ECU: a113 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a114_debugInfo` | page 114 | EPASTS ECU: a114 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a115_debugInfo` | page 115 | EPASTS ECU: a115 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a116_debugInfo` | page 116 | EPASTS ECU: a116 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a117_debugInfo` | page 117 | EPASTS ECU: a117 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a118_debugInfo` | page 118 | EPASTS ECU: a118 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a119_debugInfo` | page 119 | EPASTS ECU: a119 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a120_debugInfo` | page 120 | EPASTS ECU: a120 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a121_debugInfo` | page 121 | EPASTS ECU: a121 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a122_debugInfo` | page 122 | EPASTS ECU: a122 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a123_debugInfo` | page 123 | EPASTS ECU: a123 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a124_debugInfo` | page 124 | EPASTS ECU: a124 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a125_debugInfo` | page 125 | EPASTS ECU: a125 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a126_debugInfo` | page 126 | EPASTS ECU: a126 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a127_debugInfo` | page 127 | EPASTS ECU: a127 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a128_debugInfo` | page 128 | EPASTS ECU: a128 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a129_debugInfo` | page 129 | EPASTS ECU: a129 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a130_debugInfo` | page 130 | EPASTS ECU: a130 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a131_debugInfo` | page 131 | EPASTS ECU: a131 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a132_debugInfo` | page 132 | EPASTS ECU: a132 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a133_debugInfo` | page 133 | EPASTS ECU: a133 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a134_debugInfo` | page 134 | EPASTS ECU: a134 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a135_debugInfo` | page 135 | EPASTS ECU: a135 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a136_debugInfo` | page 136 | EPASTS ECU: a136 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a137_debugInfo` | page 137 | EPASTS ECU: a137 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a138_debugInfo` | page 138 | EPASTS ECU: a138 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a139_debugInfo` | page 139 | EPASTS ECU: a139 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a140_debugInfo` | page 140 | EPASTS ECU: a140 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a141_debugInfo` | page 141 | EPASTS ECU: a141 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a142_debugInfo` | page 142 | EPASTS ECU: a142 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a143_debugInfo` | page 143 | EPASTS ECU: a143 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a144_debugInfo` | page 144 | EPASTS ECU: a144 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a145_debugInfo` | page 145 | EPASTS ECU: a145 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a146_debugInfo` | page 146 | EPASTS ECU: a146 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a147_debugInfo` | page 147 | EPASTS ECU: a147 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a148_debugInfo` | page 148 | EPASTS ECU: a148 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a149_debugInfo` | page 149 | EPASTS ECU: a149 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a150_debugInfo` | page 150 | EPASTS ECU: a150 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a152_debugInfo` | page 152 | EPASTS ECU: a152 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a153_debugInfo` | page 153 | EPASTS ECU: a153 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a154_debugInfo` | page 154 | EPASTS ECU: a154 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a155_debugInfo` | page 155 | EPASTS ECU: a155 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a156_debugInfo` | page 156 | EPASTS ECU: a156 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a157_debugInfo` | page 157 | EPASTS ECU: a157 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a158_debugInfo` | page 158 | EPASTS ECU: a158 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a159_debugInfo` | page 159 | EPASTS ECU: a159 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a160_debugInfo` | page 160 | EPASTS ECU: a160 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a161_debugInfo` | page 161 | EPASTS ECU: a161 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a162_debugInfo` | page 162 | EPASTS ECU: a162 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a163_debugInfo` | page 163 | EPASTS ECU: a163 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a164_debugInfo` | page 164 | EPASTS ECU: a164 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a165_debugInfo` | page 165 | EPASTS ECU: a165 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a166_debugInfo` | page 166 | EPASTS ECU: a166 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a167_debugInfo` | page 167 | EPASTS ECU: a167 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a168_debugInfo` | page 168 | EPASTS ECU: a168 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a169_debugInfo` | page 169 | EPASTS ECU: a169 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a170_debugInfo` | page 170 | EPASTS ECU: a170 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a171_debugInfo` | page 171 | EPASTS ECU: a171 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a172_debugInfo` | page 172 | EPASTS ECU: a172 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a173_debugInfo` | page 173 | EPASTS ECU: a173 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a174_debugInfo` | page 174 | EPASTS ECU: a174 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a175_debugInfo` | page 175 | EPASTS ECU: a175 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a176_debugInfo` | page 176 | EPASTS ECU: a176 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a177_debugInfo` | page 177 | EPASTS ECU: a177 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a178_debugInfo` | page 178 | EPASTS ECU: a178 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a179_debugInfo` | page 179 | EPASTS ECU: a179 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a180_debugInfo` | page 180 | EPASTS ECU: a180 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a181_debugInfo` | page 181 | EPASTS ECU: a181 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a182_debugInfo` | page 182 | EPASTS ECU: a182 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a183_debugInfo` | page 183 | EPASTS ECU: a183 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a184_debugInfo` | page 184 | EPASTS ECU: a184 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a185_debugInfo` | page 185 | EPASTS ECU: a185 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a186_debugInfo` | page 186 | EPASTS ECU: a186 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a188_debugInfo` | page 188 | EPASTS ECU: a188 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a189_debugInfo` | page 189 | EPASTS ECU: a189 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a190_debugInfo` | page 190 | EPASTS ECU: a190 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a191_debugInfo` | page 191 | EPASTS ECU: a191 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a192_debugInfo` | page 192 | EPASTS ECU: a192 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a193_debugInfo` | page 193 | EPASTS ECU: a193 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a194_debugInfo` | page 194 | EPASTS ECU: a194 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a195_debugInfo` | page 195 | EPASTS ECU: a195 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a196_debugInfo` | page 196 | EPASTS ECU: a196 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a197_debugInfo` | page 197 | EPASTS ECU: a197 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a198_debugInfo` | page 198 | EPASTS ECU: a198 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a199_debugInfo` | page 199 | EPASTS ECU: a199 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a200_debugInfo` | page 200 | EPASTS ECU: a200 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a201_debugInfo` | page 201 | EPASTS ECU: a201 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a202_debugInfo` | page 202 | EPASTS ECU: a202 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a203_debugInfo` | page 203 | EPASTS ECU: a203 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a204_debugInfo` | page 204 | EPASTS ECU: a204 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a205_debugInfo` | page 205 | EPASTS ECU: a205 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a206_debugInfo` | page 206 | EPASTS ECU: a206 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a207_debugInfo` | page 207 | EPASTS ECU: a207 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a208_debugInfo` | page 208 | EPASTS ECU: a208 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a209_debugInfo` | page 209 | EPASTS ECU: a209 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a210_debugInfo` | page 210 | EPASTS ECU: a210 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a211_debugInfo` | page 211 | EPASTS ECU: a211 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a212_debugInfo` | page 212 | EPASTS ECU: a212 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a213_debugInfo` | page 213 | EPASTS ECU: a213 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a214_debugInfo` | page 214 | EPASTS ECU: a214 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a215_debugInfo` | page 215 | EPASTS ECU: a215 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a216_debugInfo` | page 216 | EPASTS ECU: a216 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a217_debugInfo` | page 217 | EPASTS ECU: a217 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a218_debugInfo` | page 218 | EPASTS ECU: a218 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a219_debugInfo` | page 219 | EPASTS ECU: a219 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a220_debugInfo` | page 220 | EPASTS ECU: a220 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a221_debugInfo` | page 221 | EPASTS ECU: a221 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a222_debugInfo` | page 222 | EPASTS ECU: a222 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a223_debugInfo` | page 223 | EPASTS ECU: a223 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a224_debugInfo` | page 224 | EPASTS ECU: a224 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a225_debugInfo` | page 225 | EPASTS ECU: a225 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a226_debugInfo` | page 226 | EPASTS ECU: a226 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a227_debugInfo` | page 227 | EPASTS ECU: a227 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a228_debugInfo` | page 228 | EPASTS ECU: a228 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a229_debugInfo` | page 229 | EPASTS ECU: a229 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a230_debugInfo` | page 230 | EPASTS ECU: a230 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a231_debugInfo` | page 231 | EPASTS ECU: a231 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a232_debugInfo` | page 232 | EPASTS ECU: a232 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a233_debugInfo` | page 233 | EPASTS ECU: a233 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a234_debugInfo` | page 234 | EPASTS ECU: a234 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a235_debugInfo` | page 235 | EPASTS ECU: a235 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a236_debugInfo` | page 236 | EPASTS ECU: a236 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a237_debugInfo` | page 237 | EPASTS ECU: a237 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a238_debugInfo` | page 238 | EPASTS ECU: a238 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a239_debugInfo` | page 239 | EPASTS ECU: a239 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a240_debugInfo` | page 240 | EPASTS ECU: a240 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a241_debugInfo` | page 241 | EPASTS ECU: a241 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a242_debugInfo` | page 242 | EPASTS ECU: a242 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a243_debugInfo` | page 243 | EPASTS ECU: a243 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a244_debugInfo` | page 244 | EPASTS ECU: a244 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a245_debugInfo` | page 245 | EPASTS ECU: a245 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a246_debugInfo` | page 246 | EPASTS ECU: a246 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a247_debugInfo` | page 247 | EPASTS ECU: a247 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a248_debugInfo` | page 248 | EPASTS ECU: a248 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a249_debugInfo` | page 249 | EPASTS ECU: a249 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a250_debugInfo` | page 250 | EPASTS ECU: a250 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a252_debugInfo` | page 252 | EPASTS ECU: a252 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a253_debugInfo` | page 253 | EPASTS ECU: a253 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a254_debugInfo` | page 254 | EPASTS ECU: a254 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a255_debugInfo` | page 255 | EPASTS ECU: a255 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a256_debugInfo` | page 256 | EPASTS ECU: a256 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a257_debugInfo` | page 257 | EPASTS ECU: a257 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a258_debugInfo` | page 258 | EPASTS ECU: a258 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a259_debugInfo` | page 259 | EPASTS ECU: a259 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a260_debugInfo` | page 260 | EPASTS ECU: a260 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a261_debugInfo` | page 261 | EPASTS ECU: a261 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a262_debugInfo` | page 262 | EPASTS ECU: a262 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a263_debugInfo` | page 263 | EPASTS ECU: a263 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |
| `EPASTS_a264_degradedECU` | page 264 | EPASTS ECU: a264 degraded ECU | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `OWN_ECU_SIDE`<br>2 = `OTHER_ECU_SIDE`<br>3 = `BOTH_ECU_SIDES` | plausible |
| `EPASTS_a264_vehicleSpeed` | page 264 | EPASTS ECU: a264 vehicle speed | 24\|16 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6553.5 |  | plausible |
| `EPASTS_a264_powerRatio` | page 264 | EPASTS ECU: a264 power ratio | 40\|8 | little-endian | unsigned | 1 | 0 | percent | 0 to 255 |  | plausible |
| `EPASTS_a264_ownSideDegradationReason` | page 264 | EPASTS ECU: a264 own side degradation reason | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NO_DEGRADATION_ON_THIS_ECU_SIDE`<br>4 = `CORE1_DEGRADATION`<br>8 = `BRIDGE_FET_JUNCTION_TEMPERATURE`<br>12 = `RELAY_FET_JUNCTION_TEMPERATURE`<br>20 = `REVERSE_BATTERY_FET_JUNCTION_TEMPERATURE`<br>24 = `MAIN_BOARD_TEMPERATURE`<br>28 = `BATTERY_FET_JUNCTION_TEMPERATURE`<br>32 = `MOTOR_COIL_TEMPERATURE`<br>36 = `POWER_MODULE_TEMPERATURE`<br>40 = `PHASECURRENT_SHUNT_TEMPERATURE`<br>44 = `DCLINK_SHUNT_TEMPERATURE`<br>48 = `EMIFILTER_CMC_TEMPERATURE`<br>52 = `EMIFILTER_DMC_TEMPERATURE`<br>80 = `DC_LINK_CAPACITOR_TEMPERATURE`<br>84 = `PHASECURRENT_SHUNT_TEMPERATURE_MOMENTARY`<br>92 = `DC_LINK_CAPACITOR_HOTSPOTCASEDIFF_TEMPERATURE` | plausible |
| `EPASTS_a264_otherSideDegradationReason` | page 264 | EPASTS ECU: a264 other side degradation reason | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NO_DEGRADATION_ON_THIS_ECU_SIDE`<br>4 = `CORE1_DEGRADATION`<br>8 = `BRIDGE_FET_JUNCTION_TEMPERATURE`<br>12 = `RELAY_FET_JUNCTION_TEMPERATURE`<br>20 = `REVERSE_BATTERY_FET_JUNCTION_TEMPERATURE`<br>24 = `MAIN_BOARD_TEMPERATURE`<br>28 = `BATTERY_FET_JUNCTION_TEMPERATURE`<br>32 = `MOTOR_COIL_TEMPERATURE`<br>36 = `POWER_MODULE_TEMPERATURE`<br>40 = `PHASECURRENT_SHUNT_TEMPERATURE`<br>44 = `DCLINK_SHUNT_TEMPERATURE`<br>48 = `EMIFILTER_CMC_TEMPERATURE`<br>52 = `EMIFILTER_DMC_TEMPERATURE`<br>80 = `DC_LINK_CAPACITOR_TEMPERATURE`<br>84 = `PHASECURRENT_SHUNT_TEMPERATURE_MOMENTARY`<br>92 = `DC_LINK_CAPACITOR_HOTSPOTCASEDIFF_TEMPERATURE` | plausible |
| `EPASTS_a265_degradedECU` | page 265 | EPASTS ECU: a265 degraded ECU | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `OWN_ECU_SIDE`<br>2 = `OTHER_ECU_SIDE`<br>3 = `BOTH_ECU_SIDES` | plausible |
| `EPASTS_a265_vehicleSpeed` | page 265 | EPASTS ECU: a265 vehicle speed | 24\|16 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6553.5 |  | plausible |
| `EPASTS_a265_rawMcuTemperature` | page 265 | EPASTS ECU: a265 raw mcu temperature | 40\|16 | little-endian | unsigned | 1 | -100 | C | -100 to 65435 |  | plausible |
| `EPASTS_a265_degradedCurrentLimit` | page 265 | EPASTS ECU: a265 degraded current limit | 56\|8 | little-endian | unsigned | 1 | 0 | A | 0 to 255 |  | plausible |
| `EPASTS_a266_cdpAssistFactor` | page 266 | EPASTS ECU: a266 cdp assist factor | 16\|8 | little-endian | unsigned | 1 | 0 | percent | 0 to 255 |  | plausible |
| `EPASTS_a266_vehicleSpeed` | page 266 | EPASTS ECU: a266 vehicle speed | 24\|16 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6553.5 |  | plausible |
| `EPASTS_a267_vehicleSpeed` | page 267 | EPASTS ECU: a267 vehicle speed | 16\|16 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6553.5 |  | plausible |
| `EPASTS_a267_velocityEstimatorState` | page 267 | EPASTS ECU: a267 velocity estimator state | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NOT_INITIALIZED`<br>1 = `WHEELS_NORMAL`<br>2 = `WHEELS_REDUCED`<br>3 = `BACKUP_WHEELS_A`<br>4 = `BACKUP_WHEELS_B`<br>5 = `BACKUP_MOTOR` | plausible |
| `EPASTS_a269_vehicleSpeed` | page 269 | EPASTS ECU: a269 vehicle speed | 16\|16 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 6553.5 |  | plausible |
| `EPASTS_a270_debugInfo` | page 270 | EPASTS ECU: a270 debug info | 16\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | layout-only |

## Multiplexing

`EPASTS_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 5 (1 signals), page 6 (1 signals), page 7 (1 signals), page 9 (1 signals), page 10 (1 signals), page 11 (1 signals), page 12 (1 signals), page 13 (1 signals), page 14 (1 signals), page 15 (1 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (1 signals), page 21 (1 signals), page 22 (1 signals), page 23 (1 signals), page 24 (1 signals), page 25 (1 signals), page 26 (1 signals), page 27 (1 signals), page 28 (1 signals), page 29 (1 signals), page 30 (1 signals), page 31 (1 signals), page 32 (1 signals), page 33 (1 signals), page 34 (1 signals), page 35 (1 signals), page 36 (1 signals), page 37 (1 signals), page 38 (1 signals), page 39 (1 signals), page 40 (1 signals), page 41 (1 signals), page 42 (1 signals), page 43 (1 signals), page 44 (1 signals), page 45 (1 signals), page 46 (1 signals), page 47 (1 signals), page 48 (1 signals), page 49 (1 signals), page 50 (1 signals), page 51 (1 signals), page 52 (1 signals), page 53 (1 signals), page 54 (1 signals), page 55 (1 signals), page 56 (1 signals), page 57 (1 signals), page 58 (1 signals), page 59 (1 signals), page 60 (1 signals), page 61 (1 signals), page 62 (1 signals), page 63 (1 signals), page 64 (1 signals), page 65 (1 signals), page 66 (1 signals), page 67 (1 signals), page 68 (1 signals), page 69 (1 signals), page 70 (1 signals), page 71 (1 signals), page 72 (1 signals), page 73 (1 signals), page 74 (1 signals), page 75 (1 signals), page 76 (1 signals), page 77 (1 signals), page 78 (1 signals), page 79 (1 signals), page 80 (1 signals), page 81 (1 signals), page 82 (1 signals), page 83 (1 signals), page 84 (1 signals), page 85 (1 signals), page 86 (1 signals), page 87 (1 signals), page 88 (1 signals), page 89 (1 signals), page 90 (1 signals), page 91 (1 signals), page 92 (1 signals), page 93 (1 signals), page 94 (1 signals), page 95 (1 signals), page 96 (1 signals), page 97 (1 signals), page 98 (1 signals), page 99 (1 signals), page 100 (1 signals), page 101 (1 signals), page 102 (1 signals), page 103 (1 signals), page 104 (1 signals), page 105 (1 signals), page 106 (1 signals), page 107 (1 signals), page 108 (1 signals), page 109 (1 signals), page 110 (1 signals), page 111 (1 signals), page 112 (1 signals), page 113 (1 signals), page 114 (1 signals), page 115 (1 signals), page 116 (1 signals), page 117 (1 signals), page 118 (1 signals), page 119 (1 signals), page 120 (1 signals), page 121 (1 signals), page 122 (1 signals), page 123 (1 signals), page 124 (1 signals), page 125 (1 signals), page 126 (1 signals), page 127 (1 signals), page 128 (1 signals), page 129 (1 signals), page 130 (1 signals), page 131 (1 signals), page 132 (1 signals), page 133 (1 signals), page 134 (1 signals), page 135 (1 signals), page 136 (1 signals), page 137 (1 signals), page 138 (1 signals), page 139 (1 signals), page 140 (1 signals), page 141 (1 signals), page 142 (1 signals), page 143 (1 signals), page 144 (1 signals), page 145 (1 signals), page 146 (1 signals), page 147 (1 signals), page 148 (1 signals), page 149 (1 signals), page 150 (1 signals), page 152 (1 signals), page 153 (1 signals), page 154 (1 signals), page 155 (1 signals), page 156 (1 signals), page 157 (1 signals), page 158 (1 signals), page 159 (1 signals), page 160 (1 signals), page 161 (1 signals), page 162 (1 signals), page 163 (1 signals), page 164 (1 signals), page 165 (1 signals), page 166 (1 signals), page 167 (1 signals), page 168 (1 signals), page 169 (1 signals), page 170 (1 signals), page 171 (1 signals), page 172 (1 signals), page 173 (1 signals), page 174 (1 signals), page 175 (1 signals), page 176 (1 signals), page 177 (1 signals), page 178 (1 signals), page 179 (1 signals), page 180 (1 signals), page 181 (1 signals), page 182 (1 signals), page 183 (1 signals), page 184 (1 signals), page 185 (1 signals), page 186 (1 signals), page 188 (1 signals), page 189 (1 signals), page 190 (1 signals), page 191 (1 signals), page 192 (1 signals), page 193 (1 signals), page 194 (1 signals), page 195 (1 signals), page 196 (1 signals), page 197 (1 signals), page 198 (1 signals), page 199 (1 signals), page 200 (1 signals), page 201 (1 signals), page 202 (1 signals), page 203 (1 signals), page 204 (1 signals), page 205 (1 signals), page 206 (1 signals), page 207 (1 signals), page 208 (1 signals), page 209 (1 signals), page 210 (1 signals), page 211 (1 signals), page 212 (1 signals), page 213 (1 signals), page 214 (1 signals), page 215 (1 signals), page 216 (1 signals), page 217 (1 signals), page 218 (1 signals), page 219 (1 signals), page 220 (1 signals), page 221 (1 signals), page 222 (1 signals), page 223 (1 signals), page 224 (1 signals), page 225 (1 signals), page 226 (1 signals), page 227 (1 signals), page 228 (1 signals), page 229 (1 signals), page 230 (1 signals), page 231 (1 signals), page 232 (1 signals), page 233 (1 signals), page 234 (1 signals), page 235 (1 signals), page 236 (1 signals), page 237 (1 signals), page 238 (1 signals), page 239 (1 signals), page 240 (1 signals), page 241 (1 signals), page 242 (1 signals), page 243 (1 signals), page 244 (1 signals), page 245 (1 signals), page 246 (1 signals), page 247 (1 signals), page 248 (1 signals), page 249 (1 signals), page 250 (1 signals), page 252 (1 signals), page 253 (1 signals), page 254 (1 signals), page 255 (1 signals), page 256 (1 signals), page 257 (1 signals), page 258 (1 signals), page 259 (1 signals), page 260 (1 signals), page 261 (1 signals), page 262 (1 signals), page 263 (1 signals), page 264 (5 signals), page 265 (4 signals), page 266 (2 signals), page 267 (2 signals), page 269 (1 signals), page 270 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All EPASTS ECU messages (EPASTS)](../../epasts.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
