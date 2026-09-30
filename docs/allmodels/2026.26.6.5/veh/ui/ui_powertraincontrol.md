---
layout: default
title: "UI_powertrainControl (0x334) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: powertrain control. Tesla Model 3 / Model Y CAN bus message UI_powertrainControl (0x334) of Touchscreen user interface computer, firmware 2026.26.6.5, 16 signals (UI_systemPowerLimit, UI_pedalMap, UI_enableRegenBackfill, UI_systemTorqueLimit and 12 more). Bit layout, scaling, units and value tables."
---

# UI_powertrainControl (0x334) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: powertrain control; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 16 signals of UI_powertrainControl as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_powertrainControl` |
| CAN id | 0x334 (820) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 16 |

## Signals of UI_powertrainControl

Tesla Model 3 / Model Y CAN bus signals in `UI_powertrainControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_systemPowerLimit` | Touchscreen user interface computer: system power limit; raw 31 = signal not available (SNA) | 0\|5 | little-endian | unsigned | 20 | 20 | kW | 20 to 620 | 31 = `SNA` | plausible |
| `UI_pedalMap` | Switch between various platform specific pedal maps | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHILL`<br>1 = `SPORT`<br>2 = `PERFORMANCE` | validated |
| `UI_enableRegenBackfill` | Indicates if regenerative braking backfill has been enabled by the driver | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_systemTorqueLimit` | Touchscreen user interface computer: system torque limit; raw 63 = signal not available (SNA) | 8\|6 | little-endian | unsigned | 150 | 1000 | Nm | 1000 to 10300 | 63 = `SNA` | plausible |
| `UI_closureConfirmed` | Touchscreen user interface computer: closure confirmed | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `FRUNK`<br>2 = `PROX`<br>3 = `TRUNK` | plausible |
| `UI_regenTorqueMax` | Maximum regen torque from UI - reports different value when in track mode | 16\|5 | little-endian | unsigned | 5 | 0 | % | 0 to 100 |  | validated |
| `UI_limitMode` | Commands limited drive inverter capabilities based on special vehicle modes | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LIMIT_NORMAL`<br>1 = `LIMIT_VALET`<br>2 = `LIMIT_FACTORY`<br>3 = `LIMIT_SERVICE` | validated |
| `UI_factoryCustomerDrivingModeRequest` | Touchscreen user interface computer: factory customer driving mode request | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_motorOnMode` | Request from the UI to selectively enable or disable a drive unit (dev-only) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MOTORONMODE_NORMAL`<br>1 = `MOTORONMODE_FRONT_ONLY`<br>2 = `MOTORONMODE_REAR_ONLY` | validated |
| `UI_stoppingMode` | Low-speed behavior when no pedal is pressed (stopping/rolling/creeping) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `CREEP`<br>2 = `HOLD` | validated |
| `UI_DIAppSliderDebug` | Touchscreen user interface computer: DI app slider debug | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | plausible |
| `UI_speedLimit` | Maximum allowed speed enforced at vehicle level; raw 511 = signal not available (SNA) | 32\|12 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 335 | 511 = `SNA` | validated |
| `UI_enableSmartShift` | Stalkless convenience feature that allows unparking with only a firm press of brake pedal | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ENABLED_P`<br>2 = `ENABLED_P_R_D` | validated |
| `UI_navVehParallelToRdCanContinue` | Whether the vehicle is parallel parked on a public road; raw 0 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `FALSE`<br>2 = `TRUE` | validated |
| `UI_powertrainControlCounter` | Touchscreen user interface computer: powertrain control counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_powertrainControlChecksum` | Touchscreen user interface computer: powertrain control checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
