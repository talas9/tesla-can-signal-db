---
layout: default
title: "UDS_dasRequest (0x649) — UDS ECU, Tesla Model Y 2026.26.6.5 CH CAN"
description: "UDS ECU message: das request. Tesla Model Y CAN bus message UDS_dasRequest (0x649) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_dasRequestData). Bit layout, scaling, units and value tables."
---

# UDS_dasRequest (0x649) — UDS ECU, Tesla Model Y 2026.26.6.5 CH CAN

UDS ECU message: das request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_dasRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_dasRequest` |
| CAN id | 0x649 (1609) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_dasRequest

Tesla Model Y CAN bus signals in `UDS_dasRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_dasRequestData` | UDS ECU: das request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
