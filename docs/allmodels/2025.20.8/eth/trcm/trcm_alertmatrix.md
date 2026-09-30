---
layout: default
title: "TRCM_alertMatrix (0x7EE) — TRCM ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "TRCM ECU message: alert matrix. Ethernet-side message TRCM_alertMatrix of TRCM ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 551 signals (TRCM_matrixIndex, TRCM_a003_SWAssertion, TRCM_a005_CANTXError, TRCM_a006_CANTX_cyclicError and 547 more). Bit layout, scaling, units and value tables."
---

# TRCM_alertMatrix (0x7EE) — TRCM ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

TRCM ECU message: alert matrix. This page documents the 551 signals of TRCM_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TRCM_alertMatrix` |
| Ethernet-side id | 0x7EE (2030) |
| ECU | [TRCM ECU](../../trcm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TRCM |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 551 |

## Signals of TRCM_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `TRCM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TRCM_matrixIndex` | selector | TRCM ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | plausible |
| `TRCM_a003_SWAssertion` | page 0 | TRCM ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a005_CANTXError` | page 0 | TRCM ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a006_CANTX_cyclicError` | page 0 | TRCM ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a007_chassisChecksumError` | page 0 | TRCM ECU: a007 chassis checksum error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a008_chassisCounterError` | page 0 | TRCM ECU: a008 chassis counter error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a009_partyChecksumError` | page 0 | TRCM ECU: a009 party checksum error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a010_partyCounterError` | page 0 | TRCM ECU: a010 party counter error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a030_ECULogUploadRequest` | page 0 | TRCM ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a031_UDSActive` | page 0 | TRCM ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a033_HercLogCreated` | page 0 | TRCM ECU: a033 herc log created | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a034_apClipTrigger` | page 0 | TRCM ECU: a034 ap clip trigger | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a035_hvDisconnectCommanded` | page 0 | TRCM ECU: a035 hv disconnect commanded | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a041_HighCPULoad` | page 0 | TRCM ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a042_HighStackUsage` | page 0 | TRCM ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a043_Task1msError` | page 0 | TRCM ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a044_Task10msError` | page 0 | TRCM ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a045_Task100msError` | page 0 | TRCM ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a046_Task1000msError` | page 0 | TRCM ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a057_HVP_MIA` | page 0 | TRCM ECU: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a058_inputRHighSyncDebug` | page 0 | TRCM ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a059_inputResistanceHigh` | page 0 | TRCM ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a060_engineeringBuild` | page 0 | TRCM ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a061_XCPConnected` | page 1 | TRCM ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a062_XCPWasConnected` | page 1 | TRCM ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a063_SwitchFault` | page 1 | TRCM ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a064_busSleepReqTimeout` | page 1 | TRCM ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a065_vSafingFetUnderVoltage` | page 1 | TRCM ECU: a065 v safing fet under voltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a066_vBusAUnderVoltage` | page 1 | TRCM ECU: a066 v bus a under voltage | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a067_vBusBUnderVoltage` | page 1 | TRCM ECU: a067 v bus b under voltage | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a081_autarkyActive` | page 1 | TRCM ECU: a081 autarky active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a121_glacierInitialStatusFailure` | page 2 | TRCM ECU: a121 glacier initial status failure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a122_glacierTraceabilityReadoutA0A0Failure` | page 2 | TRCM ECU: a122 glacier traceability readout A0 A0 failure | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a123_glacierTraceabilityReadoutB0B0Failure` | page 2 | TRCM ECU: a123 glacier traceability readout B0 B0 failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a124_glacierRegisterPatternWriteFailure` | page 2 | TRCM ECU: a124 glacier register pattern write failure | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a125_glacierFixedPatternSelfTestFailure` | page 2 | TRCM ECU: a125 glacier fixed pattern self test failure | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a126_glacierSelfTestEFailure` | page 2 | TRCM ECU: a126 glacier self test e failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a127_glacierSelfTestFFailure` | page 2 | TRCM ECU: a127 glacier self test f failure | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a128_glacierAnalogSelfTestFailure` | page 2 | TRCM ECU: a128 glacier analog self test failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a129_glacierOscillatorVerificationFailure` | page 2 | TRCM ECU: a129 glacier oscillator verification failure | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a130_glacierFinalStatusFailure` | page 2 | TRCM ECU: a130 glacier final status failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a131_glacierOffsetVerificationFailure` | page 2 | TRCM ECU: a131 glacier offset verification failure | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a132_glacierNormalOperationFailure` | page 2 | TRCM ECU: a132 glacier normal operation failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a133_glacierDeviceReset` | page 2 | TRCM ECU: a133 glacier device reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a134_glacierDeviceFaulted` | page 2 | TRCM ECU: a134 glacier device faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a135_asm5StatusError` | page 2 | TRCM ECU: a135 asm5 status error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a136_asm5DeviceFaulted` | page 2 | TRCM ECU: a136 asm5 device faulted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a137_ext1AsicSnoopTestFailed` | page 2 | TRCM ECU: a137 ext1 asic snoop test failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a138_ext2AsicSnoopTestFailed` | page 2 | TRCM ECU: a138 ext2 asic snoop test failed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a139_disarmed` | page 2 | TRCM ECU: a139 disarmed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a140_frontRightAccelInitFailure` | page 2 | TRCM ECU: a140 front right accel init failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a141_frontRightAccelShortToGround` | page 2 | TRCM ECU: a141 front right accel short to ground | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a142_frontRightAccelShortToBattery` | page 2 | TRCM ECU: a142 front right accel short to battery | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a143_frontRightAccelConfigError` | page 2 | TRCM ECU: a143 front right accel config error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a144_frontRightAccelOpen` | page 2 | TRCM ECU: a144 front right accel open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a145_frontRightAccelCommError` | page 2 | TRCM ECU: a145 front right accel comm error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a146_frontRightAccelSensorDefect` | page 2 | TRCM ECU: a146 front right accel sensor defect | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a147_frontRightAccelSignalMonitor` | page 2 | TRCM ECU: a147 front right accel signal monitor | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a150_rightFrontDoorPressureInitFailure` | page 2 | TRCM ECU: a150 right front door pressure init failure | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a151_rightFrontDoorPressureShortToGround` | page 2 | TRCM ECU: a151 right front door pressure short to ground | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a152_rightFrontDoorPressureShortToBattery` | page 2 | TRCM ECU: a152 right front door pressure short to battery | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a153_rightFrontDoorPressureConfigError` | page 2 | TRCM ECU: a153 right front door pressure config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a154_rightFrontDoorPressureOpen` | page 2 | TRCM ECU: a154 right front door pressure open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a155_rightFrontDoorPressureCommError` | page 2 | TRCM ECU: a155 right front door pressure comm error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a156_rightFrontDoorPressureSensorDefect` | page 2 | TRCM ECU: a156 right front door pressure sensor defect | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a157_rightFrontDoorPressureSignalMonitor` | page 2 | TRCM ECU: a157 right front door pressure signal monitor | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a160_frontLeftAccelInitFailure` | page 2 | TRCM ECU: a160 front left accel init failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a161_frontLeftAccelShortToGround` | page 2 | TRCM ECU: a161 front left accel short to ground | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a162_frontLeftAccelShortToBattery` | page 2 | TRCM ECU: a162 front left accel short to battery | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a163_frontLeftAccelConfigError` | page 2 | TRCM ECU: a163 front left accel config error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a164_frontLeftAccelOpen` | page 2 | TRCM ECU: a164 front left accel open | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a165_frontLeftAccelCommError` | page 2 | TRCM ECU: a165 front left accel comm error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a166_frontLeftAccelSensorDefect` | page 2 | TRCM ECU: a166 front left accel sensor defect | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a167_frontLeftAccelSignalMonitor` | page 2 | TRCM ECU: a167 front left accel signal monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a170_leftFrontDoorPressureInitFailure` | page 2 | TRCM ECU: a170 left front door pressure init failure | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a171_leftFrontDoorPressureShortToGround` | page 2 | TRCM ECU: a171 left front door pressure short to ground | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a172_leftFrontDoorPressureShortToBattery` | page 2 | TRCM ECU: a172 left front door pressure short to battery | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a173_leftFrontDoorPressureConfigError` | page 2 | TRCM ECU: a173 left front door pressure config error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a174_leftFrontDoorPressureOpen` | page 2 | TRCM ECU: a174 left front door pressure open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a175_leftFrontDoorPressureCommError` | page 2 | TRCM ECU: a175 left front door pressure comm error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a176_leftFrontDoorPressureSensorDefect` | page 2 | TRCM ECU: a176 left front door pressure sensor defect | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a177_leftFrontDoorPressureSignalMonitor` | page 2 | TRCM ECU: a177 left front door pressure signal monitor | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a180_rightBPillarAccelInitFailure` | page 2 | TRCM ECU: a180 right b pillar accel init failure | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a181_rightBPillarAccelShortToGround` | page 3 | TRCM ECU: a181 right b pillar accel short to ground | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a182_rightBPillarAccelShortToBattery` | page 3 | TRCM ECU: a182 right b pillar accel short to battery | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a183_rightBPillarAccelConfigError` | page 3 | TRCM ECU: a183 right b pillar accel config error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a184_rightBPillarAccelOpen` | page 3 | TRCM ECU: a184 right b pillar accel open | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a185_rightBPillarAccelCommError` | page 3 | TRCM ECU: a185 right b pillar accel comm error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a186_rightBPillarAccelSensorDefect` | page 3 | TRCM ECU: a186 right b pillar accel sensor defect | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a187_rightBPillarAccelSignalMonitor` | page 3 | TRCM ECU: a187 right b pillar accel signal monitor | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a190_leftBPillarAccelInitFailure` | page 3 | TRCM ECU: a190 left b pillar accel init failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a191_leftBPillarAccelShortToGround` | page 3 | TRCM ECU: a191 left b pillar accel short to ground | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a192_leftBPillarAccelShortToBattery` | page 3 | TRCM ECU: a192 left b pillar accel short to battery | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a193_leftBPillarAccelConfigError` | page 3 | TRCM ECU: a193 left b pillar accel config error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a194_leftBPillarAccelOpen` | page 3 | TRCM ECU: a194 left b pillar accel open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a195_leftBPillarAccelCommError` | page 3 | TRCM ECU: a195 left b pillar accel comm error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a196_leftBPillarAccelSensorDefect` | page 3 | TRCM ECU: a196 left b pillar accel sensor defect | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a197_leftBPillarAccelSignalMonitor` | page 3 | TRCM ECU: a197 left b pillar accel signal monitor | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a200_frontCenterAccelInitFailure` | page 3 | TRCM ECU: a200 front center accel init failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a201_frontCenterAccelShortToGround` | page 3 | TRCM ECU: a201 front center accel short to ground | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a202_frontCenterAccelShortToBattery` | page 3 | TRCM ECU: a202 front center accel short to battery | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a203_frontCenterAccelConfigError` | page 3 | TRCM ECU: a203 front center accel config error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a204_frontCenterAccelOpen` | page 3 | TRCM ECU: a204 front center accel open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a205_frontCenterAccelCommError` | page 3 | TRCM ECU: a205 front center accel comm error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a206_frontCenterAccelSensorDefect` | page 3 | TRCM ECU: a206 front center accel sensor defect | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a207_frontCenterAccelSignalMonitor` | page 3 | TRCM ECU: a207 front center accel signal monitor | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a210_leftCPillarAccelInitFailure` | page 3 | TRCM ECU: a210 left c pillar accel init failure | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a211_leftCPillarAccelShortToGround` | page 3 | TRCM ECU: a211 left c pillar accel short to ground | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a212_leftCPillarAccelShortToBattery` | page 3 | TRCM ECU: a212 left c pillar accel short to battery | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a213_leftCPillarAccelConfigError` | page 3 | TRCM ECU: a213 left c pillar accel config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a214_leftCPillarAccelOpen` | page 3 | TRCM ECU: a214 left c pillar accel open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a215_leftCPillarAccelCommError` | page 3 | TRCM ECU: a215 left c pillar accel comm error | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a216_leftCPillarAccelSensorDefect` | page 3 | TRCM ECU: a216 left c pillar accel sensor defect | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a217_leftCPillarAccelSignalMonitor` | page 3 | TRCM ECU: a217 left c pillar accel signal monitor | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a220_rightCPillarAccelInitFailure` | page 3 | TRCM ECU: a220 right c pillar accel init failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a221_rightCPillarAccelShortToGround` | page 3 | TRCM ECU: a221 right c pillar accel short to ground | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a222_rightCPillarAccelShortToBattery` | page 3 | TRCM ECU: a222 right c pillar accel short to battery | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a223_rightCPillarAccelConfigError` | page 3 | TRCM ECU: a223 right c pillar accel config error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a224_rightCPillarAccelOpen` | page 3 | TRCM ECU: a224 right c pillar accel open | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a225_rightCPillarAccelCommError` | page 3 | TRCM ECU: a225 right c pillar accel comm error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a226_rightCPillarAccelSensorDefect` | page 3 | TRCM ECU: a226 right c pillar accel sensor defect | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a227_rightCPillarAccelSignalMonitor` | page 3 | TRCM ECU: a227 right c pillar accel signal monitor | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a230_leftRearDoorPressureInitFailure` | page 3 | TRCM ECU: a230 left rear door pressure init failure | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a231_leftRearDoorPressureShortToGround` | page 3 | TRCM ECU: a231 left rear door pressure short to ground | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a232_leftRearDoorPressureShortToBattery` | page 3 | TRCM ECU: a232 left rear door pressure short to battery | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a233_leftRearDoorPressureConfigError` | page 3 | TRCM ECU: a233 left rear door pressure config error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a234_leftRearDoorPressureOpen` | page 3 | TRCM ECU: a234 left rear door pressure open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a235_leftRearDoorPressureCommError` | page 3 | TRCM ECU: a235 left rear door pressure comm error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a236_leftRearDoorPressureSensorDefect` | page 3 | TRCM ECU: a236 left rear door pressure sensor defect | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a237_leftRearDoorPressureSignalMonitor` | page 3 | TRCM ECU: a237 left rear door pressure signal monitor | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a240_rightRearDoorPressureInitFailure` | page 3 | TRCM ECU: a240 right rear door pressure init failure | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a241_rightRearDoorPressureShortToGround` | page 4 | TRCM ECU: a241 right rear door pressure short to ground | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a242_rightRearDoorPressureShortToBattery` | page 4 | TRCM ECU: a242 right rear door pressure short to battery | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a243_rightRearDoorPressureConfigError` | page 4 | TRCM ECU: a243 right rear door pressure config error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a244_rightRearDoorPressureOpen` | page 4 | TRCM ECU: a244 right rear door pressure open | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a245_rightRearDoorPressureCommError` | page 4 | TRCM ECU: a245 right rear door pressure comm error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a246_rightRearDoorPressureSensorDefect` | page 4 | TRCM ECU: a246 right rear door pressure sensor defect | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a247_rightRearDoorPressureSignalMonitor` | page 4 | TRCM ECU: a247 right rear door pressure signal monitor | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a250_frontCenterAccelXInitFailure` | page 4 | TRCM ECU: a250 front center accel x init failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a251_frontCenterAccelXShortToGround` | page 4 | TRCM ECU: a251 front center accel x short to ground | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a252_frontCenterAccelXShortToBattery` | page 4 | TRCM ECU: a252 front center accel x short to battery | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a253_frontCenterAccelXConfigError` | page 4 | TRCM ECU: a253 front center accel x config error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a254_frontCenterAccelXOpen` | page 4 | TRCM ECU: a254 front center accel x open | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a255_frontCenterAccelXCommError` | page 4 | TRCM ECU: a255 front center accel x comm error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a256_frontCenterAccelXSensorDefect` | page 4 | TRCM ECU: a256 front center accel x sensor defect | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a257_frontCenterAccelXSignalMonitor` | page 4 | TRCM ECU: a257 front center accel x signal monitor | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a260_frontCenterAccelYInitFailure` | page 4 | TRCM ECU: a260 front center accel y init failure | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a261_frontCenterAccelYShortToGround` | page 4 | TRCM ECU: a261 front center accel y short to ground | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a262_frontCenterAccelYShortToBattery` | page 4 | TRCM ECU: a262 front center accel y short to battery | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a263_frontCenterAccelYConfigError` | page 4 | TRCM ECU: a263 front center accel y config error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a264_frontCenterAccelYOpen` | page 4 | TRCM ECU: a264 front center accel y open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a265_frontCenterAccelYCommError` | page 4 | TRCM ECU: a265 front center accel y comm error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a266_frontCenterAccelYSensorDefect` | page 4 | TRCM ECU: a266 front center accel y sensor defect | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a267_frontCenterAccelYSignalMonitor` | page 4 | TRCM ECU: a267 front center accel y signal monitor | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a300_unarmedAB1FPDeployCommand` | page 4 | TRCM ECU: a300 unarmed AB1 FP deploy command | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a301_unarmedAB1FDDeployCommand` | page 5 | TRCM ECU: a301 unarmed AB1 FD deploy command | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a302_unarmedAV1FPDeployCommand` | page 5 | TRCM ECU: a302 unarmed AV1 FP deploy command | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a303_unarmedFSABDeployCommand` | page 5 | TRCM ECU: a303 unarmed FSAB deploy command | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a304_unarmedAB2FPDeployCommand` | page 5 | TRCM ECU: a304 unarmed AB2 FP deploy command | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a305_unarmedAB2FDDeployCommand` | page 5 | TRCM ECU: a305 unarmed AB2 FD deploy command | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a306_unarmedAV1FDDeployCommand` | page 5 | TRCM ECU: a306 unarmed AV1 FD deploy command | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a307_unarmedLoop7DeployCommand` | page 5 | TRCM ECU: a307 unarmed loop7 deploy command | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a308_unarmedKA1FPDeployCommand` | page 5 | TRCM ECU: a308 unarmed KA1 FP deploy command | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a309_unarmedKA1FDDeployCommand` | page 5 | TRCM ECU: a309 unarmed KA1 FD deploy command | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a310_unarmedALLFRDeployCommand` | page 5 | TRCM ECU: a310 unarmed ALLFR deploy command | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a311_unarmedALLFLDeployCommand` | page 5 | TRCM ECU: a311 unarmed ALLFL deploy command | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a312_unarmedBT2FRDeployCommand` | page 5 | TRCM ECU: a312 unarmed BT2 FR deploy command | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a313_unarmedBT2FLDeployCommand` | page 5 | TRCM ECU: a313 unarmed BT2 FL deploy command | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a314_unarmedSA1FLDeployCommand` | page 5 | TRCM ECU: a314 unarmed SA1 FL deploy command | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a315_unarmedSA1FRDeployCommand` | page 5 | TRCM ECU: a315 unarmed SA1 FR deploy command | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a316_unarmedBT1RRDeployCommand` | page 5 | TRCM ECU: a316 unarmed BT1 RR deploy command | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a317_unarmedBT1RLDeployCommand` | page 5 | TRCM ECU: a317 unarmed BT1 RL deploy command | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a318_unarmedBT1FRDeployCommand` | page 5 | TRCM ECU: a318 unarmed BT1 FR deploy command | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a319_unarmedBT1FLDeployCommand` | page 5 | TRCM ECU: a319 unarmed BT1 FL deploy command | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a320_unarmedLoop20DeployCommand` | page 5 | TRCM ECU: a320 unarmed loop20 deploy command | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a321_unarmedLoop21DeployCommand` | page 5 | TRCM ECU: a321 unarmed loop21 deploy command | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a322_unarmedIC1FRDeployCommand` | page 5 | TRCM ECU: a322 unarmed IC1 FR deploy command | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a323_unarmedIC1FLDeployCommand` | page 5 | TRCM ECU: a323 unarmed IC1 FL deploy command | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a324_unarmedLoop24DeployCommand` | page 5 | TRCM ECU: a324 unarmed loop24 deploy command | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a325_unarmedLoop25DeployCommand` | page 5 | TRCM ECU: a325 unarmed loop25 deploy command | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a326_unarmedLoop26DeployCommand` | page 5 | TRCM ECU: a326 unarmed loop26 deploy command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a327_unarmedLoop27DeployCommand` | page 5 | TRCM ECU: a327 unarmed loop27 deploy command | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a328_unarmedLoop28DeployCommand` | page 5 | TRCM ECU: a328 unarmed loop28 deploy command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a329_unarmedLoop29DeployCommand` | page 5 | TRCM ECU: a329 unarmed loop29 deploy command | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a330_unarmedLoop30DeployCommand` | page 5 | TRCM ECU: a330 unarmed loop30 deploy command | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a331_unarmedLoop31DeployCommand` | page 5 | TRCM ECU: a331 unarmed loop31 deploy command | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a332_AB1FPDeployment` | page 5 | TRCM ECU: a332 AB1 FP deployment | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a333_AB1FDDeployment` | page 5 | TRCM ECU: a333 AB1 FD deployment | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a334_AV1FPDeployment` | page 5 | TRCM ECU: a334 AV1 FP deployment | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a335_Loop3Deployment` | page 5 | TRCM ECU: a335 loop3 deployment | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a336_AB2FPDeployment` | page 5 | TRCM ECU: a336 AB2 FP deployment | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a337_AB2FDDeployment` | page 5 | TRCM ECU: a337 AB2 FD deployment | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a338_AV1FDDeployment` | page 5 | TRCM ECU: a338 AV1 FD deployment | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a339_Loop7Deployment` | page 5 | TRCM ECU: a339 loop7 deployment | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a340_KA1FPDeployment` | page 5 | TRCM ECU: a340 KA1 FP deployment | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a341_KA1FDDeployment` | page 5 | TRCM ECU: a341 KA1 FD deployment | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a342_ALLFRDeployment` | page 5 | TRCM ECU: a342 ALLFR deployment | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a343_ALLFLDeployment` | page 5 | TRCM ECU: a343 ALLFL deployment | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a344_BT2FRDeployment` | page 5 | TRCM ECU: a344 BT2 FR deployment | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a345_BT2FLDeployment` | page 5 | TRCM ECU: a345 BT2 FL deployment | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a346_SA1FLDeployment` | page 5 | TRCM ECU: a346 SA1 FL deployment | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a347_SA1FRDeployment` | page 5 | TRCM ECU: a347 SA1 FR deployment | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a348_BT1RRDeployment` | page 5 | TRCM ECU: a348 BT1 RR deployment | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a349_BT1RLDeployment` | page 5 | TRCM ECU: a349 BT1 RL deployment | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a350_BT1FRDeployment` | page 5 | TRCM ECU: a350 BT1 FR deployment | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a351_BT1FLDeployment` | page 5 | TRCM ECU: a351 BT1 FL deployment | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a352_Loop20Deployment` | page 5 | TRCM ECU: a352 loop20 deployment | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a353_Loop21Deployment` | page 5 | TRCM ECU: a353 loop21 deployment | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a354_IC1FRDeployment` | page 5 | TRCM ECU: a354 IC1 FR deployment | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a355_IC1FLDeployment` | page 5 | TRCM ECU: a355 IC1 FL deployment | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a356_Loop24Deployment` | page 5 | TRCM ECU: a356 loop24 deployment | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a357_Loop25Deployment` | page 5 | TRCM ECU: a357 loop25 deployment | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a358_Loop26Deployment` | page 5 | TRCM ECU: a358 loop26 deployment | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a359_Loop27Deployment` | page 5 | TRCM ECU: a359 loop27 deployment | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a360_Loop28Deployment` | page 5 | TRCM ECU: a360 loop28 deployment | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a361_Loop29Deployment` | page 6 | TRCM ECU: a361 loop29 deployment | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a362_Loop30Deployment` | page 6 | TRCM ECU: a362 loop30 deployment | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a363_Loop31Deployment` | page 6 | TRCM ECU: a363 loop31 deployment | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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
| `TRCM_a395_imuCalibrationNotDone` | page 6 | TRCM ECU: a395 imu calibration not done | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a396_spiCommunicationProgramError` | page 6 | TRCM ECU: a396 spi communication program error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a397_safingMonitorError` | page 6 | TRCM ECU: a397 safing monitor error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a398_asicNvmReprogrammed` | page 6 | TRCM ECU: a398 asic nvm reprogrammed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a400_AB1FPShortToGround` | page 6 | TRCM ECU: a400 AB1 FP short to ground | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a401_AB1FPShortToBattery` | page 6 | TRCM ECU: a401 AB1 FP short to battery | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a402_AB1FPOpen` | page 6 | TRCM ECU: a402 AB1 FP open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a403_AB1FPShortToSelf` | page 6 | TRCM ECU: a403 AB1 FP short to self | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a404_AB1FPCrossCoupled` | page 6 | TRCM ECU: a404 AB1 FP cross coupled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a405_AB1FPConfigError` | page 6 | TRCM ECU: a405 AB1 FP config error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a406_AB1FDShortToGround` | page 6 | TRCM ECU: a406 AB1 FD short to ground | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a407_AB1FDShortToBattery` | page 6 | TRCM ECU: a407 AB1 FD short to battery | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a408_AB1FDOpen` | page 6 | TRCM ECU: a408 AB1 FD open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a409_AB1FDShortToSelf` | page 6 | TRCM ECU: a409 AB1 FD short to self | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a410_AB1FDCrossCoupled` | page 6 | TRCM ECU: a410 AB1 FD cross coupled | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a411_AB1FDConfigError` | page 6 | TRCM ECU: a411 AB1 FD config error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a412_PAVShortToGround` | page 6 | TRCM ECU: a412 PAV short to ground | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a413_PAVShortToBattery` | page 6 | TRCM ECU: a413 PAV short to battery | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a414_PAVOpen` | page 6 | TRCM ECU: a414 PAV open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a415_PAVShortToSelf` | page 6 | TRCM ECU: a415 PAV short to self | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a416_PAVCrossCoupled` | page 6 | TRCM ECU: a416 PAV cross coupled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a417_PAVConfigError` | page 6 | TRCM ECU: a417 PAV config error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a418_AB2FPShortToGround` | page 6 | TRCM ECU: a418 AB2 FP short to ground | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a419_AB2FPShortToBattery` | page 6 | TRCM ECU: a419 AB2 FP short to battery | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a420_AB2FPOpen` | page 6 | TRCM ECU: a420 AB2 FP open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a421_AB2FPShortToSelf` | page 7 | TRCM ECU: a421 AB2 FP short to self | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a422_AB2FPCrossCoupled` | page 7 | TRCM ECU: a422 AB2 FP cross coupled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a423_AB2FPConfigError` | page 7 | TRCM ECU: a423 AB2 FP config error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a424_AB2FDShortToGround` | page 7 | TRCM ECU: a424 AB2 FD short to ground | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a425_AB2FDShortToBattery` | page 7 | TRCM ECU: a425 AB2 FD short to battery | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a426_AB2FDOpen` | page 7 | TRCM ECU: a426 AB2 FD open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a427_AB2FDShortToSelf` | page 7 | TRCM ECU: a427 AB2 FD short to self | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a428_AB2FDCrossCoupled` | page 7 | TRCM ECU: a428 AB2 FD cross coupled | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a429_AB2FDConfigError` | page 7 | TRCM ECU: a429 AB2 FD config error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a430_DAVShortToGround` | page 7 | TRCM ECU: a430 DAV short to ground | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a431_DAVShortToBattery` | page 7 | TRCM ECU: a431 DAV short to battery | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a432_DAVOpen` | page 7 | TRCM ECU: a432 DAV open | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a433_DAVShortToSelf` | page 7 | TRCM ECU: a433 DAV short to self | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a434_DAVCrossCoupled` | page 7 | TRCM ECU: a434 DAV cross coupled | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a435_DAVConfigError` | page 7 | TRCM ECU: a435 DAV config error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a436_IKBFPShortToGround` | page 7 | TRCM ECU: a436 IKBFP short to ground | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a437_IKBFPShortToBattery` | page 7 | TRCM ECU: a437 IKBFP short to battery | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a438_IKBFPOpen` | page 7 | TRCM ECU: a438 IKBFP open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a439_IKBFPShortToSelf` | page 7 | TRCM ECU: a439 IKBFP short to self | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a440_IKBFPCrossCoupled` | page 7 | TRCM ECU: a440 IKBFP cross coupled | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a441_IKBFPConfigError` | page 7 | TRCM ECU: a441 IKBFP config error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a442_IKBFDShortToGround` | page 7 | TRCM ECU: a442 IKBFD short to ground | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a443_IKBFDShortToBattery` | page 7 | TRCM ECU: a443 IKBFD short to battery | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a444_IKBFDOpen` | page 7 | TRCM ECU: a444 IKBFD open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a445_IKBFDShortToSelf` | page 7 | TRCM ECU: a445 IKBFD short to self | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a446_IKBFDCrossCoupled` | page 7 | TRCM ECU: a446 IKBFD cross coupled | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a447_IKBFDConfigError` | page 7 | TRCM ECU: a447 IKBFD config error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a448_PLLShortToGround` | page 7 | TRCM ECU: a448 PLL short to ground | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a449_PLLShortToBattery` | page 7 | TRCM ECU: a449 PLL short to battery | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a450_PLLOpen` | page 7 | TRCM ECU: a450 PLL open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a451_PLLShortToSelf` | page 7 | TRCM ECU: a451 PLL short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a452_PLLCrossCoupled` | page 7 | TRCM ECU: a452 PLL cross coupled | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a453_PLLConfigError` | page 7 | TRCM ECU: a453 PLL config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a454_DLLShortToGround` | page 7 | TRCM ECU: a454 DLL short to ground | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a455_DLLShortToBattery` | page 7 | TRCM ECU: a455 DLL short to battery | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a456_DLLOpen` | page 7 | TRCM ECU: a456 DLL open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a457_DLLShortToSelf` | page 7 | TRCM ECU: a457 DLL short to self | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a458_DLLCrossCoupled` | page 7 | TRCM ECU: a458 DLL cross coupled | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a459_DLLConfigError` | page 7 | TRCM ECU: a459 DLL config error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a460_BTRP_RetractorShortToGround` | page 7 | TRCM ECU: a460 BTRP retractor short to ground | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a461_BTRP_RetractorShortToBattery` | page 7 | TRCM ECU: a461 BTRP retractor short to battery | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a462_BTRP_RetractorOpen` | page 7 | TRCM ECU: a462 BTRP retractor open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a463_BTRP_RetractorShortToSelf` | page 7 | TRCM ECU: a463 BTRP retractor short to self | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a464_BTRP_RetractorCrossCoupled` | page 7 | TRCM ECU: a464 BTRP retractor cross coupled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a465_BTRP_RetractorConfigError` | page 7 | TRCM ECU: a465 BTRP retractor config error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a466_BTRD_RetractorShortToGround` | page 7 | TRCM ECU: a466 BTRD retractor short to ground | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a467_BTRD_RetractorShortToBattery` | page 7 | TRCM ECU: a467 BTRD retractor short to battery | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a468_BTRD_RetractorOpen` | page 7 | TRCM ECU: a468 BTRD retractor open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a469_BTRD_RetractorShortToSelf` | page 7 | TRCM ECU: a469 BTRD retractor short to self | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a470_BTRD_RetractorCrossCoupled` | page 7 | TRCM ECU: a470 BTRD retractor cross coupled | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a471_BTRD_RetractorConfigError` | page 7 | TRCM ECU: a471 BTRD retractor config error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a472_SA1FLShortToGround` | page 7 | TRCM ECU: a472 SA1 FL short to ground | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a473_SA1FLShortToBattery` | page 7 | TRCM ECU: a473 SA1 FL short to battery | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a474_SA1FLOpen` | page 7 | TRCM ECU: a474 SA1 FL open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a475_SA1FLShortToSelf` | page 7 | TRCM ECU: a475 SA1 FL short to self | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a476_SA1FLCrossCoupled` | page 7 | TRCM ECU: a476 SA1 FL cross coupled | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a477_SA1FLConfigError` | page 7 | TRCM ECU: a477 SA1 FL config error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a478_SA1FRShortToGround` | page 7 | TRCM ECU: a478 SA1 FR short to ground | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a479_SA1FRShortToBattery` | page 7 | TRCM ECU: a479 SA1 FR short to battery | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a480_SA1FROpen` | page 7 | TRCM ECU: a480 SA1 FR open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a481_SA1FRShortToSelf` | page 8 | TRCM ECU: a481 SA1 FR short to self | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a482_SA1FRCrossCoupled` | page 8 | TRCM ECU: a482 SA1 FR cross coupled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a483_SA1FRConfigError` | page 8 | TRCM ECU: a483 SA1 FR config error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a484_BTRRShortToGround` | page 8 | TRCM ECU: a484 BTRR short to ground | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a485_BTRRShortToBattery` | page 8 | TRCM ECU: a485 BTRR short to battery | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a486_BTRROpen` | page 8 | TRCM ECU: a486 BTRR open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a487_BTRRShortToSelf` | page 8 | TRCM ECU: a487 BTRR short to self | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a488_BTRRCrossCoupled` | page 8 | TRCM ECU: a488 BTRR cross coupled | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a489_BTRRConfigError` | page 8 | TRCM ECU: a489 BTRR config error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a490_BTRLShortToGround` | page 8 | TRCM ECU: a490 BTRL short to ground | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a491_BTRLShortToBattery` | page 8 | TRCM ECU: a491 BTRL short to battery | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a492_BTRLOpen` | page 8 | TRCM ECU: a492 BTRL open | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a493_BTRLShortToSelf` | page 8 | TRCM ECU: a493 BTRL short to self | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a494_BTRLCrossCoupled` | page 8 | TRCM ECU: a494 BTRL cross coupled | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a495_BTRLConfigError` | page 8 | TRCM ECU: a495 BTRL config error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a496_BTRP_AnchorShortToGround` | page 8 | TRCM ECU: a496 BTRP anchor short to ground | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a497_BTRP_AnchorShortToBattery` | page 8 | TRCM ECU: a497 BTRP anchor short to battery | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a498_BTRP_AnchorOpen` | page 8 | TRCM ECU: a498 BTRP anchor open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a499_BTRP_AnchorShortToSelf` | page 8 | TRCM ECU: a499 BTRP anchor short to self | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a500_BTRP_AnchorCrossCoupled` | page 8 | TRCM ECU: a500 BTRP anchor cross coupled | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a501_BTRP_AnchorConfigError` | page 8 | TRCM ECU: a501 BTRP anchor config error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a502_BTRD_AnchorShortToGround` | page 8 | TRCM ECU: a502 BTRD anchor short to ground | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a503_BTRD_AnchorShortToBattery` | page 8 | TRCM ECU: a503 BTRD anchor short to battery | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a504_BTRD_AnchorOpen` | page 8 | TRCM ECU: a504 BTRD anchor open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a505_BTRD_AnchorShortToSelf` | page 8 | TRCM ECU: a505 BTRD anchor short to self | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a506_BTRD_AnchorCrossCoupled` | page 8 | TRCM ECU: a506 BTRD anchor cross coupled | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a507_BTRD_AnchorConfigError` | page 8 | TRCM ECU: a507 BTRD anchor config error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a508_IC1FRShortToGround` | page 8 | TRCM ECU: a508 IC1 FR short to ground | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a509_IC1FRShortToBattery` | page 8 | TRCM ECU: a509 IC1 FR short to battery | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a510_IC1FROpen` | page 8 | TRCM ECU: a510 IC1 FR open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a511_IC1FRShortToSelf` | page 8 | TRCM ECU: a511 IC1 FR short to self | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a512_IC1FRCrossCoupled` | page 8 | TRCM ECU: a512 IC1 FR cross coupled | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a513_IC1FRConfigError` | page 8 | TRCM ECU: a513 IC1 FR config error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a514_IC1FLShortToGround` | page 8 | TRCM ECU: a514 IC1 FL short to ground | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a515_IC1FLShortToBattery` | page 8 | TRCM ECU: a515 IC1 FL short to battery | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a516_IC1FLOpen` | page 8 | TRCM ECU: a516 IC1 FL open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a517_IC1FLShortToSelf` | page 8 | TRCM ECU: a517 IC1 FL short to self | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a518_IC1FLCrossCoupled` | page 8 | TRCM ECU: a518 IC1 FL cross coupled | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a519_IC1FLConfigError` | page 8 | TRCM ECU: a519 IC1 FL config error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a520_FSABShortToGround` | page 8 | TRCM ECU: a520 FSAB short to ground | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a521_FSABShortToBattery` | page 8 | TRCM ECU: a521 FSAB short to battery | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a522_FSABOpen` | page 8 | TRCM ECU: a522 FSAB open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a523_FSABShortToSelf` | page 8 | TRCM ECU: a523 FSAB short to self | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a524_FSABCrossCoupled` | page 8 | TRCM ECU: a524 FSAB cross coupled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a525_FSABConfigError` | page 8 | TRCM ECU: a525 FSAB config error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a544_erCapDiagnosticsFailed` | page 9 | TRCM ECU: a544 er cap diagnostics failed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a545_erCapBelowAutarkyThreshold` | page 9 | TRCM ECU: a545 er cap below autarky threshold | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a546_sensorValuesFaultedBySmart` | page 9 | TRCM ECU: a546 sensor values faulted by smart | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a550_AlgoWake_RCM_WAKE_FRONT` | page 9 | TRCM ECU: a550 algo wake RCM WAKE FRONT | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a551_AlgoWake_RCM_WAKE_REAR` | page 9 | TRCM ECU: a551 algo wake RCM WAKE REAR | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a552_AlgoWake_RCM_WAKE_LEFT` | page 9 | TRCM ECU: a552 algo wake RCM WAKE LEFT | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a553_AlgoWake_RCM_WAKE_RIGHT` | page 9 | TRCM ECU: a553 algo wake RCM WAKE RIGHT | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a554_AlgoWake_PAS_LH_PLAUSI_FRONT` | page 9 | TRCM ECU: a554 algo wake PAS LH PLAUSI FRONT | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a555_AlgoWake_PAS_LH_PLAUSI_REAR` | page 9 | TRCM ECU: a555 algo wake PAS LH PLAUSI REAR | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a556_AlgoWake_PAS_LH_PLAUSI` | page 9 | TRCM ECU: a556 algo wake PAS LH PLAUSI | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a557_AlgoWake_PAS_RH_PLAUSI_FRONT` | page 9 | TRCM ECU: a557 algo wake PAS RH PLAUSI FRONT | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a558_AlgoWake_PAS_RH_PLAUSI_REAR` | page 9 | TRCM ECU: a558 algo wake PAS RH PLAUSI REAR | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a559_AlgoWake_PAS_RH_PLAUSI` | page 9 | TRCM ECU: a559 algo wake PAS RH PLAUSI | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a560_AlgoWake_RCM_WAKE_ROLL_LEFT` | page 9 | TRCM ECU: a560 algo wake RCM WAKE ROLL LEFT | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a561_AlgoWake_RCM_WAKE_ROLL_RIGHT` | page 9 | TRCM ECU: a561 algo wake RCM WAKE ROLL RIGHT | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a562_AlgoWake_RCM_AWAKE_FRONT` | page 9 | TRCM ECU: a562 algo wake RCM AWAKE FRONT | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a563_AlgoWake_RCM_AWAKE_REAR` | page 9 | TRCM ECU: a563 algo wake RCM AWAKE REAR | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a564_AlgoWake_RCM_AWAKE_LEFT` | page 9 | TRCM ECU: a564 algo wake RCM AWAKE LEFT | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a565_AlgoWake_RCM_AWAKE_RIGHT` | page 9 | TRCM ECU: a565 algo wake RCM AWAKE RIGHT | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a566_AlgoWake_RCM_AWAKE_ROLL` | page 9 | TRCM ECU: a566 algo wake RCM AWAKE ROLL | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a567_AlgoWake_RCM_AWAKE_X` | page 9 | TRCM ECU: a567 algo wake RCM AWAKE x | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a568_AlgoWake_RCM_AWAKE_Y` | page 9 | TRCM ECU: a568 algo wake RCM AWAKE y | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a569_AlgoWake_IMPACT_FINISH_X_FRONT` | page 9 | TRCM ECU: a569 algo wake IMPACT FINISH x FRONT | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a570_AlgoWake_IMPACT_FINISH_X_REAR` | page 9 | TRCM ECU: a570 algo wake IMPACT FINISH x REAR | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a571_AlgoWake_IMPACT_FINISH_Y_RCM_POS` | page 9 | TRCM ECU: a571 algo wake IMPACT FINISH y RCM POS | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a572_AlgoWake_IMPACT_FINISH_Y_RCM_NEG` | page 9 | TRCM ECU: a572 algo wake IMPACT FINISH y RCM NEG | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a573_AlgoWake_IMPACT_FINISH_Y_RCM` | page 9 | TRCM ECU: a573 algo wake IMPACT FINISH y RCM | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a574_AlgoWake_IMPACT_FINISH_ROLL_RIGHT` | page 9 | TRCM ECU: a574 algo wake IMPACT FINISH ROLL RIGHT | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TRCM_a575_AlgoWake_IMPACT_FINISH_ROLL_LEFT` | page 9 | TRCM ECU: a575 algo wake IMPACT FINISH ROLL LEFT | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
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

## Multiplexing

`TRCM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (38 signals), page 1 (57 signals), page 2 (52 signals), page 3 (48 signals), page 4 (51 signals), page 5 (60 signals), page 6 (58 signals), page 7 (60 signals), page 8 (45 signals), page 9 (49 signals), page 10 (32 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TRCM ECU messages (TRCM)](../../trcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
