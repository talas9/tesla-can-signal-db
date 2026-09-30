---
layout: default
title: "UI_weatherDataServiceForecast (0x7B1) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: weather data service forecast. Tesla Model 3 CAN bus message UI_weatherDataServiceForecast (0x7B1) of Touchscreen user interface computer, firmware 2026.26.6.5, 34 signals (UI_weatherSvcForecastMuxIndex, UI_weatherSvcForecastTempC_hour1, UI_weatherSvcForecastTempC_hour2, UI_weatherSvcForecastTempC_hour3 and 30 more). Bit layout, scaling, units and value tables."
---

# UI_weatherDataServiceForecast (0x7B1) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: weather data service forecast; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 34 signals of UI_weatherDataServiceForecast as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_weatherDataServiceForecast` |
| CAN id | 0x7B1 (1969) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 34 |

## Signals of UI_weatherDataServiceForecast

Tesla Model 3 CAN bus signals in `UI_weatherDataServiceForecast`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_weatherSvcForecastMuxIndex` | selector | Touchscreen user interface computer: weather svc forecast mux index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MUX0`<br>1 = `MUX1`<br>2 = `MUX2`<br>3 = `MUX3`<br>4 = `MUX4` | plausible |
| `UI_weatherSvcForecastTempC_hour1` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour1; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour2` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour2; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour3` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour3; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour4` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour4; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour5` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour5; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour6` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour6; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour7` | page 0 | Touchscreen user interface computer: weather svc forecast temp c hour7; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour8` | page 1 | Touchscreen user interface computer: weather svc forecast temp c hour8; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour9` | page 1 | Touchscreen user interface computer: weather svc forecast temp c hour9; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour10` | page 1 | Touchscreen user interface computer: weather svc forecast temp c hour10; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastTempC_hour11` | page 1 | Touchscreen user interface computer: weather svc forecast temp c hour11; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | C | -40 to 87 | 0 = `MIN`<br>250 = `MAX`<br>255 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour1` | page 1 | Touchscreen user interface computer: weather svc forecast humidity hour1; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour2` | page 1 | Touchscreen user interface computer: weather svc forecast humidity hour2; raw 63 = signal not available (SNA) | 48\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour3` | page 1 | Touchscreen user interface computer: weather svc forecast humidity hour3; raw 63 = signal not available (SNA) | 56\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour4` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour4; raw 63 = signal not available (SNA) | 8\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour5` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour5; raw 63 = signal not available (SNA) | 16\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour6` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour6; raw 63 = signal not available (SNA) | 24\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour7` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour7; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour8` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour8; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour9` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour9; raw 63 = signal not available (SNA) | 48\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour10` | page 2 | Touchscreen user interface computer: weather svc forecast humidity hour10; raw 63 = signal not available (SNA) | 56\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastHumidity_hour11` | page 3 | Touchscreen user interface computer: weather svc forecast humidity hour11; raw 63 = signal not available (SNA) | 8\|6 | little-endian | unsigned | 1.62 | 0 | % | 0 to 100.44 | 0 = `MIN`<br>62 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour1` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour1; raw 63 = signal not available (SNA) | 16\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour2` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour2; raw 63 = signal not available (SNA) | 24\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour3` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour3; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour4` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour4; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour5` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour5; raw 63 = signal not available (SNA) | 48\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour6` | page 3 | Touchscreen user interface computer: weather svc forecast wind speed kph hour6; raw 63 = signal not available (SNA) | 56\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour7` | page 4 | Touchscreen user interface computer: weather svc forecast wind speed kph hour7; raw 63 = signal not available (SNA) | 8\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour8` | page 4 | Touchscreen user interface computer: weather svc forecast wind speed kph hour8; raw 63 = signal not available (SNA) | 16\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour9` | page 4 | Touchscreen user interface computer: weather svc forecast wind speed kph hour9; raw 63 = signal not available (SNA) | 24\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour10` | page 4 | Touchscreen user interface computer: weather svc forecast wind speed kph hour10; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |
| `UI_weatherSvcForecastWindSpeedKph_hour11` | page 4 | Touchscreen user interface computer: weather svc forecast wind speed kph hour11; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 2 | 0 | kph | 0 to 124 | 0 = `MIN`<br>60 = `MAX`<br>63 = `SNA` | plausible |

## Multiplexing

`UI_weatherSvcForecastMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (7 signals), page 3 (7 signals), page 4 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
