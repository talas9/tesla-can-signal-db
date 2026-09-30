---
layout: default
title: "VCSEAT2R_alertLog (0x55E) — VCSEAT2R ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCSEAT2R ECU message: alert log. Tesla Model Y CAN bus message VCSEAT2R_alertLog (0x55E) of VCSEAT2R ECU, firmware 2026.26.6.5, 520 signals (VCSEAT2R_alertID, VCSEAT2R_alertState, VCSEAT2R_a001_InternalWatchdog, VCSEAT2R_a010_UnderVoltDetected and 516 more). Bit layout, scaling, units and value tables."
---

# VCSEAT2R_alertLog (0x55E) — VCSEAT2R ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCSEAT2R ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 520 signals of VCSEAT2R_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEAT2R_alertLog` |
| CAN id | 0x55E (1374) |
| ECU | [VCSEAT2R ECU](../../vcseat2r.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEAT2R |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 520 |

## Signals of VCSEAT2R_alertLog

Tesla Model Y CAN bus signals in `VCSEAT2R_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEAT2R_alertID` | selector | VCSEAT2R ECU: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>10 = `a010_ExtSupplyVoltError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>190 = `a190_seatChoreographyIsBlockedByFrontSeat`<br>191 = `a191_seatChoreographyIsBlockedBySecondSeat`<br>200 = `a200_motorPhantomEncoder`<br>201 = `a201_motorDutyEncDisabl`<br>210 = `a210_armrestEncStall`<br>211 = `a211_armrestCurrUnder`<br>212 = `a212_armrestUncal`<br>213 = `a213_armrestEncOver`<br>214 = `a214_armrestStallDebug`<br>215 = `a215_armrestHCEncStlDbg`<br>218 = `a218_motorDriverFault`<br>219 = `a219_motorCurrentDropout`<br>224 = `a224_seatEncStallTrack`<br>225 = `a225_seatEncStallBack`<br>228 = `a228_seatEncOverTrack`<br>229 = `a229_seatEncOverBack`<br>232 = `a232_seatCurrUnderTrack`<br>233 = `a233_seatCurrUnderBack`<br>234 = `a234_seatTrackStatsFromLastStateDbg`<br>235 = `a235_seatTrackStatsFromLastStateDbg2`<br>236 = `a236_seatArmrestStatsFromLastStateDbg`<br>237 = `a237_seatArmrestStatsFromLastStateDbg2`<br>238 = `a238_seatArmrestInhibitedByBackrest`<br>239 = `a239_seatHeatIRow2`<br>240 = `a240_seatHeatShortRow2`<br>241 = `a241_seatArmrestHistoryScore`<br>242 = `a242_seatHeatTmpRow2`<br>243 = `a243_seatArmrestHistoryScoreDbg`<br>244 = `a244_seatArmrestSpeedTableReferenceStatus`<br>245 = `a245_seatArmrestEcuLogStatus`<br>251 = `a251_seatUncalTrack`<br>252 = `a252_seatUncalBack`<br>260 = `a260_seatTrackObstacleDetected`<br>261 = `a261_seatArmrestObstacleDetected`<br>263 = `a263_seatTrackStallDebug`<br>264 = `a264_seatBackStallDebug`<br>267 = `a267_seatTrackHCEncStl`<br>268 = `a268_seatBackHCEncStlDbg`<br>270 = `a270_seatUncalibrated`<br>271 = `a271_seatPositionNonsensical`<br>272 = `a272_seatAbsPosOffsetApplied`<br>273 = `a273_seatObstacleDetected`<br>274 = `a274_seatTempHigh`<br>275 = `a275_seatAbsPosSensorTransitionDbg`<br>276 = `a276_seatStatsFromLastStateDbg`<br>277 = `a277_seatRequestWhileUncalibrated`<br>278 = `a278_seatClashAvoidanceBlocked`<br>279 = `a279_seatOverfolded`<br>280 = `a280_seatStatsFromLastStateDbg2`<br>290 = `a290_occupancyFaultRow2`<br>291 = `a291_buckleFaultedRow2`<br>426 = `a426_seatAbuseMotorWarn`<br>427 = `a427_seatAbuseMotorStop`<br>428 = `a428_seatAbuseBufferWarn`<br>429 = `a429_seatAbuseBufferFull`<br>444 = `a444_drv8703Fault`<br>445 = `a445_drv8703SpiFaultDBG`<br>526 = `a526_pcbaOverTemperature`<br>550 = `a550_ambientTempDelta`<br>571 = `a571_seatHeatDisabledRear` | plausible |
| `VCSEAT2R_alertState` |  | VCSEAT2R ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCSEAT2R_a001_InternalWatchdog` | page 1 | VCSEAT2R ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a010_UnderVoltDetected` | page 10 | VCSEAT2R ECU: a010 under volt detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a010_UnderVoltTimeout` | page 10 | VCSEAT2R ECU: a010 under volt timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a015_NVMMMemOverflow` | page 15 | VCSEAT2R ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a015_NVMMFilesystemError` | page 15 | VCSEAT2R ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a015_NVMMRecordIDError` | page 15 | VCSEAT2R ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a057_VEH_cpControl` | page 57 | VCSEAT2R ECU: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a059_voltageDrop` | page 59 | VCSEAT2R ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCSEAT2R_a059_resistanceEstimate` | page 59 | VCSEAT2R ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCSEAT2R_a059_current` | page 59 | VCSEAT2R ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCSEAT2R_a063_switchChannel` | page 63 | VCSEAT2R ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a063_switchType` | page 63 | VCSEAT2R ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a063_ADCVoltage` | page 63 | VCSEAT2R ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCSEAT2R_a063_disconnected` | page 63 | VCSEAT2R ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a063_indeterminate` | page 63 | VCSEAT2R ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a063_stuckActive` | page 63 | VCSEAT2R ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a063_faulted` | page 63 | VCSEAT2R ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a082_RIPC_epbPrivateState` | page 82 | VCSEAT2R ECU: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a082_RIPC_remoteHSD` | page 82 | VCSEAT2R ECU: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a082_RIPC_railStatus` | page 82 | VCSEAT2R ECU: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a082_RIPC_remoteMux` | page 82 | VCSEAT2R ECU: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a083_LIPC_epbPrivateState` | page 83 | VCSEAT2R ECU: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a083_LIPC_remoteHSD` | page 83 | VCSEAT2R ECU: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a083_LIPC_railStatus` | page 83 | VCSEAT2R ECU: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a083_LIPC_HSDFaults` | page 83 | VCSEAT2R ECU: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a084_CH_StatusC` | page 84 | VCSEAT2R ECU: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a085_PARTY_buttonStatus` | page 85 | VCSEAT2R ECU: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_LVBMS_statusHigh` | page 86 | VCSEAT2R ECU: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_LVBMS_statusLow` | page 86 | VCSEAT2R ECU: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_status` | page 86 | VCSEAT2R ECU: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_12VBatteryStatus` | page 86 | VCSEAT2R ECU: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_LVPowerState` | page 86 | VCSEAT2R ECU: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_lightStatus` | page 86 | VCSEAT2R ECU: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_systemStatus` | page 86 | VCSEAT2R ECU: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_thermalStatus` | page 86 | VCSEAT2R ECU: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VEH_vehNm` | page 86 | VCSEAT2R ECU: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_VEH_temperature` | page 87 | VCSEAT2R ECU: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_VEH_thermalControl` | page 87 | VCSEAT2R ECU: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_VEH_torque` | page 87 | VCSEAT2R ECU: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_VEH_status` | page 87 | VCSEAT2R ECU: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_PARTY_torque` | page 87 | VCSEAT2R ECU: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_PARTY_status` | page 87 | VCSEAT2R ECU: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_PARTY_temperature` | page 87 | VCSEAT2R ECU: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_PARTY_thermalControl` | page 87 | VCSEAT2R ECU: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_VEH_motorStatus` | page 87 | VCSEAT2R ECU: a087 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_VEH_temperature` | page 88 | VCSEAT2R ECU: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_VEH_thermalControl` | page 88 | VCSEAT2R ECU: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_VEH_torque` | page 88 | VCSEAT2R ECU: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_VEH_status` | page 88 | VCSEAT2R ECU: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_PARTY_torque` | page 88 | VCSEAT2R ECU: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_PARTY_status` | page 88 | VCSEAT2R ECU: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_PARTY_temperature` | page 88 | VCSEAT2R ECU: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_PARTY_thermalControl` | page 88 | VCSEAT2R ECU: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_VEH_motorStatus` | page 88 | VCSEAT2R ECU: a088 VEH motor status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_PARTY_party1` | page 89 | VCSEAT2R ECU: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_PARTY_status` | page 89 | VCSEAT2R ECU: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_VEH_status` | page 89 | VCSEAT2R ECU: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_BDY_party1` | page 89 | VCSEAT2R ECU: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_BDY_status` | page 89 | VCSEAT2R ECU: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_CH_status` | page 89 | VCSEAT2R ECU: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_CH_party1` | page 89 | VCSEAT2R ECU: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_CH_party3` | page 89 | VCSEAT2R ECU: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_VEH_party1` | page 89 | VCSEAT2R ECU: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_VEH_party3` | page 89 | VCSEAT2R ECU: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a091_VEH_faultsAndExtras` | page 91 | VCSEAT2R ECU: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a091_VEH_info` | page 91 | VCSEAT2R ECU: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a091_VEH_state` | page 91 | VCSEAT2R ECU: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a092_VEH_restraintStatus` | page 92 | VCSEAT2R ECU: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a092_VEH_switchStatus` | page 92 | VCSEAT2R ECU: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a092_VEH_seatStatus2` | page 92 | VCSEAT2R ECU: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a092_VEH_vehNm` | page 92 | VCSEAT2R ECU: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a093_VEH_restraintStatus` | page 93 | VCSEAT2R ECU: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a093_VEH_switchStatus` | page 93 | VCSEAT2R ECU: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a093_VEH_seatStatus2` | page 93 | VCSEAT2R ECU: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a093_VEH_vehNm` | page 93 | VCSEAT2R ECU: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a094_VEH_sysStatus` | page 94 | VCSEAT2R ECU: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a094_PARTY_sysStatus` | page 94 | VCSEAT2R ECU: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a094_CH_sysStatus` | page 94 | VCSEAT2R ECU: a094 CH sys status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a095_PT_ptNm` | page 95 | VCSEAT2R ECU: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a095_PT_status` | page 95 | VCSEAT2R ECU: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a096_VEH_status` | page 96 | VCSEAT2R ECU: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a096_CH_status` | page 96 | VCSEAT2R ECU: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a097_VEH_HVStatus` | page 97 | VCSEAT2R ECU: a097 VEH HV status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a097_VEH_state` | page 97 | VCSEAT2R ECU: a097 VEH state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_CH_torque` | page 98 | VCSEAT2R ECU: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_hvStatus` | page 98 | VCSEAT2R ECU: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_status` | page 98 | VCSEAT2R ECU: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_thermalControl` | page 98 | VCSEAT2R ECU: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_temperature` | page 98 | VCSEAT2R ECU: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_torque` | page 98 | VCSEAT2R ECU: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PARTY_status` | page 98 | VCSEAT2R ECU: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PARTY_temperature` | page 98 | VCSEAT2R ECU: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PARTY_thermalControl` | page 98 | VCSEAT2R ECU: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PARTY_torque` | page 98 | VCSEAT2R ECU: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PT_thermalControl` | page 98 | VCSEAT2R ECU: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PT_temperature` | page 98 | VCSEAT2R ECU: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_PARTY_motorStatus` | page 98 | VCSEAT2R ECU: a098 PARTY motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_VEH_motorStatus` | page 98 | VCSEAT2R ECU: a098 VEH motor status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a099_VEH_oocStatus` | page 99 | VCSEAT2R ECU: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_VEH` | page 100 | VCSEAT2R ECU: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_PARTY` | page 100 | VCSEAT2R ECU: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_PT` | page 100 | VCSEAT2R ECU: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_CH` | page 100 | VCSEAT2R ECU: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_OBD` | page 100 | VCSEAT2R ECU: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_VEH_state` | page 101 | VCSEAT2R ECU: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_PARTY_locState` | page 101 | VCSEAT2R ECU: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_LIPC_externalWatchdogHeartBeat` | page 101 | VCSEAT2R ECU: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_VEH_locState` | page 101 | VCSEAT2R ECU: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_BDY_locState` | page 101 | VCSEAT2R ECU: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a102_VEH_faultsAndExtras` | page 102 | VCSEAT2R ECU: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a102_VEH_feedbackStatus` | page 102 | VCSEAT2R ECU: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a102_VEH_sensorStatus` | page 102 | VCSEAT2R ECU: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a102_VEH_rods` | page 102 | VCSEAT2R ECU: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_VEH_hvsNm` | page 103 | VCSEAT2R ECU: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_VEH_vehNm` | page 103 | VCSEAT2R ECU: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_VEH_status` | page 103 | VCSEAT2R ECU: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_PT_ptNm` | page 103 | VCSEAT2R ECU: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_PT_status` | page 103 | VCSEAT2R ECU: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_VEH_evseStatus` | page 103 | VCSEAT2R ECU: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a105_VEH_states` | page 105 | VCSEAT2R ECU: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a105_VEH_chNm` | page 105 | VCSEAT2R ECU: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a105_VEH_dampingStates` | page 105 | VCSEAT2R ECU: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_VEH_dcdcStatus` | page 106 | VCSEAT2R ECU: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_VEH_thermalControl` | page 106 | VCSEAT2R ECU: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_VEH_dcdcRailStatus` | page 106 | VCSEAT2R ECU: a106 VEH dcdc rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_CH_dcdcRailStatus` | page 106 | VCSEAT2R ECU: a106 CH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_CH_alertMatrix` | page 106 | VCSEAT2R ECU: a106 CH alert matrix | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_hvsNm` | page 107 | VCSEAT2R ECU: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_vehNm` | page 107 | VCSEAT2R ECU: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_status` | page 107 | VCSEAT2R ECU: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_thermalStatus` | page 107 | VCSEAT2R ECU: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_bmbMinMax` | page 107 | VCSEAT2R ECU: a107 VEH bmb min max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_powerAvailable` | page 107 | VCSEAT2R ECU: a107 VEH power available | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_PT_ptNm` | page 107 | VCSEAT2R ECU: a107 PT pt nm | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_PT_status` | page 107 | VCSEAT2R ECU: a107 PT status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_PT_thermalStatus` | page 107 | VCSEAT2R ECU: a107 PT thermal status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_PT_socStatus` | page 107 | VCSEAT2R ECU: a107 PT soc status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_socStatus` | page 107 | VCSEAT2R ECU: a107 VEH soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_packConfig` | page 107 | VCSEAT2R ECU: a107 VEH pack config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_energyStatus` | page 107 | VCSEAT2R ECU: a107 VEH energy status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_VEH_chargeInfo` | page 107 | VCSEAT2R ECU: a107 VEH charge info | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_hvStatus` | page 108 | VCSEAT2R ECU: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_temperature` | page 108 | VCSEAT2R ECU: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_thermalControl` | page 108 | VCSEAT2R ECU: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_torque` | page 108 | VCSEAT2R ECU: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_status` | page 108 | VCSEAT2R ECU: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PARTY_torque` | page 108 | VCSEAT2R ECU: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PARTY_status` | page 108 | VCSEAT2R ECU: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PARTY_temperature` | page 108 | VCSEAT2R ECU: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PARTY_thermalControl` | page 108 | VCSEAT2R ECU: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PT_temperature` | page 108 | VCSEAT2R ECU: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PT_thermalControl` | page 108 | VCSEAT2R ECU: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_PARTY_motorStatus` | page 108 | VCSEAT2R ECU: a108 PARTY motor status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_VEH_motorStatus` | page 108 | VCSEAT2R ECU: a108 VEH motor status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_CH_torque` | page 108 | VCSEAT2R ECU: a108 CH torque | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_carState` | page 110 | VCSEAT2R ECU: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_carConfig` | page 110 | VCSEAT2R ECU: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_time` | page 110 | VCSEAT2R ECU: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_updateStatus` | page 110 | VCSEAT2R ECU: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_vehNm` | page 110 | VCSEAT2R ECU: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_mismatchFault` | page 110 | VCSEAT2R ECU: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_vin` | page 110 | VCSEAT2R ECU: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_bmpDebug` | page 110 | VCSEAT2R ECU: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_gearControl` | page 110 | VCSEAT2R ECU: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_VEH_canLogAvailability` | page 110 | VCSEAT2R ECU: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_airbagCutoffStatus` | page 110 | VCSEAT2R ECU: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_carConfig` | page 110 | VCSEAT2R ECU: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_carState` | page 110 | VCSEAT2R ECU: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_vin` | page 110 | VCSEAT2R ECU: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_chNm` | page 110 | VCSEAT2R ECU: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_CH_epochTimeGtw` | page 110 | VCSEAT2R ECU: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_PARTY_carConfig` | page 110 | VCSEAT2R ECU: a110 PARTY car config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_VEH_internalStatus` | page 111 | VCSEAT2R ECU: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_VEH_status` | page 111 | VCSEAT2R ECU: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_VEH_vehNm` | page 111 | VCSEAT2R ECU: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_RIPC_LVPowerState` | page 111 | VCSEAT2R ECU: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_RIPC_epbPrivateState` | page 111 | VCSEAT2R ECU: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_RIPC_railStatus` | page 111 | VCSEAT2R ECU: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_RIPC_remoteADC` | page 111 | VCSEAT2R ECU: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_RIPC_switchStatus` | page 111 | VCSEAT2R ECU: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_VEH_LVPowerState` | page 111 | VCSEAT2R ECU: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_VEH_seatStatus` | page 111 | VCSEAT2R ECU: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_PARTY_status` | page 111 | VCSEAT2R ECU: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_CH_status` | page 111 | VCSEAT2R ECU: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_VEH_internalStatus` | page 112 | VCSEAT2R ECU: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_VEH_status` | page 112 | VCSEAT2R ECU: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_VEH_vehNm` | page 112 | VCSEAT2R ECU: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_LIPC_LVPowerState` | page 112 | VCSEAT2R ECU: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_LIPC_epbPrivateState` | page 112 | VCSEAT2R ECU: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_LIPC_railStatus` | page 112 | VCSEAT2R ECU: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_LIPC_remoteADC` | page 112 | VCSEAT2R ECU: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_LIPC_switchStatus` | page 112 | VCSEAT2R ECU: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_VEH_LVPowerState` | page 112 | VCSEAT2R ECU: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_PARTY_status` | page 112 | VCSEAT2R ECU: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_CH_status` | page 112 | VCSEAT2R ECU: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_status` | page 114 | VCSEAT2R ECU: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_wheelSpeeds` | page 114 | VCSEAT2R ECU: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_VEH_wheelSpeeds` | page 114 | VCSEAT2R ECU: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_CH_wheelSpeeds` | page 114 | VCSEAT2R ECU: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_party3` | page 114 | VCSEAT2R ECU: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_VEH_party3` | page 114 | VCSEAT2R ECU: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_VEH_status` | page 114 | VCSEAT2R ECU: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_wheelRotation` | page 114 | VCSEAT2R ECU: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_CH_wheelRotation` | page 114 | VCSEAT2R ECU: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_VEH_wheelRotation` | page 114 | VCSEAT2R ECU: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_brakeTorque` | page 114 | VCSEAT2R ECU: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_PARTY_offsets` | page 114 | VCSEAT2R ECU: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_BDY_offsets` | page 114 | VCSEAT2R ECU: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_BDY_party3` | page 114 | VCSEAT2R ECU: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_BDY_status` | page 114 | VCSEAT2R ECU: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_BDY_wheelRotation` | page 114 | VCSEAT2R ECU: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_BDY_wheelSpeeds` | page 114 | VCSEAT2R ECU: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_CH_party1` | page 114 | VCSEAT2R ECU: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_CH_party3` | page 114 | VCSEAT2R ECU: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_CH_status` | page 114 | VCSEAT2R ECU: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VEH_vehNm` | page 115 | VCSEAT2R ECU: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VEH_authentication` | page 115 | VCSEAT2R ECU: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VEH_BLEResetRequest` | page 115 | VCSEAT2R ECU: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VEH_requests` | page 115 | VCSEAT2R ECU: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VEH_requests2` | page 115 | VCSEAT2R ECU: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_REM_authentication` | page 115 | VCSEAT2R ECU: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_UI_corianderVehicleControl` | page 115 | VCSEAT2R ECU: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_CH_TPMSDisplay` | page 115 | VCSEAT2R ECU: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_PARTY_epbmStatus` | page 116 | VCSEAT2R ECU: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_vehNm` | page 116 | VCSEAT2R ECU: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_hvacRequest` | page 116 | VCSEAT2R ECU: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_hvacStatus` | page 116 | VCSEAT2R ECU: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_LVPowerState` | page 116 | VCSEAT2R ECU: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_lightStatus` | page 116 | VCSEAT2R ECU: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_seatStatus` | page 116 | VCSEAT2R ECU: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_thsStatus` | page 116 | VCSEAT2R ECU: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_doorStatus` | page 116 | VCSEAT2R ECU: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_seatHeatStatus` | page 116 | VCSEAT2R ECU: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_restraintStatus` | page 116 | VCSEAT2R ECU: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_switchStatus` | page 116 | VCSEAT2R ECU: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_logging1Hz` | page 116 | VCSEAT2R ECU: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_seatStatus2` | page 116 | VCSEAT2R ECU: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_status` | page 116 | VCSEAT2R ECU: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_thermalCommand` | page 116 | VCSEAT2R ECU: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VEH_windowStatus` | page 116 | VCSEAT2R ECU: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_PARTY_restraintStatus` | page 116 | VCSEAT2R ECU: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_PARTY_doorStatus` | page 116 | VCSEAT2R ECU: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_BDY_epbmStatus` | page 116 | VCSEAT2R ECU: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_BDY_restraintStatus` | page 116 | VCSEAT2R ECU: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_BDY_switchStatus` | page 116 | VCSEAT2R ECU: a116 BDY switch status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_BDY_epbmStatus` | page 117 | VCSEAT2R ECU: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_BDY_restraintStatus` | page 117 | VCSEAT2R ECU: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_prndStatus` | page 117 | VCSEAT2R ECU: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_PARTY_epbmStatus` | page 117 | VCSEAT2R ECU: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_vehNm` | page 117 | VCSEAT2R ECU: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_hvacBlowerFdb` | page 117 | VCSEAT2R ECU: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_LVPowerState` | page 117 | VCSEAT2R ECU: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_restraintStatus` | page 117 | VCSEAT2R ECU: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_lightStatus` | page 117 | VCSEAT2R ECU: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_seatStatus` | page 117 | VCSEAT2R ECU: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_BDY_falconSwitchStatus` | page 117 | VCSEAT2R ECU: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_doorStatus` | page 117 | VCSEAT2R ECU: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_doorStatus2` | page 117 | VCSEAT2R ECU: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_windowStatus` | page 117 | VCSEAT2R ECU: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_switchStatus` | page 117 | VCSEAT2R ECU: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_intrusionSensorStatus` | page 117 | VCSEAT2R ECU: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_liftgateStatus` | page 117 | VCSEAT2R ECU: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_seatStatus2` | page 117 | VCSEAT2R ECU: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_PARTY_restraintStatus` | page 117 | VCSEAT2R ECU: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_thermalStatus` | page 117 | VCSEAT2R ECU: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_PARTY_doorStatus` | page 117 | VCSEAT2R ECU: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VEH_status` | page 117 | VCSEAT2R ECU: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_PARTY_prndStatus` | page 117 | VCSEAT2R ECU: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_PARTY_lightingSecondary` | page 117 | VCSEAT2R ECU: a117 PARTY lighting secondary | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_vehNm` | page 118 | VCSEAT2R ECU: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_lighting` | page 118 | VCSEAT2R ECU: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_sensors` | page 118 | VCSEAT2R ECU: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_status` | page 118 | VCSEAT2R ECU: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_okToUseHighPwr` | page 118 | VCSEAT2R ECU: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_LVPowerState` | page 118 | VCSEAT2R ECU: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_coolant` | page 118 | VCSEAT2R ECU: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_vehicleStatus` | page 118 | VCSEAT2R ECU: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_12VBatteryStatus` | page 118 | VCSEAT2R ECU: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_systemStatus` | page 118 | VCSEAT2R ECU: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_LVPowerState` | page 118 | VCSEAT2R ECU: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_outputPowerStatus` | page 118 | VCSEAT2R ECU: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_vehicleTime` | page 118 | VCSEAT2R ECU: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_thermalCommand` | page 118 | VCSEAT2R ECU: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_LVPowerState` | page 118 | VCSEAT2R ECU: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_sensors` | page 118 | VCSEAT2R ECU: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_sensors` | page 118 | VCSEAT2R ECU: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_interNodeResistance` | page 118 | VCSEAT2R ECU: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_lighting` | page 118 | VCSEAT2R ECU: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VEH_lightStatus` | page 118 | VCSEAT2R ECU: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_vehNm` | page 118 | VCSEAT2R ECU: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_12VBatteryStatus` | page 118 | VCSEAT2R ECU: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_LVBMS_statusHigh` | page 118 | VCSEAT2R ECU: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_CH_alertMatrix` | page 118 | VCSEAT2R ECU: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_BDY_outputPowerStatus` | page 118 | VCSEAT2R ECU: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_BDY_vehicleTime` | page 118 | VCSEAT2R ECU: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | VCSEAT2R ECU: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | VCSEAT2R ECU: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_PARTY_VCFRONT_cameraCleaningStatus` | page 118 | VCSEAT2R ECU: a118 PARTY VCFRONT camera cleaning status | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_VEH_steerAngle` | page 119 | VCSEAT2R ECU: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_VEH_leftStalk` | page 119 | VCSEAT2R ECU: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_VEH_rightStalk` | page 119 | VCSEAT2R ECU: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_PARTY_rightStalk` | page 119 | VCSEAT2R ECU: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_CH_steerAngle` | page 119 | VCSEAT2R ECU: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_PARTY_steerAngle` | page 119 | VCSEAT2R ECU: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_chassisCntl` | page 120 | VCSEAT2R ECU: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_systemStatus` | page 120 | VCSEAT2R ECU: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_CH_chassisCntl` | page 120 | VCSEAT2R ECU: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_systemStatus` | page 120 | VCSEAT2R ECU: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_torque` | page 120 | VCSEAT2R ECU: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_torque` | page 120 | VCSEAT2R ECU: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_locStatus` | page 120 | VCSEAT2R ECU: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_speed` | page 120 | VCSEAT2R ECU: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_speed` | page 120 | VCSEAT2R ECU: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_status` | page 120 | VCSEAT2R ECU: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PT_speed` | page 120 | VCSEAT2R ECU: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PT_systemStatus` | page 120 | VCSEAT2R ECU: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_vehicleEstimates` | page 120 | VCSEAT2R ECU: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_aggregatedAxleSpeed` | page 120 | VCSEAT2R ECU: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_aggregatedAxleSpeed` | page 120 | VCSEAT2R ECU: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_systemPower` | page 120 | VCSEAT2R ECU: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_autonomyHealth` | page 120 | VCSEAT2R ECU: a120 PARTY autonomy health | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_autonomyHealth` | page 120 | VCSEAT2R ECU: a120 VEH autonomy health | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PT_systemPower` | page 120 | VCSEAT2R ECU: a120 PT system power | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_stalklessInterfaces` | page 120 | VCSEAT2R ECU: a120 PARTY stalkless interfaces | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_CH_speed` | page 120 | VCSEAT2R ECU: a120 CH speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_estimatedBrakeTemp` | page 120 | VCSEAT2R ECU: a120 VEH estimated brake temp | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_prndControl` | page 120 | VCSEAT2R ECU: a120 PARTY prnd control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_locStatus2` | page 120 | VCSEAT2R ECU: a120 PARTY loc status2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_chassisCntl` | page 120 | VCSEAT2R ECU: a120 VEH chassis cntl | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_CH_locStatus2` | page 120 | VCSEAT2R ECU: a120 CH loc status2 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_locStatus` | page 120 | VCSEAT2R ECU: a120 VEH loc status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_locStatus2` | page 120 | VCSEAT2R ECU: a120 VEH loc status2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_prndControl` | page 120 | VCSEAT2R ECU: a120 VEH prnd control | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_vehicleEstimates` | page 120 | VCSEAT2R ECU: a120 VEH vehicle estimates | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_PARTY_motorStatus` | page 120 | VCSEAT2R ECU: a120 PARTY motor status | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_VEH_motorStatus` | page 120 | VCSEAT2R ECU: a120 VEH motor status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_BDY_speed` | page 120 | VCSEAT2R ECU: a120 BDY speed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a210_seatMotorCalibrated` | page 210 | VCSEAT2R ECU: a210 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a210_seatMotorCurrent` | page 210 | VCSEAT2R ECU: a210 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a210_seatMotorState` | page 210 | VCSEAT2R ECU: a210 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a210_seatSwitchBack` | page 210 | VCSEAT2R ECU: a210 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a210_seatSwitchForward` | page 210 | VCSEAT2R ECU: a210 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a211_seatMotorCurrent` | page 211 | VCSEAT2R ECU: a211 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a211_seatMotorPosReal` | page 211 | VCSEAT2R ECU: a211 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a211_seatMotorState` | page 211 | VCSEAT2R ECU: a211 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a211_seatSwitchBack` | page 211 | VCSEAT2R ECU: a211 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a211_seatSwitchForward` | page 211 | VCSEAT2R ECU: a211 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a212_seatMotorCurrent` | page 212 | VCSEAT2R ECU: a212 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a212_seatMotorPosReal` | page 212 | VCSEAT2R ECU: a212 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a212_seatMotorState` | page 212 | VCSEAT2R ECU: a212 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a212_seatSwitchBack` | page 212 | VCSEAT2R ECU: a212 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a212_seatSwitchForward` | page 212 | VCSEAT2R ECU: a212 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a213_seatMotorCalibrated` | page 213 | VCSEAT2R ECU: a213 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a213_seatMotorCurrent` | page 213 | VCSEAT2R ECU: a213 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a213_seatMotorPosReal` | page 213 | VCSEAT2R ECU: a213 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a213_seatMotorState` | page 213 | VCSEAT2R ECU: a213 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a213_seatSwitchBack` | page 213 | VCSEAT2R ECU: a213 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a213_seatSwitchForward` | page 213 | VCSEAT2R ECU: a213 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a214_seatMotorCurrent` | page 214 | VCSEAT2R ECU: a214 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a214_seatMotorDCurrent` | page 214 | VCSEAT2R ECU: a214 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a214_seatMotorPosReal` | page 214 | VCSEAT2R ECU: a214 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a214_seatMotorState` | page 214 | VCSEAT2R ECU: a214 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a215_seatMotorCurrent` | page 215 | VCSEAT2R ECU: a215 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a215_seatMotorDCurrent` | page 215 | VCSEAT2R ECU: a215 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a215_seatMotorPosReal` | page 215 | VCSEAT2R ECU: a215 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a215_seatMotorState` | page 215 | VCSEAT2R ECU: a215 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a224_seatMotorCalibrated` | page 224 | VCSEAT2R ECU: a224 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a224_seatMotorCurrent` | page 224 | VCSEAT2R ECU: a224 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a224_seatMotorState` | page 224 | VCSEAT2R ECU: a224 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a224_seatSwitchBack` | page 224 | VCSEAT2R ECU: a224 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a224_seatSwitchForward` | page 224 | VCSEAT2R ECU: a224 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a225_seatMotorCalibrated` | page 225 | VCSEAT2R ECU: a225 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a225_seatMotorCurrent` | page 225 | VCSEAT2R ECU: a225 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a225_seatMotorState` | page 225 | VCSEAT2R ECU: a225 seat motor state | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a225_seatSwitchBack` | page 225 | VCSEAT2R ECU: a225 seat switch back; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a225_seatSwitchForward` | page 225 | VCSEAT2R ECU: a225 seat switch forward; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a228_seatMotorCalibrated` | page 228 | VCSEAT2R ECU: a228 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a228_seatMotorCurrent` | page 228 | VCSEAT2R ECU: a228 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a228_seatMotorPosReal` | page 228 | VCSEAT2R ECU: a228 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a228_seatMotorState` | page 228 | VCSEAT2R ECU: a228 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a228_seatSwitchBack` | page 228 | VCSEAT2R ECU: a228 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a228_seatSwitchForward` | page 228 | VCSEAT2R ECU: a228 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a229_seatMotorCalibrated` | page 229 | VCSEAT2R ECU: a229 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a229_seatMotorCurrent` | page 229 | VCSEAT2R ECU: a229 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a229_seatMotorPosReal` | page 229 | VCSEAT2R ECU: a229 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a229_seatMotorState` | page 229 | VCSEAT2R ECU: a229 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a229_seatSwitchBack` | page 229 | VCSEAT2R ECU: a229 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a229_seatSwitchForward` | page 229 | VCSEAT2R ECU: a229 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a232_seatMotorCurrent` | page 232 | VCSEAT2R ECU: a232 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a232_seatMotorPosReal` | page 232 | VCSEAT2R ECU: a232 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a232_seatMotorState` | page 232 | VCSEAT2R ECU: a232 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a232_seatSwitchBack` | page 232 | VCSEAT2R ECU: a232 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a232_seatSwitchForward` | page 232 | VCSEAT2R ECU: a232 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a233_seatMotorCurrent` | page 233 | VCSEAT2R ECU: a233 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a233_seatMotorPosReal` | page 233 | VCSEAT2R ECU: a233 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a233_seatMotorState` | page 233 | VCSEAT2R ECU: a233 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a233_seatSwitchBack` | page 233 | VCSEAT2R ECU: a233 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a233_seatSwitchForward` | page 233 | VCSEAT2R ECU: a233 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a239_seatHeatCurrent` | page 239 | VCSEAT2R ECU: a239 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCSEAT2R_a239_seatHeatTmp` | page 239 | VCSEAT2R ECU: a239 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCSEAT2R_a239_seatHeatTmpTarget` | page 239 | VCSEAT2R ECU: a239 seat heat tmp target | 40\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63.5 |  | plausible |
| `VCSEAT2R_a240_seatHeatCurrent` | page 240 | VCSEAT2R ECU: a240 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCSEAT2R_a240_seatHeatTmp` | page 240 | VCSEAT2R ECU: a240 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |
| `VCSEAT2R_a242_snsShortCircuit` | page 242 | VCSEAT2R ECU: a242 sns short circuit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a242_snsDisconnect` | page 242 | VCSEAT2R ECU: a242 sns disconnect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a242_snsRateChangeUp` | page 242 | VCSEAT2R ECU: a242 sns rate change up | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a242_snsRateChangeDown` | page 242 | VCSEAT2R ECU: a242 sns rate change down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a251_seatMotorCurrent` | page 251 | VCSEAT2R ECU: a251 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a251_seatMotorPosReal` | page 251 | VCSEAT2R ECU: a251 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a251_seatMotorState` | page 251 | VCSEAT2R ECU: a251 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a251_seatSwitchBack` | page 251 | VCSEAT2R ECU: a251 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a251_seatSwitchForward` | page 251 | VCSEAT2R ECU: a251 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a252_seatMotorCurrent` | page 252 | VCSEAT2R ECU: a252 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a252_seatMotorPosReal` | page 252 | VCSEAT2R ECU: a252 seat motor pos real | 28\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a252_seatMotorState` | page 252 | VCSEAT2R ECU: a252 seat motor state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a252_seatSwitchBack` | page 252 | VCSEAT2R ECU: a252 seat switch back; raw 0 = signal not available (SNA) | 43\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a252_seatSwitchForward` | page 252 | VCSEAT2R ECU: a252 seat switch forward; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a260_seatStatePrev` | page 260 | VCSEAT2R ECU: a260 seat state prev | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a260_obstacleDetectReason` | page 260 | VCSEAT2R ECU: a260 obstacle detect reason | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `STALL_DETECTED`<br>2 = `SPEED_THRESHOLD`<br>3 = `MAX_SPEED_DIFF`<br>4 = `ACCEL_LOOKBACK_ABS`<br>5 = `SENSITIVE_CURRENT`<br>6 = `HISTORY_BASED` | plausible |
| `VCSEAT2R_a260_obstacleDetectPosition` | page 260 | VCSEAT2R ECU: a260 obstacle detect position | 22\|9 | little-endian | signed | 1 | 140 | mm | -116 to 395 |  | plausible |
| `VCSEAT2R_a260_accelLookbackTripDepth` | page 260 | VCSEAT2R ECU: a260 accel lookback trip depth | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a260_seatMotorCurrent` | page 260 | VCSEAT2R ECU: a260 seat motor current | 40\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a261_seatStatePrev` | page 261 | VCSEAT2R ECU: a261 seat state prev | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a261_obstacleDetectReason` | page 261 | VCSEAT2R ECU: a261 obstacle detect reason | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `STALL_DETECTED`<br>2 = `SPEED_THRESHOLD`<br>3 = `MAX_SPEED_DIFF`<br>4 = `ACCEL_LOOKBACK_ABS`<br>5 = `SENSITIVE_CURRENT`<br>6 = `HISTORY_BASED` | plausible |
| `VCSEAT2R_a261_obstacleDetectPosition` | page 261 | VCSEAT2R ECU: a261 obstacle detect position | 22\|9 | little-endian | signed | 1 | 140 | mm | -116 to 395 |  | plausible |
| `VCSEAT2R_a261_accelLookbackTripDepth` | page 261 | VCSEAT2R ECU: a261 accel lookback trip depth | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a261_seatMotorCurrent` | page 261 | VCSEAT2R ECU: a261 seat motor current | 40\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a263_seatMotorCurrent` | page 263 | VCSEAT2R ECU: a263 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a263_seatMotorDCurrent` | page 263 | VCSEAT2R ECU: a263 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a263_seatMotorPosReal` | page 263 | VCSEAT2R ECU: a263 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a263_seatMotorState` | page 263 | VCSEAT2R ECU: a263 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a264_seatMotorCurrent` | page 264 | VCSEAT2R ECU: a264 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a264_seatMotorDCurrent` | page 264 | VCSEAT2R ECU: a264 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a264_seatMotorPosReal` | page 264 | VCSEAT2R ECU: a264 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a264_seatMotorState` | page 264 | VCSEAT2R ECU: a264 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a267_seatMotorCurrent` | page 267 | VCSEAT2R ECU: a267 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a267_seatMotorDCurrent` | page 267 | VCSEAT2R ECU: a267 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a267_seatMotorPosReal` | page 267 | VCSEAT2R ECU: a267 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a267_seatMotorState` | page 267 | VCSEAT2R ECU: a267 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a268_seatMotorCurrent` | page 268 | VCSEAT2R ECU: a268 seat motor current | 16\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a268_seatMotorDCurrent` | page 268 | VCSEAT2R ECU: a268 seat motor d current | 28\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a268_seatMotorPosReal` | page 268 | VCSEAT2R ECU: a268 seat motor pos real | 40\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a268_seatMotorState` | page 268 | VCSEAT2R ECU: a268 seat motor state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a270_isRearwardEndstopUncalibrated` | page 270 | VCSEAT2R ECU: a270 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a270_isAbsPosSensorUncalibrated` | page 270 | VCSEAT2R ECU: a270 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a270_seatState` | page 270 | VCSEAT2R ECU: a270 seat state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCSEAT2R_a270_motorType` | page 270 | VCSEAT2R ECU: a270 motor type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCSEAT2R_a270_absPosSensState` | page 270 | VCSEAT2R ECU: a270 abs pos sens state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAULTED`<br>1 = `REARWARD`<br>2 = `FORWARD`<br>3 = `DISCONNECTED` | plausible |
| `VCSEAT2R_a273_calibrated` | page 273 | VCSEAT2R ECU: a273 calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a273_angle` | page 273 | VCSEAT2R ECU: a273 angle | 17\|8 | little-endian | signed | 0.5 | 59 | deg | -5 to 122.5 |  | plausible |
| `VCSEAT2R_a273_seatStatePrev` | page 273 | VCSEAT2R ECU: a273 seat state prev; raw 15 = signal not available (SNA) | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCSEAT2R_a273_obstacleDetectReason` | page 273 | VCSEAT2R ECU: a273 obstacle detect reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `MOTOR_CURRENT_STALL`<br>2 = `MOTOR_ENCODER_STALL`<br>3 = `ACCEL_LOOKBACK_UNCOMP_ABS`<br>4 = `ACCEL_LOOKBACK_UNCOMP_REL`<br>5 = `ACCEL_LOOKBACK_COMP_ABS`<br>6 = `MEDIUM_CURRENT_THRESHOLD`<br>7 = `SPEED_THRESHOLD`<br>8 = `MAX_SPEED_DIFF` | plausible |
| `VCSEAT2R_a273_accelLookbackTripDepth` | page 273 | VCSEAT2R ECU: a273 accel lookback trip depth | 33\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |
| `VCSEAT2R_a273_duty` | page 273 | VCSEAT2R ECU: a273 duty | 40\|8 | little-endian | signed | 1 | 0 | % | -128 to 127 |  | plausible |
| `VCSEAT2R_a273_currentAbsFilt` | page 273 | VCSEAT2R ECU: a273 current abs filt | 48\|8 | little-endian | unsigned | 0.25 | 0 | A | 0 to 63.75 |  | plausible |
| `VCSEAT2R_a273_motorType` | page 273 | VCSEAT2R ECU: a273 motor type | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB_OR_UNKNOWN`<br>1 = `KEIPER` | plausible |
| `VCSEAT2R_a273_absolutePosSensorForward` | page 273 | VCSEAT2R ECU: a273 absolute pos sensor forward | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a273_cabinTemp` | page 273 | VCSEAT2R ECU: a273 cabin temp | 58\|6 | little-endian | signed | 2 | 20 | degC | -44 to 82 |  | plausible |
| `VCSEAT2R_a277_isRearwardEndstopUncalibrated` | page 277 | VCSEAT2R ECU: a277 is rearward endstop uncalibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a277_isAbsPosSensorUncalibrated` | page 277 | VCSEAT2R ECU: a277 is abs pos sensor uncalibrated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a278_seatState` | page 278 | VCSEAT2R ECU: a278 seat state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `STOPPED`<br>1 = `ADJUSTING_FORWARD_COMFORT`<br>2 = `ADJUSTING_REARWARD_COMFORT`<br>3 = `ADJUSTING_FORWARD_FAST`<br>4 = `ADJUSTING_REARWARD_FAST`<br>5 = `FOLDING`<br>6 = `UNFOLDING`<br>7 = `MOVING_FORWARD_TO_POSITION`<br>8 = `MOVING_REARWARD_TO_POSITION`<br>9 = `WAITING_TO_CLEAR_FOR_FOLD`<br>10 = `WAITING_TO_CLEAR_FOR_UNFOLD`<br>11 = `CALIBRATING_ZERO_POSITION`<br>12 = `CALIBRATING_ABSOLUTE_SENSOR`<br>15 = `SNA` | plausible |
| `VCSEAT2R_a290_isNetworkSwitch` | page 290 | VCSEAT2R ECU: a290 is network switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a290_occupancySensorV` | page 290 | VCSEAT2R ECU: a290 occupancy sensor v | 17\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a290_railVoltage` | page 290 | VCSEAT2R ECU: a290 rail voltage | 32\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a291_buckleSensorVoltage` | page 291 | VCSEAT2R ECU: a291 buckle sensor voltage | 16\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCSEAT2R_a291_railVoltage` | page 291 | VCSEAT2R ECU: a291 rail voltage | 28\|12 | little-endian | unsigned | 0.01 | 0 | V | 0 to 40.95 |  | plausible |
| `VCSEAT2R_a426_seatMotorCalibrated` | page 426 | VCSEAT2R ECU: a426 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a426_seatMotorCurrent` | page 426 | VCSEAT2R ECU: a426 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a426_seatMotorPosReal` | page 426 | VCSEAT2R ECU: a426 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a426_seatMotorState` | page 426 | VCSEAT2R ECU: a426 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a426_seatSwitchBack` | page 426 | VCSEAT2R ECU: a426 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a426_seatSwitchForward` | page 426 | VCSEAT2R ECU: a426 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a426_cabinTmp` | page 426 | VCSEAT2R ECU: a426 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCSEAT2R_a427_seatMotorCalibrated` | page 427 | VCSEAT2R ECU: a427 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a427_seatMotorCurrent` | page 427 | VCSEAT2R ECU: a427 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a427_seatMotorPosReal` | page 427 | VCSEAT2R ECU: a427 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a427_seatMotorState` | page 427 | VCSEAT2R ECU: a427 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a427_seatSwitchBack` | page 427 | VCSEAT2R ECU: a427 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a427_seatSwitchForward` | page 427 | VCSEAT2R ECU: a427 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a427_cabinTmp` | page 427 | VCSEAT2R ECU: a427 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCSEAT2R_a428_seatMotorCalibrated` | page 428 | VCSEAT2R ECU: a428 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a428_seatMotorCurrent` | page 428 | VCSEAT2R ECU: a428 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a428_seatMotorPosReal` | page 428 | VCSEAT2R ECU: a428 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a428_seatMotorState` | page 428 | VCSEAT2R ECU: a428 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a428_seatSwitchBack` | page 428 | VCSEAT2R ECU: a428 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a428_seatSwitchForward` | page 428 | VCSEAT2R ECU: a428 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a428_cabinTmp` | page 428 | VCSEAT2R ECU: a428 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCSEAT2R_a429_seatMotorCalibrated` | page 429 | VCSEAT2R ECU: a429 seat motor calibrated | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a429_seatMotorCurrent` | page 429 | VCSEAT2R ECU: a429 seat motor current | 17\|12 | little-endian | signed | 0.01 | 0 | A | -20.48 to 20.47 |  | plausible |
| `VCSEAT2R_a429_seatMotorPosReal` | page 429 | VCSEAT2R ECU: a429 seat motor pos real | 32\|12 | little-endian | signed | 1 | 0 | mm | -2048 to 2047 |  | plausible |
| `VCSEAT2R_a429_seatMotorState` | page 429 | VCSEAT2R ECU: a429 seat motor state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STOPPED`<br>1 = `MOVING_UP`<br>2 = `MOVING_DOWN`<br>3 = `RECALLING`<br>4 = `CALIBRATING`<br>5 = `UNDEFINED` | plausible |
| `VCSEAT2R_a429_seatSwitchBack` | page 429 | VCSEAT2R ECU: a429 seat switch back; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a429_seatSwitchForward` | page 429 | VCSEAT2R ECU: a429 seat switch forward; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `OFF`<br>2 = `ON`<br>3 = `FAULT` | plausible |
| `VCSEAT2R_a429_cabinTmp` | page 429 | VCSEAT2R ECU: a429 cabin tmp | 52\|12 | little-endian | signed | 0.1 | 0 | degC | -204.8 to 204.7 |  | plausible |
| `VCSEAT2R_a444_retriesAvailable` | page 444 | VCSEAT2R ECU: a444 retries available | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a444_channel` | page 444 | VCSEAT2R ECU: a444 channel | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEAT2R_a444_watchdog` | page 444 | VCSEAT2R ECU: a444 watchdog | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_gateDriver` | page 444 | VCSEAT2R ECU: a444 gate driver | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_overcurrent` | page 444 | VCSEAT2R ECU: a444 overcurrent | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_supplyUndervoltage` | page 444 | VCSEAT2R ECU: a444 supply undervoltage | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_cpUndervoltage` | page 444 | VCSEAT2R ECU: a444 cp undervoltage | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_overTempShutdown` | page 444 | VCSEAT2R ECU: a444 over temp shutdown | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_overTempWarning` | page 444 | VCSEAT2R ECU: a444 over temp warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_highSide2GateDriver` | page 444 | VCSEAT2R ECU: a444 high side2 gate driver | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_lowSide2GateDriver` | page 444 | VCSEAT2R ECU: a444 low side2 gate driver | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_highSide1GateDriver` | page 444 | VCSEAT2R ECU: a444 high side1 gate driver | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_lowSide1GateDriver` | page 444 | VCSEAT2R ECU: a444 low side1 gate driver | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_highSide2OverCurent` | page 444 | VCSEAT2R ECU: a444 high side2 over curent | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_lowSide2OverCurent` | page 444 | VCSEAT2R ECU: a444 low side2 over curent | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_highSide1OverCurent` | page 444 | VCSEAT2R ECU: a444 high side1 over curent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_lowSide1OverCurent` | page 444 | VCSEAT2R ECU: a444 low side1 over curent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_spiInit` | page 444 | VCSEAT2R ECU: a444 spi init | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_spiPeriodicCheck` | page 444 | VCSEAT2R ECU: a444 spi periodic check | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_spiFault` | page 444 | VCSEAT2R ECU: a444 spi fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_voltageMonitor` | page 444 | VCSEAT2R ECU: a444 voltage monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_enableLow` | page 444 | VCSEAT2R ECU: a444 enable low | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a571_seatHeatCurrent` | page 571 | VCSEAT2R ECU: a571 seat heat current | 16\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | plausible |
| `VCSEAT2R_a571_seatHeatTmp` | page 571 | VCSEAT2R ECU: a571 seat heat tmp | 28\|12 | little-endian | signed | 0.05 | 0 | degC | -102.4 to 102.35 |  | plausible |

## Multiplexing

`VCSEAT2R_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 10 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (9 signals), page 88 (9 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (3 signals), page 95 (2 signals), page 96 (2 signals), page 97 (2 signals), page 98 (14 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (5 signals), page 107 (14 signals), page 108 (14 signals), page 110 (17 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (22 signals), page 117 (24 signals), page 118 (29 signals), page 119 (6 signals), page 120 (33 signals), page 210 (5 signals), page 211 (5 signals), page 212 (5 signals), page 213 (6 signals), page 214 (4 signals), page 215 (4 signals), page 224 (5 signals), page 225 (5 signals), page 228 (6 signals), page 229 (6 signals), page 232 (5 signals), page 233 (5 signals), page 239 (3 signals), page 240 (2 signals), page 242 (4 signals), page 251 (5 signals), page 252 (5 signals), page 260 (5 signals), page 261 (5 signals), page 263 (4 signals), page 264 (4 signals), page 267 (4 signals), page 268 (4 signals), page 270 (5 signals), page 273 (10 signals), page 277 (2 signals), page 278 (1 signals), page 290 (3 signals), page 291 (2 signals), page 426 (7 signals), page 427 (7 signals), page 428 (7 signals), page 429 (7 signals), page 444 (22 signals), page 571 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCSEAT2R ECU messages (VCSEAT2R)](../../vcseat2r.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
