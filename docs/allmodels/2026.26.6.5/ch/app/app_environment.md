---
layout: default
title: "APP_environment (0x25B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: environment. Tesla Model 3 / Model Y CAN bus message APP_environment (0x25B) of Driver assistance computer (primary), firmware 2026.26.6.5, 11 signals (APP_environmentRainy, APP_environmentSnowy, APP_offgassingSeverity, APP_offgassingDetectionState and 7 more). Bit layout, scaling, units and value tables."
---

# APP_environment (0x25B) — Driver assistance computer (primary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: environment; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of APP_environment as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_environment` |
| CAN id | 0x25B (603) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 11 |

## Signals of APP_environment

Tesla Model 3 / Model Y CAN bus signals in `APP_environment`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_environmentRainy` | Driver assistance computer (primary): environment rainy | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_environmentSnowy` | Driver assistance computer (primary): environment snowy | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_offgassingSeverity` | Driver assistance computer (primary): offgassing severity; raw 0 = signal not available (SNA) | 2\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `APP_OFFGASSING_SEVERITY_SNA`<br>1 = `APP_OFFGASSING_SEVERITY_CLEAR`<br>2 = `APP_OFFGASSING_SEVERITY_LESS_SEVERITY`<br>3 = `APP_OFFGASSING_SEVERITY_MEDIUM_SEVERITY`<br>4 = `APP_OFFGASSING_SEVERITY_HIGH_SEVERITY` | validated |
| `APP_offgassingDetectionState` | Driver assistance computer (primary): offgassing detection state; raw 0 = signal not available (SNA) | 5\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `APP_OFFGASSING_DETECTION_SNA`<br>1 = `APP_OFFGASSING_DETECTION_SKIPPED`<br>2 = `APP_OFFGASSING_DETECTION_ACTIVE` | validated |
| `APP_offgassingAlertEnabled` | Driver assistance computer (primary): offgassing alert enabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_offgassingMaxProbabilityLong` | Driver assistance computer (primary): offgassing max probability long; raw 0 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `APP_OFFGASSING_DETECTION_PERCENT_SNA`<br>1 = `APP_OFFGASSING_DETECTION_PERCENT_0`<br>2 = `APP_OFFGASSING_DETECTION_PERCENT_0_25`<br>3 = `APP_OFFGASSING_DETECTION_PERCENT_0_5`<br>4 = `APP_OFFGASSING_DETECTION_PERCENT_0_75`<br>5 = `APP_OFFGASSING_DETECTION_PERCENT_1`<br>6 = `APP_OFFGASSING_DETECTION_PERCENT_1_5`<br>7 = `APP_OFFGASSING_DETECTION_PERCENT_2`<br>8 = `APP_OFFGASSING_DETECTION_PERCENT_3`<br>9 = `APP_OFFGASSING_DETECTION_PERCENT_4`<br>10 = `APP_OFFGASSING_DETECTION_PERCENT_8`<br>11 = `APP_OFFGASSING_DETECTION_PERCENT_16`<br>12 = `APP_OFFGASSING_DETECTION_PERCENT_16_PLUS` | validated |
| `APP_offgassingMaxProbabilityShort` | Driver assistance computer (primary): offgassing max probability short; raw 0 = signal not available (SNA) | 12\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `APP_OFFGASSING_DETECTION_PERCENT_SNA`<br>1 = `APP_OFFGASSING_DETECTION_PERCENT_0`<br>2 = `APP_OFFGASSING_DETECTION_PERCENT_0_25`<br>3 = `APP_OFFGASSING_DETECTION_PERCENT_0_5`<br>4 = `APP_OFFGASSING_DETECTION_PERCENT_0_75`<br>5 = `APP_OFFGASSING_DETECTION_PERCENT_1`<br>6 = `APP_OFFGASSING_DETECTION_PERCENT_1_5`<br>7 = `APP_OFFGASSING_DETECTION_PERCENT_2`<br>8 = `APP_OFFGASSING_DETECTION_PERCENT_3`<br>9 = `APP_OFFGASSING_DETECTION_PERCENT_4`<br>10 = `APP_OFFGASSING_DETECTION_PERCENT_8`<br>11 = `APP_OFFGASSING_DETECTION_PERCENT_16`<br>12 = `APP_OFFGASSING_DETECTION_PERCENT_16_PLUS` | validated |
| `APP_offgassingLongMaxCamera` | Driver assistance computer (primary): offgassing long max camera; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `MAIN`<br>2 = `NARROW`<br>3 = `FISHEYE` | validated |
| `APP_offgassingShortMaxCamera` | Driver assistance computer (primary): offgassing short max camera; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `MAIN`<br>2 = `NARROW`<br>3 = `FISHEYE` | validated |
| `APP_offgassingLongMaxDetector` | Driver assistance computer (primary): offgassing long max detector; raw 0 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `VEHICLE`<br>2 = `TRAFFIC_LIGHT` | validated |
| `APP_offgassingShortMaxDetector` | Driver assistance computer (primary): offgassing short max detector; raw 0 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `VEHICLE`<br>2 = `TRAFFIC_LIGHT` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
