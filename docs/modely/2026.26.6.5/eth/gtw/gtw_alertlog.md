---
layout: default
title: "GTW_alertLog (0x568) — Gateway, Tesla Model Y 2026.26.6.5 ETH"
description: "Gateway message: alert log. Ethernet-side message GTW_alertLog of Gateway for Tesla Model Y firmware 2026.26.6.5, 139 signals (GTW_alertID, GTW_alertState, GTW_a014_crcVersion, GTW_a015_crcVersion and 135 more). Bit layout, scaling, units and value tables."
---

# GTW_alertLog (0x568) — Gateway, Tesla Model Y 2026.26.6.5 ETH

Gateway message: alert log. This page documents the 139 signals of GTW_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_alertLog` |
| Ethernet-side id | 0x568 (1384) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 139 |

## Signals of GTW_alertLog

Tesla Model Y CAN bus signals in `GTW_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_alertID` | selector | Gateway: alert ID | 0\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_canEthTxQueue`<br>2 = `a002_taskError`<br>3 = `a003_logWriteRecord`<br>4 = `a004_mallocHook`<br>5 = `a005_stackOverflowHook`<br>6 = `a006_ifTxOutputFull`<br>7 = `a007_ifRxBufError`<br>8 = `a008_ifPbufAllocError`<br>9 = `a009_lateTask`<br>10 = `a010_wdTaskCount`<br>11 = `a011_cancoreWatchdog`<br>12 = `a012_maincoreWatchdog`<br>14 = `a014_APSversionMismatch`<br>15 = `a015_DIFversionMismatch`<br>16 = `a016_BLEEPCENTERversionMismatch`<br>17 = `a017_BMSversionMismatch`<br>18 = `a018_CMPversionMismatch`<br>19 = `a019_CPversionMismatch`<br>20 = `a020_DIRversionMismatch`<br>21 = `a021_EPAS3PversionMismatch`<br>22 = `a022_EPBLversionMismatch`<br>23 = `a023_EPBRversionMismatch`<br>24 = `a024_ESPversionMismatch`<br>25 = `a025_ESPCALversionMismatch`<br>26 = `a026_GTWversionMismatch`<br>27 = `a027_HVPversionMismatch`<br>28 = `a028_IBSTversionMismatch`<br>29 = `a029_IBSTCALversionMismatch`<br>30 = `a030_OCS1PversionMismatch`<br>31 = `a031_PARKversionMismatch`<br>32 = `a032_PCSversionMismatch`<br>33 = `a033_PCSCPU2versionMismatch`<br>34 = `a034_PMRversionMismatch`<br>35 = `a035_PMFversionMismatch`<br>36 = `a036_PTCversionMismatch`<br>37 = `a037_RADCversionMismatch`<br>38 = `a038_RCMversionMismatch`<br>39 = `a039_RCMCALversionMismatch`<br>40 = `a040_SCCMversionMismatch`<br>41 = `a041_VCSECversionMismatch`<br>42 = `a042_TASversionMismatch`<br>43 = `a043_THSversionMismatch`<br>45 = `a045_VCFRONTversionMismatch`<br>46 = `a046_VCLEFTversionMismatch`<br>47 = `a047_VCRIGHTversionMismatch`<br>48 = `a048_EPAS3SversionMismatch`<br>49 = `a049_corruptedManifest`<br>50 = `a050_sdCardInitFailure`<br>51 = `a051_sdCardFileSystemFailure`<br>52 = `a052_ifTxSpans`<br>53 = `a053_busSleepFailure`<br>54 = `a054_OPCRversionMismatch`<br>55 = `a055_OPCFversionMismatch`<br>57 = `a057_i2cFailure`<br>58 = `a058_rtcAlarmFailure`<br>59 = `a059_inFactoryMode`<br>60 = `a060_unFused`<br>61 = `a061_bmpSleepFailure`<br>62 = `a062_bmpWatchdog`<br>63 = `a063_VEH_canFault`<br>64 = `a064_CH_canFault`<br>65 = `a065_PARTY_canFault`<br>66 = `a066_exception`<br>67 = `a067_tcpDebug`<br>68 = `a068_prodKeyMissing`<br>69 = `a069_diskioErr`<br>70 = `a070_hrlDump`<br>71 = `a071_hrlTrigger`<br>72 = `a072_updateFailure`<br>73 = `a073_steeringWheelReset`<br>74 = `a074_epas3pMIA`<br>75 = `a075_epas3sMIA`<br>76 = `a076_ethInterfaceReset`<br>77 = `a077_bmpPmicError`<br>78 = `a078_VEHbusOverloaded`<br>79 = `a079_PARTYbusOverloaded`<br>80 = `a080_CHbusOverloaded`<br>81 = `a081_udsMessageRejected`<br>82 = `a082_sdCardBSCorrupted`<br>83 = `a083_udsMsgDroppedByTcpStack`<br>84 = `a084_canFrameDropped`<br>85 = `a085_fuseStateUnknown`<br>86 = `a086_ocu`<br>87 = `a087_ocuInProgress`<br>88 = `a088_sdCardInvReqParallel`<br>89 = `a089_sdCardWatchdog`<br>90 = `a090_ocuFailed`<br>91 = `a091_lowStack`<br>92 = `a092_sdCardInvReqZero`<br>93 = `a093_sdCardInvReqOverflowBase`<br>94 = `a094_sdCardInvReqOverflowCount`<br>95 = `a095_sdCardFull`<br>96 = `a096_sdCardFatCorrupted`<br>97 = `a097_HCMLversionMismatch`<br>98 = `a098_HCMRversionMismatch`<br>99 = `a099_SWCversionMismatch`<br>100 = `a100_CBCversionMismatch`<br>101 = `a101_switchWatchdog`<br>103 = `a103_sdCardFormatted`<br>104 = `a104_sdCardDriverArgCorrupted`<br>105 = `a105_eBuckConfigured`<br>106 = `a106_BLEEPLEFTversionMismatch`<br>107 = `a107_BLEEPRIGHTversionMismatch`<br>108 = `a108_BLEEPREARversionMismatch`<br>109 = `a109_failedToStartUpdater`<br>110 = `a110_readMdioFailed`<br>111 = `a111_writeMdioFailed`<br>112 = `a112_z4bDisabled`<br>113 = `a113_unrecognizedCanMessage`<br>114 = `a114_updtRetried`<br>115 = `a115_hrlEventFileAvail`<br>116 = `a116_switchInitFailed`<br>117 = `a117_unexpectedDestructiveResetStatus`<br>118 = `a118_unexpectedFunctionalResetStatus`<br>120 = `a120_switchUnlocked`<br>122 = `a122_BDY_canFault`<br>123 = `a123_BDYbusOverloaded`<br>125 = `a125_switchReplayUnlocked`<br>127 = `a127_noFilePointersAvailable`<br>129 = `a129_ICRversionMismatch`<br>133 = `a133_adspFaultDetected`<br>134 = `a134_disableFeatureFailed`<br>135 = `a135_canLogQueueFull`<br>136 = `a136_hrlGameModeFileAvail`<br>137 = `a137_lowHeap`<br>138 = `a138_sdCardEndOfLife`<br>139 = `a139_CMPDversionMismatch`<br>140 = `a140_cancoreHeartbeat`<br>141 = `a141_teleCANETHis`<br>143 = `a143_possibleCanWakeIssue`<br>144 = `a144_hrlStateMachine`<br>145 = `a145_carConfigsNotWritten`<br>146 = `a146_performancePackageMismatch`<br>147 = `a147_updateAbortFor12v`<br>149 = `a149_rtcTimeSetInPast`<br>150 = `a150_HCM3LversionMismatch`<br>151 = `a151_HCM3RversionMismatch`<br>153 = `a153_externalRtcAlarmFailure`<br>155 = `a155_PMversionMismatch`<br>164 = `a164_VCBATTversionMismatch`<br>165 = `a165_USMversionMismatch`<br>166 = `a166_nErrCanFaultVeh`<br>167 = `a167_nErrCanFaultCh`<br>168 = `a168_nErrCanFaultParty`<br>169 = `a169_TPMSsoftWarnFrontLeft`<br>170 = `a170_TPMSsoftWarnFrontRight`<br>171 = `a171_TPMSsoftWarnRearLeft`<br>172 = `a172_TPMSsoftWarnRearRight`<br>173 = `a173_TPMShardWarnFrontLeft`<br>174 = `a174_TPMShardWarnFrontRight`<br>175 = `a175_TPMShardWarnRearLeft`<br>176 = `a176_TPMShardWarnRearRight`<br>186 = `a186_swrPrecaution`<br>218 = `a218_switchOTPIncorrect`<br>219 = `a219_CMPSversionMismatch`<br>223 = `a223_LVBMSversionMismatch`<br>224 = `a224_sdCardUpgradeNeeded`<br>225 = `a225_resetOnSleepWake`<br>226 = `a226_DISPversionMismatch`<br>227 = `a227_DISPTOUCHversionMismatch`<br>228 = `a228_DISPOSDversionMismatch`<br>229 = `a229_displaySoftsetConnection`<br>230 = `a230_touchInterruptStorm`<br>244 = `a244_SDCRversionMismatch`<br>245 = `a245_apsNotDisabled`<br>246 = `a246_touchcoreHeartbeat`<br>255 = `a255_rtc32KHzWatchdog`<br>260 = `a260_unknownPN`<br>261 = `a261_adspWatchdog`<br>262 = `a262_canLogBlockDropped`<br>263 = `a263_hrlUdpFileAvail`<br>264 = `a264_hrlPseudoFileAvail`<br>265 = `a265_optionFlagsError`<br>266 = `a266_dpp1MIA`<br>267 = `a267_dpp2MIA`<br>268 = `a268_stoMIA`<br>273 = `a273_BLEEPREARLEFTversionMismatch`<br>274 = `a274_BLEEPREARRIGHTversionMismatch`<br>275 = `a275_VDDCORE_DrMOS_Fault`<br>276 = `a276_VDDSOC_DrMOS_Fault`<br>277 = `a277_NonRevCDrMOSMitigationFailed`<br>278 = `a278_ethSwitchCongested`<br>279 = `a279_adspRepeatedWatchdog`<br>280 = `a280_hrlFrameDropped`<br>281 = `a281_likelyMissedPoke`<br>282 = `a282_tcuPhyConfigurationFailed`<br>309 = `a309_VCUSBversionMismatch`<br>311 = `a311_canLogQueueFullBeforeFsInit`<br>312 = `a312_hrlFileIncomplete`<br>313 = `a313_OSDActive`<br>314 = `a314_canLogBlockWriteErr`<br>316 = `a316_sdCardChkdskRepair`<br>317 = `a317_sdCardChkdskRepairFailed`<br>322 = `a322_gestureUnrecognizedFromMoving`<br>323 = `a323_gestureStartOutOfStrip`<br>328 = `a328_smartShiftDisabled`<br>329 = `a329_FOHMversionMismatch`<br>330 = `a330_SWSLversionMismatch`<br>331 = `a331_SWSRversionMismatch`<br>332 = `a332_unknownDisplayPN`<br>334 = `a334_hrlFolderSpaceLow`<br>336 = `a336_possibleCanTxIssue`<br>342 = `a342_VCBLDCPPversionMismatch`<br>348 = `a348_VCBLDCFversionMismatch`<br>349 = `a349_VCBLDCPBversionMismatch`<br>350 = `a350_mOSDCrcCheck`<br>351 = `a351_sOSDCrcCheck`<br>352 = `a352_mASILStatusCheck`<br>353 = `a353_sASILStatusCheck`<br>354 = `a354_EPASTPversionMismatch`<br>355 = `a355_EPASTSversionMismatch`<br>356 = `a356_touchGPIOStatusCheck`<br>358 = `a358_RGBIPFLversionMismatch`<br>359 = `a359_RGBIPFRversionMismatch`<br>360 = `a360_RGBDOORFLversionMismatch`<br>361 = `a361_RGBDOORRLversionMismatch`<br>362 = `a362_RGBDOORFRversionMismatch`<br>363 = `a363_RGBDOORRRversionMismatch`<br>364 = `a364_BLEEPCRADLEversionMismatch`<br>366 = `a366_uiGearRequestMismatch`<br>376 = `a376_blFailedToExecBootImg`<br>380 = `a380_DPBversionMismatch`<br>381 = `a381_DPBCALversionMismatch`<br>382 = `a382_IDBversionMismatch`<br>383 = `a383_IDB1versionMismatch`<br>384 = `a384_IDBCALversionMismatch`<br>385 = `a385_RCUversionMismatch`<br>386 = `a386_RCUCALversionMismatch`<br>387 = `a387_externalRtcReadFailure`<br>388 = `a388_adspWatchdogSkipped`<br>389 = `a389_rcmEventDetected`<br>390 = `a390_displayFwQueryFailed`<br>391 = `a391_adspMacAddrCheckFailed`<br>393 = `a393_osdSramCrcMismatch`<br>394 = `a394_WIPERversionMismatch`<br>395 = `a395_lwipIcmpError`<br>396 = `a396_alreadyInReverse`<br>397 = `a397_alreadyInDrive`<br>398 = `a398_awakeForExtendedTime`<br>399 = `a399_ethIfRxTcpipQueueDrop`<br>400 = `a400_ethlSwitchOTPIncorrect`<br>401 = `a401_VCSEAT2LversionMismatch`<br>402 = `a402_VCSEAT2RversionMismatch`<br>409 = `a409_unexpectedResetCause`<br>410 = `a410_unexpectedResetCause2`<br>411 = `a411_tASILStatusCheck`<br>414 = `a414_socHeldInReset`<br>418 = `a418_TRCMversionMismatch`<br>420 = `a420_unexpectedCanMessageLength`<br>421 = `a421_ModemEthLinkDown`<br>422 = `a422_ethSwitchSevereCongestionWatchdog`<br>427 = `a427_DISPBRIDGEversionMismatch`<br>428 = `a428_LUMBAR32LversionMismatch`<br>429 = `a429_LUMBAR32RversionMismatch`<br>436 = `a436_possibleCanRxIssue`<br>437 = `a437_softFlowControlNotRunning`<br>438 = `a438_wakeSourceUnknown`<br>439 = `a439_VCCCversionMismatch`<br>450 = `a450_unexpectedAutopilotControlCanMessage`<br>451 = `a451_diagCanBufferExhausted`<br>452 = `a452_diagCanStaleSocket`<br>453 = `a453_diagCanFdSetDesync`<br>454 = `a454_diagCanFrameOverread`<br>455 = `a455_hrlDumpPageOwnershipError`<br>456 = `a456_hrlStateMachinePageOwnershipError`<br>463 = `a463_displayEdidReadFailed`<br>469 = `a469_backlightFsmUnhealthy` | plausible |
| `GTW_alertState` |  | Gateway: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `GTW_a014_crcVersion` | page 14 | Gateway: a014 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a015_crcVersion` | page 15 | Gateway: a015 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a016_crcVersion` | page 16 | Gateway: a016 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a017_crcVersion` | page 17 | Gateway: a017 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a018_crcVersion` | page 18 | Gateway: a018 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a019_crcVersion` | page 19 | Gateway: a019 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a020_crcVersion` | page 20 | Gateway: a020 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a021_crcVersion` | page 21 | Gateway: a021 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a022_crcVersion` | page 22 | Gateway: a022 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a023_crcVersion` | page 23 | Gateway: a023 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a024_crcVersion` | page 24 | Gateway: a024 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a025_crcVersion` | page 25 | Gateway: a025 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a026_crcVersion` | page 26 | Gateway: a026 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a027_crcVersion` | page 27 | Gateway: a027 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a028_crcVersion` | page 28 | Gateway: a028 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a029_crcVersion` | page 29 | Gateway: a029 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a030_crcVersion` | page 30 | Gateway: a030 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a031_crcVersion` | page 31 | Gateway: a031 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a032_crcVersion` | page 32 | Gateway: a032 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a033_crcVersion` | page 33 | Gateway: a033 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a034_crcVersion` | page 34 | Gateway: a034 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a035_crcVersion` | page 35 | Gateway: a035 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a036_crcVersion` | page 36 | Gateway: a036 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a037_crcVersion` | page 37 | Gateway: a037 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a038_crcVersion` | page 38 | Gateway: a038 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a039_crcVersion` | page 39 | Gateway: a039 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a040_crcVersion` | page 40 | Gateway: a040 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a041_crcVersion` | page 41 | Gateway: a041 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a042_crcVersion` | page 42 | Gateway: a042 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a043_crcVersion` | page 43 | Gateway: a043 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a045_crcVersion` | page 45 | Gateway: a045 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a046_crcVersion` | page 46 | Gateway: a046 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a047_crcVersion` | page 47 | Gateway: a047 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a048_crcVersion` | page 48 | Gateway: a048 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a049_headerError` | page 49 | Gateway: a049 header error | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEADER_OK`<br>1 = `HEADER_INFO_BAD`<br>2 = `MUID_LIST_UNEXPECTED`<br>3 = `HEADER_READ_FAIL` | plausible |
| `GTW_a054_crcVersion` | page 54 | Gateway: a054 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a055_crcVersion` | page 55 | Gateway: a055 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a062_bmpWatchdogReason` | page 62 | Gateway: a062 bmp watchdog reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WATCHDOG_NONE`<br>1 = `RUNTIME_FAILURE`<br>2 = `WAKE_FAILURE`<br>3 = `SLEEP_FAILURE`<br>4 = `THERMAL_TRIP` | plausible |
| `GTW_a063_VEH_faultConfinement` | page 63 | Gateway: a063 VEH fault confinement | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_a064_CH_faultConfinement` | page 64 | Gateway: a064 CH fault confinement | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_a065_PARTY_faultConfinement` | page 65 | Gateway: a065 PARTY fault confinement | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_a066_type` | page 66 | Gateway: a066 type | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `GTW_a066_exceptionCfgId` | page 66 | Gateway: a066 exception cfg id | 21\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a066_uptime` | page 66 | Gateway: a066 uptime | 29\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a066_core` | page 66 | Gateway: a066 core | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `GTW_a068_codeKeyMissing` | page 68 | Gateway: a068 code key missing | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a068_cmdKeyMissing` | page 68 | Gateway: a068 cmd key missing | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_sdIntStatusErrs` | page 69 | Gateway: a069 sd int status errs | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_sdTimeout` | page 69 | Gateway: a069 sd timeout | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_sdCmdErr` | page 69 | Gateway: a069 sd cmd err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_sdWriteErr` | page 69 | Gateway: a069 sd write err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_sdReadErr` | page 69 | Gateway: a069 sd read err | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a069_autoCmd12Err` | page 69 | Gateway: a069 auto cmd12 err | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a072_updtFailureMask` | page 72 | Gateway: a072 updt failure mask | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a073_SOCResetRequestor` | page 73 | Gateway: a073 SOC reset requestor | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `BUTTONS`<br>2 = `FORCE`<br>3 = `VCSEC`<br>4 = `DAS` | plausible |
| `GTW_a077_bmpPmicErrorType` | page 77 | Gateway: a077 bmp pmic error type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `OC_OV_CC`<br>2 = `MEM_CORRUPT`<br>3 = `OT`<br>4 = `INTERNAL_SM` | plausible |
| `GTW_a097_crcVersion` | page 97 | Gateway: a097 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a098_crcVersion` | page 98 | Gateway: a098 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a099_crcVersion` | page 99 | Gateway: a099 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a100_crcVersion` | page 100 | Gateway: a100 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a101_switchStuck` | page 101 | Gateway: a101 switch stuck | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a101_ETH_SW_nINT` | page 101 | Gateway: a101 ETH SW n INT | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_a106_crcVersion` | page 106 | Gateway: a106 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a107_crcVersion` | page 107 | Gateway: a107 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a108_crcVersion` | page 108 | Gateway: a108 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a117_MC_RGM_DES` | page 117 | Gateway: a117 MC RGM DES | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a118_MC_RGM_FES` | page 118 | Gateway: a118 MC RGM FES | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a122_BDY_faultConfinement` | page 122 | Gateway: a122 BDY fault confinement | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_a129_crcVersion` | page 129 | Gateway: a129 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a138_sdLifetimeUsed` | page 138 | Gateway: a138 sd lifetime used | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a139_crcVersion` | page 139 | Gateway: a139 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a150_crcVersion` | page 150 | Gateway: a150 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a151_crcVersion` | page 151 | Gateway: a151 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a155_crcVersion` | page 155 | Gateway: a155 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a164_crcVersion` | page 164 | Gateway: a164 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a165_crcVersion` | page 165 | Gateway: a165 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a169_TPMS_pressureFL` | page 169 | Gateway: a169 TPMS pressure FL | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a170_TPMS_pressureFR` | page 170 | Gateway: a170 TPMS pressure FR | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a171_TPMS_pressureRL` | page 171 | Gateway: a171 TPMS pressure RL | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a172_TPMS_pressureRR` | page 172 | Gateway: a172 TPMS pressure RR | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a173_TPMS_pressureFL` | page 173 | Gateway: a173 TPMS pressure FL | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a174_TPMS_pressureFR` | page 174 | Gateway: a174 TPMS pressure FR | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a175_TPMS_pressureRL` | page 175 | Gateway: a175 TPMS pressure RL | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a176_TPMS_pressureRR` | page 176 | Gateway: a176 TPMS pressure RR | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a219_crcVersion` | page 219 | Gateway: a219 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a223_crcVersion` | page 223 | Gateway: a223 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a226_crcVersion` | page 226 | Gateway: a226 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a227_crcVersion` | page 227 | Gateway: a227 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a228_crcVersion` | page 228 | Gateway: a228 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a244_crcVersion` | page 244 | Gateway: a244 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a245_page0ControlValue` | page 245 | Gateway: a245 page0 control value | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a245_page1ControlValue` | page 245 | Gateway: a245 page1 control value | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a261_failureReason` | page 261 | Gateway: a261 failure reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ERROR`<br>1 = `RECEIVE_ERROR`<br>2 = `INCORRECT_LENGTH`<br>3 = `INCORRECT_ADDRESS`<br>4 = `INCORRECT_ID`<br>5 = `INCORRECT_SEQ_NO`<br>6 = `INCORRECT_TYPE` | plausible |
| `GTW_a261_failureData1` | page 261 | Gateway: a261 failure data1 | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a261_failureData2` | page 261 | Gateway: a261 failure data2 | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a273_crcVersion` | page 273 | Gateway: a273 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a274_crcVersion` | page 274 | Gateway: a274 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a277_mitigationFailureReason` | page 277 | Gateway: a277 mitigation failure reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APPLIED_SUCCESSFULLY`<br>1 = `NOT_NEEDED`<br>2 = `FAILED_ICE_NOT_AWAKE`<br>3 = `FAILED_REGISTER_READ`<br>4 = `FAILED_REGISTER_WRITE`<br>5 = `FAILED_REGISTERS_WRITE_PROTECTED`<br>6 = `FAILED_NVRAM_WRITE_PROTECTED`<br>7 = `FAILED_NVRAM_WRITE` | plausible |
| `GTW_a279_repeatCount` | page 279 | Gateway: a279 repeat count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_a279_failureReason` | page 279 | Gateway: a279 failure reason | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ERROR`<br>1 = `RECEIVE_ERROR`<br>2 = `INCORRECT_LENGTH`<br>3 = `INCORRECT_ADDRESS`<br>4 = `INCORRECT_ID`<br>5 = `INCORRECT_SEQ_NO`<br>6 = `INCORRECT_TYPE` | plausible |
| `GTW_a279_failureData1` | page 279 | Gateway: a279 failure data1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a279_failureData2` | page 279 | Gateway: a279 failure data2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `GTW_a309_crcVersion` | page 309 | Gateway: a309 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a317_status` | page 317 | Gateway: a317 status | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `NOT_NEEDED`<br>2 = `SUCCESS`<br>3 = `FAILED`<br>4 = `PARTIAL`<br>7 = `MASK` | plausible |
| `GTW_a317_errorCode` | page 317 | Gateway: a317 error code | 19\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NO_ERROR`<br>1 = `ERROR_FOUND`<br>2 = `ERROR_FOUND_FIXED`<br>3 = `INSUFFICIENT_MEMORY`<br>4 = `DISK_INIT_FAILED`<br>5 = `MBR_READ_FAILED`<br>6 = `BR_READ_FAILED`<br>7 = `BAD_SECTOR_SIZE`<br>8 = `NOT_FAT32`<br>9 = `FAT_WRITE_FAILED`<br>10 = `FAT_READ_FAILED`<br>11 = `FAT_MISMATCHED`<br>12 = `CLUSTER_IN_USE`<br>13 = `UNKNOWN_FS`<br>14 = `DIR_TOO_DEEP`<br>15 = `INVALID_CLUSTER`<br>16 = `FS_INFO_WRITE_FAILED`<br>17 = `FS_INFO_READ_FAILED`<br>18 = `FS_INFO_SECTOR_NOT_FOUND`<br>19 = `FS_INFO_INVALID_SIG` | plausible |
| `GTW_a329_crcVersion` | page 329 | Gateway: a329 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a330_crcVersion` | page 330 | Gateway: a330 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a331_crcVersion` | page 331 | Gateway: a331 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a342_crcVersion` | page 342 | Gateway: a342 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a348_crcVersion` | page 348 | Gateway: a348 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a349_crcVersion` | page 349 | Gateway: a349 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a354_crcVersion` | page 354 | Gateway: a354 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a355_crcVersion` | page 355 | Gateway: a355 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a358_crcVersion` | page 358 | Gateway: a358 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a359_crcVersion` | page 359 | Gateway: a359 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a360_crcVersion` | page 360 | Gateway: a360 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a361_crcVersion` | page 361 | Gateway: a361 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a362_crcVersion` | page 362 | Gateway: a362 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a363_crcVersion` | page 363 | Gateway: a363 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a364_crcVersion` | page 364 | Gateway: a364 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a380_crcVersion` | page 380 | Gateway: a380 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a381_crcVersion` | page 381 | Gateway: a381 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a382_crcVersion` | page 382 | Gateway: a382 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a383_crcVersion` | page 383 | Gateway: a383 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a384_crcVersion` | page 384 | Gateway: a384 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a385_crcVersion` | page 385 | Gateway: a385 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a386_crcVersion` | page 386 | Gateway: a386 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a394_crcVersion` | page 394 | Gateway: a394 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a401_crcVersion` | page 401 | Gateway: a401 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a402_crcVersion` | page 402 | Gateway: a402 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a409_RES_CAUSE` | page 409 | Gateway: a409 RES CAUSE | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a410_RES_CAUSE2` | page 410 | Gateway: a410 RES CAUSE2 | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a418_crcVersion` | page 418 | Gateway: a418 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a427_crcVersion` | page 427 | Gateway: a427 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a428_crcVersion` | page 428 | Gateway: a428 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a429_crcVersion` | page 429 | Gateway: a429 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_a439_crcVersion` | page 439 | Gateway: a439 crc version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`GTW_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 14 (1 signals), page 15 (1 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (1 signals), page 21 (1 signals), page 22 (1 signals), page 23 (1 signals), page 24 (1 signals), page 25 (1 signals), page 26 (1 signals), page 27 (1 signals), page 28 (1 signals), page 29 (1 signals), page 30 (1 signals), page 31 (1 signals), page 32 (1 signals), page 33 (1 signals), page 34 (1 signals), page 35 (1 signals), page 36 (1 signals), page 37 (1 signals), page 38 (1 signals), page 39 (1 signals), page 40 (1 signals), page 41 (1 signals), page 42 (1 signals), page 43 (1 signals), page 45 (1 signals), page 46 (1 signals), page 47 (1 signals), page 48 (1 signals), page 49 (1 signals), page 54 (1 signals), page 55 (1 signals), page 62 (1 signals), page 63 (1 signals), page 64 (1 signals), page 65 (1 signals), page 66 (4 signals), page 68 (2 signals), page 69 (6 signals), page 72 (1 signals), page 73 (1 signals), page 77 (1 signals), page 97 (1 signals), page 98 (1 signals), page 99 (1 signals), page 100 (1 signals), page 101 (2 signals), page 106 (1 signals), page 107 (1 signals), page 108 (1 signals), page 117 (1 signals), page 118 (1 signals), page 122 (1 signals), page 129 (1 signals), page 138 (1 signals), page 139 (1 signals), page 150 (1 signals), page 151 (1 signals), page 155 (1 signals), page 164 (1 signals), page 165 (1 signals), page 169 (1 signals), page 170 (1 signals), page 171 (1 signals), page 172 (1 signals), page 173 (1 signals), page 174 (1 signals), page 175 (1 signals), page 176 (1 signals), page 219 (1 signals), page 223 (1 signals), page 226 (1 signals), page 227 (1 signals), page 228 (1 signals), page 244 (1 signals), page 245 (2 signals), page 261 (3 signals), page 273 (1 signals), page 274 (1 signals), page 277 (1 signals), page 279 (4 signals), page 309 (1 signals), page 317 (2 signals), page 329 (1 signals), page 330 (1 signals), page 331 (1 signals), page 342 (1 signals), page 348 (1 signals), page 349 (1 signals), page 354 (1 signals), page 355 (1 signals), page 358 (1 signals), page 359 (1 signals), page 360 (1 signals), page 361 (1 signals), page 362 (1 signals), page 363 (1 signals), page 364 (1 signals), page 380 (1 signals), page 381 (1 signals), page 382 (1 signals), page 383 (1 signals), page 384 (1 signals), page 385 (1 signals), page 386 (1 signals), page 394 (1 signals), page 401 (1 signals), page 402 (1 signals), page 409 (1 signals), page 410 (1 signals), page 418 (1 signals), page 427 (1 signals), page 428 (1 signals), page 429 (1 signals), page 439 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
