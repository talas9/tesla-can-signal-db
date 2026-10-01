---
layout: default
title: "DIR_debug (0x7D5) — Rear drive inverter, Tesla Model 3 2025.20.8 VEH CAN"
description: "Rear drive inverter message: debug. Tesla Model 3 CAN bus message DIR_debug (0x7D5) of Rear drive inverter, firmware 2025.20.8, 14 signals (DIR_debugSelector, DIR_phaseOutBusbarTemp, DIR_phaseOutBusbarWeldTemp, DIR_phaseOutLugTemp and 10 more). Bit layout, scaling, units and value tables."
---

# DIR_debug (0x7D5) — Rear drive inverter, Tesla Model 3 2025.20.8 VEH CAN

Rear drive inverter message: debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of DIR_debug as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_debug` |
| CAN id | 0x7D5 (2005) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of DIR_debug

Tesla Model 3 CAN bus signals in `DIR_debug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_debugSelector` | selector | Rear drive inverter: debug selector | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 32 = `Mux32`<br>33 = `Mux33`<br>34 = `Mux34`<br>35 = `Mux35`<br>36 = `Mux36`<br>37 = `Mux37`<br>38 = `Mux38`<br>39 = `Mux39`<br>40 = `Mux40`<br>41 = `Mux41`<br>42 = `Mux42`<br>43 = `Mux43`<br>44 = `Mux44`<br>46 = `Mux46`<br>47 = `Mux47`<br>48 = `Mux48`<br>49 = `Mux49`<br>50 = `Mux50`<br>52 = `Mux52`<br>63 = `Mux63`<br>64 = `Mux64`<br>66 = `Mux66`<br>67 = `Mux67`<br>68 = `Mux68`<br>69 = `Mux69`<br>70 = `Mux70`<br>72 = `Mux72`<br>128 = `Mux128`<br>131 = `Mux131`<br>132 = `Mux132` | plausible |
| `DIR_phaseOutBusbarTemp` | page 70 | Rear drive inverter: phase out busbar temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_phaseOutBusbarWeldTemp` | page 70 | Rear drive inverter: phase out busbar weld temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_phaseOutLugTemp` | page 70 | Rear drive inverter: phase out lug temp; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_dcLinkCapTemp` | page 70 | Rear drive inverter: dc link cap temp; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_hvDcCableTemp` | page 70 | Rear drive inverter: hv dc cable temp; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_negDcBusbarTemp` | page 70 | Rear drive inverter: neg dc busbar temp; raw 0 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_posDcBusbarTemp` | page 70 | Rear drive inverter: pos dc busbar temp; raw 0 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_statorEndWindingTemp` | page 72 | Rear drive inverter: stator end winding temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_rotorMaxMagnetTemp` | page 72 | Reports the maximum temperature of the rotor magnet; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_lightSenseV` | page 72 | Rear drive inverter: light sense v | 24\|6 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3.3 |  | plausible |
| `DIR_pyroSenseV` | page 72 | Rear drive inverter: pyro sense v | 30\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 3.3 |  | plausible |
| `DIR_statorSlotWindingTemp` | page 72 | Rear drive inverter: stator slot winding temp; raw 0 = signal not available (SNA) | 46\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `DIR_intervalMaxHvBusV` | page 72 | Rear drive inverter: interval max hv bus v | 54\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | plausible |

## Multiplexing

`DIR_debugSelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 70 (7 signals), page 72 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
