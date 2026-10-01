---
layout: default
title: "PARK_sensorStatusFront (0x32E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: sensor status front. Tesla Model 3 / Model Y CAN bus message PARK_sensorStatusFront (0x32E) of Parking assist sensors, firmware 2026.26.6.5, 10 signals (PARK_frontRightSensorState, PARK_frontRightMiddleSensorState, PARK_frontLeftMiddleSensorState, PARK_frontLeftSensorState and 6 more). Bit layout, scaling, units and value tables."
---

# PARK_sensorStatusFront (0x32E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: sensor status front; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of PARK_sensorStatusFront as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_sensorStatusFront` |
| CAN id | 0x32E (814) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of PARK_sensorStatusFront

Tesla Model 3 / Model Y CAN bus signals in `PARK_sensorStatusFront`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_frontRightSensorState` | Reports the state of the front right ultrasonic sensor; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_frontRightMiddleSensorState` | Reports the state of the front right middle ultrasonic sensor; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_frontLeftMiddleSensorState` | Reports the state of the front left middle ultrasonic sensor; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_frontLeftSensorState` | Reports the state of the front left ultrasonic sensor; raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_frontLeftRawDistData` | Zone defined as -90 degrees -&gt; -38 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_frontRightRawDistData` | Zone defined as +38 degrees -&gt; +90 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_systemStatusFront` | Parking assist sensors: system status front; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `ENABLED`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `PARK_frontDtcPresent` | Parking assist sensors: front dtc present; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FALSE`<br>1 = `TRUE`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `PARK_sensorStatusFrontCounter` | Parking assist sensors: sensor status front counter | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PARK_sensorStatusFrontChecksum` | Parking assist sensors: sensor status front checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
