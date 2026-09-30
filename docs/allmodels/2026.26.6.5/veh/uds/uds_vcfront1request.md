---
layout: default
title: "UDS_vcfront1Request (0x62C) — UDS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "UDS ECU message: vcfront1 request. Tesla Model 3 / Model Y CAN bus message UDS_vcfront1Request (0x62C) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_vcfront1RequestData). Bit layout, scaling, units and value tables."
---

# UDS_vcfront1Request (0x62C) — UDS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

UDS ECU message: vcfront1 request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_vcfront1Request as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_vcfront1Request` |
| CAN id | 0x62C (1580) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_vcfront1Request

Tesla Model 3 / Model Y CAN bus signals in `UDS_vcfront1Request`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_vcfront1RequestData` | UDS ECU: vcfront1 request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
