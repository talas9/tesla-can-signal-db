---
layout: default
title: "UI_vehicleControl3 (0x274) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: vehicle control3. Ethernet-side message UI_vehicleControl3 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 41 signals (UI_lightFlashRequest, UI_keylessDrivingEnabled, UI_phoneCallActive, UI_drivingSideVEH and 37 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleControl3 (0x274) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: vehicle control3. This page documents the 41 signals of UI_vehicleControl3 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleControl3` |
| Ethernet-side id | 0x274 (628) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 41 |

## Signals of UI_vehicleControl3

Tesla Model Y CAN bus signals in `UI_vehicleControl3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_lightFlashRequest` | UI flash lights request | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LIGHT_FLASH_INACTIVE`<br>1 = `LIGHT_FLASH_HOMELINK`<br>2 = `LIGHT_FLASH_MOBILE_APP`<br>3 = `LIGHT_FLASH_SENTRY` | plausible |
| `UI_keylessDrivingEnabled` | Touchscreen user interface computer: keyless driving enabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_phoneCallActive` | On phone call via Bluetooth if active | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_drivingSideVEH` | Touchscreen user interface computer: driving side VEH | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEFT`<br>1 = `RIGHT`<br>2 = `UNKNOWN` | plausible |
| `UI_keyPairResponse` | Touchscreen user interface computer: key pair response | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `CONFIRMED`<br>2 = `DENIED` | plausible |
| `UI_lightShowClosuresEnabled` | Closure movements enabled during light show | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_steeringWheelHeatAutoReq` | UI setting to request auto steering wheel heat | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_steeringWheelHeatLevelReq` | Request for steering wheel heat | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STEERING_WHEEL_HEAT_OFF`<br>1 = `STEERING_WHEEL_HEAT_LEVEL1`<br>2 = `STEERING_WHEEL_HEAT_LEVEL2`<br>3 = `STEERING_WHEEL_HEAT_LEVEL3` | plausible |
| `UI_headlightPulseRequest` | Request headlights to pulse | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_VCSECFeature2` | Touchscreen user interface computer: VCSEC feature2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_VCSECFeature3` | Touchscreen user interface computer: VCSEC feature3 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_VCSECFeature4` | Touchscreen user interface computer: VCSEC feature4 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_VCSECFeature5` | Touchscreen user interface computer: VCSEC feature5 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_shortHornRequest` | Touchscreen user interface computer: short horn request | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_packTempLoggingRequest` | Touchscreen user interface computer: pack temp logging request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |
| `UI_UMC3UpdateInhibit` | Touchscreen user interface computer: UMC3 update inhibit | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_handsFreeTrunk` | Touchscreen user interface computer: hands free trunk | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_displayRedShiftActive` | UI's reduce blue light setting is active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_handsFreeFrunk` | Touchscreen user interface computer: hands free frunk | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fasciaCameraWashRequest` | User request to activate fascia camera wash | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autoClosuresExcludeHome` | Touchscreen user interface computer: auto closures exclude home | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_leftRearSeatAdjustmentRequest` | Reports request from UI to actuate the left rear seat | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_COMFORT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_FAST`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_COMFORT`<br>4 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_FAST`<br>5 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_TOGGLE_FOLD`<br>6 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_STOP` | plausible |
| `UI_rightRearSeatAdjustmentRequest` | Reports request from UI to actuate the right rear seat | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_COMFORT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_FORWARD_FAST`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_COMFORT`<br>4 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_REARWARD_FAST`<br>5 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_TOGGLE_FOLD`<br>6 = `UI_ADJUSTABLE_FOLD_FLAT_REQUEST_STOP` | plausible |
| `UI_blindSpotIndicatorLightRequest` | Request for blind spot indicator light | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_etcBluetoothControl` | Touchscreen user interface computer: etc bluetooth control | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INACTIVE`<br>1 = `OFF`<br>2 = `ON`<br>3 = `RESERVED` | plausible |
| `UI_keepOnAccessoryPortsReq` | User setting to keep 12V outlets, USB ports, and phone chargers powered in CONDITIONING | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fasciaCameraShown` | Whether the UI is currently showing the fascia camera view | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rearSeatChildLock` | Reports the state of second row seat fold flat child lock from the UI | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_NONE`<br>1 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_LEFT`<br>2 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_RIGHT`<br>3 = `UI_ADJUSTABLE_FOLD_FLAT_CHILD_LOCK_BOTH` | plausible |
| `UI_windowPercentageRequest` | Reports the window percentage value when window request is WINDOW_REQUEST_GOTO_PERCENT. | 42\|6 | little-endian | signed | 5 | 0 | % | -100 to 100 |  | plausible |
| `UI_windowRequestedFL` | Reports that the front left window is requested. | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_windowRequestedFR` | Reports that the front right window is requested. | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_windowRequestedRL` | Reports that the rear left window is requested. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_windowRequestedRR` | Reports that the rear right window is requested. | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_windowRequest` | Window operation request from the mobile app. | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WINDOW_REQUEST_IDLE`<br>1 = `WINDOW_REQUEST_GOTO_PERCENT`<br>2 = `WINDOW_REQUEST_GOTO_VENT`<br>3 = `WINDOW_REQUEST_GOTO_CLOSED`<br>4 = `WINDOW_REQUEST_GOTO_OPEN`<br>5 = `WINDOW_REQUEST_GOTO_CLOSED_CARWASH`<br>6 = `WINDOW_REQUEST_GOTO_RELATIVE_PERCENT` | plausible |
| `UI_closeTrunkRequest` | Explicity request for the rear trunk to close | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_childPresenceDetectionDisableRequest` | User request to disable child presence detection behaviors until the next drive cycle | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_derivedLoadshedFeature` | Reports whether vehicle controllers should enable derived loadshed feature. | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rearSeatFoldConfirmed` | Touchscreen user interface computer: rear seat fold confirmed | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_leftRearSeatRequestFromRearDisplay` | Touchscreen user interface computer: left rear seat request from rear display | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_selfParkStandingBy` | Reports that summon is in standby. | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_rightRearSeatRequestFromRearDisplay` | Touchscreen user interface computer: right rear seat request from rear display | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
