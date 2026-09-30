---
layout: default
title: "VCLEFT_lightStatus (0x3E2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: light status. Tesla Model 3 / Model Y CAN bus message VCLEFT_lightStatus (0x3E2) of Left body controller, firmware 2026.26.6.5, 27 signals (VCLEFT_brakeLightStatus, VCLEFT_tailLightStatus, VCLEFT_turnSignalStatus, VCLEFT_FLMapLightStatus and 23 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_lightStatus (0x3E2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left body controller message: light status; frame length observed on a vehicle bus. This page documents the 27 signals of VCLEFT_lightStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_lightStatus` |
| CAN id | 0x3E2 (994) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 27 |

## Signals of VCLEFT_lightStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_lightStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_brakeLightStatus` | Status of rear left brake light source; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_tailLightStatus` | Status of left tail (rear position) light source; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_turnSignalStatus` | Status of rear left turn signal light source; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_FLMapLightStatus` | Status of front left overhead map light; raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_FRMapLightStatus` | Status of front right overhead map light; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_RLMapLightStatus` | Status of rear left overhead map light; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_RRMapLightStatus` | Status of rear right overhead map light; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_FLMapLightSwitchPressed` | Status of front left overhead map light switch | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_FRMapLightSwitchPressed` | Status of front right overhead map light switch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_RLMapLightSwitchPressed` | Status of rear left overhead map light switch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_RRMapLightSwitchPressed` | Status of rear right overhead map light switch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_leftTurnTrailerLightStatus` | The desired on/off state of the trailer left turn light; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_rightTrnTrailerLightStatus` | The desired on/off state of the trailer right turn light; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_brakeTrailerLightStatus` | The desired on/off state of the trailer brake light; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_tailTrailerLightStatus` | The desired on/off state of the trailer tail light; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_fogTrailerLightStatus` | The desired on/off state of the trailer fog light; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_frontRideHeight` | Left body controller: front ride height; raw 128 = signal not available (SNA) | 28\|8 | little-endian | signed | 1 | 0 | mm | -127 to 127 | -128 = `SNA` | validated |
| `VCLEFT_rearRideHeight` | Left body controller: rear ride height; raw 128 = signal not available (SNA) | 36\|8 | little-endian | signed | 1 | 0 | mm | -127 to 127 | -128 = `SNA` | validated |
| `VCLEFT_leftDashRGBPowerRequest` | Left body controller: left dash RGB power request | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rightDashRGBPowerRequest` | Left body controller: right dash RGB power request | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_trailerDetected` | Trailer light detection status; raw 0 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `TRAILER_LIGHT_DETECTION_SNA`<br>1 = `TRAILER_LIGHT_DETECTION_FAULT`<br>2 = `TRAILER_LIGHT_DETECTION_DETECTED`<br>3 = `TRAILER_LIGHT_DETECTION_NOT_DETECTED` | validated |
| `VCLEFT_rideHeightSensorFault` | Fault status of the front and rear ride height sensors | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_reverseTrailerLightStatus` | The desired on/off state of the trailer reverse light; raw 3 = signal not available (SNA) | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_tailLightOutageStatus` | Left body controller: tail light outage status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_reverseLightStatus` | Status of left rear body side reverse light source; raw 3 = signal not available (SNA) | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_thirdRowLeftMapLightSwitchPressed` | Reports the status of the third row left overhead map light switch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_thirdRowRightMapLightSwitchPressed` | Reports the status of the third row right overhead map light switch | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
