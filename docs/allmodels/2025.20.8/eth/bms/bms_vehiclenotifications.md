---
layout: default
title: "BMS_vehicleNotifications (0x32A) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: vehicle notifications. Ethernet-side message BMS_vehicleNotifications of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 4 signals (BMS_thermalEventSuspected, BMS_vehicleNotificationsCounter, BMS_isolationResistance, BMS_vehicleNotificationsChecksum). Bit layout, scaling, units and value tables."
---

# BMS_vehicleNotifications (0x32A) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: vehicle notifications. This page documents the 4 signals of BMS_vehicleNotifications as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_vehicleNotifications` |
| Ethernet-side id | 0x32A (810) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 5 bytes |
| Cycle time | 5000 ms |
| Signals | 4 |

## Signals of BMS_vehicleNotifications

Tesla Model 3 / Model Y CAN bus signals in `BMS_vehicleNotifications`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_thermalEventSuspected` | Indicates the Battery Management System (BMS) has detected conditions that reflect a possible battery thermal event | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_vehicleNotificationsCounter` | High-voltage battery management system: vehicle notifications counter | 1\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `BMS_isolationResistance` | Resistance between HV bus and chassis; raw 1023 = signal not available (SNA) | 6\|10 | little-endian | unsigned | 10 | 0 | kOhm | 0 to 10000 | 1023 = `SNA` | plausible |
| `BMS_vehicleNotificationsChecksum` | High-voltage battery management system: vehicle notifications checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
