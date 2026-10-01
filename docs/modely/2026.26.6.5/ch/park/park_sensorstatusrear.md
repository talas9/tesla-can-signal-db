---
layout: default
title: "PARK_sensorStatusRear (0x33E) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: sensor status rear. Tesla Model Y CAN bus message PARK_sensorStatusRear (0x33E) of Parking assist sensors, firmware 2026.26.6.5, 10 signals (PARK_rearRightSensorState, PARK_rearRightMiddleSensorState, PARK_rearLeftMiddleSensorState, PARK_rearLeftSensorState and 6 more). Bit layout, scaling, units and value tables."
---

# PARK_sensorStatusRear (0x33E) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: sensor status rear; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of PARK_sensorStatusRear as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_sensorStatusRear` |
| CAN id | 0x33E (830) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of PARK_sensorStatusRear

Tesla Model Y CAN bus signals in `PARK_sensorStatusRear`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_rearRightSensorState` | Reports the state of the rear right ultrasonic sensor; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_rearRightMiddleSensorState` | Reports the state of the rear right middle ultrasonic sensor; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_rearLeftMiddleSensorState` | Reports the state of the rear left middle ultrasonic sensor; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_rearLeftSensorState` | Reports the state of the rear left ultrasonic sensor; raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `PERMANENT_FAILURE`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `PARK_rearLeftRawDistData` | Zone defined as -90 degrees to -125 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_rearRightRawDistData` | Zone defined as +125 degrees to +90 degrees, distance to object in units of centimeters; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `PARK_systemStatusRear` | Parking assist sensors: system status rear; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `ENABLED`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `PARK_rearDtcPresent` | Parking assist sensors: rear dtc present; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FALSE`<br>1 = `TRUE`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `PARK_sensorStatusRearCounter` | Parking assist sensors: sensor status rear counter | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PARK_sensorStatusRearChecksum` | Parking assist sensors: sensor status rear checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
