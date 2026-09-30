---
layout: default
title: "UI_driverAssistRoadSign (0x218) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: driver assist road sign. Tesla Model 3 CAN bus message UI_driverAssistRoadSign (0x218) of Touchscreen user interface computer, firmware 2025.20.8, 20 signals (UI_roadSign, UI_splineLocConfidence, UI_splineID, UI_roadSignCounter and 16 more). Bit layout, scaling, units and value tables."
---

# UI_driverAssistRoadSign (0x218) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN

Touchscreen user interface computer message: driver assist road sign; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 20 signals of UI_driverAssistRoadSign as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverAssistRoadSign` |
| CAN id | 0x218 (536) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 20 |

## Signals of UI_driverAssistRoadSign

Tesla Model 3 CAN bus signals in `UI_driverAssistRoadSign`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_roadSign` | selector | Touchscreen user interface computer: road sign; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 0 = `NONE`<br>1 = `STOP_SIGN`<br>2 = `TRAFFIC_LIGHT`<br>3 = `SPEED_LIMIT`<br>4 = `SPEED_SPLINE`<br>5 = `SPLINE_ID_FULL`<br>255 = `SNA` | plausible |
| `UI_splineLocConfidence` |  | Touchscreen user interface computer: spline loc confidence; raw 0 = signal not available (SNA) | 40\|7 | little-endian | unsigned | 1 | 0 | 1 | 1 to 127 | 0 = `SNA` | plausible |
| `UI_splineID` |  | Touchscreen user interface computer: spline ID | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_roadSignCounter` |  | Touchscreen user interface computer: road sign counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_roadSignChecksum` |  | Touchscreen user interface computer: road sign checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_dummyData` | page 0 | Touchscreen user interface computer: dummy data | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_stopSignStopLineDist` | page 1 | Touchscreen user interface computer: stop sign stop line dist; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.25 | -8 | m | -8 to 247.5 | 1023 = `SNA` | plausible |
| `UI_stopSignStopLineConf` | page 1 | Touchscreen user interface computer: stop sign stop line conf; raw 0 = signal not available (SNA) | 18\|7 | little-endian | unsigned | 1 | 0 | 1 | 1 to 127 | 0 = `SNA` | plausible |
| `UI_trafficLightStopLineDist` | page 2 | Touchscreen user interface computer: traffic light stop line dist; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.25 | -8 | m | -8 to 247.5 | 1023 = `SNA` | plausible |
| `UI_trafficLightStopLineConf` | page 2 | Touchscreen user interface computer: traffic light stop line conf; raw 0 = signal not available (SNA) | 18\|7 | little-endian | unsigned | 1 | 0 | 1 | 1 to 127 | 0 = `SNA` | plausible |
| `UI_baseMapSpeedLimitMPS` | page 3 | Touchscreen user interface computer: base map speed limit MPS; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.25 | 0 | m/s | 0 to 63.5 | 255 = `SNA` | plausible |
| `UI_bottomQrtlFleetSpeedMPS` | page 3 | Touchscreen user interface computer: bottom qrtl fleet speed MPS; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.25 | 0 | m/s | 0 to 63.5 | 255 = `SNA` | plausible |
| `UI_topQrtlFleetSpeedMPS` | page 3 | Touchscreen user interface computer: top qrtl fleet speed MPS; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.25 | 0 | m/s | 0 to 63.5 | 255 = `SNA` | plausible |
| `UI_meanFleetSplineSpeedMPS` | page 4 | Touchscreen user interface computer: mean fleet spline speed MPS; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.25 | 0 | m/s | 0 to 63.5 | 255 = `SNA` | plausible |
| `UI_medianFleetSpeedMPS` | page 4 | Touchscreen user interface computer: median fleet speed MPS; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.25 | 0 | m/s | 0 to 63.5 | 255 = `SNA` | plausible |
| `UI_meanFleetSplineAccelMPS2` | page 4 | Touchscreen user interface computer: mean fleet spline accel MPS2; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.05 | -6.35 | m/s^2 | -6.35 to 6.35 | 255 = `SNA` | plausible |
| `UI_rampType` | page 4 | Touchscreen user interface computer: ramp type; raw 0 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `NONE_SNA`<br>1 = `ENTRANCE`<br>2 = `EXIT`<br>3 = `INTERCHANGE_ENTRANCE`<br>4 = `INTERCHANGE_EXIT` | plausible |
| `UI_valhallaRamp` | page 4 | Touchscreen user interface computer: valhalla ramp; raw 0 = signal not available (SNA) | 35\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NOT_ON_RAMP`<br>2 = `ON_RAMP` | plausible |
| `UI_overrideACMFleetSpeed` | page 4 | Touchscreen user interface computer: override ACM fleet speed | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_currSplineIdFull` | page 5 | Touchscreen user interface computer: curr spline id full; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 | 1 | 1 to 4294967295 | 0 = `SNA` | plausible |

## Multiplexing

`UI_roadSign` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (2 signals), page 2 (2 signals), page 3 (3 signals), page 4 (6 signals), page 5 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
