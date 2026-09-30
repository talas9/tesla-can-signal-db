---
layout: default
title: "TAS_axleData (0x20B) — Air suspension controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Air suspension controller message: axle data. Tesla Model 3 / Model Y CAN bus message TAS_axleData (0x20B) of Air suspension controller, firmware 2026.26.6.5, 13 signals (TAS_axleIndex, TAS_rawHeightFL, TAS_staticHeightEstimateFL, TAS_componentPressureFL and 9 more). Bit layout, scaling, units and value tables."
---

# TAS_axleData (0x20B) — Air suspension controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Air suspension controller message: axle data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of TAS_axleData as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_axleData` |
| CAN id | 0x20B (523) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 13 |

## Signals of TAS_axleData

Tesla Model 3 / Model Y CAN bus signals in `TAS_axleData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_axleIndex` | selector | Air suspension controller: axle index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `axleFront`<br>1 = `axleRear` | plausible |
| `TAS_rawHeightFL` | page 0 | Current height of the FL air spring; raw 1023 = signal not available (SNA) | 4\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_staticHeightEstimateFL` | page 0 | Current static height estimate of the FL air spring; raw 1023 = signal not available (SNA) | 14\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_componentPressureFL` | page 0 | Current static pressure of the FL air spring; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | validated |
| `TAS_rawHeightFR` | page 0 | Current height of the FR air spring; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_staticHeightEstimateFR` | page 0 | Current static height estimate of the FR air spring; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_componentPressureFR` | page 0 | Current static pressure of the FR air spring; raw 255 = signal not available (SNA) | 52\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | validated |
| `TAS_rawHeightRL` | page 1 | Current height of the RL air spring; raw 1023 = signal not available (SNA) | 4\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_staticHeightEstimateRL` | page 1 | Current static height estimate of the RL air spring; raw 1023 = signal not available (SNA) | 14\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_componentPressureRL` | page 1 | Current static pressure of the RL air spring; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | validated |
| `TAS_rawHeightRR` | page 1 | Current height of the RR air spring; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_staticHeightEstimateRR` | page 1 | Current static height estimate of the RR air spring; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 1 | -512 | mm | -512 to 510 | 1023 = `SNA` | validated |
| `TAS_componentPressureRR` | page 1 | Current static pressure of the RR air spring; raw 255 = signal not available (SNA) | 52\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | validated |

## Multiplexing

`TAS_axleIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
