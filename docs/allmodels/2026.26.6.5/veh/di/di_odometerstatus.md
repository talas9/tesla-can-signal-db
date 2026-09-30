---
layout: default
title: "DI_odometerStatus (0x3B6) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: odometer status. Tesla Model 3 / Model Y CAN bus message DI_odometerStatus (0x3B6) of Drive inverter, firmware 2026.26.6.5, 4 signals (DI_odometer, DI_obdDriveCycleStatus, DI_odometerStatusCounter, DI_odometerStatusChecksum). Bit layout, scaling, units and value tables."
---

# DI_odometerStatus (0x3B6) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Drive inverter message: odometer status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of DI_odometerStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_odometerStatus` |
| CAN id | 0x3B6 (950) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of DI_odometerStatus

Tesla Model 3 / Model Y CAN bus signals in `DI_odometerStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_odometer` | Total traveled distance; raw 4294967295 = signal not available (SNA) | 0\|32 | little-endian | unsigned | 0.001 | 0 | km | 0 to 4294967.294 | 4294967295 = `SNA` | validated |
| `DI_obdDriveCycleStatus` | OBD qualified drive cycle status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_odometerStatusCounter` | Drive inverter: odometer status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_odometerStatusChecksum` | Drive inverter: odometer status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
