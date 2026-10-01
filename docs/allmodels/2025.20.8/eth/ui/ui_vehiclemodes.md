---
layout: default
title: "UI_vehicleModes (0x284) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: vehicle modes. Ethernet-side message UI_vehicleModes of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 22 signals (UI_factoryMode, UI_transportMode, UI_showroomMode, UI_serviceMode and 18 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleModes (0x284) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: vehicle modes. This page documents the 22 signals of UI_vehicleModes as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleModes` |
| Ethernet-side id | 0x284 (644) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 22 |

## Signals of UI_vehicleModes

Tesla Model 3 / Model Y CAN bus signals in `UI_vehicleModes`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_factoryMode` | Touchscreen user interface computer: factory mode | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `UI_transportMode` | Reports UI Transport mode. Distinct from GTW transport mode. | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TRANSPORT_MODE_DISABLED`<br>1 = `TRANSPORT_MODE_ENABLED` | plausible |
| `UI_showroomMode` | Reports UI showroom mode. | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHOWROOM_MODE_DISABLED`<br>1 = `SHOWROOM_MODE_ENABLED` | plausible |
| `UI_serviceMode` | Service diagnostics mode active | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SERVICE_MODE_DISABLED`<br>1 = `SERVICE_MODE_ENABLED` | plausible |
| `UI_isDelivered` | Touchscreen user interface computer: is delivered | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_hasEverBeenDelivered` | Touchscreen user interface computer: has ever been delivered | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_homelinkV2Command0` | Touchscreen user interface computer: homelink V2 command0 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UI_homelinkV2Command1` | Touchscreen user interface computer: homelink V2 command1 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UI_homelinkV2Command2` | Touchscreen user interface computer: homelink V2 command2 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `UI_carWashMode` | Car Wash Mode | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_valetMode` | Touchscreen user interface computer: valet mode | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_gameMode` | Game mode | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_diagnosticsAllowed` | Touchscreen user interface computer: diagnostics allowed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ALLOWED`<br>1 = `ALLOWED` | plausible |
| `UI_serviceModePlus` | Extended service diagnostics mode active | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SERVICE_MODE_PLUS_DISABLED`<br>1 = `SERVICE_MODE_PLUS_ENABLED` | plausible |
| `UI_premiumAmpPowerOff` | Premium amplifier power off request | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_signedCmdHardLocked` | Touchscreen user interface computer: signed cmd hard locked | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `UI_signedCmdServiceMode` | Signal reported by Touchscreen user interface computer | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `UI_closureEasterEggStatus` | Touchscreen user interface computer: closure easter egg status | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `PRIMED_REMOTE`<br>2 = `PRIMED`<br>3 = `PLAYING` | plausible |
| `UI_lightShowType` | Type of the light show to be run | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LIGHT_SHOW_TYPE_CUSTOM_USB`<br>1 = `LIGHT_SHOW_TYPE_STANDARD_CAROL_OF_THE_BELLS`<br>2 = `LIGHT_SHOW_TYPE_STANDARD_AULD_LANG_SYNE`<br>3 = `LIGHT_SHOW_TYPE_STANDARD_CNY23`<br>4 = `LIGHT_SHOW_TYPE_STANDARD_THE_ARRIVAL`<br>5 = `LIGHT_SHOW_TYPE_STANDARD_CNY24` | plausible |
| `UI_sohTestRequest` | Touchscreen user interface computer: soh test request | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_vehicleModesCounter` | Touchscreen user interface computer: vehicle modes counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_vehicleModesChecksum` | Touchscreen user interface computer: vehicle modes checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
