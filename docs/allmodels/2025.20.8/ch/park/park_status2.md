---
layout: default
title: "PARK_status2 (0x30E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Parking assist sensors message: status2. Tesla Model 3 / Model Y CAN bus message PARK_status2 (0x30E) of Parking assist sensors, firmware 2025.20.8, 15 signals (PARK_frontSVACharID, PARK_pscRightCurbType, PARK_rearSVACharID, PARK_pscLeftCurbType and 11 more). Bit layout, scaling, units and value tables."
---

# PARK_status2 (0x30E) — Parking assist sensors, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Parking assist sensors message: status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of PARK_status2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_status2` |
| CAN id | 0x30E (782) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 250 ms |
| Signals | 15 |

## Signals of PARK_status2

Tesla Model 3 / Model Y CAN bus signals in `PARK_status2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_frontSVACharID` | Parking assist sensors: front SVA char ID | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `PARK_pscRightCurbType` | The type of curb for the parallel parking slot on the right side. | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VIRTUAL_CURB`<br>1 = `LOW_CURB`<br>2 = `HIGH_CURB` | validated |
| `PARK_rearSVACharID` | Parking assist sensors: rear SVA char ID | 8\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | validated |
| `PARK_pscLeftCurbType` | The type of curb identified for a parallel parking space on the left. | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VIRTUAL_CURB`<br>1 = `LOW_CURB`<br>2 = `HIGH_CURB` | validated |
| `PARK_autoCalComplete` | Parking assist sensors: auto cal complete | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INCOMPLETE`<br>1 = `COMPLETE` | validated |
| `PARK_geometryType` | Parking assist sensors: geometry type | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MODELS`<br>1 = `MODELX`<br>2 = `MODEL3`<br>3 = `MODELY` | validated |
| `PARK_tireFitment` | Parking assist sensors: tire fitment; raw 3 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SQUARE`<br>1 = `STAGGERED`<br>2 = `NOT_USED`<br>3 = `SNA` | validated |
| `PARK_rackDetected` | Parking assist sensors: rack detected; raw 3 = signal not available (SNA) | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `UNKNOWN`<br>1 = `NO_RACK`<br>2 = `RACK_DETECTED`<br>3 = `SNA` | validated |
| `PARK_sdiActive` | Whether or not the raw sensor measurements from the ultrasonics are present and valid | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SDI_DISABLED`<br>1 = `SDI_ENABLED` | validated |
| `PARK_sdiNoise` | The output of the noise detection algorithm for raw sensor measurements, indicates if the measurements are degraded due to ambient noise; raw 3 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SDI_NOISE_NOMINAL`<br>1 = `SDI_NOISE_HIGH`<br>2 = `SDI_NOISE_RAIN`<br>3 = `SDI_NOISE_SNA` | validated |
| `PARK_sdiBlindSpotRight` | The output of the PARK ECU blindspot algorithm on the right side of the car, indicates the presence of a vehicle; raw 3 = signal not available (SNA) | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_WARNING`<br>1 = `WARNING`<br>2 = `UNUSED`<br>3 = `SNA` | validated |
| `PARK_sdiBlindSpotLeft` | The output of the PARK ECU blindspot algorithm on the left side of the car, indicates the presence of a vehicle; raw 3 = signal not available (SNA) | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NO_WARNING`<br>1 = `WARNING`<br>2 = `UNUSED`<br>3 = `SNA` | validated |
| `PARK_sensorType` | Parking assist sensors: sensor type; raw 3 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | validated |
| `PARK_status2Counter` | Parking assist sensors: status2 counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `PARK_status2Checksum` | Parking assist sensors: status2 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
