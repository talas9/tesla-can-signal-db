---
layout: default
title: "ODIN_IsoTpPipeVCSEC (0x480) — External diagnostic tester, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "External diagnostic tester message: iso tp pipe VCSEC. Tesla Model 3 / Model Y CAN bus message ODIN_IsoTpPipeVCSEC (0x480) of External diagnostic tester, firmware 2026.26.6.5, 8 signals (ODIN_IsoTpPipeVCSEC0, ODIN_IsoTpPipeVCSEC1, ODIN_IsoTpPipeVCSEC2, ODIN_IsoTpPipeVCSEC3 and 4 more). Bit layout, scaling, units and value tables."
---

# ODIN_IsoTpPipeVCSEC (0x480) — External diagnostic tester, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

External diagnostic tester message: iso tp pipe VCSEC; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of ODIN_IsoTpPipeVCSEC as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ODIN_IsoTpPipeVCSEC` |
| CAN id | 0x480 (1152) |
| ECU | [External diagnostic tester](../../tester.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of ODIN_IsoTpPipeVCSEC

Tesla Model 3 / Model Y CAN bus signals in `ODIN_IsoTpPipeVCSEC`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ODIN_IsoTpPipeVCSEC0` | External diagnostic tester: iso tp pipe VCSEC0 | 7\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC1` | External diagnostic tester: iso tp pipe VCSEC1 | 15\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC2` | External diagnostic tester: iso tp pipe VCSEC2 | 23\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC3` | External diagnostic tester: iso tp pipe VCSEC3 | 31\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC4` | External diagnostic tester: iso tp pipe VCSEC4 | 39\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC5` | External diagnostic tester: iso tp pipe VCSEC5 | 47\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC6` | External diagnostic tester: iso tp pipe VCSEC6 | 55\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ODIN_IsoTpPipeVCSEC7` | External diagnostic tester: iso tp pipe VCSEC7 | 63\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All External diagnostic tester messages (tester)](../../tester.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
