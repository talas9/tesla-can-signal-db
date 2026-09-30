---
layout: default
title: "DIF_alertLog (0x526) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front drive inverter message: alert log. Tesla Model 3 / Model Y CAN bus message DIF_alertLog (0x526) of Front drive inverter, firmware 2026.26.6.5, 580 signals (DIF_alertID, DIF_alertState, DIF_a001_thermalWarning_H, DIF_a001_thermalShutdown_H and 576 more). Bit layout, scaling, units and value tables."
---

# DIF_alertLog (0x526) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front drive inverter message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 580 signals of DIF_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_alertLog` |
| CAN id | 0x526 (1318) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 580 |

## Signals of DIF_alertLog

Tesla Model 3 / Model Y CAN bus signals in `DIF_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_alertID` | selector | Front drive inverter: alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_hwPhaseAgateDrive`<br>2 = `a002_hwPhaseBgateDrive`<br>3 = `a003_hwPhaseCgateDrive`<br>4 = `a004_hwPhaseApeak`<br>5 = `a005_hwPhaseBpeak`<br>6 = `a006_hwPhaseCpeak`<br>7 = `a007_statorAnomalyDetected`<br>8 = `a008_hwEncoderA`<br>9 = `a009_hwEncoderB`<br>10 = `a010_unintendedReset`<br>11 = `a011_swPowerStageNotReady`<br>12 = `a012_hvilNotClosed`<br>13 = `a013_eccError`<br>14 = `a014_activeDamping`<br>15 = `a015_mechSafeStateAnomaly`<br>16 = `a016_safeStateApplied`<br>17 = `a017_hwPedalMonitor`<br>18 = `a018_hwLVSupplyUV`<br>20 = `a020_hwMotorEncoder`<br>21 = `a021_hwBusOV`<br>22 = `a022_hw5vSupplyUV`<br>24 = `a024_selfTest`<br>25 = `a025_phaseApeak`<br>26 = `a026_phaseBpeak`<br>27 = `a027_phaseCpeak`<br>28 = `a028_phaseArms`<br>29 = `a029_phaseBrms`<br>30 = `a030_phaseCrms`<br>31 = `a031_phaseAcurrentOffset`<br>32 = `a032_phaseBcurrentOffset`<br>33 = `a033_phaseAcurrentSensor`<br>34 = `a034_phaseBcurrentSensor`<br>35 = `a035_phaseCurrentBalance`<br>36 = `a036_busOV`<br>37 = `a037_busUV`<br>38 = `a038_busVsensor`<br>39 = `a039_exceptionUndefinedInstruction`<br>40 = `a040_difMIA`<br>41 = `a041_sdcMIA`<br>42 = `a042_inletSensor`<br>43 = `a043_outletOT`<br>44 = `a044_outletUT`<br>45 = `a045_outletSensor`<br>46 = `a046_statorOT`<br>47 = `a047_statorSensor1`<br>48 = `a048_statorSensor2`<br>49 = `a049_statorSensorDiff`<br>50 = `a050_noStatorSensor`<br>52 = `a052_dirMIA`<br>53 = `a053_unexpectedLatchState`<br>54 = `a054_driveInverterOT`<br>55 = `a055_trqCrossCheck`<br>56 = `a056_ambientOT`<br>57 = `a057_ambientUT`<br>58 = `a058_ambientSensor`<br>59 = `a059_heatsinkOT`<br>60 = `a060_heatsinkUT`<br>61 = `a061_heatsinkSensor`<br>62 = `a062_systemLimpMode`<br>63 = `a063_bbMIA`<br>64 = `a064_torqueIntervention`<br>65 = `a065_canHardwareBusB`<br>66 = `a066_canDataBusB`<br>67 = `a067_canOverrunBusB`<br>69 = `a069_rotorTempLimit`<br>70 = `a070_udsTransactionInitiated`<br>71 = `a071_busDisconnected`<br>72 = `a072_gateDriveFaultCounter`<br>73 = `a073_motorSpeed`<br>74 = `a074_motorEncoder`<br>75 = `a075_motorSpeedMismatch`<br>76 = `a076_lvSupplyOV`<br>77 = `a077_lvSupplyUV`<br>78 = `a078_adcRefLow`<br>79 = `a079_adcRefHigh`<br>84 = `a084_eccTestData0`<br>85 = `d085_driveInverterBoardFailure`<br>86 = `a086_activeDischargeOn`<br>87 = `a087_gtwMIA`<br>88 = `a088_uiMIA`<br>89 = `d089_invalidTorqueCommand`<br>90 = `a090_pmMIA`<br>91 = `a091_espMIA`<br>92 = `a092_bmsMIA`<br>93 = `a093_canHardwareBusA`<br>94 = `a094_canDataBusA`<br>95 = `a095_canOverrunBusA`<br>96 = `a096_memoryError`<br>97 = `a097_eepromError`<br>98 = `a098_intTimeTooLong`<br>99 = `a099_threadOverrun`<br>100 = `a100_assertion`<br>101 = `a101_eccTestData1`<br>102 = `a102_exceptionPrefetchAbort`<br>103 = `a103_lowFlow`<br>104 = `d104_resetUnintended`<br>105 = `d105_busVoltageSensorIssue`<br>106 = `a106_idleTaskStarving`<br>107 = `a107_fpgaError`<br>108 = `a108_stateTrans`<br>109 = `a109_ahbWriteError`<br>110 = `a110_brakeMIA`<br>111 = `a111_badPhaseSensorCalib`<br>112 = `a112_noPhaseCurrent`<br>113 = `a113_noFuncHeatsinkSensor`<br>114 = `a114_exceptionDataAbort`<br>115 = `a115_exceptionDataAbort2`<br>116 = `a116_highSpeedWearCounter`<br>117 = `a117_diMIA`<br>118 = `d118_oilPumpCommsLost`<br>119 = `a119_hvpMIA`<br>120 = `a120_hvlinkMIA`<br>121 = `a121_motorControlRegulation`<br>122 = `a122_highStackUsage`<br>123 = `a123_lossMotorControl`<br>124 = `d124_oilPumpServiceRequired`<br>125 = `d125_currentSensorIssue`<br>126 = `a126_limpMode`<br>127 = `a127_gracefulPowerOff`<br>128 = `a128_fpgaVersionMismatch`<br>129 = `d129_oilPumpIssue`<br>130 = `d130_positionSensorIssue`<br>131 = `d131_currentSensorOffset`<br>132 = `d132_busUVIssue`<br>133 = `a133_capacitorOT`<br>134 = `a134_wheelSpeedIrrational`<br>135 = `d135_rotatedStator`<br>136 = `a136_spiError`<br>137 = `d137_currentSensorOutOfRange`<br>138 = `d138_inverterLVPowerSupplyLow`<br>141 = `d141_coolingSystemIssue`<br>142 = `a142_highLashAngle`<br>143 = `d143_wheelSpeedCorrelationIssue`<br>144 = `a144_configMismatch`<br>147 = `a147_highTorqueWearLimit`<br>148 = `a148_burnInCycleEnded`<br>149 = `a149_oilPumpFailure`<br>150 = `a150_busVD`<br>151 = `a151_shockTorqueLimiter`<br>152 = `a152_linError`<br>153 = `a153_oilPumpDiagnostics`<br>154 = `a154_resolver`<br>155 = `a155_vcfrontMIA`<br>156 = `a156_currentObserver`<br>157 = `a157_rcmMIA`<br>158 = `a158_ibstMIA`<br>160 = `a160_busVoltageAnomaly`<br>161 = `a161_epas3pMIA`<br>162 = `a162_endOfLifetimeBurnIn`<br>163 = `d163_recoverableOvercurrent`<br>164 = `d164_firmwareConfigMismatch`<br>165 = `d165_statorOverTemperature`<br>166 = `d166_rotorOverTemperature`<br>167 = `d167_tempSensorIssue`<br>168 = `d168_clutchPerformance`<br>169 = `d169_clutchPosition`<br>170 = `d170_clutchFailure`<br>172 = `a172_statorOilTempOT`<br>173 = `a173_ascFdbkDiagnostic`<br>174 = `a174_unitMayNotRestart`<br>176 = `a176_safetyICFault`<br>177 = `a177_fluxReferenceCorrected`<br>202 = `a202_excessHeatUnavailable`<br>225 = `a225_tmpEstPlausibility`<br>229 = `a229_busVsensorOverCAN`<br>233 = `a233_diMsgMissed`<br>234 = `a234_pcsMIA`<br>236 = `a236_tasMIA`<br>240 = `a240_clearFusesRoutine`<br>241 = `a241_systemThermallyLimited`<br>242 = `a242_spinDownLearning`<br>243 = `a243_ecuLogAvailable`<br>244 = `a244_mechSafeStateApplied`<br>245 = `a245_mechSafeStatePreWarn`<br>246 = `a246_recoveryAtSpeedError`<br>247 = `a247_rotorOffsetError`<br>249 = `a249_highStatorTempFromResist`<br>250 = `a250_preregulatorRail`<br>251 = `a251_oilPumpService`<br>252 = `a252_currentCoreFallback`<br>253 = `a253_lvBoostedRail`<br>254 = `a254_activeDischargeRail`<br>255 = `a255_currentGainFallback` | plausible |
| `DIF_alertState` |  | Front drive inverter: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `DIF_a001_thermalWarning_H` | page 1 | Front drive inverter: a001 thermal warning h | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_thermalShutdown_H` | page 1 | Front drive inverter: a001 thermal shutdown h | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVL_H` | page 1 | Front drive inverter: a001 undervolt VL h | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVH_H` | page 1 | Front drive inverter: a001 undervolt VH h | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_sense_H` | page 1 | Front drive inverter: a001 sense h | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_desat_H` | page 1 | Front drive inverter: a001 desat h | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVL_H` | page 1 | Front drive inverter: a001 overvolt VL h | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVH_H` | page 1 | Front drive inverter: a001 overvolt VH h | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVCC_H` | page 1 | Front drive inverter: a001 undervolt VCC h | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_asynchStop_H` | page 1 | Front drive inverter: a001 asynch stop h | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_remoteRegError_H` | page 1 | Front drive inverter: a001 remote reg error h | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVDD_H` | page 1 | Front drive inverter: a001 undervolt VDD h | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVDD_H` | page 1 | Front drive inverter: a001 overvolt VDD h | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localRegError_H` | page 1 | Front drive inverter: a001 local reg error h | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_spiError_H` | page 1 | Front drive inverter: a001 spi error h | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_deadtimeError_H` | page 1 | Front drive inverter: a001 deadtime error h | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_thermalWarning_L` | page 1 | Front drive inverter: a001 thermal warning l | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_thermalShutdown_L` | page 1 | Front drive inverter: a001 thermal shutdown l | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVL_L` | page 1 | Front drive inverter: a001 undervolt VL l | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVH_L` | page 1 | Front drive inverter: a001 undervolt VH l | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_sense_L` | page 1 | Front drive inverter: a001 sense l | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_desat_L` | page 1 | Front drive inverter: a001 desat l | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVL_L` | page 1 | Front drive inverter: a001 overvolt VL l | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVH_L` | page 1 | Front drive inverter: a001 overvolt VH l | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVCC_L` | page 1 | Front drive inverter: a001 undervolt VCC l | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_asynchStop_L` | page 1 | Front drive inverter: a001 asynch stop l | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_remoteRegError_L` | page 1 | Front drive inverter: a001 remote reg error l | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_undervoltVDD_L` | page 1 | Front drive inverter: a001 undervolt VDD l | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_overvoltVDD_L` | page 1 | Front drive inverter: a001 overvolt VDD l | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localRegError_L` | page 1 | Front drive inverter: a001 local reg error l | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_spiError_L` | page 1 | Front drive inverter: a001 spi error l | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_deadtimeError_L` | page 1 | Front drive inverter: a001 deadtime error l | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_gateDriveErrCounter` | page 1 | Front drive inverter: a001 gate drive err counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a001_remoteCommError_H` | page 1 | Front drive inverter: a001 remote comm error h | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localCommError_H` | page 1 | Front drive inverter: a001 local comm error h | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_remoteReset_H` | page 1 | Front drive inverter: a001 remote reset h | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localReset_H` | page 1 | Front drive inverter: a001 local reset h | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_remoteCommError_L` | page 1 | Front drive inverter: a001 remote comm error l | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localCommError_L` | page 1 | Front drive inverter: a001 local comm error l | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_remoteReset_L` | page 1 | Front drive inverter: a001 remote reset l | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_localReset_L` | page 1 | Front drive inverter: a001 local reset l | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_faultLine1Gpio_H` | page 1 | Front drive inverter: a001 fault line1 gpio h | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a001_faultLine1Gpio_L` | page 1 | Front drive inverter: a001 fault line1 gpio l | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_thermalWarning_H` | page 2 | Front drive inverter: a002 thermal warning h | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_thermalShutdown_H` | page 2 | Front drive inverter: a002 thermal shutdown h | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVL_H` | page 2 | Front drive inverter: a002 undervolt VL h | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVH_H` | page 2 | Front drive inverter: a002 undervolt VH h | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_sense_H` | page 2 | Front drive inverter: a002 sense h | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_desat_H` | page 2 | Front drive inverter: a002 desat h | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVL_H` | page 2 | Front drive inverter: a002 overvolt VL h | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVH_H` | page 2 | Front drive inverter: a002 overvolt VH h | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVCC_H` | page 2 | Front drive inverter: a002 undervolt VCC h | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_asynchStop_H` | page 2 | Front drive inverter: a002 asynch stop h | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_remoteRegError_H` | page 2 | Front drive inverter: a002 remote reg error h | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVDD_H` | page 2 | Front drive inverter: a002 undervolt VDD h | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVDD_H` | page 2 | Front drive inverter: a002 overvolt VDD h | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localRegError_H` | page 2 | Front drive inverter: a002 local reg error h | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_spiError_H` | page 2 | Front drive inverter: a002 spi error h | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_deadtimeError_H` | page 2 | Front drive inverter: a002 deadtime error h | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_thermalWarning_L` | page 2 | Front drive inverter: a002 thermal warning l | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_thermalShutdown_L` | page 2 | Front drive inverter: a002 thermal shutdown l | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVL_L` | page 2 | Front drive inverter: a002 undervolt VL l | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVH_L` | page 2 | Front drive inverter: a002 undervolt VH l | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_sense_L` | page 2 | Front drive inverter: a002 sense l | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_desat_L` | page 2 | Front drive inverter: a002 desat l | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVL_L` | page 2 | Front drive inverter: a002 overvolt VL l | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVH_L` | page 2 | Front drive inverter: a002 overvolt VH l | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVCC_L` | page 2 | Front drive inverter: a002 undervolt VCC l | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_asynchStop_L` | page 2 | Front drive inverter: a002 asynch stop l | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_remoteRegError_L` | page 2 | Front drive inverter: a002 remote reg error l | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_undervoltVDD_L` | page 2 | Front drive inverter: a002 undervolt VDD l | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_overvoltVDD_L` | page 2 | Front drive inverter: a002 overvolt VDD l | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localRegError_L` | page 2 | Front drive inverter: a002 local reg error l | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_spiError_L` | page 2 | Front drive inverter: a002 spi error l | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_deadtimeError_L` | page 2 | Front drive inverter: a002 deadtime error l | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_gateDriveErrCounter` | page 2 | Front drive inverter: a002 gate drive err counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a002_remoteCommError_H` | page 2 | Front drive inverter: a002 remote comm error h | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localCommError_H` | page 2 | Front drive inverter: a002 local comm error h | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_remoteReset_H` | page 2 | Front drive inverter: a002 remote reset h | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localReset_H` | page 2 | Front drive inverter: a002 local reset h | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_remoteCommError_L` | page 2 | Front drive inverter: a002 remote comm error l | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localCommError_L` | page 2 | Front drive inverter: a002 local comm error l | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_remoteReset_L` | page 2 | Front drive inverter: a002 remote reset l | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_localReset_L` | page 2 | Front drive inverter: a002 local reset l | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_faultLine1Gpio_H` | page 2 | Front drive inverter: a002 fault line1 gpio h | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a002_faultLine1Gpio_L` | page 2 | Front drive inverter: a002 fault line1 gpio l | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_thermalWarning_H` | page 3 | Front drive inverter: a003 thermal warning h | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_thermalShutdown_H` | page 3 | Front drive inverter: a003 thermal shutdown h | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVL_H` | page 3 | Front drive inverter: a003 undervolt VL h | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVH_H` | page 3 | Front drive inverter: a003 undervolt VH h | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_sense_H` | page 3 | Front drive inverter: a003 sense h | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_desat_H` | page 3 | Front drive inverter: a003 desat h | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVL_H` | page 3 | Front drive inverter: a003 overvolt VL h | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVH_H` | page 3 | Front drive inverter: a003 overvolt VH h | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVCC_H` | page 3 | Front drive inverter: a003 undervolt VCC h | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_asynchStop_H` | page 3 | Front drive inverter: a003 asynch stop h | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_remoteRegError_H` | page 3 | Front drive inverter: a003 remote reg error h | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVDD_H` | page 3 | Front drive inverter: a003 undervolt VDD h | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVDD_H` | page 3 | Front drive inverter: a003 overvolt VDD h | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localRegError_H` | page 3 | Front drive inverter: a003 local reg error h | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_spiError_H` | page 3 | Front drive inverter: a003 spi error h | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_deadtimeError_H` | page 3 | Front drive inverter: a003 deadtime error h | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_thermalWarning_L` | page 3 | Front drive inverter: a003 thermal warning l | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_thermalShutdown_L` | page 3 | Front drive inverter: a003 thermal shutdown l | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVL_L` | page 3 | Front drive inverter: a003 undervolt VL l | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVH_L` | page 3 | Front drive inverter: a003 undervolt VH l | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_sense_L` | page 3 | Front drive inverter: a003 sense l | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_desat_L` | page 3 | Front drive inverter: a003 desat l | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVL_L` | page 3 | Front drive inverter: a003 overvolt VL l | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVH_L` | page 3 | Front drive inverter: a003 overvolt VH l | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVCC_L` | page 3 | Front drive inverter: a003 undervolt VCC l | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_asynchStop_L` | page 3 | Front drive inverter: a003 asynch stop l | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_remoteRegError_L` | page 3 | Front drive inverter: a003 remote reg error l | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_undervoltVDD_L` | page 3 | Front drive inverter: a003 undervolt VDD l | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_overvoltVDD_L` | page 3 | Front drive inverter: a003 overvolt VDD l | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localRegError_L` | page 3 | Front drive inverter: a003 local reg error l | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_spiError_L` | page 3 | Front drive inverter: a003 spi error l | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_deadtimeError_L` | page 3 | Front drive inverter: a003 deadtime error l | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_gateDriveErrCounter` | page 3 | Front drive inverter: a003 gate drive err counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a003_remoteCommError_H` | page 3 | Front drive inverter: a003 remote comm error h | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localCommError_H` | page 3 | Front drive inverter: a003 local comm error h | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_remoteReset_H` | page 3 | Front drive inverter: a003 remote reset h | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localReset_H` | page 3 | Front drive inverter: a003 local reset h | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_remoteCommError_L` | page 3 | Front drive inverter: a003 remote comm error l | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localCommError_L` | page 3 | Front drive inverter: a003 local comm error l | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_remoteReset_L` | page 3 | Front drive inverter: a003 remote reset l | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_localReset_L` | page 3 | Front drive inverter: a003 local reset l | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_faultLine1Gpio_H` | page 3 | Front drive inverter: a003 fault line1 gpio h | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a003_faultLine1Gpio_L` | page 3 | Front drive inverter: a003 fault line1 gpio l | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a007_phaseAcurrent` | page 7 | Front drive inverter: a007 phase acurrent | 16\|8 | little-endian | unsigned | 8 | 0 | A | 0 to 2040 |  | plausible |
| `DIF_a007_phaseBcurrent` | page 7 | Front drive inverter: a007 phase bcurrent | 24\|8 | little-endian | unsigned | 8 | 0 | A | 0 to 2040 |  | plausible |
| `DIF_a007_offsetError` | page 7 | Front drive inverter: a007 offset error | 32\|14 | little-endian | signed | 0.0003834952 | 0 | rad | -3.1415926784 to 3.1412091832 |  | plausible |
| `DIF_a007_idFdbStdDeviation` | page 7 | Front drive inverter: a007 id fdb std deviation | 46\|8 | little-endian | unsigned | 4 | 0 | A | 0 to 1020 |  | plausible |
| `DIF_a007_iqFdbStdDeviation` | page 7 | Front drive inverter: a007 iq fdb std deviation | 54\|8 | little-endian | unsigned | 4 | 0 | A | 0 to 1020 |  | plausible |
| `DIF_a007_motorShift` | page 7 | Front drive inverter: a007 motor shift | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a007_motorShort` | page 7 | Front drive inverter: a007 motor short | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_sccReset` | page 10 | Front drive inverter: a010 scc reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_hibernate` | page 10 | Front drive inverter: a010 hibernate | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_hwBist` | page 10 | Front drive inverter: a010 hw bist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_nmiWatchdog` | page 10 | Front drive inverter: a010 nmi watchdog | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_watchdog` | page 10 | Front drive inverter: a010 watchdog | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_clockFailNmi` | page 10 | Front drive inverter: a010 clock fail nmi | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_ramUncErrorNmi` | page 10 | Front drive inverter: a010 ram unc error nmi | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_flashUncErrorNmi` | page 10 | Front drive inverter: a010 flash unc error nmi | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_cpu1signMismatchNmi` | page 10 | Front drive inverter: a010 cpu1sign mismatch nmi | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_cpu2signMismatchNmi` | page 10 | Front drive inverter: a010 cpu2sign mismatch nmi | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_pieVectErrorNmi` | page 10 | Front drive inverter: a010 pie vect error nmi | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_sysDbgNmi` | page 10 | Front drive inverter: a010 sys dbg nmi | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_rlNmi` | page 10 | Front drive inverter: a010 rl nmi | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_ovfNmi` | page 10 | Front drive inverter: a010 ovf nmi | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a010_wdtFlags` | page 10 | Front drive inverter: a010 wdt flags | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a011_reason` | page 11 | Front drive inverter: a011 reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `GATE_DRIVE_SUPPLY`<br>1 = `REG_DATA_MISMATCH`<br>2 = `CRC_MISMATCH`<br>3 = `FAULT_DURING_CONFIG`<br>4 = `SPI_ERROR` | plausible |
| `DIF_a011_phaseAHigh` | page 11 | Front drive inverter: a011 phase a high | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_phaseALow` | page 11 | Front drive inverter: a011 phase a low | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_phaseBHigh` | page 11 | Front drive inverter: a011 phase b high | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_phaseBLow` | page 11 | Front drive inverter: a011 phase b low | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_phaseCHigh` | page 11 | Front drive inverter: a011 phase c high | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_phaseCLow` | page 11 | Front drive inverter: a011 phase c low | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a011_regAddress` | page 11 | Front drive inverter: a011 reg address | 25\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `DIF_a011_badGateDriveIC` | page 11 | Front drive inverter: a011 bad gate drive IC | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DIF_a011_badDataRead` | page 11 | Front drive inverter: a011 bad data read | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a011_badDataExpected` | page 11 | Front drive inverter: a011 bad data expected | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a011_codeBranch` | page 11 | Front drive inverter: a011 code branch | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a012_hvilStatus` | page 12 | Front drive inverter: a012 hvil status; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |
| `DIF_a012_hvilCmVoltage` | page 12 | Front drive inverter: a012 hvil cm voltage | 24\|8 | little-endian | unsigned | 0.08 | 0 | V | 0 to 20.4 |  | plausible |
| `DIF_a012_hvilCurrent` | page 12 | Front drive inverter: a012 hvil current | 32\|8 | little-endian | unsigned | 0.1 | 0 | mA | 0 to 25.5 |  | plausible |
| `DIF_a012_hvilFaultGpio` | page 12 | Front drive inverter: a012 hvil fault gpio | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a012_hvilSupplyPinDI` | page 12 | Front drive inverter: a012 hvil supply pin DI | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a012_hvilSupplyPinPM` | page 12 | Front drive inverter: a012 hvil supply pin PM | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a012_activeDisOn3V3` | page 12 | Front drive inverter: a012 active dis on3 V3 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a012_hvilHeaderFault` | page 12 | Front drive inverter: a012 hvil header fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a013_address` | page 13 | Front drive inverter: a013 address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `DIF_a013_errorType` | page 13 | Front drive inverter: a013 error type | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `FLASH_UNCORRECTABLE_LOW`<br>2 = `FLASH_UNCORRECTABLE_HIGH`<br>3 = `FLASH_FAIL0_LOW`<br>4 = `FLASH_FAIL0_HIGH`<br>5 = `FLASH_FAIL1_LOW`<br>6 = `FLASH_FAIL1_HIGH`<br>7 = `RAM_UNCORRECTABLE_CPU`<br>8 = `RAM_UNCORRECTABLE_CLA`<br>9 = `RAM_UNCORRECTABLE_DMA`<br>10 = `RAM_CORRECTABLE_CPU`<br>11 = `RAM_CORRECTABLE_CLA`<br>12 = `RAM_CORRECTABLE_DMA` | plausible |
| `DIF_a014_motorSpeed` | page 14 | Front drive inverter: a014 motor speed | 16\|14 | little-endian | signed | 2 | 0 | RPM | -16384 to 16382 |  | plausible |
| `DIF_a014_adState` | page 14 | Front drive inverter: a014 ad state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STARTUP`<br>1 = `NORMAL`<br>2 = `BACKUP`<br>3 = `FAULTED` | plausible |
| `DIF_a014_torqueCommandFwd` | page 14 | Front drive inverter: a014 torque command fwd | 32\|10 | little-endian | signed | 2 | 0 | Nm | -1024 to 1022 |  | plausible |
| `DIF_a014_brakeMasterCylPress` | page 14 | Front drive inverter: a014 brake master cyl press | 42\|10 | little-endian | unsigned | 0.25 | -42.5 | bar | -42.5 to 213.25 |  | plausible |
| `DIF_a014_rmsTorqueError` | page 14 | Front drive inverter: a014 rms torque error | 52\|10 | little-endian | unsigned | 1 | 0 | Nm | 0 to 1023 |  | plausible |
| `DIF_a014_tcEnabled` | page 14 | Front drive inverter: a014 tc enabled | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a014_fbDeratedForRmsError` | page 14 | Front drive inverter: a014 fb derated for rms error | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_newSafeState` | page 16 | Front drive inverter: a016 new safe state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `ALL_OFF`<br>2 = `3PS_HIGH`<br>3 = `3PS_LOW` | plausible |
| `DIF_a016_oldSafeState` | page 16 | Front drive inverter: a016 old safe state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `ALL_OFF`<br>2 = `3PS_HIGH`<br>3 = `3PS_LOW` | plausible |
| `DIF_a016_gateDriveFaultLine` | page 16 | Front drive inverter: a016 gate drive fault line | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_ascMonitor` | page 16 | Front drive inverter: a016 asc monitor | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_uncontrolledRegenZone` | page 16 | Front drive inverter: a016 uncontrolled regen zone | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_pedalMonitorPreWatchdog` | page 16 | Front drive inverter: a016 pedal monitor pre watchdog | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_motorRPM` | page 16 | Front drive inverter: a016 motor RPM | 24\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a016_torqueMotor` | page 16 | Front drive inverter: a016 torque motor | 40\|16 | little-endian | signed | 1 | 0 | Nm | -32768 to 32767 |  | plausible |
| `DIF_a016_safetyICfaultLine` | page 16 | Front drive inverter: a016 safety i cfault line | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a016_triggerEvent` | page 16 | Front drive inverter: a016 trigger event | 57\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `UNKNOWN`<br>1 = `LV_SUPPLY_UV`<br>2 = `MOTOR_SPEED`<br>3 = `RESOLVER`<br>4 = `IRRATIONAL_CURRENT_PHASEA`<br>5 = `IRRATIONAL_CURRENT_PHASEB`<br>6 = `IRRATIONAL_CURRENT_PHASEC`<br>7 = `IRRATIONAL_CURRENT_PHASEV`<br>8 = `IRRATIONAL_CURRENT_PHASEW`<br>9 = `IRRATIONAL_CURRENT_VREF`<br>10 = `IRRATIONAL_CURRENT_DELTA_PHASEA`<br>11 = `IRRATIONAL_CURRENT_DELTA_PHASEB`<br>12 = `IRRATIONAL_CURRENT_DELTA_PHASEC`<br>13 = `IRRATIONAL_CURRENT_DELTA_PHASEV`<br>14 = `IRRATIONAL_CURRENT_DELTA_PHASEW`<br>15 = `NO_CURRENT`<br>16 = `PEAK_CURRENT`<br>17 = `BUS_OV`<br>18 = `BUS_IRRATIONAL`<br>19 = `BUS_UV`<br>20 = `SPEED_INVALID`<br>21 = `CLEAR_FUSES`<br>22 = `SELFTEST_FAIL`<br>23 = `GDIC_FAULT`<br>24 = `BUS_ANOMALY`<br>25 = `SWITCH_OFF_PATH_TRIP`<br>26 = `3PS_FEEDBACK`<br>27 = `MECHSS_CALLBACK`<br>28 = `CURRENT_OBSERVER`<br>29 = `AT_SPEED_RECOVERY`<br>30 = `SWITCH_SHORT_DISABLE_CONDITIONS_MET`<br>31 = `HV_SENSE_OVER_CAN` | plausible |
| `DIF_a024_vBat` | page 24 | Front drive inverter: a024 v bat | 16\|8 | little-endian | unsigned | 2 | 0 | V | 0 to 510 |  | plausible |
| `DIF_a024_failReason` | page 24 | Front drive inverter: a024 fail reason | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CACHED`<br>1 = `POS_CURRENT`<br>2 = `NEG_CURRENT`<br>3 = `DISAGREE`<br>4 = `TIMEDOUT`<br>5 = `SWITCH_SHORT_DISABLE_CONDITIONS_MET`<br>6 = `FAULT_PRESENT`<br>7 = `ASC_TEST` | plausible |
| `DIF_a024_state` | page 24 | Front drive inverter: a024 state | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `PSTG_BRING_UP`<br>2 = `PSTG_BRING_UP_AT_SPEED`<br>3 = `ASC_TEST`<br>4 = `ASC_TEST_PASSED`<br>5 = `PWM_ENABLE`<br>6 = `CURRENT_TEST_POS`<br>7 = `CURRENT_TEST_NEG`<br>8 = `TEST_PRE_PASSED`<br>9 = `TEST_PASSED`<br>10 = `TEST_SKIPPED`<br>11 = `TEST_FAILED`<br>12 = `TEST_RESTART`<br>13 = `DISABLED` | plausible |
| `DIF_a024_Ia` | page 24 | Front drive inverter: a024 ia | 31\|7 | little-endian | signed | 22.5 | 0 | A | -1440 to 1417.5 |  | plausible |
| `DIF_a024_Ib` | page 24 | Front drive inverter: a024 ib | 38\|7 | little-endian | signed | 22.5 | 0 | A | -1440 to 1417.5 |  | plausible |
| `DIF_a024_maxCurrMagSqrd` | page 24 | Front drive inverter: a024 max curr mag sqrd | 45\|12 | little-endian | unsigned | 500 | 0 | A2 | 0 to 2047500 |  | plausible |
| `DIF_a024_rotorAngle` | page 24 | Front drive inverter: a024 rotor angle | 57\|7 | little-endian | signed | 3 | 0 | degrees | -192 to 189 |  | plausible |
| `DIF_a025_Ia` | page 25 | Front drive inverter: a025 ia | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_a025_torqueMotor` | page 25 | Front drive inverter: a025 torque motor | 32\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a025_motorSpeed` | page 25 | Front drive inverter: a025 motor speed | 48\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a026_Ib` | page 26 | Front drive inverter: a026 ib | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_a026_torqueMotor` | page 26 | Front drive inverter: a026 torque motor | 32\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a026_motorSpeed` | page 26 | Front drive inverter: a026 motor speed | 48\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a027_Ic` | page 27 | Front drive inverter: a027 ic | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_a027_torqueMotor` | page 27 | Front drive inverter: a027 torque motor | 32\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a027_motorSpeed` | page 27 | Front drive inverter: a027 motor speed | 48\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a028_phaseAirms` | page 28 | Front drive inverter: a028 phase airms | 16\|16 | little-endian | unsigned | 1 | 0 | A | 0 to 65535 |  | plausible |
| `DIF_a028_iArmsTorque` | page 28 | Front drive inverter: a028 i arms torque | 32\|16 | little-endian | unsigned | 0.25 | 0 | Nm | 0 to 16383.75 |  | plausible |
| `DIF_a028_iArmsSpeed` | page 28 | Front drive inverter: a028 i arms speed | 48\|16 | little-endian | unsigned | 1 | 0 | RPM | 0 to 65535 |  | plausible |
| `DIF_a029_phaseBirms` | page 29 | Front drive inverter: a029 phase birms | 16\|16 | little-endian | unsigned | 1 | 0 | A | 0 to 65535 |  | plausible |
| `DIF_a029_iBrmsTorque` | page 29 | Front drive inverter: a029 i brms torque | 32\|16 | little-endian | unsigned | 0.25 | 0 | Nm | 0 to 16383.75 |  | plausible |
| `DIF_a029_iBrmsSpeed` | page 29 | Front drive inverter: a029 i brms speed | 48\|16 | little-endian | unsigned | 1 | 0 | RPM | 0 to 65535 |  | plausible |
| `DIF_a030_phaseCirms` | page 30 | Front drive inverter: a030 phase cirms | 16\|16 | little-endian | unsigned | 1 | 0 | A | 0 to 65535 |  | plausible |
| `DIF_a030_iCrmsTorque` | page 30 | Front drive inverter: a030 i crms torque | 32\|16 | little-endian | unsigned | 0.25 | 0 | Nm | 0 to 16383.75 |  | plausible |
| `DIF_a030_iCrmsSpeed` | page 30 | Front drive inverter: a030 i crms speed | 48\|16 | little-endian | unsigned | 1 | 0 | RPM | 0 to 65535 |  | plausible |
| `DIF_a031_phaseAoffset` | page 31 | Front drive inverter: a031 phase aoffset | 16\|15 | little-endian | signed | 0.002 | 0 | A | -32.768 to 32.766 |  | plausible |
| `DIF_a032_phaseBoffset` | page 32 | Front drive inverter: a032 phase boffset | 16\|15 | little-endian | signed | 0.002 | 0 | A | -32.768 to 32.766 |  | plausible |
| `DIF_a033_phaseAcurrent` | page 33 | Front drive inverter: a033 phase acurrent | 16\|16 | little-endian | signed | 1 | 0 | A | -32768 to 32767 |  | plausible |
| `DIF_a033_deltaIa` | page 33 | Front drive inverter: a033 delta ia | 32\|16 | little-endian | signed | 1 | 0 | A | -32768 to 32767 |  | plausible |
| `DIF_a033_vRefIa` | page 33 | Front drive inverter: a033 v ref ia | 48\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |
| `DIF_a034_phaseBcurrent` | page 34 | Front drive inverter: a034 phase bcurrent | 16\|16 | little-endian | signed | 1 | 0 | A | -32768 to 32767 |  | plausible |
| `DIF_a034_deltaIb` | page 34 | Front drive inverter: a034 delta ib | 32\|16 | little-endian | signed | 1 | 0 | A | -32768 to 32767 |  | plausible |
| `DIF_a034_vRefIb` | page 34 | Front drive inverter: a034 v ref ib | 48\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |
| `DIF_a035_phaseAerror` | page 35 | Front drive inverter: a035 phase aerror | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_phaseBerror` | page 35 | Front drive inverter: a035 phase berror | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_phaseCerror` | page 35 | Front drive inverter: a035 phase cerror | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_standbyCurrent` | page 35 | Front drive inverter: a035 standby current | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_unbalancedCurrent` | page 35 | Front drive inverter: a035 unbalanced current | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_wontMoveCurrent` | page 35 | Front drive inverter: a035 wont move current | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_reportingPhase` | page 35 | Front drive inverter: a035 reporting phase | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `DIF_a035_noDriveCurrent` | page 35 | Front drive inverter: a035 no drive current | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a035_phaseDifference` | page 35 | Front drive inverter: a035 phase difference | 25\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `DIF_a035_phaseCurrent` | page 35 | Front drive inverter: a035 phase current | 32\|16 | little-endian | unsigned | 1 | 0 | A | 0 to 65535 |  | plausible |
| `DIF_a035_frequency` | page 35 | Front drive inverter: a035 frequency | 48\|10 | little-endian | unsigned | 1 | 0 | Hz | 0 to 1023 |  | plausible |
| `DIF_a036_busVoltage` | page 36 | Front drive inverter: a036 bus voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `DIF_a036_busHighLimit` | page 36 | Front drive inverter: a036 bus high limit | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `DIF_a037_busVoltage` | page 37 | Front drive inverter: a037 bus voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `DIF_a037_busLowLimit` | page 37 | Front drive inverter: a037 bus low limit | 32\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.5 |  | plausible |
| `DIF_a038_vBMS` | page 38 | Front drive inverter: a038 v BMS | 16\|13 | little-endian | unsigned | 0.2 | 0 | V | 0 to 1638.2 |  | plausible |
| `DIF_a038_vBat` | page 38 | Front drive inverter: a038 v bat | 32\|13 | little-endian | unsigned | 0.2 | 0 | V | 0 to 1638.2 |  | plausible |
| `DIF_a038_iBat` | page 38 | Front drive inverter: a038 i bat | 48\|13 | little-endian | unsigned | 0.5 | 0 | A | 0 to 4095.5 |  | plausible |
| `DIF_a038_reason` | page 38 | Front drive inverter: a038 reason | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNDERVOLTAGE_PRE_CHARGE`<br>1 = `UNDERVOLTAGE_HV_UP`<br>2 = `DI_BMS_VOLTAGE_MISMATCH` | plausible |
| `DIF_a040_torque` | page 40 | Front drive inverter: a040 torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_capability` | page 40 | Front drive inverter: a040 capability | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_power` | page 40 | Front drive inverter: a040 power | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_status` | page 40 | Front drive inverter: a040 status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_capability2` | page 40 | Front drive inverter: a040 capability2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_hvStatus` | page 40 | Front drive inverter: a040 hv status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a040_temperature` | page 40 | Front drive inverter: a040 temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a041_uartRxDataAvailable` | page 41 | Front drive inverter: a041 uart rx data available | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a041_SDC_status_MIA` | page 41 | Front drive inverter: a041 SDC status MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a041_diUartRxVersion` | page 41 | Front drive inverter: a041 di uart rx version | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a041_sdcUartRxVersion` | page 41 | Front drive inverter: a041 sdc uart rx version | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a043_outletTemp` | page 43 | Front drive inverter: a043 outlet temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a044_outletTemp` | page 44 | Front drive inverter: a044 outlet temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a045_inletTemp` | page 45 | Front drive inverter: a045 inlet temp | 16\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a045_outletTemp` | page 45 | Front drive inverter: a045 outlet temp | 26\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a045_heatsinkTemp` | page 45 | Front drive inverter: a045 heatsink temp | 36\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a045_outletTempSlope` | page 45 | Front drive inverter: a045 outlet temp slope | 48\|8 | little-endian | signed | 0.5 | 0 | DegC/s | -64 to 63.5 |  | plausible |
| `DIF_a046_statorTemp1` | page 46 | Front drive inverter: a046 stator temp1 | 16\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a046_statorTemp2` | page 46 | Front drive inverter: a046 stator temp2 | 32\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a047_statorTemp1` | page 47 | Front drive inverter: a047 stator temp1 | 16\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a047_statorTslope1` | page 47 | Front drive inverter: a047 stator tslope1 | 32\|16 | little-endian | signed | 0.1 | 0 | DegC/s | -3276.8 to 3276.7 |  | plausible |
| `DIF_a050_statorTemp1` | page 50 | Front drive inverter: a050 stator temp1 | 16\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a050_statorTemp2` | page 50 | Front drive inverter: a050 stator temp2 | 32\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a052_torque` | page 52 | Front drive inverter: a052 torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_capability` | page 52 | Front drive inverter: a052 capability | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_power` | page 52 | Front drive inverter: a052 power | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_status` | page 52 | Front drive inverter: a052 status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_capability2` | page 52 | Front drive inverter: a052 capability2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_hvStatus` | page 52 | Front drive inverter: a052 hv status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a052_temperature` | page 52 | Front drive inverter: a052 temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a054_outletTemp` | page 54 | Front drive inverter: a054 outlet temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a054_heatsinkTemp` | page 54 | Front drive inverter: a054 heatsink temp | 32\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a055_parameterDI` | page 55 | Front drive inverter: a055 parameter DI | 16\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a055_parameterPM` | page 55 | Front drive inverter: a055 parameter PM | 32\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a055_torqueType` | page 55 | Front drive inverter: a055 torque type | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TORQUE_ESTIMATE`<br>1 = `TORQUE_COMMAND`<br>2 = `PEDAL_POSITION` | plausible |
| `DIF_a055_motorRPM` | page 55 | Front drive inverter: a055 motor RPM | 48\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a056_pcbTemp` | page 56 | Front drive inverter: a056 pcb temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a057_pcbTemp` | page 57 | Front drive inverter: a057 pcb temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a058_pcbTemp` | page 58 | Front drive inverter: a058 pcb temp | 16\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a058_outletTemp` | page 58 | Front drive inverter: a058 outlet temp | 26\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a058_heatsinkTemp` | page 58 | Front drive inverter: a058 heatsink temp | 36\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a058_pcbTempSlope` | page 58 | Front drive inverter: a058 pcb temp slope | 48\|8 | little-endian | signed | 0.5 | 0 | DegC/s | -64 to 63.5 |  | plausible |
| `DIF_a059_heatsinkTemp` | page 59 | Front drive inverter: a059 heatsink temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a060_heatsinkTemp` | page 60 | Front drive inverter: a060 heatsink temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a061_sensor` | page 61 | Front drive inverter: a061 sensor | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PH1`<br>1 = `PH2`<br>2 = `PH3` | plausible |
| `DIF_a061_reason` | page 61 | Front drive inverter: a061 reason | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RATE_OF_CHANGE`<br>1 = `RAILED` | plausible |
| `DIF_a061_phTemp` | page 61 | Front drive inverter: a061 ph temp | 24\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a061_otherTemp` | page 61 | Front drive inverter: a061 other temp | 40\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a062_limpReason` | page 62 | Front drive inverter: a062 limp reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `PHASE_IMBALANCE`<br>1 = `BUSV_SENSOR_IRRATIONAL`<br>2 = `NO_FUNC_STATORT_SENSOR`<br>3 = `NO_FUNC_HEATSINK_SENSOR`<br>4 = `NO_FLUID`<br>5 = `LV_SUPPLY_UNDERVOLTAGE`<br>6 = `BMS_MIA`<br>7 = `LOW_FLOW`<br>8 = `OUTLET_TEMP`<br>9 = `AMBIENT_TEMP`<br>10 = `DELTAT_TOO_POSITIVE`<br>11 = `DELTAT_TOO_NEGATIVE`<br>12 = `STATOR_TEMP`<br>13 = `WRONG_CS_CALIBRATION`<br>14 = `EXTERNAL_COMMAND`<br>15 = `TRQ_CROSS_CHECK`<br>16 = `PMHEARTBEAT`<br>17 = `PMREQUEST`<br>18 = `HEATSINK_TEMP`<br>19 = `CONFIG_MISMATCH`<br>20 = `DI_MIA`<br>21 = `TRQCMD_VALIDITY_UNKNOWN`<br>22 = `GTW_MIA`<br>23 = `CAPACITOR_OVERTEMP`<br>24 = `CONTACTOR_WELD`<br>25 = `SLAVE_REQUEST`<br>26 = `SLAVE_MIA`<br>27 = `FACTORY_GLIDER`<br>28 = `OIL_PUMP_FAILURE`<br>29 = `OIL_PUMP_FLUID_OVERTEMP`<br>30 = `HEATSINK_SENSOR_IRRATIONAL`<br>31 = `OIL_PRESSURE_LOW`<br>32 = `RESIST_STATOR_TEMP`<br>33 = `MOTION_IN_DYNO`<br>34 = `MECHANICAL_SAFE_ST_UNAVAIL`<br>35 = `CURRENT_CORE_FALLBACK`<br>36 = `XTAL_OSCILLATOR`<br>37 = `DEGRADED_REQUEST_SSFA`<br>38 = `DEGRADED_REQUEST_PSFA`<br>39 = `DEGRADED_REQUEST_SEPS`<br>40 = `DEGRADED_REQUEST_PEPS`<br>41 = `DEGRADED_REQUEST_VCLEFT`<br>42 = `DEGRADED_REQUEST_VCRIGHT`<br>43 = `UNIT_CHILL_REQUEST` | plausible |
| `DIF_a063_BB_status` | page 63 | Front drive inverter: a063 BB status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a064_interventionType` | page 64 | Front drive inverter: a064 intervention type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `masterTorqueMonitorShutoff`<br>1 = `resolver`<br>2 = `torqueCmdInvalid`<br>3 = `cruiseFault`<br>4 = `motorMovementDetected`<br>5 = `accumulatedTorque`<br>6 = `torqueReversal`<br>7 = `excessiveRegenTorque`<br>8 = `torqueInNeutral`<br>9 = `inconsistentTorqueSign`<br>10 = `switchOffPathTestFail`<br>11 = `switchingAfterIntervention`<br>12 = `currentAfterIntervention`<br>13 = `diHeartbeat`<br>14 = `inconsistentAxleTorque`<br>15 = `excessiveMotorMz` | plausible |
| `DIF_a064_torqueCmdState` | page 64 | Front drive inverter: a064 torque cmd state; raw 0 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>6 = `Valid`<br>8 = `Invalid` | plausible |
| `DIF_a069_motorSpeed` | page 69 | Front drive inverter: a069 motor speed | 16\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a069_rotorCoolingPower` | page 69 | Front drive inverter: a069 rotor cooling power | 32\|8 | little-endian | unsigned | 20 | 0 | W | 0 to 5100 |  | plausible |
| `DIF_a069_rotorMagnetTemp` | page 69 | Front drive inverter: a069 rotor magnet temp | 40\|10 | little-endian | unsigned | 0.25 | -60 | DegC | -60 to 195.75 |  | plausible |
| `DIF_a069_fittedTorqueLimit` | page 69 | Front drive inverter: a069 fitted torque limit | 50\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a072_reason` | page 72 | Front drive inverter: a072 reason | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT`<br>1 = `EXTERNAL_OSCILLATOR`<br>2 = `MECHSS`<br>3 = `SWITCH_SHORT_TEST` | plausible |
| `DIF_a073_motorSpeedrpm` | page 73 | Front drive inverter: a073 motor speedrpm | 16\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a075_motorSpeed` | page 75 | Front drive inverter: a075 motor speed | 16\|16 | little-endian | unsigned | 1 | 0 | RPM | 0 to 65535 |  | plausible |
| `DIF_a075_absSpeed` | page 75 | Front drive inverter: a075 abs speed | 32\|16 | little-endian | unsigned | 1 | 0 | RPM | 0 to 65535 |  | plausible |
| `DIF_a076_lvSupplyV` | page 76 | Front drive inverter: a076 lv supply v | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | plausible |
| `DIF_a077_lvSupplyV` | page 77 | Front drive inverter: a077 lv supply v | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | plausible |
| `DIF_a078_adcRefChan` | page 78 | Front drive inverter: a078 adc ref chan | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a078_adcRefLowAvg` | page 78 | Front drive inverter: a078 adc ref low avg | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a079_adcRefChan` | page 79 | Front drive inverter: a079 adc ref chan | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a079_adcRefHighAvg` | page 79 | Front drive inverter: a079 adc ref high avg | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a087_gtwCarConfig` | page 87 | Front drive inverter: a087 gtw car config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a087_gtwTime` | page 87 | Front drive inverter: a087 gtw time | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a087_gtwUpdateStatus` | page 87 | Front drive inverter: a087 gtw update status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a087_gearControl` | page 87 | Front drive inverter: a087 gear control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a087_carState` | page 87 | Front drive inverter: a087 car state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_reason` | page 90 | Front drive inverter: a090 reason | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TOOSLOW`<br>1 = `TOOFAST` | plausible |
| `DIF_a090_systemState` | page 90 | Front drive inverter: a090 system state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_state` | page 90 | Front drive inverter: a090 state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_locState` | page 90 | Front drive inverter: a090 loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_state2` | page 90 | Front drive inverter: a090 state2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_state4` | page 90 | Front drive inverter: a090 state4 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_brakeTorque` | page 91 | Front drive inverter: a091 ESP brake torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_wheelSpeeds` | page 91 | Front drive inverter: a091 ESP wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_wheelRotation` | page 91 | Front drive inverter: a091 ESP wheel rotation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_motorLimits` | page 91 | Front drive inverter: a091 ESP motor limits | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_offsets` | page 91 | Front drive inverter: a091 ESP offsets | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_status` | page 91 | Front drive inverter: a091 ESP status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_party3` | page 91 | Front drive inverter: a091 ESP party3 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_ESP_redundantBrakingStatus` | page 91 | Front drive inverter: a091 ESP redundant braking status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsStatus` | page 92 | Front drive inverter: a092 bms status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsDriveLimits` | page 92 | Front drive inverter: a092 bms drive limits | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsHvBusStatus` | page 92 | Front drive inverter: a092 bms hv bus status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsPowerAvailable` | page 92 | Front drive inverter: a092 bms power available | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsBmbMinMax` | page 92 | Front drive inverter: a092 bms bmb min max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsSocStatus` | page 92 | Front drive inverter: a092 bms soc status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsThermalStatus` | page 92 | Front drive inverter: a092 bms thermal status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsCtrStatus` | page 92 | Front drive inverter: a092 bms ctr status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsVoltageRegGain` | page 92 | Front drive inverter: a092 bms voltage reg gain | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsPackConfig` | page 92 | Front drive inverter: a092 bms pack config | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsSystemStatus` | page 92 | Front drive inverter: a092 bms system status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_const_fast` | page 96 | Front drive inverter: a096 const fast | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_text_fast` | page 96 | Front drive inverter: a096 text fast | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_text_flash` | page 96 | Front drive inverter: a096 text flash | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_mem_data` | page 96 | Front drive inverter: a096 mem data | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_mem_regs` | page 96 | Front drive inverter: a096 mem regs | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_boot_flash` | page 96 | Front drive inverter: a096 boot flash | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_word1` | page 96 | Front drive inverter: a096 word1 | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a096_word2` | page 96 | Front drive inverter: a096 word2 | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a097_errorType` | page 97 | Front drive inverter: a097 error type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OPEN`<br>1 = `READ`<br>2 = `WRITE`<br>3 = `CRC`<br>4 = `LOST`<br>5 = `DPOT_READ`<br>6 = `DPOT_WRITE` | plausible |
| `DIF_a097_lineNumber` | page 97 | Front drive inverter: a097 line number | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a097_argument` | page 97 | Front drive inverter: a097 argument | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a098_pwmCount` | page 98 | Front drive inverter: a098 pwm count | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a098_fluxState` | page 98 | Front drive inverter: a098 flux state | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `START`<br>1 = `TEST`<br>2 = `STANDBY`<br>3 = `FLUX_UP`<br>4 = `FLUX_DOWN`<br>5 = `ENABLED`<br>6 = `ICONTROL`<br>7 = `VCONTROL`<br>9 = `FAULT`<br>10 = `STATIONARY_WASTE`<br>11 = `MAGNET_FLUX_DETECT`<br>12 = `DISABLED` | plausible |
| `DIF_a103_fluidTorDeltaT` | page 103 | Front drive inverter: a103 fluid tor delta t | 16\|8 | little-endian | signed | 2.007874 | 68.2677154541 | C | -188.740156546 to 323.267713454 |  | plausible |
| `DIF_a103_noFlowDetected` | page 103 | Front drive inverter: a103 no flow detected | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a103_lowFlowDetected` | page 103 | Front drive inverter: a103 low flow detected | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a103_fluidImplausible` | page 103 | Front drive inverter: a103 fluid implausible | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a103_inverterTemp` | page 103 | Front drive inverter: a103 inverter temp | 27\|8 | little-endian | signed | 2.007874 | 68.2677154541 | C | -188.740156546 to 323.267713454 |  | plausible |
| `DIF_a103_rmsCurrent` | page 103 | Front drive inverter: a103 rms current | 35\|10 | little-endian | signed | 12.8199605942 | 0 | A | -6563.81982423 to 6550.99986364 |  | plausible |
| `DIF_a103_ambientTemp` | page 103 | Front drive inverter: a103 ambient temp | 45\|7 | little-endian | signed | 1.5873016119 | 11.1111106873 | C | -90.4761924743 to 111.111112237 |  | plausible |
| `DIF_a103_sensorTempEst` | page 103 | Front drive inverter: a103 sensor temp est | 52\|8 | little-endian | signed | 1.25984251499 | 40.31496 | C | -120.944881919 to 200.314959404 |  | plausible |
| `DIF_a107_fpgaVersion` | page 107 | Front drive inverter: a107 fpga version | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a107_fpgaBootVersion` | page 107 | Front drive inverter: a107 fpga boot version | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a107_fpgaMasterActive` | page 107 | Front drive inverter: a107 fpga master active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a107_fpgaFaultActive` | page 107 | Front drive inverter: a107 fpga fault active | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a107_fpgaWarningActive` | page 107 | Front drive inverter: a107 fpga warning active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a108_fromState` | page 108 | Front drive inverter: a108 from state | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a108_toState` | page 108 | Front drive inverter: a108 to state | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a108_blockingAlert` | page 108 | Front drive inverter: a108 blocking alert | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_hwPhaseAgateDrive`<br>2 = `a002_hwPhaseBgateDrive`<br>3 = `a003_hwPhaseCgateDrive`<br>4 = `a004_hwPhaseApeak`<br>5 = `a005_hwPhaseBpeak`<br>6 = `a006_hwPhaseCpeak`<br>7 = `a007_statorAnomalyDetected`<br>8 = `a008_hwEncoderA`<br>9 = `a009_hwEncoderB`<br>10 = `a010_unintendedReset`<br>11 = `a011_swPowerStageNotReady`<br>12 = `a012_hvilNotClosed`<br>13 = `a013_eccError`<br>14 = `a014_activeDamping`<br>15 = `a015_mechSafeStateAnomaly`<br>16 = `a016_safeStateApplied`<br>17 = `a017_hwPedalMonitor`<br>18 = `a018_hwLVSupplyUV`<br>20 = `a020_hwMotorEncoder`<br>21 = `a021_hwBusOV`<br>22 = `a022_hw5vSupplyUV`<br>24 = `a024_selfTest`<br>25 = `a025_phaseApeak`<br>26 = `a026_phaseBpeak`<br>27 = `a027_phaseCpeak`<br>28 = `a028_phaseArms`<br>29 = `a029_phaseBrms`<br>30 = `a030_phaseCrms`<br>31 = `a031_phaseAcurrentOffset`<br>32 = `a032_phaseBcurrentOffset`<br>33 = `a033_phaseAcurrentSensor`<br>34 = `a034_phaseBcurrentSensor`<br>35 = `a035_phaseCurrentBalance`<br>36 = `a036_busOV`<br>37 = `a037_busUV`<br>38 = `a038_busVsensor`<br>39 = `a039_exceptionUndefinedInstruction`<br>40 = `a040_difMIA`<br>41 = `a041_sdcMIA`<br>42 = `a042_inletSensor`<br>43 = `a043_outletOT`<br>44 = `a044_outletUT`<br>45 = `a045_outletSensor`<br>46 = `a046_statorOT`<br>47 = `a047_statorSensor1`<br>48 = `a048_statorSensor2`<br>49 = `a049_statorSensorDiff`<br>50 = `a050_noStatorSensor`<br>52 = `a052_dirMIA`<br>53 = `a053_unexpectedLatchState`<br>54 = `a054_driveInverterOT`<br>55 = `a055_trqCrossCheck`<br>56 = `a056_ambientOT`<br>57 = `a057_ambientUT`<br>58 = `a058_ambientSensor`<br>59 = `a059_heatsinkOT`<br>60 = `a060_heatsinkUT`<br>61 = `a061_heatsinkSensor`<br>62 = `a062_systemLimpMode`<br>63 = `a063_bbMIA`<br>64 = `a064_torqueIntervention`<br>65 = `a065_canHardwareBusB`<br>66 = `a066_canDataBusB`<br>67 = `a067_canOverrunBusB`<br>69 = `a069_rotorTempLimit`<br>70 = `a070_udsTransactionInitiated`<br>71 = `a071_busDisconnected`<br>72 = `a072_gateDriveFaultCounter`<br>73 = `a073_motorSpeed`<br>74 = `a074_motorEncoder`<br>75 = `a075_motorSpeedMismatch`<br>76 = `a076_lvSupplyOV`<br>77 = `a077_lvSupplyUV`<br>78 = `a078_adcRefLow`<br>79 = `a079_adcRefHigh`<br>84 = `a084_eccTestData0`<br>85 = `d085_driveInverterBoardFailure`<br>86 = `a086_activeDischargeOn`<br>87 = `a087_gtwMIA`<br>88 = `a088_uiMIA`<br>89 = `d089_invalidTorqueCommand`<br>90 = `a090_pmMIA`<br>91 = `a091_espMIA`<br>92 = `a092_bmsMIA`<br>93 = `a093_canHardwareBusA`<br>94 = `a094_canDataBusA`<br>95 = `a095_canOverrunBusA`<br>96 = `a096_memoryError`<br>97 = `a097_eepromError`<br>98 = `a098_intTimeTooLong`<br>99 = `a099_threadOverrun`<br>100 = `a100_assertion`<br>101 = `a101_eccTestData1`<br>102 = `a102_exceptionPrefetchAbort`<br>103 = `a103_lowFlow`<br>104 = `d104_resetUnintended`<br>105 = `d105_busVoltageSensorIssue`<br>106 = `a106_idleTaskStarving`<br>107 = `a107_fpgaError`<br>108 = `a108_stateTrans`<br>109 = `a109_ahbWriteError`<br>110 = `a110_brakeMIA`<br>111 = `a111_badPhaseSensorCalib`<br>112 = `a112_noPhaseCurrent`<br>113 = `a113_noFuncHeatsinkSensor`<br>114 = `a114_exceptionDataAbort`<br>115 = `a115_exceptionDataAbort2`<br>116 = `a116_highSpeedWearCounter`<br>117 = `a117_diMIA`<br>118 = `d118_oilPumpCommsLost`<br>119 = `a119_hvpMIA`<br>120 = `a120_hvlinkMIA`<br>121 = `a121_motorControlRegulation`<br>122 = `a122_highStackUsage`<br>123 = `a123_lossMotorControl`<br>124 = `d124_oilPumpServiceRequired`<br>125 = `d125_currentSensorIssue`<br>126 = `a126_limpMode`<br>127 = `a127_gracefulPowerOff`<br>128 = `a128_fpgaVersionMismatch`<br>129 = `d129_oilPumpIssue`<br>130 = `d130_positionSensorIssue`<br>131 = `d131_currentSensorOffset`<br>132 = `d132_busUVIssue`<br>133 = `a133_capacitorOT`<br>134 = `a134_wheelSpeedIrrational`<br>135 = `d135_rotatedStator`<br>136 = `a136_spiError`<br>137 = `d137_currentSensorOutOfRange`<br>138 = `d138_inverterLVPowerSupplyLow`<br>141 = `d141_coolingSystemIssue`<br>142 = `a142_highLashAngle`<br>143 = `d143_wheelSpeedCorrelationIssue`<br>144 = `a144_configMismatch`<br>147 = `a147_highTorqueWearLimit`<br>148 = `a148_burnInCycleEnded`<br>149 = `a149_oilPumpFailure`<br>150 = `a150_busVD`<br>151 = `a151_shockTorqueLimiter`<br>152 = `a152_linError`<br>153 = `a153_oilPumpDiagnostics`<br>154 = `a154_resolver`<br>155 = `a155_vcfrontMIA`<br>156 = `a156_currentObserver`<br>157 = `a157_rcmMIA`<br>158 = `a158_ibstMIA`<br>160 = `a160_busVoltageAnomaly`<br>161 = `a161_epas3pMIA`<br>162 = `a162_endOfLifetimeBurnIn`<br>163 = `d163_recoverableOvercurrent`<br>164 = `d164_firmwareConfigMismatch`<br>165 = `d165_statorOverTemperature`<br>166 = `d166_rotorOverTemperature`<br>167 = `d167_tempSensorIssue`<br>168 = `d168_clutchPerformance`<br>169 = `d169_clutchPosition`<br>170 = `d170_clutchFailure`<br>172 = `a172_statorOilTempOT`<br>173 = `a173_ascFdbkDiagnostic`<br>174 = `a174_unitMayNotRestart`<br>176 = `a176_safetyICFault`<br>177 = `a177_fluxReferenceCorrected`<br>202 = `a202_excessHeatUnavailable`<br>225 = `a225_tmpEstPlausibility`<br>229 = `a229_busVsensorOverCAN`<br>233 = `a233_diMsgMissed`<br>234 = `a234_pcsMIA`<br>236 = `a236_tasMIA`<br>240 = `a240_clearFusesRoutine`<br>241 = `a241_systemThermallyLimited`<br>242 = `a242_spinDownLearning`<br>243 = `a243_ecuLogAvailable`<br>244 = `a244_mechSafeStateApplied`<br>245 = `a245_mechSafeStatePreWarn`<br>246 = `a246_recoveryAtSpeedError`<br>247 = `a247_rotorOffsetError`<br>249 = `a249_highStatorTempFromResist`<br>250 = `a250_preregulatorRail`<br>251 = `a251_oilPumpService`<br>252 = `a252_currentCoreFallback`<br>253 = `a253_lvBoostedRail`<br>254 = `a254_activeDischargeRail`<br>255 = `a255_currentGainFallback` | plausible |
| `DIF_a110_EPBL_status` | page 110 | Front drive inverter: a110 EPBL status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a110_EPBR_status` | page 110 | Front drive inverter: a110 EPBR status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a110_EPBL_autonomyHealth` | page 110 | Front drive inverter: a110 EPBL autonomy health | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a110_EPBR_autonomyHealth` | page 110 | Front drive inverter: a110 EPBR autonomy health | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a111_phAcalib` | page 111 | Front drive inverter: a111 ph acalib | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a111_phBcalib` | page 111 | Front drive inverter: a111 ph bcalib | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DIF_a112_pwmSwitching` | page 112 | Front drive inverter: a112 pwm switching | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_gdicResetLine` | page 112 | Front drive inverter: a112 gdic reset line | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_allOffSafeState` | page 112 | Front drive inverter: a112 all off safe state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_ls3psSafeState` | page 112 | Front drive inverter: a112 ls3ps safe state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_hs3psSafeState` | page 112 | Front drive inverter: a112 hs3ps safe state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_modulationIndex` | page 112 | Front drive inverter: a112 modulation index | 21\|11 | little-endian | unsigned | 0.00048828125 | 0 | - | 0 to 0.99951171875 |  | plausible |
| `DIF_a113_heatsink1Temp` | page 113 | Front drive inverter: a113 heatsink1 temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a113_heatsink2Temp` | page 113 | Front drive inverter: a113 heatsink2 temp | 32\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a113_heatsink3Temp` | page 113 | Front drive inverter: a113 heatsink3 temp | 48\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a117_torque` | page 117 | Front drive inverter: a117 torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_slaveCommand` | page 117 | Front drive inverter: a117 slave command | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_power` | page 117 | Front drive inverter: a117 power | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_slaveCommand2` | page 117 | Front drive inverter: a117 slave command2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_speed` | page 117 | Front drive inverter: a117 speed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_chassisControl` | page 117 | Front drive inverter: a117 chassis control | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_systemStatus` | page 117 | Front drive inverter: a117 system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_temperature` | page 117 | Front drive inverter: a117 temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_vehicle` | page 117 | Front drive inverter: a117 vehicle | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_AddTcLimit` | page 117 | Front drive inverter: a117 add tc limit | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_dixCommand` | page 117 | Front drive inverter: a117 dix command | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_odometerStatus` | page 117 | Front drive inverter: a117 odometer status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a119_hvpFaults` | page 119 | Front drive inverter: a119 hvp faults | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a120_dcLinkInfo` | page 120 | Front drive inverter: a120 dc link info | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a121_badRegReason` | page 121 | Front drive inverter: a121 bad reg reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `RMS_I_HIGH`<br>2 = `ID_OFF_TARGET`<br>3 = `IQ_OFF_TARGET`<br>4 = `FLUX_OFF_TARGET`<br>5 = `TORQUE_OFF_TARGET` | plausible |
| `DIF_a121_torqueDelta` | page 121 | Front drive inverter: a121 torque delta | 19\|13 | little-endian | signed | 0.25 | 0 | Nm | -1024 to 1023.75 |  | plausible |
| `DIF_a121_badCurrent` | page 121 | Front drive inverter: a121 bad current | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_a121_badFlux` | page 121 | Front drive inverter: a121 bad flux | 48\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | plausible |
| `DIF_a123_lossReason` | page 123 | Front drive inverter: a123 loss reason | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `NO_FLUX_UP`<br>2 = `HIGH_VAR_FLUX`<br>3 = `HIGH_VAR_CURR`<br>4 = `HIGH_FLUX_DISTURBANCE` | plausible |
| `DIF_a123_busVoltage` | page 123 | Front drive inverter: a123 bus voltage | 19\|6 | little-endian | unsigned | 4 | 250 | V | 250 to 502 |  | plausible |
| `DIF_a123_badFlux` | page 123 | Front drive inverter: a123 bad flux | 25\|7 | little-endian | unsigned | 0.0015 | 0 | Wb | 0 to 0.1905 |  | plausible |
| `DIF_a123_lossRequest` | page 123 | Front drive inverter: a123 loss request | 32\|7 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 12.7 |  | plausible |
| `DIF_a123_badCurrent` | page 123 | Front drive inverter: a123 bad current | 39\|9 | little-endian | signed | 10 | 0 | A | -2560 to 2550 |  | plausible |
| `DIF_a123_motorRPM` | page 123 | Front drive inverter: a123 motor RPM | 48\|8 | little-endian | signed | 150 | 0 | RPM | -19200 to 19050 |  | plausible |
| `DIF_a123_varianceD` | page 123 | Front drive inverter: a123 variance d | 56\|4 | little-endian | unsigned | 20 | 0 | A | 0 to 300 |  | plausible |
| `DIF_a123_varianceQ` | page 123 | Front drive inverter: a123 variance q | 60\|4 | little-endian | unsigned | 20 | 0 | A | 0 to 300 |  | plausible |
| `DIF_a126_limpReason` | page 126 | Front drive inverter: a126 limp reason | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `PHASE_IMBALANCE`<br>1 = `BUSV_SENSOR_IRRATIONAL`<br>2 = `NO_FUNC_STATORT_SENSOR`<br>3 = `NO_FUNC_HEATSINK_SENSOR`<br>4 = `NO_FLUID`<br>5 = `LV_SUPPLY_UNDERVOLTAGE`<br>6 = `BMS_MIA`<br>7 = `LOW_FLOW`<br>8 = `OUTLET_TEMP`<br>9 = `AMBIENT_TEMP`<br>10 = `DELTAT_TOO_POSITIVE`<br>11 = `DELTAT_TOO_NEGATIVE`<br>12 = `STATOR_TEMP`<br>13 = `WRONG_CS_CALIBRATION`<br>14 = `EXTERNAL_COMMAND`<br>15 = `TRQ_CROSS_CHECK`<br>16 = `PMHEARTBEAT`<br>17 = `PMREQUEST`<br>18 = `HEATSINK_TEMP`<br>19 = `CONFIG_MISMATCH`<br>20 = `DI_MIA`<br>21 = `TRQCMD_VALIDITY_UNKNOWN`<br>22 = `GTW_MIA`<br>23 = `CAPACITOR_OVERTEMP`<br>24 = `CONTACTOR_WELD`<br>25 = `SLAVE_REQUEST`<br>26 = `SLAVE_MIA`<br>27 = `FACTORY_GLIDER`<br>28 = `OIL_PUMP_FAILURE`<br>29 = `OIL_PUMP_FLUID_OVERTEMP`<br>30 = `HEATSINK_SENSOR_IRRATIONAL`<br>31 = `OIL_PRESSURE_LOW`<br>32 = `RESIST_STATOR_TEMP`<br>33 = `MOTION_IN_DYNO`<br>34 = `MECHANICAL_SAFE_ST_UNAVAIL`<br>35 = `CURRENT_CORE_FALLBACK`<br>36 = `XTAL_OSCILLATOR`<br>37 = `DEGRADED_REQUEST_SSFA`<br>38 = `DEGRADED_REQUEST_PSFA`<br>39 = `DEGRADED_REQUEST_SEPS`<br>40 = `DEGRADED_REQUEST_PEPS`<br>41 = `DEGRADED_REQUEST_VCLEFT`<br>42 = `DEGRADED_REQUEST_VCRIGHT`<br>43 = `UNIT_CHILL_REQUEST` | plausible |
| `DIF_a127_gpoReason` | page 127 | Front drive inverter: a127 gpo reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `OUTLET_OVERTEMP`<br>1 = `HEATSINK_OVERTEMP`<br>2 = `STATOR_OVERTEMP`<br>3 = `FLUID_DELTAT`<br>4 = `AMBIENT_OVERTEMP`<br>5 = `NO_BATTERY_POWER`<br>6 = `NOT_ENOUGH_12V`<br>7 = `CAPACITOR_OVERTEMP`<br>8 = `MOTOR_HALT_REQUEST`<br>9 = `MOTION_DURING_SPINDOWN_LEARNING`<br>10 = `SBW_NODE_UNAVAILABLE`<br>11 = `DEGRADED_LIMP_TIMEOUT`<br>12 = `DEGRADED_LIMP_NO_DECEL`<br>13 = `FACTORY_DRIVE_DISTANCE_EXCEEDED`<br>14 = `MOTION_EXPECTED_DURING_SPINDOWN_LEARNING`<br>15 = `MANUAL_RECOVERY_DISTANCE_EXCEEDED` | plausible |
| `DIF_a127_temp` | page 127 | Front drive inverter: a127 temp | 24\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a133_capacitorTemp` | page 133 | Front drive inverter: a133 capacitor temp | 16\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a133_badValue1` | page 133 | Front drive inverter: a133 bad value1 | 32\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a133_badValue2` | page 133 | Front drive inverter: a133 bad value2 | 48\|16 | little-endian | signed | 0.1 | 0 | C | -3276.8 to 3276.7 |  | plausible |
| `DIF_a134_wheelSpeedDiffFrL` | page 134 | Front drive inverter: a134 wheel speed diff fr l | 16\|12 | little-endian | signed | 0.0625 | 0 | kph | -128 to 127.9375 |  | plausible |
| `DIF_a134_wheelSpeedDiffFrR` | page 134 | Front drive inverter: a134 wheel speed diff fr r | 28\|12 | little-endian | signed | 0.0625 | 0 | kph | -128 to 127.9375 |  | plausible |
| `DIF_a134_wheelSpeedDiffReL` | page 134 | Front drive inverter: a134 wheel speed diff re l | 40\|12 | little-endian | signed | 0.0625 | 0 | kph | -128 to 127.9375 |  | plausible |
| `DIF_a134_wheelSpeedDiffReR` | page 134 | Front drive inverter: a134 wheel speed diff re r | 52\|12 | little-endian | signed | 0.0625 | 0 | kph | -128 to 127.9375 |  | plausible |
| `DIF_a136_spiError_BL` | page 136 | Front drive inverter: a136 spi error BL | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_BL` | page 136 | Front drive inverter: a136 crc error BL | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_BL` | page 136 | Front drive inverter: a136 busy error BL | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError_BH` | page 136 | Front drive inverter: a136 spi error BH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_BH` | page 136 | Front drive inverter: a136 crc error BH | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_BH` | page 136 | Front drive inverter: a136 busy error BH | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError_CL` | page 136 | Front drive inverter: a136 spi error CL | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_CL` | page 136 | Front drive inverter: a136 crc error CL | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_CL` | page 136 | Front drive inverter: a136 busy error CL | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError_CH` | page 136 | Front drive inverter: a136 spi error CH | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_CH` | page 136 | Front drive inverter: a136 crc error CH | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_CH` | page 136 | Front drive inverter: a136 busy error CH | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError_AL` | page 136 | Front drive inverter: a136 spi error AL | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_AL` | page 136 | Front drive inverter: a136 crc error AL | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_AL` | page 136 | Front drive inverter: a136 busy error AL | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError_AH` | page 136 | Front drive inverter: a136 spi error AH | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_crcError_AH` | page 136 | Front drive inverter: a136 crc error AH | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_busyError_AH` | page 136 | Front drive inverter: a136 busy error AH | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_autopilot` | page 144 | Front drive inverter: a144 autopilot | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_chassisType` | page 144 | Front drive inverter: a144 chassis type | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_drivetrainType` | page 144 | Front drive inverter: a144 drivetrain type | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_packEnergy` | page 144 | Front drive inverter: a144 pack energy | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_packPerformanceDeviation` | page 144 | Front drive inverter: a144 pack performance deviation | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_performancePackage` | page 144 | Front drive inverter: a144 performance package | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_vdcType` | page 144 | Front drive inverter: a144 vdc type | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_brakeHWType` | page 144 | Front drive inverter: a144 brake HW type | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_inverterHardware` | page 144 | Front drive inverter: a144 inverter hardware | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_cabinPTCHeaterType` | page 144 | Front drive inverter: a144 cabin PTC heater type | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_frunkLatchType` | page 144 | Front drive inverter: a144 frunk latch type | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_platformMaxBusVoltage` | page 144 | Front drive inverter: a144 platform max bus voltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_oilPump1HwType` | page 144 | Front drive inverter: a144 oil pump1 hw type | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_oilPump2HwType` | page 144 | Front drive inverter: a144 oil pump2 hw type | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_heatsinkType` | page 144 | Front drive inverter: a144 heatsink type | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_softPerformanceLimit` | page 144 | Front drive inverter: a144 soft performance limit | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_brakeActuationType` | page 144 | Front drive inverter: a144 brake actuation type | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_dasHw` | page 144 | Front drive inverter: a144 das hw | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_powerLiftgateType` | page 144 | Front drive inverter: a144 power liftgate type | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_chassisSubType` | page 144 | Front drive inverter: a144 chassis sub type | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_autonomyFeatureType` | page 144 | Front drive inverter: a144 autonomy feature type | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a147_overtorque1UsedCount` | page 147 | Front drive inverter: a147 overtorque1 used count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a147_overtorque2UsedCount` | page 147 | Front drive inverter: a147 overtorque2 used count | 24\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `DIF_a147_accumulatedWear` | page 147 | Front drive inverter: a147 accumulated wear | 34\|10 | little-endian | unsigned | 0.005 | 0 | 1 | 0 to 5.115 |  | plausible |
| `DIF_a147_wearIsValid` | page 147 | Front drive inverter: a147 wear is valid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_flow` | page 149 | Front drive inverter: a149 flow; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_a149_voltage` | page 149 | Front drive inverter: a149 voltage | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `DIF_a149_temperature` | page 149 | Front drive inverter: a149 temperature | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_a149_state` | page 149 | Front drive inverter: a149 state; raw 7 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `STANDBY`<br>1 = `ENABLE`<br>2 = `COLD_STARTUP`<br>6 = `FAULTED`<br>7 = `SNA` | plausible |
| `DIF_a149_fluidTempSNA` | page 149 | Front drive inverter: a149 fluid temp SNA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_insufficientFlow` | page 149 | Front drive inverter: a149 insufficient flow | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_motorOpenPhase` | page 149 | Front drive inverter: a149 motor open phase | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_motorShorted` | page 149 | Front drive inverter: a149 motor shorted | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_motorFlowSNA` | page 149 | Front drive inverter: a149 motor flow SNA | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_responseError` | page 149 | Front drive inverter: a149 response error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_pcbaID` | page 149 | Front drive inverter: a149 pcba ID | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LESS_THAN_5`<br>1 = `5` | plausible |
| `DIF_a150_vBatRawMinusFiltered` | page 150 | Front drive inverter: a150 v bat raw minus filtered | 16\|10 | little-endian | signed | 1 | 0 | V | -512 to 511 |  | plausible |
| `DIF_a150_vBatFilteredRate` | page 150 | Front drive inverter: a150 v bat filtered rate | 32\|8 | little-endian | signed | 100 | 0 | V/s | -12800 to 12700 |  | plausible |
| `DIF_a150_elapsedMs` | page 150 | Front drive inverter: a150 elapsed ms | 40\|8 | little-endian | unsigned | 1 | 0 | ms | 0 to 255 |  | plausible |
| `DIF_a150_energy` | page 150 | Front drive inverter: a150 energy | 48\|16 | little-endian | unsigned | 1 | 0 | J | 0 to 65535 |  | plausible |
| `DIF_a152_errorType` | page 152 | Front drive inverter: a152 error type | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ERROR`<br>1 = `FRAMING_ERROR`<br>2 = `CHECKSUM_ERROR`<br>3 = `SCHEDULE_ERROR`<br>4 = `OVERFLOW_ERROR`<br>5 = `HEADER_ERROR`<br>6 = `TIMEOUT_ERROR` | plausible |
| `DIF_a152_frameId` | page 152 | Front drive inverter: a152 frame id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a152_badValue` | page 152 | Front drive inverter: a152 bad value | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a152_expectedValue` | page 152 | Front drive inverter: a152 expected value | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIF_a154_motorRPM` | page 154 | Front drive inverter: a154 motor RPM | 16\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a154_phaseError` | page 154 | Front drive inverter: a154 phase error | 32\|8 | little-endian | signed | 0.004 | 0 | 1 | -0.512 to 0.508 |  | plausible |
| `DIF_a154_commonGain` | page 154 | Front drive inverter: a154 common gain | 40\|8 | little-endian | unsigned | 0.02 | 0 | 1 | 0 to 5.1 |  | plausible |
| `DIF_a154_noCalibration` | page 154 | Front drive inverter: a154 no calibration | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_noPhaseLock` | page 154 | Front drive inverter: a154 no phase lock | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_noCarrier` | page 154 | Front drive inverter: a154 no carrier | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_notReady` | page 154 | Front drive inverter: a154 not ready | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_errorTableInvalid` | page 154 | Front drive inverter: a154 error table invalid | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_carrierOffset` | page 154 | Front drive inverter: a154 carrier offset | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_trackerIrrational` | page 154 | Front drive inverter: a154 tracker irrational | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_claMIA` | page 154 | Front drive inverter: a154 cla MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_sensors` | page 155 | Front drive inverter: a155 sensors | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_coolant` | page 155 | Front drive inverter: a155 coolant | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_LVPowerState` | page 155 | Front drive inverter: a155 LV power state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_vehicleStatus` | page 155 | Front drive inverter: a155 vehicle status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_status` | page 155 | Front drive inverter: a155 status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_leftDoorStatus` | page 155 | Front drive inverter: a155 left door status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_rightDoorStatus` | page 155 | Front drive inverter: a155 right door status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_vcleftSwitchStatus` | page 155 | Front drive inverter: a155 vcleft switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_restraintStatus` | page 155 | Front drive inverter: a155 restraint status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_systemStatus` | page 155 | Front drive inverter: a155 system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_prndStatus` | page 155 | Front drive inverter: a155 prnd status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_liftgateStatus` | page 155 | Front drive inverter: a155 liftgate status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a157_RCM_inertial1` | page 157 | Front drive inverter: a157 RCM inertial1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a157_RCM_inertial2` | page 157 | Front drive inverter: a157 RCM inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a158_IBST_party1` | page 158 | Front drive inverter: a158 IBST party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a158_BUS1_IBST_status` | page 158 | Front drive inverter: a158 BUS1 IBST status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a158_BUS2_IBST_status` | page 158 | Front drive inverter: a158 BUS2 IBST status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a158_IBST_redundantBrakingStatus` | page 158 | Front drive inverter: a158 IBST redundant braking status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a160_vBatRawMinusFiltered` | page 160 | Front drive inverter: a160 v bat raw minus filtered | 16\|10 | little-endian | signed | 1 | 0 | V | -512 to 511 |  | plausible |
| `DIF_a160_vBatFilteredRate` | page 160 | Front drive inverter: a160 v bat filtered rate | 32\|8 | little-endian | signed | 100 | 0 | V/s | -12800 to 12700 |  | plausible |
| `DIF_a160_elapsedMs` | page 160 | Front drive inverter: a160 elapsed ms | 40\|8 | little-endian | unsigned | 1 | 0 | ms | 0 to 255 |  | plausible |
| `DIF_a160_energy` | page 160 | Front drive inverter: a160 energy | 48\|16 | little-endian | unsigned | 1 | 0 | J | 0 to 65535 |  | plausible |
| `DIF_a161_EPAS3P_sysStatus` | page 161 | Front drive inverter: a161 EPAS3 p sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a161_EPAS3P_angleCalib` | page 161 | Front drive inverter: a161 EPAS3 p angle calib | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a172_statorTemp1` | page 172 | Front drive inverter: a172 stator temp1 | 16\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a172_statorTemp2` | page 172 | Front drive inverter: a172 stator temp2 | 32\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `DIF_a202_reason` | page 202 | Front drive inverter: a202 reason | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `NO_ALERT`<br>2 = `PARKBRAKE`<br>3 = `MOVEMENT`<br>4 = `LIMP`<br>5 = `GPO`<br>6 = `UPDATE_STARTED`<br>7 = `SERVICE_MODE`<br>8 = `IMMEDIATE`<br>9 = `DRV_FAULT`<br>10 = `OPD`<br>11 = `CRUISE`<br>12 = `HV_DOWN` | plausible |
| `DIF_a202_movement` | page 202 | Front drive inverter: a202 movement | 20\|9 | little-endian | unsigned | 0.005 | 0 | m | 0 to 2.555 |  | plausible |
| `DIF_a202_sysStateExitCondition` | page 202 | Front drive inverter: a202 sys state exit condition | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `IDLE_VEHICLE_POWER_STATE_NOT_DRIVE`<br>1 = `IDLE_DRIVE_RAIL_NOT_REQUESTED`<br>2 = `IDLE_LV_OR_SBW_STATUS_NOT_READY`<br>3 = `IDLE_LV_OR_SBW_STATUS_LIMP`<br>4 = `IDLE_HV_NOT_UP_FOR_DRIVE`<br>5 = `IDLE_IMMOBILIZER_INHIBIT`<br>6 = `IDLE_FRUNK_NOT_LATCHED`<br>7 = `IDLE_PROX_DETECTED`<br>8 = `IDLE_FALCON_DOOR_OPEN`<br>9 = `IDLE_NON_ZERO_PEDAL_POS`<br>10 = `IDLE_BATTERY_POWER_LIMITS`<br>11 = `IDLE_FIRMWARE_VERIFICATION`<br>12 = `IDLE_EXIT_OK`<br>13 = `UNAVAILABLE_SLIM_GPO_OR_CAN_DRIVE_GOING_DOWN`<br>14 = `UNAVAILABLE_HV_IS_NOT_UP`<br>15 = `UNAVAILABLE_ALERTS_ACTIVE`<br>16 = `UNAVAILABLE_SSPD_SPEED_IS_NOT_PUBLISHED`<br>17 = `UNAVAILABLE_UNITS_NOT_AVAILABLE`<br>18 = `UNAVAILABLE_EXIT_OK`<br>19 = `IDLE_TRUNK_OPEN`<br>20 = `IDLE_USB_ETHERNET_CABLE_CONNECTED` | plausible |
| `DIF_a233_missedMsgCount` | page 233 | Front drive inverter: a233 missed msg count | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIF_a233_serviceModeActive` | page 233 | Signal reported by Front drive inverter | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a234_PCS_dcdcStatus` | page 234 | Front drive inverter: a234 PCS dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a236_states` | page 236 | Front drive inverter: a236 states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_shortedSwitches` | page 240 | Front drive inverter: a240 shorted switches | 16\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `DIF_a240_primaryPattern` | page 240 | Front drive inverter: a240 primary pattern | 22\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `DIF_a240_secondaryPattern` | page 240 | Front drive inverter: a240 secondary pattern | 28\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 |  | layout-only |
| `DIF_a240_fuseA_I2t` | page 240 | Front drive inverter: a240 fuse a i2t | 34\|6 | little-endian | unsigned | 8 | 0 | A^2s | 0 to 504 |  | plausible |
| `DIF_a240_fuseB_I2t` | page 240 | Front drive inverter: a240 fuse b i2t | 40\|6 | little-endian | unsigned | 8 | 0 | A^2s | 0 to 504 |  | plausible |
| `DIF_a240_primaryTimeout` | page 240 | Front drive inverter: a240 primary timeout | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_secondaryTimeout` | page 240 | Front drive inverter: a240 secondary timeout | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_primNoCurrentA` | page 240 | Front drive inverter: a240 prim no current a | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_primNoCurrentB` | page 240 | Front drive inverter: a240 prim no current b | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_secNoCurrentA` | page 240 | Front drive inverter: a240 sec no current a | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_secNoCurrentB` | page 240 | Front drive inverter: a240 sec no current b | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_primaryDutyCycle` | page 240 | Front drive inverter: a240 primary duty cycle | 52\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `DIF_a240_secondaryDutyCycle` | page 240 | Front drive inverter: a240 secondary duty cycle | 57\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `DIF_a240_confNoCurrentDetected` | page 240 | Front drive inverter: a240 conf no current detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a240_secondaryStrategy3ps` | page 240 | Front drive inverter: a240 secondary strategy3ps | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a242_RotorOffset` | page 242 | Front drive inverter: a242 rotor offset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a242_RotorFlux` | page 242 | Front drive inverter: a242 rotor flux | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a242_ResolverError` | page 242 | Front drive inverter: a242 resolver error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_desatHighSide` | page 244 | Front drive inverter: a244 desat high side | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_desatLowSide` | page 244 | Front drive inverter: a244 desat low side | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_singleSwitchShort` | page 244 | Front drive inverter: a244 single switch short | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_flybackFault` | page 244 | Front drive inverter: a244 flyback fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_postShortTestFailed` | page 244 | Front drive inverter: a244 post short test failed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_udsSelfTest` | page 244 | Front drive inverter: a244 uds self test | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_irSensorV` | page 244 | Front drive inverter: a244 ir sensor v | 24\|6 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6.3 |  | plausible |
| `DIF_a244_gateDriveICUndervoltage` | page 244 | Front drive inverter: a244 gate drive IC undervoltage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_plausibleSingleSwitchShortOnly` | page 244 | Front drive inverter: a244 plausible single switch short only | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a244_delay` | page 244 | Front drive inverter: a244 delay | 32\|16 | little-endian | unsigned | 1 | 0 | us | 0 to 65535 |  | plausible |
| `DIF_a246_atSpeedDIResetCount` | page 246 | Front drive inverter: a246 at speed DI reset count | 16\|4 | little-endian | unsigned | 1 | 4294967295 |  | 4294967295 to 4294967310 |  | layout-only |
| `DIF_a246_didPMCauseSwitchOffPathNominal` | page 246 | Front drive inverter: a246 did PM cause switch off path nominal | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_didPMCauseSwitchOffPathLowSpeed` | page 246 | Front drive inverter: a246 did PM cause switch off path low speed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_currentSensorRational` | page 246 | Front drive inverter: a246 current sensor rational | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_observerDetectedSwitchOffPathNominal` | page 246 | Front drive inverter: a246 observer detected switch off path nominal | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_observerDetectedSwitchOffPathLowSpeed` | page 246 | Front drive inverter: a246 observer detected switch off path low speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_hvIsGood` | page 246 | Front drive inverter: a246 hv is good | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_lvIsGood` | page 246 | Front drive inverter: a246 lv is good | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_codeBranch` | page 246 | Front drive inverter: a246 code branch | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `QUALIFICATION`<br>1 = `PSTG_INIT`<br>2 = `SAFESTATE_RELEASE_ASC`<br>3 = `SAFESTATE_RELEASE_LATCH` | plausible |
| `DIF_a246_motorRPM` | page 246 | Front drive inverter: a246 motor RPM | 32\|8 | little-endian | signed | 150 | 0 | RPM | -19200 to 19050 |  | plausible |
| `DIF_a246_eepromOffsetIa` | page 246 | Front drive inverter: a246 eeprom offset ia | 40\|6 | little-endian | signed | 0.763 | 0 | A | -24.416 to 23.653 |  | plausible |
| `DIF_a246_eepromOffsetIb` | page 246 | Front drive inverter: a246 eeprom offset ib | 48\|6 | little-endian | signed | 0.763 | 0 | A | -24.416 to 23.653 |  | plausible |
| `DIF_a246_soptPreviouslyPassed` | page 246 | Front drive inverter: a246 sopt previously passed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a246_lowSpeedRecoveryEnabled` | page 246 | Front drive inverter: a246 low speed recovery enabled | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a247_rotorOffsetEst` | page 247 | Front drive inverter: a247 rotor offset est | 16\|10 | little-endian | signed | 0.05 | 0 | degrees | -25.6 to 25.55 |  | plausible |
| `DIF_a247_motorRPM` | page 247 | Front drive inverter: a247 motor RPM | 32\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `DIF_a247_torqueMotor` | page 247 | Front drive inverter: a247 torque motor | 48\|16 | little-endian | signed | 1 | 0 | Nm | -32768 to 32767 |  | plausible |
| `DIF_a251_oilFlow` | page 251 | Front drive inverter: a251 oil flow; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_a251_oilTemperature` | page 251 | Front drive inverter: a251 oil temperature; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 214 | 255 = `SNA` | plausible |
| `DIF_a251_dcVoltage` | page 251 | Front drive inverter: a251 dc voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.3 | 0 | V | 0 to 76.2 | 255 = `SNA` | plausible |
| `DIF_a251_dcCurrent` | page 251 | Front drive inverter: a251 dc current; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_a251_phaseCurrent` | page 251 | Front drive inverter: a251 phase current; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.4 | 255 = `SNA` | plausible |
| `DIF_a251_leadAngle` | page 251 | Front drive inverter: a251 lead angle | 56\|4 | little-endian | unsigned | 1.875 | 0 | degrees | 0 to 28.125 |  | plausible |
| `DIF_a251_reason` | page 251 | Front drive inverter: a251 reason | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `PRESSURE_LOW`<br>2 = `PRESSURE_HIGH`<br>3 = `CURRENT_SENSOR`<br>4 = `INSUFFICIENT_FLOW` | plausible |
| `DIF_a253_voltage` | page 253 | Front drive inverter: a253 voltage | 16\|14 | little-endian | unsigned | 0.002 | 0 | V | 0 to 32.766 |  | plausible |
| `DIF_a253_reason` | page 253 | Front drive inverter: a253 reason | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `UNDERVOLTAGE`<br>2 = `OVERVOLTAGE` | plausible |

