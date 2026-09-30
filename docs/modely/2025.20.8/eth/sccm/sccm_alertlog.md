---
layout: default
title: "SCCM_alertLog (0x540) — Steering column control module, Tesla Model Y 2025.20.8 ETH"
description: "Steering column control module message: alert log. Ethernet-side message SCCM_alertLog of Steering column control module for Tesla Model Y firmware 2025.20.8, 205 signals (SCCM_alertID, SCCM_alertState, SCCM_a003_debouncePosition, SCCM_a003_rawPosition and 201 more). Bit layout, scaling, units and value tables."
---

# SCCM_alertLog (0x540) — Steering column control module, Tesla Model Y 2025.20.8 ETH

Steering column control module message: alert log. This page documents the 205 signals of SCCM_alertLog as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_alertLog` |
| Ethernet-side id | 0x540 (1344) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 205 |

## Signals of SCCM_alertLog

Tesla Model Y CAN bus signals in `SCCM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_alertID` | selector | Steering column control module: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_CANBusOff`<br>2 = `a002_CANTOut`<br>3 = `a003_highBeamOpen`<br>4 = `a004_highBeamShortToGND`<br>5 = `a005_tipWipeOpen`<br>6 = `a006_tipWipeShortToGND`<br>7 = `a007_turnIndComInfo`<br>8 = `a008_turnIndInvalidTrans`<br>9 = `a009_turnIndOpen`<br>10 = `a010_turnIndShortToGnd`<br>11 = `a011_turnIndHWErr`<br>12 = `a012_turnGenErr`<br>13 = `a013_voltageHigh`<br>14 = `a014_voltageLow`<br>15 = `a015_softwareError`<br>16 = `a016_hardwareError`<br>17 = `a017_memoryError`<br>18 = `a018_angleSpeedOutOfRange`<br>19 = `a019_angleOutOfRange`<br>20 = `a020_angleInternalError`<br>21 = `a021_gearStalkSignalInvalid`<br>22 = `a022_gearStalkOpenCircuit`<br>23 = `a023_gearStalkShortCircuit`<br>24 = `a024_gearStalkGenErr`<br>25 = `a025_runTimeError`<br>26 = `a026_parkButtonInvalidSignal`<br>27 = `a027_parkButtonOpenCircuit`<br>28 = `a028_parkButtonShortToGround`<br>29 = `a029_parkButtonMalfunction`<br>61 = `a061_voltageHigh_2`<br>62 = `a062_voltageLow_2`<br>63 = `a063_angleOutOfRange_2`<br>64 = `a064_angleSpeedOutOfRange_2`<br>65 = `a065_angleNotPlausible`<br>66 = `a066_angleSpeedNotPlausible`<br>67 = `a067_CANBusOff_2`<br>68 = `a068_CANLVPowerState_LOC`<br>69 = `a069_calibrationMismatch`<br>70 = `a070_angleTrimMismatch`<br>71 = `a071_angleHallSensorError`<br>72 = `a072_spiBitErrors`<br>73 = `a073_watchdogReset`<br>74 = `a074_PLLLossOfLock`<br>75 = `a075_hardwareError_2`<br>76 = `a076_memoryError_2`<br>77 = `a077_gearAngleNotPlausible`<br>78 = `a078_ADCCalibrationError`<br>79 = `a079_chipTempOutOfRange`<br>80 = `a080_ADCSelfTestFailed`<br>81 = `a081_startupTestFailed`<br>82 = `a082_runtimeTestFailed`<br>121 = `a121_turnIndicatorAngleInvalid`<br>122 = `a122_turnIndicatorSpeedInvalid`<br>123 = `a123_turnIndicatorStuckActive`<br>124 = `a124_turnIndicatorIdleInvalid`<br>125 = `a125_turnIndicatorHallAngleMismatch`<br>126 = `a126_turnIndicatorHallMagOutOfRange` | plausible |
| `SCCM_alertState` |  | Steering column control module: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `SCCM_a003_debouncePosition` | page 3 | Steering column control module: a003 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a003_rawPosition` | page 3 | Steering column control module: a003 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a003_errorPosition` | page 3 | Steering column control module: a003 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a003_adcValue` | page 3 | Steering column control module: a003 adc value | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a004_debouncePosition` | page 4 | Steering column control module: a004 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a004_rawPosition` | page 4 | Steering column control module: a004 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a004_errorPosition` | page 4 | Steering column control module: a004 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a004_adcValue` | page 4 | Steering column control module: a004 adc value | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a005_debouncePosition` | page 5 | Steering column control module: a005 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a005_rawPosition` | page 5 | Steering column control module: a005 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a005_errorPosition` | page 5 | Steering column control module: a005 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a005_adcValue` | page 5 | Steering column control module: a005 adc value | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a006_debouncePosition` | page 6 | Steering column control module: a006 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a006_rawPosition` | page 6 | Steering column control module: a006 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a006_errorPosition` | page 6 | Steering column control module: a006 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a006_adcValue` | page 6 | Steering column control module: a006 adc value | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a007_debouncePosition` | page 7 | Steering column control module: a007 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a007_rawPosition` | page 7 | Steering column control module: a007 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a007_errorPosition` | page 7 | Steering column control module: a007 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a007_adcValue1` | page 7 | Steering column control module: a007 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a007_adcValue2` | page 7 | Steering column control module: a007 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a008_debouncePosition` | page 8 | Steering column control module: a008 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a008_rawPosition` | page 8 | Steering column control module: a008 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a008_errorPosition` | page 8 | Steering column control module: a008 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a008_adcValue1` | page 8 | Steering column control module: a008 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a008_adcValue2` | page 8 | Steering column control module: a008 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a009_debouncePosition` | page 9 | Steering column control module: a009 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a009_rawPosition` | page 9 | Steering column control module: a009 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a009_errorPosition` | page 9 | Steering column control module: a009 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a009_adcValue1` | page 9 | Steering column control module: a009 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a009_adcValue2` | page 9 | Steering column control module: a009 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a010_debouncePosition` | page 10 | Steering column control module: a010 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a010_rawPosition` | page 10 | Steering column control module: a010 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a010_errorPosition` | page 10 | Steering column control module: a010 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a010_adcValue1` | page 10 | Steering column control module: a010 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a010_adcValue2` | page 10 | Steering column control module: a010 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a011_debouncePosition` | page 11 | Steering column control module: a011 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a011_rawPosition` | page 11 | Steering column control module: a011 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a011_errorPosition` | page 11 | Steering column control module: a011 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a011_adcValue1` | page 11 | Steering column control module: a011 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a011_adcValue2` | page 11 | Steering column control module: a011 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a012_debouncePosition` | page 12 | Steering column control module: a012 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a012_rawPosition` | page 12 | Steering column control module: a012 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a012_errorPosition` | page 12 | Steering column control module: a012 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a012_adcValue1` | page 12 | Steering column control module: a012 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a012_adcValue2` | page 12 | Steering column control module: a012 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a013_voltage` | page 13 | Steering column control module: a013 voltage | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a014_voltage` | page 14 | Steering column control module: a014 voltage | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a015_intMainIndex` | page 15 | Steering column control module: a015 int main index | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a015_intSubIndex` | page 15 | Steering column control module: a015 int sub index | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a015_intMemIndex` | page 15 | Steering column control module: a015 int mem index | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a016_mainAdcTest` | page 16 | Steering column control module: a016 main adc test | 16\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a016_mainCpuTest` | page 16 | Steering column control module: a016 main cpu test | 20\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a016_wdtTest` | page 16 | Steering column control module: a016 wdt test | 24\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a016_subCpuTest` | page 16 | Steering column control module: a016 sub cpu test | 28\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a016_subAdcTest` | page 16 | Steering column control module: a016 sub adc test | 32\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_mainRamTest` | page 17 | Steering column control module: a017 main ram test | 16\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_mainRomTest` | page 17 | Steering column control module: a017 main rom test | 20\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_stackHardLimitTest` | page 17 | Steering column control module: a017 stack hard limit test | 24\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_mainDataFlashTest` | page 17 | Steering column control module: a017 main data flash test | 28\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_subRamTest` | page 17 | Steering column control module: a017 sub ram test | 32\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_subRomTest` | page 17 | Steering column control module: a017 sub rom test | 36\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_subStackHardLimitTest` | page 17 | Steering column control module: a017 sub stack hard limit test | 40\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `SCCM_a017_svError` | page 17 | Steering column control module: a017 sv error | 44\|16 | little-endian | unsigned | 1 | 0 | - | 0 to 65535 |  | plausible |
| `SCCM_a018_internalSASState` | page 18 | Steering column control module: a018 internal SAS state | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a019_internalSASState` | page 19 | Steering column control module: a019 internal SAS state | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a020_internalSASState` | page 20 | Steering column control module: a020 internal SAS state | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue1` | page 21 | Steering column control module: a021 adc value1 | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue2` | page 21 | Steering column control module: a021 adc value2 | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue3` | page 21 | Steering column control module: a021 adc value3 | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue4` | page 21 | Steering column control module: a021 adc value4 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue5` | page 21 | Steering column control module: a021 adc value5 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a021_adcValue6` | page 21 | Steering column control module: a021 adc value6 | 56\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue1` | page 22 | Steering column control module: a022 adc value1 | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue2` | page 22 | Steering column control module: a022 adc value2 | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue3` | page 22 | Steering column control module: a022 adc value3 | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue4` | page 22 | Steering column control module: a022 adc value4 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue5` | page 22 | Steering column control module: a022 adc value5 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a022_adcValue6` | page 22 | Steering column control module: a022 adc value6 | 56\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue1` | page 23 | Steering column control module: a023 adc value1 | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue2` | page 23 | Steering column control module: a023 adc value2 | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue3` | page 23 | Steering column control module: a023 adc value3 | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue4` | page 23 | Steering column control module: a023 adc value4 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue5` | page 23 | Steering column control module: a023 adc value5 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a023_adcValue6` | page 23 | Steering column control module: a023 adc value6 | 56\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue1` | page 24 | Steering column control module: a024 adc value1 | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue2` | page 24 | Steering column control module: a024 adc value2 | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue3` | page 24 | Steering column control module: a024 adc value3 | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue4` | page 24 | Steering column control module: a024 adc value4 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue5` | page 24 | Steering column control module: a024 adc value5 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a024_adcValue6` | page 24 | Steering column control module: a024 adc value6 | 56\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a025_taskState` | page 25 | Steering column control module: a025 task state | 16\|16 | little-endian | unsigned | 1 | 0 | - | 0 to 65535 |  | plausible |
| `SCCM_a026_debouncePosition` | page 26 | Steering column control module: a026 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a026_rawPosition` | page 26 | Steering column control module: a026 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a026_errorPosition` | page 26 | Steering column control module: a026 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a026_adcValue1` | page 26 | Steering column control module: a026 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a026_adcValue2` | page 26 | Steering column control module: a026 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a027_debouncePosition` | page 27 | Steering column control module: a027 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a027_rawPosition` | page 27 | Steering column control module: a027 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a027_errorPosition` | page 27 | Steering column control module: a027 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a027_adcValue1` | page 27 | Steering column control module: a027 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a027_adcValue2` | page 27 | Steering column control module: a027 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a028_debouncePosition` | page 28 | Steering column control module: a028 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a028_rawPosition` | page 28 | Steering column control module: a028 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a028_errorPosition` | page 28 | Steering column control module: a028 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a028_adcValue1` | page 28 | Steering column control module: a028 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a028_adcValue2` | page 28 | Steering column control module: a028 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a029_debouncePosition` | page 29 | Steering column control module: a029 debounce position | 16\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a029_rawPosition` | page 29 | Steering column control module: a029 raw position | 24\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a029_errorPosition` | page 29 | Steering column control module: a029 error position | 32\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a029_adcValue1` | page 29 | Steering column control module: a029 adc value1 | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a029_adcValue2` | page 29 | Steering column control module: a029 adc value2 | 48\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 255 |  | plausible |
| `SCCM_a061_voltage` | page 61 | Steering column control module: a061 voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `SCCM_a062_voltage` | page 62 | Steering column control module: a062 voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `SCCM_a063_UntrimmedAngle` | page 63 | Steering column control module: a063 untrimmed angle; raw 16383 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 5734.3 | 16383 = `SNA` | plausible |
| `SCCM_a064_Speed` | page 64 | Steering column control module: a064 speed; raw 16383 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.5 | -4096 | deg/s | -4096 to 28671.5 | 16383 = `SNA` | plausible |
| `SCCM_a065_M1RawAngleCurrent` | page 65 | Steering column control module: a065 M1 raw angle current | 16\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a065_M1RawAnglePrevious` | page 65 | Steering column control module: a065 M1 raw angle previous | 28\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a065_M2RawAngleCurrent` | page 65 | Steering column control module: a065 M2 raw angle current | 40\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a065_M2RawAnglePrevious` | page 65 | Steering column control module: a065 M2 raw angle previous | 52\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a066_M1RawAngleCurrent` | page 66 | Steering column control module: a066 M1 raw angle current | 16\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a066_M1RawAnglePrevious` | page 66 | Steering column control module: a066 M1 raw angle previous | 28\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a066_M2RawAngleCurrent` | page 66 | Steering column control module: a066 M2 raw angle current | 40\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a066_M2RawAnglePrevious` | page 66 | Steering column control module: a066 M2 raw angle previous | 52\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a071_M1LogicBISTFailed` | page 71 | Steering column control module: a071 M1 logic BIST failed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1PowerOnReset` | page 71 | Steering column control module: a071 M1 power on reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1UnderVoltage` | page 71 | Steering column control module: a071 M1 under voltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1OverVoltage` | page 71 | Steering column control module: a071 M1 over voltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1DualBitError` | page 71 | Steering column control module: a071 M1 dual bit error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1RefVoltageOutOfRange` | page 71 | Steering column control module: a071 M1 ref voltage out of range | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1RegisterParityError` | page 71 | Steering column control module: a071 M1 register parity error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1OscillatorFreqError` | page 71 | Steering column control module: a071 M1 oscillator freq error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1SignalOutOfRange` | page 71 | Steering column control module: a071 M1 signal out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1TempOutOfRange` | page 71 | Steering column control module: a071 M1 temp out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1AngleMismatch` | page 71 | Steering column control module: a071 M1 angle mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1RadiusOutOfRange` | page 71 | Steering column control module: a071 M1 radius out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2LogicBISTFailed` | page 71 | Steering column control module: a071 M2 logic BIST failed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2PowerOnReset` | page 71 | Steering column control module: a071 M2 power on reset | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2UnderVoltage` | page 71 | Steering column control module: a071 M2 under voltage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2OverVoltage` | page 71 | Steering column control module: a071 M2 over voltage | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2DualBitError` | page 71 | Steering column control module: a071 M2 dual bit error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2RefVoltageOutOfRange` | page 71 | Steering column control module: a071 M2 ref voltage out of range | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2RegisterParityError` | page 71 | Steering column control module: a071 M2 register parity error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2OscillatorFreqError` | page 71 | Steering column control module: a071 M2 oscillator freq error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2SignalOutOfRange` | page 71 | Steering column control module: a071 M2 signal out of range | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2TempOutOfRange` | page 71 | Steering column control module: a071 M2 temp out of range | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2AngleMismatch` | page 71 | Steering column control module: a071 M2 angle mismatch | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2RadiusOutOfRange` | page 71 | Steering column control module: a071 M2 radius out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M1ProcessLogicFailed` | page 71 | Steering column control module: a071 M1 process logic failed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_M2ProcessLogicFailed` | page 71 | Steering column control module: a071 M2 process logic failed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSOSCHighFreqError` | page 71 | Steering column control module: a071 TSOSC high freq error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSOSCLowFreqError` | page 71 | Steering column control module: a071 TSOSC low freq error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSOPRStatMismatch` | page 71 | Steering column control module: a071 TSOPR stat mismatch | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSCRCStatError` | page 71 | Steering column control module: a071 TSCRC stat error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSFrameStatError` | page 71 | Steering column control module: a071 TS frame stat error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSOverVoltage` | page 71 | Steering column control module: a071 TS over voltage | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSUnderVoltage` | page 71 | Steering column control module: a071 TS under voltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSPowerOnReset` | page 71 | Steering column control module: a071 TS power on reset | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSLDOStatError` | page 71 | Steering column control module: a071 TSLDO stat error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSTempOutOfRange` | page 71 | Steering column control module: a071 TS temp out of range | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSAlertIntegrityCheck` | page 71 | Steering column control module: a071 TS alert integrity check | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSMemoryCRCError` | page 71 | Steering column control module: a071 TS memory CRC error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSAFECheck` | page 71 | Steering column control module: a071 TSAFE check | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSADCCheck` | page 71 | Steering column control module: a071 TSADC check | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_TSConfigFault` | page 71 | Steering column control module: a071 TS config fault | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a072_M1CRCCalculated` | page 72 | Steering column control module: a072 M1 CRC calculated | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a072_M1CRCReceived` | page 72 | Steering column control module: a072 M1 CRC received | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a072_M2CRCCalculated` | page 72 | Steering column control module: a072 M2 CRC calculated | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a072_M2CRCReceived` | page 72 | Steering column control module: a072 M2 CRC received | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a072_TSCRCCalculated` | page 72 | Steering column control module: a072 TSCRC calculated | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a072_TSCRCReceived` | page 72 | Steering column control module: a072 TSCRC received | 36\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_a075_ClockOutOfRange` | page 75 | Steering column control module: a075 clock out of range | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a075_ExtWatchdogTestFailed` | page 75 | Steering column control module: a075 ext watchdog test failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a075_InterruptMonitorError` | page 75 | Steering column control module: a075 interrupt monitor error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a076_RAMTestFailed` | page 76 | Steering column control module: a076 RAM test failed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a076_NVMTestFailed` | page 76 | Steering column control module: a076 NVM test failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a077_M1ExpectAngleCurrent` | page 77 | Steering column control module: a077 M1 expect angle current | 16\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a077_M1ExpectAnglePrevious` | page 77 | Steering column control module: a077 M1 expect angle previous | 28\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a077_M1AngleCurrent` | page 77 | Steering column control module: a077 M1 angle current | 40\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a077_M1AnglePrevious` | page 77 | Steering column control module: a077 M1 angle previous | 52\|12 | little-endian | unsigned | 0.08791209 | 0 | deg | 0 to 360.00000855 |  | plausible |
| `SCCM_a079_ChipTemperature` | page 79 | Steering column control module: a079 chip temperature | 16\|11 | little-endian | unsigned | 0.1 | -50 | degC | -50 to 154.7 |  | plausible |
| `SCCM_a081_StartupTestStatus` | page 81 | Steering column control module: a081 startup test status | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `SCCM_a081_sCheckTestFailedData` | page 81 | Steering column control module: a081 s check test failed data | 19\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SCCM_a081_sBootTestFailedData` | page 81 | Steering column control module: a081 s boot test failed data | 27\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SCCM_a081_BISTTestFailedData` | page 81 | Steering column control module: a081 BIST test failed data | 43\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SCCM_a082_RuntimeTestStatus` | page 82 | Steering column control module: a082 runtime test status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `SCCM_a082_sCheckTestFailedData` | page 82 | Steering column control module: a082 s check test failed data | 18\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SCCM_a082_ArrayIntegrFailedData` | page 82 | Steering column control module: a082 array integr failed data | 26\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SCCM_a121_turnIndicatorStalkAngle` | page 121 | Steering column control module: a121 turn indicator stalk angle | 16\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a121_turnIndicatorHallAngle` | page 121 | Steering column control module: a121 turn indicator hall angle | 28\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a122_turnIndicatorSpeed` | page 122 | Steering column control module: a122 turn indicator speed | 16\|12 | little-endian | unsigned | 0.02 | -36 | deg/ms | -36 to 45.9 |  | plausible |
| `SCCM_a123_turnIndicatorStalkAngle` | page 123 | Steering column control module: a123 turn indicator stalk angle | 16\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a124_turnIndicatorStalkAngle` | page 124 | Steering column control module: a124 turn indicator stalk angle | 16\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a125_turnIndicatorHallAngle` | page 125 | Steering column control module: a125 turn indicator hall angle | 16\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a125_turnIndicatorVectorAngle` | page 125 | Steering column control module: a125 turn indicator vector angle | 28\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 229.5 |  | plausible |
| `SCCM_a126_turnIndicatorXVectorOutOfRange` | page 126 | Steering column control module: a126 turn indicator x vector out of range | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a126_turnIndicatorYVectorOutOfRange` | page 126 | Steering column control module: a126 turn indicator y vector out of range | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a126_turnIndicatorZVectorOutOfRange` | page 126 | Steering column control module: a126 turn indicator z vector out of range | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a126_turnIndicatorResultantOutOfRange` | page 126 | Steering column control module: a126 turn indicator resultant out of range | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a126_turnIndicatorXMagnitude` | page 126 | Steering column control module: a126 turn indicator x magnitude | 24\|8 | little-endian | unsigned | 1 | 0 | mT | 0 to 255 |  | plausible |
| `SCCM_a126_turnIndicatorYMagnitude` | page 126 | Steering column control module: a126 turn indicator y magnitude | 32\|8 | little-endian | unsigned | 1 | 0 | mT | 0 to 255 |  | plausible |
| `SCCM_a126_turnIndicatorZMagnitude` | page 126 | Steering column control module: a126 turn indicator z magnitude | 40\|8 | little-endian | unsigned | 1 | 0 | mT | 0 to 255 |  | plausible |
| `SCCM_a126_turnIndicatorResultantMagnitude` | page 126 | Steering column control module: a126 turn indicator resultant magnitude | 48\|8 | little-endian | unsigned | 1 | 0 | mT | 0 to 255 |  | plausible |

## Multiplexing

`SCCM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 3 (4 signals), page 4 (4 signals), page 5 (4 signals), page 6 (4 signals), page 7 (5 signals), page 8 (5 signals), page 9 (5 signals), page 10 (5 signals), page 11 (5 signals), page 12 (5 signals), page 13 (1 signals), page 14 (1 signals), page 15 (3 signals), page 16 (5 signals), page 17 (8 signals), page 18 (1 signals), page 19 (1 signals), page 20 (1 signals), page 21 (6 signals), page 22 (6 signals), page 23 (6 signals), page 24 (6 signals), page 25 (1 signals), page 26 (5 signals), page 27 (5 signals), page 28 (5 signals), page 29 (5 signals), page 61 (1 signals), page 62 (1 signals), page 63 (1 signals), page 64 (1 signals), page 65 (4 signals), page 66 (4 signals), page 71 (41 signals), page 72 (6 signals), page 75 (3 signals), page 76 (2 signals), page 77 (4 signals), page 79 (1 signals), page 81 (4 signals), page 82 (3 signals), page 121 (2 signals), page 122 (1 signals), page 123 (1 signals), page 124 (1 signals), page 125 (2 signals), page 126 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
