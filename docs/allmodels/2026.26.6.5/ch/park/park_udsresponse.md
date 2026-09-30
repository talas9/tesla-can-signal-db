---
layout: default
title: "PARK_udsResponse (0x65E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: uds response. Tesla Model 3 / Model Y CAN bus message PARK_udsResponse (0x65E) of Parking assist sensors, firmware 2026.26.6.5, 1 signals (PARK_udsResponseData). Bit layout, scaling, units and value tables."
---

# PARK_udsResponse (0x65E) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PARK_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_udsResponse` |
| CAN id | 0x65E (1630) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PARK_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `PARK_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_udsResponseData` | Parking assist sensors: uds response data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
