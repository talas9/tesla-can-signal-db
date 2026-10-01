---
layout: default
title: "UI_stalklessControl (0x233) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: stalkless control. Ethernet-side message UI_stalklessControl of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 16 signals (UI_stalklessControlCounter, UI_stalklessControlChecksum, UI_gearStripSuppressCounter, UI_gearRequest and 12 more). Bit layout, scaling, units and value tables."
---

# UI_stalklessControl (0x233) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: stalkless control. This page documents the 16 signals of UI_stalklessControl as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_stalklessControl` |
| Ethernet-side id | 0x233 (563) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 6 bytes |
| Cycle time | 500 ms |
| Signals | 16 |

## Signals of UI_stalklessControl

Tesla Model 3 / Model Y CAN bus signals in `UI_stalklessControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_stalklessControlCounter` | Touchscreen user interface computer: stalkless control counter | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UI_stalklessControlChecksum` | Touchscreen user interface computer: stalkless control checksum | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_gearStripSuppressCounter` | Touchscreen user interface computer: gear strip suppress counter | 16\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `UI_gearRequest` | UI gear request from UI; raw 0 = signal not available (SNA) | 26\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `GEAR_REQUEST_IDLE_SNA`<br>1 = `GEAR_REQUEST_PARK`<br>2 = `GEAR_REQUEST_REVERSE`<br>3 = `GEAR_REQUEST_NEUTRAL`<br>4 = `GEAR_REQUEST_DRIVE` | plausible |
| `UI_autopilotRequest` | Touchscreen user interface computer: autopilot request | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `IDLE`<br>1 = `PRESSED` | plausible |
| `UI_fullScreenMode` | Aggregates all situations with which the UI is using the entire screen so stalkless gear controls are not present | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_gearStripShowing` | UI communicating to GTW that the gear strip is visible on the screen as part of a handshake | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_gearStripLocation` | Touchscreen user interface computer: gear strip location | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT`<br>1 = `RIGHT` | plausible |
| `UI_parkButtonShowing` | Touchscreen user interface computer: park button showing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_neutralButtonShowing` | Touchscreen user interface computer: neutral button showing | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_gearStripForceShow` | UI request to GTW to show the gear strip | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_neutralButtonDrawerForceShow` | Touchscreen user interface computer: neutral button drawer force show | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_autoParkAvailable` | UI communicating to GTW that the autpark functionality is available | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autoParkShowing` | Touchscreen user interface computer: auto park showing | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_gearStripSuppressActive` | UI communicating to GTW that the gear strip should not be shown | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_gearNeutralPressed` | Neutral button is being pressed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
