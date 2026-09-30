---
layout: default
title: "TAS_uiAdaptiveActivity1 (0x19A) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: ui adaptive activity1. Tesla Model 3 / Model Y CAN bus message TAS_uiAdaptiveActivity1 (0x19A) of Air suspension controller, firmware 2025.20.8, 4 signals (TAS_bodyAccelFL, TAS_bodyAccelFR, TAS_bodyAccelRL, TAS_bodyAccelRR). Bit layout, scaling, units and value tables."
---

# TAS_uiAdaptiveActivity1 (0x19A) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Air suspension controller message: ui adaptive activity1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of TAS_uiAdaptiveActivity1 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_uiAdaptiveActivity1` |
| CAN id | 0x19A (410) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 4 bytes |
| Cycle time | 50 ms |
| Signals | 4 |

## Signals of TAS_uiAdaptiveActivity1

Tesla Model 3 / Model Y CAN bus signals in `TAS_uiAdaptiveActivity1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_bodyAccelFL` | Air suspension controller: body accel FL; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.05 | -5 | g | -5 to 5 | 255 = `SNA` | validated |
| `TAS_bodyAccelFR` | Air suspension controller: body accel FR; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.05 | -5 | g | -5 to 5 | 255 = `SNA` | validated |
| `TAS_bodyAccelRL` | Air suspension controller: body accel RL; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.05 | -5 | g | -5 to 5 | 255 = `SNA` | validated |
| `TAS_bodyAccelRR` | Air suspension controller: body accel RR; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | -5 | g | -5 to 5 | 255 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
