---
layout: default
title: "EPAS3S_alertMatrix (0x391) — Electric power steering (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Electric power steering (secondary) message: alert matrix. Ethernet-side message EPAS3S_alertMatrix of Electric power steering (secondary) for Tesla Model 3 / Model Y firmware 2025.20.8, 151 signals (EPAS3S_matrixIndex, EPAS3S_a001_sent1Mia, EPAS3S_a002_sent1Error, EPAS3S_a003_trqSens1Supply and 147 more). Bit layout, scaling, units and value tables."
---

# EPAS3S_alertMatrix (0x391) — Electric power steering (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH

Electric power steering (secondary) message: alert matrix. This page documents the 151 signals of EPAS3S_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3S_alertMatrix` |
| Ethernet-side id | 0x391 (913) |
| ECU | [Electric power steering (secondary)](../../epas3s.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPAS3S |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 151 |

## Signals of EPAS3S_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `EPAS3S_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3S_matrixIndex` | selector | Electric power steering (secondary): matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `EPAS3S_a001_sent1Mia` | page 0 | Electric power steering (secondary): a001 sent1 mia | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a002_sent1Error` | page 0 | Electric power steering (secondary): a002 sent1 error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a003_trqSens1Supply` | page 0 | Electric power steering (secondary): a003 trq sens1 supply | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a004_trqSens1Eeprom` | page 0 | Electric power steering (secondary): a004 trq sens1 eeprom | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a005_sent2Mia` | page 0 | Electric power steering (secondary): a005 sent2 mia | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a006_sent2Error` | page 0 | Electric power steering (secondary): a006 sent2 error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a007_trqSens2Supply` | page 0 | Electric power steering (secondary): a007 trq sens2 supply | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a008_trqSens2Eeprom` | page 0 | Electric power steering (secondary): a008 trq sens2 eeprom | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a009_sentDiff` | page 0 | Electric power steering (secondary): a009 sent diff | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a010_trqSensCalError` | page 0 | Electric power steering (secondary): a010 trq sens cal error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a011_currentSensError` | page 0 | Electric power steering (secondary): a011 current sens error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a012_currentSensCalError` | page 0 | Electric power steering (secondary): a012 current sens cal error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a013_gateDriveError` | page 0 | Electric power steering (secondary): a013 gate drive error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a014_gateDriveTxError` | page 0 | Electric power steering (secondary): a014 gate drive tx error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a015_gateDriveEeprom` | page 0 | Electric power steering (secondary): a015 gate drive eeprom | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a016_phaseUhighUv` | page 0 | Electric power steering (secondary): a016 phase uhigh uv | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a017_phaseUlowUv` | page 0 | Electric power steering (secondary): a017 phase ulow uv | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a018_phaseVhighUv` | page 0 | Electric power steering (secondary): a018 phase vhigh uv | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a019_phaseVlowUv` | page 0 | Electric power steering (secondary): a019 phase vlow uv | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a020_phaseWhighUv` | page 0 | Electric power steering (secondary): a020 phase whigh uv | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a021_phaseWlowUv` | page 0 | Electric power steering (secondary): a021 phase wlow uv | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a022_phaseUhighOv` | page 0 | Electric power steering (secondary): a022 phase uhigh ov | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a023_phaseUlowOv` | page 0 | Electric power steering (secondary): a023 phase ulow ov | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a024_phaseVhighOv` | page 0 | Electric power steering (secondary): a024 phase vhigh ov | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a025_phaseVlowOv` | page 0 | Electric power steering (secondary): a025 phase vlow ov | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a026_phaseWhighOv` | page 0 | Electric power steering (secondary): a026 phase whigh ov | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a027_phaseWlowOv` | page 0 | Electric power steering (secondary): a027 phase wlow ov | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a028_phaseUbootUv` | page 0 | Electric power steering (secondary): a028 phase uboot uv | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a029_phaseVbootUv` | page 0 | Electric power steering (secondary): a029 phase vboot uv | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a030_phaseWbootUv` | page 0 | Electric power steering (secondary): a030 phase wboot uv | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a031_abnormalShutdown` | page 0 | Electric power steering (secondary): a031 abnormal shutdown | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a032_vRegOutputUv` | page 0 | Electric power steering (secondary): a032 v reg output uv | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a033_vRegOutputOv` | page 0 | Electric power steering (secondary): a033 v reg output ov | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a034_vRegError` | page 0 | Electric power steering (secondary): a034 v reg error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a035_vbbSupplyUv` | page 0 | Electric power steering (secondary): a035 vbb supply uv | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a036_vbbSupplyOv` | page 0 | Electric power steering (secondary): a036 vbb supply ov | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a037_motPos1ParityError` | page 0 | Electric power steering (secondary): a037 mot pos1 parity error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a038_motPos1Uv` | page 0 | Electric power steering (secondary): a038 mot pos1 uv | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a039_motPos1MagnetMia` | page 0 | Electric power steering (secondary): a039 mot pos1 magnet mia | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a040_motPos1LogicError` | page 0 | Electric power steering (secondary): a040 mot pos1 logic error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a041_motPos1tempError` | page 0 | Electric power steering (secondary): a041 mot pos1temp error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a042_motPos2ParityError` | page 0 | Electric power steering (secondary): a042 mot pos2 parity error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a043_motPos2Uv` | page 0 | Electric power steering (secondary): a043 mot pos2 uv | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a044_motPos2MagnetMia` | page 0 | Electric power steering (secondary): a044 mot pos2 magnet mia | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a045_motPos2LogicError` | page 0 | Electric power steering (secondary): a045 mot pos2 logic error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a046_motPos2tempError` | page 0 | Electric power steering (secondary): a046 mot pos2temp error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a047_motPosCorrError` | page 0 | Electric power steering (secondary): a047 mot pos corr error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a048_motPosCalError` | page 0 | Electric power steering (secondary): a048 mot pos cal error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a049_piCtrlError` | page 0 | Electric power steering (secondary): a049 pi ctrl error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a050_mcuSmuError` | page 0 | Electric power steering (secondary): a050 mcu smu error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a051_mcuSupError` | page 0 | Electric power steering (secondary): a051 mcu sup error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a052_intWatchdogError` | page 0 | Electric power steering (secondary): a052 int watchdog error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a053_extWatchdogError` | page 0 | Electric power steering (secondary): a053 ext watchdog error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a054_memoryProtectError` | page 0 | Electric power steering (secondary): a054 memory protect error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a055_floatPointError` | page 0 | Electric power steering (secondary): a055 float point error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a056_battUv` | page 0 | Electric power steering (secondary): a056 batt uv | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a057_battUvReduced` | page 0 | Electric power steering (secondary): a057 batt uv reduced | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a058_battOv` | page 0 | Electric power steering (secondary): a058 batt ov | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a059_battOvReduced` | page 0 | Electric power steering (secondary): a059 batt ov reduced | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a060_battBridgeDiff` | page 0 | Electric power steering (secondary): a060 batt bridge diff | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a061_bridgeUv` | page 1 | Electric power steering (secondary): a061 bridge uv | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a062_assistCorrError` | page 1 | Electric power steering (secondary): a062 assist corr error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a063_dampCorrError` | page 1 | Electric power steering (secondary): a063 damp corr error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a064_phaseCompCorrError` | page 1 | Electric power steering (secondary): a064 phase comp corr error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a065_trqTarCorrError` | page 1 | Electric power steering (secondary): a065 trq tar corr error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a066_returnCorrError` | page 1 | Electric power steering (secondary): a066 return corr error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a067_yawDampCorrError` | page 1 | Electric power steering (secondary): a067 yaw damp corr error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a068_hystCorrError` | page 1 | Electric power steering (secondary): a068 hyst corr error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a069_eacCorrError` | page 1 | Electric power steering (secondary): a069 eac corr error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a070_hodCorrError` | page 1 | Electric power steering (secondary): a070 hod corr error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a071_vehSpdCorrError` | page 1 | Electric power steering (secondary): a071 veh spd corr error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a072_motFeedFwdError` | page 1 | Electric power steering (secondary): a072 mot feed fwd error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a073_motParEstError` | page 1 | Electric power steering (secondary): a073 mot par est error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a074_overHeatProtect` | page 1 | Electric power steering (secondary): a074 over heat protect | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a075_fspPwrCut` | page 1 | Electric power steering (secondary): a075 fsp pwr cut | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a076_tempSensOutofRange` | page 1 | Electric power steering (secondary): a076 temp sens outof range | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a077_highSideFetError` | page 1 | Electric power steering (secondary): a077 high side fet error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a078_phaseDisconnectError` | page 1 | Electric power steering (secondary): a078 phase disconnect error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a079_backupCurrentPlaus` | page 1 | Electric power steering (secondary): a079 backup current plaus | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a080_ecuInitArbError` | page 1 | Electric power steering (secondary): a080 ecu init arb error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a081_coggCompError` | page 1 | Electric power steering (secondary): a081 cogg comp error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a082_polarityCalError` | page 1 | Electric power steering (secondary): a082 polarity cal error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a083_crcMismatch` | page 1 | Electric power steering (secondary): a083 crc mismatch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a084_eacCancelled` | page 1 | Electric power steering (secondary): a084 eac cancelled | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a085_canBusOff` | page 1 | Electric power steering (secondary): a085 can bus off | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a086_dasMia` | page 1 | Electric power steering (secondary): a086 das mia | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a087_dasCntError` | page 1 | Electric power steering (secondary): a087 das cnt error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a088_dasCsError` | page 1 | Electric power steering (secondary): a088 das cs error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a089_espWsMia` | page 1 | Electric power steering (secondary): a089 esp ws mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a090_espWsCntError` | page 1 | Electric power steering (secondary): a090 esp ws cnt error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a091_espWsCsError` | page 1 | Electric power steering (secondary): a091 esp ws cs error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a092_espWrMia` | page 1 | Electric power steering (secondary): a092 esp wr mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a093_espWrCntError` | page 1 | Electric power steering (secondary): a093 esp wr cnt error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a094_espWrCsError` | page 1 | Electric power steering (secondary): a094 esp wr cs error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a095_espWsStatus` | page 1 | Electric power steering (secondary): a095 esp ws status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a096_rcmMia` | page 1 | Electric power steering (secondary): a096 rcm mia | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a097_rcmCntError` | page 1 | Electric power steering (secondary): a097 rcm cnt error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a098_rcmCsError` | page 1 | Electric power steering (secondary): a098 rcm cs error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a099_yawRateStatus` | page 1 | Electric power steering (secondary): a099 yaw rate status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a100_diMia` | page 1 | Electric power steering (secondary): a100 di mia | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a101_diCntError` | page 1 | Electric power steering (secondary): a101 di cnt error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a102_diCsError` | page 1 | Electric power steering (secondary): a102 di cs error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a103_vcFrontMia` | page 1 | Electric power steering (secondary): a103 vc front mia | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a104_vcFrontCntError` | page 1 | Electric power steering (secondary): a104 vc front cnt error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a105_vcFrontCsError` | page 1 | Electric power steering (secondary): a105 vc front cs error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a106_vcFrontTempMia` | page 1 | Electric power steering (secondary): a106 vc front temp mia | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a107_uiTuneReqMia` | page 1 | Electric power steering (secondary): a107 ui tune req mia | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a108_uiTuneReqCntError` | page 1 | Electric power steering (secondary): a108 ui tune req cnt error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a109_uiTuneReqCsError` | page 1 | Electric power steering (secondary): a109 ui tune req cs error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a110_sasMia` | page 1 | Electric power steering (secondary): a110 sas mia | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a111_sasCntError` | page 1 | Electric power steering (secondary): a111 sas cnt error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a112_sasCsError` | page 1 | Electric power steering (secondary): a112 sas cs error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a113_sasStatusError` | page 1 | Electric power steering (secondary): a113 sas status error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a114_gtwConfigMia` | page 1 | Electric power steering (secondary): a114 gtw config mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a115_ecuStatMia` | page 1 | Electric power steering (secondary): a115 ecu stat mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a116_ecuStatCntError` | page 1 | Electric power steering (secondary): a116 ecu stat cnt error | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a117_ecuStatCrcError` | page 1 | Electric power steering (secondary): a117 ecu stat crc error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a118_privateBusOff` | page 1 | Electric power steering (secondary): a118 private bus off | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a119_pvtEcuStatMia` | page 1 | Electric power steering (secondary): a119 pvt ecu stat mia | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a120_pvtEcuStatCntError` | page 1 | Electric power steering (secondary): a120 pvt ecu stat cnt error | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a121_pvtEcuStatCrcError` | page 2 | Electric power steering (secondary): a121 pvt ecu stat crc error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a122_olpActive` | page 2 | Electric power steering (secondary): a122 olp active | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a123_combEcu2StatFail` | page 2 | Electric power steering (secondary): a123 comb ecu2 stat fail | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a124_tempSensStuckInRange` | page 2 | Electric power steering (secondary): a124 temp sens stuck in range | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a125_trqSensTrimOutRange` | page 2 | Electric power steering (secondary): a125 trq sens trim out range | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a126_apsMia` | page 2 | Electric power steering (secondary): a126 aps mia | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a127_apsCntError` | page 2 | Electric power steering (secondary): a127 aps cnt error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a128_apsCsError` | page 2 | Electric power steering (secondary): a128 aps cs error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a129_combEcu1StatFail` | page 2 | Electric power steering (secondary): a129 comb ecu1 stat fail | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a130_sasOffsetNotCal` | page 2 | Electric power steering (secondary): a130 sas offset not cal | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a131_phaseFeedbackError` | page 2 | Electric power steering (secondary): a131 phase feedback error | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a132_motFeedFwdCounter25` | page 2 | Electric power steering (secondary): a132 mot feed fwd counter25 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a133_motFeedFwdCounter50` | page 2 | Electric power steering (secondary): a133 mot feed fwd counter50 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a134_motFeedFwdCounter85` | page 2 | Electric power steering (secondary): a134 mot feed fwd counter85 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a135_piCtrlCounter25` | page 2 | Electric power steering (secondary): a135 pi ctrl counter25 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a136_piCtrlCounter50` | page 2 | Electric power steering (secondary): a136 pi ctrl counter50 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a137_piCtrlCounter85` | page 2 | Electric power steering (secondary): a137 pi ctrl counter85 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a144_diSpdMia` | page 2 | Electric power steering (secondary): a144 di spd mia | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a145_diSpdCntError` | page 2 | Electric power steering (secondary): a145 di spd cnt error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a146_diSpdCsError` | page 2 | Electric power steering (secondary): a146 di spd cs error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a147_backupVehSpeed` | page 2 | Electric power steering (secondary): a147 backup veh speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a148_vMaxAssist` | page 2 | Electric power steering (secondary): a148 v max assist | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a149_currentSensPathSwitch` | page 2 | Electric power steering (secondary): a149 current sens path switch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a150_currentSensOffsetDetect` | page 2 | Electric power steering (secondary): a150 current sens offset detect | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a151_dcsCboot` | page 2 | Electric power steering (secondary): a151 dcs cboot | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a152_dcsDiagReg` | page 2 | Electric power steering (secondary): a152 dcs diag reg | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a153_dcsInitOffset` | page 2 | Electric power steering (secondary): a153 dcs init offset | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a154_assistTorqueDisabled` | page 2 | Electric power steering (secondary): a154 assist torque disabled | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a155_backupEacActive` | page 2 | Electric power steering (secondary): a155 backup eac active | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPAS3S_a156_angleSensorDivergence` | page 2 | Electric power steering (secondary): a156 angle sensor divergence | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`EPAS3S_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (30 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electric power steering (secondary) messages (EPAS3S)](../../epas3s.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
