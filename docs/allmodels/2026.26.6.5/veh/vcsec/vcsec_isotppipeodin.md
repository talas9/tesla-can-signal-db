---
layout: default
title: "VCSEC_IsoTpPipeODIN (0x3B9) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message. Tesla Model 3 / Model Y CAN bus message VCSEC_IsoTpPipeODIN (0x3B9) of Vehicle security controller, firmware 2026.26.6.5, 8 signals (VCSEC_IsoTpPipeODIN0, VCSEC_IsoTpPipeODIN1, VCSEC_IsoTpPipeODIN2, VCSEC_IsoTpPipeODIN3 and 4 more). Bit layout, scaling, units and value tables."
---

# VCSEC_IsoTpPipeODIN (0x3B9) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Vehicle security controller message; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of VCSEC_IsoTpPipeODIN as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_IsoTpPipeODIN` |
| CAN id | 0x3B9 (953) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of VCSEC_IsoTpPipeODIN

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_IsoTpPipeODIN`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_IsoTpPipeODIN0` | Vehicle security controller: iso tp pipe ODIN0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN1` | Vehicle security controller: iso tp pipe ODIN1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN2` | Vehicle security controller: iso tp pipe ODIN2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN3` | Vehicle security controller: iso tp pipe ODIN3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN4` | Vehicle security controller: iso tp pipe ODIN4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN5` | Vehicle security controller: iso tp pipe ODIN5 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN6` | Vehicle security controller: iso tp pipe ODIN6 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpPipeODIN7` | Vehicle security controller: iso tp pipe ODIN7 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
