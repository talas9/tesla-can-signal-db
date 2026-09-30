---
layout: default
title: "CP_alertMatrix (0x31E) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: alert matrix. Tesla Model Y CAN bus message CP_alertMatrix (0x31E) of Charge port controller, firmware 2026.26.6.5, 218 signals (CP_matrixIndex, CP_a001_canRx, CP_a002_canTx, CP_a003_canError and 214 more). Bit layout, scaling, units and value tables."
---

# CP_alertMatrix (0x31E) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN

Charge port controller message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 218 signals of CP_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_alertMatrix` |
| CAN id | 0x31E (798) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 218 |

## Signals of CP_alertMatrix

Tesla Model Y CAN bus signals in `CP_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_matrixIndex` | selector | Charge port controller: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3` | plausible |
| `CP_a001_canRx` | page 0 | Charge port controller: a001 can rx | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a002_canTx` | page 0 | Charge port controller: a002 can tx | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a003_canError` | page 0 | Charge port controller: a003 can error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a004_proximityRationality` | page 0 | Charge port controller: a004 proximity rationality | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a005_gbdcLiveDisconnect` | page 0 | Charge port controller: a005 gbdc live disconnect | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a006_lostCommsBMS` | page 0 | Charge port controller: a006 lost comms BMS | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a007_watchdog` | page 0 | Charge port controller: a007 watchdog | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a008_memoryError` | page 0 | Charge port controller: a008 memory error | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a009_coverOpenAllChgBlocked` | page 0 | Charge port controller: a009 cover open all chg blocked | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a010_pilotRationality` | page 0 | Charge port controller: a010 pilot rationality | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a011_eeprom` | page 0 | Charge port controller: a011 eeprom | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a012_ledDriver` | page 0 | Charge port controller: a012 led driver | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a013_lostCommsGTW` | page 0 | Charge port controller: a013 lost comms GTW | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a014_lostCommsCHG` | page 0 | Charge port controller: a014 lost comms CHG | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a015_apsVov` | page 0 | Charge port controller: a015 aps vov | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a016_apsVuv` | page 0 | Charge port controller: a016 aps vuv | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a017_fiveVov` | page 0 | Charge port controller: a017 five vov | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a018_fiveVuv` | page 0 | Charge port controller: a018 five vuv | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a019_threeVov` | page 0 | Charge port controller: a019 three vov | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a020_threeVuv` | page 0 | Charge port controller: a020 three vuv | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a021_zeroVov` | page 0 | Charge port controller: a021 zero vov | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a022_zeroVuv` | page 0 | Charge port controller: a022 zero vuv | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a023_gbdcSessionFailed` | page 0 | Charge port controller: a023 gbdc session failed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a024_ledsUC` | page 0 | Charge port controller: a024 leds UC | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a025_ledsOC` | page 0 | Charge port controller: a025 leds OC | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a026_networkManagement` | page 0 | Charge port controller: a026 network management | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a027_doorSensorOutOfSpec` | page 0 | Charge port controller: a027 door sensor out of spec | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a028_insertEnableMismatch` | page 0 | Charge port controller: a028 insert enable mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a029_doorClosedProxPilot` | page 0 | Charge port controller: a029 door closed prox pilot | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a030_busOff` | page 0 | Charge port controller: a030 bus off | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a031_doorClosedCommandedOpen` | page 0 | Charge port controller: a031 door closed commanded open | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a032_doorOpenExpectedClosed` | page 0 | Charge port controller: a032 door open expected closed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a033_spiOpen` | page 0 | Charge port controller: a033 spi open | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a034_calibrationIncomplete` | page 0 | Charge port controller: a034 calibration incomplete | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a035_latchMovement_1` | page 0 | Charge port controller: a035 latch movement 1 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a036_latchNotDisengaged` | page 0 | Charge port controller: a036 latch not disengaged | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a037_latchNotEngaged` | page 0 | Charge port controller: a037 latch not engaged | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a038_latchNotBlocking` | page 0 | Charge port controller: a038 latch not blocking | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a039_latchMovement_2` | page 0 | Charge port controller: a039 latch movement 2 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a040_doNotUse` | page 0 | Charge port controller: a040 do not use | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a041_doorSensorUnplugged` | page 0 | Charge port controller: a041 door sensor unplugged | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a042_doorAssemblyBroken` | page 0 | Charge port controller: a042 door assembly broken | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a043_doorPotIrrational` | page 0 | Charge port controller: a043 door pot irrational | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a044_lostCommsHVP` | page 0 | Charge port controller: a044 lost comms HVP | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a045_lostCommsVCSEC` | page 0 | Charge port controller: a045 lost comms VCSEC | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a046_lostCommsEVSE` | page 0 | Charge port controller: a046 lost comms EVSE | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a047_lostCommsVCFRONT` | page 0 | Charge port controller: a047 lost comms VCFRONT | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a048_lostCommsUI` | page 0 | Charge port controller: a048 lost comms UI | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a049_multipleCablesDetected` | page 0 | Charge port controller: a049 multiple cables detected | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a050_latchNotConnected` | page 0 | Charge port controller: a050 latch not connected | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a051_doorInductiveSensorMIA` | page 0 | Charge port controller: a051 door inductive sensor MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a052_chademoNotSupported` | page 0 | Charge port controller: a052 chademo not supported | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a053_proxLatchedNoPilot` | page 0 | Charge port controller: a053 prox latched no pilot | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a054_cableNotSecured` | page 0 | Charge port controller: a054 cable not secured | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a055_chargeStoppedNoPilot` | page 0 | Charge port controller: a055 charge stopped no pilot | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a056_proxDisconnected` | page 0 | Charge port controller: a056 prox disconnected | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a057_ccs1AdapterBtnPress` | page 0 | Charge port controller: a057 ccs1 adapter btn press | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a058_acChargeRetryPending` | page 0 | Charge port controller: a058 ac charge retry pending | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a059_swcanError` | page 0 | Charge port controller: a059 swcan error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a060_lostCommsPCS` | page 0 | Charge port controller: a060 lost comms PCS | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a061_uhfReceiverMIA` | page 1 | Charge port controller: a061 uhf receiver MIA | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a062_scOutOfService` | page 1 | Charge port controller: a062 sc out of service | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a063_scUpdateInProgress` | page 1 | Charge port controller: a063 sc update in progress | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a064_superchargingBlocked` | page 1 | Charge port controller: a064 supercharging blocked | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a065_selfTestFailed` | page 1 | Charge port controller: a065 self test failed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a066_proxLatchedIdlePilot` | page 1 | Charge port controller: a066 prox latched idle pilot | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a067_gbdcConnFault` | page 1 | Charge port controller: a067 gbdc conn fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a068_doorSensorMismatch` | page 1 | Charge port controller: a068 door sensor mismatch | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a069_doorInductiveSensorError` | page 1 | Charge port controller: a069 door inductive sensor error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a070_doorInductiveSensorReset` | page 1 | Charge port controller: a070 door inductive sensor reset | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a071_exiDecodeFailure` | page 1 | Charge port controller: a071 exi decode failure | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a072_v2gEvccTimeout` | page 1 | Charge port controller: a072 v2g evcc timeout | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a073_iecComboShutdown` | page 1 | Charge port controller: a073 iec combo shutdown | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a074_failedToEstablishV2gComm` | page 1 | Charge port controller: a074 failed to establish v2g comm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a075_v2gCommsFailure` | page 1 | Charge port controller: a075 v2g comms failure | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a076_LDC1612errorWatchdog` | page 1 | Charge port controller: a076 ldc1612error watchdog | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a077_invalidMacAddress` | page 1 | Charge port controller: a077 invalid mac address | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a078_latchNotDisengagedCold` | page 1 | Charge port controller: a078 latch not disengaged cold | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a079_cableNotSecuredCold` | page 1 | Charge port controller: a079 cable not secured cold | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a080_taskStackOverflow` | page 1 | Charge port controller: a080 task stack overflow | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a081_swException` | page 1 | Charge port controller: a081 sw exception | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a082_powerOnReset` | page 1 | Charge port controller: a082 power on reset | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a083_watchdogTraceData` | page 1 | Charge port controller: a083 watchdog trace data | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a084_proxPeDisconnected_gb` | page 1 | Charge port controller: a084 prox pe disconnected gb | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a085_dcPinTempFaulted` | page 1 | Charge port controller: a085 dc pin temp faulted | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a086_dcPinTempIrrational` | page 1 | Charge port controller: a086 dc pin temp irrational | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a087_dcTempModelFault` | page 1 | Charge port controller: a087 dc temp model fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a088_dcTempModelDeviation` | page 1 | Charge port controller: a088 dc temp model deviation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a089_plcConfigMismatch` | page 1 | Charge port controller: a089 plc config mismatch | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a090_ccsEvseLowIso` | page 1 | Charge port controller: a090 ccs evse low iso | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a091_wrongSuperchargerHandle` | page 1 | Charge port controller: a091 wrong supercharger handle | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a092_modemAppLoadFailed` | page 1 | Charge port controller: a092 modem app load failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a093_modemLoadedWithReset` | page 1 | Charge port controller: a093 modem loaded with reset | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a094_inductiveResetSuccessful` | page 1 | Charge port controller: a094 inductive reset successful | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a095_thermalDcLimitActive` | page 1 | Charge port controller: a095 thermal dc limit active | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a096_pilotWake` | page 1 | Charge port controller: a096 pilot wake | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a097_modeTransitionFailure` | page 1 | Charge port controller: a097 mode transition failure | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a098_proximityWake` | page 1 | Charge port controller: a098 proximity wake | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a099_cableStateUnknown` | page 1 | Charge port controller: a099 cable state unknown | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a100_inletHarnessIdIrrational` | page 1 | Charge port controller: a100 inlet harness id irrational | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a101_wcFoldbackActive` | page 1 | Charge port controller: a101 wc foldback active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a102_wcOvertempFault` | page 1 | Charge port controller: a102 wc overtemp fault | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a103_proximityPeDisconnected` | page 1 | Charge port controller: a103 proximity pe disconnected | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a104_uhfResetSuccessful` | page 1 | Charge port controller: a104 uhf reset successful | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a105_hwUnableToSleep` | page 1 | Charge port controller: a105 hw unable to sleep | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a106_uhfReceiverReset` | page 1 | Charge port controller: a106 uhf receiver reset | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a107_chademoFoldbackActive` | page 1 | Charge port controller: a107 chademo foldback active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a108_chademoOvertempFault` | page 1 | Charge port controller: a108 chademo overtemp fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a109_thermistorIrrational` | page 1 | Charge port controller: a109 thermistor irrational | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a110_thermalVelocityHigh` | page 1 | Charge port controller: a110 thermal velocity high | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a111_inletHeaterUnableToHeat` | page 1 | Charge port controller: a111 inlet heater unable to heat | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a112_inletHeaterIrrationalTemperature` | page 1 | Charge port controller: a112 inlet heater irrational temperature | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a113_inletHeaterShortCircuit` | page 1 | Charge port controller: a113 inlet heater short circuit | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a114_ccsEvseFailed` | page 1 | Charge port controller: a114 ccs evse failed | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a115_unexpectedTcan1145State` | page 1 | Charge port controller: a115 unexpected tcan1145 state | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a116_misconfigurationDetected` | page 1 | Charge port controller: a116 misconfiguration detected | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a117_inletHeaterUnableToRegulate` | page 1 | Charge port controller: a117 inlet heater unable to regulate | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a118_iecComboLockUp` | page 1 | Charge port controller: a118 iec combo lock up | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a119_plcTransmitFailure` | page 1 | Charge port controller: a119 plc transmit failure | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a120_comboAdapterFoldback` | page 1 | Charge port controller: a120 combo adapter foldback | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a121_PLCRLY_lostCommsCP` | page 2 | Charge port controller: a121 PLCRLY lost comms CP | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a122_plcModemFailure` | page 2 | Charge port controller: a122 plc modem failure | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a123_latchPotIrrational` | page 2 | Charge port controller: a123 latch pot irrational | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a124_ivledFault` | page 2 | Charge port controller: a124 ivled fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a125_unexpectedLVJuiceState` | page 2 | Charge port controller: a125 unexpected LV juice state | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a126_wakeOnUhfFault` | page 2 | Charge port controller: a126 wake on uhf fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a127_lostCommsHVLINK` | page 2 | Charge port controller: a127 lost comms HVLINK | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a128_lostCommsVC` | page 2 | Charge port controller: a128 lost comms VC | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a129_bldcDriverCommsFailed` | page 2 | Charge port controller: a129 bldc driver comms failed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a130_bldcDriverCommsRecovered` | page 2 | Charge port controller: a130 bldc driver comms recovered | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a131_evseCommTimeout` | page 2 | Charge port controller: a131 evse comm timeout | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a132_contractAuthTimeout` | page 2 | Charge port controller: a132 contract auth timeout | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a133_proxNeverLatched` | page 2 | Charge port controller: a133 prox never latched | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a134_plcModemNotExpected` | page 2 | Charge port controller: a134 plc modem not expected | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a135_sdpAttemptsFailed` | page 2 | Charge port controller: a135 sdp attempts failed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a136_sdpSideReqFailed` | page 2 | Charge port controller: a136 sdp side req failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a137_plcForwardError` | page 2 | Charge port controller: a137 plc forward error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a138_swcanCommsAcEvseFaulted` | page 2 | Charge port controller: a138 swcan comms ac evse faulted | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a139_pilotFaulted` | page 2 | Charge port controller: a139 pilot faulted | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a140_superchargerFaulted` | page 2 | Charge port controller: a140 supercharger faulted | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a141_chademoAdapterFault` | page 2 | Charge port controller: a141 chademo adapter fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a142_gbdcScConnFault` | page 2 | Charge port controller: a142 gbdc sc conn fault | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a143_unsupportedChargeAdapter` | page 2 | Charge port controller: a143 unsupported charge adapter | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a144_nvmInitFailed` | page 2 | Charge port controller: a144 nvm init failed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a145_modemAppLoadFailedNA` | page 2 | Charge port controller: a145 modem app load failed NA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a146_ccsEvseMalfunction` | page 2 | Charge port controller: a146 ccs evse malfunction | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a147_inductiveRecoveredMia` | page 2 | Charge port controller: a147 inductive recovered mia | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a148_bldcTachFeedbackMia` | page 2 | Charge port controller: a148 bldc tach feedback mia | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a149_pilotPeriodInvalid` | page 2 | Charge port controller: a149 pilot period invalid | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a150_railToggleTimeout` | page 2 | Charge port controller: a150 rail toggle timeout | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a151_badPilotDiodeDetected` | page 2 | Charge port controller: a151 bad pilot diode detected | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a152_pilotEdgeDetectionFailed` | page 2 | Charge port controller: a152 pilot edge detection failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a153_thermalAcLimitActive` | page 2 | Charge port controller: a153 thermal ac limit active | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a154_acChargingStoppedOT` | page 2 | Charge port controller: a154 ac charging stopped OT | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a155_hallPresenceRationality` | page 2 | Charge port controller: a155 hall presence rationality | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a156_gbdcPrechargingConcern` | page 2 | Charge port controller: a156 gbdc precharging concern | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a157_doorOpenRateLimiter` | page 2 | Charge port controller: a157 door open rate limiter | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a158_doorCloseRateLimiter` | page 2 | Charge port controller: a158 door close rate limiter | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a159_swcanHealthCheckFailed` | page 2 | Charge port controller: a159 swcan health check failed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a160_latchDisengageInDcCharge` | page 2 | Charge port controller: a160 latch disengage in dc charge | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a161_badPilotDiodeDetectedCN` | page 2 | Charge port controller: a161 bad pilot diode detected CN | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a162_pilotEdgeDetectionFailedCN` | page 2 | Charge port controller: a162 pilot edge detection failed CN | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a163_coverOpenDcChgBlocked` | page 2 | Charge port controller: a163 cover open dc chg blocked | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a164_latchRedisengageRequested` | page 2 | Charge port controller: a164 latch redisengage requested | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a165_proxWiggleDetected` | page 2 | Charge port controller: a165 prox wiggle detected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a166_faultLineMismatchDetected` | page 2 | Charge port controller: a166 fault line mismatch detected | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a167_doorIdIrrational` | page 2 | Charge port controller: a167 door id irrational | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a168_pilotHSDFaulted` | page 2 | Charge port controller: a168 pilot HSD faulted | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a170_selfTestFailed2` | page 2 | Charge port controller: a170 self test failed2 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a172_triggerOdin` | page 2 | Signal reported by Charge port controller | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a173_coverOpenAcChgBlocked` | page 2 | Charge port controller: a173 cover open ac chg blocked | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a174_fwdedMsgLoadWarning` | page 2 | Charge port controller: a174 fwded msg load warning | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a175_fwdedMsgDropped` | page 2 | Charge port controller: a175 fwded msg dropped | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a176_lostCommsV2l` | page 2 | Charge port controller: a176 lost comms v2l | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a177_incompatibleV2lDeviceDetected` | page 2 | Charge port controller: a177 incompatible v2l device detected | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a178_v2xPlcCommsFault` | page 2 | Charge port controller: a178 v2x plc comms fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a179_evseCommsTlsError` | page 2 | Charge port controller: a179 evse comms tls error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a182_pncdCommsError` | page 3 | Charge port controller: a182 pncd comms error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a183_certManagerError` | page 3 | Charge port controller: a183 cert manager error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a184_certChangeEvent` | page 3 | Charge port controller: a184 cert change event | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a185_pncAuthRejection` | page 3 | Charge port controller: a185 pnc auth rejection | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a186_spiDmaFailure` | page 3 | Charge port controller: a186 spi dma failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a187_highStackUsage` | page 3 | Charge port controller: a187 high stack usage | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a188_v2lEvseRequiresUpdate` | page 3 | Charge port controller: a188 v2l evse requires update | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a189_resistivePresenceRationality` | page 3 | Charge port controller: a189 resistive presence rationality | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d190_backCoverCircuitIssue` | page 3 | Charge port controller: d190 back cover circuit issue | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d191_latchConnectionIssue` | page 3 | Charge port controller: d191 latch connection issue | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d192_couplerTempHigh` | page 3 | Charge port controller: d192 coupler temp high | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d193_proximityCircuitErratic` | page 3 | Charge port controller: d193 proximity circuit erratic | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d194_proximityCircuitRangeIssue` | page 3 | Charge port controller: d194 proximity circuit range issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d195_couplerLockActuatorIssue` | page 3 | Charge port controller: d195 coupler lock actuator issue | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d196_doorActuatorPerformanceIssue` | page 3 | Charge port controller: d196 door actuator performance issue | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d197_doorSensorCircuitErratic` | page 3 | Charge port controller: d197 door sensor circuit erratic | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d198_couplerTempSensorCircuitErratic` | page 3 | Charge port controller: d198 coupler temp sensor circuit erratic | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d199_hardwareConfigMismatch` | page 3 | Charge port controller: d199 hardware config mismatch | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_d200_pilotCircuitIssue` | page 3 | Charge port controller: d200 pilot circuit issue | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a201_uhfDoorOpenRepeatedlyOverLimit` | page 3 | Charge port controller: a201 uhf door open repeatedly over limit | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a202_failedToEstablishV2gComm2` | page 3 | Charge port controller: a202 failed to establish v2g comm2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a203_evseCommTimeout2` | page 3 | Charge port controller: a203 evse comm timeout2 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a204_sdpAttemptsFailed2` | page 3 | Charge port controller: a204 sdp attempts failed2 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a205_doorPositionUndetectable` | page 3 | Charge port controller: a205 door position undetectable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a206_peToChassisDisconnected` | page 3 | Charge port controller: a206 pe to chassis disconnected | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a207_v2xAuthenticationFailed` | page 3 | Charge port controller: a207 v2x authentication failed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a208_eipmCommsError` | page 3 | Charge port controller: a208 eipm comms error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a209_macphyFault` | page 3 | Charge port controller: a209 macphy fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a210_lostCommsPCSR` | page 3 | Charge port controller: a210 lost comms PCSR | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a211_lostCommsPCSL` | page 3 | Charge port controller: a211 lost comms PCSL | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a212_mcsPacketDrops` | page 3 | Charge port controller: a212 mcs packet drops | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a213_mcsTcpRetransmitStorm` | page 3 | Charge port controller: a213 mcs tcp retransmit storm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a214_mcsEthDriverRetransmitFail` | page 3 | Charge port controller: a214 mcs eth driver retransmit fail | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a215_mcsMacPhyErrors` | page 3 | Charge port controller: a215 mcs mac phy errors | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a216_mcsLinkLoss` | page 3 | Charge port controller: a216 mcs link loss | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a217_teslaV2gCommsFailure` | page 3 | Charge port controller: a217 tesla v2g comms failure | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a218_v2gCommsFailure2` | page 3 | Charge port controller: a218 v2g comms failure2 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a219_doorOpenInDrive` | page 3 | Charge port controller: a219 door open in drive | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a220_mcsChargingInterrupted` | page 3 | Charge port controller: a220 mcs charging interrupted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CP_a221_evseStartupTimeout` | page 3 | Charge port controller: a221 evse startup timeout | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`CP_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (57 signals), page 3 (40 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
