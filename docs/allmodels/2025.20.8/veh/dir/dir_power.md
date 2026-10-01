---
layout: default
title: "DIR_power (0x266) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Rear drive inverter message: power. Tesla Model 3 / Model Y CAN bus message DIR_power (0x266) of Rear drive inverter, firmware 2025.20.8, 6 signals (DIR_elecPower, DIR_heatPowerOptimal, DIR_heatPowerMax, DIR_heatPowerActual and 2 more). Bit layout, scaling, units and value tables."
---

# DIR_power (0x266) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Rear drive inverter message: power; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of DIR_power as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_power` |
| CAN id | 0x266 (614) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of DIR_power

Tesla Model 3 / Model Y CAN bus signals in `DIR_power`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_elecPower` | Rear drive inverter: elec power; raw 1024 = signal not available (SNA) | 0\|11 | little-endian | signed | 0.5 | 0 | kW | -500 to 500 | -1024 = `SNA` | plausible |
| `DIR_heatPowerOptimal` | Rear drive inverter: heat power optimal | 16\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DIR_heatPowerMax` | Drive Inverter maximum heat power capability | 24\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DIR_heatPowerActual` | Drive Inverter heat power | 32\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DIR_excessHeatCommand` | Drive Inverter excess heat command | 40\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DIR_drivePowerMax` | Rear drive inverter: drive power max; raw 511 = signal not available (SNA) | 48\|9 | little-endian | unsigned | 1 | 0 | kW | 0 to 400 | 511 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
