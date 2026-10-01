---
layout: default
title: "APP_frontParkAssistData (0x34B) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: front park assist data. Tesla Model 3 CAN bus message APP_frontParkAssistData (0x34B) of Driver assistance computer (primary), firmware 2025.20.8, 7 signals (APP_frontLeftParkAssist, APP_frontLeftMiddleParkAssist, APP_frontMiddleParkAssist, APP_frontRightMiddleParkAssist and 3 more). Bit layout, scaling, units and value tables."
---

# APP_frontParkAssistData (0x34B) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (primary) message: front park assist data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of APP_frontParkAssistData as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_frontParkAssistData` |
| CAN id | 0x34B (843) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of APP_frontParkAssistData

Tesla Model 3 CAN bus signals in `APP_frontParkAssistData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_frontLeftParkAssist` | Driver assistance computer (primary): front left park assist; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_frontLeftMiddleParkAssist` | Driver assistance computer (primary): front left middle park assist; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_frontMiddleParkAssist` | Driver assistance computer (primary): front middle park assist; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_frontRightMiddleParkAssist` | Driver assistance computer (primary): front right middle park assist; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_frontRightParkAssist` | Driver assistance computer (primary): front right park assist; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_parkAssistStatus` | Driver assistance computer (primary): park assist status; raw 3 = signal not available (SNA) | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `ENABLED`<br>2 = `TEMPORARY_FAILURE`<br>3 = `SNA` | plausible |
| `APP_useParkDistancesFromAP` | Driver assistance computer (primary): use park distances from AP | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
