---
layout: default
title: "VCLEFT_thermalLogging1Hz (0x291) — Left body controller, Tesla Model 3 2025.20.8 ETH"
description: "Left body controller message: thermal logging1 hz. Ethernet-side message VCLEFT_thermalLogging1Hz of Left body controller for Tesla Model 3 firmware 2025.20.8, 13 signals (VCLEFT_thermalLogging1HzIndex, VCLEFT_hvac2RLeftLateralZeroStopVoltage, VCLEFT_hvac2RLeftVerticalZeroStopVoltage, VCLEFT_hvac2RRightLateralZeroStopVoltage and 9 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_thermalLogging1Hz (0x291) — Left body controller, Tesla Model 3 2025.20.8 ETH

Left body controller message: thermal logging1 hz. This page documents the 13 signals of VCLEFT_thermalLogging1Hz as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_thermalLogging1Hz` |
| Ethernet-side id | 0x291 (657) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 13 |

## Signals of VCLEFT_thermalLogging1Hz

Tesla Model 3 CAN bus signals in `VCLEFT_thermalLogging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_thermalLogging1HzIndex` | selector | Left body controller: thermal logging1 hz index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `ZEROSTOP`<br>1 = `ENDSTOP`<br>2 = `END`<br>15 = `MAX` | plausible |
| `VCLEFT_hvac2RLeftLateralZeroStopVoltage` | page 0 | Left body controller: hvac2 r left lateral zero stop voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalZeroStopVoltage` | page 0 | Left body controller: hvac2 r left vertical zero stop voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightLateralZeroStopVoltage` | page 0 | Left body controller: hvac2 r right lateral zero stop voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightVerticalZeroStopVoltage` | page 0 | Left body controller: hvac2 r right vertical zero stop voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RLeftLateralEndStopVoltage` | page 1 | Left body controller: hvac2 r left lateral end stop voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalEndStopVoltage` | page 1 | Left body controller: hvac2 r left vertical end stop voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightLateralEndStopVoltage` | page 1 | Left body controller: hvac2 r right lateral end stop voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightVerticalEndStopVoltage` | page 1 | Left body controller: hvac2 r right vertical end stop voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvacBlowerArbState` | page 1 | Left body controller: hvac blower arb state | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARBITRATOR_NOT_READY`<br>1 = `ARBITRATOR_READY`<br>2 = `ARBITRATOR_HIGH_FREQ_VOLT_INJECTION`<br>3 = `ARBITRATOR_WAIT_BEFORE_REQUEST`<br>4 = `ARBITRATOR_REQUEST_CURRENT`<br>5 = `ARBITRATOR_COMPLETED`<br>6 = `ARBITRATOR_FAULTED` | plausible |
| `VCLEFT_hvacBlowerArbResult` | page 1 | Left body controller: hvac blower arb result | 43\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_MOTOR_ID_UNKNOWN`<br>1 = `VC_MOTOR_ID_DELTA`<br>2 = `VC_MOTOR_ID_BOSCH` | plausible |
| `VCLEFT_hvacBlowerArbCurrent` | page 1 | Left body controller: hvac blower arb current | 48\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | plausible |
| `VCLEFT_hvacBlowerTorqueIndexFiltered` | page 1 | Left body controller: hvac blower torque index filtered | 56\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |

## Multiplexing

`VCLEFT_thermalLogging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
