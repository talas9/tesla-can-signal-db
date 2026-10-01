---
layout: default
title: "APP_cameraStatus (0x410) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: camera status. Tesla Model 3 / Model Y CAN bus message APP_cameraStatus (0x410) of Driver assistance computer (primary), firmware 2026.26.6.5, 11 signals (APP_backupCameraFeedGood, APP_backupCameraFrameRate, APP_cameraBlockedFrontMain, APP_cameraBlockedFrontFisheye and 7 more). Bit layout, scaling, units and value tables."
---

# APP_cameraStatus (0x410) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: camera status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of APP_cameraStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_cameraStatus` |
| CAN id | 0x410 (1040) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 11 |

## Signals of APP_cameraStatus

Tesla Model 3 / Model Y CAN bus signals in `APP_cameraStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_backupCameraFeedGood` | Indicates if the backup camera stream is healthy. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_backupCameraFrameRate` | The backup camera frame rate. | 1\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | plausible |
| `APP_cameraBlockedFrontMain` | Indicates that a blockage was detected by the main forward camera. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedFrontFisheye` | Indicates that a blockage was detected by the fisheye camera. | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedFrontNarrow` | Indicates that a blockage was detected by the narrow camera. | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedLeftPillar` | Indicates that a blockage was detected by the left pillar camera. | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedLeftRepeater` | Indicates that a blockage was detected by the left repeater camera. | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedRightPillar` | Indicates that a blockage was detected by the right pillar camera. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedRightRepeater` | Indicates that a blockage was detected by the right repeater camera. | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_cameraBlockedBackup` | Indicates that a blockage was detected by the backup camera. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_fasciaCameraTemperature` | Die temperature of camera image sensor; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -60 | C | -60 to 194 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
