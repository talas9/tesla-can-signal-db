---
layout: default
title: "PCS_alertMatrix (0x3A4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: alert matrix. Tesla Model Y CAN bus message PCS_alertMatrix (0x3A4) of Power conversion system (on-board charger and DC-DC converter), firmware 2026.26.6.5, 117 signals (PCS_matrixIndex, PCS_a001_chgHwInputOc, PCS_a002_chgHwOutputOc, PCS_a003_chgHwInputOv and 113 more). Bit layout, scaling, units and value tables."
---

# PCS_alertMatrix (0x3A4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 117 signals of PCS_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_alertMatrix` |
| CAN id | 0x3A4 (932) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 117 |

## Signals of PCS_alertMatrix

Tesla Model Y CAN bus signals in `PCS_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_matrixIndex` | selector | Power conversion system (on-board charger and DC-DC converter): matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1` | plausible |
| `PCS_a001_chgHwInputOc` | page 0 | Power conversion system (on-board charger and DC-DC converter): a001 chg hw input oc | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a002_chgHwOutputOc` | page 0 | Power conversion system (on-board charger and DC-DC converter): a002 chg hw output oc | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a003_chgHwInputOv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a003 chg hw input ov | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a004_chgHwIntBusOv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a004 chg hw int bus ov | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a005_chgOutputOv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a005 chg output ov | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a006_chgPrechargeFailedScr` | page 0 | Power conversion system (on-board charger and DC-DC converter): a006 chg precharge failed scr | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a007_chgPhaseTempHot` | page 0 | Power conversion system (on-board charger and DC-DC converter): a007 chg phase temp hot | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a008_chgPhaseOverTemp` | page 0 | Power conversion system (on-board charger and DC-DC converter): a008 chg phase over temp | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a009_chgPfcCurrentRegulation` | page 0 | Power conversion system (on-board charger and DC-DC converter): a009 chg pfc current regulation | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a010_chgIntBusVRegulation` | page 0 | Power conversion system (on-board charger and DC-DC converter): a010 chg int bus v regulation | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a011_chgLlcCurrentRegulation` | page 0 | Power conversion system (on-board charger and DC-DC converter): a011 chg llc current regulation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a012_chgPfcIBandTracerFault` | page 0 | Power conversion system (on-board charger and DC-DC converter): a012 chg pfc i band tracer fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a013_chgPrechargeFailedBoost` | page 0 | Power conversion system (on-board charger and DC-DC converter): a013 chg precharge failed boost | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a014_chgTempRationality` | page 0 | Power conversion system (on-board charger and DC-DC converter): a014 chg temp rationality | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a015_chg12vUv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a015 chg12v uv | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a016_chgAllPhasesFaulted` | page 0 | Power conversion system (on-board charger and DC-DC converter): a016 chg all phases faulted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a017_chgWallPowerRemoval` | page 0 | Power conversion system (on-board charger and DC-DC converter): a017 chg wall power removal | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a018_chgUnknownGridConfig` | page 0 | Power conversion system (on-board charger and DC-DC converter): a018 chg unknown grid config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a019_acChargePowerLimited` | page 0 | Power conversion system (on-board charger and DC-DC converter): a019 ac charge power limited | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a020_chgEnableLineMismatch` | page 0 | Power conversion system (on-board charger and DC-DC converter): a020 chg enable line mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a021_hvpMia` | page 0 | Power conversion system (on-board charger and DC-DC converter): a021 hvp mia | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a022_bmsMia` | page 0 | Power conversion system (on-board charger and DC-DC converter): a022 bms mia | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a023_cpMia` | page 0 | Power conversion system (on-board charger and DC-DC converter): a023 cp mia | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a024_vcfrontMia` | page 0 | Power conversion system (on-board charger and DC-DC converter): a024 vcfront mia | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a025_cpu2Malfunction` | page 0 | Power conversion system (on-board charger and DC-DC converter): a025 cpu2 malfunction | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a026_watchdogAlarmed` | page 0 | Power conversion system (on-board charger and DC-DC converter): a026 watchdog alarmed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a027_chgInsufficientCooling` | page 0 | Power conversion system (on-board charger and DC-DC converter): a027 chg insufficient cooling | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a028_chgOutputUv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a028 chg output uv | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a029_chgPowerRationality` | page 0 | Power conversion system (on-board charger and DC-DC converter): a029 chg power rationality | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a030_canRationality` | page 0 | Power conversion system (on-board charger and DC-DC converter): a030 can rationality | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a031_uiMia` | page 0 | Power conversion system (on-board charger and DC-DC converter): a031 ui mia | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a032_excessiveGridTransientsDetected` | page 0 | Power conversion system (on-board charger and DC-DC converter): a032 excessive grid transients detected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a033_hvBusUv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a033 hv bus uv | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a034_hvBusOv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a034 hv bus ov | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a035_lvBusUv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a035 lv bus uv | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a036_lvBusOv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a036 lv bus ov | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a037_resonantTankOc` | page 0 | Power conversion system (on-board charger and DC-DC converter): a037 resonant tank oc | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a038_claFaulted` | page 0 | Power conversion system (on-board charger and DC-DC converter): a038 cla faulted | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a039_sdModuleClkFault` | page 0 | Power conversion system (on-board charger and DC-DC converter): a039 sd module clk fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a040_dcdcMaxPowerReached` | page 0 | Power conversion system (on-board charger and DC-DC converter): a040 dcdc max power reached | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a041_dcdcOverTemp` | page 0 | Power conversion system (on-board charger and DC-DC converter): a041 dcdc over temp | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a042_dcdcEnableLineMismatch` | page 0 | Power conversion system (on-board charger and DC-DC converter): a042 dcdc enable line mismatch | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a043_hvBusPrechargeFailure` | page 0 | Power conversion system (on-board charger and DC-DC converter): a043 hv bus precharge failure | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a044_12vSupportRegulation` | page 0 | Power conversion system (on-board charger and DC-DC converter): a044 12v support regulation | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a045_hvBusLowImpedance` | page 0 | Power conversion system (on-board charger and DC-DC converter): a045 hv bus low impedance | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a046_hvBusHighImpedence` | page 0 | Power conversion system (on-board charger and DC-DC converter): a046 hv bus high impedence | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a047_bootloaderCrcMismatch` | page 0 | Power conversion system (on-board charger and DC-DC converter): a047 bootloader crc mismatch | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a048_softwareAssertion` | page 0 | Power conversion system (on-board charger and DC-DC converter): a048 software assertion | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a049_dcdcTempRationality` | page 0 | Power conversion system (on-board charger and DC-DC converter): a049 dcdc temp rationality | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a050_dcdc12VsupportFaulted` | page 0 | Power conversion system (on-board charger and DC-DC converter): a050 dcdc12 vsupport faulted | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a051_chgIntBusUv` | page 0 | Power conversion system (on-board charger and DC-DC converter): a051 chg int bus uv | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a052_acVoltageNotPresent` | page 0 | Power conversion system (on-board charger and DC-DC converter): a052 ac voltage not present | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a053_chgInputVDropHigh` | page 0 | Power conversion system (on-board charger and DC-DC converter): a053 chg input v drop high | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a054_chgInputVDropTooHigh` | page 0 | Power conversion system (on-board charger and DC-DC converter): a054 chg input v drop too high | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a055_chgLineImpedanceHigh` | page 0 | Power conversion system (on-board charger and DC-DC converter): a055 chg line impedance high | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a056_chgLineImpedanceTooHigh` | page 0 | Power conversion system (on-board charger and DC-DC converter): a056 chg line impedance too high | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a057_chgInputOverFreq` | page 0 | Power conversion system (on-board charger and DC-DC converter): a057 chg input over freq | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a058_chgInputUnderFreq` | page 0 | Power conversion system (on-board charger and DC-DC converter): a058 chg input under freq | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a059_chgInputOvRms` | page 0 | Power conversion system (on-board charger and DC-DC converter): a059 chg input ov rms | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a060_chgInputOvPeak` | page 0 | Power conversion system (on-board charger and DC-DC converter): a060 chg input ov peak | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a061_chgVLineRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a061 chg v line rationality | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a062_chgILineRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a062 chg i line rationality | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a063_chgVOutRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a063 chg v out rationality | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a064_chgIOutRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a064 chg i out rationality | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a065_chgPllNotLocked` | page 1 | Power conversion system (on-board charger and DC-DC converter): a065 chg pll not locked | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a066_dcdcHvRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a066 dcdc hv rationality | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a067_dcdcLvRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a067 dcdc lv rationality | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a068_dcdcTankvRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a068 dcdc tankv rationality | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a069_chgPfcLineDidt` | page 1 | Power conversion system (on-board charger and DC-DC converter): a069 chg pfc line didt | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a070_chgPfcLineDvdt` | page 1 | Power conversion system (on-board charger and DC-DC converter): a070 chg pfc line dvdt | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a071_chgPfcILoopRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a071 chg pfc i loop rationality | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a072_cpu2ClaStopped` | page 1 | Power conversion system (on-board charger and DC-DC converter): a072 cpu2 cla stopped | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a073_unexpectedAcInputVoltage` | page 1 | Power conversion system (on-board charger and DC-DC converter): a073 unexpected ac input voltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a074_hvBusDischargeFailure` | page 1 | Power conversion system (on-board charger and DC-DC converter): a074 hv bus discharge failure | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a075_hvBusDischargeTimeout` | page 1 | Power conversion system (on-board charger and DC-DC converter): a075 hv bus discharge timeout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a076_dcdcEnDeassertedErr` | page 1 | Power conversion system (on-board charger and DC-DC converter): a076 dcdc en deasserted err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a077_microGridWobbleDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a077 micro grid wobble detected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a078_chgStopDcdcTooHot` | page 1 | Power conversion system (on-board charger and DC-DC converter): a078 chg stop dcdc too hot | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a079_eepromOperationError` | page 1 | Power conversion system (on-board charger and DC-DC converter): a079 eeprom operation error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a080_damagedPhaseDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a080 damaged phase detected | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a081_dcdcPchgTimeout` | page 1 | Power conversion system (on-board charger and DC-DC converter): a081 dcdc pchg timeout | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a082_dcdcPchgUnsafeDiVoltage` | page 1 | Power conversion system (on-board charger and DC-DC converter): a082 dcdc pchg unsafe di voltage | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a083_triggerOdin` | page 1 | Signal reported by Power conversion system (on-board charger and DC-DC converter) | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a084_vDropFastInParasiticDiodeRegion` | page 1 | Power conversion system (on-board charger and DC-DC converter): a084 v drop fast in parasitic diode region | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a085_dcdcFetsNotSwitching` | page 1 | Power conversion system (on-board charger and DC-DC converter): a085 dcdc fets not switching | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a086_dcdcInsufficientCooling` | page 1 | Power conversion system (on-board charger and DC-DC converter): a086 dcdc insufficient cooling | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a087_nvramRecordStatusError` | page 1 | Power conversion system (on-board charger and DC-DC converter): a087 nvram record status error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a088_gridFreqDroopDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a088 grid freq droop detected | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a089_hvBusDischargeIrrational` | page 1 | Power conversion system (on-board charger and DC-DC converter): a089 hv bus discharge irrational | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a090_expectedAcVoltageSourceMissing` | page 1 | Power conversion system (on-board charger and DC-DC converter): a090 expected ac voltage source missing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a091_chgIntBusRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a091 chg int bus rationality | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a092_chgPowerLimitedByBusRipple` | page 1 | Power conversion system (on-board charger and DC-DC converter): a092 chg power limited by bus ripple | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a093_powerRailRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a093 power rail rationality | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a094_pcsDcdcNeedService` | page 1 | Power conversion system (on-board charger and DC-DC converter): a094 pcs dcdc need service | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a095_dcdcSensorlessModeActive` | page 1 | Power conversion system (on-board charger and DC-DC converter): a095 dcdc sensorless mode active | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a096_microGridOverLoaded` | page 1 | Power conversion system (on-board charger and DC-DC converter): a096 micro grid over loaded | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a097_rebootPhaseDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a097 reboot phase detected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a098_gridFreqDroopDetectedSilent` | page 1 | Power conversion system (on-board charger and DC-DC converter): a098 grid freq droop detected silent | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a099_microGridOverLoadedSilent` | page 1 | Power conversion system (on-board charger and DC-DC converter): a099 micro grid over loaded silent | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a100_suspectedViperChipIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): a100 suspected viper chip issue | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a101_phMachineModelIrrational` | page 1 | Power conversion system (on-board charger and DC-DC converter): a101 ph machine model irrational | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a102_resetWithDCDCCmdAsserted` | page 1 | Power conversion system (on-board charger and DC-DC converter): a102 reset with DCDC cmd asserted | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a103_pchgWithLowLvDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a103 pchg with low lv detected | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a104_ambientTempRationality` | page 1 | Power conversion system (on-board charger and DC-DC converter): a104 ambient temp rationality | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a105_redundantVoltageSourceIrrational` | page 1 | Power conversion system (on-board charger and DC-DC converter): a105 redundant voltage source irrational | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a106_clockSourceNotFromExternalCrystal` | page 1 | Power conversion system (on-board charger and DC-DC converter): a106 clock source not from external crystal | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a107_vcPcsDCDCInterfaceMia` | page 1 | Power conversion system (on-board charger and DC-DC converter): a107 vc pcs DCDC interface mia | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a108_misconfigurationDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a108 misconfiguration detected | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_a109_deltaChargingL2L3SwappedDetected` | page 1 | Power conversion system (on-board charger and DC-DC converter): a109 delta charging L2 L3 swapped detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d110_dcdcNeedsService` | page 1 | Power conversion system (on-board charger and DC-DC converter): d110 dcdc needs service | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d111_batteryChargerPowerLimited` | page 1 | Power conversion system (on-board charger and DC-DC converter): d111 battery charger power limited | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d112_logicHardwareIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): d112 logic hardware issue | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d113_dcdcConverterTempSensorAIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): d113 dcdc converter temp sensor a issue | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d114_dcdcConverterVoltSensorAIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): d114 dcdc converter volt sensor a issue | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d115_dcdcConverterTempSensorBIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): d115 dcdc converter temp sensor b issue | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_d116_dcdcConverterVoltSensorBIssue` | page 1 | Power conversion system (on-board charger and DC-DC converter): d116 dcdc converter volt sensor b issue | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`PCS_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (56 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
