---
layout: default
title: "BMS_socStatus (0x292) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: soc status. Tesla Model 3 / Model Y CAN bus message BMS_socStatus (0x292) of High-voltage battery management system, firmware 2026.26.6.5, 6 signals (BMS_socMin, BMS_socUI, BMS_socMax, BMS_socAvg and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_socStatus (0x292) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: soc status; frame length observed on a vehicle bus. This page documents the 6 signals of BMS_socStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_socStatus` |
| CAN id | 0x292 (658) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of BMS_socStatus

Tesla Model 3 / Model Y CAN bus signals in `BMS_socStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_socMin` | BMS State Of Charge (SOC). This is the minimum brick SOC. | 0\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socUI` | BMS State Of Energy (SOE) for the UI. This is ideal discharge energy from present state / ideal discharge energy from full. | 10\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `BMS_socMax` | BMS State Of Charge (SOC). This is the maximum brick SOC. | 20\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socAvg` | BMS State Of Charge (SOC). This is the average of all the brick SOCs | 30\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_enoughEnergyForConvenienceFeatures` | Flag to indicate if there is enough energy for user facing features that are function of the UI discharge limit | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_instantChargePowerCapability` | Indicates the instantaneous charge power capability of the high voltage battery; raw 65535 = signal not available (SNA) | 48\|16 | little-endian | unsigned | 0.05 | 0 | kW | 0 to 3276.7 | 65535 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
