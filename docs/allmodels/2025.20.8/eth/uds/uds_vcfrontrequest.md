---
layout: default
title: "UDS_vcfrontRequest (0x600) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "UDS ECU message: vcfront request. Ethernet-side message UDS_vcfrontRequest of UDS ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 1 signals (UDS_vcfrontRequestData). Bit layout, scaling, units and value tables."
---

# UDS_vcfrontRequest (0x600) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

UDS ECU message: vcfront request. This page documents the 1 signals of UDS_vcfrontRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_vcfrontRequest` |
| Ethernet-side id | 0x600 (1536) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_vcfrontRequest

Tesla Model 3 / Model Y CAN bus signals in `UDS_vcfrontRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_vcfrontRequestData` | UDS ECU: vcfront request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
