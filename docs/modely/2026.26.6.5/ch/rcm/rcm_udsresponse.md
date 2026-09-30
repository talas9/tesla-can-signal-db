---
layout: default
title: "RCM_udsResponse (0x651) — Restraint control module, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Restraint control module message: uds response. Tesla Model Y CAN bus message RCM_udsResponse (0x651) of Restraint control module, firmware 2026.26.6.5, 1 signals (RCM_udsResponseData). Bit layout, scaling, units and value tables."
---

# RCM_udsResponse (0x651) — Restraint control module, Tesla Model Y 2026.26.6.5 CH CAN

Restraint control module message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of RCM_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_udsResponse` |
| CAN id | 0x651 (1617) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of RCM_udsResponse

Tesla Model Y CAN bus signals in `RCM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_udsResponseData` | Restraint control module: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
