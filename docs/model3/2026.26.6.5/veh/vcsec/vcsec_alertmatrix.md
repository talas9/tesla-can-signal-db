---
layout: default
title: "VCSEC_alertMatrix (0x3F9) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: alert matrix. Tesla Model 3 CAN bus message VCSEC_alertMatrix (0x3F9) of Vehicle security controller, firmware 2026.26.6.5, 314 signals (VCSEC_matrixIndex, VCSEC_a001_WatchdogReset, VCSEC_a002_PowerLossReset, VCSEC_a003_SWAssertion and 310 more). Bit layout, scaling, units and value tables."
---

# VCSEC_alertMatrix (0x3F9) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN

Vehicle security controller message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 314 signals of VCSEC_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_alertMatrix` |
| CAN id | 0x3F9 (1017) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 314 |

## Signals of VCSEC_alertMatrix

Tesla Model 3 CAN bus signals in `VCSEC_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_matrixIndex` | selector | Vehicle security controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8` | validated |
| `VCSEC_a001_WatchdogReset` | page 0 | Vehicle security controller: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a002_PowerLossReset` | page 0 | Vehicle security controller: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a003_SWAssertion` | page 0 | Vehicle security controller: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a005_CANTXError` | page 0 | Vehicle security controller: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a006_CANTX_cyclicError` | page 0 | Vehicle security controller: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a010_ExtSupplyVoltError` | page 0 | Vehicle security controller: a010 ext supply volt error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a012_CPUReset` | page 0 | Vehicle security controller: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a013_AlertManagerFault` | page 0 | Vehicle security controller: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a015_NVMMError` | page 0 | Vehicle security controller: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a016_NVMMRecordError` | page 0 | Vehicle security controller: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a017_NVMMStatusDbg` | page 0 | Vehicle security controller: a017 NVMM status dbg | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a021_TaskSchedulerError` | page 0 | Vehicle security controller: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a022_TaskInitError` | page 0 | Vehicle security controller: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a029_CoreDump` | page 0 | Vehicle security controller: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a030_ECULogUploadRequest` | page 0 | Vehicle security controller: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a031_UDSActive` | page 0 | Vehicle security controller: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a041_HighCPULoad` | page 0 | Vehicle security controller: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a042_HighStackUsage` | page 0 | Vehicle security controller: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a043_Task1msError` | page 0 | Vehicle security controller: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a044_Task10msError` | page 0 | Vehicle security controller: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a045_Task100msError` | page 0 | Vehicle security controller: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a046_Task1000msError` | page 0 | Vehicle security controller: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a057_HVP_MIA` | page 0 | Vehicle security controller: a057 HVP MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a058_inputRHighSyncDebug` | page 0 | Vehicle security controller: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a059_inputResistanceHigh` | page 0 | Vehicle security controller: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a060_engineeringBuild` | page 0 | Vehicle security controller: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a061_XCPConnected` | page 1 | Vehicle security controller: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a062_XCPWasConnected` | page 1 | Vehicle security controller: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a063_SwitchFault` | page 1 | Vehicle security controller: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a064_busSleepReqTimeout` | page 1 | Vehicle security controller: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a082_VCRIGHT_IPC_MIA` | page 1 | Vehicle security controller: a082 VCRIGHT IPC MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a083_VCLEFT_IPC_MIA` | page 1 | Vehicle security controller: a083 VCLEFT IPC MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a084_TPMS_MIA` | page 1 | Vehicle security controller: a084 TPMS MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a085_CCCM_MIA` | page 1 | Vehicle security controller: a085 CCCM MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a086_VCBATT_MIA` | page 1 | Vehicle security controller: a086 VCBATT MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a087_DIREL_MIA` | page 1 | Vehicle security controller: a087 DIREL MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a088_DIRER_MIA` | page 1 | Vehicle security controller: a088 DIRER MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a089_IBST_MIA` | page 1 | Vehicle security controller: a089 IBST MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a090_APS_MIA` | page 1 | Vehicle security controller: a090 APS MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a091_CMPD_MIA` | page 1 | Vehicle security controller: a091 CMPD MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a092_VCSEATD_MIA` | page 1 | Vehicle security controller: a092 VCSEATD MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a093_VCSEATP_MIA` | page 1 | Vehicle security controller: a093 VCSEATP MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a094_EPAS3P_MIA` | page 1 | Vehicle security controller: a094 EPAS3 p MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a095_CHG_MIA` | page 1 | Vehicle security controller: a095 CHG MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a096_OCS1P_MIA` | page 1 | Vehicle security controller: a096 OCS1 p MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a097_CMP_MIA` | page 1 | Vehicle security controller: a097 CMP MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a098_DIR_MIA` | page 1 | Vehicle security controller: a098 DIR MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a099_PARK_MIA` | page 1 | Vehicle security controller: a099 PARK MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a100_CANbus_MIA` | page 1 | Vehicle security controller: a100 CA nbus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a101_PM_MIA` | page 1 | Vehicle security controller: a101 PM MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a102_PTC_MIA` | page 1 | Vehicle security controller: a102 PTC MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a103_CP_MIA` | page 1 | Vehicle security controller: a103 CP MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a104_DAS_MIA` | page 1 | Vehicle security controller: a104 DAS MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a105_TAS_MIA` | page 1 | Vehicle security controller: a105 TAS MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a106_PCS_MIA` | page 1 | Vehicle security controller: a106 PCS MIA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a107_BMS_MIA` | page 1 | Vehicle security controller: a107 BMS MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a108_DIF_MIA` | page 1 | Vehicle security controller: a108 DIF MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a109_RCM_MIA` | page 1 | Vehicle security controller: a109 RCM MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a110_GTW_MIA` | page 1 | Vehicle security controller: a110 GTW MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a111_EPBR_MIA` | page 1 | Vehicle security controller: a111 EPBR MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a112_EPBL_MIA` | page 1 | Vehicle security controller: a112 EPBL MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a113_UI_MIA` | page 1 | Vehicle security controller: a113 UI MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a114_ESP_MIA` | page 1 | Vehicle security controller: a114 ESP MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a115_VCSEC_MIA` | page 1 | Vehicle security controller: a115 VCSEC MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a116_VCRIGHT_MIA` | page 1 | Vehicle security controller: a116 VCRIGHT MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a117_VCLEFT_MIA` | page 1 | Vehicle security controller: a117 VCLEFT MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a118_VCFRONT_MIA` | page 1 | Vehicle security controller: a118 VCFRONT MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a119_SCCM_MIA` | page 1 | Vehicle security controller: a119 SCCM MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a120_DI_DRIVE_MIA` | page 1 | Vehicle security controller: a120 DI DRIVE MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a121_ICR_MIA` | page 2 | Vehicle security controller: a121 ICR MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a133_alarmTriggered` | page 2 | Vehicle security controller: a133 alarm triggered | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a134_noVINLoaded` | page 2 | Vehicle security controller: a134 no VIN loaded | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a135_centerEndpointBusy` | page 2 | Vehicle security controller: a135 center endpoint busy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a136_leftEndpointBusy` | page 2 | Vehicle security controller: a136 left endpoint busy | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a137_rightEndpointBusy` | page 2 | Vehicle security controller: a137 right endpoint busy | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a138_rearEndpointBusy` | page 2 | Vehicle security controller: a138 rear endpoint busy | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a140_nfcAuthentication` | page 2 | Vehicle security controller: a140 nfc authentication | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a141_tooFewKeysOnWhitelist` | page 2 | Vehicle security controller: a141 too few keys on whitelist | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a142_bleGattAlertC` | page 2 | Vehicle security controller: a142 ble gatt alert c | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a143_bleGattAlertL` | page 2 | Vehicle security controller: a143 ble gatt alert l | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a144_bleGattAlertR` | page 2 | Vehicle security controller: a144 ble gatt alert r | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a145_bleGattAlertRe` | page 2 | Vehicle security controller: a145 ble gatt alert re | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a147_protobufRXTimeout` | page 2 | Vehicle security controller: a147 protobuf RX timeout | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a148_keyWhitelistFull` | page 2 | Vehicle security controller: a148 key whitelist full | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a149_attrsWentMissingL` | page 2 | Vehicle security controller: a149 attrs went missing l | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a150_attrsWentMissingR` | page 2 | Vehicle security controller: a150 attrs went missing r | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a151_attrsWentMissingRe` | page 2 | Vehicle security controller: a151 attrs went missing re | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a153_srvcCmdTimeoutC` | page 2 | Vehicle security controller: a153 srvc cmd timeout c | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a154_srvcCmdTimeoutL` | page 2 | Vehicle security controller: a154 srvc cmd timeout l | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a155_srvcCmdTimeoutR` | page 2 | Vehicle security controller: a155 srvc cmd timeout r | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a156_srvcCmdTimeoutRe` | page 2 | Vehicle security controller: a156 srvc cmd timeout re | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a158_hciDebugC` | page 2 | Vehicle security controller: a158 hci debug c | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a159_hciDebugL` | page 2 | Vehicle security controller: a159 hci debug l | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a161_hciDebugR` | page 2 | Vehicle security controller: a161 hci debug r | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a162_hciDebugRe` | page 2 | Vehicle security controller: a162 hci debug re | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a164_attrsWentMissingC` | page 2 | Vehicle security controller: a164 attrs went missing c | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a165_ephemeralKeyGenerated` | page 2 | Vehicle security controller: a165 ephemeral key generated | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a166_BLECenterPowerCycled` | page 2 | Vehicle security controller: a166 BLE center power cycled | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a167_BLECenterSoftReset` | page 2 | Vehicle security controller: a167 BLE center soft reset | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a168_BLELeftSoftReset` | page 2 | Vehicle security controller: a168 BLE left soft reset | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a169_BLERightSoftReset` | page 2 | Vehicle security controller: a169 BLE right soft reset | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a170_BLERearSoftReset` | page 2 | Vehicle security controller: a170 BLE rear soft reset | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a172_BLEUnexpectedResetC` | page 2 | Vehicle security controller: a172 BLE unexpected reset c | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a173_BLEUnexpectedResetL` | page 2 | Vehicle security controller: a173 BLE unexpected reset l | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a174_BLEUnexpectedResetRi` | page 2 | Vehicle security controller: a174 BLE unexpected reset ri | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a175_BLEUnexpectedResetRe` | page 2 | Vehicle security controller: a175 BLE unexpected reset re | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a177_whitelistAddedKey` | page 2 | Vehicle security controller: a177 whitelist added key | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a178_whitelistRemovedKey` | page 2 | Vehicle security controller: a178 whitelist removed key | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a179_InfotainmentNotPaired` | page 2 | Vehicle security controller: a179 infotainment not paired | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a180_wlistRemovedPermission` | page 2 | Vehicle security controller: a180 wlist removed permission | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a181_signedMessageFault` | page 3 | Vehicle security controller: a181 signed message fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a182_cryptoHighStackUsage` | page 3 | Vehicle security controller: a182 crypto high stack usage | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a183_centerEndpointRFMia` | page 3 | Vehicle security controller: a183 center endpoint RF mia | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a184_driverEndpointRFMia` | page 3 | Vehicle security controller: a184 driver endpoint RF mia | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a185_passengerEndpointRFMia` | page 3 | Vehicle security controller: a185 passenger endpoint RF mia | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a186_rearEndpointRFMia` | page 3 | Vehicle security controller: a186 rear endpoint RF mia | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a187_badConnectionDropped` | page 3 | Vehicle security controller: a187 bad connection dropped | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a188_protobufDecodeError` | page 3 | Vehicle security controller: a188 protobuf decode error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a189_protoExpLengthTooLarge` | page 3 | Vehicle security controller: a189 proto exp length too large | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a190_protoTooManyBytes` | page 3 | Vehicle security controller: a190 proto too many bytes | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a191_macIDWlistingFailedC` | page 3 | Vehicle security controller: a191 mac ID wlisting failed c | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a192_macIDWlistingFailedL` | page 3 | Vehicle security controller: a192 mac ID wlisting failed l | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a193_macIDWlistingFailedRi` | page 3 | Vehicle security controller: a193 mac ID wlisting failed ri | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a194_macIDWlistingFailedRe` | page 3 | Vehicle security controller: a194 mac ID wlisting failed re | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a195_keyMissingInDrive` | page 3 | Vehicle security controller: a195 key missing in drive | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a196_protobufTXTimeout` | page 3 | Vehicle security controller: a196 protobuf TX timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a197_indicationFault` | page 3 | Vehicle security controller: a197 indication fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a198_BPillarNFCReaderMIA` | page 3 | Vehicle security controller: a198 b pillar NFC reader MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a199_CenterNFCReaderMIA` | page 3 | Vehicle security controller: a199 center NFC reader MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a200_centerEndpointLostComm` | page 3 | Vehicle security controller: a200 center endpoint lost comm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a201_leftEndpointLostComm` | page 3 | Vehicle security controller: a201 left endpoint lost comm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_a202_rightEndpointLostComm` | page 3 | Vehicle security controller: a202 right endpoint lost comm | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_a203_rearEndpointLostComm` | page 3 | Vehicle security controller: a203 rear endpoint lost comm | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_a204_SharedSecretsWritten` | page 3 | Vehicle security controller: a204 shared secrets written | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a205_MTUUpdateNotConfirmed` | page 3 | Vehicle security controller: a205 MTU update not confirmed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a206_BLELeftAssertFailure` | page 3 | Vehicle security controller: a206 BLE left assert failure | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a207_BLERightAssertFailure` | page 3 | Vehicle security controller: a207 BLE right assert failure | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a208_BLERearAssertFailure` | page 3 | Vehicle security controller: a208 BLE rear assert failure | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a209_BLECenterAssertFailure` | page 3 | Vehicle security controller: a209 BLE center assert failure | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a210_keyDeviceBatteryLow` | page 3 | Vehicle security controller: a210 key device battery low | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a211_handlePullWithoutAuth` | page 3 | Vehicle security controller: a211 handle pull without auth | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a212_snifferRSSIMIA` | page 3 | Vehicle security controller: a212 sniffer RSSIMIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a213_gattTimeoutWithExptdCount` | page 3 | Vehicle security controller: a213 gatt timeout with exptd count | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a214_gattServFalseWaitToBoot` | page 3 | Vehicle security controller: a214 gatt serv false wait to boot | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a215_TPMSUnexpectedDisconnectSensor0` | page 3 | Vehicle security controller: a215 TPMS unexpected disconnect sensor0 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a216_TPMSUnexpectedDisconnectSensor1` | page 3 | Vehicle security controller: a216 TPMS unexpected disconnect sensor1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a217_TPMSUnexpectedDisconnectSensor2` | page 3 | Vehicle security controller: a217 TPMS unexpected disconnect sensor2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a218_TPMSUnexpectedDisconnectSensor3` | page 3 | Vehicle security controller: a218 TPMS unexpected disconnect sensor3 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a219_TPMSSensorPairingRemoved` | page 3 | Vehicle security controller: a219 TPMS sensor pairing removed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a220_TPMSSensorPairingNotCompleted` | page 3 | Vehicle security controller: a220 TPMS sensor pairing not completed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a221_TPMSSoftWarning` | page 3 | Vehicle security controller: a221 TPMS soft warning | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a222_TPMSSystemMalfunction` | page 3 | Vehicle security controller: a222 TPMS system malfunction | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a223_TPMSSensorConnectionCycling0` | page 3 | Vehicle security controller: a223 TPMS sensor connection cycling0 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a224_TPMSSensorConnectionCycling1` | page 3 | Vehicle security controller: a224 TPMS sensor connection cycling1 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a225_TPMSSensorConnectionCycling2` | page 3 | Vehicle security controller: a225 TPMS sensor connection cycling2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a226_TPMSSensorConnectionCycling3` | page 3 | Vehicle security controller: a226 TPMS sensor connection cycling3 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a227_connectionWithoutLinkEvent` | page 3 | Vehicle security controller: a227 connection without link event | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a228_TPMSHardWarning` | page 3 | Vehicle security controller: a228 TPMS hard warning | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a235_presentWithoutHandlePull` | page 3 | Vehicle security controller: a235 present without handle pull | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a236_keyIdentificationMaxAttemptReached` | page 3 | Vehicle security controller: a236 key identification max attempt reached | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a237_keyNotReadyToReceiveIDRequests` | page 3 | Vehicle security controller: a237 key not ready to receive ID requests | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a238_TPMSLocationsUpdated` | page 3 | Vehicle security controller: a238 TPMS locations updated | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a239_TPMSIdleConnection` | page 3 | Vehicle security controller: a239 TPMS idle connection | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a240_noKeysPaired` | page 3 | Vehicle security controller: a240 no keys paired | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a241_TPMSUpdateStartedSensor0` | page 4 | Vehicle security controller: a241 TPMS update started sensor0 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a242_TPMSUpdateStartedSensor1` | page 4 | Vehicle security controller: a242 TPMS update started sensor1 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a243_TPMSUpdateStartedSensor2` | page 4 | Vehicle security controller: a243 TPMS update started sensor2 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a244_TPMSUpdateStartedSensor3` | page 4 | Vehicle security controller: a244 TPMS update started sensor3 | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a245_TPMSUpdateInterruptedSensor0` | page 4 | Vehicle security controller: a245 TPMS update interrupted sensor0 | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a246_TPMSUpdateInterruptedSensor1` | page 4 | Vehicle security controller: a246 TPMS update interrupted sensor1 | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a247_TPMSUpdateInterruptedSensor2` | page 4 | Vehicle security controller: a247 TPMS update interrupted sensor2 | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a248_TPMSUpdateInterruptedSensor3` | page 4 | Vehicle security controller: a248 TPMS update interrupted sensor3 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a249_TPMSUpdateCompleteSensor0` | page 4 | Vehicle security controller: a249 TPMS update complete sensor0 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a250_TPMSUpdateCompleteSensor1` | page 4 | Vehicle security controller: a250 TPMS update complete sensor1 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a251_TPMSUpdateCompleteSensor2` | page 4 | Vehicle security controller: a251 TPMS update complete sensor2 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a252_TPMSUpdateCompleteSensor3` | page 4 | Vehicle security controller: a252 TPMS update complete sensor3 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a254_whitelistUpdatedKey` | page 4 | Vehicle security controller: a254 whitelist updated key | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a255_wlistUpdatedPermission` | page 4 | Vehicle security controller: a255 wlist updated permission | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a256_whitelistOperationFail` | page 4 | Vehicle security controller: a256 whitelist operation fail | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a257_connectedKeyIsExpiring` | page 4 | Vehicle security controller: a257 connected key is expiring | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a258_keyIsExpiring` | page 4 | Vehicle security controller: a258 key is expiring | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a260_prsntPhoneKeyDisconnected` | page 4 | Vehicle security controller: a260 prsnt phone key disconnected | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a261_TPMSFactoryLearnActive` | page 4 | Vehicle security controller: a261 TPMS factory learn active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a262_flowControlBackedUp` | page 4 | Vehicle security controller: a262 flow control backed up | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a263_dispatchCouldNotBeCompleted` | page 4 | Vehicle security controller: a263 dispatch could not be completed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a264_noOnePopulatedMessage` | page 4 | Vehicle security controller: a264 no one populated message | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a265_tooManyPopulatedMessage` | page 4 | Vehicle security controller: a265 too many populated message | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a266_TPMSSoftWarningFrontLeft` | page 4 | Vehicle security controller: a266 TPMS soft warning front left | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a267_TPMSSoftWarningFrontRight` | page 4 | Vehicle security controller: a267 TPMS soft warning front right | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a268_TPMSSoftWarningRearLeft` | page 4 | Vehicle security controller: a268 TPMS soft warning rear left | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a269_TPMSSoftWarningRearRight` | page 4 | Vehicle security controller: a269 TPMS soft warning rear right | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a270_TPMSHardWarningFrontLeft` | page 4 | Vehicle security controller: a270 TPMS hard warning front left | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a271_TPMSHardWarningFrontRight` | page 4 | Vehicle security controller: a271 TPMS hard warning front right | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a272_TPMSHardWarningRearLeft` | page 4 | Vehicle security controller: a272 TPMS hard warning rear left | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a273_TPMSHardWarningRearRight` | page 4 | Vehicle security controller: a273 TPMS hard warning rear right | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a274_handlePullWithoutAuth2` | page 4 | Vehicle security controller: a274 handle pull without auth2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a275_childSeatNotConnectedAtStartOfDrive` | page 4 | Vehicle security controller: a275 child seat not connected at start of drive | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a276_childSeatNotConnectedAtEndOfDrive` | page 4 | Vehicle security controller: a276 child seat not connected at end of drive | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a277_childSeatBatteryIsLow` | page 4 | Vehicle security controller: a277 child seat battery is low | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a280_TPMSLowBattery0` | page 4 | Vehicle security controller: a280 TPMS low battery0 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a281_TPMSLowBattery1` | page 4 | Vehicle security controller: a281 TPMS low battery1 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a282_TPMSLowBattery2` | page 4 | Vehicle security controller: a282 TPMS low battery2 | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a283_TPMSLowBattery3` | page 4 | Vehicle security controller: a283 TPMS low battery3 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a300_scheduleItKeyAdded` | page 4 | Vehicle security controller: a300 schedule it key added | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a301_imposterDetected` | page 5 | Vehicle security controller: a301 imposter detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a302_unfused` | page 5 | Vehicle security controller: a302 unfused | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a303_KeyfobUpdateInterrupted` | page 5 | Vehicle security controller: a303 keyfob update interrupted | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a304_KeyfobUpdateComplete` | page 5 | Vehicle security controller: a304 keyfob update complete | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a305_ATTFlowControlViolatedC` | page 5 | Vehicle security controller: a305 ATT flow control violated c | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a306_KeyfobAdvReceivedWhileConnected` | page 5 | Vehicle security controller: a306 keyfob adv received while connected | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a307_ATTTimeout` | page 5 | Vehicle security controller: a307 ATT timeout | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a308_NonConnectableAdvReceived` | page 5 | Vehicle security controller: a308 non connectable adv received | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a309_serviceKeyConditionsNotMet` | page 5 | Vehicle security controller: a309 service key conditions not met | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a310_chargePortFilterFalsePositive` | page 5 | Vehicle security controller: a310 charge port filter false positive | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a311_moreThanThreeKeysPresent` | page 5 | Vehicle security controller: a311 more than three keys present | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a312_unexpectedBLEDisconnect` | page 5 | Vehicle security controller: a312 unexpected BLE disconnect | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a315_bleBondingEvent` | page 5 | Vehicle security controller: a315 ble bonding event | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a316_ltkRequestRejected` | page 5 | Vehicle security controller: a316 ltk request rejected | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a401_rearLeftEndpointLostComm` | page 6 | Vehicle security controller: a401 rear left endpoint lost comm | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a402_rearRightEndpointLostComm` | page 6 | Vehicle security controller: a402 rear right endpoint lost comm | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a404_NFCCradleEndpointLostComm` | page 6 | Vehicle security controller: a404 NFC cradle endpoint lost comm | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a406_hciDebugRL` | page 6 | Vehicle security controller: a406 hci debug RL | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a407_hciDebugRR` | page 6 | Vehicle security controller: a407 hci debug RR | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a408_hciDebugNFCC` | page 6 | Vehicle security controller: a408 hci debug NFCC | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a411_leftRearEndpointBusy` | page 6 | Vehicle security controller: a411 left rear endpoint busy | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a412_rightRearEndpointBusy` | page 6 | Vehicle security controller: a412 right rear endpoint busy | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a413_NFCCradleEndpointBusy` | page 6 | Vehicle security controller: a413 NFC cradle endpoint busy | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a416_BLECradleNFCSoftReset` | page 6 | Vehicle security controller: a416 BLE cradle NFC soft reset | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a417_BLERearLeftSoftReset` | page 6 | Vehicle security controller: a417 BLE rear left soft reset | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a418_BLERearRightSoftReset` | page 6 | Vehicle security controller: a418 BLE rear right soft reset | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a420_BLEUnexpectedResetNFCCradle` | page 6 | Vehicle security controller: a420 BLE unexpected reset NFC cradle | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a421_BLEUnexpectedResetRL` | page 7 | Vehicle security controller: a421 BLE unexpected reset RL | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a422_BLEUnexpectedResetRR` | page 7 | Vehicle security controller: a422 BLE unexpected reset RR | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a425_BLENFCCradleAssertFailure` | page 7 | Vehicle security controller: a425 BLENFC cradle assert failure | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a426_BLERearLeftAssertFailure` | page 7 | Vehicle security controller: a426 BLE rear left assert failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a427_BLERearRightAssertFailure` | page 7 | Vehicle security controller: a427 BLE rear right assert failure | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a428_UWBCenterUpdateInterrupted` | page 7 | Vehicle security controller: a428 UWB center update interrupted | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a429_UWBLeftUpdateInterrupted` | page 7 | Vehicle security controller: a429 UWB left update interrupted | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a430_UWBRightUpdateInterrupted` | page 7 | Vehicle security controller: a430 UWB right update interrupted | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a432_UWBRearLeftUpdateInterrupted` | page 7 | Vehicle security controller: a432 UWB rear left update interrupted | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a433_UWBRearRightUpdateInterrupted` | page 7 | Vehicle security controller: a433 UWB rear right update interrupted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a434_UWBRadioConfigUpdated` | page 7 | Vehicle security controller: a434 UWB radio config updated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a435_NFCCardPresentWhileCharging` | page 7 | Vehicle security controller: a435 NFC card present while charging | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a436_uhfHWDoesNotMatchCountry` | page 7 | Vehicle security controller: a436 uhf HW does not match country | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a437_NearbyInteractionDebug` | page 7 | Vehicle security controller: a437 nearby interaction debug | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a438_UWBRearUpdateInterrupted` | page 7 | Vehicle security controller: a438 UWB rear update interrupted | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a453_passiveDisabled` | page 7 | Vehicle security controller: a453 passive disabled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a454_TPMSOverPressureWarning` | page 7 | Vehicle security controller: a454 TPMS over pressure warning | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a455_TPMSOverPressureWarningFrontLeft` | page 7 | Vehicle security controller: a455 TPMS over pressure warning front left | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a456_TPMSOverPressureWarningFrontRight` | page 7 | Vehicle security controller: a456 TPMS over pressure warning front right | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a457_TPMSOverPressureWarningRearLeft` | page 7 | Vehicle security controller: a457 TPMS over pressure warning rear left | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a458_TPMSOverPressureWarningRearRight` | page 7 | Vehicle security controller: a458 TPMS over pressure warning rear right | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a459_TPMSCertCheckFailedSensor0` | page 7 | Vehicle security controller: a459 TPMS cert check failed sensor0 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a460_TPMSCertCheckFailedSensor1` | page 7 | Vehicle security controller: a460 TPMS cert check failed sensor1 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a461_TPMSCertCheckFailedSensor2` | page 7 | Vehicle security controller: a461 TPMS cert check failed sensor2 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a462_TPMSCertCheckFailedSensor3` | page 7 | Vehicle security controller: a462 TPMS cert check failed sensor3 | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a465_UWBRearLeftKeyVerificationFailure` | page 7 | Vehicle security controller: a465 UWB rear left key verification failure | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a466_UWBRearRightKeyVerificationFailure` | page 7 | Vehicle security controller: a466 UWB rear right key verification failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a467_UWBCenterKeyVerificationFailure` | page 7 | Vehicle security controller: a467 UWB center key verification failure | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a468_UWBRearKeyVerificationFailure` | page 7 | Vehicle security controller: a468 UWB rear key verification failure | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a469_UWBLeftKeyVerificationFailure` | page 7 | Vehicle security controller: a469 UWB left key verification failure | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a470_UWBRightKeyVerificationFailure` | page 7 | Vehicle security controller: a470 UWB right key verification failure | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a472_peerRemovedInformation` | page 7 | Vehicle security controller: a472 peer removed information | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a473_handlePullWithoutAuth3` | page 7 | Vehicle security controller: a473 handle pull without auth3 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a474_handlePullWithoutAuth4` | page 7 | Vehicle security controller: a474 handle pull without auth4 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a475_handlePullWithoutAuth5` | page 7 | Vehicle security controller: a475 handle pull without auth5 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a476_handlePullWithoutAuth6` | page 7 | Vehicle security controller: a476 handle pull without auth6 | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a477_phoneStartedBonding` | page 7 | Vehicle security controller: a477 phone started bonding | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a478_handlePullWithoutAuth7` | page 7 | Vehicle security controller: a478 handle pull without auth7 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a479_handlePullWithoutAuthNIStateDev0` | page 7 | Vehicle security controller: a479 handle pull without auth NI state dev0 | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a480_handlePullWithoutAuthNIStateDev1` | page 7 | Vehicle security controller: a480 handle pull without auth NI state dev1 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a481_handlePullWithoutAuthNIStateDev2` | page 8 | Vehicle security controller: a481 handle pull without auth NI state dev2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a482_VINChanged` | page 8 | Vehicle security controller: a482 VIN changed | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a483_highThermalGradiantDetected` | page 8 | Vehicle security controller: a483 high thermal gradiant detected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a484_UWBLeftUpdateTriggered` | page 8 | Vehicle security controller: a484 UWB left update triggered | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a485_UWBCenterUpdateTriggered` | page 8 | Vehicle security controller: a485 UWB center update triggered | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a486_UWBRightUpdateTriggered` | page 8 | Vehicle security controller: a486 UWB right update triggered | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a487_unrecognizedProto` | page 8 | Vehicle security controller: a487 unrecognized proto | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a488_FiraRangingRejected` | page 8 | Vehicle security controller: a488 fira ranging rejected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a489_UWBRearLeftUpdateTriggered` | page 8 | Vehicle security controller: a489 UWB rear left update triggered | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a490_UWBRearRightUpdateTriggered` | page 8 | Vehicle security controller: a490 UWB rear right update triggered | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a494_UWBRearUpdateTriggered` | page 8 | Vehicle security controller: a494 UWB rear update triggered | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a495_handlePullWithoutAuth_iOS` | page 8 | Vehicle security controller: a495 handle pull without auth i OS | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a496_handlePullWithoutAuth_Android` | page 8 | Vehicle security controller: a496 handle pull without auth android | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a497_incorrectEndpointInstallation` | page 8 | Vehicle security controller: a497 incorrect endpoint installation | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a498_TPMSFeature0Reached` | page 8 | Vehicle security controller: a498 TPMS feature0 reached | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a499_TPMSAssertFailure0` | page 8 | Vehicle security controller: a499 TPMS assert failure0 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a500_TPMSAssertFailure1` | page 8 | Vehicle security controller: a500 TPMS assert failure1 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a501_TPMSAssertFailure2` | page 8 | Vehicle security controller: a501 TPMS assert failure2 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a502_TPMSAssertFailure3` | page 8 | Vehicle security controller: a502 TPMS assert failure3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a503_CANMsgMACVerificationFailure` | page 8 | Vehicle security controller: a503 CAN msg MAC verification failure | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a504_CANMsgMACVerificationKeyNotProvisioned` | page 8 | Vehicle security controller: a504 CAN msg MAC verification key not provisioned | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a505_CANMsgMACVerificationKeyMismatch` | page 8 | Vehicle security controller: a505 CAN msg MAC verification key mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a510_watchKeyOffWrist` | page 8 | Vehicle security controller: a510 watch key off wrist | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a511_phoneKeyStationary` | page 8 | Vehicle security controller: a511 phone key stationary | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a513_TPMSConnectionStatsNotReceived0` | page 8 | Vehicle security controller: a513 TPMS connection stats not received0 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a514_TPMSConnectionStatsNotReceived1` | page 8 | Vehicle security controller: a514 TPMS connection stats not received1 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a515_TPMSConnectionStatsNotReceived2` | page 8 | Vehicle security controller: a515 TPMS connection stats not received2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a516_TPMSConnectionStatsNotReceived3` | page 8 | Vehicle security controller: a516 TPMS connection stats not received3 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a517_TPMSOutOfRangePressureReceived0` | page 8 | Vehicle security controller: a517 TPMS out of range pressure received0 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a518_TPMSOutOfRangePressureReceived1` | page 8 | Vehicle security controller: a518 TPMS out of range pressure received1 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a519_TPMSOutOfRangePressureReceived2` | page 8 | Vehicle security controller: a519 TPMS out of range pressure received2 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a520_TPMSOutOfRangePressureReceived3` | page 8 | Vehicle security controller: a520 TPMS out of range pressure received3 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a521_TPMSSensorLowConfidenceSensorLocalization0` | page 8 | Vehicle security controller: a521 TPMS sensor low confidence sensor localization0 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a522_TPMSSensorLowConfidenceSensorLocalization1` | page 8 | Vehicle security controller: a522 TPMS sensor low confidence sensor localization1 | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a523_TPMSSensorLowConfidenceSensorLocalization2` | page 8 | Vehicle security controller: a523 TPMS sensor low confidence sensor localization2 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a524_TPMSSensorLowConfidenceSensorLocalization3` | page 8 | Vehicle security controller: a524 TPMS sensor low confidence sensor localization3 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a525_TPMSLocalizationMultipleSensorsForPositionFL` | page 8 | Vehicle security controller: a525 TPMS localization multiple sensors for position FL | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a526_TPMSLocalizationMultipleSensorsForPositionFR` | page 8 | Vehicle security controller: a526 TPMS localization multiple sensors for position FR | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a527_TPMSLocalizationMultipleSensorsForPositionRL` | page 8 | Vehicle security controller: a527 TPMS localization multiple sensors for position RL | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a528_TPMSLocalizationMultipleSensorsForPositionRR` | page 8 | Vehicle security controller: a528 TPMS localization multiple sensors for position RR | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a529_TPMSTireServiceDetected` | page 8 | Vehicle security controller: a529 TPMS tire service detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_a540_dummyAlertMax` | page 8 | Vehicle security controller: a540 dummy alert max | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCSEC_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (26 signals), page 1 (43 signals), page 2 (41 signals), page 3 (54 signals), page 4 (40 signals), page 5 (14 signals), page 6 (13 signals), page 7 (40 signals), page 8 (42 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
