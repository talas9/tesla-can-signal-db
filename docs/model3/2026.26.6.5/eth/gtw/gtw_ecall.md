---
layout: default
title: "GTW_ECall (0x378) — Gateway, Tesla Model 3 2026.26.6.5 ETH"
description: "Gateway message: e call. Ethernet-side message GTW_ECall of Gateway for Tesla Model 3 firmware 2026.26.6.5, 2 signals (GTW_GTW_SOS_ECALL_RQST, GTW_LTE_ECALL_LOCK). Bit layout, scaling, units and value tables."
---

# GTW_ECall (0x378) — Gateway, Tesla Model 3 2026.26.6.5 ETH

Gateway message: e call. This page documents the 2 signals of GTW_ECall as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_ECall` |
| Ethernet-side id | 0x378 (888) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of GTW_ECall

Tesla Model 3 CAN bus signals in `GTW_ECall`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_GTW_SOS_ECALL_RQST` | State of the GTW-SOS-ECALL-RQST pin | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_LTE_ECALL_LOCK` | State of the LTE-ECALL-LOCK pin | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
