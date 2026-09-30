---
layout: default
title: "VCSEC_udsResponse (0x7D8) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH"
description: "Vehicle security controller message: uds response. Ethernet-side message VCSEC_udsResponse of Vehicle security controller for Tesla Model Y firmware 2025.20.8, 1 signals (VCSEC_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCSEC_udsResponse (0x7D8) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH

Vehicle security controller message: uds response. This page documents the 1 signals of VCSEC_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_udsResponse` |
| Ethernet-side id | 0x7D8 (2008) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCSEC_udsResponse

Tesla Model Y CAN bus signals in `VCSEC_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_udsResponseData` | Vehicle security controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
