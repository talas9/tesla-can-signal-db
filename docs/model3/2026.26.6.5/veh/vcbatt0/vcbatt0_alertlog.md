---
layout: default
title: "VCBATT0_alertLog (0x53A) — VCBATT0 ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "VCBATT0 ECU message: alert log. Tesla Model 3 CAN bus message VCBATT0_alertLog (0x53A) of VCBATT0 ECU, firmware 2026.26.6.5, 16 signals (VCBATT0_alertID, VCBATT0_alertState, VCBATT0_a001_InternalWatchdog, VCBATT0_a015_NVMMMemOverflow and 12 more). Bit layout, scaling, units and value tables."
---

# VCBATT0_alertLog (0x53A) — VCBATT0 ECU, Tesla Model 3 2026.26.6.5 VEH CAN

VCBATT0 ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 16 signals of VCBATT0_alertLog as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT0_alertLog` |
| CAN id | 0x53A (1338) |
| ECU | [VCBATT0 ECU](../../vcbatt0.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT0 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 16 |

## Signals of VCBATT0_alertLog

Tesla Model 3 CAN bus signals in `VCBATT0_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT0_alertID` | selector | VCBATT0 ECU: alert ID | 0\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>32 = `a032_ipcWatchdogExpired`<br>33 = `a033_eccNonCorrectableError`<br>38 = `a038_ProtFaultInfo`<br>39 = `a039_ProtFaultAddress`<br>40 = `a040_Backtrace`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>47 = `a047_resetReason`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>423 = `a423_rtosSleepFailed` | plausible |
| `VCBATT0_alertState` |  | VCBATT0 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `VCBATT0_a001_InternalWatchdog` | page 1 | VCBATT0 ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a015_NVMMMemOverflow` | page 15 | VCBATT0 ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a015_NVMMFilesystemError` | page 15 | VCBATT0 ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a015_NVMMRecordIDError` | page 15 | VCBATT0 ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a059_voltageDrop` | page 59 | VCBATT0 ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCBATT0_a059_resistanceEstimate` | page 59 | VCBATT0 ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `VCBATT0_a059_current` | page 59 | VCBATT0 ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `VCBATT0_a063_switchChannel` | page 63 | VCBATT0 ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT0_a063_switchType` | page 63 | VCBATT0 ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT0_a063_ADCVoltage` | page 63 | VCBATT0 ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `VCBATT0_a063_disconnected` | page 63 | VCBATT0 ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a063_indeterminate` | page 63 | VCBATT0 ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a063_stuckActive` | page 63 | VCBATT0 ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a063_faulted` | page 63 | VCBATT0 ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCBATT0_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 15 (3 signals), page 59 (3 signals), page 63 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All VCBATT0 ECU messages (VCBATT0)](../../vcbatt0.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
