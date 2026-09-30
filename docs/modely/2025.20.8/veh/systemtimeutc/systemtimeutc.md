---
layout: default
title: "SystemTimeUTC (0x318) — SystemTimeUTC ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "Vector__XXX ECU message: system time UTC. Tesla Model Y CAN bus message SystemTimeUTC (0x318) of SystemTimeUTC ECU, firmware 2025.20.8, 6 signals (UTC_year, UTC_month, UTC_seconds, UTC_hour and 2 more). Bit layout, scaling, units and value tables."
---

# SystemTimeUTC (0x318) — SystemTimeUTC ECU, Tesla Model Y 2025.20.8 VEH CAN

Vector__XXX ECU message: system time UTC; frame length observed on a vehicle bus. This page documents the 6 signals of SystemTimeUTC as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SystemTimeUTC` |
| CAN id | 0x318 (792) |
| ECU | [SystemTimeUTC ECU](../../systemtimeutc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | other |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of SystemTimeUTC

Tesla Model Y CAN bus signals in `SystemTimeUTC`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UTC_year` | UTC date: year | 0\|8 | little-endian | unsigned | 1 | 2000 |  | 2000 to 2255 |  | validated |
| `UTC_month` | UTC date: month | 8\|8 | little-endian | unsigned | 1 | 0 |  | 1 to 12 |  | validated |
| `UTC_seconds` | UTC time: seconds | 16\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 59 |  | validated |
| `UTC_hour` | UTC time: hour | 24\|8 | little-endian | unsigned | 1 | 0 | h | 0 to 23 |  | validated |
| `UTC_day` | UTC date: day of month | 32\|8 | little-endian | unsigned | 1 | 0 |  | 1 to 31 |  | validated |
| `UTC_minutes` | UTC time: minutes | 40\|8 | little-endian | unsigned | 1 | 0 | min | 0 to 59 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All SystemTimeUTC ECU messages (SystemTimeUTC)](../../systemtimeutc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
