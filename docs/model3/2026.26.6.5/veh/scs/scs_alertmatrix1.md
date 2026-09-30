---
layout: default
title: "SCS_alertMatrix1 (0x365) — SCS ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "SCS ECU message: alert matrix1. Tesla Model 3 CAN bus message SCS_alertMatrix1 (0x365) of SCS ECU, firmware 2026.26.6.5, 62 signals (SCS_a001_hwDSPfault, SCS_a002_hwIbatOC, SCS_a003_hwCordOT, SCS_a004_hwVbusOV and 58 more). Bit layout, scaling, units and value tables."
---

# SCS_alertMatrix1 (0x365) — SCS ECU, Tesla Model 3 2026.26.6.5 VEH CAN

SCS ECU message: alert matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 62 signals of SCS_alertMatrix1 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCS_alertMatrix1` |
| CAN id | 0x365 (869) |
| ECU | [SCS ECU](../../scs.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 62 |

## Signals of SCS_alertMatrix1

Tesla Model 3 CAN bus signals in `SCS_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCS_a001_hwDSPfault` | SCS ECU: a001 hw DS pfault | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a002_hwIbatOC` | SCS ECU: a002 hw ibat OC | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a003_hwCordOT` | SCS ECU: a003 hw cord OT | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a004_hwVbusOV` | SCS ECU: a004 hw vbus OV | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a005_hwHVIL` | SCS ECU: a005 hw HVIL | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a006_hwWeld_V1` | SCS ECU: a006 hw weld V1 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a007_hwWeld_V2` | SCS ECU: a007 hw weld V2 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a008_hwIllegalCntrShoot` | SCS ECU: a008 hw illegal cntr shoot | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a009_hwOpen_V1` | SCS ECU: a009 hw open V1 | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a010_hwOpen_V2` | SCS ECU: a010 hw open V2 | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a011_hwIllegalCntrCmdV1` | SCS ECU: a011 hw illegal cntr cmd V1 | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a012_hwIllegalCntrCmdV2` | SCS ECU: a012 hw illegal cntr cmd V2 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a013_cordTempHiFoldBk` | SCS ECU: a013 cord temp hi fold bk | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a014_coolantTempHiFoldBk` | SCS ECU: a014 coolant temp hi fold bk | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a015_cpldRationality` | SCS ECU: a015 cpld rationality | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a016_unusedHW16` | SCS ECU: a016 unused HW16 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a017_unusedHW17` | SCS ECU: a017 unused HW17 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a018_unusedHW18` | SCS ECU: a018 unused HW18 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a019_unusedHW19` | SCS ECU: a019 unused HW19 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a020_unusedHW20` | SCS ECU: a020 unused HW20 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a021_unusedHW21` | SCS ECU: a021 unused HW21 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a024_emergencyShutdown` | SCS ECU: a024 emergency shutdown | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a025_internalIsolationFault` | SCS ECU: a025 internal isolation fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a026_internalIsolationLow` | SCS ECU: a026 internal isolation low | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a027_externalIsolationLow` | SCS ECU: a027 external isolation low | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a028_isolationRationality` | SCS ECU: a028 isolation rationality | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a029_VbatOV` | SCS ECU: a029 vbat OV | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a030_VbusOV` | SCS ECU: a030 vbus OV | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a031_IbatOC` | SCS ECU: a031 ibat OC | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a032_VBatRationality` | SCS ECU: a032 v bat rationality | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a033_VBusRationality` | SCS ECU: a033 v bus rationality | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a034_IBatRationality` | SCS ECU: a034 i bat rationality | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a035_unexpectedVbusBehavior` | SCS ECU: a035 unexpected vbus behavior | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a036_internalContactorWelded` | SCS ECU: a036 internal contactor welded | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a037_outputContactorWelded` | SCS ECU: a037 output contactor welded | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a038_contactorFailedOpen` | SCS ECU: a038 contactor failed open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a039_ibatRegulation` | SCS ECU: a039 ibat regulation | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a040_plus12VOutOfRange` | SCS ECU: a040 plus12 v out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a041_minus12VOutOfRange` | SCS ECU: a041 minus12 v out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a042_pilotOutOfRange` | SCS ECU: a042 pilot out of range | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a043_pilotRationality` | SCS ECU: a043 pilot rationality | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a044_proximityRationality` | SCS ECU: a044 proximity rationality | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a045_pcbaOT` | SCS ECU: a045 pcba OT | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a046_coolantOT` | SCS ECU: a046 coolant OT | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a047_cordOT` | SCS ECU: a047 cord OT | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a048_ambientOT` | SCS ECU: a048 ambient OT | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a049_pcbaTempRationality` | SCS ECU: a049 pcba temp rationality | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a050_coolantTempRationality` | SCS ECU: a050 coolant temp rationality | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a051_cordTempRationality` | SCS ECU: a051 cord temp rationality | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a052_ambientTempRationality` | SCS ECU: a052 ambient temp rationality | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a053_unexpectedThermalBehavi` | SCS ECU: a053 unexpected thermal behavi | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a054_pumpRegulation` | SCS ECU: a054 pump regulation | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a055_coolantLevelLow` | SCS ECU: a055 coolant level low | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a056_stateTransitionDenied` | SCS ECU: a056 state transition denied | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a057_watchdogReset` | SCS ECU: a057 watchdog reset | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a058_adcRef` | SCS ECU: a058 adc ref | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a059_memoryError` | SCS ECU: a059 memory error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a060_swHVIL` | SCS ECU: a060 sw HVIL | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a061_postOutOfService` | SCS ECU: a061 post out of service | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a062_unused` | SCS ECU: a062 unused | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a063_canRationality` | SCS ECU: a063 can rationality | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a064_vehicleCommandTimeout` | SCS ECU: a064 vehicle command timeout | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All SCS ECU messages (SCS)](../../scs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
