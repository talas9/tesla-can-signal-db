---
layout: default
title: "UI_driverAssistControl (0x3F8) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: driver assist control. Tesla Model 3 / Model Y CAN bus message UI_driverAssistControl (0x3F8) of Touchscreen user interface computer, firmware 2026.26.6.5, 45 signals (UI_autopilotControlRequest, UI_ulcStalkConfirm, UI_summonHeartbeat, UI_curvSpeedAdaptDisable and 41 more). Bit layout, scaling, units and value tables."
---

# UI_driverAssistControl (0x3F8) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Touchscreen user interface computer message: driver assist control; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 45 signals of UI_driverAssistControl as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_driverAssistControl` |
| CAN id | 0x3F8 (1016) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 45 |

## Signals of UI_driverAssistControl

Tesla Model 3 / Model Y CAN bus signals in `UI_driverAssistControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_autopilotControlRequest` | Touchscreen user interface computer: autopilot control request | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEGACY_LAT_CTRL`<br>1 = `NEXT_GEN_CTRL` | plausible |
| `UI_ulcStalkConfirm` | Drive on autopilot stalk confirmation mode (set by feature config). | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_summonHeartbeat` | Touchscreen user interface computer: summon heartbeat | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `UI_curvSpeedAdaptDisable` | Touchscreen user interface computer: curv speed adapt disable | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_dasDeveloper` | Touchscreen user interface computer: das developer | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_enableVinAssociation` | Touchscreen user interface computer: enable vin association | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_lssLkaEnabled` | User setting for lane keep assist | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LKA_OFF`<br>1 = `LKA_ON` | validated |
| `UI_lssLdwEnabled` | User setting for lane departure warning | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LDW_OFF`<br>1 = `LDW_ON` | validated |
| `UI_coastToCoast` | Touchscreen user interface computer: coast to coast | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_autoSummonEnable` | Touchscreen user interface computer: auto summon enable | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_exceptionListEnable` | Touchscreen user interface computer: exception list enable | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_roadCheckDisable` | Touchscreen user interface computer: road check disable | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_driveOnMapsEnable` | Drive on Autopilot enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOM_OFF`<br>1 = `DOM_ON` | validated |
| `UI_handsOnRequirementDisable` | Touchscreen user interface computer: hands on requirement disable | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_ulcOffHighway` | Touchscreen user interface computer: ulc off highway | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_fuseLanesDisable` | Touchscreen user interface computer: fuse lanes disable | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_fuseHPPDisable` | Touchscreen user interface computer: fuse HPP disable | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_fuseVehiclesDisable` | Touchscreen user interface computer: fuse vehicles disable | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ON`<br>1 = `OFF` | plausible |
| `UI_enableClipParkedTelemetry` | Touchscreen user interface computer: enable clip parked telemetry | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_visionSpeedType` | Touchscreen user interface computer: vision speed type | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `ONE_SECOND`<br>2 = `TWO_SECOND`<br>3 = `OPTIMIZED` | plausible |
| `UI_curvatureDatabaseOnly` | Touchscreen user interface computer: curvature database only | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_lssElkEnabled` | User setting for emergency lane keep | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ELK_OFF`<br>1 = `ELK_ON` | validated |
| `UI_summonExitType` | Touchscreen user interface computer: summon exit type; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `STRAIGHT`<br>1 = `TURN_RIGHT`<br>2 = `TURN_LEFT`<br>3 = `SNA` | plausible |
| `UI_summonEntryType` | Touchscreen user interface computer: summon entry type; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `STRAIGHT`<br>1 = `TURN_RIGHT`<br>2 = `TURN_LEFT`<br>3 = `SNA` | plausible |
| `UI_selfParkRequest` | Self park request; raw 15 = signal not available (SNA) | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `NONE`<br>1 = `SELF_PARK_FORWARD`<br>2 = `SELF_PARK_REVERSE`<br>3 = `ABORT`<br>4 = `PRIME`<br>5 = `PAUSE`<br>6 = `RESUME`<br>7 = `AUTO_SUMMON_FORWARD`<br>8 = `AUTO_SUMMON_REVERSE`<br>9 = `AUTO_SUMMON_CANCEL`<br>10 = `AUTO_SUMMON_PRIMED`<br>11 = `SMART_SUMMON`<br>12 = `SMART_SUMMON_NO_OP`<br>15 = `SNA` | validated |
| `UI_summonReverseDist` | Touchscreen user interface computer: summon reverse dist; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 62 | 63 = `SNA` | plausible |
| `UI_undertakeAssistEnable` | Touchscreen user interface computer: undertake assist enable | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_adaptiveSetSpeedEnable` | Touchscreen user interface computer: adaptive set speed enable | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_drivingSide` | Touchscreen user interface computer: driving side | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LEFT`<br>1 = `RIGHT`<br>2 = `UNKNOWN` | plausible |
| `UI_enableClipTelemetry` | Touchscreen user interface computer: enable clip telemetry | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_enableTripTelemetry` | Touchscreen user interface computer: enable trip telemetry | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_enableRoadSegmentTelemetry` | Touchscreen user interface computer: enable road segment telemetry | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_accFollowDistanceSetting` | Touchscreen user interface computer: acc follow distance setting; raw 7 = signal not available (SNA) | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `1`<br>1 = `2`<br>2 = `3`<br>3 = `4`<br>4 = `5`<br>5 = `6`<br>6 = `7`<br>7 = `SNA` | plausible |
| `UI_hasDriveOnNav` | Touchscreen user interface computer: has drive on nav | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_followNavRouteEnable` | Following route with Drive on Autopilot | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NAV_ROUTE_OFF`<br>1 = `NAV_ROUTE_ON` | validated |
| `UI_ulcSpeedConfig` | Drive on autopilot speed base lane changes mode. | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SPEED_BASED_ULC_DISABLED`<br>1 = `SPEED_BASED_ULC_MILD`<br>2 = `SPEED_BASED_ULC_AVERAGE`<br>3 = `SPEED_BASED_ULC_MAD_MAX` | validated |
| `UI_ulcBlindSpotConfig` | Touchscreen user interface computer: ulc blind spot config | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `AGGRESSIVE`<br>2 = `MAD_MAX` | plausible |
| `UI_suppressExitPassingLane` | Navigate on Autopilot will not suggest lane changes out of the passing lane | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_enableClipStartStopTelemetry` | Touchscreen user interface computer: enable clip start stop telemetry | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_alcOffHighwayEnable` | Touchscreen user interface computer: alc off highway enable | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_validationLoop` | Touchscreen user interface computer: validation loop | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_smartSummonType` | Type of smart summon session (Find Me, Pin Drop, Smart Autopark) | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PIN_DROP`<br>1 = `FIND_ME`<br>2 = `SMART_AUTOPARK` | validated |
| `UI_enableVisionOnlyStops` | Touchscreen user interface computer: enable vision only stops | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_source3D` | Touchscreen user interface computer: source3 d | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Z_FROM_MAP`<br>1 = `Z_FROM_PATH_PREDICTION`<br>2 = `XYZ_PREDICTION` | plausible |
| `UI_isaSpeedingChimeMuted` | Reports the user input of Intelligent Speed Assist (ISA) speed chime alert option. | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
