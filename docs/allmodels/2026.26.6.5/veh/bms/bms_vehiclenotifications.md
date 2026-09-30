---
layout: default
title: "BMS_vehicleNotifications (0x32A) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: vehicle notifications. Tesla Model 3 / Model Y CAN bus message BMS_vehicleNotifications (0x32A) of High-voltage battery management system, firmware 2026.26.6.5, 5 signals (BMS_thermalEventSuspected, BMS_vehicleNotificationsCounter, BMS_isolationResistance, BMS_chgTimeToFull and 1 more). Bit layout, scaling, units and value tables."
---

# BMS_vehicleNotifications (0x32A) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: vehicle notifications; frame length observed on a vehicle bus. This page documents the 5 signals of BMS_vehicleNotifications as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_vehicleNotifications` |
| CAN id | 0x32A (810) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 5 bytes |
| Cycle time | 5000 ms |
| Signals | 5 |

## Signals of BMS_vehicleNotifications

Tesla Model 3 / Model Y CAN bus signals in `BMS_vehicleNotifications`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_thermalEventSuspected` | Indicates the Battery Management System (BMS) has detected conditions that reflect a possible battery thermal event | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_vehicleNotificationsCounter` | High-voltage battery management system: vehicle notifications counter | 1\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `BMS_isolationResistance` | Resistance between HV bus and chassis; raw 1023 = signal not available (SNA) | 6\|10 | little-endian | unsigned | 10 | 0 | kOhm | 0 to 10000 | 1023 = `SNA` | validated |
| `BMS_chgTimeToFull` | Estimated time remaining until charge termination percent will be reached; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 0.01666667 | 0 | Hours | 0 to 68.23334698 | 4095 = `SNA` | validated |
| `BMS_vehicleNotificationsChecksum` | High-voltage battery management system: vehicle notifications checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
