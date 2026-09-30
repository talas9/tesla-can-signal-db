---
layout: default
title: "VCRIGHT_alertMatrix (0x3C0) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right body controller message: alert matrix. Tesla Model 3 CAN bus message VCRIGHT_alertMatrix (0x3C0) of Right body controller, firmware 2026.26.6.5, 432 signals (VCRIGHT_matrixIndex, VCRIGHT_a001_WatchdogReset, VCRIGHT_a002_PowerLossReset, VCRIGHT_a003_SWAssertion and 428 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_alertMatrix (0x3C0) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Right body controller message: alert matrix; frame length observed on a vehicle bus. This page documents the 432 signals of VCRIGHT_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_alertMatrix` |
| CAN id | 0x3C0 (960) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 432 |

## Signals of VCRIGHT_alertMatrix

Tesla Model 3 CAN bus signals in `VCRIGHT_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_matrixIndex` | selector | Right body controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | plausible |
| `VCRIGHT_a001_WatchdogReset` | page 0 | Right body controller: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a002_PowerLossReset` | page 0 | Right body controller: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a003_SWAssertion` | page 0 | Right body controller: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a005_CANTXError` | page 0 | Right body controller: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a006_CANTX_cyclicError` | page 0 | Right body controller: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a010_ExtSupplyVoltError` | page 0 | Right body controller: a010 ext supply volt error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a012_CPUReset` | page 0 | Right body controller: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a013_AlertManagerFault` | page 0 | Right body controller: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a015_NVMMError` | page 0 | Right body controller: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a016_NVMMRecordError` | page 0 | Right body controller: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a017_NVMMStatusDbg` | page 0 | Right body controller: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a021_TaskSchedulerError` | page 0 | Right body controller: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a022_TaskInitError` | page 0 | Right body controller: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a029_CoreDump` | page 0 | Right body controller: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a030_ECULogUploadRequest` | page 0 | Right body controller: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a031_UDSActive` | page 0 | Right body controller: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a041_HighCPULoad` | page 0 | Right body controller: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a042_HighStackUsage` | page 0 | Right body controller: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a043_Task1msError` | page 0 | Right body controller: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a044_Task10msError` | page 0 | Right body controller: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a045_Task100msError` | page 0 | Right body controller: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a046_Task1000msError` | page 0 | Right body controller: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a057_HVP_MIA` | page 0 | Right body controller: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a058_inputRHighSyncDebug` | page 0 | Right body controller: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a059_inputResistanceHigh` | page 0 | Right body controller: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a060_engineeringBuild` | page 0 | Right body controller: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a061_XCPConnected` | page 1 | Right body controller: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a062_XCPWasConnected` | page 1 | Right body controller: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a063_SwitchFault` | page 1 | Right body controller: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a064_busSleepReqTimeout` | page 1 | Right body controller: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a065_emiosIsrRateLimitedDbg` | page 1 | Right body controller: a065 emios isr rate limited dbg | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a066_emiosIsrShortPeriodDetectedDbg` | page 1 | Right body controller: a066 emios isr short period detected dbg | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a082_VCRIGHT_IPC_MIA` | page 1 | Right body controller: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a083_VCLEFT_IPC_MIA` | page 1 | Right body controller: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a084_TPMS_MIA` | page 1 | Right body controller: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a085_CCCM_MIA` | page 1 | Right body controller: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a086_VCBATT_MIA` | page 1 | Right body controller: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a087_DIREL_MIA` | page 1 | Right body controller: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a088_DIRER_MIA` | page 1 | Right body controller: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a089_IBST_MIA` | page 1 | Right body controller: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a090_APS_MIA` | page 1 | Right body controller: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a091_CMPD_MIA` | page 1 | Right body controller: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a092_VCSEATD_MIA` | page 1 | Right body controller: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a093_VCSEATP_MIA` | page 1 | Right body controller: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a094_EPAS3P_MIA` | page 1 | Right body controller: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a095_CHG_MIA` | page 1 | Right body controller: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a096_OCS1P_MIA` | page 1 | Right body controller: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a097_CMP_MIA` | page 1 | Right body controller: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a098_DIR_MIA` | page 1 | Right body controller: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a099_PARK_MIA` | page 1 | Right body controller: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a100_CANbus_MIA` | page 1 | Right body controller: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a101_PM_MIA` | page 1 | Right body controller: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a102_PTC_MIA` | page 1 | Right body controller: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a103_CP_MIA` | page 1 | Right body controller: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a104_DAS_MIA` | page 1 | Right body controller: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a105_TAS_MIA` | page 1 | Right body controller: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a106_PCS_MIA` | page 1 | Right body controller: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a107_BMS_MIA` | page 1 | Right body controller: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a108_DIF_MIA` | page 1 | Right body controller: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a109_RCM_MIA` | page 1 | Right body controller: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a110_GTW_MIA` | page 1 | Right body controller: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a111_EPBR_MIA` | page 1 | Right body controller: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a112_EPBL_MIA` | page 1 | Right body controller: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a113_UI_MIA` | page 1 | Right body controller: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a114_ESP_MIA` | page 1 | Right body controller: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a115_VCSEC_MIA` | page 1 | Right body controller: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a116_VCRIGHT_MIA` | page 1 | Right body controller: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a117_VCLEFT_MIA` | page 1 | Right body controller: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a118_VCFRONT_MIA` | page 1 | Right body controller: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a119_SCCM_MIA` | page 1 | Right body controller: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a120_DI_DRIVE_MIA` | page 1 | Right body controller: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a121_ETC_MIA` | page 2 | Right body controller: a121 ETC MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a122_ICR_MIA` | page 2 | Right body controller: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a123_VC_SECONDARY_LIGHTING_LEADER_MIA` | page 2 | Right body controller: a123 VC SECONDARY LIGHTING LEADER MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a124_BB_MIA` | page 2 | Right body controller: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a125_RCU_MIA` | page 2 | Right body controller: a125 RCU MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a126_hvacActOpenLoadDBG` | page 2 | Right body controller: a126 hvac act open load DBG | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a127_hvacActOvercurrentDBG` | page 2 | Right body controller: a127 hvac act overcurrent DBG | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a128_hvacActDrvFaultDBG` | page 2 | Right body controller: a128 hvac act drv fault DBG | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a129_hvacIntakeUncalib` | page 2 | Right body controller: a129 hvac intake uncalib | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a130_hvacLHBleedUncalib` | page 2 | Right body controller: a130 hvac LH bleed uncalib | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a131_hvacRHBleedUncalib` | page 2 | Right body controller: a131 hvac RH bleed uncalib | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a132_hvacLHVaneUncalib` | page 2 | Right body controller: a132 hvac LH vane uncalib | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a133_hvacRHVaneUncalib` | page 2 | Right body controller: a133 hvac RH vane uncalib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a134_hvacUpprModeUncalib` | page 2 | Right body controller: a134 hvac uppr mode uncalib | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a135_hvacLowrModeUncalib` | page 2 | Right body controller: a135 hvac lowr mode uncalib | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a136_hvacIntakeFault` | page 2 | Right body controller: a136 hvac intake fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a137_hvacLHBleedFault` | page 2 | Right body controller: a137 hvac LH bleed fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a138_hvacRHBleedFault` | page 2 | Right body controller: a138 hvac RH bleed fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a139_hvacLHVaneFault` | page 2 | Right body controller: a139 hvac LH vane fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a140_hvacRHVaneFault` | page 2 | Right body controller: a140 hvac RH vane fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a141_hvacUpperModeFault` | page 2 | Right body controller: a141 hvac upper mode fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a142_hvacLowerModeFault` | page 2 | Right body controller: a142 hvac lower mode fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a143_mirrorManuallyFolded` | page 2 | Right body controller: a143 mirror manually folded | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a144_evaporatorTempSns` | page 2 | Right body controller: a144 evaporator temp sns | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a145_ductLeftTempSns` | page 2 | Right body controller: a145 duct left temp sns | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a146_ductRightTempSns` | page 2 | Right body controller: a146 duct right temp sns | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a147_incarProbeTempSns` | page 2 | Right body controller: a147 incar probe temp sns | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a148_incarMidTempSns` | page 2 | Right body controller: a148 incar mid temp sns | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a149_incarDeepTempSns` | page 2 | Right body controller: a149 incar deep temp sns | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a150_windowPinchFront` | page 2 | Right body controller: a150 window pinch front | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a151_windowPinchRear` | page 2 | Right body controller: a151 window pinch rear | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a152_windowUncalFront` | page 2 | Right body controller: a152 window uncal front | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a153_windowUncalRear` | page 2 | Right body controller: a153 window uncal rear | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a154_windowThermalFront` | page 2 | Right body controller: a154 window thermal front | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a155_windowThermalRear` | page 2 | Right body controller: a155 window thermal rear | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a156_windowNoInputFront` | page 2 | Right body controller: a156 window no input front | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a157_windowNoInputRear` | page 2 | Right body controller: a157 window no input rear | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a158_windowPinchOverideF` | page 2 | Right body controller: a158 window pinch overide f | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a159_windowPinchOverideR` | page 2 | Right body controller: a159 window pinch overide r | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a160_windowUndercurrentF` | page 2 | Right body controller: a160 window undercurrent f | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a161_windowUndercurrentR` | page 2 | Right body controller: a161 window undercurrent r | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a162_windowEncoderStallF` | page 2 | Right body controller: a162 window encoder stall f | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a163_windowEncoderStallR` | page 2 | Right body controller: a163 window encoder stall r | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a164_windowFactoryTest` | page 2 | Right body controller: a164 window factory test | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a165_windowFactoryTest2` | page 2 | Right body controller: a165 window factory test2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a166_windowDebug` | page 2 | Right body controller: a166 window debug | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a167_windowDebugPinchF` | page 2 | Right body controller: a167 window debug pinch f | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a168_windowDebugPinchR` | page 2 | Right body controller: a168 window debug pinch r | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a169_windowCurrentPeakF` | page 2 | Right body controller: a169 window current peak f | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a170_windowCurrentPeakR` | page 2 | Right body controller: a170 window current peak r | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a171_hvacRearUncalib` | page 2 | Right body controller: a171 hvac rear uncalib | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a172_SPI_MIA` | page 2 | Right body controller: a172 SPI MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a173_windowBtnDoorOpen` | page 2 | Right body controller: a173 window btn door open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a174_BLERightPowerCycled` | page 2 | Right body controller: a174 BLE right power cycled | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a175_windowSealDefectFront` | page 2 | Right body controller: a175 window seal defect front | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a176_windowSealDefectRear` | page 2 | Right body controller: a176 window seal defect rear | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a177_hvacRearFault` | page 2 | Right body controller: a177 hvac rear fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a178_trunkSwitchVCBATTMIA` | page 2 | Right body controller: a178 trunk switch VCBATTMIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a179_trunkSwitchVCFRONTMIA` | page 2 | Right body controller: a179 trunk switch VCFRONTMIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a180_frontDoorLatchRehome` | page 2 | Right body controller: a180 front door latch rehome | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a181_rearDoorLatchRehome` | page 3 | Right body controller: a181 rear door latch rehome | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a182_emergencyLatchRel` | page 3 | Right body controller: a182 emergency latch rel | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a183_doorStateFactoryTest` | page 3 | Right body controller: a183 door state factory test | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a184_trunkFailedOpening` | page 3 | Right body controller: a184 trunk failed opening | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a185_summonAborted` | page 3 | Right body controller: a185 summon aborted | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a186_latchReleaseFailedF` | page 3 | Right body controller: a186 latch release failed f | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a187_latchReleaseFailedR` | page 3 | Right body controller: a187 latch release failed r | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a188_latchUnableToRearmF` | page 3 | Right body controller: a188 latch unable to rearm f | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a189_latchUnableToRearmR` | page 3 | Right body controller: a189 latch unable to rearm r | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a190_eFuseMgmtVbatFused` | page 3 | Right body controller: a190 e fuse mgmt vbat fused | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a191_gloveboxPower` | page 3 | Right body controller: a191 glovebox power | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a192_gloveboxLatchRel` | page 3 | Right body controller: a192 glovebox latch rel | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a193_amplifierEFuseFault` | page 3 | Right body controller: a193 amplifier e fuse fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a194_cntctrPwrEFuseFault` | page 3 | Right body controller: a194 cntctr pwr e fuse fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a195_hvcEFuseFault` | page 3 | Right body controller: a195 hvc e fuse fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a196_VEHCANOverterminate` | page 3 | Right body controller: a196 VEHCAN overterminate | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a197_VEHCANUndertrminate` | page 3 | Right body controller: a197 VEHCAN undertrminate | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a198_PRVCANOverterminate` | page 3 | Right body controller: a198 PRVCAN overterminate | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a199_PRVCANUndertrminate` | page 3 | Right body controller: a199 PRVCAN undertrminate | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a200_motorPhantomEncoder` | page 3 | Right body controller: a200 motor phantom encoder | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a201_motorDutyEncDisabl` | page 3 | Right body controller: a201 motor duty enc disabl | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a202_epbmUnderIStatic` | page 3 | Right body controller: a202 epbm under i static | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a203_epbmOverIStatic` | page 3 | Right body controller: a203 epbm over i static | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a204_epbmUnderIDyn` | page 3 | Right body controller: a204 epbm under i dyn | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a205_epbmOverIDyn` | page 3 | Right body controller: a205 epbm over i dyn | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a206_epbWrongDirection` | page 3 | Right body controller: a206 epb wrong direction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a207_epbmEnableWrong` | page 3 | Right body controller: a207 epbm enable wrong | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a208_epbFaulted` | page 3 | Right body controller: a208 epb faulted | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a209_epbStateMisTime` | page 3 | Right body controller: a209 epb state mis time | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a210_epbStateTime` | page 3 | Right body controller: a210 epb state time | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a211_epbmUnderIStaticNew` | page 3 | Right body controller: a211 epbm under i static new | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a212_epbmOverIStaticNew` | page 3 | Right body controller: a212 epbm over i static new | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a213_epbmUnderIDynNew` | page 3 | Right body controller: a213 epbm under i dyn new | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a214_epbmOverIDynNew` | page 3 | Right body controller: a214 epbm over i dyn new | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a215_currentDesyncWarning` | page 3 | Right body controller: a215 current desync warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a216_SPI_MIA_debugData1` | page 3 | Right body controller: a216 SPI MIA debug data1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a217_SPI_MIA_debugData2` | page 3 | Right body controller: a217 SPI MIA debug data2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a218_motorDriverFault` | page 3 | Right body controller: a218 motor driver fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a219_motorCurrentDropout` | page 3 | Right body controller: a219 motor current dropout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a220_reverseLightFaultUser` | page 3 | Right body controller: a220 reverse light fault user | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a221_undervoltageLoadshedTriggered` | page 3 | Right body controller: a221 undervoltage loadshed triggered | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a222_rearFasciaFogLightFaultUser` | page 3 | Right body controller: a222 rear fascia fog light fault user | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a223_VCBATT1_MIA` | page 3 | Right body controller: a223 VCBATT1 MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a224_seatEncStallTrack` | page 3 | Right body controller: a224 seat enc stall track | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a225_seatEncStallBack` | page 3 | Right body controller: a225 seat enc stall back | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a226_seatEncStallTilt` | page 3 | Right body controller: a226 seat enc stall tilt | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a227_seatEncStallLift` | page 3 | Right body controller: a227 seat enc stall lift | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a228_seatEncOverTrack` | page 3 | Right body controller: a228 seat enc over track | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a229_seatEncOverBack` | page 3 | Right body controller: a229 seat enc over back | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a230_seatEncOverTilt` | page 3 | Right body controller: a230 seat enc over tilt | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a231_seatEncOverLift` | page 3 | Right body controller: a231 seat enc over lift | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a232_seatCurrUnderTrack` | page 3 | Right body controller: a232 seat curr under track | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a233_seatCurrUnderBack` | page 3 | Right body controller: a233 seat curr under back | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a234_seatCurrUnderTilt` | page 3 | Right body controller: a234 seat curr under tilt | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a235_seatCurrUnderLift` | page 3 | Right body controller: a235 seat curr under lift | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a236_lumbarOverPresA` | page 3 | Right body controller: a236 lumbar over pres a | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a237_lumbarOverPresB` | page 3 | Right body controller: a237 lumbar over pres b | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a238_lumbarValveMIA` | page 3 | Right body controller: a238 lumbar valve MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a239_seatHeatIFront` | page 3 | Right body controller: a239 seat heat i front | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a240_seatHeatShortFront` | page 3 | Right body controller: a240 seat heat short front | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a241_seatHeatMIAFront` | page 4 | Right body controller: a241 seat heat MIA front | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a242_seatHeatIRearL` | page 4 | Right body controller: a242 seat heat i rear l | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a243_seatHeatShortRearL` | page 4 | Right body controller: a243 seat heat short rear l | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a244_seatHeatMIARearL` | page 4 | Right body controller: a244 seat heat MIA rear l | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a245_seatHeatIRearC` | page 4 | Right body controller: a245 seat heat i rear c | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a246_seatHeatShortRearC` | page 4 | Right body controller: a246 seat heat short rear c | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a247_seatHeatMIARearC` | page 4 | Right body controller: a247 seat heat MIA rear c | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a248_seatHeatIRearR` | page 4 | Right body controller: a248 seat heat i rear r | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a249_seatHeatShortRearR` | page 4 | Right body controller: a249 seat heat short rear r | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a250_seatHeatMIARearR` | page 4 | Right body controller: a250 seat heat MIA rear r | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a251_seatUncalTrack` | page 4 | Right body controller: a251 seat uncal track | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a252_seatUncalBack` | page 4 | Right body controller: a252 seat uncal back | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a253_seatUncalTilt` | page 4 | Right body controller: a253 seat uncal tilt | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a254_seatUncalLift` | page 4 | Right body controller: a254 seat uncal lift | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a255_PTCOverTemp` | page 4 | Right body controller: a255 PTC over temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a256_PTCCurrentDrawNoReq` | page 4 | Right body controller: a256 PTC current draw no req | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a257_THSMIA` | page 4 | Right body controller: a257 THSMIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a258_PTCStuckInBoot` | page 4 | Right body controller: a258 PTC stuck in boot | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a259_latchDisarmDelayF` | page 4 | Right body controller: a259 latch disarm delay f | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a260_latchDisarmDelayR` | page 4 | Right body controller: a260 latch disarm delay r | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a261_emergencyLatchRelRear` | page 4 | Right body controller: a261 emergency latch rel rear | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a262_PTCFaulted` | page 4 | Right body controller: a262 PTC faulted | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a263_seatTrackStallDebug` | page 4 | Right body controller: a263 seat track stall debug | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a264_seatBackStallDebug` | page 4 | Right body controller: a264 seat back stall debug | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a265_seatTiltStallDebug` | page 4 | Right body controller: a265 seat tilt stall debug | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a266_seatLiftStallDebug` | page 4 | Right body controller: a266 seat lift stall debug | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a267_seatTrackHCEncStlDbg` | page 4 | Right body controller: a267 seat track HC enc stl dbg | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a268_seatBackHCEncStlDbg` | page 4 | Right body controller: a268 seat back HC enc stl dbg | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a269_seatTiltHCEncStlDbg` | page 4 | Right body controller: a269 seat tilt HC enc stl dbg | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a270_seatLiftHCEncStlDbg` | page 4 | Right body controller: a270 seat lift HC enc stl dbg | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a271_THSSensorFault` | page 4 | Right body controller: a271 THS sensor fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a272_vhclPwrStateMsmtch` | page 4 | Right body controller: a272 vhcl pwr state msmtch | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a273_handleStuckActiveF` | page 4 | Right body controller: a273 handle stuck active f | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a274_handleStuckActiveR` | page 4 | Right body controller: a274 handle stuck active r | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a275_rightTurnLightFault` | page 4 | Right body controller: a275 right turn light fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a276_mirrorDebug` | page 4 | Right body controller: a276 mirror debug | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a277_BLERightUnderVoltage` | page 4 | Right body controller: a277 BLE right under voltage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a278_hvacPtcHeatingUnavailable` | page 4 | Right body controller: a278 hvac ptc heating unavailable | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a279_trunkFailedToClose` | page 4 | Right body controller: a279 trunk failed to close | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a280_latchDidNotDisarmF` | page 4 | Right body controller: a280 latch did not disarm f | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a281_latchDidNotDisarmR` | page 4 | Right body controller: a281 latch did not disarm r | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a282_latchUnexpectedArmF` | page 4 | Right body controller: a282 latch unexpected arm f | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a283_latchUnexpectedArmR` | page 4 | Right body controller: a283 latch unexpected arm r | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a284_gloveboxUnderCurrentDetected` | page 4 | Right body controller: a284 glovebox under current detected | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a285_gloveboxOverCurrentDetected` | page 4 | Right body controller: a285 glovebox over current detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a286_windowSpeedInvalidF` | page 4 | Right body controller: a286 window speed invalid f | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a287_windowSpeedInvalidR` | page 4 | Right body controller: a287 window speed invalid r | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a288_handlePWMPeriodF` | page 4 | Right body controller: a288 handle PWM period f | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a289_handlePWMPeriodR` | page 4 | Right body controller: a289 handle PWM period r | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a290_occupancyFaultedFront` | page 4 | Right body controller: a290 occupancy faulted front | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a291_buckleFaultedFront` | page 4 | Right body controller: a291 buckle faulted front | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a292_buckleFaultedRearC` | page 4 | Right body controller: a292 buckle faulted rear c | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a293_buckleFaultedRearR` | page 4 | Right body controller: a293 buckle faulted rear r | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a294_occupancyFaultedRearR` | page 4 | Right body controller: a294 occupancy faulted rear r | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a295_occupancyFaulted3RowL` | page 4 | Right body controller: a295 occupancy faulted3 row l | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a296_occupancyFaulted3RowR` | page 4 | Right body controller: a296 occupancy faulted3 row r | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a297_seatBelowMinPumpTmp` | page 4 | Right body controller: a297 seat below min pump tmp | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a298_buckleFaulted3RowL` | page 4 | Right body controller: a298 buckle faulted3 row l | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a299_buckleFaulted3RowR` | page 4 | Right body controller: a299 buckle faulted3 row r | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a300_VCFRONT1_MIA` | page 4 | Right body controller: a300 VCFRONT1 MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a301_airwaveRightVerticalWarning` | page 5 | Right body controller: a301 airwave right vertical warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a302_airwaveRightVerticalUnavailable` | page 5 | Right body controller: a302 airwave right vertical unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a303_eFuseMgmtWindowLift` | page 5 | Right body controller: a303 e fuse mgmt window lift | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a304_frontIntHandleUnexpectedVoltage` | page 5 | Right body controller: a304 front int handle unexpected voltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a305_rearIntHandleUnexpectedVoltage` | page 5 | Right body controller: a305 rear int handle unexpected voltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a306_handleDisconnectedF` | page 5 | Right body controller: a306 handle disconnected f | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a307_handleDisconnectedR` | page 5 | Right body controller: a307 handle disconnected r | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a308_airwaveRightLateralUnavailable` | page 5 | Right body controller: a308 airwave right lateral unavailable | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a310_mirrorFoldStall` | page 5 | Right body controller: a310 mirror fold stall | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a311_rightBrakeLightFault` | page 5 | Right body controller: a311 right brake light fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a312_rightTailLightFault` | page 5 | Right body controller: a312 right tail light fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a313_rightFootwellLightFault` | page 5 | Right body controller: a313 right footwell light fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a314_rightMapPocketLightFault` | page 5 | Right body controller: a314 right map pocket light fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a315_rightInteriorTrunkLightFault` | page 5 | Right body controller: a315 right interior trunk light fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a316_mirrorPrematureFoldStall` | page 5 | Right body controller: a316 mirror premature fold stall | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a317_epbmLimpModeEnabled` | page 5 | Right body controller: a317 epbm limp mode enabled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a318_leftExteriorTrunkLightFault` | page 5 | Right body controller: a318 left exterior trunk light fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a319_rightExteriorTrunkLightFault` | page 5 | Right body controller: a319 right exterior trunk light fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a320_windowReportCrackedAtTrimClear` | page 5 | Right body controller: a320 window report cracked at trim clear | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a321_windowRezeroedDebugF` | page 5 | Right body controller: a321 window rezeroed debug f | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a322_windowRezeroedDebugR` | page 5 | Right body controller: a322 window rezeroed debug r | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a323_mirrorCalibrated` | page 5 | Right body controller: a323 mirror calibrated | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a324_mirrorHeatFault` | page 5 | Right body controller: a324 mirror heat fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a325_airwaveLeftVerticalUnavailable` | page 5 | Right body controller: a325 airwave left vertical unavailable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a326_airwaveLeftLateralUnavailable` | page 5 | Right body controller: a326 airwave left lateral unavailable | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a327_airwaveLeftLateralWarning` | page 5 | Right body controller: a327 airwave left lateral warning | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a328_airwaveLeftVerticalWarning` | page 5 | Right body controller: a328 airwave left vertical warning | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a329_airwaveRightLateralWarning` | page 5 | Right body controller: a329 airwave right lateral warning | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a330_shortDropFailedF` | page 5 | Right body controller: a330 short drop failed f | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a331_shortDropFailedR` | page 5 | Right body controller: a331 short drop failed r | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a336_windowDropRevThermalF` | page 5 | Right body controller: a336 window drop rev thermal f | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a337_windowDropRevThermalR` | page 5 | Right body controller: a337 window drop rev thermal r | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a342_rearDefrostDisabled` | page 5 | Right body controller: a342 rear defrost disabled | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a343_rearDefrostUndercurrent` | page 5 | Right body controller: a343 rear defrost undercurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a344_rearDefrostOvercurrent` | page 5 | Right body controller: a344 rear defrost overcurrent | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a345_HVACPTCHeaterPwrEFuseFault` | page 5 | Right body controller: a345 HVACPTC heater pwr e fuse fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a346_cabinRadarEFuseFault` | page 5 | Right body controller: a346 cabin radar e fuse fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a347_nonContMonitorClearedDBG` | page 5 | Right body controller: a347 non cont monitor cleared DBG | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a352_audioCurrentSpikeData` | page 5 | Right body controller: a352 audio current spike data | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a355_hvacLHBleedWarning` | page 5 | Right body controller: a355 hvac LH bleed warning | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a356_hvacRHBleedWarning` | page 5 | Right body controller: a356 hvac RH bleed warning | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a357_hvacLHVaneWarning` | page 5 | Right body controller: a357 hvac LH vane warning | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a358_hvacRHVaneWarning` | page 5 | Right body controller: a358 hvac RH vane warning | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a359_hvacUpperModeWarning` | page 5 | Right body controller: a359 hvac upper mode warning | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a360_detectedStationaryWhileMoving` | page 5 | Right body controller: a360 detected stationary while moving | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a361_stationaryThresholdsIncorrect` | page 6 | Right body controller: a361 stationary thresholds incorrect | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a362_movingThresholdsIncorrect` | page 6 | Right body controller: a362 moving thresholds incorrect | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a363_hvacLowerModeWarning` | page 6 | Right body controller: a363 hvac lower mode warning | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a364_hvacIntakeWarning` | page 6 | Right body controller: a364 hvac intake warning | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a365_pitchUnlatchDisabled` | page 6 | Right body controller: a365 pitch unlatch disabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a366_trunkLatchUnhomed` | page 6 | Right body controller: a366 trunk latch unhomed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a367_trunkLatchSwFault` | page 6 | Right body controller: a367 trunk latch sw fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a368_ductLeftLowerTempSns` | page 6 | Right body controller: a368 duct left lower temp sns | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a369_ductRightLowerTempSns` | page 6 | Right body controller: a369 duct right lower temp sns | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a370_seat2RowPitchUnlatched` | page 6 | Right body controller: a370 seat2 row pitch unlatched | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a371_seat2RowTrackUnlatched` | page 6 | Right body controller: a371 seat2 row track unlatched | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a372_seat2RowBackrestUnlatched` | page 6 | Right body controller: a372 seat2 row backrest unlatched | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a373_windowSwOpenReqInDogMode` | page 6 | Right body controller: a373 window sw open req in dog mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a375_windowPinchOverrideNudge` | page 6 | Right body controller: a375 window pinch override nudge | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a376_seat2RowBridgeCurrentExceeded` | page 6 | Right body controller: a376 seat2 row bridge current exceeded | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a377_ambientTempSns` | page 6 | Right body controller: a377 ambient temp sns | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a378_ductLeftUpperTempSns` | page 6 | Right body controller: a378 duct left upper temp sns | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a379_ductRightUpperTempSns` | page 6 | Right body controller: a379 duct right upper temp sns | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a380_reverseLightFault` | page 6 | Right body controller: a380 reverse light fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a381_rearFogLightFault` | page 6 | Right body controller: a381 rear fog light fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a382_leftLiftgateTailLightFault` | page 6 | Right body controller: a382 left liftgate tail light fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a383_hvacRearWarning` | page 6 | Right body controller: a383 hvac rear warning | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a385_glareShieldHeaterUnavailable` | page 6 | Right body controller: a385 glare shield heater unavailable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a406_aptivOCSMIA` | page 6 | Right body controller: a406 aptiv OCSMIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a407_aptivOCSInterfaceError` | page 6 | Right body controller: a407 aptiv OCS interface error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a408_aptivOCSDeviceError` | page 6 | Right body controller: a408 aptiv OCS device error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a409_aptivOCSDeviceErrorDebug` | page 6 | Right body controller: a409 aptiv OCS device error debug | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a411_undervoltageSelfTestFailure` | page 6 | Right body controller: a411 undervoltage self test failure | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a412_rightBrakeTailLightFault` | page 6 | Right body controller: a412 right brake tail light fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a413_centerHighMountStopLightFault` | page 6 | Right body controller: a413 center high mount stop light fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a414_rearFasciaReverseLightFault` | page 6 | Right body controller: a414 rear fascia reverse light fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a415_rearFasciaFogLightFault` | page 6 | Right body controller: a415 rear fascia fog light fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a416_rearFasciaTailLightFault` | page 6 | Right body controller: a416 rear fascia tail light fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a417_rearFasciaLeftTurnLightFault` | page 6 | Right body controller: a417 rear fascia left turn light fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a418_rearFasciaRightTurnLightFault` | page 6 | Right body controller: a418 rear fascia right turn light fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a419_tailFasciaLeftLightFault` | page 6 | Right body controller: a419 tail fascia left light fault | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a420_tailFasciaRightLightFault` | page 6 | Right body controller: a420 tail fascia right light fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a421_leftTailLightFault` | page 7 | Right body controller: a421 left tail light fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a422_undervoltageSelfTestStuckOff` | page 7 | Right body controller: a422 undervoltage self test stuck off | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a426_seatAbuseMotorWarn` | page 7 | Right body controller: a426 seat abuse motor warn | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a427_seatAbuseMotorStop` | page 7 | Right body controller: a427 seat abuse motor stop | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a428_seatAbuseBufferWarn` | page 7 | Right body controller: a428 seat abuse buffer warn | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a429_seatAbuseBufferFull` | page 7 | Right body controller: a429 seat abuse buffer full | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a444_drv8703Fault` | page 7 | Right body controller: a444 drv8703 fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a445_drv8703SpiFaultDBG` | page 7 | Right body controller: a445 drv8703 spi fault DBG | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a446_cabinHVACUnavailableContext` | page 7 | Right body controller: a446 cabin HVAC unavailable context | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a448_manualHVACAlert` | page 7 | Right body controller: a448 manual HVAC alert | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a450_ptcForcedOutOfSeqRod` | page 7 | Right body controller: a450 ptc forced out of seq rod | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a451_ptcSeqRodOutOfRetries` | page 7 | Right body controller: a451 ptc seq rod out of retries | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a454_ptcHeaterBadRodDetected` | page 7 | Right body controller: a454 ptc heater bad rod detected | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a482_NCV77XXFault` | page 8 | Right body controller: a482 NCV77 XX fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a483_rightTurnLightFaultUser` | page 8 | Right body controller: a483 right turn light fault user | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a484_rightBrakeLightFaultUser` | page 8 | Right body controller: a484 right brake light fault user | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a485_leftTailLightFaultUser` | page 8 | Right body controller: a485 left tail light fault user | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a486_rightTailLightFaultUser` | page 8 | Right body controller: a486 right tail light fault user | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a487_centerHighMountStopLightFaultUser` | page 8 | Right body controller: a487 center high mount stop light fault user | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a488_undervoltageSelfTestStuckOnDebug` | page 8 | Right body controller: a488 undervoltage self test stuck on debug | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a489_undervoltageSelfTestStuckOn` | page 8 | Right body controller: a489 undervoltage self test stuck on | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a490_vehicleOccupiedOnOTAStart` | page 8 | Right body controller: a490 vehicle occupied on OTA start | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a491_BPillarCameraHeaterFault` | page 8 | Right body controller: a491 b pillar camera heater fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a492_uvSelfTestLoadUnattemptedOnDbg` | page 8 | Right body controller: a492 uv self test load unattempted on dbg | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a496_gloveboxOpenFailed` | page 8 | Right body controller: a496 glovebox open failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a497_CANMsgMACVerificationKeyNotProvisioned` | page 8 | Right body controller: a497 CAN msg MAC verification key not provisioned | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a498_CANMsgMACVerificationFailure` | page 8 | Right body controller: a498 CAN msg MAC verification failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a499_epbmInvalidateCdp` | page 8 | Right body controller: a499 epbm invalidate cdp | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a510_3RowSeatUncalibrated` | page 8 | Right body controller: a510 3 row seat uncalibrated | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a511_3RowSeatPositionNonsensical` | page 8 | Right body controller: a511 3 row seat position nonsensical | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a512_3RowSeatAbsPosOffsetApplied` | page 8 | Right body controller: a512 3 row seat abs pos offset applied | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a513_3RowSeatObstacleDetected` | page 8 | Right body controller: a513 3 row seat obstacle detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a514_3RowSeatTempHigh` | page 8 | Right body controller: a514 3 row seat temp high | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a515_3RowSeatAbsPosSensorTransitionDbg` | page 8 | Right body controller: a515 3 row seat abs pos sensor transition dbg | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a516_3RowSeatStatsFromLastStateDbg` | page 8 | Right body controller: a516 3 row seat stats from last state dbg | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a517_3RowSeatRequestWhileUncalibrated` | page 8 | Right body controller: a517 3 row seat request while uncalibrated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a518_3RowSeatClashAvoidanceBlocked` | page 8 | Right body controller: a518 3 row seat clash avoidance blocked | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a519_3RowSeatOverfolded` | page 8 | Right body controller: a519 3 row seat overfolded | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a520_configMismatch` | page 8 | Right body controller: a520 config mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a525_LVBatterySWMisconfiguration` | page 8 | Right body controller: a525 LV battery SW misconfiguration | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a526_pcbaOverTemperature` | page 8 | Right body controller: a526 pcba over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a527_continuousFeedUnexpectedVoltage` | page 8 | Right body controller: a527 continuous feed unexpected voltage | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a528_unableToRunStuckOnTest` | page 8 | Right body controller: a528 unable to run stuck on test | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a529_airflowFeedBackModelError` | page 8 | Right body controller: a529 airflow feed back model error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a531_airflowModelTmpCompDisabled` | page 8 | Right body controller: a531 airflow model tmp comp disabled | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a532_airflowModelFeedForwardError` | page 8 | Right body controller: a532 airflow model feed forward error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a533_cabinModelDebug` | page 8 | Right body controller: a533 cabin model debug | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a537_solarCalcsNotNominal` | page 8 | Right body controller: a537 solar calcs not nominal | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a538_hvacSystemNotNominal` | page 8 | Right body controller: a538 hvac system not nominal | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a539_dogModeMonitorTrip` | page 8 | Right body controller: a539 dog mode monitor trip | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a540_hvacActuatorDitherDebug` | page 8 | Right body controller: a540 hvac actuator dither debug | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a542_steeringWheelHeatingInhibited` | page 9 | Right body controller: a542 steering wheel heating inhibited | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a545_LVBatteryTypeUnknown` | page 9 | Right body controller: a545 LV battery type unknown | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a546_mirrorFoldTypeChanged` | page 9 | Right body controller: a546 mirror fold type changed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a550_ambientTempDelta` | page 9 | Right body controller: a550 ambient temp delta | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a551_interiorDoorRequestInhibited` | page 9 | Right body controller: a551 interior door request inhibited | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a555_RCM2_MIA` | page 9 | Right body controller: a555 RCM2 MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a556_rcmReportedOCSError` | page 9 | Right body controller: a556 rcm reported OCS error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a560_2RowSeatUncalibrated` | page 9 | Right body controller: a560 2 row seat uncalibrated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a561_2RowSeatPositionNonsensical` | page 9 | Right body controller: a561 2 row seat position nonsensical | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a562_2RowSeatAbsPosOffsetApplied` | page 9 | Right body controller: a562 2 row seat abs pos offset applied | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a563_2RowSeatObstacleDetected` | page 9 | Right body controller: a563 2 row seat obstacle detected | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a564_2RowSeatTempHigh` | page 9 | Right body controller: a564 2 row seat temp high | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a565_2RowSeatAbsPosSensorTransitionDbg` | page 9 | Right body controller: a565 2 row seat abs pos sensor transition dbg | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a566_2RowSeatStatsFromLastStateDbg` | page 9 | Right body controller: a566 2 row seat stats from last state dbg | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a567_2RowSeatRequestWhileUncalibrated` | page 9 | Right body controller: a567 2 row seat request while uncalibrated | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a568_2RowSeatClashAvoidanceBlocked` | page 9 | Right body controller: a568 2 row seat clash avoidance blocked | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a569_2RowSeatOverfolded` | page 9 | Right body controller: a569 2 row seat overfolded | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a570_seatHeatDisabledF` | page 9 | Right body controller: a570 seat heat disabled f | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a571_seatHeatDisabledRearL` | page 9 | Right body controller: a571 seat heat disabled rear l | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a572_seatHeatDisabledRearC` | page 9 | Right body controller: a572 seat heat disabled rear c | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a573_seatHeatDisabledRearR` | page 9 | Right body controller: a573 seat heat disabled rear r | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a574_2RowSeatStatsFromLastStateDbg2` | page 9 | Right body controller: a574 2 row seat stats from last state dbg2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a575_3RowSeatStatsFromLastStateDbg2` | page 9 | Right body controller: a575 3 row seat stats from last state dbg2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a577_bsiHardwareIssue` | page 9 | Right body controller: a577 bsi hardware issue | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a578_RGBLightFault` | page 9 | Right body controller: a578 RGB light fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a579_liftgateFollowerUnexpectedStop` | page 9 | Right body controller: a579 liftgate follower unexpected stop | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a580_debugLiftgateFollowerCurrentSpike` | page 9 | Right body controller: a580 debug liftgate follower current spike | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a583_doorRemoteUnlatchedFront` | page 9 | Right body controller: a583 door remote unlatched front | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a584_doorRemoteUnlatchedRear` | page 9 | Right body controller: a584 door remote unlatched rear | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a585_doorRemoteUnlatchFailedFront` | page 9 | Right body controller: a585 door remote unlatch failed front | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a586_doorRemoteUnlatchFailedRear` | page 9 | Right body controller: a586 door remote unlatch failed rear | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a587_VCSEAT2L_MIA` | page 9 | Right body controller: a587 VCSEAT2 l MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a588_VCSEAT2R_MIA` | page 9 | Right body controller: a588 VCSEAT2 r MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a589_defogSysDriverlessSelfTest` | page 9 | Right body controller: a589 defog sys driverless self test | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a590_seatEncStallThighSupport` | page 9 | Right body controller: a590 seat enc stall thigh support | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a591_seatCurrUnderThighSupport` | page 9 | Right body controller: a591 seat curr under thigh support | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a592_seatUncalThighSupport` | page 9 | Right body controller: a592 seat uncal thigh support | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a593_seatEncOverThighSupport` | page 9 | Right body controller: a593 seat enc over thigh support | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a594_seatThighSupportStallDebug` | page 9 | Right body controller: a594 seat thigh support stall debug | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a595_seatThighSupportHCEncStlDbg` | page 9 | Right body controller: a595 seat thigh support HC enc stl dbg | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a596_frontDoorLatchUnexpectedVoltage` | page 9 | Right body controller: a596 front door latch unexpected voltage | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a597_rearDoorLatchUnexpectedVoltage` | page 9 | Right body controller: a597 rear door latch unexpected voltage | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a598_childModeMonitorTrip` | page 9 | Right body controller: a598 child mode monitor trip | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a599_LVBatteryTypeUnsupported` | page 9 | Right body controller: a599 LV battery type unsupported | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a601_wakeToOpenDoorDbg` | page 10 | Right body controller: a601 wake to open door dbg | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a605_CANMsgMACVerificationKeyMismatch` | page 10 | Right body controller: a605 CAN msg MAC verification key mismatch | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_a617_APP_MIA` | page 10 | Right body controller: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`VCRIGHT_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (26 signals), page 1 (45 signals), page 2 (60 signals), page 3 (60 signals), page 4 (60 signals), page 5 (45 signals), page 6 (37 signals), page 7 (13 signals), page 8 (38 signals), page 9 (44 signals), page 10 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
