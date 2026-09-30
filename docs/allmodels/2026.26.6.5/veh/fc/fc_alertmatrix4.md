---
layout: default
title: "FC_alertMatrix4 (0x39F) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: alert matrix4. Tesla Model 3 / Model Y CAN bus message FC_alertMatrix4 (0x39F) of FC ECU, firmware 2026.26.6.5, 1 signals (FC_a193_FCAlertPlaceholder). Bit layout, scaling, units and value tables."
---

# FC_alertMatrix4 (0x39F) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

FC ECU message: alert matrix4; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of FC_alertMatrix4 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_alertMatrix4` |
| CAN id | 0x39F (927) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of FC_alertMatrix4

Tesla Model 3 / Model Y CAN bus signals in `FC_alertMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_a193_FCAlertPlaceholder` | FC ECU: a193 FC alert placeholder | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
