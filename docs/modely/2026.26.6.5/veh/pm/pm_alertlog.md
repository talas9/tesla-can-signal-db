---
layout: default
title: "PM_alertLog (0x5A4) — PM ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "PM ECU message: alert log. Tesla Model Y CAN bus message PM_alertLog (0x5A4) of PM ECU, firmware 2026.26.6.5, 299 signals (PM_alertID, PM_alertState, PM_a001_w0, PM_a001_w1 and 295 more). Bit layout, scaling, units and value tables."
---

# PM_alertLog (0x5A4) — PM ECU, Tesla Model Y 2026.26.6.5 VEH CAN

PM ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 299 signals of PM_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_alertLog` |
| CAN id | 0x5A4 (1444) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 299 |

## Signals of PM_alertLog

Tesla Model Y CAN bus signals in `PM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PM_alertID` | selector | PM ECU: alert ID | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_absoluteTorque`<br>2 = `a002_excessiveAccelTorque`<br>3 = `a003_excessiveReversalTorque`<br>4 = `a004_excessiveDecelTorque`<br>5 = `a005_torqueInNeutralOrPark`<br>6 = `a006_inconsistentDIGear`<br>7 = `a007_ibstMIA`<br>8 = `a008_memoryError`<br>9 = `a009_espMIA`<br>10 = `a010_diMIA`<br>11 = `a011_systemHvilNotClosed`<br>12 = `a012_canDataBusA`<br>13 = `a013_canHardwareBusA`<br>14 = `a014_accelPedalError`<br>15 = `a015_shifterMIA`<br>16 = `a016_bbMIA`<br>17 = `a017_brakeMIA`<br>21 = `a021_difMIA`<br>22 = `a022_dirMIA`<br>23 = `a023_cruiseInhibit`<br>24 = `a024_brakeIrrational`<br>25 = `a025_unintendedReset`<br>26 = `a026_diHeartBeatMIA`<br>28 = `a028_torqueCmdError`<br>29 = `a029_cruiseRollback`<br>30 = `a030_inconsistentAebState`<br>31 = `a031_highStackUsage`<br>32 = `a032_registerConfigError`<br>33 = `a033_appMIA`<br>34 = `a034_trqCrossCheck`<br>35 = `a035_udsTransactionInitiated`<br>36 = `a036_preWatchdog`<br>38 = `a038_inconsistentTorqueSign`<br>39 = `a039_disMIA`<br>40 = `a040_alignmentDriftDetected`<br>41 = `a041_dasMIA`<br>42 = `a042_gtwMIA`<br>43 = `a043_inconsistentConfig`<br>44 = `a044_ebrIntervention`<br>45 = `a045_regenBackfillIntervention`<br>46 = `a046_inconsVehicleHoldState`<br>47 = `a047_inconsAutoparkState`<br>48 = `a048_stabilityControlInhibit`<br>49 = `a049_stbCtrlInWrongDir`<br>50 = `a050_excessiveStbCtrlTrq`<br>51 = `a051_unintDecelStbCtrl`<br>52 = `a052_stbCtrlDrvrDecelCflct`<br>53 = `a053_vcfrontMIA`<br>54 = `a054_uiMIA`<br>55 = `a055_accelPedalSyncWarn`<br>56 = `a056_canHardwareBusB`<br>57 = `a057_canDataBusB`<br>58 = `a058_cmpMIA`<br>59 = `a059_ptcMIA`<br>60 = `a060_onePedalDrivingInhibit`<br>61 = `a061_DIPMVersionMismatch`<br>62 = `a062_eccError`<br>63 = `a063_torqueCommandInhibit`<br>64 = `a064_torqueIntervention`<br>66 = `a066_pmfMIA`<br>67 = `a067_pmrMIA`<br>68 = `a068_brakePedalMonitor`<br>69 = `a069_brakeMonitorsUnhealthy`<br>70 = `a070_brakeTorqueSplitMonitorTrip`<br>71 = `a071_baseBrakingMonitor`<br>72 = `a072_brakeTorqueCommandInterface`<br>73 = `a073_canDataBusC`<br>74 = `a074_canHardwareBusC`<br>75 = `a075_canDataBusD`<br>76 = `a076_canHardwareBusD`<br>77 = `a077_canDataBusE`<br>78 = `a078_canHardwareBusE`<br>79 = `a079_rcuMIA`<br>80 = `a080_exceptionPrefetchAbort`<br>81 = `a081_exceptionDataAbort`<br>82 = `a082_exceptionDataAbort2`<br>83 = `a083_ahbWriteError`<br>84 = `a084_exceptionMpuFirewall`<br>85 = `a085_dpbMIA`<br>86 = `a086_exceptionUndefinedInstruction`<br>87 = `a087_canHardwareBusLIPC`<br>88 = `a088_absMonitor`<br>92 = `a092_xtalOscillator`<br>93 = `a093_accelPedalSupply`<br>94 = `a094_torqueSplitMonitor`<br>95 = `a095_ITPMSTimeoutGNSSConvergence`<br>96 = `a096_ITPMSConvergedGNSSAbsRadiusTimes`<br>97 = `a097_ITPMSRelativeCalibratedFactors`<br>98 = `a098_ITPMSTriggerDebug`<br>99 = `a099_ITPMSCalibrated`<br>100 = `a100_diTraceInfo1`<br>110 = `a110_indirectTPMSPressureLossWarning`<br>111 = `a111_unintendedResetCausedNeutral`<br>112 = `a112_indirectTPMSPressureLossWarningHard`<br>113 = `a113_btcMonitor`<br>114 = `a114_ramScrubTimedOut`<br>115 = `a115_indirectTPMSFaultedGhosted`<br>116 = `a116_ITPMSBlowoutCalProgress`<br>117 = `a117_ITPMSPermeabilityCalibrated`<br>118 = `a118_vehicleSpeedQFDiagnostic`<br>120 = `a120_indirectTPMSFaulted`<br>121 = `a121_unintendedReset2`<br>125 = `a125_btcOutputIrrational` | plausible |
| `PM_alertState` |  | PM ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `PM_a001_w0` | page 1 | PM ECU: a001 w0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a001_w1` | page 1 | PM ECU: a001 w1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a001_w2` | page 1 | PM ECU: a001 w2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a002_torqueAverage` | page 2 | PM ECU: a002 torque average | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a002_torqueWindow` | page 2 | PM ECU: a002 torque window | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a002_torqueMeasured` | page 2 | PM ECU: a002 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a002_torqueAccelAverage` | page 2 | PM ECU: a002 torque accel average; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a002_torqueAccelWindow` | page 2 | PM ECU: a002 torque accel window; raw 4096 = signal not available (SNA) | 48\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a003_torqueMeasured` | page 3 | PM ECU: a003 torque measured; raw 4096 = signal not available (SNA) | 16\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a003_torqueCommanded` | page 3 | PM ECU: a003 torque commanded; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a003_reverseGear` | page 3 | PM ECU: a003 reverse gear | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a003_pedalPos` | page 3 | PM ECU: a003 pedal pos | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `PM_a003_zeroPointPedal` | page 3 | PM ECU: a003 zero point pedal | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `PM_a004_torqueAverage` | page 4 | PM ECU: a004 torque average | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a004_torqueWindow` | page 4 | PM ECU: a004 torque window | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a004_torqueMeasured` | page 4 | PM ECU: a004 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a004_torqueDecelAverage` | page 4 | PM ECU: a004 torque decel average; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a004_torqueDecelWindow` | page 4 | PM ECU: a004 torque decel window; raw 4096 = signal not available (SNA) | 48\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a005_torqueReason` | page 5 | PM ECU: a005 torque reason | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TORQUE_IN_NEUTRAL`<br>1 = `CURRENT_IN_NEUTRAL`<br>2 = `SLAVE_ENABLE_IN_NEUTRAL` | plausible |
| `PM_a005_torqueMeasured` | page 5 | PM ECU: a005 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_a005_iDQmagnitude` | page 5 | PM ECU: a005 i d qmagnitude | 32\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PM_a006_unknownGearAllowed` | page 6 | PM ECU: a006 unknown gear allowed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_parkGearAllowed` | page 6 | PM ECU: a006 park gear allowed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_reverseGearAllowed` | page 6 | PM ECU: a006 reverse gear allowed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_neutralGearAllowed` | page 6 | PM ECU: a006 neutral gear allowed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_driveGearAllowed` | page 6 | PM ECU: a006 drive gear allowed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_shiftState` | page 6 | PM ECU: a006 shift state; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `PM_a006_brakePedalPress` | page 6 | PM ECU: a006 brake pedal press | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_accelPedalBelowLimit` | page 6 | PM ECU: a006 accel pedal below limit | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_allowReverseShiftSpeed` | page 6 | PM ECU: a006 allow reverse shift speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_allowDriveShiftSpeed` | page 6 | PM ECU: a006 allow drive shift speed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_requireAccelPedalCheckSpeed` | page 6 | PM ECU: a006 require accel pedal check speed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_requireParkSpeed` | page 6 | PM ECU: a006 require park speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_stalkCommandP` | page 6 | PM ECU: a006 stalk command p | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_stalkCommandR` | page 6 | PM ECU: a006 stalk command r | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_stalkCommandN` | page 6 | PM ECU: a006 stalk command n | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_stalkCommandD` | page 6 | PM ECU: a006 stalk command d | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_unsecuredNeutralRequest` | page 6 | PM ECU: a006 unsecured neutral request | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_recentGearChange` | page 6 | PM ECU: a006 recent gear change | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_smartShiftCommandD` | page 6 | PM ECU: a006 smart shift command d | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_smartShiftCommandR` | page 6 | PM ECU: a006 smart shift command r | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_driverSeatbeltBuckled` | page 6 | PM ECU: a006 driver seatbelt buckled | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_secGearSelRisingEdgeR` | page 6 | PM ECU: a006 sec gear sel rising edge r | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_secGearSelRisingEdgeN` | page 6 | PM ECU: a006 sec gear sel rising edge n | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_secGearSelRisingEdgeD` | page 6 | PM ECU: a006 sec gear sel rising edge d | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a007_IBST_party1` | page 7 | PM ECU: a007 IBST party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a007_BUS1_IBST_status` | page 7 | PM ECU: a007 BUS1 IBST status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a007_BUS2_IBST_status` | page 7 | PM ECU: a007 BUS2 IBST status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_brakeTorque` | page 9 | PM ECU: a009 ESP brake torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_motorLimits` | page 9 | PM ECU: a009 ESP motor limits | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_offsets` | page 9 | PM ECU: a009 ESP offsets | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_party3` | page 9 | PM ECU: a009 ESP party3 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_status` | page 9 | PM ECU: a009 ESP status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_ESP_wheelSpeeds` | page 9 | PM ECU: a009 ESP wheel speeds | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_messageId` | page 10 | PM ECU: a010 message id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a010_DI_status` | page 10 | PM ECU: a010 DI status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_torque` | page 10 | PM ECU: a010 DI torque | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_slaveCommand` | page 10 | PM ECU: a010 DI slave command | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_locStatus` | page 10 | PM ECU: a010 DI loc status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_speed` | page 10 | PM ECU: a010 DI speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_systemStatus` | page 10 | PM ECU: a010 DI system status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_chassisControl` | page 10 | PM ECU: a010 DI chassis control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_chassisControl2` | page 10 | PM ECU: a010 DI chassis control2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_vdcLeft` | page 10 | PM ECU: a010 vdc left | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_vdcRight` | page 10 | PM ECU: a010 vdc right | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_vehicleEstimates` | page 10 | PM ECU: a010 DI vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_brakeCommand` | page 10 | PM ECU: a010 DI brake command | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_autonomyHealth` | page 10 | PM ECU: a010 DI autonomy health | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_difCommand` | page 10 | PM ECU: a010 DI dif command | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_dirCommand` | page 10 | PM ECU: a010 DI dir command | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_dirVehicle` | page 10 | PM ECU: a010 DI dir vehicle | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_DI_locStatus2` | page 10 | PM ECU: a010 DI loc status2 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_stalklessInterfaces` | page 10 | PM ECU: a010 stalkless interfaces | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a011_pmfHvilStatus` | page 11 | PM ECU: a011 pmf hvil status; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |
| `PM_a011_pmfStatusValid` | page 11 | PM ECU: a011 pmf status valid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a011_pmrHvilStatus` | page 11 | PM ECU: a011 pmr hvil status; raw 3 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |
| `PM_a011_pmrStatusValid` | page 11 | PM ECU: a011 pmr status valid | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a011_vehiclePowerState` | page 11 | PM ECU: a011 vehicle power state | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `CONDITIONING`<br>2 = `ACCESSORY`<br>3 = `DRIVE` | plausible |
| `PM_a011_hvilSystemStatus` | page 11 | PM ECU: a011 hvil system status; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |
| `PM_a014_track1Voltage` | page 14 | PM ECU: a014 track1 voltage | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | plausible |
| `PM_a014_track2Voltage` | page 14 | PM ECU: a014 track2 voltage | 32\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | plausible |
| `PM_a014_accelErrorType` | page 14 | PM ECU: a014 accel error type; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `Accel1RangeError`<br>2 = `Accel2RangeError`<br>3 = `AccelTracksOutOfSync` | plausible |
| `PM_a015_SCCM_rightStalk` | page 15 | PM ECU: a015 SCCM right stalk | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a016_BB_status` | page 16 | PM ECU: a016 BB status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a016_BB_brakeActuation` | page 16 | PM ECU: a016 BB brake actuation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_EPBL_status` | page 17 | PM ECU: a017 EPBL status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_EPBR_status` | page 17 | PM ECU: a017 EPBR status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_EPBL_autonomyHealth` | page 17 | PM ECU: a017 EPBL autonomy health | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_EPBR_autonomyHealth` | page 17 | PM ECU: a017 EPBR autonomy health | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_torque` | page 21 | PM ECU: a021 torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_capability` | page 21 | PM ECU: a021 capability | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_status` | page 21 | PM ECU: a021 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_capability2` | page 21 | PM ECU: a021 capability2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_power` | page 21 | PM ECU: a021 power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_torque` | page 22 | PM ECU: a022 torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_capability` | page 22 | PM ECU: a022 capability | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_status` | page 22 | PM ECU: a022 status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_capability2` | page 22 | PM ECU: a022 capability2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_power` | page 22 | PM ECU: a022 power | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a023_diCrsState` | page 23 | PM ECU: a023 di crs state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a023_pmCrsState` | page 23 | PM ECU: a023 pm crs state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a023_crsFaultReason` | page 23 | PM ECU: a023 crs fault reason | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `EBR_FAULT`<br>2 = `ESP_FAULT`<br>3 = `ESP_MIA`<br>4 = `SCCM_MIA`<br>5 = `EPB_MIA`<br>6 = `WHEEL_SPDS_INVAL`<br>7 = `CONFIG`<br>9 = `EPB_FAULT`<br>10 = `TC_FAULT`<br>11 = `ACCEL_RQ`<br>12 = `JERK_RQ`<br>13 = `DI_MIA`<br>14 = `TORQUE`<br>15 = `ACCEL`<br>16 = `DECEL`<br>17 = `APC_FAULT`<br>18 = `VDC_FAULT`<br>19 = `GEAR` | plausible |
| `PM_a023_crsCancelReason` | page 23 | PM ECU: a023 crs cancel reason | 29\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `OFF_BTN`<br>2 = `AEB_ACTIVE`<br>3 = `GEAR`<br>4 = `ESP`<br>5 = `TC`<br>6 = `DAS`<br>7 = `EPB`<br>8 = `BRAKE`<br>9 = `STALK_CMD`<br>10 = `SKID` | plausible |
| `PM_a023_cruiseTorquePed` | page 23 | PM ECU: a023 cruise torque ped | 33\|11 | little-endian | signed | 1 | 0 | Nm | -1024 to 1023 |  | plausible |
| `PM_a023_wheelSpdEstimateAbs` | page 23 | PM ECU: a023 wheel spd estimate abs | 44\|10 | little-endian | unsigned | 0.25 | 0 | kph | 0 to 255.75 |  | plausible |
| `PM_a023_accelEstimateDis` | page 23 | PM ECU: a023 accel estimate dis | 54\|10 | little-endian | signed | 0.05 | -4.7 | m/s^2 | -30.3 to 20.85 |  | plausible |
| `PM_a025_powerOnReset` | page 25 | PM ECU: a025 power on reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_watchdogTimer0` | page 25 | PM ECU: a025 watchdog timer0 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_watchdogTimer1` | page 25 | PM ECU: a025 watchdog timer1 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_watchdogTimer2` | page 25 | PM ECU: a025 watchdog timer2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_watchdogTimer3` | page 25 | PM ECU: a025 watchdog timer3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_warmResetReq` | page 25 | PM ECU: a025 warm reset req | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_externalPadReset` | page 25 | PM ECU: a025 external pad reset | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_hwSecModuleWatchdogTimer` | page 25 | PM ECU: a025 hw sec module watchdog timer | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_debugReset` | page 25 | PM ECU: a025 debug reset | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_tempSense0` | page 25 | PM ECU: a025 temp sense0 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_tempSense1` | page 25 | PM ECU: a025 temp sense1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_reason` | page 26 | PM ECU: a026 reason | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TooSlow`<br>1 = `TooFast` | plausible |
| `PM_a026_isrCount20kHz` | page 26 | PM ECU: a026 isr count20k hz | 17\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `PM_a026_isrCount1kHz` | page 26 | PM ECU: a026 isr count1k hz | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PM_a026_switchingActive` | page 26 | PM ECU: a026 switching active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_systemStackOvf` | page 26 | PM ECU: a026 system stack ovf | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_controlStackOvf` | page 26 | PM ECU: a026 control stack ovf | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_idleStackOvf` | page 26 | PM ECU: a026 idle stack ovf | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_eepStackOvf` | page 26 | PM ECU: a026 eep stack ovf | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_immStackOvf` | page 26 | PM ECU: a026 imm stack ovf | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_xdcErrorIdMSW` | page 26 | PM ECU: a026 xdc error id MSW | 32\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `PM_a026_xdcErrorArg1` | page 26 | PM ECU: a026 xdc error arg1 | 42\|22 | little-endian | signed | 1 | 0 |  | -2097152 to 2097151 |  | layout-only |
| `PM_a030_diAebState` | page 30 | PM ECU: a030 di aeb state; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `FAULT`<br>5 = `UNAVAILABLE_ALERT`<br>7 = `SNA` | plausible |
| `PM_a030_pmAebState` | page 30 | PM ECU: a030 pm aeb state; raw 7 = signal not available (SNA) | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `FAULT`<br>5 = `UNAVAILABLE_ALERT`<br>7 = `SNA` | plausible |
| `PM_a030_dasAebEvent` | page 30 | PM ECU: a030 das aeb event; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE`<br>2 = `FAULT`<br>3 = `SNA` | plausible |
| `PM_a030_aebFaultReason` | page 30 | PM ECU: a030 aeb fault reason | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>2 = `ESP_MIA`<br>3 = `WHEEL_SPEEDS_INVALID`<br>4 = `EBR_FAULT`<br>5 = `ESP_FAULT`<br>6 = `SPEED_DELTA` | plausible |
| `PM_a030_aebUnavailableReason` | page 30 | PM ECU: a030 aeb unavailable reason | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNAVAILABLE_NONE`<br>1 = `UNAVAILBLE_EPB_PARK`<br>2 = `UNAVAILABLE_DI_STATE`<br>3 = `UNAVAILABLE_ESP_UNAVAILABLE`<br>4 = `UNAVAILABLE_SKID`<br>5 = `UNAVAILABLE_GEAR`<br>6 = `UNAVAILABLE_NEGATIVE_SPEED`<br>7 = `UNAVAILABLE_EBR`<br>8 = `UNAVAILABLE_REVERSE_SPEED`<br>9 = `UNAVAILABLE_DAS_CONTROL_MIA`<br>10 = `UNAVAILABLE_WHEEL_SPEEDS_INVALID`<br>11 = `UNAVAILABLE_ABS_FAULT` | plausible |
| `PM_a030_aebCancelReason` | page 30 | PM ECU: a030 aeb cancel reason | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `DAS`<br>2 = `EPB_FAULT` | plausible |
| `PM_a030_diBrakeTorqueCommand` | page 30 | PM ECU: a030 di brake torque command | 34\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a032_w0` | page 32 | PM ECU: a032 w0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a032_w1` | page 32 | PM ECU: a032 w1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a032_w2` | page 32 | PM ECU: a032 w2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a036_timeSinceTxHWI` | page 36 | PM ECU: a036 time since tx HWI | 16\|6 | little-endian | unsigned | 64 | 0 | us | 0 to 4032 |  | plausible |
| `PM_a036_timeSinceRxHWI` | page 36 | PM ECU: a036 time since rx HWI | 22\|6 | little-endian | unsigned | 64 | 0 | us | 0 to 4032 |  | plausible |
| `PM_a036_timeSince100HzTxSWI` | page 36 | PM ECU: a036 time since100 hz tx SWI | 28\|6 | little-endian | unsigned | 0.32 | 0 | ms | 0 to 20.16 |  | plausible |
| `PM_a036_timeSince1kHzCLK` | page 36 | PM ECU: a036 time since1k hz CLK | 34\|6 | little-endian | unsigned | 32 | 0 | us | 0 to 2016 |  | plausible |
| `PM_a036_timeSince1kHzSWI` | page 36 | PM ECU: a036 time since1k hz SWI | 40\|6 | little-endian | unsigned | 32 | 0 | us | 0 to 2016 |  | plausible |
| `PM_a036_timeSinceIdle` | page 36 | PM ECU: a036 time since idle | 46\|6 | little-endian | unsigned | 0.16 | 0 | ms | 0 to 10.08 |  | plausible |
| `PM_a036_ovfStackId` | page 36 | PM ECU: a036 ovf stack id; raw 15 = signal not available (SNA) | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 15 = `SNA` | plausible |
| `PM_a036_inTxISR` | page 36 | PM ECU: a036 in tx ISR | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_inTxHWI` | page 36 | PM ECU: a036 in tx HWI | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_inRxHWI` | page 36 | PM ECU: a036 in rx HWI | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_in1kHzSWI` | page 36 | PM ECU: a036 in1k hz SWI | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_in1kHzCLK` | page 36 | PM ECU: a036 in1k hz CLK | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_in100HzCLK` | page 36 | PM ECU: a036 in100 hz CLK | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_in10HzCLK` | page 36 | PM ECU: a036 in10 hz CLK | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_in1HzCLK` | page 36 | PM ECU: a036 in1 hz CLK | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a038_masterTorque` | page 38 | PM ECU: a038 master torque | 16\|13 | little-endian | signed | 0.4 | 0 | Nm | -1638.4 to 1638 |  | plausible |
| `PM_a038_slaveTorque` | page 38 | PM ECU: a038 slave torque | 32\|13 | little-endian | signed | 0.4 | 0 | Nm | -1638.4 to 1638 |  | plausible |
| `PM_a038_pedalPos` | page 38 | PM ECU: a038 pedal pos | 48\|8 | little-endian | signed | 0.4 | 50.4 | % | -0.8 to 101.2 |  | plausible |
| `PM_a039_DIS_status` | page 39 | PM ECU: a039 DIS status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a039_DIS_torque` | page 39 | PM ECU: a039 DIS torque | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a039_messageId` | page 39 | PM ECU: a039 message id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a041_DAS_control` | page 41 | PM ECU: a041 DAS control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_longControl` | page 41 | PM ECU: a041 DAS long control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_longControlTuningParameters` | page 41 | PM ECU: a041 DAS long control tuning parameters | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_status` | page 41 | PM ECU: a041 DAS status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_status2` | page 41 | PM ECU: a041 DAS status2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_smartShift` | page 41 | PM ECU: a041 DAS smart shift | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_DAS_autonomyControl` | page 41 | PM ECU: a041 DAS autonomy control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a042_GTW_carConfig` | page 42 | PM ECU: a042 GTW car config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a042_GTW_time` | page 42 | PM ECU: a042 GTW time | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a042_GTW_drivetrainType` | page 42 | PM ECU: a042 GTW drivetrain type | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RWD`<br>1 = `AWD` | plausible |
| `PM_a042_expectedPerformanceCfg` | page 42 | PM ECU: a042 expected performance cfg | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RWD`<br>1 = `AWD` | plausible |
| `PM_a042_gearControl` | page 42 | PM ECU: a042 gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_configInconsistent` | page 43 | PM ECU: a043 config inconsistent | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_GTW_autopilot` | page 43 | PM ECU: a043 GTW autopilot | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_expectedAutopilot` | page 43 | PM ECU: a043 expected autopilot | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_GTW_drivetrainType` | page 43 | PM ECU: a043 GTW drivetrain type | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_a043_expectedDrivetrainType` | page 43 | PM ECU: a043 expected drivetrain type | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_a043_GTW_chassisType` | page 43 | PM ECU: a043 GTW chassis type | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_a043_expectedChassisType` | page 43 | PM ECU: a043 expected chassis type | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_a043_packEnergy` | page 43 | PM ECU: a043 pack energy | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_packPerformanceDeviation` | page 43 | PM ECU: a043 pack performance deviation | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_performancePackage` | page 43 | PM ECU: a043 performance package | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_GTW_vdcType` | page 43 | PM ECU: a043 GTW vdc type | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_expectedVdcType` | page 43 | PM ECU: a043 expected vdc type | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_brakeHWType` | page 43 | PM ECU: a043 brake HW type | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_cabinPTCHeaterType` | page 43 | PM ECU: a043 cabin PTC heater type | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_softPerformanceLimit` | page 43 | PM ECU: a043 soft performance limit | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_GTW_dasHw` | page 43 | PM ECU: a043 GTW das hw | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a044_pmCruiseState` | page 44 | PM ECU: a044 pm cruise state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a044_diCruiseState` | page 44 | PM ECU: a044 di cruise state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a044_pmAebState` | page 44 | PM ECU: a044 pm aeb state; raw 7 = signal not available (SNA) | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `FAULT`<br>5 = `UNAVAILABLE_ALERT`<br>7 = `SNA` | plausible |
| `PM_a044_diAebState` | page 44 | PM ECU: a044 di aeb state; raw 7 = signal not available (SNA) | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `FAULT`<br>5 = `UNAVAILABLE_ALERT`<br>7 = `SNA` | plausible |
| `PM_a044_diBrakeTorqueCommand` | page 44 | PM ECU: a044 di brake torque command | 30\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a044_pmBfillTorqueAllowed` | page 44 | PM ECU: a044 pm bfill torque allowed | 43\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a044_pmVehicleHoldState` | page 44 | PM ECU: a044 pm vehicle hold state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `BLEND_IN`<br>3 = `STANDSTILL`<br>4 = `BLEND_OUT`<br>5 = `PARK`<br>6 = `FAULT`<br>7 = `INIT` | plausible |
| `PM_a044_diVehicleHoldState` | page 44 | PM ECU: a044 di vehicle hold state | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `BLEND_IN`<br>3 = `STANDSTILL`<br>4 = `BLEND_OUT`<br>5 = `PARK`<br>6 = `FAULT`<br>7 = `INIT` | plausible |
| `PM_a044_regenBackfillPmState` | page 44 | PM ECU: a044 regen backfill pm state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ACTIVE` | plausible |
| `PM_a045_regenBackfillPmState` | page 45 | PM ECU: a045 regen backfill pm state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ACTIVE` | plausible |
| `PM_a045_regenBackfillDiState` | page 45 | PM ECU: a045 regen backfill di state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ACTIVE` | plausible |
| `PM_a045_unavailableReason` | page 45 | PM ECU: a045 unavailable reason | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `GTW_DISABLE`<br>2 = `UI_DISABLE`<br>3 = `EBR_UNAVAILABLE`<br>4 = `NON_DRIVE_GEAR`<br>5 = `SYSTEM_STATE`<br>6 = `UI_COASTDOWN_MODE`<br>7 = `ACTIVE_DAMPING_UNAVAILABLE`<br>8 = `TRACTION_CONTROL_UNAVAILABLE`<br>9 = `VELOCITY_ESTIMATOR_UNAVAILABLE`<br>10 = `TRACK_MODE_ACTIVE`<br>11 = `PM_DISABLE_REQUEST`<br>12 = `EBR_FAULT`<br>13 = `BRAKE_TEMP`<br>14 = `CARBON_CERAMIC_BRAKES`<br>15 = `PM_DISABLE_REQUEST_BLEND`<br>16 = `PM_DISABLE_REQUEST_BPED`<br>17 = `EBR_FULL_FAULT`<br>18 = `DI_LATENT_FAULT_TRIP` | plausible |
| `PM_a045_diBrakeTorqueCommand` | page 45 | PM ECU: a045 di brake torque command | 32\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a045_pmBrakeTorqueAllowed` | page 45 | PM ECU: a045 pm brake torque allowed | 48\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a046_diVhldState` | page 46 | PM ECU: a046 di vhld state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `BLEND_IN`<br>3 = `STANDSTILL`<br>4 = `BLEND_OUT`<br>5 = `PARK`<br>6 = `FAULT`<br>7 = `INIT` | plausible |
| `PM_a046_pmVhldState` | page 46 | PM ECU: a046 pm vhld state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `BLEND_IN`<br>3 = `STANDSTILL`<br>4 = `BLEND_OUT`<br>5 = `PARK`<br>6 = `FAULT`<br>7 = `INIT` | plausible |
| `PM_a046_vhldFaultReason` | page 46 | PM ECU: a046 vhld fault reason | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `EBR_FAULT`<br>2 = `BRAKE_INVALID`<br>3 = `ESP_FAULT`<br>4 = `ESP_MIA`<br>5 = `EPB_MIA`<br>6 = `WHEEL_SPDS_INVAL`<br>7 = `REQUESTED` | plausible |
| `PM_a046_vhldUnavailableReason` | page 46 | PM ECU: a046 vhld unavailable reason | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `EPB`<br>2 = `EPB_FAULT`<br>3 = `DI_FAULT`<br>4 = `SKID`<br>5 = `GEAR`<br>6 = `SPEED`<br>7 = `CRUISE_ACTIVE`<br>8 = `AEB_ACTIVE`<br>9 = `EBR` | plausible |
| `PM_a046_diBrakeTorqueCommand` | page 46 | PM ECU: a046 di brake torque command | 32\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | plausible |
| `PM_a046_diBrakeCommandType` | page 46 | PM ECU: a046 di brake command type | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `PM_a047_pmAutoparkState` | page 47 | PM ECU: a047 pm autopark state; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `STARTED`<br>3 = `ACTIVE`<br>4 = `COMPLETE`<br>5 = `PAUSED`<br>6 = `ABORTED`<br>7 = `RESUMED`<br>8 = `UNPARK_COMPLETE`<br>9 = `SELFPARK_STARTED`<br>15 = `SNA` | plausible |
| `PM_a047_diAutoparkState` | page 47 | PM ECU: a047 di autopark state; raw 15 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `STARTED`<br>3 = `ACTIVE`<br>4 = `COMPLETE`<br>5 = `PAUSED`<br>6 = `ABORTED`<br>7 = `RESUMED`<br>8 = `UNPARK_COMPLETE`<br>9 = `SELFPARK_STARTED`<br>15 = `SNA` | plausible |
| `PM_a047_autoparkCancelReason` | page 47 | PM ECU: a047 autopark cancel reason | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CANCEL_NONE`<br>1 = `CANCEL_BRAKE_APPLY`<br>2 = `CRUISE_CANCEL_TIMEOUT`<br>3 = `CANCEL_SPEED_VIOLATION` | plausible |
| `PM_a048_vdcFaultReason` | page 48 | PM ECU: a048 vdc fault reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `DECEL_INABILITY`<br>2 = `DECEL_UNINTENDED`<br>3 = `REVERSAL_YAW_TORQUE`<br>4 = `EXCESSIVE_YAW_TORQUE`<br>5 = `INVALID_GEAR`<br>6 = `INVALID_REQUEST`<br>7 = `EXCESSIVE_TSC_ACTIVITY`<br>8 = `CP_ESTIMATE_MISMATCH`<br>9 = `OUTPUT_RATIONALITY` | plausible |
| `PM_a053_LVPowerState` | page 53 | PM ECU: a053 LV power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_coolant` | page 53 | PM ECU: a053 coolant | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_vcleftSwitchStatus` | page 53 | PM ECU: a053 vcleft switch status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_restraintStatus` | page 53 | PM ECU: a053 restraint status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_sensors` | page 53 | PM ECU: a053 sensors | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiPowertrainControl` | page 54 | PM ECU: a054 ui powertrain control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiChassisControl` | page 54 | PM ECU: a054 ui chassis control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiCruiseControl` | page 54 | PM ECU: a054 ui cruise control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiTrackModeSettings` | page 54 | PM ECU: a054 ui track mode settings | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiTPMSRCPSetting` | page 54 | PM ECU: a054 ui TPMSRCP setting | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a058_CMP_HVStatus` | page 58 | PM ECU: a058 CMP HV status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a058_CMPD_state` | page 58 | PM ECU: a058 CMPD state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a059_PTC_feedbackStatus` | page 59 | PM ECU: a059 PTC feedback status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a060_TorqueAccelWindow` | page 60 | PM ECU: a060 torque accel window | 16\|16 | little-endian | signed | 0.05 | 0 | NmS | -1638.4 to 1638.35 |  | plausible |
| `PM_a060_TorqueDecelWindow` | page 60 | PM ECU: a060 torque decel window | 32\|16 | little-endian | signed | 0.05 | 0 | NmS | -1638.4 to 1638.35 |  | plausible |
| `PM_a060_TorqueReversalWindow` | page 60 | PM ECU: a060 torque reversal window | 48\|16 | little-endian | signed | 0.05 | 0 | NmS | -1638.4 to 1638.35 |  | plausible |
| `PM_a061_diIpcVersion` | page 61 | PM ECU: a061 di ipc version | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a061_pmIpcVersion` | page 61 | PM ECU: a061 pm ipc version | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a062_address` | page 62 | PM ECU: a062 address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PM_a062_errorType` | page 62 | PM ECU: a062 error type | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `FLASH_UNCORRECTABLE_LOW`<br>2 = `FLASH_UNCORRECTABLE_HIGH`<br>3 = `FLASH_FAIL0_LOW`<br>4 = `FLASH_FAIL0_HIGH`<br>5 = `FLASH_FAIL1_LOW`<br>6 = `FLASH_FAIL1_HIGH`<br>7 = `RAM_UNCORRECTABLE_CPU`<br>8 = `RAM_UNCORRECTABLE_CLA`<br>9 = `RAM_UNCORRECTABLE_DMA`<br>10 = `RAM_CORRECTABLE_CPU`<br>11 = `RAM_CORRECTABLE_CLA`<br>12 = `RAM_CORRECTABLE_DMA` | plausible |
| `PM_a062_detectedByRamScrub` | page 62 | PM ECU: a062 detected by ram scrub | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a063_totalSystemTorqueCommand` | page 63 | PM ECU: a063 total system torque command | 16\|13 | little-endian | signed | 0.4 | 0 | Nm | -1638.4 to 1638 |  | plausible |
| `PM_a063_totalSystemTorqueMeasured` | page 63 | PM ECU: a063 total system torque measured | 32\|13 | little-endian | signed | 0.4 | 0 | Nm | -1638.4 to 1638 |  | plausible |
| `PM_a064_interventionType` | page 64 | PM ECU: a064 intervention type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `masterTorqueMonitorShutoff`<br>1 = `resolver`<br>2 = `torqueCmdInvalid`<br>3 = `cruiseFault`<br>4 = `motorMovementDetected`<br>5 = `accumulatedTorque`<br>6 = `torqueReversal`<br>7 = `excessiveRegenTorque`<br>8 = `torqueInNeutral`<br>9 = `inconsistentTorqueSign`<br>10 = `switchOffPathTestFail`<br>11 = `switchingAfterIntervention`<br>12 = `currentAfterIntervention`<br>13 = `diHeartbeat`<br>14 = `inconsistentAxleTorque`<br>15 = `excessiveMotorMz` | plausible |
| `PM_a064_torqueCmdState` | page 64 | PM ECU: a064 torque cmd state; raw 0 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>6 = `Valid`<br>8 = `Invalid` | plausible |
| `PM_a064_shortDetectedByDI` | page 64 | PM ECU: a064 short detected by DI | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a064_UI_stoppingMode` | page 64 | PM ECU: a064 UI stopping mode | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `CREEP`<br>2 = `HOLD` | plausible |
| `PM_a064_diCrsState` | page 64 | PM ECU: a064 di crs state | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a064_pmCrsState` | page 64 | PM ECU: a064 pm crs state | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PM_a066_state4` | page 66 | PM ECU: a066 state4 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a067_state4` | page 67 | PM ECU: a067 state4 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_unitTorqueActualMonitor` | page 70 | PM ECU: a070 unit torque actual monitor | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_TRIP`<br>1 = `TRIP_EXCESSIVE_BRAKING`<br>2 = `TRIP_UNINTENDED_BRAKING`<br>3 = `TRIP_UNDER_BRAKING`<br>4 = `TRIP_SOFT_LANDING` | plausible |
| `PM_a070_unitTorqueCommandedMonitor` | page 70 | PM ECU: a070 unit torque commanded monitor | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_TRIP`<br>1 = `TRIP_EXCESSIVE_BRAKING`<br>2 = `TRIP_UNINTENDED_BRAKING`<br>3 = `TRIP_UNDER_BRAKING`<br>4 = `TRIP_SOFT_LANDING` | plausible |
| `PM_a070_diTorqueCommandedMonitor` | page 70 | PM ECU: a070 di torque commanded monitor | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_TRIP`<br>1 = `TRIP_EXCESSIVE_BRAKING`<br>2 = `TRIP_UNINTENDED_BRAKING`<br>3 = `TRIP_UNDER_BRAKING`<br>4 = `TRIP_SOFT_LANDING` | plausible |
| `PM_a070_rearAxleMotorTorqueLimitExceeded` | page 70 | PM ECU: a070 rear axle motor torque limit exceeded | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_areAllInputsValid` | page 70 | PM ECU: a070 are all inputs valid | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_isBrakeBlendingAvailable` | page 70 | PM ECU: a070 is brake blending available | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_faultReason` | page 70 | PM ECU: a070 fault reason | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `BRAKE_BOOSTER`<br>2 = `REGEN_BLENDING`<br>3 = `BRAKE_PEDAL_MAP`<br>4 = `TORQUE_CMD_RATIONALITY`<br>5 = `MISSING_INPUTS`<br>6 = `PM_UNHEALTHY`<br>7 = `EBR_OR_BACKFILL`<br>8 = `REAR_AXLE_TORQUE_LIM`<br>9 = `VELOCITY_EST_FAULT`<br>10 = `EBR_INVALID_NONZERO`<br>11 = `SOFT_LANDING` | plausible |
| `PM_a079_VEH_RCU_actuation` | page 79 | PM ECU: a079 VEH RCU actuation | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a079_PARTY_RCU_actuation` | page 79 | PM ECU: a079 PARTY RCU actuation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a082_faultAddress` | page 82 | PM ECU: a082 fault address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PM_a082_isWriteNotRead` | page 82 | PM ECU: a082 is write not read | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a084_faultAddress` | page 84 | PM ECU: a084 fault address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PM_a084_firewallId` | page 84 | PM ECU: a084 firewall id | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `L2OCRAM_BANK0_SLV`<br>1 = `L2OCRAM_BANK1_SLV`<br>2 = `L2OCRAM_BANK2_SLV`<br>3 = `L2OCRAM_BANK3_SLV`<br>4 = `R5SS0_CORE0_AXIS_SLV`<br>5 = `R5SS0_CORE1_AXIS_SLV`<br>6 = `R5SS1_CORE0_AXIS_SLV`<br>7 = `R5SS1_CORE1_AXIS_SLV`<br>8 = `DTHE_SLV`<br>9 = `MBOX_RAM_SLV`<br>10 = `QSPI0_SLV`<br>11 = `SCRM2SCRP0_SLV`<br>12 = `SCRM2SCRP1_SLV`<br>13 = `R5SS0_CORE0_AHB_MST`<br>14 = `R5SS0_CORE1_AHB_MST`<br>15 = `R5SS1_CORE0_AHB_MST`<br>16 = `R5SS1_CORE1_AHB_MST`<br>17 = `HSM_SLV` | plausible |
| `PM_a084_privId` | page 84 | PM ECU: a084 priv id | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 1 = `M4FSS0_0`<br>4 = `R5FSS0_0`<br>5 = `R5FSS0_1`<br>6 = `R5FSS1_0`<br>7 = `R5FSS1_1`<br>9 = `ICSSM`<br>10 = `CPSW` | plausible |
| `PM_a084_ns` | page 84 | PM ECU: a084 ns | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a084_faultType` | page 84 | PM ECU: a084 fault type | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_FAULT`<br>1 = `USER_EXE`<br>2 = `USER_WRITE`<br>3 = `USER_READ`<br>4 = `SUPER_EXE`<br>5 = `SUPER_WRITE`<br>6 = `SUPER_READ` | plausible |
| `PM_a085_DPB_actuator3` | page 85 | PM ECU: a085 DPB actuator3 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a087_mailboxID` | page 87 | PM ECU: a087 mailbox ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a087_canID` | page 87 | PM ECU: a087 can ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PM_a087_errorType` | page 87 | PM ECU: a087 error type | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RX`<br>1 = `TX`<br>2 = `RX_OVERRUN`<br>3 = `TX_OVERRUN`<br>4 = `IPC_RX_OVERRUN`<br>5 = `IPC_TX_OVERRUN` | plausible |
| `PM_a092_pllClockSource` | page 92 | PM ECU: a092 pll clock source | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INTOSC2`<br>1 = `XTAL`<br>2 = `INTOSC1` | plausible |
| `PM_a100_index1kHzPeriodic` | page 100 | PM ECU: a100 index1k hz periodic | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a100_index100HzPeriodic` | page 100 | PM ECU: a100 index100 hz periodic | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a100_index10HzPeriodic` | page 100 | PM ECU: a100 index10 hz periodic | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a100_indexSWI` | page 100 | PM ECU: a100 index SWI | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a100_eepEvent` | page 100 | PM ECU: a100 eep event | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PM_a100_module500HzActive` | page 100 | PM ECU: a100 module500 hz active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_module50HzActive` | page 100 | PM ECU: a100 module50 hz active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_module1HzActive` | page 100 | PM ECU: a100 module1 hz active | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_task10HzActive` | page 100 | PM ECU: a100 task10 hz active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_taskUdsActive` | page 100 | PM ECU: a100 task uds active | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a110_itpmsWarningFrL` | page 110 | PM ECU: a110 itpms warning fr l | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a110_itpmsWarningFrR` | page 110 | PM ECU: a110 itpms warning fr r | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a110_itpmsWarningReL` | page 110 | PM ECU: a110 itpms warning re l | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a110_itpmsWarningReR` | page 110 | PM ECU: a110 itpms warning re r | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a111_prevGearUnit0` | page 111 | PM ECU: a111 prev gear unit0; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `PM_a111_prevGearUnit1` | page 111 | PM ECU: a111 prev gear unit1; raw 7 = signal not available (SNA) | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `PM_a111_prevGearUnit2` | page 111 | PM ECU: a111 prev gear unit2; raw 7 = signal not available (SNA) | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `PM_a111_vehicleSpeed` | page 111 | PM ECU: a111 vehicle speed | 27\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `PM_a111_recoveryTargetGear` | page 111 | PM ECU: a111 recovery target gear; raw 7 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `INVALID`<br>1 = `P`<br>2 = `R`<br>3 = `N`<br>4 = `D`<br>7 = `SNA` | plausible |
| `PM_a111_unitsConsensus` | page 111 | PM ECU: a111 units consensus | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a111_speedPolarityMatch` | page 111 | PM ECU: a111 speed polarity match | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a111_failureReason` | page 111 | PM ECU: a111 failure reason | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RECOVERY_SUCCESS`<br>1 = `EEPROM_INVALID`<br>2 = `RETRY_LIMIT_EXCEEDED`<br>3 = `UNIT_CONSENSUS_FAILED`<br>4 = `NOT_IN_NEUTRAL`<br>5 = `EPB_MIA_OR_ENGAGED`<br>6 = `SPEED_POLARITY_MISMATCH`<br>7 = `SSM_NOT_READY`<br>8 = `EEPROM_WRITE_FAILED`<br>9 = `NO_UNINTENDED_RESET`<br>10 = `SAFETY_CONDITIONS_CHANGED` | plausible |
| `PM_a112_itpmsWarningFrL` | page 112 | PM ECU: a112 itpms warning fr l | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a112_itpmsWarningFrR` | page 112 | PM ECU: a112 itpms warning fr r | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a112_itpmsWarningReL` | page 112 | PM ECU: a112 itpms warning re l | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a112_itpmsWarningReR` | page 112 | PM ECU: a112 itpms warning re r | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | plausible |
| `PM_a120_diMIA` | page 120 | PM ECU: a120 di MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_diUnitsMIA` | page 120 | PM ECU: a120 di units MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_rcmMIA` | page 120 | PM ECU: a120 rcm MIA | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_wssMIA` | page 120 | PM ECU: a120 wss MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_gtwMIA` | page 120 | PM ECU: a120 gtw MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_vcMIA` | page 120 | PM ECU: a120 vc MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_steeringMIA` | page 120 | PM ECU: a120 steering MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_gnssEpochMIA` | page 120 | PM ECU: a120 gnss epoch MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (3 signals), page 2 (5 signals), page 3 (5 signals), page 4 (5 signals), page 5 (3 signals), page 6 (24 signals), page 7 (3 signals), page 9 (6 signals), page 10 (19 signals), page 11 (6 signals), page 14 (3 signals), page 15 (1 signals), page 16 (2 signals), page 17 (4 signals), page 21 (5 signals), page 22 (5 signals), page 23 (7 signals), page 25 (11 signals), page 26 (11 signals), page 30 (7 signals), page 32 (3 signals), page 36 (15 signals), page 38 (3 signals), page 39 (3 signals), page 41 (7 signals), page 42 (5 signals), page 43 (16 signals), page 44 (9 signals), page 45 (5 signals), page 46 (6 signals), page 47 (3 signals), page 48 (1 signals), page 53 (5 signals), page 54 (5 signals), page 58 (2 signals), page 59 (1 signals), page 60 (3 signals), page 61 (2 signals), page 62 (3 signals), page 63 (2 signals), page 64 (6 signals), page 66 (1 signals), page 67 (1 signals), page 70 (7 signals), page 79 (2 signals), page 82 (2 signals), page 84 (5 signals), page 85 (1 signals), page 87 (3 signals), page 92 (1 signals), page 100 (10 signals), page 110 (4 signals), page 111 (8 signals), page 112 (4 signals), page 120 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
