---
layout: default
title: "PARK_sdiRear (0x22E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Parking assist sensors message: sdi rear. Tesla Model 3 / Model Y CAN bus message PARK_sdiRear (0x22E) of Parking assist sensors, firmware 2025.20.8, 8 signals (PARK_sdiSensor7RawDistData, PARK_sdiSensor8RawDistData, PARK_sdiSensor9RawDistData, PARK_sdiSensor10RawDistData and 4 more). Bit layout, scaling, units and value tables."
---

# PARK_sdiRear (0x22E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Parking assist sensors message: sdi rear; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of PARK_sdiRear as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_sdiRear` |
| CAN id | 0x22E (558) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 40 ms |
| Signals | 8 |

## Signals of PARK_sdiRear

Tesla Model 3 / Model Y CAN bus signals in `PARK_sdiRear`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_sdiSensor7RawDistData` | Parking assist sensors: sdi sensor7 raw dist data; raw 511 = signal not available (SNA) | 0\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor8RawDistData` | Parking assist sensors: sdi sensor8 raw dist data; raw 511 = signal not available (SNA) | 9\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor9RawDistData` | Parking assist sensors: sdi sensor9 raw dist data; raw 511 = signal not available (SNA) | 18\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor10RawDistData` | Parking assist sensors: sdi sensor10 raw dist data; raw 511 = signal not available (SNA) | 27\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor11RawDistData` | Parking assist sensors: sdi sensor11 raw dist data; raw 511 = signal not available (SNA) | 36\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor12RawDistData` | Parking assist sensors: sdi sensor12 raw dist data; raw 511 = signal not available (SNA) | 45\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiRearCounter` | Parking assist sensors: sdi rear counter | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `PARK_sdiRearChecksum` | Parking assist sensors: sdi rear checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
