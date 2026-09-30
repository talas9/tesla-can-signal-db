---
layout: default
title: "VCSEAT2R_alertMatrix (0x3F0) — VCSEAT2R ECU, Tesla Model 3 2026.26.6.5 ETH"
description: "VCSEAT2R ECU message: alert matrix. Ethernet-side message VCSEAT2R_alertMatrix of VCSEAT2R ECU for Tesla Model 3 firmware 2026.26.6.5, 129 signals (VCSEAT2R_matrixIndex, VCSEAT2R_a001_WatchdogReset, VCSEAT2R_a002_PowerLossReset, VCSEAT2R_a003_SWAssertion and 125 more). Bit layout, scaling, units and value tables."
---

# VCSEAT2R_alertMatrix (0x3F0) — VCSEAT2R ECU, Tesla Model 3 2026.26.6.5 ETH

VCSEAT2R ECU message: alert matrix. This page documents the 129 signals of VCSEAT2R_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEAT2R_alertMatrix` |
| Ethernet-side id | 0x3F0 (1008) |
| ECU | [VCSEAT2R ECU](../../vcseat2r.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEAT2R |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 129 |

## Signals of VCSEAT2R_alertMatrix

Tesla Model 3 CAN bus signals in `VCSEAT2R_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEAT2R_matrixIndex` | selector | VCSEAT2R ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9` | plausible |
| `VCSEAT2R_a001_WatchdogReset` | page 0 | VCSEAT2R ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a002_PowerLossReset` | page 0 | VCSEAT2R ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a003_SWAssertion` | page 0 | VCSEAT2R ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a005_CANTXError` | page 0 | VCSEAT2R ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a006_CANTX_cyclicError` | page 0 | VCSEAT2R ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a010_ExtSupplyVoltError` | page 0 | VCSEAT2R ECU: a010 ext supply volt error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a012_CPUReset` | page 0 | VCSEAT2R ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a013_AlertManagerFault` | page 0 | VCSEAT2R ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a015_NVMMError` | page 0 | VCSEAT2R ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a016_NVMMRecordError` | page 0 | VCSEAT2R ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a021_TaskSchedulerError` | page 0 | VCSEAT2R ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a022_TaskInitError` | page 0 | VCSEAT2R ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a029_CoreDump` | page 0 | VCSEAT2R ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a030_ECULogUploadRequest` | page 0 | VCSEAT2R ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a031_UDSActive` | page 0 | VCSEAT2R ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a041_HighCPULoad` | page 0 | VCSEAT2R ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a042_HighStackUsage` | page 0 | VCSEAT2R ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a043_Task1msError` | page 0 | VCSEAT2R ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a044_Task10msError` | page 0 | VCSEAT2R ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a045_Task100msError` | page 0 | VCSEAT2R ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a046_Task1000msError` | page 0 | VCSEAT2R ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a057_HVP_MIA` | page 0 | VCSEAT2R ECU: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a058_inputRHighSyncDebug` | page 0 | VCSEAT2R ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a059_inputResistanceHigh` | page 0 | VCSEAT2R ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a060_engineeringBuild` | page 0 | VCSEAT2R ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a061_XCPConnected` | page 1 | VCSEAT2R ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a062_XCPWasConnected` | page 1 | VCSEAT2R ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a063_SwitchFault` | page 1 | VCSEAT2R ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a064_busSleepReqTimeout` | page 1 | VCSEAT2R ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a082_VCRIGHT_IPC_MIA` | page 1 | VCSEAT2R ECU: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a083_VCLEFT_IPC_MIA` | page 1 | VCSEAT2R ECU: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a084_TPMS_MIA` | page 1 | VCSEAT2R ECU: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a085_CCCM_MIA` | page 1 | VCSEAT2R ECU: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a086_VCBATT_MIA` | page 1 | VCSEAT2R ECU: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a087_DIREL_MIA` | page 1 | VCSEAT2R ECU: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a088_DIRER_MIA` | page 1 | VCSEAT2R ECU: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a089_IBST_MIA` | page 1 | VCSEAT2R ECU: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a090_APS_MIA` | page 1 | VCSEAT2R ECU: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a091_CMPD_MIA` | page 1 | VCSEAT2R ECU: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a092_VCSEATD_MIA` | page 1 | VCSEAT2R ECU: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a093_VCSEATP_MIA` | page 1 | VCSEAT2R ECU: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a094_EPAS3P_MIA` | page 1 | VCSEAT2R ECU: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a095_CHG_MIA` | page 1 | VCSEAT2R ECU: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a096_OCS1P_MIA` | page 1 | VCSEAT2R ECU: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a097_CMP_MIA` | page 1 | VCSEAT2R ECU: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a098_DIR_MIA` | page 1 | VCSEAT2R ECU: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a099_PARK_MIA` | page 1 | VCSEAT2R ECU: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a100_CANbus_MIA` | page 1 | VCSEAT2R ECU: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a101_PM_MIA` | page 1 | VCSEAT2R ECU: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a102_PTC_MIA` | page 1 | VCSEAT2R ECU: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a103_CP_MIA` | page 1 | VCSEAT2R ECU: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a104_DAS_MIA` | page 1 | VCSEAT2R ECU: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a105_TAS_MIA` | page 1 | VCSEAT2R ECU: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a106_PCS_MIA` | page 1 | VCSEAT2R ECU: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a107_BMS_MIA` | page 1 | VCSEAT2R ECU: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a108_DIF_MIA` | page 1 | VCSEAT2R ECU: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a109_RCM_MIA` | page 1 | VCSEAT2R ECU: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a110_GTW_MIA` | page 1 | VCSEAT2R ECU: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a111_EPBR_MIA` | page 1 | VCSEAT2R ECU: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a112_EPBL_MIA` | page 1 | VCSEAT2R ECU: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a113_UI_MIA` | page 1 | VCSEAT2R ECU: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a114_ESP_MIA` | page 1 | VCSEAT2R ECU: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a115_VCSEC_MIA` | page 1 | VCSEAT2R ECU: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a116_VCRIGHT_MIA` | page 1 | VCSEAT2R ECU: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a117_VCLEFT_MIA` | page 1 | VCSEAT2R ECU: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a118_VCFRONT_MIA` | page 1 | VCSEAT2R ECU: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a119_SCCM_MIA` | page 1 | VCSEAT2R ECU: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a120_DI_DRIVE_MIA` | page 1 | VCSEAT2R ECU: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a190_seatChoreographyIsBlockedByFrontSeat` | page 3 | VCSEAT2R ECU: a190 seat choreography is blocked by front seat | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a191_seatChoreographyIsBlockedBySecondSeat` | page 3 | VCSEAT2R ECU: a191 seat choreography is blocked by second seat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a200_motorPhantomEncoder` | page 3 | VCSEAT2R ECU: a200 motor phantom encoder | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a201_motorDutyEncDisabl` | page 3 | VCSEAT2R ECU: a201 motor duty enc disabl | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a210_armrestEncStall` | page 3 | VCSEAT2R ECU: a210 armrest enc stall | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a211_armrestCurrUnder` | page 3 | VCSEAT2R ECU: a211 armrest curr under | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a212_armrestUncal` | page 3 | VCSEAT2R ECU: a212 armrest uncal | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a213_armrestEncOver` | page 3 | VCSEAT2R ECU: a213 armrest enc over | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a214_armrestStallDebug` | page 3 | VCSEAT2R ECU: a214 armrest stall debug | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a215_armrestHCEncStlDbg` | page 3 | VCSEAT2R ECU: a215 armrest HC enc stl dbg | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a218_motorDriverFault` | page 3 | VCSEAT2R ECU: a218 motor driver fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a219_motorCurrentDropout` | page 3 | VCSEAT2R ECU: a219 motor current dropout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a224_seatEncStallTrack` | page 3 | VCSEAT2R ECU: a224 seat enc stall track | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a225_seatEncStallBack` | page 3 | VCSEAT2R ECU: a225 seat enc stall back | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a228_seatEncOverTrack` | page 3 | VCSEAT2R ECU: a228 seat enc over track | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a229_seatEncOverBack` | page 3 | VCSEAT2R ECU: a229 seat enc over back | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a232_seatCurrUnderTrack` | page 3 | VCSEAT2R ECU: a232 seat curr under track | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a233_seatCurrUnderBack` | page 3 | VCSEAT2R ECU: a233 seat curr under back | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a234_seatTrackStatsFromLastStateDbg` | page 3 | VCSEAT2R ECU: a234 seat track stats from last state dbg | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a235_seatTrackStatsFromLastStateDbg2` | page 3 | VCSEAT2R ECU: a235 seat track stats from last state dbg2 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a236_seatArmrestStatsFromLastStateDbg` | page 3 | VCSEAT2R ECU: a236 seat armrest stats from last state dbg | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a237_seatArmrestStatsFromLastStateDbg2` | page 3 | VCSEAT2R ECU: a237 seat armrest stats from last state dbg2 | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a238_seatArmrestInhibitedByBackrest` | page 3 | VCSEAT2R ECU: a238 seat armrest inhibited by backrest | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a239_seatHeatIRow2` | page 3 | VCSEAT2R ECU: a239 seat heat i row2 | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a240_seatHeatShortRow2` | page 3 | VCSEAT2R ECU: a240 seat heat short row2 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a241_seatArmrestHistoryScore` | page 4 | VCSEAT2R ECU: a241 seat armrest history score | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a242_seatHeatTmpRow2` | page 4 | VCSEAT2R ECU: a242 seat heat tmp row2 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a243_seatArmrestHistoryScoreDbg` | page 4 | VCSEAT2R ECU: a243 seat armrest history score dbg | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a244_seatArmrestSpeedTableReferenceStatus` | page 4 | VCSEAT2R ECU: a244 seat armrest speed table reference status | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a245_seatArmrestEcuLogStatus` | page 4 | VCSEAT2R ECU: a245 seat armrest ecu log status | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a251_seatUncalTrack` | page 4 | VCSEAT2R ECU: a251 seat uncal track | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a252_seatUncalBack` | page 4 | VCSEAT2R ECU: a252 seat uncal back | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a260_seatTrackObstacleDetected` | page 4 | VCSEAT2R ECU: a260 seat track obstacle detected | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a261_seatArmrestObstacleDetected` | page 4 | VCSEAT2R ECU: a261 seat armrest obstacle detected | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a263_seatTrackStallDebug` | page 4 | VCSEAT2R ECU: a263 seat track stall debug | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a264_seatBackStallDebug` | page 4 | VCSEAT2R ECU: a264 seat back stall debug | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a267_seatTrackHCEncStl` | page 4 | VCSEAT2R ECU: a267 seat track HC enc stl | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a268_seatBackHCEncStlDbg` | page 4 | VCSEAT2R ECU: a268 seat back HC enc stl dbg | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a270_seatUncalibrated` | page 4 | VCSEAT2R ECU: a270 seat uncalibrated | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a271_seatPositionNonsensical` | page 4 | VCSEAT2R ECU: a271 seat position nonsensical | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a272_seatAbsPosOffsetApplied` | page 4 | VCSEAT2R ECU: a272 seat abs pos offset applied | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a273_seatObstacleDetected` | page 4 | VCSEAT2R ECU: a273 seat obstacle detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a274_seatTempHigh` | page 4 | VCSEAT2R ECU: a274 seat temp high | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a275_seatAbsPosSensorTransitionDbg` | page 4 | VCSEAT2R ECU: a275 seat abs pos sensor transition dbg | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a276_seatStatsFromLastStateDbg` | page 4 | VCSEAT2R ECU: a276 seat stats from last state dbg | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a277_seatRequestWhileUncalibrated` | page 4 | VCSEAT2R ECU: a277 seat request while uncalibrated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a278_seatClashAvoidanceBlocked` | page 4 | VCSEAT2R ECU: a278 seat clash avoidance blocked | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a279_seatOverfolded` | page 4 | VCSEAT2R ECU: a279 seat overfolded | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a280_seatStatsFromLastStateDbg2` | page 4 | VCSEAT2R ECU: a280 seat stats from last state dbg2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a290_occupancyFaultRow2` | page 4 | VCSEAT2R ECU: a290 occupancy fault row2 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a291_buckleFaultedRow2` | page 4 | VCSEAT2R ECU: a291 buckle faulted row2 | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a426_seatAbuseMotorWarn` | page 7 | VCSEAT2R ECU: a426 seat abuse motor warn | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a427_seatAbuseMotorStop` | page 7 | VCSEAT2R ECU: a427 seat abuse motor stop | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a428_seatAbuseBufferWarn` | page 7 | VCSEAT2R ECU: a428 seat abuse buffer warn | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a429_seatAbuseBufferFull` | page 7 | VCSEAT2R ECU: a429 seat abuse buffer full | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a444_drv8703Fault` | page 7 | VCSEAT2R ECU: a444 drv8703 fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a445_drv8703SpiFaultDBG` | page 7 | VCSEAT2R ECU: a445 drv8703 spi fault DBG | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a526_pcbaOverTemperature` | page 8 | VCSEAT2R ECU: a526 pcba over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a550_ambientTempDelta` | page 9 | VCSEAT2R ECU: a550 ambient temp delta | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEAT2R_a571_seatHeatDisabledRear` | page 9 | VCSEAT2R ECU: a571 seat heat disabled rear | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCSEAT2R_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (25 signals), page 1 (43 signals), page 3 (25 signals), page 4 (26 signals), page 7 (6 signals), page 8 (1 signals), page 9 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All VCSEAT2R ECU messages (VCSEAT2R)](../../vcseat2r.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
