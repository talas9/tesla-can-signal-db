---
layout: default
title: "APP_cameraTemperatures (0x499) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: camera temperatures. Tesla Model 3 CAN bus message APP_cameraTemperatures (0x499) of Driver assistance computer (primary), firmware 2026.26.6.5, 2 signals (APP_rRepeaterCameraTemperature, APP_lRepeaterCameraTemperature). Bit layout, scaling, units and value tables."
---

# APP_cameraTemperatures (0x499) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: camera temperatures; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of APP_cameraTemperatures as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_cameraTemperatures` |
| CAN id | 0x499 (1177) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of APP_cameraTemperatures

Tesla Model 3 CAN bus signals in `APP_cameraTemperatures`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_rRepeaterCameraTemperature` | Driver assistance computer (primary): r repeater camera temperature | 24\|8 | little-endian | unsigned | 1 | -60 | C | -60 to 195 | 255 = `SNA` | plausible |
| `APP_lRepeaterCameraTemperature` | Driver assistance computer (primary): l repeater camera temperature | 32\|8 | little-endian | unsigned | 1 | -60 | C | -60 to 195 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
