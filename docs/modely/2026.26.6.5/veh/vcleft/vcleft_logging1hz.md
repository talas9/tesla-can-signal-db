---
layout: default
title: "VCLEFT_logging1Hz (0x3A8) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: logging1 hz. Tesla Model Y CAN bus message VCLEFT_logging1Hz (0x3A8) of Left body controller, firmware 2026.26.6.5, 16 signals (VCLEFT_logging1HzIndex, VCLEFT_tohcPCBATemperature, VCLEFT_phoneChargingFL, VCLEFT_phoneChargingFR and 12 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_logging1Hz (0x3A8) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Left body controller message: logging1 hz; frame length observed on a vehicle bus. This page documents the 16 signals of VCLEFT_logging1Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_logging1Hz` |
| CAN id | 0x3A8 (936) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 16 |

## Signals of VCLEFT_logging1Hz

Tesla Model Y CAN bus signals in `VCLEFT_logging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_logging1HzIndex` | selector | Left body controller: logging1 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MISC`<br>1 = `HSD_CURRENTS_1`<br>2 = `HSD_CURRENTS_2`<br>3 = `BODY_CONTROLS_LOGGING`<br>4 = `CURRENT_LOGGING`<br>5 = `END` | validated |
| `VCLEFT_tohcPCBATemperature` | page 0 | Left body controller: tohc PCBA temperature; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | validated |
| `VCLEFT_phoneChargingFL` | page 0 | Charging status of front left wireless phone charger (if installed) | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_phoneChargingFR` | page 0 | Charging status of front right wireless phone charger (if installed) | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_swcResistance` | page 0 | Left body controller: swc resistance; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.025 | 0 | Ohm | 0 to 3.15 | 127 = `SNA` | validated |
| `VCLEFT_frontSeatHeatCushionPwr` | page 0 | Left body controller: front seat heat cushion pwr | 32\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | validated |
| `VCLEFT_frontSeatHeatBackrestPwr` | page 0 | Left body controller: front seat heat backrest pwr | 40\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | validated |
| `VCLEFT_rgbLedIPFLCurrent` | page 3 | Current drawn by the IPFL RGB LED | 3\|10 | little-endian | unsigned | 0.000488758552819 | 0 | A | 0 to 0.499999999534 |  | validated |
| `VCLEFT_rgbLedIPFRCurrent` | page 3 | Current drawn by the IPFR RGB LED | 13\|10 | little-endian | unsigned | 0.000488758552819 | 0 | A | 0 to 0.499999999534 |  | validated |
| `VCLEFT_rgbLedIPFLOutput` | page 3 | The power state of the IPFL RGB LED | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rgbLedIPFROutput` | page 3 | The power state of the IPFR RGB LED | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rgbLedFrontCurrent` | page 3 | Current drawn by the front door RGB LED | 25\|10 | little-endian | unsigned | 0.000488758552819 | 0 | A | 0 to 0.499999999534 |  | validated |
| `VCLEFT_rgbLedRearCurrent` | page 3 | Current drawn by the rear door RGB LED | 35\|10 | little-endian | unsigned | 0.000488758552819 | 0 | A | 0 to 0.499999999534 |  | validated |
| `VCLEFT_rgbLedFrontOutput` | page 3 | The power state of the front door RGB LED | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rgbLedRearOutput` | page 3 | The power state of the rear door RGB LED | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_seat2RControllerCurrent` | page 3 | Left body controller: seat2 r controller current | 55\|9 | little-endian | unsigned | 0.2 | 0 | A | 0 to 102 |  | validated |

## Multiplexing

`VCLEFT_logging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 3 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
