---
layout: default
title: "VCSEC_IsoTpPipeRemoteUI (0x1DA) — Vehicle security controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: iso tp pipe remote UI. Tesla Model Y CAN bus message VCSEC_IsoTpPipeRemoteUI (0x1DA) of Vehicle security controller, firmware 2025.20.8, 8 signals (VCSEC_IsoTpRemoteUI0, VCSEC_IsoTpRemoteUI1, VCSEC_IsoTpRemoteUI2, VCSEC_IsoTpRemoteUI3 and 4 more). Bit layout, scaling, units and value tables."
---

# VCSEC_IsoTpPipeRemoteUI (0x1DA) — Vehicle security controller, Tesla Model Y 2025.20.8 VEH CAN

Vehicle security controller message: iso tp pipe remote UI; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of VCSEC_IsoTpPipeRemoteUI as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_IsoTpPipeRemoteUI` |
| CAN id | 0x1DA (474) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of VCSEC_IsoTpPipeRemoteUI

Tesla Model Y CAN bus signals in `VCSEC_IsoTpPipeRemoteUI`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_IsoTpRemoteUI0` | Vehicle security controller: iso tp remote UI0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI1` | Vehicle security controller: iso tp remote UI1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI2` | Vehicle security controller: iso tp remote UI2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI3` | Vehicle security controller: iso tp remote UI3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI4` | Vehicle security controller: iso tp remote UI4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI5` | Vehicle security controller: iso tp remote UI5 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI6` | Vehicle security controller: iso tp remote UI6 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_IsoTpRemoteUI7` | Vehicle security controller: iso tp remote UI7 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
