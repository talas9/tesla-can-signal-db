---
layout: default
title: "APP_warningMatrix1 (0x369) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix1. Tesla Model Y CAN bus message APP_warningMatrix1 (0x369) of Driver assistance computer (primary), firmware 2026.26.6.5, 42 signals (APP_w065_deserializerOvercurrent, APP_w066_deserializerLockLost, APP_w067_steeringAlignment, APP_w068_vlInconsistency and 38 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix1 (0x369) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: warning matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 42 signals of APP_warningMatrix1 as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix1` |
| CAN id | 0x369 (873) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 42 |

## Signals of APP_warningMatrix1

Tesla Model Y CAN bus signals in `APP_warningMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w065_deserializerOvercurrent` | Driver assistance computer (primary): w065 deserializer overcurrent | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w066_deserializerLockLost` | Driver assistance computer (primary): w066 deserializer lock lost | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w067_steeringAlignment` | Driver assistance computer (primary): w067 steering alignment | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w068_vlInconsistency` | Driver assistance computer (primary): w068 vl inconsistency | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w069_apcSpaceMasked` | Driver assistance computer (primary): w069 apc space masked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w070_apcIncompleteCal` | Driver assistance computer (primary): w070 apc incomplete cal | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w071_selfparkStarted` | Driver assistance computer (primary): w071 selfpark started | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w072_selfparkComplete` | Driver assistance computer (primary): w072 selfpark complete | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w073_issueEscalatedLDW` | Driver assistance computer (primary): w073 issue escalated LDW | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w074_inPathStationaryObst` | Driver assistance computer (primary): w074 in path stationary obst | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w075_scMia` | Driver assistance computer (primary): w075 sc mia | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w076_mobilEyeSetC` | Driver assistance computer (primary): w076 mobil eye set c | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w077_pmmActive` | Driver assistance computer (primary): w077 pmm active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w078_pmmActive2` | Driver assistance computer (primary): w078 pmm active2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w079_edrAvailable` | Driver assistance computer (primary): w079 edr available | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w080_accFailedActivation` | Driver assistance computer (primary): w080 acc failed activation | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w081_pmmActiveBraking` | Driver assistance computer (primary): w081 pmm active braking | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w082_inPathFSviolation` | Driver assistance computer (primary): w082 in path f sviolation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w083_inPathRADObject` | Driver assistance computer (primary): w083 in path RAD object | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w084_pmmIPSO` | Driver assistance computer (primary): w084 pmm IPSO | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w085_pmmSteering` | Driver assistance computer (primary): w085 pmm steering | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w086_robCollision` | Driver assistance computer (primary): w086 rob collision | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w087_DEPRECATED` | Driver assistance computer (primary): w087 DEPRECATED | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w088_DEPRECATED` | Driver assistance computer (primary): w088 DEPRECATED | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w089_DEPRECATED` | Driver assistance computer (primary): w089 DEPRECATED | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w090_DEPRECATED` | Driver assistance computer (primary): w090 DEPRECATED | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w091_DEPRECATED` | Driver assistance computer (primary): w091 DEPRECATED | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w092_DEPRECATED` | Driver assistance computer (primary): w092 DEPRECATED | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w093_DEPRECATED` | Driver assistance computer (primary): w093 DEPRECATED | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w094_DEPRECATED` | Driver assistance computer (primary): w094 DEPRECATED | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w095_DEPRECATED` | Driver assistance computer (primary): w095 DEPRECATED | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w096_DEPRECATED` | Driver assistance computer (primary): w096 DEPRECATED | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w097_DEPRECATED` | Driver assistance computer (primary): w097 DEPRECATED | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w098_DEPRECATED` | Driver assistance computer (primary): w098 DEPRECATED | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w099_DEPRECATED` | Driver assistance computer (primary): w099 DEPRECATED | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w100_DEPRECATED` | Driver assistance computer (primary): w100 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w101_DEPRECATED` | Driver assistance computer (primary): w101 DEPRECATED | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w102_DEPRECATED` | Driver assistance computer (primary): w102 DEPRECATED | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w103_robExperimentalAEB` | Driver assistance computer (primary): w103 rob experimental AEB | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w104_DEPRECATED` | Driver assistance computer (primary): w104 DEPRECATED | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w105_DEPRECATED` | Driver assistance computer (primary): w105 DEPRECATED | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w106_torsionBarOffset` | Driver assistance computer (primary): w106 torsion bar offset | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
