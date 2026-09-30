---
layout: default
title: "HVP_udsResponse (0x611) — High-voltage processor (pack contactor and isolation controller), Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: uds response. Tesla Model Y CAN bus message HVP_udsResponse (0x611) of High-voltage processor (pack contactor and isolation controller), firmware 2026.26.6.5, 1 signals (HVP_udsResponseData). Bit layout, scaling, units and value tables."
---

# HVP_udsResponse (0x611) — High-voltage processor (pack contactor and isolation controller), Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of HVP_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_udsResponse` |
| CAN id | 0x611 (1553) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of HVP_udsResponse

Tesla Model Y CAN bus signals in `HVP_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_udsResponseData` | High-voltage processor (pack contactor and isolation controller): uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
