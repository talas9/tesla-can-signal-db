---
layout: default
title: "VCLEFT_lightStatus (0x3E2) — Left body controller, Tesla Model 3 2025.20.8 ETH"
description: "Left body controller message: light status. Ethernet-side message VCLEFT_lightStatus of Left body controller for Tesla Model 3 firmware 2025.20.8, 25 signals (VCLEFT_brakeLightStatus, VCLEFT_tailLightStatus, VCLEFT_turnSignalStatus, VCLEFT_FLMapLightStatus and 21 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_lightStatus (0x3E2) — Left body controller, Tesla Model 3 2025.20.8 ETH

Left body controller message: light status. This page documents the 25 signals of VCLEFT_lightStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_lightStatus` |
| Ethernet-side id | 0x3E2 (994) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 25 |

## Signals of VCLEFT_lightStatus

Tesla Model 3 CAN bus signals in `VCLEFT_lightStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

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

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
