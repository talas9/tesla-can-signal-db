---
layout: default
title: "RCM_alertLog (0x511) — Restraint control module, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Restraint control module message: alert log. Ethernet-side message RCM_alertLog of Restraint control module for Tesla Model 3 / Model Y firmware 2026.26.6.5, 1566 signals (RCM_alertID, RCM_alertState, RCM_a000_eventArmStatus, RCM_a000_eventFactoryMode and 1562 more). Bit layout, scaling, units and value tables."
---

# RCM_alertLog (0x511) — Restraint control module, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Restraint control module message: alert log. This page documents the 1566 signals of RCM_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_alertLog` |
| Ethernet-side id | 0x511 (1297) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1566 |

## Signals of RCM_alertLog

Tesla Model 3 / Model Y CAN bus signals in `RCM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_alertID` | selector | Restraint control module: alert ID | 0\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 | 0 = `a000_crashDetected`<br>1 = `a001_nearDeploy`<br>2 = `a002_airbagsNotArmed`<br>3 = `a003_warningIndicator`<br>4 = `a004_internalFault`<br>5 = `a005_crcError`<br>6 = `a006_batteryVoltageRange`<br>7 = `a007_powerSupplyExternal`<br>8 = `a008_powerSupplyInternal`<br>9 = `a009_reprogramLimit`<br>10 = `a010_scmDisabled`<br>11 = `a011_eepromDataLocked`<br>12 = `a012_vinStorage`<br>13 = `a013_driverOrientation`<br>14 = `a014_driverABStage1`<br>15 = `a015_driverABStage2`<br>16 = `a016_passABStage1`<br>17 = `a017_passABStage2`<br>18 = `a018_passengerActiveVent`<br>19 = `a019_pretenShldrFrontLeft`<br>20 = `a020_pretenShldFrontRight`<br>21 = `a021_pretenLapFrontLeft`<br>22 = `a022_pretenLapFrontRight`<br>23 = `a023_loadLimiterLeftSide`<br>24 = `a024_loadLimiterRightSide`<br>25 = `a025_kneeABDriver`<br>26 = `a026_kneeABFrontPassenger`<br>27 = `a027_sideAB1stRowLeft`<br>28 = `a028_sideAB1stRowRight`<br>29 = `a029_driverABActiveVent`<br>30 = `a030_farSideInboardAirbag`<br>31 = `a031_frontCenterAirbag`<br>32 = `a032_curtainABLeft`<br>33 = `a033_curtainABRight`<br>34 = `a034_preten2ndRowLeft`<br>35 = `a035_preten2ndRowRight`<br>36 = `a036_curAB2ndRowLeft`<br>37 = `a037_curAB2ndRowRight`<br>38 = `a038_unusedA`<br>39 = `a039_unusedB`<br>40 = `a040_hoodActuatorRight`<br>41 = `a041_hoodActuatorLeft`<br>42 = `a042_ens1Line`<br>43 = `a043_ens2Line`<br>44 = `a044_upFrontSensorLeft`<br>45 = `a045_upFrontSensorRight`<br>46 = `a046_sideAccelBPillarLeft`<br>47 = `a047_sideAccelBPillarRight`<br>48 = `a048_sideAccelCPillarLeft`<br>49 = `a049_sideAccelCPillarRight`<br>50 = `a050_upFrontSensorCenter`<br>51 = `a051_pressureFrontLftDoor`<br>52 = `a052_pressureFrontRtDoor`<br>53 = `a053_pressurePedProLeft`<br>54 = `a054_pressurePedProRight`<br>55 = `a055_inertialMeasurement`<br>56 = `a056_passengerFrontOCS`<br>57 = `a057_driverOCS`<br>58 = `a058_buckle1stRowLeft`<br>59 = `a059_buckle1stRowRight`<br>60 = `a060_stpsLeft`<br>61 = `a061_stpsRight`<br>62 = `a062_alrSwitch`<br>63 = `a063_sbsw2ndRowRight`<br>64 = `a064_hardwareCodingPin1`<br>65 = `a065_driverOrientConfigPin`<br>66 = `a066_seatBackSw2ndRowLeft`<br>67 = `a067_comCANInitFailure`<br>68 = `a068_comChassisBusOff`<br>69 = `a069_comCHCANPH7`<br>70 = `a070_comCHCANPH8`<br>71 = `a071_comCHCANPH9`<br>72 = `a072_comUnused`<br>73 = `a073_comCHCANPH4`<br>74 = `a074_comCHCANPH5`<br>75 = `a075_comCHCANPH6`<br>76 = `a076_comEPBLStatus`<br>77 = `a077_comEPBRStatus`<br>78 = `a078_comOCS1PStatus`<br>79 = `a079_comOCS1DStatus`<br>80 = `a080_comGTWACS`<br>81 = `a081_comVCFRONTLVPwr`<br>82 = `a082_comUIodo`<br>83 = `a083_comGTWCarState`<br>84 = `a084_comTPMSStatus`<br>85 = `a085_comGTWCarConfig`<br>86 = `a086_comVINMIA`<br>87 = `a087_comCANSilent`<br>88 = `a088_comCHCANPH2`<br>89 = `a089_comCHCANPH3`<br>90 = `a090_comPartyBusOff`<br>91 = `a091_comEPAS3PsysStatus`<br>92 = `a092_comDASISF`<br>93 = `a093_comVCLEFTStatus`<br>94 = `a094_comVCRIGHTStatus`<br>95 = `a095_comESPstatus`<br>96 = `a096_comESPwheelSpeeds`<br>97 = `a097_comDIspeed`<br>98 = `a098_comDIchassisControl`<br>99 = `a099_comDItorque`<br>100 = `a100_comDIsystemStatus`<br>101 = `a101_idfSystem`<br>102 = `a102_imuYawR8OffstCompLim`<br>103 = `a103_imuPtchR8OffstCompLim`<br>104 = `a104_imuRollR8OffstCompLim`<br>105 = `a105_imuLongAccOffstCompLim`<br>106 = `a106_imuLatAccOffstCompLim`<br>107 = `a107_imuVertAccOffstCompLim`<br>108 = `a108_crashAlgoWakeup`<br>109 = `a109_abuseImmunity`<br>110 = `a110_factoryMode`<br>111 = `a111_diagnosticsEnabled`<br>112 = `a112_imuYawRate`<br>113 = `a113_imuPitchRate`<br>114 = `a114_imuRollRate`<br>115 = `a115_imuLinearAcceleration`<br>116 = `a116_imuLateralAcceleration`<br>117 = `a117_imuVerticalAcceleration`<br>118 = `a118_imuInPlaneAcceleration` | plausible |
| `RCM_alertState` |  | Restraint control module: alert state | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `RCM_a000_eventArmStatus` | page 0 | Restraint control module: a000 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a000_eventFactoryMode` | page 0 | Restraint control module: a000 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a000_eventDiagEnabled` | page 0 | Restraint control module: a000 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a000_eventDriveOrientation` | page 0 | Restraint control module: a000 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a000_crashDetectedFront` | page 0 | Restraint control module: a000 crash detected front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedRear` | page 0 | Restraint control module: a000 crash detected rear | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedLeft` | page 0 | Restraint control module: a000 crash detected left | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedRight` | page 0 | Restraint control module: a000 crash detected right | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedRoll` | page 0 | Restraint control module: a000 crash detected roll | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedPreten` | page 0 | Restraint control module: a000 crash detected preten | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedStage1` | page 0 | Restraint control module: a000 crash detected stage1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedStage2` | page 0 | Restraint control module: a000 crash detected stage2 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_crashDetectedHVpyro` | page 0 | Restraint control module: a000 crash detected h vpyro | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a000_eventIDFsignal` | page 0 | Restraint control module: a000 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a000_eventFrontLeftSeatbelt` | page 0 | Restraint control module: a000 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a000_eventFrontRightSeatbelt` | page 0 | Restraint control module: a000 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a000_eventVehicleSpeed` | page 0 | Restraint control module: a000 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a000_eventSteeringAngle` | page 0 | Restraint control module: a000 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a000_eventDriverBrakeApply` | page 0 | Restraint control module: a000 event driver brake apply | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a000_eventAccelPedalPos` | page 0 | Restraint control module: a000 event accel pedal pos | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 | 255 = `SNA` | plausible |
| `RCM_a001_eventArmStatus` | page 1 | Restraint control module: a001 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a001_eventFactoryMode` | page 1 | Restraint control module: a001 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a001_eventDiagEnabled` | page 1 | Restraint control module: a001 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a001_eventDriveOrientation` | page 1 | Restraint control module: a001 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a001_nearDeployFront` | page 1 | Restraint control module: a001 near deploy front | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeployRear` | page 1 | Restraint control module: a001 near deploy rear | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeployLeft` | page 1 | Restraint control module: a001 near deploy left | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeployRight` | page 1 | Restraint control module: a001 near deploy right | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeployRoll` | page 1 | Restraint control module: a001 near deploy roll | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeployPretensioner` | page 1 | Restraint control module: a001 near deploy pretensioner | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_eventIDFsignal` | page 1 | Restraint control module: a001 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a001_eventFrontLeftSeatbelt` | page 1 | Restraint control module: a001 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a001_eventFrontRightSeatbelt` | page 1 | Restraint control module: a001 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a001_eventVehicleSpeed` | page 1 | Restraint control module: a001 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a001_eventSteeringAngle` | page 1 | Restraint control module: a001 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a001_eventDriverBrakeApply` | page 1 | Restraint control module: a001 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a001_eventAccelPedalPos` | page 1 | Restraint control module: a001 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a002_eventArmStatus` | page 2 | Restraint control module: a002 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a002_eventFactoryMode` | page 2 | Restraint control module: a002 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a002_eventDiagEnabled` | page 2 | Restraint control module: a002 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a002_eventDriveOrientation` | page 2 | Restraint control module: a002 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a002_airbagsUnArmed` | page 2 | Restraint control module: a002 airbags un armed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a002_eventIDFsignal` | page 2 | Restraint control module: a002 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a002_eventFrontLeftSeatbelt` | page 2 | Restraint control module: a002 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a002_eventFrontRightSeatbelt` | page 2 | Restraint control module: a002 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a002_eventVehicleSpeed` | page 2 | Restraint control module: a002 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a002_eventSteeringAngle` | page 2 | Restraint control module: a002 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a002_eventDriverBrakeApply` | page 2 | Restraint control module: a002 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a002_eventAccelPedalPos` | page 2 | Restraint control module: a002 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a003_eventArmStatus` | page 3 | Restraint control module: a003 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a003_eventFactoryMode` | page 3 | Restraint control module: a003 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a003_eventDiagEnabled` | page 3 | Restraint control module: a003 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a003_eventDriveOrientation` | page 3 | Restraint control module: a003 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a003_warningIndicatorOn` | page 3 | Restraint control module: a003 warning indicator on | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a003_eventIDFsignal` | page 3 | Restraint control module: a003 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a003_eventFrontLeftSeatbelt` | page 3 | Restraint control module: a003 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a003_eventFrontRightSeatbelt` | page 3 | Restraint control module: a003 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a003_eventVehicleSpeed` | page 3 | Restraint control module: a003 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a003_eventSteeringAngle` | page 3 | Restraint control module: a003 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a003_eventDriverBrakeApply` | page 3 | Restraint control module: a003 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a003_eventAccelPedalPos` | page 3 | Restraint control module: a003 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a004_eventArmStatus` | page 4 | Restraint control module: a004 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a004_eventFactoryMode` | page 4 | Restraint control module: a004 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a004_eventDiagEnabled` | page 4 | Restraint control module: a004 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a004_eventDriveOrientation` | page 4 | Restraint control module: a004 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a004_frontAlgoDisabled` | page 4 | Restraint control module: a004 front algo disabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_sideAlgoDisabled` | page 4 | Restraint control module: a004 side algo disabled | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_rollAlgoDisabled` | page 4 | Restraint control module: a004 roll algo disabled | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_idleMode` | page 4 | Restraint control module: a004 idle mode | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_internalFaultDetected` | page 4 | Restraint control module: a004 internal fault detected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_swVersionMismatch` | page 4 | Restraint control module: a004 sw version mismatch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_paramLayoutIDInv` | page 4 | Restraint control module: a004 param layout ID inv | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_algoPASIDMismatch` | page 4 | Restraint control module: a004 algo PASID mismatch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_eventIDFsignal` | page 4 | Restraint control module: a004 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a004_eventFrontLeftSeatbelt` | page 4 | Restraint control module: a004 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a004_eventFrontRightSeatbelt` | page 4 | Restraint control module: a004 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a004_eventVehicleSpeed` | page 4 | Restraint control module: a004 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a004_eventSteeringAngle` | page 4 | Restraint control module: a004 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a004_eventDriverBrakeApply` | page 4 | Restraint control module: a004 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a004_eventAccelPedalPos` | page 4 | Restraint control module: a004 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a005_eventArmStatus` | page 5 | Restraint control module: a005 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a005_eventFactoryMode` | page 5 | Restraint control module: a005 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a005_eventDiagEnabled` | page 5 | Restraint control module: a005 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a005_eventDriveOrientation` | page 5 | Restraint control module: a005 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a005_externalCRCError` | page 5 | Restraint control module: a005 external CRC error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a005_eventIDFsignal` | page 5 | Restraint control module: a005 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a005_eventFrontLeftSeatbelt` | page 5 | Restraint control module: a005 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a005_eventFrontRightSeatbelt` | page 5 | Restraint control module: a005 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a005_eventVehicleSpeed` | page 5 | Restraint control module: a005 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a005_eventSteeringAngle` | page 5 | Restraint control module: a005 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a005_eventDriverBrakeApply` | page 5 | Restraint control module: a005 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a005_eventAccelPedalPos` | page 5 | Restraint control module: a005 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a006_eventArmStatus` | page 6 | Restraint control module: a006 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a006_eventFactoryMode` | page 6 | Restraint control module: a006 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a006_eventDiagEnabled` | page 6 | Restraint control module: a006 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a006_eventDriveOrientation` | page 6 | Restraint control module: a006 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a006_batteryVoltageTooHigh` | page 6 | Restraint control module: a006 battery voltage too high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a006_batteryVoltageTooLow` | page 6 | Restraint control module: a006 battery voltage too low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a006_eventIDFsignal` | page 6 | Restraint control module: a006 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a006_eventFrontLeftSeatbelt` | page 6 | Restraint control module: a006 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a006_eventFrontRightSeatbelt` | page 6 | Restraint control module: a006 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a006_eventVehicleSpeed` | page 6 | Restraint control module: a006 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a006_eventSteeringAngle` | page 6 | Restraint control module: a006 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a006_eventDriverBrakeApply` | page 6 | Restraint control module: a006 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a006_eventAccelPedalPos` | page 6 | Restraint control module: a006 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a008_eventArmStatus` | page 8 | Restraint control module: a008 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a008_eventFactoryMode` | page 8 | Restraint control module: a008 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a008_eventDiagEnabled` | page 8 | Restraint control module: a008 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a008_eventDriveOrientation` | page 8 | Restraint control module: a008 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a008_lossOfMainPwrSupMonit` | page 8 | Restraint control module: a008 loss of main pwr sup monit | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a008_lossOfBckupPwrSupMonit` | page 8 | Restraint control module: a008 loss of bckup pwr sup monit | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a008_normalShtdwnUnavail` | page 8 | Restraint control module: a008 normal shtdwn unavail | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a008_eventIDFsignal` | page 8 | Restraint control module: a008 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a008_eventFrontLeftSeatbelt` | page 8 | Restraint control module: a008 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a008_eventFrontRightSeatbelt` | page 8 | Restraint control module: a008 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a008_eventVehicleSpeed` | page 8 | Restraint control module: a008 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a008_eventSteeringAngle` | page 8 | Restraint control module: a008 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a008_eventDriverBrakeApply` | page 8 | Restraint control module: a008 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a008_eventAccelPedalPos` | page 8 | Restraint control module: a008 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a009_eventArmStatus` | page 9 | Restraint control module: a009 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a009_eventFactoryMode` | page 9 | Restraint control module: a009 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a009_eventDiagEnabled` | page 9 | Restraint control module: a009 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a009_eventDriveOrientation` | page 9 | Restraint control module: a009 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a009_reprogramLimitExceeded` | page 9 | Restraint control module: a009 reprogram limit exceeded | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a009_eventIDFsignal` | page 9 | Restraint control module: a009 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a009_eventFrontLeftSeatbelt` | page 9 | Restraint control module: a009 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a009_eventFrontRightSeatbelt` | page 9 | Restraint control module: a009 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a009_eventVehicleSpeed` | page 9 | Restraint control module: a009 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a009_eventSteeringAngle` | page 9 | Restraint control module: a009 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a009_eventDriverBrakeApply` | page 9 | Restraint control module: a009 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a009_eventAccelPedalPos` | page 9 | Restraint control module: a009 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a011_eventArmStatus` | page 11 | Restraint control module: a011 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a011_eventFactoryMode` | page 11 | Restraint control module: a011 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a011_eventDiagEnabled` | page 11 | Restraint control module: a011 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a011_eventDriveOrientation` | page 11 | Restraint control module: a011 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a011_edrDataAreaLocked` | page 11 | Restraint control module: a011 edr data area locked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a011_eventIDFsignal` | page 11 | Restraint control module: a011 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a011_eventFrontLeftSeatbelt` | page 11 | Restraint control module: a011 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a011_eventFrontRightSeatbelt` | page 11 | Restraint control module: a011 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a011_eventVehicleSpeed` | page 11 | Restraint control module: a011 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a011_eventSteeringAngle` | page 11 | Restraint control module: a011 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a011_eventDriverBrakeApply` | page 11 | Restraint control module: a011 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a011_eventAccelPedalPos` | page 11 | Restraint control module: a011 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a012_eventArmStatus` | page 12 | Restraint control module: a012 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a012_eventFactoryMode` | page 12 | Restraint control module: a012 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a012_eventDiagEnabled` | page 12 | Restraint control module: a012 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a012_eventDriveOrientation` | page 12 | Restraint control module: a012 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a012_vinMismatch` | page 12 | Restraint control module: a012 vin mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a012_vinNotProgrammed` | page 12 | Restraint control module: a012 vin not programmed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a012_eventIDFsignal` | page 12 | Restraint control module: a012 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a012_eventFrontLeftSeatbelt` | page 12 | Restraint control module: a012 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a012_eventFrontRightSeatbelt` | page 12 | Restraint control module: a012 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a012_eventVehicleSpeed` | page 12 | Restraint control module: a012 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a012_eventSteeringAngle` | page 12 | Restraint control module: a012 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a012_eventDriverBrakeApply` | page 12 | Restraint control module: a012 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a012_eventAccelPedalPos` | page 12 | Restraint control module: a012 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a013_eventArmStatus` | page 13 | Restraint control module: a013 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a013_eventFactoryMode` | page 13 | Restraint control module: a013 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a013_eventDiagEnabled` | page 13 | Restraint control module: a013 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a013_eventDriveOrientation` | page 13 | Restraint control module: a013 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a013_driveOrientiInitNotDone` | page 13 | Restraint control module: a013 drive orienti init not done | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a013_driveOrientPlausiCheck` | page 13 | Restraint control module: a013 drive orient plausi check | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a013_eventIDFsignal` | page 13 | Restraint control module: a013 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a013_eventFrontLeftSeatbelt` | page 13 | Restraint control module: a013 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a013_eventFrontRightSeatbelt` | page 13 | Restraint control module: a013 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a013_eventVehicleSpeed` | page 13 | Restraint control module: a013 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a013_eventSteeringAngle` | page 13 | Restraint control module: a013 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a013_eventDriverBrakeApply` | page 13 | Restraint control module: a013 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a013_eventAccelPedalPos` | page 13 | Restraint control module: a013 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a014_eventArmStatus` | page 14 | Restraint control module: a014 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a014_eventFactoryMode` | page 14 | Restraint control module: a014 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a014_eventDiagEnabled` | page 14 | Restraint control module: a014 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a014_eventDriveOrientation` | page 14 | Restraint control module: a014 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a014_driverABStg1Sht2Gnd` | page 14 | Restraint control module: a014 driver AB stg1 sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStg1Sht2Bat` | page 14 | Restraint control module: a014 driver AB stg1 sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStg1Open` | page 14 | Restraint control module: a014 driver AB stg1 open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStg1Short` | page 14 | Restraint control module: a014 driver AB stg1 short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStg1CrossCoup` | page 14 | Restraint control module: a014 driver AB stg1 cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStg1Config` | page 14 | Restraint control module: a014 driver AB stg1 config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_eventIDFsignal` | page 14 | Restraint control module: a014 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a014_eventFrontLeftSeatbelt` | page 14 | Restraint control module: a014 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a014_eventFrontRightSeatbelt` | page 14 | Restraint control module: a014 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a014_eventVehicleSpeed` | page 14 | Restraint control module: a014 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a014_eventSteeringAngle` | page 14 | Restraint control module: a014 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a014_eventDriverBrakeApply` | page 14 | Restraint control module: a014 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a014_eventAccelPedalPos` | page 14 | Restraint control module: a014 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a015_eventArmStatus` | page 15 | Restraint control module: a015 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a015_eventFactoryMode` | page 15 | Restraint control module: a015 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a015_eventDiagEnabled` | page 15 | Restraint control module: a015 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a015_eventDriveOrientation` | page 15 | Restraint control module: a015 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a015_driverABStg2Sht2Gnd` | page 15 | Restraint control module: a015 driver AB stg2 sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStg2Sht2Bat` | page 15 | Restraint control module: a015 driver AB stg2 sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStg2Open` | page 15 | Restraint control module: a015 driver AB stg2 open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStg2Short` | page 15 | Restraint control module: a015 driver AB stg2 short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStg2CrossCoup` | page 15 | Restraint control module: a015 driver AB stg2 cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStg2Config` | page 15 | Restraint control module: a015 driver AB stg2 config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_eventIDFsignal` | page 15 | Restraint control module: a015 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a015_eventFrontLeftSeatbelt` | page 15 | Restraint control module: a015 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a015_eventFrontRightSeatbelt` | page 15 | Restraint control module: a015 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a015_eventVehicleSpeed` | page 15 | Restraint control module: a015 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a015_eventSteeringAngle` | page 15 | Restraint control module: a015 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a015_eventDriverBrakeApply` | page 15 | Restraint control module: a015 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a015_eventAccelPedalPos` | page 15 | Restraint control module: a015 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a016_eventArmStatus` | page 16 | Restraint control module: a016 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a016_eventFactoryMode` | page 16 | Restraint control module: a016 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a016_eventDiagEnabled` | page 16 | Restraint control module: a016 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a016_eventDriveOrientation` | page 16 | Restraint control module: a016 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a016_passABStg1Sht2Gnd` | page 16 | Restraint control module: a016 pass AB stg1 sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStg1Sht2Bat` | page 16 | Restraint control module: a016 pass AB stg1 sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStg1Open` | page 16 | Restraint control module: a016 pass AB stg1 open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStg1Short` | page 16 | Restraint control module: a016 pass AB stg1 short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStg1CrossCoup` | page 16 | Restraint control module: a016 pass AB stg1 cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStg1Config` | page 16 | Restraint control module: a016 pass AB stg1 config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_eventIDFsignal` | page 16 | Restraint control module: a016 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a016_eventFrontLeftSeatbelt` | page 16 | Restraint control module: a016 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a016_eventFrontRightSeatbelt` | page 16 | Restraint control module: a016 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a016_eventVehicleSpeed` | page 16 | Restraint control module: a016 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a016_eventSteeringAngle` | page 16 | Restraint control module: a016 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a016_eventDriverBrakeApply` | page 16 | Restraint control module: a016 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a016_eventAccelPedalPos` | page 16 | Restraint control module: a016 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a017_eventArmStatus` | page 17 | Restraint control module: a017 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a017_eventFactoryMode` | page 17 | Restraint control module: a017 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a017_eventDiagEnabled` | page 17 | Restraint control module: a017 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a017_eventDriveOrientation` | page 17 | Restraint control module: a017 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a017_passABStg2Sht2Gnd` | page 17 | Restraint control module: a017 pass AB stg2 sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStg2Sht2Bat` | page 17 | Restraint control module: a017 pass AB stg2 sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStg2Open` | page 17 | Restraint control module: a017 pass AB stg2 open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStg2Short` | page 17 | Restraint control module: a017 pass AB stg2 short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStg2CrossCoup` | page 17 | Restraint control module: a017 pass AB stg2 cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStg2Config` | page 17 | Restraint control module: a017 pass AB stg2 config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_eventIDFsignal` | page 17 | Restraint control module: a017 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a017_eventFrontLeftSeatbelt` | page 17 | Restraint control module: a017 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a017_eventFrontRightSeatbelt` | page 17 | Restraint control module: a017 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a017_eventVehicleSpeed` | page 17 | Restraint control module: a017 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a017_eventSteeringAngle` | page 17 | Restraint control module: a017 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a017_eventDriverBrakeApply` | page 17 | Restraint control module: a017 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a017_eventAccelPedalPos` | page 17 | Restraint control module: a017 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a018_eventArmStatus` | page 18 | Restraint control module: a018 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a018_eventFactoryMode` | page 18 | Restraint control module: a018 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a018_eventDiagEnabled` | page 18 | Restraint control module: a018 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a018_eventDriveOrientation` | page 18 | Restraint control module: a018 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a018_passActiveVentSht2Gnd` | page 18 | Restraint control module: a018 pass active vent sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passActiveVentSht2Bat` | page 18 | Restraint control module: a018 pass active vent sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passActiveVentOpen` | page 18 | Restraint control module: a018 pass active vent open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passActiveVentShort` | page 18 | Restraint control module: a018 pass active vent short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passActiveVentCrossCoup` | page 18 | Restraint control module: a018 pass active vent cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passActiveVentConfig` | page 18 | Restraint control module: a018 pass active vent config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_eventIDFsignal` | page 18 | Restraint control module: a018 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a018_eventFrontLeftSeatbelt` | page 18 | Restraint control module: a018 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a018_eventFrontRightSeatbelt` | page 18 | Restraint control module: a018 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a018_eventVehicleSpeed` | page 18 | Restraint control module: a018 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a018_eventSteeringAngle` | page 18 | Restraint control module: a018 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a018_eventDriverBrakeApply` | page 18 | Restraint control module: a018 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a018_eventAccelPedalPos` | page 18 | Restraint control module: a018 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a019_eventArmStatus` | page 19 | Restraint control module: a019 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a019_eventFactoryMode` | page 19 | Restraint control module: a019 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a019_eventDiagEnabled` | page 19 | Restraint control module: a019 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a019_eventDriveOrientation` | page 19 | Restraint control module: a019 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a019_pretenShldLeftSht2Gnd` | page 19 | Restraint control module: a019 preten shld left sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldLeftSht2Bat` | page 19 | Restraint control module: a019 preten shld left sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldLeftOpen` | page 19 | Restraint control module: a019 preten shld left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldLeftShort` | page 19 | Restraint control module: a019 preten shld left short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldLeftCrossC` | page 19 | Restraint control module: a019 preten shld left cross c | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldLeftConfig` | page 19 | Restraint control module: a019 preten shld left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_eventIDFsignal` | page 19 | Restraint control module: a019 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a019_eventFrontLeftSeatbelt` | page 19 | Restraint control module: a019 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a019_eventFrontRightSeatbelt` | page 19 | Restraint control module: a019 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a019_eventVehicleSpeed` | page 19 | Restraint control module: a019 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a019_eventSteeringAngle` | page 19 | Restraint control module: a019 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a019_eventDriverBrakeApply` | page 19 | Restraint control module: a019 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a019_eventAccelPedalPos` | page 19 | Restraint control module: a019 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a020_eventArmStatus` | page 20 | Restraint control module: a020 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a020_eventFactoryMode` | page 20 | Restraint control module: a020 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a020_eventDiagEnabled` | page 20 | Restraint control module: a020 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a020_eventDriveOrientation` | page 20 | Restraint control module: a020 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a020_pretenShldRightSht2Gnd` | page 20 | Restraint control module: a020 preten shld right sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldRightSht2Bat` | page 20 | Restraint control module: a020 preten shld right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldRightOpen` | page 20 | Restraint control module: a020 preten shld right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldRightShort` | page 20 | Restraint control module: a020 preten shld right short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldRightCrossC` | page 20 | Restraint control module: a020 preten shld right cross c | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldRightConfig` | page 20 | Restraint control module: a020 preten shld right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_eventIDFsignal` | page 20 | Restraint control module: a020 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a020_eventFrontLeftSeatbelt` | page 20 | Restraint control module: a020 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a020_eventFrontRightSeatbelt` | page 20 | Restraint control module: a020 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a020_eventVehicleSpeed` | page 20 | Restraint control module: a020 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a020_eventSteeringAngle` | page 20 | Restraint control module: a020 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a020_eventDriverBrakeApply` | page 20 | Restraint control module: a020 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a020_eventAccelPedalPos` | page 20 | Restraint control module: a020 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a021_eventArmStatus` | page 21 | Restraint control module: a021 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a021_eventFactoryMode` | page 21 | Restraint control module: a021 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a021_eventDiagEnabled` | page 21 | Restraint control module: a021 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a021_eventDriveOrientation` | page 21 | Restraint control module: a021 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a021_pretenLapLeftSht2Gnd` | page 21 | Restraint control module: a021 preten lap left sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapLeftSht2Bat` | page 21 | Restraint control module: a021 preten lap left sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapLeftOpen` | page 21 | Restraint control module: a021 preten lap left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapLeftShort` | page 21 | Restraint control module: a021 preten lap left short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapLeftCrossCoup` | page 21 | Restraint control module: a021 preten lap left cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapLeftConfig` | page 21 | Restraint control module: a021 preten lap left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_eventIDFsignal` | page 21 | Restraint control module: a021 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a021_eventFrontLeftSeatbelt` | page 21 | Restraint control module: a021 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a021_eventFrontRightSeatbelt` | page 21 | Restraint control module: a021 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a021_eventVehicleSpeed` | page 21 | Restraint control module: a021 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a021_eventSteeringAngle` | page 21 | Restraint control module: a021 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a021_eventDriverBrakeApply` | page 21 | Restraint control module: a021 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a021_eventAccelPedalPos` | page 21 | Restraint control module: a021 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a022_eventArmStatus` | page 22 | Restraint control module: a022 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a022_eventFactoryMode` | page 22 | Restraint control module: a022 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a022_eventDiagEnabled` | page 22 | Restraint control module: a022 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a022_eventDriveOrientation` | page 22 | Restraint control module: a022 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a022_pretenLapRightSht2Gnd` | page 22 | Restraint control module: a022 preten lap right sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapRightSht2Bat` | page 22 | Restraint control module: a022 preten lap right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapRightOpen` | page 22 | Restraint control module: a022 preten lap right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapRightShort` | page 22 | Restraint control module: a022 preten lap right short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapRightCrossCoup` | page 22 | Restraint control module: a022 preten lap right cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapRightConfig` | page 22 | Restraint control module: a022 preten lap right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_eventIDFsignal` | page 22 | Restraint control module: a022 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a022_eventFrontLeftSeatbelt` | page 22 | Restraint control module: a022 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a022_eventFrontRightSeatbelt` | page 22 | Restraint control module: a022 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a022_eventVehicleSpeed` | page 22 | Restraint control module: a022 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a022_eventSteeringAngle` | page 22 | Restraint control module: a022 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a022_eventDriverBrakeApply` | page 22 | Restraint control module: a022 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a022_eventAccelPedalPos` | page 22 | Restraint control module: a022 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a023_eventArmStatus` | page 23 | Restraint control module: a023 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a023_eventFactoryMode` | page 23 | Restraint control module: a023 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a023_eventDiagEnabled` | page 23 | Restraint control module: a023 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a023_eventDriveOrientation` | page 23 | Restraint control module: a023 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a023_loadLimLeftSht2Gnd` | page 23 | Restraint control module: a023 load lim left sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimLeftSht2Bat` | page 23 | Restraint control module: a023 load lim left sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimLeftOpen` | page 23 | Restraint control module: a023 load lim left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimLeftShort` | page 23 | Restraint control module: a023 load lim left short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimLeftCrossCoup` | page 23 | Restraint control module: a023 load lim left cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimLeftConfig` | page 23 | Restraint control module: a023 load lim left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_eventIDFsignal` | page 23 | Restraint control module: a023 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a023_eventFrontLeftSeatbelt` | page 23 | Restraint control module: a023 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a023_eventFrontRightSeatbelt` | page 23 | Restraint control module: a023 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a023_eventVehicleSpeed` | page 23 | Restraint control module: a023 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a023_eventSteeringAngle` | page 23 | Restraint control module: a023 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a023_eventDriverBrakeApply` | page 23 | Restraint control module: a023 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a023_eventAccelPedalPos` | page 23 | Restraint control module: a023 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a024_eventArmStatus` | page 24 | Restraint control module: a024 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a024_eventFactoryMode` | page 24 | Restraint control module: a024 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a024_eventDiagEnabled` | page 24 | Restraint control module: a024 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a024_eventDriveOrientation` | page 24 | Restraint control module: a024 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a024_loadLimRightSht2Gnd` | page 24 | Restraint control module: a024 load lim right sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimRightSht2Bat` | page 24 | Restraint control module: a024 load lim right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimRightOpen` | page 24 | Restraint control module: a024 load lim right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimRightShort` | page 24 | Restraint control module: a024 load lim right short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimRightCrossCoup` | page 24 | Restraint control module: a024 load lim right cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimRightConfig` | page 24 | Restraint control module: a024 load lim right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_eventIDFsignal` | page 24 | Restraint control module: a024 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a024_eventFrontLeftSeatbelt` | page 24 | Restraint control module: a024 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a024_eventFrontRightSeatbelt` | page 24 | Restraint control module: a024 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a024_eventVehicleSpeed` | page 24 | Restraint control module: a024 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a024_eventSteeringAngle` | page 24 | Restraint control module: a024 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a024_eventDriverBrakeApply` | page 24 | Restraint control module: a024 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a024_eventAccelPedalPos` | page 24 | Restraint control module: a024 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a025_eventArmStatus` | page 25 | Restraint control module: a025 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a025_eventFactoryMode` | page 25 | Restraint control module: a025 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a025_eventDiagEnabled` | page 25 | Restraint control module: a025 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a025_eventDriveOrientation` | page 25 | Restraint control module: a025 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a025_kneeABDrvrSht2Gnd` | page 25 | Restraint control module: a025 knee AB drvr sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDrvrSht2Bat` | page 25 | Restraint control module: a025 knee AB drvr sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDrvrOpen` | page 25 | Restraint control module: a025 knee AB drvr open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDrvrShort` | page 25 | Restraint control module: a025 knee AB drvr short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDrvrCrossCoup` | page 25 | Restraint control module: a025 knee AB drvr cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDrvrConfig` | page 25 | Restraint control module: a025 knee AB drvr config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_eventIDFsignal` | page 25 | Restraint control module: a025 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a025_eventFrontLeftSeatbelt` | page 25 | Restraint control module: a025 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a025_eventFrontRightSeatbelt` | page 25 | Restraint control module: a025 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a025_eventVehicleSpeed` | page 25 | Restraint control module: a025 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a025_eventSteeringAngle` | page 25 | Restraint control module: a025 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a025_eventDriverBrakeApply` | page 25 | Restraint control module: a025 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a025_eventAccelPedalPos` | page 25 | Restraint control module: a025 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a026_eventArmStatus` | page 26 | Restraint control module: a026 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a026_eventFactoryMode` | page 26 | Restraint control module: a026 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a026_eventDiagEnabled` | page 26 | Restraint control module: a026 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a026_eventDriveOrientation` | page 26 | Restraint control module: a026 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a026_kneeABPassSht2Gnd` | page 26 | Restraint control module: a026 knee AB pass sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABPassSht2Bat` | page 26 | Restraint control module: a026 knee AB pass sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABPassOpen` | page 26 | Restraint control module: a026 knee AB pass open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABPassShort` | page 26 | Restraint control module: a026 knee AB pass short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABPassCrossCoup` | page 26 | Restraint control module: a026 knee AB pass cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABPassConfig` | page 26 | Restraint control module: a026 knee AB pass config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_eventIDFsignal` | page 26 | Restraint control module: a026 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a026_eventFrontLeftSeatbelt` | page 26 | Restraint control module: a026 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a026_eventFrontRightSeatbelt` | page 26 | Restraint control module: a026 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a026_eventVehicleSpeed` | page 26 | Restraint control module: a026 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a026_eventSteeringAngle` | page 26 | Restraint control module: a026 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a026_eventDriverBrakeApply` | page 26 | Restraint control module: a026 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a026_eventAccelPedalPos` | page 26 | Restraint control module: a026 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a027_eventArmStatus` | page 27 | Restraint control module: a027 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a027_eventFactoryMode` | page 27 | Restraint control module: a027 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a027_eventDiagEnabled` | page 27 | Restraint control module: a027 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a027_eventDriveOrientation` | page 27 | Restraint control module: a027 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a027_sideAB1stRowLSht2Gnd` | page 27 | Restraint control module: a027 side ab1st row l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLSht2Bat` | page 27 | Restraint control module: a027 side ab1st row l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLOpen` | page 27 | Restraint control module: a027 side ab1st row l open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLShort` | page 27 | Restraint control module: a027 side ab1st row l short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLCrossCoup` | page 27 | Restraint control module: a027 side ab1st row l cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLConfig` | page 27 | Restraint control module: a027 side ab1st row l config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_eventIDFsignal` | page 27 | Restraint control module: a027 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a027_eventFrontLeftSeatbelt` | page 27 | Restraint control module: a027 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a027_eventFrontRightSeatbelt` | page 27 | Restraint control module: a027 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a027_eventVehicleSpeed` | page 27 | Restraint control module: a027 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a027_eventSteeringAngle` | page 27 | Restraint control module: a027 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a027_eventDriverBrakeApply` | page 27 | Restraint control module: a027 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a027_eventAccelPedalPos` | page 27 | Restraint control module: a027 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a028_eventArmStatus` | page 28 | Restraint control module: a028 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a028_eventFactoryMode` | page 28 | Restraint control module: a028 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a028_eventDiagEnabled` | page 28 | Restraint control module: a028 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a028_eventDriveOrientation` | page 28 | Restraint control module: a028 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a028_sideAB1stRowRSht2Gnd` | page 28 | Restraint control module: a028 side ab1st row r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowRSht2Bat` | page 28 | Restraint control module: a028 side ab1st row r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowROpen` | page 28 | Restraint control module: a028 side ab1st row r open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowRShort` | page 28 | Restraint control module: a028 side ab1st row r short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowRCrossCoup` | page 28 | Restraint control module: a028 side ab1st row r cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowRConfig` | page 28 | Restraint control module: a028 side ab1st row r config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_eventIDFsignal` | page 28 | Restraint control module: a028 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a028_eventFrontLeftSeatbelt` | page 28 | Restraint control module: a028 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a028_eventFrontRightSeatbelt` | page 28 | Restraint control module: a028 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a028_eventVehicleSpeed` | page 28 | Restraint control module: a028 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a028_eventSteeringAngle` | page 28 | Restraint control module: a028 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a028_eventDriverBrakeApply` | page 28 | Restraint control module: a028 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a028_eventAccelPedalPos` | page 28 | Restraint control module: a028 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a029_eventArmStatus` | page 29 | Restraint control module: a029 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a029_eventFactoryMode` | page 29 | Restraint control module: a029 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a029_eventDiagEnabled` | page 29 | Restraint control module: a029 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a029_eventDriveOrientation` | page 29 | Restraint control module: a029 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a029_driverABAVSht2Gnd` | page 29 | Restraint control module: a029 driver ABAV sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABAVSht2Bat` | page 29 | Restraint control module: a029 driver ABAV sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABAVOpen` | page 29 | Restraint control module: a029 driver ABAV open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABAVShort` | page 29 | Restraint control module: a029 driver ABAV short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABAVCrossCoup` | page 29 | Restraint control module: a029 driver ABAV cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABAVConfig` | page 29 | Restraint control module: a029 driver ABAV config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_eventIDFsignal` | page 29 | Restraint control module: a029 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a029_eventFrontLeftSeatbelt` | page 29 | Restraint control module: a029 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a029_eventFrontRightSeatbelt` | page 29 | Restraint control module: a029 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a029_eventVehicleSpeed` | page 29 | Restraint control module: a029 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a029_eventSteeringAngle` | page 29 | Restraint control module: a029 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a029_eventDriverBrakeApply` | page 29 | Restraint control module: a029 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a029_eventAccelPedalPos` | page 29 | Restraint control module: a029 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a030_eventArmStatus` | page 30 | Restraint control module: a030 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a030_eventFactoryMode` | page 30 | Restraint control module: a030 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a030_eventDiagEnabled` | page 30 | Restraint control module: a030 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a030_eventDriveOrientation` | page 30 | Restraint control module: a030 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a030_farsideABSht2Gnd` | page 30 | Restraint control module: a030 farside AB sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farsideABSht2Bat` | page 30 | Restraint control module: a030 farside AB sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farsideABOpen` | page 30 | Restraint control module: a030 farside AB open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farsideABShort` | page 30 | Restraint control module: a030 farside AB short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farsideABCrossCoup` | page 30 | Restraint control module: a030 farside AB cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farsideABConfig` | page 30 | Restraint control module: a030 farside AB config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_eventIDFsignal` | page 30 | Restraint control module: a030 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a030_eventFrontLeftSeatbelt` | page 30 | Restraint control module: a030 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a030_eventFrontRightSeatbelt` | page 30 | Restraint control module: a030 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a030_eventVehicleSpeed` | page 30 | Restraint control module: a030 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a030_eventSteeringAngle` | page 30 | Restraint control module: a030 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a030_eventDriverBrakeApply` | page 30 | Restraint control module: a030 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a030_eventAccelPedalPos` | page 30 | Restraint control module: a030 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a031_eventArmStatus` | page 31 | Restraint control module: a031 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a031_eventFactoryMode` | page 31 | Restraint control module: a031 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a031_eventDiagEnabled` | page 31 | Restraint control module: a031 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a031_eventDriveOrientation` | page 31 | Restraint control module: a031 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a031_frntCentrABSht2Gnd` | page 31 | Restraint control module: a031 frnt centr AB sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frntCentrABSht2Bat` | page 31 | Restraint control module: a031 frnt centr AB sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frntCentrABOpen` | page 31 | Restraint control module: a031 frnt centr AB open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frntCentrABShort` | page 31 | Restraint control module: a031 frnt centr AB short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frntCentrABCrossCoup` | page 31 | Restraint control module: a031 frnt centr AB cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frntCentrABConfig` | page 31 | Restraint control module: a031 frnt centr AB config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_eventIDFsignal` | page 31 | Restraint control module: a031 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a031_eventFrontLeftSeatbelt` | page 31 | Restraint control module: a031 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a031_eventFrontRightSeatbelt` | page 31 | Restraint control module: a031 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a031_eventVehicleSpeed` | page 31 | Restraint control module: a031 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a031_eventSteeringAngle` | page 31 | Restraint control module: a031 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a031_eventDriverBrakeApply` | page 31 | Restraint control module: a031 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a031_eventAccelPedalPos` | page 31 | Restraint control module: a031 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a032_eventArmStatus` | page 32 | Restraint control module: a032 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a032_eventFactoryMode` | page 32 | Restraint control module: a032 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a032_eventDiagEnabled` | page 32 | Restraint control module: a032 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a032_eventDriveOrientation` | page 32 | Restraint control module: a032 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a032_curABLeftSht2Gnd` | page 32 | Restraint control module: a032 cur AB left sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curABLeftSht2Bat` | page 32 | Restraint control module: a032 cur AB left sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curABLeftOpen` | page 32 | Restraint control module: a032 cur AB left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curABLeftShort` | page 32 | Restraint control module: a032 cur AB left short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curABLeftCrossCoup` | page 32 | Restraint control module: a032 cur AB left cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curABLeftConfig` | page 32 | Restraint control module: a032 cur AB left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_eventIDFsignal` | page 32 | Restraint control module: a032 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a032_eventFrontLeftSeatbelt` | page 32 | Restraint control module: a032 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a032_eventFrontRightSeatbelt` | page 32 | Restraint control module: a032 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a032_eventVehicleSpeed` | page 32 | Restraint control module: a032 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a032_eventSteeringAngle` | page 32 | Restraint control module: a032 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a032_eventDriverBrakeApply` | page 32 | Restraint control module: a032 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a032_eventAccelPedalPos` | page 32 | Restraint control module: a032 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a033_eventArmStatus` | page 33 | Restraint control module: a033 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a033_eventFactoryMode` | page 33 | Restraint control module: a033 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a033_eventDiagEnabled` | page 33 | Restraint control module: a033 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a033_eventDriveOrientation` | page 33 | Restraint control module: a033 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a033_curABRightSht2Gnd` | page 33 | Restraint control module: a033 cur AB right sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curABRightSht2Bat` | page 33 | Restraint control module: a033 cur AB right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curABRightOpen` | page 33 | Restraint control module: a033 cur AB right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curABRightShort` | page 33 | Restraint control module: a033 cur AB right short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curABRightCrossCoup` | page 33 | Restraint control module: a033 cur AB right cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curABRightConfig` | page 33 | Restraint control module: a033 cur AB right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_eventIDFsignal` | page 33 | Restraint control module: a033 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a033_eventFrontLeftSeatbelt` | page 33 | Restraint control module: a033 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a033_eventFrontRightSeatbelt` | page 33 | Restraint control module: a033 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a033_eventVehicleSpeed` | page 33 | Restraint control module: a033 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a033_eventSteeringAngle` | page 33 | Restraint control module: a033 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a033_eventDriverBrakeApply` | page 33 | Restraint control module: a033 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a033_eventAccelPedalPos` | page 33 | Restraint control module: a033 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a034_eventArmStatus` | page 34 | Restraint control module: a034 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a034_eventFactoryMode` | page 34 | Restraint control module: a034 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a034_eventDiagEnabled` | page 34 | Restraint control module: a034 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a034_eventDriveOrientation` | page 34 | Restraint control module: a034 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a034_preten2ndRowLSht2Gnd` | page 34 | Restraint control module: a034 preten2nd row l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLSht2Bat` | page 34 | Restraint control module: a034 preten2nd row l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLOpen` | page 34 | Restraint control module: a034 preten2nd row l open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLShort` | page 34 | Restraint control module: a034 preten2nd row l short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLCrossCoup` | page 34 | Restraint control module: a034 preten2nd row l cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLCgf` | page 34 | Restraint control module: a034 preten2nd row l cgf | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_eventIDFsignal` | page 34 | Restraint control module: a034 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a034_eventFrontLeftSeatbelt` | page 34 | Restraint control module: a034 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a034_eventFrontRightSeatbelt` | page 34 | Restraint control module: a034 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a034_eventVehicleSpeed` | page 34 | Restraint control module: a034 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a034_eventSteeringAngle` | page 34 | Restraint control module: a034 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a034_eventDriverBrakeApply` | page 34 | Restraint control module: a034 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a034_eventAccelPedalPos` | page 34 | Restraint control module: a034 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a035_eventArmStatus` | page 35 | Restraint control module: a035 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a035_eventFactoryMode` | page 35 | Restraint control module: a035 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a035_eventDiagEnabled` | page 35 | Restraint control module: a035 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a035_eventDriveOrientation` | page 35 | Restraint control module: a035 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a035_preten2ndRowRSht2Gnd` | page 35 | Restraint control module: a035 preten2nd row r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowRSht2Bat` | page 35 | Restraint control module: a035 preten2nd row r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowROpen` | page 35 | Restraint control module: a035 preten2nd row r open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowRShort` | page 35 | Restraint control module: a035 preten2nd row r short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowRCrossCoup` | page 35 | Restraint control module: a035 preten2nd row r cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowRCgf` | page 35 | Restraint control module: a035 preten2nd row r cgf | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_eventIDFsignal` | page 35 | Restraint control module: a035 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a035_eventFrontLeftSeatbelt` | page 35 | Restraint control module: a035 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a035_eventFrontRightSeatbelt` | page 35 | Restraint control module: a035 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a035_eventVehicleSpeed` | page 35 | Restraint control module: a035 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a035_eventSteeringAngle` | page 35 | Restraint control module: a035 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a035_eventDriverBrakeApply` | page 35 | Restraint control module: a035 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a035_eventAccelPedalPos` | page 35 | Restraint control module: a035 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a036_eventArmStatus` | page 36 | Restraint control module: a036 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a036_eventFactoryMode` | page 36 | Restraint control module: a036 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a036_eventDiagEnabled` | page 36 | Restraint control module: a036 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a036_eventDriveOrientation` | page 36 | Restraint control module: a036 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a036_curAB2ndRowLSht2Gnd` | page 36 | Restraint control module: a036 cur ab2nd row l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLSht2Bat` | page 36 | Restraint control module: a036 cur ab2nd row l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLOpen` | page 36 | Restraint control module: a036 cur ab2nd row l open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLShort` | page 36 | Restraint control module: a036 cur ab2nd row l short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLCrossCoup` | page 36 | Restraint control module: a036 cur ab2nd row l cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLConfig` | page 36 | Restraint control module: a036 cur ab2nd row l config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_eventIDFsignal` | page 36 | Restraint control module: a036 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a036_eventFrontLeftSeatbelt` | page 36 | Restraint control module: a036 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a036_eventFrontRightSeatbelt` | page 36 | Restraint control module: a036 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a036_eventVehicleSpeed` | page 36 | Restraint control module: a036 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a036_eventSteeringAngle` | page 36 | Restraint control module: a036 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a036_eventDriverBrakeApply` | page 36 | Restraint control module: a036 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a036_eventAccelPedalPos` | page 36 | Restraint control module: a036 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a037_eventArmStatus` | page 37 | Restraint control module: a037 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a037_eventFactoryMode` | page 37 | Restraint control module: a037 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a037_eventDiagEnabled` | page 37 | Restraint control module: a037 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a037_eventDriveOrientation` | page 37 | Restraint control module: a037 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a037_curAB2ndRowRSht2Gnd` | page 37 | Restraint control module: a037 cur ab2nd row r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowRSht2Bat` | page 37 | Restraint control module: a037 cur ab2nd row r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowROpen` | page 37 | Restraint control module: a037 cur ab2nd row r open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowRShort` | page 37 | Restraint control module: a037 cur ab2nd row r short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowRCrossCoup` | page 37 | Restraint control module: a037 cur ab2nd row r cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowRConfig` | page 37 | Restraint control module: a037 cur ab2nd row r config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_eventIDFsignal` | page 37 | Restraint control module: a037 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a037_eventFrontLeftSeatbelt` | page 37 | Restraint control module: a037 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a037_eventFrontRightSeatbelt` | page 37 | Restraint control module: a037 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a037_eventVehicleSpeed` | page 37 | Restraint control module: a037 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a037_eventSteeringAngle` | page 37 | Restraint control module: a037 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a037_eventDriverBrakeApply` | page 37 | Restraint control module: a037 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a037_eventAccelPedalPos` | page 37 | Restraint control module: a037 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a040_eventArmStatus` | page 40 | Restraint control module: a040 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a040_eventFactoryMode` | page 40 | Restraint control module: a040 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a040_eventDiagEnabled` | page 40 | Restraint control module: a040 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a040_eventDriveOrientation` | page 40 | Restraint control module: a040 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a040_hoodActuatorRSht2Gnd` | page 40 | Restraint control module: a040 hood actuator r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorRSht2Bat` | page 40 | Restraint control module: a040 hood actuator r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorROpen` | page 40 | Restraint control module: a040 hood actuator r open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorRShort` | page 40 | Restraint control module: a040 hood actuator r short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorRCrossCoup` | page 40 | Restraint control module: a040 hood actuator r cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorRConfig` | page 40 | Restraint control module: a040 hood actuator r config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_eventIDFsignal` | page 40 | Restraint control module: a040 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a040_eventFrontLeftSeatbelt` | page 40 | Restraint control module: a040 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a040_eventFrontRightSeatbelt` | page 40 | Restraint control module: a040 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a040_eventVehicleSpeed` | page 40 | Restraint control module: a040 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a040_eventSteeringAngle` | page 40 | Restraint control module: a040 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a040_eventDriverBrakeApply` | page 40 | Restraint control module: a040 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a040_eventAccelPedalPos` | page 40 | Restraint control module: a040 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a041_eventArmStatus` | page 41 | Restraint control module: a041 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a041_eventFactoryMode` | page 41 | Restraint control module: a041 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a041_eventDiagEnabled` | page 41 | Restraint control module: a041 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a041_eventDriveOrientation` | page 41 | Restraint control module: a041 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a041_hoodActuatorLSht2Gnd` | page 41 | Restraint control module: a041 hood actuator l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLSht2Bat` | page 41 | Restraint control module: a041 hood actuator l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLOpen` | page 41 | Restraint control module: a041 hood actuator l open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLShort` | page 41 | Restraint control module: a041 hood actuator l short | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLCrossCoup` | page 41 | Restraint control module: a041 hood actuator l cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLConfig` | page 41 | Restraint control module: a041 hood actuator l config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_eventIDFsignal` | page 41 | Restraint control module: a041 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a041_eventFrontLeftSeatbelt` | page 41 | Restraint control module: a041 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a041_eventFrontRightSeatbelt` | page 41 | Restraint control module: a041 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a041_eventVehicleSpeed` | page 41 | Restraint control module: a041 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a041_eventSteeringAngle` | page 41 | Restraint control module: a041 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a041_eventDriverBrakeApply` | page 41 | Restraint control module: a041 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a041_eventAccelPedalPos` | page 41 | Restraint control module: a041 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a042_eventArmStatus` | page 42 | Restraint control module: a042 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a042_eventFactoryMode` | page 42 | Restraint control module: a042 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a042_eventDiagEnabled` | page 42 | Restraint control module: a042 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a042_eventDriveOrientation` | page 42 | Restraint control module: a042 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a042_ens1Sht2Bat` | page 42 | Restraint control module: a042 ens1 sht2 bat | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a042_ens1Sht2Gnd` | page 42 | Restraint control module: a042 ens1 sht2 gnd | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a042_ens1Config` | page 42 | Restraint control module: a042 ens1 config | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a042_eventIDFsignal` | page 42 | Restraint control module: a042 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a042_eventFrontLeftSeatbelt` | page 42 | Restraint control module: a042 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a042_eventFrontRightSeatbelt` | page 42 | Restraint control module: a042 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a042_eventVehicleSpeed` | page 42 | Restraint control module: a042 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a042_eventSteeringAngle` | page 42 | Restraint control module: a042 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a042_eventDriverBrakeApply` | page 42 | Restraint control module: a042 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a042_eventAccelPedalPos` | page 42 | Restraint control module: a042 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a043_eventArmStatus` | page 43 | Restraint control module: a043 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a043_eventFactoryMode` | page 43 | Restraint control module: a043 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a043_eventDiagEnabled` | page 43 | Restraint control module: a043 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a043_eventDriveOrientation` | page 43 | Restraint control module: a043 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a043_ens2Sht2Bat` | page 43 | Restraint control module: a043 ens2 sht2 bat | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a043_ens2Sht2Gnd` | page 43 | Restraint control module: a043 ens2 sht2 gnd | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a043_ens2Config` | page 43 | Restraint control module: a043 ens2 config | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a043_eventIDFsignal` | page 43 | Restraint control module: a043 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a043_eventFrontLeftSeatbelt` | page 43 | Restraint control module: a043 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a043_eventFrontRightSeatbelt` | page 43 | Restraint control module: a043 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a043_eventVehicleSpeed` | page 43 | Restraint control module: a043 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a043_eventSteeringAngle` | page 43 | Restraint control module: a043 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a043_eventDriverBrakeApply` | page 43 | Restraint control module: a043 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a043_eventAccelPedalPos` | page 43 | Restraint control module: a043 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a044_eventArmStatus` | page 44 | Restraint control module: a044 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a044_eventFactoryMode` | page 44 | Restraint control module: a044 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a044_eventDiagEnabled` | page 44 | Restraint control module: a044 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a044_eventDriveOrientation` | page 44 | Restraint control module: a044 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a044_upFrontSensorLSht2Gnd` | page 44 | Restraint control module: a044 up front sensor l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLSht2Bat` | page 44 | Restraint control module: a044 up front sensor l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLCrossCoup` | page 44 | Restraint control module: a044 up front sensor l cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLComm` | page 44 | Restraint control module: a044 up front sensor l comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLInitTyp` | page 44 | Restraint control module: a044 up front sensor l init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLOption` | page 44 | Restraint control module: a044 up front sensor l option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLplaus` | page 44 | Restraint control module: a044 up front sensor lplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLDefect` | page 44 | Restraint control module: a044 up front sensor l defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_eventIDFsignal` | page 44 | Restraint control module: a044 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a044_eventFrontLeftSeatbelt` | page 44 | Restraint control module: a044 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a044_eventFrontRightSeatbelt` | page 44 | Restraint control module: a044 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a044_eventVehicleSpeed` | page 44 | Restraint control module: a044 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a044_eventSteeringAngle` | page 44 | Restraint control module: a044 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a044_eventDriverBrakeApply` | page 44 | Restraint control module: a044 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a044_eventAccelPedalPos` | page 44 | Restraint control module: a044 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a045_eventArmStatus` | page 45 | Restraint control module: a045 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a045_eventFactoryMode` | page 45 | Restraint control module: a045 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a045_eventDiagEnabled` | page 45 | Restraint control module: a045 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a045_eventDriveOrientation` | page 45 | Restraint control module: a045 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a045_upFrontSensorRSht2Gnd` | page 45 | Restraint control module: a045 up front sensor r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRSht2Bat` | page 45 | Restraint control module: a045 up front sensor r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRCrossCoup` | page 45 | Restraint control module: a045 up front sensor r cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRComm` | page 45 | Restraint control module: a045 up front sensor r comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRInitTyp` | page 45 | Restraint control module: a045 up front sensor r init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorROption` | page 45 | Restraint control module: a045 up front sensor r option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRplaus` | page 45 | Restraint control module: a045 up front sensor rplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRDefect` | page 45 | Restraint control module: a045 up front sensor r defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_eventIDFsignal` | page 45 | Restraint control module: a045 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a045_eventFrontLeftSeatbelt` | page 45 | Restraint control module: a045 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a045_eventFrontRightSeatbelt` | page 45 | Restraint control module: a045 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a045_eventVehicleSpeed` | page 45 | Restraint control module: a045 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a045_eventSteeringAngle` | page 45 | Restraint control module: a045 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a045_eventDriverBrakeApply` | page 45 | Restraint control module: a045 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a045_eventAccelPedalPos` | page 45 | Restraint control module: a045 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a046_eventArmStatus` | page 46 | Restraint control module: a046 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a046_eventFactoryMode` | page 46 | Restraint control module: a046 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a046_eventDiagEnabled` | page 46 | Restraint control module: a046 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a046_eventDriveOrientation` | page 46 | Restraint control module: a046 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a046_sideAccelBPilLSht2Gnd` | page 46 | Restraint control module: a046 side accel b pil l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLSht2Bat` | page 46 | Restraint control module: a046 side accel b pil l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLCLosCoup` | page 46 | Restraint control module: a046 side accel b pil LC los coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLComm` | page 46 | Restraint control module: a046 side accel b pil l comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLInitTyp` | page 46 | Restraint control module: a046 side accel b pil l init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLOption` | page 46 | Restraint control module: a046 side accel b pil l option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLplaus` | page 46 | Restraint control module: a046 side accel b pil lplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPilLDefect` | page 46 | Restraint control module: a046 side accel b pil l defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_eventIDFsignal` | page 46 | Restraint control module: a046 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a046_eventFrontLeftSeatbelt` | page 46 | Restraint control module: a046 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a046_eventFrontRightSeatbelt` | page 46 | Restraint control module: a046 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a046_eventVehicleSpeed` | page 46 | Restraint control module: a046 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a046_eventSteeringAngle` | page 46 | Restraint control module: a046 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a046_eventDriverBrakeApply` | page 46 | Restraint control module: a046 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a046_eventAccelPedalPos` | page 46 | Restraint control module: a046 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a047_eventArmStatus` | page 47 | Restraint control module: a047 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a047_eventFactoryMode` | page 47 | Restraint control module: a047 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a047_eventDiagEnabled` | page 47 | Restraint control module: a047 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a047_eventDriveOrientation` | page 47 | Restraint control module: a047 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a047_sideAccelBPilRSht2Gnd` | page 47 | Restraint control module: a047 side accel b pil r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRSht2Bat` | page 47 | Restraint control module: a047 side accel b pil r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRCrossCoup` | page 47 | Restraint control module: a047 side accel b pil r cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRComm` | page 47 | Restraint control module: a047 side accel b pil r comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRInitTyp` | page 47 | Restraint control module: a047 side accel b pil r init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilROption` | page 47 | Restraint control module: a047 side accel b pil r option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRplaus` | page 47 | Restraint control module: a047 side accel b pil rplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPilRDefect` | page 47 | Restraint control module: a047 side accel b pil r defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_eventIDFsignal` | page 47 | Restraint control module: a047 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a047_eventFrontLeftSeatbelt` | page 47 | Restraint control module: a047 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a047_eventFrontRightSeatbelt` | page 47 | Restraint control module: a047 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a047_eventVehicleSpeed` | page 47 | Restraint control module: a047 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a047_eventSteeringAngle` | page 47 | Restraint control module: a047 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a047_eventDriverBrakeApply` | page 47 | Restraint control module: a047 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a047_eventAccelPedalPos` | page 47 | Restraint control module: a047 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a048_eventArmStatus` | page 48 | Restraint control module: a048 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a048_eventFactoryMode` | page 48 | Restraint control module: a048 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a048_eventDiagEnabled` | page 48 | Restraint control module: a048 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a048_eventDriveOrientation` | page 48 | Restraint control module: a048 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a048_sideAccelCPilLSht2Gnd` | page 48 | Restraint control module: a048 side accel c pil l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLSht2Bat` | page 48 | Restraint control module: a048 side accel c pil l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLCrossCoup` | page 48 | Restraint control module: a048 side accel c pil l cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLComm` | page 48 | Restraint control module: a048 side accel c pil l comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLInitTyp` | page 48 | Restraint control module: a048 side accel c pil l init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLOption` | page 48 | Restraint control module: a048 side accel c pil l option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLplaus` | page 48 | Restraint control module: a048 side accel c pil lplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPilLDefect` | page 48 | Restraint control module: a048 side accel c pil l defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_eventIDFsignal` | page 48 | Restraint control module: a048 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a048_eventFrontLeftSeatbelt` | page 48 | Restraint control module: a048 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a048_eventFrontRightSeatbelt` | page 48 | Restraint control module: a048 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a048_eventVehicleSpeed` | page 48 | Restraint control module: a048 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a048_eventSteeringAngle` | page 48 | Restraint control module: a048 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a048_eventDriverBrakeApply` | page 48 | Restraint control module: a048 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a048_eventAccelPedalPos` | page 48 | Restraint control module: a048 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a049_eventArmStatus` | page 49 | Restraint control module: a049 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a049_eventFactoryMode` | page 49 | Restraint control module: a049 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a049_eventDiagEnabled` | page 49 | Restraint control module: a049 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a049_eventDriveOrientation` | page 49 | Restraint control module: a049 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a049_sideAccelCPilRSht2Gnd` | page 49 | Restraint control module: a049 side accel c pil r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRSht2Bat` | page 49 | Restraint control module: a049 side accel c pil r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRCrossCoup` | page 49 | Restraint control module: a049 side accel c pil r cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRComm` | page 49 | Restraint control module: a049 side accel c pil r comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRInitTyp` | page 49 | Restraint control module: a049 side accel c pil r init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilROption` | page 49 | Restraint control module: a049 side accel c pil r option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRplaus` | page 49 | Restraint control module: a049 side accel c pil rplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPilRDefect` | page 49 | Restraint control module: a049 side accel c pil r defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_eventIDFsignal` | page 49 | Restraint control module: a049 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a049_eventFrontLeftSeatbelt` | page 49 | Restraint control module: a049 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a049_eventFrontRightSeatbelt` | page 49 | Restraint control module: a049 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a049_eventVehicleSpeed` | page 49 | Restraint control module: a049 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a049_eventSteeringAngle` | page 49 | Restraint control module: a049 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a049_eventDriverBrakeApply` | page 49 | Restraint control module: a049 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a049_eventAccelPedalPos` | page 49 | Restraint control module: a049 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a050_eventArmStatus` | page 50 | Restraint control module: a050 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a050_eventFactoryMode` | page 50 | Restraint control module: a050 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a050_eventDiagEnabled` | page 50 | Restraint control module: a050 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a050_eventDriveOrientation` | page 50 | Restraint control module: a050 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a050_upFrontSensorCSht2Gnd` | page 50 | Restraint control module: a050 up front sensor c sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCSht2Bat` | page 50 | Restraint control module: a050 up front sensor c sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCCrossCoup` | page 50 | Restraint control module: a050 up front sensor c cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCComm` | page 50 | Restraint control module: a050 up front sensor c comm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCInitTyp` | page 50 | Restraint control module: a050 up front sensor c init typ | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCOption` | page 50 | Restraint control module: a050 up front sensor c option | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCplaus` | page 50 | Restraint control module: a050 up front sensor cplaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCDefect` | page 50 | Restraint control module: a050 up front sensor c defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_eventIDFsignal` | page 50 | Restraint control module: a050 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a050_eventFrontLeftSeatbelt` | page 50 | Restraint control module: a050 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a050_eventFrontRightSeatbelt` | page 50 | Restraint control module: a050 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a050_eventVehicleSpeed` | page 50 | Restraint control module: a050 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a050_eventSteeringAngle` | page 50 | Restraint control module: a050 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a050_eventDriverBrakeApply` | page 50 | Restraint control module: a050 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a050_eventAccelPedalPos` | page 50 | Restraint control module: a050 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a051_eventArmStatus` | page 51 | Restraint control module: a051 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a051_eventFactoryMode` | page 51 | Restraint control module: a051 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a051_eventDiagEnabled` | page 51 | Restraint control module: a051 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a051_eventDriveOrientation` | page 51 | Restraint control module: a051 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a051_presFrntLDoorComm` | page 51 | Restraint control module: a051 pres frnt l door comm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorInitTyp` | page 51 | Restraint control module: a051 pres frnt l door init typ | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorOption` | page 51 | Restraint control module: a051 pres frnt l door option | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorPlaus` | page 51 | Restraint control module: a051 pres frnt l door plaus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorAbsPre` | page 51 | Restraint control module: a051 pres frnt l door abs pre | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorDefect` | page 51 | Restraint control module: a051 pres frnt l door defect | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorSht2Gnd` | page 51 | Restraint control module: a051 pres frnt l door sht2 gnd | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorSht2Bat` | page 51 | Restraint control module: a051 pres frnt l door sht2 bat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_presFrntLDoorCrossCoup` | page 51 | Restraint control module: a051 pres frnt l door cross coup | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_eventIDFsignal` | page 51 | Restraint control module: a051 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a051_eventFrontLeftSeatbelt` | page 51 | Restraint control module: a051 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a051_eventFrontRightSeatbelt` | page 51 | Restraint control module: a051 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a051_eventVehicleSpeed` | page 51 | Restraint control module: a051 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a051_eventSteeringAngle` | page 51 | Restraint control module: a051 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a051_eventDriverBrakeApply` | page 51 | Restraint control module: a051 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a051_eventAccelPedalPos` | page 51 | Restraint control module: a051 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a052_eventArmStatus` | page 52 | Restraint control module: a052 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a052_eventFactoryMode` | page 52 | Restraint control module: a052 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a052_eventDiagEnabled` | page 52 | Restraint control module: a052 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a052_eventDriveOrientation` | page 52 | Restraint control module: a052 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a052_presFrntRDoorComm` | page 52 | Restraint control module: a052 pres frnt r door comm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorInitTyp` | page 52 | Restraint control module: a052 pres frnt r door init typ | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorOption` | page 52 | Restraint control module: a052 pres frnt r door option | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorPlaus` | page 52 | Restraint control module: a052 pres frnt r door plaus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorAbsPre` | page 52 | Restraint control module: a052 pres frnt r door abs pre | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorDefect` | page 52 | Restraint control module: a052 pres frnt r door defect | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorSht2Gnd` | page 52 | Restraint control module: a052 pres frnt r door sht2 gnd | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorSht2Bat` | page 52 | Restraint control module: a052 pres frnt r door sht2 bat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_presFrntRDoorCrossCoup` | page 52 | Restraint control module: a052 pres frnt r door cross coup | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_eventIDFsignal` | page 52 | Restraint control module: a052 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a052_eventFrontLeftSeatbelt` | page 52 | Restraint control module: a052 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a052_eventFrontRightSeatbelt` | page 52 | Restraint control module: a052 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a052_eventVehicleSpeed` | page 52 | Restraint control module: a052 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a052_eventSteeringAngle` | page 52 | Restraint control module: a052 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a052_eventDriverBrakeApply` | page 52 | Restraint control module: a052 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a052_eventAccelPedalPos` | page 52 | Restraint control module: a052 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a053_eventArmStatus` | page 53 | Restraint control module: a053 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a053_eventFactoryMode` | page 53 | Restraint control module: a053 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a053_eventDiagEnabled` | page 53 | Restraint control module: a053 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a053_eventDriveOrientation` | page 53 | Restraint control module: a053 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a053_presPedProLComm` | page 53 | Restraint control module: a053 pres ped pro l comm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLInitTyp` | page 53 | Restraint control module: a053 pres ped pro l init typ | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLOption` | page 53 | Restraint control module: a053 pres ped pro l option | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLPlaus` | page 53 | Restraint control module: a053 pres ped pro l plaus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLAbsPre` | page 53 | Restraint control module: a053 pres ped pro l abs pre | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLDefect` | page 53 | Restraint control module: a053 pres ped pro l defect | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLSht2Gnd` | page 53 | Restraint control module: a053 pres ped pro l sht2 gnd | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLSht2Bat` | page 53 | Restraint control module: a053 pres ped pro l sht2 bat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_presPedProLCrossCoup` | page 53 | Restraint control module: a053 pres ped pro l cross coup | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_eventIDFsignal` | page 53 | Restraint control module: a053 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a053_eventFrontLeftSeatbelt` | page 53 | Restraint control module: a053 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a053_eventFrontRightSeatbelt` | page 53 | Restraint control module: a053 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a053_eventVehicleSpeed` | page 53 | Restraint control module: a053 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a053_eventSteeringAngle` | page 53 | Restraint control module: a053 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a053_eventDriverBrakeApply` | page 53 | Restraint control module: a053 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a053_eventAccelPedalPos` | page 53 | Restraint control module: a053 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a054_eventArmStatus` | page 54 | Restraint control module: a054 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a054_eventFactoryMode` | page 54 | Restraint control module: a054 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a054_eventDiagEnabled` | page 54 | Restraint control module: a054 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a054_eventDriveOrientation` | page 54 | Restraint control module: a054 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a054_presPedProRComm` | page 54 | Restraint control module: a054 pres ped pro r comm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRInitTyp` | page 54 | Restraint control module: a054 pres ped pro r init typ | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProROption` | page 54 | Restraint control module: a054 pres ped pro r option | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRPlaus` | page 54 | Restraint control module: a054 pres ped pro r plaus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRAbsPre` | page 54 | Restraint control module: a054 pres ped pro r abs pre | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRDefect` | page 54 | Restraint control module: a054 pres ped pro r defect | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRSht2Gnd` | page 54 | Restraint control module: a054 pres ped pro r sht2 gnd | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRSht2Bat` | page 54 | Restraint control module: a054 pres ped pro r sht2 bat | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_presPedProRCrossCoup` | page 54 | Restraint control module: a054 pres ped pro r cross coup | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_eventIDFsignal` | page 54 | Restraint control module: a054 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a054_eventFrontLeftSeatbelt` | page 54 | Restraint control module: a054 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a054_eventFrontRightSeatbelt` | page 54 | Restraint control module: a054 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a054_eventVehicleSpeed` | page 54 | Restraint control module: a054 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a054_eventSteeringAngle` | page 54 | Restraint control module: a054 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a054_eventDriverBrakeApply` | page 54 | Restraint control module: a054 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a054_eventAccelPedalPos` | page 54 | Restraint control module: a054 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a055_eventArmStatus` | page 55 | Restraint control module: a055 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a055_eventFactoryMode` | page 55 | Restraint control module: a055 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a055_eventDiagEnabled` | page 55 | Restraint control module: a055 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a055_eventDriveOrientation` | page 55 | Restraint control module: a055 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a055_imuCalibrationNotDone` | page 55 | Restraint control module: a055 imu calibration not done | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a055_imuCalibrationFailed` | page 55 | Restraint control module: a055 imu calibration failed | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a055_eventIDFsignal` | page 55 | Restraint control module: a055 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a055_eventFrontLeftSeatbelt` | page 55 | Restraint control module: a055 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a055_eventFrontRightSeatbelt` | page 55 | Restraint control module: a055 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a055_eventVehicleSpeed` | page 55 | Restraint control module: a055 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a055_eventSteeringAngle` | page 55 | Restraint control module: a055 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a055_eventDriverBrakeApply` | page 55 | Restraint control module: a055 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a055_eventAccelPedalPos` | page 55 | Restraint control module: a055 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a056_eventArmStatus` | page 56 | Restraint control module: a056 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a056_eventFactoryMode` | page 56 | Restraint control module: a056 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a056_eventDiagEnabled` | page 56 | Restraint control module: a056 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a056_eventDriveOrientation` | page 56 | Restraint control module: a056 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a056_ocs1pFaulted` | page 56 | Restraint control module: a056 ocs1p faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a056_ocs1pWrongCalD` | page 56 | Restraint control module: a056 ocs1p wrong cal d | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a056_eventIDFsignal` | page 56 | Restraint control module: a056 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a056_eventFrontLeftSeatbelt` | page 56 | Restraint control module: a056 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a056_eventFrontRightSeatbelt` | page 56 | Restraint control module: a056 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a056_eventVehicleSpeed` | page 56 | Restraint control module: a056 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a056_eventSteeringAngle` | page 56 | Restraint control module: a056 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a056_eventDriverBrakeApply` | page 56 | Restraint control module: a056 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a056_eventAccelPedalPos` | page 56 | Restraint control module: a056 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a057_eventArmStatus` | page 57 | Restraint control module: a057 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a057_eventFactoryMode` | page 57 | Restraint control module: a057 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a057_eventDiagEnabled` | page 57 | Restraint control module: a057 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a057_eventDriveOrientation` | page 57 | Restraint control module: a057 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a057_ocs1dFaulted` | page 57 | Restraint control module: a057 ocs1d faulted | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a057_ocs1dWrongCalD` | page 57 | Restraint control module: a057 ocs1d wrong cal d | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a057_eventIDFsignal` | page 57 | Restraint control module: a057 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a057_eventFrontLeftSeatbelt` | page 57 | Restraint control module: a057 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a057_eventFrontRightSeatbelt` | page 57 | Restraint control module: a057 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a057_eventVehicleSpeed` | page 57 | Restraint control module: a057 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a057_eventSteeringAngle` | page 57 | Restraint control module: a057 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a057_eventDriverBrakeApply` | page 57 | Restraint control module: a057 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a057_eventAccelPedalPos` | page 57 | Restraint control module: a057 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a058_eventArmStatus` | page 58 | Restraint control module: a058 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a058_eventFactoryMode` | page 58 | Restraint control module: a058 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a058_eventDiagEnabled` | page 58 | Restraint control module: a058 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a058_eventDriveOrientation` | page 58 | Restraint control module: a058 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a058_bucklHallLeftShort` | page 58 | Restraint control module: a058 buckl hall left short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_bucklHallLeftSht2Bat` | page 58 | Restraint control module: a058 buckl hall left sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_bucklHallLeftOpen` | page 58 | Restraint control module: a058 buckl hall left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_bucklHallLeftUndef` | page 58 | Restraint control module: a058 buckl hall left undef | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_bucklHallLeftCrossCoup` | page 58 | Restraint control module: a058 buckl hall left cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_bucklHallLeftConfig` | page 58 | Restraint control module: a058 buckl hall left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_eventIDFsignal` | page 58 | Restraint control module: a058 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a058_eventFrontLeftSeatbelt` | page 58 | Restraint control module: a058 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a058_eventFrontRightSeatbelt` | page 58 | Restraint control module: a058 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a058_eventVehicleSpeed` | page 58 | Restraint control module: a058 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a058_eventSteeringAngle` | page 58 | Restraint control module: a058 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a058_eventDriverBrakeApply` | page 58 | Restraint control module: a058 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a058_eventAccelPedalPos` | page 58 | Restraint control module: a058 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a059_eventArmStatus` | page 59 | Restraint control module: a059 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a059_eventFactoryMode` | page 59 | Restraint control module: a059 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a059_eventDiagEnabled` | page 59 | Restraint control module: a059 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a059_eventDriveOrientation` | page 59 | Restraint control module: a059 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a059_bucklHallRightShort` | page 59 | Restraint control module: a059 buckl hall right short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_bucklHallRightSht2Bat` | page 59 | Restraint control module: a059 buckl hall right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_bucklHallRightOpen` | page 59 | Restraint control module: a059 buckl hall right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_bucklHallRightUndef` | page 59 | Restraint control module: a059 buckl hall right undef | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_bucklHallRightCrossCoup` | page 59 | Restraint control module: a059 buckl hall right cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_bucklSwRightConfig` | page 59 | Restraint control module: a059 buckl sw right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_eventIDFsignal` | page 59 | Restraint control module: a059 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a059_eventFrontLeftSeatbelt` | page 59 | Restraint control module: a059 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a059_eventFrontRightSeatbelt` | page 59 | Restraint control module: a059 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a059_eventVehicleSpeed` | page 59 | Restraint control module: a059 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a059_eventSteeringAngle` | page 59 | Restraint control module: a059 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a059_eventDriverBrakeApply` | page 59 | Restraint control module: a059 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a059_eventAccelPedalPos` | page 59 | Restraint control module: a059 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a060_eventArmStatus` | page 60 | Restraint control module: a060 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a060_eventFactoryMode` | page 60 | Restraint control module: a060 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a060_eventDiagEnabled` | page 60 | Restraint control module: a060 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a060_eventDriveOrientation` | page 60 | Restraint control module: a060 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a060_seaTrkPosLeftShort` | page 60 | Restraint control module: a060 sea trk pos left short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_seaTrkPosLeftShort2Bat` | page 60 | Restraint control module: a060 sea trk pos left short2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_seaTrkPosLeftOpen` | page 60 | Restraint control module: a060 sea trk pos left open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_seaTrkPosLeftUndefined` | page 60 | Restraint control module: a060 sea trk pos left undefined | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_seaTrkPosLeftCrossCoup` | page 60 | Restraint control module: a060 sea trk pos left cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_seaTrkPosLeftConfig` | page 60 | Restraint control module: a060 sea trk pos left config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_eventIDFsignal` | page 60 | Restraint control module: a060 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a060_eventFrontLeftSeatbelt` | page 60 | Restraint control module: a060 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a060_eventFrontRightSeatbelt` | page 60 | Restraint control module: a060 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a060_eventVehicleSpeed` | page 60 | Restraint control module: a060 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a060_eventSteeringAngle` | page 60 | Restraint control module: a060 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a060_eventDriverBrakeApply` | page 60 | Restraint control module: a060 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a060_eventAccelPedalPos` | page 60 | Restraint control module: a060 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a061_eventArmStatus` | page 61 | Restraint control module: a061 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a061_eventFactoryMode` | page 61 | Restraint control module: a061 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a061_eventDiagEnabled` | page 61 | Restraint control module: a061 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a061_eventDriveOrientation` | page 61 | Restraint control module: a061 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a061_seaTrkPosRightShort` | page 61 | Restraint control module: a061 sea trk pos right short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_seaTrkPosRightSht2Bat` | page 61 | Restraint control module: a061 sea trk pos right sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_seaTrkPosRightOpen` | page 61 | Restraint control module: a061 sea trk pos right open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_seaTrkPosRightUndefined` | page 61 | Restraint control module: a061 sea trk pos right undefined | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_seaTrkPosRightCrossCoup` | page 61 | Restraint control module: a061 sea trk pos right cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_seaTrkPosRightConfig` | page 61 | Restraint control module: a061 sea trk pos right config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_eventIDFsignal` | page 61 | Restraint control module: a061 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a061_eventFrontLeftSeatbelt` | page 61 | Restraint control module: a061 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a061_eventFrontRightSeatbelt` | page 61 | Restraint control module: a061 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a061_eventVehicleSpeed` | page 61 | Restraint control module: a061 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a061_eventSteeringAngle` | page 61 | Restraint control module: a061 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a061_eventDriverBrakeApply` | page 61 | Restraint control module: a061 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a061_eventAccelPedalPos` | page 61 | Restraint control module: a061 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a062_eventArmStatus` | page 62 | Restraint control module: a062 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a062_eventFactoryMode` | page 62 | Restraint control module: a062 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a062_eventDiagEnabled` | page 62 | Restraint control module: a062 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a062_eventDriveOrientation` | page 62 | Restraint control module: a062 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a062_alrShort` | page 62 | Restraint control module: a062 alr short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrSht2Bat` | page 62 | Restraint control module: a062 alr sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrOpen` | page 62 | Restraint control module: a062 alr open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrUndefined` | page 62 | Restraint control module: a062 alr undefined | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrCrossCoup` | page 62 | Restraint control module: a062 alr cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrConfig` | page 62 | Restraint control module: a062 alr config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_eventIDFsignal` | page 62 | Restraint control module: a062 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a062_eventFrontLeftSeatbelt` | page 62 | Restraint control module: a062 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a062_eventFrontRightSeatbelt` | page 62 | Restraint control module: a062 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a062_eventVehicleSpeed` | page 62 | Restraint control module: a062 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a062_eventSteeringAngle` | page 62 | Restraint control module: a062 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a062_eventDriverBrakeApply` | page 62 | Restraint control module: a062 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a062_eventAccelPedalPos` | page 62 | Restraint control module: a062 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a063_eventArmStatus` | page 63 | Restraint control module: a063 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a063_eventFactoryMode` | page 63 | Restraint control module: a063 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a063_eventDiagEnabled` | page 63 | Restraint control module: a063 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a063_eventDriveOrientation` | page 63 | Restraint control module: a063 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a063_sbsw2ndRowRSht2Gnd` | page 63 | Restraint control module: a063 sbsw2nd row r sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowRSht2Bat` | page 63 | Restraint control module: a063 sbsw2nd row r sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowROpen` | page 63 | Restraint control module: a063 sbsw2nd row r open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowRUndefined` | page 63 | Restraint control module: a063 sbsw2nd row r undefined | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowRCrossCoup` | page 63 | Restraint control module: a063 sbsw2nd row r cross coup | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowRConfig` | page 63 | Restraint control module: a063 sbsw2nd row r config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_eventIDFsignal` | page 63 | Restraint control module: a063 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a063_eventFrontLeftSeatbelt` | page 63 | Restraint control module: a063 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a063_eventFrontRightSeatbelt` | page 63 | Restraint control module: a063 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a063_eventVehicleSpeed` | page 63 | Restraint control module: a063 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a063_eventSteeringAngle` | page 63 | Restraint control module: a063 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a063_eventDriverBrakeApply` | page 63 | Restraint control module: a063 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a063_eventAccelPedalPos` | page 63 | Restraint control module: a063 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a064_eventArmStatus` | page 64 | Restraint control module: a064 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a064_eventFactoryMode` | page 64 | Restraint control module: a064 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a064_eventDiagEnabled` | page 64 | Restraint control module: a064 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a064_eventDriveOrientation` | page 64 | Restraint control module: a064 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a064_hwcp1CheckFail` | page 64 | Restraint control module: a064 hwcp1 check fail | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a064_hwcp1Sht2Bat` | page 64 | Restraint control module: a064 hwcp1 sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a064_hwcp1CrossCoup` | page 64 | Restraint control module: a064 hwcp1 cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a064_hwcp1Config` | page 64 | Restraint control module: a064 hwcp1 config | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a064_eventIDFsignal` | page 64 | Restraint control module: a064 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a064_eventFrontLeftSeatbelt` | page 64 | Restraint control module: a064 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a064_eventFrontRightSeatbelt` | page 64 | Restraint control module: a064 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a064_eventVehicleSpeed` | page 64 | Restraint control module: a064 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a064_eventSteeringAngle` | page 64 | Restraint control module: a064 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a064_eventDriverBrakeApply` | page 64 | Restraint control module: a064 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a064_eventAccelPedalPos` | page 64 | Restraint control module: a064 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a065_eventArmStatus` | page 65 | Restraint control module: a065 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a065_eventFactoryMode` | page 65 | Restraint control module: a065 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a065_eventDiagEnabled` | page 65 | Restraint control module: a065 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a065_eventDriveOrientation` | page 65 | Restraint control module: a065 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a065_swDrvrOrientCheck` | page 65 | Restraint control module: a065 sw drvr orient check | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a065_swDrvrOrientSht2Bat` | page 65 | Restraint control module: a065 sw drvr orient sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a065_swDrvrOrientCrossCoup` | page 65 | Restraint control module: a065 sw drvr orient cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a065_swDrvrOrientConfig` | page 65 | Restraint control module: a065 sw drvr orient config | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a065_eventIDFsignal` | page 65 | Restraint control module: a065 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a065_eventFrontLeftSeatbelt` | page 65 | Restraint control module: a065 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a065_eventFrontRightSeatbelt` | page 65 | Restraint control module: a065 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a065_eventVehicleSpeed` | page 65 | Restraint control module: a065 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a065_eventSteeringAngle` | page 65 | Restraint control module: a065 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a065_eventDriverBrakeApply` | page 65 | Restraint control module: a065 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a065_eventAccelPedalPos` | page 65 | Restraint control module: a065 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a066_eventArmStatus` | page 66 | Restraint control module: a066 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a066_eventFactoryMode` | page 66 | Restraint control module: a066 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a066_eventDiagEnabled` | page 66 | Restraint control module: a066 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a066_eventDriveOrientation` | page 66 | Restraint control module: a066 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a066_sbsw2ndRowLShort` | page 66 | Restraint control module: a066 sbsw2nd row l short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a066_sbsw2ndRowLSht2Bat` | page 66 | Restraint control module: a066 sbsw2nd row l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a066_sbsw2ndRowLCrossCoup` | page 66 | Restraint control module: a066 sbsw2nd row l cross coup | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a066_sbsw2ndRowLConfig` | page 66 | Restraint control module: a066 sbsw2nd row l config | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a066_eventIDFsignal` | page 66 | Restraint control module: a066 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a066_eventFrontLeftSeatbelt` | page 66 | Restraint control module: a066 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a066_eventFrontRightSeatbelt` | page 66 | Restraint control module: a066 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a066_eventVehicleSpeed` | page 66 | Restraint control module: a066 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a066_eventSteeringAngle` | page 66 | Restraint control module: a066 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a066_eventDriverBrakeApply` | page 66 | Restraint control module: a066 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a066_eventAccelPedalPos` | page 66 | Restraint control module: a066 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a067_eventArmStatus` | page 67 | Restraint control module: a067 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a067_eventFactoryMode` | page 67 | Restraint control module: a067 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a067_eventDiagEnabled` | page 67 | Restraint control module: a067 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a067_eventDriveOrientation` | page 67 | Restraint control module: a067 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a067_comCANInitialization` | page 67 | Restraint control module: a067 com CAN initialization | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a067_eventIDFsignal` | page 67 | Restraint control module: a067 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a067_eventFrontLeftSeatbelt` | page 67 | Restraint control module: a067 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a067_eventFrontRightSeatbelt` | page 67 | Restraint control module: a067 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a067_eventVehicleSpeed` | page 67 | Restraint control module: a067 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a067_eventSteeringAngle` | page 67 | Restraint control module: a067 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a067_eventDriverBrakeApply` | page 67 | Restraint control module: a067 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a067_eventAccelPedalPos` | page 67 | Restraint control module: a067 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a068_eventArmStatus` | page 68 | Restraint control module: a068 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a068_eventFactoryMode` | page 68 | Restraint control module: a068 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a068_eventDiagEnabled` | page 68 | Restraint control module: a068 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a068_eventDriveOrientation` | page 68 | Restraint control module: a068 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a068_comChassisCANBusOff` | page 68 | Restraint control module: a068 com chassis CAN bus off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a068_eventIDFsignal` | page 68 | Restraint control module: a068 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a068_eventFrontLeftSeatbelt` | page 68 | Restraint control module: a068 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a068_eventFrontRightSeatbelt` | page 68 | Restraint control module: a068 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a068_eventVehicleSpeed` | page 68 | Restraint control module: a068 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a068_eventSteeringAngle` | page 68 | Restraint control module: a068 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a068_eventDriverBrakeApply` | page 68 | Restraint control module: a068 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a068_eventAccelPedalPos` | page 68 | Restraint control module: a068 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a069_eventArmStatus` | page 69 | Restraint control module: a069 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a069_eventFactoryMode` | page 69 | Restraint control module: a069 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a069_eventDiagEnabled` | page 69 | Restraint control module: a069 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a069_eventDriveOrientation` | page 69 | Restraint control module: a069 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a069_comChassisCANPH7MIA` | page 69 | Restraint control module: a069 com chassis CANPH7 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a069_comChassisCANPH7ChkSm` | page 69 | Restraint control module: a069 com chassis CANPH7 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a069_comChassisCANPH7Cntr` | page 69 | Restraint control module: a069 com chassis CANPH7 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a069_eventIDFsignal` | page 69 | Restraint control module: a069 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a069_eventFrontLeftSeatbelt` | page 69 | Restraint control module: a069 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a069_eventFrontRightSeatbelt` | page 69 | Restraint control module: a069 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a069_eventVehicleSpeed` | page 69 | Restraint control module: a069 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a069_eventSteeringAngle` | page 69 | Restraint control module: a069 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a069_eventDriverBrakeApply` | page 69 | Restraint control module: a069 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a069_eventAccelPedalPos` | page 69 | Restraint control module: a069 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a070_eventArmStatus` | page 70 | Restraint control module: a070 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a070_eventFactoryMode` | page 70 | Restraint control module: a070 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a070_eventDiagEnabled` | page 70 | Restraint control module: a070 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a070_eventDriveOrientation` | page 70 | Restraint control module: a070 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a070_comChassisCANPH8MIA` | page 70 | Restraint control module: a070 com chassis CANPH8 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a070_comChassisCANPH8ChkSm` | page 70 | Restraint control module: a070 com chassis CANPH8 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a070_comChassisCANPH8Cntr` | page 70 | Restraint control module: a070 com chassis CANPH8 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a070_eventIDFsignal` | page 70 | Restraint control module: a070 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a070_eventFrontLeftSeatbelt` | page 70 | Restraint control module: a070 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a070_eventFrontRightSeatbelt` | page 70 | Restraint control module: a070 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a070_eventVehicleSpeed` | page 70 | Restraint control module: a070 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a070_eventSteeringAngle` | page 70 | Restraint control module: a070 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a070_eventDriverBrakeApply` | page 70 | Restraint control module: a070 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a070_eventAccelPedalPos` | page 70 | Restraint control module: a070 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a071_eventArmStatus` | page 71 | Restraint control module: a071 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a071_eventFactoryMode` | page 71 | Restraint control module: a071 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a071_eventDiagEnabled` | page 71 | Restraint control module: a071 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a071_eventDriveOrientation` | page 71 | Restraint control module: a071 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a071_comChassisCANPH9MIA` | page 71 | Restraint control module: a071 com chassis CANPH9 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a071_comChassisCANPH9ChkSm` | page 71 | Restraint control module: a071 com chassis CANPH9 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a071_comChassisCANPH9Cntr` | page 71 | Restraint control module: a071 com chassis CANPH9 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a071_eventIDFsignal` | page 71 | Restraint control module: a071 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a071_eventFrontLeftSeatbelt` | page 71 | Restraint control module: a071 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a071_eventFrontRightSeatbelt` | page 71 | Restraint control module: a071 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a071_eventVehicleSpeed` | page 71 | Restraint control module: a071 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a071_eventSteeringAngle` | page 71 | Restraint control module: a071 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a071_eventDriverBrakeApply` | page 71 | Restraint control module: a071 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a071_eventAccelPedalPos` | page 71 | Restraint control module: a071 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a072_eventArmStatus` | page 72 | Restraint control module: a072 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a072_eventFactoryMode` | page 72 | Restraint control module: a072 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a072_eventDiagEnabled` | page 72 | Restraint control module: a072 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a072_eventDriveOrientation` | page 72 | Restraint control module: a072 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a072_comUnusedMIA` | page 72 | Restraint control module: a072 com unused MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a072_comUnusedChkSm` | page 72 | Restraint control module: a072 com unused chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a072_comUnusedCntr` | page 72 | Restraint control module: a072 com unused cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a072_eventIDFsignal` | page 72 | Restraint control module: a072 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a072_eventFrontLeftSeatbelt` | page 72 | Restraint control module: a072 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a072_eventFrontRightSeatbelt` | page 72 | Restraint control module: a072 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a072_eventVehicleSpeed` | page 72 | Restraint control module: a072 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a072_eventSteeringAngle` | page 72 | Restraint control module: a072 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a072_eventDriverBrakeApply` | page 72 | Restraint control module: a072 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a072_eventAccelPedalPos` | page 72 | Restraint control module: a072 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a073_eventArmStatus` | page 73 | Restraint control module: a073 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a073_eventFactoryMode` | page 73 | Restraint control module: a073 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a073_eventDiagEnabled` | page 73 | Restraint control module: a073 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a073_eventDriveOrientation` | page 73 | Restraint control module: a073 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a073_comChassisCANPH4MIA` | page 73 | Restraint control module: a073 com chassis CANPH4 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a073_comChassisCANPH4ChkSm` | page 73 | Restraint control module: a073 com chassis CANPH4 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a073_comChassisCANPH4Cntr` | page 73 | Restraint control module: a073 com chassis CANPH4 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a073_eventIDFsignal` | page 73 | Restraint control module: a073 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a073_eventFrontLeftSeatbelt` | page 73 | Restraint control module: a073 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a073_eventFrontRightSeatbelt` | page 73 | Restraint control module: a073 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a073_eventVehicleSpeed` | page 73 | Restraint control module: a073 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a073_eventSteeringAngle` | page 73 | Restraint control module: a073 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a073_eventDriverBrakeApply` | page 73 | Restraint control module: a073 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a073_eventAccelPedalPos` | page 73 | Restraint control module: a073 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a074_eventArmStatus` | page 74 | Restraint control module: a074 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a074_eventFactoryMode` | page 74 | Restraint control module: a074 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a074_eventDiagEnabled` | page 74 | Restraint control module: a074 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a074_eventDriveOrientation` | page 74 | Restraint control module: a074 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a074_comChassisCANPH5MIA` | page 74 | Restraint control module: a074 com chassis CANPH5 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a074_comChassisCANPH5ChkSm` | page 74 | Restraint control module: a074 com chassis CANPH5 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a074_comChassisCANPH5Cntr` | page 74 | Restraint control module: a074 com chassis CANPH5 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a074_eventIDFsignal` | page 74 | Restraint control module: a074 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a074_eventFrontLeftSeatbelt` | page 74 | Restraint control module: a074 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a074_eventFrontRightSeatbelt` | page 74 | Restraint control module: a074 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a074_eventVehicleSpeed` | page 74 | Restraint control module: a074 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a074_eventSteeringAngle` | page 74 | Restraint control module: a074 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a074_eventDriverBrakeApply` | page 74 | Restraint control module: a074 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a074_eventAccelPedalPos` | page 74 | Restraint control module: a074 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a075_eventArmStatus` | page 75 | Restraint control module: a075 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a075_eventFactoryMode` | page 75 | Restraint control module: a075 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a075_eventDiagEnabled` | page 75 | Restraint control module: a075 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a075_eventDriveOrientation` | page 75 | Restraint control module: a075 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a075_comChassisCANPH6MIA` | page 75 | Restraint control module: a075 com chassis CANPH6 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a075_comChassisCANPH6ChkSm` | page 75 | Restraint control module: a075 com chassis CANPH6 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a075_comChassisCANPH6Cntr` | page 75 | Restraint control module: a075 com chassis CANPH6 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a075_eventIDFsignal` | page 75 | Restraint control module: a075 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a075_eventFrontLeftSeatbelt` | page 75 | Restraint control module: a075 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a075_eventFrontRightSeatbelt` | page 75 | Restraint control module: a075 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a075_eventVehicleSpeed` | page 75 | Restraint control module: a075 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a075_eventSteeringAngle` | page 75 | Restraint control module: a075 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a075_eventDriverBrakeApply` | page 75 | Restraint control module: a075 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a075_eventAccelPedalPos` | page 75 | Restraint control module: a075 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a078_eventArmStatus` | page 78 | Restraint control module: a078 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a078_eventFactoryMode` | page 78 | Restraint control module: a078 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a078_eventDiagEnabled` | page 78 | Restraint control module: a078 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a078_eventDriveOrientation` | page 78 | Restraint control module: a078 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a078_comOCS1PMIA` | page 78 | Restraint control module: a078 com OCS1 PMIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a078_comOCS1PChkSm` | page 78 | Restraint control module: a078 com OCS1 p chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a078_comOCS1PCntr` | page 78 | Restraint control module: a078 com OCS1 p cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a078_eventIDFsignal` | page 78 | Restraint control module: a078 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a078_eventFrontLeftSeatbelt` | page 78 | Restraint control module: a078 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a078_eventFrontRightSeatbelt` | page 78 | Restraint control module: a078 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a078_eventVehicleSpeed` | page 78 | Restraint control module: a078 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a078_eventSteeringAngle` | page 78 | Restraint control module: a078 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a078_eventDriverBrakeApply` | page 78 | Restraint control module: a078 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a078_eventAccelPedalPos` | page 78 | Restraint control module: a078 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a079_eventArmStatus` | page 79 | Restraint control module: a079 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a079_eventFactoryMode` | page 79 | Restraint control module: a079 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a079_eventDiagEnabled` | page 79 | Restraint control module: a079 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a079_eventDriveOrientation` | page 79 | Restraint control module: a079 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a079_comOCS1DMIA` | page 79 | Restraint control module: a079 com OCS1 DMIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a079_comOCS1DChkSm` | page 79 | Restraint control module: a079 com OCS1 d chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a079_comOCS1DCntr` | page 79 | Restraint control module: a079 com OCS1 d cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a079_eventIDFsignal` | page 79 | Restraint control module: a079 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a079_eventFrontLeftSeatbelt` | page 79 | Restraint control module: a079 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a079_eventFrontRightSeatbelt` | page 79 | Restraint control module: a079 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a079_eventVehicleSpeed` | page 79 | Restraint control module: a079 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a079_eventSteeringAngle` | page 79 | Restraint control module: a079 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a079_eventDriverBrakeApply` | page 79 | Restraint control module: a079 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a079_eventAccelPedalPos` | page 79 | Restraint control module: a079 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a080_eventArmStatus` | page 80 | Restraint control module: a080 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a080_eventFactoryMode` | page 80 | Restraint control module: a080 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a080_eventDiagEnabled` | page 80 | Restraint control module: a080 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a080_eventDriveOrientation` | page 80 | Restraint control module: a080 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a080_comGTWACSMIA` | page 80 | Restraint control module: a080 com GTWACSMIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a080_comGTWACSChkSm` | page 80 | Restraint control module: a080 com GTWACS chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a080_comGTWACSCntr` | page 80 | Restraint control module: a080 com GTWACS cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a080_eventIDFsignal` | page 80 | Restraint control module: a080 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a080_eventFrontLeftSeatbelt` | page 80 | Restraint control module: a080 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a080_eventFrontRightSeatbelt` | page 80 | Restraint control module: a080 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a080_eventVehicleSpeed` | page 80 | Restraint control module: a080 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a080_eventSteeringAngle` | page 80 | Restraint control module: a080 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a080_eventDriverBrakeApply` | page 80 | Restraint control module: a080 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a080_eventAccelPedalPos` | page 80 | Restraint control module: a080 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a083_eventArmStatus` | page 83 | Restraint control module: a083 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a083_eventFactoryMode` | page 83 | Restraint control module: a083 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a083_eventDiagEnabled` | page 83 | Restraint control module: a083 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a083_eventDriveOrientation` | page 83 | Restraint control module: a083 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a083_comGTWCarStateMIA` | page 83 | Restraint control module: a083 com GTW car state MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a083_eventIDFsignal` | page 83 | Restraint control module: a083 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a083_eventFrontLeftSeatbelt` | page 83 | Restraint control module: a083 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a083_eventFrontRightSeatbelt` | page 83 | Restraint control module: a083 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a083_eventVehicleSpeed` | page 83 | Restraint control module: a083 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a083_eventSteeringAngle` | page 83 | Restraint control module: a083 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a083_eventDriverBrakeApply` | page 83 | Restraint control module: a083 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a083_eventAccelPedalPos` | page 83 | Restraint control module: a083 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a087_eventArmStatus` | page 87 | Restraint control module: a087 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a087_eventFactoryMode` | page 87 | Restraint control module: a087 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a087_eventDiagEnabled` | page 87 | Restraint control module: a087 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a087_eventDriveOrientation` | page 87 | Restraint control module: a087 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a087_comChassisCANSilent` | page 87 | Restraint control module: a087 com chassis CAN silent | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a087_comPARTYCANSilent` | page 87 | Restraint control module: a087 com PARTYCAN silent | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a087_comUnusedCANSilent` | page 87 | Restraint control module: a087 com unused CAN silent | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a087_eventIDFsignal` | page 87 | Restraint control module: a087 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a087_eventFrontLeftSeatbelt` | page 87 | Restraint control module: a087 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a087_eventFrontRightSeatbelt` | page 87 | Restraint control module: a087 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a087_eventVehicleSpeed` | page 87 | Restraint control module: a087 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a087_eventSteeringAngle` | page 87 | Restraint control module: a087 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a087_eventDriverBrakeApply` | page 87 | Restraint control module: a087 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a087_eventAccelPedalPos` | page 87 | Restraint control module: a087 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a088_eventArmStatus` | page 88 | Restraint control module: a088 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a088_eventFactoryMode` | page 88 | Restraint control module: a088 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a088_eventDiagEnabled` | page 88 | Restraint control module: a088 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a088_eventDriveOrientation` | page 88 | Restraint control module: a088 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a088_comChassisCANPH2MIA` | page 88 | Restraint control module: a088 com chassis CANPH2 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a088_comChassisCANPH2ChkSm` | page 88 | Restraint control module: a088 com chassis CANPH2 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a088_comChassisCANPH2Cntr` | page 88 | Restraint control module: a088 com chassis CANPH2 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a088_eventIDFsignal` | page 88 | Restraint control module: a088 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a088_eventFrontLeftSeatbelt` | page 88 | Restraint control module: a088 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a088_eventFrontRightSeatbelt` | page 88 | Restraint control module: a088 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a088_eventVehicleSpeed` | page 88 | Restraint control module: a088 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a088_eventSteeringAngle` | page 88 | Restraint control module: a088 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a088_eventDriverBrakeApply` | page 88 | Restraint control module: a088 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a088_eventAccelPedalPos` | page 88 | Restraint control module: a088 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a089_eventArmStatus` | page 89 | Restraint control module: a089 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a089_eventFactoryMode` | page 89 | Restraint control module: a089 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a089_eventDiagEnabled` | page 89 | Restraint control module: a089 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a089_eventDriveOrientation` | page 89 | Restraint control module: a089 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a089_comChassisCANPH3MIA` | page 89 | Restraint control module: a089 com chassis CANPH3 MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a089_comChassisCANPH3ChkSm` | page 89 | Restraint control module: a089 com chassis CANPH3 chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a089_comChassisCANPH3Cntr` | page 89 | Restraint control module: a089 com chassis CANPH3 cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a089_eventIDFsignal` | page 89 | Restraint control module: a089 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a089_eventFrontLeftSeatbelt` | page 89 | Restraint control module: a089 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a089_eventFrontRightSeatbelt` | page 89 | Restraint control module: a089 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a089_eventVehicleSpeed` | page 89 | Restraint control module: a089 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a089_eventSteeringAngle` | page 89 | Restraint control module: a089 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a089_eventDriverBrakeApply` | page 89 | Restraint control module: a089 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a089_eventAccelPedalPos` | page 89 | Restraint control module: a089 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a090_eventArmStatus` | page 90 | Restraint control module: a090 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a090_eventFactoryMode` | page 90 | Restraint control module: a090 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a090_eventDiagEnabled` | page 90 | Restraint control module: a090 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a090_eventDriveOrientation` | page 90 | Restraint control module: a090 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a090_comPartyCANBusOff` | page 90 | Restraint control module: a090 com party CAN bus off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a090_eventIDFsignal` | page 90 | Restraint control module: a090 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a090_eventFrontLeftSeatbelt` | page 90 | Restraint control module: a090 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a090_eventFrontRightSeatbelt` | page 90 | Restraint control module: a090 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a090_eventVehicleSpeed` | page 90 | Restraint control module: a090 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a090_eventSteeringAngle` | page 90 | Restraint control module: a090 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a090_eventDriverBrakeApply` | page 90 | Restraint control module: a090 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a090_eventAccelPedalPos` | page 90 | Restraint control module: a090 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a092_eventArmStatus` | page 92 | Restraint control module: a092 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a092_eventFactoryMode` | page 92 | Restraint control module: a092 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a092_eventDiagEnabled` | page 92 | Restraint control module: a092 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a092_eventDriveOrientation` | page 92 | Restraint control module: a092 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a092_comDASSafetyFrontMIA` | page 92 | Restraint control module: a092 com DAS safety front MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a092_comDASSafetyFrontChkSm` | page 92 | Restraint control module: a092 com DAS safety front chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a092_comDASSafetyFrontCntr` | page 92 | Restraint control module: a092 com DAS safety front cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a092_eventIDFsignal` | page 92 | Restraint control module: a092 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a092_eventFrontLeftSeatbelt` | page 92 | Restraint control module: a092 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a092_eventFrontRightSeatbelt` | page 92 | Restraint control module: a092 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a092_eventVehicleSpeed` | page 92 | Restraint control module: a092 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a092_eventSteeringAngle` | page 92 | Restraint control module: a092 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a092_eventDriverBrakeApply` | page 92 | Restraint control module: a092 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a092_eventAccelPedalPos` | page 92 | Restraint control module: a092 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a093_eventArmStatus` | page 93 | Restraint control module: a093 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a093_eventFactoryMode` | page 93 | Restraint control module: a093 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a093_eventDiagEnabled` | page 93 | Restraint control module: a093 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a093_eventDriveOrientation` | page 93 | Restraint control module: a093 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a093_comVCLEFTStatusMIA` | page 93 | Restraint control module: a093 com VCLEFT status MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_comVCLEFTStatusChkSm` | page 93 | Restraint control module: a093 com VCLEFT status chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_comVCLEFTStatusCntr` | page 93 | Restraint control module: a093 com VCLEFT status cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_bucklSwVCFrontLeftFault` | page 93 | Restraint control module: a093 buckl sw VC front left fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_bucklSwVCRearLeftFault` | page 93 | Restraint control module: a093 buckl sw VC rear left fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_eventIDFsignal` | page 93 | Restraint control module: a093 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a093_eventFrontLeftSeatbelt` | page 93 | Restraint control module: a093 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a093_eventFrontRightSeatbelt` | page 93 | Restraint control module: a093 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a093_eventVehicleSpeed` | page 93 | Restraint control module: a093 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a093_eventSteeringAngle` | page 93 | Restraint control module: a093 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a093_eventDriverBrakeApply` | page 93 | Restraint control module: a093 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a093_eventAccelPedalPos` | page 93 | Restraint control module: a093 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a094_eventArmStatus` | page 94 | Restraint control module: a094 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a094_eventFactoryMode` | page 94 | Restraint control module: a094 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a094_eventDiagEnabled` | page 94 | Restraint control module: a094 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a094_eventDriveOrientation` | page 94 | Restraint control module: a094 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a094_comVCRIGHTStatusMIA` | page 94 | Restraint control module: a094 com VCRIGHT status MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_comVCRIGHTStatusChkSm` | page 94 | Restraint control module: a094 com VCRIGHT status chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_comVCRIGHTStatusCntr` | page 94 | Restraint control module: a094 com VCRIGHT status cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_bucklSwVCFrontRghtFault` | page 94 | Restraint control module: a094 buckl sw VC front rght fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_bucklSwVCRearRghtFault` | page 94 | Restraint control module: a094 buckl sw VC rear rght fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_bucklSwVCRearCnterFault` | page 94 | Restraint control module: a094 buckl sw VC rear cnter fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_eventIDFsignal` | page 94 | Restraint control module: a094 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a094_eventFrontLeftSeatbelt` | page 94 | Restraint control module: a094 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a094_eventFrontRightSeatbelt` | page 94 | Restraint control module: a094 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a094_eventVehicleSpeed` | page 94 | Restraint control module: a094 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a094_eventSteeringAngle` | page 94 | Restraint control module: a094 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a094_eventDriverBrakeApply` | page 94 | Restraint control module: a094 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a094_eventAccelPedalPos` | page 94 | Restraint control module: a094 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a101_eventArmStatus` | page 101 | Restraint control module: a101 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a101_eventFactoryMode` | page 101 | Restraint control module: a101 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a101_eventDiagEnabled` | page 101 | Restraint control module: a101 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a101_eventDriveOrientation` | page 101 | Restraint control module: a101 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a101_idfMisuseMonitoringErr` | page 101 | Restraint control module: a101 idf misuse monitoring err | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a101_idfEnviMonitoringError` | page 101 | Restraint control module: a101 idf envi monitoring error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a101_idfEnviMonitoringEvent` | page 101 | Restraint control module: a101 idf envi monitoring event | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a101_eventIDFsignal` | page 101 | Restraint control module: a101 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a101_eventFrontLeftSeatbelt` | page 101 | Restraint control module: a101 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a101_eventFrontRightSeatbelt` | page 101 | Restraint control module: a101 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a101_eventVehicleSpeed` | page 101 | Restraint control module: a101 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a101_eventSteeringAngle` | page 101 | Restraint control module: a101 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a101_eventDriverBrakeApply` | page 101 | Restraint control module: a101 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a101_eventAccelPedalPos` | page 101 | Restraint control module: a101 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a102_eventArmStatus` | page 102 | Restraint control module: a102 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a102_eventFactoryMode` | page 102 | Restraint control module: a102 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a102_eventDiagEnabled` | page 102 | Restraint control module: a102 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a102_eventDriveOrientation` | page 102 | Restraint control module: a102 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a102_imuYawR8OffCompPosLife` | page 102 | Restraint control module: a102 imu yaw R8 off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffCompNegLife` | page 102 | Restraint control module: a102 imu yaw R8 off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffCompPosFLDC` | page 102 | Restraint control module: a102 imu yaw R8 off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffCompNegFLDC` | page 102 | Restraint control module: a102 imu yaw R8 off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffCompPosSLDC` | page 102 | Restraint control module: a102 imu yaw R8 off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffCompNegSLDC` | page 102 | Restraint control module: a102 imu yaw R8 off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_eventIDFsignal` | page 102 | Restraint control module: a102 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a102_eventFrontLeftSeatbelt` | page 102 | Restraint control module: a102 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a102_eventFrontRightSeatbelt` | page 102 | Restraint control module: a102 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a102_eventVehicleSpeed` | page 102 | Restraint control module: a102 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a102_eventSteeringAngle` | page 102 | Restraint control module: a102 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a102_eventDriverBrakeApply` | page 102 | Restraint control module: a102 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a102_eventAccelPedalPos` | page 102 | Restraint control module: a102 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a103_eventArmStatus` | page 103 | Restraint control module: a103 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a103_eventFactoryMode` | page 103 | Restraint control module: a103 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a103_eventDiagEnabled` | page 103 | Restraint control module: a103 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a103_eventDriveOrientation` | page 103 | Restraint control module: a103 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a103_imuPtchR8OffCompPosLife` | page 103 | Restraint control module: a103 imu ptch R8 off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffCompNegLife` | page 103 | Restraint control module: a103 imu ptch R8 off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffCompPosFLDC` | page 103 | Restraint control module: a103 imu ptch R8 off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffCompNegFLDC` | page 103 | Restraint control module: a103 imu ptch R8 off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffCompPosSLDC` | page 103 | Restraint control module: a103 imu ptch R8 off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffCompNegSLDC` | page 103 | Restraint control module: a103 imu ptch R8 off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_eventIDFsignal` | page 103 | Restraint control module: a103 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a103_eventFrontLeftSeatbelt` | page 103 | Restraint control module: a103 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a103_eventFrontRightSeatbelt` | page 103 | Restraint control module: a103 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a103_eventVehicleSpeed` | page 103 | Restraint control module: a103 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a103_eventSteeringAngle` | page 103 | Restraint control module: a103 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a103_eventDriverBrakeApply` | page 103 | Restraint control module: a103 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a103_eventAccelPedalPos` | page 103 | Restraint control module: a103 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a104_eventArmStatus` | page 104 | Restraint control module: a104 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a104_eventFactoryMode` | page 104 | Restraint control module: a104 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a104_eventDiagEnabled` | page 104 | Restraint control module: a104 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a104_eventDriveOrientation` | page 104 | Restraint control module: a104 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a104_imuRollR8OffCompPosLife` | page 104 | Restraint control module: a104 imu roll R8 off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffCompNegLife` | page 104 | Restraint control module: a104 imu roll R8 off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffCompPosFLDC` | page 104 | Restraint control module: a104 imu roll R8 off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffCompNegFLDC` | page 104 | Restraint control module: a104 imu roll R8 off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffCompPosSLDC` | page 104 | Restraint control module: a104 imu roll R8 off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffCompNegSLDC` | page 104 | Restraint control module: a104 imu roll R8 off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_eventIDFsignal` | page 104 | Restraint control module: a104 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a104_eventFrontLeftSeatbelt` | page 104 | Restraint control module: a104 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a104_eventFrontRightSeatbelt` | page 104 | Restraint control module: a104 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a104_eventVehicleSpeed` | page 104 | Restraint control module: a104 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a104_eventSteeringAngle` | page 104 | Restraint control module: a104 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a104_eventDriverBrakeApply` | page 104 | Restraint control module: a104 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a104_eventAccelPedalPos` | page 104 | Restraint control module: a104 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a105_eventArmStatus` | page 105 | Restraint control module: a105 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a105_eventFactoryMode` | page 105 | Restraint control module: a105 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a105_eventDiagEnabled` | page 105 | Restraint control module: a105 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a105_eventDriveOrientation` | page 105 | Restraint control module: a105 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a105_imuLongAOffCompPosLife` | page 105 | Restraint control module: a105 imu long a off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAOffCompNegLife` | page 105 | Restraint control module: a105 imu long a off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAOffCompPosFLDC` | page 105 | Restraint control module: a105 imu long a off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAOffCompNegFLDC` | page 105 | Restraint control module: a105 imu long a off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAOffCompPosSLDC` | page 105 | Restraint control module: a105 imu long a off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAOffCompNegSLDC` | page 105 | Restraint control module: a105 imu long a off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_eventIDFsignal` | page 105 | Restraint control module: a105 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a105_eventFrontLeftSeatbelt` | page 105 | Restraint control module: a105 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a105_eventFrontRightSeatbelt` | page 105 | Restraint control module: a105 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a105_eventVehicleSpeed` | page 105 | Restraint control module: a105 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a105_eventSteeringAngle` | page 105 | Restraint control module: a105 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a105_eventDriverBrakeApply` | page 105 | Restraint control module: a105 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a105_eventAccelPedalPos` | page 105 | Restraint control module: a105 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a106_eventArmStatus` | page 106 | Restraint control module: a106 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a106_eventFactoryMode` | page 106 | Restraint control module: a106 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a106_eventDiagEnabled` | page 106 | Restraint control module: a106 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a106_eventDriveOrientation` | page 106 | Restraint control module: a106 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a106_imuLatAcOffCompPosLife` | page 106 | Restraint control module: a106 imu lat ac off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAcOffCompNegLife` | page 106 | Restraint control module: a106 imu lat ac off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAcOffCompPosFLDC` | page 106 | Restraint control module: a106 imu lat ac off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAcOffCompNegFLDC` | page 106 | Restraint control module: a106 imu lat ac off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAcOffCompPosSLDC` | page 106 | Restraint control module: a106 imu lat ac off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAcOffCompNegSLDC` | page 106 | Restraint control module: a106 imu lat ac off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_eventIDFsignal` | page 106 | Restraint control module: a106 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a106_eventFrontLeftSeatbelt` | page 106 | Restraint control module: a106 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a106_eventFrontRightSeatbelt` | page 106 | Restraint control module: a106 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a106_eventVehicleSpeed` | page 106 | Restraint control module: a106 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a106_eventSteeringAngle` | page 106 | Restraint control module: a106 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a106_eventDriverBrakeApply` | page 106 | Restraint control module: a106 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a106_eventAccelPedalPos` | page 106 | Restraint control module: a106 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a107_eventArmStatus` | page 107 | Restraint control module: a107 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a107_eventFactoryMode` | page 107 | Restraint control module: a107 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a107_eventDiagEnabled` | page 107 | Restraint control module: a107 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a107_eventDriveOrientation` | page 107 | Restraint control module: a107 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a107_imuVertAOffCompPosLife` | page 107 | Restraint control module: a107 imu vert a off comp pos life | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAOffCompNegLife` | page 107 | Restraint control module: a107 imu vert a off comp neg life | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAOffCompPosFLDC` | page 107 | Restraint control module: a107 imu vert a off comp pos FLDC | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAOffCompNegFLDC` | page 107 | Restraint control module: a107 imu vert a off comp neg FLDC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAOffCompPosSLDC` | page 107 | Restraint control module: a107 imu vert a off comp pos SLDC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAOffCompNegSLDC` | page 107 | Restraint control module: a107 imu vert a off comp neg SLDC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_eventIDFsignal` | page 107 | Restraint control module: a107 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a107_eventFrontLeftSeatbelt` | page 107 | Restraint control module: a107 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a107_eventFrontRightSeatbelt` | page 107 | Restraint control module: a107 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a107_eventVehicleSpeed` | page 107 | Restraint control module: a107 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a107_eventSteeringAngle` | page 107 | Restraint control module: a107 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a107_eventDriverBrakeApply` | page 107 | Restraint control module: a107 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a107_eventAccelPedalPos` | page 107 | Restraint control module: a107 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a108_eventArmStatus` | page 108 | Restraint control module: a108 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a108_eventFactoryMode` | page 108 | Restraint control module: a108 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a108_eventDiagEnabled` | page 108 | Restraint control module: a108 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a108_eventDriveOrientation` | page 108 | Restraint control module: a108 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a108_crashAlgoWakeupSig` | page 108 | Restraint control module: a108 crash algo wakeup sig | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a108_eventIDFsignal` | page 108 | Restraint control module: a108 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a108_eventFrontLeftSeatbelt` | page 108 | Restraint control module: a108 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a108_eventFrontRightSeatbelt` | page 108 | Restraint control module: a108 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a108_eventVehicleSpeed` | page 108 | Restraint control module: a108 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a108_eventSteeringAngle` | page 108 | Restraint control module: a108 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a108_eventDriverBrakeApply` | page 108 | Restraint control module: a108 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a108_eventAccelPedalPos` | page 108 | Restraint control module: a108 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a109_eventArmStatus` | page 109 | Restraint control module: a109 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a109_eventFactoryMode` | page 109 | Restraint control module: a109 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a109_eventDiagEnabled` | page 109 | Restraint control module: a109 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a109_eventDriveOrientation` | page 109 | Restraint control module: a109 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a109_immunityThrsholdCrossed` | page 109 | Restraint control module: a109 immunity thrshold crossed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a109_eventIDFsignal` | page 109 | Restraint control module: a109 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a109_eventFrontLeftSeatbelt` | page 109 | Restraint control module: a109 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a109_eventFrontRightSeatbelt` | page 109 | Restraint control module: a109 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a109_eventVehicleSpeed` | page 109 | Restraint control module: a109 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a109_eventSteeringAngle` | page 109 | Restraint control module: a109 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a109_eventDriverBrakeApply` | page 109 | Restraint control module: a109 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a109_eventAccelPedalPos` | page 109 | Restraint control module: a109 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a110_eventArmStatus` | page 110 | Restraint control module: a110 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a110_eventFactoryMode` | page 110 | Restraint control module: a110 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a110_eventDiagEnabled` | page 110 | Restraint control module: a110 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a110_eventDriveOrientation` | page 110 | Restraint control module: a110 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a110_inFactoryMode` | page 110 | Restraint control module: a110 in factory mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a110_eventIDFsignal` | page 110 | Restraint control module: a110 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a110_eventFrontLeftSeatbelt` | page 110 | Restraint control module: a110 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a110_eventFrontRightSeatbelt` | page 110 | Restraint control module: a110 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a110_eventVehicleSpeed` | page 110 | Restraint control module: a110 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a110_eventSteeringAngle` | page 110 | Restraint control module: a110 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a110_eventDriverBrakeApply` | page 110 | Restraint control module: a110 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a110_eventAccelPedalPos` | page 110 | Restraint control module: a110 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a112_eventArmStatus` | page 112 | Restraint control module: a112 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a112_eventFactoryMode` | page 112 | Restraint control module: a112 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a112_eventDiagEnabled` | page 112 | Restraint control module: a112 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a112_eventDriveOrientation` | page 112 | Restraint control module: a112 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a112_imuYawR8SnsrMonitTmp` | page 112 | Restraint control module: a112 imu yaw R8 snsr monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a112_imuYawR8SnsrMonitPerm` | page 112 | Restraint control module: a112 imu yaw R8 snsr monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a112_imuYawR8ChnlMonitTmp` | page 112 | Restraint control module: a112 imu yaw R8 chnl monit tmp | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a112_imuYawR8ChnlMonitPerm` | page 112 | Restraint control module: a112 imu yaw R8 chnl monit perm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a112_eventIDFsignal` | page 112 | Restraint control module: a112 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a112_eventFrontLeftSeatbelt` | page 112 | Restraint control module: a112 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a112_eventFrontRightSeatbelt` | page 112 | Restraint control module: a112 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a112_eventVehicleSpeed` | page 112 | Restraint control module: a112 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a112_eventSteeringAngle` | page 112 | Restraint control module: a112 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a112_eventDriverBrakeApply` | page 112 | Restraint control module: a112 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a112_eventAccelPedalPos` | page 112 | Restraint control module: a112 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a113_eventArmStatus` | page 113 | Restraint control module: a113 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a113_eventFactoryMode` | page 113 | Restraint control module: a113 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a113_eventDiagEnabled` | page 113 | Restraint control module: a113 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a113_eventDriveOrientation` | page 113 | Restraint control module: a113 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a113_imuPitchR8SnsrMonitTmp` | page 113 | Restraint control module: a113 imu pitch R8 snsr monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a113_imuPitchR8SnsrMonitPerm` | page 113 | Restraint control module: a113 imu pitch R8 snsr monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a113_imuPitchR8ChnlMonitTmp` | page 113 | Restraint control module: a113 imu pitch R8 chnl monit tmp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a113_imuPitchR8ChnlMonitPerm` | page 113 | Restraint control module: a113 imu pitch R8 chnl monit perm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a113_eventIDFsignal` | page 113 | Restraint control module: a113 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a113_eventFrontLeftSeatbelt` | page 113 | Restraint control module: a113 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a113_eventFrontRightSeatbelt` | page 113 | Restraint control module: a113 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a113_eventVehicleSpeed` | page 113 | Restraint control module: a113 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a113_eventSteeringAngle` | page 113 | Restraint control module: a113 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a113_eventDriverBrakeApply` | page 113 | Restraint control module: a113 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a113_eventAccelPedalPos` | page 113 | Restraint control module: a113 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a114_eventArmStatus` | page 114 | Restraint control module: a114 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a114_eventFactoryMode` | page 114 | Restraint control module: a114 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a114_eventDiagEnabled` | page 114 | Restraint control module: a114 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a114_eventDriveOrientation` | page 114 | Restraint control module: a114 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a114_imuRollR8SnsrMonitTmp` | page 114 | Restraint control module: a114 imu roll R8 snsr monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a114_imuRollR8SnsrMonitPerm` | page 114 | Restraint control module: a114 imu roll R8 snsr monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a114_imuRollR8ChnlMonitTmp` | page 114 | Restraint control module: a114 imu roll R8 chnl monit tmp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a114_imuRollR8ChnlMonitPerm` | page 114 | Restraint control module: a114 imu roll R8 chnl monit perm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a114_eventIDFsignal` | page 114 | Restraint control module: a114 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a114_eventFrontLeftSeatbelt` | page 114 | Restraint control module: a114 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a114_eventFrontRightSeatbelt` | page 114 | Restraint control module: a114 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a114_eventVehicleSpeed` | page 114 | Restraint control module: a114 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a114_eventSteeringAngle` | page 114 | Restraint control module: a114 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a114_eventDriverBrakeApply` | page 114 | Restraint control module: a114 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a114_eventAccelPedalPos` | page 114 | Restraint control module: a114 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a115_eventArmStatus` | page 115 | Restraint control module: a115 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a115_eventFactoryMode` | page 115 | Restraint control module: a115 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a115_eventDiagEnabled` | page 115 | Restraint control module: a115 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a115_eventDriveOrientation` | page 115 | Restraint control module: a115 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a115_imuLinAccChnlMonitTmp` | page 115 | Restraint control module: a115 imu lin acc chnl monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a115_imuLinAccChnlMonitPerm` | page 115 | Restraint control module: a115 imu lin acc chnl monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a115_eventIDFsignal` | page 115 | Restraint control module: a115 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a115_eventFrontLeftSeatbelt` | page 115 | Restraint control module: a115 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a115_eventFrontRightSeatbelt` | page 115 | Restraint control module: a115 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a115_eventVehicleSpeed` | page 115 | Restraint control module: a115 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a115_eventSteeringAngle` | page 115 | Restraint control module: a115 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a115_eventDriverBrakeApply` | page 115 | Restraint control module: a115 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a115_eventAccelPedalPos` | page 115 | Restraint control module: a115 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a116_eventArmStatus` | page 116 | Restraint control module: a116 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a116_eventFactoryMode` | page 116 | Restraint control module: a116 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a116_eventDiagEnabled` | page 116 | Restraint control module: a116 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a116_eventDriveOrientation` | page 116 | Restraint control module: a116 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a116_imuLatAccChnlMonitTmp` | page 116 | Restraint control module: a116 imu lat acc chnl monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a116_imuLatAccChnlMonitPerm` | page 116 | Restraint control module: a116 imu lat acc chnl monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a116_eventIDFsignal` | page 116 | Restraint control module: a116 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a116_eventFrontLeftSeatbelt` | page 116 | Restraint control module: a116 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a116_eventFrontRightSeatbelt` | page 116 | Restraint control module: a116 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a116_eventVehicleSpeed` | page 116 | Restraint control module: a116 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a116_eventSteeringAngle` | page 116 | Restraint control module: a116 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a116_eventDriverBrakeApply` | page 116 | Restraint control module: a116 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a116_eventAccelPedalPos` | page 116 | Restraint control module: a116 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a117_eventArmStatus` | page 117 | Restraint control module: a117 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a117_eventFactoryMode` | page 117 | Restraint control module: a117 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a117_eventDiagEnabled` | page 117 | Restraint control module: a117 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a117_eventDriveOrientation` | page 117 | Restraint control module: a117 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a117_imuZaccelChnlMonitTmp` | page 117 | Restraint control module: a117 imu zaccel chnl monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a117_imuZaccelChnlMonitPerm` | page 117 | Restraint control module: a117 imu zaccel chnl monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a117_eventIDFsignal` | page 117 | Restraint control module: a117 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a117_eventFrontLeftSeatbelt` | page 117 | Restraint control module: a117 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a117_eventFrontRightSeatbelt` | page 117 | Restraint control module: a117 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a117_eventVehicleSpeed` | page 117 | Restraint control module: a117 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a117_eventSteeringAngle` | page 117 | Restraint control module: a117 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a117_eventDriverBrakeApply` | page 117 | Restraint control module: a117 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a117_eventAccelPedalPos` | page 117 | Restraint control module: a117 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |
| `RCM_a118_eventArmStatus` | page 118 | Restraint control module: a118 event arm status | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNARMED`<br>1 = `ARMED` | plausible |
| `RCM_a118_eventFactoryMode` | page 118 | Restraint control module: a118 event factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a118_eventDiagEnabled` | page 118 | Restraint control module: a118 event diag enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `RCM_a118_eventDriveOrientation` | page 118 | Restraint control module: a118 event drive orientation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT_HAND_DRIVE`<br>1 = `RIGHT_HAND_DRIVE` | plausible |
| `RCM_a118_imuInPlaneSnsrMonitTmp` | page 118 | Restraint control module: a118 imu in plane snsr monit tmp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a118_imuInPlaneSnsrMonitPerm` | page 118 | Restraint control module: a118 imu in plane snsr monit perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a118_eventIDFsignal` | page 118 | Restraint control module: a118 event ID fsignal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | plausible |
| `RCM_a118_eventFrontLeftSeatbelt` | page 118 | Restraint control module: a118 event front left seatbelt | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a118_eventFrontRightSeatbelt` | page 118 | Restraint control module: a118 event front right seatbelt | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNLATCHED`<br>1 = `LATCHED` | plausible |
| `RCM_a118_eventVehicleSpeed` | page 118 | Restraint control module: a118 event vehicle speed | 28\|12 | little-endian | unsigned | 0.08 | -40 | kph | -40 to 287.6 |  | plausible |
| `RCM_a118_eventSteeringAngle` | page 118 | Restraint control module: a118 event steering angle | 45\|14 | big-endian | unsigned | 0.1 | -819.2 | deg | -819.2 to 819.1 |  | plausible |
| `RCM_a118_eventDriverBrakeApply` | page 118 | Restraint control module: a118 event driver brake apply; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `RCM_a118_eventAccelPedalPos` | page 118 | Restraint control module: a118 event accel pedal pos; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 101.6 | 255 = `SNA` | plausible |

