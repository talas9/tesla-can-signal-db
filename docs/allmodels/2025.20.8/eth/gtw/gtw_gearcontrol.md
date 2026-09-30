---
layout: default
title: "GTW_gearControl (0x678) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Gateway message: gear control. Ethernet-side message GTW_gearControl of Gateway for Tesla Model 3 / Model Y firmware 2025.20.8, 16 signals (GTW_gearControlChecksum, GTW_gearControlCounter, GTW_gearShiftRequest, GTW_osdActive and 12 more). Bit layout, scaling, units and value tables."
---

# GTW_gearControl (0x678) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH

Gateway message: gear control. This page documents the 16 signals of GTW_gearControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_gearControl` |
| Ethernet-side id | 0x678 (1656) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 16 |

## Signals of GTW_gearControl

Tesla Model 3 / Model Y CAN bus signals in `GTW_gearControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_gearControlChecksum` | Gateway: gear control checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `GTW_gearControlCounter` | Gateway: gear control counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `GTW_gearShiftRequest` | Request to change gear state from center display UI control; raw 0 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `GEAR_REQUEST_IDLE_SNA`<br>1 = `GEAR_REQUEST_PARK`<br>2 = `GEAR_REQUEST_REVERSE`<br>3 = `GEAR_REQUEST_NEUTRAL`<br>4 = `GEAR_REQUEST_DRIVE` | validated |
| `GTW_osdActive` | Whether OSD is active | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_primaryGearControlStatus` | Status of the center display UI control | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_QUALIFIED`<br>1 = `QUALIFIED`<br>2 = `NOT_QUALIFIED_FULLSCREEN`<br>3 = `NOT_QUALIFIED_DISPLAY_ERRS`<br>4 = `NOT_QUALIFIED_MANUAL`<br>5 = `NOT_QUALIFIED_FALSE_TOUCH`<br>6 = `NOT_QUALIFIED_LOW_BRIGHTNESS`<br>7 = `NOT_QUALIFIED_DISPLAY_FROZEN_ON_GESTURE`<br>8 = `NOT_QUALIFIED_CENTER_DISP_UI_UNHEALTHY`<br>9 = `NOT_QUALIFIED_UI_NO_RESP_GEAR_STRIP`<br>10 = `NOT_QUALIFIED_DISPLAY_UNTRAINED`<br>11 = `NOT_QUALIFIED_GEAR_STRIP_MISMATCH`<br>12 = `NOT_QUALIFIED_DISPLAY_ASIL_VIDEO_ERROR`<br>13 = `NOT_QUALIFIED_DISPLAY_KNOWN_FROZEN_SCREEN`<br>14 = `NOT_QUALIFIED_RHD_CONFIG_UNAVAILABLE` | validated |
| `GTW_gearStripEnable` | UI control for showing and or activating the primary gear strip interface | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_showNeutralButton` | Tell UI that it is time to animate the N button to be shown | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_showAutoParkButton` | Tell UI that it is time to animate the autopark button to be shown | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_autoParkRequest` | Request to auto park from center display UI control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `IDLE`<br>1 = `ACTIVE` | validated |
| `GTW_smartShiftStatus` | Based on the status of the infotainment system smart shift feature should be disabled; raw 0 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `DISABLED_SNA`<br>1 = `ENABLED`<br>2 = `DISABLED_UI_CONFIG`<br>3 = `DISABLED_CENTER_DISP_ERR`<br>4 = `DISABLED_CLUSTER_DISP_ERR`<br>5 = `DISABLED_UI_MIA`<br>6 = `DISABLED_FULLSCREEN`<br>7 = `DISABLED_DISQUALIFIED`<br>8 = `DISABLED_OSD_ACTIVATED`<br>9 = `DISABLED_AUDIO_NOT_READY` | validated |
| `GTW_processingRDgestures` | Is GTW processing R and D swipe gestures | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_processingTapPgestures` | Is GTW processing contextual tap-to-park gestures | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_gearStripChangeReason` | Gateway: gear strip change reason; raw 0 = signal not available (SNA) | 32\|5 | little-endian | unsigned | 1 | 0 |  | 1 to 31 | 0 = `SNA`<br>1 = `DRIVER_BRAKE_APPLY_ENABLE`<br>2 = `HIGH_JERK_ENABLE`<br>3 = `HIGH_STEERING_ANGLE_ENABLE`<br>4 = `VERY_LOW_SPEED_ENABLE`<br>5 = `TRAFFIC_CONTROL_NO_CHANGE`<br>6 = `MEDIUM_SPEED_DISABLE`<br>7 = `HIGH_ACCEL_DISABLE`<br>8 = `DI_MIA_ENABLE`<br>9 = `CRUISE_ACTIVE_DISABLE`<br>10 = `CHARGING_DISABLE`<br>11 = `P_AND_BRAKE_ENABLE`<br>12 = `NEUTRAL_ENABLE`<br>13 = `REVERSE_ENABLE`<br>14 = `DEFAULT_DISABLE`<br>15 = `FULLSCREEN_DISABLE`<br>16 = `NOT_DRIVE_STATE_DISABLE`<br>18 = `UI_MIA_ENABLE`<br>19 = `MISSING_SPEED_OR_STEERING_ESTIMATE_IN_D_ENABLE`<br>20 = `PARK_ENGAGED_ENABLE`<br>21 = `WOT_ENABLE`<br>22 = `EMERGENCY_OPERATION_ENABLE`<br>23 = `DRIVERLESS_NO_TAKEOVER_DISABLE`<br>24 = `VC_MIA_ENABLE`<br>25 = `VC_MIA_GRACE_DISABLE`<br>26 = `SLEEP_DISABLE`<br>27 = `EBUCK_DISABLE` | validated |
| `GTW_touchActive` | User present as touch on display is active | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_steamOff` | Let UI know to turn Steam off | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_screenPCBTemperature` | Reading from display i2c temperature sensor; raw 2047 = signal not available (SNA) | 47\|12 | big-endian | signed | 0.0625 | 0 | degC | -128 to 127.875 | 2047 = `GTW_I2C_TEMP_SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
