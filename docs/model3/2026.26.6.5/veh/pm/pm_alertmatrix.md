---
layout: default
title: "PM_alertMatrix (0x384) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "PM ECU message: alert matrix. Tesla Model 3 CAN bus message PM_alertMatrix (0x384) of PM ECU, firmware 2026.26.6.5, 104 signals (PM_matrixIndex, PM_a001_absoluteTorque, PM_a002_excessiveAccelTorque, PM_a003_excessiveReversalTorque and 100 more). Bit layout, scaling, units and value tables."
---

# PM_alertMatrix (0x384) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN

PM ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 104 signals of PM_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_alertMatrix` |
| CAN id | 0x384 (900) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 104 |

## Signals of PM_alertMatrix

Tesla Model 3 CAN bus signals in `PM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PM_matrixIndex` | selector | PM ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `PM_a001_absoluteTorque` | page 0 | PM ECU: a001 absolute torque | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a002_excessiveAccelTorque` | page 0 | PM ECU: a002 excessive accel torque | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a003_excessiveReversalTorque` | page 0 | PM ECU: a003 excessive reversal torque | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a004_excessiveDecelTorque` | page 0 | PM ECU: a004 excessive decel torque | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a005_torqueInNeutralOrPark` | page 0 | PM ECU: a005 torque in neutral or park | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_inconsistentDIGear` | page 0 | PM ECU: a006 inconsistent DI gear | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a007_ibstMIA` | page 0 | PM ECU: a007 ibst MIA | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a008_memoryError` | page 0 | PM ECU: a008 memory error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_espMIA` | page 0 | PM ECU: a009 esp MIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_diMIA` | page 0 | PM ECU: a010 di MIA | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a011_systemHvilNotClosed` | page 0 | PM ECU: a011 system hvil not closed | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a012_canDataBusA` | page 0 | PM ECU: a012 can data bus a | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a013_canHardwareBusA` | page 0 | PM ECU: a013 can hardware bus a | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a014_accelPedalError` | page 0 | PM ECU: a014 accel pedal error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a015_shifterMIA` | page 0 | PM ECU: a015 shifter MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a016_bbMIA` | page 0 | PM ECU: a016 bb MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_brakeMIA` | page 0 | PM ECU: a017 brake MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_difMIA` | page 0 | PM ECU: a021 dif MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_dirMIA` | page 0 | PM ECU: a022 dir MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a023_cruiseInhibit` | page 0 | PM ECU: a023 cruise inhibit | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a024_brakeIrrational` | page 0 | PM ECU: a024 brake irrational | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_unintendedReset` | page 0 | PM ECU: a025 unintended reset | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_diHeartBeatMIA` | page 0 | PM ECU: a026 di heart beat MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a028_torqueCmdError` | page 0 | PM ECU: a028 torque cmd error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a029_cruiseRollback` | page 0 | PM ECU: a029 cruise rollback | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a030_inconsistentAebState` | page 0 | PM ECU: a030 inconsistent aeb state | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a031_highStackUsage` | page 0 | PM ECU: a031 high stack usage | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a032_registerConfigError` | page 0 | PM ECU: a032 register config error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a033_appMIA` | page 0 | PM ECU: a033 app MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a034_trqCrossCheck` | page 0 | PM ECU: a034 trq cross check | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a035_udsTransactionInitiated` | page 0 | PM ECU: a035 uds transaction initiated | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_preWatchdog` | page 0 | PM ECU: a036 pre watchdog | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a038_inconsistentTorqueSign` | page 0 | PM ECU: a038 inconsistent torque sign | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a039_disMIA` | page 0 | PM ECU: a039 dis MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a040_alignmentDriftDetected` | page 0 | PM ECU: a040 alignment drift detected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_dasMIA` | page 0 | PM ECU: a041 das MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a042_gtwMIA` | page 0 | PM ECU: a042 gtw MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_inconsistentConfig` | page 0 | PM ECU: a043 inconsistent config | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a044_ebrIntervention` | page 0 | PM ECU: a044 ebr intervention | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a045_regenBackfillIntervention` | page 0 | PM ECU: a045 regen backfill intervention | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a046_inconsVehicleHoldState` | page 0 | PM ECU: a046 incons vehicle hold state | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a047_inconsAutoparkState` | page 0 | PM ECU: a047 incons autopark state | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a048_stabilityControlInhibit` | page 0 | PM ECU: a048 stability control inhibit | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a049_stbCtrlInWrongDir` | page 0 | PM ECU: a049 stb ctrl in wrong dir | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a050_excessiveStbCtrlTrq` | page 0 | PM ECU: a050 excessive stb ctrl trq | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a051_unintDecelStbCtrl` | page 0 | PM ECU: a051 unint decel stb ctrl | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a052_stbCtrlDrvrDecelCflct` | page 0 | PM ECU: a052 stb ctrl drvr decel cflct | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_vcfrontMIA` | page 0 | PM ECU: a053 vcfront MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiMIA` | page 0 | PM ECU: a054 ui MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a055_accelPedalSyncWarn` | page 0 | PM ECU: a055 accel pedal sync warn | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a056_canHardwareBusB` | page 0 | PM ECU: a056 can hardware bus b | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a057_canDataBusB` | page 0 | PM ECU: a057 can data bus b | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a058_cmpMIA` | page 0 | PM ECU: a058 cmp MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a059_ptcMIA` | page 0 | PM ECU: a059 ptc MIA | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a060_onePedalDrivingInhibit` | page 0 | PM ECU: a060 one pedal driving inhibit | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a061_DIPMVersionMismatch` | page 1 | PM ECU: a061 DIPM version mismatch | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a062_eccError` | page 1 | PM ECU: a062 ecc error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a063_torqueCommandInhibit` | page 1 | PM ECU: a063 torque command inhibit | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a064_torqueIntervention` | page 1 | PM ECU: a064 torque intervention | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a066_pmfMIA` | page 1 | PM ECU: a066 pmf MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a067_pmrMIA` | page 1 | PM ECU: a067 pmr MIA | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a068_brakePedalMonitor` | page 1 | PM ECU: a068 brake pedal monitor | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a069_brakeMonitorsUnhealthy` | page 1 | PM ECU: a069 brake monitors unhealthy | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_brakeTorqueSplitMonitorTrip` | page 1 | PM ECU: a070 brake torque split monitor trip | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a071_baseBrakingMonitor` | page 1 | PM ECU: a071 base braking monitor | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a072_brakeTorqueCommandInterface` | page 1 | PM ECU: a072 brake torque command interface | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a073_canDataBusC` | page 1 | PM ECU: a073 can data bus c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a074_canHardwareBusC` | page 1 | PM ECU: a074 can hardware bus c | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a075_canDataBusD` | page 1 | PM ECU: a075 can data bus d | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a076_canHardwareBusD` | page 1 | PM ECU: a076 can hardware bus d | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a077_canDataBusE` | page 1 | PM ECU: a077 can data bus e | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a078_canHardwareBusE` | page 1 | PM ECU: a078 can hardware bus e | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a079_rcuMIA` | page 1 | PM ECU: a079 rcu MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a080_exceptionPrefetchAbort` | page 1 | PM ECU: a080 exception prefetch abort | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a081_exceptionDataAbort` | page 1 | PM ECU: a081 exception data abort | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a082_exceptionDataAbort2` | page 1 | PM ECU: a082 exception data abort2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a083_ahbWriteError` | page 1 | PM ECU: a083 ahb write error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a084_exceptionMpuFirewall` | page 1 | PM ECU: a084 exception mpu firewall | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a085_dpbMIA` | page 1 | PM ECU: a085 dpb MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a086_exceptionUndefinedInstruction` | page 1 | PM ECU: a086 exception undefined instruction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a087_canHardwareBusLIPC` | page 1 | PM ECU: a087 can hardware bus LIPC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a088_absMonitor` | page 1 | PM ECU: a088 abs monitor | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a092_xtalOscillator` | page 1 | PM ECU: a092 xtal oscillator | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a093_accelPedalSupply` | page 1 | PM ECU: a093 accel pedal supply | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a094_torqueSplitMonitor` | page 1 | PM ECU: a094 torque split monitor | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a095_ITPMSTimeoutGNSSConvergence` | page 1 | PM ECU: a095 ITPMS timeout GNSS convergence | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a096_ITPMSConvergedGNSSAbsRadiusTimes` | page 1 | PM ECU: a096 ITPMS converged GNSS abs radius times | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a097_ITPMSRelativeCalibratedFactors` | page 1 | PM ECU: a097 ITPMS relative calibrated factors | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a098_ITPMSTriggerDebug` | page 1 | PM ECU: a098 ITPMS trigger debug | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a099_ITPMSCalibrated` | page 1 | PM ECU: a099 ITPMS calibrated | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_diTraceInfo1` | page 1 | PM ECU: a100 di trace info1 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a110_indirectTPMSPressureLossWarning` | page 1 | PM ECU: a110 indirect TPMS pressure loss warning | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a111_unintendedResetCausedNeutral` | page 1 | PM ECU: a111 unintended reset caused neutral | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a112_indirectTPMSPressureLossWarningHard` | page 1 | PM ECU: a112 indirect TPMS pressure loss warning hard | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a113_btcMonitor` | page 1 | PM ECU: a113 btc monitor | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a114_ramScrubTimedOut` | page 1 | PM ECU: a114 ram scrub timed out | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a115_indirectTPMSFaultedGhosted` | page 1 | PM ECU: a115 indirect TPMS faulted ghosted | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a116_ITPMSBlowoutCalProgress` | page 1 | PM ECU: a116 ITPMS blowout cal progress | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a117_ITPMSPermeabilityCalibrated` | page 1 | PM ECU: a117 ITPMS permeability calibrated | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a118_vehicleSpeedQFDiagnostic` | page 1 | PM ECU: a118 vehicle speed QF diagnostic | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_indirectTPMSFaulted` | page 1 | PM ECU: a120 indirect TPMS faulted | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a121_unintendedReset2` | page 2 | PM ECU: a121 unintended reset2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a125_btcOutputIrrational` | page 2 | PM ECU: a125 btc output irrational | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (55 signals), page 1 (46 signals), page 2 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
