---
layout: default
title: "RCM_inertial2 (0x111) — Restraint control module, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Restraint control module message: inertial2. Tesla Model 3 CAN bus message RCM_inertial2 (0x111) of Restraint control module, firmware 2026.26.6.5, 9 signals (RCM_longitudinalAccel, RCM_lateralAccel, RCM_verticalAccel, RCM_longitudinalAccelQF and 5 more). Bit layout, scaling, units and value tables."
---

# RCM_inertial2 (0x111) — Restraint control module, Tesla Model 3 2026.26.6.5 CH CAN

Restraint control module message: inertial2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of RCM_inertial2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_inertial2` |
| CAN id | 0x111 (273) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 9 |

## Signals of RCM_inertial2

Tesla Model 3 CAN bus signals in `RCM_inertial2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_longitudinalAccel` | Offset compensated longitudinal acceleration measured by the airbag ECU. ISO axis convention (positive during forward acceleration); raw 32768 = signal not available (SNA) | 0\|16 | little-endian | signed | 0.00125 | 0 | m/s^2 | -40.9575 to 40.9575 | -32768 = `SNA` | validated |
| `RCM_lateralAccel` | Reports offset compensated lateral acceleration measured by the airbag ECU. Follows ISO axis convention that measurements are positive during left turns and negative during right turns; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.00125 | 0 | m/s^2 | -40.9575 to 40.9575 | -32768 = `SNA` | validated |
| `RCM_verticalAccel` | Offset compensated vertical acceleration measured by the airbag ECU. ISO axis convention (positive up); raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.00125 | 0 | m/s^2 | -40.9575 to 39.2 | -32768 = `SNA` | validated |
| `RCM_longitudinalAccelQF` | Restraint control module: longitudinal accel QF | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAULTED`<br>1 = `NOT_FAULTED` | validated |
| `RCM_lateralAccelQF` | Restraint control module: lateral accel QF | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAULTED`<br>1 = `NOT_FAULTED` | validated |
| `RCM_verticalAccelQF` | Restraint control module: vertical accel QF | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAULTED`<br>1 = `NOT_FAULTED` | validated |
| `RCM_CGTranslationFault` | Restraint control module: CG translation fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RCM_COG_TRANSLATION_NOT_FAULTED`<br>1 = `RCM_COG_TRANSLATION_FAULTED` | validated |
| `RCM_inertial2Counter` | Restraint control module: inertial2 counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `RCM_inertial2Checksum` | Restraint control module: inertial2 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
