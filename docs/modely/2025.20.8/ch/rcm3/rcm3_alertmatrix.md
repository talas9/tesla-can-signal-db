---
layout: default
title: "RCM3_alertMatrix (0x3F2) — RCM3 ECU, Tesla Model Y 2025.20.8 CH CAN"
description: "RCM3 ECU message: alert matrix. Tesla Model Y CAN bus message RCM3_alertMatrix (0x3F2) of RCM3 ECU, firmware 2025.20.8, 2 signals (RCM3_matrixIndex, RCM3_a001_LVPowerLossDetected). Bit layout, scaling, units and value tables."
---

# RCM3_alertMatrix (0x3F2) — RCM3 ECU, Tesla Model Y 2025.20.8 CH CAN

RCM3 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of RCM3_alertMatrix as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM3_alertMatrix` |
| CAN id | 0x3F2 (1010) |
| ECU | [RCM3 ECU](../../rcm3.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM3 |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of RCM3_alertMatrix

Tesla Model Y CAN bus signals in `RCM3_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCM3_matrixIndex` | selector | RCM3 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RCM3_AlertMatrix0` | plausible |
| `RCM3_a001_LVPowerLossDetected` | page 0 | RCM3 ECU: a001 LV power loss detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`RCM3_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All RCM3 ECU messages (RCM3)](../../rcm3.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
