---
layout: default
title: "BMS_udsResponse (0x612) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: uds response. Ethernet-side message BMS_udsResponse of High-voltage battery management system for Tesla Model Y firmware 2025.20.8, 1 signals (BMS_udsResponseData). Bit layout, scaling, units and value tables."
---

# BMS_udsResponse (0x612) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH

High-voltage battery management system message: uds response. This page documents the 1 signals of BMS_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_udsResponse` |
| Ethernet-side id | 0x612 (1554) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of BMS_udsResponse

Tesla Model Y CAN bus signals in `BMS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_udsResponseData` | High-voltage battery management system: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
