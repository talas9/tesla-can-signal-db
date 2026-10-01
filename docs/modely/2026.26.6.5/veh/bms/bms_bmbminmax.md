---
layout: default
title: "BMS_bmbMinMax (0x332) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: bmb min max. Tesla Model Y CAN bus message BMS_bmbMinMax (0x332) of High-voltage battery management system, firmware 2026.26.6.5, 10 signals (BMS_bmbMinMaxMultiplexer, BMS_thermistorNumTMin, BMS_thermistorNumTMax, BMS_thermistorTMax and 6 more). Bit layout, scaling, units and value tables."
---

# BMS_bmbMinMax (0x332) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: bmb min max; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of BMS_bmbMinMax as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_bmbMinMax` |
| CAN id | 0x332 (818) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 10 |

## Signals of BMS_bmbMinMax

Tesla Model Y CAN bus signals in `BMS_bmbMinMax`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_bmbMinMaxMultiplexer` | selector | High-voltage battery management system: bmb min max multiplexer | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `THERM_MUX0`<br>1 = `VOLT_MUX1`<br>2 = `END` | validated |
| `BMS_thermistorNumTMin` | page 0 | BMB module number with minimum temperature. | 2\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `BMS_thermistorNumTMax` | page 0 | BMB module number with maximum temperature. | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `BMS_thermistorTMax` | page 0 | Max temperature of all valid filtered thermistors | 16\|8 | little-endian | unsigned | 0.5 | -40 | DegC | -40 to 87.5 |  | validated |
| `BMS_thermistorTMin` | page 0 | Min temperature of all valid filtered thermistors | 24\|8 | little-endian | unsigned | 0.5 | -40 | DegC | -40 to 87.5 |  | validated |
| `BMS_thermistorTAvg` | page 0 | Average temperature of all valid filtered thermistors | 32\|8 | little-endian | unsigned | 0.5 | -40 | DegC | -40 to 87.5 |  | validated |
| `BMS_brickVoltageMax` | page 1 | Brick voltage maximum. | 2\|12 | little-endian | unsigned | 0.002 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageMin` | page 1 | Brick voltage minimum. | 16\|12 | little-endian | unsigned | 0.002 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickNumVoltageMax` | page 1 | Brick number with maximum voltage (1 indexed) | 32\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | validated |
| `BMS_brickNumVoltageMin` | page 1 | Brick number with minimum voltage (1 indexed) | 40\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | validated |

## Multiplexing

`BMS_bmbMinMaxMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
