---
layout: default
title: "DIR_alertMatrix4 (0x3E5) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: alert matrix4. Ethernet-side message DIR_alertMatrix4 of Rear drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 21 signals (DIR_a202_excessHeatUnavailable, DIR_a225_tmpEstPlausibility, DIR_a231_unintendedReset2, DIR_a233_diMsgMissed and 17 more). Bit layout, scaling, units and value tables."
---

# DIR_alertMatrix4 (0x3E5) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Rear drive inverter message: alert matrix4. This page documents the 21 signals of DIR_alertMatrix4 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_alertMatrix4` |
| Ethernet-side id | 0x3E5 (997) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 21 |

## Signals of DIR_alertMatrix4

Tesla Model 3 / Model Y CAN bus signals in `DIR_alertMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_a202_excessHeatUnavailable` | Rear drive inverter: a202 excess heat unavailable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a225_tmpEstPlausibility` | Rear drive inverter: a225 tmp est plausibility | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a231_unintendedReset2` | Rear drive inverter: a231 unintended reset2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a233_diMsgMissed` | Rear drive inverter: a233 di msg missed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a234_pcsMIA` | Rear drive inverter: a234 pcs MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a236_tasMIA` | Rear drive inverter: a236 tas MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a241_systemThermallyLimited` | Rear drive inverter: a241 system thermally limited | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a242_spinDownLearning` | Rear drive inverter: a242 spin down learning | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a243_ecuLogAvailable` | Rear drive inverter: a243 ecu log available | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a244_mechSafeStateApplied` | Rear drive inverter: a244 mech safe state applied | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a245_mechSafeStatePreWarn` | Rear drive inverter: a245 mech safe state pre warn | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a246_recoveryAtSpeedError` | Rear drive inverter: a246 recovery at speed error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a247_rotorOffsetError` | Rear drive inverter: a247 rotor offset error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a248_vehicleSpeedLimited` | Rear drive inverter: a248 vehicle speed limited | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a249_highStatorTempFromResist` | Rear drive inverter: a249 high stator temp from resist | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a250_preregulatorRail` | Rear drive inverter: a250 preregulator rail | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a251_oilPumpService` | Rear drive inverter: a251 oil pump service | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a252_currentCoreFallback` | Rear drive inverter: a252 current core fallback | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a253_lvBoostedRail` | Rear drive inverter: a253 lv boosted rail | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a254_activeDischargeRail` | Rear drive inverter: a254 active discharge rail | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a255_currentGainFallback` | Rear drive inverter: a255 current gain fallback | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
