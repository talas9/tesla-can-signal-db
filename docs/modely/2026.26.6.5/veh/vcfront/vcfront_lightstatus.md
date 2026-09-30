---
layout: default
title: "VCFRONT_lightStatus (0x3F6) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: light status. Tesla Model Y CAN bus message VCFRONT_lightStatus (0x3F6) of Front body controller, firmware 2026.26.6.5, 27 signals (VCFRONT_lowBeamLeftStatus, VCFRONT_lowBeamRightStatus, VCFRONT_highBeamLeftStatus, VCFRONT_highBeamRightStatus and 23 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_lightStatus (0x3F6) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: light status; frame length observed on a vehicle bus. This page documents the 27 signals of VCFRONT_lightStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_lightStatus` |
| CAN id | 0x3F6 (1014) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 27 |

## Signals of VCFRONT_lightStatus

Tesla Model Y CAN bus signals in `VCFRONT_lightStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_lowBeamLeftStatus` |  | State of the left headlamp low beam light source; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_lowBeamRightStatus` |  | State of the right headlamp low beam light source; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_highBeamLeftStatus` |  | State of the left headlamp high beam light source; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_highBeamRightStatus` |  | State of the right headlamp high beam light source; raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_DRLLeftStatus` |  | Status of the left daytime running light source; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_DRLRightStatus` |  | Status of the right daytime running light source; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_fogLeftStatus` |  | State of the left front fog light source; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_fogRightStatus` |  | State of the right front fog light source; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_sideMarkersStatus` |  | State of the side marker / auxiliary park light sources (left and right are on a shared HSD); raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_sideRepeaterLeftStatus` |  | State of the left side repeater light source; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_sideRepeaterRightStatus` |  | State of the right side repeater light source; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_turnSignalLeftStatus` |  | State of the left front turn signal light source; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_turnSignalRightStatus` |  | State of the right front turn signal light source; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_parkLeftStatus` |  | State of the left position/park light source; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_parkRightStatus` |  | State of the right position/park light source; raw 3 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCFRONT_lowBeamLeftReadyForAiming` |  | Front body controller: low beam left ready for aiming | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_lowBeamRightReadyForAiming` |  | Front body controller: low beam right ready for aiming | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_lowBeamsOnForDRL` |  | Shows if the low beam light source is being used to fulfil the daytime running light function (for Canada) | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_rightHeadlampHealth` |  | Signal to report whether the right headlamp is powered and communicating | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SMART_LIGHT_HEALTH_OFF`<br>1 = `SMART_LIGHT_HEALTH_WAIT`<br>2 = `SMART_LIGHT_HEALTH_TIMEOUT`<br>3 = `SMART_LIGHT_HEALTH_OK`<br>4 = `SMART_LIGHT_HEALTH_COMMS_OK_NO_LIGHT`<br>5 = `SMART_LIGHT_HEALTH_NOT_CONFIGURED`<br>6 = `SMART_LIGHT_HEALTH_UPDATING`<br>7 = `SMART_LIGHT_HEALTH_RESERVED` | validated |
| `VC_leftHeadlampHealth` |  | Signal to report whether the left headlamp is powered and communicating | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SMART_LIGHT_HEALTH_OFF`<br>1 = `SMART_LIGHT_HEALTH_WAIT`<br>2 = `SMART_LIGHT_HEALTH_TIMEOUT`<br>3 = `SMART_LIGHT_HEALTH_OK`<br>4 = `SMART_LIGHT_HEALTH_COMMS_OK_NO_LIGHT`<br>5 = `SMART_LIGHT_HEALTH_NOT_CONFIGURED`<br>6 = `SMART_LIGHT_HEALTH_UPDATING`<br>7 = `SMART_LIGHT_HEALTH_RESERVED` | validated |
| `VCFRONT_lightStatusMuxIndex` | selector | Front body controller: light status mux index | 39\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HCM1_MIGRATION`<br>1 = `ADVANCED_LIGHTING` | plausible |
| `VCFRONT_isAdaptiveHighBeamAvailable` | page 1 | Indication that the conditions (country code, hardware config, etc.) are acceptable to use the advanced driving beam feature. | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isAdaptiveHighBeamFaulted` | page 1 | Detects if adaptive high beam functionality is unavailable or not operating as expected due to other dependencies. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_isBendLightingAvailable` | page 1 | Detects if region and hardware conditions currently allow operation of the bend lighting feature. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_advancedDrivingBeamStatus` | page 1 | Reports the current advanced driving beam system state. | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_SUPPORTED_OR_DISABLED`<br>1 = `ENABLED_AND_INACTIVE`<br>2 = `ACTIVE_SOME_COLUMNS_EXTINGUISHED`<br>3 = `ACTIVE_NO_COLUMNS_EXTINGUISHED` | validated |
| `VCFRONT_headlampBendAngle` | page 1 | Measures the adaptive headlight bend angle. | 47\|8 | little-endian | signed | 0.1 | 0 | deg | -12.7 to 12.7 |  | validated |
| `VCFRONT_headlampRoadClass` | page 1 | Reports the road class informing the use of dynamic low beams. | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOMINAL`<br>1 = `TOWNLIGHT`<br>2 = `MOTORWAY`<br>3 = `WET` | validated |

## Multiplexing

`VCFRONT_lightStatusMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
