---
layout: default
title: "DI_systemPower (0x268) — Drive inverter, Tesla Model Y 2025.20.8 VEH CAN"
description: "Drive inverter message: system power. Tesla Model Y CAN bus message DI_systemPower (0x268) of Drive inverter, firmware 2025.20.8, 5 signals (DI_sysHeatPowerMax, DI_sysHeatPowerActual, DI_sysDrivePowerMax, DI_primaryUnitSiliconType and 1 more). Bit layout, scaling, units and value tables."
---

# DI_systemPower (0x268) — Drive inverter, Tesla Model Y 2025.20.8 VEH CAN

Drive inverter message: system power; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of DI_systemPower as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_systemPower` |
| CAN id | 0x268 (616) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of DI_systemPower

Tesla Model Y CAN bus signals in `DI_systemPower`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_sysHeatPowerMax` | Drive inverter: sys heat power max | 0\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DI_sysHeatPowerActual` | Drive Inverter system heat power | 8\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | plausible |
| `DI_sysDrivePowerMax` | Maximum drive power output total for all motors; raw 511 = signal not available (SNA) | 16\|10 | little-endian | unsigned | 1 | 0 | kW | 0 to 1023 | 511 = `SNA` | plausible |
| `DI_primaryUnitSiliconType` | Drive inverter: primary unit silicon type | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MOSFET`<br>1 = `IGBT` | plausible |
| `DI_sysRegenPowerMax` | Maximum regen power output total for all motors; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | -100 | kW | -100 to 0 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
