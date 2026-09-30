---
layout: default
title: "IDB_alertLog (0x5BE) — IDB ECU, Tesla Model 3 2025.20.8 ETH"
description: "IDB ECU message: alert log. Ethernet-side message IDB_alertLog of IDB ECU for Tesla Model 3 firmware 2025.20.8, 101 signals (IDB_alertID, IDB_alertState, IDB_a014_wheelSpeedSensorFreq, IDB_a014_wheelSpeedSensorPhase and 97 more). Bit layout, scaling, units and value tables."
---

# IDB_alertLog (0x5BE) — IDB ECU, Tesla Model 3 2025.20.8 ETH

IDB ECU message: alert log. This page documents the 101 signals of IDB_alertLog as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `IDB_alertLog` |
| Ethernet-side id | 0x5BE (1470) |
| ECU | [IDB ECU](../../idb.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | IDB |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 101 |

## Signals of IDB_alertLog

Tesla Model 3 CAN bus signals in `IDB_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `IDB_alertID` | selector | IDB ECU: alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_mcuGenericFault`<br>2 = `a002_supplyOvervoltage`<br>3 = `a003_supplyHardOvervoltage`<br>4 = `a004_supplyUndervoltage`<br>5 = `a005_supplyMidUndervoltage`<br>6 = `a006_supplyHardUndervoltage`<br>7 = `a007_wakeLineOpen`<br>8 = `a008_motorPowerOpen`<br>9 = `a009_asicBoostFault`<br>10 = `a010_asicGenericFault`<br>11 = `a011_solenoidValveFault`<br>12 = `a012_motorGenericFault`<br>13 = `a013_motorPosSensorFault`<br>14 = `a014_FrLWSSFault`<br>15 = `a015_FrRWSSFault`<br>16 = `a016_ReLWSSFault`<br>17 = `a017_ReRWSSFault`<br>18 = `a018_WSSGenericFault`<br>19 = `a019_pedalSensorFault`<br>20 = `a020_RCUpedalTravelMismatch`<br>21 = `a021_pedalSensorNotCal`<br>22 = `a022_brakeFluidLow`<br>23 = `a023_steeringImplausible`<br>24 = `a024_yawImplausible`<br>25 = `a025_ayImplausible`<br>26 = `a026_axImplausible`<br>27 = `a027_circuitPresSensorFault`<br>28 = `a028_simPresSensorFault`<br>29 = `a029_pressureSensNotCal`<br>30 = `a030_fluidLeakDetected`<br>31 = `a031_solenoidValveStuck`<br>32 = `a032_motorSoftOverheat`<br>33 = `a033_motorHardOverheat`<br>34 = `a034_motorPositionSetFault`<br>35 = `a035_motorStuck`<br>36 = `a036_partyBusOff`<br>37 = `a037_chassisBusOff`<br>38 = `a038_motorInitFault`<br>39 = `a039_absActive`<br>40 = `a040_ebdActive`<br>41 = `a041_vdcActive`<br>42 = `a042_btcActive`<br>43 = `a043_DItorquePathActive`<br>44 = `a044_standstillSkidDetected`<br>45 = `a045_panicBrakeAssistActive`<br>46 = `a046_fadeCompensationActive`<br>47 = `a047_brakeDiscWipeActive`<br>48 = `a048_scmActive`<br>49 = `a049_cdpActive`<br>50 = `a050_absFaulted`<br>51 = `a051_ebdFaulted`<br>52 = `a052_vdcFaulted`<br>53 = `a053_DItorquePathFaulted`<br>54 = `a054_skidDetectionFaulted`<br>55 = `a055_panicBrakeAssistFaulted`<br>56 = `a056_fadeCompensationFaulted`<br>57 = `a057_bdwRequestInvalid`<br>58 = `a058_scmFaulted`<br>59 = `a059_cdpFaulted`<br>60 = `a060_RCUstatusDLC`<br>61 = `a061_RCUstatusChecksum`<br>62 = `a062_RCUstatusCounter`<br>63 = `a063_RCUactuationDLC`<br>64 = `a064_RCUactuationChecksum`<br>65 = `a065_RCUactuationCounter`<br>66 = `a066_DIFtorqueDLC`<br>67 = `a067_DIFtorqueChecksum`<br>68 = `a068_DIFtorqueCounter`<br>69 = `a069_DIchassisControlDLC`<br>70 = `a070_DIchassisControlChecksum`<br>71 = `a071_DIchassisControlCounter`<br>72 = `a072_DIsystemStatusDLC`<br>73 = `a073_DIsystemStatusChecksum`<br>74 = `a074_DIsystemStatusCounter`<br>75 = `a075_DIRtorqueDLC`<br>76 = `a076_DIRtorqueChecksum`<br>77 = `a077_DIRtorqueCounter`<br>78 = `a078_DIvdcLeftDLC`<br>79 = `a079_DIvdcLeftChecksum`<br>80 = `a080_DIvdcLeftCounter`<br>81 = `a081_DIvdcRightDLC`<br>82 = `a082_DIvdcRightChecksum`<br>83 = `a083_DIvdcRightCounter`<br>84 = `a084_EPAS3PsysStatusDLC`<br>85 = `a085_EPAS3PsysStatusChecksum`<br>86 = `a086_EPAS3PsysStatusCounter`<br>87 = `a087_PMstate2DLC`<br>88 = `a088_PMstate2Checksum`<br>89 = `a089_PMstate2Counter`<br>90 = `a090_RCMinertial1DLC`<br>91 = `a091_RCMinertial1Checksum`<br>92 = `a092_RCMinertial1Counter`<br>93 = `a093_RCMinertial2DLC`<br>94 = `a094_RCMinertial2Checksum`<br>95 = `a095_RCMinertial2Counter`<br>96 = `a096_VCFRONTLVPowerStateDLC`<br>97 = `a097_VCFRONTLVPwrStChecksum`<br>98 = `a098_VCFRONTLVPwrStCounter`<br>99 = `a099_RCMcollisionDLC`<br>100 = `a100_RCMcollisionChecksum`<br>101 = `a101_RCMcollisionCounter`<br>102 = `a102_bdwRequestActiveInvalid`<br>103 = `a103_DIfullTorquePathFaulted`<br>104 = `a104_DIaccelPosInvalid`<br>105 = `a105_DIgearInvalid`<br>106 = `a106_DIFtorqueInvalid`<br>107 = `a107_DIRtorqueInvalid`<br>108 = `a108_EPBstatusDLC`<br>109 = `a109_BDWsignalInvalid`<br>110 = `a110_EPBstatusCounter`<br>111 = `a111_EPBstatusChecksum`<br>112 = `a112_yawRateInvalid`<br>113 = `a113_latAccelInvalid`<br>114 = `a114_longAccelInvalid`<br>115 = `a115_VCFRONTespLvStInvalid`<br>116 = `a116_VCFRONTsensorsDLC`<br>117 = `a117_VCLEFTepbmStatusDLC`<br>118 = `a118_VCLEFTepbmStatusCounter`<br>119 = `a119_VCLEFTepbmStatusChecksum`<br>120 = `a120_EPAS3Pinvalid`<br>121 = `a121_dynoModeActive`<br>122 = `a122_DIFtorqueCommandInvalid`<br>123 = `a123_DIRtorqueCommandInvalid`<br>124 = `a124_VCFRONTtempInvalid`<br>125 = `a125_PMvdcCmdStateInvalid`<br>126 = `a126_DItorqueRequestInvalid`<br>127 = `a127_brakeFluidLevelInvalid`<br>128 = `a128_reserved1`<br>129 = `a129_RCUinputRodStrokeInvalid`<br>130 = `a130_DIfullTorqueRequestInvalid`<br>131 = `a131_DIfullTorquePathActive`<br>132 = `a132_RCUinputRodStrokeQFInvalid`<br>133 = `a133_DIbrakeCommandDLC`<br>134 = `a134_DIbrakeCommandCounter`<br>135 = `a135_DIbrakeCommandChecksum`<br>136 = `a136_RCUptsCalMissing`<br>137 = `a137_VCLEFTcdpRequestInvalid`<br>138 = `a138_DIbrakeTorqueCommandAndFlagMismatch`<br>139 = `a139_DIbrakeTorqueCommandFullSNA`<br>140 = `a140_PMbrakePedalCmdQFInvalid`<br>141 = `a141_DIbrakeTorqueCommandFullTooLow`<br>142 = `a142_PMebrCmdStateInvalid`<br>143 = `a143_factoryModeActive`<br>144 = `a144_hydraulicPushthroughActive` | plausible |
| `IDB_alertState` |  | IDB ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `IDB_a014_wheelSpeedSensorFreq` | page 14 | IDB ECU: a014 wheel speed sensor freq | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorPhase` | page 14 | IDB ECU: a014 wheel speed sensor phase | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorMisinstallation` | page 14 | IDB ECU: a014 wheel speed sensor misinstallation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorWrongExciter` | page 14 | IDB ECU: a014 wheel speed sensor wrong exciter | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorSpeedJumpMinus` | page 14 | IDB ECU: a014 wheel speed sensor speed jump minus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorSpeedJumpPlus` | page 14 | IDB ECU: a014 wheel speed sensor speed jump plus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorAirGap` | page 14 | IDB ECU: a014 wheel speed sensor air gap | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorBIST` | page 14 | IDB ECU: a014 wheel speed sensor BIST | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorLeakageCur` | page 14 | IDB ECU: a014 wheel speed sensor leakage cur | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorOverTemp` | page 14 | IDB ECU: a014 wheel speed sensor over temp | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorShortToGnd` | page 14 | IDB ECU: a014 wheel speed sensor short to gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorShortToBat` | page 14 | IDB ECU: a014 wheel speed sensor short to bat | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a014_wheelSpeedSensorOpen` | page 14 | IDB ECU: a014 wheel speed sensor open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorFreq` | page 15 | IDB ECU: a015 wheel speed sensor freq | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorPhase` | page 15 | IDB ECU: a015 wheel speed sensor phase | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorMisinstallation` | page 15 | IDB ECU: a015 wheel speed sensor misinstallation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorWrongExciter` | page 15 | IDB ECU: a015 wheel speed sensor wrong exciter | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorSpeedJumpMinus` | page 15 | IDB ECU: a015 wheel speed sensor speed jump minus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorSpeedJumpPlus` | page 15 | IDB ECU: a015 wheel speed sensor speed jump plus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorAirGap` | page 15 | IDB ECU: a015 wheel speed sensor air gap | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorBIST` | page 15 | IDB ECU: a015 wheel speed sensor BIST | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorLeakageCur` | page 15 | IDB ECU: a015 wheel speed sensor leakage cur | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorOverTemp` | page 15 | IDB ECU: a015 wheel speed sensor over temp | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorShortToGnd` | page 15 | IDB ECU: a015 wheel speed sensor short to gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorShortToBat` | page 15 | IDB ECU: a015 wheel speed sensor short to bat | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a015_wheelSpeedSensorOpen` | page 15 | IDB ECU: a015 wheel speed sensor open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorFreq` | page 16 | IDB ECU: a016 wheel speed sensor freq | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorPhase` | page 16 | IDB ECU: a016 wheel speed sensor phase | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorMisinstallation` | page 16 | IDB ECU: a016 wheel speed sensor misinstallation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorWrongExciter` | page 16 | IDB ECU: a016 wheel speed sensor wrong exciter | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorSpeedJumpMinus` | page 16 | IDB ECU: a016 wheel speed sensor speed jump minus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorSpeedJumpPlus` | page 16 | IDB ECU: a016 wheel speed sensor speed jump plus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorAirGap` | page 16 | IDB ECU: a016 wheel speed sensor air gap | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorBIST` | page 16 | IDB ECU: a016 wheel speed sensor BIST | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorLeakageCur` | page 16 | IDB ECU: a016 wheel speed sensor leakage cur | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorOverTemp` | page 16 | IDB ECU: a016 wheel speed sensor over temp | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorShortToGnd` | page 16 | IDB ECU: a016 wheel speed sensor short to gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorShortToBat` | page 16 | IDB ECU: a016 wheel speed sensor short to bat | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a016_wheelSpeedSensorOpen` | page 16 | IDB ECU: a016 wheel speed sensor open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorFreq` | page 17 | IDB ECU: a017 wheel speed sensor freq | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorPhase` | page 17 | IDB ECU: a017 wheel speed sensor phase | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorMisinstallation` | page 17 | IDB ECU: a017 wheel speed sensor misinstallation | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorWrongExciter` | page 17 | IDB ECU: a017 wheel speed sensor wrong exciter | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorSpeedJumpMinus` | page 17 | IDB ECU: a017 wheel speed sensor speed jump minus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorSpeedJumpPlus` | page 17 | IDB ECU: a017 wheel speed sensor speed jump plus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorAirGap` | page 17 | IDB ECU: a017 wheel speed sensor air gap | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorBIST` | page 17 | IDB ECU: a017 wheel speed sensor BIST | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorLeakageCur` | page 17 | IDB ECU: a017 wheel speed sensor leakage cur | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorOverTemp` | page 17 | IDB ECU: a017 wheel speed sensor over temp | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorShortToGnd` | page 17 | IDB ECU: a017 wheel speed sensor short to gnd | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorShortToBat` | page 17 | IDB ECU: a017 wheel speed sensor short to bat | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a017_wheelSpeedSensorOpen` | page 17 | IDB ECU: a017 wheel speed sensor open | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a020_canSignalValidity` | page 20 | IDB ECU: a020 can signal validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a020_signalValueCrosscheck` | page 20 | IDB ECU: a020 signal value crosscheck | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_primaryExternalCircuitLeakage` | page 30 | IDB ECU: a030 primary external circuit leakage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_secondaryExternalCircuitLeakage` | page 30 | IDB ECU: a030 secondary external circuit leakage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_primaryChamberInternalLeakage` | page 30 | IDB ECU: a030 primary chamber internal leakage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_syncModeInternalLeakage` | page 30 | IDB ECU: a030 sync mode internal leakage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_secondaryChamberInternalLeakage` | page 30 | IDB ECU: a030 secondary chamber internal leakage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a030_masterCylinderInternalLeakage` | page 30 | IDB ECU: a030 master cylinder internal leakage | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a060_validityOnChassisBus` | page 60 | IDB ECU: a060 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a060_validityOnPartyBus` | page 60 | IDB ECU: a060 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a061_validityOnChassisBus` | page 61 | IDB ECU: a061 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a061_validityOnPartyBus` | page 61 | IDB ECU: a061 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a062_validityOnChassisBus` | page 62 | IDB ECU: a062 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a062_validityOnPartyBus` | page 62 | IDB ECU: a062 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a063_validityOnChassisBus` | page 63 | IDB ECU: a063 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a063_validityOnPartyBus` | page 63 | IDB ECU: a063 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a064_validityOnChassisBus` | page 64 | IDB ECU: a064 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a064_validityOnPartyBus` | page 64 | IDB ECU: a064 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a065_validityOnChassisBus` | page 65 | IDB ECU: a065 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a065_validityOnPartyBus` | page 65 | IDB ECU: a065 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a106_qualifierValidity` | page 106 | IDB ECU: a106 qualifier validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a106_signalNotAvailable` | page 106 | IDB ECU: a106 signal not available | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a107_qualifierValidity` | page 107 | IDB ECU: a107 qualifier validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a107_signalNotAvailable` | page 107 | IDB ECU: a107 signal not available | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a112_qualifierValidity` | page 112 | IDB ECU: a112 qualifier validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a112_signalNotAvailable` | page 112 | IDB ECU: a112 signal not available | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a113_qualifierValidity` | page 113 | IDB ECU: a113 qualifier validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a113_signalNotAvailable` | page 113 | IDB ECU: a113 signal not available | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a114_qualifierValidity` | page 114 | IDB ECU: a114 qualifier validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a114_signalNotAvailable` | page 114 | IDB ECU: a114 signal not available | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_PMebrCmdStateValidity` | page 126 | IDB ECU: a126 p mebr cmd state validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_PMstate2Validity` | page 126 | IDB ECU: a126 p mstate2 validity | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_PMstate2Missing` | page 126 | IDB ECU: a126 p mstate2 missing | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_DIchassisControlValidity` | page 126 | IDB ECU: a126 d ichassis control validity | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_DIchassisControlMissing` | page 126 | IDB ECU: a126 d ichassis control missing | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a126_DIrequestActiveValidity` | page 126 | IDB ECU: a126 d irequest active validity | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a129_validityOnChassisBus` | page 129 | IDB ECU: a129 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a129_validityOnPartyBus` | page 129 | IDB ECU: a129 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_PMbrakePedalCmdQFValidity` | page 130 | IDB ECU: a130 p mbrake pedal cmd QF validity | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_PMstate2Validity` | page 130 | IDB ECU: a130 p mstate2 validity | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_PMstate2Missing` | page 130 | IDB ECU: a130 p mstate2 missing | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_DIbrakeCommandValidity` | page 130 | IDB ECU: a130 d ibrake command validity | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_DIbrakeCommandMissing` | page 130 | IDB ECU: a130 d ibrake command missing | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_DIbrakeTorqueCommandFullSNA` | page 130 | IDB ECU: a130 d ibrake torque command full SNA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a130_DIbrakeTorqueCommandFullTooLow` | page 130 | IDB ECU: a130 d ibrake torque command full too low | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a132_validityOnChassisBus` | page 132 | IDB ECU: a132 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `IDB_a132_validityOnPartyBus` | page 132 | IDB ECU: a132 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |

## Multiplexing

`IDB_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 14 (13 signals), page 15 (13 signals), page 16 (13 signals), page 17 (13 signals), page 20 (2 signals), page 30 (6 signals), page 60 (2 signals), page 61 (2 signals), page 62 (2 signals), page 63 (2 signals), page 64 (2 signals), page 65 (2 signals), page 106 (2 signals), page 107 (2 signals), page 112 (2 signals), page 113 (2 signals), page 114 (2 signals), page 126 (6 signals), page 129 (2 signals), page 130 (7 signals), page 132 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All IDB ECU messages (IDB)](../../idb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
