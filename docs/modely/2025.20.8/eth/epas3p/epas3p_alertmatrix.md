---
layout: default
title: "EPAS3P_alertMatrix (0x7F4) — Electric power steering (primary), Tesla Model Y 2025.20.8 ETH"
description: "Electric power steering (primary) message: alert matrix. Ethernet-side message EPAS3P_alertMatrix of Electric power steering (primary) for Tesla Model Y firmware 2025.20.8, 151 signals (EPAS3P_matrixIndex, EPAS3P_a001_sent1Mia, EPAS3P_a002_sent1Error, EPAS3P_a003_trqSens1Supply and 147 more). Bit layout, scaling, units and value tables."
---

# EPAS3P_alertMatrix (0x7F4) — Electric power steering (primary), Tesla Model Y 2025.20.8 ETH

Electric power steering (primary) message: alert matrix. This page documents the 151 signals of EPAS3P_alertMatrix as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3P_alertMatrix` |
| Ethernet-side id | 0x7F4 (2036) |
| ECU | [Electric power steering (primary)](../../epas3p.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPAS3P |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 151 |

## Signals of EPAS3P_alertMatrix

Tesla Model Y CAN bus signals in `EPAS3P_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3P_matrixIndex` | selector | Electric power steering (primary): matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `EPAS3P_a001_sent1Mia` | page 0 | Electric power steering (primary): a001 sent1 mia | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a002_sent1Error` | page 0 | Electric power steering (primary): a002 sent1 error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a003_trqSens1Supply` | page 0 | Electric power steering (primary): a003 trq sens1 supply | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a004_trqSens1Eeprom` | page 0 | Electric power steering (primary): a004 trq sens1 eeprom | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a005_sent2Mia` | page 0 | Electric power steering (primary): a005 sent2 mia | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a006_sent2Error` | page 0 | Electric power steering (primary): a006 sent2 error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a007_trqSens2Supply` | page 0 | Electric power steering (primary): a007 trq sens2 supply | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a008_trqSens2Eeprom` | page 0 | Electric power steering (primary): a008 trq sens2 eeprom | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a009_sentDiff` | page 0 | Electric power steering (primary): a009 sent diff | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a010_trqSensCalError` | page 0 | Electric power steering (primary): a010 trq sens cal error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a011_currentSensError` | page 0 | Electric power steering (primary): a011 current sens error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a012_currentSensCalError` | page 0 | Electric power steering (primary): a012 current sens cal error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a013_gateDriveError` | page 0 | Electric power steering (primary): a013 gate drive error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a014_gateDriveTxError` | page 0 | Electric power steering (primary): a014 gate drive tx error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a015_gateDriveEeprom` | page 0 | Electric power steering (primary): a015 gate drive eeprom | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a016_phaseUhighUv` | page 0 | Electric power steering (primary): a016 phase uhigh uv | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a017_phaseUlowUv` | page 0 | Electric power steering (primary): a017 phase ulow uv | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a018_phaseVhighUv` | page 0 | Electric power steering (primary): a018 phase vhigh uv | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a019_phaseVlowUv` | page 0 | Electric power steering (primary): a019 phase vlow uv | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a020_phaseWhighUv` | page 0 | Electric power steering (primary): a020 phase whigh uv | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a021_phaseWlowUv` | page 0 | Electric power steering (primary): a021 phase wlow uv | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a022_phaseUhighOv` | page 0 | Electric power steering (primary): a022 phase uhigh ov | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a023_phaseUlowOv` | page 0 | Electric power steering (primary): a023 phase ulow ov | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a024_phaseVhighOv` | page 0 | Electric power steering (primary): a024 phase vhigh ov | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a025_phaseVlowOv` | page 0 | Electric power steering (primary): a025 phase vlow ov | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a026_phaseWhighOv` | page 0 | Electric power steering (primary): a026 phase whigh ov | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a027_phaseWlowOv` | page 0 | Electric power steering (primary): a027 phase wlow ov | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a028_phaseUbootUv` | page 0 | Electric power steering (primary): a028 phase uboot uv | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a029_phaseVbootUv` | page 0 | Electric power steering (primary): a029 phase vboot uv | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a030_phaseWbootUv` | page 0 | Electric power steering (primary): a030 phase wboot uv | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a031_abnormalShutdown` | page 0 | Electric power steering (primary): a031 abnormal shutdown | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a032_vRegOutputUv` | page 0 | Electric power steering (primary): a032 v reg output uv | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a033_vRegOutputOv` | page 0 | Electric power steering (primary): a033 v reg output ov | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a034_vRegError` | page 0 | Electric power steering (primary): a034 v reg error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a035_vbbSupplyUv` | page 0 | Electric power steering (primary): a035 vbb supply uv | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a036_vbbSupplyOv` | page 0 | Electric power steering (primary): a036 vbb supply ov | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a037_motPos1ParityError` | page 0 | Electric power steering (primary): a037 mot pos1 parity error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a038_motPos1Uv` | page 0 | Electric power steering (primary): a038 mot pos1 uv | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a039_motPos1MagnetMia` | page 0 | Electric power steering (primary): a039 mot pos1 magnet mia | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a040_motPos1LogicError` | page 0 | Electric power steering (primary): a040 mot pos1 logic error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a041_motPos1tempError` | page 0 | Electric power steering (primary): a041 mot pos1temp error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a042_motPos2ParityError` | page 0 | Electric power steering (primary): a042 mot pos2 parity error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a043_motPos2Uv` | page 0 | Electric power steering (primary): a043 mot pos2 uv | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a044_motPos2MagnetMia` | page 0 | Electric power steering (primary): a044 mot pos2 magnet mia | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a045_motPos2LogicError` | page 0 | Electric power steering (primary): a045 mot pos2 logic error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a046_motPos2tempError` | page 0 | Electric power steering (primary): a046 mot pos2temp error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a047_motPosCorrError` | page 0 | Electric power steering (primary): a047 mot pos corr error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a048_motPosCalError` | page 0 | Electric power steering (primary): a048 mot pos cal error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a049_piCtrlError` | page 0 | Electric power steering (primary): a049 pi ctrl error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a050_mcuSmuError` | page 0 | Electric power steering (primary): a050 mcu smu error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a051_mcuSupError` | page 0 | Electric power steering (primary): a051 mcu sup error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a052_intWatchdogError` | page 0 | Electric power steering (primary): a052 int watchdog error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a053_extWatchdogError` | page 0 | Electric power steering (primary): a053 ext watchdog error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a054_memoryProtectError` | page 0 | Electric power steering (primary): a054 memory protect error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a055_floatPointError` | page 0 | Electric power steering (primary): a055 float point error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a056_battUv` | page 0 | Electric power steering (primary): a056 batt uv | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a057_battUvReduced` | page 0 | Electric power steering (primary): a057 batt uv reduced | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a058_battOv` | page 0 | Electric power steering (primary): a058 batt ov | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a059_battOvReduced` | page 0 | Electric power steering (primary): a059 batt ov reduced | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a060_battBridgeDiff` | page 0 | Electric power steering (primary): a060 batt bridge diff | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a061_bridgeUv` | page 1 | Electric power steering (primary): a061 bridge uv | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a062_assistCorrError` | page 1 | Electric power steering (primary): a062 assist corr error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a063_dampCorrError` | page 1 | Electric power steering (primary): a063 damp corr error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a064_phaseCompCorrError` | page 1 | Electric power steering (primary): a064 phase comp corr error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a065_trqTarCorrError` | page 1 | Electric power steering (primary): a065 trq tar corr error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a066_returnCorrError` | page 1 | Electric power steering (primary): a066 return corr error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a067_yawDampCorrError` | page 1 | Electric power steering (primary): a067 yaw damp corr error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a068_hystCorrError` | page 1 | Electric power steering (primary): a068 hyst corr error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a069_eacCorrError` | page 1 | Electric power steering (primary): a069 eac corr error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a070_hodCorrError` | page 1 | Electric power steering (primary): a070 hod corr error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a071_vehSpdCorrError` | page 1 | Electric power steering (primary): a071 veh spd corr error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a072_motFeedFwdError` | page 1 | Electric power steering (primary): a072 mot feed fwd error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a073_motParEstError` | page 1 | Electric power steering (primary): a073 mot par est error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a074_overHeatProtect` | page 1 | Electric power steering (primary): a074 over heat protect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a075_fspPwrCut` | page 1 | Electric power steering (primary): a075 fsp pwr cut | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a076_tempSensOutofRange` | page 1 | Electric power steering (primary): a076 temp sens outof range | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a077_highSideFetError` | page 1 | Electric power steering (primary): a077 high side fet error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a078_phaseDisconnectError` | page 1 | Electric power steering (primary): a078 phase disconnect error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a079_backupCurrentPlaus` | page 1 | Electric power steering (primary): a079 backup current plaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a080_ecuInitArbError` | page 1 | Electric power steering (primary): a080 ecu init arb error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a081_coggCompError` | page 1 | Electric power steering (primary): a081 cogg comp error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a082_polarityCalError` | page 1 | Electric power steering (primary): a082 polarity cal error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a083_crcMismatch` | page 1 | Electric power steering (primary): a083 crc mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a084_eacCancelled` | page 1 | Electric power steering (primary): a084 eac cancelled | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a085_canBusOff` | page 1 | Electric power steering (primary): a085 can bus off | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a086_dasMia` | page 1 | Electric power steering (primary): a086 das mia | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a087_dasCntError` | page 1 | Electric power steering (primary): a087 das cnt error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a088_dasCsError` | page 1 | Electric power steering (primary): a088 das cs error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a089_espWsMia` | page 1 | Electric power steering (primary): a089 esp ws mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a090_espWsCntError` | page 1 | Electric power steering (primary): a090 esp ws cnt error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a091_espWsCsError` | page 1 | Electric power steering (primary): a091 esp ws cs error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a092_espWrMia` | page 1 | Electric power steering (primary): a092 esp wr mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a093_espWrCntError` | page 1 | Electric power steering (primary): a093 esp wr cnt error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a094_espWrCsError` | page 1 | Electric power steering (primary): a094 esp wr cs error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a095_espWsStatus` | page 1 | Electric power steering (primary): a095 esp ws status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a096_rcmMia` | page 1 | Electric power steering (primary): a096 rcm mia | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a097_rcmCntError` | page 1 | Electric power steering (primary): a097 rcm cnt error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a098_rcmCsError` | page 1 | Electric power steering (primary): a098 rcm cs error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a099_yawRateStatus` | page 1 | Electric power steering (primary): a099 yaw rate status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a100_diMia` | page 1 | Electric power steering (primary): a100 di mia | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a101_diCntError` | page 1 | Electric power steering (primary): a101 di cnt error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a102_diCsError` | page 1 | Electric power steering (primary): a102 di cs error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a103_vcFrontMia` | page 1 | Electric power steering (primary): a103 vc front mia | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a104_vcFrontCntError` | page 1 | Electric power steering (primary): a104 vc front cnt error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a105_vcFrontCsError` | page 1 | Electric power steering (primary): a105 vc front cs error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a106_vcFrontTempMia` | page 1 | Electric power steering (primary): a106 vc front temp mia | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a107_uiTuneReqMia` | page 1 | Electric power steering (primary): a107 ui tune req mia | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a108_uiTuneReqCntError` | page 1 | Electric power steering (primary): a108 ui tune req cnt error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a109_uiTuneReqCsError` | page 1 | Electric power steering (primary): a109 ui tune req cs error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a110_sasMia` | page 1 | Electric power steering (primary): a110 sas mia | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a111_sasCntError` | page 1 | Electric power steering (primary): a111 sas cnt error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a112_sasCsError` | page 1 | Electric power steering (primary): a112 sas cs error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a113_sasStatusError` | page 1 | Electric power steering (primary): a113 sas status error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a114_gtwConfigMia` | page 1 | Electric power steering (primary): a114 gtw config mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a115_ecuStatMia` | page 1 | Electric power steering (primary): a115 ecu stat mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a116_ecuStatCntError` | page 1 | Electric power steering (primary): a116 ecu stat cnt error | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a117_ecuStatCrcError` | page 1 | Electric power steering (primary): a117 ecu stat crc error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a118_privateBusOff` | page 1 | Electric power steering (primary): a118 private bus off | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a119_pvtEcuStatMia` | page 1 | Electric power steering (primary): a119 pvt ecu stat mia | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a120_pvtEcuStatCntError` | page 1 | Electric power steering (primary): a120 pvt ecu stat cnt error | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a121_pvtEcuStatCrcError` | page 2 | Electric power steering (primary): a121 pvt ecu stat crc error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a122_olpActive` | page 2 | Electric power steering (primary): a122 olp active | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a123_combEcu2StatFail` | page 2 | Electric power steering (primary): a123 comb ecu2 stat fail | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a124_tempSensStuckInRange` | page 2 | Electric power steering (primary): a124 temp sens stuck in range | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a125_trqSensTrimOutRange` | page 2 | Electric power steering (primary): a125 trq sens trim out range | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a126_apsMia` | page 2 | Electric power steering (primary): a126 aps mia | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a127_apsCntError` | page 2 | Electric power steering (primary): a127 aps cnt error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a128_apsCsError` | page 2 | Electric power steering (primary): a128 aps cs error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a129_combEcu1StatFail` | page 2 | Electric power steering (primary): a129 comb ecu1 stat fail | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a130_sasOffsetNotCal` | page 2 | Electric power steering (primary): a130 sas offset not cal | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a131_phaseFeedbackError` | page 2 | Electric power steering (primary): a131 phase feedback error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a132_motFeedFwdCounter25` | page 2 | Electric power steering (primary): a132 mot feed fwd counter25 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a133_motFeedFwdCounter50` | page 2 | Electric power steering (primary): a133 mot feed fwd counter50 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a134_motFeedFwdCounter85` | page 2 | Electric power steering (primary): a134 mot feed fwd counter85 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a135_piCtrlCounter25` | page 2 | Electric power steering (primary): a135 pi ctrl counter25 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a136_piCtrlCounter50` | page 2 | Electric power steering (primary): a136 pi ctrl counter50 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a137_piCtrlCounter85` | page 2 | Electric power steering (primary): a137 pi ctrl counter85 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a144_diSpdMia` | page 2 | Electric power steering (primary): a144 di spd mia | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a145_diSpdCntError` | page 2 | Electric power steering (primary): a145 di spd cnt error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a146_diSpdCsError` | page 2 | Electric power steering (primary): a146 di spd cs error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a147_backupVehSpeed` | page 2 | Electric power steering (primary): a147 backup veh speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a148_vMaxAssist` | page 2 | Electric power steering (primary): a148 v max assist | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a149_currentSensPathSwitch` | page 2 | Electric power steering (primary): a149 current sens path switch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a150_currentSensOffsetDetect` | page 2 | Electric power steering (primary): a150 current sens offset detect | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a151_dcsCboot` | page 2 | Electric power steering (primary): a151 dcs cboot | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a152_dcsDiagReg` | page 2 | Electric power steering (primary): a152 dcs diag reg | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a153_dcsInitOffset` | page 2 | Electric power steering (primary): a153 dcs init offset | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a154_assistTorqueDisabled` | page 2 | Electric power steering (primary): a154 assist torque disabled | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a155_backupEacActive` | page 2 | Electric power steering (primary): a155 backup eac active | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3P_a156_angleSensorDivergence` | page 2 | Electric power steering (primary): a156 angle sensor divergence | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`EPAS3P_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (30 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric power steering (primary) messages (EPAS3P)](../../epas3p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
