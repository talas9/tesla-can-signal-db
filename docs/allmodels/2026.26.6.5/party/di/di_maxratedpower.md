---
layout: default
title: "DI_maxRatedPower (0x336) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Drive inverter message: max rated power. Tesla Model 3 / Model Y CAN bus message DI_maxRatedPower (0x336) of Drive inverter, firmware 2026.26.6.5, 3 signals (DI_sysDrivePowerRated, DI_performancePackage, DI_sysRegenPowerRated). Bit layout, scaling, units and value tables."
---

# DI_maxRatedPower (0x336) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Drive inverter message: max rated power; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of DI_maxRatedPower as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_maxRatedPower` |
| CAN id | 0x336 (822) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of DI_maxRatedPower

Tesla Model 3 / Model Y CAN bus signals in `DI_maxRatedPower`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_sysDrivePowerRated` | Drive inverter: sys drive power rated; raw 511 = signal not available (SNA) | 0\|10 | little-endian | unsigned | 1 | 0 | kW | 0 to 1023 | 511 = `SNA` | plausible |
| `DI_performancePackage` | Drive inverter: performance package; raw 7 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `BASE`<br>1 = `PERFORMANCE`<br>2 = `BASE_2024`<br>3 = `BASE_PLUS`<br>4 = `BASE_2022`<br>5 = `BASE_PLUS_2022`<br>6 = `PERFORMANCE_2022`<br>7 = `SNA` | plausible |
| `DI_sysRegenPowerRated` | Drive inverter: sys regen power rated; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -100 | kW | -100 to 0 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
