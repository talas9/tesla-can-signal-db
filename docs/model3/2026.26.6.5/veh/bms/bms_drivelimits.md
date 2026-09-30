---
layout: default
title: "BMS_driveLimits (0x2D2) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: drive limits. Tesla Model 3 CAN bus message BMS_driveLimits (0x2D2) of High-voltage battery management system, firmware 2026.26.6.5, 4 signals (BMS_minBusVoltage, BMS_maxBusVoltage, BMS_maxChargeCurrent, BMS_maxDischargeCurrent). Bit layout, scaling, units and value tables."
---

# BMS_driveLimits (0x2D2) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: drive limits; frame length observed on a vehicle bus. This page documents the 4 signals of BMS_driveLimits as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_driveLimits` |
| CAN id | 0x2D2 (722) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 4 |

## Signals of BMS_driveLimits

Tesla Model 3 CAN bus signals in `BMS_driveLimits`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_minBusVoltage` | Calculated min bus voltage limit | 0\|16 | little-endian | unsigned | 0.02 | 0 | V | 0 to 1200 |  | validated |
| `BMS_maxBusVoltage` | Calculated max bus voltage limit for the pack | 16\|16 | little-endian | unsigned | 0.02 | 0 | V | 0 to 1200 |  | validated |
| `BMS_maxChargeCurrent` | Calculated max charge current limit for the pack | 32\|14 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1638.2 |  | validated |
| `BMS_maxDischargeCurrent` | Calculated max discharge current limit for the pack | 48\|14 | little-endian | unsigned | 0.15 | 0 | A | 0 to 2455 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
