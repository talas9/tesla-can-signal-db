---
layout: default
title: "UI_vehicleControl2 (0x3B3) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: vehicle control2. Ethernet-side message UI_vehicleControl2 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 41 signals (UI_gloveboxRequest, UI_trunkRequest, UI_UMCUpdateInhibit, UI_WCUpdateInhibit and 37 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleControl2 (0x3B3) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: vehicle control2. This page documents the 41 signals of UI_vehicleControl2 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleControl2` |
| Ethernet-side id | 0x3B3 (947) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 41 |

## Signals of UI_vehicleControl2

Tesla Model Y CAN bus signals in `UI_vehicleControl2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_gloveboxRequest` | UI request to open the glovebox | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_trunkRequest` | Rear trunk request | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_UMCUpdateInhibit` | Touchscreen user interface computer: UMC update inhibit | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_WCUpdateInhibit` | Touchscreen user interface computer: WC update inhibit | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_soundHornOnLock` | Touchscreen user interface computer: sound horn on lock | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_locksPanelActive` | Touchscreen user interface computer: locks panel active | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_PINToDriveEnabled` | UI customer level request to pin to drive enabled. | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_PINToDrivePassed` | UI customer level request to enable drive with pin passed. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_disableMirrorAutoDim` | Request to disable side and rear-view mirror auto dim | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_lightSwitch` | Headlight mode; raw 4 = signal not available (SNA) | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LIGHT_SWITCH_AUTO`<br>1 = `LIGHT_SWITCH_ON`<br>2 = `LIGHT_SWITCH_PARKING`<br>3 = `LIGHT_SWITCH_OFF`<br>4 = `LIGHT_SWITCH_SNA` | validated |
| `UI_readyToAddKey` | Ready to add key | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_alarmTriggerRequest` | Alarm activation request from UI | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_VCSECFeature1` | Touchscreen user interface computer: VCSEC feature1 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_VCLEFTFeature1` | Touchscreen user interface computer: VCLEFT feature1 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_summonState` | Touchscreen user interface computer: summon state; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `IDLE`<br>2 = `PRE_PRIMED`<br>3 = `ACTIVE` | plausible |
| `UI_displayOnForUser` | User is present | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_freeRollModeRequest` | Touchscreen user interface computer: free roll mode request | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_BLEPushNotificationRequest` | Reports that the User Interface (UI) wants to talk to a phone and Vehicle Controller Security (VCSEC) should let all connected phones know. | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_pairKeyQRCodeDisplaying` | Touchscreen user interface computer: pair key QR code displaying | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_keepAutopilotAwake` | Reports the request for Vehicle Controller (VC) to keep autopilot awake. | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_batteryPreconditioningRequest` | Requests battery preconditioning. | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_coastDownMode` | Touchscreen user interface computer: coast down mode | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autopilotPowerStateRequest` | Requests different power states from autopilot ECU depending on feature usage. | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTOPILOT_NOMINAL`<br>1 = `AUTOPILOT_SENTRY`<br>2 = `AUTOPILOT_SUSPEND` | validated |
| `UI_shorted12VCellTestMode` | Touchscreen user interface computer: shorted12 v cell test mode | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `SHADOW`<br>2 = `ACTIVE` | plausible |
| `UI_autoRollWindowsOnLockEnable` | UI customer level request to enable auto-roll windows on lock | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_virtualPitchSensorOverrideOKForAim` | Touchscreen user interface computer: virtual pitch sensor override OK for aim | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_conditionalLoggingEnabledVCSEC` | Touchscreen user interface computer: conditional logging enabled VCSEC | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_WC3UpdateInhibit` | Touchscreen user interface computer: WC3 update inhibit | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_steeringWheelHeatReq` | Request to enable steering wheel heater | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_disableHorn` | Request to disable horn | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_frontLeftSeatFanReq` | Request for front left seat ventilation | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | validated |
| `UI_frontRightSeatAutoClimateReq` | UI setting to enable auto seat heating and cooling for front right seat | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_frontRightSeatFanReq` | Request for front left seat ventilation | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAN_REQUEST_OFF`<br>1 = `FAN_REQUEST_LEVEL1`<br>2 = `FAN_REQUEST_LEVEL2`<br>3 = `FAN_REQUEST_LEVEL3` | validated |
| `UI_sleepFeature1` | Touchscreen user interface computer: sleep feature1 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_dcr12VThreshold` | Touchscreen user interface computer: dcr12 v threshold | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `40_MILLIOHMS`<br>2 = `35_MILLIOHMS`<br>3 = `30_MILLIOHMS`<br>4 = `27_MILLIOHMS`<br>5 = `24_MILLIOHMS`<br>6 = `22_MILLIOHMS`<br>7 = `20_MILLIOHMS`<br>8 = `19_MILLIOHMS`<br>9 = `18_MILLIOHMS`<br>10 = `17_MILLIOHMS`<br>11 = `16_MILLIOHMS`<br>12 = `15_MILLIOHMS` | plausible |
| `UI_frontLeftSeatAutoClimateReq` | UI setting to enable auto seat heating and cooling for front left seat | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_wiperHeaterReq` | UI request to enable the wiper heater | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_tireSeason` | Touchscreen user interface computer: tire season | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NON_WINTER`<br>1 = `WINTER` | plausible |
| `UI_saveTireConfigReq` | Touchscreen user interface computer: save tire config req | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |
| `UI_silentAlarm` | Signal indicating alarms should be silenced | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_sleepFeature2` | Touchscreen user interface computer: sleep feature2 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
