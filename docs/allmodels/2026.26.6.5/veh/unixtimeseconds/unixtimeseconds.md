---
layout: default
title: "UnixTimeSeconds (0x528) — UnixTimeSeconds ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Vector__XXX ECU message: unix time seconds. Tesla Model 3 / Model Y CAN bus message UnixTimeSeconds (0x528) of UnixTimeSeconds ECU, firmware 2026.26.6.5, 1 signals (UnixTimeSeconds). Bit layout, scaling, units and value tables."
---

# UnixTimeSeconds (0x528) — UnixTimeSeconds ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Vector__XXX ECU message: unix time seconds; frame length observed on a vehicle bus. This page documents the 1 signals of UnixTimeSeconds as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UnixTimeSeconds` |
| CAN id | 0x528 (1320) |
| ECU | [UnixTimeSeconds ECU](../../unixtimeseconds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | other |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of UnixTimeSeconds

Tesla Model 3 / Model Y CAN bus signals in `UnixTimeSeconds`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UnixTimeSeconds` | Vehicle clock, seconds since 1970-01-01 UTC | 7\|32 | big-endian | unsigned | 1 | 0 | s | 0 to 4294967295 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All UnixTimeSeconds ECU messages (UnixTimeSeconds)](../../unixtimeseconds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
