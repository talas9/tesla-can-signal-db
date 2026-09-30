---
layout: default
title: "DAS_alertLog (0x5B9) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: alert log. Tesla Model 3 CAN bus message DAS_alertLog (0x5B9) of Driver assistance computer, firmware 2026.26.6.5, 25 signals (DAS_alertID, DAS_alertState, DAS_sw073_escalateLDWs, DAS_sw073_silentEscalatedLDW and 21 more). Bit layout, scaling, units and value tables."
---

# DAS_alertLog (0x5B9) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 25 signals of DAS_alertLog as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_alertLog` |
| CAN id | 0x5B9 (1465) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 25 |

## Signals of DAS_alertLog

Tesla Model 3 CAN bus signals in `DAS_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_alertID` | selector | Driver assistance computer: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>2 = `w002_ldwDisabled`<br>3 = `w003_isaDisabled`<br>4 = `w004_accDisabled`<br>5 = `w005_fcwCancelled`<br>6 = `w006_aebCancelled`<br>7 = `w007_ahlbDisabled`<br>8 = `w008_parkDisabled`<br>9 = `w009_aebFault`<br>10 = `w010_radcCalibIssue`<br>11 = `w011_scaEvent`<br>12 = `w012_Cam_BootFailure`<br>13 = `w013_Cam_Watchdog`<br>14 = `w014_swAssert`<br>15 = `w015_Camera_Failsafes`<br>16 = `w016_aeb_e_event`<br>17 = `w017_Cam_Msg_MIA`<br>18 = `w018_ECU_Power_Issue`<br>19 = `w019_ECU_Stack_Overflow`<br>20 = `w020_ECU_checkstopError`<br>21 = `w021_ECU_Temperature_Issue`<br>22 = `w022_ECU_EEPROM_Failure`<br>23 = `w023_ECU_Cam_Statemismatc`<br>24 = `w024_ECU_Watchdog_Reset`<br>25 = `w025_LC_Steering_Override`<br>26 = `w026_ECU_timingIssue`<br>27 = `w027_ECU_Reset_Fault`<br>28 = `w028_spi_rx_error`<br>29 = `w029_spi_tx_error`<br>30 = `w030_Heater_Issue`<br>31 = `w031_canRxError`<br>32 = `w032_canTxError`<br>33 = `w033_gtwMia`<br>34 = `w034_sccmMia`<br>35 = `w035_espMia`<br>36 = `w036_bdyMia`<br>37 = `w037_camTacIssue`<br>38 = `w038_camFailure`<br>39 = `w039_sdm_rcm_Mia`<br>40 = `w040_autopilotAngleSaturated`<br>41 = `w041_autopilotRateSaturated`<br>42 = `w042_autopilotAborting`<br>43 = `w043_camLongRunTime`<br>44 = `w044_appMobileyeFailure`<br>45 = `w045_radMia`<br>46 = `w046_eepromRecordAbsent`<br>47 = `w047_edrEvent`<br>48 = `w048_DAS_Features_Disabled`<br>49 = `w049_eyeqVersionMismatch`<br>50 = `w050_aeb_event`<br>51 = `w051_radcEcuIssue`<br>52 = `w052_radcSensorIssue`<br>53 = `w053_radcCommIssue`<br>54 = `w054_camAutofix`<br>55 = `w055_radcVersionMismatch`<br>56 = `w056_diMia`<br>57 = `w057_mcuMia`<br>58 = `w058_epbMia`<br>59 = `w059_parkMia`<br>60 = `w060_fcw_event`<br>61 = `w061_airSuspensionMia`<br>62 = `w062_radcAlignment`<br>63 = `w063_parkVersionMismatch`<br>64 = `w064_epasMia`<br>65 = `w065_deserializerOvercurrent`<br>66 = `w066_deserializerLockLost`<br>67 = `w067_steeringAlignment`<br>68 = `w068_vlInconsistency`<br>69 = `w069_apcSpaceMasked`<br>70 = `w070_apcIncompleteCal`<br>71 = `w071_selfparkStarted`<br>72 = `w072_selfparkComplete`<br>73 = `w073_issueEscalatedLDW`<br>74 = `w074_inPathStationaryObst`<br>75 = `w075_scMia`<br>76 = `w076_mobilEyeSetC`<br>77 = `w077_pmmActive`<br>78 = `w078_pmmActive2`<br>79 = `w079_edrAvailable`<br>80 = `w080_accFailedActivation`<br>81 = `w081_pmmActiveBraking`<br>82 = `w082_inPathFSviolation`<br>83 = `w083_inPathRADObject`<br>84 = `w084_pmmIPSO`<br>85 = `w085_pmmSteering`<br>86 = `w086_robCollision`<br>87 = `w087_DEPRECATED`<br>88 = `w088_DEPRECATED`<br>89 = `w089_DEPRECATED`<br>90 = `w090_DEPRECATED`<br>91 = `w091_DEPRECATED`<br>92 = `w092_DEPRECATED`<br>93 = `w093_DEPRECATED`<br>94 = `w094_DEPRECATED`<br>95 = `w095_DEPRECATED`<br>96 = `w096_DEPRECATED`<br>97 = `w097_DEPRECATED`<br>98 = `w098_DEPRECATED`<br>99 = `w099_DEPRECATED`<br>100 = `w100_DEPRECATED`<br>101 = `w101_DEPRECATED`<br>102 = `w102_DEPRECATED`<br>103 = `w103_robExperimentalAEB`<br>104 = `w104_DEPRECATED`<br>105 = `w105_DEPRECATED`<br>106 = `w106_torsionBarCalibrated`<br>129 = `w129_mainCamExtNotCal`<br>130 = `w130_narrowCamExtNotCal`<br>131 = `w131_mainCamCalSaved`<br>132 = `w132_narrowCamCalSaved`<br>133 = `w133_mainCamInitFault`<br>134 = `w134_narrowCamInitFault`<br>135 = `w135_fisheyeCamInitFault`<br>136 = `w136_lPillarCamInitFault`<br>137 = `w137_rPillarCamInitFault`<br>138 = `w138_lRepeatCamInitFault`<br>139 = `w139_rRepeatCamInitFault`<br>140 = `w140_backupCamInitFault`<br>141 = `w141_ECU_Thermal_Issue`<br>142 = `w142_fwdCamPitchProblem`<br>143 = `w143_IDF_event`<br>144 = `w144_selfieCamInitFault`<br>171 = `w171_fisheyeCamExtNotCal`<br>172 = `w172_lPillarCamExtNotCal`<br>173 = `w173_rPillarCamExtNotCal`<br>174 = `w174_lRepeatCamExtNotCal`<br>175 = `w175_rRepeatCamExtNotCal`<br>177 = `w177_fisheyeCamCalSaved`<br>178 = `w178_lPillarCamCalSaved`<br>179 = `w179_rPillarCamCalSaved`<br>180 = `w180_lRepeatCamCalSaved`<br>181 = `w181_rRepeatCamCalSaved`<br>193 = `w193_camWindshieldUnclean`<br>194 = `w194_accDriverResumeRqrd`<br>195 = `w195_scwUnavailable`<br>196 = `w196_stopSignWarning`<br>197 = `w197_redLightWarning`<br>198 = `w198_tsrUnavailable`<br>199 = `w199_apcAbort`<br>200 = `w200_lcSlowdown`<br>201 = `w201_lcAborting`<br>202 = `w202_scwNoisyEnvironment`<br>203 = `w203_apcActivation`<br>204 = `w204_apcFinalFront`<br>205 = `w205_apcFinalRear`<br>206 = `w206_autosteerNotEnabled`<br>207 = `w207_autosteerUnavailable`<br>208 = `w208_rackDetected`<br>209 = `w209_autoSummonRequest`<br>210 = `w210_camObstrcted`<br>211 = `w211_accNoSeatBelt`<br>212 = `w212_lcUnavailableStrikeOut`<br>213 = `w213_autosteerStruckOut`<br>214 = `w214_driverNotIntracting`<br>215 = `w215_contDriverNotIntracting`<br>216 = `w216_driverOverriding`<br>217 = `w217_lcUnavailableSpeeding`<br>218 = `w218_lcSpeedExceededLimit`<br>219 = `w219_lcTempUnavailableSpeed`<br>220 = `w220_lcTempUnavailableRoad`<br>221 = `w221_accRadarBlind`<br>222 = `w222_accCameraBlind`<br>223 = `w223_accObjectInPath`<br>224 = `w224_accCameraCalibration`<br>225 = `w225_lcDegradedVisSpeedLmt`<br>226 = `w226_lcCamCalNeededSpeedLmt`<br>227 = `w227_virtualWallBlocked`<br>228 = `w228_DEPRECATED`<br>229 = `w229_alcUltrasoundDamaged`<br>230 = `w230_alcUltrasoundBlocked`<br>231 = `w231_idfEvent`<br>232 = `w232_laneChangeRequested` | plausible |
| `DAS_alertState` |  | Driver assistance computer: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `DAS_sw073_escalateLDWs` | page 73 | Driver assistance computer: sw073 escalate LD ws | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw073_silentEscalatedLDW` | page 73 | Driver assistance computer: sw073 silent escalated LDW | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw073_escalateLDWreason` | page 73 | Driver assistance computer: sw073 escalate LD wreason | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `SINGLE_PULL`<br>2 = `DOUBLE_PULL`<br>3 = `STW_TAKEOVER`<br>4 = `SELFIE` | plausible |
| `DAS_sw073_rawMobileyeLDW` | page 73 | Driver assistance computer: sw073 raw mobileye LDW | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `DAS_sw073_freespaceLDW` | page 73 | Driver assistance computer: sw073 freespace LDW | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `DAS_sw073_freespaceLeftC0` | page 73 | Driver assistance computer: sw073 freespace left C0 | 26\|7 | little-endian | unsigned | 0.2 | -12.8 | m | -12.8 to 12.6 |  | plausible |
| `DAS_sw073_freespaceRightC0` | page 73 | Driver assistance computer: sw073 freespace right C0 | 33\|7 | little-endian | unsigned | 0.2 | -12.8 | m | -12.8 to 12.6 |  | plausible |
| `DAS_sw073_freespaceLeftC1` | page 73 | Driver assistance computer: sw073 freespace left C1 | 40\|8 | little-endian | unsigned | 0.0016 | -0.2 | rad | -0.2 to 0.208 |  | plausible |
| `DAS_sw073_freespaceRightC1` | page 73 | Driver assistance computer: sw073 freespace right C1 | 48\|8 | little-endian | unsigned | 0.0016 | -0.2 | rad | -0.2 to 0.208 |  | plausible |
| `DAS_sw073_freespaceLeftFarZ` | page 73 | Driver assistance computer: sw073 freespace left far z | 56\|4 | little-endian | unsigned | 4 | 0 | m | 0 to 60 |  | plausible |
| `DAS_sw073_freespaceRightFarZ` | page 73 | Driver assistance computer: sw073 freespace right far z | 60\|4 | little-endian | unsigned | 4 | 0 | m | 0 to 60 |  | plausible |
| `DAS_sw230_sensor1Blocked` | page 230 | Driver assistance computer: sw230 sensor1 blocked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor2Blocked` | page 230 | Driver assistance computer: sw230 sensor2 blocked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor3Blocked` | page 230 | Driver assistance computer: sw230 sensor3 blocked | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor4Blocked` | page 230 | Driver assistance computer: sw230 sensor4 blocked | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor5Blocked` | page 230 | Driver assistance computer: sw230 sensor5 blocked | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor6Blocked` | page 230 | Driver assistance computer: sw230 sensor6 blocked | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor7Blocked` | page 230 | Driver assistance computer: sw230 sensor7 blocked | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor8Blocked` | page 230 | Driver assistance computer: sw230 sensor8 blocked | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor9Blocked` | page 230 | Driver assistance computer: sw230 sensor9 blocked | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor10Blocked` | page 230 | Driver assistance computer: sw230 sensor10 blocked | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor11Blocked` | page 230 | Driver assistance computer: sw230 sensor11 blocked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_sw230_sensor12Blocked` | page 230 | Driver assistance computer: sw230 sensor12 blocked | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`DAS_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 73 (11 signals), page 230 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
