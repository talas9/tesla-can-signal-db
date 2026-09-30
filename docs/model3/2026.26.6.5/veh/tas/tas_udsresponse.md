---
layout: default
title: "TAS_udsResponse (0x65B) — Air suspension controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Air suspension controller message: uds response. Tesla Model 3 CAN bus message TAS_udsResponse (0x65B) of Air suspension controller, firmware 2026.26.6.5, 1 signals (TAS_udsResponseData). Bit layout, scaling, units and value tables."
---

# TAS_udsResponse (0x65B) — Air suspension controller, Tesla Model 3 2026.26.6.5 VEH CAN

Air suspension controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of TAS_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_udsResponse` |
| CAN id | 0x65B (1627) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of TAS_udsResponse

Tesla Model 3 CAN bus signals in `TAS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_udsResponseData` | Air suspension controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
