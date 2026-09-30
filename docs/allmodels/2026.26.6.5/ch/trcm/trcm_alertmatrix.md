---
layout: default
title: "TRCM_alertMatrix (0x372) — TRCM ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "TRCM ECU message: alert matrix. Tesla Model 3 / Model Y CAN bus message TRCM_alertMatrix (0x372) of TRCM ECU, firmware 2026.26.6.5, 421 signals (TRCM_matrixIndex, TRCM_a001_airbagsDisabled, TRCM_a002_systemDisabled, TRCM_a003_SWAssertion and 417 more). Bit layout, scaling, units and value tables."
---

# TRCM_alertMatrix (0x372) — TRCM ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

TRCM ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 421 signals of TRCM_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TRCM_alertMatrix` |
| CAN id | 0x372 (882) |
| ECU | [TRCM ECU](../../trcm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TRCM |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 421 |

## Signals of TRCM_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `TRCM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TRCM_matrixIndex` | selector | TRCM ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | plausible |
| `TRCM_a001_airbagsDisabled` | page 0 | TRCM ECU: a001 airbags disabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a002_systemDisabled` | page 0 | TRCM ECU: a002 system disabled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a003_SWAssertion` | page 0 | TRCM ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a004_internalFailure` | page 0 | TRCM ECU: a004 internal failure | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a005_CANTXError` | page 0 | TRCM ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a006_CANTX_cyclicError` | page 0 | TRCM ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a007_chassisChecksumError` | page 0 | TRCM ECU: a007 chassis checksum error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a008_chassisCounterError` | page 0 | TRCM ECU: a008 chassis counter error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a009_partyChecksumError` | page 0 | TRCM ECU: a009 party checksum error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a010_partyCounterError` | page 0 | TRCM ECU: a010 party counter error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a011_edrDataLocked` | page 0 | TRCM ECU: a011 edr data locked | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a012_asm5TemperatureOutsideSignalRange` | page 0 | TRCM ECU: a012 asm5 temperature outside signal range | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a013_AlertManagerFault` | page 0 | TRCM ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a014_asm3TemperatureOutsideSignalRange` | page 0 | TRCM ECU: a014 asm3 temperature outside signal range | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a015_NVMMError` | page 0 | TRCM ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a016_NVMMRecordError` | page 0 | TRCM ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a017_asm5TemperatureOutsideOperatingRange` | page 0 | TRCM ECU: a017 asm5 temperature outside operating range | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a018_asm3TemperatureOutsideOperatingRange` | page 0 | TRCM ECU: a018 asm3 temperature outside operating range | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a019_Task500usError` | page 0 | TRCM ECU: a019 task500us error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a020_asm3ComStatusError` | page 0 | TRCM ECU: a020 asm3 com status error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a021_TaskSchedulerError` | page 0 | TRCM ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a022_TaskInitError` | page 0 | TRCM ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a023_asm3ArsStatusXError` | page 0 | TRCM ECU: a023 asm3 ars status x error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a024_asm3AccStatusError` | page 0 | TRCM ECU: a024 asm3 acc status error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a025_CHCANBusFaults` | page 0 | TRCM ECU: a025 CHCAN bus faults | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a026_airbagAsicDiagnosticFault` | page 0 | TRCM ECU: a026 airbag asic diagnostic fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a027_airbagAsicDeploymentDiagnosticFault` | page 0 | TRCM ECU: a027 airbag asic deployment diagnostic fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a028_chassisLengthError` | page 0 | TRCM ECU: a028 chassis length error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a030_ECULogUploadRequest` | page 0 | TRCM ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a031_UDSActive` | page 0 | TRCM ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a032_ScrollCreated` | page 0 | TRCM ECU: a032 scroll created | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a033_HercLogCreated` | page 0 | TRCM ECU: a033 herc log created | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a034_apClipTrigger` | page 0 | TRCM ECU: a034 ap clip trigger | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a035_hvDisconnectCommanded` | page 0 | TRCM ECU: a035 hv disconnect commanded | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a036_crashDetected` | page 0 | TRCM ECU: a036 crash detected | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a037_nearDeploy` | page 0 | TRCM ECU: a037 near deploy | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a038_ens1Degraded` | page 0 | TRCM ECU: a038 ens1 degraded | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a039_ens2Degraded` | page 0 | TRCM ECU: a039 ens2 degraded | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a040_task500usOverrunDebug` | page 0 | TRCM ECU: a040 task500us overrun debug | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a041_HighCPULoad` | page 0 | TRCM ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a042_HighStackUsage` | page 0 | TRCM ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a043_Task1msError` | page 0 | TRCM ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a044_Task10msError` | page 0 | TRCM ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a045_Task100msError` | page 0 | TRCM ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a046_Task1000msError` | page 0 | TRCM ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a047_vinNotLearned` | page 0 | TRCM ECU: a047 vin not learned | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a048_vinMismatch` | page 0 | TRCM ECU: a048 vin mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a049_nvmDebugInfo` | page 0 | TRCM ECU: a049 nvm debug info | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a050_partyLengthError` | page 0 | TRCM ECU: a050 party length error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a051_systemSelfTestTimeout` | page 0 | TRCM ECU: a051 system self test timeout | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a057_HVP_MIA` | page 0 | TRCM ECU: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a058_inputRHighSyncDebug` | page 0 | TRCM ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a059_inputResistanceHigh` | page 0 | TRCM ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a060_engineeringBuild` | page 0 | TRCM ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a061_XCPConnected` | page 1 | TRCM ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a062_XCPWasConnected` | page 1 | TRCM ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a063_SwitchFault` | page 1 | TRCM ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a064_busSleepReqTimeout` | page 1 | TRCM ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a065_vSafingFetUnderVoltage` | page 1 | TRCM ECU: a065 v safing fet under voltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a066_leftPowerIssue` | page 1 | TRCM ECU: a066 left power issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a067_rightPowerIssue` | page 1 | TRCM ECU: a067 right power issue | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a068_vBusCUnderVoltage` | page 1 | TRCM ECU: a068 v bus c under voltage | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a069_swAppBoot` | page 1 | TRCM ECU: a069 sw app boot | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a070_asm3StatusError` | page 1 | TRCM ECU: a070 asm3 status error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a071_asm3DeviceFaulted` | page 1 | TRCM ECU: a071 asm3 device faulted | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a072_ais2120StatusError` | page 1 | TRCM ECU: a072 ais2120 status error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a073_ais2120DeviceFaulted` | page 1 | TRCM ECU: a073 ais2120 device faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a074_ais2120SelfTestXPositiveFailed` | page 1 | TRCM ECU: a074 ais2120 self test x positive failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a075_ais2120SelfTestXNegativeFailed` | page 1 | TRCM ECU: a075 ais2120 self test x negative failed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a076_ais2120SelfTestYPositiveFailed` | page 1 | TRCM ECU: a076 ais2120 self test y positive failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a077_ais2120SelfTestYNegativeFailed` | page 1 | TRCM ECU: a077 ais2120 self test y negative failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a078_imuSensorSignalMonitor` | page 1 | TRCM ECU: a078 imu sensor signal monitor | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a081_powerLossDetected` | page 1 | TRCM ECU: a081 power loss detected | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a082_VCRIGHT_IPC_MIA` | page 1 | TRCM ECU: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a083_VCLEFT_IPC_MIA` | page 1 | TRCM ECU: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a084_TPMS_MIA` | page 1 | TRCM ECU: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a085_CCCM_MIA` | page 1 | TRCM ECU: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a086_VCBATT_MIA` | page 1 | TRCM ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a087_DIREL_MIA` | page 1 | TRCM ECU: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a088_DIRER_MIA` | page 1 | TRCM ECU: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a089_IBST_MIA` | page 1 | TRCM ECU: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a090_APS_MIA` | page 1 | TRCM ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a091_CMPD_MIA` | page 1 | TRCM ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a092_VCSEATD_MIA` | page 1 | TRCM ECU: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a093_VCSEATP_MIA` | page 1 | TRCM ECU: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a094_EPAS3P_MIA` | page 1 | TRCM ECU: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a095_CHG_MIA` | page 1 | TRCM ECU: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a096_OCS1P_MIA` | page 1 | TRCM ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a097_CMP_MIA` | page 1 | TRCM ECU: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a098_DIR_MIA` | page 1 | TRCM ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a099_PARK_MIA` | page 1 | TRCM ECU: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a100_CANbus_MIA` | page 1 | TRCM ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a101_PM_MIA` | page 1 | TRCM ECU: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a102_PTC_MIA` | page 1 | TRCM ECU: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a103_CP_MIA` | page 1 | TRCM ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a104_DAS_MIA` | page 1 | TRCM ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a105_TAS_MIA` | page 1 | TRCM ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a106_PCS_MIA` | page 1 | TRCM ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a107_BMS_MIA` | page 1 | TRCM ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a108_DIF_MIA` | page 1 | TRCM ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a109_RCM_MIA` | page 1 | TRCM ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a110_GTW_MIA` | page 1 | TRCM ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a111_EPBR_MIA` | page 1 | TRCM ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a112_EPBL_MIA` | page 1 | TRCM ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a113_UI_MIA` | page 1 | TRCM ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a114_ESP_MIA` | page 1 | TRCM ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a115_VCSEC_MIA` | page 1 | TRCM ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a116_VCRIGHT_MIA` | page 1 | TRCM ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a117_VCLEFT_MIA` | page 1 | TRCM ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a118_VCFRONT_MIA` | page 1 | TRCM ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a119_SCCM_MIA` | page 1 | TRCM ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a120_DI_DRIVE_MIA` | page 1 | TRCM ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a121_buckleStatusFrontLeftSignalNotOkay` | page 2 | TRCM ECU: a121 buckle status front left signal not okay | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a122_buckleStatusFrontRightSignalNotOkay` | page 2 | TRCM ECU: a122 buckle status front right signal not okay | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a123_buckleStatusRearLeftSignalNotOkay` | page 2 | TRCM ECU: a123 buckle status rear left signal not okay | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a124_buckleStatusRearRightSignalNotOkay` | page 2 | TRCM ECU: a124 buckle status rear right signal not okay | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a125_occupantClassificationSignalNotOkay` | page 2 | TRCM ECU: a125 occupant classification signal not okay | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a126_seatTrackPositionLeftSignalNotOkay` | page 2 | TRCM ECU: a126 seat track position left signal not okay | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a127_seatTrackPositionRightSignalNotOkay` | page 2 | TRCM ECU: a127 seat track position right signal not okay | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a135_asm5StatusError` | page 2 | TRCM ECU: a135 asm5 status error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a136_asm5DeviceFaulted` | page 2 | TRCM ECU: a136 asm5 device faulted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a137_ext1AsicSnoopTestFailed` | page 2 | TRCM ECU: a137 ext1 asic snoop test failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a138_ext2AsicSnoopTestFailed` | page 2 | TRCM ECU: a138 ext2 asic snoop test failed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a145_frontCenterAccelReportedError` | page 2 | TRCM ECU: a145 front center accel reported error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a146_frontCenterAccelGeneralIssue` | page 2 | TRCM ECU: a146 front center accel general issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a147_frontCenterAccelElectricalIssue` | page 2 | TRCM ECU: a147 front center accel electrical issue | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a148_frontCenterAccelConfigError` | page 2 | TRCM ECU: a148 front center accel config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a149_frontCenterAccelSignalMonitor` | page 2 | TRCM ECU: a149 front center accel signal monitor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a150_frontLeftAccelReportedError` | page 2 | TRCM ECU: a150 front left accel reported error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a151_frontLeftAccelGeneralIssue` | page 2 | TRCM ECU: a151 front left accel general issue | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a152_frontLeftAccelElectricalIssue` | page 2 | TRCM ECU: a152 front left accel electrical issue | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a153_frontLeftAccelConfigError` | page 2 | TRCM ECU: a153 front left accel config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a154_frontLeftAccelSignalMonitor` | page 2 | TRCM ECU: a154 front left accel signal monitor | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a155_frontLeftDoorPressureReportedError` | page 2 | TRCM ECU: a155 front left door pressure reported error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a156_frontLeftDoorPressureGeneralIssue` | page 2 | TRCM ECU: a156 front left door pressure general issue | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a157_frontLeftDoorPressureElectricalIssue` | page 2 | TRCM ECU: a157 front left door pressure electrical issue | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a158_frontLeftDoorPressureConfigError` | page 2 | TRCM ECU: a158 front left door pressure config error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a159_frontLeftDoorPressureSignalMonitor` | page 2 | TRCM ECU: a159 front left door pressure signal monitor | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a160_frontRightAccelReportedError` | page 2 | TRCM ECU: a160 front right accel reported error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a161_frontRightAccelGeneralIssue` | page 2 | TRCM ECU: a161 front right accel general issue | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a162_frontRightAccelElectricalIssue` | page 2 | TRCM ECU: a162 front right accel electrical issue | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a163_frontRightAccelConfigError` | page 2 | TRCM ECU: a163 front right accel config error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a164_frontRightAccelSignalMonitor` | page 2 | TRCM ECU: a164 front right accel signal monitor | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a165_frontRightDoorPressureReportedError` | page 2 | TRCM ECU: a165 front right door pressure reported error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a166_frontRightDoorPressureGeneralIssue` | page 2 | TRCM ECU: a166 front right door pressure general issue | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a167_frontRightDoorPressureElectricalIssue` | page 2 | TRCM ECU: a167 front right door pressure electrical issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a168_frontRightDoorPressureConfigError` | page 2 | TRCM ECU: a168 front right door pressure config error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a169_frontRightDoorPressureSignalMonitor` | page 2 | TRCM ECU: a169 front right door pressure signal monitor | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a170_leftBPillarAccelReportedError` | page 2 | TRCM ECU: a170 left b pillar accel reported error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a171_leftBPillarAccelGeneralIssue` | page 2 | TRCM ECU: a171 left b pillar accel general issue | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a172_leftBPillarAccelElectricalIssue` | page 2 | TRCM ECU: a172 left b pillar accel electrical issue | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a173_leftBPillarAccelConfigError` | page 2 | TRCM ECU: a173 left b pillar accel config error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a174_leftBPillarAccelSignalMonitor` | page 2 | TRCM ECU: a174 left b pillar accel signal monitor | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a175_leftCPillarAccelReportedError` | page 2 | TRCM ECU: a175 left c pillar accel reported error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a176_leftCPillarAccelGeneralIssue` | page 2 | TRCM ECU: a176 left c pillar accel general issue | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a177_leftCPillarAccelElectricalIssue` | page 2 | TRCM ECU: a177 left c pillar accel electrical issue | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a178_leftCPillarAccelConfigError` | page 2 | TRCM ECU: a178 left c pillar accel config error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a179_leftCPillarAccelSignalMonitor` | page 2 | TRCM ECU: a179 left c pillar accel signal monitor | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a190_rearLeftDoorPressureReportedError` | page 3 | TRCM ECU: a190 rear left door pressure reported error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a191_rearLeftDoorPressureGeneralIssue` | page 3 | TRCM ECU: a191 rear left door pressure general issue | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a192_rearLeftDoorPressureElectricalIssue` | page 3 | TRCM ECU: a192 rear left door pressure electrical issue | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a193_rearLeftDoorPressureConfigError` | page 3 | TRCM ECU: a193 rear left door pressure config error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a194_rearLeftDoorPressureSignalMonitor` | page 3 | TRCM ECU: a194 rear left door pressure signal monitor | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a195_rearRightDoorPressureReportedError` | page 3 | TRCM ECU: a195 rear right door pressure reported error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a196_rearRightDoorPressureGeneralIssue` | page 3 | TRCM ECU: a196 rear right door pressure general issue | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a197_rearRightDoorPressureElectricalIssue` | page 3 | TRCM ECU: a197 rear right door pressure electrical issue | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a198_rearRightDoorPressureConfigError` | page 3 | TRCM ECU: a198 rear right door pressure config error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a199_rearRightDoorPressureSignalMonitor` | page 3 | TRCM ECU: a199 rear right door pressure signal monitor | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a200_rightBPillarAccelReportedError` | page 3 | TRCM ECU: a200 right b pillar accel reported error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a201_rightBPillarAccelGeneralIssue` | page 3 | TRCM ECU: a201 right b pillar accel general issue | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a202_rightBPillarAccelElectricalIssue` | page 3 | TRCM ECU: a202 right b pillar accel electrical issue | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a203_rightBPillarAccelConfigError` | page 3 | TRCM ECU: a203 right b pillar accel config error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a204_rightBPillarAccelSignalMonitor` | page 3 | TRCM ECU: a204 right b pillar accel signal monitor | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a205_rightCPillarAccelReportedError` | page 3 | TRCM ECU: a205 right c pillar accel reported error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a206_rightCPillarAccelGeneralIssue` | page 3 | TRCM ECU: a206 right c pillar accel general issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a207_rightCPillarAccelElectricalIssue` | page 3 | TRCM ECU: a207 right c pillar accel electrical issue | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a208_rightCPillarAccelConfigError` | page 3 | TRCM ECU: a208 right c pillar accel config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a209_rightCPillarAccelSignalMonitor` | page 3 | TRCM ECU: a209 right c pillar accel signal monitor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a272_asm5ComStatusError` | page 4 | TRCM ECU: a272 asm5 com status error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a273_asm5ArsStatusXError` | page 4 | TRCM ECU: a273 asm5 ars status x error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a274_asm5ArsStatusZError` | page 4 | TRCM ECU: a274 asm5 ars status z error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a275_asm5AccStatusError` | page 4 | TRCM ECU: a275 asm5 acc status error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a276_watchdogStatus` | page 4 | TRCM ECU: a276 watchdog status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a278_safingEngine0Armed` | page 4 | TRCM ECU: a278 safing engine0 armed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a279_safingEngine1Armed` | page 4 | TRCM ECU: a279 safing engine1 armed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a280_safingEngine2Armed` | page 4 | TRCM ECU: a280 safing engine2 armed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a281_safingEngine3Armed` | page 4 | TRCM ECU: a281 safing engine3 armed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a282_safingEngine4Armed` | page 4 | TRCM ECU: a282 safing engine4 armed | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a283_safingEngine5Armed` | page 4 | TRCM ECU: a283 safing engine5 armed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a284_safingEngine6Armed` | page 4 | TRCM ECU: a284 safing engine6 armed | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a285_safingEngine7Armed` | page 4 | TRCM ECU: a285 safing engine7 armed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a286_safingEngine8Armed` | page 4 | TRCM ECU: a286 safing engine8 armed | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a287_safingEngine9Armed` | page 4 | TRCM ECU: a287 safing engine9 armed | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a288_safingEngine10Armed` | page 4 | TRCM ECU: a288 safing engine10 armed | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a289_safingEngine11Armed` | page 4 | TRCM ECU: a289 safing engine11 armed | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a290_safingEngine12Armed` | page 4 | TRCM ECU: a290 safing engine12 armed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a291_safingEngine13Armed` | page 4 | TRCM ECU: a291 safing engine13 armed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a292_safingEngine14Armed` | page 4 | TRCM ECU: a292 safing engine14 armed | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a293_safingEngine15Armed` | page 4 | TRCM ECU: a293 safing engine15 armed | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a294_safingEngine16Armed` | page 4 | TRCM ECU: a294 safing engine16 armed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a295_safingEngine17Armed` | page 4 | TRCM ECU: a295 safing engine17 armed | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a296_safingEngine18Armed` | page 4 | TRCM ECU: a296 safing engine18 armed | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a297_safingEngine19Armed` | page 4 | TRCM ECU: a297 safing engine19 armed | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a298_safingEngine20Armed` | page 4 | TRCM ECU: a298 safing engine20 armed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a299_safingEngine21Armed` | page 4 | TRCM ECU: a299 safing engine21 armed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a300_driverAirbagStage1Suppressed` | page 4 | TRCM ECU: a300 driver airbag stage1 suppressed | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a301_passengerAirbagStage1Suppressed` | page 5 | TRCM ECU: a301 passenger airbag stage1 suppressed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a302_driverAirbagStage2Suppressed` | page 5 | TRCM ECU: a302 driver airbag stage2 suppressed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a303_driverAirbagActiveVentSuppressed` | page 5 | TRCM ECU: a303 driver airbag active vent suppressed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a304_passengerAirbagStage2Suppressed` | page 5 | TRCM ECU: a304 passenger airbag stage2 suppressed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a305_passengerAirbagActiveVentSuppressed` | page 5 | TRCM ECU: a305 passenger airbag active vent suppressed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a306_inboardSeatAirbagSuppressed` | page 5 | TRCM ECU: a306 inboard seat airbag suppressed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a308_kneeAirbagLeftSuppressed` | page 5 | TRCM ECU: a308 knee airbag left suppressed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a309_kneeAirbagRightSuppressed` | page 5 | TRCM ECU: a309 knee airbag right suppressed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a310_curtainAirbagLeftSuppressed` | page 5 | TRCM ECU: a310 curtain airbag left suppressed | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a311_curtainAirbagRightSuppressed` | page 5 | TRCM ECU: a311 curtain airbag right suppressed | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a312_seatbeltLoadLimiterFrontLeftSuppressed` | page 5 | TRCM ECU: a312 seatbelt load limiter front left suppressed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a313_seatbeltLoadLimiterFrontRightSuppressed` | page 5 | TRCM ECU: a313 seatbelt load limiter front right suppressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a314_seatbeltShoulderPretensionerFrontLeftSuppressed` | page 5 | TRCM ECU: a314 seatbelt shoulder pretensioner front left suppressed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a315_seatbeltShoulderPretensionerFrontRightSuppressed` | page 5 | TRCM ECU: a315 seatbelt shoulder pretensioner front right suppressed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a316_seatbeltLapPretensionerFrontLeftSuppressed` | page 5 | TRCM ECU: a316 seatbelt lap pretensioner front left suppressed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a317_seatbeltLapPretensionerFrontRightSuppressed` | page 5 | TRCM ECU: a317 seatbelt lap pretensioner front right suppressed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a318_outboardSeatAirbagLeftSuppressed` | page 5 | TRCM ECU: a318 outboard seat airbag left suppressed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a319_outboardSeatAirbagRightSuppressed` | page 5 | TRCM ECU: a319 outboard seat airbag right suppressed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a320_hoodLifterLeftSuppressed` | page 5 | TRCM ECU: a320 hood lifter left suppressed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a321_hoodLifterRightSuppressed` | page 5 | TRCM ECU: a321 hood lifter right suppressed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a322_seatbeltShoulderPretensionerRearLeftSuppressed` | page 5 | TRCM ECU: a322 seatbelt shoulder pretensioner rear left suppressed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a323_seatbeltShoulderPretensionerRearRightSuppressed` | page 5 | TRCM ECU: a323 seatbelt shoulder pretensioner rear right suppressed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_driverAirbagStage1Deployed` | page 5 | TRCM ECU: a332 driver airbag stage1 deployed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a333_passengerAirbagStage1Deployed` | page 5 | TRCM ECU: a333 passenger airbag stage1 deployed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a334_driverAirbagStage2Deployed` | page 5 | TRCM ECU: a334 driver airbag stage2 deployed | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a335_driverAirbagActiveVentDeployed` | page 5 | TRCM ECU: a335 driver airbag active vent deployed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a336_passengerAirbagStage2Deployed` | page 5 | TRCM ECU: a336 passenger airbag stage2 deployed | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a337_passengerAirbagActiveVentDeployed` | page 5 | TRCM ECU: a337 passenger airbag active vent deployed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a338_inboardSeatAirbagDeployed` | page 5 | TRCM ECU: a338 inboard seat airbag deployed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a340_kneeAirbagLeftDeployed` | page 5 | TRCM ECU: a340 knee airbag left deployed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a341_kneeAirbagRightDeployed` | page 5 | TRCM ECU: a341 knee airbag right deployed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a342_curtainAirbagLeftDeployed` | page 5 | TRCM ECU: a342 curtain airbag left deployed | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a343_curtainAirbagRightDeployed` | page 5 | TRCM ECU: a343 curtain airbag right deployed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a344_seatbeltLoadLimiterFrontLeftDeployed` | page 5 | TRCM ECU: a344 seatbelt load limiter front left deployed | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a345_seatbeltLoadLimiterFrontRightDeployed` | page 5 | TRCM ECU: a345 seatbelt load limiter front right deployed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a346_seatbeltShoulderPretensionerFrontLeftDeployed` | page 5 | TRCM ECU: a346 seatbelt shoulder pretensioner front left deployed | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a347_seatbeltShoulderPretensionerFrontRightDeployed` | page 5 | TRCM ECU: a347 seatbelt shoulder pretensioner front right deployed | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a348_seatbeltLapPretensionerFrontLeftDeployed` | page 5 | TRCM ECU: a348 seatbelt lap pretensioner front left deployed | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a349_seatbeltLapPretensionerFrontRightDeployed` | page 5 | TRCM ECU: a349 seatbelt lap pretensioner front right deployed | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a350_outboardSeatAirbagLeftDeployed` | page 5 | TRCM ECU: a350 outboard seat airbag left deployed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a351_outboardSeatAirbagRightDeployed` | page 5 | TRCM ECU: a351 outboard seat airbag right deployed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a352_hoodLifterLeftDeployed` | page 5 | TRCM ECU: a352 hood lifter left deployed | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a353_hoodLifterRightDeployed` | page 5 | TRCM ECU: a353 hood lifter right deployed | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a354_seatbeltShoulderPretensionerRearLeftDeployed` | page 5 | TRCM ECU: a354 seatbelt shoulder pretensioner rear left deployed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a355_seatbeltShoulderPretensionerRearRightDeployed` | page 5 | TRCM ECU: a355 seatbelt shoulder pretensioner rear right deployed | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a364_safingEngine0NoValidData` | page 6 | TRCM ECU: a364 safing engine0 no valid data | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a365_safingEngine1NoValidData` | page 6 | TRCM ECU: a365 safing engine1 no valid data | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a366_safingEngine2NoValidData` | page 6 | TRCM ECU: a366 safing engine2 no valid data | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a367_safingEngine3NoValidData` | page 6 | TRCM ECU: a367 safing engine3 no valid data | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a368_safingEngine4NoValidData` | page 6 | TRCM ECU: a368 safing engine4 no valid data | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a369_safingEngine5NoValidData` | page 6 | TRCM ECU: a369 safing engine5 no valid data | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a370_safingEngine6NoValidData` | page 6 | TRCM ECU: a370 safing engine6 no valid data | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a371_safingEngine7NoValidData` | page 6 | TRCM ECU: a371 safing engine7 no valid data | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a372_safingEngine8NoValidData` | page 6 | TRCM ECU: a372 safing engine8 no valid data | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a373_safingEngine9NoValidData` | page 6 | TRCM ECU: a373 safing engine9 no valid data | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a374_safingEngine10NoValidData` | page 6 | TRCM ECU: a374 safing engine10 no valid data | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a375_safingEngine11NoValidData` | page 6 | TRCM ECU: a375 safing engine11 no valid data | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a376_safingEngine12NoValidData` | page 6 | TRCM ECU: a376 safing engine12 no valid data | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a377_safingEngine13NoValidData` | page 6 | TRCM ECU: a377 safing engine13 no valid data | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a378_safingEngine14NoValidData` | page 6 | TRCM ECU: a378 safing engine14 no valid data | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a379_safingEngine15NoValidData` | page 6 | TRCM ECU: a379 safing engine15 no valid data | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a380_safingEngine16NoValidData` | page 6 | TRCM ECU: a380 safing engine16 no valid data | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a381_safingEngine17NoValidData` | page 6 | TRCM ECU: a381 safing engine17 no valid data | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a382_safingEngine18NoValidData` | page 6 | TRCM ECU: a382 safing engine18 no valid data | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a383_safingEngine19NoValidData` | page 6 | TRCM ECU: a383 safing engine19 no valid data | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a384_safingEngine20NoValidData` | page 6 | TRCM ECU: a384 safing engine20 no valid data | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a385_safingEngine21NoValidData` | page 6 | TRCM ECU: a385 safing engine21 no valid data | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a387_primaryAsicResetSource` | page 6 | TRCM ECU: a387 primary asic reset source | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a388_cpuLoadHigh` | page 6 | TRCM ECU: a388 cpu load high | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a389_asicPwrStatusError` | page 6 | TRCM ECU: a389 asic pwr status error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a390_systemAsicClockOrOperatingStateError` | page 6 | TRCM ECU: a390 system asic clock or operating state error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a391_extAsic1ClockOrOperatingStateError` | page 6 | TRCM ECU: a391 ext asic1 clock or operating state error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a392_extAsic2ClockOrOperatingStateError` | page 6 | TRCM ECU: a392 ext asic2 clock or operating state error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a393_depAdcConvertRatioError` | page 6 | TRCM ECU: a393 dep adc convert ratio error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a394_gspiGlobalStatusWordError` | page 6 | TRCM ECU: a394 gspi global status word error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a395_imuUncalibrated` | page 6 | TRCM ECU: a395 imu uncalibrated | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a396_spiCommunicationProgramError` | page 6 | TRCM ECU: a396 spi communication program error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a397_safingMonitorError` | page 6 | TRCM ECU: a397 safing monitor error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a398_asicNvmReprogrammed` | page 6 | TRCM ECU: a398 asic nvm reprogrammed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a399_imuCalibrationComplete` | page 6 | TRCM ECU: a399 imu calibration complete | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_driverAirbagStage1Issue` | page 6 | TRCM ECU: a400 driver airbag stage1 issue | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_passengerAirbagStage1Issue` | page 6 | TRCM ECU: a401 passenger airbag stage1 issue | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_driverAirbagStage2Issue` | page 6 | TRCM ECU: a402 driver airbag stage2 issue | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_driverAirbagActiveVentIssue` | page 6 | TRCM ECU: a403 driver airbag active vent issue | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_passengerAirbagStage2Issue` | page 6 | TRCM ECU: a404 passenger airbag stage2 issue | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_passengerAirbagActiveVentIssue` | page 6 | TRCM ECU: a405 passenger airbag active vent issue | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_inboardSeatAirbagIssue` | page 6 | TRCM ECU: a406 inboard seat airbag issue | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_kneeAirbagLeftIssue` | page 6 | TRCM ECU: a408 knee airbag left issue | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_kneeAirbagRightIssue` | page 6 | TRCM ECU: a409 knee airbag right issue | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_curtainAirbagLeftIssue` | page 6 | TRCM ECU: a410 curtain airbag left issue | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_curtainAirbagRightIssue` | page 6 | TRCM ECU: a411 curtain airbag right issue | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_seatbeltLoadLimiterFrontLeftIssue` | page 6 | TRCM ECU: a412 seatbelt load limiter front left issue | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_seatbeltLoadLimiterFrontRightIssue` | page 6 | TRCM ECU: a413 seatbelt load limiter front right issue | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_seatbeltShoulderPretensionerFrontLeftIssue` | page 6 | TRCM ECU: a414 seatbelt shoulder pretensioner front left issue | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_seatbeltShoulderPretensionerFrontRightIssue` | page 6 | TRCM ECU: a415 seatbelt shoulder pretensioner front right issue | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_seatbeltLapPretensionerFrontLeftIssue` | page 6 | TRCM ECU: a416 seatbelt lap pretensioner front left issue | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_seatbeltLapPretensionerFrontRightIssue` | page 6 | TRCM ECU: a417 seatbelt lap pretensioner front right issue | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_outboardSeatAirbagLeftIssue` | page 6 | TRCM ECU: a418 outboard seat airbag left issue | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_outboardSeatAirbagRightIssue` | page 6 | TRCM ECU: a419 outboard seat airbag right issue | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_hoodLifterLeftIssue` | page 6 | TRCM ECU: a420 hood lifter left issue | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_hoodLifterRightIssue` | page 7 | TRCM ECU: a421 hood lifter right issue | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_seatbeltShoulderPretensionerRearLeftIssue` | page 7 | TRCM ECU: a422 seatbelt shoulder pretensioner rear left issue | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_seatbeltShoulderPretensionerRearRightIssue` | page 7 | TRCM ECU: a423 seatbelt shoulder pretensioner rear right issue | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a432_driverAirbagStage1ConfigError` | page 7 | TRCM ECU: a432 driver airbag stage1 config error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a433_passengerAirbagStage1ConfigError` | page 7 | TRCM ECU: a433 passenger airbag stage1 config error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a434_driverAirbagStage2ConfigError` | page 7 | TRCM ECU: a434 driver airbag stage2 config error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a435_driverAirbagActiveVentConfigError` | page 7 | TRCM ECU: a435 driver airbag active vent config error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a436_passengerAirbagStage2ConfigError` | page 7 | TRCM ECU: a436 passenger airbag stage2 config error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a437_passengerAirbagActiveVentConfigError` | page 7 | TRCM ECU: a437 passenger airbag active vent config error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a438_inboardSeatAirbagConfigError` | page 7 | TRCM ECU: a438 inboard seat airbag config error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a440_kneeAirbagLeftConfigError` | page 7 | TRCM ECU: a440 knee airbag left config error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a441_kneeAirbagRightConfigError` | page 7 | TRCM ECU: a441 knee airbag right config error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a442_curtainAirbagLeftConfigError` | page 7 | TRCM ECU: a442 curtain airbag left config error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a443_curtainAirbagRightConfigError` | page 7 | TRCM ECU: a443 curtain airbag right config error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a444_seatbeltLoadLimiterFrontLeftConfigError` | page 7 | TRCM ECU: a444 seatbelt load limiter front left config error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a445_seatbeltLoadLimiterFrontRightConfigError` | page 7 | TRCM ECU: a445 seatbelt load limiter front right config error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a446_seatbeltShoulderPretensionerFrontLeftConfigError` | page 7 | TRCM ECU: a446 seatbelt shoulder pretensioner front left config error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a447_seatbeltShoulderPretensionerFrontRightConfigError` | page 7 | TRCM ECU: a447 seatbelt shoulder pretensioner front right config error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a448_seatbeltLapPretensionerFrontLeftConfigError` | page 7 | TRCM ECU: a448 seatbelt lap pretensioner front left config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a449_seatbeltLapPretensionerFrontRightConfigError` | page 7 | TRCM ECU: a449 seatbelt lap pretensioner front right config error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a450_outboardSeatAirbagLeftConfigError` | page 7 | TRCM ECU: a450 outboard seat airbag left config error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a451_outboardSeatAirbagRightConfigError` | page 7 | TRCM ECU: a451 outboard seat airbag right config error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a452_hoodLifterLeftConfigError` | page 7 | TRCM ECU: a452 hood lifter left config error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a453_hoodLifterRightConfigError` | page 7 | TRCM ECU: a453 hood lifter right config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a454_seatbeltShoulderPretensionerRearLeftConfigError` | page 7 | TRCM ECU: a454 seatbelt shoulder pretensioner rear left config error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a455_seatbeltShoulderPretensionerRearRightConfigError` | page 7 | TRCM ECU: a455 seatbelt shoulder pretensioner rear right config error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a544_erCapDiagnosticsFailed` | page 9 | TRCM ECU: a544 er cap diagnostics failed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a545_erCapBelowAutarkyThreshold` | page 9 | TRCM ECU: a545 er cap below autarky threshold | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a546_sensorValuesFaultedBySmart` | page 9 | TRCM ECU: a546 sensor values faulted by smart | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a550_AlgoWake_RCM_WAKE_FRONT` | page 9 | TRCM ECU: a550 algo wake RCM WAKE FRONT | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a551_AlgoWake_RCM_WAKE_REAR` | page 9 | TRCM ECU: a551 algo wake RCM WAKE REAR | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a552_AlgoWake_RCM_WAKE_LEFT` | page 9 | TRCM ECU: a552 algo wake RCM WAKE LEFT | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a553_AlgoWake_RCM_WAKE_RIGHT` | page 9 | TRCM ECU: a553 algo wake RCM WAKE RIGHT | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a554_AlgoWake_PAS_LH_PLAUSI_FRONT` | page 9 | TRCM ECU: a554 algo wake PAS LH PLAUSI FRONT | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a555_AlgoWake_PAS_LH_PLAUSI_REAR` | page 9 | TRCM ECU: a555 algo wake PAS LH PLAUSI REAR | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a557_AlgoWake_PAS_RH_PLAUSI_FRONT` | page 9 | TRCM ECU: a557 algo wake PAS RH PLAUSI FRONT | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a558_AlgoWake_PAS_RH_PLAUSI_REAR` | page 9 | TRCM ECU: a558 algo wake PAS RH PLAUSI REAR | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a560_AlgoWake_RCM_WAKE_ROLL_LEFT` | page 9 | TRCM ECU: a560 algo wake RCM WAKE ROLL LEFT | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a561_AlgoWake_RCM_WAKE_ROLL_RIGHT` | page 9 | TRCM ECU: a561 algo wake RCM WAKE ROLL RIGHT | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a562_AlgoWake_RCM_AWAKE_FRONT` | page 9 | TRCM ECU: a562 algo wake RCM AWAKE FRONT | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a563_AlgoWake_RCM_AWAKE_REAR` | page 9 | TRCM ECU: a563 algo wake RCM AWAKE REAR | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a564_AlgoWake_RCM_AWAKE_LEFT` | page 9 | TRCM ECU: a564 algo wake RCM AWAKE LEFT | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a565_AlgoWake_RCM_AWAKE_RIGHT` | page 9 | TRCM ECU: a565 algo wake RCM AWAKE RIGHT | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a566_AlgoWake_RCM_AWAKE_ROLL` | page 9 | TRCM ECU: a566 algo wake RCM AWAKE ROLL | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a567_AlgoWake_RCM_AWAKE_X` | page 9 | TRCM ECU: a567 algo wake RCM AWAKE x | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a568_AlgoWake_RCM_AWAKE_Y` | page 9 | TRCM ECU: a568 algo wake RCM AWAKE y | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a569_AlgoWake_PAS_WAKE_LEFT` | page 9 | TRCM ECU: a569 algo wake PAS WAKE LEFT | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a570_AlgoWake_PAS_WAKE_RIGHT` | page 9 | TRCM ECU: a570 algo wake PAS WAKE RIGHT | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a576_AlgoWake_IMPACT_FINISH_X` | page 9 | TRCM ECU: a576 algo wake IMPACT FINISH x | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a577_AlgoWake_IMPACT_FINISH_Y` | page 9 | TRCM ECU: a577 algo wake IMPACT FINISH y | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a578_AlgoWake_IMPACT_FINISH_ROLL` | page 9 | TRCM ECU: a578 algo wake IMPACT FINISH ROLL | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a579_AlgoWake_RCM_ENABLED_X` | page 9 | TRCM ECU: a579 algo wake RCM ENABLED x | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a580_AlgoWake_RCM_ENABLED_Y` | page 9 | TRCM ECU: a580 algo wake RCM ENABLED y | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a581_AlgoWake_RCM_ENABLED_ROLL` | page 9 | TRCM ECU: a581 algo wake RCM ENABLED ROLL | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a582_AlgoWake_RCM_AWAKE` | page 9 | TRCM ECU: a582 algo wake RCM AWAKE | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a588_yawRateOffsetPosLimit` | page 9 | TRCM ECU: a588 yaw rate offset pos limit | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a589_yawRateOffsetNegLimit` | page 9 | TRCM ECU: a589 yaw rate offset neg limit | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a590_pitchRateOffsetPosLimit` | page 9 | TRCM ECU: a590 pitch rate offset pos limit | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a591_pitchRateOffsetNegLimit` | page 9 | TRCM ECU: a591 pitch rate offset neg limit | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a592_rollRateOffsetPosLimit` | page 9 | TRCM ECU: a592 roll rate offset pos limit | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a593_rollRateOffsetNegLimit` | page 9 | TRCM ECU: a593 roll rate offset neg limit | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a594_longitudinalAccelOffsetPosLimit` | page 9 | TRCM ECU: a594 longitudinal accel offset pos limit | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a595_longitudinalAccelOffsetNegLimit` | page 9 | TRCM ECU: a595 longitudinal accel offset neg limit | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a596_lateralAccelOffsetPosLimit` | page 9 | TRCM ECU: a596 lateral accel offset pos limit | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a597_lateralAccelOffsetNegLimit` | page 9 | TRCM ECU: a597 lateral accel offset neg limit | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a598_verticalAccelOffsetPosLimit` | page 9 | TRCM ECU: a598 vertical accel offset pos limit | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a599_verticalAccelOffsetNegLimit` | page 9 | TRCM ECU: a599 vertical accel offset neg limit | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a600_airbagAsicStartupFailure` | page 9 | TRCM ECU: a600 airbag asic startup failure | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a601_loop0AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a601 loop0 asic startup diagnostic failure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a602_loop1AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a602 loop1 asic startup diagnostic failure | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a603_loop2AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a603 loop2 asic startup diagnostic failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a604_loop3AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a604 loop3 asic startup diagnostic failure | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a605_loop4AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a605 loop4 asic startup diagnostic failure | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a606_loop5AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a606 loop5 asic startup diagnostic failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a607_loop6AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a607 loop6 asic startup diagnostic failure | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a608_loop7AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a608 loop7 asic startup diagnostic failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a609_loop8AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a609 loop8 asic startup diagnostic failure | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a610_loop9AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a610 loop9 asic startup diagnostic failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a611_loop10AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a611 loop10 asic startup diagnostic failure | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a612_loop11AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a612 loop11 asic startup diagnostic failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a613_loop12AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a613 loop12 asic startup diagnostic failure | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a614_loop13AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a614 loop13 asic startup diagnostic failure | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a615_loop14AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a615 loop14 asic startup diagnostic failure | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a616_loop15AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a616 loop15 asic startup diagnostic failure | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a617_loop16AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a617 loop16 asic startup diagnostic failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a618_loop17AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a618 loop17 asic startup diagnostic failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a619_loop18AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a619 loop18 asic startup diagnostic failure | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a620_loop19AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a620 loop19 asic startup diagnostic failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a621_loop20AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a621 loop20 asic startup diagnostic failure | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a622_loop21AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a622 loop21 asic startup diagnostic failure | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a623_loop22AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a623 loop22 asic startup diagnostic failure | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a624_loop23AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a624 loop23 asic startup diagnostic failure | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a625_loop24AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a625 loop24 asic startup diagnostic failure | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a626_loop25AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a626 loop25 asic startup diagnostic failure | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a627_loop26AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a627 loop26 asic startup diagnostic failure | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a628_loop27AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a628 loop27 asic startup diagnostic failure | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a629_loop28AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a629 loop28 asic startup diagnostic failure | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a630_loop29AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a630 loop29 asic startup diagnostic failure | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a631_loop30AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a631 loop30 asic startup diagnostic failure | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a632_loop31AsicStartupDiagnosticFailure` | page 10 | TRCM ECU: a632 loop31 asic startup diagnostic failure | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a633_glacierInitialStatusFailure` | page 10 | TRCM ECU: a633 glacier initial status failure | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a634_glacierTraceabilityReadoutA0A0Failure` | page 10 | TRCM ECU: a634 glacier traceability readout A0 A0 failure | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a635_glacierTraceabilityReadoutB0B0Failure` | page 10 | TRCM ECU: a635 glacier traceability readout B0 B0 failure | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a636_glacierRegisterPatternWriteFailure` | page 10 | TRCM ECU: a636 glacier register pattern write failure | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a637_glacierFixedPatternSelfTestFailure` | page 10 | TRCM ECU: a637 glacier fixed pattern self test failure | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a638_glacierSelfTestEFailure` | page 10 | TRCM ECU: a638 glacier self test e failure | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a639_glacierSelfTestFFailure` | page 10 | TRCM ECU: a639 glacier self test f failure | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a640_glacierAnalogSelfTestFailure` | page 10 | TRCM ECU: a640 glacier analog self test failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a641_glacierOscillatorVerificationFailure` | page 10 | TRCM ECU: a641 glacier oscillator verification failure | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a642_glacierFinalStatusFailure` | page 10 | TRCM ECU: a642 glacier final status failure | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a643_glacierOffsetVerificationFailure` | page 10 | TRCM ECU: a643 glacier offset verification failure | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a644_glacierNormalOperationFailure` | page 10 | TRCM ECU: a644 glacier normal operation failure | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a645_glacierDeviceReset` | page 10 | TRCM ECU: a645 glacier device reset | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a646_glacierDeviceFaulted` | page 10 | TRCM ECU: a646 glacier device faulted | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`TRCM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (54 signals), page 1 (58 signals), page 2 (46 signals), page 3 (20 signals), page 4 (28 signals), page 5 (45 signals), page 6 (55 signals), page 7 (26 signals), page 9 (42 signals), page 10 (46 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All TRCM ECU messages (TRCM)](../../trcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
