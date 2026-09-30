---
layout: default
title: "DI_chassisControl2 (0x745) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Drive inverter message: chassis control2. Ethernet-side message DI_chassisControl2 of Drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 22 signals (DI_gradeAngle, DI_bankAngle, DI_chassisControlVideoRequest, DI_tireUtilizationRatioFrL and 18 more). Bit layout, scaling, units and value tables."
---

# DI_chassisControl2 (0x745) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Drive inverter message: chassis control2. This page documents the 22 signals of DI_chassisControl2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_chassisControl2` |
| Ethernet-side id | 0x745 (1861) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 22 |

## Signals of DI_chassisControl2

Tesla Model 3 / Model Y CAN bus signals in `DI_chassisControl2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_gradeAngle` | Reports the grade angle. | 0\|6 | little-endian | signed | 0.01 | 0 | rad | -0.3125 to 0.31 |  | validated |
| `DI_bankAngle` | Reports the bank angle. | 6\|6 | little-endian | signed | 0.01 | 0 | rad | -0.3125 to 0.31 |  | validated |
| `DI_chassisControlVideoRequest` | Drive inverter: chassis control video request | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CHASSIS_CONTROL_EVENT_NONE`<br>1 = `CHASSIS_CONTROL_EVENT_1`<br>2 = `CHASSIS_CONTROL_EVENT_2`<br>3 = `CHASSIS_CONTROL_EVENT_3`<br>4 = `CHASSIS_CONTROL_EVENT_4`<br>5 = `CHASSIS_CONTROL_EVENT_5`<br>6 = `CHASSIS_CONTROL_EVENT_6`<br>7 = `CHASSIS_CONTROL_EVENT_7`<br>8 = `CHASSIS_CONTROL_EVENT_8`<br>9 = `CHASSIS_CONTROL_EVENT_9`<br>10 = `CHASSIS_CONTROL_EVENT_10`<br>11 = `CHASSIS_CONTROL_EVENT_11`<br>12 = `CHASSIS_CONTROL_EVENT_12`<br>13 = `CHASSIS_CONTROL_EVENT_13`<br>14 = `CHASSIS_CONTROL_EVENT_14`<br>15 = `CHASSIS_CONTROL_EVENT_15` | validated |
| `DI_tireUtilizationRatioFrL` | Drive inverter: tire utilization ratio fr l | 17\|5 | little-endian | unsigned | 0.0625 | 0 | - | 0 to 1.9375 |  | validated |
| `DI_tireUtilizationRatioFrR` | Drive inverter: tire utilization ratio fr r | 22\|5 | little-endian | unsigned | 0.0625 | 0 | - | 0 to 1.9375 |  | validated |
| `DI_tireUtilizationRatioReL` | Drive inverter: tire utilization ratio re l | 27\|5 | little-endian | unsigned | 0.0625 | 0 | - | 0 to 1.9375 |  | validated |
| `DI_tireUtilizationRatioReR` | Drive inverter: tire utilization ratio re r | 32\|5 | little-endian | unsigned | 0.0625 | 0 | - | 0 to 1.9375 |  | validated |
| `DI_counterSteerTarget` | Drive inverter: counter steer target | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INACTIVE`<br>1 = `ACTIVE`<br>2 = `EXPIRED` | validated |
| `DI_splitMuProbability` | Drive inverter: split mu probability | 39\|2 | little-endian | unsigned | 0.334 | 0 | - | 0 to 1 |  | validated |
| `DI_mzError` | Drive inverter: mz error | 41\|2 | little-endian | unsigned | 1667 | 0 | Nm | 0 to 5000 |  | validated |
| `DI_slipDifferenceFrontRear` | Drive inverter: slip difference front rear | 43\|3 | little-endian | signed | 0.133 | 0 | rad | -0.52 to 0.399 |  | validated |
| `DI_highFreqYawRate` | Drive inverter: high freq yaw rate | 46\|2 | little-endian | unsigned | 0.334 | 0 | - | 0 to 1 |  | validated |
| `DI_turnDirection` | Drive inverter: turn direction | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VDC_TURNING_RIGHT`<br>1 = `VDC_TURNING_LEFT` | validated |
| `DI_absolutePreControlRequest` | Drive inverter: absolute pre control request | 49\|2 | little-endian | unsigned | 5000 | 0 | Nm | 0 to 15000 |  | validated |
| `DI_oppositeBuildDirFrontAxle` | Drive inverter: opposite build dir front axle | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DI_oppositeBuildDirRearAxle` | Drive inverter: opposite build dir rear axle | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DI_saturatedEffectiveness` | Drive inverter: saturated effectiveness | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DI_driverPanicIndex` | Drive inverter: driver panic index | 54\|2 | little-endian | unsigned | 0.334 | 0 | - | 0 to 1 |  | validated |
| `DI_learnDownMu` | Drive inverter: learn down mu | 56\|2 | little-endian | unsigned | 0.334 | 0 | mu | 0 to 1 |  | validated |
| `DI_preControlOpposingTurnDir` | Drive inverter: pre control opposing turn dir | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `DI_driverFxError` | Drive inverter: driver fx error | 59\|2 | little-endian | unsigned | 1000 | 0 | N | 0 to 3000 |  | validated |
| `DI_targetSaturation` | Drive inverter: target saturation | 61\|3 | little-endian | unsigned | 0.572 | 0 | G | 0 to 4 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
