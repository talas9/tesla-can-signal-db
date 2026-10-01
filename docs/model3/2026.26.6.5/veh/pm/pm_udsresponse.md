---
layout: default
title: "PM_udsResponse (0x640) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "PM ECU message: uds response. Tesla Model 3 CAN bus message PM_udsResponse (0x640) of PM ECU, firmware 2026.26.6.5, 1 signals (PM_udsResponseData). Bit layout, scaling, units and value tables."
---

# PM_udsResponse (0x640) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN

PM ECU message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PM_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_udsResponse` |
| CAN id | 0x640 (1600) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PM_udsResponse

Tesla Model 3 CAN bus signals in `PM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_udsResponseData` | PM ECU: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
