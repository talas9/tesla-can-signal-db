---
layout: default
title: "RCM_collision (0x11) — Restraint control module, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Restraint control module message: collision. Tesla Model Y CAN bus message RCM_collision (0x11) of Restraint control module, firmware 2026.26.6.5, 9 signals (RCM_collisionChecksum, RCM_collisionCounter, RCM_collisionRear, RCM_collisionRight and 5 more). Bit layout, scaling, units and value tables."
---

# RCM_collision (0x11) — Restraint control module, Tesla Model Y 2026.26.6.5 PARTY CAN

Restraint control module message: collision; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of RCM_collision as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_collision` |
| CAN id | 0x11 (17) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | RCM |
| Frame length | 4 bytes |
| Cycle time | 10 ms |
| Signals | 9 |

## Signals of RCM_collision

Tesla Model Y CAN bus signals in `RCM_collision`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_collisionChecksum` | Restraint control module: collision checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_collisionCounter` | Restraint control module: collision counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `RCM_collisionRear` | Indicates that a rear collision occurred; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionRight` | Indicates that a right side collision occurred; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionLeft` | Indicates that a left side collision occurred; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionFront` | Indicates that a frontal collision occurred; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionRollover` | Indicates that a rollover has occurred; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionPedPro` | Indicates that a pedestrian impact has occurred; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_COLLISION_EVENT_INACTIVE`<br>1 = `RCM_COLLISION_EVENT_ACTIVE`<br>3 = `RCM_COLLISION_EVENT_SNA` | validated |
| `RCM_collisionSeverity` | Collision severity | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_COLLISION_SEVERITY_PRETENSIONER`<br>1 = `RCM_COLLISION_SEVERITY_FIRST_STAGE`<br>2 = `RCM_COLLISION_SEVERITY_SECOND_STAGE`<br>3 = `RCM_COLLISION_SEVERITY_PEDPRO_EVENT` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
