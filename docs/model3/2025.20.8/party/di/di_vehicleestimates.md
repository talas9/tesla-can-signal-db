---
layout: default
title: "DI_vehicleEstimates (0x267) — Drive inverter, Tesla Model 3 2025.20.8 PARTY CAN"
description: "Drive inverter message: vehicle estimates. Tesla Model 3 CAN bus message DI_vehicleEstimates (0x267) of Drive inverter, firmware 2025.20.8, 13 signals (DI_mass, DI_massRLS, DI_trailerDetected, DI_vehicleEstimatesCounter and 9 more). Bit layout, scaling, units and value tables."
---

# DI_vehicleEstimates (0x267) — Drive inverter, Tesla Model 3 2025.20.8 PARTY CAN

Drive inverter message: vehicle estimates; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of DI_vehicleEstimates as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_vehicleEstimates` |
| CAN id | 0x267 (615) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 13 |

## Signals of DI_vehicleEstimates

Tesla Model 3 CAN bus signals in `DI_vehicleEstimates`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_mass` | Detects learned mass. | 0\|8 | little-endian | unsigned | 25 | 1500 | kg | 1500 to 7850 |  | plausible |
| `DI_massRLS` | Drive inverter: mass RLS | 8\|7 | little-endian | unsigned | 45 | 1500 | kg | 1500 to 7170 |  | plausible |
| `DI_trailerDetected` | Drive inverter: trailer detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TRAILER_NOT_DETECTED`<br>1 = `TRAILER_DETECTED` | plausible |
| `DI_vehicleEstimatesCounter` | Drive inverter: vehicle estimates counter | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DI_relativeTireTreadDepth` | Reports estimate of tire wear ratio, represented in estimated tread depth difference between front and rear tires. A positive value indicates the rear tires are more worn than the front tires; raw 32 = signal not available (SNA) | 19\|6 | little-endian | signed | 0.4 | 0 | mm | -12.4 to 12.4 | -32 = `SNA` | plausible |
| `DI_tireFitment` | Drive inverter: tire fitment; raw 3 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FITMENT_SQUARE`<br>1 = `FITMENT_STAGGERED`<br>3 = `FITMENT_SNA` | plausible |
| `DI_rollCoeff` | Drive inverter: roll coeff | 27\|5 | little-endian | unsigned | 0.001 | 0 | g | 0 to 0.03 |  | plausible |
| `DI_massConfidence` | Drive inverter: mass confidence | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MASS_NOT_CONFIDED`<br>1 = `MASS_CONFIDED` | plausible |
| `DI_gradeEst` | Grade estimate reported by the drive inverter. | 33\|7 | little-endian | signed | 1 | 0 | % | -40 to 40 |  | plausible |
| `DI_vehicleEstimatesChecksum` | Drive inverter: vehicle estimates checksum | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_gradeEstInternal` | Drive inverter: grade est internal | 48\|7 | little-endian | signed | 1 | 0 | % | -40 to 40 |  | plausible |
| `DI_massConfidenceRLS` | Drive inverter: mass confidence RLS | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MASS_NOT_CONFIDED`<br>1 = `MASS_CONFIDED` | plausible |
| `DI_steeringAngleOffset` | Steering angle offset learned by vehicle dynamics control (VDC) represented as a hand wheel angle | 56\|8 | little-endian | signed | 0.2 | 0 | Deg | -25.6 to 25.4 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
