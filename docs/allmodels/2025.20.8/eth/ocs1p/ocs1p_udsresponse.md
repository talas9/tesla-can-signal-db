---
layout: default
title: "OCS1P_udsResponse (0x653) — Occupant classification system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Occupant classification system message: uds response. Ethernet-side message OCS1P_udsResponse of Occupant classification system for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (OCS1P_udsResponseData). Bit layout, scaling, units and value tables."
---

# OCS1P_udsResponse (0x653) — Occupant classification system, Tesla Model 3 / Model Y 2025.20.8 ETH

Occupant classification system message: uds response. This page documents the 1 signals of OCS1P_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `OCS1P_udsResponse` |
| Ethernet-side id | 0x653 (1619) |
| ECU | [Occupant classification system](../../ocs1p.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | OCS1P |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of OCS1P_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `OCS1P_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `OCS1P_udsResponseData` | Occupant classification system: uds response data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Occupant classification system messages (OCS1P)](../../ocs1p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
