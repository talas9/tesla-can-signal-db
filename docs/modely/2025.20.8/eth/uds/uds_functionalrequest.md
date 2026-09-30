---
layout: default
title: "UDS_functionalRequest (0x7DF) — UDS ECU, Tesla Model Y 2025.20.8 ETH"
description: "UDS ECU message: functional request. Ethernet-side message UDS_functionalRequest of UDS ECU for Tesla Model Y firmware 2025.20.8, 8 signals (UDS_functionalRequestData_0, UDS_functionalRequestData_1, UDS_functionalRequestData_2, UDS_functionalRequestData_3 and 4 more). Bit layout, scaling, units and value tables."
---

# UDS_functionalRequest (0x7DF) — UDS ECU, Tesla Model Y 2025.20.8 ETH

UDS ECU message: functional request. This page documents the 8 signals of UDS_functionalRequest as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_functionalRequest` |
| Ethernet-side id | 0x7DF (2015) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of UDS_functionalRequest

Tesla Model Y CAN bus signals in `UDS_functionalRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_functionalRequestData_0` | UDS ECU: functional request data 0 | 7\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_1` | UDS ECU: functional request data 1 | 15\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_2` | UDS ECU: functional request data 2 | 23\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_3` | UDS ECU: functional request data 3 | 31\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_4` | UDS ECU: functional request data 4 | 39\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_5` | UDS ECU: functional request data 5 | 47\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_6` | UDS ECU: functional request data 6 | 55\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UDS_functionalRequestData_7` | UDS ECU: functional request data 7 | 63\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
