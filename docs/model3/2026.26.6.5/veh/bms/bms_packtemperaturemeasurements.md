---
layout: default
title: "BMS_packTemperatureMeasurements (0x712) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: pack temperature measurements. Tesla Model 3 CAN bus message BMS_packTemperatureMeasurements (0x712) of High-voltage battery management system, firmware 2026.26.6.5, 38 signals (BMS_packTemperatureMultiplexer, BMS_packTemperatureCounter, BMS_packTemperatureStatus1, BMS_packTemperatureStatus2 and 34 more). Bit layout, scaling, units and value tables."
---

# BMS_packTemperatureMeasurements (0x712) — High-voltage battery management system, Tesla Model 3 2026.26.6.5 VEH CAN

High-voltage battery management system message: pack temperature measurements; frame length observed on a vehicle bus. This page documents the 38 signals of BMS_packTemperatureMeasurements as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_packTemperatureMeasurements` |
| CAN id | 0x712 (1810) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 38 |

## Signals of BMS_packTemperatureMeasurements

Tesla Model 3 CAN bus signals in `BMS_packTemperatureMeasurements`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_packTemperatureMultiplexer` | selector | High-voltage battery management system: pack temperature multiplexer | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5` | plausible |
| `BMS_packTemperatureCounter` |  | High-voltage battery management system: pack temperature counter | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `BMS_packTemperatureStatus1` | page 0 | High-voltage battery management system: pack temperature status1 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus2` | page 0 | High-voltage battery management system: pack temperature status2 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus3` | page 0 | High-voltage battery management system: pack temperature status3 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature1` | page 0 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature2` | page 0 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature3` | page 0 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperatureStatus4` | page 1 | High-voltage battery management system: pack temperature status4 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus5` | page 1 | High-voltage battery management system: pack temperature status5 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus6` | page 1 | High-voltage battery management system: pack temperature status6 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature4` | page 1 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature5` | page 1 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature6` | page 1 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperatureStatus7` | page 2 | High-voltage battery management system: pack temperature status7 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus8` | page 2 | High-voltage battery management system: pack temperature status8 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus9` | page 2 | High-voltage battery management system: pack temperature status9 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature7` | page 2 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature8` | page 2 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature9` | page 2 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperatureStatus10` | page 3 | High-voltage battery management system: pack temperature status10 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus11` | page 3 | High-voltage battery management system: pack temperature status11 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus12` | page 3 | High-voltage battery management system: pack temperature status12 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature10` | page 3 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature11` | page 3 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature12` | page 3 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperatureStatus13` | page 4 | High-voltage battery management system: pack temperature status13 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus14` | page 4 | High-voltage battery management system: pack temperature status14 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus15` | page 4 | High-voltage battery management system: pack temperature status15 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature13` | page 4 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature14` | page 4 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature15` | page 4 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperatureStatus16` | page 5 | High-voltage battery management system: pack temperature status16 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus17` | page 5 | High-voltage battery management system: pack temperature status17 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperatureStatus18` | page 5 | High-voltage battery management system: pack temperature status18 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_packTemperature16` | page 5 | Measured temperature of location within the pack | 16\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature17` | page 5 | Measured temperature of location within the pack | 32\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |
| `BMS_packTemperature18` | page 5 | Measured temperature of location within the pack | 48\|16 | little-endian | signed | 0.01 | 0 | C | -327.68 to 327.67 |  | validated |

## Multiplexing

`BMS_packTemperatureMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 1 (6 signals), page 2 (6 signals), page 3 (6 signals), page 4 (6 signals), page 5 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
