---
layout: default
title: "RADC_alertMatrix0 (0x502) — Radar, Tesla Model Y 2025.20.8 CH CAN"
description: "Radar message: alert matrix0. Tesla Model Y CAN bus message RADC_alertMatrix0 (0x502) of Radar, firmware 2025.20.8, 55 signals (RADC_a001_can1BusOff, RADC_a002_ecuAdcError, RADC_a003_ecuBistDisabled, RADC_a004_ecuCrcHwError and 51 more). Bit layout, scaling, units and value tables."
---

# RADC_alertMatrix0 (0x502) — Radar, Tesla Model Y 2025.20.8 CH CAN

Radar message: alert matrix0; frame length from the layout, not yet observed on a vehicle bus. This page documents the 55 signals of RADC_alertMatrix0 as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RADC_alertMatrix0` |
| CAN id | 0x502 (1282) |
| ECU | [Radar](../../radc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RADC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 55 |

## Signals of RADC_alertMatrix0

Tesla Model Y CAN bus signals in `RADC_alertMatrix0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RADC_a001_can1BusOff` | Radar: a001 can1 bus off | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a002_ecuAdcError` | Radar: a002 ecu adc error | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a003_ecuBistDisabled` | Radar: a003 ecu bist disabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a004_ecuCrcHwError` | Radar: a004 ecu crc hw error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a005_ecuEcuMError` | Radar: a005 ecu ecu m error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a006_ecuFimError` | Radar: a006 ecu fim error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a007_ecuGptCheckError` | Radar: a007 ecu gpt check error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a008_ecuHwSwInterlock` | Radar: a008 ecu hw sw interlock | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a009_plantModeActive` | Radar: a009 plant mode active | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a010_ecuIoHwAbError` | Radar: a010 ecu io hw ab error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a011_ecuMcemError` | Radar: a011 ecu mcem error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a012_ecuSpiError` | Radar: a012 ecu spi error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a013_ecuWdgError` | Radar: a013 ecu wdg error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a014_fctSelfTestNotDone` | Radar: a014 fct self test not done | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a015_fctSenInterference` | Radar: a015 fct sen interference | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a016_adcOverVolt` | Radar: a016 adc over volt | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a017_adcUnderVolt` | Radar: a017 adc under volt | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a018_internalHardwareFault` | Radar: a018 internal hardware fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a019_internalSoftwareFault` | Radar: a019 internal software fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a020_overTemp` | Radar: a020 over temp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a021_overTempCrit` | Radar: a021 over temp crit | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a022_tempImplausible` | Radar: a022 temp implausible | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a023_underTemp` | Radar: a023 under temp | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a024_underTempCrit` | Radar: a024 under temp crit | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a025_overVoltage` | Radar: a025 over voltage | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a026_underVoltage` | Radar: a026 under voltage | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a027_nvmFailure` | Radar: a027 nvm failure | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a028_rfChipError` | Radar: a028 rf chip error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a029_rhcError` | Radar: a029 rhc error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a030_rspError` | Radar: a030 rsp error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a031_sensorMisaligned` | Radar: a031 sensor misaligned | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a032_sensorBlocked` | Radar: a032 sensor blocked | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a033_sensorNeverAligned` | Radar: a033 sensor never aligned | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a034_vehDynamicsError` | Radar: a034 veh dynamics error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a035_vinMIA` | Radar: a035 vin MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a036_carConfigMIA` | Radar: a036 car config MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a037_inertialSignalsMIA` | Radar: a037 inertial signals MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a038_steeringWheelAngleMIA` | Radar: a038 steering wheel angle MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a039_vehicleStateMIA` | Radar: a039 vehicle state MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a040_wheelSpeedsMIA` | Radar: a040 wheel speeds MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a041_vinErr` | Radar: a041 vin err | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a042_carConfigErr` | Radar: a042 car config err | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a043_inertialSignalsErr` | Radar: a043 inertial signals err | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a044_steeringWheelAngleErr` | Radar: a044 steering wheel angle err | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a045_vehicleStateErr` | Radar: a045 vehicle state err | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a046_wheelSpeedsErr` | Radar: a046 wheel speeds err | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a047_mismatchChassisType` | Radar: a047 mismatch chassis type | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a048_mismatchAirSuspension` | Radar: a048 mismatch air suspension | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a049_mismatchFourWheelDrive` | Radar: a049 mismatch four wheel drive | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a050_mismatchCountry` | Radar: a050 mismatch country | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a051_mismatchEPASType` | Radar: a051 mismatch EPAS type | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a052_mismatcRadPos` | Radar: a052 mismatc rad pos | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a053_emError` | Radar: a053 em error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a054_blockageInfo_Frame_1` | Radar: a054 blockage info frame 1 | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RADC_a055_blockageInfo_Frame_2` | Radar: a055 blockage info frame 2 | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Radar messages (RADC)](../../radc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
