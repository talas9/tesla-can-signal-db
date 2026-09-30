---
layout: default
title: "UI_trackModeSettings (0x313) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: track mode settings. Tesla Model 3 CAN bus message UI_trackModeSettings (0x313) of Touchscreen user interface computer, firmware 2026.26.6.5, 10 signals (UI_trackModeRequest, UI_trackRotationTendency, UI_trackStabilityAssist, UI_trackPostCooling and 6 more). Bit layout, scaling, units and value tables."
---

# UI_trackModeSettings (0x313) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: track mode settings; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 10 signals of UI_trackModeSettings as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_trackModeSettings` |
| CAN id | 0x313 (787) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 10 |

## Signals of UI_trackModeSettings

Tesla Model 3 CAN bus signals in `UI_trackModeSettings`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_trackModeRequest` | User selected track mode | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK_MODE_REQUEST_IDLE`<br>1 = `TRACK_MODE_REQUEST_ON`<br>2 = `TRACK_MODE_REQUEST_OFF` | validated |
| `UI_trackRotationTendency` | Touchscreen user interface computer: track rotation tendency | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `UI_trackStabilityAssist` | Touchscreen user interface computer: track stability assist | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `UI_trackPostCooling` | Touchscreen user interface computer: track post cooling | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackCmpOverclock` | Touchscreen user interface computer: track cmp overclock | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackModeBrakeTemps` | Touchscreen user interface computer: track mode brake temps | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackDrivePowerAvailability` | Reports power deployment strategy for Track Mode. Ranges from endurance limit to maximum power. | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK_MODE_POWER_ENDURANCE`<br>1 = `TRACK_MODE_POWER_MIDDLE`<br>2 = `TRACK_MODE_POWER_MAX` | validated |
| `UI_stabilityModeRequest` | Touchscreen user interface computer: stability mode request | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NORMAL_REQUEST`<br>1 = `REDUCED_REQUEST` | plausible |
| `UI_trackModeSettingsCounter` | Touchscreen user interface computer: track mode settings counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_trackModeSettingsChecksum` | Touchscreen user interface computer: track mode settings checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
