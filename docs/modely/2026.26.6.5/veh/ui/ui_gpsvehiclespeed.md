---
layout: default
title: "UI_gpsVehicleSpeed (0x373) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: gps vehicle speed. Tesla Model Y CAN bus message UI_gpsVehicleSpeed (0x373) of Touchscreen user interface computer, firmware 2026.26.6.5, 11 signals (UI_gpsHDOP, UI_gpsVehicleHeading, UI_gpsVehicleSpeed, UI_userSpeedOffset and 7 more). Bit layout, scaling, units and value tables."
---

# UI_gpsVehicleSpeed (0x373) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: gps vehicle speed; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 11 signals of UI_gpsVehicleSpeed as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_gpsVehicleSpeed` |
| CAN id | 0x373 (883) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 11 |

## Signals of UI_gpsVehicleSpeed

Tesla Model Y CAN bus signals in `UI_gpsVehicleSpeed`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_gpsHDOP` | Touchscreen user interface computer: gps HDOP | 0\|8 | little-endian | unsigned | 0.1 | 0 | 1 | 0 to 25.5 |  | validated |
| `UI_gpsVehicleHeading` | Touchscreen user interface computer: gps vehicle heading | 8\|16 | little-endian | unsigned | 0.0078125 | 0 | deg | 0 to 511.9921875 |  | plausible |
| `UI_gpsVehicleSpeed` | Touchscreen user interface computer: gps vehicle speed | 24\|16 | little-endian | unsigned | 0.00390625 | 0 | km/hr | 0 to 255.99609375 |  | plausible |
| `UI_userSpeedOffset` | Touchscreen user interface computer: user speed offset | 40\|6 | little-endian | unsigned | 1 | -30 | kph/mph | -30 to 33 |  | plausible |
| `UI_mapSpeedLimitUnits` | Autopilot map speed limit units. | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MPH`<br>1 = `KPH` | validated |
| `UI_userSpeedOffsetUnits` | Touchscreen user interface computer: user speed offset units | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MPH`<br>1 = `KPH` | plausible |
| `UI_mppSpeedLimit` | Autopilot map speed limit | 48\|5 | little-endian | unsigned | 5 | 0 | kph/mph | 0 to 155 |  | validated |
| `UI_gpsNmeaMIA` | GPS NMEA data MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_gpsAntennaDisconnected` | GPS antenna state | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_conditionalLimitActive` | Conditional speed limit condition is currently active | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_conditionalSpeedLimit` | Conditional speed limit value; raw 31 = signal not available (SNA) | 56\|5 | little-endian | unsigned | 5 | 0 | kph/mph | 0 to 150 | 31 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
