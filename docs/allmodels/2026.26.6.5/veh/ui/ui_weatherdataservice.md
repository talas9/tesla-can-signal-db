---
layout: default
title: "UI_weatherDataService (0x61D) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: weather data service. Tesla Model 3 / Model Y CAN bus message UI_weatherDataService (0x61D) of Touchscreen user interface computer, firmware 2026.26.6.5, 10 signals (UI_weatherSvcTimeSinceLast, UI_weatherSvcWindDir, UI_weatherSvcTemperature, UI_weatherSvcHumidity and 6 more). Bit layout, scaling, units and value tables."
---

# UI_weatherDataService (0x61D) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: weather data service; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 10 signals of UI_weatherDataService as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_weatherDataService` |
| CAN id | 0x61D (1565) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 10 |

## Signals of UI_weatherDataService

Tesla Model 3 / Model Y CAN bus signals in `UI_weatherDataService`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_weatherSvcTimeSinceLast` | Touchscreen user interface computer: weather svc time since last; raw 127 = signal not available (SNA) | 0\|7 | little-endian | unsigned | 1 | 0 | minutes | 0 to 126 | 127 = `SNA` | validated |
| `UI_weatherSvcWindDir` | Touchscreen user interface computer: weather svc wind dir; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1.5 | 0 | deg | 0 to 381 | 0 = `MIN`<br>240 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcTemperature` | Touchscreen user interface computer: weather svc temperature; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcHumidity` | Touchscreen user interface computer: weather svc humidity; raw 63 = signal not available (SNA) | 24\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcDewPoint` | Touchscreen user interface computer: weather svc dew point; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -60 | degC | -60 to 67 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcCloudCover` | Touchscreen user interface computer: weather svc cloud cover; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcPrecipProb` | Touchscreen user interface computer: weather svc precip prob; raw 63 = signal not available (SNA) | 48\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcRaining` | Touchscreen user interface computer: weather svc raining | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_weatherSvcSnowing` | Touchscreen user interface computer: weather svc snowing | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_weatherSvcWindSpeed` | Touchscreen user interface computer: weather svc wind speed; raw 63 = signal not available (SNA) | 58\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
