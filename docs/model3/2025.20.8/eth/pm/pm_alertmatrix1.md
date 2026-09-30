---
layout: default
title: "PM_alertMatrix1 (0x384) — PM ECU, Tesla Model 3 2025.20.8 ETH"
description: "PM ECU message: alert matrix1. Ethernet-side message PM_alertMatrix1 of PM ECU for Tesla Model 3 firmware 2025.20.8, 60 signals (PM_a001_absoluteTorque, PM_a002_excessiveAccelTorque, PM_a003_excessiveReversalTorque, PM_a004_excessiveDecelTorque and 56 more). Bit layout, scaling, units and value tables."
---

# PM_alertMatrix1 (0x384) — PM ECU, Tesla Model 3 2025.20.8 ETH

PM ECU message: alert matrix1. This page documents the 60 signals of PM_alertMatrix1 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PM_alertMatrix1` |
| Ethernet-side id | 0x384 (900) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 60 |

## Signals of PM_alertMatrix1

Tesla Model 3 CAN bus signals in `PM_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_a001_absoluteTorque` | PM ECU: a001 absolute torque | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a002_excessiveAccelTorque` | PM ECU: a002 excessive accel torque | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a003_excessiveReversalTorque` | PM ECU: a003 excessive reversal torque | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a004_excessiveDecelTorque` | PM ECU: a004 excessive decel torque | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a005_torqueInNeutralOrPark` | PM ECU: a005 torque in neutral or park | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a006_inconsistentDIGear` | PM ECU: a006 inconsistent DI gear | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a007_ibstMIA` | PM ECU: a007 ibst MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a008_memoryError` | PM ECU: a008 memory error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a009_espMIA` | PM ECU: a009 esp MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a010_diMIA` | PM ECU: a010 di MIA | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a011_systemHvilNotClosed` | PM ECU: a011 system hvil not closed | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a012_canDataBusA` | PM ECU: a012 can data bus a | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a013_canHardwareBusA` | PM ECU: a013 can hardware bus a | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a014_accelPedalError` | PM ECU: a014 accel pedal error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a015_shifterMIA` | PM ECU: a015 shifter MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a016_bbMIA` | PM ECU: a016 bb MIA | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a017_brakeMIA` | PM ECU: a017 brake MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a019_vehicleSpeedQFDiagnostic` | PM ECU: a019 vehicle speed QF diagnostic | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a021_difMIA` | PM ECU: a021 dif MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a022_dirMIA` | PM ECU: a022 dir MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a023_cruiseInhibit` | PM ECU: a023 cruise inhibit | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a024_brakeIrrational` | PM ECU: a024 brake irrational | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a025_unintendedReset` | PM ECU: a025 unintended reset | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a026_diHeartBeatMIA` | PM ECU: a026 di heart beat MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a028_torqueCmdError` | PM ECU: a028 torque cmd error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a029_cruiseRollback` | PM ECU: a029 cruise rollback | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a030_inconsistentAebState` | PM ECU: a030 inconsistent aeb state | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a031_highStackUsage` | PM ECU: a031 high stack usage | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a032_registerConfigError` | PM ECU: a032 register config error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a033_appMIA` | PM ECU: a033 app MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a034_trqCrossCheck` | PM ECU: a034 trq cross check | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a035_udsTransactionInitiated` | PM ECU: a035 uds transaction initiated | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a036_preWatchdog` | PM ECU: a036 pre watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a038_inconsistentTorqueSign` | PM ECU: a038 inconsistent torque sign | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a039_disMIA` | PM ECU: a039 dis MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a040_latLinkLooseBoltDetectedDebug` | PM ECU: a040 lat link loose bolt detected debug | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a041_dasMIA` | PM ECU: a041 das MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a042_gtwMIA` | PM ECU: a042 gtw MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a043_inconsistentConfig` | PM ECU: a043 inconsistent config | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a044_ebrIntervention` | PM ECU: a044 ebr intervention | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a045_regenBackfillIntervention` | PM ECU: a045 regen backfill intervention | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a046_inconsVehicleHoldState` | PM ECU: a046 incons vehicle hold state | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a047_inconsAutoparkState` | PM ECU: a047 incons autopark state | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a048_stabilityControlInhibit` | PM ECU: a048 stability control inhibit | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a049_stbCtrlInWrongDir` | PM ECU: a049 stb ctrl in wrong dir | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a050_excessiveStbCtrlTrq` | PM ECU: a050 excessive stb ctrl trq | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a051_unintDecelStbCtrl` | PM ECU: a051 unint decel stb ctrl | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a052_stbCtrlDrvrDecelCflct` | PM ECU: a052 stb ctrl drvr decel cflct | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a053_vcfrontMIA` | PM ECU: a053 vcfront MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a054_uiMIA` | PM ECU: a054 ui MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a055_accelPedalSyncWarn` | PM ECU: a055 accel pedal sync warn | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a056_canHardwareBusB` | PM ECU: a056 can hardware bus b | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a057_canDataBusB` | PM ECU: a057 can data bus b | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a058_cmpMIA` | PM ECU: a058 cmp MIA | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a059_ptcMIA` | PM ECU: a059 ptc MIA | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a060_onePedalDrivingInhibit` | PM ECU: a060 one pedal driving inhibit | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a061_DIPMVersionMismatch` | PM ECU: a061 DIPM version mismatch | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a062_eccError` | PM ECU: a062 ecc error | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a063_torqueCommandInhibit` | PM ECU: a063 torque command inhibit | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a064_torqueIntervention` | PM ECU: a064 torque intervention | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
