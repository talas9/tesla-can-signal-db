---
layout: default
title: "APP_backupDashCamStatus (0x415) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: backup dash cam status. Tesla Model 3 CAN bus message APP_backupDashCamStatus (0x415) of Driver assistance computer (primary), firmware 2025.20.8, 2 signals (APP_backupDashCamFeedGood, APP_backupDashCamFrameRate). Bit layout, scaling, units and value tables."
---

# APP_backupDashCamStatus (0x415) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (primary) message: backup dash cam status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of APP_backupDashCamStatus as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_backupDashCamStatus` |
| CAN id | 0x415 (1045) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 1 bytes |
| Cycle time | 500 ms |
| Signals | 2 |

## Signals of APP_backupDashCamStatus

Tesla Model 3 CAN bus signals in `APP_backupDashCamStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_backupDashCamFeedGood` | Indicates if the backup dash cam stream is healthy. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_backupDashCamFrameRate` | The backup dash cam frame rate. | 1\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
