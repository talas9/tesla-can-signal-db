---
layout: default
title: "IBST_udsResponse (0x65D) — Electric brake booster, Tesla Model 3 2025.20.8 ETH"
description: "Electric brake booster message: uds response. Ethernet-side message IBST_udsResponse of Electric brake booster for Tesla Model 3 firmware 2025.20.8, 1 signals (IBST_udsResponseData). Bit layout, scaling, units and value tables."
---

# IBST_udsResponse (0x65D) — Electric brake booster, Tesla Model 3 2025.20.8 ETH

Electric brake booster message: uds response. This page documents the 1 signals of IBST_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `IBST_udsResponse` |
| Ethernet-side id | 0x65D (1629) |
| ECU | [Electric brake booster](../../ibst.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | IBST |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of IBST_udsResponse

Tesla Model 3 CAN bus signals in `IBST_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `IBST_udsResponseData` | Electric brake booster: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric brake booster messages (IBST)](../../ibst.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
