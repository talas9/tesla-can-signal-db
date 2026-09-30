---
layout: default
title: "BMS_log2 (0x3B2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: log2. Tesla Model Y CAN bus message BMS_log2 (0x3B2) of High-voltage battery management system, firmware 2026.26.6.5, 131 signals (BMS_log2MuxId, BMS_maxChargeRestartNeededByVoltage, BMS_cacAvg, BMS_maxChargeNearComplete and 127 more). Bit layout, scaling, units and value tables."
---

# BMS_log2 (0x3B2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: log2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 131 signals of BMS_log2 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_log2` |
| CAN id | 0x3B2 (946) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 30000 ms |
| Signals | 131 |

## Signals of BMS_log2

Tesla Model Y CAN bus signals in `BMS_log2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_log2MuxId` | selector | High-voltage battery management system: log2 mux id | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `CAC1`<br>1 = `CAC2`<br>2 = `FLOOD_PORT`<br>3 = `VSH_TEST`<br>4 = `CHARGING`<br>5 = `AHR_COUNTER`<br>6 = `1HZ_TASK_STATS`<br>7 = `10HZ_TASK_STATS`<br>8 = `100HZ_1KHZ_TASK_STATS`<br>9 = `CTR_RESISTANCE`<br>10 = `POS_CTR_HEALTH_1`<br>11 = `POS_CTR_HEALTH_2`<br>12 = `POS_CTR_HEALTH_3`<br>13 = `POS_CTR_HEALTH_4`<br>14 = `NEG_CTR_HEALTH_1`<br>15 = `NEG_CTR_HEALTH_2`<br>16 = `NEG_CTR_HEALTH_3`<br>17 = `NEG_CTR_HEALTH_4`<br>18 = `HV_CHAIN_MODEL`<br>19 = `ENERGY_RESERVE`<br>20 = `FC_LINK_LEAKAGE_TEST`<br>21 = `ENERGY_AND_REST_DATA`<br>22 = `CAC3`<br>23 = `BRICK_VOLTAGE_CHANGE`<br>24 = `SOC_BY_OCV_CORRECTION`<br>25 = `VSH_RES_1`<br>26 = `VSH_RES_2`<br>27 = `VSH_RES_3`<br>28 = `HISTOGRAMS_0`<br>29 = `HISTOGRAMS_1`<br>30 = `HISTOGRAMS_2`<br>31 = `HISTOGRAMS_3`<br>32 = `HISTOGRAMS_4`<br>33 = `ALPHA_1`<br>34 = `BRICK_BALANCE_1`<br>35 = `BRICK_BALANCE_2`<br>36 = `BRICK_BALANCE_3`<br>37 = `BRICK_BALANCE_4`<br>38 = `LIFE_MODEL`<br>39 = `BRICK_BLEED_TIMES_1`<br>40 = `BRICK_BLEED_TIMES_2`<br>41 = `BRICK_BLEED_TIMES_3`<br>42 = `BRICK_BLEED_TIMES_4`<br>43 = `ISOLATION`<br>44 = `CAC4`<br>45 = `SOH`<br>46 = `HISTOGRAMS_SUMMARY`<br>47 = `BRICK_BLEED_TIMES_5`<br>48 = `SPME_PACK_LEVEL`<br>49 = `SPME_BRICK_1_DATA_1`<br>50 = `SPME_BRICK_1_DATA_2`<br>51 = `SPME_DATA_3`<br>52 = `SPME_MIN_SOC_BRICK_DATA`<br>53 = `SPME_MAX_SOC_BRICK_DATA`<br>54 = `LIFE_MODEL_STORAGE_HIST_DATA`<br>55 = `LIFE_MODEL_HIST_SUMMARY_DATA`<br>56 = `MUX_56`<br>57 = `MUX_57`<br>58 = `MUX_58`<br>59 = `MUX_59`<br>60 = `MUX_60`<br>61 = `MUX_61`<br>62 = `MUX_62`<br>63 = `MUX_63`<br>64 = `MUX_64`<br>65 = `MUX_65`<br>66 = `MUX_66`<br>67 = `MUX_67`<br>68 = `MUX_68`<br>69 = `MUX_69`<br>70 = `MUX_70`<br>71 = `MUX_71`<br>72 = `MUX_72`<br>73 = `MUX_73`<br>74 = `MUX_74`<br>75 = `MUX_75`<br>76 = `MUX_76`<br>77 = `MUX_77`<br>78 = `BANDOLIER_MODEL_THERMISTOR_TEMPS_1`<br>79 = `MUX_79`<br>80 = `MUX_80`<br>81 = `MUX_81`<br>82 = `MUX_82`<br>83 = `MUX_83`<br>84 = `MUX_84`<br>85 = `MUX_85`<br>86 = `MUX_86`<br>87 = `MUX_87`<br>88 = `MUX_88`<br>89 = `MUX_89`<br>90 = `MUX_90`<br>91 = `MUX_91`<br>92 = `BANDOLIER_MODEL_THERMISTOR_TEMPS_2`<br>93 = `MUX_93`<br>94 = `SOC_IMBALANCE_BY_DV_DSOC`<br>95 = `MUX_95` | plausible |
| `BMS_maxChargeRestartNeededByVoltage` | page 0 | High-voltage battery management system: max charge restart needed by voltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cacAvg` | page 0 | BMS Calculated Ah Capacity (CAC). This is the average of all the brick CACs | 8\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819.1 |  | validated |
| `BMS_maxChargeNearComplete` | page 0 | High-voltage battery management system: max charge near complete | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cacMin` | page 0 | BMS Calculated Ah Capacity (CAC). This is the min of all the brick CACs | 24\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819.1 |  | validated |
| `BMS_cacMinBrickId` | page 0 | High-voltage battery management system: cac min brick id | 37\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | validated |
| `BMS_cacMax` | page 0 | BMS Calculated Ah Capacity (CAC). This is the max of all the brick CACs | 44\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819.1 |  | validated |
| `BMS_cacMaxBrickId` | page 0 | High-voltage battery management system: cac max brick id | 57\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | validated |
| `BMS_acRippleConfigNvramValid` | page 18 | High-voltage battery management system: ac ripple config nvram valid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_hvChain_useLeakyBucket` | page 18 | Is the leaky bucket being used - an indicator of the HV Chain Model health | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_hvChain_iLimit` | page 18 | High-voltage battery management system: hv chain i limit; raw 16383 = signal not available (SNA) | 9\|14 | little-endian | unsigned | 0.2 | 0 | A | 0 to 3275 | 16383 = `SNA` | validated |
| `BMS_hvChain_limitingState` | page 18 | High-voltage battery management system: hv chain limiting state; raw 511 = signal not available (SNA) | 23\|9 | little-endian | unsigned | 1 | 1 |  | 1 to 511 | 511 = `SNA` | validated |
| `BMS_hvChain_limitingStateTemperature` | page 18 | High-voltage battery management system: hv chain limiting state temperature; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 0.1 | 367.6 | DegC | -40 to 775 | -4096 = `SNA` | contradicted |
| `BMS_acRippleIsSupported` | page 18 | High-voltage battery management system: ac ripple is supported | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_acRippleStartTemperatureMax` | page 18 | High-voltage battery management system: ac ripple start temperature max | 46\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_acRippleStartTemperatureMin` | page 18 | High-voltage battery management system: ac ripple start temperature min | 55\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_fcLinkTestDecayTime` | page 20 | High-voltage battery management system: fc link test decay time; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 2 | 0 | mS | 0 to 2044 | 1023 = `SNA` | validated |
| `BMS_fcLinkTestTimeSinceLastRun` | page 20 | High-voltage battery management system: fc link test time since last run | 18\|12 | little-endian | unsigned | 0.0175824183971 | 0 | Hours | 0 to 71.99 |  | validated |
| `BMS_pcsPrechargeRequest` | page 20 | Enum indicating the active precharge request type from BMS to PCS | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PRECHARGE_INACTIVE`<br>1 = `FC_LINK_TEST`<br>2 = `LV_DISCHARGE` | validated |
| `BMS_pcsPrechargeTargetVoltage` | page 20 | Target voltage for precharging HV bus | 32\|16 | little-endian | signed | 0.1 | 0 | V | -3276.8 to 3276.7 |  | validated |
| `BMS_recentOvUvAlert` | page 20 | At least one of the Brick OV or UV alerts has been active recently; consumed by BMS_a049_SW_Thermal_Event set condition | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_recentIsoAlert` | page 20 | At least one of the isolation alerts has been active recently; consumed by BMS_a049_SW_Thermal_Event set condition | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_recentBmbMiaAlert` | page 20 | At least one of the BMB communication alerts has been active recently; consumed by BMS_a049_SW_Thermal_Event set condition | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cacBlendingConfigNvramValid` | page 20 | High-voltage battery management system: cac blending config nvram valid | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cacBlendingEnabled` | page 20 | High-voltage battery management system: cac blending enabled | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cacBlendPercentPerCycle` | page 20 | High-voltage battery management system: cac blend percent per cycle | 53\|10 | little-endian | unsigned | 0.001 | 0 | % | 0 to 1.023 |  | validated |
| `BMS_energyVariableChgRequested` | page 21 | High-voltage battery management system: energy variable chg requested | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_packRestTime` | page 21 | Minimum resting time of all bricks | 9\|12 | little-endian | unsigned | 0.0175824183971 | 0 | Hours | 0 to 71.99 |  | validated |
| `BMS_idealEnergyFloor` | page 21 | Ideal energy estimate based on the min bounded SOC that accounts for accumulated shunt error; raw 1023 = signal not available (SNA) | 21\|10 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 102.2 | 1023 = `SNA` | validated |
| `BMS_thmGradientSlopeCondition` | page 21 | High-voltage battery management system: thm gradient slope condition | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_recentSlopeConditon` | page 21 | High-voltage battery management system: recent slope conditon | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_dynamicEnergyBuffer` | page 21 | BMS estimate of energy error based on SOC measurement inaccuracy; raw 1023 = signal not available (SNA) | 33\|10 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 102.2 | 1023 = `SNA` | validated |
| `BMS_temperatureCondition` | page 21 | High-voltage battery management system: temperature condition | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_thmGradientSlope` | page 21 | High-voltage battery management system: thm gradient slope | 44\|10 | little-endian | signed | 0.01 | 0 | C/min | -5.12 to 5.11 |  | validated |
| `BMS_thmGradient` | page 21 | High-voltage battery management system: thm gradient | 56\|8 | little-endian | unsigned | 0.1 | 0 | C | 0 to 25.5 |  | validated |
| `BMS_epochTimeEstimate` | page 29 | High-voltage battery management system: epoch time estimate | 8\|32 | little-endian | unsigned | 1 | 0 | s | 0 to 4294967295 |  | plausible |
| `BMS_histogramStartTimeIrrational` | page 30 | High-voltage battery management system: histogram start time irrational | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_histogramDischargeThroughputIrrational` | page 30 | High-voltage battery management system: histogram discharge throughput irrational | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_histogramChargeThroughputIrrational` | page 30 | High-voltage battery management system: histogram charge throughput irrational | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_histogramTotalTimeIrrational` | page 30 | High-voltage battery management system: histogram total time irrational | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_histogramStorageDataIsLow` | page 30 | High-voltage battery management system: histogram storage data is low | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_tempVsSocTotalChgEnergy` | page 31 | High-voltage battery management system: temp vs soc total chg energy | 7\|25 | little-endian | unsigned | 0.000149011611938 | 0 | wh/wh | 0 to 4999.99985097 |  | validated |
| `BMS_powerVsVoltageTotalChgEnergy` | page 31 | High-voltage battery management system: power vs voltage total chg energy | 32\|25 | little-endian | unsigned | 0.000149011611938 | 0 | wh/wh | 0 to 4999.99985097 |  | validated |
| `BMS_lifeModelOutputsAreTrustworthy` | page 31 | High-voltage battery management system: life model outputs are trustworthy | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_dSocNormalizedMin` | page 33 | High-voltage battery management system: d soc normalized min; raw 4095 = signal not available (SNA) | 8\|12 | little-endian | unsigned | 0.0030517578125 | -12.4969482422 | % | -12.4969482422 to -0.003051757825 | 4095 = `SNA` | validated |
| `BMS_dSocNormalizedFiltMin` | page 33 | High-voltage battery management system: d soc normalized filt min; raw 4095 = signal not available (SNA) | 20\|12 | little-endian | unsigned | 0.0030517578125 | -12.4969482422 | % | -12.4969482422 to -0.003051757825 | 4095 = `SNA` | validated |
| `BMS_dSocMinAlpha` | page 33 | minimum calculated alpha value across all bricks and all dSOC calculations; raw 4095 = signal not available (SNA) | 32\|12 | little-endian | unsigned | 0.0030517578125 | -12.4969482422 | % | -12.4969482422 to -0.003051757825 | 4095 = `SNA` | validated |
| `BMS_dSocMaxLowAlphaCounter` | page 33 | High-voltage battery management system: d soc max low alpha counter | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `BMS_dSocMinAlphaBrickID` | page 33 | High-voltage battery management system: d soc min alpha brick ID | 48\|7 | little-endian | unsigned | 1 | 1 |  | 1 to 128 |  | validated |
| `BMS_dSocCacMargin` | page 33 | High-voltage battery management system: d soc cac margin; raw 511 = signal not available (SNA) | 55\|9 | little-endian | unsigned | 0.0030517578125 | 0 | % | 0 to 1.55639648438 | 511 = `SNA` | validated |
| `BMS_lifeModelNoCurrentStorageCapacityLoss` | page 54 | High-voltage battery management system: life model no current storage capacity loss; raw 511 = signal not available (SNA) | 7\|9 | little-endian | unsigned | 0.1 | 0 | % | 0 to 51 | 511 = `SNA` | validated |
| `BMS_lifeModelShortDcr` | page 54 | High-voltage battery management system: life model short dcr; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.01 | 0 | mOhm | 0 to 2.54 | 255 = `SNA` | validated |
| `BMS_lifeModelLongDcr` | page 54 | High-voltage battery management system: life model long dcr; raw 4096 = signal not available (SNA) | 24\|13 | little-endian | signed | 0.1 | 309.6 | mOhm | -100 to 719 | -4096 = `SNA` | validated |
| `BMS_lifeModelStorageCapacityLoss` | page 54 | High-voltage battery management system: life model storage capacity loss; raw 511 = signal not available (SNA) | 37\|9 | little-endian | unsigned | 0.1 | 0 | % | 0 to 51 | 511 = `SNA` | validated |
| `BMS_lifeModelThroughputCapacityLoss` | page 54 | High-voltage battery management system: life model throughput capacity loss; raw 511 = signal not available (SNA) | 46\|9 | little-endian | unsigned | 0.1 | 0 | % | 0 to 51 | 511 = `SNA` | validated |
| `BMS_passiveCoolCellTargetT` | page 54 | High-voltage battery management system: passive cool cell target t | 55\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_lifeModelAvgTempSeverity` | page 55 | High-voltage battery management system: life model avg temp severity; raw 31 = signal not available (SNA) | 8\|5 | little-endian | unsigned | 0.1 | 0 | - | 0 to 3 | 31 = `SNA` | validated |
| `BMS_lifeModelDepthOfDischargeSeverity` | page 55 | High-voltage battery management system: life model depth of discharge severity; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.01 | 0 | - | 0 to 1.5 | 255 = `SNA` | validated |
| `BMS_lifeModelHistogramCapacityLoss` | page 55 | High-voltage battery management system: life model histogram capacity loss; raw 511 = signal not available (SNA) | 24\|9 | little-endian | unsigned | 0.1 | 0 | % | 0 to 51 | 511 = `SNA` | validated |
| `BMS_lifeModelHistogramBrickCapacity` | page 55 | High-voltage battery management system: life model histogram brick capacity; raw 8191 = signal not available (SNA) | 33\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819 | 8191 = `SNA` | validated |
| `BMS_lifeModelDcrGrowthPercent` | page 55 | High-voltage battery management system: life model dcr growth percent; raw 8192 = signal not available (SNA) | 48\|14 | little-endian | signed | 0.1 | 200 | % | -100 to 500 | -8192 = `SNA` | validated |
| `BMS_nominalFullPackEnergyRaw` | page 56 | Non-latched version of BMS_nominalEnergyRemaining; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_nominalEnergyRemainingBuffered` | page 56 | Buffered version of BMS_nominalEnergyRemaining; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_idealEnergyRemainingBuffered` | page 56 | Buffered version of BMS_idealEnergyRemaining; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_largestSynchronizedCacErrorPct` | page 56 | High-voltage battery management system: largest synchronized cac error pct; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.1 | 0 | % | 0 to 25.4 | 255 = `SNA` | validated |
| `BMS_lifeModelSpreadMinOffset` | page 60 | High-voltage battery management system: life model spread min offset | 8\|10 | little-endian | signed | 0.1 | 0 | Ah | -51.1 to 51.1 | -512 = `SNA` | plausible |
| `BMS_lifeModelSpreadMaxOffset` | page 60 | High-voltage battery management system: life model spread max offset | 18\|10 | little-endian | signed | 0.1 | 0 | Ah | -51.1 to 51.1 | -512 = `SNA` | plausible |
| `BMS_largestCacSpreadErrorLower` | page 64 | High-voltage battery management system: largest cac spread error lower; raw 4095 = signal not available (SNA) | 8\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_lifeModelAverageCac` | page 64 | High-voltage battery management system: life model average cac; raw 4095 = signal not available (SNA) | 20\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_lifeModelCacBrick1` | page 64 | High-voltage battery management system: life model cac brick1; raw 4095 = signal not available (SNA) | 32\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_lifeModelAverageOffset` | page 64 | High-voltage battery management system: life model average offset; raw 512 = signal not available (SNA) | 44\|10 | little-endian | signed | 0.1 | 0 | Ah | -51.1 to 51.1 | -512 = `SNA` | validated |
| `BMS_percentCacUpdatesInTimeWindow` | page 64 | High-voltage battery management system: percent cac updates in time window | 54\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `BMS_lifeModelMaxCacBrickId` | page 65 | High-voltage battery management system: life model max cac brick id; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 255 | 255 = `SNA` | validated |
| `BMS_lifeModelMaxCac` | page 65 | High-voltage battery management system: life model max cac; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_lifeModelMinCacBrickId` | page 65 | High-voltage battery management system: life model min cac brick id; raw 255 = signal not available (SNA) | 28\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 255 | 255 = `SNA` | validated |
| `BMS_lifeModelMinCac` | page 65 | High-voltage battery management system: life model min cac; raw 4095 = signal not available (SNA) | 36\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_restingPointCacAvg` | page 65 | High-voltage battery management system: resting point cac avg; raw 4095 = signal not available (SNA) | 48\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_cacEstimationSource` | page 65 | High-voltage battery management system: cac estimation source | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CAC_SOURCE_UNKNOWN`<br>1 = `CAC_SOURCE_RESTING_POINT_CAC`<br>2 = `CAC_SOURCE_LIFE_MODEL` | validated |
| `BMS_packCalibrationBirthDateBinned` | page 67 | High-voltage battery management system: pack calibration birth date binned | 26\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `BMS_synchronizedCacMaxRaw` | page 71 | High-voltage battery management system: synchronized cac max raw; raw 4095 = signal not available (SNA) | 8\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_synchronizedCacMinRaw` | page 71 | High-voltage battery management system: synchronized cac min raw; raw 4095 = signal not available (SNA) | 20\|12 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 409.4 | 4095 = `SNA` | validated |
| `BMS_largestSyncCacErrorStartSoc` | page 71 | Start SOC for CAC update from the brick with the highest synchronized CAC error | 32\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_largestSyncCacErrorEndSoc` | page 71 | Start SOC for CAC update from the brick with the highest synchronized CAC error | 42\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_runtimeSocConfigNvramValid` | page 71 | High-voltage battery management system: runtime soc config nvram valid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_runtimeSocCorrectionsEnabled` | page 71 | High-voltage battery management system: runtime soc corrections enabled | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_rubberBandingEnabled` | page 71 | Reports whether rubber banding of output energy corrections is enabled. | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_rubberBandingConfigNvramValid` | page 71 | High-voltage battery management system: rubber banding config nvram valid | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_runtimeSocMinTempForModel` | page 71 | High-voltage battery management system: runtime soc min temp for model | 56\|6 | little-endian | unsigned | 0.5 | 0 | DegC | 0 to 20 |  | validated |
| `BMS_energyBufferConfigNvramValid` | page 71 | High-voltage battery management system: energy buffer config nvram valid | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_thermalEvent1pDetectConfigDisabled` | page 71 | High-voltage battery management system: thermal event1p detect config disabled | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_sohEnergy` | page 79 | Battery SOH energy estimate. If calibrated SOH capacity is unavailable, this value is a filtered result from brick CACs; raw 2047 = signal not available (SNA) | 8\|11 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 204.6 | 2047 = `SNA` | validated |
| `BMS_fullCapacitySohEnergy` | page 79 | Energy estimate using nominal brick capacity at maximum SOC using SOH retention test conditions; raw 2047 = signal not available (SNA) | 19\|11 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 204.6 | 2047 = `SNA` | validated |
| `BMS_calibratedCapacitySohEnergy` | page 79 | Energy estimate using CAC from the most recent valid SOH test at maximum SOC using SOH retention test conditions; raw 2047 = signal not available (SNA) | 30\|11 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 204.6 | 2047 = `SNA` | validated |
| `BMS_estimatedCapacitySohEnergy` | page 79 | Energy estimate using filtered brick capacities at maximum SOC using SOH retention test conditions; raw 2047 = signal not available (SNA) | 41\|11 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 204.6 | 2047 = `SNA` | validated |
| `BMS_prevUserFacingSohEnergy` | page 79 | The last soh energy stored in NVM for rate limiting purposes; raw 2047 = signal not available (SNA) | 52\|11 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 204.6 | 2047 = `SNA` | validated |
| `BMS_stateOfHealthMinCac` | page 80 | Reports the minimum Calculated Amp-hour Capacity (CAC) by aged Open Circuit Voltage (OCV) raw values across bricks that could be used in State of Health (SOH) calculations; raw 8191 = signal not available (SNA) | 8\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819 | 8191 = `SNA` | validated |
| `BMS_lifeModelStorageLossPackAge` | page 80 | High-voltage battery management system: life model storage loss pack age; raw 16383 = signal not available (SNA) | 24\|14 | little-endian | unsigned | 1 | 0 | days | 0 to 16382 | 16383 = `SNA` | validated |
| `BMS_lifeModelThroughputDcrCycleCount` | page 80 | High-voltage battery management system: life model throughput dcr cycle count; raw 4095 = signal not available (SNA) | 38\|12 | little-endian | unsigned | 1 | 0 | Cycles | 0 to 4094 | 4095 = `SNA` | validated |
| `BMS_stateOfHealthMinCacLowerBound` | page 80 | Reports the minimum Calculated Amp-hour Capacity (CAC) by aged Open Circuit Voltage (OCV) raw lower bound values across bricks that could be used in State of Health (SOH) calculations; raw 8191 = signal not available (SNA) | 50\|13 | little-endian | unsigned | 0.1 | 0 | Ah | 0 to 819 | 8191 = `SNA` | validated |
| `BMS_energyWalkCounter` | page 83 | High-voltage battery management system: energy walk counter | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_energyWalkTimeoutCounter` | page 83 | High-voltage battery management system: energy walk timeout counter | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_dynamicCcvEnabled` | page 83 | High-voltage battery management system: dynamic ccv enabled | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_chargeTargetLookupSoc` | page 83 | High-voltage battery management system: charge target lookup soc | 25\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_stateOfHealth` | page 83 | Most recent battery capacity estimate, from a successful SOH test in %; raw 1023 = signal not available (SNA) | 35\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 | 1023 = `SNA` | validated |
| `BMS_avgShuntAsicCurrentOffset` | page 83 | High-voltage battery management system: avg shunt asic current offset; raw 16384 = signal not available (SNA) | 48\|15 | little-endian | signed | 0.2 | 0 | mA | -3276.6 to 3276.6 | -16384 = `SNA` | validated |
| `BMS_cellAttributesGeneralAttributes` | page 85 | High-voltage battery management system: cell attributes general attributes; raw 0 = signal not available (SNA) | 7\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `SNA` | validated |
| `BMS_cellAttributesPackManufacturingLocation` | page 85 | High-voltage battery management system: cell attributes pack manufacturing location; raw 0 = signal not available (SNA) | 39\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA` | validated |
| `BMS_cellAttributesRemanufacturedPack` | page 85 | High-voltage battery management system: cell attributes remanufactured pack | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cellAttributesConfigNvramValid` | page 85 | High-voltage battery management system: cell attributes config nvram valid | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cellAttributesCellType` | page 85 | High-voltage battery management system: cell attributes cell type; raw 0 = signal not available (SNA) | 44\|6 | little-endian | unsigned | 1 | 0 |  | 1 to 63 | 0 = `SNA` | validated |
| `BMS_cellAttributesAutocloseAndScrapPackOnFieldReturn` | page 85 | High-voltage battery management system: cell attributes autoclose and scrap pack on field return | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_cellAttributesShipPackForFailureAnalysis` | page 85 | High-voltage battery management system: cell attributes ship pack for failure analysis | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_lifeModelThroughputCycleCount` | page 85 | High-voltage battery management system: life model throughput cycle count; raw 4095 = signal not available (SNA) | 52\|12 | little-endian | unsigned | 1 | 0 | Cycles | 0 to 4094 | 4095 = `SNA` | validated |
| `BMS_limpChargeCurrentLimit` | page 89 | DC current limit based on limp mode; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 1 | 0 | A | 0 to 1022 | 1023 = `SNA` | validated |
| `BMS_energyRemainingDisplayError` | page 89 | High-voltage battery management system: energy remaining display error | 18\|10 | little-endian | signed | 0.1 | 0 | kWh | -50 to 50 |  | validated |
| `BMS_energyRemainingTDisplayError` | page 89 | High-voltage battery management system: energy remaining t display error | 28\|10 | little-endian | signed | 0.1 | 0 | kWh | -50 to 50 |  | validated |
| `BMS_numOfThermistors` | page 89 | Measures the number of thermistors in the battery pack for temperature monitoring. | 38\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `BMS_numOfBricks` | page 89 | Measures the number of battery bricks (modules or cell groups) in the pack. | 43\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_cellChargeDcCurrentLimit` | page 89 | DC current target based on cell voltage &amp; temp tables | 51\|12 | little-endian | unsigned | 0.5 | 0 | A | 0 to 2047.5 |  | validated |
| `BMS_socByDeltaVEnabled` | page 90 | High-voltage battery management system: soc by delta v enabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_socByDvMaxSocLimit` | page 90 | High-voltage battery management system: soc by dv max soc limit | 9\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socByDvVoltageChangeOverAh` | page 90 | High-voltage battery management system: soc by dv voltage change over ah | 19\|9 | little-endian | unsigned | 0.002 | 0 | V | 0 to 1 |  | validated |
| `BMS_socByDvMaxSocByAhCorrected` | page 90 | High-voltage battery management system: soc by dv max soc by ah corrected | 28\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socByDvMaxBrickVoltage` | page 90 | High-voltage battery management system: soc by dv max brick voltage | 40\|12 | little-endian | unsigned | 0.002 | 0 | V | 0 to 5 |  | validated |
| `BMS_socByDvMaxBrickId` | page 90 | High-voltage battery management system: soc by dv max brick id | 56\|8 | little-endian | unsigned | 1 | 1 |  | 1 to 256 |  | validated |
| `BMS_socByDvMaxSocByAhRaw` | page 91 | High-voltage battery management system: soc by dv max soc by ah raw | 8\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_voltageInstabilityExcessNoiseLog` | page 91 | High-voltage battery management system: voltage instability excess noise log | 18\|12 | little-endian | unsigned | 0.1 | 0 | counts | 0 to 408 |  | validated |
| `BMS_maxModelThermistorTempDelta` | page 91 | High-voltage battery management system: max model thermistor temp delta; raw 512 = signal not available (SNA) | 30\|10 | little-endian | signed | 0.1 | 0 | C | -51.2 to 51.1 | -512 = `SNA` | validated |
| `BMS_activeCoolCellTargetT` | page 91 | High-voltage battery management system: active cool cell target t | 40\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_cellTempTargetMode` | page 91 | Operating mode of the thermal controls for the Battery Management System (BMS) | 49\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DEFAULT`<br>1 = `LOW_POWER_CHARGE`<br>2 = `HIGH_POWER_CHARGE`<br>3 = `CONNECTED_PRECONDITION`<br>4 = `DISCONNECTED_PRECONDITION`<br>5 = `ACTIVE_HEAT_ON_NAV`<br>6 = `PASSIVE_HEAT_ON_NAV`<br>7 = `DRAGSTRIP`<br>8 = `SOH_HEAT_PACK`<br>9 = `ACTIVE_COOL_ON_NAV`<br>10 = `PASSIVE_COOL_ON_NAV`<br>11 = `V2X_SESSION` | validated |
| `BMS_minPackTempForChargeToStart` | page 91 | High-voltage battery management system: min pack temp for charge to start | 56\|7 | little-endian | unsigned | 0.5 | -40 | C | -40 to 23.5 |  | validated |

## Multiplexing

`BMS_log2MuxId` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 18 (8 signals), page 20 (10 signals), page 21 (9 signals), page 29 (1 signals), page 30 (5 signals), page 31 (3 signals), page 33 (6 signals), page 54 (6 signals), page 55 (5 signals), page 56 (4 signals), page 60 (2 signals), page 64 (5 signals), page 65 (6 signals), page 67 (1 signals), page 71 (11 signals), page 79 (5 signals), page 80 (4 signals), page 83 (6 signals), page 85 (8 signals), page 89 (6 signals), page 90 (6 signals), page 91 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
