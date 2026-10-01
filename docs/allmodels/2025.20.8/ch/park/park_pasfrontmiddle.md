---
layout: default
title: "PARK_pasFrontMiddle (0x34E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Parking assist sensors message: pas front middle. Tesla Model 3 / Model Y CAN bus message PARK_pasFrontMiddle (0x34E) of Parking assist sensors, firmware 2025.20.8, 5 signals (PARK_frontLeftMiddleRawDistData, PARK_frontMiddleRawDistData, PARK_frontRightMiddleRawDistData, PARK_pasFrontMiddleCounter and 1 more). Bit layout, scaling, units and value tables."
---

# PARK_pasFrontMiddle (0x34E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Parking assist sensors message: pas front middle; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of PARK_pasFrontMiddle as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pasFrontMiddle` |
| CAN id | 0x34E (846) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of PARK_pasFrontMiddle

Tesla Model 3 / Model Y CAN bus signals in `PARK_pasFrontMiddle`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_frontLeftMiddleRawDistData` | Zone defined as -38 degrees -&gt; +12 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_frontMiddleRawDistData` | Zone defined as -12 degrees to +12 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_frontRightMiddleRawDistData` | Zone defined +12 degrees to +38 degreees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_pasFrontMiddleCounter` | Parking assist sensors: pas front middle counter | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PARK_pasFrontMiddleChecksum` | Parking assist sensors: pas front middle checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
