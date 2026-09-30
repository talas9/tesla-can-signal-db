---
layout: default
title: "FC_limits (0x244) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: limits. Tesla Model 3 / Model Y CAN bus message FC_limits (0x244) of FC ECU, firmware 2026.26.6.5, 4 signals (FC_powerLimit, FC_currentLimit, FC_maxVoltageLimit, FC_minVoltageLimit). Bit layout, scaling, units and value tables."
---

# FC_limits (0x244) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

FC ECU message: limits; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of FC_limits as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_limits` |
| CAN id | 0x244 (580) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 4 |

## Signals of FC_limits

Tesla Model 3 / Model Y CAN bus signals in `FC_limits`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_powerLimit` | Instantaneous power charger can deliver; raw 8191 = signal not available (SNA) | 0\|13 | little-endian | unsigned | 0.06225586 | 0 | kW | 0 to 509.8754934 | 8191 = `SNA` | validated |
| `FC_currentLimit` | Instantaneous current charger can deliver; raw 8191 = signal not available (SNA) | 16\|13 | little-endian | unsigned | 0.07324219 | 0 | A | 0 to 599.8535361 | 8191 = `SNA` | validated |
| `FC_maxVoltageLimit` | Max voltage charger can deliver. 600/65536; raw 8191 = signal not available (SNA) | 32\|13 | little-endian | unsigned | 0.07324219 | 0 | V | 0 to 599.8535361 | 8191 = `SNA` | validated |
| `FC_minVoltageLimit` | Measures Electric Vehicle Supply Equipment (EVSE) minimum current limit; raw 8191 = signal not available (SNA) | 48\|13 | little-endian | unsigned | 0.07324219 | 0 | V | 0 to 599.8535361 | 8191 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
