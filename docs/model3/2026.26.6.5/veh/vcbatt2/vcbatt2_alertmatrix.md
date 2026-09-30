---
layout: default
title: "VCBATT2_alertMatrix (0x3CF) — VCBATT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "VCBATT2 ECU message: alert matrix. Tesla Model 3 CAN bus message VCBATT2_alertMatrix (0x3CF) of VCBATT2 ECU, firmware 2026.26.6.5, 149 signals (VCBATT2_matrixIndex, VCBATT2_a001_WatchdogReset, VCBATT2_a002_PowerLossReset, VCBATT2_a003_SWAssertion and 145 more). Bit layout, scaling, units and value tables."
---

# VCBATT2_alertMatrix (0x3CF) — VCBATT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN

VCBATT2 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 149 signals of VCBATT2_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT2_alertMatrix` |
| CAN id | 0x3CF (975) |
| ECU | [VCBATT2 ECU](../../vcbatt2.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT2 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 149 |

## Signals of VCBATT2_alertMatrix

Tesla Model 3 CAN bus signals in `VCBATT2_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT2_matrixIndex` | selector | VCBATT2 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10`<br>11 = `AlertMatrix11` | plausible |
| `VCBATT2_a001_WatchdogReset` | page 0 | VCBATT2 ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a002_PowerLossReset` | page 0 | VCBATT2 ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a003_SWAssertion` | page 0 | VCBATT2 ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a005_CANTXError` | page 0 | VCBATT2 ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a006_CANTX_cyclicError` | page 0 | VCBATT2 ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a012_CPUReset` | page 0 | VCBATT2 ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a013_AlertManagerFault` | page 0 | VCBATT2 ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a015_NVMMError` | page 0 | VCBATT2 ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a016_NVMMRecordError` | page 0 | VCBATT2 ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a017_NVMMStatusDbg` | page 0 | VCBATT2 ECU: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a018_HardFault` | page 0 | VCBATT2 ECU: a018 hard fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a019_BusFault` | page 0 | VCBATT2 ECU: a019 bus fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a021_TaskSchedulerError` | page 0 | VCBATT2 ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a022_TaskInitError` | page 0 | VCBATT2 ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a028_UsageFault` | page 0 | VCBATT2 ECU: a028 usage fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a029_CoreDump` | page 0 | VCBATT2 ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a030_ECULogUploadRequest` | page 0 | VCBATT2 ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a031_UDSActive` | page 0 | VCBATT2 ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a036_UnknownIrq` | page 0 | VCBATT2 ECU: a036 unknown irq | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a037_MemManageFault` | page 0 | VCBATT2 ECU: a037 mem manage fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a038_ProtFaultInfo` | page 0 | VCBATT2 ECU: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a039_ProtFaultAddress` | page 0 | VCBATT2 ECU: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a040_Backtrace` | page 0 | VCBATT2 ECU: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a041_HighCPULoad` | page 0 | VCBATT2 ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a042_HighStackUsage` | page 0 | VCBATT2 ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a043_Task1msError` | page 0 | VCBATT2 ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a044_Task10msError` | page 0 | VCBATT2 ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a045_Task100msError` | page 0 | VCBATT2 ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a046_Task1000msError` | page 0 | VCBATT2 ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a058_inputRHighSyncDebug` | page 0 | VCBATT2 ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a059_inputResistanceHigh` | page 0 | VCBATT2 ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a060_engineeringBuild` | page 0 | VCBATT2 ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a061_XCPConnected` | page 1 | VCBATT2 ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a062_XCPWasConnected` | page 1 | VCBATT2 ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a063_SwitchFault` | page 1 | VCBATT2 ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a064_busSleepReqTimeout` | page 1 | VCBATT2 ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a077_VCBATT0_MIA` | page 1 | VCBATT2 ECU: a077 VCBATT0 MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a078_VCBATT1_MIA` | page 1 | VCBATT2 ECU: a078 VCBATT1 MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a079_VCBATT2_MIA` | page 1 | VCBATT2 ECU: a079 VCBATT2 MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a080_VCFRONT0_MIA` | page 1 | VCBATT2 ECU: a080 VCFRONT0 MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a081_VCFRONT1_MIA` | page 1 | VCBATT2 ECU: a081 VCFRONT1 MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a082_VCFRONT2_MIA` | page 1 | VCBATT2 ECU: a082 VCFRONT2 MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a086_VCBATT_MIA` | page 1 | VCBATT2 ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a090_APS_MIA` | page 1 | VCBATT2 ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a091_CMPD_MIA` | page 1 | VCBATT2 ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a096_OCS1P_MIA` | page 1 | VCBATT2 ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a098_DIR_MIA` | page 1 | VCBATT2 ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a100_CANbus_MIA` | page 1 | VCBATT2 ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a103_CP_MIA` | page 1 | VCBATT2 ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a104_DAS_MIA` | page 1 | VCBATT2 ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a105_TAS_MIA` | page 1 | VCBATT2 ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a106_PCS_MIA` | page 1 | VCBATT2 ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a107_BMS_MIA` | page 1 | VCBATT2 ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a108_DIF_MIA` | page 1 | VCBATT2 ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a109_RCM_MIA` | page 1 | VCBATT2 ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a110_GTW_MIA` | page 1 | VCBATT2 ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a111_EPBR_MIA` | page 1 | VCBATT2 ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a112_EPBL_MIA` | page 1 | VCBATT2 ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a113_UI_MIA` | page 1 | VCBATT2 ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a114_ESP_MIA` | page 1 | VCBATT2 ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a115_VCSEC_MIA` | page 1 | VCBATT2 ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a116_VCRIGHT_MIA` | page 1 | VCBATT2 ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a117_VCLEFT_MIA` | page 1 | VCBATT2 ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a118_VCFRONT_MIA` | page 1 | VCBATT2 ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a119_SCCM_MIA` | page 1 | VCBATT2 ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a120_DI_DRIVE_MIA` | page 1 | VCBATT2 ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a122_ICR_MIA` | page 2 | VCBATT2 ECU: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a123_VC_SECONDARY_LIGHTING_LEADER_MIA` | page 2 | VCBATT2 ECU: a123 VC SECONDARY LIGHTING LEADER MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a124_BB_MIA` | page 2 | VCBATT2 ECU: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a125_SCCM_MIA` | page 2 | VCBATT2 ECU: a125 SCCM MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a126_EPAS3P_MIA` | page 2 | VCBATT2 ECU: a126 EPAS3 p MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a131_PCSCOMMON_MIA` | page 2 | VCBATT2 ECU: a131 PCSCOMMON MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a133_BRAKE_MIA` | page 2 | VCBATT2 ECU: a133 BRAKE MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a143_powerLossDuringSleep` | page 2 | VCBATT2 ECU: a143 power loss during sleep | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a144_EPAS3S_MIA` | page 2 | VCBATT2 ECU: a144 EPAS3 s MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a156_louverBlockage` | page 2 | VCBATT2 ECU: a156 louver blockage | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a157_louverBreakage` | page 2 | VCBATT2 ECU: a157 louver breakage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a158_louverDisconnected` | page 2 | VCBATT2 ECU: a158 louver disconnected | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a166_rightHCMMIA` | page 2 | VCBATT2 ECU: a166 right HCMMIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a181_homelinkMIA` | page 3 | VCBATT2 ECU: a181 homelink MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a185_washerFluidLow` | page 3 | VCBATT2 ECU: a185 washer fluid low | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a186_washerFluidLowFasciaAndRepeater` | page 3 | VCBATT2 ECU: a186 washer fluid low fascia and repeater | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a187_washerFluidLowPassengerWiper` | page 3 | VCBATT2 ECU: a187 washer fluid low passenger wiper | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a188_sleepFailed` | page 3 | VCBATT2 ECU: a188 sleep failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a192_vehicleLoadShed` | page 3 | VCBATT2 ECU: a192 vehicle load shed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a208_brakeFluidLow` | page 3 | VCBATT2 ECU: a208 brake fluid low | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a209_brakeFluidSNA` | page 3 | VCBATT2 ECU: a209 brake fluid SNA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a211_I2CFault` | page 3 | VCBATT2 ECU: a211 I2 c fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a227_radFanCompromised` | page 3 | VCBATT2 ECU: a227 rad fan compromised | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a241_radFanMIA` | page 4 | VCBATT2 ECU: a241 rad fan MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a290_leftFogLightFault` | page 4 | VCBATT2 ECU: a290 left fog light fault | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a291_rightFogLightFault` | page 4 | VCBATT2 ECU: a291 right fog light fault | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a292_sideMarkerLightPipeFault` | page 4 | VCBATT2 ECU: a292 side marker light pipe fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a295_rightSideRepeaterLightFault` | page 4 | VCBATT2 ECU: a295 right side repeater light fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a299_homelinkConfigurationFailed` | page 4 | VCBATT2 ECU: a299 homelink configuration failed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a300_louverActuatorSwapDetected` | page 4 | VCBATT2 ECU: a300 louver actuator swap detected | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a303_frunkAccessPostActive` | page 5 | VCBATT2 ECU: a303 frunk access post active | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a304_frunkReleaseFailed` | page 5 | VCBATT2 ECU: a304 frunk release failed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a305_frunkPriOverCurrent` | page 5 | VCBATT2 ECU: a305 frunk pri over current | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a306_frunkPriUnderCurrent` | page 5 | VCBATT2 ECU: a306 frunk pri under current | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a309_frunkEmergencyReleasePressed` | page 5 | VCBATT2 ECU: a309 frunk emergency release pressed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a353_wiperHeaterUndercurrent` | page 5 | VCBATT2 ECU: a353 wiper heater undercurrent | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a354_windshieldCameraHeaterUndercurrent` | page 5 | VCBATT2 ECU: a354 windshield camera heater undercurrent | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a361_washerFluidLowMomentary` | page 6 | VCBATT2 ECU: a361 washer fluid low momentary | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a364_heaterTypeEstimationChanged` | page 6 | VCBATT2 ECU: a364 heater type estimation changed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a389_frunkInhibitingReleaseAtSpeed` | page 6 | VCBATT2 ECU: a389 frunk inhibiting release at speed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a391_frunkLatchSwitchFault` | page 6 | VCBATT2 ECU: a391 frunk latch switch fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a399_frunkNeverReportedOpen` | page 6 | VCBATT2 ECU: a399 frunk never reported open | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a423_rtosSleepFailed` | page 7 | VCBATT2 ECU: a423 rtos sleep failed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a463_frunkSensorService` | page 7 | VCBATT2 ECU: a463 frunk sensor service | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a471_emergencyFrunkButtonPressIgnored` | page 7 | VCBATT2 ECU: a471 emergency frunk button press ignored | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a475_rightHeadlampInternalError` | page 7 | VCBATT2 ECU: a475 right headlamp internal error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a485_mcuGamingEFuseFault` | page 8 | VCBATT2 ECU: a485 mcu gaming e fuse fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a486_sleepPowerDebug` | page 8 | VCBATT2 ECU: a486 sleep power debug | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a516_hibernationActive` | page 8 | VCBATT2 ECU: a516 hibernation active | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a517_hibernationRecovery` | page 8 | VCBATT2 ECU: a517 hibernation recovery | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a520_rightHeadlampInternalErrorV2` | page 8 | VCBATT2 ECU: a520 right headlamp internal error V2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a522_hibernationActiveLogCapture` | page 8 | VCBATT2 ECU: a522 hibernation active log capture | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a524_rightHeadlampAimingFault` | page 8 | VCBATT2 ECU: a524 right headlamp aiming fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a547_postCrashLoadShed` | page 9 | VCBATT2 ECU: a547 post crash load shed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a548_HVFaultLoadShed` | page 9 | VCBATT2 ECU: a548 HV fault load shed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a557_rightHeadlampInternalErrorV3` | page 9 | VCBATT2 ECU: a557 right headlamp internal error V3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a558_rightHeadlampAimingDebug` | page 9 | VCBATT2 ECU: a558 right headlamp aiming debug | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a567_rightFrontTurnLightFault` | page 9 | VCBATT2 ECU: a567 right front turn light fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a569_rightDaytimeRunningLightFault` | page 9 | VCBATT2 ECU: a569 right daytime running light fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a575_frontOilPumpEFuseTrip` | page 9 | VCBATT2 ECU: a575 front oil pump e fuse trip | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a578_vbattFusedLowCurrentFeedEFuseTrip` | page 9 | VCBATT2 ECU: a578 vbatt fused low current feed e fuse trip | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a583_frunkSwitchGroupDisagreementDebug` | page 9 | VCBATT2 ECU: a583 frunk switch group disagreement debug | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a584_frunkSwitchGroupDebug` | page 9 | VCBATT2 ECU: a584 frunk switch group debug | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a586_rightLowOrHighBeamLightCondition` | page 9 | VCBATT2 ECU: a586 right low or high beam light condition | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a610_frunkOpenFailureMetricSet` | page 10 | VCBATT2 ECU: a610 frunk open failure metric set | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a617_APP_MIA` | page 10 | VCBATT2 ECU: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a619_frunkSwitchReleaseTimeDBG` | page 10 | VCBATT2 ECU: a619 frunk switch release time DBG | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a624_rightHeadlampInternalErrorV4` | page 10 | VCBATT2 ECU: a624 right headlamp internal error V4 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a631_rightHeadlampFactoryFault` | page 10 | VCBATT2 ECU: a631 right headlamp factory fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a634_indeterminateSwitchTransitionDetectedDbg` | page 10 | VCBATT2 ECU: a634 indeterminate switch transition detected dbg | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a643_rightHeadlampUartCondition` | page 10 | VCBATT2 ECU: a643 right headlamp uart condition | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a644_washPumpHealthCalculationDbg0` | page 10 | VCBATT2 ECU: a644 wash pump health calculation dbg0 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a645_washPumpHealthCalculationDbg1` | page 10 | VCBATT2 ECU: a645 wash pump health calculation dbg1 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a646_washPumpHealthCalculationDbg2` | page 10 | VCBATT2 ECU: a646 wash pump health calculation dbg2 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a649_persistAccPortPowerReqOverridden` | page 10 | VCBATT2 ECU: a649 persist acc port power req overridden | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a650_powerConsumptionInfo` | page 10 | VCBATT2 ECU: a650 power consumption info | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a662_mculessRightHeadlampCurrentAlertDbg` | page 11 | VCBATT2 ECU: a662 mculess right headlamp current alert dbg | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a664_rightHeadlampUartWaterMarkWarning` | page 11 | VCBATT2 ECU: a664 right headlamp uart water mark warning | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a666_rightHeadlampRetryInfo` | page 11 | VCBATT2 ECU: a666 right headlamp retry info | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a668_rightHeadlampRegionOrSideMismatch` | page 11 | VCBATT2 ECU: a668 right headlamp region or side mismatch | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a698_rightHeadlampNotAimed` | page 11 | VCBATT2 ECU: a698 right headlamp not aimed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT2_a702_dynamicHeadlightLevelingUnavailable` | page 11 | VCBATT2 ECU: a702 dynamic headlight leveling unavailable | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCBATT2_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (32 signals), page 1 (34 signals), page 2 (13 signals), page 3 (10 signals), page 4 (7 signals), page 5 (7 signals), page 6 (5 signals), page 7 (4 signals), page 8 (7 signals), page 9 (11 signals), page 10 (12 signals), page 11 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All VCBATT2 ECU messages (VCBATT2)](../../vcbatt2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
