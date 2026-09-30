---
layout: default
title: "VINbroadcast (0x405) — VINbroadcast ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "Vector__XXX ECU message: VI nbroadcast. Tesla Model 3 CAN bus message VINbroadcast (0x405) of VINbroadcast ECU, firmware 2025.20.8, 18 signals (VIN_muxID, VIN_char01, VIN_char02, VIN_char03 and 14 more). Bit layout, scaling, units and value tables."
---

# VINbroadcast (0x405) — VINbroadcast ECU, Tesla Model 3 2025.20.8 VEH CAN

Vector__XXX ECU message: VI nbroadcast; frame length observed on a vehicle bus. This page documents the 18 signals of VINbroadcast as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VINbroadcast` |
| CAN id | 0x405 (1029) |
| ECU | [VINbroadcast ECU](../../vinbroadcast.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | other |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of VINbroadcast

Tesla Model 3 CAN bus signals in `VINbroadcast`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VIN_muxID` | selector | Page index of the vehicle identification number text (16 = characters 1-3, 17 = characters 4-10, 18 = characters 11-17) | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 16 = `VIN_PAGE_1`<br>17 = `VIN_PAGE_2`<br>18 = `VIN_PAGE_3` | validated |
| `VIN_char01` | page 16 | Vehicle identification number, character 1 (ASCII) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char02` | page 16 | Vehicle identification number, character 2 (ASCII) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char03` | page 16 | Vehicle identification number, character 3 (ASCII) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char04` | page 17 | Vehicle identification number, character 4 (ASCII) | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char05` | page 17 | Vehicle identification number, character 5 (ASCII) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char06` | page 17 | Vehicle identification number, character 6 (ASCII) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char07` | page 17 | Vehicle identification number, character 7 (ASCII) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char08` | page 17 | Vehicle identification number, character 8 (ASCII) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char09` | page 17 | Vehicle identification number, character 9 (ASCII) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char10` | page 17 | Vehicle identification number, character 10 (ASCII) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char11` | page 18 | Vehicle identification number, character 11 (ASCII) | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char12` | page 18 | Vehicle identification number, character 12 (ASCII) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char13` | page 18 | Vehicle identification number, character 13 (ASCII) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char14` | page 18 | Vehicle identification number, character 14 (ASCII) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char15` | page 18 | Vehicle identification number, character 15 (ASCII) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char16` | page 18 | Vehicle identification number, character 16 (ASCII) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VIN_char17` | page 18 | Vehicle identification number, character 17 (ASCII) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Multiplexing

`VIN_muxID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 16 (3 signals), page 17 (7 signals), page 18 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All VINbroadcast ECU messages (VINbroadcast)](../../vinbroadcast.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
