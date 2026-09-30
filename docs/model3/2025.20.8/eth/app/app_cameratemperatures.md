---
layout: default
title: "APP_cameraTemperatures (0x499) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: camera temperatures. Ethernet-side message APP_cameraTemperatures of Driver assistance computer (primary) for Tesla Model 3 firmware 2025.20.8, 2 signals (APP_rRepeaterCameraTemperature, APP_lRepeaterCameraTemperature). Bit layout, scaling, units and value tables."
---

# APP_cameraTemperatures (0x499) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 ETH

Driver assistance computer (primary) message: camera temperatures. This page documents the 2 signals of APP_cameraTemperatures as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_cameraTemperatures` |
| Ethernet-side id | 0x499 (1177) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
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

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
