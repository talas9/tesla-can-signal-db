---
layout: default
title: "APSB_warningMatrix1 (0x477) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: warning matrix1. Ethernet-side message APSB_warningMatrix1 of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 42 signals (APSB_w065_deserializerOvercurrent, APSB_w066_deserializerLockLost, APSB_w067_steeringAlignment, APSB_w068_vlInconsistency and 38 more). Bit layout, scaling, units and value tables."
---

# APSB_warningMatrix1 (0x477) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: warning matrix1. This page documents the 42 signals of APSB_warningMatrix1 as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_warningMatrix1` |
| Ethernet-side id | 0x477 (1143) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 42 |

## Signals of APSB_warningMatrix1

Tesla Model Y CAN bus signals in `APSB_warningMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_w065_deserializerOvercurrent` | APSB ECU: w065 deserializer overcurrent | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w066_deserializerLockLost` | APSB ECU: w066 deserializer lock lost | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w067_steeringAlignment` | APSB ECU: w067 steering alignment | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w068_vlInconsistency` | APSB ECU: w068 vl inconsistency | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w069_apcSpaceMasked` | APSB ECU: w069 apc space masked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w070_apcIncompleteCal` | APSB ECU: w070 apc incomplete cal | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w071_selfparkStarted` | APSB ECU: w071 selfpark started | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w072_selfparkComplete` | APSB ECU: w072 selfpark complete | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w073_issueEscalatedLDW` | APSB ECU: w073 issue escalated LDW | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w074_inPathStationaryObst` | APSB ECU: w074 in path stationary obst | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w075_scMia` | APSB ECU: w075 sc mia | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w076_mobilEyeSetC` | APSB ECU: w076 mobil eye set c | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w077_pmmActive` | APSB ECU: w077 pmm active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w078_pmmActive2` | APSB ECU: w078 pmm active2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w079_edrAvailable` | APSB ECU: w079 edr available | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w080_accFailedActivation` | APSB ECU: w080 acc failed activation | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w081_pmmActiveBraking` | APSB ECU: w081 pmm active braking | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w082_inPathFSviolation` | APSB ECU: w082 in path f sviolation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w083_inPathRADObject` | APSB ECU: w083 in path RAD object | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w084_pmmIPSO` | APSB ECU: w084 pmm IPSO | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w085_pmmSteering` | APSB ECU: w085 pmm steering | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w086_robCollision` | APSB ECU: w086 rob collision | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w087_DEPRECATED` | APSB ECU: w087 DEPRECATED | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w088_DEPRECATED` | APSB ECU: w088 DEPRECATED | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w089_DEPRECATED` | APSB ECU: w089 DEPRECATED | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w090_DEPRECATED` | APSB ECU: w090 DEPRECATED | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w091_DEPRECATED` | APSB ECU: w091 DEPRECATED | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w092_DEPRECATED` | APSB ECU: w092 DEPRECATED | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w093_DEPRECATED` | APSB ECU: w093 DEPRECATED | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w094_DEPRECATED` | APSB ECU: w094 DEPRECATED | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w095_DEPRECATED` | APSB ECU: w095 DEPRECATED | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w096_DEPRECATED` | APSB ECU: w096 DEPRECATED | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w097_DEPRECATED` | APSB ECU: w097 DEPRECATED | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w098_DEPRECATED` | APSB ECU: w098 DEPRECATED | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w099_DEPRECATED` | APSB ECU: w099 DEPRECATED | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w100_DEPRECATED` | APSB ECU: w100 DEPRECATED | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w101_DEPRECATED` | APSB ECU: w101 DEPRECATED | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w102_DEPRECATED` | APSB ECU: w102 DEPRECATED | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w103_robExperimentalAEB` | APSB ECU: w103 rob experimental AEB | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w104_DEPRECATED` | APSB ECU: w104 DEPRECATED | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w105_DEPRECATED` | APSB ECU: w105 DEPRECATED | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w106_torsionBarOffset` | APSB ECU: w106 torsion bar offset | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
