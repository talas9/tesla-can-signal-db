---
layout: default
title: "VCFRONT_udsResponse (0x601) — Front body controller, Tesla Model Y 2025.20.8 ETH"
description: "Front body controller message: uds response. Ethernet-side message VCFRONT_udsResponse of Front body controller for Tesla Model Y firmware 2025.20.8, 1 signals (VCFRONT_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCFRONT_udsResponse (0x601) — Front body controller, Tesla Model Y 2025.20.8 ETH

Front body controller message: uds response. This page documents the 1 signals of VCFRONT_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_udsResponse` |
| Ethernet-side id | 0x601 (1537) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
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

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
