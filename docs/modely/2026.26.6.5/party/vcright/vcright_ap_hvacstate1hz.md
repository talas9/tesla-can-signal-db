---
layout: default
title: "VCRIGHT_AP_hvacState1Hz (0x464) — Right body controller, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Right body controller message: AP hvac state1 hz. Tesla Model Y CAN bus message VCRIGHT_AP_hvacState1Hz (0x464) of Right body controller, firmware 2026.26.6.5, 9 signals (VCRIGHT_AP_hvacState1HzIndex, VCRIGHT_AP_tempCameraModeledWindshieldOut, VCRIGHT_AP_tempCameraModeledWindshieldIn, VCRIGHT_AP_cameraModeledWindshieldOutRh and 5 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_AP_hvacState1Hz (0x464) — Right body controller, Tesla Model Y 2026.26.6.5 PARTY CAN

Right body controller message: AP hvac state1 hz; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of VCRIGHT_AP_hvacState1Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_AP_hvacState1Hz` |
| CAN id | 0x464 (1124) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of VCRIGHT_AP_hvacState1Hz

Tesla Model Y CAN bus signals in `VCRIGHT_AP_hvacState1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_AP_hvacState1HzIndex` | selector | Right body controller: AP hvac state1 hz index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `END` | plausible |
| `VCRIGHT_AP_tempCameraModeledWindshieldOut` | page 0 | Right body controller: AP temp camera modeled windshield out; raw 255 = signal not available (SNA) | 2\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_tempCameraModeledWindshieldIn` | page 0 | Right body controller: AP temp camera modeled windshield in; raw 255 = signal not available (SNA) | 10\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | plausible |
| `VCRIGHT_AP_cameraModeledWindshieldOutRh` | page 0 | Right body controller: AP camera modeled windshield out rh; raw 127 = signal not available (SNA) | 18\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | plausible |
| `VCRIGHT_AP_cameraModeledWindshieldInRh` | page 0 | Right body controller: AP camera modeled windshield in rh; raw 127 = signal not available (SNA) | 25\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | plausible |
| `VCRIGHT_AP_maxAchievableASideTempCameraPocket` | page 0 | Right body controller: AP max achievable a side temp camera pocket | 32\|7 | little-endian | unsigned | 1 | -20 | degC | -20 to 70 |  | plausible |
| `VCRIGHT_AP_cameraModeledPocketWaterMass` | page 0 | Right body controller: AP camera modeled pocket water mass; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 0.04 | 0 | g/kg | 0 to 40 | 1023 = `SNA` | plausible |
| `VCRIGHT_AP_humidityModelInitStatus` | page 0 | Right body controller: AP humidity model init status | 52\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT_STATUS_UNKNOWN`<br>1 = `INIT_STATUS_WAITING_FOR_GTW`<br>2 = `INIT_STATUS_WAITING_FOR_CABIN_MODEL_INIT`<br>3 = `INIT_STATUS_WAITING_FOR_SENSORS_API`<br>4 = `INIT_STATUS_FAULTED_FROM_SENSORS_THS_INVALID`<br>5 = `INIT_STATUS_FAULTED_FORWARD_CALC_WEATHER_AND_AMBIENT_INVALID`<br>6 = `INIT_STATUS_FAULTED_ALL_INVALID`<br>7 = `INIT_STATUS_FAULTED_MULTI_CYCLE_SENSOR_INVALID`<br>8 = `INIT_STATUS_FROM_SENSORS`<br>9 = `INIT_STATUS_FROM_FORWARD_CALC`<br>10 = `INIT_STATUS_LIMP_FROM_SENSORS_PROBE_ONLY`<br>11 = `INIT_STATUS_LIMP_FORWARD_CALC_WEATHER_ONLY`<br>12 = `INIT_STATUS_LIMP_FORWARD_CALC_AMBIENT_ONLY`<br>13 = `INIT_STATUS_LIMP_FORWARD_CALC_PROBE_ONLY`<br>14 = `INIT_STATUS_LIMP_FORWARD_CALC_WEATHER_AND_PROBE`<br>15 = `INIT_STATUS_LIMP_FORWARD_CALC_AMBIENT_AND_PROBE`<br>16 = `INIT_STATUS_LIMP_FORWARD_CALC_THS_ONLY`<br>17 = `INIT_STATUS_LIMP_FORWARD_CALC_WEATHER_AND_THS`<br>18 = `INIT_STATUS_LIMP_FORWARD_CALC_AMBIENT_AND_THS`<br>19 = `INIT_STATUS_LIMP_FORWARD_CALC_PROBE_AND_THS`<br>20 = `INIT_STATUS_LIMP_FORWARD_CALC_WEATHER_PROBE_AND_THS`<br>21 = `INIT_STATUS_LIMP_FORWARD_CALC_AMBIENT_PROBE_AND_THS` | plausible |
| `VCRIGHT_AP_humidityModelStatus` | page 0 | Right body controller: AP humidity model status | 57\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `STATUS_UNKNOWN`<br>1 = `STATUS_RUNNING_NOMINAL`<br>2 = `STATUS_RUNNING_PAUSED_AWAITING_RECOVERY`<br>3 = `STATUS_RUNNING_RECOVERED_CATCHUP`<br>4 = `STATUS_RUNNING_LIMP_WEATHER_SUBSTITUTED_WITH_THS_FEEDBACK`<br>5 = `STATUS_RUNNING_LIMP_AMBIENT_SUBSTITUTED_WITH_THS_FEEDBACK`<br>6 = `STATUS_RUNNING_LIMP_PROBE_SUBSTITUTED_WITH_THS_FEEDBACK`<br>7 = `STATUS_RUNNING_LIMP_EVAP_SUBSTITUTED_WITH_THS_FEEDBACK`<br>8 = `STATUS_RUNNING_LIMP_WEATHER_SUBSTITUTED_NO_THS_FEEDBACK`<br>9 = `STATUS_RUNNING_LIMP_AMBIENT_SUBSTITUTED_NO_THS_FEEDBACK`<br>10 = `STATUS_RUNNING_LIMP_PROBE_SUBSTITUTED_NO_THS_FEEDBACK`<br>11 = `STATUS_RUNNING_LIMP_EVAP_SUBSTITUTED_NO_THS_FEEDBACK`<br>12 = `STATUS_RUNNING_LIMP_WEATHER_AND_PROBE_SUBSTITUTED_WITH_THS_FEEDBACK`<br>13 = `STATUS_RUNNING_LIMP_AMBIENT_AND_PROBE_SUBSTITUTED_WITH_THS_FEEDBACK`<br>14 = `STATUS_RUNNING_LIMP_WEATHER_AND_PROBE_SUBSTITUTED_NO_THS_FEEDBACK`<br>15 = `STATUS_RUNNING_LIMP_AMBIENT_AND_PROBE_SUBSTITUTED_NO_THS_FEEDBACK`<br>16 = `STATUS_RUNNING_LIMP_THS_ONLY_SUBSTITUTED`<br>17 = `STATUS_RUNNING_LIMP_THS_DIRECTLY_WITH_PROBE_LIMIT`<br>18 = `STATUS_RUNNING_LIMP_THS_DIRECTLY_NO_PROBE_LIMIT`<br>19 = `STATUS_RUNNING_FAULTED_WEATHER_AND_AMBIENT_INVALID` | plausible |

## Multiplexing

`VCRIGHT_AP_hvacState1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
