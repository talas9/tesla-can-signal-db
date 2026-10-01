---
layout: default
title: "BMS_kwhCountersMultiplexed (0x3F2) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: kwh counters multiplexed. Tesla Model 3 / Model Y CAN bus message BMS_kwhCountersMultiplexed (0x3F2) of High-voltage battery management system, firmware 2026.26.6.5, 21 signals (BMS_kwhCounter_Id, BMS_acChargerKwhTotal, BMS_dcChargerKwhTotal, BMS_kwhRegenChargeTotal and 17 more). Bit layout, scaling, units and value tables."
---

# BMS_kwhCountersMultiplexed (0x3F2) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: kwh counters multiplexed; frame length observed on a vehicle bus. This page documents the 21 signals of BMS_kwhCountersMultiplexed as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_kwhCountersMultiplexed` |
| CAN id | 0x3F2 (1010) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 21 |

## Signals of BMS_kwhCountersMultiplexed

Tesla Model 3 / Model Y CAN bus signals in `BMS_kwhCountersMultiplexed`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_kwhCounter_Id` | selector | High-voltage battery management system: kwh counter id | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `MUX0`<br>1 = `MUX1`<br>2 = `MUX2`<br>3 = `MUX3`<br>4 = `MUX4`<br>5 = `MUX5`<br>6 = `MUX6`<br>7 = `MUX7`<br>8 = `MUX8`<br>9 = `MUX9`<br>10 = `MUX10`<br>11 = `MUX11`<br>12 = `MUX12`<br>13 = `MUX13`<br>14 = `END` | validated |
| `BMS_acChargerKwhTotal` | page 0 | Total energy-gained kWh count during AC charge | 8\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |
| `BMS_dcChargerKwhTotal` | page 1 | Total energy-gained kWh count during DC charging | 8\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |
| `BMS_kwhRegenChargeTotal` | page 2 | Total energy-gained kWh count during charging with regen | 8\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |
| `BMS_kwhDriveDischargeTotal` | page 3 | Total energy-lost kWh count during discharging while driving | 8\|32 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.456 |  | validated |
| `BMS_kwhDischargeTotalModule1` | page 4 | Total energy-lost kWh count during discharging for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhChargeTotalModule1` | page 4 | Total energy-gained kWh count for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhAcChargeTotalModule1` | page 5 | Total energy-gained kWh count during AC charge for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDcChargeTotalModule1` | page 5 | Total energy-gained kWh count during DC charge for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDischargeTotalModule2` | page 6 | Total energy-lost kWh count during discharging for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhChargeTotalModule2` | page 6 | Total energy-gained kWh count for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhAcChargeTotalModule2` | page 7 | Total energy-gained kWh count during AC charge for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDcChargeTotalModule2` | page 7 | Total energy-gained kWh count during DC charge for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDischargeTotalModule3` | page 8 | Total energy-lost kWh count during discharging for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhChargeTotalModule3` | page 8 | Total energy-gained kWh count for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhAcChargeTotalModule3` | page 9 | Total energy-gained kWh count during AC charge for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDcChargeTotalModule3` | page 9 | Total energy-gained kWh count during DC charge for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDischargeTotalModule4` | page 10 | Total energy-lost kWh count during discharging for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhChargeTotalModule4` | page 10 | Total energy-gained kWh count for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhAcChargeTotalModule4` | page 11 | Total energy-gained kWh count during AC charge for module number (1 indexed) | 8\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |
| `BMS_kwhDcChargeTotalModule4` | page 11 | Total energy-gained kWh count during DC charge for module number (1 indexed) | 36\|28 | little-endian | unsigned | 0.001 | 0 | KWh | 0 to 268435.455 |  | validated |

## Multiplexing

`BMS_kwhCounter_Id` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (2 signals), page 5 (2 signals), page 6 (2 signals), page 7 (2 signals), page 8 (2 signals), page 9 (2 signals), page 10 (2 signals), page 11 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
