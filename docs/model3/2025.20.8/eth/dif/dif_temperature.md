---
layout: default
title: "DIF_temperature (0x376) — Front drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Front drive inverter message: temperature. Ethernet-side message DIF_temperature of Front drive inverter for Tesla Model 3 firmware 2025.20.8, 20 signals (DIF_tempIndex, DIF_inverterTQF, DIF_pcbT, DIF_inverterT and 16 more). Bit layout, scaling, units and value tables."
---

# DIF_temperature (0x376) — Front drive inverter, Tesla Model 3 2025.20.8 ETH

Front drive inverter message: temperature. This page documents the 20 signals of DIF_temperature as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_temperature` |
| Ethernet-side id | 0x376 (886) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 20 |

## Signals of DIF_temperature

Tesla Model 3 CAN bus signals in `DIF_temperature`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_tempIndex` | selector | Front drive inverter: temp index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4` | plausible |
| `DIF_inverterTQF` | page 0 | Detects the Drive Inverter (DI) outlet temperature qualifier. | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVERTERT_INIT`<br>1 = `INVERTERT_IRRATIONAL`<br>2 = `INVERTERT_RATIONAL`<br>3 = `INVERTERT_UNKNOWN` | plausible |
| `DIF_pcbT` | page 0 | Front drive inverter: pcb t; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIF_inverterT` | page 0 | Drive Inverter measured outlet temperature | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_statorT` | page 0 | Drive Inverter measured stator temperature; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIF_dcCapT` | page 0 | Front drive inverter: dc cap t; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIF_heatsinkT` | page 0 | Drive Inverter measured heatsink temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIF_inverterTpct` | page 0 | Front drive inverter: inverter tpct | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `DIF_statorTpct` | page 0 | Front drive inverter: stator tpct | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `DIF_fluidInTemp` | page 2 | Inlet fluid temperature; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIF_normalFetBurnIn` | page 2 | Front drive inverter: normal fet burn in; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.00763 | 0 | Hours | 0 to 500 | 65535 = `SNA` | plausible |
| `DIF_additionalFetBurnIn` | page 2 | Front drive inverter: additional fet burn in; raw 65535 = signal not available (SNA) | 32\|16 | little-endian | unsigned | 0.00763 | 0 | Hours | 0 to 500 | 65535 = `SNA` | plausible |
| `DIF_currentWeibullMiles` | page 3 | Front drive inverter: current weibull miles; raw 32767 = signal not available (SNA) | 3\|16 | little-endian | unsigned | 8 | 0 | miles | 0 to 500000 | 32767 = `SNA` | plausible |
| `DIF_endOfServiceWeibullMiles` | page 3 | Front drive inverter: end of service weibull miles; raw 32767 = signal not available (SNA) | 19\|16 | little-endian | unsigned | 8 | 0 | miles | 0 to 500000 | 32767 = `SNA` | plausible |
| `DIF_burnInDamageRatio` | page 3 | Front drive inverter: burn in damage ratio; raw 511 = signal not available (SNA) | 35\|9 | little-endian | unsigned | 0.01 | 0 | 1 | 0 to 5 | 510 = `DEFAULT_1`<br>511 = `SNA` | plausible |
| `DIF_inverterSensorEst` | page 3 | Front drive inverter: inverter sensor est | 44\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 120 |  | plausible |
| `DIF_inverterHS1Est` | page 3 | Front drive inverter: inverter HS1 est | 52\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 120 |  | plausible |
| `DIF_initialBurnInVehicleOdometer` | page 4 | Front drive inverter: initial burn in vehicle odometer; raw 4294967295 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 0.001 | 0 | km | 0 to 4294967.294 | 4294967295 = `SNA` | plausible |
| `DIF_inverterHS2Est` | page 4 | Front drive inverter: inverter HS2 est | 40\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 120 |  | plausible |
| `DIF_inverterInletEst` | page 4 | Front drive inverter: inverter inlet est | 48\|8 | little-endian | unsigned | 1 | -40 | C | -40 to 120 |  | plausible |

## Multiplexing

`DIF_tempIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (8 signals), page 2 (3 signals), page 3 (5 signals), page 4 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
