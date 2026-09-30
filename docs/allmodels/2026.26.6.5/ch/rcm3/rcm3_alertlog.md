---
layout: default
title: "RCM3_alertLog (0x4E4) — RCM3 ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "RCM3 ECU message: alert log. Tesla Model 3 / Model Y CAN bus message RCM3_alertLog (0x4E4) of RCM3 ECU, firmware 2026.26.6.5, 2 signals (RCM3_alertID, RCM3_alertState). Bit layout, scaling, units and value tables."
---

# RCM3_alertLog (0x4E4) — RCM3 ECU, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

RCM3 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of RCM3_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM3_alertLog` |
| CAN id | 0x4E4 (1252) |
| ECU | [RCM3 ECU](../../rcm3.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM3 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of RCM3_alertLog

Tesla Model 3 / Model Y CAN bus signals in `RCM3_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM3_alertID` | RCM3 ECU: alert ID | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 1 = `RCM3_a001_LVPowerLossDetected` | plausible |
| `RCM3_alertState` | RCM3 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All RCM3 ECU messages (RCM3)](../../rcm3.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
