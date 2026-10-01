---
layout: default
title: "DI_maxRatedPower (0x336) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: max rated power. Ethernet-side message DI_maxRatedPower of Drive inverter for Tesla Model 3 firmware 2025.20.8, 4 signals (DI_sysDrivePowerRated, DI_obdDriveCycleStatus, DI_performancePackage, DI_sysRegenPowerRated). Bit layout, scaling, units and value tables."
---

# DI_maxRatedPower (0x336) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: max rated power. This page documents the 4 signals of DI_maxRatedPower as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_maxRatedPower` |
| Ethernet-side id | 0x336 (822) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of DI_maxRatedPower

Tesla Model 3 CAN bus signals in `DI_maxRatedPower`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_sysDrivePowerRated` | Drive inverter: sys drive power rated; raw 511 = signal not available (SNA) | 0\|10 | little-endian | unsigned | 1 | 0 | kW | 0 to 1023 | 511 = `SNA` | plausible |
| `DI_obdDriveCycleStatus` | OBD qualified drive cycle status | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DI_performancePackage` | Drive inverter: performance package; raw 7 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `BASE`<br>1 = `PERFORMANCE`<br>2 = `BASE_2024`<br>3 = `BASE_PLUS`<br>4 = `BASE_2022`<br>5 = `BASE_PLUS_2022`<br>6 = `PERFORMANCE_2022`<br>7 = `SNA` | plausible |
| `DI_sysRegenPowerRated` | Drive inverter: sys regen power rated; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -100 | kW | -100 to 0 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
