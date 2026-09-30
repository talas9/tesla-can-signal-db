---
layout: default
title: "PMR_alertMatrix1 (0x386) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "PMR ECU message: alert matrix1. Ethernet-side message PMR_alertMatrix1 of PMR ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 38 signals (PMR_a001_absoluteTorque, PMR_a002_excessiveAccelTorque, PMR_a003_excessiveReversalTorque, PMR_a004_excessiveDecelTorque and 34 more). Bit layout, scaling, units and value tables."
---

# PMR_alertMatrix1 (0x386) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

PMR ECU message: alert matrix1. This page documents the 38 signals of PMR_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_alertMatrix1` |
| Ethernet-side id | 0x386 (902) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 38 |

## Signals of PMR_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `PMR_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_a001_absoluteTorque` | PMR ECU: a001 absolute torque | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a002_excessiveAccelTorque` | PMR ECU: a002 excessive accel torque | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a003_excessiveReversalTorque` | PMR ECU: a003 excessive reversal torque | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a004_excessiveDecelTorque` | PMR ECU: a004 excessive decel torque | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a005_torqueInNeutralOrPark` | PMR ECU: a005 torque in neutral or park | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a006_underTorqueCheck` | PMR ECU: a006 under torque check | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a008_memoryError` | PMR ECU: a008 memory error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a010_diMIA` | PMR ECU: a010 di MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a011_phaseCurrentIrrational` | PMR ECU: a011 phase current irrational | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a012_canDataBusA` | PMR ECU: a012 can data bus a | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a013_canHardwareBusA` | PMR ECU: a013 can hardware bus a | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a017_brakeMIA` | PMR ECU: a017 brake MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a018_encoderIrrational` | PMR ECU: a018 encoder irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a019_statorTempIrrational` | PMR ECU: a019 stator temp irrational | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a025_unintendedReset` | PMR ECU: a025 unintended reset | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a026_diHeartBeatMIA` | PMR ECU: a026 di heart beat MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a027_torqueEstimationOutOfBounds` | PMR ECU: a027 torque estimation out of bounds | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a028_torqueCmdError` | PMR ECU: a028 torque cmd error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a031_highStackUsage` | PMR ECU: a031 high stack usage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a032_registerConfigError` | PMR ECU: a032 register config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a033_selfTest` | PMR ECU: a033 self test | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a034_trqCrossCheck` | PMR ECU: a034 trq cross check | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a035_udsTransactionInitiated` | PMR ECU: a035 uds transaction initiated | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a036_preWatchdog` | PMR ECU: a036 pre watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a037_hvpMIA` | PMR ECU: a037 hvp MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a039_disMIA` | PMR ECU: a039 dis MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a040_pmMIA` | PMR ECU: a040 pm MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a042_gtwMIA` | PMR ECU: a042 gtw MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a045_motorMovementDetected` | PMR ECU: a045 motor movement detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a053_vcfrontMIA` | PMR ECU: a053 vcfront MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a054_uiMIA` | PMR ECU: a054 ui MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a055_resolver` | PMR ECU: a055 resolver | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a056_canHardwareBusB` | PMR ECU: a056 can hardware bus b | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a057_canDataBusB` | PMR ECU: a057 can data bus b | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a058_measuredHvilCurrentFrozen` | PMR ECU: a058 measured hvil current frozen | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a061_DIPMVersionMismatch` | PMR ECU: a061 DIPM version mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a062_eccError` | PMR ECU: a062 ecc error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a064_torqueIntervention` | PMR ECU: a064 torque intervention | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
