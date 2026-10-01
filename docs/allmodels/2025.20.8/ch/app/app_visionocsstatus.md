---
layout: default
title: "APP_visionOcsStatus (0x35B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: vision ocs status. Tesla Model 3 / Model Y CAN bus message APP_visionOcsStatus (0x35B) of Driver assistance computer (primary), firmware 2025.20.8, 7 signals (APP_visionOcsStatusChecksum, APP_visionOcsStateRaw, APP_visionOcsEmptyProbRaw, APP_visionOcsChildProbRaw and 3 more). Bit layout, scaling, units and value tables."
---

# APP_visionOcsStatus (0x35B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2025.20.8 CH CAN

Driver assistance computer (primary) message: vision ocs status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of APP_visionOcsStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_visionOcsStatus` |
| CAN id | 0x35B (859) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of APP_visionOcsStatus

Tesla Model 3 / Model Y CAN bus signals in `APP_visionOcsStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_visionOcsStatusChecksum` | Driver assistance computer (primary): vision ocs status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `APP_visionOcsStateRaw` | Reports classification state raw signal for front passenger from interior camera. | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `EMPTY`<br>2 = `CHILD`<br>3 = `ADULT` | plausible |
| `APP_visionOcsEmptyProbRaw` | Driver assistance computer (primary): vision ocs empty prob raw; raw 255 = signal not available (SNA) | 10\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `APP_visionOcsChildProbRaw` | Driver assistance computer (primary): vision ocs child prob raw; raw 255 = signal not available (SNA) | 18\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `APP_visionOcsAdultProbRaw` | Driver assistance computer (primary): vision ocs adult prob raw; raw 255 = signal not available (SNA) | 26\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `APP_visionOcsFrontPasClsVisionStateFlt` | Reports classification state of front passenger seat after Bayesian filter. | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `EMPTY`<br>2 = `CHILD`<br>3 = `ADULT` | plausible |
| `APP_visionOcsStatusCounter` | Driver assistance computer (primary): vision ocs status counter | 36\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
