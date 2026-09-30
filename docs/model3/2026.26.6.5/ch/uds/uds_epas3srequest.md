---
layout: default
title: "UDS_epas3sRequest (0x730) — UDS ECU, Tesla Model 3 2026.26.6.5 CH CAN"
description: "UDS ECU message: epas3s request. Tesla Model 3 CAN bus message UDS_epas3sRequest (0x730) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_epas3sRequestData). Bit layout, scaling, units and value tables."
---

# UDS_epas3sRequest (0x730) — UDS ECU, Tesla Model 3 2026.26.6.5 CH CAN

UDS ECU message: epas3s request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_epas3sRequest as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_epas3sRequest` |
| CAN id | 0x730 (1840) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_epas3sRequest

Tesla Model 3 CAN bus signals in `UDS_epas3sRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_epas3sRequestData` | UDS ECU: epas3s request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
