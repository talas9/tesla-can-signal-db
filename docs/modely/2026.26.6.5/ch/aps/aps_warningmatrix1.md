---
layout: default
title: "APS_warningMatrix1 (0x36C) — Driver assistance computer (secondary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: warning matrix1. Tesla Model Y CAN bus message APS_warningMatrix1 (0x36C) of Driver assistance computer (secondary), firmware 2026.26.6.5, 42 signals (APS_w065_deserializerOvercurrent, APS_w066_deserializerLockLost, APS_w067_steeringAlignment, APS_w068_vlInconsistency and 38 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix1 (0x36C) — Driver assistance computer (secondary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: warning matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 42 signals of APS_warningMatrix1 as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix1` |
| CAN id | 0x36C (876) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 42 |

## Signals of APS_warningMatrix1

Tesla Model Y CAN bus signals in `APS_warningMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_w065_deserializerOvercurrent` | Driver assistance computer (secondary): w065 deserializer overcurrent | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w066_deserializerLockLost` | Driver assistance computer (secondary): w066 deserializer lock lost | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w067_steeringAlignment` | Driver assistance computer (secondary): w067 steering alignment | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w068_vlInconsistency` | Driver assistance computer (secondary): w068 vl inconsistency | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w069_apcSpaceMasked` | Driver assistance computer (secondary): w069 apc space masked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w070_apcIncompleteCal` | Driver assistance computer (secondary): w070 apc incomplete cal | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w071_selfparkStarted` | Driver assistance computer (secondary): w071 selfpark started | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w072_selfparkComplete` | Driver assistance computer (secondary): w072 selfpark complete | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w073_issueEscalatedLDW` | Driver assistance computer (secondary): w073 issue escalated LDW | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w074_inPathStationaryObst` | Driver assistance computer (secondary): w074 in path stationary obst | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w075_scMia` | Driver assistance computer (secondary): w075 sc mia | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w076_mobilEyeSetC` | Driver assistance computer (secondary): w076 mobil eye set c | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w077_pmmActive` | Driver assistance computer (secondary): w077 pmm active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w078_pmmActive2` | Driver assistance computer (secondary): w078 pmm active2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w079_edrAvailable` | Driver assistance computer (secondary): w079 edr available | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w080_accFailedActivation` | Driver assistance computer (secondary): w080 acc failed activation | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w081_pmmActiveBraking` | Driver assistance computer (secondary): w081 pmm active braking | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w082_inPathFSviolation` | Driver assistance computer (secondary): w082 in path f sviolation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w083_inPathRADObject` | Driver assistance computer (secondary): w083 in path RAD object | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w084_pmmIPSO` | Driver assistance computer (secondary): w084 pmm IPSO | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w085_pmmSteering` | Driver assistance computer (secondary): w085 pmm steering | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w086_robCollision` | Driver assistance computer (secondary): w086 rob collision | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w087_DEPRECATED` | Driver assistance computer (secondary): w087 DEPRECATED | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w088_DEPRECATED` | Driver assistance computer (secondary): w088 DEPRECATED | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w089_DEPRECATED` | Driver assistance computer (secondary): w089 DEPRECATED | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w090_DEPRECATED` | Driver assistance computer (secondary): w090 DEPRECATED | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w091_DEPRECATED` | Driver assistance computer (secondary): w091 DEPRECATED | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w092_DEPRECATED` | Driver assistance computer (secondary): w092 DEPRECATED | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w093_DEPRECATED` | Driver assistance computer (secondary): w093 DEPRECATED | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w094_DEPRECATED` | Driver assistance computer (secondary): w094 DEPRECATED | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w095_DEPRECATED` | Driver assistance computer (secondary): w095 DEPRECATED | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w096_DEPRECATED` | Driver assistance computer (secondary): w096 DEPRECATED | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w097_DEPRECATED` | Driver assistance computer (secondary): w097 DEPRECATED | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w098_DEPRECATED` | Driver assistance computer (secondary): w098 DEPRECATED | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w099_DEPRECATED` | Driver assistance computer (secondary): w099 DEPRECATED | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w100_DEPRECATED` | Driver assistance computer (secondary): w100 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w101_DEPRECATED` | Driver assistance computer (secondary): w101 DEPRECATED | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w102_DEPRECATED` | Driver assistance computer (secondary): w102 DEPRECATED | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w103_robExperimentalAEB` | Driver assistance computer (secondary): w103 rob experimental AEB | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w104_DEPRECATED` | Driver assistance computer (secondary): w104 DEPRECATED | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w105_DEPRECATED` | Driver assistance computer (secondary): w105 DEPRECATED | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w106_torsionBarOffset` | Driver assistance computer (secondary): w106 torsion bar offset | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
