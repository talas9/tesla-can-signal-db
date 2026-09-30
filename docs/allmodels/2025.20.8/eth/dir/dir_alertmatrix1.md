---
layout: default
title: "DIR_alertMatrix1 (0x3A7) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: alert matrix1. Ethernet-side message DIR_alertMatrix1 of Rear drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 61 signals (DIR_a001_hwPhaseAgateDrive, DIR_a002_hwPhaseBgateDrive, DIR_a003_hwPhaseCgateDrive, DIR_a004_hwPhaseApeak and 57 more). Bit layout, scaling, units and value tables."
---

# DIR_alertMatrix1 (0x3A7) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Rear drive inverter message: alert matrix1. This page documents the 61 signals of DIR_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_alertMatrix1` |
| Ethernet-side id | 0x3A7 (935) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 61 |

## Signals of DIR_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `DIR_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_a001_hwPhaseAgateDrive` | Rear drive inverter: a001 hw phase agate drive | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a002_hwPhaseBgateDrive` | Rear drive inverter: a002 hw phase bgate drive | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a003_hwPhaseCgateDrive` | Rear drive inverter: a003 hw phase cgate drive | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a004_hwPhaseApeak` | Rear drive inverter: a004 hw phase apeak | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a005_hwPhaseBpeak` | Rear drive inverter: a005 hw phase bpeak | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a006_hwPhaseCpeak` | Rear drive inverter: a006 hw phase cpeak | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a007_statorAnomalyDetected` | Rear drive inverter: a007 stator anomaly detected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a008_hwEncoderA` | Rear drive inverter: a008 hw encoder a | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a009_hwEncoderB` | Rear drive inverter: a009 hw encoder b | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a010_unintendedReset` | Rear drive inverter: a010 unintended reset | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a011_swPowerStageNotReady` | Rear drive inverter: a011 sw power stage not ready | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a012_hvilNotClosed` | Rear drive inverter: a012 hvil not closed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a013_eccError` | Rear drive inverter: a013 ecc error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a014_activeDamping` | Rear drive inverter: a014 active damping | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a015_mechSafeStateAnomaly` | Rear drive inverter: a015 mech safe state anomaly | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a016_safeStateApplied` | Rear drive inverter: a016 safe state applied | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a017_hwPedalMonitor` | Rear drive inverter: a017 hw pedal monitor | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a018_hwLVSupplyUV` | Rear drive inverter: a018 hw LV supply UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a020_hwMotorEncoder` | Rear drive inverter: a020 hw motor encoder | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a021_hwBusOV` | Rear drive inverter: a021 hw bus OV | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a022_hw5vSupplyUV` | Rear drive inverter: a022 hw5v supply UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a024_selfTest` | Rear drive inverter: a024 self test | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a025_phaseApeak` | Rear drive inverter: a025 phase apeak | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a026_phaseBpeak` | Rear drive inverter: a026 phase bpeak | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a027_phaseCpeak` | Rear drive inverter: a027 phase cpeak | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a028_phaseArms` | Rear drive inverter: a028 phase arms | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a029_phaseBrms` | Rear drive inverter: a029 phase brms | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a030_phaseCrms` | Rear drive inverter: a030 phase crms | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a031_phaseAcurrentOffset` | Rear drive inverter: a031 phase acurrent offset | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a032_phaseBcurrentOffset` | Rear drive inverter: a032 phase bcurrent offset | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a033_phaseAcurrentSensor` | Rear drive inverter: a033 phase acurrent sensor | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a034_phaseBcurrentSensor` | Rear drive inverter: a034 phase bcurrent sensor | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a035_phaseCurrentBalance` | Rear drive inverter: a035 phase current balance | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a036_busOV` | Rear drive inverter: a036 bus OV | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a037_busUV` | Rear drive inverter: a037 bus UV | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a038_busVsensor` | Rear drive inverter: a038 bus vsensor | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a039_exceptionUndefinedInstruction` | Rear drive inverter: a039 exception undefined instruction | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a040_difMIA` | Rear drive inverter: a040 dif MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a041_sdcMIA` | Rear drive inverter: a041 sdc MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a042_inletSensor` | Rear drive inverter: a042 inlet sensor | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a043_outletOT` | Rear drive inverter: a043 outlet OT | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a044_outletUT` | Rear drive inverter: a044 outlet UT | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a045_outletSensor` | Rear drive inverter: a045 outlet sensor | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a046_statorOT` | Rear drive inverter: a046 stator OT | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a047_statorSensor1` | Rear drive inverter: a047 stator sensor1 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a048_statorSensor2` | Rear drive inverter: a048 stator sensor2 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a049_statorSensorDiff` | Rear drive inverter: a049 stator sensor diff | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a050_noStatorSensor` | Rear drive inverter: a050 no stator sensor | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a052_dirMIA` | Rear drive inverter: a052 dir MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a053_unexpectedLatchState` | Rear drive inverter: a053 unexpected latch state | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a054_driveInverterOT` | Rear drive inverter: a054 drive inverter OT | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a055_trqCrossCheck` | Rear drive inverter: a055 trq cross check | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a056_ambientOT` | Rear drive inverter: a056 ambient OT | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a057_ambientUT` | Rear drive inverter: a057 ambient UT | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a058_ambientSensor` | Rear drive inverter: a058 ambient sensor | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a059_heatsinkOT` | Rear drive inverter: a059 heatsink OT | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a060_heatsinkUT` | Rear drive inverter: a060 heatsink UT | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a061_heatsinkSensor` | Rear drive inverter: a061 heatsink sensor | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a062_systemLimpMode` | Rear drive inverter: a062 system limp mode | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a063_bbMIA` | Rear drive inverter: a063 bb MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a064_torqueIntervention` | Rear drive inverter: a064 torque intervention | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
