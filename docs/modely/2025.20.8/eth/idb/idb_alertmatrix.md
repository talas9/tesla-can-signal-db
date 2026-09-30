---
layout: default
title: "IDB_alertMatrix (0x3D7) — IDB ECU, Tesla Model Y 2025.20.8 ETH"
description: "IDB ECU message: alert matrix. Ethernet-side message IDB_alertMatrix of IDB ECU for Tesla Model Y firmware 2025.20.8, 145 signals (IDB_matrixIndex, IDB_a001_mcuGenericFault, IDB_a002_supplyOvervoltage, IDB_a003_supplyHardOvervoltage and 141 more). Bit layout, scaling, units and value tables."
---

# IDB_alertMatrix (0x3D7) — IDB ECU, Tesla Model Y 2025.20.8 ETH

IDB ECU message: alert matrix. This page documents the 145 signals of IDB_alertMatrix as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `IDB_alertMatrix` |
| Ethernet-side id | 0x3D7 (983) |
| ECU | [IDB ECU](../../idb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | IDB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 145 |

## Signals of IDB_alertMatrix

Tesla Model Y CAN bus signals in `IDB_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `IDB_matrixIndex` | selector | IDB ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `IDB_a001_mcuGenericFault` | page 0 | IDB ECU: a001 mcu generic fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a002_supplyOvervoltage` | page 0 | IDB ECU: a002 supply overvoltage | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a003_supplyHardOvervoltage` | page 0 | IDB ECU: a003 supply hard overvoltage | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a004_supplyUndervoltage` | page 0 | IDB ECU: a004 supply undervoltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a005_supplyMidUndervoltage` | page 0 | IDB ECU: a005 supply mid undervoltage | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a006_supplyHardUndervoltage` | page 0 | IDB ECU: a006 supply hard undervoltage | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a007_wakeLineOpen` | page 0 | IDB ECU: a007 wake line open | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a008_motorPowerOpen` | page 0 | IDB ECU: a008 motor power open | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a009_asicBoostFault` | page 0 | IDB ECU: a009 asic boost fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a010_asicGenericFault` | page 0 | IDB ECU: a010 asic generic fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a011_solenoidValveFault` | page 0 | IDB ECU: a011 solenoid valve fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a012_motorGenericFault` | page 0 | IDB ECU: a012 motor generic fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a013_motorPosSensorFault` | page 0 | IDB ECU: a013 motor pos sensor fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a014_FrLWSSFault` | page 0 | IDB ECU: a014 fr LWSS fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a015_FrRWSSFault` | page 0 | IDB ECU: a015 fr RWSS fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a016_ReLWSSFault` | page 0 | IDB ECU: a016 re LWSS fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a017_ReRWSSFault` | page 0 | IDB ECU: a017 re RWSS fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a018_WSSGenericFault` | page 0 | IDB ECU: a018 WSS generic fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a019_pedalSensorFault` | page 0 | IDB ECU: a019 pedal sensor fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a020_RCUpedalTravelMismatch` | page 0 | IDB ECU: a020 RC upedal travel mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a021_pedalSensorNotCal` | page 0 | IDB ECU: a021 pedal sensor not cal | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a022_brakeFluidLow` | page 0 | IDB ECU: a022 brake fluid low | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a023_steeringImplausible` | page 0 | IDB ECU: a023 steering implausible | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a024_yawImplausible` | page 0 | IDB ECU: a024 yaw implausible | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a025_ayImplausible` | page 0 | IDB ECU: a025 ay implausible | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a026_axImplausible` | page 0 | IDB ECU: a026 ax implausible | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a027_circuitPresSensorFault` | page 0 | IDB ECU: a027 circuit pres sensor fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a028_simPresSensorFault` | page 0 | IDB ECU: a028 sim pres sensor fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a029_pressureSensNotCal` | page 0 | IDB ECU: a029 pressure sens not cal | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a030_fluidLeakDetected` | page 0 | IDB ECU: a030 fluid leak detected | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a031_solenoidValveStuck` | page 0 | IDB ECU: a031 solenoid valve stuck | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a032_motorSoftOverheat` | page 0 | IDB ECU: a032 motor soft overheat | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a033_motorHardOverheat` | page 0 | IDB ECU: a033 motor hard overheat | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a034_motorPositionSetFault` | page 0 | IDB ECU: a034 motor position set fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a035_motorStuck` | page 0 | IDB ECU: a035 motor stuck | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a036_partyBusOff` | page 0 | IDB ECU: a036 party bus off | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a037_chassisBusOff` | page 0 | IDB ECU: a037 chassis bus off | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a038_motorInitFault` | page 0 | IDB ECU: a038 motor init fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a039_absActive` | page 0 | IDB ECU: a039 abs active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a040_ebdActive` | page 0 | IDB ECU: a040 ebd active | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a041_vdcActive` | page 0 | IDB ECU: a041 vdc active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a042_btcActive` | page 0 | IDB ECU: a042 btc active | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a043_DItorquePathActive` | page 0 | IDB ECU: a043 d itorque path active | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a044_standstillSkidDetected` | page 0 | IDB ECU: a044 standstill skid detected | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a045_panicBrakeAssistActive` | page 0 | IDB ECU: a045 panic brake assist active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a046_fadeCompensationActive` | page 0 | IDB ECU: a046 fade compensation active | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a047_brakeDiscWipeActive` | page 0 | IDB ECU: a047 brake disc wipe active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a048_scmActive` | page 0 | IDB ECU: a048 scm active | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a049_cdpActive` | page 0 | IDB ECU: a049 cdp active | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a050_absFaulted` | page 0 | IDB ECU: a050 abs faulted | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a051_ebdFaulted` | page 0 | IDB ECU: a051 ebd faulted | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a052_vdcFaulted` | page 0 | IDB ECU: a052 vdc faulted | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a053_DItorquePathFaulted` | page 0 | IDB ECU: a053 d itorque path faulted | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a054_skidDetectionFaulted` | page 0 | IDB ECU: a054 skid detection faulted | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a055_panicBrakeAssistFaulted` | page 0 | IDB ECU: a055 panic brake assist faulted | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a056_fadeCompensationFaulted` | page 0 | IDB ECU: a056 fade compensation faulted | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a057_bdwRequestInvalid` | page 0 | IDB ECU: a057 bdw request invalid | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a058_scmFaulted` | page 0 | IDB ECU: a058 scm faulted | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a059_cdpFaulted` | page 0 | IDB ECU: a059 cdp faulted | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a060_RCUstatusDLC` | page 0 | IDB ECU: a060 RC ustatus DLC | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a061_RCUstatusChecksum` | page 1 | IDB ECU: a061 RC ustatus checksum | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a062_RCUstatusCounter` | page 1 | IDB ECU: a062 RC ustatus counter | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a063_RCUactuationDLC` | page 1 | IDB ECU: a063 RC uactuation DLC | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a064_RCUactuationChecksum` | page 1 | IDB ECU: a064 RC uactuation checksum | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a065_RCUactuationCounter` | page 1 | IDB ECU: a065 RC uactuation counter | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a066_DIFtorqueDLC` | page 1 | IDB ECU: a066 DI ftorque DLC | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a067_DIFtorqueChecksum` | page 1 | IDB ECU: a067 DI ftorque checksum | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a068_DIFtorqueCounter` | page 1 | IDB ECU: a068 DI ftorque counter | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a069_DIchassisControlDLC` | page 1 | IDB ECU: a069 d ichassis control DLC | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a070_DIchassisControlChecksum` | page 1 | IDB ECU: a070 d ichassis control checksum | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a071_DIchassisControlCounter` | page 1 | IDB ECU: a071 d ichassis control counter | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a072_DIsystemStatusDLC` | page 1 | IDB ECU: a072 d isystem status DLC | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a073_DIsystemStatusChecksum` | page 1 | IDB ECU: a073 d isystem status checksum | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a074_DIsystemStatusCounter` | page 1 | IDB ECU: a074 d isystem status counter | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a075_DIRtorqueDLC` | page 1 | IDB ECU: a075 DI rtorque DLC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a076_DIRtorqueChecksum` | page 1 | IDB ECU: a076 DI rtorque checksum | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a077_DIRtorqueCounter` | page 1 | IDB ECU: a077 DI rtorque counter | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a078_DIvdcLeftDLC` | page 1 | IDB ECU: a078 d ivdc left DLC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a079_DIvdcLeftChecksum` | page 1 | IDB ECU: a079 d ivdc left checksum | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a080_DIvdcLeftCounter` | page 1 | IDB ECU: a080 d ivdc left counter | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a081_DIvdcRightDLC` | page 1 | IDB ECU: a081 d ivdc right DLC | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a082_DIvdcRightChecksum` | page 1 | IDB ECU: a082 d ivdc right checksum | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a083_DIvdcRightCounter` | page 1 | IDB ECU: a083 d ivdc right counter | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a084_EPAS3PsysStatusDLC` | page 1 | IDB ECU: a084 EPAS3 psys status DLC | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a085_EPAS3PsysStatusChecksum` | page 1 | IDB ECU: a085 EPAS3 psys status checksum | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a086_EPAS3PsysStatusCounter` | page 1 | IDB ECU: a086 EPAS3 psys status counter | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a087_PMstate2DLC` | page 1 | IDB ECU: a087 p mstate2 DLC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a088_PMstate2Checksum` | page 1 | IDB ECU: a088 p mstate2 checksum | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a089_PMstate2Counter` | page 1 | IDB ECU: a089 p mstate2 counter | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a090_RCMinertial1DLC` | page 1 | IDB ECU: a090 RC minertial1 DLC | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a091_RCMinertial1Checksum` | page 1 | IDB ECU: a091 RC minertial1 checksum | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a092_RCMinertial1Counter` | page 1 | IDB ECU: a092 RC minertial1 counter | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a093_RCMinertial2DLC` | page 1 | IDB ECU: a093 RC minertial2 DLC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a094_RCMinertial2Checksum` | page 1 | IDB ECU: a094 RC minertial2 checksum | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a095_RCMinertial2Counter` | page 1 | IDB ECU: a095 RC minertial2 counter | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a096_VCFRONTLVPowerStateDLC` | page 1 | IDB ECU: a096 VCFRONTLV power state DLC | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a097_VCFRONTLVPwrStChecksum` | page 1 | IDB ECU: a097 VCFRONTLV pwr st checksum | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a098_VCFRONTLVPwrStCounter` | page 1 | IDB ECU: a098 VCFRONTLV pwr st counter | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a099_RCMcollisionDLC` | page 1 | IDB ECU: a099 RC mcollision DLC | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a100_RCMcollisionChecksum` | page 1 | IDB ECU: a100 RC mcollision checksum | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a101_RCMcollisionCounter` | page 1 | IDB ECU: a101 RC mcollision counter | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a102_bdwRequestActiveInvalid` | page 1 | IDB ECU: a102 bdw request active invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a103_DIfullTorquePathFaulted` | page 1 | IDB ECU: a103 d ifull torque path faulted | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a104_DIaccelPosInvalid` | page 1 | IDB ECU: a104 d iaccel pos invalid | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a105_DIgearInvalid` | page 1 | IDB ECU: a105 d igear invalid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a106_DIFtorqueInvalid` | page 1 | IDB ECU: a106 DI ftorque invalid | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a107_DIRtorqueInvalid` | page 1 | IDB ECU: a107 DI rtorque invalid | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a108_EPBstatusDLC` | page 1 | IDB ECU: a108 EP bstatus DLC | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a109_BDWsignalInvalid` | page 1 | IDB ECU: a109 BD wsignal invalid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a110_EPBstatusCounter` | page 1 | IDB ECU: a110 EP bstatus counter | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a111_EPBstatusChecksum` | page 1 | IDB ECU: a111 EP bstatus checksum | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a112_yawRateInvalid` | page 1 | IDB ECU: a112 yaw rate invalid | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a113_latAccelInvalid` | page 1 | IDB ECU: a113 lat accel invalid | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a114_longAccelInvalid` | page 1 | IDB ECU: a114 long accel invalid | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a115_VCFRONTespLvStInvalid` | page 1 | IDB ECU: a115 VCFRON tesp lv st invalid | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a116_VCFRONTsensorsDLC` | page 1 | IDB ECU: a116 VCFRON tsensors DLC | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a117_VCLEFTepbmStatusDLC` | page 1 | IDB ECU: a117 VCLEF tepbm status DLC | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a118_VCLEFTepbmStatusCounter` | page 1 | IDB ECU: a118 VCLEF tepbm status counter | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a119_VCLEFTepbmStatusChecksum` | page 1 | IDB ECU: a119 VCLEF tepbm status checksum | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a120_EPAS3Pinvalid` | page 1 | IDB ECU: a120 EPAS3 pinvalid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a121_dynoModeActive` | page 2 | IDB ECU: a121 dyno mode active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a122_DIFtorqueCommandInvalid` | page 2 | IDB ECU: a122 DI ftorque command invalid | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a123_DIRtorqueCommandInvalid` | page 2 | IDB ECU: a123 DI rtorque command invalid | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a124_VCFRONTtempInvalid` | page 2 | IDB ECU: a124 VCFRON ttemp invalid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a125_PMvdcCmdStateInvalid` | page 2 | IDB ECU: a125 p mvdc cmd state invalid | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a126_DItorqueRequestInvalid` | page 2 | IDB ECU: a126 d itorque request invalid | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a127_brakeFluidLevelInvalid` | page 2 | IDB ECU: a127 brake fluid level invalid | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a128_reserved1` | page 2 | IDB ECU: a128 reserved1 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a129_RCUinputRodStrokeInvalid` | page 2 | IDB ECU: a129 RC uinput rod stroke invalid | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a130_DIfullTorqueRequestInvalid` | page 2 | IDB ECU: a130 d ifull torque request invalid | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a131_DIfullTorquePathActive` | page 2 | IDB ECU: a131 d ifull torque path active | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a132_RCUinputRodStrokeQFInvalid` | page 2 | IDB ECU: a132 RC uinput rod stroke QF invalid | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a133_DIbrakeCommandDLC` | page 2 | IDB ECU: a133 d ibrake command DLC | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a134_DIbrakeCommandCounter` | page 2 | IDB ECU: a134 d ibrake command counter | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a135_DIbrakeCommandChecksum` | page 2 | IDB ECU: a135 d ibrake command checksum | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a136_RCUptsCalMissing` | page 2 | IDB ECU: a136 RC upts cal missing | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a137_VCLEFTcdpRequestInvalid` | page 2 | IDB ECU: a137 VCLEF tcdp request invalid | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a138_DIbrakeTorqueCommandAndFlagMismatch` | page 2 | IDB ECU: a138 d ibrake torque command and flag mismatch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a139_DIbrakeTorqueCommandFullSNA` | page 2 | IDB ECU: a139 d ibrake torque command full SNA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a140_PMbrakePedalCmdQFInvalid` | page 2 | IDB ECU: a140 p mbrake pedal cmd QF invalid | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a141_DIbrakeTorqueCommandFullTooLow` | page 2 | IDB ECU: a141 d ibrake torque command full too low | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a142_PMebrCmdStateInvalid` | page 2 | IDB ECU: a142 p mebr cmd state invalid | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a143_factoryModeActive` | page 2 | IDB ECU: a143 factory mode active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `IDB_a144_hydraulicPushthroughActive` | page 2 | IDB ECU: a144 hydraulic pushthrough active | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`IDB_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (24 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All IDB ECU messages (IDB)](../../idb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
