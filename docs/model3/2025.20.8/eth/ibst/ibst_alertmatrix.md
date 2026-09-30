---
layout: default
title: "IBST_alertMatrix (0x35D) — Electric brake booster, Tesla Model 3 2025.20.8 ETH"
description: "Electric brake booster message: alert matrix. Ethernet-side message IBST_alertMatrix of Electric brake booster for Tesla Model 3 firmware 2025.20.8, 236 signals (IBST_matrixIndex, IBST_a001_microSupplyError, IBST_a002_HWBISTError, IBST_a003_RAMFault and 232 more). Bit layout, scaling, units and value tables."
---

# IBST_alertMatrix (0x35D) — Electric brake booster, Tesla Model 3 2025.20.8 ETH

Electric brake booster message: alert matrix. This page documents the 236 signals of IBST_alertMatrix as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `IBST_alertMatrix` |
| Ethernet-side id | 0x35D (861) |
| ECU | [Electric brake booster](../../ibst.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | IBST |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 236 |

## Signals of IBST_alertMatrix

Tesla Model 3 CAN bus signals in `IBST_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `IBST_matrixIndex` | selector | Electric brake booster: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3` | plausible |
| `IBST_a001_microSupplyError` | page 0 | Electric brake booster: a001 micro supply error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a002_HWBISTError` | page 0 | Electric brake booster: a002 HWBIST error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a003_RAMFault` | page 0 | Electric brake booster: a003 RAM fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a004_flashFault` | page 0 | Electric brake booster: a004 flash fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a005_microSafetyFault` | page 0 | Electric brake booster: a005 micro safety fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a006_microSafetyLogicFault` | page 0 | Electric brake booster: a006 micro safety logic fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a007_RBCPUException` | page 0 | Electric brake booster: a007 RBCPU exception | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a008_stackOverUnderFlow` | page 0 | Electric brake booster: a008 stack over under flow | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a009_systemErrorHook` | page 0 | Electric brake booster: a009 system error hook | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a010_OSErrorHook` | page 0 | Electric brake booster: a010 OS error hook | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a011_systemTaskOverRun` | page 0 | Electric brake booster: a011 system task over run | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a012_OSTaskSchemeError` | page 0 | Electric brake booster: a012 OS task scheme error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a013_systemTaskJitter` | page 0 | Electric brake booster: a013 system task jitter | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a014_DMATransferError` | page 0 | Electric brake booster: a014 DMA transfer error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a015_asicOscillatorError` | page 0 | Electric brake booster: a015 asic oscillator error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a016_RBBLMShaftShiftError` | page 0 | Electric brake booster: a016 RBBLM shaft shift error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a017_assertionFault` | page 0 | Electric brake booster: a017 assertion fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a018_unsupportedHW` | page 0 | Electric brake booster: a018 unsupported HW | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a019_supplyASICInitFault` | page 0 | Electric brake booster: a019 supply ASIC init fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a020_VPREU5VOutOfRange` | page 0 | Electric brake booster: a020 VPREU5 v out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a021_IREFOutOfRange` | page 0 | Electric brake booster: a021 IREF out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a022_U5VTestFault` | page 0 | Electric brake booster: a022 U5 v test fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a023_U5VOutOfRange` | page 0 | Electric brake booster: a023 U5 v out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a024_chargePumpFault` | page 0 | Electric brake booster: a024 charge pump fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a025_ecuClockTestFault` | page 0 | Electric brake booster: a025 ecu clock test fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a026_ecuBistCmdTestFault` | page 0 | Electric brake booster: a026 ecu bist cmd test fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a027_ecuFastWdTestFault` | page 0 | Electric brake booster: a027 ecu fast wd test fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a028_ecuBistFaultCtrFault` | page 0 | Electric brake booster: a028 ecu bist fault ctr fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a029_ecuErrpinCounterFault` | page 0 | Electric brake booster: a029 ecu errpin counter fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a030_ecuEnableElLowFault` | page 0 | Electric brake booster: a030 ecu enable el low fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a031_decoupleBitTestFault` | page 0 | Electric brake booster: a031 decouple bit test fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a032_ecuEnableElHighFault` | page 0 | Electric brake booster: a032 ecu enable el high fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a033_ecuWdStartuptestFault` | page 0 | Electric brake booster: a033 ecu wd startuptest fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a034_ecuEnableHyHighFault` | page 0 | Electric brake booster: a034 ecu enable hy high fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a035_ecuEnableHyLowFault` | page 0 | Electric brake booster: a035 ecu enable hy low fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a036_MRGPathTestFault` | page 0 | Electric brake booster: a036 MRG path test fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a037_ecuWdSContinuousError` | page 0 | Electric brake booster: a037 ecu wd s continuous error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a038_ecuEnContinuousError` | page 0 | Electric brake booster: a038 ecu en continuous error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a039_GTMRefFrequencyError` | page 0 | Electric brake booster: a039 GTM ref frequency error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a040_GTMTbuMonError` | page 0 | Electric brake booster: a040 GTM tbu mon error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a041_micAsicClkInError` | page 0 | Electric brake booster: a041 mic asic clk in error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a042_micAsicInitTestError` | page 0 | Electric brake booster: a042 mic asic init test error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a043_micSpiTransferError` | page 0 | Electric brake booster: a043 mic spi transfer error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a044_NvMEepromWIP` | page 0 | Electric brake booster: a044 nv m eeprom WIP | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a045_WdhAsicWdErrorCntStuck` | page 0 | Electric brake booster: a045 wdh asic wd error cnt stuck | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a046_WdhAsicWdErrorCntLimit` | page 0 | Electric brake booster: a046 wdh asic wd error cnt limit | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a047_WdhAsicWdCmdMissing` | page 0 | Electric brake booster: a047 wdh asic wd cmd missing | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a048_WdhSwBistConCnt` | page 0 | Electric brake booster: a048 wdh sw bist con cnt | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a049_WdhTaskMonConCnt` | page 0 | Electric brake booster: a049 wdh task mon con cnt | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a050_VPreExternalFeeding` | page 0 | Electric brake booster: a050 v pre external feeding | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a051_ecuBandgap` | page 0 | Electric brake booster: a051 ecu bandgap | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a052_AdcPinTest` | page 0 | Electric brake booster: a052 adc pin test | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a053_AdcSelftestC5P` | page 0 | Electric brake booster: a053 adc selftest C5 p | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a054_AdcPeripheralFault` | page 0 | Electric brake booster: a054 adc peripheral fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a055_UB6SupplyPathFault` | page 0 | Electric brake booster: a055 UB6 supply path fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a056_UB6PlausiMonFault` | page 0 | Electric brake booster: a056 UB6 plausi mon fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a057_microRegisterFault` | page 0 | Electric brake booster: a057 micro register fault | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a058_NvMWriteCycleExceed` | page 0 | Electric brake booster: a058 nv m write cycle exceed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a059_NvMEepromSize` | page 0 | Electric brake booster: a059 nv m eeprom size | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a060_NvMMigrationFault` | page 0 | Electric brake booster: a060 nv m migration fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a061_AswSystemTimeOut` | page 1 | Electric brake booster: a061 asw system time out | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a062_MICB6TransferError` | page 1 | Electric brake booster: a062 MICB6 transfer error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a063_tempSens2ShortToSupply` | page 1 | Electric brake booster: a063 temp sens2 short to supply | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a064_tempSens1ShortToGround` | page 1 | Electric brake booster: a064 temp sens1 short to ground | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a065_tempSens2ShortToGround` | page 1 | Electric brake booster: a065 temp sens2 short to ground | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a066_tempSens1ShortToSupply` | page 1 | Electric brake booster: a066 temp sens1 short to supply | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a067_tempSensImplausVoltage` | page 1 | Electric brake booster: a067 temp sens implaus voltage | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a068_chargePumpUndervoltage` | page 1 | Electric brake booster: a068 charge pump undervoltage | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a069_greasingRoutineFault` | page 1 | Electric brake booster: a069 greasing routine fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a070_notShutDownNvMWrite` | page 1 | Electric brake booster: a070 not shut down nv m write | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a071_notShutDownNvMRead` | page 1 | Electric brake booster: a071 not shut down nv m read | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a072_notShutDownRight` | page 1 | Electric brake booster: a072 not shut down right | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a073_jumpInAdjustNvMRead` | page 1 | Electric brake booster: a073 jump in adjust nv m read | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a074_FindIdleDataNvMWrite` | page 1 | Electric brake booster: a074 find idle data nv m write | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a075_FindIdleRoutineFault` | page 1 | Electric brake booster: a075 find idle routine fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a076_masterCylLengthRead` | page 1 | Electric brake booster: a076 master cyl length read | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a077_runOutMotorSaturated` | page 1 | Electric brake booster: a077 run out motor saturated | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a078_wearOffsetCompNVMRead` | page 1 | Electric brake booster: a078 wear offset comp NVM read | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a079_motorTempHighLevel1` | page 1 | Electric brake booster: a079 motor temp high level1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a080_motorTempHighLevel2` | page 1 | Electric brake booster: a080 motor temp high level2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a081_travelDeviation` | page 1 | Electric brake booster: a081 travel deviation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a082_motorSpeedDeviation` | page 1 | Electric brake booster: a082 motor speed deviation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a083_spindlePositionTooHigh` | page 1 | Electric brake booster: a083 spindle position too high | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a084_CANTransceiverHWFault` | page 1 | Electric brake booster: a084 CAN transceiver HW fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a085_supplyUndervoltageLvl3` | page 1 | Electric brake booster: a085 supply undervoltage lvl3 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a086_supplyOvervoltageLvl3` | page 1 | Electric brake booster: a086 supply overvoltage lvl3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a087_rotorSinOutOfRangeLow` | page 1 | Electric brake booster: a087 rotor sin out of range low | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a088_rotorCosOutOfRangeLow` | page 1 | Electric brake booster: a088 rotor cos out of range low | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a089_rotorSinOutOfRangeHigh` | page 1 | Electric brake booster: a089 rotor sin out of range high | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a090_rotorCosOutOfRangeHigh` | page 1 | Electric brake booster: a090 rotor cos out of range high | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a091_SMMOneRequestsInit` | page 1 | Electric brake booster: a091 SMM one requests init | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a092_systemStartTimeOut` | page 1 | Electric brake booster: a092 system start time out | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a093_UEXSOvertemperature` | page 1 | Electric brake booster: a093 UEXS overtemperature | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a094_XPASSEchoTimeDeviation` | page 1 | Electric brake booster: a094 XPASS echo time deviation | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a095_XPASSTimeOut` | page 1 | Electric brake booster: a095 XPASS time out | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a096_bridgeDriverMonError` | page 1 | Electric brake booster: a096 bridge driver mon error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a097_bridgeDriverError` | page 1 | Electric brake booster: a097 bridge driver error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a098_bridgeShortedPhase` | page 1 | Electric brake booster: a098 bridge shorted phase | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a099_bridgeSwitchInitError` | page 1 | Electric brake booster: a099 bridge switch init error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a100_current2OffsetHigh` | page 1 | Electric brake booster: a100 current2 offset high | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a101_current2OffsetLow` | page 1 | Electric brake booster: a101 current2 offset low | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a102_current1OffsetHigh` | page 1 | Electric brake booster: a102 current1 offset high | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a103_current1OffsetLow` | page 1 | Electric brake booster: a103 current1 offset low | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a104_bridgeDriverShort` | page 1 | Electric brake booster: a104 bridge driver short | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a105_LiPSUndervoltage` | page 1 | Electric brake booster: a105 li PS undervoltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a106_LiPS5VSupply` | page 1 | Electric brake booster: a106 li PS5 v supply | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a107_LiPS2PwmLineHigh` | page 1 | Electric brake booster: a107 li PS2 pwm line high | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a108_LiPS2PwmLineLow` | page 1 | Electric brake booster: a108 li PS2 pwm line low | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a109_LiPS2PwmTransmission` | page 1 | Electric brake booster: a109 li PS2 pwm transmission | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a110_LiPS1SentLineHigh` | page 1 | Electric brake booster: a110 li PS1 sent line high | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a111_LiPS1SentLineLow` | page 1 | Electric brake booster: a111 li PS1 sent line low | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a112_LiPS1SentTransmission` | page 1 | Electric brake booster: a112 li PS1 sent transmission | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a113_LiPS1SentSensor` | page 1 | Electric brake booster: a113 li PS1 sent sensor | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a114_partyBusOff` | page 1 | Electric brake booster: a114 party bus off | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a115_chassisBusOff` | page 1 | Electric brake booster: a115 chassis bus off | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a116_supplyUndervoltageLvl2` | page 1 | Electric brake booster: a116 supply undervoltage lvl2 | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a117_supplyOvervoltageLvl2` | page 1 | Electric brake booster: a117 supply overvoltage lvl2 | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a118_RPSNvMReadFault` | page 1 | Electric brake booster: a118 RPS nv m read fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a119_RPSWrongCalibData` | page 1 | Electric brake booster: a119 RPS wrong calib data | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a120_RPSVectorRangeHigh` | page 1 | Electric brake booster: a120 RPS vector range high | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a121_RPSVectorRangeLow` | page 2 | Electric brake booster: a121 RPS vector range low | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a122_RPSVectorOscillating` | page 2 | Electric brake booster: a122 RPS vector oscillating | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a123_bridgeDriverUnavail` | page 2 | Electric brake booster: a123 bridge driver unavail | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a124_OBDCurrent1OORHigh` | page 2 | Electric brake booster: a124 OBD current1 OOR high | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a125_OBDCurrent2OORHigh` | page 2 | Electric brake booster: a125 OBD current2 OOR high | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a126_OBDCurrent1OORLow` | page 2 | Electric brake booster: a126 OBD current1 OOR low | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a127_OBDCurrent2OORLow` | page 2 | Electric brake booster: a127 OBD current2 OOR low | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a128_BLMMuxerTimeoutError` | page 2 | Electric brake booster: a128 BLM muxer timeout error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a129_loadDumpOnFSLTest` | page 2 | Electric brake booster: a129 load dump on FSL test | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a130_DTSFunctionalRangeLow` | page 2 | Electric brake booster: a130 DTS functional range low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a131_DTSFunctionalRangeHigh` | page 2 | Electric brake booster: a131 DTS functional range high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a132_DTSPlausiCheck1vs2` | page 2 | Electric brake booster: a132 DTS plausi check1vs2 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a133_DTSOffsetTooLow` | page 2 | Electric brake booster: a133 DTS offset too low | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a134_DTSOffsetTooHigh` | page 2 | Electric brake booster: a134 DTS offset too high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a135_ESPparty1DLC` | page 2 | Electric brake booster: a135 ES pparty1 DLC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a136_ESPparty1Timeout` | page 2 | Electric brake booster: a136 ES pparty1 timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a137_ESPparty1Checksum` | page 2 | Electric brake booster: a137 ES pparty1 checksum | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a138_ESPparty1Counter` | page 2 | Electric brake booster: a138 ES pparty1 counter | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a139_ESPparty2DLC` | page 2 | Electric brake booster: a139 ES pparty2 DLC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a140_ESPparty2Timeout` | page 2 | Electric brake booster: a140 ES pparty2 timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a141_ESPparty2Checksum` | page 2 | Electric brake booster: a141 ES pparty2 checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a142_ESPparty2Counter` | page 2 | Electric brake booster: a142 ES pparty2 counter | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a143_ESPparty3DLC` | page 2 | Electric brake booster: a143 ES pparty3 DLC | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a144_ESPparty3Timeout` | page 2 | Electric brake booster: a144 ES pparty3 timeout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a145_ESPparty3Checksum` | page 2 | Electric brake booster: a145 ES pparty3 checksum | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a146_ESPparty3Counter` | page 2 | Electric brake booster: a146 ES pparty3 counter | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a147_PSCMotorSizeReadFault` | page 2 | Electric brake booster: a147 PSC motor size read fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a148_MLIGainMechReadFault` | page 2 | Electric brake booster: a148 MLI gain mech read fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a149_MLITMCAreaReadFault` | page 2 | Electric brake booster: a149 MLITMC area read fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a150_motorTestFault` | page 2 | Electric brake booster: a150 motor test fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a151_PSCGearRatioReadFault` | page 2 | Electric brake booster: a151 PSC gear ratio read fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a152_PSCVoltageImplausible` | page 2 | Electric brake booster: a152 PSC voltage implausible | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a153_unused` | page 2 | Electric brake booster: a153 unused | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a154_unused` | page 2 | Electric brake booster: a154 unused | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a155_supplyUndervoltageLvl1` | page 2 | Electric brake booster: a155 supply undervoltage lvl1 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a156_supplyOvervoltageLvl1` | page 2 | Electric brake booster: a156 supply overvoltage lvl1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a157_masterCylPressInvalid` | page 2 | Electric brake booster: a157 master cyl press invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a158_DTSOffsHighSuspicious` | page 2 | Electric brake booster: a158 DTS offs high suspicious | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a159_FindIdleNvMReadError` | page 2 | Electric brake booster: a159 find idle nv m read error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a160_DTSIDTimeOut` | page 2 | Electric brake booster: a160 DTSID time out | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a161_powerPackMismatch` | page 2 | Electric brake booster: a161 power pack mismatch | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a162_idlePosNotDetected` | page 2 | Electric brake booster: a162 idle pos not detected | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a163_ESPpEstMaxInvalid` | page 2 | Electric brake booster: a163 ES pp est max invalid | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a164_ESPVehicleSpeedInvalid` | page 2 | Electric brake booster: a164 ESP vehicle speed invalid | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a165_ESPpForceBlendInvalid` | page 2 | Electric brake booster: a165 ES pp force blend invalid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a166_ESPpMcVirtualInvalid` | page 2 | Electric brake booster: a166 ES pp mc virtual invalid | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a167_ESPqTargetExterInvalid` | page 2 | Electric brake booster: a167 ES pq target exter invalid | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a168_CANOvervoltage` | page 2 | Electric brake booster: a168 CAN overvoltage | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a169_CANUndervoltage` | page 2 | Electric brake booster: a169 CAN undervoltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a170_LVPowerStateTimeout` | page 2 | Electric brake booster: a170 LV power state timeout | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a171_LVPowerStateChecksum` | page 2 | Electric brake booster: a171 LV power state checksum | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a172_LVPowerStateDLC` | page 2 | Electric brake booster: a172 LV power state DLC | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a173_LVPowerStateCounter` | page 2 | Electric brake booster: a173 LV power state counter | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a174_LVOffStateInvalid` | page 2 | Electric brake booster: a174 LV off state invalid | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a175_LVGoingDownInvalid` | page 2 | Electric brake booster: a175 LV going down invalid | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a176_blockedPedalDetected` | page 2 | Electric brake booster: a176 blocked pedal detected | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a177_EPBLsystemStatusMIA` | page 2 | Electric brake booster: a177 EPB lsystem status MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a178_EPBRsystemStatusMIA` | page 2 | Electric brake booster: a178 EPB rsystem status MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a179_VCLEFTepbmStatusMIA` | page 2 | Electric brake booster: a179 VCLEF tepbm status MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a180_VCRIGHTepbmStatusMIA` | page 2 | Electric brake booster: a180 VCRIGH tepbm status MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a181_DIchassisControlDLC` | page 3 | Electric brake booster: a181 d ichassis control DLC | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a182_DIchassisControlTimeout` | page 3 | Electric brake booster: a182 d ichassis control timeout | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a183_DIchassisControlChecksum` | page 3 | Electric brake booster: a183 d ichassis control checksum | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a184_DIchassisControlCounter` | page 3 | Electric brake booster: a184 d ichassis control counter | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a185_rightBusOff` | page 3 | Electric brake booster: a185 right bus off | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a186_rightBusPassive` | page 3 | Electric brake booster: a186 right bus passive | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a187_brakeBusOff` | page 3 | Electric brake booster: a187 brake bus off | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a188_brakeBusPassive` | page 3 | Electric brake booster: a188 brake bus passive | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a189_rightVCLVPowerStateTimeout` | page 3 | Electric brake booster: a189 right VCLV power state timeout | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a190_rightVCLVPowerStateDLC` | page 3 | Electric brake booster: a190 right VCLV power state DLC | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a191_rightVCLVPowerStateChecksum` | page 3 | Electric brake booster: a191 right VCLV power state checksum | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a192_rightVCLVPowerStateCounter` | page 3 | Electric brake booster: a192 right VCLV power state counter | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a193_leftVCLVPowerStateTimeout` | page 3 | Electric brake booster: a193 left VCLV power state timeout | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a194_leftVCLVPowerStateChecksum` | page 3 | Electric brake booster: a194 left VCLV power state checksum | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a195_leftVCLVPowerStateDLC` | page 3 | Electric brake booster: a195 left VCLV power state DLC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a196_leftVCLVPowerStateCounter` | page 3 | Electric brake booster: a196 left VCLV power state counter | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a197_brakeLatencyReductionActive` | page 3 | Electric brake booster: a197 brake latency reduction active | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a198_aesActive` | page 3 | Electric brake booster: a198 aes active | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a199_undefinedAlertDetected` | page 3 | Electric brake booster: a199 undefined alert detected | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a200_aesFault` | page 3 | Electric brake booster: a200 aes fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a201_EGGREAR1wheelSpeedsRearTimeOut` | page 3 | Electric brake booster: a201 eggrear1wheel speeds rear time out | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a202_EGGREAR1wheelSpeedsRearChecksum` | page 3 | Electric brake booster: a202 eggrear1wheel speeds rear checksum | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a203_EGGREAR1wheelSpeedsRearDLC` | page 3 | Electric brake booster: a203 eggrear1wheel speeds rear DLC | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a204_EGGREAR1wheelSpeedsRearCounter` | page 3 | Electric brake booster: a204 eggrear1wheel speeds rear counter | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a205_EGGRIGHT1wheelSpeedsFrontTimeOut` | page 3 | Electric brake booster: a205 eggright1wheel speeds front time out | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a206_EGGRIGHT1wheelSpeedsFrontChecksum` | page 3 | Electric brake booster: a206 eggright1wheel speeds front checksum | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a207_EGGRIGHT1wheelSpeedsFrontDLC` | page 3 | Electric brake booster: a207 eggright1wheel speeds front DLC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a208_EGGRIGHT1wheelSpeedsFrontCounter` | page 3 | Electric brake booster: a208 eggright1wheel speeds front counter | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a209_reducedBrakePowerActive` | page 3 | Electric brake booster: a209 reduced brake power active | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a210_reducedBrakePowerNotAvailable` | page 3 | Electric brake booster: a210 reduced brake power not available | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a211_DETReportError` | page 3 | Electric brake booster: a211 DET report error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a212_infoFailureWrongCUBASHandlingDetected` | page 3 | Electric brake booster: a212 info failure wrong CUBAS handling detected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a213_PDURouterinitializationFailed` | page 3 | Electric brake booster: a213 PDU routerinitialization failed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a214_LossOfPDUInstanceDetected` | page 3 | Electric brake booster: a214 loss of PDU instance detected | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a215_UnsupportedSeriesHWDetected` | page 3 | Electric brake booster: a215 unsupported series HW detected | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a216_AsicMalfunctionDetected` | page 3 | Electric brake booster: a216 asic malfunction detected | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a217_AsicTrimmingNotCompleted` | page 3 | Electric brake booster: a217 asic trimming not completed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a218_uCSafetyNotificationGRAM` | page 3 | Electric brake booster: a218 u c safety notification GRAM | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a219_uCSafetyNotification` | page 3 | Electric brake booster: a219 u c safety notification | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a220_ASICOvercurrentOnGPIO250_2` | page 3 | Electric brake booster: a220 ASIC overcurrent on GPIO250 2 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a221_ASICOvercurrentOnGPIO250_1` | page 3 | Electric brake booster: a221 ASIC overcurrent on GPIO250 1 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a222_ASICOvercurrentOnGPIO50_4` | page 3 | Electric brake booster: a222 ASIC overcurrent on GPIO50 4 | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a223_ASICOvercurrentOnGPIO50_3` | page 3 | Electric brake booster: a223 ASIC overcurrent on GPIO50 3 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a224_ASICOvercurrentOnGPIO50_2` | page 3 | Electric brake booster: a224 ASIC overcurrent on GPIO50 2 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a225_ASICOvercurrentOnGPIO50_1` | page 3 | Electric brake booster: a225 ASIC overcurrent on GPIO50 1 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a226_ASICOvercurrentOnWRHS` | page 3 | Electric brake booster: a226 ASIC overcurrent on WRHS | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a227_wakeRequestMismatchDetected` | page 3 | Electric brake booster: a227 wake request mismatch detected | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a228_BlockedPedalDetectedDuringHAD` | page 3 | Electric brake booster: a228 blocked pedal detected during HAD | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a229_BlockedPedalDetected` | page 3 | Electric brake booster: a229 blocked pedal detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a230_DTS2FunctionalRangeLow` | page 3 | Electric brake booster: a230 DTS2 functional range low | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a231_DTS2FunctionalRangeLow` | page 3 | Electric brake booster: a231 DTS2 functional range low | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a232_PostAssemblyRoutineFailed` | page 3 | Electric brake booster: a232 post assembly routine failed | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a233_ReferenceRunAbortByECUReset` | page 3 | Electric brake booster: a233 reference run abort by ECU reset | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a234_LiPSOutOfRangeHigh` | page 3 | Electric brake booster: a234 li PS out of range high | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IBST_a235_LiPSOutOfRangeLow` | page 3 | Electric brake booster: a235 li PS out of range low | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`IBST_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (55 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric brake booster messages (IBST)](../../ibst.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
