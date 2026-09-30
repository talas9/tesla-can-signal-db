---
layout: default
title: "FC_serial (0x514) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: serial. Tesla Model Y CAN bus message FC_serial (0x514) of FC ECU, firmware 2026.26.6.5, 18 signals (FC_serialDataSelect, FC_serialChar01, FC_serialChar02, FC_serialChar03 and 14 more). Bit layout, scaling, units and value tables."
---

# FC_serial (0x514) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN

FC ECU message: serial; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of FC_serial as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_serial` |
| CAN id | 0x514 (1300) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of FC_serial

Tesla Model Y CAN bus signals in `FC_serial`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_serialDataSelect` | selector | FC ECU: serial data select | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2` | plausible |
| `FC_serialChar01` | page 0 | FC ECU: serial char01 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar02` | page 0 | FC ECU: serial char02 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar03` | page 0 | FC ECU: serial char03 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar04` | page 0 | FC ECU: serial char04 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar05` | page 0 | FC ECU: serial char05 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar06` | page 0 | FC ECU: serial char06 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar07` | page 0 | FC ECU: serial char07 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar08` | page 1 | FC ECU: serial char08 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar09` | page 1 | FC ECU: serial char09 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar10` | page 1 | FC ECU: serial char10 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar11` | page 1 | FC ECU: serial char11 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar12` | page 1 | FC ECU: serial char12 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar13` | page 1 | FC ECU: serial char13 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar14` | page 1 | FC ECU: serial char14 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar15` | page 2 | FC ECU: serial char15 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar16` | page 2 | FC ECU: serial char16 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_serialChar17` | page 2 | FC ECU: serial char17 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Multiplexing

`FC_serialDataSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
