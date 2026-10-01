---
layout: default
title: "DI_stalklessInterfaces (0x258) — Drive inverter, Tesla Model 3 2025.20.8 PARTY CAN"
description: "Drive inverter message: stalkless interfaces. Tesla Model 3 CAN bus message DI_stalklessInterfaces (0x258) of Drive inverter, firmware 2025.20.8, 8 signals (DI_stalklessInterfacesChecksum, DI_stalklessInterfacesCounter, DI_smartShiftClosureOpen, DI_smartShiftSeatbeltUnbuckled and 4 more). Bit layout, scaling, units and value tables."
---

# DI_stalklessInterfaces (0x258) — Drive inverter, Tesla Model 3 2025.20.8 PARTY CAN

Drive inverter message: stalkless interfaces; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of DI_stalklessInterfaces as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_stalklessInterfaces` |
| CAN id | 0x258 (600) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of DI_stalklessInterfaces

Tesla Model 3 CAN bus signals in `DI_stalklessInterfaces`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_stalklessInterfacesChecksum` | Drive inverter: stalkless interfaces checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_stalklessInterfacesCounter` | Drive inverter: stalkless interfaces counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DI_smartShiftClosureOpen` | Drive inverter: smart shift closure open | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftSeatbeltUnbuckled` | Drive inverter: smart shift seatbelt unbuckled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftAvailable` | Drive inverter: smart shift available | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftPrimed` | Drive inverter: smart shift primed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftBrakePressed` | Drive inverter: smart shift brake pressed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftBrakeReapplyRequired` | Drive inverter: smart shift brake reapply required | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
