---
layout: default
title: "VCLEFT_thermalLogging1Hz (0x291) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: thermal logging1 hz. Tesla Model 3 CAN bus message VCLEFT_thermalLogging1Hz (0x291) of Left body controller, firmware 2026.26.6.5, 11 signals (VCLEFT_thermalLogging1HzIndex, VCLEFT_hvac2RLeftLateralZeroStopVoltage, VCLEFT_hvac2RLeftVerticalZeroStopVoltage, VCLEFT_hvac2RRightLateralZeroStopVoltage and 7 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_thermalLogging1Hz (0x291) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: thermal logging1 hz; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of VCLEFT_thermalLogging1Hz as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_thermalLogging1Hz` |
| CAN id | 0x291 (657) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 7 bytes |
| Cycle time | 500 ms |
| Signals | 11 |

## Signals of VCLEFT_thermalLogging1Hz

Tesla Model 3 CAN bus signals in `VCLEFT_thermalLogging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_thermalLogging1HzIndex` | selector | Left body controller: thermal logging1 hz index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `ZEROSTOP`<br>1 = `ENDSTOP`<br>2 = `END`<br>15 = `MAX` | plausible |
| `VCLEFT_hvac2RLeftLateralZeroStopVoltage` | page 0 | Left body controller: hvac2 r left lateral zero stop voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RLeftVerticalZeroStopVoltage` | page 0 | Left body controller: hvac2 r left vertical zero stop voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightLateralZeroStopVoltage` | page 0 | Left body controller: hvac2 r right lateral zero stop voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightVerticalZeroStopVoltage` | page 0 | Left body controller: hvac2 r right vertical zero stop voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RLeftLateralEndStopVoltage` | page 1 | Left body controller: hvac2 r left lateral end stop voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RLeftVerticalEndStopVoltage` | page 1 | Left body controller: hvac2 r left vertical end stop voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightLateralEndStopVoltage` | page 1 | Left body controller: hvac2 r right lateral end stop voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightVerticalEndStopVoltage` | page 1 | Left body controller: hvac2 r right vertical end stop voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvacBlowerArbCurrent` | page 1 | Left body controller: hvac blower arb current | 40\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | validated |
| `VCLEFT_hvacBlowerTorqueIndexFiltered` | page 1 | Left body controller: hvac blower torque index filtered | 48\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |

## Multiplexing

`VCLEFT_thermalLogging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
