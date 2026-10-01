---
layout: default
title: "DIR_oilPump (0x395) — Rear drive inverter, Tesla Model 3 2025.20.8 VEH CAN"
description: "Rear drive inverter message: oil pump. Tesla Model 3 CAN bus message DIR_oilPump (0x395) of Rear drive inverter, firmware 2025.20.8, 10 signals (DIR_oilPumpState, DIR_oilPumpFluidTQF, DIR_oilPumpLeadAngle, DIR_oilPumpFlowTarget and 6 more). Bit layout, scaling, units and value tables."
---

# DIR_oilPump (0x395) — Rear drive inverter, Tesla Model 3 2025.20.8 VEH CAN

Rear drive inverter message: oil pump; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of DIR_oilPump as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_oilPump` |
| CAN id | 0x395 (917) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of DIR_oilPump

Tesla Model 3 CAN bus signals in `DIR_oilPump`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_oilPumpState` | Reports the state of the oil pump; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OIL_PUMP_STANDBY`<br>1 = `OIL_PUMP_ENABLE`<br>2 = `OIL_PUMP_COLD_STARTUP`<br>6 = `OIL_PUMP_FAULTED`<br>7 = `OIL_PUMP_SNA` | plausible |
| `DIR_oilPumpFluidTQF` | Rear drive inverter: oil pump fluid TQF | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OIL_PUMP_FLUIDT_LOW_CONFIDENCE`<br>1 = `OIL_PUMP_FLUIDT_HIGH_CONFIDENCE` | plausible |
| `DIR_oilPumpLeadAngle` | Rear drive inverter: oil pump lead angle | 4\|4 | little-endian | unsigned | 1.875 | 0 | degrees | 0 to 28.125 |  | plausible |
| `DIR_oilPumpFlowTarget` | Detects oil pump flow target; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIR_oilPumpFlowActual` | Detects oil pump flow; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIR_oilPumpFluidT` | Detects oil pump fluid tester; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 214 | 255 = `SNA` | plausible |
| `DIR_oilPumpPhaseCurrent` | Rear drive inverter: oil pump phase current; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIR_oilPumpPressureEstimate` | Oil pump pressure estimate; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 2 | 0 | kPa | 0 to 500 | 255 = `SNA` | plausible |
| `DIR_oilPumpPressureExpected` | Oil pump pressure expected; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 2 | 0 | kPa | 0 to 500 | 255 = `SNA` | plausible |
| `DIR_oilPumpPressureResidual` | Oil pressure error outside of allowed tolerance; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | -500 | kPa | -500 to 500 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
