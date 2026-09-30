---
layout: default
title: "VCBATT1_LVSelfTests (0x45F) — VCBATT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: LV self tests. Tesla Model 3 / Model Y CAN bus message VCBATT1_LVSelfTests (0x45F) of VCBATT1 ECU, firmware 2026.26.6.5, 27 signals (VCBATT1_LVSelfTestsChecksum, VCBATT1_LVSelfTestsCounter, VCBATT1_LVSelfTestsIndex, VCBATT1_lvProtectionSelfTestsEnabled and 23 more). Bit layout, scaling, units and value tables."
---

# VCBATT1_LVSelfTests (0x45F) — VCBATT1 ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: LV self tests; frame length from the layout, not yet observed on a vehicle bus. This page documents the 27 signals of VCBATT1_LVSelfTests as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_LVSelfTests` |
| CAN id | 0x45F (1119) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 27 |

## Signals of VCBATT1_LVSelfTests

Tesla Model 3 / Model Y CAN bus signals in `VCBATT1_LVSelfTests`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_LVSelfTestsChecksum` |  | VCBATT1 ECU: LV self tests checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCBATT1_LVSelfTestsCounter` |  | VCBATT1 ECU: LV self tests counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCBATT1_LVSelfTestsIndex` | selector | VCBATT1 ECU: LV self tests index | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ORCHESTRATOR`<br>1 = `STATES` | plausible |
| `VCBATT1_lvProtectionSelfTestsEnabled` | page 1 | VCBATT1 ECU: lv protection self tests enabled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startBattDomainOvercurrentSelfTest` | page 1 | VCBATT1 ECU: start batt domain overcurrent self test | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startBattDomainOvervoltageSelfTest` | page 1 | VCBATT1 ECU: start batt domain overvoltage self test | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startBattDomainUndervoltageSelfTest` | page 1 | VCBATT1 ECU: start batt domain undervoltage self test | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startDualPowerLoadsSelfTest` | page 1 | VCBATT1 ECU: start dual power loads self test | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startVCBattBridgeEFuseASICSelfTest` | page 1 | VCBATT1 ECU: start VC batt bridge e fuse ASIC self test | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startPCSOVShutdownSelfTest` | page 1 | VCBATT1 ECU: start PCSOV shutdown self test | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startPCSDomainOvervoltageSelfTest` | page 1 | VCBATT1 ECU: start PCS domain overvoltage self test | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startBattDomainUndervoltageVCLeftSelfTest` | page 1 | VCBATT1 ECU: start batt domain undervoltage VC left self test | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startPCSDomainUndervoltageSelfTest` | page 1 | VCBATT1 ECU: start PCS domain undervoltage self test | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_startVCFrontBridgeEFuseASICSelfTest` | page 1 | VCBATT1 ECU: start VC front bridge e fuse ASIC self test | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_battDomainOvercurrentSelfTestResult` | page 1 | Self-Test Result. | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_SELF_TEST_RESULT_INVALID`<br>1 = `VC_SELF_TEST_RESULT_FAILED`<br>2 = `VC_SELF_TEST_RESULT_PASSED` | validated |
| `VCBATT1_battDomainOvercurrentSelfTestState` | page 1 | Self-Test State; raw 4 = signal not available (SNA) | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_SELF_TEST_STATE_IDLE`<br>1 = `VC_SELF_TEST_STATE_PENDING`<br>2 = `VC_SELF_TEST_STATE_RUNNING`<br>3 = `VC_SELF_TEST_STATE_NEW_RESULT`<br>4 = `VC_SELF_TEST_STATE_SNA` | validated |
| `VCBATT1_battDomainOvervoltageSelfTestResult` | page 1 | Self-Test Result. | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_SELF_TEST_RESULT_INVALID`<br>1 = `VC_SELF_TEST_RESULT_FAILED`<br>2 = `VC_SELF_TEST_RESULT_PASSED` | validated |
| `VCBATT1_battDomainOvervoltageSelfTestState` | page 1 | Self-Test State; raw 4 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_SELF_TEST_STATE_IDLE`<br>1 = `VC_SELF_TEST_STATE_PENDING`<br>2 = `VC_SELF_TEST_STATE_RUNNING`<br>3 = `VC_SELF_TEST_STATE_NEW_RESULT`<br>4 = `VC_SELF_TEST_STATE_SNA` | validated |
| `VCBATT1_battDomainUndervoltageSelfTestResult` | page 1 | Self-Test Result. | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_SELF_TEST_RESULT_INVALID`<br>1 = `VC_SELF_TEST_RESULT_FAILED`<br>2 = `VC_SELF_TEST_RESULT_PASSED` | validated |
| `VCBATT1_battDomainUndervoltageSelfTestState` | page 1 | Self-Test State; raw 4 = signal not available (SNA) | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_SELF_TEST_STATE_IDLE`<br>1 = `VC_SELF_TEST_STATE_PENDING`<br>2 = `VC_SELF_TEST_STATE_RUNNING`<br>3 = `VC_SELF_TEST_STATE_NEW_RESULT`<br>4 = `VC_SELF_TEST_STATE_SNA` | validated |
| `VCBATT1_dualPowerLoadsSelfTestResult` | page 1 | Self-Test Result. | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_SELF_TEST_RESULT_INVALID`<br>1 = `VC_SELF_TEST_RESULT_FAILED`<br>2 = `VC_SELF_TEST_RESULT_PASSED` | validated |
| `VCBATT1_dualPowerLoadsSelfTestState` | page 1 | Self-Test State; raw 4 = signal not available (SNA) | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_SELF_TEST_STATE_IDLE`<br>1 = `VC_SELF_TEST_STATE_PENDING`<br>2 = `VC_SELF_TEST_STATE_RUNNING`<br>3 = `VC_SELF_TEST_STATE_NEW_RESULT`<br>4 = `VC_SELF_TEST_STATE_SNA` | validated |
| `VCBATT1_vcbattBridgeEFuseASICSelfTestResult` | page 1 | Self-Test Result. | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_SELF_TEST_RESULT_INVALID`<br>1 = `VC_SELF_TEST_RESULT_FAILED`<br>2 = `VC_SELF_TEST_RESULT_PASSED` | validated |
| `VCBATT1_vcbattBridgeEFuseASICSelfTestState` | page 1 | Self-Test State; raw 4 = signal not available (SNA) | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_SELF_TEST_STATE_IDLE`<br>1 = `VC_SELF_TEST_STATE_PENDING`<br>2 = `VC_SELF_TEST_STATE_RUNNING`<br>3 = `VC_SELF_TEST_STATE_NEW_RESULT`<br>4 = `VC_SELF_TEST_STATE_SNA` | validated |
| `VCBATT1_uvProtectionState` | page 1 | VCBATT1 ECU: uv protection state | 51\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `VC_UV_STATE_IDLE`<br>1 = `VC_UV_STATE_SELF_TEST_SETUP`<br>2 = `VC_UV_STATE_SELF_TEST_TURN_ON_LOADS`<br>3 = `VC_UV_STATE_SELF_TEST_LOADS_ON`<br>4 = `VC_UV_STATE_SELF_TEST_LOADS_GOING_DOWN`<br>5 = `VC_UV_STATE_SELF_TEST_LOADS_GOING_DOWN_COMPLETE`<br>6 = `VC_UV_STATE_SELF_TEST_CHECK_STUCK_OFF`<br>7 = `VC_UV_STATE_SELF_TEST_CHECK_STUCK_OFF_COMPLETE`<br>8 = `VC_UV_STATE_SELF_TEST_CHECK_STUCK_ON`<br>9 = `VC_UV_STATE_SELF_TEST_CLEAN_UP`<br>10 = `VC_UV_STATE_ARMED`<br>11 = `VC_UV_STATE_TRIPPED`<br>12 = `VC_UV_STATE_DELIBERATELY_TRIPPED` | validated |
| `VCBATT1_undervoltageSelfTestFaultInjectionReady` | page 1 | VCBATT1 ECU: undervoltage self test fault injection ready | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_selfTestsRunningMode` | page 1 | VCBATT1 ECU: self tests running mode | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NORMAL`<br>1 = `FACTORY_NORMAL`<br>2 = `FACTORY_REDUCED`<br>3 = `REDUCED`<br>4 = `DISABLED` | validated |

## Multiplexing

`VCBATT1_LVSelfTestsIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (24 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
