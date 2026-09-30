---
layout: default
title: "USM_alertMatrix (0x3BA) — USM ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "USM ECU message: alert matrix. Tesla Model 3 / Model Y CAN bus message USM_alertMatrix (0x3BA) of USM ECU, firmware 2026.26.6.5, 182 signals (USM_matrixIndex, USM_a001_WatchdogReset, USM_a002_PowerLossReset, USM_a003_SWAssertion and 178 more). Bit layout, scaling, units and value tables."
---

# USM_alertMatrix (0x3BA) — USM ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

USM ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 182 signals of USM_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `USM_alertMatrix` |
| CAN id | 0x3BA (954) |
| ECU | [USM ECU](../../usm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | USM |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 182 |

## Signals of USM_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `USM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `USM_matrixIndex` | selector | USM ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4` | plausible |
| `USM_a001_WatchdogReset` | page 0 | USM ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a002_PowerLossReset` | page 0 | USM ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a003_SWAssertion` | page 0 | USM ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a005_CANTXError` | page 0 | USM ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a006_CANTX_cyclicError` | page 0 | USM ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a012_CPUReset` | page 0 | USM ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a013_AlertManagerFault` | page 0 | USM ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a015_NVMMError` | page 0 | USM ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a016_NVMMRecordError` | page 0 | USM ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a021_TaskSchedulerError` | page 0 | USM ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a022_TaskInitError` | page 0 | USM ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a029_CoreDump` | page 0 | USM ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a030_ECULogUploadRequest` | page 0 | USM ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a031_UDSActive` | page 0 | USM ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a041_HighCPULoad` | page 0 | USM ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a042_HighStackUsage` | page 0 | USM ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a043_Task1msError` | page 0 | USM ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a044_Task10msError` | page 0 | USM ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a045_Task100msError` | page 0 | USM ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a046_Task1000msError` | page 0 | USM ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a057_HVP_MIA` | page 0 | USM ECU: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a058_inputRHighSyncDebug` | page 0 | USM ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a059_inputResistanceHigh` | page 0 | USM ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a060_engineeringBuild` | page 0 | USM ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a061_XCPConnected` | page 1 | USM ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a062_XCPWasConnected` | page 1 | USM ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a063_SwitchFault` | page 1 | USM ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a064_busSleepReqTimeout` | page 1 | USM ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a082_VCRIGHT_IPC_MIA` | page 1 | USM ECU: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a083_VCLEFT_IPC_MIA` | page 1 | USM ECU: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a084_TPMS_MIA` | page 1 | USM ECU: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a085_CCCM_MIA` | page 1 | USM ECU: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VCBATT_MIA` | page 1 | USM ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_DIREL_MIA` | page 1 | USM ECU: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_DIRER_MIA` | page 1 | USM ECU: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_IBST_MIA` | page 1 | USM ECU: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a090_APS_MIA` | page 1 | USM ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a091_CMPD_MIA` | page 1 | USM ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a092_VCSEATD_MIA` | page 1 | USM ECU: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a093_VCSEATP_MIA` | page 1 | USM ECU: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a094_EPAS3P_MIA` | page 1 | USM ECU: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a095_CHG_MIA` | page 1 | USM ECU: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a096_OCS1P_MIA` | page 1 | USM ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a097_CMP_MIA` | page 1 | USM ECU: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_DIR_MIA` | page 1 | USM ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a099_PARK_MIA` | page 1 | USM ECU: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_CANbus_MIA` | page 1 | USM ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_PM_MIA` | page 1 | USM ECU: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a102_PTC_MIA` | page 1 | USM ECU: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_CP_MIA` | page 1 | USM ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a104_DAS_MIA` | page 1 | USM ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a105_TAS_MIA` | page 1 | USM ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_PCS_MIA` | page 1 | USM ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_BMS_MIA` | page 1 | USM ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_DIF_MIA` | page 1 | USM ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_RCM_MIA` | page 1 | USM ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_GTW_MIA` | page 1 | USM ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_EPBR_MIA` | page 1 | USM ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_EPBL_MIA` | page 1 | USM ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a113_UI_MIA` | page 1 | USM ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_ESP_MIA` | page 1 | USM ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VCSEC_MIA` | page 1 | USM ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VCRIGHT_MIA` | page 1 | USM ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VCLEFT_MIA` | page 1 | USM ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VCFRONT_MIA` | page 1 | USM ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_SCCM_MIA` | page 1 | USM ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_DI_DRIVE_MIA` | page 1 | USM ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a131_s1ComError` | page 2 | USM ECU: a131 s1 com error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a132_s2ComError` | page 2 | USM ECU: a132 s2 com error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a133_s3ComError` | page 2 | USM ECU: a133 s3 com error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a134_s4ComError` | page 2 | USM ECU: a134 s4 com error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a135_s5ComError` | page 2 | USM ECU: a135 s5 com error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a136_s6ComError` | page 2 | USM ECU: a136 s6 com error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a137_s7ComError` | page 2 | USM ECU: a137 s7 com error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a138_s8ComError` | page 2 | USM ECU: a138 s8 com error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a139_s9ComError` | page 2 | USM ECU: a139 s9 com error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a140_s10ComError` | page 2 | USM ECU: a140 s10 com error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a141_s11ComError` | page 2 | USM ECU: a141 s11 com error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a142_s12ComError` | page 2 | USM ECU: a142 s12 com error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a143_s1HwError` | page 2 | USM ECU: a143 s1 hw error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a144_s2HwError` | page 2 | USM ECU: a144 s2 hw error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a145_s3HwError` | page 2 | USM ECU: a145 s3 hw error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a146_s4HwError` | page 2 | USM ECU: a146 s4 hw error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a147_s5HwError` | page 2 | USM ECU: a147 s5 hw error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a148_s6HwError` | page 2 | USM ECU: a148 s6 hw error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a149_s7HwError` | page 2 | USM ECU: a149 s7 hw error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a150_s8HwError` | page 2 | USM ECU: a150 s8 hw error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a151_s9HwError` | page 2 | USM ECU: a151 s9 hw error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a152_s10HwError` | page 2 | USM ECU: a152 s10 hw error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a153_s11HwError` | page 2 | USM ECU: a153 s11 hw error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a154_s12HwError` | page 2 | USM ECU: a154 s12 hw error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a155_s1OverTemp` | page 2 | USM ECU: a155 s1 over temp | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a156_s2OverTemp` | page 2 | USM ECU: a156 s2 over temp | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a157_s3OverTemp` | page 2 | USM ECU: a157 s3 over temp | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a158_s4OverTemp` | page 2 | USM ECU: a158 s4 over temp | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a159_s5OverTemp` | page 2 | USM ECU: a159 s5 over temp | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a160_s6OverTemp` | page 2 | USM ECU: a160 s6 over temp | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a161_s7OverTemp` | page 2 | USM ECU: a161 s7 over temp | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a162_s8OverTemp` | page 2 | USM ECU: a162 s8 over temp | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a163_s9OverTemp` | page 2 | USM ECU: a163 s9 over temp | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a164_s10OverTemp` | page 2 | USM ECU: a164 s10 over temp | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a165_s11OverTemp` | page 2 | USM ECU: a165 s11 over temp | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a166_s12OverTemp` | page 2 | USM ECU: a166 s12 over temp | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a177_s1Blocked` | page 2 | USM ECU: a177 s1 blocked | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a178_s2Blocked` | page 2 | USM ECU: a178 s2 blocked | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a179_s3Blocked` | page 2 | USM ECU: a179 s3 blocked | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a180_s4Blocked` | page 2 | USM ECU: a180 s4 blocked | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a181_s5Blocked` | page 3 | USM ECU: a181 s5 blocked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a182_s6Blocked` | page 3 | USM ECU: a182 s6 blocked | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a183_s7Blocked` | page 3 | USM ECU: a183 s7 blocked | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a184_s8Blocked` | page 3 | USM ECU: a184 s8 blocked | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a185_s9Blocked` | page 3 | USM ECU: a185 s9 blocked | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a186_s10Blocked` | page 3 | USM ECU: a186 s10 blocked | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a187_s11Blocked` | page 3 | USM ECU: a187 s11 blocked | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a188_s12Blocked` | page 3 | USM ECU: a188 s12 blocked | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a189_s1Disconnected` | page 3 | USM ECU: a189 s1 disconnected | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a190_s2Disconnected` | page 3 | USM ECU: a190 s2 disconnected | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a191_s3Disconnected` | page 3 | USM ECU: a191 s3 disconnected | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a192_s4Disconnected` | page 3 | USM ECU: a192 s4 disconnected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a193_s5Disconnected` | page 3 | USM ECU: a193 s5 disconnected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a194_s6Disconnected` | page 3 | USM ECU: a194 s6 disconnected | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a195_s7Disconnected` | page 3 | USM ECU: a195 s7 disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a196_s8Disconnected` | page 3 | USM ECU: a196 s8 disconnected | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a197_s9Disconnected` | page 3 | USM ECU: a197 s9 disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a198_s10Disconnected` | page 3 | USM ECU: a198 s10 disconnected | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a199_s11Disconnected` | page 3 | USM ECU: a199 s11 disconnected | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a200_s12Disconnected` | page 3 | USM ECU: a200 s12 disconnected | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_e52142Fault` | page 3 | USM ECU: a201 e52142 fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_e52417Fault` | page 3 | USM ECU: a202 e52417 fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a203_s1NearFieldDetected` | page 3 | USM ECU: a203 s1 near field detected | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a204_s2NearFieldDetected` | page 3 | USM ECU: a204 s2 near field detected | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a205_s3NearFieldDetected` | page 3 | USM ECU: a205 s3 near field detected | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a206_s4NearFieldDetected` | page 3 | USM ECU: a206 s4 near field detected | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a207_s5NearFieldDetected` | page 3 | USM ECU: a207 s5 near field detected | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a208_s6NearFieldDetected` | page 3 | USM ECU: a208 s6 near field detected | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a209_s7NearFieldDetected` | page 3 | USM ECU: a209 s7 near field detected | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a210_s8NearFieldDetected` | page 3 | USM ECU: a210 s8 near field detected | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a211_s9NearFieldDetected` | page 3 | USM ECU: a211 s9 near field detected | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a212_s10NearFieldDetected` | page 3 | USM ECU: a212 s10 near field detected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a213_s11NearFieldDetected` | page 3 | USM ECU: a213 s11 near field detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a214_s12NearFieldDetected` | page 3 | USM ECU: a214 s12 near field detected | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a215_s1DebugEepromInvalid` | page 3 | USM ECU: a215 s1 debug eeprom invalid | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a216_s2DebugEepromInvalid` | page 3 | USM ECU: a216 s2 debug eeprom invalid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a217_s3DebugEepromInvalid` | page 3 | USM ECU: a217 s3 debug eeprom invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a218_s4DebugEepromInvalid` | page 3 | USM ECU: a218 s4 debug eeprom invalid | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a219_s5DebugEepromInvalid` | page 3 | USM ECU: a219 s5 debug eeprom invalid | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a220_s6DebugEepromInvalid` | page 3 | USM ECU: a220 s6 debug eeprom invalid | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a221_s7DebugEepromInvalid` | page 3 | USM ECU: a221 s7 debug eeprom invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a222_s8DebugEepromInvalid` | page 3 | USM ECU: a222 s8 debug eeprom invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a223_s9DebugEepromInvalid` | page 3 | USM ECU: a223 s9 debug eeprom invalid | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a224_s10DebugEepromInvalid` | page 3 | USM ECU: a224 s10 debug eeprom invalid | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a225_s11DebugEepromInvalid` | page 3 | USM ECU: a225 s11 debug eeprom invalid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a226_s12DebugEepromInvalid` | page 3 | USM ECU: a226 s12 debug eeprom invalid | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_s1InitError` | page 3 | USM ECU: a227 s1 init error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_s2InitError` | page 3 | USM ECU: a228 s2 init error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_s3InitError` | page 3 | USM ECU: a229 s3 init error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_s4InitError` | page 3 | USM ECU: a230 s4 init error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_s5InitError` | page 3 | USM ECU: a231 s5 init error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_s6InitError` | page 3 | USM ECU: a232 s6 init error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_s7InitError` | page 3 | USM ECU: a233 s7 init error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_s8InitError` | page 3 | USM ECU: a234 s8 init error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_s9InitError` | page 3 | USM ECU: a235 s9 init error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_s10InitError` | page 3 | USM ECU: a236 s10 init error | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_s11InitError` | page 3 | USM ECU: a237 s11 init error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_s12InitError` | page 3 | USM ECU: a238 s12 init error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a240_s1HwComErrDiagnostics` | page 3 | USM ECU: a240 s1 hw com err diagnostics | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a241_s2HwComErrDiagnostics` | page 4 | USM ECU: a241 s2 hw com err diagnostics | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a242_s3HwComErrDiagnostics` | page 4 | USM ECU: a242 s3 hw com err diagnostics | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a243_s4HwComErrDiagnostics` | page 4 | USM ECU: a243 s4 hw com err diagnostics | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a244_s5HwComErrDiagnostics` | page 4 | USM ECU: a244 s5 hw com err diagnostics | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a245_s6HwComErrDiagnostics` | page 4 | USM ECU: a245 s6 hw com err diagnostics | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a246_s7HwComErrDiagnostics` | page 4 | USM ECU: a246 s7 hw com err diagnostics | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a247_s8HwComErrDiagnostics` | page 4 | USM ECU: a247 s8 hw com err diagnostics | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a248_s9HwComErrDiagnostics` | page 4 | USM ECU: a248 s9 hw com err diagnostics | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a249_s10HwComErrDiagnostics` | page 4 | USM ECU: a249 s10 hw com err diagnostics | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a250_s11HwComErrDiagnostics` | page 4 | USM ECU: a250 s11 hw com err diagnostics | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a251_s12HwComErrDiagnostics` | page 4 | USM ECU: a251 s12 hw com err diagnostics | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a252_anyComErrorSet` | page 4 | USM ECU: a252 any com error set | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a253_anyHwErrorSet` | page 4 | USM ECU: a253 any hw error set | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a254_frontSensorsOvercurrent` | page 4 | USM ECU: a254 front sensors overcurrent | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a255_rearSensorsOvercurrent` | page 4 | USM ECU: a255 rear sensors overcurrent | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`USM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (24 signals), page 1 (43 signals), page 2 (40 signals), page 3 (59 signals), page 4 (15 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All USM ECU messages (USM)](../../usm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
