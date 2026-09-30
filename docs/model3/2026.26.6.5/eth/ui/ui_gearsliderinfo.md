---
layout: default
title: "UI_gearSliderInfo (0x3E1) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: gear slider info. Ethernet-side message UI_gearSliderInfo of Touchscreen user interface computer for Tesla Model 3 firmware 2026.26.6.5, 13 signals (UI_gearSliderInfoIndex, UI_gearSliderW, UI_gearSliderH, UI_gearSliderX and 9 more). Bit layout, scaling, units and value tables."
---

# UI_gearSliderInfo (0x3E1) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 ETH

Touchscreen user interface computer message: gear slider info. This page documents the 13 signals of UI_gearSliderInfo as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_gearSliderInfo` |
| Ethernet-side id | 0x3E1 (993) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 2000 ms |
| Signals | 13 |

## Signals of UI_gearSliderInfo

Tesla Model 3 CAN bus signals in `UI_gearSliderInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_gearSliderInfoIndex` | selector | Touchscreen user interface computer: gear slider info index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Slider`<br>1 = `Park`<br>2 = `Neutral` | plausible |
| `UI_gearSliderW` | page 0 | Touchscreen user interface computer: gear slider w | 2\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | layout-only |
| `UI_gearSliderH` | page 0 | Touchscreen user interface computer: gear slider h | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearSliderX` | page 0 | Touchscreen user interface computer: gear slider x | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearSliderY` | page 0 | Touchscreen user interface computer: gear slider y | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearParkW` | page 1 | Touchscreen user interface computer: gear park w | 2\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | layout-only |
| `UI_gearParkH` | page 1 | Touchscreen user interface computer: gear park h | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearParkX` | page 1 | Touchscreen user interface computer: gear park x | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearParkY` | page 1 | Touchscreen user interface computer: gear park y | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearNeutralW` | page 2 | Touchscreen user interface computer: gear neutral w | 2\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | layout-only |
| `UI_gearNeutralH` | page 2 | Touchscreen user interface computer: gear neutral h | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearNeutralX` | page 2 | Touchscreen user interface computer: gear neutral x | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `UI_gearNeutralY` | page 2 | Touchscreen user interface computer: gear neutral y | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |

## Multiplexing

`UI_gearSliderInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (4 signals), page 2 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
