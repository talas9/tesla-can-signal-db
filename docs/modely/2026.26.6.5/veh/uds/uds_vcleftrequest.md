---
layout: default
title: "UDS_vcleftRequest (0x622) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "UDS ECU message: vcleft request. Tesla Model Y CAN bus message UDS_vcleftRequest (0x622) of UDS ECU, firmware 2026.26.6.5, 2 signals (UDS_vcleftRequestData_H, UDS_vcleftRequestData_L). Bit layout, scaling, units and value tables."
---

# UDS_vcleftRequest (0x622) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN

UDS ECU message: vcleft request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of UDS_vcleftRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_vcleftRequest` |
| CAN id | 0x622 (1570) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of UDS_vcleftRequest

Tesla Model Y CAN bus signals in `UDS_vcleftRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_vcleftRequestData_H` | UDS ECU: vcleft request data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `UDS_vcleftRequestData_L` | UDS ECU: vcleft request data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
