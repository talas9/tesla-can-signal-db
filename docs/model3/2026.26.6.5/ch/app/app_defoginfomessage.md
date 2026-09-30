---
layout: default
title: "APP_defogInfoMessage (0x4FF) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: defog info message. Tesla Model 3 CAN bus message APP_defogInfoMessage (0x4FF) of Driver assistance computer (primary), firmware 2026.26.6.5, 6 signals (APP_cameraDefogMode, APP_selfieCamFanRpm, APP_forceDefroster, APP_checkThermalSysHealth and 2 more). Bit layout, scaling, units and value tables."
---

# APP_defogInfoMessage (0x4FF) — Driver assistance computer (primary), Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: defog info message; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APP_defogInfoMessage as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_defogInfoMessage` |
| CAN id | 0x4FF (1279) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of APP_defogInfoMessage

Tesla Model 3 CAN bus signals in `APP_defogInfoMessage`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_cameraDefogMode` | Instructs SGK to activate or deactivate cameras when the vehicle is in a parked state; raw 0 = signal not available (SNA) | 0\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `CAMERA_DEFOG_SNA`<br>1 = `CAMERA_DEFOG_ENABLE`<br>2 = `CAMERA_DEFOG_DISABLE_LOW_SOC`<br>3 = `CAMERA_DEFOG_DISABLE_UI_FSD_NOT_ENABLED`<br>4 = `CAMERA_DEFOG_DISABLE_INDOORS`<br>5 = `CAMERA_DEFOG_DISABLE_NOT_FSD_CAR`<br>6 = `CAMERA_DEFOG_DISABLE_FEATURE_FLAG_NOT_ENABLED`<br>7 = `CAMERA_DEFOG_DISABLE_BAD_HW`<br>8 = `CAMERA_DEFOG_DISABLE_VEHICLE_NOT_DELIVERED`<br>9 = `CAMERA_DEFOG_DISABLE_UNKNOWN`<br>10 = `CAMERA_DEFOG_DISABLE_NO_MIN_STANDBY_POWER`<br>11 = `CAMERA_DEFOG_DISABLE_START_FSD_BUTTON_NOT_ENABLED` | validated |
| `APP_selfieCamFanRpm` | Indicates the selfie camera fan rpm; raw 65535 = signal not available (SNA) | 5\|16 | little-endian | unsigned | 1 | 0 | rpm | 0 to 65534 | 65535 = `SNA` | validated |
| `APP_forceDefroster` | Force Front Defroster mode instructs VC to activate defog/defrost when AP detects dew/fog; raw 0 = signal not available (SNA) | 21\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `DEFROSTER_SNA`<br>1 = `DEFROSTER_NONE`<br>2 = `DEFROSTER_DEFOG`<br>3 = `DEFROSTER_DEFROST` | validated |
| `APP_checkThermalSysHealth` | Driver assistance computer (primary): check thermal sys health; raw 0 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `EVAL_SNA`<br>1 = `EVAL_NONE`<br>2 = `EVAL_THERMAL` | validated |
| `APP_defogInfoMessageChecksum` | Driver assistance computer (primary): defog info message checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `APP_hvacRequest` | Das request to turn on HVAC; raw 0 = signal not available (SNA) | 61\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `INACTIVE`<br>2 = `ACTIVE` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
