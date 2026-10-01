---
layout: default
title: "APP_dashCamStatus (0x413) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: dash cam status. Tesla Model Y CAN bus message APP_dashCamStatus (0x413) of Driver assistance computer (primary), firmware 2026.26.6.5, 6 signals (APP_mainDashCamFeedGood, APP_mainDashCamFrameRate, APP_lRepeatDashCamFeedGood, APP_lRepeatDashCamFrameRate and 2 more). Bit layout, scaling, units and value tables."
---

# APP_dashCamStatus (0x413) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: dash cam status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APP_dashCamStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_dashCamStatus` |
| CAN id | 0x413 (1043) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 6 |

## Signals of APP_dashCamStatus

Tesla Model Y CAN bus signals in `APP_dashCamStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_mainDashCamFeedGood` | Indicates if the main dash cam stream is healthy. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_mainDashCamFrameRate` | The main dash cam frame rate. | 1\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | plausible |
| `APP_lRepeatDashCamFeedGood` | Indicates if the left repeater dash cam stream is healthy. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_lRepeatDashCamFrameRate` | The left repeater dash cam frame rate. | 9\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | plausible |
| `APP_rRepeatDashCamFeedGood` | Indicates if the right repeater dash cam stream is healthy. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_rRepeatDashCamFrameRate` | The right repeater dash cam frame rate. | 17\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
