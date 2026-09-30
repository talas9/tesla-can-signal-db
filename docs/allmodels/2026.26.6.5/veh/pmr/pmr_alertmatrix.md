---
layout: default
title: "PMR_alertMatrix (0x386) — PMR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "PMR ECU message: alert matrix. Tesla Model 3 / Model Y CAN bus message PMR_alertMatrix (0x386) of PMR ECU, firmware 2026.26.6.5, 55 signals (PMR_matrixIndex, PMR_a001_absoluteTorque, PMR_a002_excessiveAccelTorque, PMR_a003_excessiveReversalTorque and 51 more). Bit layout, scaling, units and value tables."
---

# PMR_alertMatrix (0x386) — PMR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

PMR ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 55 signals of PMR_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_alertMatrix` |
| CAN id | 0x386 (902) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 55 |

## Signals of PMR_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `PMR_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_matrixIndex` | selector | PMR ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `PMR_a001_absoluteTorque` | page 0 | PMR ECU: a001 absolute torque | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a002_excessiveAccelTorque` | page 0 | PMR ECU: a002 excessive accel torque | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a003_excessiveReversalTorque` | page 0 | PMR ECU: a003 excessive reversal torque | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a004_excessiveDecelTorque` | page 0 | PMR ECU: a004 excessive decel torque | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a005_torqueInNeutralOrPark` | page 0 | PMR ECU: a005 torque in neutral or park | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a006_underTorqueCheck` | page 0 | PMR ECU: a006 under torque check | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a008_memoryError` | page 0 | PMR ECU: a008 memory error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a010_diMIA` | page 0 | PMR ECU: a010 di MIA | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a011_phaseCurrentIrrational` | page 0 | PMR ECU: a011 phase current irrational | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a012_canDataBusA` | page 0 | PMR ECU: a012 can data bus a | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a013_canHardwareBusA` | page 0 | PMR ECU: a013 can hardware bus a | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a017_brakeMIA` | page 0 | PMR ECU: a017 brake MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a018_encoderIrrational` | page 0 | PMR ECU: a018 encoder irrational | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a019_statorTempIrrational` | page 0 | PMR ECU: a019 stator temp irrational | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a025_unintendedReset` | page 0 | PMR ECU: a025 unintended reset | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a026_diHeartBeatMIA` | page 0 | PMR ECU: a026 di heart beat MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a027_torqueEstimationOutOfBounds` | page 0 | PMR ECU: a027 torque estimation out of bounds | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a028_torqueCmdError` | page 0 | PMR ECU: a028 torque cmd error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a031_highStackUsage` | page 0 | PMR ECU: a031 high stack usage | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a032_registerConfigError` | page 0 | PMR ECU: a032 register config error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a033_selfTest` | page 0 | PMR ECU: a033 self test | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a034_trqCrossCheck` | page 0 | PMR ECU: a034 trq cross check | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a035_udsTransactionInitiated` | page 0 | PMR ECU: a035 uds transaction initiated | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a036_preWatchdog` | page 0 | PMR ECU: a036 pre watchdog | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a037_hvpMIA` | page 0 | PMR ECU: a037 hvp MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a039_disMIA` | page 0 | PMR ECU: a039 dis MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a040_pmMIA` | page 0 | PMR ECU: a040 pm MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a042_gtwMIA` | page 0 | PMR ECU: a042 gtw MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a045_motorMovementDetected` | page 0 | PMR ECU: a045 motor movement detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a053_vcfrontMIA` | page 0 | PMR ECU: a053 vcfront MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a054_uiMIA` | page 0 | PMR ECU: a054 ui MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a055_resolver` | page 0 | PMR ECU: a055 resolver | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a056_canHardwareBusB` | page 0 | PMR ECU: a056 can hardware bus b | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a057_canDataBusB` | page 0 | PMR ECU: a057 can data bus b | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a058_measuredHvilCurrentFrozen` | page 0 | PMR ECU: a058 measured hvil current frozen | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a061_DIPMVersionMismatch` | page 1 | PMR ECU: a061 DIPM version mismatch | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a062_eccError` | page 1 | PMR ECU: a062 ecc error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a064_torqueIntervention` | page 1 | PMR ECU: a064 torque intervention | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a080_exceptionPrefetchAbort` | page 1 | PMR ECU: a080 exception prefetch abort | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a081_exceptionDataAbort` | page 1 | PMR ECU: a081 exception data abort | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a082_exceptionDataAbort2` | page 1 | PMR ECU: a082 exception data abort2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a083_ahbWriteError` | page 1 | PMR ECU: a083 ahb write error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a084_exceptionMpuFirewall` | page 1 | PMR ECU: a084 exception mpu firewall | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a086_exceptionUndefinedInstruction` | page 1 | PMR ECU: a086 exception undefined instruction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a092_xtalOscillator` | page 1 | PMR ECU: a092 xtal oscillator | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a094_safetyICWarn` | page 1 | PMR ECU: a094 safety IC warn | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a095_safetyICFault` | page 1 | PMR ECU: a095 safety IC fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a096_safetyICDebug` | page 1 | PMR ECU: a096 safety IC debug | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a097_lowFlowAlmostTripped` | page 1 | PMR ECU: a097 low flow almost tripped | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a100_diTraceInfo1` | page 1 | PMR ECU: a100 di trace info1 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a101_hwVoltageMonitorTrip` | page 1 | PMR ECU: a101 hw voltage monitor trip | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a102_ipcFluidTempHigh` | page 1 | PMR ECU: a102 ipc fluid temp high | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a114_ramScrubTimedOut` | page 1 | PMR ECU: a114 ram scrub timed out | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a121_unintendedReset2` | page 2 | PMR ECU: a121 unintended reset2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PMR_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (35 signals), page 1 (18 signals), page 2 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
