---
layout: default
title: "DIF_oilPump (0x396) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Front drive inverter message: oil pump. Tesla Model 3 / Model Y CAN bus message DIF_oilPump (0x396) of Front drive inverter, firmware 2026.26.6.5, 10 signals (DIF_oilPumpState, DIF_oilPumpFluidTQF, DIF_oilPumpLeadAngle, DIF_oilPumpFlowTarget and 6 more). Bit layout, scaling, units and value tables."
---

# DIF_oilPump (0x396) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Front drive inverter message: oil pump; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of DIF_oilPump as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_oilPump` |
| CAN id | 0x396 (918) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of DIF_oilPump

Tesla Model 3 / Model Y CAN bus signals in `DIF_oilPump`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_oilPumpState` | Reports the state of the oil pump; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OIL_PUMP_STANDBY`<br>1 = `OIL_PUMP_ENABLE`<br>2 = `OIL_PUMP_COLD_STARTUP`<br>6 = `OIL_PUMP_FAULTED`<br>7 = `OIL_PUMP_SNA` | plausible |
| `DIF_oilPumpFluidTQF` | Front drive inverter: oil pump fluid TQF | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OIL_PUMP_FLUIDT_LOW_CONFIDENCE`<br>1 = `OIL_PUMP_FLUIDT_HIGH_CONFIDENCE` | plausible |
| `DIF_oilPumpLeadAngle` | Front drive inverter: oil pump lead angle | 4\|4 | little-endian | unsigned | 1.875 | 0 | degrees | 0 to 28.125 |  | plausible |
| `DIF_oilPumpFlowTarget` | Detects oil pump flow target; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_oilPumpFlowActual` | Detects oil pump flow; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_oilPumpFluidT` | Detects oil pump fluid tester; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 214 | 255 = `SNA` | plausible |
| `DIF_oilPumpPhaseCurrent` | Front drive inverter: oil pump phase current; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_oilPumpPressureEstimate` | Oil pump pressure estimate; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 2 | 0 | kPa | 0 to 500 | 255 = `SNA` | plausible |
| `DIF_oilPumpPressureExpected` | Oil pump pressure expected; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 2 | 0 | kPa | 0 to 500 | 255 = `SNA` | plausible |
| `DIF_oilPumpPressureResidual` | Oil pressure error outside of allowed tolerance; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 4 | -500 | kPa | -500 to 500 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
