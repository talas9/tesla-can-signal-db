---
layout: default
title: "EPAS3P_udsResponseCH (0x638) — Electric power steering (primary), Tesla Model 3 2025.20.8 ETH"
description: "Electric power steering (primary) message: uds response CH. Ethernet-side message EPAS3P_udsResponseCH of Electric power steering (primary) for Tesla Model 3 firmware 2025.20.8, 1 signals (EPAS3P_udsResponseDataCH). Bit layout, scaling, units and value tables."
---

# EPAS3P_udsResponseCH (0x638) — Electric power steering (primary), Tesla Model 3 2025.20.8 ETH

Electric power steering (primary) message: uds response CH. This page documents the 1 signals of EPAS3P_udsResponseCH as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3P_udsResponseCH` |
| Ethernet-side id | 0x638 (1592) |
| ECU | [Electric power steering (primary)](../../epas3p.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPAS3P |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of EPAS3P_udsResponseCH

Tesla Model 3 CAN bus signals in `EPAS3P_udsResponseCH`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3P_udsResponseDataCH` | Electric power steering (primary): uds response data CH | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric power steering (primary) messages (EPAS3P)](../../epas3p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
