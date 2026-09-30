---
layout: default
title: "FC_maxLimits (0x541) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: max limits. Tesla Model 3 CAN bus message FC_maxLimits (0x541) of FC ECU, firmware 2025.20.8, 2 signals (FC_maxPowerLimit, FC_maxCurrentLimit). Bit layout, scaling, units and value tables."
---

# FC_maxLimits (0x541) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: max limits; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of FC_maxLimits as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_maxLimits` |
| CAN id | 0x541 (1345) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 2 |

## Signals of FC_maxLimits

Tesla Model 3 CAN bus signals in `FC_maxLimits`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_maxPowerLimit` | Max power charger can deliver; raw 8191 = signal not available (SNA) | 0\|13 | little-endian | unsigned | 0.06225586 | 0 | kW | 0 to 509.8754934 | 8191 = `SNA` | validated |
| `FC_maxCurrentLimit` | Max current charger can deliver; raw 8191 = signal not available (SNA) | 16\|13 | little-endian | unsigned | 0.07324219 | 0 | A | 0 to 599.8535361 | 8191 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
