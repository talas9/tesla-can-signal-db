---
layout: default
title: "PMF_alertMatrix (0x304) — PMF ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "PMF ECU message: alert matrix. Tesla Model 3 CAN bus message PMF_alertMatrix (0x304) of PMF ECU, firmware 2026.26.6.5, 53 signals (PMF_matrixIndex, PMF_a001_absoluteTorque, PMF_a002_excessiveAccelTorque, PMF_a003_excessiveReversalTorque and 49 more). Bit layout, scaling, units and value tables."
---

# PMF_alertMatrix (0x304) — PMF ECU, Tesla Model 3 2026.26.6.5 VEH CAN

PMF ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 53 signals of PMF_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_alertMatrix` |
| CAN id | 0x304 (772) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 53 |

## Signals of PMF_alertMatrix

Tesla Model 3 CAN bus signals in `PMF_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_matrixIndex` | selector | PMF ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `PMF_a001_absoluteTorque` | page 0 | PMF ECU: a001 absolute torque | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a002_excessiveAccelTorque` | page 0 | PMF ECU: a002 excessive accel torque | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a003_excessiveReversalTorque` | page 0 | PMF ECU: a003 excessive reversal torque | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a004_excessiveDecelTorque` | page 0 | PMF ECU: a004 excessive decel torque | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a005_torqueInNeutralOrPark` | page 0 | PMF ECU: a005 torque in neutral or park | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a006_underTorqueCheck` | page 0 | PMF ECU: a006 under torque check | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a008_memoryError` | page 0 | PMF ECU: a008 memory error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_diMIA` | page 0 | PMF ECU: a010 di MIA | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a011_phaseCurrentIrrational` | page 0 | PMF ECU: a011 phase current irrational | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a012_canDataBusA` | page 0 | PMF ECU: a012 can data bus a | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a013_canHardwareBusA` | page 0 | PMF ECU: a013 can hardware bus a | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a017_brakeMIA` | page 0 | PMF ECU: a017 brake MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a018_encoderIrrational` | page 0 | PMF ECU: a018 encoder irrational | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a019_statorTempIrrational` | page 0 | PMF ECU: a019 stator temp irrational | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_unintendedReset` | page 0 | PMF ECU: a025 unintended reset | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_diHeartBeatMIA` | page 0 | PMF ECU: a026 di heart beat MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a027_torqueEstimationOutOfBounds` | page 0 | PMF ECU: a027 torque estimation out of bounds | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a028_torqueCmdError` | page 0 | PMF ECU: a028 torque cmd error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a031_highStackUsage` | page 0 | PMF ECU: a031 high stack usage | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a032_registerConfigError` | page 0 | PMF ECU: a032 register config error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a033_selfTest` | page 0 | PMF ECU: a033 self test | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a034_trqCrossCheck` | page 0 | PMF ECU: a034 trq cross check | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a035_udsTransactionInitiated` | page 0 | PMF ECU: a035 uds transaction initiated | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_preWatchdog` | page 0 | PMF ECU: a036 pre watchdog | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a037_hvpMIA` | page 0 | PMF ECU: a037 hvp MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a039_disMIA` | page 0 | PMF ECU: a039 dis MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a040_pmMIA` | page 0 | PMF ECU: a040 pm MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a042_gtwMIA` | page 0 | PMF ECU: a042 gtw MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a045_motorMovementDetected` | page 0 | PMF ECU: a045 motor movement detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_vcfrontMIA` | page 0 | PMF ECU: a053 vcfront MIA | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiMIA` | page 0 | PMF ECU: a054 ui MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_resolver` | page 0 | PMF ECU: a055 resolver | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a056_canHardwareBusB` | page 0 | PMF ECU: a056 can hardware bus b | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a057_canDataBusB` | page 0 | PMF ECU: a057 can data bus b | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a058_measuredHvilCurrentFrozen` | page 0 | PMF ECU: a058 measured hvil current frozen | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a061_DIPMVersionMismatch` | page 1 | PMF ECU: a061 DIPM version mismatch | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a062_eccError` | page 1 | PMF ECU: a062 ecc error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a064_torqueIntervention` | page 1 | PMF ECU: a064 torque intervention | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a080_exceptionPrefetchAbort` | page 1 | PMF ECU: a080 exception prefetch abort | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a081_exceptionDataAbort` | page 1 | PMF ECU: a081 exception data abort | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a082_exceptionDataAbort2` | page 1 | PMF ECU: a082 exception data abort2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a083_ahbWriteError` | page 1 | PMF ECU: a083 ahb write error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a084_exceptionMpuFirewall` | page 1 | PMF ECU: a084 exception mpu firewall | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a086_exceptionUndefinedInstruction` | page 1 | PMF ECU: a086 exception undefined instruction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a092_xtalOscillator` | page 1 | PMF ECU: a092 xtal oscillator | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a094_safetyICWarn` | page 1 | PMF ECU: a094 safety IC warn | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a095_safetyICFault` | page 1 | PMF ECU: a095 safety IC fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a096_safetyICDebug` | page 1 | PMF ECU: a096 safety IC debug | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a097_lowFlowAlmostTripped` | page 1 | PMF ECU: a097 low flow almost tripped | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_diTraceInfo1` | page 1 | PMF ECU: a100 di trace info1 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a114_ramScrubTimedOut` | page 1 | PMF ECU: a114 ram scrub timed out | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a121_unintendedReset2` | page 2 | PMF ECU: a121 unintended reset2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PMF_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (35 signals), page 1 (16 signals), page 2 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
