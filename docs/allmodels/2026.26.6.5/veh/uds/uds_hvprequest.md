---
layout: default
title: "UDS_hvpRequest (0x610) — UDS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "UDS ECU message: hvp request. Tesla Model 3 / Model Y CAN bus message UDS_hvpRequest (0x610) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_hvpRequestData). Bit layout, scaling, units and value tables."
---

# UDS_hvpRequest (0x610) — UDS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

UDS ECU message: hvp request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_hvpRequest as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_hvpRequest` |
| CAN id | 0x610 (1552) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_hvpRequest

Tesla Model 3 / Model Y CAN bus signals in `UDS_hvpRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_hvpRequestData` | UDS ECU: hvp request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
