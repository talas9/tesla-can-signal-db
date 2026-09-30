---
layout: default
title: "VCFRONT2_alertMatrix (0x342) — VCFRONT2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCFRONT2 ECU message: alert matrix. Tesla Model Y CAN bus message VCFRONT2_alertMatrix (0x342) of VCFRONT2 ECU, firmware 2026.26.6.5, 267 signals (VCFRONT2_matrixIndex, VCFRONT2_a001_WatchdogReset, VCFRONT2_a002_PowerLossReset, VCFRONT2_a003_SWAssertion and 263 more). Bit layout, scaling, units and value tables."
---

# VCFRONT2_alertMatrix (0x342) — VCFRONT2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCFRONT2 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 267 signals of VCFRONT2_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT2_alertMatrix` |
| CAN id | 0x342 (834) |
| ECU | [VCFRONT2 ECU](../../vcfront2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT2 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 267 |

## Signals of VCFRONT2_alertMatrix

Tesla Model Y CAN bus signals in `VCFRONT2_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT2_matrixIndex` | selector | VCFRONT2 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10`<br>11 = `AlertMatrix11` | plausible |
| `VCFRONT2_a001_WatchdogReset` | page 0 | VCFRONT2 ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a002_PowerLossReset` | page 0 | VCFRONT2 ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a003_SWAssertion` | page 0 | VCFRONT2 ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a004_adaptiveHeadlightsUnavailable` | page 0 | VCFRONT2 ECU: a004 adaptive headlights unavailable | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a005_CANTXError` | page 0 | VCFRONT2 ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a006_CANTX_cyclicError` | page 0 | VCFRONT2 ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a008_adaptiveHeadlightsUnavailableStalk` | page 0 | VCFRONT2 ECU: a008 adaptive headlights unavailable stalk | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a009_LCCPurgeAttempted` | page 0 | VCFRONT2 ECU: a009 LCC purge attempted | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a012_CPUReset` | page 0 | VCFRONT2 ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a013_AlertManagerFault` | page 0 | VCFRONT2 ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a015_NVMMError` | page 0 | VCFRONT2 ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a016_NVMMRecordError` | page 0 | VCFRONT2 ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a017_NVMMStatusDbg` | page 0 | VCFRONT2 ECU: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a018_HardFault` | page 0 | VCFRONT2 ECU: a018 hard fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a019_BusFault` | page 0 | VCFRONT2 ECU: a019 bus fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a021_TaskSchedulerError` | page 0 | VCFRONT2 ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a022_TaskInitError` | page 0 | VCFRONT2 ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a028_UsageFault` | page 0 | VCFRONT2 ECU: a028 usage fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a029_CoreDump` | page 0 | VCFRONT2 ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a030_ECULogUploadRequest` | page 0 | VCFRONT2 ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a031_UDSActive` | page 0 | VCFRONT2 ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a036_UnknownIrq` | page 0 | VCFRONT2 ECU: a036 unknown irq | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a037_MemManageFault` | page 0 | VCFRONT2 ECU: a037 mem manage fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a038_ProtFaultInfo` | page 0 | VCFRONT2 ECU: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a039_ProtFaultAddress` | page 0 | VCFRONT2 ECU: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a040_Backtrace` | page 0 | VCFRONT2 ECU: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a041_HighCPULoad` | page 0 | VCFRONT2 ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a042_HighStackUsage` | page 0 | VCFRONT2 ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a043_Task1msError` | page 0 | VCFRONT2 ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a044_Task10msError` | page 0 | VCFRONT2 ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a045_Task100msError` | page 0 | VCFRONT2 ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a046_Task1000msError` | page 0 | VCFRONT2 ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a053_wiperCommErrorUser` | page 0 | VCFRONT2 ECU: a053 wiper comm error user | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a054_compressorLowFlowUserFacing` | page 0 | VCFRONT2 ECU: a054 compressor low flow user facing | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a058_inputRHighSyncDebug` | page 0 | VCFRONT2 ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a059_inputResistanceHigh` | page 0 | VCFRONT2 ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a060_engineeringBuild` | page 0 | VCFRONT2 ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a061_XCPConnected` | page 1 | VCFRONT2 ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a062_XCPWasConnected` | page 1 | VCFRONT2 ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a063_SwitchFault` | page 1 | VCFRONT2 ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a064_busSleepReqTimeout` | page 1 | VCFRONT2 ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a077_VCBATT0_MIA` | page 1 | VCFRONT2 ECU: a077 VCBATT0 MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a078_VCBATT1_MIA` | page 1 | VCFRONT2 ECU: a078 VCBATT1 MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a079_VCBATT2_MIA` | page 1 | VCFRONT2 ECU: a079 VCBATT2 MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a080_VCFRONT0_MIA` | page 1 | VCFRONT2 ECU: a080 VCFRONT0 MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a081_VCFRONT1_MIA` | page 1 | VCFRONT2 ECU: a081 VCFRONT1 MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a082_VCFRONT2_MIA` | page 1 | VCFRONT2 ECU: a082 VCFRONT2 MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a086_VCBATT_MIA` | page 1 | VCFRONT2 ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a090_APS_MIA` | page 1 | VCFRONT2 ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a091_CMPD_MIA` | page 1 | VCFRONT2 ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a096_OCS1P_MIA` | page 1 | VCFRONT2 ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a098_DIR_MIA` | page 1 | VCFRONT2 ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a100_CANbus_MIA` | page 1 | VCFRONT2 ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a103_CP_MIA` | page 1 | VCFRONT2 ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a104_DAS_MIA` | page 1 | VCFRONT2 ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a105_TAS_MIA` | page 1 | VCFRONT2 ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a106_PCS_MIA` | page 1 | VCFRONT2 ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a107_BMS_MIA` | page 1 | VCFRONT2 ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a108_DIF_MIA` | page 1 | VCFRONT2 ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a109_RCM_MIA` | page 1 | VCFRONT2 ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a110_GTW_MIA` | page 1 | VCFRONT2 ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a111_EPBR_MIA` | page 1 | VCFRONT2 ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a112_EPBL_MIA` | page 1 | VCFRONT2 ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a113_UI_MIA` | page 1 | VCFRONT2 ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a114_ESP_MIA` | page 1 | VCFRONT2 ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a115_VCSEC_MIA` | page 1 | VCFRONT2 ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a116_VCRIGHT_MIA` | page 1 | VCFRONT2 ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a117_VCLEFT_MIA` | page 1 | VCFRONT2 ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a118_VCFRONT_MIA` | page 1 | VCFRONT2 ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a119_SCCM_MIA` | page 1 | VCFRONT2 ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a120_DI_DRIVE_MIA` | page 1 | VCFRONT2 ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a122_ICR_MIA` | page 2 | VCFRONT2 ECU: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a123_VC_SECONDARY_LIGHTING_LEADER_MIA` | page 2 | VCFRONT2 ECU: a123 VC SECONDARY LIGHTING LEADER MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a124_BB_MIA` | page 2 | VCFRONT2 ECU: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a125_SCCM_MIA` | page 2 | VCFRONT2 ECU: a125 SCCM MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a126_EPAS3P_MIA` | page 2 | VCFRONT2 ECU: a126 EPAS3 p MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a131_PCSCOMMON_MIA` | page 2 | VCFRONT2 ECU: a131 PCSCOMMON MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a133_BRAKE_MIA` | page 2 | VCFRONT2 ECU: a133 BRAKE MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a135_coolantLevelLow` | page 2 | VCFRONT2 ECU: a135 coolant level low | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a136_refrigDischTempSns` | page 2 | VCFRONT2 ECU: a136 refrig disch temp sns | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a137_refrigDischPresSns` | page 2 | VCFRONT2 ECU: a137 refrig disch pres sns | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a138_refrigSuctTempSns` | page 2 | VCFRONT2 ECU: a138 refrig suct temp sns | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a139_refrigSuctPresSns` | page 2 | VCFRONT2 ECU: a139 refrig suct pres sns | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a140_coolantTempPtSns` | page 2 | VCFRONT2 ECU: a140 coolant temp pt sns | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a141_coolantTempBatSns` | page 2 | VCFRONT2 ECU: a141 coolant temp bat sns | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a142_exvMotorFault` | page 2 | VCFRONT2 ECU: a142 exv motor fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a143_powerLossDuringSleep` | page 2 | VCFRONT2 ECU: a143 power loss during sleep | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a144_EPAS3S_MIA` | page 2 | VCFRONT2 ECU: a144 EPAS3 s MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a150_pumpBatLowRPMCBang` | page 2 | VCFRONT2 ECU: a150 pump bat low RPMC bang | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a153_userPresenceDisplayMismatchClrd` | page 2 | VCFRONT2 ECU: a153 user presence display mismatch clrd | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a155_autopilotDriveNotAuthed` | page 2 | VCFRONT2 ECU: a155 autopilot drive not authed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a159_coolantValveFault` | page 2 | VCFRONT2 ECU: a159 coolant valve fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a160_compressorInhibited` | page 2 | VCFRONT2 ECU: a160 compressor inhibited | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a161_compressorSelfFault` | page 2 | VCFRONT2 ECU: a161 compressor self fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a162_compressorInhibitedContext` | page 2 | VCFRONT2 ECU: a162 compressor inhibited context | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a163_compressorDisabledFSR` | page 2 | VCFRONT2 ECU: a163 compressor disabled FSR | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a167_leftHCMMIA` | page 2 | VCFRONT2 ECU: a167 left HCMMIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a171_driveBlckdByMsmtch` | page 2 | VCFRONT2 ECU: a171 drive blckd by msmtch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a172_wsteHtBlckdByMsmtch` | page 2 | VCFRONT2 ECU: a172 wste ht blckd by msmtch | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a173_HVBlckdByMsmtch` | page 2 | VCFRONT2 ECU: a173 HV blckd by msmtch | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a174_driveNotAuthed` | page 2 | VCFRONT2 ECU: a174 drive not authed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a176_vehicleInSelfTest` | page 2 | VCFRONT2 ECU: a176 vehicle in self test | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a178_compLiquidPumpOut` | page 2 | VCFRONT2 ECU: a178 comp liquid pump out | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a184_cabinCoolingPerformanceAbnormal` | page 3 | VCFRONT2 ECU: a184 cabin cooling performance abnormal | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a186_noDriveChgCableCon` | page 3 | VCFRONT2 ECU: a186 no drive chg cable con | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a187_busesNotSleeping` | page 3 | VCFRONT2 ECU: a187 buses not sleeping | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a188_sleepFailed` | page 3 | VCFRONT2 ECU: a188 sleep failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a195_drveBlckdVltgeTooHgh` | page 3 | VCFRONT2 ECU: a195 drve blckd vltge too hgh | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a210_coolantValveCalib` | page 3 | VCFRONT2 ECU: a210 coolant valve calib | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a214_ptPumpCompromised` | page 3 | VCFRONT2 ECU: a214 pt pump compromised | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a215_ptPumpMIA` | page 3 | VCFRONT2 ECU: a215 pt pump MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a217_battPumpCompromised` | page 3 | VCFRONT2 ECU: a217 batt pump compromised | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a218_socMonitorDetectedThresholdSoc` | page 3 | VCFRONT2 ECU: a218 soc monitor detected threshold soc | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a225_driveBlckdByShowroom` | page 3 | VCFRONT2 ECU: a225 drive blckd by showroom | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a226_battPumpMIA` | page 3 | VCFRONT2 ECU: a226 batt pump MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a232_lowSideControllerHighFdbk` | page 3 | VCFRONT2 ECU: a232 low side controller high fdbk | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a235_ptTempSnsIrrational` | page 3 | VCFRONT2 ECU: a235 pt temp sns irrational | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a236_batTempSnsIrrational` | page 3 | VCFRONT2 ECU: a236 bat temp sns irrational | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a240_lowSideCompromised` | page 3 | VCFRONT2 ECU: a240 low side compromised | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a247_evapSolenoidFault` | page 4 | VCFRONT2 ECU: a247 evap solenoid fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a249_coolantValveBadMode` | page 4 | VCFRONT2 ECU: a249 coolant valve bad mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a250_headlampsNotAimed` | page 4 | VCFRONT2 ECU: a250 headlamps not aimed | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a251_UIWakeupTrigger` | page 4 | VCFRONT2 ECU: a251 UI wakeup trigger | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a254_pumpBatStopped` | page 4 | VCFRONT2 ECU: a254 pump bat stopped | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a273_wiperFrictionModelFault` | page 4 | VCFRONT2 ECU: a273 wiper friction model fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a279_refrigLiquidTempSns` | page 4 | VCFRONT2 ECU: a279 refrig liquid temp sns | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a280_refrigLiquidPresSns` | page 4 | VCFRONT2 ECU: a280 refrig liquid pres sns | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a281_alcoholInterlockBlockingDrive` | page 4 | VCFRONT2 ECU: a281 alcohol interlock blocking drive | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a282_coolantLevelSensorFault` | page 4 | VCFRONT2 ECU: a282 coolant level sensor fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a283_thmlFanLimitedByCurrent` | page 4 | VCFRONT2 ECU: a283 thml fan limited by current | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a284_chillerExvFault` | page 4 | VCFRONT2 ECU: a284 chiller exv fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a285_evaporatorExvFault` | page 4 | VCFRONT2 ECU: a285 evaporator exv fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a286_recircExvFault` | page 4 | VCFRONT2 ECU: a286 recirc exv fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a287_lccExvFault` | page 4 | VCFRONT2 ECU: a287 lcc exv fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a288_ccLeftExvFault` | page 4 | VCFRONT2 ECU: a288 cc left exv fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a289_ccRightExvFault` | page 4 | VCFRONT2 ECU: a289 cc right exv fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a294_leftSideRepeaterLightFault` | page 4 | VCFRONT2 ECU: a294 left side repeater light fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a298_radiatorLowAirFlowDetected` | page 4 | VCFRONT2 ECU: a298 radiator low air flow detected | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a301_wipersFactoryDisabled` | page 5 | VCFRONT2 ECU: a301 wipers factory disabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a302_wiperCommError` | page 5 | VCFRONT2 ECU: a302 wiper comm error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a355_coolantSysLockout` | page 5 | VCFRONT2 ECU: a355 coolant sys lockout | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a356_refrigSysLockout` | page 5 | VCFRONT2 ECU: a356 refrig sys lockout | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a360_ungracefulAccPlusExit` | page 5 | VCFRONT2 ECU: a360 ungraceful acc plus exit | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a365_burnInRoutineEntered` | page 6 | VCFRONT2 ECU: a365 burn in routine entered | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a366_burnInRoutineExited` | page 6 | VCFRONT2 ECU: a366 burn in routine exited | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a367_dischargeRoutineEntered` | page 6 | VCFRONT2 ECU: a367 discharge routine entered | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a368_dischargeRoutineExited` | page 6 | VCFRONT2 ECU: a368 discharge routine exited | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a369_reducedPowerDischarge` | page 6 | VCFRONT2 ECU: a369 reduced power discharge | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a374_lccInletSolenoidFault` | page 6 | VCFRONT2 ECU: a374 lcc inlet solenoid fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a377_wiperParkFault` | page 6 | VCFRONT2 ECU: a377 wiper park fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a378_wiperECUDebug` | page 6 | VCFRONT2 ECU: a378 wiper ECU debug | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a380_chillerExvWarning` | page 6 | VCFRONT2 ECU: a380 chiller exv warning | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a381_evaporatorExvWarning` | page 6 | VCFRONT2 ECU: a381 evaporator exv warning | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a382_recircExvWarning` | page 6 | VCFRONT2 ECU: a382 recirc exv warning | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a383_lccExvWarning` | page 6 | VCFRONT2 ECU: a383 lcc exv warning | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a384_ccLeftExvWarning` | page 6 | VCFRONT2 ECU: a384 cc left exv warning | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a385_ccRightExvWarning` | page 6 | VCFRONT2 ECU: a385 cc right exv warning | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a386_exvMotorWarning` | page 6 | VCFRONT2 ECU: a386 exv motor warning | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a393_ambientTempNetworkSna` | page 6 | VCFRONT2 ECU: a393 ambient temp network sna | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a394_pressureSensorCheckFault` | page 6 | VCFRONT2 ECU: a394 pressure sensor check fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a395_pressureSensorCheckInconclusive` | page 6 | VCFRONT2 ECU: a395 pressure sensor check inconclusive | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a396_coolantLevelLowUserFacing` | page 6 | VCFRONT2 ECU: a396 coolant level low user facing | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a397_temperatureSensorCheckFault` | page 6 | VCFRONT2 ECU: a397 temperature sensor check fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a398_tempSensorCheckInconclusive` | page 6 | VCFRONT2 ECU: a398 temp sensor check inconclusive | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a409_invalidConfiguration` | page 6 | VCFRONT2 ECU: a409 invalid configuration | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a420_holidayParty` | page 6 | VCFRONT2 ECU: a420 holiday party | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a421_leftHeadlampUartCondition` | page 7 | VCFRONT2 ECU: a421 left headlamp uart condition | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a423_rtosSleepFailed` | page 7 | VCFRONT2 ECU: a423 rtos sleep failed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a446_cabinHVACUnavailableContext` | page 7 | VCFRONT2 ECU: a446 cabin HVAC unavailable context | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a447_cabinHVACUnavailable` | page 7 | VCFRONT2 ECU: a447 cabin HVAC unavailable | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a451_refrigerantNotCommissioned` | page 7 | VCFRONT2 ECU: a451 refrigerant not commissioned | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a452_dischargePresSensIntermittent` | page 7 | VCFRONT2 ECU: a452 discharge pres sens intermittent | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a453_dischargeTempSensIntermittent` | page 7 | VCFRONT2 ECU: a453 discharge temp sens intermittent | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a454_suctionPresSensIntermittent` | page 7 | VCFRONT2 ECU: a454 suction pres sens intermittent | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a455_suctionTempSensIntermittent` | page 7 | VCFRONT2 ECU: a455 suction temp sens intermittent | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a456_liquidPresSensIntermittent` | page 7 | VCFRONT2 ECU: a456 liquid pres sens intermittent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a457_liquidTempSensIntermittent` | page 7 | VCFRONT2 ECU: a457 liquid temp sens intermittent | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a458_grosslyLowRefrigerant` | page 7 | VCFRONT2 ECU: a458 grossly low refrigerant | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a459_thermalFillAndDrive` | page 7 | VCFRONT2 ECU: a459 thermal fill and drive | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a460_hardIsentropicTdFailed` | page 7 | VCFRONT2 ECU: a460 hard isentropic td failed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a464_highFlowIndexHighSubcoolFlagged` | page 7 | VCFRONT2 ECU: a464 high flow index high subcool flagged | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a465_lowFlowIndexHighSubcoolFlagged` | page 7 | VCFRONT2 ECU: a465 low flow index high subcool flagged | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a466_highFlowIndexLowSubcoolFlagged` | page 7 | VCFRONT2 ECU: a466 high flow index low subcool flagged | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a467_lowPowerIndexFlagged` | page 7 | VCFRONT2 ECU: a467 low power index flagged | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a468_highPowerIndexFlagged` | page 7 | VCFRONT2 ECU: a468 high power index flagged | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a469_prvPopDetected` | page 7 | VCFRONT2 ECU: a469 prv pop detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a470_implausiblePdPlDetected` | page 7 | VCFRONT2 ECU: a470 implausible pd pl detected | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a471_hcm5Debug` | page 7 | VCFRONT2 ECU: a471 hcm5 debug | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a474_leftHeadlampInternalError` | page 7 | VCFRONT2 ECU: a474 left headlamp internal error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a489_ValveStuckFlagged` | page 8 | VCFRONT2 ECU: a489 valve stuck flagged | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a490_coolantPumpsNotIdentified` | page 8 | VCFRONT2 ECU: a490 coolant pumps not identified | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a499_loadShedPumpFlowRequest` | page 8 | VCFRONT2 ECU: a499 load shed pump flow request | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a504_airInRefrigerantDetected` | page 8 | VCFRONT2 ECU: a504 air in refrigerant detected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a506_invalidRefrigerantSystemConfig` | page 8 | VCFRONT2 ECU: a506 invalid refrigerant system config | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a507_leftHeadlampAimingFault` | page 8 | VCFRONT2 ECU: a507 left headlamp aiming fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a511_DCDCSaturationLoadShed` | page 8 | VCFRONT2 ECU: a511 DCDC saturation load shed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a519_leftHeadlampInternalErrorV2` | page 8 | VCFRONT2 ECU: a519 left headlamp internal error V2 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a531_lowPowerIndexFlaggedUserFacing` | page 8 | VCFRONT2 ECU: a531 low power index flagged user facing | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a534_chillerExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a534 chiller exv calib init debug | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a535_evapExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a535 evap exv calib init debug | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a536_recircExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a536 recirc exv calib init debug | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a537_lccExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a537 lcc exv calib init debug | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a538_cclExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a538 ccl exv calib init debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a539_ccrExvCalibInitDebug` | page 8 | VCFRONT2 ECU: a539 ccr exv calib init debug | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a540_radiatorSteamDetected` | page 8 | VCFRONT2 ECU: a540 radiator steam detected | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a542_refrigerantReclaim` | page 9 | VCFRONT2 ECU: a542 refrigerant reclaim | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a543_compressorLowFlowDeliveryDetected` | page 9 | VCFRONT2 ECU: a543 compressor low flow delivery detected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a546_leftLowOrHighBeamLightCondition` | page 9 | VCFRONT2 ECU: a546 left low or high beam light condition | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a549_leftHeadlampInternalErrorV3` | page 9 | VCFRONT2 ECU: a549 left headlamp internal error V3 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a560_compressorHighSuperheat` | page 9 | VCFRONT2 ECU: a560 compressor high superheat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a563_chargePortDoorOpenBlockedByBrake` | page 9 | VCFRONT2 ECU: a563 charge port door open blocked by brake | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a564_leftHeadlampAimingDebug` | page 9 | VCFRONT2 ECU: a564 left headlamp aiming debug | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a565_userPresenceDisplayStateMismatch` | page 9 | VCFRONT2 ECU: a565 user presence display state mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a566_leftFrontTurnLightFault` | page 9 | VCFRONT2 ECU: a566 left front turn light fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a568_leftDaytimeRunningLightFault` | page 9 | VCFRONT2 ECU: a568 left daytime running light fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a570_headlampsAdaptedToLeftHandTraffic` | page 9 | VCFRONT2 ECU: a570 headlamps adapted to left hand traffic | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a571_headlampsAdaptedToRightHandTraffic` | page 9 | VCFRONT2 ECU: a571 headlamps adapted to right hand traffic | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a572_hvacCompressorEFuseTrip` | page 9 | VCFRONT2 ECU: a572 hvac compressor e fuse trip | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a578_vbusFusedLowCurrentFeedEFuseTrip` | page 9 | VCFRONT2 ECU: a578 vbus fused low current feed e fuse trip | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a585_bothHeadlampsInternalError` | page 9 | VCFRONT2 ECU: a585 both headlamps internal error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a601_autopilotAirPurgeLimitReached` | page 10 | VCFRONT2 ECU: a601 autopilot air purge limit reached | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a602_unknownTurnIndicatorConfig` | page 10 | VCFRONT2 ECU: a602 unknown turn indicator config | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a603_unexpectedTurnIndicatorConfigChange` | page 10 | VCFRONT2 ECU: a603 unexpected turn indicator config change | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a604_turnIndicatorConfigInputMismatch` | page 10 | VCFRONT2 ECU: a604 turn indicator config input mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a606_chillerBattHeatingExit` | page 10 | VCFRONT2 ECU: a606 chiller batt heating exit | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a610_driveEntryDelayed` | page 10 | VCFRONT2 ECU: a610 drive entry delayed | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a611_poorRadiatorHeatRejection` | page 10 | VCFRONT2 ECU: a611 poor radiator heat rejection | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a612_selfTestsBlockingDrive` | page 10 | VCFRONT2 ECU: a612 self tests blocking drive | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a614_coolantSysDriverlessSelfTest` | page 10 | VCFRONT2 ECU: a614 coolant sys driverless self test | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a615_VCSEAT2L_MIA` | page 10 | VCFRONT2 ECU: a615 VCSEAT2 l MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a616_VCSEAT2R_MIA` | page 10 | VCFRONT2 ECU: a616 VCSEAT2 r MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a617_APP_MIA` | page 10 | VCFRONT2 ECU: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a618_cabinCoolingCapacityLimited` | page 10 | VCFRONT2 ECU: a618 cabin cooling capacity limited | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a620_pumpAirLock` | page 10 | VCFRONT2 ECU: a620 pump air lock | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a621_coolantAirPurgeIncomplete` | page 10 | VCFRONT2 ECU: a621 coolant air purge incomplete | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a622_pumpDetectsLowCoolantFlow` | page 10 | VCFRONT2 ECU: a622 pump detects low coolant flow | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a625_leftHeadlampInternalErrorV4` | page 10 | VCFRONT2 ECU: a625 left headlamp internal error V4 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a630_leftHeadlampFactoryFault` | page 10 | VCFRONT2 ECU: a630 left headlamp factory fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d636_ptCoolantPumpDetectsAirInSystem` | page 10 | VCFRONT2 ECU: d636 pt coolant pump detects air in system | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d637_battCoolantPumpDetectsAirInSystem` | page 10 | VCFRONT2 ECU: d637 batt coolant pump detects air in system | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d638_ptCoolantTempSensorIssue` | page 10 | VCFRONT2 ECU: d638 pt coolant temp sensor issue | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d639_batteryCoolantTempSensorIssue` | page 10 | VCFRONT2 ECU: d639 battery coolant temp sensor issue | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d640_firmwareVersionMismatch` | page 10 | VCFRONT2 ECU: d640 firmware version mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d641_ptCoolantPumpCircuitOpen` | page 10 | VCFRONT2 ECU: d641 pt coolant pump circuit open | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d642_batteryCoolantPumpCircuitOpen` | page 10 | VCFRONT2 ECU: d642 battery coolant pump circuit open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d647_louverCommLost` | page 10 | VCFRONT2 ECU: d647 louver comm lost | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d648_louverBlocked` | page 10 | VCFRONT2 ECU: d648 louver blocked | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d650_lowCoolantLevel` | page 10 | VCFRONT2 ECU: d650 low coolant level | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d651_ptCoolantPumpStall` | page 10 | VCFRONT2 ECU: d651 pt coolant pump stall | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d652_ptCoolantPumpCircuitIssue` | page 10 | VCFRONT2 ECU: d652 pt coolant pump circuit issue | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d653_ptCoolantPumpCommLost` | page 10 | VCFRONT2 ECU: d653 pt coolant pump comm lost | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d654_batteryCoolantPumpStall` | page 10 | VCFRONT2 ECU: d654 battery coolant pump stall | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d655_batteryCoolantPumpCircuitIssue` | page 10 | VCFRONT2 ECU: d655 battery coolant pump circuit issue | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d656_batteryCoolantPumpCommLost` | page 10 | VCFRONT2 ECU: d656 battery coolant pump comm lost | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d657_radiatorFanOperationIssue` | page 10 | VCFRONT2 ECU: d657 radiator fan operation issue | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d658_radiatorFanCircuitIssue` | page 10 | VCFRONT2 ECU: d658 radiator fan circuit issue | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d659_radiatorFanCommLost` | page 10 | VCFRONT2 ECU: d659 radiator fan comm lost | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_d660_coolantValveCircuitIssue` | page 10 | VCFRONT2 ECU: d660 coolant valve circuit issue | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a661_mculessLeftHeadlampCurrentAlertDbg` | page 11 | VCFRONT2 ECU: a661 mculess left headlamp current alert dbg | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a662_driveExitBlockedIndefinitelyBySelfTestRequest` | page 11 | VCFRONT2 ECU: a662 drive exit blocked indefinitely by self test request | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a663_leftHeadlampUartWaterMarkWarning` | page 11 | VCFRONT2 ECU: a663 left headlamp uart water mark warning | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a665_leftHeadlampRetryInfo` | page 11 | VCFRONT2 ECU: a665 left headlamp retry info | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a667_leftHeadlampRegionOrSideMismatch` | page 11 | VCFRONT2 ECU: a667 left headlamp region or side mismatch | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a669_thermalHVPowerBudgetActive` | page 11 | VCFRONT2 ECU: a669 thermal HV power budget active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a697_leftHeadlampNotAimed` | page 11 | VCFRONT2 ECU: a697 left headlamp not aimed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT2_a702_dynamicHeadlightLevelingUnavailable` | page 11 | VCFRONT2 ECU: a702 dynamic headlight leveling unavailable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCFRONT2_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (37 signals), page 1 (34 signals), page 2 (32 signals), page 3 (16 signals), page 4 (19 signals), page 5 (5 signals), page 6 (23 signals), page 7 (23 signals), page 8 (16 signals), page 9 (15 signals), page 10 (38 signals), page 11 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT2 ECU messages (VCFRONT2)](../../vcfront2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
