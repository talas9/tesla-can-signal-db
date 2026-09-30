---
layout: default
title: "DIF_alertMatrix4 (0x35B) — Front drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Front drive inverter message: alert matrix4. Ethernet-side message DIF_alertMatrix4 of Front drive inverter for Tesla Model 3 firmware 2025.20.8, 20 signals (DIF_a202_excessHeatUnavailable, DIF_a225_tmpEstPlausibility, DIF_a231_unintendedReset2, DIF_a233_diMsgMissed and 16 more). Bit layout, scaling, units and value tables."
---

# DIF_alertMatrix4 (0x35B) — Front drive inverter, Tesla Model 3 2025.20.8 ETH

Front drive inverter message: alert matrix4. This page documents the 20 signals of DIF_alertMatrix4 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_alertMatrix4` |
| Ethernet-side id | 0x35B (859) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 20 |

## Signals of DIF_alertMatrix4

Tesla Model 3 CAN bus signals in `DIF_alertMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_a202_excessHeatUnavailable` | Front drive inverter: a202 excess heat unavailable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a225_tmpEstPlausibility` | Front drive inverter: a225 tmp est plausibility | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a231_unintendedReset2` | Front drive inverter: a231 unintended reset2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a233_diMsgMissed` | Front drive inverter: a233 di msg missed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a234_pcsMIA` | Front drive inverter: a234 pcs MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a236_tasMIA` | Front drive inverter: a236 tas MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a241_systemThermallyLimited` | Front drive inverter: a241 system thermally limited | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a242_spinDownLearning` | Front drive inverter: a242 spin down learning | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a243_ecuLogAvailable` | Front drive inverter: a243 ecu log available | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_mechSafeStateApplied` | Front drive inverter: a244 mech safe state applied | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a245_mechSafeStatePreWarn` | Front drive inverter: a245 mech safe state pre warn | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_recoveryAtSpeedError` | Front drive inverter: a246 recovery at speed error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a247_rotorOffsetError` | Front drive inverter: a247 rotor offset error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a249_highStatorTempFromResist` | Front drive inverter: a249 high stator temp from resist | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a250_preregulatorRail` | Front drive inverter: a250 preregulator rail | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a251_oilPumpService` | Front drive inverter: a251 oil pump service | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a252_currentCoreFallback` | Front drive inverter: a252 current core fallback | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a253_lvBoostedRail` | Front drive inverter: a253 lv boosted rail | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a254_activeDischargeRail` | Front drive inverter: a254 active discharge rail | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a255_currentGainFallback` | Front drive inverter: a255 current gain fallback | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
