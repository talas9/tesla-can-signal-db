---
layout: default
title: "VCBATT1_alertMatrix (0x3CE) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: alert matrix. Tesla Model Y CAN bus message VCBATT1_alertMatrix (0x3CE) of VCBATT1 ECU, firmware 2026.26.6.5, 255 signals (VCBATT1_matrixIndex, VCBATT1_a001_WatchdogReset, VCBATT1_a002_PowerLossReset, VCBATT1_a003_SWAssertion and 251 more). Bit layout, scaling, units and value tables."
---

# VCBATT1_alertMatrix (0x3CE) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 255 signals of VCBATT1_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_alertMatrix` |
| CAN id | 0x3CE (974) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 255 |

## Signals of VCBATT1_alertMatrix

Tesla Model Y CAN bus signals in `VCBATT1_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_matrixIndex` | selector | VCBATT1 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10`<br>11 = `AlertMatrix11` | plausible |
| `VCBATT1_a001_WatchdogReset` | page 0 | VCBATT1 ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a002_PowerLossReset` | page 0 | VCBATT1 ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a003_SWAssertion` | page 0 | VCBATT1 ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a005_CANTXError` | page 0 | VCBATT1 ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a006_CANTX_cyclicError` | page 0 | VCBATT1 ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a012_CPUReset` | page 0 | VCBATT1 ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a013_AlertManagerFault` | page 0 | VCBATT1 ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a015_NVMMError` | page 0 | VCBATT1 ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a016_NVMMRecordError` | page 0 | VCBATT1 ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a017_NVMMStatusDbg` | page 0 | VCBATT1 ECU: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a018_HardFault` | page 0 | VCBATT1 ECU: a018 hard fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a019_BusFault` | page 0 | VCBATT1 ECU: a019 bus fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a021_TaskSchedulerError` | page 0 | VCBATT1 ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a022_TaskInitError` | page 0 | VCBATT1 ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a028_UsageFault` | page 0 | VCBATT1 ECU: a028 usage fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a029_CoreDump` | page 0 | VCBATT1 ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a030_ECULogUploadRequest` | page 0 | VCBATT1 ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a031_UDSActive` | page 0 | VCBATT1 ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a036_UnknownIrq` | page 0 | VCBATT1 ECU: a036 unknown irq | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a037_MemManageFault` | page 0 | VCBATT1 ECU: a037 mem manage fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a038_ProtFaultInfo` | page 0 | VCBATT1 ECU: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a039_ProtFaultAddress` | page 0 | VCBATT1 ECU: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a040_Backtrace` | page 0 | VCBATT1 ECU: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a041_HighCPULoad` | page 0 | VCBATT1 ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a042_HighStackUsage` | page 0 | VCBATT1 ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a043_Task1msError` | page 0 | VCBATT1 ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a044_Task10msError` | page 0 | VCBATT1 ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a045_Task100msError` | page 0 | VCBATT1 ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a046_Task1000msError` | page 0 | VCBATT1 ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a058_inputRHighSyncDebug` | page 0 | VCBATT1 ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a059_inputResistanceHigh` | page 0 | VCBATT1 ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a060_engineeringBuild` | page 0 | VCBATT1 ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a061_XCPConnected` | page 1 | VCBATT1 ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a062_XCPWasConnected` | page 1 | VCBATT1 ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a063_SwitchFault` | page 1 | VCBATT1 ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a064_busSleepReqTimeout` | page 1 | VCBATT1 ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a077_VCBATT0_MIA` | page 1 | VCBATT1 ECU: a077 VCBATT0 MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a078_VCBATT1_MIA` | page 1 | VCBATT1 ECU: a078 VCBATT1 MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a079_VCBATT2_MIA` | page 1 | VCBATT1 ECU: a079 VCBATT2 MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a080_VCFRONT0_MIA` | page 1 | VCBATT1 ECU: a080 VCFRONT0 MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a081_VCFRONT1_MIA` | page 1 | VCBATT1 ECU: a081 VCFRONT1 MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a082_VCFRONT2_MIA` | page 1 | VCBATT1 ECU: a082 VCFRONT2 MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a086_VCBATT_MIA` | page 1 | VCBATT1 ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a090_APS_MIA` | page 1 | VCBATT1 ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a091_CMPD_MIA` | page 1 | VCBATT1 ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a096_OCS1P_MIA` | page 1 | VCBATT1 ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a098_DIR_MIA` | page 1 | VCBATT1 ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a100_CANbus_MIA` | page 1 | VCBATT1 ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a103_CP_MIA` | page 1 | VCBATT1 ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a104_DAS_MIA` | page 1 | VCBATT1 ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a105_TAS_MIA` | page 1 | VCBATT1 ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a106_PCS_MIA` | page 1 | VCBATT1 ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a107_BMS_MIA` | page 1 | VCBATT1 ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a108_DIF_MIA` | page 1 | VCBATT1 ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a109_RCM_MIA` | page 1 | VCBATT1 ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a110_GTW_MIA` | page 1 | VCBATT1 ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a111_EPBR_MIA` | page 1 | VCBATT1 ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a112_EPBL_MIA` | page 1 | VCBATT1 ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a113_UI_MIA` | page 1 | VCBATT1 ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a114_ESP_MIA` | page 1 | VCBATT1 ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a115_VCSEC_MIA` | page 1 | VCBATT1 ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a116_VCRIGHT_MIA` | page 1 | VCBATT1 ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a117_VCLEFT_MIA` | page 1 | VCBATT1 ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a118_VCFRONT_MIA` | page 1 | VCBATT1 ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a119_SCCM_MIA` | page 1 | VCBATT1 ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a120_DI_DRIVE_MIA` | page 1 | VCBATT1 ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a122_ICR_MIA` | page 2 | VCBATT1 ECU: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a124_BB_MIA` | page 2 | VCBATT1 ECU: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a125_SCCM_MIA` | page 2 | VCBATT1 ECU: a125 SCCM MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a126_EPAS3P_MIA` | page 2 | VCBATT1 ECU: a126 EPAS3 p MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a127_vcleftEFuseTrip` | page 2 | VCBATT1 ECU: a127 vcleft e fuse trip | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a129_epas1EFuseTrip` | page 2 | VCBATT1 ECU: a129 epas1 e fuse trip | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a130_autopilot1EFuseTrip` | page 2 | VCBATT1 ECU: a130 autopilot1 e fuse trip | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a131_PCSCOMMON_MIA` | page 2 | VCBATT1 ECU: a131 PCSCOMMON MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a132_iBoosterEFuseTrip` | page 2 | VCBATT1 ECU: a132 i booster e fuse trip | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a133_BRAKE_MIA` | page 2 | VCBATT1 ECU: a133 BRAKE MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a134_hvContactorsEFuseTrip` | page 2 | VCBATT1 ECU: a134 hv contactors e fuse trip | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a144_EPAS3S_MIA` | page 2 | VCBATT1 ECU: a144 EPAS3 s MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a164_eFuseLckoutMissing` | page 2 | VCBATT1 ECU: a164 e fuse lckout missing | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a165_unxpctdEFuseLckout` | page 2 | VCBATT1 ECU: a165 unxpctd e fuse lckout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a180_DCDCNotSupportingLVBus` | page 2 | VCBATT1 ECU: a180 DCDC not supporting LV bus | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a182_replaceLVBattery` | page 3 | VCBATT1 ECU: a182 replace LV battery | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a183_replaceLVBattery2` | page 3 | VCBATT1 ECU: a183 replace LV battery2 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a188_sleepFailed` | page 3 | VCBATT1 ECU: a188 sleep failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a189_IBSMIA` | page 3 | VCBATT1 ECU: a189 IBSMIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a191_exitDriveLowLVBusVoltage` | page 3 | VCBATT1 ECU: a191 exit drive low LV bus voltage | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a196_discnctdLVBattery` | page 3 | VCBATT1 ECU: a196 discnctd LV battery | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a204_undervoltageLoadshedTriggered` | page 3 | VCBATT1 ECU: a204 undervoltage loadshed triggered | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a205_overvoltageProtectionTriggered` | page 3 | VCBATT1 ECU: a205 overvoltage protection triggered | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a212_IBSOverTemp` | page 3 | VCBATT1 ECU: a212 IBS over temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a213_LVOvercharge` | page 3 | VCBATT1 ECU: a213 LV overcharge | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a215_selfTestOrchestratorDebug` | page 3 | VCBATT1 ECU: a215 self test orchestrator debug | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a216_powerCutoffImminent` | page 3 | VCBATT1 ECU: a216 power cutoff imminent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a217_LVProtectionSelfTestInvalid` | page 3 | VCBATT1 ECU: a217 LV protection self test invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a219_LVVoltFloorRchd` | page 3 | VCBATT1 ECU: a219 LV volt floor rchd | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a220_LVUnhealthy` | page 3 | VCBATT1 ECU: a220 LV unhealthy | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a221_reverseBatteryFault` | page 3 | VCBATT1 ECU: a221 reverse battery fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a223_bridgeOvervoltageSelfTestFailure` | page 3 | VCBATT1 ECU: a223 bridge overvoltage self test failure | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a224_overcurrentLoadshedTriggered` | page 3 | VCBATT1 ECU: a224 overcurrent loadshed triggered | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a225_overcurrentSelfTestFailure` | page 3 | VCBATT1 ECU: a225 overcurrent self test failure | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a226_overcurrentSelfTestChannelFastDBG` | page 3 | VCBATT1 ECU: a226 overcurrent self test channel fast DBG | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a227_overcurrentSelfTestChannelMediumDBG` | page 3 | VCBATT1 ECU: a227 overcurrent self test channel medium DBG | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a228_overcurrentSelfTestChannelSlowDBG` | page 3 | VCBATT1 ECU: a228 overcurrent self test channel slow DBG | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a229_LVHealthCompromised` | page 3 | VCBATT1 ECU: a229 LV health compromised | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a230_ingoingOvercurrentSelfTestFailure` | page 3 | VCBATT1 ECU: a230 ingoing overcurrent self test failure | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a231_autopilot1EFuseTripDuringOTA` | page 3 | VCBATT1 ECU: a231 autopilot1 e fuse trip during OTA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a235_dualPowerLoadsSelfTestFailure` | page 3 | VCBATT1 ECU: a235 dual power loads self test failure | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a236_hvcDualPowerSelfTestDebug` | page 3 | VCBATT1 ECU: a236 hvc dual power self test debug | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a243_LVOverchargeInstc` | page 4 | VCBATT1 ECU: a243 LV overcharge instc | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a244_brakeValveECUEFuseTrip` | page 4 | VCBATT1 ECU: a244 brake valve ECUE fuse trip | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a245_sleepBypassFault` | page 4 | VCBATT1 ECU: a245 sleep bypass fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a252_controllerWakeup` | page 4 | VCBATT1 ECU: a252 controller wakeup | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a253_maxChrgeSssionTmeout` | page 4 | VCBATT1 ECU: a253 max chrge sssion tmeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a256_nxppca9539Fault` | page 4 | VCBATT1 ECU: a256 nxppca9539 fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a258_resistanceEstimationRun` | page 4 | VCBATT1 ECU: a258 resistance estimation run | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a259_LVVoltageDropOnHighLoadCurrent` | page 4 | VCBATT1 ECU: a259 LV voltage drop on high load current | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a260_deadLVBattery` | page 4 | VCBATT1 ECU: a260 dead LV battery | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a275_TLVBMS_BmbCommunication` | page 4 | VCBATT1 ECU: a275 TLVBMS bmb communication | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a276_TLVBMS_BmbDataIntegrityLoss` | page 4 | VCBATT1 ECU: a276 TLVBMS bmb data integrity loss | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a277_TLVBMS_BmbStatusRegError` | page 4 | VCBATT1 ECU: a277 TLVBMS bmb status reg error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a278_TLVBMS_BmbHwOverCurrentFault` | page 4 | VCBATT1 ECU: a278 TLVBMS bmb hw over current fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a297_TLVBMS_BmbHwOverTemperatureFault` | page 4 | VCBATT1 ECU: a297 TLVBMS bmb hw over temperature fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a359_postPORExcessiveAh` | page 5 | VCBATT1 ECU: a359 post POR excessive ah | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a362_TLVBMS_AllSocCorrectionTimeout` | page 6 | VCBATT1 ECU: a362 TLVBMS all soc correction timeout | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a363_TLVBMS_BleedBasedWeakShort` | page 6 | VCBATT1 ECU: a363 TLVBMS bleed based weak short | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a370_noLVSupportSocTooLow` | page 6 | VCBATT1 ECU: a370 no LV support soc too low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a371_failureToPrechargeRisk` | page 6 | VCBATT1 ECU: a371 failure to precharge risk | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a372_TLVBMS_BmbHwOverVoltageFault` | page 6 | VCBATT1 ECU: a372 TLVBMS bmb hw over voltage fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a376_controllerWakeupDebug` | page 6 | VCBATT1 ECU: a376 controller wakeup debug | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a379_shortedCellTestRunDebug` | page 6 | VCBATT1 ECU: a379 shorted cell test run debug | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a387_shortedCellInstc` | page 6 | VCBATT1 ECU: a387 shorted cell instc | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a388_shortedCell` | page 6 | VCBATT1 ECU: a388 shorted cell | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a392_TLVBMS_BmbHwUnderVoltageFault` | page 6 | VCBATT1 ECU: a392 TLVBMS bmb hw under voltage fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a400_TLVBMS_BmbVrefBad` | page 6 | VCBATT1 ECU: a400 TLVBMS bmb vref bad | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a401_deadLVMinimalAhDischarged` | page 6 | VCBATT1 ECU: a401 dead LV minimal ah discharged | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a402_LVBatteryCannotSupportVehicle` | page 6 | VCBATT1 ECU: a402 LV battery cannot support vehicle | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a403_chargeExitHardCurrentLimit` | page 6 | VCBATT1 ECU: a403 charge exit hard current limit | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a404_resistanceEstimationHardFailure` | page 6 | VCBATT1 ECU: a404 resistance estimation hard failure | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a405_dcrData1` | page 6 | VCBATT1 ECU: a405 dcr data1 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a406_dcrData2` | page 6 | VCBATT1 ECU: a406 dcr data2 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a407_dcrMilliOhmsAboveThreshold` | page 6 | VCBATT1 ECU: a407 dcr milli ohms above threshold | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a408_standbyChargeProfileHardExit` | page 6 | VCBATT1 ECU: a408 standby charge profile hard exit | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a410_LVBatteryDataCollection1` | page 6 | VCBATT1 ECU: a410 LV battery data collection1 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a411_LVBatteryDataCollection2` | page 6 | VCBATT1 ECU: a411 LV battery data collection2 | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a412_dcrData3` | page 6 | VCBATT1 ECU: a412 dcr data3 | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a413_TLVBMS_BmbVrefWarning` | page 6 | VCBATT1 ECU: a413 TLVBMS bmb vref warning | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a414_undervoltageSelfTestFailure` | page 6 | VCBATT1 ECU: a414 undervoltage self test failure | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a415_undervoltageSelfTestStuckOff` | page 6 | VCBATT1 ECU: a415 undervoltage self test stuck off | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a416_TLVBMS_BrickOverDischarged` | page 6 | VCBATT1 ECU: a416 TLVBMS brick over discharged | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a417_TLVBMS_BrickOverVoltageFault` | page 6 | VCBATT1 ECU: a417 TLVBMS brick over voltage fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a418_TLVBMS_BrickOverVoltageWarning` | page 6 | VCBATT1 ECU: a418 TLVBMS brick over voltage warning | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a419_TLVBMS_BrickSocLow` | page 6 | VCBATT1 ECU: a419 TLVBMS brick soc low | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a421_LVBatteryHealthTestInterrupted` | page 7 | VCBATT1 ECU: a421 LV battery health test interrupted | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a422_rtosSleepFailed` | page 7 | VCBATT1 ECU: a422 rtos sleep failed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a423_TLVBMS_BrickUnderVoltageFault` | page 7 | VCBATT1 ECU: a423 TLVBMS brick under voltage fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a424_TLVBMS_BrickUnderVoltageOcv` | page 7 | VCBATT1 ECU: a424 TLVBMS brick under voltage ocv | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a425_TLVBMS_BusVoltageTooHigh` | page 7 | VCBATT1 ECU: a425 TLVBMS bus voltage too high | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a426_TLVBMS_BusVoltageTooLow` | page 7 | VCBATT1 ECU: a426 TLVBMS bus voltage too low | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a427_TLVBMS_CacChange` | page 7 | VCBATT1 ECU: a427 TLVBMS cac change | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a428_TLVBMS_CacImbalance` | page 7 | VCBATT1 ECU: a428 TLVBMS cac imbalance | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a429_TLVBMS_CapacityTestResults` | page 7 | VCBATT1 ECU: a429 TLVBMS capacity test results | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a430_TLVBMS_ChargeCurrentLimitExceeded` | page 7 | VCBATT1 ECU: a430 TLVBMS charge current limit exceeded | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a431_TLVBMS_ChargeOverCurrent` | page 7 | VCBATT1 ECU: a431 TLVBMS charge over current | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a432_TLVBMS_ChargeRegulationFault` | page 7 | VCBATT1 ECU: a432 TLVBMS charge regulation fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a433_TLVBMS_ConfigFromBmbModIdFailed` | page 7 | VCBATT1 ECU: a433 TLVBMS config from bmb mod id failed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a434_TLVBMS_ConfigInitFailed` | page 7 | VCBATT1 ECU: a434 TLVBMS config init failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a435_TLVBMS_DchgCurrentLimitExceeded` | page 7 | VCBATT1 ECU: a435 TLVBMS dchg current limit exceeded | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a436_TLVBMS_DischargeOverCurrent` | page 7 | VCBATT1 ECU: a436 TLVBMS discharge over current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a437_TLVBMS_NvmRegistrationError` | page 7 | VCBATT1 ECU: a437 TLVBMS nvm registration error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a438_TLVBMS_PackOverTemperatureFault` | page 7 | VCBATT1 ECU: a438 TLVBMS pack over temperature fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a439_TLVBMS_PackOverTemperatureWarning` | page 7 | VCBATT1 ECU: a439 TLVBMS pack over temperature warning | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a440_TLVBMS_PackSNInvalidForNvm` | page 7 | VCBATT1 ECU: a440 TLVBMS pack SN invalid for nvm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a441_TLVBMS_ResetNeededForNvmPackSwap` | page 7 | VCBATT1 ECU: a441 TLVBMS reset needed for nvm pack swap | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a442_TLVBMS_SocChange` | page 7 | VCBATT1 ECU: a442 TLVBMS soc change | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a443_TLVBMS_BmbDieOverTemperature` | page 7 | VCBATT1 ECU: a443 TLVBMS bmb die over temperature | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a446_LVBatteryUnrecoverableByAnyDevice` | page 7 | VCBATT1 ECU: a446 LV battery unrecoverable by any device | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a450_doorWakeToOpenDBG` | page 7 | VCBATT1 ECU: a450 door wake to open DBG | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a461_TLVBMS_SocHighAhError` | page 7 | VCBATT1 ECU: a461 TLVBMS soc high ah error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a462_LVBMSFault` | page 7 | VCBATT1 ECU: a462 LVBMS fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a475_vnf1248Fault` | page 7 | VCBATT1 ECU: a475 vnf1248 fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a476_LVBMSMIA` | page 7 | VCBATT1 ECU: a476 LVBMSMIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a477_LVBatteryUnrecoverableByVehicle` | page 7 | VCBATT1 ECU: a477 LV battery unrecoverable by vehicle | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a478_LVBMS_MOSFET_Open` | page 7 | VCBATT1 ECU: a478 LVBMS MOSFET open | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a479_LVBMS_ECPA_NotClosed` | page 7 | VCBATT1 ECU: a479 LVBMS ECPA not closed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a480_vnf1048Fault` | page 7 | VCBATT1 ECU: a480 vnf1048 fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a481_LVBridgeCloseDBG` | page 8 | VCBATT1 ECU: a481 LV bridge close DBG | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a482_lvBridgeEFuseTrip` | page 8 | VCBATT1 ECU: a482 lv bridge e fuse trip | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a483_vnf1048SelfTestFailure` | page 8 | VCBATT1 ECU: a483 vnf1048 self test failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a484_undervoltageSelfTestStuckOn` | page 8 | VCBATT1 ECU: a484 undervoltage self test stuck on | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a485_uvSelfTestLoadUnattemptedOnDbg` | page 8 | VCBATT1 ECU: a485 uv self test load unattempted on dbg | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a486_undervoltageSelfTestBridgeSyncFailure` | page 8 | VCBATT1 ECU: a486 undervoltage self test bridge sync failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a489_vnf1248SelfTestDebug` | page 8 | VCBATT1 ECU: a489 vnf1248 self test debug | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a490_vnf1248SelfTestFailure` | page 8 | VCBATT1 ECU: a490 vnf1248 self test failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a491_vnf1248ConfigurationMismatch` | page 8 | VCBATT1 ECU: a491 vnf1248 configuration mismatch | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a492_TLVBMS_SocImbalance` | page 8 | VCBATT1 ECU: a492 TLVBMS soc imbalance | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a493_TLVBMS_SocImbalanceWarning` | page 8 | VCBATT1 ECU: a493 TLVBMS soc imbalance warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a494_LVBatteryTempBlockingOTA` | page 8 | VCBATT1 ECU: a494 LV battery temp blocking OTA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a495_LVBatteryRecoveryBlocked` | page 8 | VCBATT1 ECU: a495 LV battery recovery blocked | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a496_LVBatteryExitDriveWarning` | page 8 | VCBATT1 ECU: a496 LV battery exit drive warning | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a497_LVBatteryWarnDisconnect` | page 8 | VCBATT1 ECU: a497 LV battery warn disconnect | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a498_TLVBMS_ImpedanceTestResults` | page 8 | VCBATT1 ECU: a498 TLVBMS impedance test results | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a500_eFuseASICStateMismatch` | page 8 | VCBATT1 ECU: a500 e fuse ASIC state mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a501_vnf1048ConfigurationMismatch` | page 8 | VCBATT1 ECU: a501 vnf1048 configuration mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a502_TLVBMS_WeakShortImpedance` | page 8 | VCBATT1 ECU: a502 TLVBMS weak short impedance | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a503_TLVBMS_BrickExtendedOvFault` | page 8 | VCBATT1 ECU: a503 TLVBMS brick extended ov fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a508_TLVBMS_ImpedanceGrowth` | page 8 | VCBATT1 ECU: a508 TLVBMS impedance growth | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a509_eFuseASICManagerStateMismatch` | page 8 | VCBATT1 ECU: a509 e fuse ASIC manager state mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a510_LVBatteryRecoveryTimeout` | page 8 | VCBATT1 ECU: a510 LV battery recovery timeout | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a512_LVBMSFault_MOS_Open_hardwareOC` | page 8 | VCBATT1 ECU: a512 LVBMS fault MOS open hardware OC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a513_LVBMSFault_MOS_Open_chgOC` | page 8 | VCBATT1 ECU: a513 LVBMS fault MOS open chg OC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a514_LVBMSFault_MOS_Open_cellUV` | page 8 | VCBATT1 ECU: a514 LVBMS fault MOS open cell UV | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a515_LVBMSFault_MOS_Open_cellOV` | page 8 | VCBATT1 ECU: a515 LVBMS fault MOS open cell OV | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a518_LVBMSFault_MOS_Open_packOV` | page 8 | VCBATT1 ECU: a518 LVBMS fault MOS open pack OV | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a521_vcleftEFuseLoadShed` | page 8 | VCBATT1 ECU: a521 vcleft e fuse load shed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a523_eFuseThresholdsIncorrect` | page 8 | VCBATT1 ECU: a523 e fuse thresholds incorrect | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a525_LVBatterySWMisconfiguration` | page 8 | VCBATT1 ECU: a525 LV battery SW misconfiguration | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a527_LVBatteryCellImbalance` | page 8 | VCBATT1 ECU: a527 LV battery cell imbalance | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a528_LVBatteryCommsDiscnctd` | page 8 | VCBATT1 ECU: a528 LV battery comms discnctd | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a529_discnctdBatteryStateUnknown` | page 8 | VCBATT1 ECU: a529 discnctd battery state unknown | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a533_TLVBMS_MosfetOverTemperatureFault` | page 8 | VCBATT1 ECU: a533 TLVBMS mosfet over temperature fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a541_LVBatteryChargeOCLevel1` | page 9 | VCBATT1 ECU: a541 LV battery charge OC level1 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a544_LVBatteryCommsBusTurnedOff` | page 9 | VCBATT1 ECU: a544 LV battery comms bus turned off | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a545_LVBatteryTypeUnknown` | page 9 | VCBATT1 ECU: a545 LV battery type unknown | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a548_HVFaultLoadShed` | page 9 | VCBATT1 ECU: a548 HV fault load shed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a555_LVBatteryCellRebalancing` | page 9 | VCBATT1 ECU: a555 LV battery cell rebalancing | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a556_falseTriggerOfDiscnctdBatteryTest` | page 9 | VCBATT1 ECU: a556 false trigger of discnctd battery test | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a559_LVBatteryLowSOC` | page 9 | VCBATT1 ECU: a559 LV battery low SOC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a561_LVBMSEFuseOvertemperature` | page 9 | VCBATT1 ECU: a561 LVBMSE fuse overtemperature | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a562_LVBMSModuleOvertemperature` | page 9 | VCBATT1 ECU: a562 LVBMS module overtemperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a573_radarEFuseTrip` | page 9 | VCBATT1 ECU: a573 radar e fuse trip | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a575_vbatFusedLoadShedEFuseTrip` | page 9 | VCBATT1 ECU: a575 vbat fused load shed e fuse trip | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a576_mcuLogicEFuseTrip` | page 9 | VCBATT1 ECU: a576 mcu logic e fuse trip | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a580_rightHeadlightEFuseTrip` | page 9 | VCBATT1 ECU: a580 right headlight e fuse trip | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a581_harnessResistanceInfo` | page 9 | VCBATT1 ECU: a581 harness resistance info | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a582_goodForPCSPowerCycle` | page 9 | VCBATT1 ECU: a582 good for PCS power cycle | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a585_lvBatteryHealthTestRequired` | page 9 | VCBATT1 ECU: a585 lv battery health test required | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a587_externalLVPowerSupply` | page 9 | VCBATT1 ECU: a587 external LV power supply | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a588_vcleftPwrRationalityCurve` | page 9 | VCBATT1 ECU: a588 vcleft pwr rationality curve | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a589_vcleftFastBlowDetection` | page 9 | VCBATT1 ECU: a589 vcleft fast blow detection | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a592_vcleftCurvePowerCutoff` | page 9 | VCBATT1 ECU: a592 vcleft curve power cutoff | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a593_vcleftFastBlowPowerCutoff` | page 9 | VCBATT1 ECU: a593 vcleft fast blow power cutoff | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a595_voltageSensorMismatch` | page 9 | VCBATT1 ECU: a595 voltage sensor mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a597_LVBMBeFuseSelfTestNotReady` | page 9 | VCBATT1 ECU: a597 LVBM be fuse self test not ready | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a598_LVBMBeFuseSelfTestFailed` | page 9 | VCBATT1 ECU: a598 LVBM be fuse self test failed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a599_LVBatteryTypeUnsupported` | page 9 | VCBATT1 ECU: a599 LV battery type unsupported | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a600_currentSensorMismatch` | page 9 | VCBATT1 ECU: a600 current sensor mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a601_LVBatteryHeaterNotPresent` | page 10 | VCBATT1 ECU: a601 LV battery heater not present | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a608_TLVBMS_BleedFetFailure` | page 10 | VCBATT1 ECU: a608 TLVBMS bleed fet failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a615_TLVBMS_BatteryHeaterFault` | page 10 | VCBATT1 ECU: a615 TLVBMS battery heater fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a617_APP_MIA` | page 10 | VCBATT1 ECU: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a628_TLVBMS_BmbThermistorFault` | page 10 | VCBATT1 ECU: a628 TLVBMS bmb thermistor fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a629_TLVBMS_PackTemperatureIrrational` | page 10 | VCBATT1 ECU: a629 TLVBMS pack temperature irrational | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a670_TLVBMS_EfuseStateIrrational` | page 11 | VCBATT1 ECU: a670 TLVBMS efuse state irrational | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT1_a672_LVBatteryVitals` | page 11 | VCBATT1 ECU: a672 LV battery vitals | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCBATT1_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (32 signals), page 1 (34 signals), page 2 (15 signals), page 3 (27 signals), page 4 (14 signals), page 5 (1 signals), page 6 (29 signals), page 7 (33 signals), page 8 (35 signals), page 9 (26 signals), page 10 (6 signals), page 11 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
