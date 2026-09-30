---
layout: default
title: "UI_autopilotControl (0x3FD) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: autopilot control. Tesla Model 3 CAN bus message UI_autopilotControl (0x3FD) of Touchscreen user interface computer, firmware 2026.26.6.5, 82 signals (UI_autopilotControlIndex, UI_hovEnabled, UI_donDisableAutoWiperDuration, UI_donDisableOnAutoWiperSpeed and 78 more). Bit layout, scaling, units and value tables."
---

# UI_autopilotControl (0x3FD) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN

Touchscreen user interface computer message: autopilot control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 82 signals of UI_autopilotControl as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_autopilotControl` |
| CAN id | 0x3FD (1021) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 82 |

## Signals of UI_autopilotControl

Tesla Model 3 CAN bus signals in `UI_autopilotControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_autopilotControlIndex` | selector | Touchscreen user interface computer: autopilot control index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7` | plausible |
| `UI_hovEnabled` | page 0 | UI HOV routes enabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HOV_OFF`<br>1 = `HOV_ON` | validated |
| `UI_donDisableAutoWiperDuration` | page 0 | Touchscreen user interface computer: don disable auto wiper duration | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DEFAULT`<br>1 = `5_S`<br>2 = `15_S`<br>3 = `30_S`<br>4 = `60_S`<br>5 = `120_S`<br>6 = `OFF` | plausible |
| `UI_donDisableOnAutoWiperSpeed` | page 0 | Touchscreen user interface computer: don disable on auto wiper speed | 7\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OFF`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7`<br>8 = `8`<br>9 = `9`<br>10 = `10`<br>11 = `11`<br>12 = `12`<br>13 = `13`<br>14 = `14`<br>15 = `INVALID` | plausible |
| `UI_blindspotMinSpeed` | page 0 | Touchscreen user interface computer: blindspot min speed | 11\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DEFAULT`<br>1 = `5_KPH`<br>2 = `10_KPH`<br>3 = `15_KPH`<br>4 = `20_KPH`<br>5 = `25_KPH`<br>6 = `30_KPH`<br>7 = `35_KPH`<br>8 = `40_KPH`<br>9 = `45_KPH`<br>10 = `OFF` | plausible |
| `UI_blindspotDistance` | page 0 | Touchscreen user interface computer: blindspot distance | 15\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DEFAULT`<br>1 = `0P5_M`<br>2 = `1_M`<br>3 = `2_M`<br>4 = `4_M`<br>5 = `OFF` | plausible |
| `UI_blindspotTTC` | page 0 | Touchscreen user interface computer: blindspot TTC | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DEFAULT`<br>1 = `0P5_S`<br>2 = `1_S`<br>3 = `2_S`<br>4 = `4_S`<br>5 = `3_S`<br>6 = `5_S`<br>7 = `OFF` | plausible |
| `UI_donStopEndOfRampBuffer` | page 0 | Touchscreen user interface computer: don stop end of ramp buffer | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DEFAULT`<br>1 = `15_M`<br>2 = `30_M`<br>3 = `45_M`<br>4 = `OFF` | plausible |
| `UI_donDisableCutin` | page 0 | Touchscreen user interface computer: don disable cutin | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_smartSetSpeedOffset` | page 0 | TACC will apply this offset over the speed limit | 25\|6 | little-endian | unsigned | 1 | -30 | % | -30 to 33 |  | validated |
| `UI_smartSetSpeedOffsetType` | page 0 | Offset applied will be a percentage or fixed value based on this setting | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FIXED_OFFSET`<br>1 = `PERCENTAGE_OFFSET` | validated |
| `UI_autopilotMonarchBackup` | page 0 | Touchscreen user interface computer: autopilot monarch backup | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fsdVisualizationEnabled` | page 0 | Touchscreen user interface computer: fsd visualization enabled | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fsdStopsControlEnabled` | page 0 | Indicates if autopilot control for traffic lights and stops signs has been enabled by the driver | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_fsdContinueOnGreenWithCIPV` | page 0 | Touchscreen user interface computer: fsd continue on green with CIPV | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_smartSetSpeed` | page 0 | TACC will use speed limit + offset as user set speed when enabled | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_automaticSetSpeedOffset` | page 0 | Maximum set speed offset would be determined automatically when this option is enabled | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_apply2021_1958_ISA` | page 0 | Touchscreen user interface computer: apply2021 1958 ISA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_apply2021_646_ELKS` | page 0 | Touchscreen user interface computer: apply2021 646 ELKS | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_apply2021_1341_DDAW` | page 0 | Touchscreen user interface computer: apply2021 1341 DDAW | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_homelinkNearby` | page 0 | Touchscreen user interface computer: homelink nearby | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_NEARBY`<br>1 = `NEARBY` | plausible |
| `UI_enableFullSelfDriving` | page 0 | Indicates if the driver has enabled FSD behaviors | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_hasFullSelfDriving` | page 0 | Indicates if the vehicle hardware, software, and dependencies allow FSD | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_autosteerActivation` | page 0 | User-selected autosteer activation method | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SINGLE_CLICK`<br>1 = `DOUBLE_CLICK` | validated |
| `UI_fsdBetaRequest` | page 0 | User accepted disclaimer and requested FSD (Supervised) builds | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FSD_REQUEST_NOT_ACTIVE`<br>1 = `FSD_REQUEST_ACTIVE` | validated |
| `UI_fullSelfDrivingSuspended` | page 0 | Full self driving is suspended | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_disableOptionalLaneChanges` | page 0 | Disable optional lane changes while FSD is controlling | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_applyR152_AEBS` | page 0 | Touchscreen user interface computer: apply R152 AEBS | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_applyDCASBehavior` | page 0 | Touchscreen user interface computer: apply DCAS behavior | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_applyDCASBehaviorLegacy` | page 0 | Touchscreen user interface computer: apply DCAS behavior legacy | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_applyADDWWarnings` | page 0 | ADDW warnings are enabled on this vehicle | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_autopilotControlMux0Valid` | page 0 | Touchscreen user interface computer: autopilot control mux0 valid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_selectableCameraRequest` | page 1 | Infotainment selectable camera state request from AP signal; raw 15 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `NONE`<br>1 = `SELFIE`<br>2 = `FRONT_MAIN`<br>3 = `FRONT_FISHEYE`<br>4 = `FRONT_NARROW`<br>5 = `LEFT_PILLAR`<br>6 = `LEFT_REPEATER`<br>7 = `RIGHT_PILLAR`<br>8 = `RIGHT_REPEATER`<br>9 = `BACKUP`<br>10 = `OCTA`<br>11 = `GRID_VIEW`<br>12 = `FASCIA`<br>13 = `REPEATERS_BACKUP`<br>15 = `SNA` | validated |
| `UI_overrideSleepWithSuspend` | page 1 | Touchscreen user interface computer: override sleep with suspend | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `UI_driverMonitorConfirmation` | page 1 | Driver attentiveness confirmation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_parkAssistUseVision` | page 1 | Reports if the vehicle should use vision park assist. | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_applyEceR79` | page 1 | Touchscreen user interface computer: apply ece R79 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableMapStops` | page 1 | Touchscreen user interface computer: enable map stops | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableMain` | page 1 | Touchscreen user interface computer: disable main | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableNarrow` | page 1 | Touchscreen user interface computer: disable narrow | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableFisheye` | page 1 | Touchscreen user interface computer: disable fisheye | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableLeftPillar` | page 1 | Touchscreen user interface computer: disable left pillar | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableRightPillar` | page 1 | Touchscreen user interface computer: disable right pillar | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableLeftRepeater` | page 1 | Touchscreen user interface computer: disable left repeater | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableRightRepeater` | page 1 | Touchscreen user interface computer: disable right repeater | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableBackup` | page 1 | Touchscreen user interface computer: disable backup | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableRadar` | page 1 | Touchscreen user interface computer: disable radar | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_noStalkConfirmAlertHaptic` | page 1 | Detects if alert haptic feedback should trigger. | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_regulatoryLKA` | page 1 | Touchscreen user interface computer: regulatory LKA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_regulatoryLaneAssistLevel` | page 1 | Touchscreen user interface computer: regulatory lane assist level | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `WARNING`<br>1 = `ASSIST` | plausible |
| `UI_ulcSnooze` | page 1 | Touchscreen user interface computer: ulc snooze | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_noStalkConfirmAlertChime` | page 1 | Detects if alert chime should trigger. | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_factorySummonEnable` | page 1 | Controls Factory Summon. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_apmv3Branch` | page 1 | Touchscreen user interface computer: apmv3 branch | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LIVE`<br>1 = `STAGE`<br>2 = `DEV`<br>3 = `STAGE2`<br>4 = `EAP`<br>5 = `DEMO` | plausible |
| `UI_enableCabinCamera` | page 1 | Indicates if autopilot can enable cabin camera | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_enableAutopilotStopWarning` | page 1 | Enables the Autopilot active red light warning function. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_showLaneGraph` | page 1 | Touchscreen user interface computer: show lane graph | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_showTrackLabels` | page 1 | Touchscreen user interface computer: show track labels | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hardCoreSummon` | page 1 | Touchscreen user interface computer: hard core summon | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCabinCameraTelemetry` | page 1 | Touchscreen user interface computer: enable cabin camera telemetry | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableVisionSpeedControl` | page 1 | Indicates if autopilot can enable vision speed control | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_autopilotTelemetryInChina` | page 1 | Touchscreen user interface computer: autopilot telemetry in china | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableTeslaAutopark` | page 1 | Indicates if autopilot can enable Telsa Autopark control | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_autoTurnSignalMode` | page 1 | Turn signal activation mode | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UI_AUTO_TURN_SIGNAL_MODE_OFF`<br>1 = `UI_AUTO_TURN_SIGNAL_MODE_AUTO_CANCEL` | validated |
| `UI_enableCautionLightControl` | page 1 | Touchscreen user interface computer: enable caution light control | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_applyEceR79SmartSummonOnly` | page 1 | Touchscreen user interface computer: apply ece R79 smart summon only | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autopilotMonarchEnabled` | page 1 | Touchscreen user interface computer: autopilot monarch enabled | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autopilotEphemerisEnabled` | page 1 | Touchscreen user interface computer: autopilot ephemeris enabled | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCabinAudioRecording` | page 1 | Indicates if autopilot can record cabin audio | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_autopilotControlMux1Valid` | page 1 | Touchscreen user interface computer: autopilot control mux1 valid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableApproachingEmergencyVehicleDetection` | page 2 | Touchscreen user interface computer: enable approaching emergency vehicle detection | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableStartFsdFromParkBrakeConfirmation` | page 2 | Touchscreen user interface computer: enable start fsd from park brake confirmation | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableStartFsdFromPark` | page 2 | Touchscreen user interface computer: enable start fsd from park | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fsdMaxSpeedOffsetPercentage` | page 2 | Touchscreen user interface computer: fsd max speed offset percentage | 8\|6 | little-endian | unsigned | 1 | 0 | % | 0 to 63 |  | plausible |
| `UI_calibrationReadyInFactory` | page 2 | Touchscreen user interface computer: calibration ready in factory | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_coldStartMonarchInFactory` | page 2 | Touchscreen user interface computer: cold start monarch in factory | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_navMinutesToArrival` | page 2 | Touchscreen user interface computer: nav minutes to arrival | 17\|10 | little-endian | unsigned | 1 | 0 | minutes | 0 to 1023 |  | plausible |
| `UI_fsdQuizRequired` | page 2 | Touchscreen user interface computer: fsd quiz required | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fsdQuizPassed` | page 2 | Touchscreen user interface computer: fsd quiz passed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_fsdAllowedInLocalizedRegion` | page 2 | Touchscreen user interface computer: fsd allowed in localized region | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autopilotDrivingProfile` | page 2 | Driving profile for autopilot control | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CHILL`<br>1 = `NORMAL`<br>2 = `ASSERTIVE`<br>3 = `MAD_MAX`<br>4 = `CONSERVATIVE` | validated |
| `UI_autopilotControlMux2Valid` | page 2 | Touchscreen user interface computer: autopilot control mux2 valid | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`UI_autopilotControlIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (31 signals), page 1 (38 signals), page 2 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
