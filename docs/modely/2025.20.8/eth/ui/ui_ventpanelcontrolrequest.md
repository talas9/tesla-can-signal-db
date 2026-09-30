---
layout: default
title: "UI_ventPanelControlRequest (0x253) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: vent panel control request. Ethernet-side message UI_ventPanelControlRequest of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 14 signals (UI_ventPanelControlRequestIndex, UI_ventPanelLeftPositionX, UI_ventPanelLeftPositionY, UI_ventPanelLeftLateralSplit and 10 more). Bit layout, scaling, units and value tables."
---

# UI_ventPanelControlRequest (0x253) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: vent panel control request. This page documents the 14 signals of UI_ventPanelControlRequest as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_ventPanelControlRequest` |
| Ethernet-side id | 0x253 (595) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 14 |

## Signals of UI_ventPanelControlRequest

Tesla Model Y CAN bus signals in `UI_ventPanelControlRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_ventPanelControlRequestIndex` | selector | Touchscreen user interface computer: vent panel control request index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `UI_ventPanelLeftPositionX` | page 0 | Airwave left X position. | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelLeftPositionY` | page 0 | Airwave left Y position. | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelLeftLateralSplit` | page 0 | Airwave left split amount. | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelRightPositionX` | page 0 | Airwave right X position. | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelRightPositionY` | page 0 | Airwave right Y position. | 40\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelRightLateralSplit` | page 0 | Airwave right split amount. | 48\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_ventPanelLeftLateralMode` | page 0 | Airwave left focus or split. | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SINGLE`<br>1 = `SPLIT`<br>2 = `SWING` | validated |
| `UI_ventPanelRightLateralMode` | page 0 | Airwave right focus or split. | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SINGLE`<br>1 = `SPLIT`<br>2 = `SWING` | validated |
| `UI_hvacReqActiveVents` | page 0 | Active airwave sides - left/right/both | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BOTH`<br>1 = `LEFT`<br>2 = `RIGHT`<br>3 = `OFF` | validated |
| `UI_vent2RLeftPositionX` | page 1 | Airwave left X position. | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_vent2RLeftPositionY` | page 1 | Airwave left Y position. | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_vent2RRightPositionX` | page 1 | Airwave left X position. | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `UI_vent2RRightPositionY` | page 1 | Airwave left Y position. | 32\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |

## Multiplexing

`UI_ventPanelControlRequestIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals), page 1 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
