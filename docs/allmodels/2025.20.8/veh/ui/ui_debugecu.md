---
layout: default
title: "UI_debugECU (0x500) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Touchscreen user interface computer message: debug ECU. Tesla Model 3 / Model Y CAN bus message UI_debugECU (0x500) of Touchscreen user interface computer, firmware 2025.20.8, 15 signals (UI_debugEcuTarget, UI_DI_debugEnable, UI_DIS_debugEnable, UI_PM_debugEnable and 11 more). Bit layout, scaling, units and value tables."
---

# UI_debugECU (0x500) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Touchscreen user interface computer message: debug ECU; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of UI_debugECU as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_debugECU` |
| CAN id | 0x500 (1280) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 2 bytes |
| Cycle time | 5000 ms |
| Signals | 15 |

## Signals of UI_debugECU

Tesla Model 3 / Model Y CAN bus signals in `UI_debugECU`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_debugEcuTarget` | selector | Touchscreen user interface computer: debug ecu target | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 1 = `DI`<br>2 = `DIS`<br>3 = `PM`<br>4 = `PMS`<br>5 = `BMS`<br>6 = `VCRIGHT`<br>7 = `VCFRONT`<br>8 = `DIF`<br>9 = `DIR`<br>10 = `PMF`<br>11 = `PMR`<br>12 = `DIREL`<br>13 = `DIRER`<br>14 = `PMREL`<br>15 = `PMRER`<br>16 = `DIRE1L`<br>17 = `DIRE1R`<br>18 = `DIRE2`<br>19 = `PMRE1L`<br>20 = `PMRE2L`<br>21 = `PMRE2` | plausible |
| `UI_DI_debugEnable` | page 1 | Touchscreen user interface computer: DI debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_DIS_debugEnable` | page 2 | Touchscreen user interface computer: DIS debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PM_debugEnable` | page 3 | Touchscreen user interface computer: PM debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PM_debugAt100Hz` | page 3 | Touchscreen user interface computer: PM debug at100 hz | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PMS_debugEnable` | page 4 | Touchscreen user interface computer: PMS debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PMS_debugAt100Hz` | page 4 | Touchscreen user interface computer: PMS debug at100 hz | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_BMS_debugAllEnable` | page 5 | Touchscreen user interface computer: BMS debug all enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_BMS_debugDisable` | page 5 | Touchscreen user interface computer: BMS debug disable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_VCRIGHT_debugEnable` | page 6 | Touchscreen user interface computer: VCRIGHT debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_VCFRONT_debugEnable` | page 7 | Touchscreen user interface computer: VCFRONT debug enable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_DIF_debugEnable` | page 8 | Touchscreen user interface computer: DIF debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_DIR_debugEnable` | page 9 | Touchscreen user interface computer: DIR debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PMF_debugEnable` | page 10 | Touchscreen user interface computer: PMF debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_PMR_debugEnable` | page 11 | Touchscreen user interface computer: PMR debug enable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`UI_debugEcuTarget` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (1 signals), page 3 (2 signals), page 4 (2 signals), page 5 (2 signals), page 6 (1 signals), page 7 (1 signals), page 8 (1 signals), page 9 (1 signals), page 10 (1 signals), page 11 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
