---
layout: default
title: "DAS_udsResponse (0x659) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: uds response. Tesla Model 3 CAN bus message DAS_udsResponse (0x659) of Driver assistance computer, firmware 2026.26.6.5, 1 signals (DAS_udsResponseData). Bit layout, scaling, units and value tables."
---

# DAS_udsResponse (0x659) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of DAS_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_udsResponse` |
| CAN id | 0x659 (1625) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of DAS_udsResponse

Tesla Model 3 CAN bus signals in `DAS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_udsResponseData` | Driver assistance computer: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
