---
layout: default
title: "EPAS3S_udsResponse (0x738) — Electric power steering (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Electric power steering (secondary) message: uds response. Ethernet-side message EPAS3S_udsResponse of Electric power steering (secondary) for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (EPAS3S_udsResponseData). Bit layout, scaling, units and value tables."
---

# EPAS3S_udsResponse (0x738) — Electric power steering (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH

Electric power steering (secondary) message: uds response. This page documents the 1 signals of EPAS3S_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3S_udsResponse` |
| Ethernet-side id | 0x738 (1848) |
| ECU | [Electric power steering (secondary)](../../epas3s.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPAS3S |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of EPAS3S_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `EPAS3S_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3S_udsResponseData` | Electric power steering (secondary): uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric power steering (secondary) messages (EPAS3S)](../../epas3s.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
