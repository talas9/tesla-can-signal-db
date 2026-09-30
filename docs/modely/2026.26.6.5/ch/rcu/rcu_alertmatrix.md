---
layout: default
title: "RCU_alertMatrix (0x3E6) — RCU ECU, Tesla Model Y 2026.26.6.5 CH CAN"
description: "RCU ECU message: alert matrix. Tesla Model Y CAN bus message RCU_alertMatrix (0x3E6) of RCU ECU, firmware 2026.26.6.5, 67 signals (RCU_matrixIndex, RCU_a001_valveDriverFault, RCU_a002_solenoidValveFault, RCU_a003_pumpMotorFault and 63 more). Bit layout, scaling, units and value tables."
---

# RCU_alertMatrix (0x3E6) — RCU ECU, Tesla Model Y 2026.26.6.5 CH CAN

RCU ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 67 signals of RCU_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCU_alertMatrix` |
| CAN id | 0x3E6 (998) |
| ECU | [RCU ECU](../../rcu.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 67 |

## Signals of RCU_alertMatrix

Tesla Model Y CAN bus signals in `RCU_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCU_matrixIndex` | selector | RCU ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1` | plausible |
| `RCU_a001_valveDriverFault` | page 0 | RCU ECU: a001 valve driver fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a002_solenoidValveFault` | page 0 | RCU ECU: a002 solenoid valve fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a003_pumpMotorFault` | page 0 | RCU ECU: a003 pump motor fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a004_supplyOvervoltage` | page 0 | RCU ECU: a004 supply overvoltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a005_supplyUndervoltage` | page 0 | RCU ECU: a005 supply undervoltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a006_wakeLineOpen` | page 0 | RCU ECU: a006 wake line open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a007_pressureSensorFault` | page 0 | RCU ECU: a007 pressure sensor fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a008_pressureNotCalibrated` | page 0 | RCU ECU: a008 pressure not calibrated | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a009_brakeFluidLow` | page 0 | RCU ECU: a009 brake fluid low | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a010_pedalSensorFault` | page 0 | RCU ECU: a010 pedal sensor fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a011_idbPedalTravelMismatch` | page 0 | RCU ECU: a011 idb pedal travel mismatch | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a012_pedalSensorNotCal` | page 0 | RCU ECU: a012 pedal sensor not cal | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a013_mcuGenericFault` | page 0 | RCU ECU: a013 mcu generic fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a014_asicTempHigh` | page 0 | RCU ECU: a014 asic temp high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a015_fluidLeakDetected` | page 0 | RCU ECU: a015 fluid leak detected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a016_partyBusOff` | page 0 | RCU ECU: a016 party bus off | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a017_chassisBusOff` | page 0 | RCU ECU: a017 chassis bus off | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a018_DItorquePathFaulted` | page 0 | RCU ECU: a018 d itorque path faulted | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a019_DItorquePathActive` | page 0 | RCU ECU: a019 d itorque path active | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a020_BBstatusDLC` | page 0 | RCU ECU: a020 b bstatus DLC | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a021_BBstatusChecksum` | page 0 | RCU ECU: a021 b bstatus checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a022_BBstatusCounter` | page 0 | RCU ECU: a022 b bstatus counter | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a023_IDBstatusDLC` | page 0 | RCU ECU: a023 ID bstatus DLC | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a024_IDBstatusChecksum` | page 0 | RCU ECU: a024 ID bstatus checksum | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a025_IDBstatusCounter` | page 0 | RCU ECU: a025 ID bstatus counter | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a026_DIchassisControlDLC` | page 0 | RCU ECU: a026 d ichassis control DLC | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a027_DIchassisCtrlChecksum` | page 0 | RCU ECU: a027 d ichassis ctrl checksum | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a028_DIchassisControlCounter` | page 0 | RCU ECU: a028 d ichassis control counter | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a029_PMstate2DLC` | page 0 | RCU ECU: a029 p mstate2 DLC | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a030_PMstate2Checksum` | page 0 | RCU ECU: a030 p mstate2 checksum | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a031_PMstate2Counter` | page 0 | RCU ECU: a031 p mstate2 counter | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a032_VCFRONTLVPowerStateDLC` | page 0 | RCU ECU: a032 VCFRONTLV power state DLC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a033_VCFRONTLVPowerStateChecksum` | page 0 | RCU ECU: a033 VCFRONTLV power state checksum | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a034_VCFRONTLVPowerStateCounter` | page 0 | RCU ECU: a034 VCFRONTLV power state counter | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a035_IDBpcpInvalid` | page 0 | RCU ECU: a035 ID bpcp invalid | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a036_IDBpspInvalid` | page 0 | RCU ECU: a036 ID bpsp invalid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a037_IDBinputRodStrokeInvalid` | page 0 | RCU ECU: a037 ID binput rod stroke invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a038_DIsystemStatusDLC` | page 0 | RCU ECU: a038 d isystem status DLC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a039_DIaccelPosInvalid` | page 0 | RCU ECU: a039 d iaccel pos invalid | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a040_DIgearInvalid` | page 0 | RCU ECU: a040 d igear invalid | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a041_DIsystemStatusCounter` | page 0 | RCU ECU: a041 d isystem status counter | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a042_DIsystemStatusChecksum` | page 0 | RCU ECU: a042 d isystem status checksum | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a043_VCFRONTiBoosterLvStateInvalid` | page 0 | RCU ECU: a043 VCFRON ti booster lv state invalid | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a044_VCFRONTsensorsMIA` | page 0 | RCU ECU: a044 VCFRON tsensors MIA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a045_VCFRONTtempInvalid` | page 0 | RCU ECU: a045 VCFRON ttemp invalid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a046_brakeFluidLevelSNA` | page 0 | RCU ECU: a046 brake fluid level SNA | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a047_ESPwheelSpeedsDLC` | page 0 | RCU ECU: a047 ES pwheel speeds DLC | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a048_ESPFrLWSSLInvalid` | page 0 | RCU ECU: a048 ESP fr LWSSL invalid | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a049_ESPFrRWSSLInvalid` | page 0 | RCU ECU: a049 ESP fr RWSSL invalid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a050_ESPReLWSSLInvalid` | page 0 | RCU ECU: a050 ESP re LWSSL invalid | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a051_ESPReRWSSLInvalid` | page 0 | RCU ECU: a051 ESP re RWSSL invalid | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a052_ESPwheelSpeedsCounter` | page 0 | RCU ECU: a052 ES pwheel speeds counter | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a053_ESPwheelSpeedsChecksum` | page 0 | RCU ECU: a053 ES pwheel speeds checksum | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a054_IDBcircuitPressFaulted` | page 0 | RCU ECU: a054 ID bcircuit press faulted | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a055_IDBsimulatorPressFaulted` | page 0 | RCU ECU: a055 ID bsimulator press faulted | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a056_redundantControllerIsMaster` | page 0 | RCU ECU: a056 redundant controller is master | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a057_DASredundantBrakingControlDLC` | page 0 | RCU ECU: a057 DA sredundant braking control DLC | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a058_DASredundantBrakingControlCounter` | page 0 | RCU ECU: a058 DA sredundant braking control counter | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a059_DASredundantBrakingControlChecksum` | page 0 | RCU ECU: a059 DA sredundant braking control checksum | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a060_DASbrakeTorqueCommandInvalid` | page 0 | RCU ECU: a060 DA sbrake torque command invalid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a061_DIlocStatus2DLC` | page 1 | RCU ECU: a061 d iloc status2 DLC | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a062_DIlocStatus2Counter` | page 1 | RCU ECU: a062 d iloc status2 counter | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a063_DIlocStatus2Checksum` | page 1 | RCU ECU: a063 d iloc status2 checksum | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a064_ESPredundantBrakingStatusDLC` | page 1 | RCU ECU: a064 ES predundant braking status DLC | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a065_ESPredundantBrakingStatusCounter` | page 1 | RCU ECU: a065 ES predundant braking status counter | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCU_a066_ESPredundantBrakingStatusChecksum` | page 1 | RCU ECU: a066 ES predundant braking status checksum | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`RCU_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All RCU ECU messages (RCU)](../../rcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
