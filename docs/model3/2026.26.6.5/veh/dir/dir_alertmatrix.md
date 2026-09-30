---
layout: default
title: "DIR_alertMatrix (0x3A7) — Rear drive inverter, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Rear drive inverter message: alert matrix. Tesla Model 3 CAN bus message DIR_alertMatrix (0x3A7) of Rear drive inverter, firmware 2026.26.6.5, 188 signals (DIR_matrixIndex, DIR_a001_hwPhaseAgateDrive, DIR_a002_hwPhaseBgateDrive, DIR_a003_hwPhaseCgateDrive and 184 more). Bit layout, scaling, units and value tables."
---

# DIR_alertMatrix (0x3A7) — Rear drive inverter, Tesla Model 3 2026.26.6.5 VEH CAN

Rear drive inverter message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 188 signals of DIR_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_alertMatrix` |
| CAN id | 0x3A7 (935) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 188 |

## Signals of DIR_alertMatrix

Tesla Model 3 CAN bus signals in `DIR_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_matrixIndex` | selector | Rear drive inverter: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4` | plausible |
| `DIR_a001_hwPhaseAgateDrive` | page 0 | Rear drive inverter: a001 hw phase agate drive | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a002_hwPhaseBgateDrive` | page 0 | Rear drive inverter: a002 hw phase bgate drive | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a003_hwPhaseCgateDrive` | page 0 | Rear drive inverter: a003 hw phase cgate drive | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a004_hwPhaseApeak` | page 0 | Rear drive inverter: a004 hw phase apeak | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a005_hwPhaseBpeak` | page 0 | Rear drive inverter: a005 hw phase bpeak | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a006_hwPhaseCpeak` | page 0 | Rear drive inverter: a006 hw phase cpeak | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a007_statorAnomalyDetected` | page 0 | Rear drive inverter: a007 stator anomaly detected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a008_hwEncoderA` | page 0 | Rear drive inverter: a008 hw encoder a | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a009_hwEncoderB` | page 0 | Rear drive inverter: a009 hw encoder b | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a010_unintendedReset` | page 0 | Rear drive inverter: a010 unintended reset | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a011_swPowerStageNotReady` | page 0 | Rear drive inverter: a011 sw power stage not ready | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a012_hvilNotClosed` | page 0 | Rear drive inverter: a012 hvil not closed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a013_eccError` | page 0 | Rear drive inverter: a013 ecc error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a014_activeDamping` | page 0 | Rear drive inverter: a014 active damping | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a015_mechSafeStateAnomaly` | page 0 | Rear drive inverter: a015 mech safe state anomaly | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a016_safeStateApplied` | page 0 | Rear drive inverter: a016 safe state applied | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a017_hwPedalMonitor` | page 0 | Rear drive inverter: a017 hw pedal monitor | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a018_hwLVSupplyUV` | page 0 | Rear drive inverter: a018 hw LV supply UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a020_hwMotorEncoder` | page 0 | Rear drive inverter: a020 hw motor encoder | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a021_hwBusOV` | page 0 | Rear drive inverter: a021 hw bus OV | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a022_hw5vSupplyUV` | page 0 | Rear drive inverter: a022 hw5v supply UV | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a024_selfTest` | page 0 | Rear drive inverter: a024 self test | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a025_phaseApeak` | page 0 | Rear drive inverter: a025 phase apeak | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a026_phaseBpeak` | page 0 | Rear drive inverter: a026 phase bpeak | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a027_phaseCpeak` | page 0 | Rear drive inverter: a027 phase cpeak | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a028_phaseArms` | page 0 | Rear drive inverter: a028 phase arms | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a029_phaseBrms` | page 0 | Rear drive inverter: a029 phase brms | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a030_phaseCrms` | page 0 | Rear drive inverter: a030 phase crms | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a031_phaseAcurrentOffset` | page 0 | Rear drive inverter: a031 phase acurrent offset | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a032_phaseBcurrentOffset` | page 0 | Rear drive inverter: a032 phase bcurrent offset | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a033_phaseAcurrentSensor` | page 0 | Rear drive inverter: a033 phase acurrent sensor | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a034_phaseBcurrentSensor` | page 0 | Rear drive inverter: a034 phase bcurrent sensor | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a035_phaseCurrentBalance` | page 0 | Rear drive inverter: a035 phase current balance | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a036_busOV` | page 0 | Rear drive inverter: a036 bus OV | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a037_busUV` | page 0 | Rear drive inverter: a037 bus UV | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a038_busVsensor` | page 0 | Rear drive inverter: a038 bus vsensor | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a039_exceptionUndefinedInstruction` | page 0 | Rear drive inverter: a039 exception undefined instruction | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a040_difMIA` | page 0 | Rear drive inverter: a040 dif MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a041_sdcMIA` | page 0 | Rear drive inverter: a041 sdc MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a042_inletSensor` | page 0 | Rear drive inverter: a042 inlet sensor | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a043_outletOT` | page 0 | Rear drive inverter: a043 outlet OT | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a044_outletUT` | page 0 | Rear drive inverter: a044 outlet UT | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a045_outletSensor` | page 0 | Rear drive inverter: a045 outlet sensor | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a046_statorOT` | page 0 | Rear drive inverter: a046 stator OT | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a047_statorSensor1` | page 0 | Rear drive inverter: a047 stator sensor1 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a048_statorSensor2` | page 0 | Rear drive inverter: a048 stator sensor2 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a049_statorSensorDiff` | page 0 | Rear drive inverter: a049 stator sensor diff | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a050_noStatorSensor` | page 0 | Rear drive inverter: a050 no stator sensor | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a052_dirMIA` | page 0 | Rear drive inverter: a052 dir MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a053_unexpectedLatchState` | page 0 | Rear drive inverter: a053 unexpected latch state | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a054_driveInverterOT` | page 0 | Rear drive inverter: a054 drive inverter OT | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a055_trqCrossCheck` | page 0 | Rear drive inverter: a055 trq cross check | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a056_ambientOT` | page 0 | Rear drive inverter: a056 ambient OT | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a057_ambientUT` | page 0 | Rear drive inverter: a057 ambient UT | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a058_ambientSensor` | page 0 | Rear drive inverter: a058 ambient sensor | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a059_heatsinkOT` | page 0 | Rear drive inverter: a059 heatsink OT | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a060_heatsinkUT` | page 0 | Rear drive inverter: a060 heatsink UT | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a061_heatsinkSensor` | page 1 | Rear drive inverter: a061 heatsink sensor | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a062_systemLimpMode` | page 1 | Rear drive inverter: a062 system limp mode | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a063_bbMIA` | page 1 | Rear drive inverter: a063 bb MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a064_torqueIntervention` | page 1 | Rear drive inverter: a064 torque intervention | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a065_canHardwareBusB` | page 1 | Rear drive inverter: a065 can hardware bus b | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a066_canDataBusB` | page 1 | Rear drive inverter: a066 can data bus b | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a067_canOverrunBusB` | page 1 | Rear drive inverter: a067 can overrun bus b | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a069_rotorTempLimit` | page 1 | Rear drive inverter: a069 rotor temp limit | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a070_udsTransactionInitiated` | page 1 | Rear drive inverter: a070 uds transaction initiated | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a071_busDisconnected` | page 1 | Rear drive inverter: a071 bus disconnected | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a072_gateDriveFaultCounter` | page 1 | Rear drive inverter: a072 gate drive fault counter | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a073_motorSpeed` | page 1 | Rear drive inverter: a073 motor speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a074_motorEncoder` | page 1 | Rear drive inverter: a074 motor encoder | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a075_motorSpeedMismatch` | page 1 | Rear drive inverter: a075 motor speed mismatch | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a076_lvSupplyOV` | page 1 | Rear drive inverter: a076 lv supply OV | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a077_lvSupplyUV` | page 1 | Rear drive inverter: a077 lv supply UV | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a078_adcRefLow` | page 1 | Rear drive inverter: a078 adc ref low | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a079_adcRefHigh` | page 1 | Rear drive inverter: a079 adc ref high | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a084_eccTestData0` | page 1 | Rear drive inverter: a084 ecc test data0 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d085_driveInverterBoardFailure` | page 1 | Rear drive inverter: d085 drive inverter board failure | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a086_activeDischargeOn` | page 1 | Rear drive inverter: a086 active discharge on | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a087_gtwMIA` | page 1 | Rear drive inverter: a087 gtw MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a088_uiMIA` | page 1 | Rear drive inverter: a088 ui MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d089_invalidTorqueCommand` | page 1 | Rear drive inverter: d089 invalid torque command | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a090_pmMIA` | page 1 | Rear drive inverter: a090 pm MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a091_espMIA` | page 1 | Rear drive inverter: a091 esp MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a092_bmsMIA` | page 1 | Rear drive inverter: a092 bms MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a093_canHardwareBusA` | page 1 | Rear drive inverter: a093 can hardware bus a | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a094_canDataBusA` | page 1 | Rear drive inverter: a094 can data bus a | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a095_canOverrunBusA` | page 1 | Rear drive inverter: a095 can overrun bus a | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a096_memoryError` | page 1 | Rear drive inverter: a096 memory error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a097_eepromError` | page 1 | Rear drive inverter: a097 eeprom error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a098_intTimeTooLong` | page 1 | Rear drive inverter: a098 int time too long | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a099_threadOverrun` | page 1 | Rear drive inverter: a099 thread overrun | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a100_assertion` | page 1 | Rear drive inverter: a100 assertion | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a101_eccTestData1` | page 1 | Rear drive inverter: a101 ecc test data1 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a102_exceptionPrefetchAbort` | page 1 | Rear drive inverter: a102 exception prefetch abort | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a103_lowFlow` | page 1 | Rear drive inverter: a103 low flow | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d104_resetUnintended` | page 1 | Rear drive inverter: d104 reset unintended | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d105_busVoltageSensorIssue` | page 1 | Rear drive inverter: d105 bus voltage sensor issue | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a106_idleTaskStarving` | page 1 | Rear drive inverter: a106 idle task starving | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a107_fpgaError` | page 1 | Rear drive inverter: a107 fpga error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a108_stateTrans` | page 1 | Rear drive inverter: a108 state trans | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a109_ahbWriteError` | page 1 | Rear drive inverter: a109 ahb write error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a110_brakeMIA` | page 1 | Rear drive inverter: a110 brake MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a111_badPhaseSensorCalib` | page 1 | Rear drive inverter: a111 bad phase sensor calib | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a112_noPhaseCurrent` | page 1 | Rear drive inverter: a112 no phase current | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a113_noFuncHeatsinkSensor` | page 1 | Rear drive inverter: a113 no func heatsink sensor | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a114_exceptionDataAbort` | page 1 | Rear drive inverter: a114 exception data abort | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a115_exceptionDataAbort2` | page 1 | Rear drive inverter: a115 exception data abort2 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a116_highSpeedWearCounter` | page 1 | Rear drive inverter: a116 high speed wear counter | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a117_diMIA` | page 1 | Rear drive inverter: a117 di MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d118_oilPumpCommsLost` | page 1 | Rear drive inverter: d118 oil pump comms lost | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a119_hvpMIA` | page 1 | Rear drive inverter: a119 hvp MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a120_hvlinkMIA` | page 1 | Rear drive inverter: a120 hvlink MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a121_motorControlRegulation` | page 2 | Rear drive inverter: a121 motor control regulation | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a122_highStackUsage` | page 2 | Rear drive inverter: a122 high stack usage | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a123_lossMotorControl` | page 2 | Rear drive inverter: a123 loss motor control | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d124_oilPumpServiceRequired` | page 2 | Rear drive inverter: d124 oil pump service required | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d125_currentSensorIssue` | page 2 | Rear drive inverter: d125 current sensor issue | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a126_limpMode` | page 2 | Rear drive inverter: a126 limp mode | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a127_gracefulPowerOff` | page 2 | Rear drive inverter: a127 graceful power off | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a128_fpgaVersionMismatch` | page 2 | Rear drive inverter: a128 fpga version mismatch | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d129_oilPumpIssue` | page 2 | Rear drive inverter: d129 oil pump issue | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d130_positionSensorIssue` | page 2 | Rear drive inverter: d130 position sensor issue | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d131_currentSensorOffset` | page 2 | Rear drive inverter: d131 current sensor offset | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d132_busUVIssue` | page 2 | Rear drive inverter: d132 bus UV issue | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a133_capacitorOT` | page 2 | Rear drive inverter: a133 capacitor OT | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a134_wheelSpeedIrrational` | page 2 | Rear drive inverter: a134 wheel speed irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d135_rotatedStator` | page 2 | Rear drive inverter: d135 rotated stator | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a136_spiError` | page 2 | Rear drive inverter: a136 spi error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d137_currentSensorOutOfRange` | page 2 | Rear drive inverter: d137 current sensor out of range | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d138_inverterLVPowerSupplyLow` | page 2 | Rear drive inverter: d138 inverter LV power supply low | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d141_coolingSystemIssue` | page 2 | Rear drive inverter: d141 cooling system issue | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a142_highLashAngle` | page 2 | Rear drive inverter: a142 high lash angle | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d143_wheelSpeedCorrelationIssue` | page 2 | Rear drive inverter: d143 wheel speed correlation issue | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a144_configMismatch` | page 2 | Rear drive inverter: a144 config mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a147_highTorqueWearLimit` | page 2 | Rear drive inverter: a147 high torque wear limit | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a148_burnInCycleEnded` | page 2 | Rear drive inverter: a148 burn in cycle ended | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a149_oilPumpFailure` | page 2 | Rear drive inverter: a149 oil pump failure | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a150_busVD` | page 2 | Rear drive inverter: a150 bus VD | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a151_shockTorqueLimiter` | page 2 | Rear drive inverter: a151 shock torque limiter | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a152_linError` | page 2 | Rear drive inverter: a152 lin error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a153_oilPumpDiagnostics` | page 2 | Rear drive inverter: a153 oil pump diagnostics | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a154_resolver` | page 2 | Rear drive inverter: a154 resolver | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a155_vcfrontMIA` | page 2 | Rear drive inverter: a155 vcfront MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a156_currentObserver` | page 2 | Rear drive inverter: a156 current observer | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a157_rcmMIA` | page 2 | Rear drive inverter: a157 rcm MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a158_ibstMIA` | page 2 | Rear drive inverter: a158 ibst MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a160_busVoltageAnomaly` | page 2 | Rear drive inverter: a160 bus voltage anomaly | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a161_epas3pMIA` | page 2 | Rear drive inverter: a161 epas3p MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a162_endOfLifetimeBurnIn` | page 2 | Rear drive inverter: a162 end of lifetime burn in | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d163_recoverableOvercurrent` | page 2 | Rear drive inverter: d163 recoverable overcurrent | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d164_firmwareConfigMismatch` | page 2 | Rear drive inverter: d164 firmware config mismatch | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d165_statorOverTemperature` | page 2 | Rear drive inverter: d165 stator over temperature | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d166_rotorOverTemperature` | page 2 | Rear drive inverter: d166 rotor over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d167_tempSensorIssue` | page 2 | Rear drive inverter: d167 temp sensor issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a171_rdcError` | page 2 | Rear drive inverter: a171 rdc error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a172_statorOilTempOT` | page 2 | Rear drive inverter: a172 stator oil temp OT | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a173_ascFdbkDiagnostic` | page 2 | Rear drive inverter: a173 asc fdbk diagnostic | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a174_unitMayNotRestart` | page 2 | Rear drive inverter: a174 unit may not restart | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d175_oilPumpBCommsLost` | page 2 | Rear drive inverter: d175 oil pump b comms lost | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a176_safetyICFault` | page 2 | Rear drive inverter: a176 safety IC fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a177_fluxReferenceCorrected` | page 2 | Rear drive inverter: a177 flux reference corrected | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a178_spindownLearningBrakeAllowed` | page 2 | Rear drive inverter: a178 spindown learning brake allowed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_d179_oilPumpBIssue` | page 2 | Rear drive inverter: d179 oil pump b issue | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a194_resolverGainAnomaly` | page 3 | Rear drive inverter: a194 resolver gain anomaly | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a202_excessHeatUnavailable` | page 3 | Rear drive inverter: a202 excess heat unavailable | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a225_tmpEstPlausibility` | page 3 | Rear drive inverter: a225 tmp est plausibility | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a229_busVsensorOverCAN` | page 3 | Rear drive inverter: a229 bus vsensor over CAN | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a233_diMsgMissed` | page 3 | Rear drive inverter: a233 di msg missed | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a234_pcsMIA` | page 3 | Rear drive inverter: a234 pcs MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a236_tasMIA` | page 3 | Rear drive inverter: a236 tas MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a239_rotorDemagnetizationDetected` | page 3 | Rear drive inverter: a239 rotor demagnetization detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a240_clearFusesRoutine` | page 3 | Rear drive inverter: a240 clear fuses routine | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a241_systemThermallyLimited` | page 4 | Rear drive inverter: a241 system thermally limited | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a242_spinDownLearning` | page 4 | Rear drive inverter: a242 spin down learning | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a243_ecuLogAvailable` | page 4 | Rear drive inverter: a243 ecu log available | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a244_mechSafeStateApplied` | page 4 | Rear drive inverter: a244 mech safe state applied | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a245_mechSafeStatePreWarn` | page 4 | Rear drive inverter: a245 mech safe state pre warn | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a246_recoveryAtSpeedError` | page 4 | Rear drive inverter: a246 recovery at speed error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a247_rotorOffsetError` | page 4 | Rear drive inverter: a247 rotor offset error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a248_vehicleSpeedLimited` | page 4 | Rear drive inverter: a248 vehicle speed limited | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a249_highStatorTempFromResist` | page 4 | Rear drive inverter: a249 high stator temp from resist | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a250_preregulatorRail` | page 4 | Rear drive inverter: a250 preregulator rail | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a251_oilPumpService` | page 4 | Rear drive inverter: a251 oil pump service | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a252_currentCoreFallback` | page 4 | Rear drive inverter: a252 current core fallback | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a253_lvBoostedRail` | page 4 | Rear drive inverter: a253 lv boosted rail | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a254_activeDischargeRail` | page 4 | Rear drive inverter: a254 active discharge rail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a255_currentGainFallback` | page 4 | Rear drive inverter: a255 current gain fallback | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`DIR_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (57 signals), page 1 (55 signals), page 2 (51 signals), page 3 (9 signals), page 4 (15 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
