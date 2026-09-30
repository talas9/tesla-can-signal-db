---
layout: default
title: "ICR_alertLog (0x4B8) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: alert log. Tesla Model 3 / Model Y CAN bus message ICR_alertLog (0x4B8) of ICR ECU, firmware 2026.26.6.5, 40 signals (ICR_alertID, ICR_alertState, ICR_a001_watchdogTaskAppDPM, ICR_a001_watchdogTaskMMWControl and 36 more). Bit layout, scaling, units and value tables."
---

# ICR_alertLog (0x4B8) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

ICR ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 40 signals of ICR_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_alertLog` |
| CAN id | 0x4B8 (1208) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 40 |

## Signals of ICR_alertLog

Tesla Model 3 / Model Y CAN bus signals in `ICR_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_alertID` | selector | ICR ECU: alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>133 = `a133_radarBlocked`<br>134 = `a134_radarPgood`<br>135 = `a135_radarTxBallBreak`<br>136 = `a136_radarHighTemperature`<br>137 = `a137_radarBlocked`<br>138 = `a138_DriverSideMismatch`<br>139 = `a139_AbnormalBlockageDetected`<br>140 = `a140_OccupancyExceptionEncountered`<br>141 = `a141_RequiresReplacement`<br>142 = `a142_ModeOverrideActive`<br>143 = `a143_DSPCoreSkipped`<br>144 = `a144_OccupancyNotificationAlert` | plausible |
| `ICR_alertState` |  | ICR ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `ICR_a001_watchdogTaskAppDPM` | page 1 | ICR ECU: a001 watchdog task app DPM | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskMMWControl` | page 1 | ICR ECU: a001 watchdog task MMW control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskSentinelInterface` | page 1 | ICR ECU: a001 watchdog task sentinel interface | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskSentinelModeChange` | page 1 | ICR ECU: a001 watchdog task sentinel mode change | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskComTXRAD` | page 1 | ICR ECU: a001 watchdog task com TXRAD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskComRX` | page 1 | ICR ECU: a001 watchdog task com RX | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskComTXVEH` | page 1 | ICR ECU: a001 watchdog task com TXVEH | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskComUDS` | page 1 | ICR ECU: a001 watchdog task com UDS | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskCommonError` | page 1 | ICR ECU: a001 watchdog task common error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskUARTLog` | page 1 | ICR ECU: a001 watchdog task UART log | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogTaskDataDump` | page 1 | ICR ECU: a001 watchdog task data dump | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogRTOSAppRun10MS` | page 1 | ICR ECU: a001 watchdog RTOS app run10 MS | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_watchdogRTOSAppRun1MS` | page 1 | ICR ECU: a001 watchdog RTOS app run1 MS | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a001_InternalWatchdog` | page 1 | ICR ECU: a001 internal watchdog | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a015_NVMMMemOverflow` | page 15 | ICR ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a015_NVMMFilesystemError` | page 15 | ICR ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a015_NVMMRecordIDError` | page 15 | ICR ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a059_voltageDrop` | page 59 | ICR ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `ICR_a059_resistanceEstimate` | page 59 | ICR ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `ICR_a059_current` | page 59 | ICR ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `ICR_a063_switchChannel` | page 63 | ICR ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ICR_a063_switchType` | page 63 | ICR ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ICR_a063_ADCVoltage` | page 63 | ICR ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `ICR_a063_disconnected` | page 63 | ICR ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a063_indeterminate` | page 63 | ICR ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a063_stuckActive` | page 63 | ICR ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a063_faulted` | page 63 | ICR ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a133_nearClutter` | page 133 | ICR ECU: a133 near clutter | 16\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a133_farClutter` | page 133 | ICR ECU: a133 far clutter | 24\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a137_nearClutter` | page 137 | ICR ECU: a137 near clutter | 16\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a137_farClutter` | page 137 | ICR ECU: a137 far clutter | 24\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a139_nearClutter` | page 139 | ICR ECU: a139 near clutter | 16\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a139_farClutter` | page 139 | ICR ECU: a139 far clutter | 24\|8 | little-endian | signed | 0.2 | 0 | dB | -25.6 to 25.4 |  | plausible |
| `ICR_a141_pmicQualityExcursion` | page 141 | ICR ECU: a141 pmic quality excursion | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a141_calDataNotCalibratedOrProcessing` | page 141 | ICR ECU: a141 cal data not calibrated or processing | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a141_calDataValRXPhaseAboveMax` | page 141 | ICR ECU: a141 cal data val RX phase above max | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a141_calDataValRXPhaseMissingUnitMag` | page 141 | ICR ECU: a141 cal data val RX phase missing unit mag | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a141_calDataValRangeBiasAboveMax` | page 141 | ICR ECU: a141 cal data val range bias above max | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`ICR_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (14 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals), page 133 (2 signals), page 137 (2 signals), page 139 (2 signals), page 141 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
