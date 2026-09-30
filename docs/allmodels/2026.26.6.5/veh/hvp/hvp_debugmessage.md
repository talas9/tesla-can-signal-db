---
layout: default
title: "HVP_debugMessage (0x7AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: debug message. Tesla Model 3 / Model Y CAN bus message HVP_debugMessage (0x7AA) of High-voltage processor (pack contactor and isolation controller), firmware 2026.26.6.5, 24 signals (HVP_debugMessageMultiplexer, HVP_ecuLogUploadRequest, HVP_dcLinkVoltage, HVP_packVoltage and 20 more). Bit layout, scaling, units and value tables."
---

# HVP_debugMessage (0x7AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: debug message; frame length observed on a vehicle bus. This page documents the 24 signals of HVP_debugMessage as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_debugMessage` |
| CAN id | 0x7AA (1962) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 24 |

## Signals of HVP_debugMessage

Tesla Model 3 / Model Y CAN bus signals in `HVP_debugMessage`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_debugMessageMultiplexer` | selector | High-voltage processor (pack contactor and isolation controller): debug message multiplexer | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5`<br>6 = `Mux6`<br>7 = `Mux7`<br>8 = `Mux8`<br>9 = `Mux9`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12` | plausible |
| `HVP_ecuLogUploadRequest` | page 1 | High-voltage processor (pack contactor and isolation controller): ecu log upload request | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REQUEST_PRIORITY_NONE`<br>1 = `REQUEST_PRIORITY_1`<br>2 = `REQUEST_PRIORITY_2`<br>3 = `REQUEST_PRIORITY_3` | validated |
| `HVP_dcLinkVoltage` | page 1 | The HVP's measurement of the DC link voltage | 8\|16 | little-endian | signed | 0.1 | 0 | V | -3276.8 to 3276.7 |  | validated |
| `HVP_packVoltage` | page 1 | High-voltage processor (pack contactor and isolation controller): pack voltage | 24\|16 | little-endian | signed | 0.1 | 0 | V | -3276.8 to 3276.7 |  | validated |
| `HVP_fcLinkVoltage` | page 1 | Measured voltage on FC link | 40\|16 | little-endian | signed | 0.1 | 0 | V | -3276.8 to 3276.7 |  | validated |
| `HVP_10HzTask_stackUsage` | page 1 | High-voltage processor (pack contactor and isolation controller): 10 hz task stack usage | 56\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `HVP_packContVoltage` | page 2 | High-voltage processor (pack contactor and isolation controller): pack cont voltage | 4\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | validated |
| `HVP_packNegativeV` | page 2 | The HVP's common-mode measurement of PACK-HV-SENSE-NEG relative to chassis ground | 16\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | validated |
| `HVP_packPositiveV` | page 2 | The HVP's common-mode measurement of PACK-HV-SENSE-POS relative to chassis ground | 32\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | validated |
| `HVP_pyroAnalog` | page 2 | High-voltage processor (pack contactor and isolation controller): pyro analog | 48\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3 |  | contradicted |
| `HVP_shuntSetTCRCoeffA` | page 2 | High-voltage processor (pack contactor and isolation controller): shunt set TCR coeff a | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_shuntSetTCRCoeffB` | page 2 | High-voltage processor (pack contactor and isolation controller): shunt set TCR coeff b | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_shuntSetTCRCoeffC` | page 2 | High-voltage processor (pack contactor and isolation controller): shunt set TCR coeff c | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_shuntSetTCRCoeffD` | page 2 | High-voltage processor (pack contactor and isolation controller): shunt set TCR coeff d | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_fcContCoilCurrent` | page 4 | High-voltage processor (pack contactor and isolation controller): fc cont coil current | 4\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 7.5 |  | validated |
| `HVP_fcContVoltage` | page 4 | High-voltage processor (pack contactor and isolation controller): fc cont voltage | 16\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | validated |
| `HVP_hvilInVoltage` | page 4 | Measured HVIL input voltage | 28\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | validated |
| `HVP_hvilOutVoltage` | page 4 | Measured HVIL output voltage | 40\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | validated |
| `HVP_shuntGainInvalidCountDbg` | page 4 | High-voltage processor (pack contactor and isolation controller): shunt gain invalid count dbg | 56\|8 | little-endian | unsigned | 1 | 0 | counts | 0 to 255 |  | validated |
| `HVP_passivePyroRefVoltageMax` | page 5 | High-voltage processor (pack contactor and isolation controller): passive pyro ref voltage max; raw 1023 = signal not available (SNA) | 4\|10 | little-endian | unsigned | 0.001 | 0.7 | V | 0.7 to 1.722 | 1023 = `SNA` | validated |
| `HVP_passivePyroRefVoltageMin` | page 5 | High-voltage processor (pack contactor and isolation controller): passive pyro ref voltage min; raw 1023 = signal not available (SNA) | 14\|10 | little-endian | unsigned | 0.001 | 0.7 | V | 0.7 to 1.722 | 1023 = `SNA` | validated |
| `HVP_packContCoilCurrent` | page 5 | High-voltage processor (pack contactor and isolation controller): pack cont coil current | 24\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 7.5 |  | validated |
| `HVP_battery12V` | page 5 | Monitored voltage sense of 12V battery | 36\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | validated |
| `HVP_fcLinkPositiveV` | page 5 | High-voltage processor (pack contactor and isolation controller): fc link positive v | 48\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | validated |

## Multiplexing

`HVP_debugMessageMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals), page 2 (8 signals), page 4 (5 signals), page 5 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
