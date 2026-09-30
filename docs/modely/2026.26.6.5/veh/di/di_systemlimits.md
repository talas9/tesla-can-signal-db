---
layout: default
title: "DI_systemLimits (0x128) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: system limits. Tesla Model Y CAN bus message DI_systemLimits (0x128) of Drive inverter, firmware 2026.26.6.5, 23 signals (DI_limitRegenPower, DI_limitIBat, DI_limitVBatLow, DI_limitVBatHigh and 19 more). Bit layout, scaling, units and value tables."
---

# DI_systemLimits (0x128) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN

Drive inverter message: system limits; frame length from the layout, not yet observed on a vehicle bus. This page documents the 23 signals of DI_systemLimits as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_systemLimits` |
| CAN id | 0x128 (296) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 23 |

## Signals of DI_systemLimits

Tesla Model Y CAN bus signals in `DI_systemLimits`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_limitRegenPower` | TRUE when torque is limited due to regen power limit. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitIBat` | TRUE when torque is limited due to battery current. | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitVBatLow` | Drive inverter: limit v bat low | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitVBatHigh` | Drive inverter: limit v bat high | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitObstacleDetection` | TRUE when torque is limited due to obstacle detected in vehicle path. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitSystemLimp` | Drive inverter: limit system limp | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitSystemGPO` | Drive inverter: limit system GPO | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitShift` | Drive inverter: limit shift | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitDriveTorque` | TRUE when drive torque is limited due to driver torque limit command | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitRegenTorque` | TRUE when regen torque is limited due to driver torque limit command | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitVehicleSpeed` | Drive inverter: limit vehicle speed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitBmsMiaFreeze` | Drive inverter: limit bms mia freeze | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitSystemSpinDownLearning` | Drive inverter: limit system spin down learning | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitCdp` | Drive inverter: limit cdp | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_vehicleSpeedLimitType` | Speed limit source/type of DI_vehicleSpeedLimit. | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `USER`<br>2 = `POWERTRAIN` | validated |
| `DI_vehicleSpeedLimit` | Vehicle speed limit (including powertrain limits) being enforced by the DI and published to the UI; raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 1 | 0 | kph | 0 to 510 | 511 = `SNA` | validated |
| `DI_vehicleSpeedLimitReason` | Speed limit reason of DI_vehicleSpeedLimit. | 25\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `DRIVE_UNIT_LIMIT`<br>2 = `FACTORY_LOW_BRAKE_FLUID`<br>3 = `FACTORY_MODE`<br>4 = `SERVICE_MODE`<br>5 = `MAX_CAR_CONFIG`<br>6 = `TRAILER_MODE`<br>7 = `TAS`<br>8 = `DAS_PEDAL_CONTROL`<br>9 = `FRUNK_OPEN`<br>10 = `USER`<br>11 = `MAX_TIRE_TYPE`<br>12 = `LV_DEGRADED`<br>13 = `SLIP_START_LIMIT`<br>14 = `TAS_OFFROAD`<br>15 = `FACTORY_BRAKE_BURNISHING`<br>16 = `MANUAL_RECOVERY_MODE` | validated |
| `DI_proximity` | TRUE if the proximity hardware input signal is active. | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_limitClosureNotClosed` | Drive inverter: limit closure not closed | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_undersideAbuse` | Drive inverter: underside abuse | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_immobilizerAuthLevel` | Immobilizer Authentication Level | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IMMOBILIZER_AUTH_LEVEL_NONE`<br>1 = `IMMOBILIZER_AUTH_LEVEL_USER_DRIVE`<br>2 = `IMMOBILIZER_AUTH_LEVEL_AUTONOMY`<br>3 = `IMMOBILIZER_AUTH_LEVEL_MANUAL_RECOVERY` | validated |
| `DI_manualRecoveryDistanceRemaining` | Drive inverter: manual recovery distance remaining; raw 127 = signal not available (SNA) | 40\|7 | little-endian | unsigned | 5 | 0 | m | 0 to 500 | 127 = `SNA` | validated |
| `DI_restrictedDrivingMode` | Drive inverter: restricted driving mode | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RESTRICTED_DRIVING_MODE_NONE`<br>1 = `RESTRICTED_DRIVING_MANUAL_RECOVERY` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
