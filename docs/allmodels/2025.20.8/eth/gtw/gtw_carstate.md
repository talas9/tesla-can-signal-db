---
layout: default
title: "GTW_carState (0x318) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Gateway message: car state. Ethernet-side message GTW_carState of Gateway for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (GTW_factoryGated). Bit layout, scaling, units and value tables."
---

# GTW_carState (0x318) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH

Gateway message: car state. This page documents the 1 signals of GTW_carState as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_carState` |
| Ethernet-side id | 0x318 (792) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 1 |

## Signals of GTW_carState

Tesla Model 3 / Model Y CAN bus signals in `GTW_carState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_factoryGated` | Gateway: factory gated | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
