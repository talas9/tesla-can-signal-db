---
layout: default
title: "RCM_inertial1 (0x101) — Restraint control module, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Restraint control module message: inertial1. Tesla Model 3 CAN bus message RCM_inertial1 (0x101) of Restraint control module, firmware 2026.26.6.5, 8 signals (RCM_yawRate, RCM_pitchRate, RCM_rollRate, RCM_rollRateQF and 4 more). Bit layout, scaling, units and value tables."
---

# RCM_inertial1 (0x101) — Restraint control module, Tesla Model 3 2026.26.6.5 CH CAN

Restraint control module message: inertial1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of RCM_inertial1 as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_inertial1` |
| CAN id | 0x101 (257) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 8 |

## Signals of RCM_inertial1

Tesla Model 3 CAN bus signals in `RCM_inertial1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_yawRate` | Offset compensated yaw rate measured by the airbag ECU. ISO axis convention (Positive during left turn); raw 32768 = signal not available (SNA) | 0\|16 | little-endian | signed | 0.0001 | 0 | rad/s | -3.2766 to 3.2766 | -32768 = `SNA` | plausible |
| `RCM_pitchRate` | Offset compensated pitch rate measured by the airbag ECU. ISO axis convention (positive when the nose pitches down); raw 16384 = signal not available (SNA) | 16\|15 | little-endian | signed | 0.00025 | 0 | rad/s | -4.096 to 4.09575 | -16384 = `SNA` | plausible |
| `RCM_rollRate` | Offset compensated roll rate measured by the airbag ECU. ISO axis convention (positive during left turn); raw 16384 = signal not available (SNA) | 31\|15 | little-endian | signed | 0.00025 | 0 | rad/s | -4.096 to 4.09575 | -16384 = `SNA` | plausible |
| `RCM_rollRateQF` | Restraint control module: roll rate QF | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `VALID`<br>2 = `TEMP_INVALID`<br>3 = `FAULTED` | plausible |
| `RCM_yawRateQF` | Restraint control module: yaw rate QF | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAULTED`<br>1 = `NOT_FAULTED` | plausible |
| `RCM_pitchRateQF` | Restraint control module: pitch rate QF | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `VALID`<br>2 = `TEMP_INVALID`<br>3 = `FAULTED` | plausible |
| `RCM_inertial1Counter` | Restraint control module: inertial1 counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `RCM_inertial1Checksum` | Restraint control module: inertial1 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
