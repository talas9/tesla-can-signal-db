---
layout: default
title: "APP_warningMatrix7 (0x4D1) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix7. Tesla Model Y CAN bus message APP_warningMatrix7 (0x4D1) of Driver assistance computer (primary), firmware 2026.26.6.5, 23 signals (APP_w449_rightRepeaterImagerConfigMismatch, APP_w450_backupImagerConfigMismatch, APP_w451_fasciaImagerConfigMismatch, APP_w452_selfieImagerConfigMismatch and 19 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix7 (0x4D1) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: warning matrix7; frame length from the layout, not yet observed on a vehicle bus. This page documents the 23 signals of APP_warningMatrix7 as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix7` |
| CAN id | 0x4D1 (1233) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 23 |

## Signals of APP_warningMatrix7

Tesla Model Y CAN bus signals in `APP_warningMatrix7`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w449_rightRepeaterImagerConfigMismatch` | Driver assistance computer (primary): w449 right repeater imager config mismatch | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w450_backupImagerConfigMismatch` | Driver assistance computer (primary): w450 backup imager config mismatch | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w451_fasciaImagerConfigMismatch` | Driver assistance computer (primary): w451 fascia imager config mismatch | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w452_selfieImagerConfigMismatch` | Driver assistance computer (primary): w452 selfie imager config mismatch | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w453_driverCancelBlinker` | Driver assistance computer (primary): w453 driver cancel blinker | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w454_appAutonomySystemUnhealthy` | Driver assistance computer (primary): w454 app autonomy system unhealthy | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w455_apbAutonomySystemUnhealthy` | Driver assistance computer (primary): w455 apb autonomy system unhealthy | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w456_autonomyUnavailableCollision` | Driver assistance computer (primary): w456 autonomy unavailable collision | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w457_autonomyDegradedCollision` | Driver assistance computer (primary): w457 autonomy degraded collision | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w458_aceEvent` | Driver assistance computer (primary): w458 ace event | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w459_epbrMiaPartyBus` | Driver assistance computer (primary): w459 epbr mia party bus | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w460_epblMiaChBus` | Driver assistance computer (primary): w460 epbl mia ch bus | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w461_autonomyReroute` | Driver assistance computer (primary): w461 autonomy reroute | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w462_selfDrivingUnavailable` | Driver assistance computer (primary): w462 self driving unavailable | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w463_selfDrivingCamObstrcted` | Driver assistance computer (primary): w463 self driving cam obstrcted | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w464_autonomyUnavailableODD` | Driver assistance computer (primary): w464 autonomy unavailable ODD | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w465_autonomyDegradedODD` | Driver assistance computer (primary): w465 autonomy degraded ODD | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w466_missingSensorOTP` | Driver assistance computer (primary): w466 missing sensor OTP | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w467_imuDegraded` | Driver assistance computer (primary): w467 imu degraded | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w477_driverSeatReclined` | Driver assistance computer (primary): w477 driver seat reclined | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w478_runModeSwitch` | Driver assistance computer (primary): w478 run mode switch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w482_appVisionFailoverActivated` | Driver assistance computer (primary): w482 app vision failover activated | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w483_apbVisionFailoverActivated` | Driver assistance computer (primary): w483 apb vision failover activated | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
