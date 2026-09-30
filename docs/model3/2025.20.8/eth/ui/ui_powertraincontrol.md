---
layout: default
title: "UI_powertrainControl (0x334) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH"
description: "Touchscreen user interface computer message: powertrain control. Ethernet-side message UI_powertrainControl of Touchscreen user interface computer for Tesla Model 3 firmware 2025.20.8, 18 signals (UI_systemPowerLimit, UI_pedalMap, UI_enableRegenBackfill, UI_systemTorqueLimit and 14 more). Bit layout, scaling, units and value tables."
---

# UI_powertrainControl (0x334) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH

Touchscreen user interface computer message: powertrain control. This page documents the 18 signals of UI_powertrainControl as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_powertrainControl` |
| Ethernet-side id | 0x334 (820) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 18 |

## Signals of UI_powertrainControl

Tesla Model 3 CAN bus signals in `UI_powertrainControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

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
| `UI_wasteMode` | Touchscreen user interface computer: waste mode | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `PARTIAL`<br>2 = `FULL`<br>3 = `BURN_IN` | plausible |
| `UI_wasteModeRegenLimit` | Touchscreen user interface computer: waste mode regen limit | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MAX`<br>1 = `30A`<br>2 = `10A`<br>3 = `0A` | plausible |
| `UI_stoppingMode` | Low-speed behavior when no pedal is pressed (stopping/rolling/creeping) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `CREEP`<br>2 = `HOLD` | plausible |
| `UI_DIAppSliderDebug` | Touchscreen user interface computer: DI app slider debug | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | plausible |
| `UI_speedLimit` | Maximum allowed speed enforced at vehicle level; raw 511 = signal not available (SNA) | 34\|12 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 335 | 511 = `SNA` | plausible |
| `UI_enableSmartShift` | Stalkless convenience feature that allows unparking with only a firm press of brake pedal | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ENABLED_P`<br>2 = `ENABLED_P_R_D` | plausible |
| `UI_navVehParallelToRdCanContinue` | Whether the vehicle is parallel parked on a public road; raw 0 = signal not available (SNA) | 49\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `FALSE`<br>2 = `TRUE` | plausible |
| `UI_powertrainControlCounter` | Touchscreen user interface computer: powertrain control counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_powertrainControlChecksum` | Touchscreen user interface computer: powertrain control checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
