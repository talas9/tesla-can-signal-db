---
layout: default
title: "PNCD_IsoTpPipeToCp (0x6E6) — PNCD ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "PNCD ECU message: iso tp pipe to cp. Tesla Model Y CAN bus message PNCD_IsoTpPipeToCp (0x6E6) of PNCD ECU, firmware 2026.26.6.5, 1 signals (PNCD_isoTpToCpData). Bit layout, scaling, units and value tables."
---

# PNCD_IsoTpPipeToCp (0x6E6) — PNCD ECU, Tesla Model Y 2026.26.6.5 VEH CAN

PNCD ECU message: iso tp pipe to cp; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PNCD_IsoTpPipeToCp as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PNCD_IsoTpPipeToCp` |
| CAN id | 0x6E6 (1766) |
| ECU | [PNCD ECU](../../pncd.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PNCD_IsoTpPipeToCp

Tesla Model Y CAN bus signals in `PNCD_IsoTpPipeToCp`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PNCD_isoTpToCpData` | PNCD ECU: iso tp to cp data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All PNCD ECU messages (PNCD)](../../pncd.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
