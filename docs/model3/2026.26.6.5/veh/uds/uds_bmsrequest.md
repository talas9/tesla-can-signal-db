---
layout: default
title: "UDS_bmsRequest (0x602) — UDS ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "UDS ECU message: bms request. Tesla Model 3 CAN bus message UDS_bmsRequest (0x602) of UDS ECU, firmware 2026.26.6.5, 1 signals (UDS_bmsRequestData). Bit layout, scaling, units and value tables."
---

# UDS_bmsRequest (0x602) — UDS ECU, Tesla Model 3 2026.26.6.5 VEH CAN

UDS ECU message: bms request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of UDS_bmsRequest as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_bmsRequest` |
| CAN id | 0x602 (1538) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of UDS_bmsRequest

Tesla Model 3 CAN bus signals in `UDS_bmsRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UDS_bmsRequestData` | UDS ECU: bms request data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
