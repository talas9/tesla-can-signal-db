---
layout: default
title: "VCRIGHT_hvacRequest (0x20C) — Right body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Right body controller message: hvac request. Tesla Model Y CAN bus message VCRIGHT_hvacRequest (0x20C) of Right body controller, firmware 2025.20.8, 15 signals (VCRIGHT_wattsDemandEvap, VCRIGHT_hvacEvapEnabled, VCRIGHT_conditioningRequest, VCRIGHT_tempEvaporator and 11 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_hvacRequest (0x20C) — Right body controller, Tesla Model Y 2025.20.8 VEH CAN

Right body controller message: hvac request; frame length observed on a vehicle bus. This page documents the 15 signals of VCRIGHT_hvacRequest as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_hvacRequest` |
| CAN id | 0x20C (524) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 15 |

## Signals of VCRIGHT_hvacRequest

Tesla Model Y CAN bus signals in `VCRIGHT_hvacRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_wattsDemandEvap` | Right body controller: watts demand evap | 0\|11 | little-endian | unsigned | 5 | 0 | W | 0 to 10000 |  | validated |
| `VCRIGHT_hvacEvapEnabled` | Right body controller: hvac evap enabled | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_conditioningRequest` | Right body controller: conditioning request | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_tempEvaporator` | Evaporator temperature; raw 2047 = signal not available (SNA) | 13\|11 | little-endian | unsigned | 0.1 | -40 | degC | -40 to 105 | 2047 = `SNA` | validated |
| `VCRIGHT_tempEvaporatorTarget` | Evaporator temperature target; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.2 | 0 | degC | 0 to 50 | 255 = `SNA` | validated |
| `VCRIGHT_hvacBlowerSpeedRPMReq` | Right body controller: hvac blower speed RPM req | 32\|10 | little-endian | unsigned | 5 | 0 | RPM | 0 to 5115 |  | validated |
| `VCRIGHT_hvacPerfTestRunning` | Right body controller: hvac perf test running | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_evapPerformanceLow` | Right body controller: evap performance low | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_tempAmbientRaw` | Right body controller: temp ambient raw; raw 0 = signal not available (SNA) | 44\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 80 | 0 = `SNA` | validated |
| `VCRIGHT_hvacHeatingEnabledLeft` | Right body controller: hvac heating enabled left | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacHeatingEnabledRight` | Right body controller: hvac heating enabled right | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacPerfTestState` | The HVAC performance test running state | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STOPPED`<br>1 = `WAITING`<br>2 = `BLOWING` | validated |
| `VCRIGHT_hvacUnavailable` | Right body controller: hvac unavailable | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacBlowerRPMActualAP` | Right body controller: hvac blower RPM actual AP | 57\|5 | little-endian | unsigned | 200 | 0 | rpm | 0 to 4200 |  | validated |
| `VCRIGHT_hvacEvapEnabledInColdAmbient` | Right body controller: hvac evap enabled in cold ambient | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
