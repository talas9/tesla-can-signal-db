---
layout: default
title: "PARK_pasRearMiddle (0x35E) — Parking assist sensors, Tesla Model Y 2025.20.8 CH CAN"
description: "Parking assist sensors message: pas rear middle. Tesla Model Y CAN bus message PARK_pasRearMiddle (0x35E) of Parking assist sensors, firmware 2025.20.8, 5 signals (PARK_rearLeftMiddleRawDistData, PARK_rearMiddleRawDistData, PARK_rearRightMiddleRawDistData, PARK_pasRearMiddleCounter and 1 more). Bit layout, scaling, units and value tables."
---

# PARK_pasRearMiddle (0x35E) — Parking assist sensors, Tesla Model Y 2025.20.8 CH CAN

Parking assist sensors message: pas rear middle; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of PARK_pasRearMiddle as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pasRearMiddle` |
| CAN id | 0x35E (862) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of PARK_pasRearMiddle

Tesla Model Y CAN bus signals in `PARK_pasRearMiddle`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_rearLeftMiddleRawDistData` | Zone defined as -124 degrees to -166 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_rearMiddleRawDistData` | Zone defined as -166 degrees to +166 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_rearRightMiddleRawDistData` | Zone defined as +166 degrees to +124 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_pasRearMiddleCounter` | Parking assist sensors: pas rear middle counter | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PARK_pasRearMiddleChecksum` | Parking assist sensors: pas rear middle checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
