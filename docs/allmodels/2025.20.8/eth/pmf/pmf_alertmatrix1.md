---
layout: default
title: "PMF_alertMatrix1 (0x304) — PMF ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "PMF ECU message: alert matrix1. Ethernet-side message PMF_alertMatrix1 of PMF ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 38 signals (PMF_a001_absoluteTorque, PMF_a002_excessiveAccelTorque, PMF_a003_excessiveReversalTorque, PMF_a004_excessiveDecelTorque and 34 more). Bit layout, scaling, units and value tables."
---

# PMF_alertMatrix1 (0x304) — PMF ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

PMF ECU message: alert matrix1. This page documents the 38 signals of PMF_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_alertMatrix1` |
| Ethernet-side id | 0x304 (772) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 38 |

## Signals of PMF_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `PMF_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_a001_absoluteTorque` | PMF ECU: a001 absolute torque | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a002_excessiveAccelTorque` | PMF ECU: a002 excessive accel torque | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a003_excessiveReversalTorque` | PMF ECU: a003 excessive reversal torque | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a004_excessiveDecelTorque` | PMF ECU: a004 excessive decel torque | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a005_torqueInNeutralOrPark` | PMF ECU: a005 torque in neutral or park | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a006_underTorqueCheck` | PMF ECU: a006 under torque check | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a008_memoryError` | PMF ECU: a008 memory error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_diMIA` | PMF ECU: a010 di MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a011_phaseCurrentIrrational` | PMF ECU: a011 phase current irrational | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a012_canDataBusA` | PMF ECU: a012 can data bus a | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a013_canHardwareBusA` | PMF ECU: a013 can hardware bus a | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a017_brakeMIA` | PMF ECU: a017 brake MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a018_encoderIrrational` | PMF ECU: a018 encoder irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a019_statorTempIrrational` | PMF ECU: a019 stator temp irrational | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_unintendedReset` | PMF ECU: a025 unintended reset | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_diHeartBeatMIA` | PMF ECU: a026 di heart beat MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a027_torqueEstimationOutOfBounds` | PMF ECU: a027 torque estimation out of bounds | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a028_torqueCmdError` | PMF ECU: a028 torque cmd error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a031_highStackUsage` | PMF ECU: a031 high stack usage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a032_registerConfigError` | PMF ECU: a032 register config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a033_selfTest` | PMF ECU: a033 self test | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a034_trqCrossCheck` | PMF ECU: a034 trq cross check | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a035_udsTransactionInitiated` | PMF ECU: a035 uds transaction initiated | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_preWatchdog` | PMF ECU: a036 pre watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a037_hvpMIA` | PMF ECU: a037 hvp MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a039_disMIA` | PMF ECU: a039 dis MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a040_pmMIA` | PMF ECU: a040 pm MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a042_gtwMIA` | PMF ECU: a042 gtw MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a045_motorMovementDetected` | PMF ECU: a045 motor movement detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_vcfrontMIA` | PMF ECU: a053 vcfront MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiMIA` | PMF ECU: a054 ui MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_resolver` | PMF ECU: a055 resolver | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a056_canHardwareBusB` | PMF ECU: a056 can hardware bus b | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a057_canDataBusB` | PMF ECU: a057 can data bus b | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a058_measuredHvilCurrentFrozen` | PMF ECU: a058 measured hvil current frozen | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a061_DIPMVersionMismatch` | PMF ECU: a061 DIPM version mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a062_eccError` | PMF ECU: a062 ecc error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a064_torqueIntervention` | PMF ECU: a064 torque intervention | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
