---
layout: default
title: "UI_IsoTpUDPPipeVCSEC (0x481) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: iso tp UDP pipe VCSEC. Tesla Model Y CAN bus message UI_IsoTpUDPPipeVCSEC (0x481) of Touchscreen user interface computer, firmware 2025.20.8, 8 signals (UI_IsoTpUDPPipeVCSEC0, UI_IsoTpUDPPipeVCSEC1, UI_IsoTpUDPPipeVCSEC2, UI_IsoTpUDPPipeVCSEC3 and 4 more). Bit layout, scaling, units and value tables."
---

# UI_IsoTpUDPPipeVCSEC (0x481) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: iso tp UDP pipe VCSEC; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of UI_IsoTpUDPPipeVCSEC as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_IsoTpUDPPipeVCSEC` |
| CAN id | 0x481 (1153) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of UI_IsoTpUDPPipeVCSEC

Tesla Model Y CAN bus signals in `UI_IsoTpUDPPipeVCSEC`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_IsoTpUDPPipeVCSEC0` | Touchscreen user interface computer: iso tp UDP pipe VCSEC0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC1` | Touchscreen user interface computer: iso tp UDP pipe VCSEC1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC2` | Touchscreen user interface computer: iso tp UDP pipe VCSEC2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC3` | Touchscreen user interface computer: iso tp UDP pipe VCSEC3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC4` | Touchscreen user interface computer: iso tp UDP pipe VCSEC4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC5` | Touchscreen user interface computer: iso tp UDP pipe VCSEC5 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC6` | Touchscreen user interface computer: iso tp UDP pipe VCSEC6 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpUDPPipeVCSEC7` | Touchscreen user interface computer: iso tp UDP pipe VCSEC7 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
