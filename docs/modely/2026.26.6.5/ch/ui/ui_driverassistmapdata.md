---
layout: default
title: "UI_driverAssistMapData (0x238) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: driver assist map data. Tesla Model Y CAN bus message UI_driverAssistMapData (0x238) of Touchscreen user interface computer, firmware 2026.26.6.5, 30 signals (UI_mapSpeedLimitDependency, UI_roadClass, UI_inSuperchargerGeofence, UI_mapSpeedUnits and 26 more). Bit layout, scaling, units and value tables."
---

# UI_driverAssistMapData (0x238) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: driver assist map data; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 30 signals of UI_driverAssistMapData as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverAssistMapData` |
| CAN id | 0x238 (568) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 30 |

## Signals of UI_driverAssistMapData

Tesla Model Y CAN bus signals in `UI_driverAssistMapData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_mapSpeedLimitDependency` | Touchscreen user interface computer: map speed limit dependency; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NONE`<br>1 = `SCHOOL`<br>2 = `RAIN`<br>3 = `SNOW`<br>4 = `TIME`<br>5 = `SEASON`<br>6 = `LANE`<br>7 = `SNA` | plausible |
| `UI_roadClass` | Autopilot map road class; raw 0 = signal not available (SNA) | 3\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `UNKNOWN_INVALID_SNA`<br>1 = `CLASS_1_MAJOR`<br>2 = `CLASS_2`<br>3 = `CLASS_3`<br>4 = `CLASS_4`<br>5 = `CLASS_5`<br>6 = `CLASS_6_MINOR` | validated |
| `UI_inSuperchargerGeofence` | Touchscreen user interface computer: in supercharger geofence | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_mapSpeedUnits` | Touchscreen user interface computer: map speed units | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MPH`<br>1 = `KPH` | plausible |
| `UI_mapSpeedLimit` | Touchscreen user interface computer: map speed limit; raw 31 = signal not available (SNA) | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 30 | 0 = `UNKNOWN`<br>1 = `LESS_OR_EQ_5`<br>2 = `LESS_OR_EQ_7`<br>3 = `LESS_OR_EQ_10`<br>4 = `LESS_OR_EQ_15`<br>5 = `LESS_OR_EQ_20`<br>6 = `LESS_OR_EQ_25`<br>7 = `LESS_OR_EQ_30`<br>8 = `LESS_OR_EQ_35`<br>9 = `LESS_OR_EQ_40`<br>10 = `LESS_OR_EQ_45`<br>11 = `LESS_OR_EQ_50`<br>12 = `LESS_OR_EQ_55`<br>13 = `LESS_OR_EQ_60`<br>14 = `LESS_OR_EQ_65`<br>15 = `LESS_OR_EQ_70`<br>16 = `LESS_OR_EQ_75`<br>17 = `LESS_OR_EQ_80`<br>18 = `LESS_OR_EQ_85`<br>19 = `LESS_OR_EQ_90`<br>20 = `LESS_OR_EQ_95`<br>21 = `LESS_OR_EQ_100`<br>22 = `LESS_OR_EQ_105`<br>23 = `LESS_OR_EQ_110`<br>24 = `LESS_OR_EQ_115`<br>25 = `LESS_OR_EQ_120`<br>26 = `LESS_OR_EQ_130`<br>27 = `LESS_OR_EQ_140`<br>28 = `LESS_OR_EQ_150`<br>29 = `LESS_OR_EQ_160`<br>30 = `UNLIMITED`<br>31 = `SNA` | plausible |
| `UI_mapSpeedLimitType` | Touchscreen user interface computer: map speed limit type; raw 7 = signal not available (SNA) | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 1 = `REGULAR`<br>2 = `ADVISORY`<br>3 = `DEPENDENT`<br>4 = `BUMPS`<br>7 = `UNKNOWN_SNA` | plausible |
| `UI_countryCode` | Touchscreen user interface computer: country code; raw 1023 = signal not available (SNA) | 16\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1022 | 0 = `UNKNOWN`<br>1023 = `SNA` | plausible |
| `UI_streetCount` | Touchscreen user interface computer: street count | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | plausible |
| `UI_gpsRoadMatch` | Touchscreen user interface computer: gps road match | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_navRouteActive` | Navigation route is active | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_parallelAutoparkEnabled` | Autopilot map parallel park enabled. | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_perpendicularAutoparkEnabled` | Autopilot map perpendicular park enabled. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_nextBranchDist` | Touchscreen user interface computer: next branch dist; raw 31 = signal not available (SNA) | 32\|5 | little-endian | unsigned | 10 | 0 | m | 0 to 300 | 31 = `SNA` | plausible |
| `UI_controlledAccess` | DAS map controlled access segment. | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_nextBranchLeftOffRamp` | Touchscreen user interface computer: next branch left off ramp | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_nextBranchRightOffRamp` | Touchscreen user interface computer: next branch right off ramp | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectLeftLane` | Touchscreen user interface computer: reject left lane | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectRightLane` | Touchscreen user interface computer: reject right lane | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectHPP` | Touchscreen user interface computer: reject HPP | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectNav` | Touchscreen user interface computer: reject nav | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectLeftFreeSpace` | Touchscreen user interface computer: reject left free space | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectRightFreeSpace` | Touchscreen user interface computer: reject right free space | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectAutosteer` | Touchscreen user interface computer: reject autosteer | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rejectHandsOn` | Touchscreen user interface computer: reject hands on | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_acceptBottsDots` | Touchscreen user interface computer: accept botts dots | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autosteerRestricted` | Autopilot map is autostreer restricted. | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_pmmEnabled` | Touchscreen user interface computer: pmm enabled | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_scaEnabled` | Touchscreen user interface computer: sca enabled | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_mapDataCounter` | Touchscreen user interface computer: map data counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `UI_mapDataChecksum` | Touchscreen user interface computer: map data checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