## Multiplexing

`RCM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (20 signals), page 1 (17 signals), page 2 (12 signals), page 3 (12 signals), page 4 (19 signals), page 5 (12 signals), page 6 (13 signals), page 8 (14 signals), page 9 (12 signals), page 11 (12 signals), page 12 (13 signals), page 13 (13 signals), page 14 (17 signals), page 15 (17 signals), page 16 (17 signals), page 17 (17 signals), page 18 (17 signals), page 19 (17 signals), page 20 (17 signals), page 21 (17 signals), page 22 (17 signals), page 23 (17 signals), page 24 (17 signals), page 25 (17 signals), page 26 (17 signals), page 27 (17 signals), page 28 (17 signals), page 29 (17 signals), page 30 (17 signals), page 31 (17 signals), page 32 (17 signals), page 33 (17 signals), page 34 (17 signals), page 35 (17 signals), page 36 (17 signals), page 37 (17 signals), page 40 (17 signals), page 41 (17 signals), page 42 (14 signals), page 43 (14 signals), page 44 (19 signals), page 45 (19 signals), page 46 (19 signals), page 47 (19 signals), page 48 (19 signals), page 49 (19 signals), page 50 (19 signals), page 51 (20 signals), page 52 (20 signals), page 53 (20 signals), page 54 (20 signals), page 55 (13 signals), page 56 (13 signals), page 57 (13 signals), page 58 (17 signals), page 59 (17 signals), page 60 (17 signals), page 61 (17 signals), page 62 (17 signals), page 63 (17 signals), page 64 (15 signals), page 65 (15 signals), page 66 (15 signals), page 67 (12 signals), page 68 (12 signals), page 69 (14 signals), page 70 (14 signals), page 71 (14 signals), page 72 (14 signals), page 73 (14 signals), page 74 (14 signals), page 75 (14 signals), page 78 (14 signals), page 79 (14 signals), page 80 (14 signals), page 83 (12 signals), page 87 (14 signals), page 88 (14 signals), page 89 (14 signals), page 90 (12 signals), page 92 (14 signals), page 93 (16 signals), page 94 (17 signals), page 101 (14 signals), page 102 (17 signals), page 103 (17 signals), page 104 (17 signals), page 105 (17 signals), page 106 (17 signals), page 107 (17 signals), page 108 (12 signals), page 109 (12 signals), page 110 (12 signals), page 112 (15 signals), page 113 (15 signals), page 114 (15 signals), page 115 (13 signals), page 116 (13 signals), page 117 (13 signals), page 118 (13 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
