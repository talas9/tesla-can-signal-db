---
layout: default
title: "APP_rearParkAssistData (0x38B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: rear park assist data. Tesla Model 3 / Model Y CAN bus message APP_rearParkAssistData (0x38B) of Driver assistance computer (primary), firmware 2026.26.6.5, 5 signals (APP_rearLeftParkAssist, APP_rearLeftMiddleParkAssist, APP_rearMiddleParkAssist, APP_rearRightMiddleParkAssist and 1 more). Bit layout, scaling, units and value tables."
---

# APP_rearParkAssistData (0x38B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: rear park assist data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of APP_rearParkAssistData as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_rearParkAssistData` |
| CAN id | 0x38B (907) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of APP_rearParkAssistData

Tesla Model 3 / Model Y CAN bus signals in `APP_rearParkAssistData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_rearLeftParkAssist` | Driver assistance computer (primary): rear left park assist; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_rearLeftMiddleParkAssist` | Driver assistance computer (primary): rear left middle park assist; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_rearMiddleParkAssist` | Driver assistance computer (primary): rear middle park assist; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_rearRightMiddleParkAssist` | Driver assistance computer (primary): rear right middle park assist; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |
| `APP_rearRightParkAssist` | Driver assistance computer (primary): rear right park assist; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
