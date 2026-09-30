---
layout: default
title: "UI_IsoTpPipeRemoteVCSEC (0x482) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: iso tp pipe remote VCSEC. Tesla Model Y CAN bus message UI_IsoTpPipeRemoteVCSEC (0x482) of Touchscreen user interface computer, firmware 2026.26.6.5, 8 signals (UI_IsoTpRemoteVCSEC0, UI_IsoTpRemoteVCSEC1, UI_IsoTpRemoteVCSEC2, UI_IsoTpRemoteVCSEC3 and 4 more). Bit layout, scaling, units and value tables."
---

# UI_IsoTpPipeRemoteVCSEC (0x482) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: iso tp pipe remote VCSEC; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 8 signals of UI_IsoTpPipeRemoteVCSEC as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_IsoTpPipeRemoteVCSEC` |
| CAN id | 0x482 (1154) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of UI_IsoTpPipeRemoteVCSEC

Tesla Model Y CAN bus signals in `UI_IsoTpPipeRemoteVCSEC`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_IsoTpRemoteVCSEC0` | Touchscreen user interface computer: iso tp remote VCSEC0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC1` | Touchscreen user interface computer: iso tp remote VCSEC1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC2` | Touchscreen user interface computer: iso tp remote VCSEC2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC3` | Touchscreen user interface computer: iso tp remote VCSEC3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC4` | Touchscreen user interface computer: iso tp remote VCSEC4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC5` | Touchscreen user interface computer: iso tp remote VCSEC5 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC6` | Touchscreen user interface computer: iso tp remote VCSEC6 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_IsoTpRemoteVCSEC7` | Touchscreen user interface computer: iso tp remote VCSEC7 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
