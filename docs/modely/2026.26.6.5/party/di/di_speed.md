---
layout: default
title: "DI_speed (0x257) — Drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Drive inverter message: speed. Tesla Model Y CAN bus message DI_speed (0x257) of Drive inverter, firmware 2026.26.6.5, 11 signals (DI_speedChecksum, DI_speedCounter, DI_locSpeedEst, DI_uiSpeed and 7 more). Bit layout, scaling, units and value tables."
---

# DI_speed (0x257) — Drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN

Drive inverter message: speed; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of DI_speed as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_speed` |
| CAN id | 0x257 (599) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 11 |

## Signals of DI_speed

Tesla Model Y CAN bus signals in `DI_speed`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_speedChecksum` | Drive inverter: speed checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DI_speedCounter` | Drive inverter: speed counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_locSpeedEst` | Drive inverter: loc speed est; raw 4095 = signal not available (SNA) | 12\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 285 | 4095 = `SNA` | validated |
| `DI_uiSpeed` | Drive inverter: ui speed; raw 511 = signal not available (SNA) | 24\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 510 | 511 = `DI_UI_SPEED_SNA` | validated |
| `DI_uiSpeedUnits` | Drive inverter: ui speed units | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DI_SPEED_MPH`<br>1 = `DI_SPEED_KPH` | validated |
| `DI_accelPedalPressed` | TRUE when the calibrated accel pedal position &gt; 0.0 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_sideslipEstimate` | Drive inverter: sideslip estimate | 35\|8 | little-endian | signed | 0.0025 | 0 | rad | -0.32 to 0.3175 |  | validated |
| `DI_vehicleSpeed` | Reports vehicle speed; raw 8191 = signal not available (SNA) | 43\|13 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 480 | 8191 = `SNA` | validated |
| `DI_velocityEstimatorState` | Drive inverter: velocity estimator state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VE_STATE_NOT_INITIALIZED`<br>1 = `VE_STATE_WHEELS_NORMAL`<br>2 = `VE_STATE_WHEELS_REDUCED`<br>3 = `VE_STATE_BACKUP_WHEELS_A`<br>4 = `VE_STATE_BACKUP_WHEELS_B`<br>5 = `VE_STATE_BACKUP_MOTOR` | validated |
| `DI_autoEnableHazards` | Drive inverter: auto enable hazards | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_longControlCommandActive` | Drive inverter: long control command active | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
