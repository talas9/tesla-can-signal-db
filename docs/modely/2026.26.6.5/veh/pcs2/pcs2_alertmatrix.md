---
layout: default
title: "PCS2_alertMatrix (0x3E4) — PCS2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "PCS2 ECU message: alert matrix. Tesla Model Y CAN bus message PCS2_alertMatrix (0x3E4) of PCS2 ECU, firmware 2026.26.6.5, 193 signals (PCS2_matrixIndex, PCS2_a001_watchdogAlarmed, PCS2_a002_canRationality, PCS2_a003_softwareAssertion and 189 more). Bit layout, scaling, units and value tables."
---

# PCS2_alertMatrix (0x3E4) — PCS2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

PCS2 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 193 signals of PCS2_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS2_alertMatrix` |
| CAN id | 0x3E4 (996) |
| ECU | [PCS2 ECU](../../pcs2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS2 |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 193 |

## Signals of PCS2_alertMatrix

Tesla Model Y CAN bus signals in `PCS2_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PCS2_matrixIndex` | selector | PCS2 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3` | plausible |
| `PCS2_a001_watchdogAlarmed` | page 0 | PCS2 ECU: a001 watchdog alarmed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a002_canRationality` | page 0 | PCS2 ECU: a002 can rationality | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a003_softwareAssertion` | page 0 | PCS2 ECU: a003 software assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a004_acL1NOverVoltage` | page 0 | PCS2 ECU: a004 ac L1 n over voltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a005_acL1OverCurrent` | page 0 | PCS2 ECU: a005 ac L1 over current | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a006_acL2NOverVoltage` | page 0 | PCS2 ECU: a006 ac L2 n over voltage | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a007_acL2OverCurrent` | page 0 | PCS2 ECU: a007 ac L2 over current | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a008_acL3NOverVoltage` | page 0 | PCS2 ECU: a008 ac L3 n over voltage | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a009_acL3OverCurrent` | page 0 | PCS2 ECU: a009 ac L3 over current | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a010_acLNOverCurrent` | page 0 | PCS2 ECU: a010 ac LN over current | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a011_hvdcOverCurrent` | page 0 | PCS2 ECU: a011 hvdc over current | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a012_cycloATankOverCurrent` | page 0 | PCS2 ECU: a012 cyclo a tank over current | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a013_DcdcALv2OverTemp` | page 0 | PCS2 ECU: a013 dcdc a lv2 over temp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a014_cycloBTankOverCurrent` | page 0 | PCS2 ECU: a014 cyclo b tank over current | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a015_DcdcAHvOverTemp` | page 0 | PCS2 ECU: a015 dcdc a hv over temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a016_dcdcATankOverCurrent` | page 0 | PCS2 ECU: a016 dcdc a tank over current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a017_DcdcBLv2OverTemp` | page 0 | PCS2 ECU: a017 dcdc b lv2 over temp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a018_dcdcBTankOverCurrent` | page 0 | PCS2 ECU: a018 dcdc b tank over current | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a019_DcacADcTempTooHigh` | page 0 | PCS2 ECU: a019 dcac a dc temp too high | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a020_DcacBDcTempTooHigh` | page 0 | PCS2 ECU: a020 dcac b dc temp too high | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a021_powerRailUnderVoltage` | page 0 | PCS2 ECU: a021 power rail under voltage | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a022_dcacEnableFunctionalityDisabled` | page 0 | PCS2 ECU: a022 dcac enable functionality disabled | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a023_dcdcEnableFunctionalityDisabled` | page 0 | PCS2 ECU: a023 dcdc enable functionality disabled | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a024_DcacATxTempTooHigh` | page 0 | PCS2 ECU: a024 dcac a tx temp too high | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a025_DcacBTxTempTooHigh` | page 0 | PCS2 ECU: a025 dcac b tx temp too high | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a026_AcConnectorTempTooHigh` | page 0 | PCS2 ECU: a026 ac connector temp too high | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a027_AmbientTempTooHigh` | page 0 | PCS2 ECU: a027 ambient temp too high | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a028_CoolantTempTooHigh` | page 0 | PCS2 ECU: a028 coolant temp too high | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a029_DcacAAc1TempTooHigh` | page 0 | PCS2 ECU: a029 dcac a ac1 temp too high | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a030_DcacAAc2TempTooHigh` | page 0 | PCS2 ECU: a030 dcac a ac2 temp too high | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a031_DcacBAc1TempTooHigh` | page 0 | PCS2 ECU: a031 dcac b ac1 temp too high | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a032_DcacBAc2TempTooHigh` | page 0 | PCS2 ECU: a032 dcac b ac2 temp too high | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a033_swCoreExcessiveUsage` | page 0 | PCS2 ECU: a033 sw core excessive usage | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a034_lvBusOverVoltage` | page 0 | PCS2 ECU: a034 lv bus over voltage | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a035_lvBusUnderVoltage` | page 0 | PCS2 ECU: a035 lv bus under voltage | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a036_hvBusOverVoltage` | page 0 | PCS2 ECU: a036 hv bus over voltage | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a037_hvBusUnderVoltage` | page 0 | PCS2 ECU: a037 hv bus under voltage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a038_hvBusTopOverVoltage` | page 0 | PCS2 ECU: a038 hv bus top over voltage | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a039_hvBusTopUnderVoltage` | page 0 | PCS2 ECU: a039 hv bus top under voltage | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a040_hvBusBotOverVoltage` | page 0 | PCS2 ECU: a040 hv bus bot over voltage | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a041_hvBusBotUnderVoltage` | page 0 | PCS2 ECU: a041 hv bus bot under voltage | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a042_hvBattOverVoltage` | page 0 | PCS2 ECU: a042 hv batt over voltage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a043_hvBattUnderVoltage` | page 0 | PCS2 ECU: a043 hv batt under voltage | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a044_hvBattTopOverVoltage` | page 0 | PCS2 ECU: a044 hv batt top over voltage | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a045_hvBattTopUnderVoltage` | page 0 | PCS2 ECU: a045 hv batt top under voltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a046_hvBattBotOverVoltage` | page 0 | PCS2 ECU: a046 hv batt bot over voltage | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a047_hvBattBotUnderVoltage` | page 0 | PCS2 ECU: a047 hv batt bot under voltage | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a048_dcacOverVoltage` | page 0 | PCS2 ECU: a048 dcac over voltage | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a049_dcacUnderVoltage` | page 0 | PCS2 ECU: a049 dcac under voltage | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a050_vcPcsDCDCInterfaceMia` | page 0 | PCS2 ECU: a050 vc pcs DCDC interface mia | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a051_bmsMia` | page 0 | PCS2 ECU: a051 bms mia | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a052_cpMia` | page 0 | PCS2 ECU: a052 cp mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a053_hvDcdcControlMIA` | page 0 | PCS2 ECU: a053 hv dcdc control MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a054_uiMia` | page 0 | PCS2 ECU: a054 ui mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a055_dcdcATankUncalibrated` | page 0 | PCS2 ECU: a055 dcdc a tank uncalibrated | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a056_dcdcBTankUncalibrated` | page 0 | PCS2 ECU: a056 dcdc b tank uncalibrated | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a057_cycloATankUncalibrated` | page 0 | PCS2 ECU: a057 cyclo a tank uncalibrated | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a058_cycloBTankUncalibrated` | page 0 | PCS2 ECU: a058 cyclo b tank uncalibrated | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a059_dcdcEnableLineDeasserted` | page 0 | PCS2 ECU: a059 dcdc enable line deasserted | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a060_cycloAFaulted` | page 0 | PCS2 ECU: a060 cyclo a faulted | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a061_cycloBFaulted` | page 1 | PCS2 ECU: a061 cyclo b faulted | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a062_acVoltageNotPresent` | page 1 | PCS2 ECU: a062 ac voltage not present | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a063_chgUnknownGridConfig` | page 1 | PCS2 ECU: a063 chg unknown grid config | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a064_dcdcATankParametersOutOfSpec` | page 1 | PCS2 ECU: a064 dcdc a tank parameters out of spec | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a065_dcdcBTankParametersOutOfSpec` | page 1 | PCS2 ECU: a065 dcdc b tank parameters out of spec | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a066_cycloATankParametersOutOfSpec` | page 1 | PCS2 ECU: a066 cyclo a tank parameters out of spec | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a067_cycloBTankParametersOutOfSpec` | page 1 | PCS2 ECU: a067 cyclo b tank parameters out of spec | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a068_nvmSubsystemStalled` | page 1 | PCS2 ECU: a068 nvm subsystem stalled | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a069_dcdcAlifetimeEnergyRecordFaulty` | page 1 | PCS2 ECU: a069 dcdc alifetime energy record faulty | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a070_dcdcBlifetimeEnergyRecordFaulty` | page 1 | PCS2 ECU: a070 dcdc blifetime energy record faulty | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a071_hvBattBotSensorIrrational` | page 1 | PCS2 ECU: a071 hv batt bot sensor irrational | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a072_hvBattTopSensorIrrational` | page 1 | PCS2 ECU: a072 hv batt top sensor irrational | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a073_hvBusBotSensorIrrational` | page 1 | PCS2 ECU: a073 hv bus bot sensor irrational | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a074_hvBusTopSensorIrrational` | page 1 | PCS2 ECU: a074 hv bus top sensor irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a075_hvBattFullSensorIrrational` | page 1 | PCS2 ECU: a075 hv batt full sensor irrational | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a076_hvBusFullSensorIrrational` | page 1 | PCS2 ECU: a076 hv bus full sensor irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a077_lvBusVoltSensorIrrational` | page 1 | PCS2 ECU: a077 lv bus volt sensor irrational | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a078_acL1NVoltageOffsetIrrational` | page 1 | PCS2 ECU: a078 ac L1 n voltage offset irrational | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a079_acL2NVoltageOffsetIrrational` | page 1 | PCS2 ECU: a079 ac L2 n voltage offset irrational | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a080_acL3NVoltageOffsetIrrational` | page 1 | PCS2 ECU: a080 ac L3 n voltage offset irrational | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a081_acL1CurrentOffsetIrrational` | page 1 | PCS2 ECU: a081 ac L1 current offset irrational | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a082_acL2CurrentOffsetIrrational` | page 1 | PCS2 ECU: a082 ac L2 current offset irrational | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a083_acL3CurrentOffsetIrrational` | page 1 | PCS2 ECU: a083 ac L3 current offset irrational | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a084_acNCurrentOffsetIrrational` | page 1 | PCS2 ECU: a084 ac n current offset irrational | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a085_dcacEnableLineDeasserted` | page 1 | PCS2 ECU: a085 dcac enable line deasserted | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a086_dcacLVUnderVoltage` | page 1 | PCS2 ECU: a086 dcac LV under voltage | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a087_dcacLVOverVoltage` | page 1 | PCS2 ECU: a087 dcac LV over voltage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a088_chgInputVDropHigh` | page 1 | PCS2 ECU: a088 chg input v drop high | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a089_EndOfLineModeActivated` | page 1 | PCS2 ECU: a089 end of line mode activated | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a090_DcdcLvMosfetTempTooHigh` | page 1 | PCS2 ECU: a090 dcdc lv mosfet temp too high | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a091_DcdcTxWindingTempTooHigh` | page 1 | PCS2 ECU: a091 dcdc tx winding temp too high | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a092_dcdc_itankZcdIrrational` | page 1 | PCS2 ECU: a092 dcdc itank zcd irrational | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a093_cycloPwmsNotInterleaved` | page 1 | PCS2 ECU: a093 cyclo pwms not interleaved | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a094_acChargingUnavailable` | page 1 | PCS2 ECU: a094 ac charging unavailable | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a095_powershareUnavailable` | page 1 | PCS2 ECU: a095 powershare unavailable | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a096_vcsuperMia` | page 1 | PCS2 ECU: a096 vcsuper mia | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a097_gtwMia` | page 1 | PCS2 ECU: a097 gtw mia | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a098_eggright3Mia` | page 1 | PCS2 ECU: a098 eggright3 mia | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a099_LineChassisRmsOV` | page 1 | PCS2 ECU: a099 line chassis rms OV | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a100_LineToLineRmsOV` | page 1 | PCS2 ECU: a100 line to line rms OV | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a101_LineChassisInstantaneousOV` | page 1 | PCS2 ECU: a101 line chassis instantaneous OV | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a102_LineToLineInstantaneousOV` | page 1 | PCS2 ECU: a102 line to line instantaneous OV | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a103_IsoTempSensorIrrational` | page 1 | PCS2 ECU: a103 iso temp sensor irrational | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a104_LineChassisRmsUV` | page 1 | PCS2 ECU: a104 line chassis rms UV | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a105_LineToLineRmsUV` | page 1 | PCS2 ECU: a105 line to line rms UV | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a106_systemNeutralChassisRmsOV` | page 1 | PCS2 ECU: a106 system neutral chassis rms OV | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a107_cycloLostCurrentControl` | page 1 | PCS2 ECU: a107 cyclo lost current control | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a108_FunctionalTestModeActivated` | page 1 | PCS2 ECU: a108 functional test mode activated | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a109_ACSurgeProtectionTriggered` | page 1 | PCS2 ECU: a109 AC surge protection triggered | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a110_acCurrentIsLimited` | page 1 | PCS2 ECU: a110 ac current is limited | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a111_microgridHeartbeatMissing` | page 1 | PCS2 ECU: a111 microgrid heartbeat missing | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a112_chgInputVDropTooHigh` | page 1 | PCS2 ECU: a112 chg input v drop too high | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a113_dcdcTransientCapabilityImpacted` | page 1 | PCS2 ECU: a113 dcdc transient capability impacted | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a114_hvBusEstimatedImpedanceLow` | page 1 | PCS2 ECU: a114 hv bus estimated impedance low | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a115_chgWallPowerRemoval` | page 1 | PCS2 ECU: a115 chg wall power removal | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a116_chgPersistentFault` | page 1 | PCS2 ECU: a116 chg persistent fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a117_vcrightMia` | page 1 | PCS2 ECU: a117 vcright mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a118_dcdcFailedToPrechargeToTarget` | page 1 | PCS2 ECU: a118 dcdc failed to precharge to target | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a119_useMaxCapForHvImpedanceEstimation` | page 1 | PCS2 ECU: a119 use max cap for hv impedance estimation | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a120_triggerOdin` | page 1 | Signal reported by PCS2 ECU | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a121_insufficientCoolingDetected` | page 2 | PCS2 ECU: a121 insufficient cooling detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a122_dcacLifetimekVAhRecordError` | page 2 | PCS2 ECU: a122 dcac lifetimek v ah record error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a123_DcdcBHvOverTemp` | page 2 | PCS2 ECU: a123 dcdc b hv over temp | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a124_dcacItankSoftwareOC` | page 2 | PCS2 ECU: a124 dcac itank software OC | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a125_cycloIdleShortingNeutral` | page 2 | PCS2 ECU: a125 cyclo idle shorting neutral | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a126_ipcSuccessiveLockGrabFailure` | page 2 | PCS2 ECU: a126 ipc successive lock grab failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a127_cycloAgdpsHealthCheckFailed` | page 2 | PCS2 ECU: a127 cyclo agdps health check failed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a128_cycloBgdpsHealthCheckFailed` | page 2 | PCS2 ECU: a128 cyclo bgdps health check failed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a129_lossOfZcdEventControl` | page 2 | PCS2 ECU: a129 loss of zcd event control | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a130_IONVMMServerRetryEvent` | page 2 | PCS2 ECU: a130 IONVMM server retry event | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a131_microgridHeartbeatDetected` | page 2 | PCS2 ECU: a131 microgrid heartbeat detected | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a132_microgridDroopDetected` | page 2 | PCS2 ECU: a132 microgrid droop detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a133_unused` | page 2 | PCS2 ECU: a133 unused | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a134_unused` | page 2 | PCS2 ECU: a134 unused | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a135_backgroundTaskOverRun` | page 2 | PCS2 ECU: a135 background task over run | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a136_cycloAMosfetHealthCheckFailed` | page 2 | PCS2 ECU: a136 cyclo a mosfet health check failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a137_cycloBMosfetHealthCheckFailed` | page 2 | PCS2 ECU: a137 cyclo b mosfet health check failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a138_hvdcCurrentSensorOffsetIrrational` | page 2 | PCS2 ECU: a138 hvdc current sensor offset irrational | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a139_unused` | page 2 | PCS2 ECU: a139 unused | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a140_dcdcHalfBusBalancerSaturated` | page 2 | PCS2 ECU: a140 dcdc half bus balancer saturated | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a141_boostOverCurrent` | page 2 | PCS2 ECU: a141 boost over current | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a142_AcLineGdpsUncalibrated` | page 2 | PCS2 ECU: a142 ac line gdps uncalibrated | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a143_AcTankGdpsUncalibrated` | page 2 | PCS2 ECU: a143 ac tank gdps uncalibrated | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a144_DcTankGdpsUncalibrated` | page 2 | PCS2 ECU: a144 dc tank gdps uncalibrated | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a145_DcdcHvdcGdpsUncalibrated` | page 2 | PCS2 ECU: a145 dcdc hvdc gdps uncalibrated | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a146_acLineSharedCurrentConnectionIssue` | page 2 | PCS2 ECU: a146 ac line shared current connection issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a147_powerRailOverVoltage` | page 2 | PCS2 ECU: a147 power rail over voltage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a148_acRelayVoltageIrrational` | page 2 | PCS2 ECU: a148 ac relay voltage irrational | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a149_buckBoostFault` | page 2 | PCS2 ECU: a149 buck boost fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a150_dcdcBurstTimingNotMet` | page 2 | PCS2 ECU: a150 dcdc burst timing not met | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a151_DcdcBLv1OverTemp` | page 2 | PCS2 ECU: a151 dcdc b lv1 over temp | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a152_DcdcBLv3OverTemp` | page 2 | PCS2 ECU: a152 dcdc b lv3 over temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a153_cyclo_itankZcdIrrational` | page 2 | PCS2 ECU: a153 cyclo itank zcd irrational | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a154_adcReferenceUncalibrated` | page 2 | PCS2 ECU: a154 adc reference uncalibrated | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a155_vcbatteryMia` | page 2 | PCS2 ECU: a155 vcbattery mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a156_vcfrontMia` | page 2 | PCS2 ECU: a156 vcfront mia | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a157_VC_pcsManagementMia` | page 2 | PCS2 ECU: a157 VC pcs management mia | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a158_DcdcHvMosfetTempTooHigh` | page 2 | PCS2 ECU: a158 dcdc hv mosfet temp too high | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a159_dcdcGdpsHealthCheckFailed` | page 2 | PCS2 ECU: a159 dcdc gdps health check failed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a160_vcleftMia` | page 2 | PCS2 ECU: a160 vcleft mia | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a161_vcrearMia` | page 2 | PCS2 ECU: a161 vcrear mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a162_cycloARoutineTankInductanceMeasurement` | page 2 | PCS2 ECU: a162 cyclo a routine tank inductance measurement | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a163_cycloBRoutineTankInductanceMeasurement` | page 2 | PCS2 ECU: a163 cyclo b routine tank inductance measurement | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a164_dcdc_hwZcdFault1` | page 2 | PCS2 ECU: a164 dcdc hw zcd fault1 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a165_dcdc_hwZcdFault2` | page 2 | PCS2 ECU: a165 dcdc hw zcd fault2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a166_dcdcEnableLinePWMTripMisconfigured` | page 2 | PCS2 ECU: a166 dcdc enable line PWM trip misconfigured | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a167_unused` | page 2 | PCS2 ECU: a167 unused | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a168_gridFormVoltageDropped` | page 2 | PCS2 ECU: a168 grid form voltage dropped | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a169_cycloMosfetHealthCheckMeasuredHalfPrdAsymmetric` | page 2 | PCS2 ECU: a169 cyclo mosfet health check measured half prd asymmetric | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a170_acChargePowerIsLimited` | page 2 | PCS2 ECU: a170 ac charge power is limited | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a171_unused` | page 2 | PCS2 ECU: a171 unused | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a172_unused` | page 2 | PCS2 ECU: a172 unused | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a173_DcdcALv1OverTemp` | page 2 | PCS2 ECU: a173 dcdc a lv1 over temp | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a174_llc48V0RailOverCurrent` | page 2 | PCS2 ECU: a174 llc48 V0 rail over current | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a175_LVUVSurgePowerEvent` | page 2 | PCS2 ECU: a175 LVUV surge power event | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a176_cpLatchMotorUnavailable` | page 2 | PCS2 ECU: a176 cp latch motor unavailable | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a177_latchMotorRailOverCurrent` | page 2 | PCS2 ECU: a177 latch motor rail over current | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a178_eculogAborted` | page 2 | PCS2 ECU: a178 eculog aborted | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a179_standbyPowerUnavailable` | page 2 | PCS2 ECU: a179 standby power unavailable | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a180_DcdcTxHATTempTooHigh` | page 2 | PCS2 ECU: a180 dcdc tx HAT temp too high | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d181_dcdcConverterVoltSensorAFault` | page 3 | PCS2 ECU: d181 dcdc converter volt sensor a fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d182_dcdcConverterTempSensorAFault` | page 3 | PCS2 ECU: d182 dcdc converter temp sensor a fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d183_batteryChargerAInputVoltSensorFault` | page 3 | PCS2 ECU: d183 battery charger a input volt sensor fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d184_batteryChargerAInputCurrentSensorFault` | page 3 | PCS2 ECU: d184 battery charger a input current sensor fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d185_dcdcConverterANeedsService` | page 3 | PCS2 ECU: d185 dcdc converter a needs service | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d186_batteryChargerAInternalPowerSupplyFault` | page 3 | PCS2 ECU: d186 battery charger a internal power supply fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_d187_batteryChargerModuleANeedsService` | page 3 | PCS2 ECU: d187 battery charger module a needs service | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a188_prechargeWithLowLVDetected` | page 3 | PCS2 ECU: a188 precharge with low LV detected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a192_otherPcsMia` | page 3 | PCS2 ECU: a192 other pcs mia | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a193_unknownPcsID` | page 3 | PCS2 ECU: a193 unknown pcs ID | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a194_poorGridSync` | page 3 | PCS2 ECU: a194 poor grid sync | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS2_a197_dcdcEnableLineTransient` | page 3 | PCS2 ECU: a197 dcdc enable line transient | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PCS2_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All PCS2 ECU messages (PCS2)](../../pcs2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
