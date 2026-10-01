---
layout: default
title: "APP_camCalibrationStatus (0x3F4) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: cam calibration status. Tesla Model 3 CAN bus message APP_camCalibrationStatus (0x3F4) of Driver assistance computer (primary), firmware 2026.26.6.5, 46 signals (APP_cameraPosition, APP_mainCamExtPitchCal, APP_mainCamExtYawCal, APP_mainCalibTime and 42 more). Bit layout, scaling, units and value tables."
---

# APP_camCalibrationStatus (0x3F4) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: cam calibration status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 46 signals of APP_camCalibrationStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_camCalibrationStatus` |
| CAN id | 0x3F4 (1012) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 46 |

## Signals of APP_camCalibrationStatus

Tesla Model 3 CAN bus signals in `APP_camCalibrationStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `APP_cameraPosition` | selector | Driver assistance computer (primary): camera position | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INVALID`<br>1 = `MAIN`<br>2 = `NARROW`<br>3 = `FISHEYE`<br>4 = `L_PILLAR`<br>5 = `R_PILLAR`<br>6 = `L_REPEATER`<br>7 = `R_REPEATER`<br>8 = `BACKUP`<br>9 = `SELFIE`<br>10 = `FASCIA` | plausible |
| `APP_mainCamExtPitchCal` | page 1 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_mainCamExtYawCal` | page 1 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_mainCalibTime` | page 1 | Driver assistance computer (primary): main calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_mainCalibProgress` | page 1 | The percent progress of the main camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_mainCalibrated` | page 1 | Whether or not the main camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_narrowCamExtPitchCal` | page 2 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_narrowCamExtYawCal` | page 2 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_narrowCalibTime` | page 2 | Driver assistance computer (primary): narrow calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_narrowCalibProgress` | page 2 | The percent progress of the narrow camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_narrowCalibrated` | page 2 | Whether or not the narrow camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_fisheyeCamExtPitchCal` | page 3 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_fisheyeCamExtYawCal` | page 3 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_fisheyeCalibTime` | page 3 | Driver assistance computer (primary): fisheye calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_fisheyeCalibProgress` | page 3 | The percent progress of the fisheye camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_fisheyeCalibrated` | page 3 | Whether or not the fisheye camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_lPillarCamExtPitchCal` | page 4 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_lPillarCamExtYawCal` | page 4 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_lPillarCalibTime` | page 4 | Driver assistance computer (primary): l pillar calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_lPillarCalibProgress` | page 4 | The percent progress of the left pillar camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_lPillarCalibrated` | page 4 | Whether or not the left pillar camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_rPillarCamExtPitchCal` | page 5 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_rPillarCamExtYawCal` | page 5 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_rPillarCalibTime` | page 5 | Driver assistance computer (primary): r pillar calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_rPillarCalibProgress` | page 5 | The percent progress of the right pillar camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_rPillarCalibrated` | page 5 | Whether or not the right pillar camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_lRepeatCamExtPitchCal` | page 6 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_lRepeatCamExtYawCal` | page 6 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_lRepeatCalibTime` | page 6 | Driver assistance computer (primary): l repeat calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_lRepeatCalibProgress` | page 6 | The percent progress of the left repeater camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_lRepeatCalibrated` | page 6 | Whether or not the left repeater camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_rRepeatCamExtPitchCal` | page 7 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_rRepeatCamExtYawCal` | page 7 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_rRepeatCalibTime` | page 7 | Driver assistance computer (primary): r repeat calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_rRepeatCalibProgress` | page 7 | The percent progress of the right repeater camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_rRepeatCalibrated` | page 7 | Whether or not the right repeater camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_backupCamExtPitchCal` | page 8 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_backupCamExtYawCal` | page 8 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_backupCalibTime` | page 8 | Driver assistance computer (primary): backup calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_backupCalibProgress` | page 8 | The percent progress of the backup calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_backupCalibrated` | page 8 | Whether or not the backup camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APP_fasciaCamExtPitchCal` | page 10 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_fasciaCamExtYawCal` | page 10 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | plausible |
| `APP_fasciaCalibTime` | page 10 | Driver assistance computer (primary): fascia calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | plausible |
| `APP_fasciaCalibProgress` | page 10 | The percent progress of the fascia calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | plausible |
| `APP_fasciaCalibrated` | page 10 | Whether or not the fascia camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`APP_cameraPosition` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals), page 2 (5 signals), page 3 (5 signals), page 4 (5 signals), page 5 (5 signals), page 6 (5 signals), page 7 (5 signals), page 8 (5 signals), page 10 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
