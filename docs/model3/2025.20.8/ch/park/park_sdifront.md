---
layout: default
title: "PARK_sdiFront (0x20E) — Parking assist sensors, Tesla Model 3 2025.20.8 CH CAN"
description: "Parking assist sensors message: sdi front. Tesla Model 3 CAN bus message PARK_sdiFront (0x20E) of Parking assist sensors, firmware 2025.20.8, 8 signals (PARK_sdiSensor1RawDistData, PARK_sdiSensor2RawDistData, PARK_sdiSensor3RawDistData, PARK_sdiSensor4RawDistData and 4 more). Bit layout, scaling, units and value tables."
---

# PARK_sdiFront (0x20E) — Parking assist sensors, Tesla Model 3 2025.20.8 CH CAN

Parking assist sensors message: sdi front; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of PARK_sdiFront as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_sdiFront` |
| CAN id | 0x20E (526) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 40 ms |
| Signals | 8 |

## Signals of PARK_sdiFront

Tesla Model 3 CAN bus signals in `PARK_sdiFront`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_sdiSensor1RawDistData` | Parking assist sensors: sdi sensor1 raw dist data; raw 511 = signal not available (SNA) | 0\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor2RawDistData` | Parking assist sensors: sdi sensor2 raw dist data; raw 511 = signal not available (SNA) | 9\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor3RawDistData` | Parking assist sensors: sdi sensor3 raw dist data; raw 511 = signal not available (SNA) | 18\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor4RawDistData` | Parking assist sensors: sdi sensor4 raw dist data; raw 511 = signal not available (SNA) | 27\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor5RawDistData` | Parking assist sensors: sdi sensor5 raw dist data; raw 511 = signal not available (SNA) | 36\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiSensor6RawDistData` | Parking assist sensors: sdi sensor6 raw dist data; raw 511 = signal not available (SNA) | 45\|9 | little-endian | unsigned | 1 | 0 | cm | 0 to 510 | 0 = `BLOCKED`<br>1 = `NEAR_DETECTION`<br>500 = `NO_OBJECT_DETECTED`<br>511 = `SNA` | validated |
| `PARK_sdiFrontCounter` | Parking assist sensors: sdi front counter | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `PARK_sdiFrontChecksum` | Parking assist sensors: sdi front checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
