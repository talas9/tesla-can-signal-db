---
layout: default
title: "VC_LVBMS_brickMeasurements (0x73A) — VC ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "VC ECU message: LVBMS brick measurements. Tesla Model Y CAN bus message VC_LVBMS_brickMeasurements (0x73A) of VC ECU, firmware 2025.20.8, 13 signals (VC_LVBMS_brickMeasurementsMultiplexer, VC_LVBMS_brickVoltage1, VC_LVBMS_brickVoltage2, VC_LVBMS_brickVoltage3 and 9 more). Bit layout, scaling, units and value tables."
---

# VC_LVBMS_brickMeasurements (0x73A) — VC ECU, Tesla Model Y 2025.20.8 VEH CAN

VC ECU message: LVBMS brick measurements; frame length observed on a vehicle bus. This page documents the 13 signals of VC_LVBMS_brickMeasurements as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VC_LVBMS_brickMeasurements` |
| CAN id | 0x73A (1850) |
| ECU | [VC ECU](../../vc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 13 |

## Signals of VC_LVBMS_brickMeasurements

Tesla Model Y CAN bus signals in `VC_LVBMS_brickMeasurements`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_LVBMS_brickMeasurementsMultiplexer` | selector | VC ECU: LVBMS brick measurements multiplexer | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2` | plausible |
| `VC_LVBMS_brickVoltage1` | page 0 | Voltage of a low voltage battery brick; raw 8191 = signal not available (SNA) | 8\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 6.535 | 8191 = `SNA` | plausible |
| `VC_LVBMS_brickVoltage2` | page 0 | Voltage of a low voltage battery brick; raw 8191 = signal not available (SNA) | 24\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 6.535 | 8191 = `SNA` | plausible |
| `VC_LVBMS_brickVoltage3` | page 0 | Voltage of a low voltage battery brick; raw 8191 = signal not available (SNA) | 37\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 6.535 | 8191 = `SNA` | plausible |
| `VC_LVBMS_brickVoltage4` | page 0 | Voltage of a low voltage battery brick; raw 8191 = signal not available (SNA) | 50\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 6.535 | 8191 = `SNA` | plausible |
| `VC_LVBMS_brickBalancingAh1` | page 1 | Ah count of a low voltage battery brick; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 16777.214 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_brickBalancingAh2` | page 1 | Ah count of a low voltage battery brick; raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 16777.214 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_brickBalancingState1` | page 1 | VC ECU: LVBMS brick balancing state1 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_BALANCING_STATE_INACTIVE`<br>1 = `LVBMS_BALANCING_STATE_ACTIVE` | plausible |
| `VC_LVBMS_brickBalancingState2` | page 1 | VC ECU: LVBMS brick balancing state2 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_BALANCING_STATE_INACTIVE`<br>1 = `LVBMS_BALANCING_STATE_ACTIVE` | plausible |
| `VC_LVBMS_brickBalancingAh3` | page 2 | Ah count of a low voltage battery brick; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 16777.214 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_brickBalancingAh4` | page 2 | Ah count of a low voltage battery brick; raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 16777.214 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_brickBalancingState3` | page 2 | VC ECU: LVBMS brick balancing state3 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_BALANCING_STATE_INACTIVE`<br>1 = `LVBMS_BALANCING_STATE_ACTIVE` | plausible |
| `VC_LVBMS_brickBalancingState4` | page 2 | VC ECU: LVBMS brick balancing state4 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_BALANCING_STATE_INACTIVE`<br>1 = `LVBMS_BALANCING_STATE_ACTIVE` | plausible |

## Multiplexing

`VC_LVBMS_brickMeasurementsMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (4 signals), page 2 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All VC ECU messages (VC)](../../vc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
