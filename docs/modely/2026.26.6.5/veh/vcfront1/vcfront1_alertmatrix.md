---
layout: default
title: "VCFRONT1_alertMatrix (0x341) — VCFRONT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCFRONT1 ECU message: alert matrix. Tesla Model Y CAN bus message VCFRONT1_alertMatrix (0x341) of VCFRONT1 ECU, firmware 2026.26.6.5, 132 signals (VCFRONT1_matrixIndex, VCFRONT1_a001_WatchdogReset, VCFRONT1_a002_PowerLossReset, VCFRONT1_a003_SWAssertion and 128 more). Bit layout, scaling, units and value tables."
---

# VCFRONT1_alertMatrix (0x341) — VCFRONT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCFRONT1 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 132 signals of VCFRONT1_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT1_alertMatrix` |
| CAN id | 0x341 (833) |
| ECU | [VCFRONT1 ECU](../../vcfront1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT1 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 132 |

## Signals of VCFRONT1_alertMatrix

Tesla Model Y CAN bus signals in `VCFRONT1_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT1_matrixIndex` | selector | VCFRONT1 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | plausible |
| `VCFRONT1_a001_WatchdogReset` | page 0 | VCFRONT1 ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a002_PowerLossReset` | page 0 | VCFRONT1 ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a003_SWAssertion` | page 0 | VCFRONT1 ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a005_CANTXError` | page 0 | VCFRONT1 ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a006_CANTX_cyclicError` | page 0 | VCFRONT1 ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a012_CPUReset` | page 0 | VCFRONT1 ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a013_AlertManagerFault` | page 0 | VCFRONT1 ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a015_NVMMError` | page 0 | VCFRONT1 ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a016_NVMMRecordError` | page 0 | VCFRONT1 ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a017_NVMMStatusDbg` | page 0 | VCFRONT1 ECU: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a018_HardFault` | page 0 | VCFRONT1 ECU: a018 hard fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a019_BusFault` | page 0 | VCFRONT1 ECU: a019 bus fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a021_TaskSchedulerError` | page 0 | VCFRONT1 ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a022_TaskInitError` | page 0 | VCFRONT1 ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a028_UsageFault` | page 0 | VCFRONT1 ECU: a028 usage fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a029_CoreDump` | page 0 | VCFRONT1 ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a030_ECULogUploadRequest` | page 0 | VCFRONT1 ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a031_UDSActive` | page 0 | VCFRONT1 ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a036_UnknownIrq` | page 0 | VCFRONT1 ECU: a036 unknown irq | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a037_MemManageFault` | page 0 | VCFRONT1 ECU: a037 mem manage fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a038_ProtFaultInfo` | page 0 | VCFRONT1 ECU: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a039_ProtFaultAddress` | page 0 | VCFRONT1 ECU: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a040_Backtrace` | page 0 | VCFRONT1 ECU: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a041_HighCPULoad` | page 0 | VCFRONT1 ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a042_HighStackUsage` | page 0 | VCFRONT1 ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a043_Task1msError` | page 0 | VCFRONT1 ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a044_Task10msError` | page 0 | VCFRONT1 ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a045_Task100msError` | page 0 | VCFRONT1 ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a046_Task1000msError` | page 0 | VCFRONT1 ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a058_inputRHighSyncDebug` | page 0 | VCFRONT1 ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a059_inputResistanceHigh` | page 0 | VCFRONT1 ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a060_engineeringBuild` | page 0 | VCFRONT1 ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a061_XCPConnected` | page 1 | VCFRONT1 ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a062_XCPWasConnected` | page 1 | VCFRONT1 ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a063_SwitchFault` | page 1 | VCFRONT1 ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a064_busSleepReqTimeout` | page 1 | VCFRONT1 ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a077_VCBATT0_MIA` | page 1 | VCFRONT1 ECU: a077 VCBATT0 MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a078_VCBATT1_MIA` | page 1 | VCFRONT1 ECU: a078 VCBATT1 MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a079_VCBATT2_MIA` | page 1 | VCFRONT1 ECU: a079 VCBATT2 MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a080_VCFRONT0_MIA` | page 1 | VCFRONT1 ECU: a080 VCFRONT0 MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a081_VCFRONT1_MIA` | page 1 | VCFRONT1 ECU: a081 VCFRONT1 MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a082_VCFRONT2_MIA` | page 1 | VCFRONT1 ECU: a082 VCFRONT2 MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a086_VCBATT_MIA` | page 1 | VCFRONT1 ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a090_APS_MIA` | page 1 | VCFRONT1 ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a091_CMPD_MIA` | page 1 | VCFRONT1 ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a096_OCS1P_MIA` | page 1 | VCFRONT1 ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a098_DIR_MIA` | page 1 | VCFRONT1 ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a100_CANbus_MIA` | page 1 | VCFRONT1 ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a103_CP_MIA` | page 1 | VCFRONT1 ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a104_DAS_MIA` | page 1 | VCFRONT1 ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a105_TAS_MIA` | page 1 | VCFRONT1 ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a106_PCS_MIA` | page 1 | VCFRONT1 ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a107_BMS_MIA` | page 1 | VCFRONT1 ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a108_DIF_MIA` | page 1 | VCFRONT1 ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a109_RCM_MIA` | page 1 | VCFRONT1 ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a110_GTW_MIA` | page 1 | VCFRONT1 ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a111_EPBR_MIA` | page 1 | VCFRONT1 ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a112_EPBL_MIA` | page 1 | VCFRONT1 ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a113_UI_MIA` | page 1 | VCFRONT1 ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a114_ESP_MIA` | page 1 | VCFRONT1 ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a115_VCSEC_MIA` | page 1 | VCFRONT1 ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a116_VCRIGHT_MIA` | page 1 | VCFRONT1 ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a117_VCLEFT_MIA` | page 1 | VCFRONT1 ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a118_VCFRONT_MIA` | page 1 | VCFRONT1 ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a119_SCCM_MIA` | page 1 | VCFRONT1 ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a120_DI_DRIVE_MIA` | page 1 | VCFRONT1 ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a122_ICR_MIA` | page 2 | VCFRONT1 ECU: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a124_BB_MIA` | page 2 | VCFRONT1 ECU: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a125_SCCM_MIA` | page 2 | VCFRONT1 ECU: a125 SCCM MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a126_EPAS3P_MIA` | page 2 | VCFRONT1 ECU: a126 EPAS3 p MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a127_iBoosterEFuseTrip` | page 2 | VCFRONT1 ECU: a127 i booster e fuse trip | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a128_vcrightEFuseTrip` | page 2 | VCFRONT1 ECU: a128 vcright e fuse trip | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a129_pcsEFuseTrip` | page 2 | VCFRONT1 ECU: a129 pcs e fuse trip | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a130_autopilot2EFuseTrip` | page 2 | VCFRONT1 ECU: a130 autopilot2 e fuse trip | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a131_PCSCOMMON_MIA` | page 2 | VCFRONT1 ECU: a131 PCSCOMMON MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a132_epas2EFuseTrip` | page 2 | VCFRONT1 ECU: a132 epas2 e fuse trip | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a133_BRAKE_MIA` | page 2 | VCFRONT1 ECU: a133 BRAKE MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a134_hvContactorsEFuseTrip` | page 2 | VCFRONT1 ECU: a134 hv contactors e fuse trip | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a135_leftHeadlightEFuseTrip` | page 2 | VCFRONT1 ECU: a135 left headlight e fuse trip | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a144_EPAS3S_MIA` | page 2 | VCFRONT1 ECU: a144 EPAS3 s MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a164_eFuseLckoutMissing` | page 2 | VCFRONT1 ECU: a164 e fuse lckout missing | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a165_unxpctdEFuseLckout` | page 2 | VCFRONT1 ECU: a165 unxpctd e fuse lckout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a177_mcuAudioEFuseTrip` | page 2 | VCFRONT1 ECU: a177 mcu audio e fuse trip | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a188_sleepFailed` | page 3 | VCFRONT1 ECU: a188 sleep failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a191_exitDriveDomainDown` | page 3 | VCFRONT1 ECU: a191 exit drive domain down | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a204_undervoltageLoadshedTriggered` | page 3 | VCFRONT1 ECU: a204 undervoltage loadshed triggered | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a205_overvoltageProtectionTriggered` | page 3 | VCFRONT1 ECU: a205 overvoltage protection triggered | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a214_openCircuitDetected` | page 3 | VCFRONT1 ECU: a214 open circuit detected | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a216_powerCutoffImminent` | page 3 | VCFRONT1 ECU: a216 power cutoff imminent | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a220_LVUnhealthy` | page 3 | VCFRONT1 ECU: a220 LV unhealthy | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a223_bridgeOvervoltageSelfTestFailure` | page 3 | VCFRONT1 ECU: a223 bridge overvoltage self test failure | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a229_LVHealthCompromised` | page 3 | VCFRONT1 ECU: a229 LV health compromised | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a230_autopilot2EFuseTripDuringOTA` | page 3 | VCFRONT1 ECU: a230 autopilot2 e fuse trip during OTA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a249_pcsOvClampTripped` | page 4 | VCFRONT1 ECU: a249 pcs ov clamp tripped | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a250_pcsOvShutdownTripped` | page 4 | VCFRONT1 ECU: a250 pcs ov shutdown tripped | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a251_pcsOvShutdownSelfTestFailure` | page 4 | VCFRONT1 ECU: a251 pcs ov shutdown self test failure | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a252_pcsOvShutdownSelfTestStageFailure` | page 4 | VCFRONT1 ECU: a252 pcs ov shutdown self test stage failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a253_pcsOvShutdownHighSideSelfTestDebug` | page 4 | VCFRONT1 ECU: a253 pcs ov shutdown high side self test debug | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a256_nxppca9539Fault` | page 4 | VCFRONT1 ECU: a256 nxppca9539 fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a262_vcrightVoltageMismatch` | page 4 | VCFRONT1 ECU: a262 vcright voltage mismatch | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a263_pcsVoltageMismatch` | page 4 | VCFRONT1 ECU: a263 pcs voltage mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a264_iBoosterVoltageMismatch` | page 4 | VCFRONT1 ECU: a264 i booster voltage mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a266_EPAS2VoltageMismatch` | page 4 | VCFRONT1 ECU: a266 EPAS2 voltage mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a414_undervoltageSelfTestFailure` | page 6 | VCFRONT1 ECU: a414 undervoltage self test failure | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a415_undervoltageSelfTestStuckOff` | page 6 | VCFRONT1 ECU: a415 undervoltage self test stuck off | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a423_rtosSleepFailed` | page 7 | VCFRONT1 ECU: a423 rtos sleep failed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a450_doorWakeToOpenDBG` | page 7 | VCFRONT1 ECU: a450 door wake to open DBG | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a475_vnf1248Fault` | page 7 | VCFRONT1 ECU: a475 vnf1248 fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a480_vnf1048Fault` | page 7 | VCFRONT1 ECU: a480 vnf1048 fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a482_lvBridgeEFuseTrip` | page 8 | VCFRONT1 ECU: a482 lv bridge e fuse trip | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a483_vnf1048SelfTestFailure` | page 8 | VCFRONT1 ECU: a483 vnf1048 self test failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a484_undervoltageSelfTestStuckOn` | page 8 | VCFRONT1 ECU: a484 undervoltage self test stuck on | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a485_uvSelfTestLoadUnattemptedOnDbg` | page 8 | VCFRONT1 ECU: a485 uv self test load unattempted on dbg | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a486_undervoltageSelfTestBridgeSyncFailure` | page 8 | VCFRONT1 ECU: a486 undervoltage self test bridge sync failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a489_vnf1248SelfTestDebug` | page 8 | VCFRONT1 ECU: a489 vnf1248 self test debug | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a490_vnf1248SelfTestFailure` | page 8 | VCFRONT1 ECU: a490 vnf1248 self test failure | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a491_vnf1248ConfigurationMismatch` | page 8 | VCFRONT1 ECU: a491 vnf1248 configuration mismatch | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a496_exitDriveWarningDomainDown` | page 8 | VCFRONT1 ECU: a496 exit drive warning domain down | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a500_eFuseASICStateMismatch` | page 8 | VCFRONT1 ECU: a500 e fuse ASIC state mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a501_vnf1048ConfigurationMismatch` | page 8 | VCFRONT1 ECU: a501 vnf1048 configuration mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a509_eFuseASICManagerStateMismatch` | page 8 | VCFRONT1 ECU: a509 e fuse ASIC manager state mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a523_eFuseThresholdsIncorrect` | page 8 | VCFRONT1 ECU: a523 e fuse thresholds incorrect | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a574_frontDriveInverterEFuseTrip` | page 9 | VCFRONT1 ECU: a574 front drive inverter e fuse trip | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a575_frontDriveInverterEFuseTripDBG` | page 9 | VCFRONT1 ECU: a575 front drive inverter e fuse trip DBG | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a578_vbusFusedLoadShedEFuseTrip` | page 9 | VCFRONT1 ECU: a578 vbus fused load shed e fuse trip | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a581_harnessResistanceInfo` | page 9 | VCFRONT1 ECU: a581 harness resistance info | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a590_vcrightPwrRationalityCurve` | page 9 | VCFRONT1 ECU: a590 vcright pwr rationality curve | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a591_vcrightFastBlowDetection` | page 9 | VCFRONT1 ECU: a591 vcright fast blow detection | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a596_vcrightCurvePowerCutoff` | page 9 | VCFRONT1 ECU: a596 vcright curve power cutoff | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a597_vcrightFastBlowPowerCutoff` | page 9 | VCFRONT1 ECU: a597 vcright fast blow power cutoff | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCFRONT1_a617_APP_MIA` | page 10 | VCFRONT1 ECU: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCFRONT1_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (32 signals), page 1 (34 signals), page 2 (17 signals), page 3 (10 signals), page 4 (10 signals), page 6 (2 signals), page 7 (4 signals), page 8 (13 signals), page 9 (8 signals), page 10 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT1 ECU messages (VCFRONT1)](../../vcfront1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
