---
layout: default
title: "UDS_epblRequest (0x624) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "UDS ECU message: epbl request. Ethernet-side message UDS_epblRequest of UDS ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (UDS_epblRequestData_H, UDS_epblRequestData_L). Bit layout, scaling, units and value tables."
---

# UDS_epblRequest (0x624) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

UDS ECU message: epbl request. This page documents the 2 signals of UDS_epblRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_epblRequest` |
| Ethernet-side id | 0x624 (1572) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of UDS_epblRequest

Tesla Model 3 / Model Y CAN bus signals in `UDS_epblRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_epblRequestData_H` | UDS ECU: epbl request data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `UDS_epblRequestData_L` | UDS ECU: epbl request data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
