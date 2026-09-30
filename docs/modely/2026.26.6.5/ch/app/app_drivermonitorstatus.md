---
layout: default
title: "APP_driverMonitorStatus (0x3AB) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: driver monitor status. Tesla Model Y CAN bus message APP_driverMonitorStatus (0x3AB) of Driver assistance computer (primary), firmware 2026.26.6.5, 25 signals (APP_cabinCamTelemetryOn, APP_attnMonitorVersion, APP_attnBasedDriverMonitorOn, APP_handsOnDetected and 21 more). Bit layout, scaling, units and value tables."
---

# APP_driverMonitorStatus (0x3AB) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: driver monitor status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 25 signals of APP_driverMonitorStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_driverMonitorStatus` |
| CAN id | 0x3AB (939) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 5 bytes |
| Cycle time | 500 ms |
| Signals | 25 |

## Signals of APP_driverMonitorStatus

Tesla Model Y CAN bus signals in `APP_driverMonitorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_cabinCamTelemetryOn` | Driver assistance computer (primary): cabin cam telemetry on | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_attnMonitorVersion` | Driver assistance computer (primary): attn monitor version; raw 7 = signal not available (SNA) | 1\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `V1_0`<br>1 = `V1_1`<br>7 = `SNA` | validated |
| `APP_attnBasedDriverMonitorOn` | Indicates whether attention based Driver Monitor is currently enabled during Autosteer/Full Self-Driving (FSD). | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_handsOnDetected` | Indicates whether Driver Monitor detects that a user has their hands on the wheel during Autosteer/Full Self-Driving (FSD). | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_handsOnDetectedSource` | Reports the source of the hands on detection output from driver monitor; raw 7 = signal not available (SNA) | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `TORQUE`<br>1 = `SELFIE`<br>2 = `TORQUE_AND_SELFIE`<br>3 = `TORQUE_IGNORE_SELFIE_FOR_CAVEAT`<br>7 = `SNA` | validated |
| `APP_cabinCamBlinded` | Indicates that the cabin camera is detected as blinded. | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_cabinCamDark` | Indicates that the cabin camera is detected as dark. | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverStateUnknown` | Indicates that the cabin camera detects the driver state as unknown. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverNotLively` | Reports that the cabin camera detects the driver as not lively. | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverStateUnknownHyst` | Indicates that the cabin camera detects the driver state as unknown, with a logging lag to reduce excess signal noise by briefly indicating 'unknown' even if 'unknown' is no longer detected. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverLowNominal` | Indicates that the cabin camera detects the driver's forward eye gaze is low. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverHeadCappedHyst` | Indicates that the cabin camera detects a driver head obstruction. | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverSunglassesUseHyst` | Indicates that the cabin camera detects driver is wearing sunglasses. | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_cabinLowLux` | Indicates that the cabin camera detects cabin illumination is low. | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_cabinCamInconsistent` | Indicates that Driver Monitor detects inconsistencies in cabin camera network signals. | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverLeaningBack` | Indicates that the cabin camera detects driver may be leaning back and not ready to take over. | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverLowEyeVisibility` | Indicates that the cabin camera detects degraded driver eye visibility. | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverHandsNotReady` | Indicates that the cabin camera detects driver hands may not be near steering wheel/yoke. | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_driverSeatUnoccupied` | Reports that the cabin camera detects that driver seat may not be occupied. | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_handsOnInputRequired` | Indicates that driver monitoring requires driver hands-on acknowledgement. | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_cabinCamDarkHyst` | Indicates that the cabin camera is detected as dark, with a logging lag to reduce excess signal noise by briefly indicating 'dark' even if 'dark' is no longer detected. | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_cabinLowLuxHyst` | Indicates that the cabin camera detects cabin illumination low, with a logging lag to reduce excess signal noise by briefly indicating 'low' even if 'low' is no longer detected. | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APP_ADDWSystemStatus` | Reports the Advanced Distracted Driver Warning (ADDW) system status. | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INACTIVE`<br>1 = `ACTIVE`<br>2 = `WARN`<br>3 = `FAULTED` | validated |
| `APP_dmStrictness` | Driver assistance computer (primary): dm strictness; raw 0 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `LOW`<br>2 = `MED`<br>3 = `HIGH` | validated |
| `APP_dmStrictnessReason` | Driver assistance computer (primary): dm strictness reason; raw 0 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 1 | 0 |  | 1 to 63 | 0 = `SNA`<br>1 = `VISION_FAILSAFES_OVERRIDE_ACTIVE`<br>2 = `INCREASED_STRICTNESS_FOR_NON_REDUNDANT_EPAS`<br>3 = `TRAFFIC_CONTROL_CONTEXT_RAILROAD`<br>4 = `FOLLOWING_CIPV_HIGH_DECEL`<br>5 = `VISIBILITY_DEGRADED_OFFGASSING`<br>6 = `HIGH_STRICTNESS_DEV_CTRL`<br>7 = `HIGH_ACCEL_OR_DECEL`<br>8 = `PEDAL_OVERRIDE`<br>9 = `HIGH_STRICTNESS_REQUIRED_FOR_DISTRACTION`<br>10 = `HEAD_DOWN`<br>11 = `ADVERSE_ROAD_CONDITIONS`<br>12 = `CAUTION_LIGHTS`<br>13 = `TOLLBOOTH`<br>14 = `VRU_IN_DRIVABLE_SPACE`<br>15 = `ESV_DETECTED`<br>16 = `SEVERE_SINGLE_FRONT_VISION_OCCLUSION`<br>17 = `SEVERE_LEFT_VISION_OCCLUSION_MANEUVER`<br>18 = `SEVERE_RIGHT_VISION_OCCLUSION_MANEUVER`<br>19 = `SEVERE_BACKUP_VISION_OCCLUSION_REVERSE`<br>20 = `SEVERE_LEFT_VISION_OCCLUSION_REVERSE`<br>21 = `SEVERE_RIGHT_VISION_OCCLUSION_REVERSE`<br>22 = `INCLEMENT_WEATHER`<br>23 = `FSD_DEGRADED`<br>24 = `SIDE_CAMERA_OCCLUSION`<br>25 = `SPEED_OVER_HIGH_THRESHOLD`<br>26 = `STEERING_ANGLE_OVER_THRESHOLD`<br>27 = `REFERENCE_LATERAL_ERROR_WARNING`<br>28 = `MED_STRICTNESS_SCENE_TAG_ACTIVE`<br>29 = `ONCOMING_TRAFFIC_PRESENT`<br>30 = `CONSTRUCTION`<br>31 = `AUTOWIPER_OFF`<br>32 = `AUTOHEADLIGHT_OFF`<br>33 = `PERSISTED_OFFGASSING`<br>34 = `ON_RAMP`<br>35 = `ON_INTERCHANGE`<br>36 = `DRIVER_FATIGUE_DETECTED`<br>37 = `HIGH_LATERAL_ACCELERATION`<br>38 = `WAITING_FOR_TRAFFIC_LIGHT`<br>39 = `UPCOMING_LATERAL_MANEUVER`<br>40 = `SPEED_BELOW_LOW_THRESHOLD_ON_CITY`<br>41 = `RANKER_ACTIVATION`<br>42 = `LOW_SPEED_CIPV_PRESENT`<br>43 = `FAILSAFES_ACTIVE`<br>44 = `ON_HIGHWAY_CIPV_PRESENT`<br>45 = `UPCOMING_INTERSECTION` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
