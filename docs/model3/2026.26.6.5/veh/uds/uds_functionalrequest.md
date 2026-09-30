---
layout: default
title: "UDS_functionalRequest (0x7DF) — UDS ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "UDS ECU message: functional request. Tesla Model 3 CAN bus message UDS_functionalRequest (0x7DF) of UDS ECU, firmware 2026.26.6.5, 8 signals (UDS_functionalRequestData_0, UDS_functionalRequestData_1, UDS_functionalRequestData_2, UDS_functionalRequestData_3 and 4 more). Bit layout, scaling, units and value tables."
---

# UDS_functionalRequest (0x7DF) — UDS ECU, Tesla Model 3 2026.26.6.5 VEH CAN

UDS ECU message: functional request; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of UDS_functionalRequest as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UDS_functionalRequest` |
| CAN id | 0x7DF (2015) |
| ECU | [UDS ECU](../../uds.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of UDS_functionalRequest

Tesla Model 3 CAN bus signals in `UDS_functionalRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

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

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All UDS ECU messages (UDS)](../../uds.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
