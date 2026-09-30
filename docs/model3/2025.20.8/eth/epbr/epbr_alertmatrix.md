---
layout: default
title: "EPBR_alertMatrix (0x3E8) — Right electric parking brake, Tesla Model 3 2025.20.8 ETH"
description: "Right electric parking brake message: alert matrix. Ethernet-side message EPBR_alertMatrix of Right electric parking brake for Tesla Model 3 firmware 2025.20.8, 163 signals (EPBR_matrixIndex, EPBR_a001_WatchdogReset, EPBR_a002_PowerLossReset, EPBR_a003_SWAssertion and 159 more). Bit layout, scaling, units and value tables."
---

# EPBR_alertMatrix (0x3E8) — Right electric parking brake, Tesla Model 3 2025.20.8 ETH

Right electric parking brake message: alert matrix. This page documents the 163 signals of EPBR_alertMatrix as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPBR_alertMatrix` |
| Ethernet-side id | 0x3E8 (1000) |
| ECU | [Right electric parking brake](../../epbr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPBR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 163 |

## Signals of EPBR_alertMatrix

Tesla Model 3 CAN bus signals in `EPBR_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPBR_matrixIndex` | selector | Right electric parking brake: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6` | plausible |
| `EPBR_a001_WatchdogReset` | page 0 | Right electric parking brake: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a002_PowerLossReset` | page 0 | Right electric parking brake: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a003_SWAssertion` | page 0 | Right electric parking brake: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a005_CANTXError` | page 0 | Right electric parking brake: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a006_CANTX_cyclicError` | page 0 | Right electric parking brake: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a012_CPUReset` | page 0 | Right electric parking brake: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a013_AlertManagerFault` | page 0 | Right electric parking brake: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a015_NVMMError` | page 0 | Right electric parking brake: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a016_NVMMRecordError` | page 0 | Right electric parking brake: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a021_TaskSchedulerError` | page 0 | Right electric parking brake: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a022_TaskInitError` | page 0 | Right electric parking brake: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a029_CoreDump` | page 0 | Right electric parking brake: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a030_ECULogUploadRequest` | page 0 | Right electric parking brake: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a031_UDSActive` | page 0 | Right electric parking brake: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a041_HighCPULoad` | page 0 | Right electric parking brake: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a042_HighStackUsage` | page 0 | Right electric parking brake: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a043_Task1msError` | page 0 | Right electric parking brake: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a044_Task10msError` | page 0 | Right electric parking brake: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a045_Task100msError` | page 0 | Right electric parking brake: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a046_Task1000msError` | page 0 | Right electric parking brake: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a057_HVP_MIA` | page 0 | Right electric parking brake: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a058_inputRHighSyncDebug` | page 0 | Right electric parking brake: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a059_inputResistanceHigh` | page 0 | Right electric parking brake: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a060_engineeringBuild` | page 0 | Right electric parking brake: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a061_XCPConnected` | page 1 | Right electric parking brake: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a062_XCPWasConnected` | page 1 | Right electric parking brake: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a063_SwitchFault` | page 1 | Right electric parking brake: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a064_busSleepReqTimeout` | page 1 | Right electric parking brake: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a081_APP_MIA` | page 1 | Right electric parking brake: a081 APP MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a082_VCRIGHT_IPC_MIA` | page 1 | Right electric parking brake: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a083_VCLEFT_IPC_MIA` | page 1 | Right electric parking brake: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a084_TPMS_MIA` | page 1 | Right electric parking brake: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a085_CCCM_MIA` | page 1 | Right electric parking brake: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a086_VCBATT_MIA` | page 1 | Right electric parking brake: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a087_DIREL_MIA` | page 1 | Right electric parking brake: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a088_DIRER_MIA` | page 1 | Right electric parking brake: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a089_IBST_MIA` | page 1 | Right electric parking brake: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a090_APS_MIA` | page 1 | Right electric parking brake: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a091_CMPD_MIA` | page 1 | Right electric parking brake: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a092_VCSEATD_MIA` | page 1 | Right electric parking brake: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a093_VCSEATP_MIA` | page 1 | Right electric parking brake: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a094_EPAS3P_MIA` | page 1 | Right electric parking brake: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a095_CHG_MIA` | page 1 | Right electric parking brake: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a096_OCS1P_MIA` | page 1 | Right electric parking brake: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a097_CMP_MIA` | page 1 | Right electric parking brake: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a098_DIR_MIA` | page 1 | Right electric parking brake: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a099_PARK_MIA` | page 1 | Right electric parking brake: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a100_CANbus_MIA` | page 1 | Right electric parking brake: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a101_PM_MIA` | page 1 | Right electric parking brake: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a102_PTC_MIA` | page 1 | Right electric parking brake: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a103_CP_MIA` | page 1 | Right electric parking brake: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a104_DAS_MIA` | page 1 | Right electric parking brake: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a105_TAS_MIA` | page 1 | Right electric parking brake: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a106_PCS_MIA` | page 1 | Right electric parking brake: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a107_BMS_MIA` | page 1 | Right electric parking brake: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a108_DIF_MIA` | page 1 | Right electric parking brake: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a109_RCM_MIA` | page 1 | Right electric parking brake: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a110_GTW_MIA` | page 1 | Right electric parking brake: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a111_EPBR_MIA` | page 1 | Right electric parking brake: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a112_EPBL_MIA` | page 1 | Right electric parking brake: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a113_UI_MIA` | page 1 | Right electric parking brake: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a114_ESP_MIA` | page 1 | Right electric parking brake: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a115_VCSEC_MIA` | page 1 | Right electric parking brake: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a116_VCRIGHT_MIA` | page 1 | Right electric parking brake: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a117_VCLEFT_MIA` | page 1 | Right electric parking brake: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a118_VCFRONT_MIA` | page 1 | Right electric parking brake: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a119_SCCM_MIA` | page 1 | Right electric parking brake: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a120_DI_DRIVE_MIA` | page 1 | Right electric parking brake: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a121_nDriveFault` | page 2 | Right electric parking brake: a121 n drive fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a122_Oc` | page 2 | Right electric parking brake: a122 oc | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a123_Uc` | page 2 | Right electric parking brake: a123 uc | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a124_calOutOfBounds` | page 2 | Right electric parking brake: a124 cal out of bounds | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a125_IdleVMismatch` | page 2 | Right electric parking brake: a125 idle v mismatch | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a126_MotorNVoltLow` | page 2 | Right electric parking brake: a126 motor n volt low | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a127_MotorNVoltHigh` | page 2 | Right electric parking brake: a127 motor n volt high | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a128_MotorPVoltHigh` | page 2 | Right electric parking brake: a128 motor p volt high | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a129_ICR_MIA` | page 2 | Right electric parking brake: a129 ICR MIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a130_BB_MIA` | page 2 | Right electric parking brake: a130 BB MIA | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a131_RCU_MIA` | page 2 | Right electric parking brake: a131 RCU MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a132_VCBATT1_MIA` | page 2 | Right electric parking brake: a132 VCBATT1 MIA | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a134_NvOv` | page 2 | Right electric parking brake: a134 nv ov | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a135_NvUv` | page 2 | Right electric parking brake: a135 nv uv | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a136_PvOv` | page 2 | Right electric parking brake: a136 pv ov | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a137_PvUv` | page 2 | Right electric parking brake: a137 pv uv | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a138_NvmDualFailure` | page 2 | Right electric parking brake: a138 nvm dual failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a139_NvmRedundancyLoss` | page 2 | Right electric parking brake: a139 nvm redundancy loss | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a140_NvmSlowWrite` | page 2 | Right electric parking brake: a140 nvm slow write | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a141_invalidState` | page 2 | Right electric parking brake: a141 invalid state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a170_12vOv` | page 2 | Right electric parking brake: a170 12v ov | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a171_12vUv` | page 2 | Right electric parking brake: a171 12v uv | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a172_SPI_MIA` | page 2 | Right electric parking brake: a172 SPI MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a173_hiCurrentMissing` | page 2 | Right electric parking brake: a173 hi current missing | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a174_csmReleaseFailed` | page 2 | Right electric parking brake: a174 csm release failed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a175_csmReleaseRetry` | page 2 | Right electric parking brake: a175 csm release retry | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a176_csmApplyFailed` | page 2 | Right electric parking brake: a176 csm apply failed | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a177_csmApplyRetry` | page 2 | Right electric parking brake: a177 csm apply retry | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a178_caliperStateUnknown` | page 2 | Right electric parking brake: a178 caliper state unknown | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a179_epbProblem` | page 2 | Right electric parking brake: a179 epb problem | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a180_dynamicActive` | page 2 | Right electric parking brake: a180 dynamic active | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a181_TooSteepGradeToPark` | page 3 | Right electric parking brake: a181 too steep grade to park | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a182_OneEPBAppliedUnsecEnv` | page 3 | Right electric parking brake: a182 one EPB applied unsec env | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a183_cdpNotAvailable` | page 3 | Right electric parking brake: a183 cdp not available | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a184_dynamicParkAbort` | page 3 | Right electric parking brake: a184 dynamic park abort | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a185_summonAborted` | page 3 | Right electric parking brake: a185 summon aborted | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a186_externalParkAbort` | page 3 | Right electric parking brake: a186 external park abort | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a187_cdpDynamic` | page 3 | Right electric parking brake: a187 cdp dynamic | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a188_epbDynamic` | page 3 | Right electric parking brake: a188 epb dynamic | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a189_epbDynamicParkCanceled` | page 3 | Right electric parking brake: a189 epb dynamic park canceled | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a190_csmApplyDegraded` | page 3 | Right electric parking brake: a190 csm apply degraded | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a191_csmReleaseDegraded` | page 3 | Right electric parking brake: a191 csm release degraded | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a195_parkForDriverIsLeaving` | page 3 | Right electric parking brake: a195 park for driver is leaving | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a196_freeRollModeActive` | page 3 | Right electric parking brake: a196 free roll mode active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a197_freeRollModeAtSpeed` | page 3 | Right electric parking brake: a197 free roll mode at speed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a198_holdClampComplete` | page 3 | Right electric parking brake: a198 hold clamp complete | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a200_PmUnparkNotAllowed` | page 3 | Right electric parking brake: a200 pm unpark not allowed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a202_remoteEpbConfigIncompatible` | page 3 | Right electric parking brake: a202 remote epb config incompatible | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a203_hwBrakeTypeMismatch` | page 3 | Right electric parking brake: a203 hw brake type mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a210_parkForDriverIsLeavingDebug` | page 3 | Right electric parking brake: a210 park for driver is leaving debug | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a216_SPI_MIA_debugData1` | page 3 | Right electric parking brake: a216 SPI MIA debug data1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a217_SPI_MIA_debugData2` | page 3 | Right electric parking brake: a217 SPI MIA debug data2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a225_epbActiveDecel` | page 3 | Right electric parking brake: a225 epb active decel | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a241_diOutputLocked` | page 4 | Right electric parking brake: a241 di output locked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a242_hvOutputLocked` | page 4 | Right electric parking brake: a242 hv output locked | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a243_bdwUnavailable` | page 4 | Right electric parking brake: a243 bdw unavailable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a244_WinchModeActive` | page 4 | Right electric parking brake: a244 winch mode active | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a245_serviceModeActive` | page 4 | Signal reported by Right electric parking brake | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a246_idleFaultApply` | page 4 | Right electric parking brake: a246 idle fault apply | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a247_csmDynamicApplyRetry` | page 4 | Right electric parking brake: a247 csm dynamic apply retry | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a248_csmDynamicApplyFailed` | page 4 | Right electric parking brake: a248 csm dynamic apply failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a249_idleFaultRelease` | page 4 | Right electric parking brake: a249 idle fault release | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a250_WinchModeCanceled` | page 4 | Right electric parking brake: a250 winch mode canceled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a251_currentVarianceHigh` | page 4 | Right electric parking brake: a251 current variance high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a252_winchModePending` | page 4 | Right electric parking brake: a252 winch mode pending | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a253_esmReleaseBlocked` | page 4 | Right electric parking brake: a253 esm release blocked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a254_showStalkParkButtonFaultOnUi` | page 4 | Right electric parking brake: a254 show stalk park button fault on ui | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a256_epbSystemApply` | page 4 | Right electric parking brake: a256 epb system apply | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a261_winchModeWithoutSteering` | page 4 | Right electric parking brake: a261 winch mode without steering | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a262_cannotPrepareWinchMode` | page 4 | Right electric parking brake: a262 cannot prepare winch mode | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a263_epbRecoveryPark` | page 4 | Right electric parking brake: a263 epb recovery park | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a264_winchModeDeactivated` | page 4 | Right electric parking brake: a264 winch mode deactivated | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a272_vhclPwrStateMsmtch` | page 4 | Right electric parking brake: a272 vhcl pwr state msmtch | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a300_leftRightConfusion` | page 4 | Right electric parking brake: a300 left right confusion | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a301_oocSpeedViolation` | page 5 | Right electric parking brake: a301 ooc speed violation | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a302_csmLongRelease` | page 5 | Right electric parking brake: a302 csm long release | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a303_clampingOccuredEarly` | page 5 | Right electric parking brake: a303 clamping occured early | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a304_rearSeatControllerEFuseTrip` | page 5 | Right electric parking brake: a304 rear seat controller e fuse trip | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a305_premiumAmpEFuseTrip` | page 5 | Right electric parking brake: a305 premium amp e fuse trip | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a350_ensOutOfRange` | page 5 | Right electric parking brake: a350 ens out of range | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a352_audioCurrentSpikeData` | page 5 | Right electric parking brake: a352 audio current spike data | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a353_missingSpeedUnableToPark` | page 5 | Right electric parking brake: a353 missing speed unable to park | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a354_parkedForLowBrakeFluidMode` | page 5 | Right electric parking brake: a354 parked for low brake fluid mode | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a355_brakeHwAndEpbHwMismatch` | page 5 | Right electric parking brake: a355 brake hw and epb hw mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a356_parkingForStationaryDetect` | page 5 | Right electric parking brake: a356 parking for stationary detect | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a357_brakesTooHotForSlope` | page 5 | Right electric parking brake: a357 brakes too hot for slope | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a358_brakesTooHotForSlopeWithOnlyOneEpb` | page 5 | Right electric parking brake: a358 brakes too hot for slope with only one epb | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a360_ibstBrakeSwitchInvalid` | page 5 | Right electric parking brake: a360 ibst brake switch invalid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a361_espBrakeSwitchInvalid` | page 6 | Right electric parking brake: a361 esp brake switch invalid | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a362_ibstPressedEspNotPressedMismatch` | page 6 | Right electric parking brake: a362 ibst pressed esp not pressed mismatch | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a363_ibstNotPressedEspPressedMismatch` | page 6 | Right electric parking brake: a363 ibst not pressed esp pressed mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a364_espMasterCylCompOverThreshold` | page 6 | Right electric parking brake: a364 esp master cyl comp over threshold | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a365_TooSteepToParkWithTrailerWarning` | page 6 | Right electric parking brake: a365 too steep to park with trailer warning | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `EPBR_a366_TooSteepToParkWithTrailerUnSecEnv` | page 6 | Right electric parking brake: a366 too steep to park with trailer un sec env | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`EPBR_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (24 signals), page 1 (44 signals), page 2 (31 signals), page 3 (22 signals), page 4 (21 signals), page 5 (14 signals), page 6 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right electric parking brake messages (EPBR)](../../epbr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
