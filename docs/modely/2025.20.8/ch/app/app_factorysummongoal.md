---
layout: default
title: "APP_factorySummonGoal (0x425) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: factory summon goal. Tesla Model Y CAN bus message APP_factorySummonGoal (0x425) of Driver assistance computer (primary), firmware 2025.20.8, 3 signals (APP_factoryGoalLatitude, APP_factoryGoalLongitude, APP_factoryGoalSpeed). Bit layout, scaling, units and value tables."
---

# APP_factorySummonGoal (0x425) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: factory summon goal; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of APP_factorySummonGoal as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_factorySummonGoal` |
| CAN id | 0x425 (1061) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of APP_factorySummonGoal

Tesla Model Y CAN bus signals in `APP_factorySummonGoal`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_factoryGoalLatitude` | Driver assistance computer (primary): factory goal latitude | 0\|28 | little-endian | signed | 1.0e-06 | 0 | deg | -134.217728 to 134.217727 |  | plausible |
| `APP_factoryGoalLongitude` | Driver assistance computer (primary): factory goal longitude | 28\|29 | little-endian | signed | 1.0e-06 | 0 | deg | -268.435456 to 268.435454 |  | plausible |
| `APP_factoryGoalSpeed` | Driver assistance computer (primary): factory goal speed | 57\|7 | little-endian | unsigned | 1 | 0 | mph | 0 to 100 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
