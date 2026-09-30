---
layout: default
title: "SDCR_alertMatrix (0x5BB) — SDCR ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "SDCR ECU message: alert matrix. Tesla Model 3 CAN bus message SDCR_alertMatrix (0x5BB) of SDCR ECU, firmware 2026.26.6.5, 35 signals (SDCR_matrixIndex, SDCR_a001_powerOnSelfTestFailed, SDCR_a002_diPstSkipped, SDCR_a003_diUartMIA and 31 more). Bit layout, scaling, units and value tables."
---

# SDCR_alertMatrix (0x5BB) — SDCR ECU, Tesla Model 3 2026.26.6.5 VEH CAN

SDCR ECU message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 35 signals of SDCR_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SDCR_alertMatrix` |
| CAN id | 0x5BB (1467) |
| ECU | [SDCR ECU](../../sdcr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SDCR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 35 |

## Signals of SDCR_alertMatrix

Tesla Model 3 CAN bus signals in `SDCR_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SDCR_matrixIndex` | selector | SDCR ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SDCR_AlertMatrix0` | plausible |
| `SDCR_a001_powerOnSelfTestFailed` | page 0 | SDCR ECU: a001 power on self test failed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a002_diPstSkipped` | page 0 | SDCR ECU: a002 di pst skipped | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a003_diUartMIA` | page 0 | SDCR ECU: a003 di uart MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a004_pmRunningFdbkIrrational` | page 0 | SDCR ECU: a004 pm running fdbk irrational | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a005_motorSpeedIrrational` | page 0 | SDCR ECU: a005 motor speed irrational | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_pyroTriggered` | page 0 | SDCR ECU: a006 pyro triggered | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_faultCurrentsDetected` | page 0 | SDCR ECU: a007 fault currents detected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a008_hvlinkMIA` | page 0 | SDCR ECU: a008 hvlink MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a009_uartVersionMismatch` | page 0 | SDCR ECU: a009 uart version mismatch | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a010_vrefIrrational` | page 0 | SDCR ECU: a010 vref irrational | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a011_phaseCurrentOffset` | page 0 | SDCR ECU: a011 phase current offset | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a012_vBoostSecIrrational` | page 0 | SDCR ECU: a012 v boost sec irrational | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a013_vBkupIrrational` | page 0 | SDCR ECU: a013 v bkup irrational | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a014_vBusIrrational` | page 0 | SDCR ECU: a014 v bus irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a015_phaseVIrrational` | page 0 | SDCR ECU: a015 phase v irrational | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a016_systemReset` | page 0 | SDCR ECU: a016 system reset | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_adcSPIError` | page 0 | SDCR ECU: a017 adc SPI error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_historicalPyroTrigger` | page 0 | SDCR ECU: a018 historical pyro trigger | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_historicalFaultCurrents` | page 0 | SDCR ECU: a019 historical fault currents | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a020_eepromSPIError` | page 0 | SDCR ECU: a020 eeprom SPI error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a021_busBarTempIrrational` | page 0 | SDCR ECU: a021 bus bar temp irrational | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a022_TaskInitError` | page 0 | SDCR ECU: a022 task init error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a023_ecuLogAvailable` | page 0 | SDCR ECU: a023 ecu log available | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a024_gtwMIA` | page 0 | SDCR ECU: a024 gtw MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_diSwitchingFdbkIrrational` | page 0 | SDCR ECU: a025 di switching fdbk irrational | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a026_faultCurrentMonitoringDisabled` | page 0 | SDCR ECU: a026 fault current monitoring disabled | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a027_diCanMIA` | page 0 | SDCR ECU: a027 di can MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a028_vcLVStateMIA` | page 0 | SDCR ECU: a028 vc LV state MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a029_diMIA` | page 0 | SDCR ECU: a029 di MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a030_placeholder30` | page 0 | SDCR ECU: a030 placeholder30 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a031_placeholder31` | page 0 | SDCR ECU: a031 placeholder31 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a032_placeholder32` | page 0 | SDCR ECU: a032 placeholder32 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a033_placeholder33` | page 0 | SDCR ECU: a033 placeholder33 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a034_phaseCurrentIrrational` | page 0 | SDCR ECU: a034 phase current irrational | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`SDCR_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (34 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All SDCR ECU messages (SDCR)](../../sdcr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
