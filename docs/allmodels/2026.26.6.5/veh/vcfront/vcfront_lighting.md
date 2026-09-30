---
layout: default
title: "VCFRONT_lighting (0x3F5) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: lighting. Tesla Model 3 / Model Y CAN bus message VCFRONT_lighting (0x3F5) of Front body controller, firmware 2026.26.6.5, 20 signals (VCFRONT_indicatorLeftRequest, VCFRONT_indicatorRightRequest, VCFRONT_hazardLightRequest, VCFRONT_ambientLightingBrightnes and 16 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_lighting (0x3F5) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front body controller message: lighting; frame length observed on a vehicle bus. This page documents the 20 signals of VCFRONT_lighting as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_lighting` |
| CAN id | 0x3F5 (1013) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 20 |

## Signals of VCFRONT_lighting

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_lighting`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_indicatorLeftRequest` | Front body controller: indicator left request | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURN_SIGNAL_OFF`<br>1 = `TURN_SIGNAL_ACTIVE_LOW`<br>2 = `TURN_SIGNAL_ACTIVE_HIGH` | validated |
| `VCFRONT_indicatorRightRequest` | Front body controller: indicator right request | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURN_SIGNAL_OFF`<br>1 = `TURN_SIGNAL_ACTIVE_LOW`<br>2 = `TURN_SIGNAL_ACTIVE_HIGH` | validated |
| `VCFRONT_hazardLightRequest` | Front body controller: hazard light request | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HAZARD_REQUEST_NONE`<br>1 = `HAZARD_REQUEST_BUTTON`<br>2 = `HAZARD_REQUEST_LOCK`<br>3 = `HAZARD_REQUEST_UNLOCK`<br>4 = `HAZARD_REQUEST_MISLOCK`<br>5 = `HAZARD_REQUEST_CRASH`<br>6 = `HAZARD_REQUEST_CAR_ALARM`<br>7 = `HAZARD_REQUEST_DAS`<br>8 = `HAZARD_REQUEST_UDS` | validated |
| `VCFRONT_ambientLightingBrightnes` | Front body controller: ambient lighting brightnes; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127 | 255 = `SNA` | validated |
| `VCFRONT_switchLightingBrightness` | Front body controller: switch lighting brightness; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127 | 255 = `SNA` | validated |
| `VCFRONT_courtesyLightingRequest` | Flag to request courtesy lighting | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hazardSwitchBacklight` | Front body controller: hazard switch backlight | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_highBeamControlState` | State of the virtual high beam stalk | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HIGH_BEAM_CONTROL_IDLE`<br>1 = `HIGH_BEAM_CONTROL_INTERMITTENT`<br>2 = `HIGH_BEAM_CONTROL_LATCHED`<br>3 = `HIGH_BEAM_CONTROL_DAS_AUTO` | validated |
| `VCFRONT_dynamicBrakeLightState` | Front body controller: dynamic brake light state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DYNAMIC_BRAKE_LIGHT_OFF`<br>1 = `DYNAMIC_BRAKE_LIGHT_ACTIVE_LOW`<br>2 = `DYNAMIC_BRAKE_LIGHT_ACTIVE_HIGH` | validated |
| `VCFRONT_lightingCoreState` | Core lighting state; raw 15 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `LIGHT_CORE_STATE_OFF`<br>1 = `LIGHT_CORE_STATE_POS_PARK`<br>2 = `LIGHT_CORE_STATE_DRL`<br>3 = `LIGHT_CORE_STATE_DRL_PLUS_REAR_POS_PARK`<br>4 = `LIGHT_CORE_STATE_LOW_BEAMS`<br>5 = `LIGHT_CORE_STATE_CUSTOM`<br>15 = `LIGHT_CORE_STATE_SNA` | validated |
| `VCFRONT_intHighBeamsFunctionState` | State of the intermittent high beams lighting function | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_latchedHighBeamsFunctionState` | State of the latched high beams lighting function | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_frontFogFunctionState` | State of the front fog lighting function | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_headlightsReadyOrTimedOut` | Front body controller: headlights ready or timed out | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_turnIndicatorStalk` | Front body controller: turn indicator stalk; raw 3 = signal not available (SNA) | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SIMULATED_LATCHING_STALK_IDLE`<br>1 = `SIMULATED_LATCHING_STALK_LEFT`<br>2 = `SIMULATED_LATCHING_STALK_RIGHT`<br>3 = `SIMULATED_LATCHING_STALK_SNA` | validated |
| `VCFRONT_highBeamLatchingState` | State of high beam latching; raw 0 = signal not available (SNA) | 42\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `LATCHING_STATE_SNA`<br>1 = `LATCHING_STATE_UNLATCHED`<br>2 = `LATCHING_STATE_LATCHING`<br>3 = `LATCHING_STATE_LATCHED` | validated |
| `VCFRONT_lightingCustomState` | Custom lighting mode substate | 44\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CUSTOM_LIGHTING_STATE_NONE`<br>1 = `CUSTOM_LIGHTING_STATE_SENTRY_AWARE_RAMP_UP`<br>2 = `CUSTOM_LIGHTING_STATE_SENTRY_AWARE_RAMP_DOWN`<br>3 = `CUSTOM_LIGHTING_STATE_SENTRY_AWARE_OFF`<br>4 = `CUSTOM_LIGHTING_STATE_HAZARD_WARNING_WAIT_FOR_HEADLAMP_POWER`<br>5 = `CUSTOM_LIGHTING_STATE_HAZARD_WARNING_LIGHTS_ON`<br>6 = `CUSTOM_LIGHTING_STATE_HAZARD_WARNING_LIGHTS_OFF`<br>7 = `CUSTOM_LIGHTING_STATE_SELFTEST`<br>8 = `CUSTOM_LIGHTING_STATE_WELCOME_GOODBYE_LOCK`<br>9 = `CUSTOM_LIGHTING_STATE_WELCOME_GOODBYE_UNLOCK`<br>10 = `CUSTOM_LIGHTING_STATE_WELCOME_GOODBYE_DAY`<br>11 = `CUSTOM_LIGHTING_STATE_WELCOME_GOODBYE_NIGHT`<br>12 = `CUSTOM_LIGHTING_STATE_WELCOME_GOODBYE_SYHL`<br>13 = `CUSTOM_LIGHTING_STATE_ROBOTAXI_WELCOME_RAMP_UP`<br>14 = `CUSTOM_LIGHTING_STATE_ROBOTAXI_WELCOME_RAMP_DOWN`<br>31 = `CUSTOM_LIGHTING_STATE_RESERVED` | validated |
| `VC_fastFlashHazardsActive` | Front body controller: fast flash hazards active | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_indicatorLeftInternal` | Front body controller: indicator left internal | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURN_SIGNAL_OFF`<br>1 = `TURN_SIGNAL_ACTIVE_LOW`<br>2 = `TURN_SIGNAL_ACTIVE_HIGH` | validated |
| `VCFRONT_indicatorRightInternal` | Front body controller: indicator right internal | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURN_SIGNAL_OFF`<br>1 = `TURN_SIGNAL_ACTIVE_LOW`<br>2 = `TURN_SIGNAL_ACTIVE_HIGH` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
