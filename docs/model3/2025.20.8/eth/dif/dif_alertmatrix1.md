---
layout: default
title: "DIF_alertMatrix1 (0x356) — Front drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Front drive inverter message: alert matrix1. Ethernet-side message DIF_alertMatrix1 of Front drive inverter for Tesla Model 3 firmware 2025.20.8, 61 signals (DIF_a001_hwPhaseAgateDrive, DIF_a002_hwPhaseBgateDrive, DIF_a003_hwPhaseCgateDrive, DIF_a004_hwPhaseApeak and 57 more). Bit layout, scaling, units and value tables."
---

# DIF_alertMatrix1 (0x356) — Front drive inverter, Tesla Model 3 2025.20.8 ETH

Front drive inverter message: alert matrix1. This page documents the 61 signals of DIF_alertMatrix1 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_alertMatrix1` |
| Ethernet-side id | 0x356 (854) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 61 |

## Signals of DIF_alertMatrix1

Tesla Model 3 CAN bus signals in `DIF_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_a001_hwPhaseAgateDrive` | Front drive inverter: a001 hw phase agate drive | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_hwPhaseBgateDrive` | Front drive inverter: a002 hw phase bgate drive | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_hwPhaseCgateDrive` | Front drive inverter: a003 hw phase cgate drive | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a004_hwPhaseApeak` | Front drive inverter: a004 hw phase apeak | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a005_hwPhaseBpeak` | Front drive inverter: a005 hw phase bpeak | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a006_hwPhaseCpeak` | Front drive inverter: a006 hw phase cpeak | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a007_statorAnomalyDetected` | Front drive inverter: a007 stator anomaly detected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a008_hwEncoderA` | Front drive inverter: a008 hw encoder a | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a009_hwEncoderB` | Front drive inverter: a009 hw encoder b | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_unintendedReset` | Front drive inverter: a010 unintended reset | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_swPowerStageNotReady` | Front drive inverter: a011 sw power stage not ready | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a012_hvilNotClosed` | Front drive inverter: a012 hvil not closed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a013_eccError` | Front drive inverter: a013 ecc error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a014_activeDamping` | Front drive inverter: a014 active damping | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a015_mechSafeStateAnomaly` | Front drive inverter: a015 mech safe state anomaly | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_safeStateApplied` | Front drive inverter: a016 safe state applied | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a017_hwPedalMonitor` | Front drive inverter: a017 hw pedal monitor | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a018_hwLVSupplyUV` | Front drive inverter: a018 hw LV supply UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a020_hwMotorEncoder` | Front drive inverter: a020 hw motor encoder | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a021_hwBusOV` | Front drive inverter: a021 hw bus OV | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a022_hw5vSupplyUV` | Front drive inverter: a022 hw5v supply UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a024_selfTest` | Front drive inverter: a024 self test | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a025_phaseApeak` | Front drive inverter: a025 phase apeak | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a026_phaseBpeak` | Front drive inverter: a026 phase bpeak | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a027_phaseCpeak` | Front drive inverter: a027 phase cpeak | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a028_phaseArms` | Front drive inverter: a028 phase arms | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a029_phaseBrms` | Front drive inverter: a029 phase brms | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a030_phaseCrms` | Front drive inverter: a030 phase crms | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a031_phaseAcurrentOffset` | Front drive inverter: a031 phase acurrent offset | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a032_phaseBcurrentOffset` | Front drive inverter: a032 phase bcurrent offset | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a033_phaseAcurrentSensor` | Front drive inverter: a033 phase acurrent sensor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a034_phaseBcurrentSensor` | Front drive inverter: a034 phase bcurrent sensor | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_phaseCurrentBalance` | Front drive inverter: a035 phase current balance | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a036_busOV` | Front drive inverter: a036 bus OV | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a037_busUV` | Front drive inverter: a037 bus UV | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a038_busVsensor` | Front drive inverter: a038 bus vsensor | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a039_exceptionUndefinedInstruction` | Front drive inverter: a039 exception undefined instruction | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_difMIA` | Front drive inverter: a040 dif MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a041_sdcMIA` | Front drive inverter: a041 sdc MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a042_inletSensor` | Front drive inverter: a042 inlet sensor | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a043_outletOT` | Front drive inverter: a043 outlet OT | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a044_outletUT` | Front drive inverter: a044 outlet UT | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a045_outletSensor` | Front drive inverter: a045 outlet sensor | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a046_statorOT` | Front drive inverter: a046 stator OT | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a047_statorSensor1` | Front drive inverter: a047 stator sensor1 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a048_statorSensor2` | Front drive inverter: a048 stator sensor2 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a049_statorSensorDiff` | Front drive inverter: a049 stator sensor diff | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a050_noStatorSensor` | Front drive inverter: a050 no stator sensor | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_dirMIA` | Front drive inverter: a052 dir MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a053_unexpectedLatchState` | Front drive inverter: a053 unexpected latch state | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a054_driveInverterOT` | Front drive inverter: a054 drive inverter OT | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a055_trqCrossCheck` | Front drive inverter: a055 trq cross check | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a056_ambientOT` | Front drive inverter: a056 ambient OT | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a057_ambientUT` | Front drive inverter: a057 ambient UT | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a058_ambientSensor` | Front drive inverter: a058 ambient sensor | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a059_heatsinkOT` | Front drive inverter: a059 heatsink OT | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a060_heatsinkUT` | Front drive inverter: a060 heatsink UT | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a061_heatsinkSensor` | Front drive inverter: a061 heatsink sensor | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a062_systemLimpMode` | Front drive inverter: a062 system limp mode | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a063_bbMIA` | Front drive inverter: a063 bb MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a064_torqueIntervention` | Front drive inverter: a064 torque intervention | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
