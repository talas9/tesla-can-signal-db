---
layout: default
title: "PCS_dcdcRailStatus (0x2B4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: dcdc rail status. Tesla Model Y CAN bus message PCS_dcdcRailStatus (0x2B4) of Power conversion system (on-board charger and DC-DC converter), firmware 2026.26.6.5, 3 signals (PCS_dcdcLvBusVolt, PCS_dcdcHvBusVolt, PCS_dcdcLvOutputCurrent). Bit layout, scaling, units and value tables."
---

# PCS_dcdcRailStatus (0x2B4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2026.26.6.5 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: dcdc rail status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of PCS_dcdcRailStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_dcdcRailStatus` |
| CAN id | 0x2B4 (692) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of PCS_dcdcRailStatus

Tesla Model Y CAN bus signals in `PCS_dcdcRailStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_dcdcLvBusVolt` | DCDC's sensed LV bus voltage | 0\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 80 |  | validated |
| `PCS_dcdcHvBusVolt` | DCDC's sensed HV bus voltage | 16\|14 | little-endian | unsigned | 0.1 | 0 | V | 0 to 1600 |  | validated |
| `PCS_dcdcLvOutputCurrent` | DCDC's computed LV output current | 32\|13 | little-endian | signed | 0.1 | 0 | A | -400 to 400 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