## Multiplexing

`DIF_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (43 signals), page 2 (43 signals), page 3 (43 signals), page 7 (7 signals), page 10 (15 signals), page 11 (12 signals), page 12 (8 signals), page 13 (2 signals), page 14 (7 signals), page 16 (10 signals), page 24 (7 signals), page 25 (3 signals), page 26 (3 signals), page 27 (3 signals), page 28 (3 signals), page 29 (3 signals), page 30 (3 signals), page 31 (1 signals), page 32 (1 signals), page 33 (3 signals), page 34 (3 signals), page 35 (11 signals), page 36 (2 signals), page 37 (2 signals), page 38 (4 signals), page 40 (7 signals), page 41 (4 signals), page 43 (1 signals), page 44 (1 signals), page 45 (4 signals), page 46 (2 signals), page 47 (2 signals), page 50 (2 signals), page 52 (7 signals), page 54 (2 signals), page 55 (4 signals), page 56 (1 signals), page 57 (1 signals), page 58 (4 signals), page 59 (1 signals), page 60 (1 signals), page 61 (4 signals), page 62 (1 signals), page 63 (1 signals), page 64 (2 signals), page 69 (4 signals), page 72 (1 signals), page 73 (1 signals), page 75 (2 signals), page 76 (1 signals), page 77 (1 signals), page 78 (2 signals), page 79 (2 signals), page 87 (5 signals), page 90 (6 signals), page 91 (8 signals), page 92 (11 signals), page 96 (8 signals), page 97 (3 signals), page 98 (2 signals), page 103 (8 signals), page 107 (5 signals), page 108 (3 signals), page 110 (4 signals), page 111 (2 signals), page 112 (6 signals), page 113 (3 signals), page 117 (12 signals), page 119 (1 signals), page 120 (1 signals), page 121 (4 signals), page 123 (8 signals), page 126 (1 signals), page 127 (2 signals), page 133 (3 signals), page 134 (4 signals), page 136 (18 signals), page 144 (21 signals), page 147 (4 signals), page 149 (11 signals), page 150 (4 signals), page 152 (4 signals), page 154 (11 signals), page 155 (12 signals), page 157 (2 signals), page 158 (4 signals), page 160 (4 signals), page 161 (2 signals), page 172 (2 signals), page 202 (3 signals), page 233 (2 signals), page 234 (1 signals), page 236 (1 signals), page 240 (15 signals), page 242 (3 signals), page 244 (10 signals), page 246 (14 signals), page 247 (3 signals), page 251 (7 signals), page 253 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
