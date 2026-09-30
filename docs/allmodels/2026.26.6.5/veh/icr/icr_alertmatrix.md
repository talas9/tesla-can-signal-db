---
layout: default
title: "ICR_alertMatrix (0x3B8) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: alert matrix. Tesla Model 3 / Model Y CAN bus message ICR_alertMatrix (0x3B8) of ICR ECU, firmware 2026.26.6.5, 40 signals (ICR_matrixIndex, ICR_a001_WatchdogReset, ICR_a002_PowerLossReset, ICR_a003_SWAssertion and 36 more). Bit layout, scaling, units and value tables."
---

# ICR_alertMatrix (0x3B8) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

ICR ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 40 signals of ICR_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_alertMatrix` |
| CAN id | 0x3B8 (952) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 40 |

## Signals of ICR_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `ICR_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_matrixIndex` | selector | ICR ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2` | plausible |
| `ICR_a001_WatchdogReset` | page 0 | ICR ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a002_PowerLossReset` | page 0 | ICR ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a003_SWAssertion` | page 0 | ICR ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a005_CANTXError` | page 0 | ICR ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a006_CANTX_cyclicError` | page 0 | ICR ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a012_CPUReset` | page 0 | ICR ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a013_AlertManagerFault` | page 0 | ICR ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a015_NVMMError` | page 0 | ICR ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a016_NVMMRecordError` | page 0 | ICR ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a021_TaskSchedulerError` | page 0 | ICR ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a022_TaskInitError` | page 0 | ICR ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a029_CoreDump` | page 0 | ICR ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a030_ECULogUploadRequest` | page 0 | ICR ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a031_UDSActive` | page 0 | ICR ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a041_HighCPULoad` | page 0 | ICR ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a042_HighStackUsage` | page 0 | ICR ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a043_Task1msError` | page 0 | ICR ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a044_Task10msError` | page 0 | ICR ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a045_Task100msError` | page 0 | ICR ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a046_Task1000msError` | page 0 | ICR ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a058_inputRHighSyncDebug` | page 0 | ICR ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a059_inputResistanceHigh` | page 0 | ICR ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a060_engineeringBuild` | page 0 | ICR ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a061_XCPConnected` | page 1 | ICR ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a062_XCPWasConnected` | page 1 | ICR ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a063_SwitchFault` | page 1 | ICR ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a064_busSleepReqTimeout` | page 1 | ICR ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a133_radarBlocked` | page 2 | ICR ECU: a133 radar blocked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a134_radarPgood` | page 2 | ICR ECU: a134 radar pgood | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a135_radarTxBallBreak` | page 2 | ICR ECU: a135 radar tx ball break | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a136_radarHighTemperature` | page 2 | ICR ECU: a136 radar high temperature | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a137_radarBlocked` | page 2 | ICR ECU: a137 radar blocked | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a138_DriverSideMismatch` | page 2 | ICR ECU: a138 driver side mismatch | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a139_AbnormalBlockageDetected` | page 2 | ICR ECU: a139 abnormal blockage detected | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a140_OccupancyExceptionEncountered` | page 2 | ICR ECU: a140 occupancy exception encountered | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a141_RequiresReplacement` | page 2 | ICR ECU: a141 requires replacement | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a142_ModeOverrideActive` | page 2 | ICR ECU: a142 mode override active | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a143_DSPCoreSkipped` | page 2 | ICR ECU: a143 DSP core skipped | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ICR_a144_OccupancyNotificationAlert` | page 2 | ICR ECU: a144 occupancy notification alert | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`ICR_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (23 signals), page 1 (4 signals), page 2 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
