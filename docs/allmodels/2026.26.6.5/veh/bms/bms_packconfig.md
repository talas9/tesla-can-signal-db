---
layout: default
title: "BMS_packConfig (0x392) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: pack config. Tesla Model 3 / Model Y CAN bus message BMS_packConfig (0x392) of High-voltage battery management system, firmware 2026.26.6.5, 8 signals (BMS_packConfigMultiplexer, BMS_reservedConfig_0, BMS_moduleType, BMS_thermalPackType and 4 more). Bit layout, scaling, units and value tables."
---

# BMS_packConfig (0x392) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: pack config; frame length observed on a vehicle bus. This page documents the 8 signals of BMS_packConfig as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_packConfig` |
| CAN id | 0x392 (914) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of BMS_packConfig

Tesla Model 3 / Model Y CAN bus signals in `BMS_packConfig`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_packConfigMultiplexer` | selector | High-voltage battery management system: pack config multiplexer | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `BMS_reservedConfig_0` | page 0 | High-voltage battery management system: reserved config 0 | 8\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `BMS_CONFIG_0`<br>1 = `BMS_CONFIG_1`<br>2 = `BMS_CONFIG_2`<br>3 = `BMS_CONFIG_3`<br>4 = `BMS_CONFIG_4`<br>5 = `BMS_CONFIG_5`<br>6 = `BMS_CONFIG_6`<br>7 = `BMS_CONFIG_7`<br>8 = `BMS_CONFIG_8`<br>9 = `BMS_CONFIG_9`<br>10 = `BMS_CONFIG_10`<br>11 = `BMS_CONFIG_11`<br>12 = `BMS_CONFIG_12`<br>13 = `BMS_CONFIG_13`<br>14 = `BMS_CONFIG_14`<br>15 = `BMS_CONFIG_15`<br>16 = `BMS_CONFIG_16`<br>17 = `BMS_CONFIG_17`<br>18 = `BMS_CONFIG_18`<br>19 = `BMS_CONFIG_19`<br>20 = `BMS_CONFIG_20`<br>21 = `BMS_CONFIG_21`<br>22 = `BMS_CONFIG_22`<br>23 = `BMS_CONFIG_23`<br>24 = `BMS_CONFIG_24`<br>25 = `BMS_CONFIG_25`<br>26 = `BMS_CONFIG_26`<br>27 = `BMS_CONFIG_27`<br>28 = `BMS_CONFIG_28`<br>29 = `BMS_CONFIG_29`<br>30 = `BMS_CONFIG_30`<br>31 = `BMS_CONFIG_31`<br>32 = `BMS_CONFIG_32`<br>33 = `BMS_CONFIG_33`<br>34 = `BMS_CONFIG_34`<br>35 = `BMS_CONFIG_35`<br>36 = `BMS_CONFIG_36` | validated |
| `BMS_moduleType` | page 1 | High-voltage battery management system: module type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BMS_MOD_TYPE_UNKNOWN`<br>1 = `BMS_MOD_TYPE_1`<br>2 = `BMS_MOD_TYPE_2`<br>3 = `BMS_MOD_TYPE_3`<br>4 = `BMS_MOD_TYPE_4`<br>5 = `BMS_MOD_TYPE_5` | validated |
| `BMS_thermalPackType` | page 1 | High-voltage battery management system: thermal pack type | 11\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `E1`<br>2 = `E3`<br>3 = `CATL_E1`<br>4 = `BFF00_E1`<br>5 = `P2`<br>6 = `BFF00S`<br>7 = `BLADERUNNER_E1`<br>8 = `E3D`<br>9 = `E3D_40P` | validated |
| `BMS_packMass` | page 1 | High-voltage battery management system: pack mass | 16\|8 | little-endian | unsigned | 1 | 300 | kg | 342 to 540 |  | validated |
| `BMS_platformMaxBusVoltage` | page 1 | High-voltage battery management system: platform max bus voltage | 24\|10 | little-endian | unsigned | 1 | 300 | V | 300 to 1300 |  | validated |
| `BMS_standbySupplyContinuousPowerLimit` | page 1 | High-voltage battery management system: standby supply continuous power limit | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0W`<br>1 = `4W`<br>2 = `16W`<br>3 = `17W` | validated |
| `BMS_beginningOfLifePackEnergy` | page 1 | High-voltage battery management system: beginning of life pack energy; raw 1023 = signal not available (SNA) | 40\|10 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 102.2 | 1023 = `SNA` | validated |

## Multiplexing

`BMS_packConfigMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
