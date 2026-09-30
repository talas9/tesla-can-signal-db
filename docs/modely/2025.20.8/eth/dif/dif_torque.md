---
layout: default
title: "DIF_torque (0x186) — Front drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Front drive inverter message: torque. Ethernet-side message DIF_torque of Front drive inverter for Tesla Model Y firmware 2025.20.8, 8 signals (DIF_torqueChecksum, DIF_torqueCounter, DIF_torqueCommand, DIF_axleSpeedQF and 4 more). Bit layout, scaling, units and value tables."
---

# DIF_torque (0x186) — Front drive inverter, Tesla Model Y 2025.20.8 ETH

Front drive inverter message: torque. This page documents the 8 signals of DIF_torque as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_torque` |
| Ethernet-side id | 0x186 (390) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of DIF_torque

Tesla Model Y CAN bus signals in `DIF_torque`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_torqueChecksum` | Front drive inverter: torque checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_torqueCounter` | Front drive inverter: torque counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DIF_torqueCommand` | Torque commanded to the drive unit, referred to the axle/wheel; raw 4096 = signal not available (SNA) | 12\|13 | little-endian | signed | 2 | 0 | Nm | -7500 to 7500 | -4096 = `SNA` | validated |
| `DIF_axleSpeedQF` | Front drive inverter: axle speed QF | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `VALID`<br>2 = `FAULTED` | validated |
| `DIF_torqueActual` | Actual torque the drive unit is controlling to referred to the axle/wheel; raw 4096 = signal not available (SNA) | 27\|13 | little-endian | signed | 2 | 0 | Nm | -7500 to 7500 | -4096 = `SNA` | validated |
| `DIF_axleSpeed` | Drive Inverter motor speed normalized at axle level; raw 32768 = signal not available (SNA) | 40\|16 | little-endian | signed | 0.1 | 0 | RPM | -2750 to 2750 | -32768 = `SNA` | validated |
| `DIF_axleTorqueQF` | Front drive inverter: axle torque QF | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `VALID`<br>2 = `FAULTED` | validated |
| `DIF_axlePowerCalcQF` | Front drive inverter: axle power calc QF | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INVALID`<br>1 = `VALID` | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
