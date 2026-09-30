---
layout: default
title: "UI_trackModeSettings (0x313) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: track mode settings. Ethernet-side message UI_trackModeSettings of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 9 signals (UI_trackModeRequest, UI_trackRotationTendency, UI_trackStabilityAssist, UI_trackPostCooling and 5 more). Bit layout, scaling, units and value tables."
---

# UI_trackModeSettings (0x313) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: track mode settings. This page documents the 9 signals of UI_trackModeSettings as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_trackModeSettings` |
| Ethernet-side id | 0x313 (787) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 9 |

## Signals of UI_trackModeSettings

Tesla Model Y CAN bus signals in `UI_trackModeSettings`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_trackModeRequest` | User selected track mode | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK_MODE_REQUEST_IDLE`<br>1 = `TRACK_MODE_REQUEST_ON`<br>2 = `TRACK_MODE_REQUEST_OFF` | validated |
| `UI_trackRotationTendency` | Touchscreen user interface computer: track rotation tendency | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `UI_trackStabilityAssist` | Touchscreen user interface computer: track stability assist | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 127.5 |  | plausible |
| `UI_trackPostCooling` | Touchscreen user interface computer: track post cooling | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackCmpOverclock` | Touchscreen user interface computer: track cmp overclock | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackModeBrakeTemps` | Touchscreen user interface computer: track mode brake temps | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `UI_trackDrivePowerAvailability` | Reports power deployment strategy for Track Mode. Ranges from endurance limit to maximum power. | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK_MODE_POWER_ENDURANCE`<br>1 = `TRACK_MODE_POWER_MIDDLE`<br>2 = `TRACK_MODE_POWER_MAX` | validated |
| `UI_trackModeSettingsCounter` | Touchscreen user interface computer: track mode settings counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_trackModeSettingsChecksum` | Touchscreen user interface computer: track mode settings checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
