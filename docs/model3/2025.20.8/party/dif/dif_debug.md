---
layout: default
title: "DIF_debug (0x757) — Front drive inverter, Tesla Model 3 2025.20.8 PARTY CAN"
description: "Front drive inverter message: debug. Tesla Model 3 CAN bus message DIF_debug (0x757) of Front drive inverter, firmware 2025.20.8, 14 signals (DIF_debugSelector, DIF_phaseOutBusbarTemp, DIF_phaseOutBusbarWeldTemp, DIF_phaseOutLugTemp and 10 more). Bit layout, scaling, units and value tables."
---

# DIF_debug (0x757) — Front drive inverter, Tesla Model 3 2025.20.8 PARTY CAN

Front drive inverter message: debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of DIF_debug as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_debug` |
| CAN id | 0x757 (1879) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of DIF_debug

Tesla Model 3 CAN bus signals in `DIF_debug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_debugSelector` | selector | Front drive inverter: debug selector | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 32 = `Mux32`<br>33 = `Mux33`<br>34 = `Mux34`<br>35 = `Mux35`<br>36 = `Mux36`<br>37 = `Mux37`<br>38 = `Mux38`<br>39 = `Mux39`<br>40 = `Mux40`<br>41 = `Mux41`<br>42 = `Mux42`<br>43 = `Mux43`<br>44 = `Mux44`<br>46 = `Mux46`<br>47 = `Mux47`<br>48 = `Mux48`<br>49 = `Mux49`<br>50 = `Mux50`<br>52 = `Mux52`<br>63 = `Mux63`<br>64 = `Mux64`<br>66 = `Mux66`<br>67 = `Mux67`<br>68 = `Mux68`<br>69 = `Mux69`<br>70 = `Mux70`<br>72 = `Mux72`<br>128 = `Mux128`<br>131 = `Mux131`<br>132 = `Mux132` | plausible |
| `DIF_phaseOutBusbarTemp` | page 70 | Front drive inverter: phase out busbar temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_phaseOutBusbarWeldTemp` | page 70 | Front drive inverter: phase out busbar weld temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_phaseOutLugTemp` | page 70 | Front drive inverter: phase out lug temp; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_dcLinkCapTemp` | page 70 | Front drive inverter: dc link cap temp; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_hvDcCableTemp` | page 70 | Front drive inverter: hv dc cable temp; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_negDcBusbarTemp` | page 70 | Front drive inverter: neg dc busbar temp; raw 0 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_posDcBusbarTemp` | page 70 | Front drive inverter: pos dc busbar temp; raw 0 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_statorEndWindingTemp` | page 72 | Front drive inverter: stator end winding temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_rotorMaxMagnetTemp` | page 72 | Reports the maximum temperature of the rotor magnet; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_lightSenseV` | page 72 | Front drive inverter: light sense v | 24\|6 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3.3 |  | validated |
| `DIF_pyroSenseV` | page 72 | Front drive inverter: pyro sense v | 30\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 3.3 |  | validated |
| `DIF_statorSlotWindingTemp` | page 72 | Front drive inverter: stator slot winding temp; raw 0 = signal not available (SNA) | 46\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_intervalMaxHvBusV` | page 72 | Front drive inverter: interval max hv bus v | 54\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |

## Multiplexing

`DIF_debugSelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 70 (7 signals), page 72 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
