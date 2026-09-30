---
layout: default
title: "UI_frontSeatRequests (0x4F3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: front seat requests. Ethernet-side message UI_frontSeatRequests of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 8 signals (UI_frontRightSeatTrackForward, UI_frontRightSeatTrackBack, UI_frontLeftSeatTrackForward, UI_frontLeftSeatTrackBack and 4 more). Bit layout, scaling, units and value tables."
---

# UI_frontSeatRequests (0x4F3) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: front seat requests. This page documents the 8 signals of UI_frontSeatRequests as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_frontSeatRequests` |
| Ethernet-side id | 0x4F3 (1267) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 3 bytes |
| Cycle time | 500 ms |
| Signals | 8 |

## Signals of UI_frontSeatRequests

Tesla Model 3 / Model Y CAN bus signals in `UI_frontSeatRequests`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_frontRightSeatTrackForward` | Touchscreen user interface computer: front right seat track forward | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatTrackBack` | Touchscreen user interface computer: front right seat track back | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTrackForward` | Touchscreen user interface computer: front left seat track forward | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatTrackBack` | Touchscreen user interface computer: front left seat track back | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatBackrestBack` | Touchscreen user interface computer: front right seat backrest back | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontRightSeatBackrestForward` | Touchscreen user interface computer: front right seat backrest forward | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatBackrestBack` | Touchscreen user interface computer: front left seat backrest back | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_frontLeftSeatBackrestForward` | Touchscreen user interface computer: front left seat backrest forward | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
