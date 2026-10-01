---
layout: default
title: "CMPD_udsResponse (0x617) — CMPD ECU, Tesla Model Y 2025.20.8 ETH"
description: "CMPD ECU message: uds response. Ethernet-side message CMPD_udsResponse of CMPD ECU for Tesla Model Y firmware 2025.20.8, 1 signals (CMPD_udsResponseData). Bit layout, scaling, units and value tables."
---

# CMPD_udsResponse (0x617) — CMPD ECU, Tesla Model Y 2025.20.8 ETH

CMPD ECU message: uds response. This page documents the 1 signals of CMPD_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CMPD_udsResponse` |
| Ethernet-side id | 0x617 (1559) |
| ECU | [CMPD ECU](../../cmpd.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CMPD |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of CMPD_udsResponse

Tesla Model Y CAN bus signals in `CMPD_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CMPD_udsResponseData` | CMPD ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All CMPD ECU messages (CMPD)](../../cmpd.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
