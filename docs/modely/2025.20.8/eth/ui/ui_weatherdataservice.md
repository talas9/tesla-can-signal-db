---
layout: default
title: "UI_weatherDataService (0x621) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: weather data service. Ethernet-side message UI_weatherDataService of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 5 signals (UI_weatherSvcTimeSinceLast, UI_weatherSvcTemperature, UI_weatherSvcHumidity, UI_weatherSvcDewPoint and 1 more). Bit layout, scaling, units and value tables."
---

# UI_weatherDataService (0x621) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: weather data service. This page documents the 5 signals of UI_weatherDataService as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_weatherDataService` |
| Ethernet-side id | 0x621 (1569) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 5 |

## Signals of UI_weatherDataService

Tesla Model Y CAN bus signals in `UI_weatherDataService`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_weatherSvcTimeSinceLast` | Touchscreen user interface computer: weather svc time since last; raw 2047 = signal not available (SNA) | 0\|11 | little-endian | unsigned | 1 | 0 | minutes | 0 to 2046 | 2047 = `SNA` | plausible |
| `UI_weatherSvcTemperature` | Touchscreen user interface computer: weather svc temperature; raw 127 = signal not available (SNA) | 16\|8 | little-endian | signed | 0.5 | 0 | degC | -64 to 63 | -120 = `MIN`<br>120 = `MAX`<br>127 = `SNA` | plausible |
| `UI_weatherSvcHumidity` | Touchscreen user interface computer: weather svc humidity; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127 | 255 = `SNA` | plausible |
| `UI_weatherSvcDewPoint` | Touchscreen user interface computer: weather svc dew point; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | 0 | degC | 0 to 127 | 255 = `SNA` | plausible |
| `UI_weatherSvcCloudCover` | Touchscreen user interface computer: weather svc cloud cover; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
