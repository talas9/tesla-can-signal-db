---
layout: default
title: "VEH_isoTpToEvse (0x673) — VEH ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VEH ECU message: iso tp to evse. Tesla Model 3 / Model Y CAN bus message VEH_isoTpToEvse (0x673) of VEH ECU, firmware 2026.26.6.5, 1 signals (VEH_isoTpToEvseData). Bit layout, scaling, units and value tables."
---

# VEH_isoTpToEvse (0x673) — VEH ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VEH ECU message: iso tp to evse; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VEH_isoTpToEvse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VEH_isoTpToEvse` |
| CAN id | 0x673 (1651) |
| ECU | [VEH ECU](../../veh.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VEH_isoTpToEvse

Tesla Model 3 / Model Y CAN bus signals in `VEH_isoTpToEvse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VEH_isoTpToEvseData` | VEH ECU: iso tp to evse data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VEH ECU messages (VEH)](../../veh.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
