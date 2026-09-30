---
layout: default
title: "TAS_udsResponse (0x65B) — Air suspension controller, Tesla Model Y 2025.20.8 ETH"
description: "Air suspension controller message: uds response. Ethernet-side message TAS_udsResponse of Air suspension controller for Tesla Model Y firmware 2025.20.8, 1 signals (TAS_udsResponseData). Bit layout, scaling, units and value tables."
---

# TAS_udsResponse (0x65B) — Air suspension controller, Tesla Model Y 2025.20.8 ETH

Air suspension controller message: uds response. This page documents the 1 signals of TAS_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_udsResponse` |
| Ethernet-side id | 0x65B (1627) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of TAS_udsResponse

Tesla Model Y CAN bus signals in `TAS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_udsResponseData` | Air suspension controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
