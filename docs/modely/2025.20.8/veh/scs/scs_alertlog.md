---
layout: default
title: "SCS_alertLog (0x54A) — SCS ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "SCS ECU message: alert log. Tesla Model Y CAN bus message SCS_alertLog (0x54A) of SCS ECU, firmware 2025.20.8, 5 signals (SCS_alertID, SCS_alertType, SCS_a044_proximityV, SCS_a074_voltageWithRo and 1 more). Bit layout, scaling, units and value tables."
---

# SCS_alertLog (0x54A) — SCS ECU, Tesla Model Y 2025.20.8 VEH CAN

SCS ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of SCS_alertLog as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCS_alertLog` |
| CAN id | 0x54A (1354) |
| ECU | [SCS ECU](../../scs.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 5 |

## Signals of SCS_alertLog

Tesla Model Y CAN bus signals in `SCS_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCS_alertID` | selector | SCS ECU: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_hwDSPfault`<br>2 = `a002_hwIbatOC`<br>3 = `a003_hwCordOT`<br>4 = `a004_hwVbusOV`<br>5 = `a005_hwHVIL`<br>6 = `a006_hwWeld_V1`<br>7 = `a007_hwWeld_V2`<br>8 = `a008_hwIllegalCntrShoot`<br>9 = `a009_hwOpen_V1`<br>10 = `a010_hwOpen_V2`<br>11 = `a011_hwIllegalCntrCmdV1`<br>12 = `a012_hwIllegalCntrCmdV2`<br>13 = `a013_cordTempHiFoldBk`<br>14 = `a014_coolantTempHiFoldBk`<br>15 = `a015_cpldRationality`<br>16 = `a016_unusedHW16`<br>17 = `a017_unusedHW17`<br>18 = `a018_unusedHW18`<br>19 = `a019_unusedHW19`<br>20 = `a020_unusedHW20`<br>21 = `a021_unusedHW21`<br>24 = `a024_emergencyShutdown`<br>25 = `a025_internalIsolationFault`<br>26 = `a026_internalIsolationLow`<br>27 = `a027_externalIsolationLow`<br>28 = `a028_isolationRationality`<br>29 = `a029_VbatOV`<br>30 = `a030_VbusOV`<br>31 = `a031_IbatOC`<br>32 = `a032_VBatRationality`<br>33 = `a033_VBusRationality`<br>34 = `a034_IBatRationality`<br>35 = `a035_unexpectedVbusBehavior`<br>36 = `a036_internalContactorWelded`<br>37 = `a037_outputContactorWelded`<br>38 = `a038_contactorFailedOpen`<br>39 = `a039_ibatRegulation`<br>40 = `a040_plus12VOutOfRange`<br>41 = `a041_minus12VOutOfRange`<br>42 = `a042_pilotOutOfRange`<br>43 = `a043_pilotRationality`<br>44 = `a044_proximityRationality`<br>45 = `a045_pcbaOT`<br>46 = `a046_coolantOT`<br>47 = `a047_cordOT`<br>48 = `a048_ambientOT`<br>49 = `a049_pcbaTempRationality`<br>50 = `a050_coolantTempRationality`<br>51 = `a051_cordTempRationality`<br>52 = `a052_ambientTempRationality`<br>53 = `a053_unexpectedThermalBehavi`<br>54 = `a054_pumpRegulation`<br>55 = `a055_coolantLevelLow`<br>56 = `a056_stateTransitionDenied`<br>57 = `a057_watchdogReset`<br>58 = `a058_adcRef`<br>59 = `a059_memoryError`<br>60 = `a060_swHVIL`<br>61 = `a061_postOutOfService`<br>62 = `a062_unused`<br>63 = `a063_canRationality`<br>64 = `a064_vehicleCommandTimeout`<br>65 = `a065_vBatRationalityStage1`<br>66 = `a066_vBatRationalityStage2`<br>67 = `a067_vBatRationalityStage3`<br>68 = `a068_vBatRationalityStage4`<br>69 = `a069_vStageRationalityV1`<br>70 = `a070_vStageRationalityV2`<br>71 = `a071_chargerMIA`<br>72 = `a072_gtwMIA`<br>73 = `a073_lccMIA`<br>74 = `a074_isoVDiffHi`<br>75 = `a075_unused75`<br>76 = `a076_bmsMIA`<br>77 = `a077_unexpectedVbatBehavior`<br>78 = `a078_voltageMatchTimeout`<br>79 = `a079_unexpectedVbat`<br>80 = `a080_lccFaulted`<br>81 = `a081_rmsInputVoltageHigh`<br>82 = `a082_VbatUV`<br>83 = `a083_chargeCurrentLimited`<br>84 = `a084_unused84`<br>85 = `a085_unused85`<br>86 = `a086_lccResetDetected`<br>87 = `a087_posCordTempRationality`<br>88 = `a088_negCordTempRationality`<br>89 = `a089_posCordOT`<br>90 = `a090_negCordOT`<br>91 = `a091_voltageRiseDetection`<br>92 = `a092_cabEnableDeasserted`<br>93 = `a093_unused93`<br>94 = `a094_unused94`<br>95 = `a095_unused95`<br>96 = `a096_unused96`<br>97 = `a097_unused97`<br>98 = `a098_unused98`<br>99 = `a099_unused99`<br>100 = `a100_unused100`<br>101 = `a101_unused101`<br>102 = `a102_unused102`<br>103 = `a103_unused103`<br>104 = `a104_unused104`<br>105 = `a105_unused105`<br>106 = `a106_unused106`<br>107 = `a107_unused107`<br>108 = `a108_unused108`<br>109 = `a109_unused109`<br>110 = `a110_unused110`<br>111 = `a111_unused111`<br>112 = `a112_unused112`<br>113 = `a113_unused113`<br>114 = `a114_unused114`<br>115 = `a115_unused115`<br>116 = `a116_unused116`<br>117 = `a117_unused117`<br>118 = `a118_unused118`<br>119 = `a119_unused119`<br>120 = `a120_unused120`<br>121 = `a121_unused121`<br>122 = `a122_unused122`<br>123 = `a123_unused123`<br>124 = `a124_unused124`<br>125 = `a125_unused125`<br>126 = `a126_unused126`<br>127 = `a127_unused127`<br>128 = `a128_unused128` | plausible |
| `SCS_alertType` |  | SCS ECU: alert type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `SCS_a044_proximityV` | page 44 | SCS ECU: a044 proximity v | 16\|16 | little-endian | unsigned | 0.0001 | 0 | V | 0 to 6.5535 |  | plausible |
| `SCS_a074_voltageWithRo` | page 74 | SCS ECU: a074 voltage with ro | 16\|12 | little-endian | unsigned | 0.146520152688 | 0 | V | 0 to 600.000025257 |  | plausible |
| `SCS_a074_voltageWithoutRo` | page 74 | SCS ECU: a074 voltage without ro | 28\|12 | little-endian | unsigned | 0.146520152688 | 0 | V | 0 to 600.000025257 |  | plausible |

## Multiplexing

`SCS_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 44 (1 signals), page 74 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All SCS ECU messages (SCS)](../../scs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
