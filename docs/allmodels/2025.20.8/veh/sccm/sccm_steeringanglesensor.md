---
layout: default
title: "SCCM_steeringAngleSensor (0x129) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Steering column control module message: steering angle sensor. Tesla Model 3 / Model Y CAN bus message SCCM_steeringAngleSensor (0x129) of Steering column control module, firmware 2025.20.8, 10 signals (SCCM_steeringAngleCrc, SCCM_steeringAngleCounter, SCCM_supplierID, SCCM_steeringAngleSensorStatus and 6 more). Bit layout, scaling, units and value tables."
---

# SCCM_steeringAngleSensor (0x129) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Steering column control module message: steering angle sensor; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of SCCM_steeringAngleSensor as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_steeringAngleSensor` |
| CAN id | 0x129 (297) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 10 |

## Signals of SCCM_steeringAngleSensor

Tesla Model 3 / Model Y CAN bus signals in `SCCM_steeringAngleSensor`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_steeringAngleCrc` | Steering column control module: steering angle crc | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_steeringAngleCounter` | Message counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `SCCM_supplierID` | Steering column control module: supplier ID | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `SCCM_steeringAngleSensorStatus` | Reports steering angle sensor status and validity based on bootup checks | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `INIT`<br>2 = `ERROR`<br>3 = `ERROR_INIT` | validated |
| `SCCM_steeringAngle` | Measured ASAS sensor angle; raw 16383 = signal not available (SNA) | 16\|14 | little-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819 | 16383 = `SNA` | validated |
| `SCCM_steeringAngleValidity` | Transitions to VALID when rotation of over 4 deg has occurred; raw 3 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `INVALID`<br>1 = `VALID`<br>2 = `INIT`<br>3 = `SNA` | validated |
| `SCCM_steeringAngleSpeed` | Speed of steering angle rotation | 32\|14 | little-endian | unsigned | 0.5 | -4096 | deg/s | -4096 to 4095.5 |  | validated |
| `SCCM_steeringAngleSensorReservd1` | Steering column control module: steering angle sensor reservd1 | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `SCCM_steeringAngleSensorReservd2` | Steering column control module: steering angle sensor reservd2 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_steeringAngleSensorReservd3` | Steering column control module: steering angle sensor reservd3 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
