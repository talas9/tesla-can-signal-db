---
layout: default
title: "VCLEFT_logging1Hz (0x3A8) — Left body controller, Tesla Model Y 2025.20.8 ETH"
description: "Left body controller message: logging1 hz. Ethernet-side message VCLEFT_logging1Hz of Left body controller for Tesla Model Y firmware 2025.20.8, 9 signals (VCLEFT_logging1HzIndex, VCLEFT_tohcPCBATemperature, VCLEFT_phoneChargingFL, VCLEFT_phoneChargingFR and 5 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_logging1Hz (0x3A8) — Left body controller, Tesla Model Y 2025.20.8 ETH

Left body controller message: logging1 hz. This page documents the 9 signals of VCLEFT_logging1Hz as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_logging1Hz` |
| Ethernet-side id | 0x3A8 (936) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 333 ms |
| Signals | 9 |

## Signals of VCLEFT_logging1Hz

Tesla Model Y CAN bus signals in `VCLEFT_logging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_logging1HzIndex` | selector | Left body controller: logging1 hz index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MISC`<br>1 = `HSD_CURRENTS_1`<br>2 = `HSD_CURRENTS_2`<br>3 = `END` | plausible |
| `VCLEFT_tohcPCBATemperature` | page 0 | Left body controller: tohc PCBA temperature; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | plausible |
| `VCLEFT_phoneChargingFL` | page 0 | Charging status of front left wireless phone charger (if installed) | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_phoneChargingFR` | page 0 | Charging status of front right wireless phone charger (if installed) | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_swcResistance` | page 0 | Left body controller: swc resistance; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.025 | 0 | Ohm | 0 to 3.15 | 127 = `SNA` | plausible |
| `VCLEFT_frontSeatHeatCushionPwr` | page 0 | Left body controller: front seat heat cushion pwr | 32\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | plausible |
| `VCLEFT_frontSeatHeatBackrestPwr` | page 0 | Left body controller: front seat heat backrest pwr | 40\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | plausible |
| `VCLEFT_12vSocketFrontCurrent` | page 0 | Left body controller: 12v socket front current; raw 127 = signal not available (SNA) | 48\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.5 | 127 = `SNA` | plausible |
| `VCLEFT_12vSocketRearCurrent` | page 0 | Left body controller: 12v socket rear current; raw 127 = signal not available (SNA) | 56\|7 | little-endian | unsigned | 0.25 | 0 | A | 0 to 31.5 | 127 = `SNA` | plausible |

## Multiplexing

`VCLEFT_logging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
