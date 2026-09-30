---
layout: default
title: "DIF_power (0x2E5) — Front drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front drive inverter message: power. Tesla Model Y CAN bus message DIF_power (0x2E5) of Front drive inverter, firmware 2026.26.6.5, 6 signals (DIF_elecPower, DIF_heatPowerOptimal, DIF_heatPowerMax, DIF_heatPowerActual and 2 more). Bit layout, scaling, units and value tables."
---

# DIF_power (0x2E5) — Front drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN

Front drive inverter message: power; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of DIF_power as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_power` |
| CAN id | 0x2E5 (741) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of DIF_power

Tesla Model Y CAN bus signals in `DIF_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_elecPower` | Front drive inverter: elec power; raw 1024 = signal not available (SNA) | 0\|11 | little-endian | signed | 0.5 | 0 | kW | -500 to 500 | -1024 = `SNA` | validated |
| `DIF_heatPowerOptimal` | Front drive inverter: heat power optimal | 16\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | validated |
| `DIF_heatPowerMax` | Drive Inverter maximum heat power capability | 24\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | validated |
| `DIF_heatPowerActual` | Drive Inverter heat power | 32\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | validated |
| `DIF_excessHeatCommand` | Drive Inverter excess heat command | 40\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | validated |
| `DIF_drivePowerMax` | Front drive inverter: drive power max; raw 511 = signal not available (SNA) | 48\|9 | little-endian | unsigned | 1 | 0 | kW | 0 to 400 | 511 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
