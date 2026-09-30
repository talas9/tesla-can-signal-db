---
layout: default
title: "TAS_alertMatrix (0x354) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Air suspension controller message: alert matrix. Ethernet-side message TAS_alertMatrix of Air suspension controller for Tesla Model 3 / Model Y firmware 2025.20.8, 161 signals (TAS_matrixIndex, TAS_a001_WatchdogReset, TAS_a002_PowerLossReset, TAS_a003_SWAssertion and 157 more). Bit layout, scaling, units and value tables."
---

# TAS_alertMatrix (0x354) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Air suspension controller message: alert matrix. This page documents the 161 signals of TAS_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_alertMatrix` |
| Ethernet-side id | 0x354 (852) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 161 |

## Signals of TAS_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `TAS_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_matrixIndex` | selector | Air suspension controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4`<br>5 = `AlertMatrix5` | plausible |
| `TAS_a001_WatchdogReset` | page 0 | Air suspension controller: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a002_PowerLossReset` | page 0 | Air suspension controller: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a003_SWAssertion` | page 0 | Air suspension controller: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a012_CPUReset` | page 0 | Air suspension controller: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a015_NVMMError` | page 0 | Air suspension controller: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a016_NVMMRecordError` | page 0 | Air suspension controller: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a021_TaskSchedulerError` | page 0 | Air suspension controller: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a022_TaskInitError` | page 0 | Air suspension controller: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a023_rtosResetRequested` | page 0 | Air suspension controller: a023 rtos reset requested | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a024_prefetchAbort` | page 0 | Air suspension controller: a024 prefetch abort | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a025_CrashEvent` | page 0 | Air suspension controller: a025 crash event | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a030_PWMerrorFL` | page 0 | Air suspension controller: a030 PW merror FL | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a031_PWMerrorFR` | page 0 | Air suspension controller: a031 PW merror FR | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a032_PWMerrorRL` | page 0 | Air suspension controller: a032 PW merror RL | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a033_PWMerrorRR` | page 0 | Air suspension controller: a033 PW merror RR | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a034_PWMshortFL` | page 0 | Air suspension controller: a034 PW mshort FL | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a035_PWMshortFR` | page 0 | Air suspension controller: a035 PW mshort FR | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a036_PWMshortRL` | page 0 | Air suspension controller: a036 PW mshort RL | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a037_PWMshortRR` | page 0 | Air suspension controller: a037 PW mshort RR | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a038_PWMopenFL` | page 0 | Air suspension controller: a038 PW mopen FL | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a039_PWMopenFR` | page 0 | Air suspension controller: a039 PW mopen FR | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a040_PWMopenRL` | page 0 | Air suspension controller: a040 PW mopen RL | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a041_PWMopenRR` | page 0 | Air suspension controller: a041 PW mopen RR | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a043_Task1msError` | page 0 | Air suspension controller: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a044_Task10msError` | page 0 | Air suspension controller: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a045_Task100msError` | page 0 | Air suspension controller: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a046_Task1000msError` | page 0 | Air suspension controller: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a061_XCPConnected` | page 1 | Air suspension controller: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a062_XCPWasConnected` | page 1 | Air suspension controller: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a063_abortFault` | page 1 | Air suspension controller: a063 abort fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a064_abortFaultExt` | page 1 | Air suspension controller: a064 abort fault ext | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a065_ahbWriteFault` | page 1 | Air suspension controller: a065 ahb write fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a066_undefinedInstructionAbort` | page 1 | Air suspension controller: a066 undefined instruction abort | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a067_reservedHandlerAbort` | page 1 | Air suspension controller: a067 reserved handler abort | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a070_underVoltage12V` | page 1 | Air suspension controller: a070 under voltage12 v | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a071_overVoltage12V` | page 1 | Air suspension controller: a071 over voltage12 v | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a072_shortCircuit5VOnBoard` | page 1 | Air suspension controller: a072 short circuit5 v on board | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a073_underVoltage5VOnBoard` | page 1 | Air suspension controller: a073 under voltage5 v on board | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a074_shortCircuit5VOffBoard` | page 1 | Air suspension controller: a074 short circuit5 v off board | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a075_underVoltage5VOffBoard` | page 1 | Air suspension controller: a075 under voltage5 v off board | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a076_overVoltage5VOffBoard` | page 1 | Air suspension controller: a076 over voltage5 v off board | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a077_pressureSigVTooLow` | page 1 | Air suspension controller: a077 pressure sig v too low | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a078_pressureSigVTooHigh` | page 1 | Air suspension controller: a078 pressure sig v too high | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a080_shortCircuit5VHeight` | page 1 | Air suspension controller: a080 short circuit5 v height | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a081_underVoltage5VHeight` | page 1 | Air suspension controller: a081 under voltage5 v height | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a082_overVoltage5VHeight` | page 1 | Air suspension controller: a082 over voltage5 v height | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a083_shortCircuit5VAnalog` | page 1 | Air suspension controller: a083 short circuit5 v analog | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a084_underVoltage5VAnalog` | page 1 | Air suspension controller: a084 under voltage5 v analog | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a085_overVoltage5VAnalog` | page 1 | Air suspension controller: a085 over voltage5 v analog | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a086_underVoltage12VSwtchd` | page 1 | Air suspension controller: a086 under voltage12 v swtchd | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a087_overVoltage12VSwtchd` | page 1 | Air suspension controller: a087 over voltage12 v swtchd | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a093_OTPError` | page 1 | Air suspension controller: a093 OTP error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a098_VCFRONT_MIA` | page 1 | Air suspension controller: a098 VCFRONT MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a099_UI_MIA` | page 1 | Air suspension controller: a099 UI MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a100_RCM_MIA` | page 1 | Air suspension controller: a100 RCM MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a101_ESP_MIA` | page 1 | Air suspension controller: a101 ESP MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a102_DI_MIA` | page 1 | Air suspension controller: a102 DI MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a103_GTW_MIA` | page 1 | Air suspension controller: a103 GTW MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a105_ECUDebugMode` | page 1 | Air suspension controller: a105 ECU debug mode | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a106_HighCPULoad` | page 1 | Air suspension controller: a106 high CPU load | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a107_HighStackUsage` | page 1 | Air suspension controller: a107 high stack usage | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a150_accelAvgImplausible_FL_X` | page 2 | Air suspension controller: a150 accel avg implausible FL x | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a151_accelAvgImplausible_FL_Y` | page 2 | Air suspension controller: a151 accel avg implausible FL y | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a152_accelAvgImplausible_FL_Z` | page 2 | Air suspension controller: a152 accel avg implausible FL z | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a153_accelAvgImplausible_FR_X` | page 2 | Air suspension controller: a153 accel avg implausible FR x | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a154_accelAvgImplausible_FR_Y` | page 2 | Air suspension controller: a154 accel avg implausible FR y | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a155_accelAvgImplausible_FR_Z` | page 2 | Air suspension controller: a155 accel avg implausible FR z | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a156_accelAvgImplausible_RL_X` | page 2 | Air suspension controller: a156 accel avg implausible RL x | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a157_accelAvgImplausible_RL_Y` | page 2 | Air suspension controller: a157 accel avg implausible RL y | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a158_accelAvgImplausible_RL_Z` | page 2 | Air suspension controller: a158 accel avg implausible RL z | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a159_accelAvgImplausible_RR_X` | page 2 | Air suspension controller: a159 accel avg implausible RR x | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a160_accelAvgImplausible_RR_Y` | page 2 | Air suspension controller: a160 accel avg implausible RR y | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a161_accelAvgImplausible_RR_Z` | page 2 | Air suspension controller: a161 accel avg implausible RR z | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a164_damperSolenoidMismatch` | page 2 | Air suspension controller: a164 damper solenoid mismatch | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a165_damperValveCompFL` | page 2 | Air suspension controller: a165 damper valve comp FL | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a166_damperValveRbndFL` | page 2 | Air suspension controller: a166 damper valve rbnd FL | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a167_damperValveCompFR` | page 2 | Air suspension controller: a167 damper valve comp FR | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a168_damperValveRbndFR` | page 2 | Air suspension controller: a168 damper valve rbnd FR | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a169_damperValveCompRL` | page 2 | Air suspension controller: a169 damper valve comp RL | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a170_damperValveRbndRL` | page 2 | Air suspension controller: a170 damper valve rbnd RL | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a171_damperValveCompRR` | page 2 | Air suspension controller: a171 damper valve comp RR | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a172_damperValveRbndRR` | page 2 | Air suspension controller: a172 damper valve rbnd RR | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a173_staticLeakDetectFL` | page 2 | Air suspension controller: a173 static leak detect FL | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a174_staticLeakDetectFR` | page 2 | Air suspension controller: a174 static leak detect FR | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a175_staticLeakDetectRL` | page 2 | Air suspension controller: a175 static leak detect RL | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a176_staticLeakDetectRR` | page 2 | Air suspension controller: a176 static leak detect RR | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a190_a2bFrontAxleFault` | page 3 | Air suspension controller: a190 a2b front axle fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a191_a2bRearAxleFault` | page 3 | Air suspension controller: a191 a2b rear axle fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a192_rideHeightObserverDivergence` | page 3 | Air suspension controller: a192 ride height observer divergence | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a193_EPAS3P_MIA` | page 3 | Air suspension controller: a193 EPAS3 p MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a194_a2bFrontAxleDataError` | page 3 | Air suspension controller: a194 a2b front axle data error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a195_a2bRearAxleDataError` | page 3 | Air suspension controller: a195 a2b rear axle data error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a196_adaptiveDampingUsingDSP` | page 3 | Air suspension controller: a196 adaptive damping using DSP | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a197_invalidAdaptiveModeRequested` | page 3 | Air suspension controller: a197 invalid adaptive mode requested | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a200_jackModeActive` | page 3 | Air suspension controller: a200 jack mode active | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a201_low12VBattery` | page 3 | Air suspension controller: a201 low12 v battery | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a210_outOfRangeCalibration` | page 3 | Air suspension controller: a210 out of range calibration | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a211_noRideHeightCalib` | page 3 | Air suspension controller: a211 no ride height calib | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a213_yellowWarningLamp` | page 3 | Air suspension controller: a213 yellow warning lamp | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a214_redWarningLamp` | page 3 | Air suspension controller: a214 red warning lamp | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a215_limpHomeMode10` | page 3 | Air suspension controller: a215 limp home mode10 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a216_limpHomeMode20` | page 3 | Air suspension controller: a216 limp home mode20 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a217_limpHomeMode30` | page 3 | Air suspension controller: a217 limp home mode30 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a218_limpHomeMode40` | page 3 | Air suspension controller: a218 limp home mode40 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a220_exhaustGalleryFault` | page 3 | Air suspension controller: a220 exhaust gallery fault | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a221_valveLeakDetected` | page 3 | Air suspension controller: a221 valve leak detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a222_compressorPrefillFault` | page 3 | Air suspension controller: a222 compressor prefill fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a223_blockedAirline` | page 3 | Air suspension controller: a223 blocked airline | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a224_openAirline` | page 3 | Air suspension controller: a224 open airline | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a225_galleryPressureTooHigh` | page 3 | Air suspension controller: a225 gallery pressure too high | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a226_PWMfastDetectFL` | page 3 | Air suspension controller: a226 PW mfast detect FL | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a227_PWMfastDetectFR` | page 3 | Air suspension controller: a227 PW mfast detect FR | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a228_PWMfastDetectRL` | page 3 | Air suspension controller: a228 PW mfast detect RL | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a229_PWMfastDetectRR` | page 3 | Air suspension controller: a229 PW mfast detect RR | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a230_notifyGeofence` | page 3 | Air suspension controller: a230 notify geofence | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a231_notifyRoughRoadRaise` | page 3 | Air suspension controller: a231 notify rough road raise | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a232_suspensionTypeMismatch` | page 3 | Air suspension controller: a232 suspension type mismatch | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a233_compressorStuckOn` | page 3 | Air suspension controller: a233 compressor stuck on | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a234_damperHydraulicMismatch` | page 3 | Air suspension controller: a234 damper hydraulic mismatch | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a240_airSpringLeak` | page 3 | Air suspension controller: a240 air spring leak | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a284_serviceRunModeActive` | page 4 | Air suspension controller: a284 service run mode active | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a285_twistSustainedUserVis` | page 4 | Air suspension controller: a285 twist sustained user vis | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a286_driveCycleStats1` | page 4 | Air suspension controller: a286 drive cycle stats1 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a287_driveCycleStats2` | page 4 | Air suspension controller: a287 drive cycle stats2 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a288_driveCycleStats3` | page 4 | Air suspension controller: a288 drive cycle stats3 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a289_driveCycleStats4` | page 4 | Air suspension controller: a289 drive cycle stats4 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a290_twistSustainedAtSpeed` | page 4 | Air suspension controller: a290 twist sustained at speed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a291_frontAxleTooHigh` | page 4 | Air suspension controller: a291 front axle too high | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a292_rearAxleTooHigh` | page 4 | Air suspension controller: a292 rear axle too high | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a293_frontAxleTooLow` | page 4 | Air suspension controller: a293 front axle too low | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a294_rearAxleTooLow` | page 4 | Air suspension controller: a294 rear axle too low | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a295_targetHeightNotMet` | page 4 | Air suspension controller: a295 target height not met | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a296_chassisTypeMismatch` | page 4 | Air suspension controller: a296 chassis type mismatch | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a297_vinMismatch` | page 4 | Air suspension controller: a297 vin mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a298_vinNotLearned` | page 4 | Air suspension controller: a298 vin not learned | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a299_offsetEstimateTooLarge` | page 4 | Air suspension controller: a299 offset estimate too large | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a300_offsetEstimateData1` | page 4 | Air suspension controller: a300 offset estimate data1 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a301_offsetEstimateData2` | page 5 | Air suspension controller: a301 offset estimate data2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a303_massEstimateFrozen` | page 5 | Air suspension controller: a303 mass estimate frozen | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a304_massEstimateFrozenData` | page 5 | Air suspension controller: a304 mass estimate frozen data | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a305_newEndstopPosition` | page 5 | Air suspension controller: a305 new endstop position | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a306_hardwareProtectFrozen` | page 5 | Air suspension controller: a306 hardware protect frozen | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a307_endstopBoundaryComp` | page 5 | Air suspension controller: a307 endstop boundary comp | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a308_endstopBoundaryRbnd` | page 5 | Air suspension controller: a308 endstop boundary rbnd | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a309_controlFrozen` | page 5 | Air suspension controller: a309 control frozen | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a310_controlFrozenData` | page 5 | Air suspension controller: a310 control frozen data | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a311_accelsMIA` | page 5 | Air suspension controller: a311 accels MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a312_rotationalRatesMIA` | page 5 | Air suspension controller: a312 rotational rates MIA | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a313_dampingCntrlDisabled` | page 5 | Air suspension controller: a313 damping cntrl disabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a314_dampingReduced` | page 5 | Air suspension controller: a314 damping reduced | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a315_pcbaHighTemp` | page 5 | Air suspension controller: a315 pcba high temp | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a316_offsetsAccels` | page 5 | Air suspension controller: a316 offsets accels | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a317_offsetsRotationalRates` | page 5 | Air suspension controller: a317 offsets rotational rates | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a318_dampingCntrlInputMIA` | page 5 | Air suspension controller: a318 damping cntrl input MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a319_drivetrainTypeMismatch` | page 5 | Air suspension controller: a319 drivetrain type mismatch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a320_offsetsRotationalRates` | page 5 | Air suspension controller: a320 offsets rotational rates | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a321_speedBumpAttributes1` | page 5 | Air suspension controller: a321 speed bump attributes1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a322_speedBumpAttributes2` | page 5 | Air suspension controller: a322 speed bump attributes2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a332_levelingThresholds1` | page 5 | Air suspension controller: a332 leveling thresholds1 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_a333_levelingThresholds2` | page 5 | Air suspension controller: a333 leveling thresholds2 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`TAS_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (27 signals), page 1 (34 signals), page 2 (25 signals), page 3 (34 signals), page 4 (17 signals), page 5 (23 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
