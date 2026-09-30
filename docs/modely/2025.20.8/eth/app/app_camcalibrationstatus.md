---
layout: default
title: "APP_camCalibrationStatus (0x7FE) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH"
description: "Driver assistance computer (primary) message: cam calibration status. Ethernet-side message APP_camCalibrationStatus of Driver assistance computer (primary) for Tesla Model Y firmware 2025.20.8, 41 signals (APP_cameraPosition, APP_mainCamExtPitchCal, APP_mainCamExtYawCal, APP_mainCalibTime and 37 more). Bit layout, scaling, units and value tables."
---

# APP_camCalibrationStatus (0x7FE) — Driver assistance computer (primary), Tesla Model Y 2025.20.8 ETH

Driver assistance computer (primary) message: cam calibration status. This page documents the 41 signals of APP_camCalibrationStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APP_camCalibrationStatus` |
| Ethernet-side id | 0x7FE (2046) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APP |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 41 |

## Signals of APP_camCalibrationStatus

Tesla Model Y CAN bus signals in `APP_camCalibrationStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `APP_cameraPosition` | selector | Driver assistance computer (primary): camera position | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INVALID`<br>1 = `MAIN`<br>2 = `NARROW`<br>3 = `FISHEYE`<br>4 = `L_PILLAR`<br>5 = `R_PILLAR`<br>6 = `L_REPEATER`<br>7 = `R_REPEATER`<br>8 = `BACKUP`<br>9 = `SELFIE`<br>10 = `FASCIA` | plausible |
| `APP_mainCamExtPitchCal` | page 1 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_mainCamExtYawCal` | page 1 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_mainCalibTime` | page 1 | Driver assistance computer (primary): main calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_mainCalibProgress` | page 1 | The percent progress of the main camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_mainCalibrated` | page 1 | Whether or not the main camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_narrowCamExtPitchCal` | page 2 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_narrowCamExtYawCal` | page 2 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_narrowCalibTime` | page 2 | Driver assistance computer (primary): narrow calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_narrowCalibProgress` | page 2 | The percent progress of the narrow camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_narrowCalibrated` | page 2 | Whether or not the narrow camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_fisheyeCamExtPitchCal` | page 3 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_fisheyeCamExtYawCal` | page 3 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_fisheyeCalibTime` | page 3 | Driver assistance computer (primary): fisheye calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_fisheyeCalibProgress` | page 3 | The percent progress of the fisheye camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_fisheyeCalibrated` | page 3 | Whether or not the fisheye camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_lPillarCamExtPitchCal` | page 4 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_lPillarCamExtYawCal` | page 4 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_lPillarCalibTime` | page 4 | Driver assistance computer (primary): l pillar calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_lPillarCalibProgress` | page 4 | The percent progress of the left pillar camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_lPillarCalibrated` | page 4 | Whether or not the left pillar camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_rPillarCamExtPitchCal` | page 5 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_rPillarCamExtYawCal` | page 5 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_rPillarCalibTime` | page 5 | Driver assistance computer (primary): r pillar calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_rPillarCalibProgress` | page 5 | The percent progress of the right pillar camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_rPillarCalibrated` | page 5 | Whether or not the right pillar camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_lRepeatCamExtPitchCal` | page 6 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_lRepeatCamExtYawCal` | page 6 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_lRepeatCalibTime` | page 6 | Driver assistance computer (primary): l repeat calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_lRepeatCalibProgress` | page 6 | The percent progress of the left repeater camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_lRepeatCalibrated` | page 6 | Whether or not the left repeater camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_rRepeatCamExtPitchCal` | page 7 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_rRepeatCamExtYawCal` | page 7 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_rRepeatCalibTime` | page 7 | Driver assistance computer (primary): r repeat calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_rRepeatCalibProgress` | page 7 | The percent progress of the right repeater camera calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_rRepeatCalibrated` | page 7 | Whether or not the right repeater camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_backupCamExtPitchCal` | page 8 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 8\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_backupCamExtYawCal` | page 8 | The calibration, pitch or yaw offset of a camera; raw 511 = signal not available (SNA) | 17\|9 | little-endian | unsigned | 0.05 | -12.5 | deg | -12.5 to 12.5 | 511 = `SNA` | validated |
| `APP_backupCalibTime` | page 8 | Driver assistance computer (primary): backup calib time; raw 127 = signal not available (SNA) | 26\|7 | little-endian | unsigned | 1 | 0 | min | 0 to 126 | 127 = `SNA` | validated |
| `APP_backupCalibProgress` | page 8 | The percent progress of the backup calibration; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 1 | 0 | percent | 0 to 100 | 127 = `SNA` | validated |
| `APP_backupCalibrated` | page 8 | Whether or not the backup camera is calibrated. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`APP_cameraPosition` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals), page 2 (5 signals), page 3 (5 signals), page 4 (5 signals), page 5 (5 signals), page 6 (5 signals), page 7 (5 signals), page 8 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
