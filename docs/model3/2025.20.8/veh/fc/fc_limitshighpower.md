---
layout: default
title: "FC_limitsHighPower (0x2BE) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: limits high power. Tesla Model 3 CAN bus message FC_limitsHighPower (0x2BE) of FC ECU, firmware 2025.20.8, 6 signals (FC_powerLimit_value, FC_currentLimit_value, FC_minVoltageLimit_value, FC_powerLimit_exp and 2 more). Bit layout, scaling, units and value tables."
---

# FC_limitsHighPower (0x2BE) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: limits high power; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of FC_limitsHighPower as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_limitsHighPower` |
| CAN id | 0x2BE (702) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of FC_limitsHighPower

Tesla Model 3 CAN bus signals in `FC_limitsHighPower`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_powerLimit_value` | Instantaneous power charger can deliver. Mantissa portion of extended range version of legacy signal, used with protocol versions 9+. FC_powerLimit = value * 10^exp; raw 32768 = signal not available (SNA) | 0\|16 | little-endian | signed | 1 | 0 | *10^exp kW | -32767 to 32767 | -32768 = `SNA` | plausible |
| `FC_currentLimit_value` | FC ECU: current limit value; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 1 | 0 | *10^exp A | -32767 to 32767 | -32768 = `SNA` | plausible |
| `FC_minVoltageLimit_value` | FC ECU: min voltage limit value; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 1 | 0 | *10^exp V | -32767 to 32767 | -32768 = `SNA` | plausible |
| `FC_powerLimit_exp` | Instantaneous power charger can deliver. Exponent portion of extended ragne version of legacy signal, used with protocol versions 9+. FC_powerLimit = value * 10^exp. | 48\|3 | little-endian | signed | 1 | 0 |  | -4 to 3 |  | plausible |
| `FC_currentLimit_exp` | FC ECU: current limit exp | 51\|3 | little-endian | signed | 1 | 0 |  | -4 to 3 |  | layout-only |
| `FC_minVoltageLimit_exp` | FC ECU: min voltage limit exp | 54\|3 | little-endian | signed | 1 | 0 |  | -4 to 3 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
