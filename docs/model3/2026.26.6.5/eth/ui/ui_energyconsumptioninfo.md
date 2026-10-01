---
layout: default
title: "UI_energyConsumptionInfo (0x4FF) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: energy consumption info. Ethernet-side message UI_energyConsumptionInfo of Touchscreen user interface computer for Tesla Model 3 firmware 2026.26.6.5, 63 signals (UI_energyConsumptionInfoIndex, UI_energyLossTotal_epa, UI_energyLossDriving_epa, UI_energyLossClimate_epa and 59 more). Bit layout, scaling, units and value tables."
---

# UI_energyConsumptionInfo (0x4FF) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 ETH

Touchscreen user interface computer message: energy consumption info. This page documents the 63 signals of UI_energyConsumptionInfo as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_energyConsumptionInfo` |
| Ethernet-side id | 0x4FF (1279) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of UI_energyConsumptionInfo

Tesla Model 3 CAN bus signals in `UI_energyConsumptionInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_energyConsumptionInfoIndex` | selector | Touchscreen user interface computer: energy consumption info index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7`<br>8 = `8`<br>9 = `9`<br>10 = `10`<br>11 = `11`<br>12 = `12`<br>13 = `13`<br>14 = `14`<br>15 = `15`<br>16 = `16`<br>17 = `17`<br>18 = `18`<br>19 = `19`<br>20 = `20`<br>21 = `21` | plausible |
| `UI_energyLossTotal_epa` | page 0 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossDriving_epa` | page 0 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossClimate_epa` | page 0 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossBattCond_epa` | page 1 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossElevation_epa` | page 1 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossAcc_epa` | page 1 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossTotalSinceCharge_epa` | page 2 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossDrivingSinceCharge_epa` | page 2 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossClimateSinceCharge_epa` | page 2 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossBattCondSinceCharge_epa` | page 3 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossElevationSinceCharge_epa` | page 3 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossAccSinceCharge_epa` | page 3 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossTotalSinceTripStart` | page 4 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossDrivingSinceTripStart` | page 4 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossClimateSinceTripStart` | page 4 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossBattCondSinceTripStart` | page 5 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossElevationSinceTripStart` | page 5 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyLossAccSinceTripStart` | page 5 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaTotal_epa` | page 6 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaDriving_epa` | page 6 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaClimate_epa` | page 6 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaBattCond_epa` | page 7 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaElevation_epa` | page 7 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaAcc_epa` | page 7 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetTotal_epa` | page 8 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetDriving_epa` | page 8 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetClimate_epa` | page 8 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetBattCond_epa` | page 9 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetElevation_epa` | page 9 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetAcc_epa` | page 9 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_rawToUiEnergyRatio_epa` | page 10 | Ratio used for conversion between UI and raw energy domains | 8\|8 | little-endian | unsigned | 0.01 | 0 | - | 0 to 2.55 |  | plausible |
| `UI_driveDistance_epa` | page 10 | Distance driven for an energy consumption baseline | 16\|16 | little-endian | unsigned | 0.01 | 0 | miles | 0 to 655.35 |  | plausible |
| `UI_energyDeltaTotalSinceCharge_epa` | page 11 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaDrivingSinceCharge_epa` | page 11 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaClimateSinceCharge_epa` | page 11 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaBattCondSinceCharge_epa` | page 12 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaElevationSinceCharge_epa` | page 12 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaAccSinceCharge_epa` | page 12 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetTotalSinceCharge_epa` | page 13 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetDrivingSinceCharge_epa` | page 13 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetClimateSinceCharge_epa` | page 13 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetBattCondSinceCharge_epa` | page 14 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetElevationSinceCharge_epa` | page 14 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetAccSinceCharge_epa` | page 14 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_rawToUiEnergyRatioSinceCharge_epa` | page 15 | Ratio used for conversion between UI and raw energy domains | 8\|8 | little-endian | unsigned | 0.01 | 0 | - | 0 to 2.55 |  | plausible |
| `UI_driveDistanceSinceCharge_epa` | page 15 | Distance driven for an energy consumption baseline | 16\|16 | little-endian | unsigned | 0.01 | 0 | miles | 0 to 655.35 |  | plausible |
| `UI_energyDeltaTotalSinceTripStart` | page 16 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaDrivingSinceTripStart` | page 16 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaClimateSinceTripStart` | page 16 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaBattCondSinceTripStart` | page 17 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaElevationSinceTripStart` | page 17 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_energyDeltaAccSinceTripStart` | page 17 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetTotalSinceTripStart` | page 18 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetDrivingSinceTripStart` | page 18 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetClimateSinceTripStart` | page 18 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetBattCondSinceTripStart` | page 19 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 16\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetElevationSinceTripStart` | page 19 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 32\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_uiDeltaOffsetAccSinceTripStart` | page 19 | Energy amount for a given bucket for an energy consumption baseline (raw/real energy consumed) | 48\|16 | little-endian | signed | 1 | 0 | Wh | -32768 to 32767 |  | plausible |
| `UI_rawToUiEnergyRatioSinceTripStart` | page 20 | Ratio used for conversion between UI and raw energy domains | 8\|8 | little-endian | unsigned | 0.01 | 0 | - | 0 to 2.55 |  | plausible |
| `UI_driveDistanceSinceTripStart` | page 20 | Distance driven for an energy consumption baseline | 16\|16 | little-endian | unsigned | 0.01 | 0 | miles | 0 to 655.35 |  | plausible |
| `UI_voyagerEnabled` | page 21 | Touchscreen user interface computer: voyager enabled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_trailerMass` | page 21 | Trailer mass from user input | 16\|16 | little-endian | unsigned | 1 | 0 | kg | 0 to 65535 |  | plausible |

## Multiplexing

`UI_energyConsumptionInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals), page 1 (3 signals), page 2 (3 signals), page 3 (3 signals), page 4 (3 signals), page 5 (3 signals), page 6 (3 signals), page 7 (3 signals), page 8 (3 signals), page 9 (3 signals), page 10 (2 signals), page 11 (3 signals), page 12 (3 signals), page 13 (3 signals), page 14 (3 signals), page 15 (2 signals), page 16 (3 signals), page 17 (3 signals), page 18 (3 signals), page 19 (3 signals), page 20 (2 signals), page 21 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
