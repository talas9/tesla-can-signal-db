---
layout: default
title: "DI_estimatedBrakeTemp (0x3FE) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: estimated brake temp. Tesla Model 3 / Model Y CAN bus message DI_estimatedBrakeTemp (0x3FE) of Drive inverter, firmware 2026.26.6.5, 8 signals (DI_estimatedBrakeTempChecksum, DI_estimatedBrakeTempCounter, DI_brakeFLTemp, DI_brakeFRTemp and 4 more). Bit layout, scaling, units and value tables."
---

# DI_estimatedBrakeTemp (0x3FE) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Drive inverter message: estimated brake temp; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of DI_estimatedBrakeTemp as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_estimatedBrakeTemp` |
| CAN id | 0x3FE (1022) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of DI_estimatedBrakeTemp

Tesla Model 3 / Model Y CAN bus signals in `DI_estimatedBrakeTemp`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_estimatedBrakeTempChecksum` | Drive inverter: estimated brake temp checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DI_estimatedBrakeTempCounter` | Drive inverter: estimated brake temp counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_brakeFLTemp` | Drive inverter: brake FL temp; raw 1023 = signal not available (SNA) | 12\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | validated |
| `DI_brakeFRTemp` | Drive inverter: brake FR temp; raw 1023 = signal not available (SNA) | 22\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | validated |
| `DI_brakeRLTemp` | Drive inverter: brake RL temp; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | validated |
| `DI_brakeRRTemp` | Drive inverter: brake RR temp; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | validated |
| `DI_mcpIndex` | Brake master cylinder pressure index | 52\|5 | little-endian | signed | 0.05 | 0.75 | ratio | -0.05 to 1.5 |  | validated |
| `DI_mcpIndexPrimeFilt` | Filtered brake master cylinder pressure index prime | 57\|7 | little-endian | signed | 0.015 | 0.9 | ratio | -0.05 to 1.84 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
