---
layout: default
title: "EPAS3S_alertLog (0x591) — Electric power steering (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Electric power steering (secondary) message: alert log. Tesla Model 3 / Model Y CAN bus message EPAS3S_alertLog (0x591) of Electric power steering (secondary), firmware 2026.26.6.5, 35 signals (EPAS3S_alertID, EPAS3S_alertState, EPAS3S_a147_transitionReason, EPAS3S_a149_pcbTemp and 31 more). Bit layout, scaling, units and value tables."
---

# EPAS3S_alertLog (0x591) — Electric power steering (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Electric power steering (secondary) message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 35 signals of EPAS3S_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3S_alertLog` |
| CAN id | 0x591 (1425) |
| ECU | [Electric power steering (secondary)](../../epas3s.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | EPAS3S |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 35 |

## Signals of EPAS3S_alertLog

Tesla Model 3 / Model Y CAN bus signals in `EPAS3S_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3S_alertID` | selector | Electric power steering (secondary): alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_sent1Mia`<br>2 = `a002_sent1Error`<br>3 = `a003_trqSens1Supply`<br>4 = `a004_trqSens1Eeprom`<br>5 = `a005_sent2Mia`<br>6 = `a006_sent2Error`<br>7 = `a007_trqSens2Supply`<br>8 = `a008_trqSens2Eeprom`<br>9 = `a009_sentDiff`<br>10 = `a010_trqSensCalError`<br>11 = `a011_currentSensError`<br>12 = `a012_currentSensCalError`<br>13 = `a013_gateDriveError`<br>14 = `a014_gateDriveTxError`<br>15 = `a015_gateDriveEeprom`<br>16 = `a016_phaseUhighUv`<br>17 = `a017_phaseUlowUv`<br>18 = `a018_phaseVhighUv`<br>19 = `a019_phaseVlowUv`<br>20 = `a020_phaseWhighUv`<br>21 = `a021_phaseWlowUv`<br>22 = `a022_phaseUhighOv`<br>23 = `a023_phaseUlowOv`<br>24 = `a024_phaseVhighOv`<br>25 = `a025_phaseVlowOv`<br>26 = `a026_phaseWhighOv`<br>27 = `a027_phaseWlowOv`<br>28 = `a028_phaseUbootUv`<br>29 = `a029_phaseVbootUv`<br>30 = `a030_phaseWbootUv`<br>31 = `a031_abnormalShutdown`<br>32 = `a032_vRegOutputUv`<br>33 = `a033_vRegOutputOv`<br>34 = `a034_vRegError`<br>35 = `a035_vbbSupplyUv`<br>36 = `a036_vbbSupplyOv`<br>37 = `a037_motPos1ParityError`<br>38 = `a038_motPos1Uv`<br>39 = `a039_motPos1MagnetMia`<br>40 = `a040_motPos1LogicError`<br>41 = `a041_motPos1tempError`<br>42 = `a042_motPos2ParityError`<br>43 = `a043_motPos2Uv`<br>44 = `a044_motPos2MagnetMia`<br>45 = `a045_motPos2LogicError`<br>46 = `a046_motPos2tempError`<br>47 = `a047_motPosCorrError`<br>48 = `a048_motPosCalError`<br>49 = `a049_piCtrlError`<br>50 = `a050_mcuSmuError`<br>51 = `a051_mcuSupError`<br>52 = `a052_intWatchdogError`<br>53 = `a053_extWatchdogError`<br>54 = `a054_memoryProtectError`<br>55 = `a055_floatPointError`<br>56 = `a056_battUv`<br>57 = `a057_battUvReduced`<br>58 = `a058_battOv`<br>59 = `a059_battOvReduced`<br>60 = `a060_battBridgeDiff`<br>61 = `a061_bridgeUv`<br>62 = `a062_assistCorrError`<br>63 = `a063_dampCorrError`<br>64 = `a064_phaseCompCorrError`<br>65 = `a065_trqTarCorrError`<br>66 = `a066_returnCorrError`<br>67 = `a067_yawDampCorrError`<br>68 = `a068_hystCorrError`<br>69 = `a069_eacCorrError`<br>70 = `a070_hodCorrError`<br>71 = `a071_vehSpdCorrError`<br>72 = `a072_motFeedFwdError`<br>73 = `a073_motParEstError`<br>74 = `a074_overHeatProtect`<br>75 = `a075_fspPwrCut`<br>76 = `a076_tempSensOutofRange`<br>77 = `a077_highSideFetError`<br>78 = `a078_phaseDisconnectError`<br>79 = `a079_backupCurrentPlaus`<br>80 = `a080_ecuInitArbError`<br>81 = `a081_coggCompError`<br>82 = `a082_polarityCalError`<br>83 = `a083_crcMismatch`<br>84 = `a084_eacCancelled`<br>85 = `a085_canBusOff`<br>86 = `a086_dasMia`<br>87 = `a087_dasCntError`<br>88 = `a088_dasCsError`<br>89 = `a089_espWsMia`<br>90 = `a090_espWsCntError`<br>91 = `a091_espWsCsError`<br>92 = `a092_espWrMia`<br>93 = `a093_espWrCntError`<br>94 = `a094_espWrCsError`<br>95 = `a095_espWsStatus`<br>96 = `a096_rcmMia`<br>97 = `a097_rcmCntError`<br>98 = `a098_rcmCsError`<br>99 = `a099_yawRateStatus`<br>100 = `a100_diMia`<br>101 = `a101_diCntError`<br>102 = `a102_diCsError`<br>103 = `a103_vcFrontMia`<br>104 = `a104_vcFrontCntError`<br>105 = `a105_vcFrontCsError`<br>106 = `a106_vcFrontTempMia`<br>107 = `a107_uiTuneReqMia`<br>108 = `a108_uiTuneReqCntError`<br>109 = `a109_uiTuneReqCsError`<br>110 = `a110_sasMia`<br>111 = `a111_sasCntError`<br>112 = `a112_sasCsError`<br>113 = `a113_sasStatusError`<br>114 = `a114_gtwConfigMia`<br>115 = `a115_ecuStatMia`<br>116 = `a116_ecuStatCntError`<br>117 = `a117_ecuStatCrcError`<br>118 = `a118_privateBusOff`<br>119 = `a119_pvtEcuStatMia`<br>120 = `a120_pvtEcuStatCntError`<br>121 = `a121_pvtEcuStatCrcError`<br>122 = `a122_olpActive`<br>123 = `a123_combEcu2StatFail`<br>124 = `a124_tempSensStuckInRange`<br>125 = `a125_trqSensTrimOutRange`<br>126 = `a126_apsMia`<br>127 = `a127_apsCntError`<br>128 = `a128_apsCsError`<br>129 = `a129_combEcu1StatFail`<br>130 = `a130_sasOffsetNotCal`<br>131 = `a131_phaseFeedbackError`<br>132 = `a132_motFeedFwdCounter25`<br>133 = `a133_motFeedFwdCounter50`<br>134 = `a134_motFeedFwdCounter85`<br>135 = `a135_piCtrlCounter25`<br>136 = `a136_piCtrlCounter50`<br>137 = `a137_piCtrlCounter85`<br>144 = `a144_diSpdMia`<br>145 = `a145_diSpdCntError`<br>146 = `a146_diSpdCsError`<br>147 = `a147_backupVehSpeed`<br>148 = `a148_vMaxAssist`<br>149 = `a149_currentSensPathSwitch`<br>150 = `a150_currentSensOffsetDetect`<br>151 = `a151_dcsCboot`<br>152 = `a152_dcsDiagReg`<br>153 = `a153_dcsInitOffset`<br>154 = `a154_assistTorqueDisabled`<br>155 = `a155_backupEacActive`<br>156 = `a156_angleSensorDivergence`<br>157 = `a157_pmState2Mia`<br>158 = `a158_pmState2CntError`<br>159 = `a159_pmState2CsError`<br>160 = `a160_latentFaultTestResult`<br>161 = `a161_initTestPhaDisconnInfo`<br>162 = `a162_initTestHSDFetInfo`<br>163 = `a163_initTestGateDrvrInfo`<br>164 = `a164_initTestDCSInfo`<br>165 = `a165_epbStatusMia`<br>166 = `a166_epbStatusCntError`<br>167 = `a167_epbStatusCsError`<br>168 = `a168_torsionBarTorqueQfDegraded` | plausible |
| `EPAS3S_alertState` |  | Electric power steering (secondary): alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `EPAS3S_a147_transitionReason` | page 147 | Electric power steering (secondary): a147 transition reason | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DATA_INTEGRITY`<br>1 = `WSS_FAILURE`<br>2 = `MIA` | plausible |
| `EPAS3S_a149_pcbTemp` | page 149 | Electric power steering (secondary): a149 pcb temp | 16\|8 | little-endian | signed | 1 | 60 | degC | -68 to 187 |  | plausible |
| `EPAS3S_a150_pcbTemp` | page 150 | Electric power steering (secondary): a150 pcb temp | 16\|8 | little-endian | signed | 1 | 60 | degC | -68 to 187 |  | plausible |
| `EPAS3S_a150_phaUMainPathCalcDiff` | page 150 | Electric power steering (secondary): a150 pha u main path calc diff | 24\|15 | little-endian | unsigned | 1 | 0 | Counts | 0 to 32767 |  | plausible |
| `EPAS3S_a150_phaVMainPathCalcDiff` | page 150 | Electric power steering (secondary): a150 pha v main path calc diff | 39\|15 | little-endian | unsigned | 1 | 0 | Counts | 0 to 32767 |  | plausible |
| `EPAS3S_a150_otherECUAssistStatusFlag` | page 150 | Electric power steering (secondary): a150 other ECU assist status flag | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a155_vehicleSpeed` | page 155 | Electric power steering (secondary): a155 vehicle speed | 16\|10 | little-endian | unsigned | 0.5 | 0 | kph | 0 to 511.5 |  | plausible |
| `EPAS3S_a156_vehicleSpeed` | page 156 | Electric power steering (secondary): a156 vehicle speed | 16\|10 | little-endian | unsigned | 0.5 | 0 | kph | 0 to 511.5 |  | plausible |
| `EPAS3S_a160_currentSensorStatus` | page 160 | Electric power steering (secondary): a160 current sensor status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_ISSUE`<br>1 = `PROBABLE_FAILURE`<br>2 = `STATUS_UNKNOWN` | plausible |
| `EPAS3S_a160_gateDriverStatus` | page 160 | Electric power steering (secondary): a160 gate driver status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_ISSUE`<br>1 = `PROBABLE_FAILURE`<br>2 = `STATUS_UNKNOWN` | plausible |
| `EPAS3S_a160_highSideDisconnectFetStatus` | page 160 | Electric power steering (secondary): a160 high side disconnect fet status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_ISSUE`<br>1 = `PROBABLE_FAILURE`<br>2 = `STATUS_UNKNOWN` | plausible |
| `EPAS3S_a160_phaseDisconnectFetStatus` | page 160 | Electric power steering (secondary): a160 phase disconnect fet status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_ISSUE`<br>1 = `PROBABLE_FAILURE`<br>2 = `STATUS_UNKNOWN` | plausible |
| `EPAS3S_a160_inverterFetStatus` | page 160 | Electric power steering (secondary): a160 inverter fet status | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_ISSUE`<br>1 = `PROBABLE_FAILURE`<br>2 = `STATUS_UNKNOWN` | plausible |
| `EPAS3S_a160_hsdFetFailShortTest` | page 160 | Electric power steering (secondary): a160 hsd fet fail short test | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASS`<br>1 = `FAIL`<br>2 = `NOT_RAN` | plausible |
| `EPAS3S_a160_phaDisconnFailOpenTest` | page 160 | Electric power steering (secondary): a160 pha disconn fail open test | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASS`<br>1 = `FAIL`<br>2 = `NOT_RAN` | plausible |
| `EPAS3S_a160_phaDisconnFailShortTest` | page 160 | Electric power steering (secondary): a160 pha disconn fail short test | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASS`<br>1 = `FAIL`<br>2 = `NOT_RAN` | plausible |
| `EPAS3S_a160_invFetInitTest` | page 160 | Electric power steering (secondary): a160 inv fet init test | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASS`<br>1 = `FAIL`<br>2 = `NOT_RAN` | plausible |
| `EPAS3S_a160_gateDrvrInitTest` | page 160 | Electric power steering (secondary): a160 gate drvr init test | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PASS`<br>1 = `FAIL`<br>2 = `NOT_RAN` | plausible |
| `EPAS3S_a160_latentFaultTestTimeout` | page 160 | Electric power steering (secondary): a160 latent fault test timeout | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a161_pcoMinPhaseBCurrent` | page 161 | Electric power steering (secondary): a161 pco min phase b current | 16\|12 | little-endian | signed | 0.1025 | 0 | Amps | -209.92 to 209.8175 |  | plausible |
| `EPAS3S_a161_pcoMaxPhaseBCurrent` | page 161 | Electric power steering (secondary): a161 pco max phase b current | 28\|12 | little-endian | signed | 0.1025 | 0 | Amps | -209.92 to 209.8175 |  | plausible |
| `EPAS3S_a161_pcoMinPhaseACurrent` | page 161 | Electric power steering (secondary): a161 pco min phase a current | 40\|12 | little-endian | signed | 0.1025 | 0 | Amps | -209.92 to 209.8175 |  | plausible |
| `EPAS3S_a161_pcoMaxPhaseACurrent` | page 161 | Electric power steering (secondary): a161 pco max phase a current | 52\|12 | little-endian | signed | 0.1025 | 0 | Amps | -209.92 to 209.8175 |  | plausible |
| `EPAS3S_a162_vBridgeClosed` | page 162 | Electric power steering (secondary): a162 v bridge closed | 16\|16 | little-endian | unsigned | 0.00537 | 0 | Volts | 0 to 351.92295 |  | plausible |
| `EPAS3S_a162_vBridgeOpen` | page 162 | Electric power steering (secondary): a162 v bridge open | 32\|16 | little-endian | unsigned | 0.00537 | 0 | Volts | 0 to 351.92295 |  | plausible |
| `EPAS3S_a163_gateDrvrStatusReg` | page 163 | Electric power steering (secondary): a163 gate drvr status reg | 16\|11 | little-endian | unsigned | 1 | 0 | Counts | 0 to 2047 |  | plausible |
| `EPAS3S_a163_gateDrvrDiag2Reg` | page 163 | Electric power steering (secondary): a163 gate drvr diag2 reg | 27\|9 | little-endian | unsigned | 1 | 0 | Counts | 0 to 511 |  | plausible |
| `EPAS3S_a163_gateDrvrDiag1Reg` | page 163 | Electric power steering (secondary): a163 gate drvr diag1 reg | 36\|9 | little-endian | unsigned | 1 | 0 | Counts | 0 to 511 |  | plausible |
| `EPAS3S_a163_gateDrvrDiag0Reg` | page 163 | Electric power steering (secondary): a163 gate drvr diag0 reg | 45\|9 | little-endian | unsigned | 1 | 0 | Counts | 0 to 511 |  | plausible |
| `EPAS3S_a163_diagStatus` | page 163 | Electric power steering (secondary): a163 diag status | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a163_powerStatus` | page 163 | Electric power steering (secondary): a163 power status | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a164_dcsRegister0x19` | page 164 | Electric power steering (secondary): a164 dcs register0x19 | 16\|16 | little-endian | unsigned | 1 | 0 | Counts | 0 to 65535 |  | plausible |
| `EPAS3S_a164_currentSensorRailed` | page 164 | Electric power steering (secondary): a164 current sensor railed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`EPAS3S_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 147 (1 signals), page 149 (1 signals), page 150 (4 signals), page 155 (1 signals), page 156 (1 signals), page 160 (11 signals), page 161 (4 signals), page 162 (2 signals), page 163 (6 signals), page 164 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Electric power steering (secondary) messages (EPAS3S)](../../epas3s.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
