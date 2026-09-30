---
layout: default
title: "UDS_epbrRequest (0x626) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "UDS ECU message: epbr request. Tesla Model Y CAN bus message UDS_epbrRequest (0x626) of UDS ECU, firmware 2026.26.6.5, 2 signals (UDS_epbrRequestData_H, UDS_epbrRequestData_L). Bit layout, scaling, units and value tables."
---

# UDS_epbrRequest (0x626) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN

UDS ECU message: epbr request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of UDS_epbrRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_epbrRequest` |
| CAN id | 0x626 (1574) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of UDS_epbrRequest

Tesla Model Y CAN bus signals in `UDS_epbrRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_epbrRequestData_H` | UDS ECU: epbr request data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `UDS_epbrRequestData_L` | UDS ECU: epbr request data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
