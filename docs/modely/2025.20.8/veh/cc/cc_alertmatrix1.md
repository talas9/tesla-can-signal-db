---
layout: default
title: "CC_alertMatrix1 (0x46C) — Charge cable controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Charge cable controller message: alert matrix1. Tesla Model Y CAN bus message CC_alertMatrix1 (0x46C) of Charge cable controller, firmware 2025.20.8, 55 signals (CC_a001_gndMonIntrptLineSide, CC_a002_gndMonIntrptLoadSide, CC_a003_CCIDTripped, CC_a004_CCIDSelfTestFault and 51 more). Bit layout, scaling, units and value tables."
---

# CC_alertMatrix1 (0x46C) — Charge cable controller, Tesla Model Y 2025.20.8 VEH CAN

Charge cable controller message: alert matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 55 signals of CC_alertMatrix1 as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CC_alertMatrix1` |
| CAN id | 0x46C (1132) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 55 |

## Signals of CC_alertMatrix1

Tesla Model Y CAN bus signals in `CC_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CC_a001_gndMonIntrptLineSide` | Charge cable controller: a001 gnd mon intrpt line side | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a002_gndMonIntrptLoadSide` | Charge cable controller: a002 gnd mon intrpt load side | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a003_CCIDTripped` | Charge cable controller: a003 CCID tripped | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a004_CCIDSelfTestFault` | Charge cable controller: a004 CCID self test fault | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a005_groundedNeutral` | Charge cable controller: a005 grounded neutral | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a006_inputOverCurrent` | Charge cable controller: a006 input over current | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a007_inputOverVoltage` | Charge cable controller: a007 input over voltage | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a008_inputUnderVoltage` | Charge cable controller: a008 input under voltage | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a009_inputMiswired` | Charge cable controller: a009 input miswired | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a010_contactorWelded` | Charge cable controller: a010 contactor welded | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a011_ambientOT` | Charge cable controller: a011 ambient OT | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a012_wallPlugOT` | Charge cable controller: a012 wall plug OT | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a013_vehConnOT` | Charge cable controller: a013 veh conn OT | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a014_mcuSelfTestFault` | Charge cable controller: a014 mcu self test fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a015_PilotAFault` | Charge cable controller: a015 pilot a fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a016_PilotBFault` | Charge cable controller: a016 pilot b fault | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a017_PilotCFault` | Charge cable controller: a017 pilot c fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a018_PilotDFault` | Charge cable controller: a018 pilot d fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a019_proxDisconnected` | Charge cable controller: a019 prox disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a020_3vRailIncorrect` | Charge cable controller: a020 3v rail incorrect | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a021_CB_noMaster` | Charge cable controller: a021 CB no master | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a022_CB_tooManyMasters` | Charge cable controller: a022 CB too many masters | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a023_CB_tooManySlaves` | Charge cable controller: a023 CB too many slaves | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a024_CB_masterISetTooLow` | Charge cable controller: a024 CB master i set too low | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a025_evseTemp` | Charge cable controller: a025 evse temp | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a026_wallPlugTemp` | Charge cable controller: a026 wall plug temp | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a027_vehicleHandleTemp` | Charge cable controller: a027 vehicle handle temp | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a028_CB_rotarySelect` | Charge cable controller: a028 CB rotary select | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a029_PilotFFault` | Charge cable controller: a029 pilot f fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a030_masterSlaveMismatch` | Charge cable controller: a030 master slave mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a031_pllLockLost` | Charge cable controller: a031 pll lock lost | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a032_meteringFailure` | Charge cable controller: a032 metering failure | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a033_vRefOutOfRange` | Charge cable controller: a033 v ref out of range | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a034_bootAlert` | Charge cable controller: a034 boot alert | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a035_CCIDCalibration` | Charge cable controller: a035 CCID calibration | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a036_contactorStuckOpen` | Charge cable controller: a036 contactor stuck open | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a037_internalModuleWatchdogExpired` | Charge cable controller: a037 internal module watchdog expired | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a038_internalModuleMia` | Charge cable controller: a038 internal module mia | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a039_internalModuleOverTemp` | Charge cable controller: a039 internal module over temp | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a040_handleTempFoldback` | Charge cable controller: a040 handle temp foldback | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a041_inputWiringFoldback` | Charge cable controller: a041 input wiring foldback | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a042_pcbaTempFoldback` | Charge cable controller: a042 pcba temp foldback | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a043_configurationRequired` | Charge cable controller: a043 configuration required | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a044_relayCoilVoltageRationality` | Charge cable controller: a044 relay coil voltage rationality | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a045_ACPowerLoss` | Charge cable controller: a045 AC power loss | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a046_GFCIConfigInvalid` | Charge cable controller: a046 GFCI config invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a047_MDMotorContFault` | Charge cable controller: a047 MD motor cont fault | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a048_ACMDAdapterFault` | Charge cable controller: a048 ACMD adapter fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a049_rs485Fault` | Charge cable controller: a049 rs485 fault | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a050_eFuseFault` | Charge cable controller: a050 e fuse fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a051_chcCriticalFault` | Charge cable controller: a051 chc critical fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a052_vRefOutOfRangePWM` | Charge cable controller: a052 v ref out of range PWM | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a057_chcVitalsRequestFailure` | Charge cable controller: a057 chc vitals request failure | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a060_persistenceFault` | Charge cable controller: a060 persistence fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a061_unfinishedCommissioning` | Charge cable controller: a061 unfinished commissioning | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
