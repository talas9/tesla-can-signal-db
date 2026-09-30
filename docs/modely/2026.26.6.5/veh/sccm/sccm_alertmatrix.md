---
layout: default
title: "SCCM_alertMatrix (0x54F) — Steering column control module, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Steering column control module message: alert matrix. Tesla Model Y CAN bus message SCCM_alertMatrix (0x54F) of Steering column control module, firmware 2026.26.6.5, 58 signals (SCCM_matrixIndex, SCCM_a001_CANBusOff, SCCM_a002_CANTOut, SCCM_a003_highBeamOpen and 54 more). Bit layout, scaling, units and value tables."
---

# SCCM_alertMatrix (0x54F) — Steering column control module, Tesla Model Y 2026.26.6.5 VEH CAN

Steering column control module message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 58 signals of SCCM_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_alertMatrix` |
| CAN id | 0x54F (1359) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 58 |

## Signals of SCCM_alertMatrix

Tesla Model Y CAN bus signals in `SCCM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_matrixIndex` | selector | Steering column control module: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `SCCM_a001_CANBusOff` | page 0 | Steering column control module: a001 CAN bus off | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a002_CANTOut` | page 0 | Steering column control module: a002 CANT out | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a003_highBeamOpen` | page 0 | Steering column control module: a003 high beam open | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a004_highBeamShortToGND` | page 0 | Steering column control module: a004 high beam short to GND | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a005_tipWipeOpen` | page 0 | Steering column control module: a005 tip wipe open | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a006_tipWipeShortToGND` | page 0 | Steering column control module: a006 tip wipe short to GND | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a007_turnIndComInfo` | page 0 | Steering column control module: a007 turn ind com info | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a008_turnIndInvalidTrans` | page 0 | Steering column control module: a008 turn ind invalid trans | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a009_turnIndOpen` | page 0 | Steering column control module: a009 turn ind open | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a010_turnIndShortToGnd` | page 0 | Steering column control module: a010 turn ind short to gnd | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a011_turnIndHWErr` | page 0 | Steering column control module: a011 turn ind HW err | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a012_turnGenErr` | page 0 | Steering column control module: a012 turn gen err | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a013_voltageHigh` | page 0 | Steering column control module: a013 voltage high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a014_voltageLow` | page 0 | Steering column control module: a014 voltage low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a015_softwareError` | page 0 | Steering column control module: a015 software error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a016_hardwareError` | page 0 | Steering column control module: a016 hardware error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a017_memoryError` | page 0 | Steering column control module: a017 memory error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a018_angleSpeedOutOfRange` | page 0 | Steering column control module: a018 angle speed out of range | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a019_angleOutOfRange` | page 0 | Steering column control module: a019 angle out of range | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a020_angleInternalError` | page 0 | Steering column control module: a020 angle internal error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a021_gearStalkSignalInvalid` | page 0 | Steering column control module: a021 gear stalk signal invalid | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a022_gearStalkOpenCircuit` | page 0 | Steering column control module: a022 gear stalk open circuit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a023_gearStalkShortCircuit` | page 0 | Steering column control module: a023 gear stalk short circuit | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a024_gearStalkGenErr` | page 0 | Steering column control module: a024 gear stalk gen err | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a025_runTimeError` | page 0 | Steering column control module: a025 run time error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a026_parkButtonInvalidSignal` | page 0 | Steering column control module: a026 park button invalid signal | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a027_parkButtonOpenCircuit` | page 0 | Steering column control module: a027 park button open circuit | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a028_parkButtonShortToGround` | page 0 | Steering column control module: a028 park button short to ground | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a029_parkButtonMalfunction` | page 0 | Steering column control module: a029 park button malfunction | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a061_voltageHigh_2` | page 1 | Steering column control module: a061 voltage high 2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a062_voltageLow_2` | page 1 | Steering column control module: a062 voltage low 2 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a063_angleOutOfRange_2` | page 1 | Steering column control module: a063 angle out of range 2 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a064_angleSpeedOutOfRange_2` | page 1 | Steering column control module: a064 angle speed out of range 2 | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a065_angleNotPlausible` | page 1 | Steering column control module: a065 angle not plausible | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a066_angleSpeedNotPlausible` | page 1 | Steering column control module: a066 angle speed not plausible | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a067_CANBusOff_2` | page 1 | Steering column control module: a067 CAN bus off 2 | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a068_CANLVPowerState_LOC` | page 1 | Steering column control module: a068 CANLV power state LOC | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a069_calibrationMismatch` | page 1 | Steering column control module: a069 calibration mismatch | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a070_angleTrimMismatch` | page 1 | Steering column control module: a070 angle trim mismatch | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a071_angleHallSensorError` | page 1 | Steering column control module: a071 angle hall sensor error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a072_spiBitErrors` | page 1 | Steering column control module: a072 spi bit errors | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a073_watchdogReset` | page 1 | Steering column control module: a073 watchdog reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a074_PLLLossOfLock` | page 1 | Steering column control module: a074 PLL loss of lock | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a075_hardwareError_2` | page 1 | Steering column control module: a075 hardware error 2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a076_memoryError_2` | page 1 | Steering column control module: a076 memory error 2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a077_gearAngleNotPlausible` | page 1 | Steering column control module: a077 gear angle not plausible | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a078_ADCCalibrationError` | page 1 | Steering column control module: a078 ADC calibration error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a079_chipTempOutOfRange` | page 1 | Steering column control module: a079 chip temp out of range | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a080_ADCSelfTestFailed` | page 1 | Steering column control module: a080 ADC self test failed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a081_startupTestFailed` | page 1 | Steering column control module: a081 startup test failed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a082_runtimeTestFailed` | page 1 | Steering column control module: a082 runtime test failed | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a121_turnIndicatorAngleInvalid` | page 2 | Steering column control module: a121 turn indicator angle invalid | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a122_turnIndicatorSpeedInvalid` | page 2 | Steering column control module: a122 turn indicator speed invalid | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a123_turnIndicatorStuckActive` | page 2 | Steering column control module: a123 turn indicator stuck active | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a124_turnIndicatorIdleInvalid` | page 2 | Steering column control module: a124 turn indicator idle invalid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a125_turnIndicatorHallAngleMismatch` | page 2 | Steering column control module: a125 turn indicator hall angle mismatch | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCCM_a126_turnIndicatorHallMagOutOfRange` | page 2 | Steering column control module: a126 turn indicator hall mag out of range | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`SCCM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (29 signals), page 1 (22 signals), page 2 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
