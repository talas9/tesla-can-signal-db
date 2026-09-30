---
layout: default
title: "RCM2_alertMatrix (0x3F1) — RCM2 ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "RCM2 ECU message: alert matrix. Ethernet-side message RCM2_alertMatrix of RCM2 ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 653 signals (RCM2_matrixIndex, RCM2_a000_crashDetected, RCM2_a001_nearDeploy, RCM2_a002_airbagsUnArmed and 649 more). Bit layout, scaling, units and value tables."
---

# RCM2_alertMatrix (0x3F1) — RCM2 ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

RCM2 ECU message: alert matrix. This page documents the 653 signals of RCM2_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCM2_alertMatrix` |
| Ethernet-side id | 0x3F1 (1009) |
| ECU | [RCM2 ECU](../../rcm2.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCM2 |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 653 |

## Signals of RCM2_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `RCM2_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCM2_matrixIndex` | selector | RCM2 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6`<br>7 = `AlertMatrix7`<br>8 = `AlertMatrix8`<br>9 = `AlertMatrix9`<br>10 = `AlertMatrix10` | plausible |
| `RCM2_a000_crashDetected` | page 0 | RCM2 ECU: a000 crash detected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a001_nearDeploy` | page 0 | RCM2 ECU: a001 near deploy | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a002_airbagsUnArmed` | page 0 | RCM2 ECU: a002 airbags un armed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a003_warningIndicator` | page 0 | RCM2 ECU: a003 warning indicator | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a004_crashAlgoWakeup` | page 0 | RCM2 ECU: a004 crash algo wakeup | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a005_abuseImmunityThrshold` | page 0 | RCM2 ECU: a005 abuse immunity thrshold | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a006_supplierDiagEnabled` | page 0 | RCM2 ECU: a006 supplier diag enabled | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a007_pedProCrashDetected` | page 0 | RCM2 ECU: a007 ped pro crash detected | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a008_factoryMode` | page 0 | RCM2 ECU: a008 factory mode | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a009_edrDataAreaLocked` | page 0 | RCM2 ECU: a009 edr data area locked | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a010_pedProEDRDataLocked` | page 0 | RCM2 ECU: a010 ped pro EDR data locked | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a011_placeholder0` | page 0 | RCM2 ECU: a011 placeholder0 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a012_placeholder1` | page 0 | RCM2 ECU: a012 placeholder1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a013_placeholder2` | page 0 | RCM2 ECU: a013 placeholder2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a014_pedProNearDeploy` | page 0 | RCM2 ECU: a014 ped pro near deploy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a015_noDeployCrashCal` | page 0 | RCM2 ECU: a015 no deploy crash cal | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a016_noDeployPedProCal` | page 0 | RCM2 ECU: a016 no deploy ped pro cal | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a017_ecuLogAvailable` | page 0 | RCM2 ECU: a017 ecu log available | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a047_batteryESRhigh` | page 0 | RCM2 ECU: a047 battery ES rhigh | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a048_batteryVoltageTooHigh` | page 0 | RCM2 ECU: a048 battery voltage too high | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a049_batteryVoltageTooLow` | page 0 | RCM2 ECU: a049 battery voltage too low | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a050_driverABStg1Sht2Gnd` | page 0 | RCM2 ECU: a050 driver AB stg1 sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a051_driverABStg1Sht2Bat` | page 0 | RCM2 ECU: a051 driver AB stg1 sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a052_driverABStg1Open` | page 0 | RCM2 ECU: a052 driver AB stg1 open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a053_driverABStg1Short` | page 0 | RCM2 ECU: a053 driver AB stg1 short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a054_driverABStg1CrssCoup` | page 0 | RCM2 ECU: a054 driver AB stg1 crss coup | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a055_driverABStg1Config` | page 0 | RCM2 ECU: a055 driver AB stg1 config | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a056_driverABStg2Sht2Gnd` | page 0 | RCM2 ECU: a056 driver AB stg2 sht2 gnd | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a057_driverABStg2Sht2Bat` | page 0 | RCM2 ECU: a057 driver AB stg2 sht2 bat | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a058_driverABStg2Open` | page 0 | RCM2 ECU: a058 driver AB stg2 open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a059_driverABStg2Short` | page 0 | RCM2 ECU: a059 driver AB stg2 short | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a060_driverABStg2CrssCoup` | page 0 | RCM2 ECU: a060 driver AB stg2 crss coup | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a061_driverABStg2Config` | page 0 | RCM2 ECU: a061 driver AB stg2 config | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a062_passABStg1Sht2Gnd` | page 0 | RCM2 ECU: a062 pass AB stg1 sht2 gnd | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a063_passABStg1Sht2Bat` | page 0 | RCM2 ECU: a063 pass AB stg1 sht2 bat | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a064_passABStg1Open` | page 0 | RCM2 ECU: a064 pass AB stg1 open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a065_passABStg1Short` | page 0 | RCM2 ECU: a065 pass AB stg1 short | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a066_passABStg1CrssCoup` | page 0 | RCM2 ECU: a066 pass AB stg1 crss coup | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a067_passABStg1Config` | page 0 | RCM2 ECU: a067 pass AB stg1 config | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a068_passABStg2Sht2Gnd` | page 0 | RCM2 ECU: a068 pass AB stg2 sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a069_passABStg2Sht2Bat` | page 0 | RCM2 ECU: a069 pass AB stg2 sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a070_passABStg2Open` | page 0 | RCM2 ECU: a070 pass AB stg2 open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a071_passABStg2Short` | page 0 | RCM2 ECU: a071 pass AB stg2 short | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a072_passABStg2CrssCoup` | page 0 | RCM2 ECU: a072 pass AB stg2 crss coup | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a073_passABStg2Config` | page 0 | RCM2 ECU: a073 pass AB stg2 config | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a074_passActiveVentSht2Gnd` | page 0 | RCM2 ECU: a074 pass active vent sht2 gnd | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a075_passActiveVentSht2Bat` | page 0 | RCM2 ECU: a075 pass active vent sht2 bat | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a076_passActiveVentOpen` | page 0 | RCM2 ECU: a076 pass active vent open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a077_passActiveVentShort` | page 0 | RCM2 ECU: a077 pass active vent short | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a078_passActiveVentCrssCoup` | page 0 | RCM2 ECU: a078 pass active vent crss coup | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a079_passActiveVentConfig` | page 0 | RCM2 ECU: a079 pass active vent config | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a080_pretenShldLeftSht2Gnd` | page 0 | RCM2 ECU: a080 preten shld left sht2 gnd | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a081_pretenShldLeftSht2Bat` | page 0 | RCM2 ECU: a081 preten shld left sht2 bat | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a082_pretenShldLeftOpen` | page 0 | RCM2 ECU: a082 preten shld left open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a083_pretenShldLeftShort` | page 0 | RCM2 ECU: a083 preten shld left short | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a084_pretenShldLeftCrossC` | page 0 | RCM2 ECU: a084 preten shld left cross c | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a085_pretenShldLeftConfig` | page 0 | RCM2 ECU: a085 preten shld left config | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a086_pretenShldRightSht2Gnd` | page 0 | RCM2 ECU: a086 preten shld right sht2 gnd | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a087_pretenShldRightSht2Bat` | page 0 | RCM2 ECU: a087 preten shld right sht2 bat | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a088_pretenShldRightOpen` | page 0 | RCM2 ECU: a088 preten shld right open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a089_pretenShldRightShort` | page 1 | RCM2 ECU: a089 preten shld right short | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a090_pretenShldRightCrssCou` | page 1 | RCM2 ECU: a090 preten shld right crss cou | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a091_pretenShldRightConfig` | page 1 | RCM2 ECU: a091 preten shld right config | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a092_pretenLapLeftSht2Gnd` | page 1 | RCM2 ECU: a092 preten lap left sht2 gnd | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a093_pretenLapLeftSht2Bat` | page 1 | RCM2 ECU: a093 preten lap left sht2 bat | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a094_pretenLapLeftOpen` | page 1 | RCM2 ECU: a094 preten lap left open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a095_pretenLapLeftShort` | page 1 | RCM2 ECU: a095 preten lap left short | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a096_pretenLapLeftCrssCoup` | page 1 | RCM2 ECU: a096 preten lap left crss coup | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a097_pretenLapLeftConfig` | page 1 | RCM2 ECU: a097 preten lap left config | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a098_pretenLapRightSht2Gnd` | page 1 | RCM2 ECU: a098 preten lap right sht2 gnd | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a099_pretenLapRightSht2Bat` | page 1 | RCM2 ECU: a099 preten lap right sht2 bat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a100_pretenLapRightOpen` | page 1 | RCM2 ECU: a100 preten lap right open | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a101_pretenLapRightShort` | page 1 | RCM2 ECU: a101 preten lap right short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a102_pretenLapRightCrssCoup` | page 1 | RCM2 ECU: a102 preten lap right crss coup | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a103_pretenLapRightConfig` | page 1 | RCM2 ECU: a103 preten lap right config | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a104_loadLimLeftSht2Gnd` | page 1 | RCM2 ECU: a104 load lim left sht2 gnd | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a105_loadLimLeftSht2Bat` | page 1 | RCM2 ECU: a105 load lim left sht2 bat | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a106_loadLimLeftOpen` | page 1 | RCM2 ECU: a106 load lim left open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a107_loadLimLeftShort` | page 1 | RCM2 ECU: a107 load lim left short | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a108_loadLimLeftCrssCoup` | page 1 | RCM2 ECU: a108 load lim left crss coup | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a109_loadLimLeftConfig` | page 1 | RCM2 ECU: a109 load lim left config | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a110_loadLimRightSht2Gnd` | page 1 | RCM2 ECU: a110 load lim right sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a111_loadLimRightSht2Bat` | page 1 | RCM2 ECU: a111 load lim right sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a112_loadLimRightOpen` | page 1 | RCM2 ECU: a112 load lim right open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a113_loadLimRightShort` | page 1 | RCM2 ECU: a113 load lim right short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a114_loadLimRightCrssCoup` | page 1 | RCM2 ECU: a114 load lim right crss coup | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a115_loadLimRightConfig` | page 1 | RCM2 ECU: a115 load lim right config | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a116_kneeABDrvrSht2Gnd` | page 1 | RCM2 ECU: a116 knee AB drvr sht2 gnd | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a117_kneeABDrvrSht2Bat` | page 1 | RCM2 ECU: a117 knee AB drvr sht2 bat | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a118_kneeABDrvrOpen` | page 1 | RCM2 ECU: a118 knee AB drvr open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a119_kneeABDrvrShort` | page 1 | RCM2 ECU: a119 knee AB drvr short | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a120_kneeABDrvrCrssCoup` | page 1 | RCM2 ECU: a120 knee AB drvr crss coup | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a121_kneeABDrvrConfig` | page 1 | RCM2 ECU: a121 knee AB drvr config | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a122_kneeABPassSht2Gnd` | page 1 | RCM2 ECU: a122 knee AB pass sht2 gnd | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a123_kneeABPassSht2Bat` | page 1 | RCM2 ECU: a123 knee AB pass sht2 bat | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a124_kneeABPassOpen` | page 1 | RCM2 ECU: a124 knee AB pass open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a125_kneeABPassShort` | page 1 | RCM2 ECU: a125 knee AB pass short | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a126_kneeABPassCrssCoup` | page 1 | RCM2 ECU: a126 knee AB pass crss coup | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a127_kneeABPassConfig` | page 1 | RCM2 ECU: a127 knee AB pass config | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a128_sideAB1stRowLSht2Gnd` | page 1 | RCM2 ECU: a128 side ab1st row l sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a129_sideAB1stRowLSht2Bat` | page 1 | RCM2 ECU: a129 side ab1st row l sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a130_sideAB1stRowLOpen` | page 1 | RCM2 ECU: a130 side ab1st row l open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a131_sideAB1stRowLShort` | page 1 | RCM2 ECU: a131 side ab1st row l short | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a132_sideAB1stRowLCrssCoup` | page 1 | RCM2 ECU: a132 side ab1st row l crss coup | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a133_sideAB1stRowLConfig` | page 1 | RCM2 ECU: a133 side ab1st row l config | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a134_sideAB1stRowRSht2Gnd` | page 1 | RCM2 ECU: a134 side ab1st row r sht2 gnd | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a135_sideAB1stRowRSht2Bat` | page 1 | RCM2 ECU: a135 side ab1st row r sht2 bat | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a136_sideAB1stRowROpen` | page 1 | RCM2 ECU: a136 side ab1st row r open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a137_sideAB1stRowRShort` | page 1 | RCM2 ECU: a137 side ab1st row r short | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a138_sideAB1stRowRCrssCoup` | page 1 | RCM2 ECU: a138 side ab1st row r crss coup | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a139_sideAB1stRowRConfig` | page 1 | RCM2 ECU: a139 side ab1st row r config | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a140_hvdPyroSht2Gnd` | page 1 | RCM2 ECU: a140 hvd pyro sht2 gnd | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a141_hvdPyroSht2Bat` | page 1 | RCM2 ECU: a141 hvd pyro sht2 bat | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a142_hvdPyroOpen` | page 1 | RCM2 ECU: a142 hvd pyro open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a143_hvdPyroShort` | page 1 | RCM2 ECU: a143 hvd pyro short | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a144_hvdPyroCrssCoup` | page 1 | RCM2 ECU: a144 hvd pyro crss coup | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a145_hvdPyroConfig` | page 1 | RCM2 ECU: a145 hvd pyro config | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a146_curABLeftSht2Gnd` | page 1 | RCM2 ECU: a146 cur AB left sht2 gnd | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a147_curABLeftSht2Bat` | page 1 | RCM2 ECU: a147 cur AB left sht2 bat | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a148_curABLeftOpen` | page 1 | RCM2 ECU: a148 cur AB left open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a149_curABLeftShort` | page 2 | RCM2 ECU: a149 cur AB left short | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a150_curABLeftCrssCoup` | page 2 | RCM2 ECU: a150 cur AB left crss coup | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a151_curABLeftConfig` | page 2 | RCM2 ECU: a151 cur AB left config | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a152_curABRightSht2Gnd` | page 2 | RCM2 ECU: a152 cur AB right sht2 gnd | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a153_curABRightSht2Bat` | page 2 | RCM2 ECU: a153 cur AB right sht2 bat | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a154_curABRightOpen` | page 2 | RCM2 ECU: a154 cur AB right open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a155_curABRightShort` | page 2 | RCM2 ECU: a155 cur AB right short | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a156_curABRightCrssCoup` | page 2 | RCM2 ECU: a156 cur AB right crss coup | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a157_curABRightConfig` | page 2 | RCM2 ECU: a157 cur AB right config | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a158_preten2ndRowLSht2Gnd` | page 2 | RCM2 ECU: a158 preten2nd row l sht2 gnd | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a159_preten2ndRowLSht2Bat` | page 2 | RCM2 ECU: a159 preten2nd row l sht2 bat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a160_preten2ndRowLOpen` | page 2 | RCM2 ECU: a160 preten2nd row l open | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a161_preten2ndRowLShort` | page 2 | RCM2 ECU: a161 preten2nd row l short | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a162_preten2ndRowLCrssCoup` | page 2 | RCM2 ECU: a162 preten2nd row l crss coup | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a163_preten2ndRowLCgf` | page 2 | RCM2 ECU: a163 preten2nd row l cgf | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a164_preten2ndRowRSht2Gnd` | page 2 | RCM2 ECU: a164 preten2nd row r sht2 gnd | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a165_preten2ndRowRSht2Bat` | page 2 | RCM2 ECU: a165 preten2nd row r sht2 bat | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a166_preten2ndRowROpen` | page 2 | RCM2 ECU: a166 preten2nd row r open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a167_preten2ndRowRShort` | page 2 | RCM2 ECU: a167 preten2nd row r short | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a168_preten2ndRowRCrssCoup` | page 2 | RCM2 ECU: a168 preten2nd row r crss coup | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a169_preten2ndRowRCgf` | page 2 | RCM2 ECU: a169 preten2nd row r cgf | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a170_curAB2ndRowLSht2Gnd` | page 2 | RCM2 ECU: a170 cur ab2nd row l sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a171_curAB2ndRowLSht2Bat` | page 2 | RCM2 ECU: a171 cur ab2nd row l sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a172_curAB2ndRowLOpen` | page 2 | RCM2 ECU: a172 cur ab2nd row l open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a173_curAB2ndRowLShort` | page 2 | RCM2 ECU: a173 cur ab2nd row l short | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a174_curAB2ndRowLCrssCoup` | page 2 | RCM2 ECU: a174 cur ab2nd row l crss coup | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a175_curAB2ndRowLConfig` | page 2 | RCM2 ECU: a175 cur ab2nd row l config | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a176_curAB2ndRowRSht2Gnd` | page 2 | RCM2 ECU: a176 cur ab2nd row r sht2 gnd | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a177_curAB2ndRowRSht2Bat` | page 2 | RCM2 ECU: a177 cur ab2nd row r sht2 bat | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a178_curAB2ndRowROpen` | page 2 | RCM2 ECU: a178 cur ab2nd row r open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a179_curAB2ndRowRShort` | page 2 | RCM2 ECU: a179 cur ab2nd row r short | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a180_curAB2ndRowRCrssCoup` | page 2 | RCM2 ECU: a180 cur ab2nd row r crss coup | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a181_curAB2ndRowRConfig` | page 2 | RCM2 ECU: a181 cur ab2nd row r config | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a182_hoodActuatorRSht2Gnd` | page 2 | RCM2 ECU: a182 hood actuator r sht2 gnd | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a183_hoodActuatorRSht2Bat` | page 2 | RCM2 ECU: a183 hood actuator r sht2 bat | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a184_hoodActuatorROpen` | page 2 | RCM2 ECU: a184 hood actuator r open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a185_hoodActuatorRShort` | page 2 | RCM2 ECU: a185 hood actuator r short | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a186_hoodActuatorRCrssCoup` | page 2 | RCM2 ECU: a186 hood actuator r crss coup | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a187_hoodActuatorRConfig` | page 2 | RCM2 ECU: a187 hood actuator r config | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a188_hoodActuatorLSht2Gnd` | page 2 | RCM2 ECU: a188 hood actuator l sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a189_hoodActuatorLSht2Bat` | page 2 | RCM2 ECU: a189 hood actuator l sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a190_hoodActuatorLOpen` | page 2 | RCM2 ECU: a190 hood actuator l open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a191_hoodActuatorLShort` | page 2 | RCM2 ECU: a191 hood actuator l short | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a192_hoodActuatorLCrssCoup` | page 2 | RCM2 ECU: a192 hood actuator l crss coup | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a193_hoodActuatorLConfig` | page 2 | RCM2 ECU: a193 hood actuator l config | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a194_driverABAVSht2Gnd` | page 2 | RCM2 ECU: a194 driver ABAV sht2 gnd | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a195_driverABAVSht2Bat` | page 2 | RCM2 ECU: a195 driver ABAV sht2 bat | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a196_driverABAVOpen` | page 2 | RCM2 ECU: a196 driver ABAV open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a197_driverABAVShort` | page 2 | RCM2 ECU: a197 driver ABAV short | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a198_driverABAVCrossCoup` | page 2 | RCM2 ECU: a198 driver ABAV cross coup | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a199_driverABAVConfig` | page 2 | RCM2 ECU: a199 driver ABAV config | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a200_driverFSABSht2Gnd` | page 2 | RCM2 ECU: a200 driver FSAB sht2 gnd | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a201_driverFSABSht2Bat` | page 2 | RCM2 ECU: a201 driver FSAB sht2 bat | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a202_driverFSABOpen` | page 2 | RCM2 ECU: a202 driver FSAB open | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a203_driverFSABShort` | page 2 | RCM2 ECU: a203 driver FSAB short | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a204_driverFSABCrossCoup` | page 2 | RCM2 ECU: a204 driver FSAB cross coup | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a205_driverFSABConfig` | page 2 | RCM2 ECU: a205 driver FSAB config | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a206_sideAB2ndRowLSht2Gnd` | page 2 | RCM2 ECU: a206 side ab2nd row l sht2 gnd | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a207_sideAB2ndRowLSht2Bat` | page 2 | RCM2 ECU: a207 side ab2nd row l sht2 bat | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a208_sideAB2ndRowLOpen` | page 2 | RCM2 ECU: a208 side ab2nd row l open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a209_sideAB2ndRowLShort` | page 3 | RCM2 ECU: a209 side ab2nd row l short | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a210_sideAB2ndRowLCrssCoup` | page 3 | RCM2 ECU: a210 side ab2nd row l crss coup | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a211_sideAB2ndRowLConfig` | page 3 | RCM2 ECU: a211 side ab2nd row l config | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a212_sideAB2ndRowRSht2Gnd` | page 3 | RCM2 ECU: a212 side ab2nd row r sht2 gnd | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a213_sideAB2ndRowRSht2Bat` | page 3 | RCM2 ECU: a213 side ab2nd row r sht2 bat | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a214_sideAB2ndRowROpen` | page 3 | RCM2 ECU: a214 side ab2nd row r open | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a215_sideAB2ndRowRShort` | page 3 | RCM2 ECU: a215 side ab2nd row r short | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a216_sideAB2ndRowRCrssCoup` | page 3 | RCM2 ECU: a216 side ab2nd row r crss coup | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a217_sideAB2ndRowRConfig` | page 3 | RCM2 ECU: a217 side ab2nd row r config | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a250_ens1Sht2Bat` | page 3 | RCM2 ECU: a250 ens1 sht2 bat | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a251_ens1Sht2Gnd` | page 3 | RCM2 ECU: a251 ens1 sht2 gnd | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a252_ens1Config` | page 3 | RCM2 ECU: a252 ens1 config | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a253_ens2Sht2Bat` | page 3 | RCM2 ECU: a253 ens2 sht2 bat | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a254_ens2Sht2Gnd` | page 3 | RCM2 ECU: a254 ens2 sht2 gnd | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a255_ens2Config` | page 3 | RCM2 ECU: a255 ens2 config | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a256_ens3Sht2Bat` | page 3 | RCM2 ECU: a256 ens3 sht2 bat | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a257_ens3Sht2Gnd` | page 3 | RCM2 ECU: a257 ens3 sht2 gnd | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a258_ens3Config` | page 3 | RCM2 ECU: a258 ens3 config | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a259_ens4Sht2Bat` | page 3 | RCM2 ECU: a259 ens4 sht2 bat | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a260_ens4Sht2Gnd` | page 3 | RCM2 ECU: a260 ens4 sht2 gnd | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a261_ens4Config` | page 3 | RCM2 ECU: a261 ens4 config | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a264_imuYawR8OffCompPosLife` | page 3 | RCM2 ECU: a264 imu yaw R8 off comp pos life | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a265_imuYawR8OffCompNegLife` | page 3 | RCM2 ECU: a265 imu yaw R8 off comp neg life | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a266_imuYawR8OffCompPosFLDC` | page 3 | RCM2 ECU: a266 imu yaw R8 off comp pos FLDC | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a267_imuYawR8OffCompNegFLDC` | page 3 | RCM2 ECU: a267 imu yaw R8 off comp neg FLDC | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a268_imuYawR8OffCompPosSLDC` | page 3 | RCM2 ECU: a268 imu yaw R8 off comp pos SLDC | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a269_imuYawR8OffCompNegSLDC` | page 3 | RCM2 ECU: a269 imu yaw R8 off comp neg SLDC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a270_imuPtchR8OffCompPosLife` | page 3 | RCM2 ECU: a270 imu ptch R8 off comp pos life | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a271_imuPtchR8OffCompNegLife` | page 3 | RCM2 ECU: a271 imu ptch R8 off comp neg life | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a272_imuPtchR8OffCompPosFLDC` | page 3 | RCM2 ECU: a272 imu ptch R8 off comp pos FLDC | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a273_imuPtchR8OffCompNegFLDC` | page 3 | RCM2 ECU: a273 imu ptch R8 off comp neg FLDC | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a274_imuPtchR8OffCompPosSLDC` | page 3 | RCM2 ECU: a274 imu ptch R8 off comp pos SLDC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a275_imuPtchR8OffCompNegSLDC` | page 3 | RCM2 ECU: a275 imu ptch R8 off comp neg SLDC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a276_imuRollR8OffCompPosLife` | page 3 | RCM2 ECU: a276 imu roll R8 off comp pos life | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a277_imuRollR8OffCompNegLife` | page 3 | RCM2 ECU: a277 imu roll R8 off comp neg life | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a278_imuRollR8OffCompPosFLDC` | page 3 | RCM2 ECU: a278 imu roll R8 off comp pos FLDC | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a279_imuRollR8OffCompNegFLDC` | page 3 | RCM2 ECU: a279 imu roll R8 off comp neg FLDC | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a280_imuRollR8OffCompPosSLDC` | page 3 | RCM2 ECU: a280 imu roll R8 off comp pos SLDC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a281_imuRollR8OffCompNegSLDC` | page 3 | RCM2 ECU: a281 imu roll R8 off comp neg SLDC | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a282_imuLongAOffCompPosLife` | page 3 | RCM2 ECU: a282 imu long a off comp pos life | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a283_imuLongAOffCompNegLife` | page 3 | RCM2 ECU: a283 imu long a off comp neg life | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a284_imuLongAOffCompPosFLDC` | page 3 | RCM2 ECU: a284 imu long a off comp pos FLDC | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a285_imuLongAOffCompNegFLDC` | page 3 | RCM2 ECU: a285 imu long a off comp neg FLDC | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a286_imuLongAOffCompPosSLDC` | page 3 | RCM2 ECU: a286 imu long a off comp pos SLDC | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a287_imuLongAOffCompNegSLDC` | page 3 | RCM2 ECU: a287 imu long a off comp neg SLDC | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a288_imuLatAcOffCompPosLife` | page 3 | RCM2 ECU: a288 imu lat ac off comp pos life | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a289_imuLatAcOffCompNegLife` | page 3 | RCM2 ECU: a289 imu lat ac off comp neg life | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a290_imuLatAcOffCompPosFLDC` | page 3 | RCM2 ECU: a290 imu lat ac off comp pos FLDC | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a291_imuLatAcOffCompNegFLDC` | page 3 | RCM2 ECU: a291 imu lat ac off comp neg FLDC | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a292_imuLatAcOffCompPosSLDC` | page 3 | RCM2 ECU: a292 imu lat ac off comp pos SLDC | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a293_imuLatAcOffCompNegSLDC` | page 3 | RCM2 ECU: a293 imu lat ac off comp neg SLDC | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a294_imuVertAOffCompPosLife` | page 3 | RCM2 ECU: a294 imu vert a off comp pos life | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a295_imuVertAOffCompNegLife` | page 3 | RCM2 ECU: a295 imu vert a off comp neg life | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a296_imuVertAOffCompPosFLDC` | page 3 | RCM2 ECU: a296 imu vert a off comp pos FLDC | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a297_imuVertAOffCompNegFLDC` | page 3 | RCM2 ECU: a297 imu vert a off comp neg FLDC | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a298_imuVertAOffCompPosSLDC` | page 3 | RCM2 ECU: a298 imu vert a off comp pos SLDC | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a299_imuVertAOffCompNegSLDC` | page 3 | RCM2 ECU: a299 imu vert a off comp neg SLDC | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a300_imuAccXHgMonChlPerm` | page 3 | RCM2 ECU: a300 imu acc x hg mon chl perm | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a301_imuAccXHgMonChlTemp` | page 3 | RCM2 ECU: a301 imu acc x hg mon chl temp | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a302_imuAccYHgMonChlPerm` | page 3 | RCM2 ECU: a302 imu acc y hg mon chl perm | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a303_imuAccYHgMonChlTemp` | page 4 | RCM2 ECU: a303 imu acc y hg mon chl temp | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a304_imuYawR8SnsrPermBG` | page 4 | RCM2 ECU: a304 imu yaw R8 snsr perm BG | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a305_imuYawR8SnsrPermInit` | page 4 | RCM2 ECU: a305 imu yaw R8 snsr perm init | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a306_imuYawR8SnsrPermLF` | page 4 | RCM2 ECU: a306 imu yaw R8 snsr perm LF | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a307_imuYawR8ChnlMonTmpLF` | page 4 | RCM2 ECU: a307 imu yaw R8 chnl mon tmp LF | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a308_imuPitchR8SnsrPermBG` | page 4 | RCM2 ECU: a308 imu pitch R8 snsr perm BG | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a309_imuPitchR8SnsrPermInit` | page 4 | RCM2 ECU: a309 imu pitch R8 snsr perm init | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a310_imuPitchR8SnsrPermLF` | page 4 | RCM2 ECU: a310 imu pitch R8 snsr perm LF | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a311_imuPitchR8ChnlMonTmpLF` | page 4 | RCM2 ECU: a311 imu pitch R8 chnl mon tmp LF | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a312_imuRollR8SnsrPermBG` | page 4 | RCM2 ECU: a312 imu roll R8 snsr perm BG | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a313_imuRollR8SnsrPermInit` | page 4 | RCM2 ECU: a313 imu roll R8 snsr perm init | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a314_imuRollR8SnsrPermLF` | page 4 | RCM2 ECU: a314 imu roll R8 snsr perm LF | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a315_imuRollR8ChnlMonTmpLF` | page 4 | RCM2 ECU: a315 imu roll R8 chnl mon tmp LF | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a316_imuAccXLgMonChlPerm` | page 4 | RCM2 ECU: a316 imu acc x lg mon chl perm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a317_imuAccXLgMonChlTemp` | page 4 | RCM2 ECU: a317 imu acc x lg mon chl temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a318_imuAccYLgMonChlPerm` | page 4 | RCM2 ECU: a318 imu acc y lg mon chl perm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a319_imuAccYLgMonChlTemp` | page 4 | RCM2 ECU: a319 imu acc y lg mon chl temp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a320_imuAccZLgMonChlPerm` | page 4 | RCM2 ECU: a320 imu acc z lg mon chl perm | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a321_imuAccZLgMonChlTemp` | page 4 | RCM2 ECU: a321 imu acc z lg mon chl temp | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a322_imuCalibrationFailed` | page 4 | RCM2 ECU: a322 imu calibration failed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a323_imuCalibrationNotDone` | page 4 | RCM2 ECU: a323 imu calibration not done | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a350_upFrntSnsrLSht2Gnd` | page 4 | RCM2 ECU: a350 up frnt snsr l sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a351_upFrntSnsrLSht2Bat` | page 4 | RCM2 ECU: a351 up frnt snsr l sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a352_upFrntSnsrLOpen` | page 4 | RCM2 ECU: a352 up frnt snsr l open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a353_upFrntSnsrLCrssCoup` | page 4 | RCM2 ECU: a353 up frnt snsr l crss coup | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a354_upFrntSnsrLCommErr` | page 4 | RCM2 ECU: a354 up frnt snsr l comm err | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a355_upFrntSnsrLInitTyp` | page 4 | RCM2 ECU: a355 up frnt snsr l init typ | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a356_upFrntSnsrLConfig` | page 4 | RCM2 ECU: a356 up frnt snsr l config | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a357_upFrntSnsrLDefect` | page 4 | RCM2 ECU: a357 up frnt snsr l defect | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a358_upFrntSnsrLSigMon` | page 4 | RCM2 ECU: a358 up frnt snsr l sig mon | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a360_upFrntSnsrRSht2Gnd` | page 4 | RCM2 ECU: a360 up frnt snsr r sht2 gnd | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a361_upFrntSnsrRSht2Bat` | page 4 | RCM2 ECU: a361 up frnt snsr r sht2 bat | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a362_upFrntSnsrROpen` | page 4 | RCM2 ECU: a362 up frnt snsr r open | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a363_upFrntSnsrRCrssCoup` | page 4 | RCM2 ECU: a363 up frnt snsr r crss coup | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a364_upFrntSnsrRCommErr` | page 4 | RCM2 ECU: a364 up frnt snsr r comm err | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a365_upFrntSnsrRInitTyp` | page 4 | RCM2 ECU: a365 up frnt snsr r init typ | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a366_upFrntSnsrRConfig` | page 4 | RCM2 ECU: a366 up frnt snsr r config | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a367_upFrntSnsrRDefect` | page 4 | RCM2 ECU: a367 up frnt snsr r defect | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a368_upFrntSnsrRSigMon` | page 4 | RCM2 ECU: a368 up frnt snsr r sig mon | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a370_upFrntSnsrMidLSht2Gnd` | page 4 | RCM2 ECU: a370 up frnt snsr mid l sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a371_upFrntSnsrMidLSht2Bat` | page 4 | RCM2 ECU: a371 up frnt snsr mid l sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a372_upFrntSnsrMidLOpen` | page 4 | RCM2 ECU: a372 up frnt snsr mid l open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a373_upFrntSnsrMidLCrssCoup` | page 4 | RCM2 ECU: a373 up frnt snsr mid l crss coup | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a374_upFrntSnsrMidLCommErr` | page 4 | RCM2 ECU: a374 up frnt snsr mid l comm err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a375_upFrntSnsrMidLInitTyp` | page 4 | RCM2 ECU: a375 up frnt snsr mid l init typ | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a376_upFrntSnsrMidLConfig` | page 4 | RCM2 ECU: a376 up frnt snsr mid l config | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a377_upFrntSnsrMidLDefect` | page 4 | RCM2 ECU: a377 up frnt snsr mid l defect | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a378_upFrntSnsrMidLSigMon` | page 4 | RCM2 ECU: a378 up frnt snsr mid l sig mon | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a380_upFrntSnsrMidRSht2Gnd` | page 4 | RCM2 ECU: a380 up frnt snsr mid r sht2 gnd | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a381_upFrntSnsrMidRSht2Bat` | page 4 | RCM2 ECU: a381 up frnt snsr mid r sht2 bat | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a382_upFrntSnsrMidROpen` | page 4 | RCM2 ECU: a382 up frnt snsr mid r open | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a383_upFrntSnsrMidRCrssCoup` | page 4 | RCM2 ECU: a383 up frnt snsr mid r crss coup | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a384_upFrntSnsrMidRCommErr` | page 4 | RCM2 ECU: a384 up frnt snsr mid r comm err | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a385_upFrntSnsrMidRInitTyp` | page 4 | RCM2 ECU: a385 up frnt snsr mid r init typ | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a386_upFrntSnsrMidRConfig` | page 4 | RCM2 ECU: a386 up frnt snsr mid r config | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a387_upFrntSnsrMidRDefect` | page 4 | RCM2 ECU: a387 up frnt snsr mid r defect | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a388_upFrntSnsrMidRSigMon` | page 4 | RCM2 ECU: a388 up frnt snsr mid r sig mon | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a390_sideAccelBPilLSht2Gnd` | page 4 | RCM2 ECU: a390 side accel b pil l sht2 gnd | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a391_sideAccelBPilLSht2Bat` | page 4 | RCM2 ECU: a391 side accel b pil l sht2 bat | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a392_sideAccelBPilLOpen` | page 4 | RCM2 ECU: a392 side accel b pil l open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a393_sideAccelBPilLCLosCoup` | page 5 | RCM2 ECU: a393 side accel b pil LC los coup | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a394_sideAccelBPilLCommErr` | page 5 | RCM2 ECU: a394 side accel b pil l comm err | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a395_sideAccelBPilLInitTyp` | page 5 | RCM2 ECU: a395 side accel b pil l init typ | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a396_sideAccelBPilLConfig` | page 5 | RCM2 ECU: a396 side accel b pil l config | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a397_sideAccelBPilLDefect` | page 5 | RCM2 ECU: a397 side accel b pil l defect | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a398_sideAccelBPilLSigMon` | page 5 | RCM2 ECU: a398 side accel b pil l sig mon | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a400_sideAccelBPilRSht2Gnd` | page 5 | RCM2 ECU: a400 side accel b pil r sht2 gnd | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a401_sideAccelBPilRSht2Bat` | page 5 | RCM2 ECU: a401 side accel b pil r sht2 bat | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a402_sideAccelBPilROpen` | page 5 | RCM2 ECU: a402 side accel b pil r open | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a403_sideAccelBPilRCrssCoup` | page 5 | RCM2 ECU: a403 side accel b pil r crss coup | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a404_sideAccelBPilRCommErr` | page 5 | RCM2 ECU: a404 side accel b pil r comm err | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a405_sideAccelBPilRInitTyp` | page 5 | RCM2 ECU: a405 side accel b pil r init typ | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a406_sideAccelBPilRConfig` | page 5 | RCM2 ECU: a406 side accel b pil r config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a407_sideAccelBPilRDefect` | page 5 | RCM2 ECU: a407 side accel b pil r defect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a408_sideAccelBPilRSigMon` | page 5 | RCM2 ECU: a408 side accel b pil r sig mon | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a410_sideAccelCPilLSht2Gnd` | page 5 | RCM2 ECU: a410 side accel c pil l sht2 gnd | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a411_sideAccelCPilLSht2Bat` | page 5 | RCM2 ECU: a411 side accel c pil l sht2 bat | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a412_sideAccelCPilLOpen` | page 5 | RCM2 ECU: a412 side accel c pil l open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a413_sideAccelCPilLCrssCoup` | page 5 | RCM2 ECU: a413 side accel c pil l crss coup | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a414_sideAccelCPilLCommErr` | page 5 | RCM2 ECU: a414 side accel c pil l comm err | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a415_sideAccelCPilLInitTyp` | page 5 | RCM2 ECU: a415 side accel c pil l init typ | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a416_sideAccelCPilLConfig` | page 5 | RCM2 ECU: a416 side accel c pil l config | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a417_sideAccelCPilLDefect` | page 5 | RCM2 ECU: a417 side accel c pil l defect | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a418_sideAccelCPilLSigMon` | page 5 | RCM2 ECU: a418 side accel c pil l sig mon | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a420_sideAccelCPilRSht2Gnd` | page 5 | RCM2 ECU: a420 side accel c pil r sht2 gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a421_sideAccelCPilRSht2Bat` | page 5 | RCM2 ECU: a421 side accel c pil r sht2 bat | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a422_sideAccelCPilROpen` | page 5 | RCM2 ECU: a422 side accel c pil r open | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a423_sideAccelCPilRCrssCoup` | page 5 | RCM2 ECU: a423 side accel c pil r crss coup | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a424_sideAccelCPilRCommErr` | page 5 | RCM2 ECU: a424 side accel c pil r comm err | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a425_sideAccelCPilRInitTyp` | page 5 | RCM2 ECU: a425 side accel c pil r init typ | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a426_sideAccelCPilRConfig` | page 5 | RCM2 ECU: a426 side accel c pil r config | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a427_sideAccelCPilRDefect` | page 5 | RCM2 ECU: a427 side accel c pil r defect | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a428_sideAccelCPilRSigMon` | page 5 | RCM2 ECU: a428 side accel c pil r sig mon | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a430_presFrntLDoorSht2Gnd` | page 5 | RCM2 ECU: a430 pres frnt l door sht2 gnd | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a431_presFrntLDoorSht2Bat` | page 5 | RCM2 ECU: a431 pres frnt l door sht2 bat | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a432_presFrntLDoorOpen` | page 5 | RCM2 ECU: a432 pres frnt l door open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a433_presFrntLDoorCrssCoup` | page 5 | RCM2 ECU: a433 pres frnt l door crss coup | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a434_presFrntLDoorCommErr` | page 5 | RCM2 ECU: a434 pres frnt l door comm err | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a435_presFrntLDoorInitTyp` | page 5 | RCM2 ECU: a435 pres frnt l door init typ | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a436_presFrntLDoorConfig` | page 5 | RCM2 ECU: a436 pres frnt l door config | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a437_presFrntLDoorDefect` | page 5 | RCM2 ECU: a437 pres frnt l door defect | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a438_presFrntLDoorSigMon` | page 5 | RCM2 ECU: a438 pres frnt l door sig mon | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a439_presDoorAbsolute1` | page 5 | RCM2 ECU: a439 pres door absolute1 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a440_presFrntRDoorSht2Gnd` | page 5 | RCM2 ECU: a440 pres frnt r door sht2 gnd | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a441_presFrntRDoorSht2Bat` | page 5 | RCM2 ECU: a441 pres frnt r door sht2 bat | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a442_presFrntRDoorOpen` | page 5 | RCM2 ECU: a442 pres frnt r door open | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a443_presFrntRDoorCrssCoup` | page 5 | RCM2 ECU: a443 pres frnt r door crss coup | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a444_presFrntRDoorCommErr` | page 5 | RCM2 ECU: a444 pres frnt r door comm err | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a445_presFrntRDoorInitTyp` | page 5 | RCM2 ECU: a445 pres frnt r door init typ | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a446_presFrntRDoorConfig` | page 5 | RCM2 ECU: a446 pres frnt r door config | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a447_presFrntRDoorDefect` | page 5 | RCM2 ECU: a447 pres frnt r door defect | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a448_presFrntRDoorSigMon` | page 5 | RCM2 ECU: a448 pres frnt r door sig mon | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a449_presDoorAbsolute2` | page 5 | RCM2 ECU: a449 pres door absolute2 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a450_presPedProLSht2Gnd` | page 5 | RCM2 ECU: a450 pres ped pro l sht2 gnd | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a451_presPedProLSht2Bat` | page 5 | RCM2 ECU: a451 pres ped pro l sht2 bat | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a452_presPedProLOpen` | page 5 | RCM2 ECU: a452 pres ped pro l open | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a453_presPedProLCrssCoup` | page 5 | RCM2 ECU: a453 pres ped pro l crss coup | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a454_presPedProLCommErr` | page 5 | RCM2 ECU: a454 pres ped pro l comm err | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a455_presPedProLInitTyp` | page 5 | RCM2 ECU: a455 pres ped pro l init typ | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a456_presPedProLConfig` | page 5 | RCM2 ECU: a456 pres ped pro l config | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a457_presPedProLDefect` | page 6 | RCM2 ECU: a457 pres ped pro l defect | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a458_presPedProLSigMon` | page 6 | RCM2 ECU: a458 pres ped pro l sig mon | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a460_presPedProRSht2Gnd` | page 6 | RCM2 ECU: a460 pres ped pro r sht2 gnd | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a461_presPedProRSht2Bat` | page 6 | RCM2 ECU: a461 pres ped pro r sht2 bat | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a462_presPedProROpen` | page 6 | RCM2 ECU: a462 pres ped pro r open | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a463_presPedProRCrssCoup` | page 6 | RCM2 ECU: a463 pres ped pro r crss coup | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a464_presPedProRCommErr` | page 6 | RCM2 ECU: a464 pres ped pro r comm err | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a465_presPedProRInitTyp` | page 6 | RCM2 ECU: a465 pres ped pro r init typ | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a466_presPedProRConfig` | page 6 | RCM2 ECU: a466 pres ped pro r config | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a467_presPedProRDefect` | page 6 | RCM2 ECU: a467 pres ped pro r defect | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a468_presPedProRSigMon` | page 6 | RCM2 ECU: a468 pres ped pro r sig mon | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a469_presPedProAbsolute` | page 6 | RCM2 ECU: a469 pres ped pro absolute | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a470_upFrntPedProLSht2Gnd` | page 6 | RCM2 ECU: a470 up frnt ped pro l sht2 gnd | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a471_upFrntPedProLSht2Bat` | page 6 | RCM2 ECU: a471 up frnt ped pro l sht2 bat | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a472_upFrntPedProLOpen` | page 6 | RCM2 ECU: a472 up frnt ped pro l open | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a473_upFrntPedProLCrssCoup` | page 6 | RCM2 ECU: a473 up frnt ped pro l crss coup | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a474_upFrntPedProLCommErr` | page 6 | RCM2 ECU: a474 up frnt ped pro l comm err | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a475_upFrntPedProLIntTyp` | page 6 | RCM2 ECU: a475 up frnt ped pro l int typ | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a476_upFrntPedProLConfig` | page 6 | RCM2 ECU: a476 up frnt ped pro l config | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a477_upFrntPedProLDefect` | page 6 | RCM2 ECU: a477 up frnt ped pro l defect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a478_upFrntPedProLSigMon` | page 6 | RCM2 ECU: a478 up frnt ped pro l sig mon | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a480_upFrntPedProRSht2Gnd` | page 6 | RCM2 ECU: a480 up frnt ped pro r sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a481_upFrntPedProRSht2Bat` | page 6 | RCM2 ECU: a481 up frnt ped pro r sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a482_upFrntPedProROpen` | page 6 | RCM2 ECU: a482 up frnt ped pro r open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a483_upFrntPedProRCrssCoup` | page 6 | RCM2 ECU: a483 up frnt ped pro r crss coup | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a484_upFrntPedProRCommErr` | page 6 | RCM2 ECU: a484 up frnt ped pro r comm err | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a485_upFrntPedProRIntTyp` | page 6 | RCM2 ECU: a485 up frnt ped pro r int typ | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a486_upFrntPedProRConfig` | page 6 | RCM2 ECU: a486 up frnt ped pro r config | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a487_upFrntPedProRDefect` | page 6 | RCM2 ECU: a487 up frnt ped pro r defect | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a488_upFrntPedProRSigMon` | page 6 | RCM2 ECU: a488 up frnt ped pro r sig mon | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a490_presRearLDoorSht2Gnd` | page 6 | RCM2 ECU: a490 pres rear l door sht2 gnd | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a491_presRearLDoorSht2Bat` | page 6 | RCM2 ECU: a491 pres rear l door sht2 bat | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a492_presRearLDoorOpen` | page 6 | RCM2 ECU: a492 pres rear l door open | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a493_presRearLDoorCrssCoup` | page 6 | RCM2 ECU: a493 pres rear l door crss coup | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a494_presRearLDoorCommErr` | page 6 | RCM2 ECU: a494 pres rear l door comm err | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a495_presRearLDoorInitTyp` | page 6 | RCM2 ECU: a495 pres rear l door init typ | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a496_presRearLDoorConfig` | page 6 | RCM2 ECU: a496 pres rear l door config | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a497_presRearLDoorDefect` | page 6 | RCM2 ECU: a497 pres rear l door defect | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a498_presRearLDoorSigMon` | page 6 | RCM2 ECU: a498 pres rear l door sig mon | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a500_presRearRDoorSht2Gnd` | page 6 | RCM2 ECU: a500 pres rear r door sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a501_presRearRDoorSht2Bat` | page 6 | RCM2 ECU: a501 pres rear r door sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a502_presRearRDoorOpen` | page 6 | RCM2 ECU: a502 pres rear r door open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a503_presRearRDoorCrssCoup` | page 6 | RCM2 ECU: a503 pres rear r door crss coup | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a504_presRearRDoorCommErr` | page 6 | RCM2 ECU: a504 pres rear r door comm err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a505_presRearRDoorInitTyp` | page 6 | RCM2 ECU: a505 pres rear r door init typ | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a506_presRearRDoorConfig` | page 6 | RCM2 ECU: a506 pres rear r door config | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a507_presRearRDoorDefect` | page 6 | RCM2 ECU: a507 pres rear r door defect | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a508_presRearRDoorSigMon` | page 6 | RCM2 ECU: a508 pres rear r door sig mon | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a509_sideAccelDPilLSht2Gnd` | page 6 | RCM2 ECU: a509 side accel d pil l sht2 gnd | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a510_sideAccelDPilLSht2Bat` | page 6 | RCM2 ECU: a510 side accel d pil l sht2 bat | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a511_sideAccelDPilLOpen` | page 6 | RCM2 ECU: a511 side accel d pil l open | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a512_sideAccelDPilLCrssCoup` | page 6 | RCM2 ECU: a512 side accel d pil l crss coup | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a513_sideAccelDPilLCommErr` | page 6 | RCM2 ECU: a513 side accel d pil l comm err | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a514_sideAccelDPilLInitTyp` | page 6 | RCM2 ECU: a514 side accel d pil l init typ | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a515_sideAccelDPilLConfig` | page 6 | RCM2 ECU: a515 side accel d pil l config | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a516_sideAccelDPilLDefect` | page 6 | RCM2 ECU: a516 side accel d pil l defect | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a517_sideAccelDPilLSigMon` | page 6 | RCM2 ECU: a517 side accel d pil l sig mon | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a518_sideAccelDPilRSht2Gnd` | page 6 | RCM2 ECU: a518 side accel d pil r sht2 gnd | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a519_sideAccelDPilRSht2Bat` | page 6 | RCM2 ECU: a519 side accel d pil r sht2 bat | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a520_sideAccelDPilROpen` | page 6 | RCM2 ECU: a520 side accel d pil r open | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a521_sideAccelDPilRCrssCoup` | page 7 | RCM2 ECU: a521 side accel d pil r crss coup | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a522_sideAccelDPilRCommErr` | page 7 | RCM2 ECU: a522 side accel d pil r comm err | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a523_sideAccelDPilRInitTyp` | page 7 | RCM2 ECU: a523 side accel d pil r init typ | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a524_sideAccelDPilRConfig` | page 7 | RCM2 ECU: a524 side accel d pil r config | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a525_sideAccelDPilRDefect` | page 7 | RCM2 ECU: a525 side accel d pil r defect | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a526_sideAccelDPilRSigMon` | page 7 | RCM2 ECU: a526 side accel d pil r sig mon | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a527_upFrntSnsrCSht2Gnd` | page 7 | RCM2 ECU: a527 up frnt snsr c sht2 gnd | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a528_upFrntSnsrCSht2Bat` | page 7 | RCM2 ECU: a528 up frnt snsr c sht2 bat | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a529_upFrntSnsrCOpen` | page 7 | RCM2 ECU: a529 up frnt snsr c open | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a530_upFrntSnsrCCrssCoup` | page 7 | RCM2 ECU: a530 up frnt snsr c crss coup | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a531_upFrntSnsrCCommErr` | page 7 | RCM2 ECU: a531 up frnt snsr c comm err | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a532_upFrntSnsrCInitTyp` | page 7 | RCM2 ECU: a532 up frnt snsr c init typ | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a533_upFrntSnsrCConfig` | page 7 | RCM2 ECU: a533 up frnt snsr c config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a534_upFrntSnsrCDefect` | page 7 | RCM2 ECU: a534 up frnt snsr c defect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a535_upFrntSnsrCSigMon` | page 7 | RCM2 ECU: a535 up frnt snsr c sig mon | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a550_bucklHallLeftSht2Gnd` | page 7 | RCM2 ECU: a550 buckl hall left sht2 gnd | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a551_bucklHallLeftSht2Bat` | page 7 | RCM2 ECU: a551 buckl hall left sht2 bat | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a552_bucklHallLeftOpen` | page 7 | RCM2 ECU: a552 buckl hall left open | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a553_bucklHallLeftUndef` | page 7 | RCM2 ECU: a553 buckl hall left undef | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a554_bucklHallLeftCrssCoup` | page 7 | RCM2 ECU: a554 buckl hall left crss coup | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a555_bucklHallLeftConfig` | page 7 | RCM2 ECU: a555 buckl hall left config | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a556_bucklHallRightSht2Gnd` | page 7 | RCM2 ECU: a556 buckl hall right sht2 gnd | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a557_bucklHallRightSht2Bat` | page 7 | RCM2 ECU: a557 buckl hall right sht2 bat | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a558_bucklHallRightOpen` | page 7 | RCM2 ECU: a558 buckl hall right open | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a559_bucklHallRightUndef` | page 7 | RCM2 ECU: a559 buckl hall right undef | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a560_bucklHallRightCrssCoup` | page 7 | RCM2 ECU: a560 buckl hall right crss coup | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a561_bucklHallRightConfig` | page 7 | RCM2 ECU: a561 buckl hall right config | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a562_seaTrkPosLeftSht2Gnd` | page 7 | RCM2 ECU: a562 sea trk pos left sht2 gnd | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a563_seaTrkPosLeftShtBat` | page 7 | RCM2 ECU: a563 sea trk pos left sht bat | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a564_seaTrkPosLeftOpen` | page 7 | RCM2 ECU: a564 sea trk pos left open | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a565_seaTrkPosLeftUndefined` | page 7 | RCM2 ECU: a565 sea trk pos left undefined | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a566_seaTrkPosLeftCrssCoup` | page 7 | RCM2 ECU: a566 sea trk pos left crss coup | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a567_seaTrkPosLeftConfig` | page 7 | RCM2 ECU: a567 sea trk pos left config | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a568_occPROSSht2Gnd` | page 7 | RCM2 ECU: a568 occ PROS sht2 gnd | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a569_occPROSSht2Bat` | page 7 | RCM2 ECU: a569 occ PROS sht2 bat | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a570_occPROSOpen` | page 7 | RCM2 ECU: a570 occ PROS open | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a571_occPROSUndef` | page 7 | RCM2 ECU: a571 occ PROS undef | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a572_occPROSCrssCoup` | page 7 | RCM2 ECU: a572 occ PROS crss coup | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a573_occPROSConfig` | page 7 | RCM2 ECU: a573 occ PROS config | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a587_sbrRearNetworkSht2Gnd` | page 7 | RCM2 ECU: a587 sbr rear network sht2 gnd | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a588_sbrRearNetworkSht2Bat` | page 7 | RCM2 ECU: a588 sbr rear network sht2 bat | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a589_sbrRearNetworkOpen` | page 7 | RCM2 ECU: a589 sbr rear network open | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a590_sbrRearNetworkUndefined` | page 7 | RCM2 ECU: a590 sbr rear network undefined | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a591_sbrRearNetworkCrssCoup` | page 7 | RCM2 ECU: a591 sbr rear network crss coup | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a592_sbrRearNetworkConfig` | page 7 | RCM2 ECU: a592 sbr rear network config | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a593_driveOrientationSht2Gnd` | page 7 | RCM2 ECU: a593 drive orientation sht2 gnd | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a594_driveOrientationSht2Bat` | page 7 | RCM2 ECU: a594 drive orientation sht2 bat | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a595_driveOrientationOpen` | page 7 | RCM2 ECU: a595 drive orientation open | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a596_driveOrientationUndefined` | page 7 | RCM2 ECU: a596 drive orientation undefined | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a597_driveOrientationCrssCoup` | page 7 | RCM2 ECU: a597 drive orientation crss coup | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a598_driveOrientationConfig` | page 7 | RCM2 ECU: a598 drive orientation config | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a600_comCANinternalTimeout` | page 7 | RCM2 ECU: a600 com CA ninternal timeout | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a601_comChassisCANSilent` | page 7 | RCM2 ECU: a601 com chassis CAN silent | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a602_comChassisCANBusOff` | page 7 | RCM2 ECU: a602 com chassis CAN bus off | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a603_comPARTYCANSilent` | page 7 | RCM2 ECU: a603 com PARTYCAN silent | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a604_comPARTYCANBusOff` | page 7 | RCM2 ECU: a604 com PARTYCAN bus off | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a605_comStwAngStatMIA` | page 7 | RCM2 ECU: a605 com stw ang stat MIA | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a606_comStwAngStatChkSm` | page 7 | RCM2 ECU: a606 com stw ang stat chk sm | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a607_comStwAngStatCntr` | page 7 | RCM2 ECU: a607 com stw ang stat cntr | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a608_comDItorque1MIA` | page 7 | RCM2 ECU: a608 com d itorque1 MIA | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a609_comDItorque1ChkSm` | page 8 | RCM2 ECU: a609 com d itorque1 chk sm | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a610_comDItorque1Cntr` | page 8 | RCM2 ECU: a610 com d itorque1 cntr | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a611_comDItorque2MIA` | page 8 | RCM2 ECU: a611 com d itorque2 MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a612_comDItorque2ChkSm` | page 8 | RCM2 ECU: a612 com d itorque2 chk sm | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a613_comDItorque2Cntr` | page 8 | RCM2 ECU: a613 com d itorque2 cntr | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a614_comESP135MIA` | page 8 | RCM2 ECU: a614 com ESP135 MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a615_comESP135ChkSm` | page 8 | RCM2 ECU: a615 com ESP135 chk sm | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a616_comESP135Cntr` | page 8 | RCM2 ECU: a616 com ESP135 cntr | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a617_comESP145MIA` | page 8 | RCM2 ECU: a617 com ESP145 MIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a618_comESP145ChkSm` | page 8 | RCM2 ECU: a618 com ESP145 chk sm | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a619_comESP145Cntr` | page 8 | RCM2 ECU: a619 com ESP145 cntr | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a620_comInvalidVehicleSpeed` | page 8 | RCM2 ECU: a620 com invalid vehicle speed | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a621_comESPBMIA` | page 8 | RCM2 ECU: a621 com ESPBMIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a622_comESPBChkSm` | page 8 | RCM2 ECU: a622 com ESPB chk sm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a623_comESPBCntr` | page 8 | RCM2 ECU: a623 com ESPB cntr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a624_comESPCMIA` | page 8 | RCM2 ECU: a624 com ESPCMIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a625_comESPCChkSm` | page 8 | RCM2 ECU: a625 com ESPC chk sm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a626_comESPCCntr` | page 8 | RCM2 ECU: a626 com ESPC cntr | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a627_comEPBStatusMIA` | page 8 | RCM2 ECU: a627 com EPB status MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a628_comEPBStatusChkSm` | page 8 | RCM2 ECU: a628 com EPB status chk sm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a629_comEPBStatusCntr` | page 8 | RCM2 ECU: a629 com EPB status cntr | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a630_comGTWACSMIA` | page 8 | RCM2 ECU: a630 com GTWACSMIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a631_comGTWACSChkSm` | page 8 | RCM2 ECU: a631 com GTWACS chk sm | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a632_comGTWACSCntr` | page 8 | RCM2 ECU: a632 com GTWACS cntr | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a633_comOCS1PMIA` | page 8 | RCM2 ECU: a633 com OCS1 PMIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a634_comOCS1PChkSm` | page 8 | RCM2 ECU: a634 com OCS1 p chk sm | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a635_comOCS1PCntr` | page 8 | RCM2 ECU: a635 com OCS1 p cntr | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a636_ocsFaulted` | page 8 | RCM2 ECU: a636 ocs faulted | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a637_ocsUnknown` | page 8 | RCM2 ECU: a637 ocs unknown | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a638_comGTWodoMIA` | page 8 | RCM2 ECU: a638 com GT wodo MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a639_comGTWCarStateMIA` | page 8 | RCM2 ECU: a639 com GTW car state MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a640_comTPMSStatusCMIA` | page 8 | RCM2 ECU: a640 com TPMS status CMIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a641_comGTWCarConfigMIA` | page 8 | RCM2 ECU: a641 com GTW car config MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a642_comVINmessageMIA` | page 8 | RCM2 ECU: a642 com VI nmessage MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a643_comDASSafetyFrntMIA` | page 8 | RCM2 ECU: a643 com DAS safety frnt MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a644_comDASSafetyFrntChkSm` | page 8 | RCM2 ECU: a644 com DAS safety frnt chk sm | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a645_comDASSafetyFrntCntr` | page 8 | RCM2 ECU: a645 com DAS safety frnt cntr | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a646_comDIstateMIA` | page 8 | RCM2 ECU: a646 com d istate MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a647_comDIstateChkSm` | page 8 | RCM2 ECU: a647 com d istate chk sm | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a648_comDIstateCntr` | page 8 | RCM2 ECU: a648 com d istate cntr | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a649_comDIstate2MIA` | page 8 | RCM2 ECU: a649 com d istate2 MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a650_comDIstate2ChkSm` | page 8 | RCM2 ECU: a650 com d istate2 chk sm | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a651_comDIstate2Cntr` | page 8 | RCM2 ECU: a651 com d istate2 cntr | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a652_ambientTempFaulted` | page 8 | RCM2 ECU: a652 ambient temp faulted | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a653_comGTWESP1MIA` | page 8 | RCM2 ECU: a653 com GTWESP1 MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a654_comGTWESP1ChkSm` | page 8 | RCM2 ECU: a654 com GTWESP1 chk sm | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a655_comGTWESP1Cntr` | page 8 | RCM2 ECU: a655 com GTWESP1 cntr | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a656_comVCSEATPrestMIA` | page 8 | RCM2 ECU: a656 com VCSEAT prest MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a657_comVCSEATPrestChkSm` | page 8 | RCM2 ECU: a657 com VCSEAT prest chk sm | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a658_comVCSEATPrestCntr` | page 8 | RCM2 ECU: a658 com VCSEAT prest cntr | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a659_comVCSEATPbuckle` | page 8 | RCM2 ECU: a659 com VCSEAT pbuckle | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a660_comVCSEATPOccpy` | page 8 | RCM2 ECU: a660 com VCSEATP occpy | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a661_comVCSEATPocs` | page 8 | RCM2 ECU: a661 com VCSEAT pocs | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a662_comVCSEATPstps` | page 8 | RCM2 ECU: a662 com VCSEAT pstps | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a663_comVCSEATDrestMIA` | page 8 | RCM2 ECU: a663 com VCSEAT drest MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a664_comVCSEATDrestChkSm` | page 8 | RCM2 ECU: a664 com VCSEAT drest chk sm | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a665_comVCSEATDrestCntr` | page 8 | RCM2 ECU: a665 com VCSEAT drest cntr | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a666_comVCSEATDbuckle` | page 8 | RCM2 ECU: a666 com VCSEAT dbuckle | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a667_comVCSEATDOccpy` | page 8 | RCM2 ECU: a667 com VCSEATD occpy | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a668_comVCSEATDstps` | page 8 | RCM2 ECU: a668 com VCSEAT dstps | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a669_comEPBLstatusMIA` | page 9 | RCM2 ECU: a669 com EPB lstatus MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a670_comEPBLstatusChkSm` | page 9 | RCM2 ECU: a670 com EPB lstatus chk sm | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a671_comEPBLstatusCntr` | page 9 | RCM2 ECU: a671 com EPB lstatus cntr | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a672_comEPBRstatusMIA` | page 9 | RCM2 ECU: a672 com EPB rstatus MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a673_comEPBRstatusChkSm` | page 9 | RCM2 ECU: a673 com EPB rstatus chk sm | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a674_comEPBRstatusCntr` | page 9 | RCM2 ECU: a674 com EPB rstatus cntr | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a675_comUIodoMIA` | page 9 | RCM2 ECU: a675 com u iodo MIA | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a676_comEPAS3PsysMIA` | page 9 | RCM2 ECU: a676 com EPAS3 psys MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a677_comEPAS3PsysChkSm` | page 9 | RCM2 ECU: a677 com EPAS3 psys chk sm | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a678_comEPAS3PsysCntr` | page 9 | RCM2 ECU: a678 com EPAS3 psys cntr | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a679_comESPwheelSpeedsMIA` | page 9 | RCM2 ECU: a679 com ES pwheel speeds MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a680_comESPwheelSpeedsChkSm` | page 9 | RCM2 ECU: a680 com ES pwheel speeds chk sm | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a681_comESPwheelSpeedsCntr` | page 9 | RCM2 ECU: a681 com ES pwheel speeds cntr | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a682_comDIspeedMIA` | page 9 | RCM2 ECU: a682 com d ispeed MIA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a683_comDIspeedChkSm` | page 9 | RCM2 ECU: a683 com d ispeed chk sm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a684_comDIspeedCntr` | page 9 | RCM2 ECU: a684 com d ispeed cntr | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a685_comDIchassControlMIA` | page 9 | RCM2 ECU: a685 com d ichass control MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a686_comDIchassControlChkSm` | page 9 | RCM2 ECU: a686 com d ichass control chk sm | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a687_comDIchassControlCntr` | page 9 | RCM2 ECU: a687 com d ichass control cntr | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a688_comVCLEFTrestMIA` | page 9 | RCM2 ECU: a688 com VCLEF trest MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a689_comVCLEFTrestChkSm` | page 9 | RCM2 ECU: a689 com VCLEF trest chk sm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a690_comVCLEFTrestCntr` | page 9 | RCM2 ECU: a690 com VCLEF trest cntr | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a691_comVCLEFT1rLBuckle` | page 9 | RCM2 ECU: a691 com vcleft1r l buckle | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a692_comVCLEFT2rLBuckle` | page 9 | RCM2 ECU: a692 com vcleft2r l buckle | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a693_comVCLEFT1rLSTPS` | page 9 | RCM2 ECU: a693 com vcleft1r LSTPS | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a694_comVCRIGHTrestMIA` | page 9 | RCM2 ECU: a694 com VCRIGH trest MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a695_comVCRIGHTrestChkSm` | page 9 | RCM2 ECU: a695 com VCRIGH trest chk sm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a696_comVCRIGHTrestCntr` | page 9 | RCM2 ECU: a696 com VCRIGH trest cntr | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a697_comVCRIGHT1rRBuckle` | page 9 | RCM2 ECU: a697 com vcright1r r buckle | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a698_comVCRIGHT2rRBuckle` | page 9 | RCM2 ECU: a698 com vcright2r r buckle | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a699_comVCRIGHTocs` | page 9 | RCM2 ECU: a699 com VCRIGH tocs | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a700_comVCRIGHT1rRSTPS` | page 9 | RCM2 ECU: a700 com vcright1r RSTPS | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a701_comVCSECtpmsStatusMIA` | page 9 | RCM2 ECU: a701 com VCSE ctpms status MIA | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a750_linInternalTimeout` | page 9 | RCM2 ECU: a750 lin internal timeout | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a799_internalFault` | page 9 | RCM2 ECU: a799 internal fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a800_crcFault` | page 9 | RCM2 ECU: a800 crc fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a801_parameterLayoutID` | page 9 | RCM2 ECU: a801 parameter layout ID | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a802_parameterTransferID` | page 9 | RCM2 ECU: a802 parameter transfer ID | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a803_algoVerifySensorID` | page 9 | RCM2 ECU: a803 algo verify sensor ID | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a804_configDataInconsistent` | page 9 | RCM2 ECU: a804 config data inconsistent | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a805_swVersionWrong` | page 9 | RCM2 ECU: a805 sw version wrong | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a806_configVINnotLearned` | page 9 | RCM2 ECU: a806 config VI nnot learned | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a807_configVINmismatch` | page 9 | RCM2 ECU: a807 config VI nmismatch | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a808_configDriveNotLearned` | page 9 | RCM2 ECU: a808 config drive not learned | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a809_configDriveMismatch` | page 9 | RCM2 ECU: a809 config drive mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a810_bootUpActionFailure` | page 9 | RCM2 ECU: a810 boot up action failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a811_comAxleSpeed` | page 9 | RCM2 ECU: a811 com axle speed | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a812_idfMisuseMonitoringErr` | page 9 | RCM2 ECU: a812 idf misuse monitoring err | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a813_idfEnviMonitoringError` | page 9 | RCM2 ECU: a813 idf envi monitoring error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a814_idfEnviMonitoringEvent` | page 9 | RCM2 ECU: a814 idf envi monitoring event | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a815_upFrntPedProMLSht2Gnd` | page 9 | RCM2 ECU: a815 up frnt ped pro ML sht2 gnd | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a816_upFrntPedProMLSht2Bat` | page 9 | RCM2 ECU: a816 up frnt ped pro ML sht2 bat | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a817_upFrntPedProMLOpen` | page 9 | RCM2 ECU: a817 up frnt ped pro ML open | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a818_upFrntPedProMLCrssCoup` | page 9 | RCM2 ECU: a818 up frnt ped pro ML crss coup | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a819_upFrntPedProMLCommErr` | page 9 | RCM2 ECU: a819 up frnt ped pro ML comm err | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a820_upFrntPedProMLIntTyp` | page 9 | RCM2 ECU: a820 up frnt ped pro ML int typ | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a821_upFrntPedProMLConfig` | page 9 | RCM2 ECU: a821 up frnt ped pro ML config | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a822_upFrntPedProMLDefect` | page 9 | RCM2 ECU: a822 up frnt ped pro ML defect | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a823_upFrntPedProMLSigMon` | page 9 | RCM2 ECU: a823 up frnt ped pro ML sig mon | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a824_upFrntPedProMRSht2Gnd` | page 9 | RCM2 ECU: a824 up frnt ped pro MR sht2 gnd | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a825_upFrntPedProMRSht2Bat` | page 10 | RCM2 ECU: a825 up frnt ped pro MR sht2 bat | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a826_upFrntPedProMROpen` | page 10 | RCM2 ECU: a826 up frnt ped pro MR open | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a827_upFrntPedProMRCrssCoup` | page 10 | RCM2 ECU: a827 up frnt ped pro MR crss coup | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a828_upFrntPedProMRCommErr` | page 10 | RCM2 ECU: a828 up frnt ped pro MR comm err | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a829_upFrntPedProMRIntTyp` | page 10 | RCM2 ECU: a829 up frnt ped pro MR int typ | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a830_upFrntPedProMRConfig` | page 10 | RCM2 ECU: a830 up frnt ped pro MR config | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a831_upFrntPedProMRDefect` | page 10 | RCM2 ECU: a831 up frnt ped pro MR defect | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a832_upFrntPedProMRSigMon` | page 10 | RCM2 ECU: a832 up frnt ped pro MR sig mon | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a833_pretenShldCSht2Gnd` | page 10 | RCM2 ECU: a833 preten shld c sht2 gnd | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a834_pretenShldCSht2Bat` | page 10 | RCM2 ECU: a834 preten shld c sht2 bat | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a835_pretenShldCOpen` | page 10 | RCM2 ECU: a835 preten shld c open | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a836_pretenShldCShort` | page 10 | RCM2 ECU: a836 preten shld c short | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a837_pretenShldCCrossC` | page 10 | RCM2 ECU: a837 preten shld c cross c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a838_pretenShldCConfig` | page 10 | RCM2 ECU: a838 preten shld c config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a839_preten2ndRowCSht2Gnd` | page 10 | RCM2 ECU: a839 preten2nd row c sht2 gnd | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a840_preten2ndRowCSht2Bat` | page 10 | RCM2 ECU: a840 preten2nd row c sht2 bat | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a841_preten2ndRowCOpen` | page 10 | RCM2 ECU: a841 preten2nd row c open | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a842_preten2ndRowCShort` | page 10 | RCM2 ECU: a842 preten2nd row c short | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a843_preten2ndRowCCrssCoup` | page 10 | RCM2 ECU: a843 preten2nd row c crss coup | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a844_preten2ndRowCConfig` | page 10 | RCM2 ECU: a844 preten2nd row c config | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a845_comUIchassisControlMIA` | page 10 | RCM2 ECU: a845 com u ichassis control MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a846_comSCCMstrAnglSnsMIA` | page 10 | RCM2 ECU: a846 com SCC mstr angl sns MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a847_comDASctrlMIA` | page 10 | RCM2 ECU: a847 com DA sctrl MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a848_comDIlocStatMIA` | page 10 | RCM2 ECU: a848 com d iloc stat MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a849_comIBSTparty1MIA` | page 10 | RCM2 ECU: a849 com IBS tparty1 MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a850_comVCFRONTlightingMIA` | page 10 | RCM2 ECU: a850 com VCFRON tlighting MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a851_internalFaultTemp` | page 10 | RCM2 ECU: a851 internal fault temp | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a852_autarkyEvent` | page 10 | RCM2 ECU: a852 autarky event | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a853_ConfigParametersInconsistent` | page 10 | RCM2 ECU: a853 config parameters inconsistent | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a854_ConfigParametersNotLearned` | page 10 | RCM2 ECU: a854 config parameters not learned | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a857_comVCLEFT2rCBuckle` | page 10 | RCM2 ECU: a857 com vcleft2r c buckle | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a858_comVCxLVPowerStateMIA` | page 10 | RCM2 ECU: a858 com v cx LV power state MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a859_comVCxLVPowerStateChkSm` | page 10 | RCM2 ECU: a859 com v cx LV power state chk sm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a860_comVCxLVPowerStateCntr` | page 10 | RCM2 ECU: a860 com v cx LV power state cntr | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a861_typeApprovalStringNotLearned` | page 10 | RCM2 ECU: a861 type approval string not learned | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a862_comPCSalertMatrixMIA` | page 10 | RCM2 ECU: a862 com PC salert matrix MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a863_comVCFRONTalertMatrixMIA` | page 10 | RCM2 ECU: a863 com VCFRON talert matrix MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a864_comGTWepochTimeMIA` | page 10 | RCM2 ECU: a864 com GT wepoch time MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a865_comVCLVBMSstatusHighMIA` | page 10 | RCM2 ECU: a865 com VCLVBM sstatus high MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a866_comDASstatusMIA` | page 10 | RCM2 ECU: a866 com DA sstatus MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a868_headAB3rdRowRSht2Gnd` | page 10 | RCM2 ECU: a868 head ab3rd row r sht2 gnd | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a869_headAB3rdRowRSht2Bat` | page 10 | RCM2 ECU: a869 head ab3rd row r sht2 bat | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a870_headAB3rdRowROpen` | page 10 | RCM2 ECU: a870 head ab3rd row r open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a871_headAB3rdRowRShort` | page 10 | RCM2 ECU: a871 head ab3rd row r short | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a872_headAB3rdRowRCrossC` | page 10 | RCM2 ECU: a872 head ab3rd row r cross c | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a873_headAB3rdRowRConfig` | page 10 | RCM2 ECU: a873 head ab3rd row r config | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a874_headAB3rdRowLSht2Gnd` | page 10 | RCM2 ECU: a874 head ab3rd row l sht2 gnd | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a875_headAB3rdRowLSht2Bat` | page 10 | RCM2 ECU: a875 head ab3rd row l sht2 bat | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a876_headAB3rdRowLOpen` | page 10 | RCM2 ECU: a876 head ab3rd row l open | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a877_headAB3rdRowLShort` | page 10 | RCM2 ECU: a877 head ab3rd row l short | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a878_headAB3rdRowLCrossC` | page 10 | RCM2 ECU: a878 head ab3rd row l cross c | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `RCM2_a879_headAB3rdRowLConfig` | page 10 | RCM2 ECU: a879 head ab3rd row l config | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`RCM2_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (60 signals), page 4 (60 signals), page 5 (60 signals), page 6 (60 signals), page 7 (60 signals), page 8 (60 signals), page 9 (60 signals), page 10 (52 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All RCM2 ECU messages (RCM2)](../../rcm2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
