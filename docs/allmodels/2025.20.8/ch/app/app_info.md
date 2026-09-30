---
layout: default
title: "APP_info (0x549) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: info. Tesla Model 3 / Model Y CAN bus message APP_info (0x549) of Driver assistance computer (primary), firmware 2025.20.8, 2 signals (APP_infoIndex, APP_buildType). Bit layout, scaling, units and value tables."
---

# APP_info (0x549) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of APP_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_info` |
| CAN id | 0x549 (1353) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of APP_info

Tesla Model 3 / Model Y CAN bus signals in `APP_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `APP_infoIndex` | selector | Driver assistance computer (primary): info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `AP_BUILD_TYPE`<br>1 = `FW_GITHASH`<br>2 = `AP_GITHASH`<br>3 = `AP_BOOT_COUNT` | plausible |
| `APP_buildType` | page 0 | Driver assistance computer (primary): build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `AP_BUILDTYPE_SIGNED`<br>1 = `AP_BUILDTYPE_LOCAL`<br>3 = `AP_BUILDTYPE_REPO` | validated |

## Multiplexing

`APP_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
