---
layout: default
title: "DIR_udsResponse (0x616) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Rear drive inverter message: uds response. Ethernet-side message DIR_udsResponse of Rear drive inverter for Tesla Model 3 firmware 2025.20.8, 1 signals (DIR_udsResponseData). Bit layout, scaling, units and value tables."
---

# DIR_udsResponse (0x616) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH

Rear drive inverter message: uds response. This page documents the 1 signals of DIR_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_udsResponse` |
| Ethernet-side id | 0x616 (1558) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of DIR_udsResponse

Tesla Model 3 CAN bus signals in `DIR_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_udsResponseData` | Rear drive inverter: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
