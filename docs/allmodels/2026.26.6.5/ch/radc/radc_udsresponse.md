---
layout: default
title: "RADC_udsResponse (0x681) — Radar, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Radar message: uds response. Tesla Model 3 / Model Y CAN bus message RADC_udsResponse (0x681) of Radar, firmware 2026.26.6.5, 1 signals (RADC_udsResponseData). Bit layout, scaling, units and value tables."
---

# RADC_udsResponse (0x681) — Radar, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Radar message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of RADC_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RADC_udsResponse` |
| CAN id | 0x681 (1665) |
| ECU | [Radar](../../radc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RADC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of RADC_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `RADC_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RADC_udsResponseData` | Radar: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Radar messages (RADC)](../../radc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
