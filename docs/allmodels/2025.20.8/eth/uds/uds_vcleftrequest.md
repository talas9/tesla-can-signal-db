---
layout: default
title: "UDS_vcleftRequest (0x622) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "UDS ECU message: vcleft request. Ethernet-side message UDS_vcleftRequest of UDS ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (UDS_vcleftRequestData_H, UDS_vcleftRequestData_L). Bit layout, scaling, units and value tables."
---

# UDS_vcleftRequest (0x622) — UDS ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

UDS ECU message: vcleft request. This page documents the 2 signals of UDS_vcleftRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_vcleftRequest` |
| Ethernet-side id | 0x622 (1570) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of UDS_vcleftRequest

Tesla Model 3 / Model Y CAN bus signals in `UDS_vcleftRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_vcleftRequestData_H` | UDS ECU: vcleft request data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `UDS_vcleftRequestData_L` | UDS ECU: vcleft request data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
