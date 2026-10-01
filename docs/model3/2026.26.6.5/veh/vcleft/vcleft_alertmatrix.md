---
layout: default
title: "VCLEFT_alertMatrix (0x360) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: alert matrix. Tesla Model 3 CAN bus message VCLEFT_alertMatrix (0x360) of Left body controller, firmware 2026.26.6.5, 470 signals (VCLEFT_matrixIndex, VCLEFT_a001_WatchdogReset, VCLEFT_a002_PowerLossReset, VCLEFT_a003_SWAssertion and 466 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_alertMatrix (0x360) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: alert matrix; frame length observed on a vehicle bus. This page documents the 470 signals of VCLEFT_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_alertMatrix` |
| CAN id | 0x360 (864) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 470 |

## Signals of VCLEFT_alertMatrix

Tesla Model 3 CAN bus signals in `VCLEFT_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_matrixIndex` | selector | Left body controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | validated |
| `VCLEFT_a001_WatchdogReset` | page 0 | Left body controller: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a002_PowerLossReset` | page 0 | Left body controller: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a003_SWAssertion` | page 0 | Left body controller: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a005_CANTXError` | page 0 | Left body controller: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a006_CANTX_cyclicError` | page 0 | Left body controller: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a010_ExtSupplyVoltError` | page 0 | Left body controller: a010 ext supply volt error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a012_CPUReset` | page 0 | Left body controller: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a013_AlertManagerFault` | page 0 | Left body controller: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a015_NVMMError` | page 0 | Left body controller: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a016_NVMMRecordError` | page 0 | Left body controller: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a017_NVMMStatusDbg` | page 0 | Left body controller: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a021_TaskSchedulerError` | page 0 | Left body controller: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a022_TaskInitError` | page 0 | Left body controller: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a029_CoreDump` | page 0 | Left body controller: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a030_ECULogUploadRequest` | page 0 | Left body controller: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a031_UDSActive` | page 0 | Left body controller: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a041_HighCPULoad` | page 0 | Left body controller: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a042_HighStackUsage` | page 0 | Left body controller: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a043_Task1msError` | page 0 | Left body controller: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a044_Task10msError` | page 0 | Left body controller: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a045_Task100msError` | page 0 | Left body controller: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a046_Task1000msError` | page 0 | Left body controller: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a057_HVP_MIA` | page 0 | Left body controller: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a058_inputRHighSyncDebug` | page 0 | Left body controller: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a059_inputResistanceHigh` | page 0 | Left body controller: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a060_engineeringBuild` | page 0 | Left body controller: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a061_XCPConnected` | page 1 | Left body controller: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a062_XCPWasConnected` | page 1 | Left body controller: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a063_SwitchFault` | page 1 | Left body controller: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a064_busSleepReqTimeout` | page 1 | Left body controller: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a065_emiosIsrRateLimitedDbg` | page 1 | Left body controller: a065 emios isr rate limited dbg | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a066_emiosIsrShortPeriodDetectedDbg` | page 1 | Left body controller: a066 emios isr short period detected dbg | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a082_VCRIGHT_IPC_MIA` | page 1 | Left body controller: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a083_VCLEFT_IPC_MIA` | page 1 | Left body controller: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a084_TPMS_MIA` | page 1 | Left body controller: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a085_CCCM_MIA` | page 1 | Left body controller: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a086_VCBATT_MIA` | page 1 | Left body controller: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a087_DIREL_MIA` | page 1 | Left body controller: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a088_DIRER_MIA` | page 1 | Left body controller: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a089_IBST_MIA` | page 1 | Left body controller: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a090_APS_MIA` | page 1 | Left body controller: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a091_CMPD_MIA` | page 1 | Left body controller: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a092_VCSEATD_MIA` | page 1 | Left body controller: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a093_VCSEATP_MIA` | page 1 | Left body controller: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a094_EPAS3P_MIA` | page 1 | Left body controller: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a095_CHG_MIA` | page 1 | Left body controller: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a096_OCS1P_MIA` | page 1 | Left body controller: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a097_CMP_MIA` | page 1 | Left body controller: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a098_DIR_MIA` | page 1 | Left body controller: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a099_PARK_MIA` | page 1 | Left body controller: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a100_CANbus_MIA` | page 1 | Left body controller: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a101_PM_MIA` | page 1 | Left body controller: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a102_PTC_MIA` | page 1 | Left body controller: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a103_CP_MIA` | page 1 | Left body controller: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a104_DAS_MIA` | page 1 | Left body controller: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a105_TAS_MIA` | page 1 | Left body controller: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a106_PCS_MIA` | page 1 | Left body controller: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a107_BMS_MIA` | page 1 | Left body controller: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a108_DIF_MIA` | page 1 | Left body controller: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a109_RCM_MIA` | page 1 | Left body controller: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a110_GTW_MIA` | page 1 | Left body controller: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a111_EPBR_MIA` | page 1 | Left body controller: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a112_EPBL_MIA` | page 1 | Left body controller: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a113_UI_MIA` | page 1 | Left body controller: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a114_ESP_MIA` | page 1 | Left body controller: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a115_VCSEC_MIA` | page 1 | Left body controller: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a116_VCRIGHT_MIA` | page 1 | Left body controller: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a117_VCLEFT_MIA` | page 1 | Left body controller: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a118_VCFRONT_MIA` | page 1 | Left body controller: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a119_SCCM_MIA` | page 1 | Left body controller: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a120_DI_DRIVE_MIA` | page 1 | Left body controller: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a121_ETC_MIA` | page 2 | Left body controller: a121 ETC MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a122_ICR_MIA` | page 2 | Left body controller: a122 ICR MIA | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a123_AID_MIA` | page 2 | Left body controller: a123 AID MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a124_BB_MIA` | page 2 | Left body controller: a124 BB MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a125_RCU_MIA` | page 2 | Left body controller: a125 RCU MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a129_blowerICLatchFault` | page 2 | Left body controller: a129 blower IC latch fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a130_blowerICWarning` | page 2 | Left body controller: a130 blower IC warning | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a131_blowerICTransFault` | page 2 | Left body controller: a131 blower IC trans fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a132_blowerSoftStall` | page 2 | Left body controller: a132 blower soft stall | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a133_blowerLowRPMCBang` | page 2 | Left body controller: a133 blower low RPMC bang | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a134_SteerColUpDownUnCal` | page 2 | Left body controller: a134 steer col up down un cal | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a135_SteerColInOutUnCal` | page 2 | Left body controller: a135 steer col in out un cal | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a136_brakeSwitchMismatch` | page 2 | Left body controller: a136 brake switch mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a137_VCSECPowerCycled` | page 2 | Left body controller: a137 VCSEC power cycled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a138_consoleDoorAssist` | page 2 | Left body controller: a138 console door assist | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a139_BLERearPowerCycled` | page 2 | Left body controller: a139 BLE rear power cycled | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a140_BLELeftPowerCycled` | page 2 | Left body controller: a140 BLE left power cycled | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a141_12VAuxPowerTrip` | page 2 | Left body controller: a141 12 v aux power trip | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a143_mirrorManuallyFolded` | page 2 | Left body controller: a143 mirror manually folded | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a145_brakeSwitchStuck` | page 2 | Left body controller: a145 brake switch stuck | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a148_brakePressInputMismatch` | page 2 | Left body controller: a148 brake press input mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a150_windowPinchFront` | page 2 | Left body controller: a150 window pinch front | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a151_windowPinchRear` | page 2 | Left body controller: a151 window pinch rear | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a152_windowUncalFront` | page 2 | Left body controller: a152 window uncal front | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a153_windowUncalRear` | page 2 | Left body controller: a153 window uncal rear | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a154_windowThermalFront` | page 2 | Left body controller: a154 window thermal front | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a155_windowThermalRear` | page 2 | Left body controller: a155 window thermal rear | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a156_windowNoInputFront` | page 2 | Left body controller: a156 window no input front | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a157_windowNoInputRear` | page 2 | Left body controller: a157 window no input rear | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a158_windowPinchOverideF` | page 2 | Left body controller: a158 window pinch overide f | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a159_windowPinchOverideR` | page 2 | Left body controller: a159 window pinch overide r | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a160_windowUndercurrentF` | page 2 | Left body controller: a160 window undercurrent f | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a161_windowUndercurrentR` | page 2 | Left body controller: a161 window undercurrent r | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a162_windowEncoderStallF` | page 2 | Left body controller: a162 window encoder stall f | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a163_windowEncoderStallR` | page 2 | Left body controller: a163 window encoder stall r | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a164_windowFactoryTest` | page 2 | Left body controller: a164 window factory test | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a165_windowFactoryTest2` | page 2 | Left body controller: a165 window factory test2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a166_windowDebug` | page 2 | Left body controller: a166 window debug | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a167_windowDebugPinchF` | page 2 | Left body controller: a167 window debug pinch f | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a168_windowDebugPinchR` | page 2 | Left body controller: a168 window debug pinch r | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a169_windowCurrentPeakF` | page 2 | Left body controller: a169 window current peak f | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a170_windowCurrentPeakR` | page 2 | Left body controller: a170 window current peak r | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a172_SPI_MIA` | page 2 | Left body controller: a172 SPI MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a173_windowBtnDoorOpen` | page 2 | Left body controller: a173 window btn door open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a175_windowSealDefectFront` | page 2 | Left body controller: a175 window seal defect front | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a176_windowSealDefectRear` | page 2 | Left body controller: a176 window seal defect rear | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a180_frontDoorLatchRehome` | page 2 | Left body controller: a180 front door latch rehome | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a181_rearDoorLatchRehome` | page 3 | Left body controller: a181 rear door latch rehome | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a182_emergencyLatchRel` | page 3 | Left body controller: a182 emergency latch rel | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a183_doorStateFactoryTest` | page 3 | Left body controller: a183 door state factory test | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a185_summonAborted` | page 3 | Left body controller: a185 summon aborted | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a186_latchReleaseFailedF` | page 3 | Left body controller: a186 latch release failed f | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a187_latchReleaseFailedR` | page 3 | Left body controller: a187 latch release failed r | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a188_latchUnableToRearmF` | page 3 | Left body controller: a188 latch unable to rearm f | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a189_latchUnableToRearmR` | page 3 | Left body controller: a189 latch unable to rearm r | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a190_eFuseMgmtVbatFused` | page 3 | Left body controller: a190 e fuse mgmt vbat fused | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a191_TLCOvercurrent` | page 3 | Left body controller: a191 TLC overcurrent | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a192_blowerGeneralFault` | page 3 | Left body controller: a192 blower general fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a193_blowerMIA` | page 3 | Left body controller: a193 blower MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a194_blowerUnidentified` | page 3 | Left body controller: a194 blower unidentified | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a195_blowerIdentificationFailed` | page 3 | Left body controller: a195 blower identification failed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a196_VEHCANOverterminate` | page 3 | Left body controller: a196 VEHCAN overterminate | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a197_VEHCANUndertrminate` | page 3 | Left body controller: a197 VEHCAN undertrminate | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a200_motorPhantomEncoder` | page 3 | Left body controller: a200 motor phantom encoder | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a201_motorDutyEncDisabl` | page 3 | Left body controller: a201 motor duty enc disabl | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a202_epbmUnderIStatic` | page 3 | Left body controller: a202 epbm under i static | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a203_epbmOverIStatic` | page 3 | Left body controller: a203 epbm over i static | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a204_epbmUnderIDyn` | page 3 | Left body controller: a204 epbm under i dyn | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a205_epbmOverIDyn` | page 3 | Left body controller: a205 epbm over i dyn | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a206_epbWrongDirection` | page 3 | Left body controller: a206 epb wrong direction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a207_epbmEnableWrong` | page 3 | Left body controller: a207 epbm enable wrong | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a208_epbFaulted` | page 3 | Left body controller: a208 epb faulted | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a209_epbStateMisTime` | page 3 | Left body controller: a209 epb state mis time | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a210_epbStateTime` | page 3 | Left body controller: a210 epb state time | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a211_epbmUnderIStaticNew` | page 3 | Left body controller: a211 epbm under i static new | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a212_epbmOverIStaticNew` | page 3 | Left body controller: a212 epbm over i static new | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a213_epbmUnderIDynNew` | page 3 | Left body controller: a213 epbm under i dyn new | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a214_epbmOverIDynNew` | page 3 | Left body controller: a214 epbm over i dyn new | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a215_currentDesyncWarning` | page 3 | Left body controller: a215 current desync warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a216_SPI_MIA_debugData1` | page 3 | Left body controller: a216 SPI MIA debug data1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a217_SPI_MIA_debugData2` | page 3 | Left body controller: a217 SPI MIA debug data2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a218_motorDriverFault` | page 3 | Left body controller: a218 motor driver fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a219_motorCurrentDropout` | page 3 | Left body controller: a219 motor current dropout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a220_reverseLightFaultUser` | page 3 | Left body controller: a220 reverse light fault user | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a221_hardwareLoadshedTriggered` | page 3 | Left body controller: a221 hardware loadshed triggered | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a223_VCBATT1_MIA` | page 3 | Left body controller: a223 VCBATT1 MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a224_seatEncStallTrack` | page 3 | Left body controller: a224 seat enc stall track | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a225_seatEncStallBack` | page 3 | Left body controller: a225 seat enc stall back | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a226_seatEncStallTilt` | page 3 | Left body controller: a226 seat enc stall tilt | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a227_seatEncStallLift` | page 3 | Left body controller: a227 seat enc stall lift | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a228_seatEncOverTrack` | page 3 | Left body controller: a228 seat enc over track | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a229_seatEncOverBack` | page 3 | Left body controller: a229 seat enc over back | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a230_seatEncOverTilt` | page 3 | Left body controller: a230 seat enc over tilt | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a231_seatEncOverLift` | page 3 | Left body controller: a231 seat enc over lift | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a232_seatCurrUnderTrack` | page 3 | Left body controller: a232 seat curr under track | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a233_seatCurrUnderBack` | page 3 | Left body controller: a233 seat curr under back | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a234_seatCurrUnderTilt` | page 3 | Left body controller: a234 seat curr under tilt | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a235_seatCurrUnderLift` | page 3 | Left body controller: a235 seat curr under lift | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a236_lumbarOverPresA` | page 3 | Left body controller: a236 lumbar over pres a | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a237_lumbarOverPresB` | page 3 | Left body controller: a237 lumbar over pres b | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a238_lumbarValveMIA` | page 3 | Left body controller: a238 lumbar valve MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a239_seatHeatIFront` | page 3 | Left body controller: a239 seat heat i front | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a240_seatHeatShortFront` | page 3 | Left body controller: a240 seat heat short front | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a241_seatHeatMIAFront` | page 4 | Left body controller: a241 seat heat MIA front | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a242_seatHeatIRearL` | page 4 | Left body controller: a242 seat heat i rear l | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a243_seatHeatShortRearL` | page 4 | Left body controller: a243 seat heat short rear l | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a244_seatHeatMIARearL` | page 4 | Left body controller: a244 seat heat MIA rear l | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a245_seatHeatIRearC` | page 4 | Left body controller: a245 seat heat i rear c | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a246_seatHeatShortRearC` | page 4 | Left body controller: a246 seat heat short rear c | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a247_seatHeatMIARearC` | page 4 | Left body controller: a247 seat heat MIA rear c | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a248_seatHeatIRearR` | page 4 | Left body controller: a248 seat heat i rear r | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a249_seatHeatShortRearR` | page 4 | Left body controller: a249 seat heat short rear r | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a250_seatHeatMIARearR` | page 4 | Left body controller: a250 seat heat MIA rear r | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a251_seatUncalTrack` | page 4 | Left body controller: a251 seat uncal track | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a252_seatUncalBack` | page 4 | Left body controller: a252 seat uncal back | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a253_seatUncalTilt` | page 4 | Left body controller: a253 seat uncal tilt | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a254_seatUncalLift` | page 4 | Left body controller: a254 seat uncal lift | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a256_nxppca9539Fault` | page 4 | Left body controller: a256 nxppca9539 fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a257_USBMIA` | page 4 | Left body controller: a257 USBMIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a259_latchDisarmDelayF` | page 4 | Left body controller: a259 latch disarm delay f | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a260_latchDisarmDelayR` | page 4 | Left body controller: a260 latch disarm delay r | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a261_emergencyLatchRelRear` | page 4 | Left body controller: a261 emergency latch rel rear | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a263_seatTrackStallDebug` | page 4 | Left body controller: a263 seat track stall debug | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a264_seatBackStallDebug` | page 4 | Left body controller: a264 seat back stall debug | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a265_seatTiltStallDebug` | page 4 | Left body controller: a265 seat tilt stall debug | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a266_seatLiftStallDebug` | page 4 | Left body controller: a266 seat lift stall debug | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a267_seatTrackHCEncStlDbg` | page 4 | Left body controller: a267 seat track HC enc stl dbg | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a268_seatBackHCEncStlDbg` | page 4 | Left body controller: a268 seat back HC enc stl dbg | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a269_seatTiltHCEncStlDbg` | page 4 | Left body controller: a269 seat tilt HC enc stl dbg | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a270_seatLiftHCEncStlDbg` | page 4 | Left body controller: a270 seat lift HC enc stl dbg | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a272_vhclPwrStateMsmtch` | page 4 | Left body controller: a272 vhcl pwr state msmtch | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a273_handleStuckActiveF` | page 4 | Left body controller: a273 handle stuck active f | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a274_handleStuckActiveR` | page 4 | Left body controller: a274 handle stuck active r | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a275_leftTurnLightFault` | page 4 | Left body controller: a275 left turn light fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a276_mirrorDebug` | page 4 | Left body controller: a276 mirror debug | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a277_BLELeftUnderVoltage` | page 4 | Left body controller: a277 BLE left under voltage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a278_BLERearUnderVoltage` | page 4 | Left body controller: a278 BLE rear under voltage | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a279_VCSECUnderVoltage` | page 4 | Left body controller: a279 VCSEC under voltage | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a280_latchDidNotDisarmF` | page 4 | Left body controller: a280 latch did not disarm f | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a281_latchDidNotDisarmR` | page 4 | Left body controller: a281 latch did not disarm r | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a282_latchUnexpectedArmF` | page 4 | Left body controller: a282 latch unexpected arm f | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a283_latchUnexpectedArmR` | page 4 | Left body controller: a283 latch unexpected arm r | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a284_blowerFbkSanity` | page 4 | Left body controller: a284 blower fbk sanity | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a285_blowerChipComms` | page 4 | Left body controller: a285 blower chip comms | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a286_windowSpeedInvalidF` | page 4 | Left body controller: a286 window speed invalid f | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a287_windowSpeedInvalidR` | page 4 | Left body controller: a287 window speed invalid r | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a288_handlePWMPeriodF` | page 4 | Left body controller: a288 handle PWM period f | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a289_handlePWMPeriodR` | page 4 | Left body controller: a289 handle PWM period r | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a290_occupancyFaultedFront` | page 4 | Left body controller: a290 occupancy faulted front | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a291_buckleFaultedFront` | page 4 | Left body controller: a291 buckle faulted front | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a292_occupancyFaultedRearL` | page 4 | Left body controller: a292 occupancy faulted rear l | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a293_occupancyFaultedRearC` | page 4 | Left body controller: a293 occupancy faulted rear c | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a294_occupancyFaultedRearR` | page 4 | Left body controller: a294 occupancy faulted rear r | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a295_buckleFaultedRearL` | page 4 | Left body controller: a295 buckle faulted rear l | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a296_buckleFaultedRearC` | page 4 | Left body controller: a296 buckle faulted rear c | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a297_seatBelowMinPumpTmp` | page 4 | Left body controller: a297 seat below min pump tmp | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a299_swcMIA` | page 4 | Left body controller: a299 swc MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a300_swcUnderVoltage` | page 4 | Left body controller: a300 swc under voltage | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a301_swcOverVoltage` | page 5 | Left body controller: a301 swc over voltage | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a302_blowerGeneralFault` | page 5 | Left body controller: a302 blower general fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a303_eFuseMgmtWindowLift` | page 5 | Left body controller: a303 e fuse mgmt window lift | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a304_frontIntHandleUnexpectedVoltage` | page 5 | Left body controller: a304 front int handle unexpected voltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a305_rearIntHandleUnexpectedVoltage` | page 5 | Left body controller: a305 rear int handle unexpected voltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a306_handleDisconnectedF` | page 5 | Left body controller: a306 handle disconnected f | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a307_handleDisconnectedR` | page 5 | Left body controller: a307 handle disconnected r | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a308_sirenMIA` | page 5 | Left body controller: a308 siren MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a309_brakeSwitchFaulted` | page 5 | Left body controller: a309 brake switch faulted | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a310_mirrorFoldStall` | page 5 | Left body controller: a310 mirror fold stall | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a311_leftBrakeLightFault` | page 5 | Left body controller: a311 left brake light fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a312_leftTailLightFault` | page 5 | Left body controller: a312 left tail light fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a313_leftFootwellLightFault` | page 5 | Left body controller: a313 left footwell light fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a314_leftMapPocketLightFault` | page 5 | Left body controller: a314 left map pocket light fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a315_leftInteriorTrunkLightFault` | page 5 | Left body controller: a315 left interior trunk light fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a316_mirrorPrematureFoldStall` | page 5 | Left body controller: a316 mirror premature fold stall | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a317_epbmLimpModeEnabled` | page 5 | Left body controller: a317 epbm limp mode enabled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a318_trailerIncorrectConfig` | page 5 | Left body controller: a318 trailer incorrect config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a319_brakePressPrimaryInputFaulted` | page 5 | Left body controller: a319 brake press primary input faulted | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a320_windowReportCrackedAtTrimClear` | page 5 | Left body controller: a320 window report cracked at trim clear | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a321_windowRezeroedDebugF` | page 5 | Left body controller: a321 window rezeroed debug f | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a322_windowRezeroedDebugR` | page 5 | Left body controller: a322 window rezeroed debug r | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a323_mirrorCalibrated` | page 5 | Left body controller: a323 mirror calibrated | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a324_mirrorHeatFault` | page 5 | Left body controller: a324 mirror heat fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a325_hghtSnsrUnplgdFL` | page 5 | Left body controller: a325 hght snsr unplgd FL | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a326_hghtSnsrUnplgdRL` | page 5 | Left body controller: a326 hght snsr unplgd RL | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a327_hghtSnsrFaultFL` | page 5 | Left body controller: a327 hght snsr fault FL | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a328_hghtSnsrFaultRL` | page 5 | Left body controller: a328 hght snsr fault RL | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a329_noRideHeightCalib` | page 5 | Left body controller: a329 no ride height calib | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a330_shortDropFailedF` | page 5 | Left body controller: a330 short drop failed f | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a331_shortDropFailedR` | page 5 | Left body controller: a331 short drop failed r | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a332_intrusionSensorMIA` | page 5 | Left body controller: a332 intrusion sensor MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a333_overheadConsoleMIA` | page 5 | Left body controller: a333 overhead console MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a334_overheadConsoleInternalFault` | page 5 | Left body controller: a334 overhead console internal fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a335_intrusionSensorInternalFault` | page 5 | Left body controller: a335 intrusion sensor internal fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a336_windowDropRevThermalF` | page 5 | Left body controller: a336 window drop rev thermal f | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a337_windowDropRevThermalR` | page 5 | Left body controller: a337 window drop rev thermal r | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a338_trailerLightControllerMIA` | page 5 | Left body controller: a338 trailer light controller MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a339_trailerLeftTurnLightNotDetected` | page 5 | Left body controller: a339 trailer left turn light not detected | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a340_trailerRightTurnLightNotDetected` | page 5 | Left body controller: a340 trailer right turn light not detected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a341_trailerLightFault` | page 5 | Left body controller: a341 trailer light fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a342_trailerLightControllerFault` | page 5 | Left body controller: a342 trailer light controller fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a345_chargePortPowerCycling` | page 5 | Left body controller: a345 charge port power cycling | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a346_eFuseMgmtVbatFused2` | page 5 | Left body controller: a346 e fuse mgmt vbat fused2 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a347_nonContMonitorClearedDBG` | page 5 | Left body controller: a347 non cont monitor cleared DBG | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a348_CPSleepOvercurrent` | page 5 | Left body controller: a348 CP sleep overcurrent | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a349_CPSleepUndervoltage` | page 5 | Left body controller: a349 CP sleep undervoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a350_ensOutOfRange` | page 5 | Left body controller: a350 ens out of range | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a351_debugLiftgateCurrentSpike` | page 5 | Left body controller: a351 debug liftgate current spike | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a352_liftgateClosingLatchEntryFailed` | page 5 | Left body controller: a352 liftgate closing latch entry failed | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a353_eFuseMgmtSteeringColumn` | page 5 | Left body controller: a353 e fuse mgmt steering column | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a354_eFuseMgmtLiftGate` | page 5 | Left body controller: a354 e fuse mgmt lift gate | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a355_liftgateUnexpectedStop` | page 5 | Left body controller: a355 liftgate unexpected stop | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a356_liftgateFactoryTest` | page 5 | Left body controller: a356 liftgate factory test | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a357_liftgateUncalibrated` | page 5 | Left body controller: a357 liftgate uncalibrated | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a358_debugLiftgateCurrentDropout` | page 5 | Left body controller: a358 debug liftgate current dropout | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a359_liftgateLatchExitNoPositionChange` | page 5 | Left body controller: a359 liftgate latch exit no position change | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a360_detectedStationaryWhileMoving` | page 5 | Left body controller: a360 detected stationary while moving | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a361_stationaryThresholdsIncorrect` | page 6 | Left body controller: a361 stationary thresholds incorrect | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a362_movingThresholdsIncorrect` | page 6 | Left body controller: a362 moving thresholds incorrect | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a363_liftgateOpenAngleSetReq` | page 6 | Left body controller: a363 liftgate open angle set req | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a365_pitchUnlatchDisabled` | page 6 | Left body controller: a365 pitch unlatch disabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a366_liftgateLatchEntryDBG` | page 6 | Left body controller: a366 liftgate latch entry DBG | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a370_seat2RowPitchUnlatched` | page 6 | Left body controller: a370 seat2 row pitch unlatched | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a371_seat2RowTrackUnlatched` | page 6 | Left body controller: a371 seat2 row track unlatched | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a372_seat2RowBackrestUnlatched` | page 6 | Left body controller: a372 seat2 row backrest unlatched | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a373_windowSwOpenReqInDogMode` | page 6 | Left body controller: a373 window sw open req in dog mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a374_trailerLightFaultModelY` | page 6 | Left body controller: a374 trailer light fault model y | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a375_windowPinchOverrideNudge` | page 6 | Left body controller: a375 window pinch override nudge | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a376_seat2RowBridgeCurrentExceeded` | page 6 | Left body controller: a376 seat2 row bridge current exceeded | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a380_steerColThermalLimited` | page 6 | Left body controller: a380 steer col thermal limited | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a381_pitchEstimation1` | page 6 | Left body controller: a381 pitch estimation1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a382_pitchEstimation2` | page 6 | Left body controller: a382 pitch estimation2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a383_steerColInOutMotorStallCurrent` | page 6 | Left body controller: a383 steer col in out motor stall current | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a384_steerColUpDownMotorStallCurrent` | page 6 | Left body controller: a384 steer col up down motor stall current | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a385_steerColInOutMotorUnderCurrent` | page 6 | Left body controller: a385 steer col in out motor under current | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a386_steerColUpDownMotorUnderCurrent` | page 6 | Left body controller: a386 steer col up down motor under current | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a387_steerColInOutMotorEncoderStalled` | page 6 | Left body controller: a387 steer col in out motor encoder stalled | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a388_steerColUpDownMotorEncoderStalled` | page 6 | Left body controller: a388 steer col up down motor encoder stalled | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a389_steerColInOutEncoderOutOfRange` | page 6 | Left body controller: a389 steer col in out encoder out of range | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a390_steerColUpDownEncoderOutOfRange` | page 6 | Left body controller: a390 steer col up down encoder out of range | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a391_pitchEstimationImplausible` | page 6 | Left body controller: a391 pitch estimation implausible | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a392_pitchEstimationGPSImprovedReinit` | page 6 | Left body controller: a392 pitch estimation GPS improved reinit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a393_pitchEstimationNoGPSFusion` | page 6 | Left body controller: a393 pitch estimation no GPS fusion | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a394_swsTouchTooNegativeDelta` | page 6 | Left body controller: a394 sws touch too negative delta | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a395_swsTouchAdcCheckFail` | page 6 | Left body controller: a395 sws touch adc check fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a396_swsTouchStuckFault` | page 6 | Left body controller: a396 sws touch stuck fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a397_swsTouchOutOfRangeFault` | page 6 | Left body controller: a397 sws touch out of range fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a398_swsTouchNvmFault` | page 6 | Left body controller: a398 sws touch nvm fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a399_swsTouchNoisyBaselineInitialization` | page 6 | Left body controller: a399 sws touch noisy baseline initialization | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a400_swsTouchDebouncedProcessingError` | page 6 | Left body controller: a400 sws touch debounced processing error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a401_swsForceTestPatternViolation` | page 6 | Left body controller: a401 sws force test pattern violation | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a402_swsForceOutOfRange` | page 6 | Left body controller: a402 sws force out of range | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a403_swsForceAdcCheckFail` | page 6 | Left body controller: a403 sws force adc check fail | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a404_swsForceI2cError` | page 6 | Left body controller: a404 sws force i2c error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a405_swsForceCalibrationFault` | page 6 | Left body controller: a405 sws force calibration fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a406_swsForceParametersFault` | page 6 | Left body controller: a406 sws force parameters fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a407_swsForceNvmFault` | page 6 | Left body controller: a407 sws force nvm fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a408_swsForceTouchSensorFault` | page 6 | Left body controller: a408 sws force touch sensor fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a409_swsScrollWheelPushFault` | page 6 | Left body controller: a409 sws scroll wheel push fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a410_swsScrollWheelTiltFault` | page 6 | Left body controller: a410 sws scroll wheel tilt fault | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a411_swsScrollWheelScrollFault` | page 6 | Left body controller: a411 sws scroll wheel scroll fault | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a412_leftBrakeTailLightFault` | page 6 | Left body controller: a412 left brake tail light fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a413_undervoltageSelfTestFailure` | page 6 | Left body controller: a413 undervoltage self test failure | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a414_swsHapticMotorFault` | page 6 | Left body controller: a414 sws haptic motor fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a415_swsMiscFault` | page 6 | Left body controller: a415 sws misc fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a416_fohmTouchAdcCheckFail` | page 6 | Left body controller: a416 fohm touch adc check fail | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a417_fohmTouchOutOfRangeFault` | page 6 | Left body controller: a417 fohm touch out of range fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a418_fohmTouchVarianceFail` | page 6 | Left body controller: a418 fohm touch variance fail | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a419_fohmTouchStuck` | page 6 | Left body controller: a419 fohm touch stuck | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a420_fohmTouchSensorsImplausible` | page 6 | Left body controller: a420 fohm touch sensors implausible | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a421_fohmForceOutOfRangeFault` | page 7 | Left body controller: a421 fohm force out of range fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a422_undervoltageSelfTestStuckOff` | page 7 | Left body controller: a422 undervoltage self test stuck off | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a423_fohmForceI2cError` | page 7 | Left body controller: a423 fohm force i2c error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a424_fohmAmberLEDFault` | page 7 | Left body controller: a424 fohm amber LED fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a425_fohmVanityPowerSupplyFault` | page 7 | Left body controller: a425 fohm vanity power supply fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a426_seatAbuseMotorWarn` | page 7 | Left body controller: a426 seat abuse motor warn | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a427_seatAbuseMotorStop` | page 7 | Left body controller: a427 seat abuse motor stop | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a428_seatAbuseBufferWarn` | page 7 | Left body controller: a428 seat abuse buffer warn | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a429_seatAbuseBufferFull` | page 7 | Left body controller: a429 seat abuse buffer full | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a430_fohmRearDomeLightPowerSupplyFault` | page 7 | Left body controller: a430 fohm rear dome light power supply fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a431_fohmVbatFault` | page 7 | Left body controller: a431 fohm vbat fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a432_fohmMiscFault` | page 7 | Left body controller: a432 fohm misc fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a433_fohmForceCalibrationInvalid` | page 7 | Left body controller: a433 fohm force calibration invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a434_swsScrollWheelPushData` | page 7 | Left body controller: a434 sws scroll wheel push data | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a435_swsNoReasonTouchFault` | page 7 | Left body controller: a435 sws no reason touch fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a436_swsNoReasonForceFault` | page 7 | Left body controller: a436 sws no reason force fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a437_hvacRearLeftVerticalDriverFaulted` | page 7 | Left body controller: a437 hvac rear left vertical driver faulted | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a438_hvacRearLeftLateralDriverFaulted` | page 7 | Left body controller: a438 hvac rear left lateral driver faulted | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a439_hvacRearRightVerticalDriverFaulted` | page 7 | Left body controller: a439 hvac rear right vertical driver faulted | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a440_hvacRearRightLateralDriverFaulted` | page 7 | Left body controller: a440 hvac rear right lateral driver faulted | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a441_prndMIA` | page 7 | Left body controller: a441 prnd MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a442_swsLongTouchEvent` | page 7 | Left body controller: a442 sws long touch event | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a444_drv8703Fault` | page 7 | Left body controller: a444 drv8703 fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a445_drv8703SpiFaultDBG` | page 7 | Left body controller: a445 drv8703 spi fault DBG | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a446_trailerAuxReversePower` | page 7 | Left body controller: a446 trailer aux reverse power | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a447_steeringColInOutEndstopCal` | page 7 | Left body controller: a447 steering col in out endstop cal | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a448_steeringColUpDownEndstopCal` | page 7 | Left body controller: a448 steering col up down endstop cal | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a449_steerColInOutMotorShadowAlgoResetOffset` | page 7 | Left body controller: a449 steer col in out motor shadow algo reset offset | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a450_steerColUpDownMotorShadowAlgoResetOffset` | page 7 | Left body controller: a450 steer col up down motor shadow algo reset offset | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a451_wirelessChargerMIA` | page 7 | Left body controller: a451 wireless charger MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a453_liftgatePinchDetected` | page 7 | Left body controller: a453 liftgate pinch detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a454_wirelessChargerFault` | page 7 | Left body controller: a454 wireless charger fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a455_liftgateUnexpectedShutfaceSwPressed` | page 7 | Left body controller: a455 liftgate unexpected shutface sw pressed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a460_etcDebug` | page 7 | Left body controller: a460 etc debug | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a466_hvac2RLeftAirwaveVerticalFault` | page 7 | Left body controller: a466 hvac2 r left airwave vertical fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a467_hvac2RLeftAirwaveVerticalWarning` | page 7 | Left body controller: a467 hvac2 r left airwave vertical warning | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a468_hvac2RLeftAirwaveVerticalUncalib` | page 7 | Left body controller: a468 hvac2 r left airwave vertical uncalib | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a469_hvac2RLeftAirwaveLateralFault` | page 7 | Left body controller: a469 hvac2 r left airwave lateral fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a470_hvac2RLeftAirwaveLateralWarning` | page 7 | Left body controller: a470 hvac2 r left airwave lateral warning | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a471_hvac2RLeftAirwaveLateralUncalib` | page 7 | Left body controller: a471 hvac2 r left airwave lateral uncalib | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a472_hvac2RRightAirwaveVerticalFault` | page 7 | Left body controller: a472 hvac2 r right airwave vertical fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a473_hvac2RRightAirwaveVerticalWarning` | page 7 | Left body controller: a473 hvac2 r right airwave vertical warning | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a474_hvac2RRightAirwaveVerticalUncalib` | page 7 | Left body controller: a474 hvac2 r right airwave vertical uncalib | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a475_hvac2RRightAirwaveLateralFault` | page 7 | Left body controller: a475 hvac2 r right airwave lateral fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a476_hvac2RRightAirwaveLateralWarning` | page 7 | Left body controller: a476 hvac2 r right airwave lateral warning | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a477_hvac2RRightAirwaveLateralUncalib` | page 7 | Left body controller: a477 hvac2 r right airwave lateral uncalib | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a478_BPillarCameraHeaterFault` | page 7 | Left body controller: a478 b pillar camera heater fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a480_vnf1048Fault` | page 7 | Left body controller: a480 vnf1048 fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a481_vnf1048SelfTestFailure` | page 8 | Left body controller: a481 vnf1048 self test failure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a482_NCV77XXFault` | page 8 | Left body controller: a482 NCV77 XX fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a483_leftTurnLightFaultUser` | page 8 | Left body controller: a483 left turn light fault user | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a484_leftBrakeLightFaultUser` | page 8 | Left body controller: a484 left brake light fault user | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a485_uvSelfTestLoadUnattemptedOnDbg` | page 8 | Left body controller: a485 uv self test load unattempted on dbg | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a488_undervoltageSelfTestStuckOnDebug` | page 8 | Left body controller: a488 undervoltage self test stuck on debug | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a489_undervoltageSelfTestStuckOn` | page 8 | Left body controller: a489 undervoltage self test stuck on | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a490_vehicleOccupiedOnOTAStart` | page 8 | Left body controller: a490 vehicle occupied on OTA start | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a493_12vSocketFrontEFuseTrip` | page 8 | Left body controller: a493 12v socket front e fuse trip | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a494_12vSocketRearEFuseTrip` | page 8 | Left body controller: a494 12v socket rear e fuse trip | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a497_CANMsgMACVerificationKeyNotProvisioned` | page 8 | Left body controller: a497 CAN msg MAC verification key not provisioned | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a498_CANMsgMACVerificationFailure` | page 8 | Left body controller: a498 CAN msg MAC verification failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a499_epbmInvalidateCdp` | page 8 | Left body controller: a499 epbm invalidate cdp | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a500_eFuseASICStateMismatch` | page 8 | Left body controller: a500 e fuse ASIC state mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a501_vnf1048ConfigurationMismatch` | page 8 | Left body controller: a501 vnf1048 configuration mismatch | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a510_3RowSeatUncalibrated` | page 8 | Left body controller: a510 3 row seat uncalibrated | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a511_3RowSeatPositionNonsensical` | page 8 | Left body controller: a511 3 row seat position nonsensical | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a512_3RowSeatAbsPosOffsetApplied` | page 8 | Left body controller: a512 3 row seat abs pos offset applied | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a513_3RowSeatObstacleDetected` | page 8 | Left body controller: a513 3 row seat obstacle detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a514_3RowSeatTempHigh` | page 8 | Left body controller: a514 3 row seat temp high | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a515_3RowSeatAbsPosSensorTransitionDbg` | page 8 | Left body controller: a515 3 row seat abs pos sensor transition dbg | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a516_3RowSeatStatsFromLastStateDbg` | page 8 | Left body controller: a516 3 row seat stats from last state dbg | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a517_3RowSeatRequestWhileUncalibrated` | page 8 | Left body controller: a517 3 row seat request while uncalibrated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a518_3RowSeatClashAvoidanceBlocked` | page 8 | Left body controller: a518 3 row seat clash avoidance blocked | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a519_3RowSeatOverfolded` | page 8 | Left body controller: a519 3 row seat overfolded | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a520_configMismatch` | page 8 | Left body controller: a520 config mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a521_seatHeatPadUnexpectedVoltage` | page 8 | Left body controller: a521 seat heat pad unexpected voltage | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a522_trailerLightUnexpectedVoltage` | page 8 | Left body controller: a522 trailer light unexpected voltage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a523_eFuseThresholdsIncorrect` | page 8 | Left body controller: a523 e fuse thresholds incorrect | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a525_LVBatterySWMisconfiguration` | page 8 | Left body controller: a525 LV battery SW misconfiguration | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a526_pcbaOverTemperature` | page 8 | Left body controller: a526 pcba over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a527_continuousFeedUnexpectedVoltage` | page 8 | Left body controller: a527 continuous feed unexpected voltage | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a528_unableToRunStuckOnTest` | page 8 | Left body controller: a528 unable to run stuck on test | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a536_trunkFoldFlatSwitchFault` | page 8 | Left body controller: a536 trunk fold flat switch fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a545_LVBatteryTypeUnknown` | page 9 | Left body controller: a545 LV battery type unknown | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a546_mirrorFoldTypeChanged` | page 9 | Left body controller: a546 mirror fold type changed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a550_ambientTempDelta` | page 9 | Left body controller: a550 ambient temp delta | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a551_interiorDoorRequestInhibited` | page 9 | Left body controller: a551 interior door request inhibited | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a554_RCM2_MIA` | page 9 | Left body controller: a554 RCM2 MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a555_steeringWheelHeaterCompromised` | page 9 | Left body controller: a555 steering wheel heater compromised | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a560_2RowSeatUncalibrated` | page 9 | Left body controller: a560 2 row seat uncalibrated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a561_2RowSeatPositionNonsensical` | page 9 | Left body controller: a561 2 row seat position nonsensical | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a562_2RowSeatAbsPosOffsetApplied` | page 9 | Left body controller: a562 2 row seat abs pos offset applied | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a563_2RowSeatObstacleDetected` | page 9 | Left body controller: a563 2 row seat obstacle detected | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a564_2RowSeatTempHigh` | page 9 | Left body controller: a564 2 row seat temp high | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a565_2RowSeatAbsPosSensorTransitionDbg` | page 9 | Left body controller: a565 2 row seat abs pos sensor transition dbg | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a566_2RowSeatStatsFromLastStateDbg` | page 9 | Left body controller: a566 2 row seat stats from last state dbg | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a567_2RowSeatRequestWhileUncalibrated` | page 9 | Left body controller: a567 2 row seat request while uncalibrated | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a568_2RowSeatClashAvoidanceBlocked` | page 9 | Left body controller: a568 2 row seat clash avoidance blocked | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a569_2RowSeatOverfolded` | page 9 | Left body controller: a569 2 row seat overfolded | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a570_seatHeatDisabledF` | page 9 | Left body controller: a570 seat heat disabled f | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a571_seatHeatDisabledRearL` | page 9 | Left body controller: a571 seat heat disabled rear l | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a572_seatHeatDisabledRearC` | page 9 | Left body controller: a572 seat heat disabled rear c | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a573_seatHeatDisabledRearR` | page 9 | Left body controller: a573 seat heat disabled rear r | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a574_2RowSeatStatsFromLastStateDbg2` | page 9 | Left body controller: a574 2 row seat stats from last state dbg2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a575_3RowSeatStatsFromLastStateDbg2` | page 9 | Left body controller: a575 3 row seat stats from last state dbg2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a576_liftgateStrutPositionMismatch` | page 9 | Left body controller: a576 liftgate strut position mismatch | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a577_bsiHardwareIssue` | page 9 | Left body controller: a577 bsi hardware issue | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a578_RGBLightFault` | page 9 | Left body controller: a578 RGB light fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a579_leftSteeringWheelCtrlTypeMismatch` | page 9 | Left body controller: a579 left steering wheel ctrl type mismatch | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a580_rightSteeringWheelCtrlTypeMismatch` | page 9 | Left body controller: a580 right steering wheel ctrl type mismatch | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a581_reverseLightFault` | page 9 | Left body controller: a581 reverse light fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a582_seat2RControllerTrip` | page 9 | Left body controller: a582 seat2 r controller trip | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a583_doorRemoteUnlatchedFront` | page 9 | Left body controller: a583 door remote unlatched front | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a584_doorRemoteUnlatchedRear` | page 9 | Left body controller: a584 door remote unlatched rear | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a585_doorRemoteUnlatchFailedFront` | page 9 | Left body controller: a585 door remote unlatch failed front | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a586_doorRemoteUnlatchFailedRear` | page 9 | Left body controller: a586 door remote unlatch failed rear | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a587_VCSEAT2L_MIA` | page 9 | Left body controller: a587 VCSEAT2 l MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a589_lipcCanFault` | page 9 | Left body controller: a589 lipc can fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a590_seatEncStallThighSupport` | page 9 | Left body controller: a590 seat enc stall thigh support | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a591_seatCurrUnderThighSupport` | page 9 | Left body controller: a591 seat curr under thigh support | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a592_seatUncalThighSupport` | page 9 | Left body controller: a592 seat uncal thigh support | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a593_seatEncOverThighSupport` | page 9 | Left body controller: a593 seat enc over thigh support | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a594_seatThighSupportStallDebug` | page 9 | Left body controller: a594 seat thigh support stall debug | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a595_seatThighSupportHCEncStlDbg` | page 9 | Left body controller: a595 seat thigh support HC enc stl dbg | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a596_frontDoorLatchUnexpectedVoltage` | page 9 | Left body controller: a596 front door latch unexpected voltage | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a597_rearDoorLatchUnexpectedVoltage` | page 9 | Left body controller: a597 rear door latch unexpected voltage | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a599_LVBatteryTypeUnsupported` | page 9 | Left body controller: a599 LV battery type unsupported | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_a601_wakeToOpenDoorDbg` | page 10 | Left body controller: a601 wake to open door dbg | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a605_CANMsgMACVerificationKeyMismatch` | page 10 | Left body controller: a605 CAN msg MAC verification key mismatch | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_a617_APP_MIA` | page 10 | Left body controller: a617 APP MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCLEFT_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (26 signals), page 1 (45 signals), page 2 (47 signals), page 3 (56 signals), page 4 (55 signals), page 5 (58 signals), page 6 (53 signals), page 7 (48 signals), page 8 (34 signals), page 9 (44 signals), page 10 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
