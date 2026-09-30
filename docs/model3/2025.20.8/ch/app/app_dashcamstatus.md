---
layout: default
title: "APP_dashCamStatus (0x413) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: dash cam status. Tesla Model 3 CAN bus message APP_dashCamStatus (0x413) of Driver assistance computer (primary), firmware 2025.20.8, 6 signals (APP_mainDashCamFeedGood, APP_mainDashCamFrameRate, APP_lRepeatDashCamFeedGood, APP_lRepeatDashCamFrameRate and 2 more). Bit layout, scaling, units and value tables."
---

# APP_dashCamStatus (0x413) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (primary) message: dash cam status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APP_dashCamStatus as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_dashCamStatus` |
| CAN id | 0x413 (1043) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 6 |

## Signals of APP_dashCamStatus

Tesla Model 3 CAN bus signals in `APP_dashCamStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_mainDashCamFeedGood` | Indicates if the main dash cam stream is healthy. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_mainDashCamFrameRate` | The main dash cam frame rate. | 1\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |
| `APP_lRepeatDashCamFeedGood` | Indicates if the left repeater dash cam stream is healthy. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_lRepeatDashCamFrameRate` | The left repeater dash cam frame rate. | 9\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |
| `APP_rRepeatDashCamFeedGood` | Indicates if the right repeater dash cam stream is healthy. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_rRepeatDashCamFrameRate` | The right repeater dash cam frame rate. | 17\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
