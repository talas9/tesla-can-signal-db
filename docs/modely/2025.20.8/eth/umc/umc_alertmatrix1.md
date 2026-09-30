---
layout: default
title: "UMC_alertMatrix1 (0x338) — UMC ECU, Tesla Model Y 2025.20.8 ETH"
description: "UMC ECU message: alert matrix1. Ethernet-side message UMC_alertMatrix1 of UMC ECU for Tesla Model Y firmware 2025.20.8, 39 signals (UMC_a001_gndMonIntrptLineSide, UMC_a002_GFCITripped, UMC_a003_GFCISelfTestFault, UMC_a004_inputOverVoltage and 35 more). Bit layout, scaling, units and value tables."
---

# UMC_alertMatrix1 (0x338) — UMC ECU, Tesla Model Y 2025.20.8 ETH

UMC ECU message: alert matrix1. This page documents the 39 signals of UMC_alertMatrix1 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UMC_alertMatrix1` |
| Ethernet-side id | 0x338 (824) |
| ECU | [UMC ECU](../../umc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UMC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 39 |

## Signals of UMC_alertMatrix1

Tesla Model Y CAN bus signals in `UMC_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UMC_a001_gndMonIntrptLineSide` | UMC ECU: a001 gnd mon intrpt line side | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a002_GFCITripped` | UMC ECU: a002 GFCI tripped | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a003_GFCISelfTestFault` | UMC ECU: a003 GFCI self test fault | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a004_inputOverVoltage` | UMC ECU: a004 input over voltage | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a005_inputUnderVoltage` | UMC ECU: a005 input under voltage | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a006_contactorWelded` | UMC ECU: a006 contactor welded | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a007_pcbaOT` | UMC ECU: a007 pcba OT | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a008_wallPlugOT` | UMC ECU: a008 wall plug OT | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a009_vehConnOT` | UMC ECU: a009 veh conn OT | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a010_inputOT` | UMC ECU: a010 input OT | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a011_proxDisconnected` | UMC ECU: a011 prox disconnected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a012_pilotFault` | UMC ECU: a012 pilot fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a013_SA_Temperature` | UMC ECU: a013 SA temperature | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a014_SA_Genealogy` | UMC ECU: a014 SA genealogy | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a015_SA_Connection` | UMC ECU: a015 SA connection | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a016_pcbaOTFoldback` | UMC ECU: a016 pcba OT foldback | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a017_wallPlugOTFoldback` | UMC ECU: a017 wall plug OT foldback | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a018_vehConnOTFoldback` | UMC ECU: a018 veh conn OT foldback | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a019_inputOTFoldback` | UMC ECU: a019 input OT foldback | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a020_applicationCRC` | UMC ECU: a020 application CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a021_dataBus` | UMC ECU: a021 data bus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a022_criticalRAM` | UMC ECU: a022 critical RAM | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a023_adcSelfTest` | UMC ECU: a023 adc self test | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a024_gndResistanceHigh` | UMC ECU: a024 gnd resistance high | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a025_cntrOpenExpectedClose` | UMC ECU: a025 cntr open expected close | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a026_vRefOutOfRange` | UMC ECU: a026 v ref out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a027_watchdogExpired` | UMC ECU: a027 watchdog expired | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a028_processorBooted` | UMC ECU: a028 processor booted | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a029_acPowerLoss` | UMC ECU: a029 ac power loss | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a030_acLostPllLock` | UMC ECU: a030 ac lost pll lock | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a031_relayCoilVIrrational` | UMC ECU: a031 relay coil v irrational | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a032_chcVitalsRequestFailure` | UMC ECU: a032 chc vitals request failure | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a033_chcUpdateFault` | UMC ECU: a033 chc update fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a034_v2lSAUnsupported` | UMC ECU: a034 v2l SA unsupported | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a035_v2lHVACDetected` | UMC ECU: a035 v2l HVAC detected | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a037_GFCICalibration` | UMC ECU: a037 GFCI calibration | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a038_chcVitalsFault` | UMC ECU: a038 chc vitals fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a039_inputOverCurrent` | UMC ECU: a039 input over current | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a040_gndDisconnected` | UMC ECU: a040 gnd disconnected | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UMC ECU messages (UMC)](../../umc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
