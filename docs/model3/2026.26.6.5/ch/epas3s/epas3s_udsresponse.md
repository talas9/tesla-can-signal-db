---
layout: default
title: "EPAS3S_udsResponse (0x738) — Electric power steering (secondary), Tesla Model 3 2026.26.6.5 CH CAN"
description: "Electric power steering (secondary) message: uds response. Tesla Model 3 CAN bus message EPAS3S_udsResponse (0x738) of Electric power steering (secondary), firmware 2026.26.6.5, 1 signals (EPAS3S_udsResponseData). Bit layout, scaling, units and value tables."
---

# EPAS3S_udsResponse (0x738) — Electric power steering (secondary), Tesla Model 3 2026.26.6.5 CH CAN

Electric power steering (secondary) message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of EPAS3S_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3S_udsResponse` |
| CAN id | 0x738 (1848) |
| ECU | [Electric power steering (secondary)](../../epas3s.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | EPAS3S |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of EPAS3S_udsResponse

Tesla Model 3 CAN bus signals in `EPAS3S_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3S_udsResponseData` | Electric power steering (secondary): uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Electric power steering (secondary) messages (EPAS3S)](../../epas3s.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
