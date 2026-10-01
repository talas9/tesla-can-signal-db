---
layout: default
title: "DI_chassisControl3 (0x74D) — Drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "Drive inverter message: chassis control3. Tesla Model 3 CAN bus message DI_chassisControl3 (0x74D) of Drive inverter, firmware 2026.26.6.5, 14 signals (DI_tireWearFactor_FrL, DI_tireWearFactor_FrR, DI_tireWearFactor_ReL, DI_tireWearFactor_ReR and 10 more). Bit layout, scaling, units and value tables."
---

# DI_chassisControl3 (0x74D) — Drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN

Drive inverter message: chassis control3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of DI_chassisControl3 as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_chassisControl3` |
| CAN id | 0x74D (1869) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of DI_chassisControl3

Tesla Model 3 CAN bus signals in `DI_chassisControl3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_tireWearFactor_FrL` | Drive inverter: tire wear factor fr l | 0\|6 | little-endian | unsigned | 0.00125 | 0.96 | ratio | 0.96 to 1.03875 |  | plausible |
| `DI_tireWearFactor_FrR` | Drive inverter: tire wear factor fr r | 6\|6 | little-endian | unsigned | 0.00125 | 0.96 | ratio | 0.96 to 1.03875 |  | plausible |
| `DI_tireWearFactor_ReL` | Drive inverter: tire wear factor re l | 12\|6 | little-endian | unsigned | 0.00125 | 0.96 | ratio | 0.96 to 1.03875 |  | plausible |
| `DI_tireWearFactor_ReR` | Drive inverter: tire wear factor re r | 18\|6 | little-endian | unsigned | 0.00125 | 0.96 | ratio | 0.96 to 1.03875 |  | plausible |
| `DI_kTireEstReUnSat` | Drive inverter: k tire est re un sat; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.001 | 0.008 | - | 0.008 to 0.075 | 127 = `SNA` | plausible |
| `DI_tireConfigSaved` | Drive inverter: tire config saved | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_distanceSinceLastTireConfig` | distance since odometer reading when Tire Configuration was last run; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 500 | 0 | km | 0 to 31000 | 63 = `SNA` | plausible |
| `DI_hydroplaningRisk` | Drive inverter: hydroplaning risk | 38\|2 | little-endian | unsigned | 0.333333343267 | 0 | - | 0 to 1 |  | plausible |
| `DI_hydroplaningPuddlesWet` | Drive inverter: hydroplaning puddles wet | 40\|4 | little-endian | unsigned | 1 | 0 | - | 0 to 15 |  | plausible |
| `DI_hydroplaningPuddlesDry` | Drive inverter: hydroplaning puddles dry | 44\|3 | little-endian | unsigned | 1 | 0 | - | 0 to 7 |  | plausible |
| `DI_vehicleStuck` | Drive inverter: vehicle stuck | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_kTireEstRe` | Drive inverter: k tire est re; raw 31 = signal not available (SNA) | 48\|5 | little-endian | unsigned | 0.001 | 0.03 | - | 0.03 to 0.06 | 31 = `SNA` | plausible |
| `DI_stickyMu` | Drive inverter: sticky mu | 53\|6 | little-endian | unsigned | 0.025 | 0 | - | 0 to 1.575 |  | plausible |
| `DI_stickyMuConfidence` | Drive inverter: sticky mu confidence | 59\|5 | little-endian | unsigned | 0.1 | 0 | probability | 0 to 3 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
