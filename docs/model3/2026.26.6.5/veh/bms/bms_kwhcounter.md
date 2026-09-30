---
layout: default
title: "BMS_kwhCounter (0x3D2) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: kwh counter. Tesla Model 3 CAN bus message BMS_kwhCounter (0x3D2) of High-voltage battery management system, firmware 2026.26.6.5, 2 signals (BMS_kwhDischargeTotal, BMS_kwhChargeTotal). Bit layout, scaling, units and value tables."
---

# BMS_kwhCounter (0x3D2) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: kwh counter; frame length observed on a vehicle bus. This page documents the 2 signals of BMS_kwhCounter as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_kwhCounter` |
| CAN id | 0x3D2 (978) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of BMS_kwhCounter

Tesla Model 3 CAN bus signals in `BMS_kwhCounter`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_kwhDischargeTotal` | Total energy-lost kWh count during discharging | 0\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |
| `BMS_kwhChargeTotal` | Total energy-gained kWh count during charging | 32\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
