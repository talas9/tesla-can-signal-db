---
layout: default
title: "PCS_udsResponse (0x629) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: uds response. Tesla Model Y CAN bus message PCS_udsResponse (0x629) of Power conversion system (on-board charger and DC-DC converter), firmware 2026.26.6.5, 1 signals (PCS_udsResponseData). Bit layout, scaling, units and value tables."
---

# PCS_udsResponse (0x629) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of PCS_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_udsResponse` |
| CAN id | 0x629 (1577) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PCS_udsResponse

Tesla Model Y CAN bus signals in `PCS_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_udsResponseData` | Power conversion system (on-board charger and DC-DC converter): uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
