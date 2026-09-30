---
layout: default
title: "VCBATT0_alertMatrix (0x3CD) — VCBATT0 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT0 ECU message: alert matrix. Tesla Model Y CAN bus message VCBATT0_alertMatrix (0x3CD) of VCBATT0 ECU, firmware 2026.26.6.5, 35 signals (VCBATT0_matrixIndex, VCBATT0_a001_WatchdogReset, VCBATT0_a002_PowerLossReset, VCBATT0_a003_SWAssertion and 31 more). Bit layout, scaling, units and value tables."
---

# VCBATT0_alertMatrix (0x3CD) — VCBATT0 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT0 ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 35 signals of VCBATT0_alertMatrix as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT0_alertMatrix` |
| CAN id | 0x3CD (973) |
| ECU | [VCBATT0 ECU](../../vcbatt0.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT0 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 35 |

## Signals of VCBATT0_alertMatrix

Tesla Model Y CAN bus signals in `VCBATT0_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT0_matrixIndex` | selector | VCBATT0 ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>7 = `AlertMatrix7` | plausible |
| `VCBATT0_a001_WatchdogReset` | page 0 | VCBATT0 ECU: a001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a002_PowerLossReset` | page 0 | VCBATT0 ECU: a002 power loss reset | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a003_SWAssertion` | page 0 | VCBATT0 ECU: a003 SW assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a005_CANTXError` | page 0 | VCBATT0 ECU: a005 CANTX error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a006_CANTX_cyclicError` | page 0 | VCBATT0 ECU: a006 CANTX cyclic error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a012_CPUReset` | page 0 | VCBATT0 ECU: a012 CPU reset | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a013_AlertManagerFault` | page 0 | VCBATT0 ECU: a013 alert manager fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a015_NVMMError` | page 0 | VCBATT0 ECU: a015 NVMM error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a016_NVMMRecordError` | page 0 | VCBATT0 ECU: a016 NVMM record error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a021_TaskSchedulerError` | page 0 | VCBATT0 ECU: a021 task scheduler error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a022_TaskInitError` | page 0 | VCBATT0 ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a029_CoreDump` | page 0 | VCBATT0 ECU: a029 core dump | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a030_ECULogUploadRequest` | page 0 | VCBATT0 ECU: a030 ECU log upload request | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a031_UDSActive` | page 0 | VCBATT0 ECU: a031 UDS active | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a032_ipcWatchdogExpired` | page 0 | VCBATT0 ECU: a032 ipc watchdog expired | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a033_eccNonCorrectableError` | page 0 | VCBATT0 ECU: a033 ecc non correctable error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a038_ProtFaultInfo` | page 0 | VCBATT0 ECU: a038 prot fault info | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a039_ProtFaultAddress` | page 0 | VCBATT0 ECU: a039 prot fault address | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a040_Backtrace` | page 0 | VCBATT0 ECU: a040 backtrace | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a041_HighCPULoad` | page 0 | VCBATT0 ECU: a041 high CPU load | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a042_HighStackUsage` | page 0 | VCBATT0 ECU: a042 high stack usage | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a043_Task1msError` | page 0 | VCBATT0 ECU: a043 task1ms error | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a044_Task10msError` | page 0 | VCBATT0 ECU: a044 task10ms error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a045_Task100msError` | page 0 | VCBATT0 ECU: a045 task100ms error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a046_Task1000msError` | page 0 | VCBATT0 ECU: a046 task1000ms error | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a047_resetReason` | page 0 | VCBATT0 ECU: a047 reset reason | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a058_inputRHighSyncDebug` | page 0 | VCBATT0 ECU: a058 input r high sync debug | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a059_inputResistanceHigh` | page 0 | VCBATT0 ECU: a059 input resistance high | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a060_engineeringBuild` | page 0 | VCBATT0 ECU: a060 engineering build | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a061_XCPConnected` | page 1 | VCBATT0 ECU: a061 XCP connected | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a062_XCPWasConnected` | page 1 | VCBATT0 ECU: a062 XCP was connected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a063_SwitchFault` | page 1 | VCBATT0 ECU: a063 switch fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a064_busSleepReqTimeout` | page 1 | VCBATT0 ECU: a064 bus sleep req timeout | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCBATT0_a423_rtosSleepFailed` | page 7 | VCBATT0 ECU: a423 rtos sleep failed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`VCBATT0_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (29 signals), page 1 (4 signals), page 7 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT0 ECU messages (VCBATT0)](../../vcbatt0.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
