---
layout: default
title: "DAS_telemetryRadar (0x60C) — Driver assistance computer, Tesla Model Y 2026.26.6.5 ETH"
description: "Driver assistance computer message: telemetry radar. Ethernet-side message DAS_telemetryRadar of Driver assistance computer for Tesla Model Y firmware 2026.26.6.5, 11 signals (DAS_TR_ObjIndex, DAS_TR_Counter, DAS_TR_Obj00_Class, DAS_TR_Obj00_Dx and 7 more). Bit layout, scaling, units and value tables."
---

# DAS_telemetryRadar (0x60C) — Driver assistance computer, Tesla Model Y 2026.26.6.5 ETH

Driver assistance computer message: telemetry radar. This page documents the 11 signals of DAS_telemetryRadar as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_telemetryRadar` |
| Ethernet-side id | 0x60C (1548) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 5 ms |
| Signals | 11 |

## Signals of DAS_telemetryRadar

Tesla Model Y CAN bus signals in `DAS_telemetryRadar`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_TR_ObjIndex` | selector | Driver assistance computer: TR obj index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5`<br>6 = `Mux6`<br>7 = `Mux7`<br>8 = `Mux8`<br>9 = `Mux9`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12`<br>13 = `Mux13`<br>14 = `Mux14`<br>15 = `Mux15`<br>16 = `Mux16`<br>17 = `Mux17`<br>18 = `Mux18`<br>19 = `Mux19`<br>20 = `Mux20`<br>21 = `Mux21`<br>22 = `Mux22`<br>23 = `Mux23`<br>24 = `Mux24`<br>25 = `Mux25`<br>26 = `Mux26`<br>27 = `Mux27`<br>28 = `Mux28`<br>29 = `Mux29`<br>30 = `Mux30`<br>31 = `Mux31` | plausible |
| `DAS_TR_Counter` |  | Driver assistance computer: TR counter | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `DAS_TR_Obj00_Class` | page 0 | Driver assistance computer: TR obj00 class | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RADAR_CLASS_UNKNOWN`<br>1 = `RADAR_CLASS_MOVING_FOUR_WHEEL_VEHICLE`<br>2 = `RADAR_CLASS_MOVING_TWO_WHEEL_VEHICLE`<br>3 = `RADAR_CLASS_MOVING_PEDESTRIAN`<br>4 = `RADAR_CLASS_CONSTRUCTION_ELEMENT` | validated |
| `DAS_TR_Obj00_Dx` | page 0 | Driver assistance computer: TR obj00 dx | 8\|10 | little-endian | unsigned | 0.15625 | 0 | m | 0 to 159.84375 |  | validated |
| `DAS_TR_Obj00_Dy` | page 0 | Driver assistance computer: TR obj00 dy | 18\|6 | little-endian | unsigned | 0.5 | -15.5 | m | -15.5 to 16 |  | validated |
| `DAS_TR_Obj00_Vx` | page 0 | Driver assistance computer: TR obj00 vx | 24\|8 | little-endian | unsigned | 0.5 | -63.5 | m/s | -63.5 to 64 |  | validated |
| `DAS_TR_Obj00_RCS` | page 0 | Driver assistance computer: TR obj00 RCS | 32\|8 | little-endian | unsigned | 0.25 | -14 | dB | -14 to 49.75 |  | validated |
| `DAS_TR_Obj00_Length` | page 0 | Driver assistance computer: TR obj00 length | 40\|6 | little-endian | unsigned | 0.125 | 0 | m | 0 to 7.875 |  | validated |
| `DAS_TR_Obj00_MovingState` | page 0 | Driver assistance computer: TR obj00 moving state | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RADAR_MOVESTATE_INDETERMINATE`<br>1 = `RADAR_MOVESTATE_MOVING`<br>2 = `RADAR_MOVESTATE_STOPPED`<br>3 = `RADAR_MOVESTATE_STANDING` | validated |
| `DAS_TR_Obj00_Dz` | page 0 | Driver assistance computer: TR obj00 dz | 48\|6 | little-endian | unsigned | 0.25 | -5 | m | -5 to 10.75 |  | validated |
| `DAS_TR_Obj00_Exist` | page 0 | Driver assistance computer: TR obj00 exist | 56\|5 | little-endian | unsigned | 3.125 | 0 | % | 0 to 96.875 |  | validated |

## Multiplexing

`DAS_TR_ObjIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
