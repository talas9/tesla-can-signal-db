---
layout: default
title: "TPMS_udsResponse (0x65F) — Tire pressure monitoring, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Tire pressure monitoring message: uds response. Tesla Model Y CAN bus message TPMS_udsResponse (0x65F) of Tire pressure monitoring, firmware 2026.26.6.5, 1 signals (TPMS_udsResponseData). Bit layout, scaling, units and value tables."
---

# TPMS_udsResponse (0x65F) — Tire pressure monitoring, Tesla Model Y 2026.26.6.5 CH CAN

Tire pressure monitoring message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of TPMS_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TPMS_udsResponse` |
| CAN id | 0x65F (1631) |
| ECU | [Tire pressure monitoring](../../tpms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TPMS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of TPMS_udsResponse

Tesla Model Y CAN bus signals in `TPMS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TPMS_udsResponseData` | Tire pressure monitoring: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Tire pressure monitoring messages (TPMS)](../../tpms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
