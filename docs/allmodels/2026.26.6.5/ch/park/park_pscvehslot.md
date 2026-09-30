---
layout: default
title: "PARK_pscVehSlot (0x24E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: psc veh slot. Tesla Model 3 / Model Y CAN bus message PARK_pscVehSlot (0x24E) of Parking assist sensors, firmware 2026.26.6.5, 21 signals (PARK_pscVehSlotType, PARK_pscLeftParallelVehX, PARK_pscLeftParallelVehY, PARK_pscLeftParallelPsi and 17 more). Bit layout, scaling, units and value tables."
---

# PARK_pscVehSlot (0x24E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: psc veh slot; frame length from the layout, not yet observed on a vehicle bus. This page documents the 21 signals of PARK_pscVehSlot as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pscVehSlot` |
| CAN id | 0x24E (590) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 21 |

## Signals of PARK_pscVehSlot

Tesla Model 3 / Model Y CAN bus signals in `PARK_pscVehSlot`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_pscVehSlotType` | selector | Parking assist sensors: psc veh slot type | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEFT_PARALLEL`<br>1 = `LEFT_CROSS`<br>2 = `RIGHT_PARALLEL`<br>3 = `RIGHT_CROSS` | plausible |
| `PARK_pscLeftParallelVehX` | page 0 | Parking assist sensors: psc left parallel veh x; raw 2047 = signal not available (SNA) | 5\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscLeftParallelVehY` | page 0 | Parking assist sensors: psc left parallel veh y; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscLeftParallelPsi` | page 0 | Parking assist sensors: psc left parallel psi; raw 8191 = signal not available (SNA) | 32\|13 | little-endian | unsigned | 0.0009765625 | 0 | radians | 0 to 7.998046875 | 8190 = `NO_SPACE`<br>8191 = `SNA` | validated |
| `PARK_pscLeftParallelSizeX` | page 0 | Parking assist sensors: psc left parallel size x; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscLeftParallelSizeY` | page 0 | Parking assist sensors: psc left parallel size y; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscLeftCrossVehX` | page 1 | Parking assist sensors: psc left cross veh x; raw 2047 = signal not available (SNA) | 5\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscLeftCrossVehY` | page 1 | Parking assist sensors: psc left cross veh y; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscLeftCrossPsi` | page 1 | Parking assist sensors: psc left cross psi; raw 8191 = signal not available (SNA) | 32\|13 | little-endian | unsigned | 0.0009765625 | 0 | radians | 0 to 7.998046875 | 8190 = `NO_SPACE`<br>8191 = `SNA` | validated |
| `PARK_pscLeftCrossSizeX` | page 1 | Parking assist sensors: psc left cross size x; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscLeftCrossSizeY` | page 1 | Parking assist sensors: psc left cross size y; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscRightParallelVehX` | page 2 | Parking assist sensors: psc right parallel veh x; raw 2047 = signal not available (SNA) | 5\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscRightParallelVehY` | page 2 | Parking assist sensors: psc right parallel veh y; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscRightParallelPsi` | page 2 | Parking assist sensors: psc right parallel psi; raw 8191 = signal not available (SNA) | 32\|13 | little-endian | unsigned | 0.0009765625 | 0 | radians | 0 to 7.998046875 | 8190 = `NO_SPACE`<br>8191 = `SNA` | validated |
| `PARK_pscRightParallelSizeX` | page 2 | Parking assist sensors: psc right parallel size x; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscRightParallelSizeY` | page 2 | Parking assist sensors: psc right parallel size y; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscRightCrossVehX` | page 3 | Parking assist sensors: psc right cross veh x; raw 2047 = signal not available (SNA) | 5\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscRightCrossVehY` | page 3 | Parking assist sensors: psc right cross veh y; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | validated |
| `PARK_pscRightCrossPsi` | page 3 | Parking assist sensors: psc right cross psi; raw 8191 = signal not available (SNA) | 32\|13 | little-endian | unsigned | 0.0009765625 | 0 | radians | 0 to 7.998046875 | 8190 = `NO_SPACE`<br>8191 = `SNA` | validated |
| `PARK_pscRightCrossSizeX` | page 3 | Parking assist sensors: psc right cross size x; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |
| `PARK_pscRightCrossSizeY` | page 3 | Parking assist sensors: psc right cross size y; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | 0 | cm | 0 to 1016 | 254 = `NO_SPACE`<br>255 = `SNA` | validated |

## Multiplexing

`PARK_pscVehSlotType` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (5 signals), page 2 (5 signals), page 3 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
