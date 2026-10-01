---
layout: default
title: "DI_systemLimits (0x128) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: system limits. Ethernet-side message DI_systemLimits of Drive inverter for Tesla Model 3 firmware 2025.20.8, 20 signals (DI_limitRegenPower, DI_limitIBat, DI_limitVBatLow, DI_limitVBatHigh and 16 more). Bit layout, scaling, units and value tables."
---

# DI_systemLimits (0x128) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: system limits. This page documents the 20 signals of DI_systemLimits as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_systemLimits` |
| Ethernet-side id | 0x128 (296) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 20 |

## Signals of DI_systemLimits

Tesla Model 3 CAN bus signals in `DI_systemLimits`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_limitRegenPower` | TRUE when torque is limited due to regen power limit. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_limitIBat` | TRUE when torque is limited due to battery current. | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_limitVBatLow` | Drive inverter: limit v bat low | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitVBatHigh` | Drive inverter: limit v bat high | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitObstacleDetection` | TRUE when torque is limited due to obstacle detected in vehicle path. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_limitSystemLimp` | Drive inverter: limit system limp | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitSystemGPO` | Drive inverter: limit system GPO | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitShift` | Drive inverter: limit shift | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitDriveTorque` | TRUE when drive torque is limited due to driver torque limit command | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_limitRegenTorque` | TRUE when regen torque is limited due to driver torque limit command | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_limitVehicleSpeed` | Drive inverter: limit vehicle speed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitBmsMiaFreeze` | Drive inverter: limit bms mia freeze | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitSystemSpinDownLearning` | Drive inverter: limit system spin down learning | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_limitCdp` | Drive inverter: limit cdp | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_vehicleSpeedLimitType` | Speed limit source/type of DI_vehicleSpeedLimit. | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `USER`<br>2 = `POWERTRAIN` | plausible |
| `DI_vehicleSpeedLimit` | Vehicle speed limit (including powertrain limits) being enforced by the DI and published to the UI; raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 1 | 0 | kph | 0 to 510 | 511 = `SNA` | plausible |
| `DI_vehicleSpeedLimitReason` | Speed limit reason of DI_vehicleSpeedLimit. | 25\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `DRIVE_UNIT_LIMIT`<br>2 = `FACTORY_LOW_BRAKE_FLUID`<br>3 = `FACTORY_MODE`<br>4 = `SERVICE_MODE`<br>5 = `MAX_CAR_CONFIG`<br>6 = `TRAILER_MODE`<br>7 = `TAS`<br>8 = `DAS_PEDAL_CONTROL`<br>9 = `FRUNK_OPEN`<br>10 = `USER`<br>11 = `MAX_TIRE_TYPE`<br>12 = `LV_DEGRADED`<br>13 = `SLIP_START_LIMIT`<br>14 = `TAS_OFFROAD`<br>15 = `FACTORY_BRAKE_BURNISHING` | plausible |
| `DI_limitClosureNotClosed` | Drive inverter: limit closure not closed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_proximity` | TRUE if the proximity hardware input signal is active. | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_undersideAbuse` | Drive inverter: underside abuse | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
