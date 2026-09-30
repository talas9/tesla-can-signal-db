---
layout: default
title: "EVSE_isoTpToVeh (0x67E) — EVSE ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "EVSE ECU message: iso tp to veh. Tesla Model Y CAN bus message EVSE_isoTpToVeh (0x67E) of EVSE ECU, firmware 2025.20.8, 1 signals (EVSE_isoTpToVehData). Bit layout, scaling, units and value tables."
---

# EVSE_isoTpToVeh (0x67E) — EVSE ECU, Tesla Model Y 2025.20.8 VEH CAN

EVSE ECU message: iso tp to veh; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of EVSE_isoTpToVeh as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EVSE_isoTpToVeh` |
| CAN id | 0x67E (1662) |
| ECU | [EVSE ECU](../../evse.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EVSE |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of EVSE_isoTpToVeh

Tesla Model Y CAN bus signals in `EVSE_isoTpToVeh`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EVSE_isoTpToVehData` | EVSE ECU: iso tp to veh data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All EVSE ECU messages (EVSE)](../../evse.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
