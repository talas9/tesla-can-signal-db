---
layout: default
title: "PARK_pasSides (0x39E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: pas sides. Tesla Model 3 / Model Y CAN bus message PARK_pasSides (0x39E) of Parking assist sensors, firmware 2026.26.6.5, 6 signals (PARK_rightSideFrontRawDistData, PARK_rightSideRearRawDistData, PARK_leftSideFrontRawDistData, PARK_leftSideRearRawDistData and 2 more). Bit layout, scaling, units and value tables."
---

# PARK_pasSides (0x39E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: pas sides; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of PARK_pasSides as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pasSides` |
| CAN id | 0x39E (926) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of PARK_pasSides

Tesla Model 3 / Model Y CAN bus signals in `PARK_pasSides`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_rightSideFrontRawDistData` | Right side (from inside the car) towards the front of the car (split evenly between axles); raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_rightSideRearRawDistData` | Right side (from inside the car) towards the rear of the car (split evenly between axles); raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_leftSideFrontRawDistData` | Left side (from inside the car) towards the front of the car (split evenly between axles); raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_leftSideRearRawDistData` | Left side (from inside the car) towards the rear of the car (split evenly between axles); raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_pasSidesCounter` | Parking assist sensors: pas sides counter | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PARK_pasSidesChecksum` | Parking assist sensors: pas sides checksum | 36\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
