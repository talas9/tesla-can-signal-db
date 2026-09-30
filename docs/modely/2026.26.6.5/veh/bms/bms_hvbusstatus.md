---
layout: default
title: "BMS_hvBusStatus (0x132) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: hv bus status. Tesla Model Y CAN bus message BMS_hvBusStatus (0x132) of High-voltage battery management system, firmware 2026.26.6.5, 3 signals (BMS_dcLinkVoltage, BMS_packCurrent, BMS_currentUnfiltered). Bit layout, scaling, units and value tables."
---

# BMS_hvBusStatus (0x132) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: hv bus status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of BMS_hvBusStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_hvBusStatus` |
| CAN id | 0x132 (306) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 6 bytes |
| Cycle time | 10 ms |
| Signals | 3 |

## Signals of BMS_hvBusStatus

Tesla Model Y CAN bus signals in `BMS_hvBusStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_dcLinkVoltage` | High-voltage battery management system: dc link voltage | 0\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | validated |
| `BMS_packCurrent` | Current measured at the HV contactors of the HV battery; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.7 to 3276.7 | -32768 = `SNA` | validated |
| `BMS_currentUnfiltered` | Pack current with no filters applied; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.05 | -822 | A | -2460.3 to 816.3 | -32768 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
