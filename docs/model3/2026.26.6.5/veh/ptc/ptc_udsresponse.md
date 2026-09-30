---
layout: default
title: "PTC_udsResponse (0x6D6) — Cabin heater, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Cabin heater message: uds response. Tesla Model 3 CAN bus message PTC_udsResponse (0x6D6) of Cabin heater, firmware 2026.26.6.5, 1 signals (PTC_udsResponseData). Bit layout, scaling, units and value tables."
---

# PTC_udsResponse (0x6D6) — Cabin heater, Tesla Model 3 2026.26.6.5 VEH CAN

Cabin heater message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PTC_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PTC_udsResponse` |
| CAN id | 0x6D6 (1750) |
| ECU | [Cabin heater](../../ptc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PTC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PTC_udsResponse

Tesla Model 3 CAN bus signals in `PTC_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PTC_udsResponseData` | Cabin heater: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Cabin heater messages (PTC)](../../ptc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
