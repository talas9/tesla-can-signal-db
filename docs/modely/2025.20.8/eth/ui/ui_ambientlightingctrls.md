---
layout: default
title: "UI_ambientLightingCtrls (0x679) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: ambient lighting ctrls. Ethernet-side message UI_ambientLightingCtrls of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 13 signals (UI_ambientLightPopupOpen, UI_rgbEnableState, UI_rgbEffectType, UI_rgbLightingColorHexRed and 9 more). Bit layout, scaling, units and value tables."
---

# UI_ambientLightingCtrls (0x679) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: ambient lighting ctrls. This page documents the 13 signals of UI_ambientLightingCtrls as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_ambientLightingCtrls` |
| Ethernet-side id | 0x679 (1657) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 7 bytes |
| Cycle time | 500 ms |
| Signals | 13 |

## Signals of UI_ambientLightingCtrls

Tesla Model Y CAN bus signals in `UI_ambientLightingCtrls`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ambientLightPopupOpen` | Touchscreen user interface computer: ambient light popup open | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_rgbEnableState` | Request to enable RGB lights | 1\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ON`<br>2 = `AUTO` | validated |
| `UI_rgbEffectType` | Reports the RGB light effect type. | 3\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `RAMP_INSTANT`<br>1 = `RAMP_250MS`<br>2 = `RAMP_500MS`<br>3 = `RAMP_750MS`<br>4 = `RAMP_1000MS`<br>5 = `RAMP_1250MS`<br>6 = `RAMP_1500MS`<br>7 = `RAMP_1750MS`<br>8 = `RAMP_2000MS`<br>9 = `RAMP_2250MS`<br>10 = `RAMP_2500MS`<br>11 = `RAMP_2750MS`<br>12 = `RAMP_3000MS`<br>13 = `RAMP_3250MS`<br>14 = `RAMP_3500MS`<br>15 = `RAMP_3750MS`<br>16 = `RAMP_4000MS`<br>17 = `RAMP_4250MS`<br>18 = `RAMP_4500MS`<br>19 = `RAMP_4750MS`<br>20 = `RAMP_5000MS` | validated |
| `UI_rgbLightingColorHexRed` | Touchscreen user interface computer: rgb lighting color hex red | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_rgbLightingColorHexGreen` | Touchscreen user interface computer: rgb lighting color hex green | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_rgbLightingColorHexBlue` | Touchscreen user interface computer: rgb lighting color hex blue | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `UI_rgbBrightnessLevel` | Reports the requested RGB brightness level; raw 127 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | validated |
| `UI_rgbTargetDOORFL` | Target RGB control for front left door | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rgbTargetDOORFR` | Target RGB control for the front right door | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rgbTargetDOORRL` | Target RGB control for rear left door | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rgbTargetDOORRR` | Target RGB control for the rear right door | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rgbTargetIPFL` | Reports control for RGB lighting for the front left instrument panel. | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rgbTargetIPFR` | Reports control for RGB lighting for the front right instrument panel. | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
