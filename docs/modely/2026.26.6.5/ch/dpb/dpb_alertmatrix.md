---
layout: default
title: "DPB_alertMatrix (0x3E7) — DPB ECU, Tesla Model Y 2026.26.6.5 CH CAN"
description: "DPB ECU message: alert matrix. Tesla Model Y CAN bus message DPB_alertMatrix (0x3E7) of DPB ECU, firmware 2026.26.6.5, 338 signals (DPB_matrixIndex, DPB_a001_pPlungerSensorOffsetHigh, DPB_a002_pMC2SensorOffsetHigh, DPB_a003_AswEEPROMReadFailure and 334 more). Bit layout, scaling, units and value tables."
---

# DPB_alertMatrix (0x3E7) — DPB ECU, Tesla Model Y 2026.26.6.5 CH CAN

DPB ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 338 signals of DPB_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DPB_alertMatrix` |
| CAN id | 0x3E7 (999) |
| ECU | [DPB ECU](../../dpb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DPB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 338 |

## Signals of DPB_alertMatrix

Tesla Model Y CAN bus signals in `DPB_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DPB_matrixIndex` | selector | DPB ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5` | plausible |
| `DPB_a001_pPlungerSensorOffsetHigh` | page 0 | DPB ECU: a001 p plunger sensor offset high | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a002_pMC2SensorOffsetHigh` | page 0 | DPB ECU: a002 p MC2 sensor offset high | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a003_AswEEPROMReadFailure` | page 0 | DPB ECU: a003 asw EEPROM read failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a004_assertionFault` | page 0 | DPB ECU: a004 assertion fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a005_hardPedalChar` | page 0 | DPB ECU: a005 hard pedal char | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a006_hardPedalCharGoodCheck` | page 0 | DPB ECU: a006 hard pedal char good check | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a007_PMCLeakageDetected` | page 0 | DPB ECU: a007 PMC leakage detected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a008_LiPSPts1Offset` | page 0 | DPB ECU: a008 li PS pts1 offset | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a009_LiPSPts2Offset` | page 0 | DPB ECU: a009 li PS pts2 offset | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a010_LiPSPtsConsistency` | page 0 | DPB ECU: a010 li PS pts consistency | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a011_PtsNonZeroStage1` | page 0 | DPB ECU: a011 pts non zero stage1 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a012_PtsNonZeroStage2` | page 0 | DPB ECU: a012 pts non zero stage2 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a013_softPedalChar` | page 0 | DPB ECU: a013 soft pedal char | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a014_CANControllerHWFault` | page 0 | DPB ECU: a014 CAN controller HW fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a015_CAN1BusOff` | page 0 | DPB ECU: a015 CAN1 bus off | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a016_CAN2BusOff` | page 0 | DPB ECU: a016 CAN2 bus off | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a017_largeLeakageDetected` | page 0 | DPB ECU: a017 large leakage detected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a018_largeLeakageDetectedGoodCheck` | page 0 | DPB ECU: a018 large leakage detected good check | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a019_DETReportError` | page 0 | DPB ECU: a019 DET report error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a020_ecuHuMismatch` | page 0 | DPB ECU: a020 ecu hu mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a021_brakeSystemOverheatLvl1` | page 0 | DPB ECU: a021 brake system overheat lvl1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a022_brakeSystemOverheatLvl2` | page 0 | DPB ECU: a022 brake system overheat lvl2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a023_initialPlungerCheckFailed` | page 0 | DPB ECU: a023 initial plunger check failed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a024_ESPLDMFailure` | page 0 | DPB ECU: a024 ESPLDM failure | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a025_backupCircuitLeakage` | page 0 | DPB ECU: a025 backup circuit leakage | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a026_LiPSIDTimeout` | page 0 | DPB ECU: a026 li PSID timeout | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a027_motorTempHighLevel1` | page 0 | DPB ECU: a027 motor temp high level1 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a028_motorTempHighLevel2` | page 0 | DPB ECU: a028 motor temp high level2 | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a029_motorTestFault` | page 0 | DPB ECU: a029 motor test fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a030_notShutDownRight` | page 0 | DPB ECU: a030 not shut down right | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a031_HWParamReadFailed` | page 0 | DPB ECU: a031 HW param read failed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a032_HWParamWriteFailed` | page 0 | DPB ECU: a032 HW param write failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a033_motorDynamicLimited` | page 0 | DPB ECU: a033 motor dynamic limited | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a034_lipsMemoryEmpty` | page 0 | DPB ECU: a034 lips memory empty | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a035_PDURouterinitializationFailed` | page 0 | DPB ECU: a035 PDU routerinitialization failed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a036_lossOfPDUInstanceDetected` | page 0 | DPB ECU: a036 loss of PDU instance detected | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a037_plungerCircuitPressHigh` | page 0 | DPB ECU: a037 plunger circuit press high | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a038_plungerCircuitPressHighGoodCheck` | page 0 | DPB ECU: a038 plunger circuit press high good check | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a039_plungerCircuitPressLow` | page 0 | DPB ECU: a039 plunger circuit press low | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a040_plungerCircuitPressLowGoodCheck` | page 0 | DPB ECU: a040 plunger circuit press low good check | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a041_PSCGearRatioReadFault` | page 0 | DPB ECU: a041 PSC gear ratio read fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a042_motorLoadPressImplausible` | page 0 | DPB ECU: a042 motor load press implausible | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a043_PSCMotorSizeReadFault` | page 0 | DPB ECU: a043 PSC motor size read fault | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a044_supplyOvervoltageLvl1` | page 0 | DPB ECU: a044 supply overvoltage lvl1 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a045_supplyOvervoltageLvl2` | page 0 | DPB ECU: a045 supply overvoltage lvl2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a046_supplyOvervoltageLvl3` | page 0 | DPB ECU: a046 supply overvoltage lvl3 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a047_pPlungerPlausCheckFailure` | page 0 | DPB ECU: a047 p plunger plaus check failure | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a048_supplyUndervoltageLvl1` | page 0 | DPB ECU: a048 supply undervoltage lvl1 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a049_supplyUndervoltageLvl2` | page 0 | DPB ECU: a049 supply undervoltage lvl2 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a050_supplyUndervoltageLvl3` | page 0 | DPB ECU: a050 supply undervoltage lvl3 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a051_PSCVoltageImplausible` | page 0 | DPB ECU: a051 PSC voltage implausible | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a052_PSIDTimeOut` | page 0 | DPB ECU: a052 PSID time out | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a053_hydraulicAssemblyModeActive` | page 0 | DPB ECU: a053 hydraulic assembly mode active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a054_unsupportedHW` | page 0 | DPB ECU: a054 unsupported HW | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a055_unsupportedSeriesHWDetected` | page 0 | DPB ECU: a055 unsupported series HW detected | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a056_AdcPeripheralFault` | page 0 | DPB ECU: a056 adc peripheral fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a057_AdcPinTest` | page 0 | DPB ECU: a057 adc pin test | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a058_AdcSelftestC5P` | page 0 | DPB ECU: a058 adc selftest C5 p | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a059_factoryModeActive` | page 0 | DPB ECU: a059 factory mode active | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a060_motorBridgeDriverFault` | page 0 | DPB ECU: a060 motor bridge driver fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a061_bridgeSwitchInitError` | page 1 | DPB ECU: a061 bridge switch init error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a062_loadDumpOnFSLTest` | page 1 | DPB ECU: a062 load dump on FSL test | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a063_motorConfigMismatch` | page 1 | DPB ECU: a063 motor config mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a064_current1OffsetHigh` | page 1 | DPB ECU: a064 current1 offset high | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a065_current1OffsetLow` | page 1 | DPB ECU: a065 current1 offset low | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a066_current2OffsetHigh` | page 1 | DPB ECU: a066 current2 offset high | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a067_current2OffsetLow` | page 1 | DPB ECU: a067 current2 offset low | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a068_BLMMuxerTimeoutError` | page 1 | DPB ECU: a068 BLM muxer timeout error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a069_OBDCurrent1OORHigh` | page 1 | DPB ECU: a069 OBD current1 OOR high | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a070_OBDCurrent1OORLow` | page 1 | DPB ECU: a070 OBD current1 OOR low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a071_OBDCurrent2OORHigh` | page 1 | DPB ECU: a071 OBD current2 OOR high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a072_OBDCurrent2OORLow` | page 1 | DPB ECU: a072 OBD current2 OOR low | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a073_rotorCosOutOfRangeHigh` | page 1 | DPB ECU: a073 rotor cos out of range high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a074_rotorCosOutOfRangeLow` | page 1 | DPB ECU: a074 rotor cos out of range low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a075_rotorSinOutOfRangeHigh` | page 1 | DPB ECU: a075 rotor sin out of range high | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a076_rotorSinOutOfRangeLow` | page 1 | DPB ECU: a076 rotor sin out of range low | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a077_tempSens1ShortToSupply` | page 1 | DPB ECU: a077 temp sens1 short to supply | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a078_tempSens1ShortToGround` | page 1 | DPB ECU: a078 temp sens1 short to ground | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a079_tempSens2ShortToSupply` | page 1 | DPB ECU: a079 temp sens2 short to supply | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a080_tempSens2ShortToGround` | page 1 | DPB ECU: a080 temp sens2 short to ground | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a081_tempSensImplausVoltage` | page 1 | DPB ECU: a081 temp sens implaus voltage | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a082_chargePumpFault` | page 1 | DPB ECU: a082 charge pump fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a083_chargePumpUndervoltage` | page 1 | DPB ECU: a083 charge pump undervoltage | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a084_RBCPUException` | page 1 | DPB ECU: a084 RBCPU exception | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a085_infoFailureWrongCUBASHandlingDetected` | page 1 | DPB ECU: a085 info failure wrong CUBAS handling detected | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a086_diagHydProtectionPressFault` | page 1 | DPB ECU: a086 diag hyd protection press fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a087_diagHydProtectionVlvFault` | page 1 | DPB ECU: a087 diag hyd protection vlv fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a088_DMATransferError` | page 1 | DPB ECU: a088 DMA transfer error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a089_ecuBandgap` | page 1 | DPB ECU: a089 ecu bandgap | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a090_flashFault` | page 1 | DPB ECU: a090 flash fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a091_MRGPathTestFault` | page 1 | DPB ECU: a091 MRG path test fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a092_decoupleBitTestFault` | page 1 | DPB ECU: a092 decouple bit test fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a093_ecuBistFaultCtrFault` | page 1 | DPB ECU: a093 ecu bist fault ctr fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a094_ecuClockTestFault` | page 1 | DPB ECU: a094 ecu clock test fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a095_ecuEnableElHighFault` | page 1 | DPB ECU: a095 ecu enable el high fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a096_ecuEnableElLowFault` | page 1 | DPB ECU: a096 ecu enable el low fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a097_ecuEnableHyHighFault` | page 1 | DPB ECU: a097 ecu enable hy high fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a098_ecuEnableHyLowFault` | page 1 | DPB ECU: a098 ecu enable hy low fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a099_ecuEnContinuousError` | page 1 | DPB ECU: a099 ecu en continuous error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a100_ecuErrpinCounterFault` | page 1 | DPB ECU: a100 ecu errpin counter fault | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a101_ecuFastWdTestFault` | page 1 | DPB ECU: a101 ecu fast wd test fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a102_ecuVrOnWhileWdTimeout` | page 1 | DPB ECU: a102 ecu vr on while wd timeout | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a103_ecuVrViaSpiFails` | page 1 | DPB ECU: a103 ecu vr via spi fails | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a104_ecuWdStartuptestFault` | page 1 | DPB ECU: a104 ecu wd startuptest fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a105_ecuWdSContinuousError` | page 1 | DPB ECU: a105 ecu wd s continuous error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a106_ecuBistCmdTestFault` | page 1 | DPB ECU: a106 ecu bist cmd test fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a107_vrOnFails` | page 1 | DPB ECU: a107 vr on fails | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a108_GTMRefFrequencyError` | page 1 | DPB ECU: a108 GTM ref frequency error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a109_GTMTbuMonError` | page 1 | DPB ECU: a109 GTM tbu mon error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a110_HWBISTError` | page 1 | DPB ECU: a110 HWBIST error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a111_hydraulicHardUndervoltage` | page 1 | DPB ECU: a111 hydraulic hard undervoltage | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a112_hydraulicUndervoltage` | page 1 | DPB ECU: a112 hydraulic undervoltage | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a113_LiPS1SentLineHigh` | page 1 | DPB ECU: a113 li PS1 sent line high | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a114_LiPS1SentLineLow` | page 1 | DPB ECU: a114 li PS1 sent line low | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a115_LiPS1SentSensor` | page 1 | DPB ECU: a115 li PS1 sent sensor | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a116_LiPS1SentTransmission` | page 1 | DPB ECU: a116 li PS1 sent transmission | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a117_LiPS2PwmLineHigh` | page 1 | DPB ECU: a117 li PS2 pwm line high | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a118_LiPS2PwmLineLow` | page 1 | DPB ECU: a118 li PS2 pwm line low | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a119_LiPS2PwmTransmission` | page 1 | DPB ECU: a119 li PS2 pwm transmission | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a120_LiPSOutOfRangeHigh` | page 1 | DPB ECU: a120 li PS out of range high | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a121_LiPSOutOfRangeLow` | page 2 | DPB ECU: a121 li PS out of range low | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a122_micAsicClkInError` | page 2 | DPB ECU: a122 mic asic clk in error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a123_micAsicInitTestError` | page 2 | DPB ECU: a123 mic asic init test error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a124_asicOscillatorError` | page 2 | DPB ECU: a124 asic oscillator error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a125_B6AsicFault` | page 2 | DPB ECU: a125 B6 asic fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a126_MICB6TransferError` | page 2 | DPB ECU: a126 MICB6 transfer error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a127_hydraulicAsicShortCircuit` | page 2 | DPB ECU: a127 hydraulic asic short circuit | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a128_micSpiTransferError` | page 2 | DPB ECU: a128 mic spi transfer error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a129_AsicTrimmingNotCompleted` | page 2 | DPB ECU: a129 asic trimming not completed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a130_AsicMalfunctionDetected` | page 2 | DPB ECU: a130 asic malfunction detected | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a131_ASICOvercurrentOnGPIO250_1` | page 2 | DPB ECU: a131 ASIC overcurrent on GPIO250 1 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a132_ASICOvercurrentOnGPIO250_2` | page 2 | DPB ECU: a132 ASIC overcurrent on GPIO250 2 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a133_ASICOvercurrentOnGPIO50_1` | page 2 | DPB ECU: a133 ASIC overcurrent on GPIO50 1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a134_ASICOvercurrentOnGPIO50_2` | page 2 | DPB ECU: a134 ASIC overcurrent on GPIO50 2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a135_ASICOvercurrentOnGPIO50_3` | page 2 | DPB ECU: a135 ASIC overcurrent on GPIO50 3 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a136_ASICOvercurrentOnGPIO50_4` | page 2 | DPB ECU: a136 ASIC overcurrent on GPIO50 4 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a137_ASICOvercurrentOnWRHS` | page 2 | DPB ECU: a137 ASIC overcurrent on WRHS | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a138_DIchassisControlCounter` | page 2 | DPB ECU: a138 d ichassis control counter | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a139_DIchassisControlChecksum` | page 2 | DPB ECU: a139 d ichassis control checksum | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a140_DIchassisControlDLC` | page 2 | DPB ECU: a140 d ichassis control DLC | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a141_DIchassisControlTimeout` | page 2 | DPB ECU: a141 d ichassis control timeout | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a142_DIsystemStatusCounter` | page 2 | DPB ECU: a142 d isystem status counter | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a143_DIsystemStatusChecksum` | page 2 | DPB ECU: a143 d isystem status checksum | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a144_DIsystemStatusDLC` | page 2 | DPB ECU: a144 d isystem status DLC | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a145_DIsystemStatusTimeout` | page 2 | DPB ECU: a145 d isystem status timeout | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a146_DIFtorqueCounter` | page 2 | DPB ECU: a146 DI ftorque counter | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a147_DIFtorqueChecksum` | page 2 | DPB ECU: a147 DI ftorque checksum | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a148_DIFtorqueDLC` | page 2 | DPB ECU: a148 DI ftorque DLC | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a149_DIFtorqueTimeout` | page 2 | DPB ECU: a149 DI ftorque timeout | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a150_DIRtorqueCounter` | page 2 | DPB ECU: a150 DI rtorque counter | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a151_DIRtorqueChecksum` | page 2 | DPB ECU: a151 DI rtorque checksum | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a152_DIRtorqueDLC` | page 2 | DPB ECU: a152 DI rtorque DLC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a153_DIRtorqueTimeout` | page 2 | DPB ECU: a153 DI rtorque timeout | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a154_EPBLstatusCounter` | page 2 | DPB ECU: a154 EPB lstatus counter | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a155_EPBLstatusChecksum` | page 2 | DPB ECU: a155 EPB lstatus checksum | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a156_EPBLstatusDLC` | page 2 | DPB ECU: a156 EPB lstatus DLC | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a157_EPBLstatusTimeout` | page 2 | DPB ECU: a157 EPB lstatus timeout | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a158_EPBRstatusCounter` | page 2 | DPB ECU: a158 EPB rstatus counter | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a159_EPBRstatusChecksum` | page 2 | DPB ECU: a159 EPB rstatus checksum | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a160_EPBRstatusDLC` | page 2 | DPB ECU: a160 EPB rstatus DLC | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a161_EPBRstatusTimeout` | page 2 | DPB ECU: a161 EPB rstatus timeout | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a162_ESP_modulator1Counter` | page 2 | DPB ECU: a162 ESP modulator1 counter | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a163_ESP_modulator1Checksum` | page 2 | DPB ECU: a163 ESP modulator1 checksum | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a164_ESP_modulator1DLC` | page 2 | DPB ECU: a164 ESP modulator1 DLC | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a165_ESP_modulator1Timeout` | page 2 | DPB ECU: a165 ESP modulator1 timeout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a166_ESP_chassis3Counter` | page 2 | DPB ECU: a166 ESP chassis3 counter | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a167_ESP_chassis3Checksum` | page 2 | DPB ECU: a167 ESP chassis3 checksum | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a168_ESP_chassis3DLC` | page 2 | DPB ECU: a168 ESP chassis3 DLC | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a169_ESP_chassis3Timeout` | page 2 | DPB ECU: a169 ESP chassis3 timeout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a170_ESP_modulator2Counter` | page 2 | DPB ECU: a170 ESP modulator2 counter | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a171_ESP_modulator2Checksum` | page 2 | DPB ECU: a171 ESP modulator2 checksum | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a172_ESP_modulator2DLC` | page 2 | DPB ECU: a172 ESP modulator2 DLC | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a173_ESP_modulator2Timeout` | page 2 | DPB ECU: a173 ESP modulator2 timeout | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a174_ESP_modulator3Counter` | page 2 | DPB ECU: a174 ESP modulator3 counter | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a175_ESP_modulator3Checksum` | page 2 | DPB ECU: a175 ESP modulator3 checksum | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a176_ESP_modulator3DLC` | page 2 | DPB ECU: a176 ESP modulator3 DLC | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a177_ESP_modulator3Timeout` | page 2 | DPB ECU: a177 ESP modulator3 timeout | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a178_PMstate2Counter` | page 2 | DPB ECU: a178 p mstate2 counter | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a179_PMstate2Checksum` | page 2 | DPB ECU: a179 p mstate2 checksum | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a180_PMstate2DLC` | page 2 | DPB ECU: a180 p mstate2 DLC | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a181_PMstate2Timeout` | page 3 | DPB ECU: a181 p mstate2 timeout | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a182_RCMInertial2Counter` | page 3 | DPB ECU: a182 RCM inertial2 counter | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a183_RCMInertial2Checksum` | page 3 | DPB ECU: a183 RCM inertial2 checksum | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a184_RCMInertial2DLC` | page 3 | DPB ECU: a184 RCM inertial2 DLC | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a185_RCMInertial2Timeout` | page 3 | DPB ECU: a185 RCM inertial2 timeout | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a186_LVPowerStateTimeout` | page 3 | DPB ECU: a186 LV power state timeout | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a187_LVPowerStateChecksum` | page 3 | DPB ECU: a187 LV power state checksum | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a188_LVPowerStateDLC` | page 3 | DPB ECU: a188 LV power state DLC | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a189_LVPowerStateCounter` | page 3 | DPB ECU: a189 LV power state counter | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a190_VCLEFTepbmStatusCounter` | page 3 | DPB ECU: a190 VCLEF tepbm status counter | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a191_VCLEFTepbmStatusChecksum` | page 3 | DPB ECU: a191 VCLEF tepbm status checksum | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a192_VCLEFTepbmStatusDLC` | page 3 | DPB ECU: a192 VCLEF tepbm status DLC | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a193_VCLEFTepbmStatusTimeout` | page 3 | DPB ECU: a193 VCLEF tepbm status timeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a194_VCRIGHTepbmStatusCounter` | page 3 | DPB ECU: a194 VCRIGH tepbm status counter | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a195_VCRIGHTepbmStatusChecksum` | page 3 | DPB ECU: a195 VCRIGH tepbm status checksum | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a196_VCRIGHTepbmStatusDLC` | page 3 | DPB ECU: a196 VCRIGH tepbm status DLC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a197_VCRIGHTepbmStatusTimeout` | page 3 | DPB ECU: a197 VCRIGH tepbm status timeout | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a198_CANOvervoltage` | page 3 | DPB ECU: a198 CAN overvoltage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a199_pMC1QFaulty` | page 3 | DPB ECU: a199 p MC1 q faulty | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a200_ESPRunoutSupportNotAvailable` | page 3 | DPB ECU: a200 ESP runout support not available | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a201_vehicleSpeedQFaulty` | page 3 | DPB ECU: a201 vehicle speed q faulty | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a202_vehicleStandstillQFaulty` | page 3 | DPB ECU: a202 vehicle standstill q faulty | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a203_ABSNotAvailable` | page 3 | DPB ECU: a203 ABS not available | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a204_CANUndervoltage` | page 3 | DPB ECU: a204 CAN undervoltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a205_NvMWriteCycleExceed` | page 3 | DPB ECU: a205 nv m write cycle exceed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a206_OSTaskSchemeError` | page 3 | DPB ECU: a206 OS task scheme error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a207_hydraulicOvervoltage` | page 3 | DPB ECU: a207 hydraulic overvoltage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a208_pressureSensor1Short` | page 3 | DPB ECU: a208 pressure sensor1 short | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a209_pressureSensor1High` | page 3 | DPB ECU: a209 pressure sensor1 high | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a210_pressureSensor1Low` | page 3 | DPB ECU: a210 pressure sensor1 low | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a211_pressureSensor1Fault` | page 3 | DPB ECU: a211 pressure sensor1 fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a212_pressureSensor1Temp` | page 3 | DPB ECU: a212 pressure sensor1 temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a213_pressureSensor1Fault` | page 3 | DPB ECU: a213 pressure sensor1 fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a214_pressureSensor2Short` | page 3 | DPB ECU: a214 pressure sensor2 short | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a215_pressureSensor2High` | page 3 | DPB ECU: a215 pressure sensor2 high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a216_pressureSensor2Low` | page 3 | DPB ECU: a216 pressure sensor2 low | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a217_pressureSensor2Fault` | page 3 | DPB ECU: a217 pressure sensor2 fault | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a218_pressureSensor2Temp` | page 3 | DPB ECU: a218 pressure sensor2 temp | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a219_pressureSensor2Fault` | page 3 | DPB ECU: a219 pressure sensor2 fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a220_excessiveBoostWakeupsDetected` | page 3 | DPB ECU: a220 excessive boost wakeups detected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a221_notShutdownRight` | page 3 | DPB ECU: a221 not shutdown right | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a222_excessiveEcuResetsDetected` | page 3 | DPB ECU: a222 excessive ecu resets detected | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a223_RAMFault` | page 3 | DPB ECU: a223 RAM fault | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a224_brakeBoostLost` | page 3 | DPB ECU: a224 brake boost lost | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a225_U5VOutOfRange` | page 3 | DPB ECU: a225 U5 v out of range | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a226_U5VTestFault` | page 3 | DPB ECU: a226 U5 v test fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a227_brakeFluidLoss` | page 3 | DPB ECU: a227 brake fluid loss | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a228_supplyASICInitFault` | page 3 | DPB ECU: a228 supply ASIC init fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a229_IREFOutOfRange` | page 3 | DPB ECU: a229 IREF out of range | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a230_OSErrorHook` | page 3 | DPB ECU: a230 OS error hook | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a231_stackOverUnderFlow` | page 3 | DPB ECU: a231 stack over under flow | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a232_systemErrorHook` | page 3 | DPB ECU: a232 system error hook | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a233_systemTaskJitter` | page 3 | DPB ECU: a233 system task jitter | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a234_systemTaskOverRun` | page 3 | DPB ECU: a234 system task over run | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a235_UB6PlausiMonFault` | page 3 | DPB ECU: a235 UB6 plausi mon fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a236_UB6SupplyPathFault` | page 3 | DPB ECU: a236 UB6 supply path fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a237_uCVoltageDividerDrift` | page 3 | DPB ECU: a237 u c voltage divider drift | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a238_microRegisterFault` | page 3 | DPB ECU: a238 micro register fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a239_microSafetyFault` | page 3 | DPB ECU: a239 micro safety fault | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a240_microSafetyLogicFault` | page 3 | DPB ECU: a240 micro safety logic fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a241_uCSafetyNotification` | page 4 | DPB ECU: a241 u c safety notification | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a242_uCSafetyNotificationGRAM` | page 4 | DPB ECU: a242 u c safety notification GRAM | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a243_microSupplyError` | page 4 | DPB ECU: a243 micro supply error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a244_valvesGenericFault` | page 4 | DPB ECU: a244 valves generic fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a245_valveMV0Fault` | page 4 | DPB ECU: a245 valve MV0 fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a246_valveMV5Fault` | page 4 | DPB ECU: a246 valve MV5 fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a247_valveMV6Fault` | page 4 | DPB ECU: a247 valve MV6 fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a248_valveMV61Fault` | page 4 | DPB ECU: a248 valve MV61 fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a249_valveMV62Fault` | page 4 | DPB ECU: a249 valve MV62 fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a250_valveMV7Fault` | page 4 | DPB ECU: a250 valve MV7 fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a251_valveMV8Fault` | page 4 | DPB ECU: a251 valve MV8 fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a252_valveMV81Fault` | page 4 | DPB ECU: a252 valve MV81 fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a253_valveMV82Fault` | page 4 | DPB ECU: a253 valve MV82 fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a254_valveMV9Fault` | page 4 | DPB ECU: a254 valve MV9 fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a255_valveRelayShort` | page 4 | DPB ECU: a255 valve relay short | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a256_valveRelayActuationFault` | page 4 | DPB ECU: a256 valve relay actuation fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a257_valveRelayOnContinuous` | page 4 | DPB ECU: a257 valve relay on continuous | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a258_valveRelayOffContinuous` | page 4 | DPB ECU: a258 valve relay off continuous | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a259_valveRelayTestUndervoltage` | page 4 | DPB ECU: a259 valve relay test undervoltage | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a260_valveRelaySafetySwitchFault` | page 4 | DPB ECU: a260 valve relay safety switch fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a261_WdhAsicWdCmdMissing` | page 4 | DPB ECU: a261 wdh asic wd cmd missing | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a262_WdhAsicWdErrorCntLimit` | page 4 | DPB ECU: a262 wdh asic wd error cnt limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a263_WdhAsicWdErrorCntStuck` | page 4 | DPB ECU: a263 wdh asic wd error cnt stuck | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a264_WdhSwBistConCnt` | page 4 | DPB ECU: a264 wdh sw bist con cnt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a265_WdhTaskMonConCnt` | page 4 | DPB ECU: a265 wdh task mon con cnt | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a266_RPSNvMReadFault` | page 4 | DPB ECU: a266 RPS nv m read fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a267_RpsAngleImplausible` | page 4 | DPB ECU: a267 rps angle implausible | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a268_RPSVectorOscillating` | page 4 | DPB ECU: a268 RPS vector oscillating | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a269_RPSVectorRangeHigh` | page 4 | DPB ECU: a269 RPS vector range high | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a270_RPSVectorRangeLow` | page 4 | DPB ECU: a270 RPS vector range low | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a271_RPSWrongCalibData` | page 4 | DPB ECU: a271 RPS wrong calib data | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a272_runtimeAssertionFault` | page 4 | DPB ECU: a272 runtime assertion fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a273_SMMOneRequestsInit` | page 4 | DPB ECU: a273 SMM one requests init | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a274_AswSystemTimeOut` | page 4 | DPB ECU: a274 asw system time out | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a275_Ps1Ps2PlausibilityFault` | page 4 | DPB ECU: a275 ps1 ps2 plausibility fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a276_VCFRONTsensorsCounter` | page 4 | DPB ECU: a276 VCFRON tsensors counter | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a277_VCFRONTsensorsChecksum` | page 4 | DPB ECU: a277 VCFRON tsensors checksum | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a278_VCFRONTsensorsDLC` | page 4 | DPB ECU: a278 VCFRON tsensors DLC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a279_VCFRONTsensorsTimeout` | page 4 | DPB ECU: a279 VCFRON tsensors timeout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a280_LowBrakeFluid` | page 4 | DPB ECU: a280 low brake fluid | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a281_brakeFluidOORHigh` | page 4 | DPB ECU: a281 brake fluid OOR high | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a282_DIbrakeCommandCounter` | page 4 | DPB ECU: a282 d ibrake command counter | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a283_DIbrakeCommandChecksum` | page 4 | DPB ECU: a283 d ibrake command checksum | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a284_DIbrakeCommandDLC` | page 4 | DPB ECU: a284 d ibrake command DLC | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a285_DIbrakeCommandTimeout` | page 4 | DPB ECU: a285 d ibrake command timeout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a286_ebrCmdStateInvalid` | page 4 | DPB ECU: a286 ebr cmd state invalid | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a287_brakeCmdStateInvalid` | page 4 | DPB ECU: a287 brake cmd state invalid | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a288_PlantDegradedSW` | page 4 | DPB ECU: a288 plant degraded SW | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a289_evacFillNotComplete` | page 4 | DPB ECU: a289 evac fill not complete | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a290_securityInfo` | page 4 | DPB ECU: a290 security info | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a291_extDBRRequestTooLow` | page 4 | DPB ECU: a291 ext DBR request too low | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a292_CBDS_fillBufferThreshold` | page 4 | DPB ECU: a292 CBDS fill buffer threshold | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a293_CBDS_fmeInternalEvent` | page 4 | DPB ECU: a293 CBDS fme internal event | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a294_hbaNormalModeActive` | page 4 | DPB ECU: a294 hba normal mode active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a295_hbaTrackModeActive` | page 4 | DPB ECU: a295 hba track mode active | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a296_StatInvalid_DI_FullSNA` | page 4 | DPB ECU: a296 stat invalid DI full SNA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a297_undefinedAlertDetected` | page 4 | DPB ECU: a297 undefined alert detected | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a298_runningPlungerCircuitTest` | page 4 | DPB ECU: a298 running plunger circuit test | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a299_PM_locStateCounter` | page 4 | DPB ECU: a299 PM loc state counter | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a300_PM_locStateChecksum` | page 4 | DPB ECU: a300 PM loc state checksum | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a301_PM_locStateDLC` | page 5 | DPB ECU: a301 PM loc state DLC | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a302_PM_locStateTimeout` | page 5 | DPB ECU: a302 PM loc state timeout | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a303_actuatingDIFullTorqueCmd` | page 5 | DPB ECU: a303 actuating DI full torque cmd | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a304_actuatingDITorqueCmd` | page 5 | DPB ECU: a304 actuating DI torque cmd | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a305_DIbrakeTorqueCommandAndFlagMismatch` | page 5 | DPB ECU: a305 d ibrake torque command and flag mismatch | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a306_actuatorFallbackBasicMap` | page 5 | DPB ECU: a306 actuator fallback basic map | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a307_actuatorDegradedMap` | page 5 | DPB ECU: a307 actuator degraded map | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a308_backupMode` | page 5 | DPB ECU: a308 backup mode | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a309_DIFAxleTorqueInvalid` | page 5 | DPB ECU: a309 DIF axle torque invalid | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a310_DIRAxleTorqueInvalid` | page 5 | DPB ECU: a310 DIR axle torque invalid | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a311_postrunDurationTooLong` | page 5 | DPB ECU: a311 postrun duration too long | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a312_continuouslyActivatedValvesOff` | page 5 | DPB ECU: a312 continuously activated valves off | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a313_qualifiedBrakeEventDetected` | page 5 | DPB ECU: a313 qualified brake event detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a314_runningCyclicVolumeCheck` | page 5 | DPB ECU: a314 running cyclic volume check | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a315_runningLeakageAndAirMonitoring` | page 5 | DPB ECU: a315 running leakage and air monitoring | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a316_lowBrakeFluidDetectedOnHillSlope` | page 5 | DPB ECU: a316 low brake fluid detected on hill slope | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a317_DASredundantBrakingControlPartyChecksum` | page 5 | DPB ECU: a317 DA sredundant braking control party checksum | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a318_DASredundantBrakingControlPartyCounter` | page 5 | DPB ECU: a318 DA sredundant braking control party counter | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a319_DASredundantBrakingControlPartyDLC` | page 5 | DPB ECU: a319 DA sredundant braking control party DLC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a320_DASredundantBrakingControlPartyTimeout` | page 5 | DPB ECU: a320 DA sredundant braking control party timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a321_DASredundantBrakingControlChassisChecksum` | page 5 | DPB ECU: a321 DA sredundant braking control chassis checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a322_DASredundantBrakingControlChassisCounter` | page 5 | DPB ECU: a322 DA sredundant braking control chassis counter | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a323_DASredundantBrakingControlChassisDLC` | page 5 | DPB ECU: a323 DA sredundant braking control chassis DLC | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a324_DASredundantBrakingControlChassisTimeout` | page 5 | DPB ECU: a324 DA sredundant braking control chassis timeout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a325_DIlocStatus2Checksum` | page 5 | DPB ECU: a325 d iloc status2 checksum | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a326_DIlocStatus2Counter` | page 5 | DPB ECU: a326 d iloc status2 counter | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a327_DIlocStatus2DLC` | page 5 | DPB ECU: a327 d iloc status2 DLC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a328_DIlocStatus2Timeout` | page 5 | DPB ECU: a328 d iloc status2 timeout | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a329_standaloneEBRActive` | page 5 | DPB ECU: a329 standalone EBR active | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a330_EMCMain11Checksum` | page 5 | DPB ECU: a330 EMC main11 checksum | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a331_EMCMain11Counter` | page 5 | DPB ECU: a331 EMC main11 counter | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a332_EMCMain11DLC` | page 5 | DPB ECU: a332 EMC main11 DLC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a333_EMCMain11Timeout` | page 5 | DPB ECU: a333 EMC main11 timeout | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a334_EMCMain21Checksum` | page 5 | DPB ECU: a334 EMC main21 checksum | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a335_EMCMain21Counter` | page 5 | DPB ECU: a335 EMC main21 counter | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a336_EMCMain21DLC` | page 5 | DPB ECU: a336 EMC main21 DLC | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DPB_a337_EMCMain21Timeout` | page 5 | DPB ECU: a337 EMC main21 timeout | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`DPB_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (60 signals), page 4 (60 signals), page 5 (37 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All DPB ECU messages (DPB)](../../dpb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
