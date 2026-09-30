---
layout: default
title: "VCFRONT_udsResponse (0x601) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: uds response. Tesla Model Y CAN bus message VCFRONT_udsResponse (0x601) of Front body controller, firmware 2026.26.6.5, 1 signals (VCFRONT_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCFRONT_udsResponse (0x601) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCFRONT_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_udsResponse` |
| CAN id | 0x601 (1537) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCFRONT_udsResponse

Tesla Model Y CAN bus signals in `VCFRONT_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_udsResponseData` | Front body controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
