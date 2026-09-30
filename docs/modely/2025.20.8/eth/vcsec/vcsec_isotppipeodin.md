---
layout: default
title: "VCSEC_IsoTpPipeODIN (0x3B9) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH"
description: "Vehicle security controller message. Ethernet-side message VCSEC_IsoTpPipeODIN of Vehicle security controller for Tesla Model Y firmware 2025.20.8, 8 signals (VCSEC_IsoTpPipeODIN0, VCSEC_IsoTpPipeODIN1, VCSEC_IsoTpPipeODIN2, VCSEC_IsoTpPipeODIN3 and 4 more). Bit layout, scaling, units and value tables."
---

# VCSEC_IsoTpPipeODIN (0x3B9) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH

Vehicle security controller message. This page documents the 8 signals of VCSEC_IsoTpPipeODIN as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_IsoTpPipeODIN` |
| Ethernet-side id | 0x3B9 (953) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of VCSEC_IsoTpPipeODIN

Tesla Model Y CAN bus signals in `VCSEC_IsoTpPipeODIN`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_IsoTpPipeODIN0` | Vehicle security controller: iso tp pipe ODIN0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN1` | Vehicle security controller: iso tp pipe ODIN1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN2` | Vehicle security controller: iso tp pipe ODIN2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN3` | Vehicle security controller: iso tp pipe ODIN3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN4` | Vehicle security controller: iso tp pipe ODIN4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN5` | Vehicle security controller: iso tp pipe ODIN5 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN6` | Vehicle security controller: iso tp pipe ODIN6 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCSEC_IsoTpPipeODIN7` | Vehicle security controller: iso tp pipe ODIN7 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
