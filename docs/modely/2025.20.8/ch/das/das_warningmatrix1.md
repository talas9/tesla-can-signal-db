---
layout: default
title: "DAS_warningMatrix1 (0x36A) — Driver assistance computer, Tesla Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer message: warning matrix1. Tesla Model Y CAN bus message DAS_warningMatrix1 (0x36A) of Driver assistance computer, firmware 2025.20.8, 42 signals (DAS_w065_deserializerOvercurrent, DAS_w066_deserializerLockLost, DAS_w067_steeringAlignment, DAS_w068_vlInconsistency and 38 more). Bit layout, scaling, units and value tables."
---

# DAS_warningMatrix1 (0x36A) — Driver assistance computer, Tesla Model Y 2025.20.8 CH CAN

Driver assistance computer message: warning matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 42 signals of DAS_warningMatrix1 as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_warningMatrix1` |
| CAN id | 0x36A (874) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 42 |

## Signals of DAS_warningMatrix1

Tesla Model Y CAN bus signals in `DAS_warningMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_w065_deserializerOvercurrent` | Driver assistance computer: w065 deserializer overcurrent | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w066_deserializerLockLost` | Driver assistance computer: w066 deserializer lock lost | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w067_steeringAlignment` | Driver assistance computer: w067 steering alignment | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w068_vlInconsistency` | Driver assistance computer: w068 vl inconsistency | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w069_apcSpaceMasked` | Driver assistance computer: w069 apc space masked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w070_apcIncompleteCal` | Driver assistance computer: w070 apc incomplete cal | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w071_selfparkStarted` | Driver assistance computer: w071 selfpark started | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w072_selfparkComplete` | Driver assistance computer: w072 selfpark complete | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w073_issueEscalatedLDW` | Driver assistance computer: w073 issue escalated LDW | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w074_inPathStationaryObst` | Driver assistance computer: w074 in path stationary obst | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w075_scMia` | Driver assistance computer: w075 sc mia | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w076_mobilEyeSetC` | Driver assistance computer: w076 mobil eye set c | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w077_pmmActive` | Driver assistance computer: w077 pmm active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w078_pmmActive2` | Driver assistance computer: w078 pmm active2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w079_edrAvailable` | Driver assistance computer: w079 edr available | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w080_accFailedActivation` | Driver assistance computer: w080 acc failed activation | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w081_pmmActiveBraking` | Driver assistance computer: w081 pmm active braking | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w082_inPathFSviolation` | Driver assistance computer: w082 in path f sviolation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w083_inPathRADObject` | Driver assistance computer: w083 in path RAD object | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w084_pmmIPSO` | Driver assistance computer: w084 pmm IPSO | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w085_pmmSteering` | Driver assistance computer: w085 pmm steering | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w086_robCollision` | Driver assistance computer: w086 rob collision | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w087_DEPRECATED` | Driver assistance computer: w087 DEPRECATED | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w088_DEPRECATED` | Driver assistance computer: w088 DEPRECATED | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w089_DEPRECATED` | Driver assistance computer: w089 DEPRECATED | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w090_DEPRECATED` | Driver assistance computer: w090 DEPRECATED | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w091_DEPRECATED` | Driver assistance computer: w091 DEPRECATED | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w092_DEPRECATED` | Driver assistance computer: w092 DEPRECATED | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w093_DEPRECATED` | Driver assistance computer: w093 DEPRECATED | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w094_DEPRECATED` | Driver assistance computer: w094 DEPRECATED | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w095_DEPRECATED` | Driver assistance computer: w095 DEPRECATED | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w096_DEPRECATED` | Driver assistance computer: w096 DEPRECATED | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w097_DEPRECATED` | Driver assistance computer: w097 DEPRECATED | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w098_DEPRECATED` | Driver assistance computer: w098 DEPRECATED | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w099_DEPRECATED` | Driver assistance computer: w099 DEPRECATED | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w100_DEPRECATED` | Driver assistance computer: w100 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w101_DEPRECATED` | Driver assistance computer: w101 DEPRECATED | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w102_DEPRECATED` | Driver assistance computer: w102 DEPRECATED | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w103_robExperimentalAEB` | Driver assistance computer: w103 rob experimental AEB | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w104_DEPRECATED` | Driver assistance computer: w104 DEPRECATED | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w105_DEPRECATED` | Driver assistance computer: w105 DEPRECATED | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w106_torsionBarCalibrated` | Driver assistance computer: w106 torsion bar calibrated | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
