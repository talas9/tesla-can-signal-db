---
layout: default
title: "APP_VC_infoMessage (0x38D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Driver assistance computer (primary) message: VC info message. Tesla Model 3 / Model Y CAN bus message APP_VC_infoMessage (0x38D) of Driver assistance computer (primary), firmware 2026.26.6.5, 23 signals (APP_inTunnel, APP_windshieldHeaterOnReason, APP_selfieCameraBlocked, APP_selfieCameraLUX and 19 more). Bit layout, scaling, units and value tables."
---

# APP_VC_infoMessage (0x38D) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Driver assistance computer (primary) message: VC info message; frame length observed on a vehicle bus. This page documents the 23 signals of APP_VC_infoMessage as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_VC_infoMessage` |
| CAN id | 0x38D (909) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 23 |

## Signals of APP_VC_infoMessage

Tesla Model 3 / Model Y CAN bus signals in `APP_VC_infoMessage`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_inTunnel` | Driver assistance computer (primary): in tunnel; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `IN_TUNNEL_SNA`<br>1 = `IN_TUNNEL`<br>2 = `NOT_IN_TUNNEL` | validated |
| `APP_windshieldHeaterOnReason` | Reports the reason why Autopilot (AP) is turning windshield heater on; raw 0 = signal not available (SNA) | 2\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `WINDSHIELD_HEATER_ON_REASON_SNA`<br>1 = `WINDSHIELD_HEATER_ON_REASON_DEFROST`<br>2 = `WINDSHIELD_HEATER_ON_REASON_OCCLUDED`<br>3 = `WINDSHIELD_HEATER_ON_REASON_CONDENSATION_LIKELY`<br>4 = `WINDSHIELD_HEATER_ON_REASON_STARTUP`<br>5 = `WINDSHIELD_HEATER_ON_REASON_OFF`<br>6 = `WINDSHIELD_HEATER_ON_REASON_OVERRIDE`<br>7 = `WINDSHIELD_HEATER_ON_REASON_HVAC_REQUESTED`<br>8 = `WINDSHIELD_HEATER_ON_REASON_WIPERS_ACTIVE` | validated |
| `APP_selfieCameraBlocked` | Indicates if the selfie camera is currently blocked, or if this selfie camera model doesn't report lux; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SELFIE_CAMERA_BLOCKED_SNA`<br>1 = `SELFIE_CAMERA_NOT_BLOCKED`<br>2 = `SELFIE_CAMERA_BLOCKED` | validated |
| `APP_selfieCameraLUX` | Reports lux reading. Note that selfie camera lux is not currently calibrated against other cameras so the range is different; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | lux | 0 to 253 | 254 = `SATURATED`<br>255 = `SNA` | validated |
| `APP_sceneTagClearlyRaining` | Indicates if the vision scene tag is clearly raining; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagFog` | Indicates if the vision scene tag detects fog; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagFullyBlocked` | Indicates if the vision scene tag detects a fully blocked view; raw 0 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagIndoors` | Indicates if the vision scene tag detects an indoor environment; raw 0 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagLensFlare` | Indicates if the vision scene tag detects lens flare; raw 0 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagRaining` | Indicates if the vision scene tag detects raining conditions; raw 0 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagSevereWeather` | Indicates if the vision scene tag detects severe weather conditions; raw 0 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagSnowing` | Indicates if the vision scene tag detects snowing conditions; raw 0 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagSnowyRoad` | Indicates if the vision scene tag detects snowy road conditions; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagSunGlare` | Indicates if the vision scene tag detects sun glare conditions; raw 0 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagTunnel` | Indicates if the vision scene tag detects a tunnel environment; raw 0 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_sceneTagWetRoad` | Indicates if the vision scene tag detects wet road conditions; raw 0 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ACTIVATED`<br>2 = `NOT_ACTIVATED` | validated |
| `APP_fisheyeInPathVisibility` | Driver assistance computer (primary): fisheye in path visibility; raw 0 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_fisheyeOverallVisibility` | Driver assistance computer (primary): fisheye overall visibility; raw 0 = signal not available (SNA) | 43\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_mainInPathVisibility` | Driver assistance computer (primary): main in path visibility; raw 0 = signal not available (SNA) | 46\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_mainOverallVisibility` | Driver assistance computer (primary): main overall visibility; raw 0 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_narrowInPathVisibility` | Driver assistance computer (primary): narrow in path visibility; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_narrowOverallVisibility` | Driver assistance computer (primary): narrow overall visibility; raw 0 = signal not available (SNA) | 55\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `VISIBILITY_CONDITION_SNA`<br>1 = `VISIBILITY_OCCLUDED_HIGH_SEVERITY`<br>2 = `VISIBILITY_OCCLUDED_MEDIUM_SEVERITY`<br>3 = `VISIBILITY_OCCLUDED_LOW_SEVERITY`<br>4 = `VISIBILITY_CONDITION_NOMINAL` | validated |
| `APP_frontCamOcclusionType` | Reports the current type of what is obstructing the front camera vision. | 58\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFFGASSING`<br>1 = `CONDENSATION`<br>2 = `DIRTY_OR_BLOCKED`<br>3 = `SUN_GLARE`<br>4 = `STREAK`<br>5 = `DEW`<br>6 = `UNKNOWN_OCCLUSION` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
