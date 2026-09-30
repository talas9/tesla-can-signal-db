---
layout: default
title: "UDS_vcbatt1Request (0x60C) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "UDS ECU message: vcbatt1 request. Tesla Model Y CAN bus message UDS_vcbatt1Request (0x60C) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_vcbatt1RequestData). Bit layout, scaling, units and value tables."
---

# UDS_vcbatt1Request (0x60C) — UDS ECU, Tesla Model Y 2026.26.6.5 VEH CAN

UDS ECU message: vcbatt1 request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_vcbatt1Request as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_vcbatt1Request` |
| CAN id | 0x60C (1548) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_vcbatt1Request

Tesla Model Y CAN bus signals in `UDS_vcbatt1Request`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_vcbatt1RequestData` | UDS ECU: vcbatt1 request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
