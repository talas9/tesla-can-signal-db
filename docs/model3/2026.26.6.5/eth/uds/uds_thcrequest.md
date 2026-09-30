---
layout: default
title: "UDS_thcRequest (0x60F) — UDS ECU, Tesla Model 3 2026.26.6.5 ETH"
description: "UDS ECU message: thc request. Ethernet-side message UDS_thcRequest of UDS ECU for Tesla Model 3 firmware 2026.26.6.5, 2 signals (UDS_thcRequestData_H, UDS_thcRequestData_L). Bit layout, scaling, units and value tables."
---

# UDS_thcRequest (0x60F) — UDS ECU, Tesla Model 3 2026.26.6.5 ETH

UDS ECU message: thc request. This page documents the 2 signals of UDS_thcRequest as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_thcRequest` |
| Ethernet-side id | 0x60F (1551) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UDS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of UDS_thcRequest

Tesla Model 3 CAN bus signals in `UDS_thcRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_thcRequestData_H` | UDS ECU: thc request data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `UDS_thcRequestData_L` | UDS ECU: thc request data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
