---
layout: default
title: "APP_cameraLux (0x3FA) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: camera lux. Tesla Model Y CAN bus message APP_cameraLux (0x3FA) of Driver assistance computer (primary), firmware 2026.26.6.5, 8 signals (APP_mainCameraLUX, APP_narrowCameraLUX, APP_fisheyeCameraLUX, APP_lRepeatCameraLUX and 4 more). Bit layout, scaling, units and value tables."
---

# APP_cameraLux (0x3FA) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: camera lux; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of APP_cameraLux as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_cameraLux` |
| CAN id | 0x3FA (1018) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 8 |

## Signals of APP_cameraLux

Tesla Model Y CAN bus signals in `APP_cameraLux`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_mainCameraLUX` | Amount of illuminance seen by the main camera; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_narrowCameraLUX` | Driver assistance computer (primary): narrow camera LUX; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_fisheyeCameraLUX` | Driver assistance computer (primary): fisheye camera LUX; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_lRepeatCameraLUX` | Driver assistance computer (primary): l repeat camera LUX; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_rRepeatCameraLUX` | Driver assistance computer (primary): r repeat camera LUX; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_lPillarCameraLUX` | Driver assistance computer (primary): l pillar camera LUX; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_rPillarCameraLUX` | Driver assistance computer (primary): r pillar camera LUX; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |
| `APP_backupCameraLUX` | Driver assistance computer (primary): backup camera LUX; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | 0 | lux^0.5 | 0 to 127 | 254 = `SATURATED`<br>255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
