---
layout: default
title: "GTW_hrlExternalEvent (0x7EA) — Gateway, Tesla Model 3 2026.26.6.5 ETH"
description: "Gateway message: hrl external event. Ethernet-side message GTW_hrlExternalEvent of Gateway for Tesla Model 3 firmware 2026.26.6.5, 2 signals (GTW_hrlEventStartEpoch, GTW_hrlEventEndEpoch). Bit layout, scaling, units and value tables."
---

# GTW_hrlExternalEvent (0x7EA) — Gateway, Tesla Model 3 2026.26.6.5 ETH

Gateway message: hrl external event. This page documents the 2 signals of GTW_hrlExternalEvent as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_hrlExternalEvent` |
| Ethernet-side id | 0x7EA (2026) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of GTW_hrlExternalEvent

Tesla Model 3 CAN bus signals in `GTW_hrlExternalEvent`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_hrlEventStartEpoch` | Gateway: hrl event start epoch | 7\|32 | big-endian | unsigned | 1 | 0 | seconds | 0 to 4294967295 |  | plausible |
| `GTW_hrlEventEndEpoch` | Gateway: hrl event end epoch | 39\|32 | big-endian | unsigned | 1 | 0 | seconds | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
