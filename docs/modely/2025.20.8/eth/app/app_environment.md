---
layout: default
title: "APP_environment (0x25B) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: environment. Ethernet-side message APP_environment of Driver assistance computer (primary) for Tesla Model Y firmware 2025.20.8, 2 signals (APP_environmentRainy, APP_environmentSnowy). Bit layout, scaling, units and value tables."
---

# APP_environment (0x25B) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: environment. This page documents the 2 signals of APP_environment as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_environment` |
| Ethernet-side id | 0x25B (603) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of APP_environment

Tesla Model Y CAN bus signals in `APP_environment`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_environmentRainy` | Driver assistance computer (primary): environment rainy | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_environmentSnowy` | Driver assistance computer (primary): environment snowy | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
