---
layout: default
title: "VCFRONT_alertMatrix (0x340) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: alert matrix. Tesla Model 3 / Model Y CAN bus message VCFRONT_alertMatrix (0x340) of Front body controller, firmware 2026.26.6.5, 633 signals (VCFRONT_matrixIndex, VCFRONT_a001_WatchdogReset, VCFRONT_a002_PowerLossReset, VCFRONT_a003_SWAssertion and 629 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_alertMatrix (0x340) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front body controller message: alert matrix; frame length observed on a vehicle bus. This page documents the 633 signals of VCFRONT_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_alertMatrix` |
| CAN id | 0x340 (832) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 633 |

## Signals of VCFRONT_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_matrixIndex` | selector | Front body controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10`<br>11 = `AlertMatrix11` | plausible |
| `VCFRONT_a001_WatchdogReset` | page 0 | Front body controller: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a002_PowerLossReset` | page 0 | Front body controller: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a003_SWAssertion` | page 0 | Front body controller: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a004_adaptiveHeadlightsUnavailable` | page 0 | Front body controller: a004 adaptive headlights unavailable | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a005_CANTXError` | page 0 | Front body controller: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a006_CANTX_cyclicError` | page 0 | Front body controller: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a008_adaptiveHeadlightsUnavailableStalk` | page 0 | Front body controller: a008 adaptive headlights unavailable stalk | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a009_LCCPurgeAttempted` | page 0 | Front body controller: a009 LCC purge attempted | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a010_ExtSupplyVoltError` | page 0 | Front body controller: a010 ext supply volt error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a012_CPUReset` | page 0 | Front body controller: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a013_AlertManagerFault` | page 0 | Front body controller: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a015_NVMMError` | page 0 | Front body controller: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a016_NVMMRecordError` | page 0 | Front body controller: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a017_NVMMStatusDbg` | page 0 | Front body controller: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a021_TaskSchedulerError` | page 0 | Front body controller: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a022_TaskInitError` | page 0 | Front body controller: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a029_CoreDump` | page 0 | Front body controller: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a030_ECULogUploadRequest` | page 0 | Front body controller: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a031_UDSActive` | page 0 | Front body controller: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a032_ipcWatchdogExpired` | page 0 | Front body controller: a032 ipc watchdog expired | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a033_eccNonCorrectableError` | page 0 | Front body controller: a033 ecc non correctable error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a038_ProtFaultInfo` | page 0 | Front body controller: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a039_ProtFaultAddress` | page 0 | Front body controller: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a040_Backtrace` | page 0 | Front body controller: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a041_HighCPULoad` | page 0 | Front body controller: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a042_HighStackUsage` | page 0 | Front body controller: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a043_Task1msError` | page 0 | Front body controller: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a044_Task10msError` | page 0 | Front body controller: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a045_Task100msError` | page 0 | Front body controller: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a046_Task1000msError` | page 0 | Front body controller: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a047_resetReason` | page 0 | Front body controller: a047 reset reason | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a053_wiperCommErrorUser` | page 0 | Front body controller: a053 wiper comm error user | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a054_compressorLowFlowUserFacing` | page 0 | Front body controller: a054 compressor low flow user facing | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a057_HVP_MIA` | page 0 | Front body controller: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a058_inputRHighSyncDebug` | page 0 | Front body controller: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a059_inputResistanceHigh` | page 0 | Front body controller: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a060_engineeringBuild` | page 0 | Front body controller: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a061_XCPConnected` | page 1 | Front body controller: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a062_XCPWasConnected` | page 1 | Front body controller: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a063_SwitchFault` | page 1 | Front body controller: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a064_busSleepReqTimeout` | page 1 | Front body controller: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a082_VCRIGHT_IPC_MIA` | page 1 | Front body controller: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a083_VCLEFT_IPC_MIA` | page 1 | Front body controller: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a084_TPMS_MIA` | page 1 | Front body controller: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a085_CCCM_MIA` | page 1 | Front body controller: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a086_VCBATT_MIA` | page 1 | Front body controller: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a087_DIREL_MIA` | page 1 | Front body controller: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a088_DIRER_MIA` | page 1 | Front body controller: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a089_IBST_MIA` | page 1 | Front body controller: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a090_APS_MIA` | page 1 | Front body controller: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a091_CMPD_MIA` | page 1 | Front body controller: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a092_VCSEATD_MIA` | page 1 | Front body controller: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a093_VCSEATP_MIA` | page 1 | Front body controller: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a094_EPAS3P_MIA` | page 1 | Front body controller: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a095_CHG_MIA` | page 1 | Front body controller: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a096_OCS1P_MIA` | page 1 | Front body controller: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a097_CMP_MIA` | page 1 | Front body controller: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a098_DIR_MIA` | page 1 | Front body controller: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a099_PARK_MIA` | page 1 | Front body controller: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a100_CANbus_MIA` | page 1 | Front body controller: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a101_PM_MIA` | page 1 | Front body controller: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a102_PTC_MIA` | page 1 | Front body controller: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a103_CP_MIA` | page 1 | Front body controller: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a104_DAS_MIA` | page 1 | Front body controller: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a105_TAS_MIA` | page 1 | Front body controller: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a106_PCS_MIA` | page 1 | Front body controller: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a107_BMS_MIA` | page 1 | Front body controller: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a108_DIF_MIA` | page 1 | Front body controller: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a109_RCM_MIA` | page 1 | Front body controller: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a110_GTW_MIA` | page 1 | Front body controller: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a111_EPBR_MIA` | page 1 | Front body controller: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a112_EPBL_MIA` | page 1 | Front body controller: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a113_UI_MIA` | page 1 | Front body controller: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a114_ESP_MIA` | page 1 | Front body controller: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a115_VCSEC_MIA` | page 1 | Front body controller: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a116_VCRIGHT_MIA` | page 1 | Front body controller: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a117_VCLEFT_MIA` | page 1 | Front body controller: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a118_VCFRONT_MIA` | page 1 | Front body controller: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a119_SCCM_MIA` | page 1 | Front body controller: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a120_DI_DRIVE_MIA` | page 1 | Front body controller: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a121_pumpBatICLatchFault` | page 2 | Front body controller: a121 pump bat IC latch fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a122_pumpBatICWarning` | page 2 | Front body controller: a122 pump bat IC warning | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a123_pumpPtICLatchFault` | page 2 | Front body controller: a123 pump pt IC latch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a124_pumpPtICWarning` | page 2 | Front body controller: a124 pump pt IC warning | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a125_thmlFanICLatchFault` | page 2 | Front body controller: a125 thml fan IC latch fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a126_thmlFanICWarning` | page 2 | Front body controller: a126 thml fan IC warning | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a127_vcleftEFuseTrip` | page 2 | Front body controller: a127 vcleft e fuse trip | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a128_vcrightEFuseTrip` | page 2 | Front body controller: a128 vcright e fuse trip | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a129_pcsEFuseTrip` | page 2 | Front body controller: a129 pcs e fuse trip | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a130_epas3pEFuseTrip` | page 2 | Front body controller: a130 epas3p e fuse trip | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a131_epas3sEFuseTrip` | page 2 | Front body controller: a131 epas3s e fuse trip | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a132_iBoosterEFuseTrip` | page 2 | Front body controller: a132 i booster e fuse trip | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a133_espEFuseTrip` | page 2 | Front body controller: a133 esp e fuse trip | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a134_fusedHighEFuseTrip` | page 2 | Front body controller: a134 fused high e fuse trip | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a135_coolantLevelLow` | page 2 | Front body controller: a135 coolant level low | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a136_refrigDischTempSns` | page 2 | Front body controller: a136 refrig disch temp sns | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a137_refrigDischPresSns` | page 2 | Front body controller: a137 refrig disch pres sns | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a138_refrigSuctTempSns` | page 2 | Front body controller: a138 refrig suct temp sns | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a139_refrigSuctPresSns` | page 2 | Front body controller: a139 refrig suct pres sns | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a140_coolantTempPtSns` | page 2 | Front body controller: a140 coolant temp pt sns | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a141_coolantTempBatSns` | page 2 | Front body controller: a141 coolant temp bat sns | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a142_exvMotorFault` | page 2 | Front body controller: a142 exv motor fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a143_pumpBatICTransFault` | page 2 | Front body controller: a143 pump bat IC trans fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a144_pumpPtICTransFault` | page 2 | Front body controller: a144 pump pt IC trans fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a145_thmlFanICTransFault` | page 2 | Front body controller: a145 thml fan IC trans fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a146_pumpBatSoftStall` | page 2 | Front body controller: a146 pump bat soft stall | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a147_pumpPtSoftStall` | page 2 | Front body controller: a147 pump pt soft stall | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a148_thmlFanSoftStall` | page 2 | Front body controller: a148 thml fan soft stall | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a149_BLEFrontPowerCycled` | page 2 | Front body controller: a149 BLE front power cycled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a150_pumpBatLowRPMCBang` | page 2 | Front body controller: a150 pump bat low RPMC bang | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a151_pumpPtLowRPMCBang` | page 2 | Front body controller: a151 pump pt low RPMC bang | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a152_thmlFanLowRPMCBang` | page 2 | Front body controller: a152 thml fan low RPMC bang | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a153_userPresenceDisplayMismatchClrd` | page 2 | Front body controller: a153 user presence display mismatch clrd | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a154_prechargeDCRData1` | page 2 | Front body controller: a154 precharge DCR data1 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a155_prechargeDCRData2` | page 2 | Front body controller: a155 precharge DCR data2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a156_louverBlockage` | page 2 | Front body controller: a156 louver blockage | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a157_louverBreakage` | page 2 | Front body controller: a157 louver breakage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a158_louverDisconnected` | page 2 | Front body controller: a158 louver disconnected | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a159_coolantValveFault` | page 2 | Front body controller: a159 coolant valve fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a160_compressorInhibited` | page 2 | Front body controller: a160 compressor inhibited | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a161_compressorSelfFault` | page 2 | Front body controller: a161 compressor self fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a162_compressorInhibitedContext` | page 2 | Front body controller: a162 compressor inhibited context | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a163_compressorDisabledFSR` | page 2 | Front body controller: a163 compressor disabled FSR | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a164_eFuseLckoutMissing` | page 2 | Front body controller: a164 e fuse lckout missing | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a165_unxpctdEFuseLckout` | page 2 | Front body controller: a165 unxpctd e fuse lckout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a166_rightHCMMIA` | page 2 | Front body controller: a166 right HCMMIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a167_leftHCMMIA` | page 2 | Front body controller: a167 left HCMMIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a168_hcmShortToVBAT` | page 2 | Front body controller: a168 hcm short to VBAT | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a169_hcmPhaseEnableFail` | page 2 | Front body controller: a169 hcm phase enable fail | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a170_hcmUnderVoltage` | page 2 | Front body controller: a170 hcm under voltage | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a171_driveBlckdByMsmtch` | page 2 | Front body controller: a171 drive blckd by msmtch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a172_wsteHtBlckdByMsmtch` | page 2 | Front body controller: a172 wste ht blckd by msmtch | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a173_HVBlckdByMsmtch` | page 2 | Front body controller: a173 HV blckd by msmtch | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a174_driveNotAuthed` | page 2 | Front body controller: a174 drive not authed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a175_ambientTempSns` | page 2 | Front body controller: a175 ambient temp sns | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a176_vehicleInSelfTest` | page 2 | Front body controller: a176 vehicle in self test | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a177_mcuAudioEFuseFault` | page 2 | Front body controller: a177 mcu audio e fuse fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a178_compLiquidPumpOut` | page 2 | Front body controller: a178 comp liquid pump out | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a179_highLVAmpsIntoPCS` | page 2 | Front body controller: a179 high LV amps into PCS | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a180_DCDCNotSupportingLVBus` | page 2 | Front body controller: a180 DCDC not supporting LV bus | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a181_homelinkMIA` | page 3 | Front body controller: a181 homelink MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a182_replaceLVBattery` | page 3 | Front body controller: a182 replace LV battery | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a183_replaceLVBattery2` | page 3 | Front body controller: a183 replace LV battery2 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a184_cabinCoolingPerformanceAbnormal` | page 3 | Front body controller: a184 cabin cooling performance abnormal | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a185_washerFluidLow` | page 3 | Front body controller: a185 washer fluid low | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a186_noDriveChgCableCon` | page 3 | Front body controller: a186 no drive chg cable con | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a187_busesNotSleeping` | page 3 | Front body controller: a187 buses not sleeping | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a188_sleepFailed` | page 3 | Front body controller: a188 sleep failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a189_IBSMIA` | page 3 | Front body controller: a189 IBSMIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a190_linSchedulingInfo` | page 3 | Front body controller: a190 lin scheduling info | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a191_exitDriveLowLVBusVoltage` | page 3 | Front body controller: a191 exit drive low LV bus voltage | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a192_vehicleLoadShed` | page 3 | Front body controller: a192 vehicle load shed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a193_mcuAudioRetry` | page 3 | Front body controller: a193 mcu audio retry | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a194_iBoosterRetry` | page 3 | Front body controller: a194 i booster retry | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a195_drveBlckdVltgeTooHgh` | page 3 | Front body controller: a195 drve blckd vltge too hgh | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a196_discnctdLVBattery` | page 3 | Front body controller: a196 discnctd LV battery | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a197_prechargeDCRData3` | page 3 | Front body controller: a197 precharge DCR data3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a198_PRVCANOverterminate` | page 3 | Front body controller: a198 PRVCAN overterminate | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a199_PRVCANUndertrminate` | page 3 | Front body controller: a199 PRVCAN undertrminate | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a200_vcleftSelfTestFail` | page 3 | Front body controller: a200 vcleft self test fail | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a201_vcrightSelfTestFail` | page 3 | Front body controller: a201 vcright self test fail | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a202_pcsSelfTestFail` | page 3 | Front body controller: a202 pcs self test fail | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a203_epas3pSelfTestFail` | page 3 | Front body controller: a203 epas3p self test fail | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a204_epas3sSelfTestFail` | page 3 | Front body controller: a204 epas3s self test fail | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a205_iBoosterSelfTestFail` | page 3 | Front body controller: a205 i booster self test fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a206_espSelfTestFail` | page 3 | Front body controller: a206 esp self test fail | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a207_vbatFusdSelfTestFail` | page 3 | Front body controller: a207 vbat fusd self test fail | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a208_brakeFluidLow` | page 3 | Front body controller: a208 brake fluid low | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a209_brakeFluidSNA` | page 3 | Front body controller: a209 brake fluid SNA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a210_coolantValveCalib` | page 3 | Front body controller: a210 coolant valve calib | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a211_I2CFault` | page 3 | Front body controller: a211 I2 c fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a212_IBSOverTemp` | page 3 | Front body controller: a212 IBS over temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a213_LVOvercharge` | page 3 | Front body controller: a213 LV overcharge | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a214_ptPumpCompromised` | page 3 | Front body controller: a214 pt pump compromised | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a215_ptPumpMIA` | page 3 | Front body controller: a215 pt pump MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a216_powerCutoffImminent` | page 3 | Front body controller: a216 power cutoff imminent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a217_battPumpCompromised` | page 3 | Front body controller: a217 batt pump compromised | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a218_socMonitorDetectedThresholdSoc` | page 3 | Front body controller: a218 soc monitor detected threshold soc | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a219_LVVoltFloorRchd` | page 3 | Front body controller: a219 LV volt floor rchd | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a220_reverseBatteryFault` | page 3 | Front body controller: a220 reverse battery fault | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a221_leftTurnLightFault` | page 3 | Front body controller: a221 left turn light fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a222_rightTurnLightFault` | page 3 | Front body controller: a222 right turn light fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a223_12VTempSensDiscnect` | page 3 | Front body controller: a223 12 v temp sens discnect | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a224_revBatChrgPmpFault` | page 3 | Front body controller: a224 rev bat chrg pmp fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a225_driveBlckdByShowroom` | page 3 | Front body controller: a225 drive blckd by showroom | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a226_battPumpMIA` | page 3 | Front body controller: a226 batt pump MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a227_radFanCompromised` | page 3 | Front body controller: a227 rad fan compromised | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a228_pumpBatFbkSanity` | page 3 | Front body controller: a228 pump bat fbk sanity | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a229_pumpPtFbkSanity` | page 3 | Front body controller: a229 pump pt fbk sanity | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a230_thmlFanFbkSanity` | page 3 | Front body controller: a230 thml fan fbk sanity | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a231_12VTempSensShort` | page 3 | Front body controller: a231 12 v temp sens short | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a232_lowSideControllerHighFdbk` | page 3 | Front body controller: a232 low side controller high fdbk | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a233_autopilot1EFuseFault` | page 3 | Front body controller: a233 autopilot1 e fuse fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a234_autopilot2EFuseFault` | page 3 | Front body controller: a234 autopilot2 e fuse fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a235_ptTempSnsIrrational` | page 3 | Front body controller: a235 pt temp sns irrational | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a236_batTempSnsIrrational` | page 3 | Front body controller: a236 bat temp sns irrational | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a237_pumpBatChipComms` | page 3 | Front body controller: a237 pump bat chip comms | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a238_pumpPtChipComms` | page 3 | Front body controller: a238 pump pt chip comms | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a239_thmlFanChipComms` | page 3 | Front body controller: a239 thml fan chip comms | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a240_lowSideCompromised` | page 3 | Front body controller: a240 low side compromised | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a241_radFanMIA` | page 4 | Front body controller: a241 rad fan MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a242_drveBlckdVltgeTooLow` | page 4 | Front body controller: a242 drve blckd vltge too low | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a243_LVOverchargeInstc` | page 4 | Front body controller: a243 LV overcharge instc | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a244_sleepBypassFault` | page 4 | Front body controller: a244 sleep bypass fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a245_pump1EFuseFault` | page 4 | Front body controller: a245 pump1 e fuse fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a246_pump2EFuseFault` | page 4 | Front body controller: a246 pump2 e fuse fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a247_evapSolenoidFault` | page 4 | Front body controller: a247 evap solenoid fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a248_voltageOutOfSpec` | page 4 | Front body controller: a248 voltage out of spec | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a249_coolantValveBadMode` | page 4 | Front body controller: a249 coolant valve bad mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a250_headlampsNotAimed` | page 4 | Front body controller: a250 headlamps not aimed | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a251_UIWakeupTrigger` | page 4 | Front body controller: a251 UI wakeup trigger | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a252_controllerWakeup` | page 4 | Front body controller: a252 controller wakeup | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a253_maxChrgeSssionTmeout` | page 4 | Front body controller: a253 max chrge sssion tmeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a254_pumpBatStopped` | page 4 | Front body controller: a254 pump bat stopped | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a255_pumpPtStopped` | page 4 | Front body controller: a255 pump pt stopped | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a256_compTornShaftSeal` | page 4 | Front body controller: a256 comp torn shaft seal | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a257_portExpanderVOR` | page 4 | Front body controller: a257 port expander VOR | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a258_resistanceEstimationRun` | page 4 | Front body controller: a258 resistance estimation run | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a259_LVVoltageDropOnHighLoadCurrent` | page 4 | Front body controller: a259 LV voltage drop on high load current | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a260_deadLVBattery` | page 4 | Front body controller: a260 dead LV battery | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a261_vcleftVoltageMismatch` | page 4 | Front body controller: a261 vcleft voltage mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a262_vcrightVoltageMismatch` | page 4 | Front body controller: a262 vcright voltage mismatch | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a263_pcsVoltageMismatch` | page 4 | Front body controller: a263 pcs voltage mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a264_iBoosterVoltageMismatch` | page 4 | Front body controller: a264 i booster voltage mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a265_ESPVoltageMismatch` | page 4 | Front body controller: a265 ESP voltage mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a266_EPAS3pVoltageMismatch` | page 4 | Front body controller: a266 epas3p voltage mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a267_EPAS3sVoltageMismatch` | page 4 | Front body controller: a267 epas3s voltage mismatch | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a268_vbatFusedVoltageMismatch` | page 4 | Front body controller: a268 vbat fused voltage mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a269_drveBlckdVltgeTooLow2` | page 4 | Front body controller: a269 drve blckd vltge too low2 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a270_prechargeFailed` | page 4 | Front body controller: a270 precharge failed | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a271_LVBatteryPermSupported` | page 4 | Front body controller: a271 LV battery perm supported | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a273_wiperFrictionModelFault` | page 4 | Front body controller: a273 wiper friction model fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a274_failureToPrechargeRisk2` | page 4 | Front body controller: a274 failure to precharge risk2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a275_TLVBMS_BmbCommunication` | page 4 | Front body controller: a275 TLVBMS bmb communication | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a276_TLVBMS_BmbDataIntegrityLoss` | page 4 | Front body controller: a276 TLVBMS bmb data integrity loss | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a277_TLVBMS_BmbStatusRegError` | page 4 | Front body controller: a277 TLVBMS bmb status reg error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a278_TLVBMS_BmbHwOverCurrentFault` | page 4 | Front body controller: a278 TLVBMS bmb hw over current fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a279_refrigLiquidTempSns` | page 4 | Front body controller: a279 refrig liquid temp sns | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a280_refrigLiquidPresSns` | page 4 | Front body controller: a280 refrig liquid pres sns | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a281_alcoholInterlockBlockingDrive` | page 4 | Front body controller: a281 alcohol interlock blocking drive | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a282_coolantLevelSensorFault` | page 4 | Front body controller: a282 coolant level sensor fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a283_thmlFanLimitedByCurrent` | page 4 | Front body controller: a283 thml fan limited by current | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a284_chillerExvFault` | page 4 | Front body controller: a284 chiller exv fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a285_evaporatorExvFault` | page 4 | Front body controller: a285 evaporator exv fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a286_recircExvFault` | page 4 | Front body controller: a286 recirc exv fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a287_lccExvFault` | page 4 | Front body controller: a287 lcc exv fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a288_ccLeftExvFault` | page 4 | Front body controller: a288 cc left exv fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a289_ccRightExvFault` | page 4 | Front body controller: a289 cc right exv fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a290_leftFogLightFault` | page 4 | Front body controller: a290 left fog light fault | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a291_rightFogLightFault` | page 4 | Front body controller: a291 right fog light fault | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a292_sideMarkerLightPipeFault` | page 4 | Front body controller: a292 side marker light pipe fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a293_interiorFrunkLightFault` | page 4 | Front body controller: a293 interior frunk light fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a294_leftSideRepeaterLightFault` | page 4 | Front body controller: a294 left side repeater light fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a295_rightSideRepeaterLightFault` | page 4 | Front body controller: a295 right side repeater light fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a296_turnSignalIssue` | page 4 | Front body controller: a296 turn signal issue | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a297_TLVBMS_BmbHwOverTemperatureFault` | page 4 | Front body controller: a297 TLVBMS bmb hw over temperature fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a298_radiatorLowAirFlowDetected` | page 4 | Front body controller: a298 radiator low air flow detected | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a299_homelinkConfigurationFailed` | page 4 | Front body controller: a299 homelink configuration failed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a300_louverActuatorSwapDetected` | page 4 | Front body controller: a300 louver actuator swap detected | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a301_wipersFactoryDisabled` | page 5 | Front body controller: a301 wipers factory disabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a302_wiperCommError` | page 5 | Front body controller: a302 wiper comm error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a303_frunkAccessPostActive` | page 5 | Front body controller: a303 frunk access post active | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a304_frunkReleaseFailed` | page 5 | Front body controller: a304 frunk release failed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a305_frunkPriOverCurrent` | page 5 | Front body controller: a305 frunk pri over current | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a306_frunkPriUnderCurrent` | page 5 | Front body controller: a306 frunk pri under current | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a307_frunkSecOverCurrent` | page 5 | Front body controller: a307 frunk sec over current | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a308_frunkSecUnderCurrent` | page 5 | Front body controller: a308 frunk sec under current | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a309_frunkEmergencyReleasePressed` | page 5 | Front body controller: a309 frunk emergency release pressed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a310_vcleftOvertempSlope` | page 5 | Front body controller: a310 vcleft overtemp slope | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a311_vcrightOvertempSlope` | page 5 | Front body controller: a311 vcright overtemp slope | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a312_pcsOvertempSlope` | page 5 | Front body controller: a312 pcs overtemp slope | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a313_epas3pOvertempSlope` | page 5 | Front body controller: a313 epas3p overtemp slope | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a314_epas3sOvertempSlope` | page 5 | Front body controller: a314 epas3s overtemp slope | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a315_iboosterOvertempSlope` | page 5 | Front body controller: a315 ibooster overtemp slope | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a316_espOvertempSlope` | page 5 | Front body controller: a316 esp overtemp slope | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a317_vbatFusedOvertempSlope` | page 5 | Front body controller: a317 vbat fused overtemp slope | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a318_vcleftOvertempMax` | page 5 | Front body controller: a318 vcleft overtemp max | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a319_vcrightOvertempMax` | page 5 | Front body controller: a319 vcright overtemp max | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a320_pcsOvertempMax` | page 5 | Front body controller: a320 pcs overtemp max | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a321_epas3pOvertempMax` | page 5 | Front body controller: a321 epas3p overtemp max | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a322_epas3sOvertempMax` | page 5 | Front body controller: a322 epas3s overtemp max | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a323_iboosterOvertempMax` | page 5 | Front body controller: a323 ibooster overtemp max | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a324_espOvertempMax` | page 5 | Front body controller: a324 esp overtemp max | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a325_vbatFusedOvertempMax` | page 5 | Front body controller: a325 vbat fused overtemp max | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a326_vcleftSlowTripOC` | page 5 | Front body controller: a326 vcleft slow trip OC | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a327_vcrightSlowTripOC` | page 5 | Front body controller: a327 vcright slow trip OC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a328_pcsSlowTripOC` | page 5 | Front body controller: a328 pcs slow trip OC | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a329_epas3pSlowTripOC` | page 5 | Front body controller: a329 epas3p slow trip OC | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a330_epas3sSlowTripOC` | page 5 | Front body controller: a330 epas3s slow trip OC | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a331_iboosterSlowTripOC` | page 5 | Front body controller: a331 ibooster slow trip OC | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a332_espSlowTripOC` | page 5 | Front body controller: a332 esp slow trip OC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a333_vbatFusedSlowTripOC` | page 5 | Front body controller: a333 vbat fused slow trip OC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a334_vcleftFastTripOCMax` | page 5 | Front body controller: a334 vcleft fast trip OC max | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a335_vcrightFastTripOCMax` | page 5 | Front body controller: a335 vcright fast trip OC max | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a336_pcsFastTripOCMax` | page 5 | Front body controller: a336 pcs fast trip OC max | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a337_epas3pFastTripOCMax` | page 5 | Front body controller: a337 epas3p fast trip OC max | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a338_epas3sFastTripOCMax` | page 5 | Front body controller: a338 epas3s fast trip OC max | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a339_iboosterFastTripOCMax` | page 5 | Front body controller: a339 ibooster fast trip OC max | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a340_espFastTripOCMax` | page 5 | Front body controller: a340 esp fast trip OC max | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a341_vbatFusedFastTripOCMax` | page 5 | Front body controller: a341 vbat fused fast trip OC max | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a342_vcleftFastTripSlope` | page 5 | Front body controller: a342 vcleft fast trip slope | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a343_vcrightFastTripSlope` | page 5 | Front body controller: a343 vcright fast trip slope | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a344_pcsFastTripSlope` | page 5 | Front body controller: a344 pcs fast trip slope | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a345_epas3pFastTripSlope` | page 5 | Front body controller: a345 epas3p fast trip slope | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a346_epas3sFastTripSlope` | page 5 | Front body controller: a346 epas3s fast trip slope | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a347_iboosterFastTripSlope` | page 5 | Front body controller: a347 ibooster fast trip slope | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a348_espFastTripSlope` | page 5 | Front body controller: a348 esp fast trip slope | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a349_vbatFusedFastTripSlope` | page 5 | Front body controller: a349 vbat fused fast trip slope | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a350_espValveCurrentSenseSaturated` | page 5 | Front body controller: a350 esp valve current sense saturated | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a351_emergencyFrunkButtonPressIgnored` | page 5 | Front body controller: a351 emergency frunk button press ignored | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a352_audioCurrentSpikeData` | page 5 | Front body controller: a352 audio current spike data | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a353_wiperHeaterUndercurrent` | page 5 | Front body controller: a353 wiper heater undercurrent | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a354_windshieldCameraHeaterUndercurrent` | page 5 | Front body controller: a354 windshield camera heater undercurrent | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a355_coolantSysLockout` | page 5 | Front body controller: a355 coolant sys lockout | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a356_refrigSysLockout` | page 5 | Front body controller: a356 refrig sys lockout | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a357_hornUndercurrent` | page 5 | Front body controller: a357 horn undercurrent | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a358_hornOvercurrent` | page 5 | Front body controller: a358 horn overcurrent | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a359_postPORExcessiveAh` | page 5 | Front body controller: a359 post POR excessive ah | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a360_ungracefulAccPlusExit` | page 5 | Front body controller: a360 ungraceful acc plus exit | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a361_washerFluidLowMomentary` | page 6 | Front body controller: a361 washer fluid low momentary | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a362_TLVBMS_AllSocCorrectionTimeout` | page 6 | Front body controller: a362 TLVBMS all soc correction timeout | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a363_TLVBMS_BleedBasedWeakShort` | page 6 | Front body controller: a363 TLVBMS bleed based weak short | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a364_heaterTypeEstimationChanged` | page 6 | Front body controller: a364 heater type estimation changed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a365_burnInRoutineEntered` | page 6 | Front body controller: a365 burn in routine entered | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a366_burnInRoutineExited` | page 6 | Front body controller: a366 burn in routine exited | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a367_dischargeRoutineEntered` | page 6 | Front body controller: a367 discharge routine entered | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a368_dischargeRoutineExited` | page 6 | Front body controller: a368 discharge routine exited | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a369_reducedPowerDischarge` | page 6 | Front body controller: a369 reduced power discharge | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a370_noLVSupportSocTooLow` | page 6 | Front body controller: a370 no LV support soc too low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a371_failureToPrechargeRisk` | page 6 | Front body controller: a371 failure to precharge risk | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a372_TLVBMS_BmbHwOverVoltageFault` | page 6 | Front body controller: a372 TLVBMS bmb hw over voltage fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a373_chillerControlFlooding` | page 6 | Front body controller: a373 chiller control flooding | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a374_lccInletSolenoidFault` | page 6 | Front body controller: a374 lcc inlet solenoid fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a375_refVoltageOutOfSpec` | page 6 | Front body controller: a375 ref voltage out of spec | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a376_controllerWakeupDebug` | page 6 | Front body controller: a376 controller wakeup debug | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a377_wiperParkFault` | page 6 | Front body controller: a377 wiper park fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a378_wiperECUDebug` | page 6 | Front body controller: a378 wiper ECU debug | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a379_shortedCellTestRunDebug` | page 6 | Front body controller: a379 shorted cell test run debug | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a380_chillerExvWarning` | page 6 | Front body controller: a380 chiller exv warning | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a381_evaporatorExvWarning` | page 6 | Front body controller: a381 evaporator exv warning | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a382_recircExvWarning` | page 6 | Front body controller: a382 recirc exv warning | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a383_lccExvWarning` | page 6 | Front body controller: a383 lcc exv warning | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a384_ccLeftExvWarning` | page 6 | Front body controller: a384 cc left exv warning | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a385_ccRightExvWarning` | page 6 | Front body controller: a385 cc right exv warning | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a386_exvMotorWarning` | page 6 | Front body controller: a386 exv motor warning | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a387_shortedCellInstc` | page 6 | Front body controller: a387 shorted cell instc | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a388_shortedCell` | page 6 | Front body controller: a388 shorted cell | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a389_frunkInhibitingReleaseAtSpeed` | page 6 | Front body controller: a389 frunk inhibiting release at speed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a390_heatPumpModeConvergence` | page 6 | Front body controller: a390 heat pump mode convergence | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a391_frunkLatchSwitchFault` | page 6 | Front body controller: a391 frunk latch switch fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a392_TLVBMS_BmbHwUnderVoltageFault` | page 6 | Front body controller: a392 TLVBMS bmb hw under voltage fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a393_ambientTempNetworkSna` | page 6 | Front body controller: a393 ambient temp network sna | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a394_pressureSensorCheckFault` | page 6 | Front body controller: a394 pressure sensor check fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a395_pressureSensorCheckInconclusive` | page 6 | Front body controller: a395 pressure sensor check inconclusive | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a396_coolantLevelLowUserFacing` | page 6 | Front body controller: a396 coolant level low user facing | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a397_temperatureSensorCheckFault` | page 6 | Front body controller: a397 temperature sensor check fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a398_tempSensorCheckInconclusive` | page 6 | Front body controller: a398 temp sensor check inconclusive | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a399_frunkNeverReportedOpen` | page 6 | Front body controller: a399 frunk never reported open | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a400_TLVBMS_BmbVrefBad` | page 6 | Front body controller: a400 TLVBMS bmb vref bad | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a401_deadLVMinimalAhDischarged` | page 6 | Front body controller: a401 dead LV minimal ah discharged | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a402_LVBatteryCannotSupportVehicle` | page 6 | Front body controller: a402 LV battery cannot support vehicle | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a403_chargeExitHardCurrentLimit` | page 6 | Front body controller: a403 charge exit hard current limit | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a404_resistanceEstimationHardFailure` | page 6 | Front body controller: a404 resistance estimation hard failure | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a405_dcrData1` | page 6 | Front body controller: a405 dcr data1 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a406_dcrData2` | page 6 | Front body controller: a406 dcr data2 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a407_dcrMilliOhmsAboveThreshold` | page 6 | Front body controller: a407 dcr milli ohms above threshold | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a408_standbyChargeProfileHardExit` | page 6 | Front body controller: a408 standby charge profile hard exit | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a409_invalidConfiguration` | page 6 | Front body controller: a409 invalid configuration | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a410_LVBatteryDataCollection1` | page 6 | Front body controller: a410 LV battery data collection1 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a411_LVBatteryDataCollection2` | page 6 | Front body controller: a411 LV battery data collection2 | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a412_dcrData3` | page 6 | Front body controller: a412 dcr data3 | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a413_TLVBMS_BmbVrefWarning` | page 6 | Front body controller: a413 TLVBMS bmb vref warning | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a414_prechargeLVLoadReduction` | page 6 | Front body controller: a414 precharge LV load reduction | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a415_prechargeLVLoadReduction2` | page 6 | Front body controller: a415 precharge LV load reduction2 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a416_TLVBMS_BrickOverDischarged` | page 6 | Front body controller: a416 TLVBMS brick over discharged | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a417_TLVBMS_BrickOverVoltageFault` | page 6 | Front body controller: a417 TLVBMS brick over voltage fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a418_TLVBMS_BrickOverVoltageWarning` | page 6 | Front body controller: a418 TLVBMS brick over voltage warning | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a419_TLVBMS_BrickSocLow` | page 6 | Front body controller: a419 TLVBMS brick soc low | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a420_holidayParty` | page 6 | Front body controller: a420 holiday party | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a421_leftHeadlampUartCondition` | page 7 | Front body controller: a421 left headlamp uart condition | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a423_TLVBMS_BrickUnderVoltageFault` | page 7 | Front body controller: a423 TLVBMS brick under voltage fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a424_TLVBMS_BrickUnderVoltageOcv` | page 7 | Front body controller: a424 TLVBMS brick under voltage ocv | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a425_TLVBMS_BusVoltageTooHigh` | page 7 | Front body controller: a425 TLVBMS bus voltage too high | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a426_TLVBMS_BusVoltageTooLow` | page 7 | Front body controller: a426 TLVBMS bus voltage too low | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a427_TLVBMS_CacChange` | page 7 | Front body controller: a427 TLVBMS cac change | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a428_TLVBMS_CacImbalance` | page 7 | Front body controller: a428 TLVBMS cac imbalance | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a429_TLVBMS_CapacityTestResults` | page 7 | Front body controller: a429 TLVBMS capacity test results | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a430_TLVBMS_ChargeCurrentLimitExceeded` | page 7 | Front body controller: a430 TLVBMS charge current limit exceeded | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a431_TLVBMS_ChargeOverCurrent` | page 7 | Front body controller: a431 TLVBMS charge over current | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a432_TLVBMS_ChargeRegulationFault` | page 7 | Front body controller: a432 TLVBMS charge regulation fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a433_TLVBMS_ConfigFromBmbModIdFailed` | page 7 | Front body controller: a433 TLVBMS config from bmb mod id failed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a434_TLVBMS_ConfigInitFailed` | page 7 | Front body controller: a434 TLVBMS config init failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a435_TLVBMS_DchgCurrentLimitExceeded` | page 7 | Front body controller: a435 TLVBMS dchg current limit exceeded | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a436_TLVBMS_DischargeOverCurrent` | page 7 | Front body controller: a436 TLVBMS discharge over current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a437_TLVBMS_NvmRegistrationError` | page 7 | Front body controller: a437 TLVBMS nvm registration error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a438_TLVBMS_PackOverTemperatureFault` | page 7 | Front body controller: a438 TLVBMS pack over temperature fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a439_TLVBMS_PackOverTemperatureWarning` | page 7 | Front body controller: a439 TLVBMS pack over temperature warning | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a440_TLVBMS_PackSNInvalidForNvm` | page 7 | Front body controller: a440 TLVBMS pack SN invalid for nvm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a441_TLVBMS_ResetNeededForNvmPackSwap` | page 7 | Front body controller: a441 TLVBMS reset needed for nvm pack swap | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a442_TLVBMS_SocChange` | page 7 | Front body controller: a442 TLVBMS soc change | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a443_TLVBMS_BmbDieOverTemperature` | page 7 | Front body controller: a443 TLVBMS bmb die over temperature | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a444_drv8703Fault` | page 7 | Front body controller: a444 drv8703 fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a445_drv8703SpiFaultDBG` | page 7 | Front body controller: a445 drv8703 spi fault DBG | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a446_cabinHVACUnavailableContext` | page 7 | Front body controller: a446 cabin HVAC unavailable context | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a447_cabinHVACUnavailable` | page 7 | Front body controller: a447 cabin HVAC unavailable | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a448_gtwSteeringBtnReset` | page 7 | Front body controller: a448 gtw steering btn reset | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a449_hornSwitchStuckOn` | page 7 | Front body controller: a449 horn switch stuck on | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a450_hornSwitchNotPressedFactory` | page 7 | Front body controller: a450 horn switch not pressed factory | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a451_refrigerantNotCommissioned` | page 7 | Front body controller: a451 refrigerant not commissioned | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a452_dischargePresSensIntermittent` | page 7 | Front body controller: a452 discharge pres sens intermittent | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a453_dischargeTempSensIntermittent` | page 7 | Front body controller: a453 discharge temp sens intermittent | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a454_suctionPresSensIntermittent` | page 7 | Front body controller: a454 suction pres sens intermittent | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a455_suctionTempSensIntermittent` | page 7 | Front body controller: a455 suction temp sens intermittent | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a456_liquidPresSensIntermittent` | page 7 | Front body controller: a456 liquid pres sens intermittent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a457_liquidTempSensIntermittent` | page 7 | Front body controller: a457 liquid temp sens intermittent | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a458_grosslyLowRefrigerant` | page 7 | Front body controller: a458 grossly low refrigerant | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a459_thermalFillAndDrive` | page 7 | Front body controller: a459 thermal fill and drive | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a460_hardIsentropicTdFailed` | page 7 | Front body controller: a460 hard isentropic td failed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a461_TLVBMS_SocHighAhError` | page 7 | Front body controller: a461 TLVBMS soc high ah error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a462_LVBMSFault` | page 7 | Front body controller: a462 LVBMS fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a463_frunkSensorService` | page 7 | Front body controller: a463 frunk sensor service | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a464_highFlowIndexHighSubcoolFlagged` | page 7 | Front body controller: a464 high flow index high subcool flagged | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a465_lowFlowIndexHighSubcoolFlagged` | page 7 | Front body controller: a465 low flow index high subcool flagged | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a466_highFlowIndexLowSubcoolFlagged` | page 7 | Front body controller: a466 high flow index low subcool flagged | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a467_lowPowerIndexFlagged` | page 7 | Front body controller: a467 low power index flagged | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a468_highPowerIndexFlagged` | page 7 | Front body controller: a468 high power index flagged | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a469_prvPopDetected` | page 7 | Front body controller: a469 prv pop detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a470_implausiblePdPlDetected` | page 7 | Front body controller: a470 implausible pd pl detected | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a471_hcm5Debug` | page 7 | Front body controller: a471 hcm5 debug | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a472_leftHeadlampRangeUpdate` | page 7 | Front body controller: a472 left headlamp range update | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a473_rightHeadlampRangeUpdate` | page 7 | Front body controller: a473 right headlamp range update | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a474_leftHeadlampInternalError` | page 7 | Front body controller: a474 left headlamp internal error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a475_rightHeadlampInternalError` | page 7 | Front body controller: a475 right headlamp internal error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a476_LVBMSMIA` | page 7 | Front body controller: a476 LVBMSMIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a477_LVBatteryUnrecoverableByVehicle` | page 7 | Front body controller: a477 LV battery unrecoverable by vehicle | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a478_LVBMS_MOSFET_Open` | page 7 | Front body controller: a478 LVBMS MOSFET open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a479_LVBMS_ECPA_NotClosed` | page 7 | Front body controller: a479 LVBMS ECPA not closed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a480_vnf1048Fault` | page 7 | Front body controller: a480 vnf1048 fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a481_vnf1048SelfTestFailure` | page 8 | Front body controller: a481 vnf1048 self test failure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a482_rightHeadlampMigrationDebug` | page 8 | Front body controller: a482 right headlamp migration debug | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a483_leftHeadlampStepperMotorFault` | page 8 | Front body controller: a483 left headlamp stepper motor fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a484_headlampLevelingRideHeightDebug` | page 8 | Front body controller: a484 headlamp leveling ride height debug | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a485_leftHeadlampMigrationDebug` | page 8 | Front body controller: a485 left headlamp migration debug | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a486_mcuGraphicsEFuseFault` | page 8 | Front body controller: a486 mcu graphics e fuse fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a487_leftHeadlampLastPositionUpdate` | page 8 | Front body controller: a487 left headlamp last position update | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a488_rightHeadlampStepperMotorFault` | page 8 | Front body controller: a488 right headlamp stepper motor fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a489_ValveStuckFlagged` | page 8 | Front body controller: a489 valve stuck flagged | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a490_coolantPumpsNotIdentified` | page 8 | Front body controller: a490 coolant pumps not identified | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a491_rightHeadlampLastPositionUpdate` | page 8 | Front body controller: a491 right headlamp last position update | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a492_TLVBMS_SocImbalance` | page 8 | Front body controller: a492 TLVBMS soc imbalance | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a493_TLVBMS_SocImbalanceWarning` | page 8 | Front body controller: a493 TLVBMS soc imbalance warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a494_LVBatteryTempBlockingOTA` | page 8 | Front body controller: a494 LV battery temp blocking OTA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a495_LVBatteryRecoveryBlocked` | page 8 | Front body controller: a495 LV battery recovery blocked | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a496_LVBatteryExitDriveWarning` | page 8 | Front body controller: a496 LV battery exit drive warning | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a497_LVBatteryWarnDisconnect` | page 8 | Front body controller: a497 LV battery warn disconnect | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a498_TLVBMS_ImpedanceTestResults` | page 8 | Front body controller: a498 TLVBMS impedance test results | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a499_loadShedPumpFlowRequest` | page 8 | Front body controller: a499 load shed pump flow request | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a500_eFuseASICStateMismatch` | page 8 | Front body controller: a500 e fuse ASIC state mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a501_vnf1048ConfigurationMismatch` | page 8 | Front body controller: a501 vnf1048 configuration mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a502_TLVBMS_WeakShortImpedance` | page 8 | Front body controller: a502 TLVBMS weak short impedance | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a503_TLVBMS_BrickExtendedOvFault` | page 8 | Front body controller: a503 TLVBMS brick extended ov fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a504_airInRefrigerantDetected` | page 8 | Front body controller: a504 air in refrigerant detected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a505_BLEFrontUnderVoltage` | page 8 | Front body controller: a505 BLE front under voltage | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a506_invalidRefrigerantSystemConfig` | page 8 | Front body controller: a506 invalid refrigerant system config | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a507_leftHeadlampAimingFault` | page 8 | Front body controller: a507 left headlamp aiming fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a508_TLVBMS_ImpedanceGrowth` | page 8 | Front body controller: a508 TLVBMS impedance growth | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a509_vcrightEFuseLoadShed` | page 8 | Front body controller: a509 vcright e fuse load shed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a510_LVBatteryRecoveryTimeout` | page 8 | Front body controller: a510 LV battery recovery timeout | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a511_DCDCSaturationLoadShed` | page 8 | Front body controller: a511 DCDC saturation load shed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a512_LVBMSFault_MOS_Open_hardwareOC` | page 8 | Front body controller: a512 LVBMS fault MOS open hardware OC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a513_LVBMSFault_MOS_Open_chgOC` | page 8 | Front body controller: a513 LVBMS fault MOS open chg OC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a514_LVBMSFault_MOS_Open_cellUV` | page 8 | Front body controller: a514 LVBMS fault MOS open cell UV | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a515_LVBMSFault_MOS_Open_cellOV` | page 8 | Front body controller: a515 LVBMS fault MOS open cell OV | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a516_hibernationActive` | page 8 | Front body controller: a516 hibernation active | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a517_hibernationRecovery` | page 8 | Front body controller: a517 hibernation recovery | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a518_LVBMSFault_MOS_Open_packOV` | page 8 | Front body controller: a518 LVBMS fault MOS open pack OV | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a519_leftHeadlampInternalErrorV2` | page 8 | Front body controller: a519 left headlamp internal error V2 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a520_rightHeadlampInternalErrorV2` | page 8 | Front body controller: a520 right headlamp internal error V2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a521_vcleftEFuseLoadShed` | page 8 | Front body controller: a521 vcleft e fuse load shed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a522_hibernationActiveLogCapture` | page 8 | Front body controller: a522 hibernation active log capture | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a523_eFuseThresholdsIncorrect` | page 8 | Front body controller: a523 e fuse thresholds incorrect | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a524_rightHeadlampAimingFault` | page 8 | Front body controller: a524 right headlamp aiming fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a525_LVBatterySWMisconfiguration` | page 8 | Front body controller: a525 LV battery SW misconfiguration | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a526_pcbaOverTemperature` | page 8 | Front body controller: a526 pcba over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a527_LVBatteryCellImbalance` | page 8 | Front body controller: a527 LV battery cell imbalance | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a528_LVBatteryCommsDiscnctd` | page 8 | Front body controller: a528 LV battery comms discnctd | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a529_discnctdBatteryStateUnknown` | page 8 | Front body controller: a529 discnctd battery state unknown | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a530_sharpCurrentRise` | page 8 | Front body controller: a530 sharp current rise | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a531_lowPowerIndexFlaggedUserFacing` | page 8 | Front body controller: a531 low power index flagged user facing | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a532_gtwMIAInDrive` | page 8 | Front body controller: a532 gtw MIA in drive | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a533_TLVBMS_MosfetOverTemperatureFault` | page 8 | Front body controller: a533 TLVBMS mosfet over temperature fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a534_chillerExvCalibInitDebug` | page 8 | Front body controller: a534 chiller exv calib init debug | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a535_evapExvCalibInitDebug` | page 8 | Front body controller: a535 evap exv calib init debug | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a536_recircExvCalibInitDebug` | page 8 | Front body controller: a536 recirc exv calib init debug | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a537_lccExvCalibInitDebug` | page 8 | Front body controller: a537 lcc exv calib init debug | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a538_cclExvCalibInitDebug` | page 8 | Front body controller: a538 ccl exv calib init debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a539_ccrExvCalibInitDebug` | page 8 | Front body controller: a539 ccr exv calib init debug | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a540_radiatorSteamDetected` | page 8 | Front body controller: a540 radiator steam detected | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a541_LVBatteryChargeOCLevel1` | page 9 | Front body controller: a541 LV battery charge OC level1 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a542_refrigerantReclaim` | page 9 | Front body controller: a542 refrigerant reclaim | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a543_compressorLowFlowDeliveryDetected` | page 9 | Front body controller: a543 compressor low flow delivery detected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a544_LVBatteryCommsBusTurnedOff` | page 9 | Front body controller: a544 LV battery comms bus turned off | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a545_LVBatteryTypeUnknown` | page 9 | Front body controller: a545 LV battery type unknown | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a546_leftLowOrHighBeamLightCondition` | page 9 | Front body controller: a546 left low or high beam light condition | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a547_postCrashLoadShed` | page 9 | Front body controller: a547 post crash load shed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a548_HVFaultLoadShed` | page 9 | Front body controller: a548 HV fault load shed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a549_leftHeadlampInternalErrorV3` | page 9 | Front body controller: a549 left headlamp internal error V3 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a550_ambientTempDelta` | page 9 | Front body controller: a550 ambient temp delta | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a551_leftHeadlampSoftShort` | page 9 | Front body controller: a551 left headlamp soft short | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a552_eFuseSelfTestFailure` | page 9 | Front body controller: a552 e fuse self test failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a553_rightHeadlampSoftShort` | page 9 | Front body controller: a553 right headlamp soft short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a555_LVBatteryCellRebalancing` | page 9 | Front body controller: a555 LV battery cell rebalancing | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a556_falseTriggerOfDiscnctdBatteryTest` | page 9 | Front body controller: a556 false trigger of discnctd battery test | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a557_rightHeadlampInternalErrorV3` | page 9 | Front body controller: a557 right headlamp internal error V3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a558_rightHeadlampAimingDebug` | page 9 | Front body controller: a558 right headlamp aiming debug | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a559_LVBatteryLowSOC` | page 9 | Front body controller: a559 LV battery low SOC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a560_compressorHighSuperheat` | page 9 | Front body controller: a560 compressor high superheat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a561_LVBMSEFuseOvertemperature` | page 9 | Front body controller: a561 LVBMSE fuse overtemperature | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a562_LVBMSModuleOvertemperature` | page 9 | Front body controller: a562 LVBMS module overtemperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a563_chargePortDoorOpenBlockedByBrake` | page 9 | Front body controller: a563 charge port door open blocked by brake | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a564_leftHeadlampAimingDebug` | page 9 | Front body controller: a564 left headlamp aiming debug | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a565_userPresenceDisplayStateMismatch` | page 9 | Front body controller: a565 user presence display state mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a566_leftFrontTurnLightFault` | page 9 | Front body controller: a566 left front turn light fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a567_rightFrontTurnLightFault` | page 9 | Front body controller: a567 right front turn light fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a568_leftDaytimeRunningLightFault` | page 9 | Front body controller: a568 left daytime running light fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a569_rightDaytimeRunningLightFault` | page 9 | Front body controller: a569 right daytime running light fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a570_headlampsAdaptedToLeftHandTraffic` | page 9 | Front body controller: a570 headlamps adapted to left hand traffic | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a571_headlampsAdaptedToRightHandTraffic` | page 9 | Front body controller: a571 headlamps adapted to right hand traffic | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a572_hvacCompressorEFuseTrip` | page 9 | Front body controller: a572 hvac compressor e fuse trip | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a573_radarEFuseTrip` | page 9 | Front body controller: a573 radar e fuse trip | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a574_frontDriveInverterEFuseTrip` | page 9 | Front body controller: a574 front drive inverter e fuse trip | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a575_frontOilPumpEFuseTrip` | page 9 | Front body controller: a575 front oil pump e fuse trip | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a576_mcuLogicEFuseTrip` | page 9 | Front body controller: a576 mcu logic e fuse trip | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a577_tasEFuseTrip` | page 9 | Front body controller: a577 tas e fuse trip | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a578_vbatFusedLowCurrentFeedEFuseTrip` | page 9 | Front body controller: a578 vbat fused low current feed e fuse trip | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a579_leftHeadlightEFuseTrip` | page 9 | Front body controller: a579 left headlight e fuse trip | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a580_rightHeadlightEFuseTrip` | page 9 | Front body controller: a580 right headlight e fuse trip | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a581_windshieldWiperEFuseTrip` | page 9 | Front body controller: a581 windshield wiper e fuse trip | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a582_goodForPCSPowerCycle` | page 9 | Front body controller: a582 good for PCS power cycle | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a583_frunkSwitchGroupDisagreementDebug` | page 9 | Front body controller: a583 frunk switch group disagreement debug | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a584_frunkSwitchGroupDebug` | page 9 | Front body controller: a584 frunk switch group debug | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a585_bothHeadlampsInternalError` | page 9 | Front body controller: a585 both headlamps internal error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a586_rightLowOrHighBeamLightCondition` | page 9 | Front body controller: a586 right low or high beam light condition | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a587_externalLVPowerSupply` | page 9 | Front body controller: a587 external LV power supply | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a588_vcleftPwrRationalityCurve` | page 9 | Front body controller: a588 vcleft pwr rationality curve | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a589_vcleftFastBlowDetection` | page 9 | Front body controller: a589 vcleft fast blow detection | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a590_vcrightPwrRationalityCurve` | page 9 | Front body controller: a590 vcright pwr rationality curve | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a591_vcrightFastBlowDetection` | page 9 | Front body controller: a591 vcright fast blow detection | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a592_vcleftCurvePowerCutoff` | page 9 | Front body controller: a592 vcleft curve power cutoff | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a593_vcleftFastBlowPowerCutoff` | page 9 | Front body controller: a593 vcleft fast blow power cutoff | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a594_virtualPitchConversionDebug` | page 9 | Front body controller: a594 virtual pitch conversion debug | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a595_voltageSensorMismatch` | page 9 | Front body controller: a595 voltage sensor mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a596_vcrightCurvePowerCutoff` | page 9 | Front body controller: a596 vcright curve power cutoff | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a597_vcrightFastBlowPowerCutoff` | page 9 | Front body controller: a597 vcright fast blow power cutoff | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a598_eFuseSelfTestFailureService` | page 9 | Front body controller: a598 e fuse self test failure service | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a599_LVBatteryTypeUnsupported` | page 9 | Front body controller: a599 LV battery type unsupported | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a600_currentSensorMismatch` | page 9 | Front body controller: a600 current sensor mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a601_autopilotAirPurgeLimitReached` | page 10 | Front body controller: a601 autopilot air purge limit reached | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a602_unknownTurnIndicatorConfig` | page 10 | Front body controller: a602 unknown turn indicator config | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a603_unexpectedTurnIndicatorConfigChange` | page 10 | Front body controller: a603 unexpected turn indicator config change | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a604_turnIndicatorConfigInputMismatch` | page 10 | Front body controller: a604 turn indicator config input mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a605_sleepBypassPowerOff` | page 10 | Front body controller: a605 sleep bypass power off | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a606_chillerBattHeatingExit` | page 10 | Front body controller: a606 chiller batt heating exit | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a607_sleepPowerDebug` | page 10 | Front body controller: a607 sleep power debug | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a608_TLVBMS_BleedFetFailure` | page 10 | Front body controller: a608 TLVBMS bleed fet failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a609_autopilotDriveNotAuthed` | page 10 | Front body controller: a609 autopilot drive not authed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a610_frunkOpenFailureMetricSet` | page 10 | Front body controller: a610 frunk open failure metric set | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a611_poorRadiatorHeatRejection` | page 10 | Front body controller: a611 poor radiator heat rejection | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a612_LVUnhealthyLoadShed` | page 10 | Front body controller: a612 LV unhealthy load shed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a613_selfTestsBlockingDrive` | page 10 | Front body controller: a613 self tests blocking drive | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a614_coolantSysDriverlessSelfTest` | page 10 | Front body controller: a614 coolant sys driverless self test | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a615_TLVBMS_BatteryHeaterFault` | page 10 | Front body controller: a615 TLVBMS battery heater fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a616_VCSEAT2L_MIA` | page 10 | Front body controller: a616 VCSEAT2 l MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a617_VCSEAT2R_MIA` | page 10 | Front body controller: a617 VCSEAT2 r MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a618_cabinCoolingCapacityLimited` | page 10 | Front body controller: a618 cabin cooling capacity limited | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a619_frunkSwitchReleaseTimeDBG` | page 10 | Front body controller: a619 frunk switch release time DBG | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a620_pumpAirLock` | page 10 | Front body controller: a620 pump air lock | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a621_coolantAirPurgeIncomplete` | page 10 | Front body controller: a621 coolant air purge incomplete | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a622_pumpDetectsLowCoolantFlow` | page 10 | Front body controller: a622 pump detects low coolant flow | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a623_LVUnhealthy` | page 10 | Front body controller: a623 LV unhealthy | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a624_rightHeadlampInternalErrorV4` | page 10 | Front body controller: a624 right headlamp internal error V4 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a625_leftHeadlampInternalErrorV4` | page 10 | Front body controller: a625 left headlamp internal error V4 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a626_LVBatteryResistanceIncrease` | page 10 | Front body controller: a626 LV battery resistance increase | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a627_LVBatteryUnrecoverableByAnyDevice` | page 10 | Front body controller: a627 LV battery unrecoverable by any device | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a628_TLVBMS_BmbThermistorFault` | page 10 | Front body controller: a628 TLVBMS bmb thermistor fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a629_TLVBMS_PackTemperatureIrrational` | page 10 | Front body controller: a629 TLVBMS pack temperature irrational | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a630_leftHeadlampFactoryFault` | page 10 | Front body controller: a630 left headlamp factory fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a631_rightHeadlampFactoryFault` | page 10 | Front body controller: a631 right headlamp factory fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a634_indeterminateSwitchTransitionDetectedDbg` | page 10 | Front body controller: a634 indeterminate switch transition detected dbg | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a635_rtosSleepFailed` | page 10 | Front body controller: a635 rtos sleep failed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d636_ptCoolantPumpDetectsAirInSystem` | page 10 | Front body controller: d636 pt coolant pump detects air in system | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d637_battCoolantPumpDetectsAirInSystem` | page 10 | Front body controller: d637 batt coolant pump detects air in system | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d638_ptCoolantTempSensorIssue` | page 10 | Front body controller: d638 pt coolant temp sensor issue | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d639_batteryCoolantTempSensorIssue` | page 10 | Front body controller: d639 battery coolant temp sensor issue | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d640_firmwareVersionMismatch` | page 10 | Front body controller: d640 firmware version mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d641_ptCoolantPumpCircuitOpen` | page 10 | Front body controller: d641 pt coolant pump circuit open | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d642_batteryCoolantPumpCircuitOpen` | page 10 | Front body controller: d642 battery coolant pump circuit open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a643_rightHeadlampUartCondition` | page 10 | Front body controller: a643 right headlamp uart condition | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a644_washPumpHealthCalculationDbg0` | page 10 | Front body controller: a644 wash pump health calculation dbg0 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a645_washPumpHealthCalculationDbg1` | page 10 | Front body controller: a645 wash pump health calculation dbg1 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a646_washPumpHealthCalculationDbg2` | page 10 | Front body controller: a646 wash pump health calculation dbg2 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d647_louverCommLost` | page 10 | Front body controller: d647 louver comm lost | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d648_louverBlocked` | page 10 | Front body controller: d648 louver blocked | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a649_persistAccPortPowerReqOverridden` | page 10 | Front body controller: a649 persist acc port power req overridden | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d650_lowCoolantLevel` | page 10 | Front body controller: d650 low coolant level | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d651_ptCoolantPumpStall` | page 10 | Front body controller: d651 pt coolant pump stall | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d652_ptCoolantPumpCircuitIssue` | page 10 | Front body controller: d652 pt coolant pump circuit issue | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d653_ptCoolantPumpCommLost` | page 10 | Front body controller: d653 pt coolant pump comm lost | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d654_batteryCoolantPumpStall` | page 10 | Front body controller: d654 battery coolant pump stall | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d655_batteryCoolantPumpCircuitIssue` | page 10 | Front body controller: d655 battery coolant pump circuit issue | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d656_batteryCoolantPumpCommLost` | page 10 | Front body controller: d656 battery coolant pump comm lost | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d657_radiatorFanOperationIssue` | page 10 | Front body controller: d657 radiator fan operation issue | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d658_radiatorFanCircuitIssue` | page 10 | Front body controller: d658 radiator fan circuit issue | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d659_radiatorFanCommLost` | page 10 | Front body controller: d659 radiator fan comm lost | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d660_coolantValveCircuitIssue` | page 10 | Front body controller: d660 coolant valve circuit issue | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a661_mculessLeftHeadlampCurrentAlertDbg` | page 11 | Front body controller: a661 mculess left headlamp current alert dbg | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a662_mculessRightHeadlampCurrentAlertDbg` | page 11 | Front body controller: a662 mculess right headlamp current alert dbg | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a663_leftHeadlampUartWaterMarkWarning` | page 11 | Front body controller: a663 left headlamp uart water mark warning | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a664_rightHeadlampUartWaterMarkWarning` | page 11 | Front body controller: a664 right headlamp uart water mark warning | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a665_leftHeadlampRetryInfo` | page 11 | Front body controller: a665 left headlamp retry info | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a666_rightHeadlampRetryInfo` | page 11 | Front body controller: a666 right headlamp retry info | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a667_leftHeadlampRegionOrSideMismatch` | page 11 | Front body controller: a667 left headlamp region or side mismatch | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a668_rightHeadlampRegionOrSideMismatch` | page 11 | Front body controller: a668 right headlamp region or side mismatch | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a669_thermalHVPowerBudgetActive` | page 11 | Front body controller: a669 thermal HV power budget active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a670_TLVBMS_EfuseStateIrrational` | page 11 | Front body controller: a670 TLVBMS efuse state irrational | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a671_powerConsumptionInfo` | page 11 | Front body controller: a671 power consumption info | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a672_LVBatteryVitals` | page 11 | Front body controller: a672 LV battery vitals | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_d674_portExpanderServiceRequired` | page 11 | Front body controller: d674 port expander service required | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a675_doorWakeToOpenDBG` | page 11 | Front body controller: a675 door wake to open DBG | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a697_leftHeadlampNotAimed` | page 11 | Front body controller: a697 left headlamp not aimed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a698_rightHeadlampNotAimed` | page 11 | Front body controller: a698 right headlamp not aimed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_a702_dynamicHeadlightLevelingUnavailable` | page 11 | Front body controller: a702 dynamic headlight leveling unavailable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`VCFRONT_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (37 signals), page 1 (43 signals), page 2 (60 signals), page 3 (60 signals), page 4 (59 signals), page 5 (60 signals), page 6 (60 signals), page 7 (59 signals), page 8 (60 signals), page 9 (59 signals), page 10 (58 signals), page 11 (17 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
