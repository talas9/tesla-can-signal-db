---
layout: default
title: "VCRIGHT_hvacStatus2 (0x68B) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Right body controller message: hvac status2. Tesla Model 3 / Model Y CAN bus message VCRIGHT_hvacStatus2 (0x68B) of Right body controller, firmware 2025.20.8, 9 signals (VCRIGHT_hvacSeat1RLCushionFanTrgt, VCRIGHT_hvacSeat1RLBackrestFanTrgt, VCRIGHT_hvacSeat1RRCushionFanTrgt, VCRIGHT_hvacSeat1RRBackrestFanTrgt and 5 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_hvacStatus2 (0x68B) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Right body controller message: hvac status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of VCRIGHT_hvacStatus2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_hvacStatus2` |
| CAN id | 0x68B (1675) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of VCRIGHT_hvacStatus2

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_hvacStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_hvacSeat1RLCushionFanTrgt` | Right body controller: hvac seat1 RL cushion fan trgt | 0\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacSeat1RLBackrestFanTrgt` | Right body controller: hvac seat1 RL backrest fan trgt | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacSeat1RRCushionFanTrgt` | Right body controller: hvac seat1 RR cushion fan trgt | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacSeat1RRBackrestFanTrgt` | Right body controller: hvac seat1 RR backrest fan trgt | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvac2RActuatorsEnable` | Right body controller: hvac2 r actuators enable | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvac2RLeftLateralTarget` | Right body controller: hvac2 r left lateral target | 33\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvac2RLeftVerticalTarget` | Right body controller: hvac2 r left vertical target | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvac2RRightLateralTarget` | Right body controller: hvac2 r right lateral target | 48\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvac2RRightVerticalTarget` | Right body controller: hvac2 r right vertical target | 57\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
