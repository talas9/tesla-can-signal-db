---
layout: default
title: "UI_suspensionControl (0x297) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: suspension control. Tesla Model 3 / Model Y CAN bus message UI_suspensionControl (0x297) of Touchscreen user interface computer, firmware 2025.20.8, 12 signals (UI_adaptiveRideRequest, UI_suspensionLoweringRequest, UI_geofenceLevelingRequest, UI_jackModeToggleRequest and 8 more). Bit layout, scaling, units and value tables."
---

# UI_suspensionControl (0x297) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: suspension control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of UI_suspensionControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_suspensionControl` |
| CAN id | 0x297 (663) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 12 |

## Signals of UI_suspensionControl

Tesla Model 3 / Model Y CAN bus signals in `UI_suspensionControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_adaptiveRideRequest` | UI customer adaptive ride request for air suspension. | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ADAPTIVE_RIDE_REQUEST_COMFORT`<br>1 = `ADAPTIVE_RIDE_REQUEST_AUTO`<br>2 = `ADAPTIVE_RIDE_REQUEST_SPORT`<br>3 = `ADAPTIVE_RIDE_REQUEST_ADVANCED` | validated |
| `UI_suspensionLoweringRequest` | Touchscreen user interface computer: suspension lowering request; raw 3 = signal not available (SNA) | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NEVER`<br>1 = `ALWAYS`<br>2 = `AUTO`<br>3 = `SNA` | plausible |
| `UI_geofenceLevelingRequest` | Geofence level request from customer; raw 5 = signal not available (SNA) | 7\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `GEOFENCE_LEVELING_REQUEST_NONE`<br>1 = `GEOFENCE_LEVELING_REQUEST_HIGH_TEMPORARY`<br>2 = `GEOFENCE_LEVELING_REQUEST_VERY_HIGH_TEMPORARY`<br>3 = `GEOFENCE_LEVELING_REQUEST_HIGH_PERSIST`<br>4 = `GEOFENCE_LEVELING_REQUEST_VERY_HIGH_PERSIST`<br>5 = `GEOFENCE_LEVELING_REQUEST_SNA` | validated |
| `UI_jackModeToggleRequest` | Touchscreen user interface computer: jack mode toggle request | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `ACTIVE` | plausible |
| `UI_adaptiveTuningRequest0` | Touchscreen user interface computer: adaptive tuning request0 | 11\|5 | little-endian | signed | 0.1 | 0 | - | -1.6 to 1.5 |  | plausible |
| `UI_adaptiveTuningRequest1` | Touchscreen user interface computer: adaptive tuning request1 | 16\|5 | little-endian | signed | 0.1 | 0 | - | -1.6 to 1.5 |  | plausible |
| `UI_roadRoughnessLookahead` | Touchscreen user interface computer: road roughness lookahead; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.01 | 0 | % | 0 to 1.26 | 127 = `SNA` | plausible |
| `UI_roadRoughnessStart` | Touchscreen user interface computer: road roughness start; raw 31 = signal not available (SNA) | 32\|5 | little-endian | unsigned | 10 | 0 | m | 0 to 300 | 31 = `SNA` | plausible |
| `UI_mapVersionUsed` | Touchscreen user interface computer: map version used; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | 0 | - | 0 to 254 | 255 = `SNA` | plausible |
| `UI_suspensionControlCounter` | Touchscreen user interface computer: suspension control counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_suspensionLevelRequest` | Touchscreen user interface computer: suspension level request | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `VERY_LOW_LEVEL`<br>2 = `LOW_LEVEL`<br>3 = `STANDARD_LEVEL`<br>4 = `HIGH_LEVEL_TEMPORARY`<br>5 = `VERY_HIGH_LEVEL_TEMPORARY`<br>6 = `HIGH_LEVEL_PERSIST`<br>7 = `VERY_HIGH_LEVEL_PERSIST` | plausible |
| `UI_suspensionControlChecksum` | Touchscreen user interface computer: suspension control checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
