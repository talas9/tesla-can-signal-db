---
layout: default
title: "CP_IsoTpPipeToPncd (0x6E7) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Charge port controller message: iso tp pipe to pncd. Tesla Model 3 / Model Y CAN bus message CP_IsoTpPipeToPncd (0x6E7) of Charge port controller, firmware 2025.20.8, 1 signals (CP_isoTpToPncdData). Bit layout, scaling, units and value tables."
---

# CP_IsoTpPipeToPncd (0x6E7) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Charge port controller message: iso tp pipe to pncd; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of CP_IsoTpPipeToPncd as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_IsoTpPipeToPncd` |
| CAN id | 0x6E7 (1767) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of CP_IsoTpPipeToPncd

Tesla Model 3 / Model Y CAN bus signals in `CP_IsoTpPipeToPncd`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_isoTpToPncdData` | Charge port controller: iso tp to pncd data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
