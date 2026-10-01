---
layout: default
title: "HVP_log1hz (0x77A) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: log1hz. Tesla Model 3 CAN bus message HVP_log1hz (0x77A) of High-voltage processor (pack contactor and isolation controller), firmware 2025.20.8, 14 signals (HVP_log1HzIndex, HVP_bmbAsicType, HVP_shuntCurrentAuxLog, HVP_pyroSquibResistance and 10 more). Bit layout, scaling, units and value tables."
---

# HVP_log1hz (0x77A) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: log1hz; frame length observed on a vehicle bus. This page documents the 14 signals of HVP_log1hz as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_log1hz` |
| CAN id | 0x77A (1914) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of HVP_log1hz

Tesla Model 3 CAN bus signals in `HVP_log1hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_log1HzIndex` | selector | High-voltage processor (pack contactor and isolation controller): log1 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `HVP_bmbAsicType` | page 0 | The BMB Asic type being used by this battery pack for reading brick data | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `LTC831`<br>2 = `ADBMS6830`<br>3 = `BQ796xx` | plausible |
| `HVP_shuntCurrentAuxLog` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt current aux log | 8\|24 | little-endian | signed | 0.001 | 0 | A | -8388.607 to 8388.607 | 8388000 = `PACK_CURRENT_SNA` | plausible |
| `HVP_pyroSquibResistance` | page 0 | The pyro resistance measured on attempt to close contactor or by the Pyro selftest; raw 65535 = signal not available (SNA) | 32\|16 | little-endian | unsigned | 0.001 | 0 | Ohm | 0 to 65.534 | 65535 = `SNA` | plausible |
| `HVP_shuntAsicChipXCoordinate` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt asic chip x coordinate | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `HVP_shuntAsicChipYCoordinate` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt asic chip y coordinate | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `HVP_hvilCalType` | page 1 | High-voltage processor (pack contactor and isolation controller): hvil cal type | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `LV`<br>2 = `CAN` | plausible |
| `HVP_gpioPcsDcdcPwmEnable` | page 1 | High-voltage processor (pack contactor and isolation controller): gpio pcs dcdc pwm enable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPcsChargePwmEnable` | page 1 | High-voltage processor (pack contactor and isolation controller): gpio pcs charge pwm enable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPcsEnable` | page 1 | HVP GPIO control for PCS logic power enable line | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_shuntAsicChipWaferNumber` | page 1 | High-voltage processor (pack contactor and isolation controller): shunt asic chip wafer number | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `HVP_energyReserveMin` | page 1 | a lowest energy reserve value measured over sliding window | 16\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |
| `HVP_energyReserveMax` | page 1 | a highest energy reserve value measured over sliding window | 32\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |
| `HVP_energyReserveAvg` | page 1 | an average energy reserve value measured over sliding window | 48\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |

## Multiplexing

`HVP_log1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
