---
layout: default
title: "DAS_object (0x30A) — Driver assistance computer, Tesla Model 3 2026.26.6.5 ETH"
description: "Driver assistance computer message: object. Ethernet-side message DAS_object of Driver assistance computer for Tesla Model 3 firmware 2026.26.6.5, 50 signals (DAS_objectId, DAS_leadVehType, DAS_leadVehRelevantForControl, DAS_leadVehDx and 46 more). Bit layout, scaling, units and value tables."
---

# DAS_object (0x30A) — Driver assistance computer, Tesla Model 3 2026.26.6.5 ETH

Driver assistance computer message: object. This page documents the 50 signals of DAS_object as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_object` |
| Ethernet-side id | 0x30A (778) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 30 ms |
| Signals | 50 |

## Signals of DAS_object

Tesla Model 3 CAN bus signals in `DAS_object`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_objectId` | selector | Driver assistance computer: object id | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LEAD_VEHICLES`<br>1 = `LEFT_VEHICLES`<br>2 = `RIGHT_VEHICLES`<br>3 = `CUTIN_VEHICLE`<br>4 = `ROAD_SIGN`<br>5 = `VEHICLE_HEADINGS` | plausible |
| `DAS_leadVehType` | page 0 | Driver assistance computer: lead veh type | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN`<br>6 = `IPSO` | validated |
| `DAS_leadVehRelevantForControl` | page 0 | Driver assistance computer: lead veh relevant for control | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_leadVehDx` | page 0 | Measures the distance to lead vehicle, or vehicle in the ego lane; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_leadVehVxRel` | page 0 | Driver assistance computer: lead veh vx rel; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_leadVehDy` | page 0 | Driver assistance computer: lead veh dy | 20\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_leadVehId` | page 0 | Driver assistance computer: lead veh id; raw 127 = signal not available (SNA) | 27\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 126 | 127 = `SNA` | validated |
| `DAS_leadVeh2Type` | page 0 | Driver assistance computer: lead veh2 type | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_leadVeh2RelevantForControl` | page 0 | Driver assistance computer: lead veh2 relevant for control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_leadVeh2Dx` | page 0 | Driver assistance computer: lead veh2 dx; raw 255 = signal not available (SNA) | 39\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_leadVeh2VxRel` | page 0 | Driver assistance computer: lead veh2 vx rel; raw 15 = signal not available (SNA) | 47\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_leadVeh2Dy` | page 0 | Driver assistance computer: lead veh2 dy | 51\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_leadVeh2Id` | page 0 | Driver assistance computer: lead veh2 id; raw 0 = signal not available (SNA) | 58\|6 | little-endian | unsigned | 1 | 0 |  | 1 to 63 | 0 = `SNA` | validated |
| `DAS_leftVehType` | page 1 | Driver assistance computer: left veh type | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_leftVehRelevantForControl` | page 1 | Driver assistance computer: left veh relevant for control | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_leftVehDx` | page 1 | Driver assistance computer: left veh dx; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_leftVehVxRel` | page 1 | Driver assistance computer: left veh vx rel; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_leftVehDy` | page 1 | Driver assistance computer: left veh dy | 20\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_leftVehId` | page 1 | Driver assistance computer: left veh id; raw 127 = signal not available (SNA) | 27\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 126 | 127 = `SNA` | validated |
| `DAS_leftVeh2Type` | page 1 | Driver assistance computer: left veh2 type | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_leftVeh2RelevantForControl` | page 1 | Driver assistance computer: left veh2 relevant for control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_leftVeh2Dx` | page 1 | Driver assistance computer: left veh2 dx; raw 255 = signal not available (SNA) | 39\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_leftVeh2VxRel` | page 1 | Driver assistance computer: left veh2 vx rel; raw 15 = signal not available (SNA) | 47\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_leftVeh2Dy` | page 1 | Driver assistance computer: left veh2 dy | 51\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_leftVeh2Id` | page 1 | Driver assistance computer: left veh2 id; raw 0 = signal not available (SNA) | 58\|6 | little-endian | unsigned | 1 | 0 |  | 1 to 63 | 0 = `SNA` | validated |
| `DAS_rightVehType` | page 2 | Driver assistance computer: right veh type | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_rightVehRelevantForControl` | page 2 | Driver assistance computer: right veh relevant for control | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_rightVehDx` | page 2 | Driver assistance computer: right veh dx; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_rightVehVxRel` | page 2 | Driver assistance computer: right veh vx rel; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_rightVehDy` | page 2 | Driver assistance computer: right veh dy | 20\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_rightVehId` | page 2 | Driver assistance computer: right veh id; raw 127 = signal not available (SNA) | 27\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 126 | 127 = `SNA` | validated |
| `DAS_rightVeh2Type` | page 2 | Driver assistance computer: right veh2 type | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_rightVeh2RelevantForControl` | page 2 | Driver assistance computer: right veh2 relevant for control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_rightVeh2Dx` | page 2 | Driver assistance computer: right veh2 dx; raw 255 = signal not available (SNA) | 39\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_rightVeh2VxRel` | page 2 | Driver assistance computer: right veh2 vx rel; raw 15 = signal not available (SNA) | 47\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_rightVeh2Dy` | page 2 | Driver assistance computer: right veh2 dy | 51\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_rightVeh2Id` | page 2 | Driver assistance computer: right veh2 id; raw 0 = signal not available (SNA) | 58\|6 | little-endian | unsigned | 1 | 0 |  | 1 to 63 | 0 = `SNA` | validated |
| `DAS_cutinVehType` | page 3 | Driver assistance computer: cutin veh type | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `TRUCK`<br>2 = `CAR`<br>3 = `MOTORCYCLE`<br>4 = `BICYCLE`<br>5 = `PEDESTRIAN` | validated |
| `DAS_cutinVehRelevantForControl` | page 3 | Driver assistance computer: cutin veh relevant for control | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_cutinVehDx` | page 3 | Driver assistance computer: cutin veh dx; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | m | 0 to 127 | 255 = `SNA` | validated |
| `DAS_cutinVehVxRel` | page 3 | Driver assistance computer: cutin veh vx rel; raw 15 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 4 | -30 | m/s | -30 to 26 | 15 = `SNA` | validated |
| `DAS_cutinVehDy` | page 3 | Driver assistance computer: cutin veh dy | 20\|7 | little-endian | unsigned | 0.35 | -22.05 | m | -22.05 to 22.4 |  | validated |
| `DAS_cutinVehId` | page 3 | Driver assistance computer: cutin veh id; raw 127 = signal not available (SNA) | 27\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 126 | 127 = `SNA` | validated |
| `DAS_roadSignColor` | page 4 | Driver assistance computer: road sign color | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `RED`<br>2 = `YELLOW`<br>3 = `GREEN`<br>4 = `RED_YELLOW` | validated |
| `DAS_roadSignId` | page 4 | Driver assistance computer: road sign id; raw 255 = signal not available (SNA) | 6\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 0 = `STOP_SIGN`<br>1 = `TRAFFIC_LIGHT`<br>255 = `SNA` | validated |
| `DAS_roadSignStopLineDist` | page 4 | Driver assistance computer: road sign stop line dist; raw 1023 = signal not available (SNA) | 14\|10 | little-endian | unsigned | 0.2 | -20 | m | -20 to 184.4 | 1023 = `SNA` | validated |
| `DAS_roadSignControlActive` | page 4 | Driver assistance computer: road sign control active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DAS_roadSignSource` | page 4 | Driver assistance computer: road sign source | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `NAV`<br>2 = `VISION` | validated |
| `DAS_roadSignArrow` | page 4 | Driver assistance computer: road sign arrow | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CIRCLE`<br>1 = `LEFT`<br>2 = `RIGHT`<br>3 = `STRAIGHT`<br>4 = `UNKNOWN` | validated |
| `DAS_roadSignOrientation` | page 4 | Driver assistance computer: road sign orientation | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VERTICAL_3_LIGHT`<br>2 = `HORIZONTAL_3_LIGHT` | validated |

## Multiplexing

`DAS_objectId` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals), page 1 (12 signals), page 2 (12 signals), page 3 (6 signals), page 4 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
