---
layout: default
title: "APSB_alertLog (0x5CA) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: alert log. Ethernet-side message APSB_alertLog of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 668 signals (APSB_alertID, APSB_alertSource, APSB_alertState, APSB_sw010_a04calibNotDone and 664 more). Bit layout, scaling, units and value tables."
---

# APSB_alertLog (0x5CA) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: alert log. This page documents the 668 signals of APSB_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_alertLog` |
| Ethernet-side id | 0x5CA (1482) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 668 |

## Signals of APSB_alertLog

Tesla Model Y CAN bus signals in `APSB_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_alertID` | selector | APSB ECU: alert ID | 0\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `w001_DEPRECATED`<br>2 = `w002_ldwDisabled`<br>3 = `w003_isaDisabled`<br>4 = `w004_accDisabled`<br>5 = `w005_fcwCancelled`<br>6 = `w006_aebCancelled`<br>7 = `w007_ahlbDisabled`<br>8 = `w008_parkDisabled`<br>9 = `w009_aebFault`<br>10 = `w010_radcCalibIssue`<br>11 = `w011_scaEvent`<br>12 = `w012_Cam_BootFailure`<br>13 = `w013_Cam_Watchdog`<br>14 = `w014_swAssert`<br>15 = `w015_Camera_Failsafes`<br>16 = `w016_aeb_e_event`<br>17 = `w017_Cam_Msg_MIA`<br>18 = `w018_ECU_Power_Issue`<br>19 = `w019_ECU_Stack_Overflow`<br>20 = `w020_ECU_checkstopError`<br>21 = `w021_ECU_Temperature_Issue`<br>22 = `w022_ECU_EEPROM_Failure`<br>23 = `w023_ECU_Cam_Statemismatc`<br>24 = `w024_ECU_Watchdog_Reset`<br>25 = `w025_LC_Steering_Override`<br>26 = `w026_ECU_timingIssue`<br>27 = `w027_ECU_Reset_Fault`<br>28 = `w028_spi_rx_error`<br>29 = `w029_spi_tx_error`<br>30 = `w030_Heater_Issue`<br>31 = `w031_canRxError`<br>32 = `w032_canTxError`<br>33 = `w033_gtwMia`<br>34 = `w034_sccmMia`<br>35 = `w035_espMia`<br>36 = `w036_bdyMia`<br>37 = `w037_camTacIssue`<br>38 = `w038_camFailure`<br>39 = `w039_sdm_rcm_Mia`<br>40 = `w040_autopilotAngleSaturated`<br>41 = `w041_autopilotRateSaturated`<br>42 = `w042_autopilotAborting`<br>43 = `w043_camLongRunTime`<br>44 = `w044_appMobileyeFailure`<br>45 = `w045_radMia`<br>46 = `w046_eepromRecordAbsent`<br>47 = `w047_edrEvent`<br>48 = `w048_DAS_Features_Disabled`<br>49 = `w049_eyeqVersionMismatch`<br>50 = `w050_aeb_event`<br>51 = `w051_radcEcuIssue`<br>52 = `w052_radcSensorIssue`<br>53 = `w053_radcCommIssue`<br>54 = `w054_camAutofix`<br>55 = `w055_radcVersionMismatch`<br>56 = `w056_diMia`<br>57 = `w057_mcuMia`<br>58 = `w058_epbMia`<br>59 = `w059_parkMia`<br>60 = `w060_fcw_event`<br>61 = `w061_tasMia`<br>62 = `w062_radcAlignment`<br>63 = `w063_parkVersionMismatch`<br>64 = `w064_epasMia`<br>65 = `w065_deserializerOvercurrent`<br>66 = `w066_deserializerLockLost`<br>67 = `w067_steeringAlignment`<br>68 = `w068_vlInconsistency`<br>69 = `w069_apcSpaceMasked`<br>70 = `w070_apcIncompleteCal`<br>71 = `w071_selfparkStarted`<br>72 = `w072_selfparkComplete`<br>73 = `w073_issueEscalatedLDW`<br>74 = `w074_inPathStationaryObst`<br>75 = `w075_scMia`<br>76 = `w076_mobilEyeSetC`<br>77 = `w077_pmmActive`<br>78 = `w078_pmmActive2`<br>79 = `w079_edrAvailable`<br>80 = `w080_accFailedActivation`<br>81 = `w081_pmmActiveBraking`<br>82 = `w082_inPathFSviolation`<br>83 = `w083_inPathRADObject`<br>84 = `w084_pmmIPSO`<br>85 = `w085_pmmSteering`<br>86 = `w086_robCollision`<br>87 = `w087_DEPRECATED`<br>88 = `w088_DEPRECATED`<br>89 = `w089_DEPRECATED`<br>90 = `w090_DEPRECATED`<br>91 = `w091_DEPRECATED`<br>92 = `w092_DEPRECATED`<br>93 = `w093_DEPRECATED`<br>94 = `w094_DEPRECATED`<br>95 = `w095_DEPRECATED`<br>96 = `w096_DEPRECATED`<br>97 = `w097_DEPRECATED`<br>98 = `w098_DEPRECATED`<br>99 = `w099_DEPRECATED`<br>100 = `w100_DEPRECATED`<br>101 = `w101_DEPRECATED`<br>102 = `w102_DEPRECATED`<br>103 = `w103_robExperimentalAEB`<br>104 = `w104_DEPRECATED`<br>105 = `w105_DEPRECATED`<br>106 = `w106_torsionBarOffset`<br>129 = `w129_ECU_Power_Issue`<br>130 = `w130_ECU_Thermal_Issue`<br>131 = `w131_trap_exception`<br>132 = `w132_appVersionMismatch`<br>133 = `w133_ETHSwitchError`<br>134 = `w134_appMia`<br>135 = `w135_appCritical`<br>136 = `w136_gpsDisabled`<br>137 = `w137_gpsFaultReset`<br>138 = `w138_gpsComIssue`<br>139 = `w139_udpBufferOverflow`<br>140 = `w140_vcfrontMiaVehicleBus`<br>141 = `w141_rcmMiaPartyBus`<br>142 = `w142_diMiaPartyBus`<br>143 = `w143_espMiaPartyBus`<br>144 = `w144_vcleftMiaPartyBus`<br>145 = `w145_vcrightMiaPartyBus`<br>146 = `w146_epas3pMiaPartyBus`<br>147 = `w147_vcleftMiaVehBus`<br>148 = `w148_vcrightMiaVehBus`<br>149 = `w149_epblMiaVehBus`<br>150 = `w150_sccmMiaVehBus`<br>151 = `w151_apRecovered`<br>152 = `w152_gpsFusionStatus`<br>153 = `w153_eacInhibit`<br>155 = `w155_ethLwipError`<br>156 = `w156_lwipAssert`<br>157 = `w157_autopilotReboot`<br>158 = `w158_apbMia`<br>159 = `w159_apbCritical`<br>160 = `w160_apbVersionMismatch`<br>161 = `w161_gpsAntennaDisconnected`<br>162 = `w162_TurboA_DisRegPgoodErr`<br>163 = `w163_TurboA_DisRegNFault`<br>164 = `w164_TurboA_12VFuseFault`<br>165 = `w165_TurboA_Temp_NOS`<br>166 = `w166_TurboA_SMSLockStepErr`<br>167 = `w167_TurboA_TMU_Throttle`<br>168 = `w168_TurboA_SMS_WDOG`<br>169 = `w169_TurboA_SCS_LKUP`<br>170 = `w170_TurboA_A72_watchdog`<br>171 = `w171_TurboA_SMS_taskUtilErr`<br>172 = `w172_apFeaturesUnavailable`<br>178 = `w178_TurboB_DisRegPgoodErr`<br>179 = `w179_TurboB_DisRegNFault`<br>180 = `w180_TurboB_12VFuseFault`<br>181 = `w181_TurboB_Temp_NOS`<br>182 = `w182_TurboB_SMSLockStepErr`<br>183 = `w183_TurboB_TMU_Throttle`<br>184 = `w184_TurboB_SMS_WDOG`<br>185 = `w185_TurboB_SCS_LKUP`<br>186 = `w186_TurboB_A72_watchdog`<br>187 = `w187_TurboB_SMS_taskUtilErr`<br>188 = `w188_otherTurboUartMIA`<br>189 = `w189_vcfrontMiaPartyBus`<br>190 = `w190_iboosterMia`<br>191 = `w191_timesyncError`<br>192 = `w192_CANFault`<br>193 = `w193_camWindshieldUnclean`<br>194 = `w194_accDriverResumeRqrd`<br>195 = `w195_scwUnavailable`<br>196 = `w196_stopSignWarning`<br>197 = `w197_redLightWarning`<br>198 = `w198_tsrUnavailable`<br>199 = `w199_apcAbort`<br>200 = `w200_lcSlowdown`<br>201 = `w201_lcAborting`<br>202 = `w202_scwNoisyEnvironment`<br>203 = `w203_apcActivation`<br>204 = `w204_apcFinalFront`<br>205 = `w205_apcFinalRear`<br>206 = `w206_autosteerNotEnabled`<br>207 = `w207_autosteerUnavailable`<br>208 = `w208_rackDetected`<br>209 = `w209_autoSummonRequest`<br>210 = `w210_camObstrcted`<br>211 = `w211_accNoSeatBelt`<br>212 = `w212_lcUnavailableStrikeOut`<br>213 = `w213_autosteerStruckOut`<br>214 = `w214_driverNotIntracting`<br>215 = `w215_contDriverNotIntracting`<br>216 = `w216_driverOverriding`<br>217 = `w217_lcUnavailableSpeeding`<br>218 = `w218_lcSpeedExceededLimit`<br>219 = `w219_lcTempUnavailableSpeed`<br>220 = `w220_lcTempUnavailableRoad`<br>221 = `w221_accRadarBlind`<br>222 = `w222_accCameraBlind`<br>223 = `w223_accObjectInPath`<br>224 = `w224_accCameraCalibration`<br>225 = `w225_lcDegradedVisSpeedLmt`<br>226 = `w226_lcCamCalNeededSpeedLmt`<br>227 = `w227_virtualWallBlocked`<br>228 = `w228_DEPRECATED`<br>229 = `w229_alcUltrasoundDamaged`<br>230 = `w230_alcUltrasoundBlocked`<br>231 = `w231_idfEvent`<br>232 = `w232_laneChangeRequested`<br>235 = `w235_a72LoopDetected`<br>236 = `w236_canSharedMemError`<br>237 = `w237_faultMgrEventDetected`<br>238 = `w238_resetReason`<br>241 = `w241_ddrInitFailures`<br>242 = `w242_tripMBISTFailure`<br>243 = `w243_tripHWErrorStatus`<br>244 = `w244_gpuHWFaultStatus`<br>245 = `w245_eloopRxFromUnexpectedSourceMAC`<br>246 = `w246_ethloopSwitchPortLinkDown`<br>247 = `w247_ethernetFrameError`<br>248 = `w248_ethloopSwitchPoorSqi`<br>249 = `w249_ufsFailures`<br>250 = `w250_ethloopSwitchMemUsageTooHighPort2`<br>251 = `w251_ethloopSwitchMemUsageTooHighPort3`<br>252 = `w252_ethSwitchPortLinkDown`<br>253 = `w253_powerStateTimeout`<br>254 = `w254_sleepStateTimeout`<br>255 = `w255_bootHealth`<br>257 = `w257_assertFailure`<br>258 = `w258_qspiFlashSectorChecksumMismatch`<br>259 = `w259_qspiFailure`<br>260 = `w260_pgoodFailure`<br>261 = `w261_vrmFaultGrpA`<br>262 = `w262_vrmFaultGrpB`<br>263 = `w263_vrmFaultGrpC`<br>264 = `w264_ddrPhy0Failures`<br>265 = `w265_ddrPhy1Failures`<br>266 = `w266_ddrPhy2Failures`<br>267 = `w267_ddrPhy3Failures`<br>268 = `w268_ddrControllerFailures`<br>269 = `w269_ethSwitchRxPageCountTooHighPort0_3`<br>270 = `w270_ethSwitchRxPageCountTooHighPort4_7`<br>271 = `w271_ddrScheduler0EccErrors`<br>272 = `w272_ddrScheduler1EccErrors`<br>273 = `w273_ddrScheduler2EccErrors`<br>274 = `w274_ddrScheduler3EccErrors`<br>275 = `w275_ddrScheduler4EccErrors`<br>276 = `w276_ddrScheduler5EccErrors`<br>277 = `w277_ddrScheduler6EccErrors`<br>278 = `w278_ddrScheduler7EccErrors`<br>279 = `w279_ufsPartitionError`<br>280 = `w280_pepsMia`<br>281 = `w281_rsaMia`<br>282 = `w282_smmuError`<br>283 = `w283_psfaMia`<br>284 = `w284_cam12VBuckBoostAPwrIssue`<br>285 = `w285_cam12VBuckBoostBPwrIssue`<br>286 = `w286_cam12VEFuseAPrimaryIssue`<br>287 = `w287_cam12VEFuseASecondaryIssue`<br>288 = `w288_brakeboosterMia`<br>289 = `w289_turboTemperatureWarning`<br>290 = `w290_cam12VBuckBoostBPwrRinging`<br>291 = `w291_eplannerError`<br>292 = `w292_CH_busOff`<br>293 = `w293_PARTY_busOff`<br>294 = `w294_VEH_busOff`<br>295 = `w295_PT_busOff`<br>296 = `w296_wdogMonTaskDeadlineMiss`<br>297 = `w297_earlyWDogAlert`<br>298 = `w298_cpuToApCanSharedMemError`<br>299 = `w299_apToCpuCanSharedMemError`<br>300 = `w300_sharedMemoryAccessError`<br>301 = `w301_nocTimeoutDetected`<br>302 = `w302_canAPShmFifoFull`<br>303 = `w303_canAPShmFifoEmpty`<br>304 = `w304_dataAbort`<br>305 = `w305_gpsPgoodFailure`<br>306 = `w306_ethPgoodFailure`<br>307 = `w307_eccEventDetected`<br>308 = `w308_pmicErrorDetected`<br>309 = `w309_ethBridgeDown`<br>310 = `w310_wakeBootMetrics`<br>311 = `w311_apbdgDasMia`<br>312 = `w312_apbdgApMia`<br>313 = `w313_BDY_busOff`<br>315 = `w315_epas3pMiaBdyBus`<br>316 = `w316_apBootHealth`<br>317 = `w317_uiMia`<br>318 = `w318_ethernetNetworkBufferHighWatermark`<br>319 = `w319_vehDasImposterDetected`<br>320 = `w320_eplannerPreconditionsMet` | plausible |
| `APSB_alertSource` |  | APSB ECU: alert source | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TURBOA`<br>1 = `TURBOB` | plausible |
| `APSB_alertState` |  | APSB ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `APSB_sw010_a04calibNotDone` | page 10 | APSB ECU: sw010 a04calib not done | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw010_a05calibReqd` | page 10 | APSB ECU: sw010 a05calib reqd | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw010_a06calibNotOK` | page 10 | APSB ECU: sw010 a06calib not OK | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw010_a08PlantMode` | page 10 | APSB ECU: sw010 a08 plant mode | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw010_HorizontalMisalignment` | page 10 | APSB ECU: sw010 horizontal misalignment | 20\|16 | little-endian | unsigned | 0.00137332 | -45 | deg | -45 to 45.0005262 |  | plausible |
| `APSB_sw010_VerticalMisalignment` | page 10 | APSB ECU: sw010 vertical misalignment | 36\|10 | little-endian | unsigned | 0.087977 | -45 | deg | -45 to 45.000471 |  | plausible |
| `APSB_sw010_unusedBits` | page 10 | APSB ECU: sw010 unused bits | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `APSB_sw010_VmaPlausibility` | page 10 | APSB ECU: sw010 vma plausibility | 48\|16 | little-endian | unsigned | 1.52587890625e-05 | 0 | FIXME | 0 to 0.999984741211 |  | plausible |
| `APSB_sw019_taskId` | page 19 | APSB ECU: sw019 task id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `TASKS_RESERVED`<br>1 = `TASKS_INIT`<br>2 = `TASKS_CAN`<br>3 = `TASKS_UDS`<br>4 = `TASKS_MOBILEYE`<br>5 = `TASKS_VEHICLE`<br>6 = `TASKS_SMS_SMS_UART_TX`<br>7 = `TASKS_SMS_SMS_UART_RX`<br>8 = `TASK_DEBUG_SERIAL_TX`<br>9 = `TASK_DEBUG_SMS_SERIAL_RX`<br>10 = `TASKS_PARTY_CAN`<br>11 = `TASKS_CH_CAN`<br>12 = `TASKS_RADAR_CAN`<br>13 = `TASKS_VEH_CAN`<br>14 = `TASKS_MBX_AP_TX_LOW`<br>15 = `TASKS_MBX_AP_TX_HIGH`<br>16 = `TASKS_MBX_AP_RX_LOW`<br>17 = `TASKS_MBX_AP_RX_HIGH`<br>18 = `TASKS_MBX_SCS_TX_LOW`<br>19 = `TASKS_MBX_SCS_TX_HIGH`<br>20 = `TASKS_MBX_SCS_RX_LOW`<br>21 = `TASKS_MBX_SCS_RX_HIGH`<br>22 = `TASKS_MBX_RELAY`<br>23 = `TASKS_WDG_TASK`<br>24 = `TASKS_TMU`<br>25 = `TASKS_CAN_AP_TX`<br>26 = `TASKS_CAN_AP_RX`<br>27 = `TASKS_SMS_SERIAL`<br>28 = `TASKS_APP_1KHZ`<br>29 = `TASKS_APP_1HZ`<br>30 = `TASKS_ISOTERM_SMS`<br>31 = `TASKS_ISOTERM_A72`<br>32 = `MAX_TASK_ID` | plausible |
| `APSB_sw019_numFreeBytes` | page 19 | APSB ECU: sw019 num free bytes | 24\|8 | little-endian | unsigned | 1 | -191 | # of bytes | -191 to 64 |  | plausible |
| `APSB_sw019_timeStamp` | page 19 | APSB ECU: sw019 time stamp | 32\|32 | little-endian | unsigned | 1 | 0 | ms | 0 to 4294967295 |  | plausible |
| `APSB_sw020_unusedW0` | page 20 | APSB ECU: sw020 unused W0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw020_unusedW1` | page 20 | APSB ECU: sw020 unused W1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw020_unusedW2` | page 20 | APSB ECU: sw020 unused W2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw021_tempSensorId` | page 21 | APSB ECU: sw021 temp sensor id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw021_minThreshold` | page 21 | APSB ECU: sw021 min threshold | 24\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw021_maxThreshold` | page 21 | APSB ECU: sw021 max threshold | 32\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw021_currentTemperature` | page 21 | APSB ECU: sw021 current temperature | 40\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw021_unusedWord` | page 21 | APSB ECU: sw021 unused word | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw024_Task_ID` | page 24 | APSB ECU: sw024 task ID | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw024_numVirtualLaneVeh` | page 24 | APSB ECU: sw024 num virtual lane veh | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw024_currentVehicleApp` | page 24 | APSB ECU: sw024 current vehicle app | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw024_taskProgramCounter` | page 24 | APSB ECU: sw024 task program counter | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `APSB_sw027_JTAG_Reset` | page 27 | APSB ECU: sw027 JTAG reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Core_Reset` | page 27 | APSB ECU: sw027 core reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Bit_0` | page 27 | APSB ECU: sw027 unused bit 0 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_CPU_Checkstop_Error` | page 27 | APSB ECU: sw027 CPU checkstop error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_PLL_0_Failure` | page 27 | APSB ECU: sw027 PLL 0 failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Clock_Monitor_0_Low` | page 27 | APSB ECU: sw027 clock monitor 0 low | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Clock_Monitor_0_Off` | page 27 | APSB ECU: sw027 clock monitor 0 off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_LVD_4v5` | page 27 | APSB ECU: sw027 LVD 4v5 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Flash_Fatal_Error` | page 27 | APSB ECU: sw027 flash fatal error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_PLL_1_Failure` | page 27 | APSB ECU: sw027 PLL 1 failure | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Bit_1` | page 27 | APSB ECU: sw027 unused bit 1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_f_PLL_1_Off` | page 27 | APSB ECU: sw027 f PLL 1 off | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Nibble` | page 27 | APSB ECU: sw027 unused nibble | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw027_LVD_1v2` | page 27 | APSB ECU: sw027 LVD 1v2 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Bit_2` | page 27 | APSB ECU: sw027 unused bit 2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Watchdog` | page 27 | APSB ECU: sw027 watchdog | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Bit_3` | page 27 | APSB ECU: sw027 unused bit 3 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_LVD_2v7_VREG` | page 27 | APSB ECU: sw027 LVD 2v7 VREG | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_LVD_2v7_Flash` | page 27 | APSB ECU: sw027 LVD 2v7 flash | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_LVD_2v7_IO` | page 27 | APSB ECU: sw027 LVD 2v7 IO | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Bit_4` | page 27 | APSB ECU: sw027 unused bit 4 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_Byte` | page 27 | APSB ECU: sw027 unused byte | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw027_ESR0` | page 27 | APSB ECU: sw027 ESR0 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_ESR1` | page 27 | APSB ECU: sw027 ESR1 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_SW` | page 27 | APSB ECU: sw027 SW | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_STM0` | page 27 | APSB ECU: sw027 STM0 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_STM1` | page 27 | APSB ECU: sw027 STM1 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_STM2` | page 27 | APSB ECU: sw027 STM2 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_CBS_SYSTEM` | page 27 | APSB ECU: sw027 CBS SYSTEM | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_CBS_DEBUG` | page 27 | APSB ECU: sw027 CBS DEBUG | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_CBS_APP` | page 27 | APSB ECU: sw027 CBS APP | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_EVR13` | page 27 | APSB ECU: sw027 EVR13 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_EVR33` | page 27 | APSB ECU: sw027 EVR33 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_SWD` | page 27 | APSB ECU: sw027 SWD | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_STDBY_WDG` | page 27 | APSB ECU: sw027 STDBY WDG | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_PORST` | page 27 | APSB ECU: sw027 PORST | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw027_Unused_word` | page 27 | APSB ECU: sw027 unused word | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `APSB_sw030_heaterState` | page 30 | APSB ECU: sw030 heater state | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw030_unusedByte` | page 30 | APSB ECU: sw030 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw030_unusedW0` | page 30 | APSB ECU: sw030 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw030_unusedW1` | page 30 | APSB ECU: sw030 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw033_carConfig` | page 33 | APSB ECU: sw033 car config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw033_chNm` | page 33 | APSB ECU: sw033 ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw033_vin` | page 33 | APSB ECU: sw033 vin | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw033_carState` | page 33 | APSB ECU: sw033 car state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw034_sccmMia` | page 34 | APSB ECU: sw034 sccm mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw034_unusedByte` | page 34 | APSB ECU: sw034 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw034_unusedW0` | page 34 | APSB ECU: sw034 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw034_unusedW1` | page 34 | APSB ECU: sw034 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw035_wheelSpeeds` | page 35 | APSB ECU: sw035 wheel speeds | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw035_status` | page 35 | APSB ECU: sw035 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw035_wheelRotation` | page 35 | APSB ECU: sw035 wheel rotation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw035_redundantBrakingStatus` | page 35 | APSB ECU: sw035 redundant braking status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw036_bdyMia` | page 36 | APSB ECU: sw036 bdy mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw036_unusedByte` | page 36 | APSB ECU: sw036 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw036_unusedW0` | page 36 | APSB ECU: sw036 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw036_unusedW1` | page 36 | APSB ECU: sw036 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw039_sdm_rcm_Mia` | page 39 | APSB ECU: sw039 sdm rcm mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw039_unusedByte` | page 39 | APSB ECU: sw039 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw039_unusedW0` | page 39 | APSB ECU: sw039 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw039_unusedW1` | page 39 | APSB ECU: sw039 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw045_radMia` | page 45 | APSB ECU: sw045 rad mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw045_unusedByte` | page 45 | APSB ECU: sw045 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw045_unusedW0` | page 45 | APSB ECU: sw045 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw045_unusedW1` | page 45 | APSB ECU: sw045 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw048_swAssert` | page 48 | APSB ECU: sw048 sw assert | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_thermalIssue` | page 48 | APSB ECU: sw048 thermal issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_powerIssue` | page 48 | APSB ECU: sw048 power issue | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_stackOverflow` | page 48 | APSB ECU: sw048 stack overflow | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_checkStop` | page 48 | APSB ECU: sw048 check stop | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_ecuWatchdog` | page 48 | APSB ECU: sw048 ecu watchdog | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_ecuReset` | page 48 | APSB ECU: sw048 ecu reset | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_radcVersionMismatch` | page 48 | APSB ECU: sw048 radc version mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_radcCalibration` | page 48 | APSB ECU: sw048 radc calibration | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_radcMia` | page 48 | APSB ECU: sw048 radc mia | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_eyeQVersionMismatch` | page 48 | APSB ECU: sw048 eye q version mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_camIssue` | page 48 | APSB ECU: sw048 cam issue | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_parkerIssue` | page 48 | APSB ECU: sw048 parker issue | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_prolongedUiMia` | page 48 | APSB ECU: sw048 prolonged ui mia | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw048_uiMiaAtBootup` | page 48 | APSB ECU: sw048 ui mia at bootup | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_a01ecuInternalPerf` | page 51 | APSB ECU: sw051 a01ecu internal perf | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_a02flashPerformance` | page 51 | APSB ECU: sw051 a02flash performance | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_a03vBatHigh` | page 51 | APSB ECU: sw051 a03v bat high | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_a09configMismatch` | page 51 | APSB ECU: sw051 a09config mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_a52radomeHtrInop` | page 51 | APSB ECU: sw051 a52radome htr inop | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_unused` | page 51 | APSB ECU: sw051 unused | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw051_SCUTemperature` | page 51 | APSB ECU: sw051 SCU temperature | 24\|8 | little-endian | signed | 1 | 0 |  | -128 to 127 |  | layout-only |
| `APSB_sw051_HWFail` | page 51 | APSB ECU: sw051 HW fail | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_SGUFail` | page 51 | APSB ECU: sw051 SGU fail | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw051_unusedBits` | page 51 | APSB ECU: sw051 unused bits | 34\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `APSB_sw051_unusedB0` | page 51 | APSB ECU: sw051 unused B0 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw051_unusedW1` | page 51 | APSB ECU: sw051 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw052_a07sensorBlinded` | page 52 | APSB ECU: sw052 a07sensor blinded | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_sensorDirty` | page 52 | APSB ECU: sw052 sensor dirty | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_HWFail` | page 52 | APSB ECU: sw052 HW fail | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_overTemperature` | page 52 | APSB ECU: sw052 over temperature | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_underTemperature` | page 52 | APSB ECU: sw052 under temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_chirpError` | page 52 | APSB ECU: sw052 chirp error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_rspError` | page 52 | APSB ECU: sw052 rsp error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw052_sensorBlocked` | page 52 | APSB ECU: sw052 sensor blocked | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a10canBusOff` | page 53 | APSB ECU: sw053 a10can bus off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a11bdyMIA` | page 53 | APSB ECU: sw053 a11bdy MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a12espMIA` | page 53 | APSB ECU: sw053 a12esp MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a13gtwMIA` | page 53 | APSB ECU: sw053 a13gtw MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a14sccmMIA` | page 53 | APSB ECU: sw053 a14sccm MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a15adasMIA` | page 53 | APSB ECU: sw053 a15adas MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a16bdyInvalidCount` | page 53 | APSB ECU: sw053 a16bdy invalid count | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a17adasInvalidCount` | page 53 | APSB ECU: sw053 a17adas invalid count | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a18espInvalidCount` | page 53 | APSB ECU: sw053 a18esp invalid count | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a19sccmInvalidCount` | page 53 | APSB ECU: sw053 a19sccm invalid count | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a20bdyInvalidChkSm` | page 53 | APSB ECU: sw053 a20bdy invalid chk sm | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a21espInvalidChkSm` | page 53 | APSB ECU: sw053 a21esp invalid chk sm | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a22sccmInvalidChkSm` | page 53 | APSB ECU: sw053 a22sccm invalid chk sm | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a23sccmInvalidChkSm` | page 53 | APSB ECU: sw053 a23sccm invalid chk sm | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a24absValidity` | page 53 | APSB ECU: sw053 a24abs validity | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a25ambTValidity` | page 53 | APSB ECU: sw053 a25amb t validity | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a26brakeValidity` | page 53 | APSB ECU: sw053 a26brake validity | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a27CntryCdValidity` | page 53 | APSB ECU: sw053 a27 cntry cd validity | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a28espValidity` | page 53 | APSB ECU: sw053 a28esp validity | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a29longAccOffValidity` | page 53 | APSB ECU: sw053 a29long acc off validity | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a30longAccValidity` | page 53 | APSB ECU: sw053 a30long acc validity | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a31odoValidity` | page 53 | APSB ECU: sw053 a31odo validity | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a32gearValidity` | page 53 | APSB ECU: sw053 a32gear validity | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a33steerAngValidity` | page 53 | APSB ECU: sw053 a33steer ang validity | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a34steerAngSpdValidity` | page 53 | APSB ECU: sw053 a34steer ang spd validity | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a35indctrValidity` | page 53 | APSB ECU: sw053 a35indctr validity | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a36vehStndStllValidty` | page 53 | APSB ECU: sw053 a36veh stnd stll validty | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a37vinValidity` | page 53 | APSB ECU: sw053 a37vin validity | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a38whlRotValidity` | page 53 | APSB ECU: sw053 a38whl rot validity | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a39whlSpdValidity` | page 53 | APSB ECU: sw053 a39whl spd validity | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a40whlStndStllValidty` | page 53 | APSB ECU: sw053 a40whl stnd stll validty | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a41wiperValidity` | page 53 | APSB ECU: sw053 a41wiper validity | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a42xwdValidity` | page 53 | APSB ECU: sw053 a42xwd validity | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a43yawOffValidity` | page 53 | APSB ECU: sw053 a43yaw off validity | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a44yawValidity` | page 53 | APSB ECU: sw053 a44yaw validity | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a48steerAngOffSanity` | page 53 | APSB ECU: sw053 a48steer ang off sanity | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a49tireSizeSanity` | page 53 | APSB ECU: sw053 a49tire size sanity | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a50velocitySanity` | page 53 | APSB ECU: sw053 a50velocity sanity | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a51yawSanity` | page 53 | APSB ECU: sw053 a51yaw sanity | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a53espmodValidity` | page 53 | APSB ECU: sw053 a53espmod validity | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a54gtwmodValidity` | page 53 | APSB ECU: sw053 a54gtwmod validity | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a55stwmodValidity` | page 53 | APSB ECU: sw053 a55stwmod validity | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a56bcmodValidity` | page 53 | APSB ECU: sw053 a56bcmod validity | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a57dimodValidity` | page 53 | APSB ECU: sw053 a57dimod validity | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a59drmiInvalidChkSm` | page 53 | APSB ECU: sw053 a59drmi invalid chk sm | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a60drmiInvalidCount` | page 53 | APSB ECU: sw053 a60drmi invalid count | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a61radPositionMismatch` | page 53 | APSB ECU: sw053 a61rad position mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw053_a62strRackMismatch` | page 53 | APSB ECU: sw053 a62str rack mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw055_detectedRadcVersion` | page 55 | APSB ECU: sw055 detected radc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `APSB_sw055_expectedCrcLsw` | page 55 | APSB ECU: sw055 expected crc lsw | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw056_diMia` | page 56 | APSB ECU: sw056 di mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw056_unusedByte` | page 56 | APSB ECU: sw056 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw056_unusedW0` | page 56 | APSB ECU: sw056 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw056_unusedW1` | page 56 | APSB ECU: sw056 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw058_epbMia` | page 58 | APSB ECU: sw058 epb mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw058_unusedByte` | page 58 | APSB ECU: sw058 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw058_unusedW0` | page 58 | APSB ECU: sw058 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw058_unusedW1` | page 58 | APSB ECU: sw058 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw059_sdiFront` | page 59 | APSB ECU: sw059 sdi front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_sdiRear` | page 59 | APSB ECU: sw059 sdi rear | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_status` | page 59 | APSB ECU: sw059 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_sensorStatusFront` | page 59 | APSB ECU: sw059 sensor status front | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_pasFrontMiddle` | page 59 | APSB ECU: sw059 pas front middle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_sensorStatusRear` | page 59 | APSB ECU: sw059 sensor status rear | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_pasRearMiddle` | page 59 | APSB ECU: sw059 pas rear middle | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_pscStatus` | page 59 | APSB ECU: sw059 psc status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_pscVehSlot` | page 59 | APSB ECU: sw059 psc veh slot | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_status2` | page 59 | APSB ECU: sw059 status2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_oloDict` | page 59 | APSB ECU: sw059 olo dict | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw059_oocStatus` | page 59 | APSB ECU: sw059 ooc status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw061_states` | page 61 | APSB ECU: sw061 states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw063_expectedMajorVer` | page 63 | APSB ECU: sw063 expected major ver | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw063_detectedMajorVer` | page 63 | APSB ECU: sw063 detected major ver | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw063_expectedMinorVer` | page 63 | APSB ECU: sw063 expected minor ver | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw063_detectedMinorVer` | page 63 | APSB ECU: sw063 detected minor ver | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw063_expectedSubMinorVer` | page 63 | APSB ECU: sw063 expected sub minor ver | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw063_detectedSubMinorVer` | page 63 | APSB ECU: sw063 detected sub minor ver | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw064_sysStatus` | page 64 | APSB ECU: sw064 sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw064_status` | page 64 | APSB ECU: sw064 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw070_currTireFitment` | page 70 | APSB ECU: sw070 curr tire fitment | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw070_lastTireFitment` | page 70 | APSB ECU: sw070 last tire fitment | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw070_diGear` | page 70 | APSB ECU: sw070 di gear | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw070_driveRail` | page 70 | APSB ECU: sw070 drive rail | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw070_accRail` | page 70 | APSB ECU: sw070 acc rail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw070_temperature` | page 70 | APSB ECU: sw070 temperature | 32\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87.5 |  | plausible |
| `APSB_sw070_currentSpeed` | page 70 | APSB ECU: sw070 current speed | 40\|12 | little-endian | unsigned | 0.1 | -204.7 | mph | -204.7 to 204.8 |  | plausible |
| `APSB_sw071_selfParkType` | page 71 | APSB ECU: sw071 self park type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw071_endPosX` | page 71 | APSB ECU: sw071 end pos x | 20\|10 | little-endian | unsigned | 0.05 | -25.6 | m | -25.6 to 25.55 |  | plausible |
| `APSB_sw071_endPosY` | page 71 | APSB ECU: sw071 end pos y | 30\|10 | little-endian | unsigned | 0.05 | -25.6 | m | -25.6 to 25.55 |  | plausible |
| `APSB_sw071_roadClass` | page 71 | APSB ECU: sw071 road class | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw071_driverPresent` | page 71 | APSB ECU: sw071 driver present | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw071_airSuspension` | page 71 | APSB ECU: sw071 air suspension | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw071_temperature` | page 71 | APSB ECU: sw071 temperature | 48\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87.5 |  | plausible |
| `APSB_sw071_activationType` | page 71 | APSB ECU: sw071 activation type | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `APSB_sw072_vehicleX` | page 72 | APSB ECU: sw072 vehicle x | 16\|10 | little-endian | unsigned | 0.05 | -25.6 | m | -25.6 to 25.55 |  | plausible |
| `APSB_sw072_vehicleY` | page 72 | APSB ECU: sw072 vehicle y | 26\|10 | little-endian | unsigned | 0.05 | -25.6 | m | -25.6 to 25.55 |  | plausible |
| `APSB_sw072_vehicleHeading` | page 72 | APSB ECU: sw072 vehicle heading | 36\|10 | little-endian | unsigned | 0.005 | -2.56 | rad | -2.56 to 2.555 |  | plausible |
| `APSB_sw072_endDistance` | page 72 | APSB ECU: sw072 end distance | 48\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw072_guidanceComplete` | page 72 | APSB ECU: sw072 guidance complete | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_guidanceRunaway` | page 72 | APSB ECU: sw072 guidance runaway | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_guidanceTimer` | page 72 | APSB ECU: sw072 guidance timer | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_handlePress` | page 72 | APSB ECU: sw072 handle press | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_keyfobPress` | page 72 | APSB ECU: sw072 keyfob press | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_garageOpened` | page 72 | APSB ECU: sw072 garage opened | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw072_userTimeout` | page 72 | APSB ECU: sw072 user timeout | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw075_scMia` | page 75 | APSB ECU: sw075 sc mia | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw075_unusedByte` | page 75 | APSB ECU: sw075 unused byte | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw075_unusedW0` | page 75 | APSB ECU: sw075 unused W0 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw075_unusedW1` | page 75 | APSB ECU: sw075 unused W1 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw077_oocDistance` | page 77 | APSB ECU: sw077 ooc distance | 16\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 511 |  | plausible |
| `APSB_sw077_oocConfidence` | page 77 | APSB ECU: sw077 ooc confidence | 25\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `APSB_sw077_oocCollisionSide` | page 77 | APSB ECU: sw077 ooc collision side | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw077_oocHeight` | page 77 | APSB ECU: sw077 ooc height | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `APSB_sw077_vehicleSpeed` | page 77 | APSB ECU: sw077 vehicle speed | 37\|10 | little-endian | unsigned | 0.05 | -25 | MPH | -25 to 26.15 |  | plausible |
| `APSB_sw077_oocUntrackedTime` | page 77 | APSB ECU: sw077 ooc untracked time | 48\|6 | little-endian | unsigned | 0.1 | 0 | s | 0 to 6.3 |  | plausible |
| `APSB_sw077_oocOffCourseDist_cm` | page 77 | APSB ECU: sw077 ooc off course dist cm | 54\|10 | little-endian | signed | 1 | 0 |  | -512 to 511 |  | layout-only |
| `APSB_sw081_radarDistance` | page 81 | APSB ECU: sw081 radar distance | 16\|8 | little-endian | unsigned | 0.0625 | 0 | m | 0 to 15.9375 |  | plausible |
| `APSB_sw081_radarTTC` | page 81 | APSB ECU: sw081 radar TTC | 24\|8 | little-endian | unsigned | 0.02 | 0 | seconds | 0 to 5.1 |  | plausible |
| `APSB_sw081_cameraDistance` | page 81 | APSB ECU: sw081 camera distance | 32\|8 | little-endian | unsigned | 0.0625 | 0 | m | 0 to 15.9375 |  | plausible |
| `APSB_sw081_cameraTTC` | page 81 | APSB ECU: sw081 camera TTC | 40\|8 | little-endian | unsigned | 0.02 | 0 | seconds | 0 to 5.1 |  | plausible |
| `APSB_sw081_pedalPosition` | page 81 | APSB ECU: sw081 pedal position | 48\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `APSB_sw129_currentVoltage` | page 129 | APSB ECU: sw129 current voltage | 16\|14 | little-endian | unsigned | 1 | 0 | mV | 0 to 16383 |  | plausible |
| `APSB_sw129_maxThreshold` | page 129 | APSB ECU: sw129 max threshold | 30\|13 | little-endian | unsigned | 1 | 50 | mV | 50 to 8241 |  | plausible |
| `APSB_sw129_minThreshold` | page 129 | APSB ECU: sw129 min threshold | 43\|13 | little-endian | unsigned | 1 | 0 | mV | 0 to 8191 |  | plausible |
| `APSB_sw129_powerSequnceError` | page 129 | APSB ECU: sw129 power sequnce error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw129_railControl` | page 129 | APSB ECU: sw129 rail control | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw129_railID` | page 129 | APSB ECU: sw129 rail ID | 58\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `5V0_MAIN1`<br>1 = `5V0_MAIN2`<br>2 = `5V0_MAIN3`<br>3 = `5V0_MAIN4`<br>4 = `5V0_ARX`<br>5 = `1V8_ARX`<br>6 = `1V3_ARX`<br>7 = `1V5_ETH`<br>8 = `1V1_ETH`<br>9 = `VDD_FAN`<br>10 = `PARK_SYS_RST_ARX_MON`<br>11 = `PARK_THERM_ALERT_MON`<br>12 = `GPS_ANT_DET`<br>13 = `SENSOR0_TEMP`<br>14 = `SENSOR1_TEMP`<br>15 = `SENSOR2_TEMP`<br>16 = `SENSOR3_TEMP`<br>17 = `C_RAIL` | plausible |
| `APSB_sw130_currentTemperature` | page 130 | APSB ECU: sw130 current temperature | 16\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw130_maxThreshold` | page 130 | APSB ECU: sw130 max threshold | 24\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw130_minThreshold` | page 130 | APSB ECU: sw130 min threshold | 32\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 |  | plausible |
| `APSB_sw130_tempSensorId` | page 130 | APSB ECU: sw130 temp sensor id | 40\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `APSB_sw130_shouldForceApPowerOn` | page 130 | APSB ECU: sw130 should force ap power on | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw130_shouldBlockOkToPowerAp` | page 130 | APSB ECU: sw130 should block ok to power ap | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw132_mismatchType` | page 132 | APSB ECU: sw132 mismatch type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `APS_APP_FW_REPO_GITHASH`<br>1 = `GTW_APP_FW_REPO_GITHASH` | plausible |
| `APSB_sw132_actualHash` | page 132 | APSB ECU: sw132 actual hash | 24\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `APSB_sw132_expectedHash` | page 132 | APSB ECU: sw132 expected hash | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw133_failedInitStep` | page 133 | APSB ECU: sw133 failed init step | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw133_switchInReset` | page 133 | APSB ECU: sw133 switch in reset | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_phyIsNotRMIIMode` | page 133 | APSB ECU: sw133 phy is not RMII mode | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_phyInterruptStorm` | page 133 | APSB ECU: sw133 phy interrupt storm | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_switchEthernetInterLinkDown` | page 133 | APSB ECU: sw133 switch ethernet inter link down | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchReadFwVerFailed` | page 133 | APSB ECU: sw133 eth switch read fw ver failed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchFailedToBoot` | page 133 | APSB ECU: sw133 eth switch failed to boot | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchTimedoutUpdate` | page 133 | APSB ECU: sw133 eth switch timedout update | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchMcuLinkFailover` | page 133 | APSB ECU: sw133 eth switch mcu link failover | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchMcuLinkDuplicated` | page 133 | APSB ECU: sw133 eth switch mcu link duplicated | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_ethSwitchMcuLinkDisconnected` | page 133 | APSB ECU: sw133 eth switch mcu link disconnected | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw133_unused` | page 133 | APSB ECU: sw133 unused | 34\|30 | little-endian | unsigned | 1 | 0 |  | 0 to 1073741823 |  | layout-only |
| `APSB_sw134_appCamCalibStatus` | page 134 | APSB ECU: sw134 app cam calib status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_appCameraLux` | page 134 | APSB ECU: sw134 app camera lux | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_appInfo` | page 134 | APSB ECU: sw134 app info | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_appStatus` | page 134 | APSB ECU: sw134 app status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasAutonomyControlParty` | page 134 | APSB ECU: sw134 das autonomy control party | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasAutonomyControlVeh` | page 134 | APSB ECU: sw134 das autonomy control veh | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasBodyControlsVEH` | page 134 | APSB ECU: sw134 das body controls VEH | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasControl` | page 134 | APSB ECU: sw134 das control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasControlPty` | page 134 | APSB ECU: sw134 das control pty | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasIntSafetyFrontPty` | page 134 | APSB ECU: sw134 das int safety front pty | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasLanes` | page 134 | APSB ECU: sw134 das lanes | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasObject` | page 134 | APSB ECU: sw134 das object | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasPscControl` | page 134 | APSB ECU: sw134 das psc control | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasStatus` | page 134 | APSB ECU: sw134 das status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasStatus2` | page 134 | APSB ECU: sw134 das status2 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasSteeringControl` | page 134 | APSB ECU: sw134 das steering control | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasVisualDebug` | page 134 | APSB ECU: sw134 das visual debug | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasSteeringControlPty` | page 134 | APSB ECU: sw134 das steering control pty | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasChNm` | page 134 | APSB ECU: sw134 das ch nm | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_appSummon` | page 134 | APSB ECU: sw134 app summon | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_appEnvironment` | page 134 | APSB ECU: sw134 app environment | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasStatusPty` | page 134 | APSB ECU: sw134 das status pty | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasStatus2Pty` | page 134 | APSB ECU: sw134 das status2 pty | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasMatrixHighBeamRqVEH` | page 134 | APSB ECU: sw134 das matrix high beam rq VEH | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasMatrixBendAngleRqPty` | page 134 | APSB ECU: sw134 das matrix bend angle rq pty | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasBodyControls2VEH` | page 134 | APSB ECU: sw134 das body controls2 VEH | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasRedundantBrakingControl` | page 134 | APSB ECU: sw134 das redundant braking control | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_dasRedundantBrakingControlPty` | page 134 | APSB ECU: sw134 das redundant braking control pty | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw134_timeSinceLastMsg` | page 134 | APSB ECU: sw134 time since last msg | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw135_appCriticalReason` | page 135 | APSB ECU: sw135 app critical reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `BOOT_TIMEOUT`<br>2 = `GPIO_CRITICAL`<br>3 = `VERSION_MISMATCH`<br>4 = `MIA`<br>5 = `WATCHDOG_CRITICAL`<br>6 = `OTHER_TURBO_VERSION_MISMATCH`<br>7 = `TIMESYNC_ERROR`<br>8 = `OTHER_TURBO_TIMESYNC_ERROR` | plausible |
| `APSB_sw135_appTimesyncStatus` | page 135 | APSB ECU: sw135 app timesync status | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `APSB_sw136_gpsCommIrrecoverable` | page 136 | APSB ECU: sw136 gps comm irrecoverable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw136_fusionIrrecoverable` | page 136 | APSB ECU: sw136 fusion irrecoverable | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw136_antennaUnplugged` | page 136 | APSB ECU: sw136 antenna unplugged | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw136_badgpsfix` | page 136 | APSB ECU: sw136 badgpsfix | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsCommMissing` | page 137 | APSB ECU: sw137 gps comm missing | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsJunkData` | page 137 | APSB ECU: sw137 gps junk data | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsNMEAmissing` | page 137 | APSB ECU: sw137 gps NME amissing | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsUBXmissing` | page 137 | APSB ECU: sw137 gps UB xmissing | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_fusionModeDisabled` | page 137 | APSB ECU: sw137 fusion mode disabled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsCfgFail` | page 137 | APSB ECU: sw137 gps cfg fail | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_esfStatusMsgMIA` | page 137 | APSB ECU: sw137 esf status msg MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_wheelTickCfgMissmatch` | page 137 | APSB ECU: sw137 wheel tick cfg missmatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_exitTransportMode` | page 137 | APSB ECU: sw137 exit transport mode | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_satRejectionTimeout` | page 137 | APSB ECU: sw137 sat rejection timeout | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw137_gpsPPSMissing` | page 137 | APSB ECU: sw137 gps PPS missing | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_cfgBufNull` | page 138 | APSB ECU: sw138 cfg buf null | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_invalidID` | page 138 | APSB ECU: sw138 invalid ID | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_gpsBufferOverflow` | page 138 | APSB ECU: sw138 gps buffer overflow | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_navx5CfgFailed` | page 138 | APSB ECU: sw138 navx5 cfg failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_mcuNMEAmsgUDPinvalid` | page 138 | APSB ECU: sw138 mcu NME amsg UD pinvalid | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_mcuDbgMsgInvalid` | page 138 | APSB ECU: sw138 mcu dbg msg invalid | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_mcuDbgMsgTooBig` | page 138 | APSB ECU: sw138 mcu dbg msg too big | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_mcuFwdNMEAfail` | page 138 | APSB ECU: sw138 mcu fwd NME afail | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_NMEAinvalidChecksum` | page 138 | APSB ECU: sw138 NME ainvalid checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_unexpectedNMEAmsg` | page 138 | APSB ECU: sw138 unexpected NME amsg | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTbusFull` | page 138 | APSB ECU: sw138 UAR tbus full | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTframeError` | page 138 | APSB ECU: sw138 UAR tframe error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UBXrxFrameTooBig` | page 138 | APSB ECU: sw138 UB xrx frame too big | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_emptyValidNMEA` | page 138 | APSB ECU: sw138 empty valid NMEA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_invalidAsciiNMEA` | page 138 | APSB ECU: sw138 invalid ascii NMEA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_wheeltickUARTfault` | page 138 | APSB ECU: sw138 wheeltick UAR tfault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_baudrateMismatch` | page 138 | APSB ECU: sw138 baudrate mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_wheelTickInvalidSrc` | page 138 | APSB ECU: sw138 wheel tick invalid src | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTparityError` | page 138 | APSB ECU: sw138 UAR tparity error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTrxFifoOverflow` | page 138 | APSB ECU: sw138 UAR trx fifo overflow | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTrxFifoUnderflow` | page 138 | APSB ECU: sw138 UAR trx fifo underflow | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_UARTtxFifoOverflow` | page 138 | APSB ECU: sw138 UAR ttx fifo overflow | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_esfWtMsgTimeout` | page 138 | APSB ECU: sw138 esf wt msg timeout | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_PFLASHReadError` | page 138 | APSB ECU: sw138 PFLASH read error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_PFLASHWriteError` | page 138 | APSB ECU: sw138 PFLASH write error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_gpsCfgNack` | page 138 | APSB ECU: sw138 gps cfg nack | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_gpsCfgIdFail` | page 138 | APSB ECU: sw138 gps cfg id fail | 42\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `APSB_sw138_gpsSetCfgNoAck` | page 138 | APSB ECU: sw138 gps set cfg no ack | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_gpsReadCfgNoResponse` | page 138 | APSB ECU: sw138 gps read cfg no response | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw138_ubxErrorReported` | page 138 | APSB ECU: sw138 ubx error reported | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_lvPowerState` | page 140 | APSB ECU: sw140 lv power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_vehicleStatus` | page 140 | APSB ECU: sw140 vehicle status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_status` | page 140 | APSB ECU: sw140 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_lighting` | page 140 | APSB ECU: sw140 lighting | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_sensors` | page 140 | APSB ECU: sw140 sensors | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_coolant` | page 140 | APSB ECU: sw140 coolant | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw140_okToUseHighPower` | page 140 | APSB ECU: sw140 ok to use high power | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw141_inertial1` | page 141 | APSB ECU: sw141 inertial1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw141_inertial2` | page 141 | APSB ECU: sw141 inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_speed` | page 142 | APSB ECU: sw142 speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_locStatus` | page 142 | APSB ECU: sw142 loc status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_locStatus2` | page 142 | APSB ECU: sw142 loc status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_systemStatus` | page 142 | APSB ECU: sw142 system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_chassisControl` | page 142 | APSB ECU: sw142 chassis control | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_epbStatus` | page 142 | APSB ECU: sw142 epb status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw142_brakeSystem` | page 142 | APSB ECU: sw142 brake system | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw143_status` | page 143 | APSB ECU: sw143 status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw143_wheelRotation` | page 143 | APSB ECU: sw143 wheel rotation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw143_wheelSpeeds` | page 143 | APSB ECU: sw143 wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw143_redundantBrakingStatus` | page 143 | APSB ECU: sw143 redundant braking status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw144_restraintStatus` | page 144 | APSB ECU: sw144 restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw145_restraintStatus` | page 145 | APSB ECU: sw145 restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw146_sysStatus` | page 146 | APSB ECU: sw146 sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw146_status` | page 146 | APSB ECU: sw146 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw147_doorStatus` | page 147 | APSB ECU: sw147 door status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw147_switchStatus` | page 147 | APSB ECU: sw147 switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw148_doorStatus` | page 148 | APSB ECU: sw148 door status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw148_hvacStatus` | page 148 | APSB ECU: sw148 hvac status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw149_status` | page 149 | APSB ECU: sw149 status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw150_steeringAngleSensor` | page 150 | APSB ECU: sw150 steering angle sensor | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw150_rightStalk` | page 150 | APSB ECU: sw150 right stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw150_leftStalk` | page 150 | APSB ECU: sw150 left stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw153_eacInhibitReason` | page 153 | APSB ECU: sw153 eac inhibit reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `EPAS`<br>2 = `DURATION`<br>3 = `HYSTERESIS`<br>4 = `EPAS_MIA`<br>5 = `DAS_MIA`<br>6 = `DI_MIA`<br>7 = `LSS_DURATION`<br>8 = `PEPS_MIA`<br>9 = `RSA_MIA` | plausible |
| `APSB_sw153_eacInternalState` | page 153 | APSB ECU: sw153 eac internal state | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATE_INIT`<br>1 = `STATE_MOMENTARY`<br>2 = `STATE_CONTINUOUS`<br>3 = `STATE_AUTOPARK`<br>4 = `STATE_INHIBIT`<br>5 = `STATE_OVERRIDE`<br>6 = `STATE_LSS`<br>7 = `NUM_STATES` | plausible |
| `APSB_sw155_InUnicastError` | page 155 | APSB ECU: sw155 in unicast error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPRecvError` | page 155 | APSB ECU: sw155 UDP recv error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPMiscError` | page 155 | APSB ECU: sw155 UDP misc error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPRTEError` | page 155 | APSB ECU: sw155 UDPRTE error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPCheckError` | page 155 | APSB ECU: sw155 UDP check error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPDropError` | page 155 | APSB ECU: sw155 UDP drop error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPMemError` | page 155 | APSB ECU: sw155 UDP mem error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_UDPProtoError` | page 155 | APSB ECU: sw155 UDP proto error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPRecvError` | page 155 | APSB ECU: sw155 IP recv error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPMiscError` | page 155 | APSB ECU: sw155 IP misc error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPRTEError` | page 155 | APSB ECU: sw155 IPRTE error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPCheckError` | page 155 | APSB ECU: sw155 IP check error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPMemError` | page 155 | APSB ECU: sw155 IP mem error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPDropError` | page 155 | APSB ECU: sw155 IP drop error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw155_IPProtoError` | page 155 | APSB ECU: sw155 IP proto error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_apbInfo` | page 158 | APSB ECU: sw158 apb info | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_apbStatus` | page 158 | APSB ECU: sw158 apb status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasAutonomyControlParty` | page 158 | APSB ECU: sw158 das autonomy control party | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasAutonomyControlVeh` | page 158 | APSB ECU: sw158 das autonomy control veh | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasBodyControlsVEH` | page 158 | APSB ECU: sw158 das body controls VEH | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasControl` | page 158 | APSB ECU: sw158 das control | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasControlPty` | page 158 | APSB ECU: sw158 das control pty | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasIntSafetyFrontPty` | page 158 | APSB ECU: sw158 das int safety front pty | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasLanes` | page 158 | APSB ECU: sw158 das lanes | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasObject` | page 158 | APSB ECU: sw158 das object | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasPscControl` | page 158 | APSB ECU: sw158 das psc control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasStatus` | page 158 | APSB ECU: sw158 das status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasStatus2` | page 158 | APSB ECU: sw158 das status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasSteeringControl` | page 158 | APSB ECU: sw158 das steering control | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasVisualDebug` | page 158 | APSB ECU: sw158 das visual debug | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasSteeringControlPty` | page 158 | APSB ECU: sw158 das steering control pty | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasChNm` | page 158 | APSB ECU: sw158 das ch nm | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasStatusPty` | page 158 | APSB ECU: sw158 das status pty | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasStatus2Pty` | page 158 | APSB ECU: sw158 das status2 pty | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasMatrixHighBeamRqVEH` | page 158 | APSB ECU: sw158 das matrix high beam rq VEH | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasMatrixBendAngleRqPty` | page 158 | APSB ECU: sw158 das matrix bend angle rq pty | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasBodyControls2VEH` | page 158 | APSB ECU: sw158 das body controls2 VEH | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasRedundantBrakingControl` | page 158 | APSB ECU: sw158 das redundant braking control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_dasRedundantBrakingControlPty` | page 158 | APSB ECU: sw158 das redundant braking control pty | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw158_timeSinceLastMsg` | page 158 | APSB ECU: sw158 time since last msg | 40\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `APSB_sw159_apbCriticalReason` | page 159 | APSB ECU: sw159 apb critical reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `BOOT_TIMEOUT`<br>2 = `GPIO_CRITICAL`<br>3 = `VERSION_MISMATCH`<br>4 = `MIA`<br>5 = `WATCHDOG_CRITICAL`<br>6 = `OTHER_TURBO_VERSION_MISMATCH`<br>7 = `TIMESYNC_ERROR`<br>8 = `OTHER_TURBO_TIMESYNC_ERROR` | plausible |
| `APSB_sw159_apbTimesyncStatus` | page 159 | APSB ECU: sw159 apb timesync status | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `APSB_sw160_mismatchType` | page 160 | APSB ECU: sw160 mismatch type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `APS_APP_FW_REPO_GITHASH`<br>1 = `GTW_APP_FW_REPO_GITHASH` | plausible |
| `APSB_sw160_actualHash` | page 160 | APSB ECU: sw160 actual hash | 24\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `APSB_sw160_expectedHash` | page 160 | APSB ECU: sw160 expected hash | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw161_antennaDisconnected` | page 161 | APSB ECU: sw161 antenna disconnected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw172_prolongedUiMia` | page 172 | APSB ECU: sw172 prolonged ui mia | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw172_uiMiaAtBootup` | page 172 | APSB ECU: sw172 ui mia at bootup | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_otherTurbo` | page 188 | APSB ECU: sw188 other turbo | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `A`<br>1 = `B`<br>2 = `UNKNOWN` | plausible |
| `APSB_sw188_arbUartMiaState` | page 188 | APSB ECU: sw188 arb uart mia state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_powerUartMiaState` | page 188 | APSB ECU: sw188 power uart mia state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_faultsUartMiaState` | page 188 | APSB ECU: sw188 faults uart mia state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_sleepUartMiaState` | page 188 | APSB ECU: sw188 sleep uart mia state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_resetUartMiaState` | page 188 | APSB ECU: sw188 reset uart mia state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_statMonUartMiaState` | page 188 | APSB ECU: sw188 stat mon uart mia state | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_wdogStateUartMiaState` | page 188 | APSB ECU: sw188 wdog state uart mia state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw188_critReasUartMiaState` | page 188 | APSB ECU: sw188 crit reas uart mia state | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw189_AP_vehicleState10Hz` | page 189 | APSB ECU: sw189 AP vehicle state10 hz | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw189_AP_vehicleState1Hz` | page 189 | APSB ECU: sw189 AP vehicle state1 hz | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw190_IBST_status` | page 190 | APSB ECU: sw190 IBST status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_CANbus` | page 192 | APSB ECU: sw192 CA nbus | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PARTY`<br>1 = `CH`<br>2 = `RAD0`<br>3 = `VEH`<br>4 = `UNKNOWN` | plausible |
| `APSB_sw192_SWTxQueueFull` | page 192 | APSB ECU: sw192 SW tx queue full | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_Busoff` | page 192 | APSB ECU: sw192 busoff | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_UncorrectedBitError` | page 192 | APSB ECU: sw192 uncorrected bit error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_CorrectedBitError` | page 192 | APSB ECU: sw192 corrected bit error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_ErrorPassive` | page 192 | APSB ECU: sw192 error passive | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_RamAccessFailed` | page 192 | APSB ECU: sw192 ram access failed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_RxMsgLost` | page 192 | APSB ECU: sw192 rx msg lost | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw192_msgIo` | page 192 | APSB ECU: sw192 msg io | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_MESSAGE`<br>1 = `RX`<br>2 = `TX` | plausible |
| `APSB_sw192_queueFailure` | page 192 | APSB ECU: sw192 queue failure | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_FAILURE`<br>1 = `SW`<br>2 = `HW` | plausible |
| `APSB_sw192_msgId` | page 192 | APSB ECU: sw192 msg id | 32\|11 | little-endian | unsigned | 1 | 0 |  | 0 to 2047 |  | layout-only |
| `APSB_sw199_abortCodeDas` | page 199 | APSB ECU: sw199 abort code das | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `NONE`<br>1 = `LOST_ANGLE_CONTROL`<br>2 = `PARK_GUIDANCE_ENDED`<br>3 = `MCU_REQUEST_MISMATCH`<br>4 = `INVALID_SPACE`<br>5 = `PREGUIDANCE_TIMEOUT`<br>6 = `PARK_MIA`<br>7 = `EPAS_MIA`<br>8 = `DI_MIA`<br>9 = `MCU_MIA`<br>10 = `SCCM_MIA`<br>11 = `ESP_MIA`<br>12 = `PAUSE_OBSTACLE_TIMEOUT`<br>13 = `PAUSE_USER_TIMEOUT`<br>14 = `RESTART_TIMEOUT`<br>15 = `PARK_GEAR`<br>16 = `LOST_DI_CONTROL`<br>17 = `UI_REQUEST`<br>18 = `PRECRUISE_TIMEOUT`<br>19 = `SENSOR_FAILURE`<br>20 = `SC_MIA`<br>21 = `USER_KEYFOB`<br>22 = `EPAS_INHIBITED`<br>23 = `PAUSE_CYCLES`<br>24 = `APP_MIA`<br>25 = `HEARTBEAT_MISSING`<br>26 = `PARKER_HEARTBEAT_MISSING`<br>27 = `TRAILER_MODE`<br>28 = `TOO_MANY_GEAR_CHANGES`<br>29 = `DRIVABLE_SPACE_STALE`<br>30 = `UNAUTHORIZED_REQUEST`<br>31 = `DRIVER_NOT_DETECTED`<br>32 = `EXTERIOR_LIGHTS_OFF`<br>33 = `BACKUP_CAMERA_BLINDED`<br>34 = `REPEATER_CAMERA_BLINDED`<br>35 = `FORWARD_CAMERAS_BLINDED`<br>36 = `REQUIRED_CAMERA_NOT_READY`<br>37 = `EXTENDED_COMPUTE_NOT_ACTIVE`<br>38 = `UI_DISPLAY_NOT_OK`<br>39 = `GRADE_TOO_HIGH`<br>40 = `CONTROL_INTEGRATOR`<br>41 = `GEAR_SHIFT_TIMEOUT`<br>42 = `SEATBELT_UNBUCKLED`<br>43 = `SPEED_TOO_HIGH`<br>44 = `PLANNER_HEALTH`<br>45 = `CONTROLLER_HEALTH`<br>46 = `COLLISION_RISK`<br>47 = `CLOSURE_OPEN` | plausible |
| `APSB_sw199_abortCodePARK` | page 199 | APSB ECU: sw199 abort code PARK; raw 31 = signal not available (SNA) | 22\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 30 | 0 = `NONE`<br>1 = `VELOCITY_TOO_HIGH`<br>2 = `MAX_NUM_OF_MOVES`<br>3 = `NO_VALID_PATH`<br>4 = `UNCONTROLLED_TRAVEL_DIST_REACHED`<br>5 = `OFF_TRACK`<br>6 = `MAX_SWA_DEV_EXCEEDED`<br>7 = `MAX_YAW_ANGLE_REACHED`<br>8 = `OBSTACLE_ON_PATH`<br>9 = `PARK_SPACE_TOO_SMALL`<br>10 = `FULL_WARNING_ON_BOTH_SIDES`<br>11 = `HANDS_ON_DETECTED`<br>12 = `VEHICLE_DYNAMICS_INTERVENTION`<br>13 = `EPAS_FAULT`<br>14 = `DAS_ABORT`<br>15 = `ECU_INTERNAL_FAULT`<br>16 = `SYSTEM_FAULT`<br>17 = `SYSTEM_SERVICE`<br>18 = `ERROR`<br>19 = `PSC_ASYNC_CTRL_SYSTEM`<br>20 = `PSC_HIGH_TORQUE`<br>21 = `PSC_VCTL_GENERAL_ABORT`<br>22 = `PSC_PARK_PONR_NOT_REACHED`<br>23 = `PSC_PARK_STC_FAILED`<br>24 = `PSC_MAX_WAY_BEHIND_HINT`<br>25 = `PSC_MOVEMENT_AT_ACTIVATION`<br>31 = `SNA` | plausible |
| `APSB_sw199_currentSTW` | page 199 | APSB ECU: sw199 current STW | 27\|14 | little-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `APSB_sw199_currentSpeed` | page 199 | APSB ECU: sw199 current speed | 41\|8 | little-endian | unsigned | 0.1 | -12.2 | mph | -12.2 to 13.3 |  | plausible |
| `APSB_sw199_internalState` | page 199 | APSB ECU: sw199 internal state | 49\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw199_maxSpeed` | page 199 | APSB ECU: sw199 max speed | 53\|7 | little-endian | unsigned | 0.2 | -12.2 | mph | -12.2 to 13.2 |  | plausible |
| `APSB_sw199_numShifts` | page 199 | APSB ECU: sw199 num shifts | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APSB_sw203_controlType` | page 203 | APSB ECU: sw203 control type; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `NONE`<br>1 = `PARK_LEFT_PARALLEL`<br>2 = `PARK_LEFT_CROSS`<br>3 = `PARK_RIGHT_PARALLEL`<br>4 = `PARK_RIGHT_CROSS`<br>5 = `PARALLEL_PULL_OUT_TO_LEFT`<br>6 = `PARALLEL_PULL_OUT_TO_RIGHT`<br>7 = `ABORT`<br>8 = `COMPLETE`<br>9 = `SEARCH`<br>10 = `PAUSE`<br>14 = `SUMMON`<br>15 = `SNA` | plausible |
| `APSB_sw203_curbType` | page 203 | APSB ECU: sw203 curb type | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `APSB_sw203_roadClass` | page 203 | APSB ECU: sw203 road class | 22\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw203_slotSizeX` | page 203 | APSB ECU: sw203 slot size x | 25\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1020 |  | plausible |
| `APSB_sw203_slotSizeY` | page 203 | APSB ECU: sw203 slot size y | 33\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1020 |  | plausible |
| `APSB_sw203_startDistance` | page 203 | APSB ECU: sw203 start distance | 41\|11 | little-endian | unsigned | 1 | 0 | cm | 0 to 2047 |  | plausible |
| `APSB_sw203_vehicleSkew` | page 203 | APSB ECU: sw203 vehicle skew | 52\|12 | little-endian | unsigned | 0.002 | 0 | radians | 0 to 8.19 |  | plausible |
| `APSB_sw204_frLeft` | page 204 | APSB ECU: sw204 fr left | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw204_frLeftMiddle` | page 204 | APSB ECU: sw204 fr left middle | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw204_frMiddle` | page 204 | APSB ECU: sw204 fr middle | 32\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw204_frRight` | page 204 | APSB ECU: sw204 fr right | 40\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw204_frRightMiddle` | page 204 | APSB ECU: sw204 fr right middle | 48\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw204_maxSpeed` | page 204 | APSB ECU: sw204 max speed | 56\|8 | little-endian | unsigned | 0.1 | -12.2 | mph | -12.2 to 13.3 |  | plausible |
| `APSB_sw205_oocDistance` | page 205 | APSB ECU: sw205 ooc distance | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw205_rrLeft` | page 205 | APSB ECU: sw205 rr left | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw205_rrLeftMiddle` | page 205 | APSB ECU: sw205 rr left middle | 32\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw205_rrMiddle` | page 205 | APSB ECU: sw205 rr middle | 40\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw205_rrRight` | page 205 | APSB ECU: sw205 rr right | 48\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw205_rrRightMiddle` | page 205 | APSB ECU: sw205 rr right middle | 56\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 255 |  | plausible |
| `APSB_sw235_resetOrigin` | page 235 | APSB ECU: sw235 reset origin | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_RESET`<br>1 = `HARDWARE`<br>2 = `SOFTWARE` | plausible |
| `APSB_sw235_generalUnrecoverable` | page 235 | APSB ECU: sw235 general unrecoverable | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_pgoodUnrecoverable` | page 235 | APSB ECU: sw235 pgood unrecoverable | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_faultUnrecoverable` | page 235 | APSB ECU: sw235 fault unrecoverable | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_12VFuseUnrecoverable` | page 235 | APSB ECU: sw235 12 v fuse unrecoverable | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_pgoodLevelUnrcvrble` | page 235 | APSB ECU: sw235 pgood level unrcvrble | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_faultLevelUnrcvrble` | page 235 | APSB ECU: sw235 fault level unrcvrble | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_12VFuseLvlUnrcvrble` | page 235 | APSB ECU: sw235 12 v fuse lvl unrcvrble | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_localSoftwareFault` | page 235 | APSB ECU: sw235 local software fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_unrecoverableFailReset` | page 235 | APSB ECU: sw235 unrecoverable fail reset | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_generalGic` | page 235 | APSB ECU: sw235 general gic | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_a72WdtTimeout` | page 235 | APSB ECU: sw235 a72 wdt timeout | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_generalScs` | page 235 | APSB ECU: sw235 general scs | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_generalUnexpected` | page 235 | APSB ECU: sw235 general unexpected | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_canUncorrectedBitError` | page 235 | APSB ECU: sw235 can uncorrected bit error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_canExitBusoffFailed` | page 235 | APSB ECU: sw235 can exit busoff failed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_txEnFdbckNotExpected` | page 235 | APSB ECU: sw235 tx en fdbck not expected | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_nocSmsFailed` | page 235 | APSB ECU: sw235 noc sms failed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_nocCamFailed` | page 235 | APSB ECU: sw235 noc cam failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_nocCoreFailed` | page 235 | APSB ECU: sw235 noc core failed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_nocScsFailed` | page 235 | APSB ECU: sw235 noc scs failed | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_model3UiReset` | page 235 | APSB ECU: sw235 model3 ui reset | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_modelsUiReset` | page 235 | APSB ECU: sw235 models ui reset | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_pmicApOnPrpUnrcvrble` | page 235 | APSB ECU: sw235 pmic ap on prp unrcvrble | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_apOnReadyTimeout` | page 235 | APSB ECU: sw235 ap on ready timeout | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_pmicApOnWaitUnrcvrble` | page 235 | APSB ECU: sw235 pmic ap on wait unrcvrble | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_apBootingTimeout` | page 235 | APSB ECU: sw235 ap booting timeout | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_pmicApOffWaitUnrcvrble` | page 235 | APSB ECU: sw235 pmic ap off wait unrcvrble | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_resetBeingSent` | page 235 | APSB ECU: sw235 reset being sent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_udsResetBeingSent` | page 235 | APSB ECU: sw235 uds reset being sent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_smsWdtTimeout` | page 235 | APSB ECU: sw235 sms wdt timeout | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_smsCanApHealthTimeout` | page 235 | APSB ECU: sw235 sms can ap health timeout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw235_smsTaskWdtTimeout` | page 235 | APSB ECU: sw235 sms task wdt timeout | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw237_faultSource` | page 237 | APSB ECU: sw237 fault source | 16\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `SGK_WDT0`<br>1 = `SGK_WDT1`<br>2 = `SGK_DD_FAST`<br>3 = `SGK_DD_SLOW`<br>4 = `SGK_HPM`<br>5 = `SGK_GBE`<br>6 = `SGK_ADT`<br>7 = `SGK_SSS_LOCKUP`<br>8 = `SGK_SSS_UNCORRECT`<br>9 = `SGK_SSS_PKE_UNC`<br>10 = `SGK_SSS_FAULT`<br>11 = `CR5_TOP_SGK_TCM_ECC_PFU`<br>12 = `CR5_TOP_SGK_TCM_ECC_LSU`<br>13 = `CR5_TOP_SGK_DCACHE_ECC_FATAL`<br>14 = `CR5_TOP_SGK_DCACHE_TAG_ECC_FATAL`<br>15 = `CR5_TOP_SGK_TCM_ECC_AXI_SLV_FATAL`<br>16 = `CR5_TOP_SGK_ALL_FATAL_EVTS`<br>17 = `CR5_TOP_SGK_ALL_FATAL_BUS_FTLS`<br>18 = `CR5_TOP_SGK_LOCKSTEP_FAIL`<br>19 = `NOC_SGK_INT0`<br>20 = `NOC_SGK_INT1`<br>21 = `NOC_SGK_INT2`<br>22 = `NOC_SGK_INT3`<br>23 = `NOC_SGK_INT8`<br>24 = `NOC_SGK_INT9`<br>25 = `NOC_SGK_INT10`<br>26 = `NOC_SGK_INT12`<br>27 = `NOC_SGK_INT13`<br>28 = `NOC_SGK_INT14`<br>29 = `NOC_SGK_INT15`<br>30 = `NOC_SGK_PD0_mainMissionInt`<br>31 = `NOC_SGK_PD1_mainMissionInt`<br>32 = `PUF_SGK_INT0`<br>33 = `IntMEM_SGK_ECC_INTR0`<br>34 = `TMU_SGK_THERM_TRIP`<br>35 = `TCU_AON_fmu_error_int`<br>36 = `NOC_SOJU_AXI2APB_AON_T_mainTimeOut`<br>37 = `VEH_FaultManager_FAULT`<br>38 = `CORE_WDT0`<br>39 = `CORE_WDT1`<br>40 = `CORE_WDT2`<br>41 = `CORE_WDT3`<br>42 = `CORE_WDT4`<br>43 = `IMEM_HPM`<br>44 = `NOC_IMEM_AXI2APB_IMEM_T_mainTimeOut`<br>45 = `NOC_IMEM_INTMEM_IMEM_T_mainTimeOut`<br>46 = `NOC_IMEM_NS_BRDG_IMEM_D_T_mainTimeOut`<br>47 = `NOC_LSIO_AXI2APB_LSIO0_T_mainTimeOut`<br>48 = `NOC_LSIO_AXI2APB_LSIO1_T_mainTimeOut`<br>49 = `NOC_LSIO_AXI2APB_LSIO2_T_mainTimeOut`<br>50 = `NOC_LSIO_AHBBR_UFS_T_mainTimeOut`<br>51 = `NOC_LSIO_NS_BRDG_LSIO_D_T_mainTimeOut`<br>52 = `FAD_LSIO`<br>53 = `MemoryStack0_0_nw_UR_int`<br>54 = `MemoryStack1_0_nw_UR_int`<br>55 = `MemoryStack0_1_nw_UR_int`<br>56 = `MemoryStack1_1_nw_UR_int`<br>57 = `MemoryStack0_2_nw_UR_int`<br>58 = `MemoryStack1_2_nw_UR_int`<br>59 = `MemoryStack0_3_nw_UR_int`<br>60 = `MemoryStack1_3_nw_UR_int`<br>61 = `MemoryStack0_0_UR_int`<br>62 = `MemoryStack1_0_UR_int`<br>63 = `MemoryStack0_1_UR_int`<br>64 = `MemoryStack1_1_UR_int`<br>65 = `MemoryStack0_2_UR_int`<br>66 = `MemoryStack1_2_UR_int`<br>67 = `MemoryStack0_3_UR_int`<br>68 = `MemoryStack1_3_UR_int`<br>69 = `FaultManager_softfault`<br>70 = `FaultManager_fm_parity`<br>71 = `SSS_SW_RESET`<br>72 = `SSS_WDG_RESET`<br>73 = `NOC_ERRORLOG`<br>74 = `CAUSE1_RECEIVED`<br>75 = `CAUSE2_RECEIVED`<br>76 = `Veh_FAULT`<br>77 = `PEER_AP_NFAULT`<br>78 = `PEER_SGK_NFAULT`<br>79 = `PEER_TMUTHROT` | plausible |
| `APSB_sw237_peerSoCFaulted` | page 237 | APSB ECU: sw237 peer so c faulted | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_unknownVendorOnResume` | page 241 | APSB ECU: sw241 unknown vendor on resume | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_unknownVendorOnNonResume` | page 241 | APSB ECU: sw241 unknown vendor on non resume | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phyReinitFailedOnResume` | page 241 | APSB ECU: sw241 phy reinit failed on resume | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phyReinitFailedOnNonResume` | page 241 | APSB ECU: sw241 phy reinit failed on non resume | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_illTestFailed` | page 241 | APSB ECU: sw241 ill test failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_memTestFailed` | page 241 | APSB ECU: sw241 mem test failed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_dfiInitCompleteTimeout` | page 241 | APSB ECU: sw241 dfi init complete timeout | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0TimeoutWaitingForInterrupts` | page 241 | APSB ECU: sw241 phy0 timeout waiting for interrupts | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0Ch0ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy0 ch0 read gate offset bug | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0Ch1ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy0 ch1 read gate offset bug | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0RdlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy0 rdlvl reinit training timeout | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0RdlvlReinitFailed` | page 241 | APSB ECU: sw241 phy0 rdlvl reinit failed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0WdqlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy0 wdqlvl reinit training timeout | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0WdqlvlPhaseMarginOutOfRange` | page 241 | APSB ECU: sw241 phy0 wdqlvl phase margin out of range | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy0WdqlvlReinitFailed` | page 241 | APSB ECU: sw241 phy0 wdqlvl reinit failed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1TimeoutWaitingForInterrupts` | page 241 | APSB ECU: sw241 phy1 timeout waiting for interrupts | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1Ch0ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy1 ch0 read gate offset bug | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1Ch1ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy1 ch1 read gate offset bug | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1RdlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy1 rdlvl reinit training timeout | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1RdlvlReinitFailed` | page 241 | APSB ECU: sw241 phy1 rdlvl reinit failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1WdqlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy1 wdqlvl reinit training timeout | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1WdqlvlPhaseMarginOutOfRange` | page 241 | APSB ECU: sw241 phy1 wdqlvl phase margin out of range | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy1WdqlvlReinitFailed` | page 241 | APSB ECU: sw241 phy1 wdqlvl reinit failed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2TimeoutWaitingForInterrupts` | page 241 | APSB ECU: sw241 phy2 timeout waiting for interrupts | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2Ch0ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy2 ch0 read gate offset bug | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2Ch1ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy2 ch1 read gate offset bug | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2RdlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy2 rdlvl reinit training timeout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2RdlvlReinitFailed` | page 241 | APSB ECU: sw241 phy2 rdlvl reinit failed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2WdqlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy2 wdqlvl reinit training timeout | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2WdqlvlPhaseMarginOutOfRange` | page 241 | APSB ECU: sw241 phy2 wdqlvl phase margin out of range | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy2WdqlvlReinitFailed` | page 241 | APSB ECU: sw241 phy2 wdqlvl reinit failed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3TimeoutWaitingForInterrupts` | page 241 | APSB ECU: sw241 phy3 timeout waiting for interrupts | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3Ch0ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy3 ch0 read gate offset bug | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3Ch1ReadGateOffsetBug` | page 241 | APSB ECU: sw241 phy3 ch1 read gate offset bug | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3RdlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy3 rdlvl reinit training timeout | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3RdlvlReinitFailed` | page 241 | APSB ECU: sw241 phy3 rdlvl reinit failed | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3WdqlvlReinitTrainingTimeout` | page 241 | APSB ECU: sw241 phy3 wdqlvl reinit training timeout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3WdqlvlPhaseMarginOutOfRange` | page 241 | APSB ECU: sw241 phy3 wdqlvl phase margin out of range | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw241_phy3WdqlvlReinitFailed` | page 241 | APSB ECU: sw241 phy3 wdqlvl reinit failed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw242_instance` | page 242 | APSB ECU: sw242 instance | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw242_clusterSRAMMBISTFailed` | page 242 | APSB ECU: sw242 cluster SRAMMBIST failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw242_SRAMBankMBISTFailed` | page 242 | APSB ECU: sw242 SRAM bank MBIST failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw243_instance` | page 243 | APSB ECU: sw243 instance | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw243_errorStatus` | page 243 | APSB ECU: sw243 error status | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `BAD_COMMAND`<br>2 = `SRAM_PARITY_ERROR`<br>3 = `DMA_CRC_ERROR`<br>4 = `DMA_ACE_PROTOCOL_ERROR`<br>5 = `AXI_SLAVE_PROTOCOL_ERROR`<br>6 = `FP_INVALID_ERROR`<br>7 = `FP_DENORM_ERROR`<br>8 = `FP_OVERFLOW_ERROR`<br>9 = `FP_UNDERFLOW_ERROR`<br>10 = `HW_ASSERT_ERROR`<br>11 = `WATCHDOG_TIMEOUT_ERROR` | plausible |
| `APSB_sw243_extendedErrorStatus` | page 243 | APSB ECU: sw243 extended error status | 32\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `APSB_sw244_instance` | page 244 | APSB ECU: sw244 instance | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw244_exceptionCode` | page 244 | APSB ECU: sw244 exception code | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte0` | page 245 | APSB ECU: sw245 unknown MAC addr byte0 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte1` | page 245 | APSB ECU: sw245 unknown MAC addr byte1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte2` | page 245 | APSB ECU: sw245 unknown MAC addr byte2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte3` | page 245 | APSB ECU: sw245 unknown MAC addr byte3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte4` | page 245 | APSB ECU: sw245 unknown MAC addr byte4 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw245_unknownMACAddrByte5` | page 245 | APSB ECU: sw245 unknown MAC addr byte5 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort0` | page 246 | APSB ECU: sw246 ethloop switch port0 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort1` | page 246 | APSB ECU: sw246 ethloop switch port1 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort2` | page 246 | APSB ECU: sw246 ethloop switch port2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort3` | page 246 | APSB ECU: sw246 ethloop switch port3 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort4` | page 246 | APSB ECU: sw246 ethloop switch port4 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort5` | page 246 | APSB ECU: sw246 ethloop switch port5 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort6` | page 246 | APSB ECU: sw246 ethloop switch port6 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw246_ethloopSwitchPort7` | page 246 | APSB ECU: sw246 ethloop switch port7 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_crcError` | page 247 | APSB ECU: sw247 crc error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_dribbleError` | page 247 | APSB ECU: sw247 dribble error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_receiveError` | page 247 | APSB ECU: sw247 receive error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_wdogTimeout` | page 247 | APSB ECU: sw247 wdog timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_overflowError` | page 247 | APSB ECU: sw247 overflow error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_giantPacket` | page 247 | APSB ECU: sw247 giant packet | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_destAddrFilterFail` | page 247 | APSB ECU: sw247 dest addr filter fail | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw247_saAddressFilterFail` | page 247 | APSB ECU: sw247 sa address filter fail | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw248_ethloopSwitchPort2Sqi` | page 248 | APSB ECU: sw248 ethloop switch port2 sqi | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw248_ethloopSwitchPort3Sqi` | page 248 | APSB ECU: sw248 ethloop switch port3 sqi | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `APSB_sw249_ufsInitFailureReason` | page 249 | APSB ECU: sw249 ufs init failure reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ERROR`<br>1 = `LINK_STARTUP_CMD_FAILED`<br>2 = `INIT_DESCRIPTOR_FAILED`<br>3 = `NOP_CMD_FAILED`<br>4 = `POWER_MODE_CHANGE_FAILED`<br>5 = `FDEVICEINIT_FAILED`<br>6 = `TESTREADY_FAILED` | plausible |
| `APSB_sw252_ethSwitchPort2` | page 252 | APSB ECU: sw252 eth switch port2 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apWaitForShutdownTimeout` | page 253 | APSB ECU: sw253 ap wait for shutdown timeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apOffPrepareTimeout` | page 253 | APSB ECU: sw253 ap off prepare timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apSuspendedTimeout` | page 253 | APSB ECU: sw253 ap suspended timeout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_socOffReadyTimeout` | page 253 | APSB ECU: sw253 soc off ready timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apInLinuxTimeout` | page 253 | APSB ECU: sw253 ap in linux timeout | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apInCorebootTimeout` | page 253 | APSB ECU: sw253 ap in coreboot timeout | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apBootingTimeout` | page 253 | APSB ECU: sw253 ap booting timeout | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw253_apOnTimeout` | page 253 | APSB ECU: sw253 ap on timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw254_waitForBusSilenceTimeout` | page 254 | APSB ECU: sw254 wait for bus silence timeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw254_sleepReadyTimeout` | page 254 | APSB ECU: sw254 sleep ready timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw254_sleepingTimeout` | page 254 | APSB ECU: sw254 sleeping timeout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_unknownBootError` | page 255 | APSB ECU: sw255 unknown boot error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_adcWrapperInitBootError` | page 255 | APSB ECU: sw255 adc wrapper init boot error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_boardRevisionInitBootError` | page 255 | APSB ECU: sw255 board revision init boot error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_i2cInitBootError` | page 255 | APSB ECU: sw255 i2c init boot error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_provisionInitBootError` | page 255 | APSB ECU: sw255 provision init boot error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_rtcInitBootError` | page 255 | APSB ECU: sw255 rtc init boot error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_vrmInitConfigBootError` | page 255 | APSB ECU: sw255 vrm init config boot error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_powerAonIoBootError` | page 255 | APSB ECU: sw255 power aon io boot error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_bl1TocInitBootError` | page 255 | APSB ECU: sw255 bl1 toc init boot error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_tmuInitBootError` | page 255 | APSB ECU: sw255 tmu init boot error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_udpInitBootError` | page 255 | APSB ECU: sw255 udp init boot error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_gpsInitBootError` | page 255 | APSB ECU: sw255 gps init boot error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_canInitBootError` | page 255 | APSB ECU: sw255 can init boot error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_dfuCheckinSubsystemBootError` | page 255 | APSB ECU: sw255 dfu checkin subsystem boot error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_sectorProtectionBootError` | page 255 | APSB ECU: sw255 sector protection boot error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_flashOpBootError` | page 255 | APSB ECU: sw255 flash op boot error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw255_socIdInitBootError` | page 255 | APSB ECU: sw255 soc id init boot error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodTripSramStatus` | page 260 | APSB ECU: sw260 pgood trip sram status | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultSd0` | page 260 | APSB ECU: sw260 pgood pmic fault sd0 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultSd1` | page 260 | APSB ECU: sw260 pgood pmic fault sd1 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultSd2` | page 260 | APSB ECU: sw260 pgood pmic fault sd2 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultSd3` | page 260 | APSB ECU: sw260 pgood pmic fault sd3 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultSd4` | page 260 | APSB ECU: sw260 pgood pmic fault sd4 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo0` | page 260 | APSB ECU: sw260 pgood pmic fault ldo0 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo1` | page 260 | APSB ECU: sw260 pgood pmic fault ldo1 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo2` | page 260 | APSB ECU: sw260 pgood pmic fault ldo2 | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo3` | page 260 | APSB ECU: sw260 pgood pmic fault ldo3 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo4` | page 260 | APSB ECU: sw260 pgood pmic fault ldo4 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo5` | page 260 | APSB ECU: sw260 pgood pmic fault ldo5 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo6` | page 260 | APSB ECU: sw260 pgood pmic fault ldo6 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo7` | page 260 | APSB ECU: sw260 pgood pmic fault ldo7 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodPmicFaultLdo8` | page 260 | APSB ECU: sw260 pgood pmic fault ldo8 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodUfs3V3Fail` | page 260 | APSB ECU: sw260 pgood ufs3 V3 fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodTripVrmRailFail` | page 260 | APSB ECU: sw260 pgood trip vrm rail fail | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodIntVrmRailFail` | page 260 | APSB ECU: sw260 pgood int vrm rail fail | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodCpuVrmRailFail` | page 260 | APSB ECU: sw260 pgood cpu vrm rail fail | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodGpuVrmRailFail` | page 260 | APSB ECU: sw260 pgood gpu vrm rail fail | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodDdr0V75VrmRailFail` | page 260 | APSB ECU: sw260 pgood ddr0 V75 vrm rail fail | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_pgoodDdr1V25VrmRailFail` | page 260 | APSB ECU: sw260 pgood ddr1 V25 vrm rail fail | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw260_unknownSource` | page 260 | APSB ECU: sw260 unknown source | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw261_vrmPublicFaultValues` | page 261 | APSB ECU: sw261 vrm public fault values | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw261_vrmRail1FaultValues` | page 261 | APSB ECU: sw261 vrm rail1 fault values | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw261_vrmRail2FaultValues` | page 261 | APSB ECU: sw261 vrm rail2 fault values | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw261_vrmRail3FaultValues` | page 261 | APSB ECU: sw261 vrm rail3 fault values | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw261_vrmType` | page 261 | APSB ECU: sw261 vrm type | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRIP_INT_VRM`<br>1 = `CPU_GPU_VRM`<br>2 = `DDR_0V75_1V25_VRM`<br>3 = `TRIP_INT_GPU_VRM`<br>4 = `DDR_0V75_1V25_CPU_VRM` | plausible |
| `APSB_sw262_vrmPublicFaultValues` | page 262 | APSB ECU: sw262 vrm public fault values | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw262_vrmRail1FaultValues` | page 262 | APSB ECU: sw262 vrm rail1 fault values | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw262_vrmRail2FaultValues` | page 262 | APSB ECU: sw262 vrm rail2 fault values | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw262_vrmRail3FaultValues` | page 262 | APSB ECU: sw262 vrm rail3 fault values | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw262_vrmType` | page 262 | APSB ECU: sw262 vrm type | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRIP_INT_VRM`<br>1 = `CPU_GPU_VRM`<br>2 = `DDR_0V75_1V25_VRM`<br>3 = `TRIP_INT_GPU_VRM`<br>4 = `DDR_0V75_1V25_CPU_VRM` | plausible |
| `APSB_sw263_vrmPublicFaultValues` | page 263 | APSB ECU: sw263 vrm public fault values | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `APSB_sw263_vrmRail1FaultValues` | page 263 | APSB ECU: sw263 vrm rail1 fault values | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw263_vrmRail2FaultValues` | page 263 | APSB ECU: sw263 vrm rail2 fault values | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw263_vrmType` | page 263 | APSB ECU: sw263 vrm type | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TRIP_INT_VRM`<br>1 = `CPU_GPU_VRM`<br>2 = `DDR_0V75_1V25_VRM`<br>3 = `TRIP_INT_GPU_VRM`<br>4 = `DDR_0V75_1V25_CPU_VRM` | plausible |
| `APSB_sw279_corruptDirectorySource` | page 279 | APSB ECU: sw279 corrupt directory source | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VAR`<br>1 = `AUTOPILOT`<br>2 = `FACTORY`<br>3 = `MAP`<br>4 = `HOME`<br>5 = `TELEMETRY`<br>6 = `UNRECOGNIZED` | plausible |
| `APSB_sw279_errorCode` | page 279 | APSB ECU: sw279 error code | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APSB_sw280_pepsStatus` | page 280 | APSB ECU: sw280 peps status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw281_rearSteerStatus` | page 281 | APSB ECU: sw281 rear steer status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw283_psfaStatus` | page 283 | APSB ECU: sw283 psfa status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw288_status` | page 288 | APSB ECU: sw288 status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw289_turboTemperature` | page 289 | APSB ECU: sw289 turbo temperature; raw 128 = signal not available (SNA) | 16\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 | -128 = `SNA` | plausible |
| `APSB_sw289_turboProbe` | page 289 | APSB ECU: sw289 turbo probe | 24\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `APSB_sw289_peer_turboTemperature` | page 289 | APSB ECU: sw289 peer turbo temperature; raw 128 = signal not available (SNA) | 32\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 | -128 = `SNA` | plausible |
| `APSB_sw289_peer_turboProbe` | page 289 | APSB ECU: sw289 peer turbo probe | 40\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `APSB_sw315_sysStatus` | page 315 | APSB ECU: sw315 sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw315_status` | page 315 | APSB ECU: sw315 status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw317_motionControlCommand` | page 317 | APSB ECU: sw317 motion control command | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_sw317_vehicleControl2` | page 317 | APSB ECU: sw317 vehicle control2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`APSB_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (8 signals), page 19 (3 signals), page 20 (3 signals), page 21 (5 signals), page 24 (4 signals), page 27 (37 signals), page 30 (4 signals), page 33 (4 signals), page 34 (4 signals), page 35 (4 signals), page 36 (4 signals), page 39 (4 signals), page 45 (4 signals), page 48 (15 signals), page 51 (12 signals), page 52 (8 signals), page 53 (48 signals), page 55 (2 signals), page 56 (4 signals), page 58 (4 signals), page 59 (12 signals), page 61 (1 signals), page 63 (6 signals), page 64 (2 signals), page 70 (7 signals), page 71 (8 signals), page 72 (11 signals), page 75 (4 signals), page 77 (7 signals), page 81 (5 signals), page 129 (6 signals), page 130 (6 signals), page 132 (3 signals), page 133 (12 signals), page 134 (29 signals), page 135 (2 signals), page 136 (4 signals), page 137 (11 signals), page 138 (30 signals), page 140 (7 signals), page 141 (2 signals), page 142 (7 signals), page 143 (4 signals), page 144 (1 signals), page 145 (1 signals), page 146 (2 signals), page 147 (2 signals), page 148 (2 signals), page 149 (1 signals), page 150 (3 signals), page 153 (2 signals), page 155 (15 signals), page 158 (25 signals), page 159 (2 signals), page 160 (3 signals), page 161 (1 signals), page 172 (2 signals), page 188 (9 signals), page 189 (2 signals), page 190 (1 signals), page 192 (11 signals), page 199 (7 signals), page 203 (7 signals), page 204 (6 signals), page 205 (6 signals), page 235 (33 signals), page 237 (2 signals), page 241 (39 signals), page 242 (3 signals), page 243 (3 signals), page 244 (2 signals), page 245 (6 signals), page 246 (8 signals), page 247 (8 signals), page 248 (2 signals), page 249 (1 signals), page 252 (1 signals), page 253 (8 signals), page 254 (3 signals), page 255 (17 signals), page 260 (23 signals), page 261 (5 signals), page 262 (5 signals), page 263 (4 signals), page 279 (2 signals), page 280 (1 signals), page 281 (1 signals), page 283 (1 signals), page 288 (1 signals), page 289 (4 signals), page 315 (2 signals), page 317 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
