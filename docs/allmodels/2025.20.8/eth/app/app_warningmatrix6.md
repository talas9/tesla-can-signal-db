---
layout: default
title: "APP_warningMatrix6 (0x47D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: warning matrix6. Ethernet-side message APP_warningMatrix6 of Driver assistance computer (primary) for Tesla Model 3 / Model Y firmware 2025.20.8, 18 signals (APP_w385_posEngineUnhealthy, APP_w386_radarOnlyBrakingEvent, APP_w387_radarBlockageDetected, APP_w388_windshieldCameraHeaterFaulted and 14 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix6 (0x47D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: warning matrix6. This page documents the 18 signals of APP_warningMatrix6 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix6` |
| Ethernet-side id | 0x47D (1149) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of APP_warningMatrix6

Tesla Model 3 / Model Y CAN bus signals in `APP_warningMatrix6`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w385_posEngineUnhealthy` | Driver assistance computer (primary): w385 pos engine unhealthy | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w386_radarOnlyBrakingEvent` | Driver assistance computer (primary): w386 radar only braking event | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w387_radarBlockageDetected` | Driver assistance computer (primary): w387 radar blockage detected | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w388_windshieldCameraHeaterFaulted` | Driver assistance computer (primary): w388 windshield camera heater faulted | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w389_camFovResidueDetected` | Driver assistance computer (primary): w389 cam fov residue detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w390_cabinCamVisDegraded` | Driver assistance computer (primary): w390 cabin cam vis degraded | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w391_cabinCameraBlockedonAP` | Driver assistance computer (primary): w391 cabin camera blockedon AP | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w392_fsdSuspended` | Driver assistance computer (primary): w392 fsd suspended | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w393_attnMntrUnavailable` | Driver assistance computer (primary): w393 attn mntr unavailable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w394_apImuGrossErrors` | Driver assistance computer (primary): w394 ap imu gross errors | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w395_cabinCameraLEDFaultSvc` | Driver assistance computer (primary): w395 cabin camera LED fault svc | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w396_severeResidueDetected` | Driver assistance computer (primary): w396 severe residue detected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w397_apFeatDisabledPermanent` | Driver assistance computer (primary): w397 ap feat disabled permanent | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w398_imuOutputUnhealthy` | Driver assistance computer (primary): w398 imu output unhealthy | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w399_brakeboosterMia` | Driver assistance computer (primary): w399 brakebooster mia | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w400_selfieCameraFanFault` | Driver assistance computer (primary): w400 selfie camera fan fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w401_leftPillarCameraHeaterFaulted` | Driver assistance computer (primary): w401 left pillar camera heater faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w402_rightPillarCameraHeaterFaulted` | Driver assistance computer (primary): w402 right pillar camera heater faulted | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
