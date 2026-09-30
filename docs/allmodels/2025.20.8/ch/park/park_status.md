---
layout: default
title: "PARK_status (0x31E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Parking assist sensors message: status. Tesla Model 3 / Model Y CAN bus message PARK_status (0x31E) of Parking assist sensors, firmware 2025.20.8, 8 signals (PARK_status, PARK_serviceRequest, PARK_systemDtcPresent, PARK_statusCounter and 4 more). Bit layout, scaling, units and value tables."
---

# PARK_status (0x31E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Parking assist sensors message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of PARK_status as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_status` |
| CAN id | 0x31E (798) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 6 bytes |
| Cycle time | 500 ms |
| Signals | 8 |

## Signals of PARK_status

Tesla Model 3 / Model Y CAN bus signals in `PARK_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_status` | Indicates status of park assist function; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `ENABLED`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | validated |
| `PARK_serviceRequest` | Indicates whether or not PARK sensors/ECU require service; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_FAILURE`<br>1 = `FAILURE`<br>2 = `UNUSED`<br>3 = `SNA` | validated |
| `PARK_systemDtcPresent` | Boolean indicating whether or not there is a DTC present; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FALSE`<br>1 = `TRUE`<br>2 = `UNUSED`<br>3 = `SNA` | validated |
| `PARK_statusCounter` | Parking assist sensors: status counter | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `PARK_statusChecksum` | Parking assist sensors: status checksum | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PARK_majorVersion` | Parking assist sensors: major version; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 255 = `SNA` | validated |
| `PARK_minorVersion` | Parking assist sensors: minor version; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 255 = `SNA` | validated |
| `PARK_subMinorVersion` | Parking assist sensors: sub minor version; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 255 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
