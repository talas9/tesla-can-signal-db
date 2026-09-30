---
layout: default
title: "DI_alertMatrix4 (0x36E) — Drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Drive inverter message: alert matrix4. Ethernet-side message DI_alertMatrix4 of Drive inverter for Tesla Model Y firmware 2025.20.8, 57 signals (DI_a193_vdcBrakeTorqueFr, DI_a194_vdcBrakeTorqueRe, DI_a195_vdcEspSlipFr, DI_a196_vdcEspSlipRe and 53 more). Bit layout, scaling, units and value tables."
---

# DI_alertMatrix4 (0x36E) — Drive inverter, Tesla Model Y 2025.20.8 ETH

Drive inverter message: alert matrix4. This page documents the 57 signals of DI_alertMatrix4 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_alertMatrix4` |
| Ethernet-side id | 0x36E (878) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 57 |

## Signals of DI_alertMatrix4

Tesla Model Y CAN bus signals in `DI_alertMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_a193_vdcBrakeTorqueFr` | Drive inverter: a193 vdc brake torque fr | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a194_vdcBrakeTorqueRe` | Drive inverter: a194 vdc brake torque re | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a195_vdcEspSlipFr` | Drive inverter: a195 vdc esp slip fr | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a196_vdcEspSlipRe` | Drive inverter: a196 vdc esp slip re | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a197_vdcEspWheelSaturations` | Drive inverter: a197 vdc esp wheel saturations | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a198_vdcEspMCPressAndSteering` | Drive inverter: a198 vdc esp MC press and steering | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a199_vdcFaulted` | Drive inverter: a199 vdc faulted | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a200_vdcModelBasedPlausibility` | Drive inverter: a200 vdc model based plausibility | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a201_decelTorqueLimited` | Drive inverter: a201 decel torque limited | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a202_excessHeatUnavailable` | Drive inverter: a202 excess heat unavailable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a203_TCReducedByADD` | Drive inverter: a203 TC reduced by ADD | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a204_vdcRcmLongitudinal` | Drive inverter: a204 vdc rcm longitudinal | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a205_vdcRcmLateral` | Drive inverter: a205 vdc rcm lateral | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a206_vdcRcmVertical` | Drive inverter: a206 vdc rcm vertical | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a207_vdcPowertrainTorque_dif` | Drive inverter: a207 vdc powertrain torque dif | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a208_vdcPowertrainTorque_dir` | Drive inverter: a208 vdc powertrain torque dir | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a210_vdcOtherControllerStates` | Drive inverter: a210 vdc other controller states | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a211_vdcMotorSpeed_dif` | Drive inverter: a211 vdc motor speed dif | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a212_vdcWheelRotations` | Drive inverter: a212 vdc wheel rotations | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a213_lowMuProbabilityChange` | Drive inverter: a213 low mu probability change | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a214_vdcWheelSpeedFr` | Drive inverter: a214 vdc wheel speed fr | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a215_vdcWheelSpeedRe` | Drive inverter: a215 vdc wheel speed re | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a216_vdcMBPAlmostTripped` | Drive inverter: a216 vdc MBP almost tripped | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a217_vdcOutputIrrational` | Drive inverter: a217 vdc output irrational | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a218_vdcOSPreControlActive` | Drive inverter: a218 vdc OS pre control active | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a219_vdcOversteerdMzActive` | Drive inverter: a219 vdc oversteerd mz active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a220_vdcUndersteerDecelActive` | Drive inverter: a220 vdc understeer decel active | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a221_vdcUndersteerdMzActive` | Drive inverter: a221 vdc understeerd mz active | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a222_vdcDisabled` | Drive inverter: a222 vdc disabled | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a223_tractionControlDisabled` | Drive inverter: a223 traction control disabled | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a224_brakeOverTemp` | Drive inverter: a224 brake over temp | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a225_vyEstimatorDegradedDebug` | Drive inverter: a225 vy estimator degraded debug | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a226_sysStartConditionNotMet` | Drive inverter: a226 sys start condition not met | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a227_contactorsNotClosed` | Drive inverter: a227 contactors not closed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a228_brakeTempEstUnavailable` | Drive inverter: a228 brake temp est unavailable | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a230_cmpMIA` | Drive inverter: a230 cmp MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a231_unintendedReset2` | Drive inverter: a231 unintended reset2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a232_velocityEstimatorDegraded` | Drive inverter: a232 velocity estimator degraded | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a233_frontWheelImpactDetected` | Drive inverter: a233 front wheel impact detected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a235_trackModeActive` | Drive inverter: a235 track mode active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a236_tasMIA` | Drive inverter: a236 tas MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a237_undersideAbuse` | Drive inverter: a237 underside abuse | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a238_secondaryCollisionMitigationActive` | Drive inverter: a238 secondary collision mitigation active | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a239_neutralRequestByPM` | Drive inverter: a239 neutral request by PM | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a240_torqueSplitStuck` | Drive inverter: a240 torque split stuck | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a241_vdcMotorSpeed_dir` | Drive inverter: a241 vdc motor speed dir | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a242_vdcTrailerSwayDetected` | Drive inverter: a242 vdc trailer sway detected | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a243_rcuMIA` | Drive inverter: a243 rcu MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a244_vseRLSMassMismatch` | Drive inverter: a244 vse RLS mass mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a245_opdReducedWithoutEbr` | Drive inverter: a245 opd reduced without ebr | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a246_opdUnavailable` | Drive inverter: a246 opd unavailable | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a248_vdcPreControlHighDynamicActive` | Drive inverter: a248 vdc pre control high dynamic active | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a249_spinDownLearningInProgress` | Drive inverter: a249 spin down learning in progress | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a250_tasSpeedLimitActive` | Drive inverter: a250 tas speed limit active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a251_diPowerOnStateMismatch` | Drive inverter: a251 di power on state mismatch | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a253_accelSynchWarn` | Drive inverter: a253 accel synch warn | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a254_vehicleStuckDetected` | Drive inverter: a254 vehicle stuck detected | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
