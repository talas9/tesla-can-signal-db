---
layout: default
title: "PARK_pscEnvSlot (0x25E) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: psc env slot. Tesla Model Y CAN bus message PARK_pscEnvSlot (0x25E) of Parking assist sensors, firmware 2026.26.6.5, 25 signals (PARK_pscEnvSlotType, PARK_pscLeftParallelObj1X, PARK_pscLeftParallelObj1Y, PARK_pscLeftParallelObj1Alpha and 21 more). Bit layout, scaling, units and value tables."
---

# PARK_pscEnvSlot (0x25E) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: psc env slot; frame length from the layout, not yet observed on a vehicle bus. This page documents the 25 signals of PARK_pscEnvSlot as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_pscEnvSlot` |
| CAN id | 0x25E (606) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 25 |

## Signals of PARK_pscEnvSlot

Tesla Model Y CAN bus signals in `PARK_pscEnvSlot`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_pscEnvSlotType` | selector | Parking assist sensors: psc env slot type | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEFT_PARALLEL`<br>1 = `LEFT_CROSS`<br>2 = `RIGHT_PARALLEL`<br>3 = `RIGHT_CROSS` | plausible |
| `PARK_pscLeftParallelObj1X` | page 0 | Parking assist sensors: psc left parallel obj1 x; raw 2047 = signal not available (SNA) | 3\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftParallelObj1Y` | page 0 | Parking assist sensors: psc left parallel obj1 y; raw 2047 = signal not available (SNA) | 14\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftParallelObj1Alpha` | page 0 | Parking assist sensors: psc left parallel obj1 alpha; raw 127 = signal not available (SNA) | 25\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscLeftParallelObj2Y` | page 0 | Parking assist sensors: psc left parallel obj2 y; raw 2047 = signal not available (SNA) | 35\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftParallelObj2X` | page 0 | Parking assist sensors: psc left parallel obj2 x; raw 2047 = signal not available (SNA) | 46\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftParallelObj2Alpha` | page 0 | Parking assist sensors: psc left parallel obj2 alpha; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscLeftCrossObj1X` | page 1 | Parking assist sensors: psc left cross obj1 x; raw 2047 = signal not available (SNA) | 3\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftCrossObj1Y` | page 1 | Parking assist sensors: psc left cross obj1 y; raw 2047 = signal not available (SNA) | 14\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftCrossObj1Alpha` | page 1 | Parking assist sensors: psc left cross obj1 alpha; raw 127 = signal not available (SNA) | 25\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscLeftCrossObj2Y` | page 1 | Parking assist sensors: psc left cross obj2 y; raw 2047 = signal not available (SNA) | 35\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftCrossObj2X` | page 1 | Parking assist sensors: psc left cross obj2 x; raw 2047 = signal not available (SNA) | 46\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscLeftCrossObj2Alpha` | page 1 | Parking assist sensors: psc left cross obj2 alpha; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscRightParallelObj1X` | page 2 | Parking assist sensors: psc right parallel obj1 x; raw 2047 = signal not available (SNA) | 3\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightParallelObj1Y` | page 2 | Parking assist sensors: psc right parallel obj1 y; raw 2047 = signal not available (SNA) | 14\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightParallelObj1Alpha` | page 2 | Parking assist sensors: psc right parallel obj1 alpha; raw 127 = signal not available (SNA) | 25\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscRightParallelObj2Y` | page 2 | Parking assist sensors: psc right parallel obj2 y; raw 2047 = signal not available (SNA) | 35\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightParallelObj2X` | page 2 | Parking assist sensors: psc right parallel obj2 x; raw 2047 = signal not available (SNA) | 46\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightParallelObj2Alpha` | page 2 | Parking assist sensors: psc right parallel obj2 alpha; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscRightCrossObj1X` | page 3 | Parking assist sensors: psc right cross obj1 x; raw 2047 = signal not available (SNA) | 3\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightCrossObj1Y` | page 3 | Parking assist sensors: psc right cross obj1 y; raw 2047 = signal not available (SNA) | 14\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightCrossObj1Alpha` | page 3 | Parking assist sensors: psc right cross obj1 alpha; raw 127 = signal not available (SNA) | 25\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |
| `PARK_pscRightCrossObj2Y` | page 3 | Parking assist sensors: psc right cross obj2 y; raw 2047 = signal not available (SNA) | 35\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightCrossObj2X` | page 3 | Parking assist sensors: psc right cross obj2 x; raw 2047 = signal not available (SNA) | 46\|11 | little-endian | unsigned | 2 | -2048 | cm | -2048 to 2044 | 2046 = `NO_SPACE`<br>2047 = `SNA` | plausible |
| `PARK_pscRightCrossObj2Alpha` | page 3 | Parking assist sensors: psc right cross obj2 alpha; raw 127 = signal not available (SNA) | 57\|7 | little-endian | unsigned | 2 | -128 | deg | -128 to 124 | 126 = `NO_SPACE`<br>127 = `SNA` | plausible |

## Multiplexing

`PARK_pscEnvSlotType` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 1 (6 signals), page 2 (6 signals), page 3 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
