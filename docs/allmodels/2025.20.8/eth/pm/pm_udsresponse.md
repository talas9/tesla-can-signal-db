---
layout: default
title: "PM_udsResponse (0x640) — PM ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "PM ECU message: uds response. Ethernet-side message PM_udsResponse of PM ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (PM_udsResponseData). Bit layout, scaling, units and value tables."
---

# PM_udsResponse (0x640) — PM ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

PM ECU message: uds response. This page documents the 1 signals of PM_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PM_udsResponse` |
| Ethernet-side id | 0x640 (1600) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PM_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `PM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_udsResponseData` | PM ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
