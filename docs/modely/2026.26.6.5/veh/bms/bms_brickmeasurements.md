---
layout: default
title: "BMS_brickMeasurements (0x401) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: brick measurements. Tesla Model Y CAN bus message BMS_brickMeasurements (0x401) of High-voltage battery management system, firmware 2026.26.6.5, 218 signals (BMS_brickVoltageMultiplexer, BMS_brickVoltageCounter, BMS_brickVoltageStatus1, BMS_brickVoltageStatus2 and 214 more). Bit layout, scaling, units and value tables."
---

# BMS_brickMeasurements (0x401) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: brick measurements; frame length from the layout, not yet observed on a vehicle bus. This page documents the 218 signals of BMS_brickMeasurements as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_brickMeasurements` |
| CAN id | 0x401 (1025) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 218 |

## Signals of BMS_brickMeasurements

Tesla Model Y CAN bus signals in `BMS_brickMeasurements`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_brickVoltageMultiplexer` | selector | High-voltage battery management system: brick voltage multiplexer | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5`<br>6 = `Mux6`<br>7 = `Mux7`<br>8 = `Mux8`<br>9 = `Mux9`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12`<br>13 = `Mux13`<br>14 = `Mux14`<br>15 = `Mux15`<br>16 = `Mux16`<br>17 = `Mux17`<br>18 = `Mux18`<br>19 = `Mux19`<br>20 = `Mux20`<br>21 = `Mux21`<br>22 = `Mux22`<br>23 = `Mux23`<br>24 = `Mux24`<br>25 = `Mux25`<br>26 = `Mux26`<br>27 = `Mux27`<br>28 = `Mux28`<br>29 = `Mux29`<br>30 = `Mux30`<br>31 = `Mux31`<br>32 = `Mux32`<br>33 = `Mux33`<br>34 = `Mux34`<br>35 = `Mux35` | plausible |
| `BMS_brickVoltageCounter` |  | High-voltage battery management system: brick voltage counter | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `BMS_brickVoltageStatus1` | page 0 | High-voltage battery management system: brick voltage status1 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus2` | page 0 | High-voltage battery management system: brick voltage status2 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus3` | page 0 | High-voltage battery management system: brick voltage status3 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage1` | page 0 | High-voltage battery management system: brick voltage1 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage2` | page 0 | High-voltage battery management system: brick voltage2 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage3` | page 0 | High-voltage battery management system: brick voltage3 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus4` | page 1 | High-voltage battery management system: brick voltage status4 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus5` | page 1 | High-voltage battery management system: brick voltage status5 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus6` | page 1 | High-voltage battery management system: brick voltage status6 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage4` | page 1 | High-voltage battery management system: brick voltage4 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage5` | page 1 | High-voltage battery management system: brick voltage5 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage6` | page 1 | High-voltage battery management system: brick voltage6 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus7` | page 2 | High-voltage battery management system: brick voltage status7 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus8` | page 2 | High-voltage battery management system: brick voltage status8 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus9` | page 2 | High-voltage battery management system: brick voltage status9 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage7` | page 2 | High-voltage battery management system: brick voltage7 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage8` | page 2 | High-voltage battery management system: brick voltage8 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage9` | page 2 | High-voltage battery management system: brick voltage9 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus10` | page 3 | High-voltage battery management system: brick voltage status10 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus11` | page 3 | High-voltage battery management system: brick voltage status11 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus12` | page 3 | High-voltage battery management system: brick voltage status12 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage10` | page 3 | High-voltage battery management system: brick voltage10 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage11` | page 3 | High-voltage battery management system: brick voltage11 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage12` | page 3 | High-voltage battery management system: brick voltage12 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus13` | page 4 | High-voltage battery management system: brick voltage status13 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus14` | page 4 | High-voltage battery management system: brick voltage status14 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus15` | page 4 | High-voltage battery management system: brick voltage status15 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage13` | page 4 | High-voltage battery management system: brick voltage13 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage14` | page 4 | High-voltage battery management system: brick voltage14 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage15` | page 4 | High-voltage battery management system: brick voltage15 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus16` | page 5 | High-voltage battery management system: brick voltage status16 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus17` | page 5 | High-voltage battery management system: brick voltage status17 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus18` | page 5 | High-voltage battery management system: brick voltage status18 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage16` | page 5 | High-voltage battery management system: brick voltage16 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage17` | page 5 | High-voltage battery management system: brick voltage17 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage18` | page 5 | High-voltage battery management system: brick voltage18 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus19` | page 6 | High-voltage battery management system: brick voltage status19 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus20` | page 6 | High-voltage battery management system: brick voltage status20 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus21` | page 6 | High-voltage battery management system: brick voltage status21 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage19` | page 6 | High-voltage battery management system: brick voltage19 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage20` | page 6 | High-voltage battery management system: brick voltage20 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage21` | page 6 | High-voltage battery management system: brick voltage21 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus22` | page 7 | High-voltage battery management system: brick voltage status22 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus23` | page 7 | High-voltage battery management system: brick voltage status23 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus24` | page 7 | High-voltage battery management system: brick voltage status24 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage22` | page 7 | High-voltage battery management system: brick voltage22 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage23` | page 7 | High-voltage battery management system: brick voltage23 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage24` | page 7 | High-voltage battery management system: brick voltage24 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus25` | page 8 | High-voltage battery management system: brick voltage status25 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus26` | page 8 | High-voltage battery management system: brick voltage status26 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus27` | page 8 | High-voltage battery management system: brick voltage status27 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage25` | page 8 | High-voltage battery management system: brick voltage25 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage26` | page 8 | High-voltage battery management system: brick voltage26 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage27` | page 8 | High-voltage battery management system: brick voltage27 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus28` | page 9 | High-voltage battery management system: brick voltage status28 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus29` | page 9 | High-voltage battery management system: brick voltage status29 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus30` | page 9 | High-voltage battery management system: brick voltage status30 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage28` | page 9 | High-voltage battery management system: brick voltage28 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage29` | page 9 | High-voltage battery management system: brick voltage29 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage30` | page 9 | High-voltage battery management system: brick voltage30 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus31` | page 10 | High-voltage battery management system: brick voltage status31 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus32` | page 10 | High-voltage battery management system: brick voltage status32 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus33` | page 10 | High-voltage battery management system: brick voltage status33 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage31` | page 10 | High-voltage battery management system: brick voltage31 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage32` | page 10 | High-voltage battery management system: brick voltage32 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage33` | page 10 | High-voltage battery management system: brick voltage33 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus34` | page 11 | High-voltage battery management system: brick voltage status34 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus35` | page 11 | High-voltage battery management system: brick voltage status35 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus36` | page 11 | High-voltage battery management system: brick voltage status36 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage34` | page 11 | High-voltage battery management system: brick voltage34 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage35` | page 11 | High-voltage battery management system: brick voltage35 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage36` | page 11 | High-voltage battery management system: brick voltage36 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus37` | page 12 | High-voltage battery management system: brick voltage status37 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus38` | page 12 | High-voltage battery management system: brick voltage status38 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus39` | page 12 | High-voltage battery management system: brick voltage status39 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage37` | page 12 | High-voltage battery management system: brick voltage37 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage38` | page 12 | High-voltage battery management system: brick voltage38 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage39` | page 12 | High-voltage battery management system: brick voltage39 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus40` | page 13 | High-voltage battery management system: brick voltage status40 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus41` | page 13 | High-voltage battery management system: brick voltage status41 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus42` | page 13 | High-voltage battery management system: brick voltage status42 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage40` | page 13 | High-voltage battery management system: brick voltage40 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage41` | page 13 | High-voltage battery management system: brick voltage41 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage42` | page 13 | High-voltage battery management system: brick voltage42 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus43` | page 14 | High-voltage battery management system: brick voltage status43 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus44` | page 14 | High-voltage battery management system: brick voltage status44 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus45` | page 14 | High-voltage battery management system: brick voltage status45 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage43` | page 14 | High-voltage battery management system: brick voltage43 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage44` | page 14 | High-voltage battery management system: brick voltage44 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage45` | page 14 | High-voltage battery management system: brick voltage45 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus46` | page 15 | High-voltage battery management system: brick voltage status46 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus47` | page 15 | High-voltage battery management system: brick voltage status47 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus48` | page 15 | High-voltage battery management system: brick voltage status48 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage46` | page 15 | High-voltage battery management system: brick voltage46 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage47` | page 15 | High-voltage battery management system: brick voltage47 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage48` | page 15 | High-voltage battery management system: brick voltage48 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus49` | page 16 | High-voltage battery management system: brick voltage status49 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus50` | page 16 | High-voltage battery management system: brick voltage status50 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus51` | page 16 | High-voltage battery management system: brick voltage status51 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage49` | page 16 | High-voltage battery management system: brick voltage49 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage50` | page 16 | High-voltage battery management system: brick voltage50 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage51` | page 16 | High-voltage battery management system: brick voltage51 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus52` | page 17 | High-voltage battery management system: brick voltage status52 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus53` | page 17 | High-voltage battery management system: brick voltage status53 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus54` | page 17 | High-voltage battery management system: brick voltage status54 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage52` | page 17 | High-voltage battery management system: brick voltage52 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage53` | page 17 | High-voltage battery management system: brick voltage53 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage54` | page 17 | High-voltage battery management system: brick voltage54 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus55` | page 18 | High-voltage battery management system: brick voltage status55 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus56` | page 18 | High-voltage battery management system: brick voltage status56 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus57` | page 18 | High-voltage battery management system: brick voltage status57 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage55` | page 18 | High-voltage battery management system: brick voltage55 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage56` | page 18 | High-voltage battery management system: brick voltage56 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage57` | page 18 | High-voltage battery management system: brick voltage57 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus58` | page 19 | High-voltage battery management system: brick voltage status58 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus59` | page 19 | High-voltage battery management system: brick voltage status59 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus60` | page 19 | High-voltage battery management system: brick voltage status60 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage58` | page 19 | High-voltage battery management system: brick voltage58 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage59` | page 19 | High-voltage battery management system: brick voltage59 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage60` | page 19 | High-voltage battery management system: brick voltage60 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus61` | page 20 | High-voltage battery management system: brick voltage status61 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus62` | page 20 | High-voltage battery management system: brick voltage status62 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus63` | page 20 | High-voltage battery management system: brick voltage status63 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage61` | page 20 | High-voltage battery management system: brick voltage61 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage62` | page 20 | High-voltage battery management system: brick voltage62 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage63` | page 20 | High-voltage battery management system: brick voltage63 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus64` | page 21 | High-voltage battery management system: brick voltage status64 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus65` | page 21 | High-voltage battery management system: brick voltage status65 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus66` | page 21 | High-voltage battery management system: brick voltage status66 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage64` | page 21 | High-voltage battery management system: brick voltage64 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage65` | page 21 | High-voltage battery management system: brick voltage65 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage66` | page 21 | High-voltage battery management system: brick voltage66 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus67` | page 22 | High-voltage battery management system: brick voltage status67 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus68` | page 22 | High-voltage battery management system: brick voltage status68 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus69` | page 22 | High-voltage battery management system: brick voltage status69 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage67` | page 22 | High-voltage battery management system: brick voltage67 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage68` | page 22 | High-voltage battery management system: brick voltage68 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage69` | page 22 | High-voltage battery management system: brick voltage69 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus70` | page 23 | High-voltage battery management system: brick voltage status70 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus71` | page 23 | High-voltage battery management system: brick voltage status71 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus72` | page 23 | High-voltage battery management system: brick voltage status72 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage70` | page 23 | High-voltage battery management system: brick voltage70 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage71` | page 23 | High-voltage battery management system: brick voltage71 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage72` | page 23 | High-voltage battery management system: brick voltage72 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus73` | page 24 | High-voltage battery management system: brick voltage status73 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus74` | page 24 | High-voltage battery management system: brick voltage status74 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus75` | page 24 | High-voltage battery management system: brick voltage status75 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage73` | page 24 | High-voltage battery management system: brick voltage73 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage74` | page 24 | High-voltage battery management system: brick voltage74 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage75` | page 24 | High-voltage battery management system: brick voltage75 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus76` | page 25 | High-voltage battery management system: brick voltage status76 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus77` | page 25 | High-voltage battery management system: brick voltage status77 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus78` | page 25 | High-voltage battery management system: brick voltage status78 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage76` | page 25 | High-voltage battery management system: brick voltage76 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage77` | page 25 | High-voltage battery management system: brick voltage77 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage78` | page 25 | High-voltage battery management system: brick voltage78 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus79` | page 26 | High-voltage battery management system: brick voltage status79 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus80` | page 26 | High-voltage battery management system: brick voltage status80 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus81` | page 26 | High-voltage battery management system: brick voltage status81 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage79` | page 26 | High-voltage battery management system: brick voltage79 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage80` | page 26 | High-voltage battery management system: brick voltage80 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage81` | page 26 | High-voltage battery management system: brick voltage81 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus82` | page 27 | High-voltage battery management system: brick voltage status82 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus83` | page 27 | High-voltage battery management system: brick voltage status83 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus84` | page 27 | High-voltage battery management system: brick voltage status84 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage82` | page 27 | High-voltage battery management system: brick voltage82 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage83` | page 27 | High-voltage battery management system: brick voltage83 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage84` | page 27 | High-voltage battery management system: brick voltage84 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus85` | page 28 | High-voltage battery management system: brick voltage status85 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus86` | page 28 | High-voltage battery management system: brick voltage status86 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus87` | page 28 | High-voltage battery management system: brick voltage status87 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage85` | page 28 | High-voltage battery management system: brick voltage85 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage86` | page 28 | High-voltage battery management system: brick voltage86 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage87` | page 28 | High-voltage battery management system: brick voltage87 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus88` | page 29 | High-voltage battery management system: brick voltage status88 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus89` | page 29 | High-voltage battery management system: brick voltage status89 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus90` | page 29 | High-voltage battery management system: brick voltage status90 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage88` | page 29 | High-voltage battery management system: brick voltage88 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage89` | page 29 | High-voltage battery management system: brick voltage89 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage90` | page 29 | High-voltage battery management system: brick voltage90 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus91` | page 30 | High-voltage battery management system: brick voltage status91 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus92` | page 30 | High-voltage battery management system: brick voltage status92 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus93` | page 30 | High-voltage battery management system: brick voltage status93 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage91` | page 30 | High-voltage battery management system: brick voltage91 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage92` | page 30 | High-voltage battery management system: brick voltage92 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage93` | page 30 | High-voltage battery management system: brick voltage93 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus94` | page 31 | High-voltage battery management system: brick voltage status94 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus95` | page 31 | High-voltage battery management system: brick voltage status95 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus96` | page 31 | High-voltage battery management system: brick voltage status96 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage94` | page 31 | High-voltage battery management system: brick voltage94 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage95` | page 31 | High-voltage battery management system: brick voltage95 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage96` | page 31 | High-voltage battery management system: brick voltage96 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus97` | page 32 | High-voltage battery management system: brick voltage status97 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus98` | page 32 | High-voltage battery management system: brick voltage status98 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus99` | page 32 | High-voltage battery management system: brick voltage status99 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage97` | page 32 | High-voltage battery management system: brick voltage97 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage98` | page 32 | High-voltage battery management system: brick voltage98 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage99` | page 32 | High-voltage battery management system: brick voltage99 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus100` | page 33 | High-voltage battery management system: brick voltage status100 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus101` | page 33 | High-voltage battery management system: brick voltage status101 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus102` | page 33 | High-voltage battery management system: brick voltage status102 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage100` | page 33 | High-voltage battery management system: brick voltage100 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage101` | page 33 | High-voltage battery management system: brick voltage101 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage102` | page 33 | High-voltage battery management system: brick voltage102 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus103` | page 34 | High-voltage battery management system: brick voltage status103 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus104` | page 34 | High-voltage battery management system: brick voltage status104 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus105` | page 34 | High-voltage battery management system: brick voltage status105 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage103` | page 34 | High-voltage battery management system: brick voltage103 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage104` | page 34 | High-voltage battery management system: brick voltage104 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage105` | page 34 | High-voltage battery management system: brick voltage105 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltageStatus106` | page 35 | High-voltage battery management system: brick voltage status106 | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus107` | page 35 | High-voltage battery management system: brick voltage status107 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltageStatus108` | page 35 | High-voltage battery management system: brick voltage status108 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SENSOR_MISSING`<br>1 = `SENSOR_BAD`<br>2 = `SENSOR_NOMINAL`<br>3 = `SENSOR_BYPASSED` | validated |
| `BMS_brickVoltage106` | page 35 | High-voltage battery management system: brick voltage106 | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage107` | page 35 | High-voltage battery management system: brick voltage107 | 32\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |
| `BMS_brickVoltage108` | page 35 | High-voltage battery management system: brick voltage108 | 48\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 5 |  | validated |

## Multiplexing

`BMS_brickVoltageMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 1 (6 signals), page 2 (6 signals), page 3 (6 signals), page 4 (6 signals), page 5 (6 signals), page 6 (6 signals), page 7 (6 signals), page 8 (6 signals), page 9 (6 signals), page 10 (6 signals), page 11 (6 signals), page 12 (6 signals), page 13 (6 signals), page 14 (6 signals), page 15 (6 signals), page 16 (6 signals), page 17 (6 signals), page 18 (6 signals), page 19 (6 signals), page 20 (6 signals), page 21 (6 signals), page 22 (6 signals), page 23 (6 signals), page 24 (6 signals), page 25 (6 signals), page 26 (6 signals), page 27 (6 signals), page 28 (6 signals), page 29 (6 signals), page 30 (6 signals), page 31 (6 signals), page 32 (6 signals), page 33 (6 signals), page 34 (6 signals), page 35 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
