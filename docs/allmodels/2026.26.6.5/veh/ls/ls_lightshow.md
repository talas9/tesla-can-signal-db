---
layout: default
title: "LS_lightShow (0x3F4) — LS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "LS ECU message: light show. Tesla Model 3 / Model Y CAN bus message LS_lightShow (0x3F4) of LS ECU, firmware 2026.26.6.5, 219 signals (LS_lightShowIndex, LS_lightLeftRampedChannel1Request, LS_lightLeftRampedChannel1Duration, LS_lightLeftRampedChannel2Request and 215 more). Bit layout, scaling, units and value tables."
---

# LS_lightShow (0x3F4) — LS ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

LS ECU message: light show; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 219 signals of LS_lightShow as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `LS_lightShow` |
| CAN id | 0x3F4 (1012) |
| ECU | [LS ECU](../../ls.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 219 |

## Signals of LS_lightShow

Tesla Model 3 / Model Y CAN bus signals in `LS_lightShow`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `LS_lightShowIndex` | selector | LS ECU: light show index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `LightShowMux0`<br>1 = `LightShowMux1`<br>2 = `LightShowMux2`<br>3 = `LightShowMux3`<br>4 = `LightShowMux4`<br>5 = `LightShowMux5`<br>6 = `LightShowMux6`<br>7 = `LightShowMux7`<br>8 = `LightShowMux8`<br>9 = `LightShowMux9`<br>10 = `LightShowMux10`<br>11 = `LightShowMux11`<br>12 = `LightShowMux12`<br>13 = `LightShowMux13`<br>14 = `LightShowMux14`<br>15 = `LightShowMux15`<br>16 = `LightShowMux16`<br>17 = `LightShowMux17`<br>18 = `LightShowMux18`<br>19 = `LightShowMux19`<br>20 = `LightShowMux20`<br>21 = `LightShowMux21`<br>22 = `LightShowMux22`<br>23 = `LightShowMux23`<br>24 = `LightShowMux24` | plausible |
| `LS_lightLeftRampedChannel1Request` | page 0 | LS ECU: light left ramped channel1 request | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel1Duration` | page 0 | LS ECU: light left ramped channel1 duration | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel2Request` | page 0 | LS ECU: light left ramped channel2 request | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel2Duration` | page 0 | LS ECU: light left ramped channel2 duration | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel3Request` | page 0 | LS ECU: light left ramped channel3 request | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel3Duration` | page 0 | LS ECU: light left ramped channel3 duration | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel4Request` | page 0 | LS ECU: light left ramped channel4 request | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel4Duration` | page 0 | LS ECU: light left ramped channel4 duration | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel5Request` | page 0 | LS ECU: light left ramped channel5 request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel5Duration` | page 0 | LS ECU: light left ramped channel5 duration | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel6Request` | page 0 | LS ECU: light left ramped channel6 request | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel6Duration` | page 0 | LS ECU: light left ramped channel6 duration | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightLeftRampedChannel7Request` | page 0 | LS ECU: light left ramped channel7 request | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLeftRampedChannel7Duration` | page 0 | LS ECU: light left ramped channel7 duration | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel1Request` | page 0 | LS ECU: light right ramped channel1 request | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel1Duration` | page 0 | LS ECU: light right ramped channel1 duration; raw 1 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel2Request` | page 0 | LS ECU: light right ramped channel2 request | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel2Duration` | page 0 | LS ECU: light right ramped channel2 duration; raw 1 = signal not available (SNA) | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel3Request` | page 0 | LS ECU: light right ramped channel3 request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel3Duration` | page 0 | LS ECU: light right ramped channel3 duration | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel4Request` | page 0 | LS ECU: light right ramped channel4 request | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel4Duration` | page 0 | LS ECU: light right ramped channel4 duration | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel5Request` | page 0 | LS ECU: light right ramped channel5 request | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel5Duration` | page 0 | LS ECU: light right ramped channel5 duration | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel6Request` | page 0 | LS ECU: light right ramped channel6 request | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel6Duration` | page 0 | LS ECU: light right ramped channel6 duration | 43\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRightRampedChannel7Request` | page 0 | LS ECU: light right ramped channel7 request | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRightRampedChannel7Duration` | page 0 | LS ECU: light right ramped channel7 duration | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTANT`<br>1 = `HALF_SECOND`<br>2 = `ONE_SECOND`<br>3 = `TWO_SECONDS` | validated |
| `LS_lightRearTurnLeftRequest` | page 0 | LS ECU: light rear turn left request | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRearTurnRightRequest` | page 0 | LS ECU: light rear turn right request | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightSideRepeaterLeftRequest` | page 0 | LS ECU: light side repeater left request | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightSideRepeaterRightRequest` | page 0 | LS ECU: light side repeater right request | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightSideMarkerLeftRequest` | page 0 | LS ECU: light side marker left request | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightSideMarkerRightRequest` | page 0 | LS ECU: light side marker right request | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightFrontFogLeftRequest` | page 0 | LS ECU: light front fog left request | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightFrontFogRightRequest` | page 0 | LS ECU: light front fog right request | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightRearFogRequest` | page 0 | LS ECU: light rear fog request | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightBrakeRequest` | page 0 | LS ECU: light brake request | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightTailLeftRequest` | page 0 | LS ECU: light tail left request | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightTailRightRequest` | page 0 | LS ECU: light tail right request | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightLicensePlateRequest` | page 0 | LS ECU: light license plate request | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightReverseRequest` | page 0 | LS ECU: light reverse request | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightAuxParkLeftRequest` | page 0 | LS ECU: light aux park left request | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_lightAuxParkRightRequest` | page 0 | LS ECU: light aux park right request | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_mirrorRequestLeft` | page 1 | LS ECU: mirror request left | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_mirrorRequestRight` | page 1 | LS ECU: mirror request right | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_liftgateRequest` | page 1 | LS ECU: liftgate request | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_windowRequestLF` | page 1 | LS ECU: window request LF | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_windowRequestLR` | page 1 | LS ECU: window request LR | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_windowRequestRF` | page 1 | LS ECU: window request RF | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_windowRequestRR` | page 1 | LS ECU: window request RR | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_presentingHandleRequestLF` | page 1 | LS ECU: presenting handle request LF | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_presentingHandleRequestLR` | page 1 | LS ECU: presenting handle request LR | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_presentingHandleRequestRF` | page 1 | LS ECU: presenting handle request RF | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_presentingHandleRequestRR` | page 1 | LS ECU: presenting handle request RR | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_powerFrontDoorRequestLeft` | page 1 | LS ECU: power front door request left | 46\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_powerFrontDoorRequestRight` | page 1 | LS ECU: power front door request right | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_falconDoorRequestLeft` | page 1 | LS ECU: falcon door request left | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_falconDoorRequestRight` | page 1 | LS ECU: falcon door request right | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HOLIDAY_PARTY_IDLE`<br>1 = `HOLIDAY_PARTY_OPEN`<br>2 = `HOLIDAY_PARTY_DANCE`<br>3 = `HOLIDAY_PARTY_CLOSE`<br>4 = `HOLIDAY_PARTY_STOP` | validated |
| `LS_chargePortRequest` | page 1 | LS ECU: charge port request; raw 3 = signal not available (SNA) | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `REQUEST_NONE`<br>1 = `REQUEST_OPEN`<br>2 = `REQUEST_CLOSE`<br>3 = `REQUEST_SNA` | validated |
| `LS_chargePortRaveRequest` | page 1 | LS ECU: charge port rave request | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `LS_suspensionRequest` | page 1 | LS ECU: suspension request; raw 3 = signal not available (SNA) | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SUSPENSION_REQUEST_NONE`<br>1 = `SUSPENSION_REQUEST_RAISE`<br>2 = `SUSPENSION_REQUEST_LOWER`<br>3 = `SUSPENSION_REQUEST_SNA` | validated |
| `LS_rgbIPFLRed` | page 2 | LS ECU: rgb IPFL red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbIPFLGreen` | page 2 | LS ECU: rgb IPFL green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbIPFLBlue` | page 2 | LS ECU: rgb IPFL blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbIPFRRed` | page 2 | LS ECU: rgb IPFR red | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbIPFRGreen` | page 2 | LS ECU: rgb IPFR green | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbIPFRBlue` | page 2 | LS ECU: rgb IPFR blue | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLForeRed` | page 3 | LS ECU: rgb door FL fore red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLForeGreen` | page 3 | LS ECU: rgb door FL fore green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLForeBlue` | page 3 | LS ECU: rgb door FL fore blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLAftRed` | page 3 | LS ECU: rgb door FL aft red | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLAftGreen` | page 3 | LS ECU: rgb door FL aft green | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFLAftBlue` | page 3 | LS ECU: rgb door FL aft blue | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRForeRed` | page 4 | LS ECU: rgb door FR fore red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRForeGreen` | page 4 | LS ECU: rgb door FR fore green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRForeBlue` | page 4 | LS ECU: rgb door FR fore blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRAftRed` | page 4 | LS ECU: rgb door FR aft red | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRAftGreen` | page 4 | LS ECU: rgb door FR aft green | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorFRAftBlue` | page 4 | LS ECU: rgb door FR aft blue | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLForeRed` | page 5 | LS ECU: rgb door RL fore red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLForeGreen` | page 5 | LS ECU: rgb door RL fore green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLForeBlue` | page 5 | LS ECU: rgb door RL fore blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLAftRed` | page 5 | LS ECU: rgb door RL aft red | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLAftGreen` | page 5 | LS ECU: rgb door RL aft green | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRLAftBlue` | page 5 | LS ECU: rgb door RL aft blue | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRForeRed` | page 6 | LS ECU: rgb door RR fore red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRForeGreen` | page 6 | LS ECU: rgb door RR fore green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRForeBlue` | page 6 | LS ECU: rgb door RR fore blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRAftRed` | page 6 | LS ECU: rgb door RR aft red | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRAftGreen` | page 6 | LS ECU: rgb door RR aft green | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rgbDoorRRAftBlue` | page 6 | LS ECU: rgb door RR aft blue | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix0` | page 7 | LS ECU: front matrix0 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix1` | page 7 | LS ECU: front matrix1 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix2` | page 7 | LS ECU: front matrix2 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix3` | page 7 | LS ECU: front matrix3 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix4` | page 7 | LS ECU: front matrix4 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix5` | page 7 | LS ECU: front matrix5 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix6` | page 7 | LS ECU: front matrix6 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix7` | page 8 | LS ECU: front matrix7 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix8` | page 8 | LS ECU: front matrix8 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix9` | page 8 | LS ECU: front matrix9 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix10` | page 8 | LS ECU: front matrix10 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix11` | page 8 | LS ECU: front matrix11 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix12` | page 8 | LS ECU: front matrix12 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix13` | page 8 | LS ECU: front matrix13 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix14` | page 9 | LS ECU: front matrix14 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix15` | page 9 | LS ECU: front matrix15 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix16` | page 9 | LS ECU: front matrix16 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix17` | page 9 | LS ECU: front matrix17 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix18` | page 9 | LS ECU: front matrix18 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix19` | page 9 | LS ECU: front matrix19 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix20` | page 9 | LS ECU: front matrix20 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix21` | page 10 | LS ECU: front matrix21 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix22` | page 10 | LS ECU: front matrix22 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix23` | page 10 | LS ECU: front matrix23 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix24` | page 10 | LS ECU: front matrix24 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix25` | page 10 | LS ECU: front matrix25 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix26` | page 10 | LS ECU: front matrix26 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix27` | page 10 | LS ECU: front matrix27 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix28` | page 11 | LS ECU: front matrix28 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix29` | page 11 | LS ECU: front matrix29 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix30` | page 11 | LS ECU: front matrix30 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix31` | page 11 | LS ECU: front matrix31 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix32` | page 11 | LS ECU: front matrix32 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix33` | page 11 | LS ECU: front matrix33 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix34` | page 11 | LS ECU: front matrix34 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix35` | page 12 | LS ECU: front matrix35 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix36` | page 12 | LS ECU: front matrix36 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix37` | page 12 | LS ECU: front matrix37 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix38` | page 12 | LS ECU: front matrix38 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix39` | page 12 | LS ECU: front matrix39 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix40` | page 12 | LS ECU: front matrix40 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix41` | page 12 | LS ECU: front matrix41 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix42` | page 13 | LS ECU: front matrix42 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix43` | page 13 | LS ECU: front matrix43 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix44` | page 13 | LS ECU: front matrix44 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix45` | page 13 | LS ECU: front matrix45 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix46` | page 13 | LS ECU: front matrix46 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix47` | page 13 | LS ECU: front matrix47 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix48` | page 13 | LS ECU: front matrix48 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix49` | page 14 | LS ECU: front matrix49 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix50` | page 14 | LS ECU: front matrix50 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix51` | page 14 | LS ECU: front matrix51 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix52` | page 14 | LS ECU: front matrix52 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix53` | page 14 | LS ECU: front matrix53 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix54` | page 14 | LS ECU: front matrix54 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix55` | page 14 | LS ECU: front matrix55 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix56` | page 15 | LS ECU: front matrix56 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix57` | page 15 | LS ECU: front matrix57 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix58` | page 15 | LS ECU: front matrix58 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_frontMatrix59` | page 15 | LS ECU: front matrix59 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix0` | page 15 | LS ECU: rear matrix0 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix1` | page 15 | LS ECU: rear matrix1 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix2` | page 15 | LS ECU: rear matrix2 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix3` | page 16 | LS ECU: rear matrix3 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix4` | page 16 | LS ECU: rear matrix4 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix5` | page 16 | LS ECU: rear matrix5 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix6` | page 16 | LS ECU: rear matrix6 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix7` | page 16 | LS ECU: rear matrix7 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix8` | page 16 | LS ECU: rear matrix8 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix9` | page 16 | LS ECU: rear matrix9 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix10` | page 17 | LS ECU: rear matrix10 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix11` | page 17 | LS ECU: rear matrix11 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix12` | page 17 | LS ECU: rear matrix12 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix13` | page 17 | LS ECU: rear matrix13 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix14` | page 17 | LS ECU: rear matrix14 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix15` | page 17 | LS ECU: rear matrix15 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix16` | page 17 | LS ECU: rear matrix16 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix17` | page 18 | LS ECU: rear matrix17 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix18` | page 18 | LS ECU: rear matrix18 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix19` | page 18 | LS ECU: rear matrix19 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix20` | page 18 | LS ECU: rear matrix20 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix21` | page 18 | LS ECU: rear matrix21 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix22` | page 18 | LS ECU: rear matrix22 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix23` | page 18 | LS ECU: rear matrix23 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix24` | page 19 | LS ECU: rear matrix24 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix25` | page 19 | LS ECU: rear matrix25 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix26` | page 19 | LS ECU: rear matrix26 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix27` | page 19 | LS ECU: rear matrix27 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix28` | page 19 | LS ECU: rear matrix28 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix29` | page 19 | LS ECU: rear matrix29 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix30` | page 19 | LS ECU: rear matrix30 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix31` | page 20 | LS ECU: rear matrix31 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix32` | page 20 | LS ECU: rear matrix32 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix33` | page 20 | LS ECU: rear matrix33 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix34` | page 20 | LS ECU: rear matrix34 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix35` | page 20 | LS ECU: rear matrix35 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix36` | page 20 | LS ECU: rear matrix36 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix37` | page 20 | LS ECU: rear matrix37 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix38` | page 21 | LS ECU: rear matrix38 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix39` | page 21 | LS ECU: rear matrix39 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix40` | page 21 | LS ECU: rear matrix40 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix41` | page 21 | LS ECU: rear matrix41 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix42` | page 21 | LS ECU: rear matrix42 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix43` | page 21 | LS ECU: rear matrix43 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix44` | page 21 | LS ECU: rear matrix44 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix45` | page 22 | LS ECU: rear matrix45 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix46` | page 22 | LS ECU: rear matrix46 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix47` | page 22 | LS ECU: rear matrix47 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix48` | page 22 | LS ECU: rear matrix48 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix49` | page 22 | LS ECU: rear matrix49 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix50` | page 22 | LS ECU: rear matrix50 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix51` | page 22 | LS ECU: rear matrix51 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix52` | page 23 | LS ECU: rear matrix52 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix53` | page 23 | LS ECU: rear matrix53 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix54` | page 23 | LS ECU: rear matrix54 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix55` | page 23 | LS ECU: rear matrix55 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix56` | page 23 | LS ECU: rear matrix56 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix57` | page 23 | LS ECU: rear matrix57 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix58` | page 23 | LS ECU: rear matrix58 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_rearMatrix59` | page 24 | LS ECU: rear matrix59 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar0` | page 24 | LS ECU: offroad light bar0 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar1` | page 24 | LS ECU: offroad light bar1 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar2` | page 24 | LS ECU: offroad light bar2 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar3` | page 24 | LS ECU: offroad light bar3 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar4` | page 24 | LS ECU: offroad light bar4 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `LS_offroadLightBar5` | page 24 | LS ECU: offroad light bar5 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Multiplexing

`LS_lightShowIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (44 signals), page 1 (18 signals), page 2 (6 signals), page 3 (6 signals), page 4 (6 signals), page 5 (6 signals), page 6 (6 signals), page 7 (7 signals), page 8 (7 signals), page 9 (7 signals), page 10 (7 signals), page 11 (7 signals), page 12 (7 signals), page 13 (7 signals), page 14 (7 signals), page 15 (7 signals), page 16 (7 signals), page 17 (7 signals), page 18 (7 signals), page 19 (7 signals), page 20 (7 signals), page 21 (7 signals), page 22 (7 signals), page 23 (7 signals), page 24 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All LS ECU messages (LS)](../../ls.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
