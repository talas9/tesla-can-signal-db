---
layout: default
title: "IBST_udsResponse (0x65D) — Electric brake booster, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Electric brake booster message: uds response. Tesla Model 3 / Model Y CAN bus message IBST_udsResponse (0x65D) of Electric brake booster, firmware 2026.26.6.5, 1 signals (IBST_udsResponseData). Bit layout, scaling, units and value tables."
---

# IBST_udsResponse (0x65D) — Electric brake booster, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Electric brake booster message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of IBST_udsResponse as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `IBST_udsResponse` |
| CAN id | 0x65D (1629) |
| ECU | [Electric brake booster](../../ibst.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | IBST |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of IBST_udsResponse

Tesla Model 3 / Model Y CAN bus signals in `IBST_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `IBST_udsResponseData` | Electric brake booster: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Electric brake booster messages (IBST)](../../ibst.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
