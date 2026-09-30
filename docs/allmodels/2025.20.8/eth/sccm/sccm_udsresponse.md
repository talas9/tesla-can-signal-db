---
layout: default
title: "SCCM_udsResponse (0x690) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Steering column control module message: uds response. Ethernet-side message SCCM_udsResponse of Steering column control module for Tesla Model 3 / Model Y firmware 2025.20.8, 8 signals (SCCM_functionalResponseData_0, SCCM_functionalResponseData_1, SCCM_functionalResponseData_2, SCCM_functionalResponseData_3 and 4 more). Bit layout, scaling, units and value tables."
---

# SCCM_udsResponse (0x690) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 ETH

Steering column control module message: uds response. This page documents the 8 signals of SCCM_udsResponse as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_udsResponse` |
| Ethernet-side id | 0x690 (1680) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of SCCM_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `SCCM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_functionalResponseData_0` | Steering column control module: functional response data 0 | 7\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_1` | Steering column control module: functional response data 1 | 15\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_2` | Steering column control module: functional response data 2 | 23\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_3` | Steering column control module: functional response data 3 | 31\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_4` | Steering column control module: functional response data 4 | 39\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_5` | Steering column control module: functional response data 5 | 47\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_6` | Steering column control module: functional response data 6 | 55\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_7` | Steering column control module: functional response data 7 | 63\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
