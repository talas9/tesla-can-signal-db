---
layout: default
title: "FC_alertMatrix6 (0x3DE) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: alert matrix6. Tesla Model Y CAN bus message FC_alertMatrix6 (0x3DE) of FC ECU, firmware 2026.26.6.5, 1 signals (FC_a321_FCAlertPlaceholder). Bit layout, scaling, units and value tables."
---

# FC_alertMatrix6 (0x3DE) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN

FC ECU message: alert matrix6; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of FC_alertMatrix6 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_alertMatrix6` |
| CAN id | 0x3DE (990) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of FC_alertMatrix6

Tesla Model Y CAN bus signals in `FC_alertMatrix6`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_a321_FCAlertPlaceholder` | FC ECU: a321 FC alert placeholder | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
