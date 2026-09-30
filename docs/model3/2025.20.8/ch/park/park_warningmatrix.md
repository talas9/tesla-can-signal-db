---
layout: default
title: "PARK_warningMatrix (0x37E) — Parking assist sensors, Tesla Model 3 2025.20.8 CH CAN"
description: "Parking assist sensors message: warning matrix. Tesla Model 3 CAN bus message PARK_warningMatrix (0x37E) of Parking assist sensors, firmware 2025.20.8, 88 signals (PARK_matrixIndex, PARK_a001_s1_overTemp, PARK_a002_s1_internalFail, PARK_a003_s1_linCommError and 84 more). Bit layout, scaling, units and value tables."
---

# PARK_warningMatrix (0x37E) — Parking assist sensors, Tesla Model 3 2025.20.8 CH CAN

Parking assist sensors message: warning matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 88 signals of PARK_warningMatrix as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_warningMatrix` |
| CAN id | 0x37E (894) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 88 |

## Signals of PARK_warningMatrix

Tesla Model 3 CAN bus signals in `PARK_warningMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_matrixIndex` | selector | Parking assist sensors: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1` | plausible |
| `PARK_a001_s1_overTemp` | page 0 | Parking assist sensors: a001 s1 over temp | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a002_s1_internalFail` | page 0 | Parking assist sensors: a002 s1 internal fail | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a003_s1_linCommError` | page 0 | Parking assist sensors: a003 s1 lin comm error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a004_s1_blocked` | page 0 | Parking assist sensors: a004 s1 blocked | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a005_s1_crossTalk` | page 0 | Parking assist sensors: a005 s1 cross talk | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a006_s2_overTemp` | page 0 | Parking assist sensors: a006 s2 over temp | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a007_s2_internalFail` | page 0 | Parking assist sensors: a007 s2 internal fail | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a008_s2_linCommError` | page 0 | Parking assist sensors: a008 s2 lin comm error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a009_s2_blocked` | page 0 | Parking assist sensors: a009 s2 blocked | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a010_s2_crossTalk` | page 0 | Parking assist sensors: a010 s2 cross talk | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a011_s3_overTemp` | page 0 | Parking assist sensors: a011 s3 over temp | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a012_s3_internalFail` | page 0 | Parking assist sensors: a012 s3 internal fail | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a013_s3_linCommError` | page 0 | Parking assist sensors: a013 s3 lin comm error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a014_s3_blocked` | page 0 | Parking assist sensors: a014 s3 blocked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a015_s3_crossTalk` | page 0 | Parking assist sensors: a015 s3 cross talk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a016_s4_overTemp` | page 0 | Parking assist sensors: a016 s4 over temp | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a017_s4_internalFail` | page 0 | Parking assist sensors: a017 s4 internal fail | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a018_s4_linCommError` | page 0 | Parking assist sensors: a018 s4 lin comm error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a019_s4_blocked` | page 0 | Parking assist sensors: a019 s4 blocked | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a020_s4_crossTalk` | page 0 | Parking assist sensors: a020 s4 cross talk | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a021_s5_overTemp` | page 0 | Parking assist sensors: a021 s5 over temp | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a022_s5_internalFail` | page 0 | Parking assist sensors: a022 s5 internal fail | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a023_s5_linCommError` | page 0 | Parking assist sensors: a023 s5 lin comm error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a024_s5_blocked` | page 0 | Parking assist sensors: a024 s5 blocked | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a025_s5_crossTalk` | page 0 | Parking assist sensors: a025 s5 cross talk | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a026_s6_overTemp` | page 0 | Parking assist sensors: a026 s6 over temp | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a027_s6_internalFail` | page 0 | Parking assist sensors: a027 s6 internal fail | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a028_s6_linCommError` | page 0 | Parking assist sensors: a028 s6 lin comm error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a029_s6_blocked` | page 0 | Parking assist sensors: a029 s6 blocked | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a030_s6_crossTalk` | page 0 | Parking assist sensors: a030 s6 cross talk | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a031_s7_overTemp` | page 0 | Parking assist sensors: a031 s7 over temp | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a032_s7_internalFail` | page 0 | Parking assist sensors: a032 s7 internal fail | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a033_s7_linCommError` | page 0 | Parking assist sensors: a033 s7 lin comm error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a034_s7_blocked` | page 0 | Parking assist sensors: a034 s7 blocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a035_s7_crossTalk` | page 0 | Parking assist sensors: a035 s7 cross talk | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a036_s8_overTemp` | page 0 | Parking assist sensors: a036 s8 over temp | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a037_s8_internalFail` | page 0 | Parking assist sensors: a037 s8 internal fail | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a038_s8_linCommError` | page 0 | Parking assist sensors: a038 s8 lin comm error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a039_s8_blocked` | page 0 | Parking assist sensors: a039 s8 blocked | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a040_s8_crossTalk` | page 0 | Parking assist sensors: a040 s8 cross talk | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a041_s9_overTemp` | page 0 | Parking assist sensors: a041 s9 over temp | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a042_s9_internalFail` | page 0 | Parking assist sensors: a042 s9 internal fail | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a043_s9_linCommError` | page 0 | Parking assist sensors: a043 s9 lin comm error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a044_s9_blocked` | page 0 | Parking assist sensors: a044 s9 blocked | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a045_s9_crossTalk` | page 0 | Parking assist sensors: a045 s9 cross talk | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a046_s10_overTemp` | page 0 | Parking assist sensors: a046 s10 over temp | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a047_s10_internalFail` | page 0 | Parking assist sensors: a047 s10 internal fail | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a048_s10_linCommError` | page 0 | Parking assist sensors: a048 s10 lin comm error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a049_s10_blocked` | page 0 | Parking assist sensors: a049 s10 blocked | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a050_s10_crossTalk` | page 0 | Parking assist sensors: a050 s10 cross talk | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a051_s11_overTemp` | page 0 | Parking assist sensors: a051 s11 over temp | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a052_s11_internalFail` | page 0 | Parking assist sensors: a052 s11 internal fail | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a053_s11_linCommError` | page 0 | Parking assist sensors: a053 s11 lin comm error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a054_s11_blocked` | page 0 | Parking assist sensors: a054 s11 blocked | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a055_s11_crossTalk` | page 0 | Parking assist sensors: a055 s11 cross talk | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a056_s12_overTemp` | page 0 | Parking assist sensors: a056 s12 over temp | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a057_s12_internalFail` | page 0 | Parking assist sensors: a057 s12 internal fail | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a058_s12_linCommError` | page 0 | Parking assist sensors: a058 s12 lin comm error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a059_s12_blocked` | page 0 | Parking assist sensors: a059 s12 blocked | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a060_s12_crossTalk` | page 0 | Parking assist sensors: a060 s12 cross talk | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a061_ecuUnderVoltage` | page 1 | Parking assist sensors: a061 ecu under voltage | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a062_ecuOverVoltage` | page 1 | Parking assist sensors: a062 ecu over voltage | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a063_sensorVoltage` | page 1 | Parking assist sensors: a063 sensor voltage | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a064_ecuFault` | page 1 | Parking assist sensors: a064 ecu fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a065_crcFault` | page 1 | Parking assist sensors: a065 crc fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a066_calibrationMissing` | page 1 | Parking assist sensors: a066 calibration missing | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a067_privateCANBusOff` | page 1 | Parking assist sensors: a067 private CAN bus off | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a068_hardwareWatchDog` | page 1 | Parking assist sensors: a068 hardware watch dog | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a069_dasMia` | page 1 | Parking assist sensors: a069 das mia | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a070_sccmMia` | page 1 | Parking assist sensors: a070 sccm mia | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a071_diMia` | page 1 | Parking assist sensors: a071 di mia | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a072_epasMia` | page 1 | Parking assist sensors: a072 epas mia | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a073_epbMia` | page 1 | Parking assist sensors: a073 epb mia | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a074_espMia` | page 1 | Parking assist sensors: a074 esp mia | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a075_rcmMia` | page 1 | Parking assist sensors: a075 rcm mia | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a076_vcFrontMia` | page 1 | Parking assist sensors: a076 vc front mia | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a077_dasError` | page 1 | Parking assist sensors: a077 das error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a078_diError` | page 1 | Parking assist sensors: a078 di error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a079_epasError` | page 1 | Parking assist sensors: a079 epas error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a080_epbError` | page 1 | Parking assist sensors: a080 epb error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a081_espError` | page 1 | Parking assist sensors: a081 esp error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a082_rcmError` | page 1 | Parking assist sensors: a082 rcm error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a083_vcFrontError` | page 1 | Parking assist sensors: a083 vc front error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a084_sccmError` | page 1 | Parking assist sensors: a084 sccm error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a085_watchdogReset` | page 1 | Parking assist sensors: a085 watchdog reset | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a086_nvmFault` | page 1 | Parking assist sensors: a086 nvm fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_a087_sensorMismatchError` | page 1 | Parking assist sensors: a087 sensor mismatch error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PARK_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (27 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
