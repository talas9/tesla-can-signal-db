---
layout: default
title: "PMF_alertLog (0x525) — PMF ECU, Tesla Model Y 2025.20.8 ETH"
description: "PMF ECU message: alert log. Ethernet-side message PMF_alertLog of PMF ECU for Tesla Model Y firmware 2025.20.8, 189 signals (PMF_alertID, PMF_alertState, PMF_a001_w0, PMF_a001_w1 and 185 more). Bit layout, scaling, units and value tables."
---

# PMF_alertLog (0x525) — PMF ECU, Tesla Model Y 2025.20.8 ETH

PMF ECU message: alert log. This page documents the 189 signals of PMF_alertLog as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_alertLog` |
| Ethernet-side id | 0x525 (1317) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 189 |

## Signals of PMF_alertLog

Tesla Model Y CAN bus signals in `PMF_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_alertID` | selector | PMF ECU: alert ID | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_absoluteTorque`<br>2 = `a002_excessiveAccelTorque`<br>3 = `a003_excessiveReversalTorque`<br>4 = `a004_excessiveDecelTorque`<br>5 = `a005_torqueInNeutralOrPark`<br>6 = `a006_underTorqueCheck`<br>8 = `a008_memoryError`<br>10 = `a010_diMIA`<br>11 = `a011_phaseCurrentIrrational`<br>12 = `a012_canDataBusA`<br>13 = `a013_canHardwareBusA`<br>17 = `a017_brakeMIA`<br>18 = `a018_encoderIrrational`<br>19 = `a019_statorTempIrrational`<br>25 = `a025_unintendedReset`<br>26 = `a026_diHeartBeatMIA`<br>27 = `a027_torqueEstimationOutOfBounds`<br>28 = `a028_torqueCmdError`<br>31 = `a031_highStackUsage`<br>32 = `a032_registerConfigError`<br>33 = `a033_selfTest`<br>34 = `a034_trqCrossCheck`<br>35 = `a035_udsTransactionInitiated`<br>36 = `a036_preWatchdog`<br>37 = `a037_hvpMIA`<br>39 = `a039_disMIA`<br>40 = `a040_pmMIA`<br>42 = `a042_gtwMIA`<br>45 = `a045_motorMovementDetected`<br>53 = `a053_vcfrontMIA`<br>54 = `a054_uiMIA`<br>55 = `a055_resolver`<br>56 = `a056_canHardwareBusB`<br>57 = `a057_canDataBusB`<br>58 = `a058_measuredHvilCurrentFrozen`<br>61 = `a061_DIPMVersionMismatch`<br>62 = `a062_eccError`<br>64 = `a064_torqueIntervention`<br>80 = `a080_exceptionPrefetchAbort`<br>81 = `a081_exceptionDataAbort`<br>82 = `a082_exceptionDataAbort2`<br>83 = `a083_ahbWriteError`<br>84 = `a084_exceptionMpuFirewall`<br>86 = `a086_exceptionUndefinedInstruction`<br>92 = `a092_xtalOscillator`<br>94 = `a094_safetyICWarn`<br>95 = `a095_safetyICFault`<br>96 = `a096_safetyICDebug`<br>97 = `a097_lowFlowAlmostTripped`<br>100 = `a100_diTraceInfo1`<br>121 = `a121_unintendedReset2` | plausible |
| `PMF_alertState` |  | PMF ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `PMF_a001_w0` | page 1 | PMF ECU: a001 w0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a001_w1` | page 1 | PMF ECU: a001 w1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a001_w2` | page 1 | PMF ECU: a001 w2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a002_torqueAverage` | page 2 | PMF ECU: a002 torque average | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a002_torqueWindow` | page 2 | PMF ECU: a002 torque window | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a002_torqueMeasured` | page 2 | PMF ECU: a002 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a002_torqueAccelAverage` | page 2 | PMF ECU: a002 torque accel average; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a002_torqueAccelWindow` | page 2 | PMF ECU: a002 torque accel window; raw 4096 = signal not available (SNA) | 48\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a003_reverseGear` | page 3 | PMF ECU: a003 reverse gear | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a003_pedalPos` | page 3 | PMF ECU: a003 pedal pos | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `PMF_a003_zeroPointPedal` | page 3 | PMF ECU: a003 zero point pedal | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `PMF_a004_torqueAverage` | page 4 | PMF ECU: a004 torque average | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a004_torqueWindow` | page 4 | PMF ECU: a004 torque window | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a004_torqueMeasured` | page 4 | PMF ECU: a004 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a004_torqueDecelAverage` | page 4 | PMF ECU: a004 torque decel average; raw 4096 = signal not available (SNA) | 32\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a004_torqueDecelWindow` | page 4 | PMF ECU: a004 torque decel window; raw 4096 = signal not available (SNA) | 48\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a005_torqueReason` | page 5 | PMF ECU: a005 torque reason | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TORQUE_IN_NEUTRAL`<br>1 = `CURRENT_IN_NEUTRAL`<br>2 = `SLAVE_ENABLE_IN_NEUTRAL` | plausible |
| `PMF_a005_torqueMeasured` | page 5 | PMF ECU: a005 torque measured; raw 4096 = signal not available (SNA) | 18\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a005_iDQmagnitude` | page 5 | PMF ECU: a005 i d qmagnitude | 32\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PMF_a006_torqueActual` | page 6 | PMF ECU: a006 torque actual; raw 4096 = signal not available (SNA) | 16\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a006_motorRPM` | page 6 | PMF ECU: a006 motor RPM | 32\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `PMF_a006_torqueMeasured` | page 6 | PMF ECU: a006 torque measured; raw 4096 = signal not available (SNA) | 48\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PMF_a010_messageId` | page 10 | PMF ECU: a010 message id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a010_DI_status` | page 10 | PMF ECU: a010 DI status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_torque` | page 10 | PMF ECU: a010 DI torque | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_slaveCommand` | page 10 | PMF ECU: a010 DI slave command | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_locStatus` | page 10 | PMF ECU: a010 DI loc status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_speed` | page 10 | PMF ECU: a010 DI speed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_systemStatus` | page 10 | PMF ECU: a010 DI system status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_chassisControl` | page 10 | PMF ECU: a010 DI chassis control | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_chassisControl2` | page 10 | PMF ECU: a010 DI chassis control2 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_vdcLeft` | page 10 | PMF ECU: a010 vdc left | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_vdcRight` | page 10 | PMF ECU: a010 vdc right | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_vehicleEstimates` | page 10 | PMF ECU: a010 DI vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_brakeCommand` | page 10 | PMF ECU: a010 DI brake command | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_difCommand` | page 10 | PMF ECU: a010 DI dif command | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_dirCommand` | page 10 | PMF ECU: a010 DI dir command | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_dirVehicle` | page 10 | PMF ECU: a010 DI dir vehicle | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a010_DI_locStatus2` | page 10 | PMF ECU: a010 DI loc status2 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a011_Ia` | page 11 | PMF ECU: a011 ia | 16\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PMF_a011_Ib` | page 11 | PMF ECU: a011 ib | 32\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PMF_a011_currentVref` | page 11 | PMF ECU: a011 current vref | 48\|11 | little-endian | unsigned | 0.005 | 0 | V | 0 to 10.235 |  | plausible |
| `PMF_a011_badPhaseAsample` | page 11 | PMF ECU: a011 bad phase asample | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a011_badPhaseBsample` | page 11 | PMF ECU: a011 bad phase bsample | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a011_sampleFreeze` | page 11 | PMF ECU: a011 sample freeze | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a012_canID` | page 12 | PMF ECU: a012 can ID | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PMF_a012_errorType` | page 12 | PMF ECU: a012 error type | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH_SHORT`<br>2 = `LENGTH_LONG`<br>3 = `CHECKSUM`<br>4 = `SEQUENCE`<br>5 = `DATA_INVALID`<br>6 = `UNKNOWN_ID` | plausible |
| `PMF_a012_badValue1` | page 12 | PMF ECU: a012 bad value1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a012_badValue2` | page 12 | PMF ECU: a012 bad value2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a013_mailboxID` | page 13 | PMF ECU: a013 mailbox ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a013_canID` | page 13 | PMF ECU: a013 can ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a013_errorType` | page 13 | PMF ECU: a013 error type | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RX`<br>1 = `TX`<br>2 = `RX_OVERRUN`<br>3 = `TX_OVERRUN`<br>4 = `IPC_RX_OVERRUN`<br>5 = `IPC_TX_OVERRUN` | plausible |
| `PMF_a017_EPBL_status` | page 17 | PMF ECU: a017 EPBL status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a017_EPBR_status` | page 17 | PMF ECU: a017 EPBR status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a018_w0` | page 18 | PMF ECU: a018 w0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a018_w1` | page 18 | PMF ECU: a018 w1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a018_w2` | page 18 | PMF ECU: a018 w2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a019_statorTemp1` | page 19 | PMF ECU: a019 stator temp1 | 16\|16 | little-endian | signed | 0.1 | 0 | DegC | -3276.8 to 3276.7 |  | plausible |
| `PMF_a019_statorTslope1` | page 19 | PMF ECU: a019 stator tslope1 | 32\|16 | little-endian | signed | 0.1 | 0 | DegC/s | -3276.8 to 3276.7 |  | plausible |
| `PMF_a025_sccReset` | page 25 | PMF ECU: a025 scc reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_hibernate` | page 25 | PMF ECU: a025 hibernate | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_hwBist` | page 25 | PMF ECU: a025 hw bist | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_nmiWatchdog` | page 25 | PMF ECU: a025 nmi watchdog | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_watchdog` | page 25 | PMF ECU: a025 watchdog | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_clockFailNmi` | page 25 | PMF ECU: a025 clock fail nmi | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_ramUncErrorNmi` | page 25 | PMF ECU: a025 ram unc error nmi | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_flashUncErrorNmi` | page 25 | PMF ECU: a025 flash unc error nmi | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_cpu1signMismatchNmi` | page 25 | PMF ECU: a025 cpu1sign mismatch nmi | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_cpu2signMismatchNmi` | page 25 | PMF ECU: a025 cpu2sign mismatch nmi | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_pieVectErrorNmi` | page 25 | PMF ECU: a025 pie vect error nmi | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_sysDbgNmi` | page 25 | PMF ECU: a025 sys dbg nmi | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_rlNmi` | page 25 | PMF ECU: a025 rl nmi | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_ovfNmi` | page 25 | PMF ECU: a025 ovf nmi | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_possibleSafetyICReset` | page 25 | PMF ECU: a025 possible safety IC reset | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_powerOnReset` | page 25 | PMF ECU: a025 power on reset | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_watchdogTimer0` | page 25 | PMF ECU: a025 watchdog timer0 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_watchdogTimer1` | page 25 | PMF ECU: a025 watchdog timer1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_watchdogTimer2` | page 25 | PMF ECU: a025 watchdog timer2 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_watchdogTimer3` | page 25 | PMF ECU: a025 watchdog timer3 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_warmResetReq` | page 25 | PMF ECU: a025 warm reset req | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_externalPadReset` | page 25 | PMF ECU: a025 external pad reset | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_hwSecModuleWatchdogTimer` | page 25 | PMF ECU: a025 hw sec module watchdog timer | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_debugReset` | page 25 | PMF ECU: a025 debug reset | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_tempSense0` | page 25 | PMF ECU: a025 temp sense0 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a025_tempSense1` | page 25 | PMF ECU: a025 temp sense1 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_reason` | page 26 | PMF ECU: a026 reason | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TooSlow`<br>1 = `TooFast` | plausible |
| `PMF_a026_isrCount20kHz` | page 26 | PMF ECU: a026 isr count20k hz | 17\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `PMF_a026_isrCount1kHz` | page 26 | PMF ECU: a026 isr count1k hz | 22\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PMF_a026_switchingActive` | page 26 | PMF ECU: a026 switching active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_systemStackOvf` | page 26 | PMF ECU: a026 system stack ovf | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_controlStackOvf` | page 26 | PMF ECU: a026 control stack ovf | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_idleStackOvf` | page 26 | PMF ECU: a026 idle stack ovf | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_eepStackOvf` | page 26 | PMF ECU: a026 eep stack ovf | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_immStackOvf` | page 26 | PMF ECU: a026 imm stack ovf | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a026_xdcErrorIdMSW` | page 26 | PMF ECU: a026 xdc error id MSW | 32\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `PMF_a026_xdcErrorArg1` | page 26 | PMF ECU: a026 xdc error arg1 | 42\|22 | little-endian | signed | 1 | 0 |  | -2097152 to 2097151 |  | layout-only |
| `PMF_a032_w0` | page 32 | PMF ECU: a032 w0 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a032_w1` | page 32 | PMF ECU: a032 w1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a032_w2` | page 32 | PMF ECU: a032 w2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a033_state` | page 33 | PMF ECU: a033 state | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `INIT`<br>1 = `PSTG_BRING_UP`<br>2 = `PSTG_BRING_UP_AT_SPEED`<br>3 = `ASC_TEST`<br>4 = `ASC_TEST_PASSED`<br>5 = `PWM_ENABLE`<br>6 = `CURRENT_TEST_POS`<br>7 = `CURRENT_TEST_NEG`<br>8 = `TEST_PRE_PASSED`<br>9 = `TEST_PASSED`<br>10 = `TEST_SKIPPED`<br>11 = `TEST_FAILED`<br>12 = `TEST_RESTART` | plausible |
| `PMF_a033_failReason` | page 33 | PMF ECU: a033 fail reason | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CACHED`<br>1 = `POS_CURRENT`<br>2 = `NEG_CURRENT`<br>3 = `DISAGREE`<br>4 = `TIMEDOUT`<br>5 = `GATE_DRIVE_ERROR`<br>6 = `FAULT_PRESENT`<br>7 = `ASC_TEST` | plausible |
| `PMF_a033_DSADC_Ia` | page 33 | PMF ECU: a033 DSADC ia | 24\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PMF_a033_DSADC_Ib` | page 33 | PMF ECU: a033 DSADC ib | 40\|16 | little-endian | signed | 0.0939 | 0 | A | -3076.9152 to 3076.8213 |  | plausible |
| `PMF_a036_timeSinceTxHWI` | page 36 | PMF ECU: a036 time since tx HWI | 16\|6 | little-endian | unsigned | 64 | 0 | us | 0 to 4032 |  | plausible |
| `PMF_a036_timeSinceRxHWI` | page 36 | PMF ECU: a036 time since rx HWI | 22\|6 | little-endian | unsigned | 64 | 0 | us | 0 to 4032 |  | plausible |
| `PMF_a036_timeSince100HzTxSWI` | page 36 | PMF ECU: a036 time since100 hz tx SWI | 28\|6 | little-endian | unsigned | 0.32 | 0 | ms | 0 to 20.16 |  | plausible |
| `PMF_a036_timeSince1kHzCLK` | page 36 | PMF ECU: a036 time since1k hz CLK | 34\|6 | little-endian | unsigned | 32 | 0 | us | 0 to 2016 |  | plausible |
| `PMF_a036_timeSince1kHzSWI` | page 36 | PMF ECU: a036 time since1k hz SWI | 40\|6 | little-endian | unsigned | 32 | 0 | us | 0 to 2016 |  | plausible |
| `PMF_a036_timeSinceIdle` | page 36 | PMF ECU: a036 time since idle | 46\|6 | little-endian | unsigned | 0.16 | 0 | ms | 0 to 10.08 |  | plausible |
| `PMF_a036_ovfStackId` | page 36 | PMF ECU: a036 ovf stack id; raw 15 = signal not available (SNA) | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 15 = `SNA` | plausible |
| `PMF_a036_inTxISR` | page 36 | PMF ECU: a036 in tx ISR | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_inTxHWI` | page 36 | PMF ECU: a036 in tx HWI | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_inRxHWI` | page 36 | PMF ECU: a036 in rx HWI | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_in1kHzSWI` | page 36 | PMF ECU: a036 in1k hz SWI | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_in1kHzCLK` | page 36 | PMF ECU: a036 in1k hz CLK | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_in100HzCLK` | page 36 | PMF ECU: a036 in100 hz CLK | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_in10HzCLK` | page 36 | PMF ECU: a036 in10 hz CLK | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a036_in1HzCLK` | page 36 | PMF ECU: a036 in1 hz CLK | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a037_hvpFaults` | page 37 | PMF ECU: a037 hvp faults | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a039_DIS_status` | page 39 | PMF ECU: a039 DIS status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a039_DIS_torque` | page 39 | PMF ECU: a039 DIS torque | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a039_messageId` | page 39 | PMF ECU: a039 message id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a040_PM_state` | page 40 | PMF ECU: a040 PM state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a040_messageId` | page 40 | PMF ECU: a040 message id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a040_PM_locState` | page 40 | PMF ECU: a040 PM loc state | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a042_GTW_carConfig` | page 42 | PMF ECU: a042 GTW car config | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a042_GTW_time` | page 42 | PMF ECU: a042 GTW time | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a042_GTW_drivetrainType` | page 42 | PMF ECU: a042 GTW drivetrain type | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RWD`<br>1 = `AWD` | plausible |
| `PMF_a042_expectedPerformanceCfg` | page 42 | PMF ECU: a042 expected performance cfg | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RWD`<br>1 = `AWD` | plausible |
| `PMF_a042_gearControl` | page 42 | PMF ECU: a042 gear control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_LVPowerState` | page 53 | PMF ECU: a053 LV power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_coolant` | page 53 | PMF ECU: a053 coolant | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_vcleftSwitchStatus` | page 53 | PMF ECU: a053 vcleft switch status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_restraintStatus` | page 53 | PMF ECU: a053 restraint status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a053_sensors` | page 53 | PMF ECU: a053 sensors | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiPowertrainControl` | page 54 | PMF ECU: a054 ui powertrain control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiChassisControl` | page 54 | PMF ECU: a054 ui chassis control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiCruiseControl` | page 54 | PMF ECU: a054 ui cruise control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiTrackModeSettings` | page 54 | PMF ECU: a054 ui track mode settings | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a054_uiTPMSRCPSetting` | page 54 | PMF ECU: a054 ui TPMSRCP setting | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_motorRPM` | page 55 | PMF ECU: a055 motor RPM | 16\|16 | little-endian | signed | 1 | 0 | RPM | -32768 to 32767 |  | plausible |
| `PMF_a055_phaseAngle` | page 55 | PMF ECU: a055 phase angle | 32\|8 | little-endian | unsigned | 0.00308 | 0 | 1 | 0 to 0.7854 |  | plausible |
| `PMF_a055_commonGain` | page 55 | PMF ECU: a055 common gain | 40\|8 | little-endian | unsigned | 0.02 | 0 | 1 | 0 to 5.1 |  | plausible |
| `PMF_a055_notReady` | page 55 | PMF ECU: a055 not ready | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_noCarrier` | page 55 | PMF ECU: a055 no carrier | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_phaseOutOfSpec` | page 55 | PMF ECU: a055 phase out of spec | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_diElecAngleMismatch` | page 55 | PMF ECU: a055 di elec angle mismatch | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_diSpeedMismatch` | page 55 | PMF ECU: a055 di speed mismatch | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_claMIA` | page 55 | PMF ECU: a055 cla MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_diMIA` | page 55 | PMF ECU: a055 di MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a055_diElecAngleMismatchWarn` | page 55 | PMF ECU: a055 di elec angle mismatch warn | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a056_mailboxID` | page 56 | PMF ECU: a056 mailbox ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a056_canID` | page 56 | PMF ECU: a056 can ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a056_errorType` | page 56 | PMF ECU: a056 error type | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RX`<br>1 = `TX`<br>2 = `RX_OVERRUN`<br>3 = `TX_OVERRUN`<br>4 = `IPC_RX_OVERRUN`<br>5 = `IPC_TX_OVERRUN` | plausible |
| `PMF_a057_canID` | page 57 | PMF ECU: a057 can ID | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PMF_a057_errorType` | page 57 | PMF ECU: a057 error type | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH_SHORT`<br>2 = `LENGTH_LONG`<br>3 = `CHECKSUM`<br>4 = `SEQUENCE`<br>5 = `DATA_INVALID`<br>6 = `UNKNOWN_ID` | plausible |
| `PMF_a057_badValue1` | page 57 | PMF ECU: a057 bad value1 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a057_badValue2` | page 57 | PMF ECU: a057 bad value2 | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_a058_hvilCurrent` | page 58 | PMF ECU: a058 hvil current | 16\|8 | little-endian | unsigned | 0.1 | 0 | mA | 0 to 25.5 |  | plausible |
| `PMF_a061_diIpcVersion` | page 61 | PMF ECU: a061 di ipc version | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a061_pmIpcVersion` | page 61 | PMF ECU: a061 pm ipc version | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a062_address` | page 62 | PMF ECU: a062 address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PMF_a062_errorType` | page 62 | PMF ECU: a062 error type | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `FLASH_UNCORRECTABLE_LOW`<br>2 = `FLASH_UNCORRECTABLE_HIGH`<br>3 = `FLASH_FAIL0_LOW`<br>4 = `FLASH_FAIL0_HIGH`<br>5 = `FLASH_FAIL1_LOW`<br>6 = `FLASH_FAIL1_HIGH`<br>7 = `RAM_UNCORRECTABLE_CPU`<br>8 = `RAM_UNCORRECTABLE_CLA`<br>9 = `RAM_UNCORRECTABLE_DMA`<br>10 = `RAM_CORRECTABLE_CPU`<br>11 = `RAM_CORRECTABLE_CLA`<br>12 = `RAM_CORRECTABLE_DMA` | plausible |
| `PMF_a064_interventionType` | page 64 | PMF ECU: a064 intervention type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `masterTorqueMonitorShutoff`<br>1 = `resolver`<br>2 = `torqueCmdInvalid`<br>3 = `cruiseFault`<br>4 = `motorMovementDetected`<br>5 = `accumulatedTorque`<br>6 = `torqueReversal`<br>7 = `excessiveRegenTorque`<br>8 = `torqueInNeutral`<br>9 = `inconsistentTorqueSign`<br>10 = `switchOffPathTestFail`<br>11 = `switchingAfterIntervention`<br>12 = `currentAfterIntervention`<br>13 = `diHeartbeat`<br>14 = `inconsistentAxleTorque`<br>15 = `excessiveMotorMz` | plausible |
| `PMF_a064_torqueCmdState` | page 64 | PMF ECU: a064 torque cmd state; raw 0 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>6 = `Valid`<br>8 = `Invalid` | plausible |
| `PMF_a064_shortDetectedByDI` | page 64 | PMF ECU: a064 short detected by DI | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a064_UI_stoppingMode` | page 64 | PMF ECU: a064 UI stopping mode | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `CREEP`<br>2 = `HOLD` | plausible |
| `PMF_a064_diCrsState` | page 64 | PMF ECU: a064 di crs state | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PMF_a064_pmCrsState` | page 64 | PMF ECU: a064 pm crs state | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNAVAILABLE`<br>1 = `STANDBY`<br>2 = `ENABLED`<br>3 = `STANDSTILL`<br>4 = `OVERRIDE`<br>5 = `FAULT`<br>6 = `PRE_FAULT`<br>7 = `PRE_CANCEL` | plausible |
| `PMF_a082_faultAddress` | page 82 | PMF ECU: a082 fault address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PMF_a082_isWriteNotRead` | page 82 | PMF ECU: a082 is write not read | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a084_faultAddress` | page 84 | PMF ECU: a084 fault address | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PMF_a084_firewallId` | page 84 | PMF ECU: a084 firewall id | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `L2OCRAM_BANK0_SLV`<br>1 = `L2OCRAM_BANK1_SLV`<br>2 = `L2OCRAM_BANK2_SLV`<br>3 = `L2OCRAM_BANK3_SLV`<br>4 = `R5SS0_CORE0_AXIS_SLV`<br>5 = `R5SS0_CORE1_AXIS_SLV`<br>6 = `R5SS1_CORE0_AXIS_SLV`<br>7 = `R5SS1_CORE1_AXIS_SLV`<br>8 = `DTHE_SLV`<br>9 = `MBOX_RAM_SLV`<br>10 = `QSPI0_SLV`<br>11 = `SCRM2SCRP0_SLV`<br>12 = `SCRM2SCRP1_SLV`<br>13 = `R5SS0_CORE0_AHB_MST`<br>14 = `R5SS0_CORE1_AHB_MST`<br>15 = `R5SS1_CORE0_AHB_MST`<br>16 = `R5SS1_CORE1_AHB_MST`<br>17 = `HSM_SLV` | plausible |
| `PMF_a084_privId` | page 84 | PMF ECU: a084 priv id | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 1 = `M4FSS0_0`<br>4 = `R5FSS0_0`<br>5 = `R5FSS0_1`<br>6 = `R5FSS1_0`<br>7 = `R5FSS1_1`<br>9 = `ICSSM`<br>10 = `CPSW` | plausible |
| `PMF_a084_ns` | page 84 | PMF ECU: a084 ns | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a084_faultType` | page 84 | PMF ECU: a084 fault type | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_FAULT`<br>1 = `USER_EXE`<br>2 = `USER_WRITE`<br>3 = `USER_READ`<br>4 = `SUPER_EXE`<br>5 = `SUPER_WRITE`<br>6 = `SUPER_READ` | plausible |
| `PMF_a092_pllClockSource` | page 92 | PMF ECU: a092 pll clock source | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INTOSC2`<br>1 = `XTAL`<br>2 = `INTOSC1` | plausible |
| `PMF_a100_index1kHzPeriodic` | page 100 | PMF ECU: a100 index1k hz periodic | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a100_index100HzPeriodic` | page 100 | PMF ECU: a100 index100 hz periodic | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a100_index10HzPeriodic` | page 100 | PMF ECU: a100 index10 hz periodic | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a100_indexSWI` | page 100 | PMF ECU: a100 index SWI | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a100_eepEvent` | page 100 | PMF ECU: a100 eep event | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_a100_module500HzActive` | page 100 | PMF ECU: a100 module500 hz active | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_module50HzActive` | page 100 | PMF ECU: a100 module50 hz active | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_module1HzActive` | page 100 | PMF ECU: a100 module1 hz active | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_task10HzActive` | page 100 | PMF ECU: a100 task10 hz active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_taskUdsActive` | page 100 | PMF ECU: a100 task uds active | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`PMF_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (3 signals), page 2 (5 signals), page 3 (3 signals), page 4 (5 signals), page 5 (3 signals), page 6 (3 signals), page 10 (17 signals), page 11 (6 signals), page 12 (4 signals), page 13 (3 signals), page 17 (2 signals), page 18 (3 signals), page 19 (2 signals), page 25 (26 signals), page 26 (11 signals), page 32 (3 signals), page 33 (4 signals), page 36 (15 signals), page 37 (1 signals), page 39 (3 signals), page 40 (3 signals), page 42 (5 signals), page 53 (5 signals), page 54 (5 signals), page 55 (11 signals), page 56 (3 signals), page 57 (4 signals), page 58 (1 signals), page 61 (2 signals), page 62 (2 signals), page 64 (6 signals), page 82 (2 signals), page 84 (5 signals), page 92 (1 signals), page 100 (10 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
