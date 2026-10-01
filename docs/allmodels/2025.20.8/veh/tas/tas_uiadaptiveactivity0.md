---
layout: default
title: "TAS_uiAdaptiveActivity0 (0x199) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: ui adaptive activity0. Tesla Model 3 / Model Y CAN bus message TAS_uiAdaptiveActivity0 (0x199) of Air suspension controller, firmware 2025.20.8, 12 signals (TAS_adaptiveActivityFL_C, TAS_adaptiveActivityFL_R, TAS_adaptiveActivityFR_C, TAS_adaptiveActivityFR_R and 8 more). Bit layout, scaling, units and value tables."
---

# TAS_uiAdaptiveActivity0 (0x199) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Air suspension controller message: ui adaptive activity0; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of TAS_uiAdaptiveActivity0 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_uiAdaptiveActivity0` |
| CAN id | 0x199 (409) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 12 |

## Signals of TAS_uiAdaptiveActivity0

Tesla Model 3 / Model Y CAN bus signals in `TAS_uiAdaptiveActivity0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_adaptiveActivityFL_C` | Air suspension controller: adaptive activity FL c; raw 31 = signal not available (SNA) | 0\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityFL_R` | Air suspension controller: adaptive activity FL r; raw 31 = signal not available (SNA) | 5\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityFR_C` | Air suspension controller: adaptive activity FR c; raw 31 = signal not available (SNA) | 10\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityFR_R` | Air suspension controller: adaptive activity FR r; raw 31 = signal not available (SNA) | 15\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityRL_C` | Air suspension controller: adaptive activity RL c; raw 31 = signal not available (SNA) | 20\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityRL_R` | Air suspension controller: adaptive activity RL r; raw 31 = signal not available (SNA) | 25\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityRR_C` | Air suspension controller: adaptive activity RR c; raw 31 = signal not available (SNA) | 30\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_adaptiveActivityRR_R` | Air suspension controller: adaptive activity RR r; raw 31 = signal not available (SNA) | 35\|5 | little-endian | unsigned | 0.04 | 0 | - | 0 to 1 | 31 = `SNA` | plausible |
| `TAS_uiHeightFL` | Air suspension controller: ui height FL; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 4 | -128 | mm | -128 to 120 | 63 = `SNA` | plausible |
| `TAS_uiHeightFR` | Air suspension controller: ui height FR; raw 63 = signal not available (SNA) | 46\|6 | little-endian | unsigned | 4 | -128 | mm | -128 to 120 | 63 = `SNA` | plausible |
| `TAS_uiHeightRL` | Air suspension controller: ui height RL; raw 63 = signal not available (SNA) | 52\|6 | little-endian | unsigned | 4 | -128 | mm | -128 to 120 | 63 = `SNA` | plausible |
| `TAS_uiHeightRR` | Air suspension controller: ui height RR; raw 63 = signal not available (SNA) | 58\|6 | little-endian | unsigned | 4 | -128 | mm | -128 to 120 | 63 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
