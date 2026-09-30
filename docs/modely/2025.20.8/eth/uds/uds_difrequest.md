---
layout: default
title: "UDS_difRequest (0x605) — UDS ECU, Tesla Model Y 2025.20.8 ETH"
description: "UDS ECU message: dif request. Ethernet-side message UDS_difRequest of UDS ECU for Tesla Model Y firmware 2025.20.8, 1 signals (UDS_difRequestData). Bit layout, scaling, units and value tables."
---

# UDS_difRequest (0x605) — UDS ECU, Tesla Model Y 2025.20.8 ETH

UDS ECU message: dif request. This page documents the 1 signals of UDS_difRequest as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_difRequest` |
| Ethernet-side id | 0x605 (1541) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_difRequest

Tesla Model Y CAN bus signals in `UDS_difRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_difRequestData` | UDS ECU: dif request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
