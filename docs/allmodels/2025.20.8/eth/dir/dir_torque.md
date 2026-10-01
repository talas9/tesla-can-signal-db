---
layout: default
title: "DIR_torque (0x108) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: torque. Ethernet-side message DIR_torque of Rear drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 8 signals (DIR_torqueChecksum, DIR_torqueCounter, DIR_torqueCommand, DIR_axleSpeedQF and 4 more). Bit layout, scaling, units and value tables."
---

# DIR_torque (0x108) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Rear drive inverter message: torque. This page documents the 8 signals of DIR_torque as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_torque` |
| Ethernet-side id | 0x108 (264) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 8 |

## Signals of DIR_torque

Tesla Model 3 / Model Y CAN bus signals in `DIR_torque`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_torqueChecksum` | Rear drive inverter: torque checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIR_torqueCounter` | Rear drive inverter: torque counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIR_torqueCommand` | Torque commanded to the drive unit, referred to the axle/wheel; raw 4096 = signal not available (SNA) | 12\|13 | little-endian | signed | 2 | 0 | Nm | -7500 to 7500 | -4096 = `SNA` | plausible |
| `DIR_axleSpeedQF` | Rear drive inverter: axle speed QF | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `VALID`<br>2 = `FAULTED` | plausible |
| `DIR_torqueActual` | Actual torque the drive unit is controlling to referred to the axle/wheel; raw 4096 = signal not available (SNA) | 27\|13 | little-endian | signed | 2 | 0 | Nm | -7500 to 7500 | -4096 = `SNA` | plausible |
| `DIR_axleSpeed` | Drive Inverter motor speed normalized at axle level; raw 32768 = signal not available (SNA) | 40\|16 | little-endian | signed | 0.1 | 0 | RPM | -2750 to 2750 | -32768 = `SNA` | plausible |
| `DIR_axleTorqueQF` | Rear drive inverter: axle torque QF | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `VALID`<br>2 = `FAULTED` | plausible |
| `DIR_axlePowerCalcQF` | Rear drive inverter: axle power calc QF | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INVALID`<br>1 = `VALID` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
