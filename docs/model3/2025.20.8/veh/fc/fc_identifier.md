---
layout: default
title: "FC_identifier (0x517) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: identifier. Tesla Model 3 CAN bus message FC_identifier (0x517) of FC ECU, firmware 2025.20.8, 2 signals (FC_id, FC_sessionId). Bit layout, scaling, units and value tables."
---

# FC_identifier (0x517) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: identifier; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of FC_identifier as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_identifier` |
| CAN id | 0x517 (1303) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of FC_identifier

Tesla Model 3 CAN bus signals in `FC_identifier`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_id` | Fast charger identifying number | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `FC_sessionId` | Fast charge session ID | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
