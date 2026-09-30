---
layout: default
title: "ESP_alertMatrix (0x3D5) — Electronic stability control, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Electronic stability control message: alert matrix. Ethernet-side message ESP_alertMatrix of Electronic stability control for Tesla Model 3 / Model Y firmware 2025.20.8, 379 signals (ESP_matrixIndex, ESP_a001_ecuGenericFault, ESP_a002_valvesGenericFault, ESP_a003_outletValvesFault and 375 more). Bit layout, scaling, units and value tables."
---

# ESP_alertMatrix (0x3D5) — Electronic stability control, Tesla Model 3 / Model Y 2025.20.8 ETH

Electronic stability control message: alert matrix. This page documents the 379 signals of ESP_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_alertMatrix` |
| Ethernet-side id | 0x3D5 (981) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 379 |

## Signals of ESP_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `ESP_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_matrixIndex` | selector | Electronic stability control: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5`<br>6 = `AlertMatrix6` | plausible |
| `ESP_a001_ecuGenericFault` | page 0 | Electronic stability control: a001 ecu generic fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a002_valvesGenericFault` | page 0 | Electronic stability control: a002 valves generic fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a003_outletValvesFault` | page 0 | Electronic stability control: a003 outlet valves fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a004_inletValvesFault` | page 0 | Electronic stability control: a004 inlet valves fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a005_HSVValvesFault` | page 0 | Electronic stability control: a005 HSV valves fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a006_USVValvesFault` | page 0 | Electronic stability control: a006 USV valves fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a007_pumpMotorFault` | page 0 | Electronic stability control: a007 pump motor fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a008_pumpMotor12VsupplyLow` | page 0 | Electronic stability control: a008 pump motor12 vsupply low | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a009_12VHardUndervoltage` | page 0 | Electronic stability control: a009 12 v hard undervoltage | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a010_12VUndervoltage` | page 0 | Electronic stability control: a010 12 v undervoltage | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a011_12VSystemUndervoltage` | page 0 | Electronic stability control: a011 12 v system undervoltage | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a012_netUndervoltage` | page 0 | Electronic stability control: a012 net undervoltage | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a013_valveRelayUndervoltage` | page 0 | Electronic stability control: a013 valve relay undervoltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a014_WSSSupplyUndervoltage` | page 0 | Electronic stability control: a014 WSS supply undervoltage | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a015_12VSupplyOvervoltage` | page 0 | Electronic stability control: a015 12 v supply overvoltage | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a016_12VSystemOvervoltage` | page 0 | Electronic stability control: a016 12 v system overvoltage | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a017_netOvervoltage` | page 0 | Electronic stability control: a017 net overvoltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a018_WSSSignFrontAxle` | page 0 | Electronic stability control: a018 WSS sign front axle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a019_WSSSignRearAxle` | page 0 | Electronic stability control: a019 WSS sign rear axle | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a020_WSSGenericTempFault` | page 0 | Electronic stability control: a020 WSS generic temp fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a021_WSSGeneralVDiffFault` | page 0 | Electronic stability control: a021 WSS general v diff fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a022_WSSDirectionFault` | page 0 | Electronic stability control: a022 WSS direction fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a023_WSSSeveralSuspected` | page 0 | Electronic stability control: a023 WSS several suspected | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a024_WSSReverseCurrent` | page 0 | Electronic stability control: a024 WSS reverse current | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a025_FrLWSSOpenOrShortToGnd` | page 0 | Electronic stability control: a025 fr LWSS open or short to gnd | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a026_FrLWSSShortTo12V` | page 0 | Electronic stability control: a026 fr LWSS short to12 v | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a027_FrLWSSLineInterruption` | page 0 | Electronic stability control: a027 fr LWSS line interruption | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a028_FrLWSSMaxSpeedExceeded` | page 0 | Electronic stability control: a028 fr LWSS max speed exceeded | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a029_FrLWSSTooManyPulses` | page 0 | Electronic stability control: a029 fr LWSS too many pulses | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a030_FrLWSSLostSignal` | page 0 | Electronic stability control: a030 fr LWSS lost signal | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a031_FrLWSSNoPulsesDetected` | page 0 | Electronic stability control: a031 fr LWSS no pulses detected | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a032_FrLWSSWrongSensorType` | page 0 | Electronic stability control: a032 fr LWSS wrong sensor type | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a033_FrLWSSSignalNoise` | page 0 | Electronic stability control: a033 fr LWSS signal noise | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a034_FrLWSSVDiffFault` | page 0 | Electronic stability control: a034 fr LWSSV diff fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a035_FrLWSSDirectionFault` | page 0 | Electronic stability control: a035 fr LWSS direction fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a036_FrLWSSLargeAirGap` | page 0 | Electronic stability control: a036 fr LWSS large air gap | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a037_FrLWSSSupplyShortToGnd` | page 0 | Electronic stability control: a037 fr LWSS supply short to gnd | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a038_FrLWSSGeneralFault` | page 0 | Electronic stability control: a038 fr LWSS general fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a039_FrRWSSOpenOrShortToGnd` | page 0 | Electronic stability control: a039 fr RWSS open or short to gnd | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a040_FrRWSSShortTo12V` | page 0 | Electronic stability control: a040 fr RWSS short to12 v | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a041_FrRWSSLineInterruption` | page 0 | Electronic stability control: a041 fr RWSS line interruption | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a042_FrRWSSMaxSpeedExceeded` | page 0 | Electronic stability control: a042 fr RWSS max speed exceeded | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a043_FrRWSSTooManyPulses` | page 0 | Electronic stability control: a043 fr RWSS too many pulses | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a044_FrRWSSLostSignal` | page 0 | Electronic stability control: a044 fr RWSS lost signal | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a045_FrRWSSNoPulsesDetected` | page 0 | Electronic stability control: a045 fr RWSS no pulses detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a046_FrRWSSWrongSensorType` | page 0 | Electronic stability control: a046 fr RWSS wrong sensor type | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a047_FrRWSSSignalNoise` | page 0 | Electronic stability control: a047 fr RWSS signal noise | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a048_FrRWSSVDiffFault` | page 0 | Electronic stability control: a048 fr RWSSV diff fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a049_FrRWSSDirectionFault` | page 0 | Electronic stability control: a049 fr RWSS direction fault | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a050_FrRWSSLargeAirGap` | page 0 | Electronic stability control: a050 fr RWSS large air gap | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a051_FrRWSSSupplyShortToGnd` | page 0 | Electronic stability control: a051 fr RWSS supply short to gnd | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a052_FrRWSSGeneralFault` | page 0 | Electronic stability control: a052 fr RWSS general fault | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a053_ReLWSSOpenOrShortToGnd` | page 0 | Electronic stability control: a053 re LWSS open or short to gnd | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a054_ReLWSSShortTo12V` | page 0 | Electronic stability control: a054 re LWSS short to12 v | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a055_ReLWSSLineInterruption` | page 0 | Electronic stability control: a055 re LWSS line interruption | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a056_ReLWSSMaxSpeedExceeded` | page 0 | Electronic stability control: a056 re LWSS max speed exceeded | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a057_ReLWSSTooManyPulses` | page 0 | Electronic stability control: a057 re LWSS too many pulses | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a058_ReLWSSLostSignal` | page 0 | Electronic stability control: a058 re LWSS lost signal | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a059_ReLWSSNoPulsesDetected` | page 0 | Electronic stability control: a059 re LWSS no pulses detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a060_ReLWSSWrongSensorType` | page 0 | Electronic stability control: a060 re LWSS wrong sensor type | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a061_ReLWSSSignalNoise` | page 1 | Electronic stability control: a061 re LWSS signal noise | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a062_ReLWSSVDiffFault` | page 1 | Electronic stability control: a062 re LWSSV diff fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a063_ReLWSSDirectionFault` | page 1 | Electronic stability control: a063 re LWSS direction fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a064_ReLWSSLargeAirGap` | page 1 | Electronic stability control: a064 re LWSS large air gap | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a065_ReLWSSSupplyShortToGnd` | page 1 | Electronic stability control: a065 re LWSS supply short to gnd | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a066_ReLWSSGeneralFault` | page 1 | Electronic stability control: a066 re LWSS general fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a067_ReRWSSOpenOrShortToGnd` | page 1 | Electronic stability control: a067 re RWSS open or short to gnd | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a068_ReRWSSShortTo12V` | page 1 | Electronic stability control: a068 re RWSS short to12 v | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a069_ReRWSSLineInterruption` | page 1 | Electronic stability control: a069 re RWSS line interruption | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a070_ReRWSSMaxSpeedExceeded` | page 1 | Electronic stability control: a070 re RWSS max speed exceeded | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a071_ReRWSSTooManyPulses` | page 1 | Electronic stability control: a071 re RWSS too many pulses | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a072_ReRWSSLostSignal` | page 1 | Electronic stability control: a072 re RWSS lost signal | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a073_ReRWSSNoPulsesDetected` | page 1 | Electronic stability control: a073 re RWSS no pulses detected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a074_ReRWSSWrongSensorType` | page 1 | Electronic stability control: a074 re RWSS wrong sensor type | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a075_ReRWSSSignalNoise` | page 1 | Electronic stability control: a075 re RWSS signal noise | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a076_ReRWSSVDiffFault` | page 1 | Electronic stability control: a076 re RWSSV diff fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a077_ReRWSSDirectionFault` | page 1 | Electronic stability control: a077 re RWSS direction fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a078_ReRWSSLargeAirGap` | page 1 | Electronic stability control: a078 re RWSS large air gap | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a079_ReRWSSSupplyShortToGnd` | page 1 | Electronic stability control: a079 re RWSS supply short to gnd | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a080_ReRWSSGeneralFault` | page 1 | Electronic stability control: a080 re RWSS general fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a081_PressureSensorShort` | page 1 | Electronic stability control: a081 pressure sensor short | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a082_PMCSensorOffsetHigh` | page 1 | Electronic stability control: a082 PMC sensor offset high | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a083_PMCSensorFault` | page 1 | Electronic stability control: a083 PMC sensor fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a084_BrakeFluidReservoirLow` | page 1 | Electronic stability control: a084 brake fluid reservoir low | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a085_BrakeSwitchStuckHigh` | page 1 | Electronic stability control: a085 brake switch stuck high | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a086_BrakeSwitchImplausible1` | page 1 | Electronic stability control: a086 brake switch implausible1 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a087_BrakeSwitchImplausible3` | page 1 | Electronic stability control: a087 brake switch implausible3 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a088_absContinuousControl` | page 1 | Electronic stability control: a088 abs continuous control | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a089_absNoPressureIncrease` | page 1 | Electronic stability control: a089 abs no pressure increase | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a090_vdcContinuousControl` | page 1 | Electronic stability control: a090 vdc continuous control | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a091_CANUndervoltage` | page 1 | Electronic stability control: a091 CAN undervoltage | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a092_CANOvervoltage` | page 1 | Electronic stability control: a092 CAN overvoltage | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a093_partyBusOff` | page 1 | Electronic stability control: a093 party bus off | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a094_partyBusPassive` | page 1 | Electronic stability control: a094 party bus passive | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a095_chassisBusOff` | page 1 | Electronic stability control: a095 chassis bus off | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a096_chassisBusPassive` | page 1 | Electronic stability control: a096 chassis bus passive | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a097_tcsRefSpeedNotInit` | page 1 | Electronic stability control: a097 tcs ref speed not init | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a098_vdcRefSpeedNotInit` | page 1 | Electronic stability control: a098 vdc ref speed not init | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a099_brakeTempModelOverheat` | page 1 | Electronic stability control: a099 brake temp model overheat | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a100_brakeTempModelDisabled` | page 1 | Electronic stability control: a100 brake temp model disabled | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a101_ebdFault` | page 1 | Electronic stability control: a101 ebd fault | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a102_absFault` | page 1 | Electronic stability control: a102 abs fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a103_stabilityControlFault` | page 1 | Electronic stability control: a103 stability control fault | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a104_hbcEnabled` | page 1 | Electronic stability control: a104 hbc enabled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a105_ebrFault` | page 1 | Electronic stability control: a105 ebr fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a106_vdcActuatorFault` | page 1 | Electronic stability control: a106 vdc actuator fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a107_reserved107` | page 1 | Electronic stability control: a107 reserved107 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a108_reserved108` | page 1 | Electronic stability control: a108 reserved108 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a109_reserved109` | page 1 | Electronic stability control: a109 reserved109 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a110_rollerBenchActive` | page 1 | Electronic stability control: a110 roller bench active | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a111_absActive` | page 1 | Electronic stability control: a111 abs active | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a112_espActive` | page 1 | Electronic stability control: a112 esp active | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a113_btcActive` | page 1 | Electronic stability control: a113 btc active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a114_tvdcActive` | page 1 | Electronic stability control: a114 tvdc active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a115_ebdActive` | page 1 | Electronic stability control: a115 ebd active | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a116_tsmActive` | page 1 | Electronic stability control: a116 tsm active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a117_hbaActive` | page 1 | Electronic stability control: a117 hba active | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a118_hfcActive` | page 1 | Electronic stability control: a118 hfc active | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a119_hbbActive` | page 1 | Electronic stability control: a119 hbb active | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a120_rmiActive` | page 1 | Electronic stability control: a120 rmi active | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a121_regenTcActive` | page 2 | Electronic stability control: a121 regen tc active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a122_bdwActive` | page 2 | Electronic stability control: a122 bdw active | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a123_ebrActive` | page 2 | Electronic stability control: a123 ebr active | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a124_ebrSkidActive` | page 2 | Electronic stability control: a124 ebr skid active | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a125_reserved125` | page 2 | Electronic stability control: a125 reserved125 | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a126_reserved126` | page 2 | Electronic stability control: a126 reserved126 | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a127_reserved127` | page 2 | Electronic stability control: a127 reserved127 | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a128_reserved128` | page 2 | Electronic stability control: a128 reserved128 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a129_reserved129` | page 2 | Electronic stability control: a129 reserved129 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a130_EPAS3PsysStatusTimeout` | page 2 | Electronic stability control: a130 EPAS3 psys status timeout | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a131_EPAS3PsysStatusDLC` | page 2 | Electronic stability control: a131 EPAS3 psys status DLC | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a132_EPAS3PsysStatusChecksum` | page 2 | Electronic stability control: a132 EPAS3 psys status checksum | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a133_EPAS3PsysStatusCounter` | page 2 | Electronic stability control: a133 EPAS3 psys status counter | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a134_steeringAngleInvalid` | page 2 | Electronic stability control: a134 steering angle invalid | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a135_steeringAngleNoCenter` | page 2 | Electronic stability control: a135 steering angle no center | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a136_steeringAngleFrozen` | page 2 | Electronic stability control: a136 steering angle frozen | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a137_steeringOffsetTooLarge` | page 2 | Electronic stability control: a137 steering offset too large | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a138_steeringAngleImplaus` | page 2 | Electronic stability control: a138 steering angle implaus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a139_steeringAngleWrongSign` | page 2 | Electronic stability control: a139 steering angle wrong sign | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a140_RCMInertial1Timeout` | page 2 | Electronic stability control: a140 RCM inertial1 timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a141_RCMInertial1DLC` | page 2 | Electronic stability control: a141 RCM inertial1 DLC | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a142_RCMInertial1Checksum` | page 2 | Electronic stability control: a142 RCM inertial1 checksum | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a143_RCMInertial1Counter` | page 2 | Electronic stability control: a143 RCM inertial1 counter | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a144_yawMaxLatency` | page 2 | Electronic stability control: a144 yaw max latency | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a145_yawInitFault` | page 2 | Electronic stability control: a145 yaw init fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a146_yawInvalidValue` | page 2 | Electronic stability control: a146 yaw invalid value | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a147_yawSensorNotAvailable` | page 2 | Electronic stability control: a147 yaw sensor not available | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a148_yawSignalFault` | page 2 | Electronic stability control: a148 yaw signal fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a149_yawInvalidSign` | page 2 | Electronic stability control: a149 yaw invalid sign | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a150_yawImplausible` | page 2 | Electronic stability control: a150 yaw implausible | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a151_RCMInertial2Timeout` | page 2 | Electronic stability control: a151 RCM inertial2 timeout | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a152_RCMInertial2DLC` | page 2 | Electronic stability control: a152 RCM inertial2 DLC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a153_RCMInertial2Checksum` | page 2 | Electronic stability control: a153 RCM inertial2 checksum | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a154_RCMInertial2Counter` | page 2 | Electronic stability control: a154 RCM inertial2 counter | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a155_ayMaxLatency` | page 2 | Electronic stability control: a155 ay max latency | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a156_ayInitFault` | page 2 | Electronic stability control: a156 ay init fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a157_ayInvalidValue` | page 2 | Electronic stability control: a157 ay invalid value | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a158_aySensorNotAvailable` | page 2 | Electronic stability control: a158 ay sensor not available | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a159_aySignalFault` | page 2 | Electronic stability control: a159 ay signal fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a160_ayRangeExceeded` | page 2 | Electronic stability control: a160 ay range exceeded | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a161_ayOffsetExceeded` | page 2 | Electronic stability control: a161 ay offset exceeded | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a162_ayImplausible` | page 2 | Electronic stability control: a162 ay implausible | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a163_axMaxLatency` | page 2 | Electronic stability control: a163 ax max latency | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a164_axInitFault` | page 2 | Electronic stability control: a164 ax init fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a165_axInvalidValue` | page 2 | Electronic stability control: a165 ax invalid value | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a166_axSensorNotAvailable` | page 2 | Electronic stability control: a166 ax sensor not available | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a167_axSignalFault` | page 2 | Electronic stability control: a167 ax signal fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a168_axRangeExceeded` | page 2 | Electronic stability control: a168 ax range exceeded | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a169_axOffsetExceeded` | page 2 | Electronic stability control: a169 ax offset exceeded | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a170_axSignalFrozen` | page 2 | Electronic stability control: a170 ax signal frozen | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a171_axImplausible` | page 2 | Electronic stability control: a171 ax implausible | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a172_IBSTparty1Timeout` | page 2 | Electronic stability control: a172 IBS tparty1 timeout | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a173_IBSTparty1DLC` | page 2 | Electronic stability control: a173 IBS tparty1 DLC | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a174_IBSTparty1Checksum` | page 2 | Electronic stability control: a174 IBS tparty1 checksum | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a175_IBSTparty1Counter` | page 2 | Electronic stability control: a175 IBS tparty1 counter | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a176_IBSTEBRNotAvailable` | page 2 | Electronic stability control: a176 IBSTEBR not available | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a177_IBSTOutputRodDrvInvalid` | page 2 | Electronic stability control: a177 IBST output rod drv invalid | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a178_IBSTOutputRodActInvalid` | page 2 | Electronic stability control: a178 IBST output rod act invalid | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a179_IBSTparty2Timeout` | page 2 | Electronic stability control: a179 IBS tparty2 timeout | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a180_IBSTparty2Checksum` | page 2 | Electronic stability control: a180 IBS tparty2 checksum | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a181_IBSTparty2DLC` | page 3 | Electronic stability control: a181 IBS tparty2 DLC | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a182_IBSTparty2Counter` | page 3 | Electronic stability control: a182 IBS tparty2 counter | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a183_IBSTStatusOff` | page 3 | Electronic stability control: a183 IBST status off | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a184_IBSTpRunoutInvalid` | page 3 | Electronic stability control: a184 IBS tp runout invalid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a185_IBSTFeedforwardBackup` | page 3 | Electronic stability control: a185 IBST feedforward backup | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a186_IBSTBrakeAppliedInvalid` | page 3 | Electronic stability control: a186 IBST brake applied invalid | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a187_DIbtcRequestTimeout` | page 3 | Electronic stability control: a187 d ibtc request timeout | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a188_DIbtcRequestDLC` | page 3 | Electronic stability control: a188 d ibtc request DLC | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a189_DIbtcRequestChecksum` | page 3 | Electronic stability control: a189 d ibtc request checksum | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a190_DIbtcRequestCounter` | page 3 | Electronic stability control: a190 d ibtc request counter | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a191_DIchassisControlTimeout` | page 3 | Electronic stability control: a191 d ichassis control timeout | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a192_DIchassisControlDLC` | page 3 | Electronic stability control: a192 d ichassis control DLC | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a193_DIchassisControlChecksum` | page 3 | Electronic stability control: a193 d ichassis control checksum | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a194_DIchassisControlCounter` | page 3 | Electronic stability control: a194 d ichassis control counter | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a195_ptcStateInvalid` | page 3 | Electronic stability control: a195 ptc state invalid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a196_DIsystemStatusTimeout` | page 3 | Electronic stability control: a196 d isystem status timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a197_DIsystemStatusDLC` | page 3 | Electronic stability control: a197 d isystem status DLC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a198_DIsystemStatusChecksum` | page 3 | Electronic stability control: a198 d isystem status checksum | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a199_DIsystemStatusCounter` | page 3 | Electronic stability control: a199 d isystem status counter | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a200_reverseGearStuckHigh` | page 3 | Electronic stability control: a200 reverse gear stuck high | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a201_reverseGearStuckLow` | page 3 | Electronic stability control: a201 reverse gear stuck low | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a202_accelPedalInvalid` | page 3 | Electronic stability control: a202 accel pedal invalid | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a203_DItorqueTimeout` | page 3 | Electronic stability control: a203 d itorque timeout | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a204_DItorqueDLC` | page 3 | Electronic stability control: a204 d itorque DLC | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a205_DItorqueChecksum` | page 3 | Electronic stability control: a205 d itorque checksum | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a206_DItorqueCounter` | page 3 | Electronic stability control: a206 d itorque counter | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a207_DITorqueCommandInvalid` | page 3 | Electronic stability control: a207 DI torque command invalid | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a208_DIRPMInvalid` | page 3 | Electronic stability control: a208 DIRPM invalid | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a209_DITorqueActualInvalid` | page 3 | Electronic stability control: a209 DI torque actual invalid | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a210_DIStorqueTimeout` | page 3 | Electronic stability control: a210 DI storque timeout | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a211_DIStorqueDLC` | page 3 | Electronic stability control: a211 DI storque DLC | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a212_DIStorqueChecksum` | page 3 | Electronic stability control: a212 DI storque checksum | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a213_DIStorqueCounter` | page 3 | Electronic stability control: a213 DI storque counter | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a214_DISTorqueCommandInvalid` | page 3 | Electronic stability control: a214 DIS torque command invalid | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a215_DISRPMInvalid` | page 3 | Electronic stability control: a215 DISRPM invalid | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a216_DISTorqueActualInvalid` | page 3 | Electronic stability control: a216 DIS torque actual invalid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a217_DIvdcLeftTimeout` | page 3 | Electronic stability control: a217 d ivdc left timeout | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a218_DIvdcLeftDLC` | page 3 | Electronic stability control: a218 d ivdc left DLC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a219_DIvdcLeftChecksum` | page 3 | Electronic stability control: a219 d ivdc left checksum | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a220_DIvdcLeftCounter` | page 3 | Electronic stability control: a220 d ivdc left counter | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a221_DIvdcRightTimeout` | page 3 | Electronic stability control: a221 d ivdc right timeout | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a222_DIvdcRightDLC` | page 3 | Electronic stability control: a222 d ivdc right DLC | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a223_DIvdcRightChecksum` | page 3 | Electronic stability control: a223 d ivdc right checksum | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a224_DIvdcRightCounter` | page 3 | Electronic stability control: a224 d ivdc right counter | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a225_configMismatch` | page 3 | Electronic stability control: a225 config mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a226_bdwRequestInvalid` | page 3 | Electronic stability control: a226 bdw request invalid | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a227_bdwRequestActiveInvalid` | page 3 | Electronic stability control: a227 bdw request active invalid | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a228_GTWvinTimeout` | page 3 | Electronic stability control: a228 GT wvin timeout | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a229_GTWvinDLC` | page 3 | Electronic stability control: a229 GT wvin DLC | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a230_vinNotLearned` | page 3 | Electronic stability control: a230 vin not learned | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a231_storedVINMismatch` | page 3 | Electronic stability control: a231 stored VIN mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a232_PMstate2Timeout` | page 3 | Electronic stability control: a232 p mstate2 timeout | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a233_PMstate2Checksum` | page 3 | Electronic stability control: a233 p mstate2 checksum | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a234_PMstate2DLC` | page 3 | Electronic stability control: a234 p mstate2 DLC | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a235_PMstate2Counter` | page 3 | Electronic stability control: a235 p mstate2 counter | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a236_ebrCommandStateInvalid` | page 3 | Electronic stability control: a236 ebr command state invalid | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a237_vdcCommandStateInvalid` | page 3 | Electronic stability control: a237 vdc command state invalid | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a238_UIodoTimeout` | page 3 | Electronic stability control: a238 u iodo timeout | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a239_UIodoDLC` | page 3 | Electronic stability control: a239 u iodo DLC | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a240_LVPowerStateTimeout` | page 3 | Electronic stability control: a240 LV power state timeout | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a241_LVPowerStateChecksum` | page 4 | Electronic stability control: a241 LV power state checksum | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a242_LVPowerStateDLC` | page 4 | Electronic stability control: a242 LV power state DLC | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a243_LVPowerStateCounter` | page 4 | Electronic stability control: a243 LV power state counter | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a244_LVOffStateInvalid` | page 4 | Electronic stability control: a244 LV off state invalid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a245_LVGoingDownStateInvalid` | page 4 | Electronic stability control: a245 LV going down state invalid | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a246_VCFRONTsensorTimeout` | page 4 | Electronic stability control: a246 VCFRON tsensor timeout | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a247_VCFRONTsensorDLC` | page 4 | Electronic stability control: a247 VCFRON tsensor DLC | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a248_vdcBrkeTrqTarFrLInvalid` | page 4 | Electronic stability control: a248 vdc brke trq tar fr l invalid | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a249_vdcBrkeTrqTarFrRInvalid` | page 4 | Electronic stability control: a249 vdc brke trq tar fr r invalid | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a250_vdcBrkeTrqTarReLInvalid` | page 4 | Electronic stability control: a250 vdc brke trq tar re l invalid | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a251_vdcBrkeTrqTarReRInvalid` | page 4 | Electronic stability control: a251 vdc brke trq tar re r invalid | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a252_vdcWhlSlipLimFrLInvalid` | page 4 | Electronic stability control: a252 vdc whl slip lim fr l invalid | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a253_vdcWhlSlipLimFrRInvalid` | page 4 | Electronic stability control: a253 vdc whl slip lim fr r invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a254_vdcWhlSlipLimReLInvalid` | page 4 | Electronic stability control: a254 vdc whl slip lim re l invalid | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a255_vdcWhlSlipLimReRInvalid` | page 4 | Electronic stability control: a255 vdc whl slip lim re r invalid | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a256_epbmStatusTimeout` | page 4 | Electronic stability control: a256 epbm status timeout | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a257_epbmStatusChecksum` | page 4 | Electronic stability control: a257 epbm status checksum | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a258_epbmStatusDLC` | page 4 | Electronic stability control: a258 epbm status DLC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a259_epbmStatusCounter` | page 4 | Electronic stability control: a259 epbm status counter | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a260_epblStatusTimeout` | page 4 | Electronic stability control: a260 epbl status timeout | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a261_epblStatusChecksum` | page 4 | Electronic stability control: a261 epbl status checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a262_epblStatusDLC` | page 4 | Electronic stability control: a262 epbl status DLC | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a263_epblStatusCounter` | page 4 | Electronic stability control: a263 epbl status counter | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a264_pumpSpeedLimitInvalid` | page 4 | Electronic stability control: a264 pump speed limit invalid | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a265_DIRELtorqueTimeout` | page 4 | Electronic stability control: a265 DIRE ltorque timeout | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a266_DIRELtorqueDLC` | page 4 | Electronic stability control: a266 DIRE ltorque DLC | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a267_DIRELtorqueChecksum` | page 4 | Electronic stability control: a267 DIRE ltorque checksum | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a268_DIRELtorqueCounter` | page 4 | Electronic stability control: a268 DIRE ltorque counter | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a269_DIRELTorqueCommandInvalid` | page 4 | Electronic stability control: a269 DIREL torque command invalid | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a270_DIRELRPMInvalid` | page 4 | Electronic stability control: a270 DIRELRPM invalid | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a271_DIRELTorqueActualInvalid` | page 4 | Electronic stability control: a271 DIREL torque actual invalid | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a272_DIRERtorqueTimeout` | page 4 | Electronic stability control: a272 DIRE rtorque timeout | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a273_DIRERtorqueDLC` | page 4 | Electronic stability control: a273 DIRE rtorque DLC | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a274_DIRERtorqueChecksum` | page 4 | Electronic stability control: a274 DIRE rtorque checksum | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a275_DIRERtorqueCounter` | page 4 | Electronic stability control: a275 DIRE rtorque counter | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a276_DIRERTorqueCommandInvalid` | page 4 | Electronic stability control: a276 DIRER torque command invalid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a277_DIRERRPMInvalid` | page 4 | Electronic stability control: a277 DIRERRPM invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a278_DIRERTorqueActualInvalid` | page 4 | Electronic stability control: a278 DIRER torque actual invalid | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a279_lifetimeManagementOverrun` | page 4 | Electronic stability control: a279 lifetime management overrun | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a280_trackModeABSEnabled` | page 4 | Electronic stability control: a280 track mode ABS enabled | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a281_trackModeABSdisabled` | page 4 | Electronic stability control: a281 track mode AB sdisabled | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a282_trackModeABSRequestInvalid` | page 4 | Electronic stability control: a282 track mode ABS request invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a283_secondaryCollisionMitigationActive` | page 4 | Electronic stability control: a283 secondary collision mitigation active | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a284_scmRequestInvalidChecksum` | page 4 | Electronic stability control: a284 scm request invalid checksum | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a285_scmRequestDLC` | page 4 | Electronic stability control: a285 scm request DLC | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a286_hydroplaneDetected` | page 4 | Electronic stability control: a286 hydroplane detected | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a287_failedBrakeCircuitDetected` | page 4 | Electronic stability control: a287 failed brake circuit detected | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a288_leftBusOff` | page 4 | Electronic stability control: a288 left bus off | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a289_leftBusPassive` | page 4 | Electronic stability control: a289 left bus passive | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a290_brakeBusOff` | page 4 | Electronic stability control: a290 brake bus off | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a291_brakeBusPassive` | page 4 | Electronic stability control: a291 brake bus passive | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a292_PEPSstatusTimeout` | page 4 | Electronic stability control: a292 PEP sstatus timeout | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a293_PEPSstatusDLC` | page 4 | Electronic stability control: a293 PEP sstatus DLC | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a294_PEPSstatusChecksum` | page 4 | Electronic stability control: a294 PEP sstatus checksum | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a295_PEPSstatusCounter` | page 4 | Electronic stability control: a295 PEP sstatus counter | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a296_roadWheelAngleHealthDegraded` | page 4 | Electronic stability control: a296 road wheel angle health degraded | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a297_roadWheelAngleHealthFaulted` | page 4 | Electronic stability control: a297 road wheel angle health faulted | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a298_RSArearSteerStatusTimeout` | page 4 | Electronic stability control: a298 RS arear steer status timeout | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a299_RSArearSteerStatusDLC` | page 4 | Electronic stability control: a299 RS arear steer status DLC | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a300_RSArearSteerStatusChecksum` | page 4 | Electronic stability control: a300 RS arear steer status checksum | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a301_PEPSstatusCounter` | page 5 | Electronic stability control: a301 PEP sstatus counter | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a302_rearRoadWheelAngleHealthDegraded` | page 5 | Electronic stability control: a302 rear road wheel angle health degraded | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a303_rearRoadWheelAngleHealthFaulted` | page 5 | Electronic stability control: a303 rear road wheel angle health faulted | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a304_rearVCLVPowerStateTimeout` | page 5 | Electronic stability control: a304 rear VCLV power state timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a305_rearVCLVPowerStateDLC` | page 5 | Electronic stability control: a305 rear VCLV power state DLC | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a306_rearVCLVPowerStateChecksum` | page 5 | Electronic stability control: a306 rear VCLV power state checksum | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a307_rearVCLVPowerStateCounter` | page 5 | Electronic stability control: a307 rear VCLV power state counter | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a308_evacFillNotComplete` | page 5 | Electronic stability control: a308 evac fill not complete | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a309_factoryModeActive` | page 5 | Electronic stability control: a309 factory mode active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a310_brakeLatencyReductionActive` | page 5 | Electronic stability control: a310 brake latency reduction active | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a311_aesActive` | page 5 | Electronic stability control: a311 aes active | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a312_undefinedAlertDetected` | page 5 | Electronic stability control: a312 undefined alert detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a313_cdpRequestStateInvalid` | page 5 | Electronic stability control: a313 cdp request state invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a314_aesFault` | page 5 | Electronic stability control: a314 aes fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a315_EMCBackup11Timeout` | page 5 | Electronic stability control: a315 EMC backup11 timeout | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a316_EMCBackup11DLC` | page 5 | Electronic stability control: a316 EMC backup11 DLC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a317_EMCBackup11Checksum` | page 5 | Electronic stability control: a317 EMC backup11 checksum | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a318_EMCBackup11Counter` | page 5 | Electronic stability control: a318 EMC backup11 counter | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a319_AES_BackupActuatorActive` | page 5 | Electronic stability control: a319 AES backup actuator active | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a320_DPB_actuator1Counter` | page 5 | Electronic stability control: a320 DPB actuator1 counter | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a321_DPB_actuator1Checksum` | page 5 | Electronic stability control: a321 DPB actuator1 checksum | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a322_DPB_actuator1DLC` | page 5 | Electronic stability control: a322 DPB actuator1 DLC | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a323_DPB_actuator1Timeout` | page 5 | Electronic stability control: a323 DPB actuator1 timeout | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a324_DPB_actuator2Counter` | page 5 | Electronic stability control: a324 DPB actuator2 counter | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a325_DPB_actuator2Checksum` | page 5 | Electronic stability control: a325 DPB actuator2 checksum | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a326_DPB_actuator2DLC` | page 5 | Electronic stability control: a326 DPB actuator2 DLC | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a327_DPB_actuator2Timeout` | page 5 | Electronic stability control: a327 DPB actuator2 timeout | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a328_DPB_actuator3Counter` | page 5 | Electronic stability control: a328 DPB actuator3 counter | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a329_DPB_actuator3Checksum` | page 5 | Electronic stability control: a329 DPB actuator3 checksum | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a330_DPB_actuator3DLC` | page 5 | Electronic stability control: a330 DPB actuator3 DLC | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a331_DPB_actuator3Timeout` | page 5 | Electronic stability control: a331 DPB actuator3 timeout | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a332_PressureSensorValHigh` | page 5 | Electronic stability control: a332 pressure sensor val high | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a333_ActCircuitNoPressure` | page 5 | Electronic stability control: a333 act circuit no pressure | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a334_BrakePedalAppliedInvalid` | page 5 | Electronic stability control: a334 brake pedal applied invalid | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a335_LdmFxTarBrakeActInvalid` | page 5 | Electronic stability control: a335 ldm fx tar brake act invalid | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a336_FxTargetDriverInvalid` | page 5 | Electronic stability control: a336 fx target driver invalid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a337_pReductionPotentialInvalid` | page 5 | Electronic stability control: a337 p reduction potential invalid | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a338_pRunoutInvalid` | page 5 | Electronic stability control: a338 p runout invalid | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a339_sInputRodInvalid` | page 5 | Electronic stability control: a339 s input rod invalid | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a340_RollerBenchMisuse` | page 5 | Electronic stability control: a340 roller bench misuse | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a341_EnhancedPressureBuildActive` | page 5 | Electronic stability control: a341 enhanced pressure build active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a342_EnhancedPressureBuildNotActive` | page 5 | Electronic stability control: a342 enhanced pressure build not active | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a343_EnhancedPressureBuildLtmReached` | page 5 | Electronic stability control: a343 enhanced pressure build ltm reached | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a344_DIbrakeCommandCounter` | page 5 | Electronic stability control: a344 d ibrake command counter | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a345_DIbrakeCommandChecksum` | page 5 | Electronic stability control: a345 d ibrake command checksum | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a346_DIbrakeCommandDLC` | page 5 | Electronic stability control: a346 d ibrake command DLC | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a347_DIbrakeCommandTimeout` | page 5 | Electronic stability control: a347 d ibrake command timeout | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a348_brakeCmdStateInvalid` | page 5 | Electronic stability control: a348 brake cmd state invalid | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a349_ForceLampToRed` | page 5 | Electronic stability control: a349 force lamp to red | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a350_ActuatorOff` | page 5 | Electronic stability control: a350 actuator off | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a351_ActuatorYellowLampRequested` | page 5 | Electronic stability control: a351 actuator yellow lamp requested | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a352_ActuatorLDMFailure` | page 5 | Electronic stability control: a352 actuator LDM failure | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a353_PressureSensorImplausHigh` | page 5 | Electronic stability control: a353 pressure sensor implaus high | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a354_HBCRequestInvalid` | page 5 | Electronic stability control: a354 HBC request invalid | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a355_RecuStatusActInvalid` | page 5 | Electronic stability control: a355 recu status act invalid | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a356_DIFAxleTorqueInvalid` | page 5 | Electronic stability control: a356 DIF axle torque invalid | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a357_DIRAxleTorqueInvalid` | page 5 | Electronic stability control: a357 DIR axle torque invalid | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a358_externalActuatorFallback` | page 5 | Electronic stability control: a358 external actuator fallback | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a359_externalActuatorNoExtReq` | page 5 | Electronic stability control: a359 external actuator no ext req | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a360_BBbrakeActuationTimeout` | page 5 | Electronic stability control: a360 b bbrake actuation timeout | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a361_BBbrakeActuationDLC` | page 6 | Electronic stability control: a361 b bbrake actuation DLC | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a362_BBbrakeActuationChecksum` | page 6 | Electronic stability control: a362 b bbrake actuation checksum | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a363_BBbrakeActuationCounter` | page 6 | Electronic stability control: a363 b bbrake actuation counter | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a364_DIgearInvalid` | page 6 | Electronic stability control: a364 d igear invalid | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a365_TCSInputQualityTooLow` | page 6 | Electronic stability control: a365 TCS input quality too low | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a366_ActuatorBlendingModeReqNotAvailable` | page 6 | Electronic stability control: a366 actuator blending mode req not available | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a367_CBDS_fillBufferThreshold` | page 6 | Electronic stability control: a367 CBDS fill buffer threshold | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a368_CBDS_fmeInternalEvent` | page 6 | Electronic stability control: a368 CBDS fme internal event | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a369_LargeLeakageDetectedByDPB` | page 6 | Electronic stability control: a369 large leakage detected by DPB | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a370_DPB_actuator4Timeout` | page 6 | Electronic stability control: a370 DPB actuator4 timeout | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a371_DPB_actuator4DLC` | page 6 | Electronic stability control: a371 DPB actuator4 DLC | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a372_DPB_actuator4Checksum` | page 6 | Electronic stability control: a372 DPB actuator4 checksum | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a373_DPB_actuator4Counter` | page 6 | Electronic stability control: a373 DPB actuator4 counter | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a374_StatInvalid_DI_FullSNA` | page 6 | Electronic stability control: a374 stat invalid DI full SNA | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a375_PM_locStateCounter` | page 6 | Electronic stability control: a375 PM loc state counter | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a376_PM_locStateChecksum` | page 6 | Electronic stability control: a376 PM loc state checksum | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a377_PM_locStateDLC` | page 6 | Electronic stability control: a377 PM loc state DLC | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_a378_PM_locStateTimeout` | page 6 | Electronic stability control: a378 PM loc state timeout | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`ESP_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (60 signals), page 4 (60 signals), page 5 (60 signals), page 6 (18 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
