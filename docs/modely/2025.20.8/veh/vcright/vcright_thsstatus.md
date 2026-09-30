---
layout: default
title: "VCRIGHT_thsStatus (0x383) — Right body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Right body controller message: ths status. Tesla Model Y CAN bus message VCRIGHT_thsStatus (0x383) of Right body controller, firmware 2025.20.8, 11 signals (VCRIGHT_thsActive, VCRIGHT_thsTemperature, VCRIGHT_thsState, VCRIGHT_thsLINCurrentSchedule and 7 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_thsStatus (0x383) — Right body controller, Tesla Model Y 2025.20.8 VEH CAN

Right body controller message: ths status; frame length observed on a vehicle bus. This page documents the 11 signals of VCRIGHT_thsStatus as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_thsStatus` |
| CAN id | 0x383 (899) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 11 |

## Signals of VCRIGHT_thsStatus

Tesla Model Y CAN bus signals in `VCRIGHT_thsStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_thsActive` | Right body controller: ths active | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_thsTemperature` | Tesla HVAC sensor temperature; raw 255 = signal not available (SNA) | 1\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 | 255 = `SNA` | validated |
| `VCRIGHT_thsState` | Right body controller: ths state | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `CONFIG`<br>2 = `WAIT_CRC_REQUEST`<br>3 = `WAIT_CRC_RESPONSE`<br>4 = `IDLE` | validated |
| `VCRIGHT_thsLINCurrentSchedule` | Right body controller: ths LIN current schedule | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `MAIN`<br>2 = `CONFIG`<br>3 = `DIAGNOSTIC`<br>7 = `OTHER` | validated |
| `VCRIGHT_thsDetected` | Tesla HVAC sensor connection is detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_thsHumidity` | Tesla HVAC sensor humidity; raw 127 = signal not available (SNA) | 17\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | validated |
| `VCRIGHT_estimatedVehicleSituation` | Right body controller: estimated vehicle situation | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VEHICLE_SITUATION_UNKNOWN`<br>1 = `VEHICLE_SITUATION_INDOOR`<br>2 = `VEHICLE_SITUATION_OUTDOOR` | validated |
| `VCRIGHT_thsSolarLoadInfrared` | Solar power hitting the vehicle in the infrared spectrum; raw 1023 = signal not available (SNA) | 33\|10 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 2044 | 1023 = `SNA` | validated |
| `VCRIGHT_thsSolarLoadVisible` | Solar power hitting the vehicle in the visible spectrum; raw 1023 = signal not available (SNA) | 43\|10 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 2044 | 1023 = `SNA` | validated |
| `VCRIGHT_estimatedThsSolarLoad` | Right body controller: estimated ths solar load; raw 1023 = signal not available (SNA) | 53\|10 | little-endian | unsigned | 1 | 0 | W/m2 | 0 to 1022 | 1023 = `SNA` | validated |
| `VCRIGHT_hvacFastLoggingEnabled` | Right body controller: hvac fast logging enabled | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
