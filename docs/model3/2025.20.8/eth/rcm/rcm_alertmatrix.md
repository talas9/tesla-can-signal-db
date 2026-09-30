---
layout: default
title: "RCM_alertMatrix (0x371) — Restraint control module, Tesla Model 3 2025.20.8 ETH"
description: "Restraint control module message: alert matrix. Ethernet-side message RCM_alertMatrix of Restraint control module for Tesla Model 3 firmware 2025.20.8, 120 signals (RCM_matrixIndex, RCM_a000_crashDetected, RCM_a001_nearDeploy, RCM_a002_airbagsNotArmed and 116 more). Bit layout, scaling, units and value tables."
---

# RCM_alertMatrix (0x371) — Restraint control module, Tesla Model 3 2025.20.8 ETH

Restraint control module message: alert matrix. This page documents the 120 signals of RCM_alertMatrix as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_alertMatrix` |
| Ethernet-side id | 0x371 (881) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 120 |

## Signals of RCM_alertMatrix

Tesla Model 3 CAN bus signals in `RCM_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_matrixIndex` | selector | Restraint control module: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1` | plausible |
| `RCM_a000_crashDetected` | page 0 | Restraint control module: a000 crash detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a001_nearDeploy` | page 0 | Restraint control module: a001 near deploy | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a002_airbagsNotArmed` | page 0 | Restraint control module: a002 airbags not armed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a003_warningIndicator` | page 0 | Restraint control module: a003 warning indicator | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a004_internalFault` | page 0 | Restraint control module: a004 internal fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a005_crcError` | page 0 | Restraint control module: a005 crc error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a006_batteryVoltageRange` | page 0 | Restraint control module: a006 battery voltage range | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a007_powerSupplyExternal` | page 0 | Restraint control module: a007 power supply external | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a008_powerSupplyInternal` | page 0 | Restraint control module: a008 power supply internal | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a009_reprogramLimit` | page 0 | Restraint control module: a009 reprogram limit | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a010_scmDisabled` | page 0 | Restraint control module: a010 scm disabled | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a011_eepromDataLocked` | page 0 | Restraint control module: a011 eeprom data locked | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a012_vinStorage` | page 0 | Restraint control module: a012 vin storage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a013_driverOrientation` | page 0 | Restraint control module: a013 driver orientation | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a014_driverABStage1` | page 0 | Restraint control module: a014 driver AB stage1 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a015_driverABStage2` | page 0 | Restraint control module: a015 driver AB stage2 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a016_passABStage1` | page 0 | Restraint control module: a016 pass AB stage1 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a017_passABStage2` | page 0 | Restraint control module: a017 pass AB stage2 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a018_passengerActiveVent` | page 0 | Restraint control module: a018 passenger active vent | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a019_pretenShldrFrontLeft` | page 0 | Restraint control module: a019 preten shldr front left | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a020_pretenShldFrontRight` | page 0 | Restraint control module: a020 preten shld front right | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a021_pretenLapFrontLeft` | page 0 | Restraint control module: a021 preten lap front left | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a022_pretenLapFrontRight` | page 0 | Restraint control module: a022 preten lap front right | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a023_loadLimiterLeftSide` | page 0 | Restraint control module: a023 load limiter left side | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a024_loadLimiterRightSide` | page 0 | Restraint control module: a024 load limiter right side | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a025_kneeABDriver` | page 0 | Restraint control module: a025 knee AB driver | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a026_kneeABFrontPassenger` | page 0 | Restraint control module: a026 knee AB front passenger | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a027_sideAB1stRowLeft` | page 0 | Restraint control module: a027 side ab1st row left | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a028_sideAB1stRowRight` | page 0 | Restraint control module: a028 side ab1st row right | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a029_driverABActiveVent` | page 0 | Restraint control module: a029 driver AB active vent | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a030_farSideInboardAirbag` | page 0 | Restraint control module: a030 far side inboard airbag | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a031_frontCenterAirbag` | page 0 | Restraint control module: a031 front center airbag | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a032_curtainABLeft` | page 0 | Restraint control module: a032 curtain AB left | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a033_curtainABRight` | page 0 | Restraint control module: a033 curtain AB right | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a034_preten2ndRowLeft` | page 0 | Restraint control module: a034 preten2nd row left | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a035_preten2ndRowRight` | page 0 | Restraint control module: a035 preten2nd row right | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a036_curAB2ndRowLeft` | page 0 | Restraint control module: a036 cur ab2nd row left | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a037_curAB2ndRowRight` | page 0 | Restraint control module: a037 cur ab2nd row right | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a038_unusedA` | page 0 | Restraint control module: a038 unused a | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a039_unusedB` | page 0 | Restraint control module: a039 unused b | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a040_hoodActuatorRight` | page 0 | Restraint control module: a040 hood actuator right | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a041_hoodActuatorLeft` | page 0 | Restraint control module: a041 hood actuator left | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a042_ens1Line` | page 0 | Restraint control module: a042 ens1 line | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a043_ens2Line` | page 0 | Restraint control module: a043 ens2 line | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a044_upFrontSensorLeft` | page 0 | Restraint control module: a044 up front sensor left | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a045_upFrontSensorRight` | page 0 | Restraint control module: a045 up front sensor right | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a046_sideAccelBPillarLeft` | page 0 | Restraint control module: a046 side accel b pillar left | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a047_sideAccelBPillarRight` | page 0 | Restraint control module: a047 side accel b pillar right | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a048_sideAccelCPillarLeft` | page 0 | Restraint control module: a048 side accel c pillar left | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a049_sideAccelCPillarRight` | page 0 | Restraint control module: a049 side accel c pillar right | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a050_upFrontSensorCenter` | page 0 | Restraint control module: a050 up front sensor center | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a051_pressureFrontLftDoor` | page 0 | Restraint control module: a051 pressure front lft door | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a052_pressureFrontRtDoor` | page 0 | Restraint control module: a052 pressure front rt door | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a053_pressurePedProLeft` | page 0 | Restraint control module: a053 pressure ped pro left | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a054_pressurePedProRight` | page 0 | Restraint control module: a054 pressure ped pro right | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a055_inertialMeasurement` | page 0 | Restraint control module: a055 inertial measurement | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a056_passengerFrontOCS` | page 0 | Restraint control module: a056 passenger front OCS | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a057_driverOCS` | page 0 | Restraint control module: a057 driver OCS | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a058_buckle1stRowLeft` | page 0 | Restraint control module: a058 buckle1st row left | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a059_buckle1stRowRight` | page 0 | Restraint control module: a059 buckle1st row right | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a060_stpsLeft` | page 1 | Restraint control module: a060 stps left | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a061_stpsRight` | page 1 | Restraint control module: a061 stps right | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a062_alrSwitch` | page 1 | Restraint control module: a062 alr switch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a063_sbsw2ndRowRight` | page 1 | Restraint control module: a063 sbsw2nd row right | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a064_hardwareCodingPin1` | page 1 | Restraint control module: a064 hardware coding pin1 | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a065_driverOrientConfigPin` | page 1 | Restraint control module: a065 driver orient config pin | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a066_seatBackSw2ndRowLeft` | page 1 | Restraint control module: a066 seat back sw2nd row left | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a067_comCANInitFailure` | page 1 | Restraint control module: a067 com CAN init failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a068_comChassisBusOff` | page 1 | Restraint control module: a068 com chassis bus off | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a069_comCHCANPH7` | page 1 | Restraint control module: a069 com CHCANPH7 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a070_comCHCANPH8` | page 1 | Restraint control module: a070 com CHCANPH8 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a071_comCHCANPH9` | page 1 | Restraint control module: a071 com CHCANPH9 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a072_comUnused` | page 1 | Restraint control module: a072 com unused | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a073_comCHCANPH4` | page 1 | Restraint control module: a073 com CHCANPH4 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a074_comCHCANPH5` | page 1 | Restraint control module: a074 com CHCANPH5 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a075_comCHCANPH6` | page 1 | Restraint control module: a075 com CHCANPH6 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a076_comEPBLStatus` | page 1 | Restraint control module: a076 com EPBL status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a077_comEPBRStatus` | page 1 | Restraint control module: a077 com EPBR status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a078_comOCS1PStatus` | page 1 | Restraint control module: a078 com OCS1 p status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a079_comOCS1DStatus` | page 1 | Restraint control module: a079 com OCS1 d status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a080_comGTWACS` | page 1 | Restraint control module: a080 com GTWACS | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a081_comVCFRONTLVPwr` | page 1 | Restraint control module: a081 com VCFRONTLV pwr | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a082_comUIodo` | page 1 | Restraint control module: a082 com u iodo | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a083_comGTWCarState` | page 1 | Restraint control module: a083 com GTW car state | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a084_comTPMSStatus` | page 1 | Restraint control module: a084 com TPMS status | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a085_comGTWCarConfig` | page 1 | Restraint control module: a085 com GTW car config | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a086_comVINMIA` | page 1 | Restraint control module: a086 com VINMIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a087_comCANSilent` | page 1 | Restraint control module: a087 com CAN silent | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a088_comCHCANPH2` | page 1 | Restraint control module: a088 com CHCANPH2 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a089_comCHCANPH3` | page 1 | Restraint control module: a089 com CHCANPH3 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a090_comPartyBusOff` | page 1 | Restraint control module: a090 com party bus off | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a091_comEPAS3PsysStatus` | page 1 | Restraint control module: a091 com EPAS3 psys status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a092_comDASISF` | page 1 | Restraint control module: a092 com DASISF | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a093_comVCLEFTStatus` | page 1 | Restraint control module: a093 com VCLEFT status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a094_comVCRIGHTStatus` | page 1 | Restraint control module: a094 com VCRIGHT status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a095_comESPstatus` | page 1 | Restraint control module: a095 com ES pstatus | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a096_comESPwheelSpeeds` | page 1 | Restraint control module: a096 com ES pwheel speeds | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a097_comDIspeed` | page 1 | Restraint control module: a097 com d ispeed | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a098_comDIchassisControl` | page 1 | Restraint control module: a098 com d ichassis control | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a099_comDItorque` | page 1 | Restraint control module: a099 com d itorque | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a100_comDIsystemStatus` | page 1 | Restraint control module: a100 com d isystem status | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a101_idfSystem` | page 1 | Restraint control module: a101 idf system | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a102_imuYawR8OffstCompLim` | page 1 | Restraint control module: a102 imu yaw R8 offst comp lim | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a103_imuPtchR8OffstCompLim` | page 1 | Restraint control module: a103 imu ptch R8 offst comp lim | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a104_imuRollR8OffstCompLim` | page 1 | Restraint control module: a104 imu roll R8 offst comp lim | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a105_imuLongAccOffstCompLim` | page 1 | Restraint control module: a105 imu long acc offst comp lim | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a106_imuLatAccOffstCompLim` | page 1 | Restraint control module: a106 imu lat acc offst comp lim | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a107_imuVertAccOffstCompLim` | page 1 | Restraint control module: a107 imu vert acc offst comp lim | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a108_crashAlgoWakeup` | page 1 | Restraint control module: a108 crash algo wakeup | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a109_abuseImmunity` | page 1 | Restraint control module: a109 abuse immunity | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a110_factoryMode` | page 1 | Restraint control module: a110 factory mode | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a111_diagnosticsEnabled` | page 1 | Restraint control module: a111 diagnostics enabled | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a112_imuYawRate` | page 1 | Restraint control module: a112 imu yaw rate | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a113_imuPitchRate` | page 1 | Restraint control module: a113 imu pitch rate | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a114_imuRollRate` | page 1 | Restraint control module: a114 imu roll rate | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a115_imuLinearAcceleration` | page 1 | Restraint control module: a115 imu linear acceleration | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a116_imuLateralAcceleration` | page 1 | Restraint control module: a116 imu lateral acceleration | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a117_imuVerticalAcceleration` | page 1 | Restraint control module: a117 imu vertical acceleration | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM_a118_imuInPlaneAcceleration` | page 1 | Restraint control module: a118 imu in plane acceleration | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`RCM_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (59 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
