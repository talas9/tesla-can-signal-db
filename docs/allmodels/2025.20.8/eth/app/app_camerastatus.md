---
layout: default
title: "APP_cameraStatus (0x410) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: camera status. Ethernet-side message APP_cameraStatus of Driver assistance computer (primary) for Tesla Model 3 / Model Y firmware 2025.20.8, 10 signals (APP_backupCameraFeedGood, APP_backupCameraFrameRate, APP_cameraBlockedFrontMain, APP_cameraBlockedFrontFisheye and 6 more). Bit layout, scaling, units and value tables."
---

# APP_cameraStatus (0x410) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: camera status. This page documents the 10 signals of APP_cameraStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_cameraStatus` |
| Ethernet-side id | 0x410 (1040) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 2 bytes |
| Cycle time | 500 ms |
| Signals | 10 |

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

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
