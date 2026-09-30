---
layout: default
title: "GTW_alertMatrix (0x3E) — Gateway, Tesla Model Y 2025.20.8 ETH"
description: "Gateway message: alert matrix. Ethernet-side message GTW_alertMatrix of Gateway for Tesla Model Y firmware 2025.20.8, 241 signals (GTW_matrixIndex, GTW_w001_canEthTxQueue, GTW_w002_taskError, GTW_w003_logWriteRecord and 237 more). Bit layout, scaling, units and value tables."
---

# GTW_alertMatrix (0x3E) — Gateway, Tesla Model Y 2025.20.8 ETH

Gateway message: alert matrix. This page documents the 241 signals of GTW_alertMatrix as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_alertMatrix` |
| Ethernet-side id | 0x3E (62) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 241 |

## Signals of GTW_alertMatrix

Tesla Model Y CAN bus signals in `GTW_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_matrixIndex` | selector | Gateway: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6` | plausible |
| `GTW_w001_canEthTxQueue` | page 0 | Gateway: w001 can eth tx queue | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w002_taskError` | page 0 | Gateway: w002 task error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w003_logWriteRecord` | page 0 | Gateway: w003 log write record | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w004_mallocHook` | page 0 | Gateway: w004 malloc hook | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w005_stackOverflowHook` | page 0 | Gateway: w005 stack overflow hook | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w006_ifTxOutputFull` | page 0 | Gateway: w006 if tx output full | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w007_ifRxBufError` | page 0 | Gateway: w007 if rx buf error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w008_ifPbufAllocError` | page 0 | Gateway: w008 if pbuf alloc error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w009_lateTask` | page 0 | Gateway: w009 late task | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w010_wdTaskCount` | page 0 | Gateway: w010 wd task count | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w011_cancoreWatchdog` | page 0 | Gateway: w011 cancore watchdog | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w012_maincoreWatchdog` | page 0 | Gateway: w012 maincore watchdog | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w014_APSversionMismatch` | page 0 | Gateway: w014 AP sversion mismatch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w015_DIFversionMismatch` | page 0 | Gateway: w015 DI fversion mismatch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w016_BLEEPCENTERversionMismatch` | page 0 | Gateway: w016 BLEEPCENTE rversion mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w017_BMSversionMismatch` | page 0 | Gateway: w017 BM sversion mismatch | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w018_CMPversionMismatch` | page 0 | Gateway: w018 CM pversion mismatch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w019_CPversionMismatch` | page 0 | Gateway: w019 c pversion mismatch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w020_DIRversionMismatch` | page 0 | Gateway: w020 DI rversion mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w021_EPAS3PversionMismatch` | page 0 | Gateway: w021 EPAS3 pversion mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w022_EPBLversionMismatch` | page 0 | Gateway: w022 EPB lversion mismatch | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w023_EPBRversionMismatch` | page 0 | Gateway: w023 EPB rversion mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w024_ESPversionMismatch` | page 0 | Gateway: w024 ES pversion mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w025_ESPCALversionMismatch` | page 0 | Gateway: w025 ESPCA lversion mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w026_GTWversionMismatch` | page 0 | Gateway: w026 GT wversion mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w027_HVPversionMismatch` | page 0 | Gateway: w027 HV pversion mismatch | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w028_IBSTversionMismatch` | page 0 | Gateway: w028 IBS tversion mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w029_IBSTCALversionMismatch` | page 0 | Gateway: w029 IBSTCA lversion mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w030_OCS1PversionMismatch` | page 0 | Gateway: w030 OCS1 pversion mismatch | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w031_PARKversionMismatch` | page 0 | Gateway: w031 PAR kversion mismatch | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w032_PCSversionMismatch` | page 0 | Gateway: w032 PC sversion mismatch | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w033_PCSCPU2versionMismatch` | page 0 | Gateway: w033 pcscpu2version mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w034_PMRversionMismatch` | page 0 | Gateway: w034 PM rversion mismatch | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w035_PMFversionMismatch` | page 0 | Gateway: w035 PM fversion mismatch | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w036_PTCversionMismatch` | page 0 | Gateway: w036 PT cversion mismatch | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w037_RADCversionMismatch` | page 0 | Gateway: w037 RAD cversion mismatch | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w038_RCMversionMismatch` | page 0 | Gateway: w038 RC mversion mismatch | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w039_RCMCALversionMismatch` | page 0 | Gateway: w039 RCMCA lversion mismatch | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w040_SCCMversionMismatch` | page 0 | Gateway: w040 SCC mversion mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w041_VCSECversionMismatch` | page 0 | Gateway: w041 VCSE cversion mismatch | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w042_TASversionMismatch` | page 0 | Gateway: w042 TA sversion mismatch | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w043_THSversionMismatch` | page 0 | Gateway: w043 TH sversion mismatch | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w045_VCFRONTversionMismatch` | page 0 | Gateway: w045 VCFRON tversion mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w046_VCLEFTversionMismatch` | page 0 | Gateway: w046 VCLEF tversion mismatch | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w047_VCRIGHTversionMismatch` | page 0 | Gateway: w047 VCRIGH tversion mismatch | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w048_EPAS3SversionMismatch` | page 0 | Gateway: w048 EPAS3 sversion mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w049_corruptedManifest` | page 0 | Gateway: w049 corrupted manifest | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w050_sdCardInitFailure` | page 0 | Gateway: w050 sd card init failure | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w051_sdCardFileSystemFailure` | page 0 | Gateway: w051 sd card file system failure | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w052_ifTxSpans` | page 0 | Gateway: w052 if tx spans | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w053_busSleepFailure` | page 0 | Gateway: w053 bus sleep failure | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w054_OPCRversionMismatch` | page 0 | Gateway: w054 OPC rversion mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w055_OPCFversionMismatch` | page 0 | Gateway: w055 OPC fversion mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w057_i2cFailure` | page 0 | Gateway: w057 i2c failure | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w058_rtcAlarmFailure` | page 0 | Gateway: w058 rtc alarm failure | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w059_inFactoryMode` | page 0 | Gateway: w059 in factory mode | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w060_unFused` | page 0 | Gateway: w060 un fused | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w061_bmpSleepFailure` | page 1 | Gateway: w061 bmp sleep failure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w062_bmpWatchdog` | page 1 | Gateway: w062 bmp watchdog | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w063_VEH_canFault` | page 1 | Gateway: w063 VEH can fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w064_CH_canFault` | page 1 | Gateway: w064 CH can fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w065_PARTY_canFault` | page 1 | Gateway: w065 PARTY can fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w066_exception` | page 1 | Gateway: w066 exception | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w067_tcpDebug` | page 1 | Gateway: w067 tcp debug | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w068_prodKeyMissing` | page 1 | Gateway: w068 prod key missing | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w069_diskioErr` | page 1 | Gateway: w069 diskio err | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w070_hrlDump` | page 1 | Gateway: w070 hrl dump | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w071_hrlTrigger` | page 1 | Gateway: w071 hrl trigger | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w072_updateFailure` | page 1 | Gateway: w072 update failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w073_steeringWheelReset` | page 1 | Gateway: w073 steering wheel reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w074_epas3pMIA` | page 1 | Gateway: w074 epas3p MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w075_epas3sMIA` | page 1 | Gateway: w075 epas3s MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w076_ethInterfaceReset` | page 1 | Gateway: w076 eth interface reset | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w077_bmpPmicError` | page 1 | Gateway: w077 bmp pmic error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w078_VEHbusOverloaded` | page 1 | Gateway: w078 VE hbus overloaded | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w079_PARTYbusOverloaded` | page 1 | Gateway: w079 PART ybus overloaded | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w080_CHbusOverloaded` | page 1 | Gateway: w080 c hbus overloaded | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w081_udsMessageRejected` | page 1 | Gateway: w081 uds message rejected | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w082_sdCardBSCorrupted` | page 1 | Gateway: w082 sd card BS corrupted | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w083_udsMsgDroppedByTcpStack` | page 1 | Gateway: w083 uds msg dropped by tcp stack | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w084_canFrameDropped` | page 1 | Gateway: w084 can frame dropped | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w086_ocu` | page 1 | Gateway: w086 ocu | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w087_ocuInProgress` | page 1 | Gateway: w087 ocu in progress | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w088_sdCardInvReqParallel` | page 1 | Gateway: w088 sd card inv req parallel | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w089_sdCardWatchdog` | page 1 | Gateway: w089 sd card watchdog | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w090_ocuFailed` | page 1 | Gateway: w090 ocu failed | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w091_lowStack` | page 1 | Gateway: w091 low stack | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w092_sdCardInvReqZero` | page 1 | Gateway: w092 sd card inv req zero | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w093_sdCardInvReqOverflowBase` | page 1 | Gateway: w093 sd card inv req overflow base | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w094_sdCardInvReqOverflowCount` | page 1 | Gateway: w094 sd card inv req overflow count | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w095_sdCardFull` | page 1 | Gateway: w095 sd card full | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w096_sdCardFatCorrupted` | page 1 | Gateway: w096 sd card fat corrupted | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w097_HCMLversionMismatch` | page 1 | Gateway: w097 HCM lversion mismatch | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w098_HCMRversionMismatch` | page 1 | Gateway: w098 HCM rversion mismatch | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w099_SWCversionMismatch` | page 1 | Gateway: w099 SW cversion mismatch | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w100_CBCversionMismatch` | page 1 | Gateway: w100 CB cversion mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w101_switchWatchdog` | page 1 | Gateway: w101 switch watchdog | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w103_sdCardFormatted` | page 1 | Gateway: w103 sd card formatted | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w104_sdCardDriverArgCorrupted` | page 1 | Gateway: w104 sd card driver arg corrupted | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w105_eBuckConfigured` | page 1 | Gateway: w105 e buck configured | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w106_BLEEPLEFTversionMismatch` | page 1 | Gateway: w106 BLEEPLEF tversion mismatch | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w107_BLEEPRIGHTversionMismatch` | page 1 | Gateway: w107 BLEEPRIGH tversion mismatch | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w108_BLEEPREARversionMismatch` | page 1 | Gateway: w108 BLEEPREA rversion mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w109_failedToStartUpdater` | page 1 | Gateway: w109 failed to start updater | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w110_readMdioFailed` | page 1 | Gateway: w110 read mdio failed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w111_writeMdioFailed` | page 1 | Gateway: w111 write mdio failed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w112_z4bDisabled` | page 1 | Gateway: w112 z4b disabled | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w113_unrecognizedCanMessage` | page 1 | Gateway: w113 unrecognized can message | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w114_updtRetried` | page 1 | Gateway: w114 updt retried | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w115_hrlEventFileAvail` | page 1 | Gateway: w115 hrl event file avail | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w116_switchInitFailed` | page 1 | Gateway: w116 switch init failed | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w117_unexpectedDestructiveResetStatus` | page 1 | Gateway: w117 unexpected destructive reset status | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w118_unexpectedFunctionalResetStatus` | page 1 | Gateway: w118 unexpected functional reset status | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w120_switchUnlocked` | page 1 | Gateway: w120 switch unlocked | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w122_BDY_canFault` | page 2 | Gateway: w122 BDY can fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w123_BDYbusOverloaded` | page 2 | Gateway: w123 BD ybus overloaded | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w125_switchReplayUnlocked` | page 2 | Gateway: w125 switch replay unlocked | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w127_noFilePointersAvailable` | page 2 | Gateway: w127 no file pointers available | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w129_ICRversionMismatch` | page 2 | Gateway: w129 IC rversion mismatch | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w133_adspFaultDetected` | page 2 | Gateway: w133 adsp fault detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w134_disableFeatureFailed` | page 2 | Gateway: w134 disable feature failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w135_canLogQueueFull` | page 2 | Gateway: w135 can log queue full | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w136_hrlGameModeFileAvail` | page 2 | Gateway: w136 hrl game mode file avail | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w137_lowHeap` | page 2 | Gateway: w137 low heap | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w138_sdCardEndOfLife` | page 2 | Gateway: w138 sd card end of life | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w139_CMPDversionMismatch` | page 2 | Gateway: w139 CMP dversion mismatch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w140_cancoreHeartbeat` | page 2 | Gateway: w140 cancore heartbeat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w141_teleCANETHis` | page 2 | Gateway: w141 tele CANET his | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w143_possibleCanWakeIssue` | page 2 | Gateway: w143 possible can wake issue | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w144_hrlStateMachine` | page 2 | Gateway: w144 hrl state machine | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w145_carConfigsNotWritten` | page 2 | Gateway: w145 car configs not written | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w146_performancePackageMismatch` | page 2 | Gateway: w146 performance package mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w147_updateAbortFor12v` | page 2 | Gateway: w147 update abort for12v | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w149_rtcTimeSetInPast` | page 2 | Gateway: w149 rtc time set in past | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w150_HCM3LversionMismatch` | page 2 | Gateway: w150 HCM3 lversion mismatch | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w151_HCM3RversionMismatch` | page 2 | Gateway: w151 HCM3 rversion mismatch | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w153_externalRtcAlarmFailure` | page 2 | Gateway: w153 external rtc alarm failure | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w155_PMversionMismatch` | page 2 | Gateway: w155 p mversion mismatch | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w165_USMversionMismatch` | page 2 | Gateway: w165 US mversion mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w166_nErrCanFaultVeh` | page 2 | Gateway: w166 n err can fault veh | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w167_nErrCanFaultCh` | page 2 | Gateway: w167 n err can fault ch | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w168_nErrCanFaultParty` | page 2 | Gateway: w168 n err can fault party | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w169_TPMSsoftWarnFrontLeft` | page 2 | Gateway: w169 TPM ssoft warn front left | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w170_TPMSsoftWarnFrontRight` | page 2 | Gateway: w170 TPM ssoft warn front right | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w171_TPMSsoftWarnRearLeft` | page 2 | Gateway: w171 TPM ssoft warn rear left | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w172_TPMSsoftWarnRearRight` | page 2 | Gateway: w172 TPM ssoft warn rear right | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w173_TPMShardWarnFrontLeft` | page 2 | Gateway: w173 TPM shard warn front left | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w174_TPMShardWarnFrontRight` | page 2 | Gateway: w174 TPM shard warn front right | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w175_TPMShardWarnRearLeft` | page 2 | Gateway: w175 TPM shard warn rear left | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w176_TPMShardWarnRearRight` | page 2 | Gateway: w176 TPM shard warn rear right | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w186_swrPrecaution` | page 3 | Gateway: w186 swr precaution | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w218_switchOTPIncorrect` | page 3 | Gateway: w218 switch OTP incorrect | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w219_CMPSversionMismatch` | page 3 | Gateway: w219 CMP sversion mismatch | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w223_LVBMSversionMismatch` | page 3 | Gateway: w223 LVBM sversion mismatch | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w224_sdCardUpgradeNeeded` | page 3 | Gateway: w224 sd card upgrade needed | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w225_resetOnSleepWake` | page 3 | Gateway: w225 reset on sleep wake | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w226_DISPversionMismatch` | page 3 | Gateway: w226 DIS pversion mismatch | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w227_DISPTOUCHversionMismatch` | page 3 | Gateway: w227 DISPTOUC hversion mismatch | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w228_DISPOSDversionMismatch` | page 3 | Gateway: w228 DISPOS dversion mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w229_displaySoftsetConnection` | page 3 | Gateway: w229 display softset connection | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w230_touchInterruptStorm` | page 3 | Gateway: w230 touch interrupt storm | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w244_SDCRversionMismatch` | page 4 | Gateway: w244 SDC rversion mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w245_apsNotDisabled` | page 4 | Gateway: w245 aps not disabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w246_touchcoreHeartbeat` | page 4 | Gateway: w246 touchcore heartbeat | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w255_rtc32KHzWatchdog` | page 4 | Gateway: w255 rtc32 k hz watchdog | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w260_unknownPN` | page 4 | Gateway: w260 unknown PN | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w261_adspWatchdog` | page 4 | Gateway: w261 adsp watchdog | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w262_canLogBlockDropped` | page 4 | Gateway: w262 can log block dropped | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w263_hrlUdpFileAvail` | page 4 | Gateway: w263 hrl udp file avail | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w264_hrlPseudoFileAvail` | page 4 | Gateway: w264 hrl pseudo file avail | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w265_optionFlagsError` | page 4 | Gateway: w265 option flags error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w266_dpp1MIA` | page 4 | Gateway: w266 dpp1 MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w267_dpp2MIA` | page 4 | Gateway: w267 dpp2 MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w268_stoMIA` | page 4 | Gateway: w268 sto MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w273_BLEEPREARLEFTversionMismatch` | page 4 | Gateway: w273 BLEEPREARLEF tversion mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w274_BLEEPREARRIGHTversionMismatch` | page 4 | Gateway: w274 BLEEPREARRIGH tversion mismatch | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w275_VDDCORE_DrMOS_Fault` | page 4 | Gateway: w275 VDDCORE dr MOS fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w276_VDDSOC_DrMOS_Fault` | page 4 | Gateway: w276 VDDSOC dr MOS fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w277_NonRevCDrMOSMitigationFailed` | page 4 | Gateway: w277 non rev c dr MOS mitigation failed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w278_ethSwitchCongested` | page 4 | Gateway: w278 eth switch congested | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w279_adspRepeatedWatchdog` | page 4 | Gateway: w279 adsp repeated watchdog | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w280_hrlFrameDropped` | page 4 | Gateway: w280 hrl frame dropped | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w281_likelyMissedPoke` | page 4 | Gateway: w281 likely missed poke | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w282_tcuPhyConfigurationFailed` | page 4 | Gateway: w282 tcu phy configuration failed | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w309_VCUSBversionMismatch` | page 5 | Gateway: w309 VCUS bversion mismatch | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w311_canLogQueueFullBeforeFsInit` | page 5 | Gateway: w311 can log queue full before fs init | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w312_hrlFileIncomplete` | page 5 | Gateway: w312 hrl file incomplete | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w313_OSDActive` | page 5 | Gateway: w313 OSD active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w314_canLogBlockWriteErr` | page 5 | Gateway: w314 can log block write err | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w316_sdCardChkdskRepair` | page 5 | Gateway: w316 sd card chkdsk repair | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w317_sdCardChkdskRepairFailed` | page 5 | Gateway: w317 sd card chkdsk repair failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w322_gestureUnrecognizedFromMoving` | page 5 | Gateway: w322 gesture unrecognized from moving | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w323_gestureStartOutOfStrip` | page 5 | Gateway: w323 gesture start out of strip | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w328_smartShiftDisabled` | page 5 | Gateway: w328 smart shift disabled | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w329_FOHMversionMismatch` | page 5 | Gateway: w329 FOH mversion mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w330_SWSLversionMismatch` | page 5 | Gateway: w330 SWS lversion mismatch | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w331_SWSRversionMismatch` | page 5 | Gateway: w331 SWS rversion mismatch | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w332_unknownDisplayPN` | page 5 | Gateway: w332 unknown display PN | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w334_hrlFolderSpaceLow` | page 5 | Gateway: w334 hrl folder space low | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w336_possibleCanTxIssue` | page 5 | Gateway: w336 possible can tx issue | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w342_VCBLDCPPversionMismatch` | page 5 | Gateway: w342 VCBLDCP pversion mismatch | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w348_VCBLDCFversionMismatch` | page 5 | Gateway: w348 VCBLDC fversion mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w349_VCBLDCPBversionMismatch` | page 5 | Gateway: w349 VCBLDCP bversion mismatch | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w350_mOSDCrcCheck` | page 5 | Gateway: w350 m OSD crc check | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w351_sOSDCrcCheck` | page 5 | Gateway: w351 s OSD crc check | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w352_mASILStatusCheck` | page 5 | Gateway: w352 m ASIL status check | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w353_sASILStatusCheck` | page 5 | Gateway: w353 s ASIL status check | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w354_EPASTPversionMismatch` | page 5 | Gateway: w354 EPAST pversion mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w355_EPASTSversionMismatch` | page 5 | Gateway: w355 EPAST sversion mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w356_touchGPIOStatusCheck` | page 5 | Gateway: w356 touch GPIO status check | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w358_RGBIPFLversionMismatch` | page 5 | Gateway: w358 RGBIPF lversion mismatch | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w359_RGBIPFRversionMismatch` | page 5 | Gateway: w359 RGBIPF rversion mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w360_RGBDOORFLversionMismatch` | page 5 | Gateway: w360 RGBDOORF lversion mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w361_RGBDOORRLversionMismatch` | page 6 | Gateway: w361 RGBDOORR lversion mismatch | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w362_RGBDOORFRversionMismatch` | page 6 | Gateway: w362 RGBDOORF rversion mismatch | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w363_RGBDOORRRversionMismatch` | page 6 | Gateway: w363 RGBDOORR rversion mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w364_BLEEPCRADLEversionMismatch` | page 6 | Gateway: w364 BLEEPCRADL eversion mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w366_uiGearRequestMismatch` | page 6 | Gateway: w366 ui gear request mismatch | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w376_blFailedToExecBootImg` | page 6 | Gateway: w376 bl failed to exec boot img | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w380_DPBversionMismatch` | page 6 | Gateway: w380 DP bversion mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w381_DPBCALversionMismatch` | page 6 | Gateway: w381 DPBCA lversion mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w382_IDBversionMismatch` | page 6 | Gateway: w382 ID bversion mismatch | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w383_IDB1versionMismatch` | page 6 | Gateway: w383 idb1version mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w384_IDBCALversionMismatch` | page 6 | Gateway: w384 IDBCA lversion mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w385_RCUversionMismatch` | page 6 | Gateway: w385 RC uversion mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w386_RCUCALversionMismatch` | page 6 | Gateway: w386 RCUCA lversion mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w387_externalRtcReadFailure` | page 6 | Gateway: w387 external rtc read failure | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w388_adspWatchdogSkipped` | page 6 | Gateway: w388 adsp watchdog skipped | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w389_rcmEventDetected` | page 6 | Gateway: w389 rcm event detected | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w391_adspMacAddrCheckFailed` | page 6 | Gateway: w391 adsp mac addr check failed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w393_osdSramCrcMismatch` | page 6 | Gateway: w393 osd sram crc mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w395_lwipIcmpError` | page 6 | Gateway: w395 lwip icmp error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w396_alreadyInReverse` | page 6 | Gateway: w396 already in reverse | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w397_alreadyInDrive` | page 6 | Gateway: w397 already in drive | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w398_awakeForExtendedTime` | page 6 | Gateway: w398 awake for extended time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w399_ethIfRxTcpipQueueDrop` | page 6 | Gateway: w399 eth if rx tcpip queue drop | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w400_ethlSwitchOTPIncorrect` | page 6 | Gateway: w400 ethl switch OTP incorrect | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w409_unexpectedResetCause` | page 6 | Gateway: w409 unexpected reset cause | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w410_unexpectedResetCause2` | page 6 | Gateway: w410 unexpected reset cause2 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_w414_socHeldInReset` | page 6 | Gateway: w414 soc held in reset | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`GTW_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (57 signals), page 1 (57 signals), page 2 (36 signals), page 3 (11 signals), page 4 (23 signals), page 5 (29 signals), page 6 (27 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
