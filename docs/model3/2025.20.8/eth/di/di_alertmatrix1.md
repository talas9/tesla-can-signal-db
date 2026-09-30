---
layout: default
title: "DI_alertMatrix1 (0x367) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: alert matrix1. Ethernet-side message DI_alertMatrix1 of Drive inverter for Tesla Model 3 firmware 2025.20.8, 48 signals (DI_a001_frunkSpeedLimitActive, DI_a002_parkButtonDuringStalkReq, DI_a003_suggestedGearOverride, DI_a004_smartShiftUnavailable and 44 more). Bit layout, scaling, units and value tables."
---

# DI_alertMatrix1 (0x367) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: alert matrix1. This page documents the 48 signals of DI_alertMatrix1 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_alertMatrix1` |
| Ethernet-side id | 0x367 (871) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 48 |

## Signals of DI_alertMatrix1

Tesla Model 3 CAN bus signals in `DI_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_a001_frunkSpeedLimitActive` | Drive inverter: a001 frunk speed limit active | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a002_parkButtonDuringStalkReq` | Drive inverter: a002 park button during stalk req | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a003_suggestedGearOverride` | Drive inverter: a003 suggested gear override | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a004_smartShiftUnavailable` | Drive inverter: a004 smart shift unavailable | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a005_stalkPanicked` | Drive inverter: a005 stalk panicked | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a006_shifterUnavailable` | Drive inverter: a006 shifter unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a007_secGearSelButtonStuck` | Drive inverter: a007 sec gear sel button stuck | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a010_unintendedReset` | Drive inverter: a010 unintended reset | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a012_accel5VSupply` | Drive inverter: a012 accel5 v supply | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a013_eccError` | Drive inverter: a013 ecc error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a014_secGearSelActivated` | Drive inverter: a014 sec gear sel activated | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a015_immobilizer` | Drive inverter: a015 immobilizer | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a016_parkRequestByPM` | Drive inverter: a016 park request by PM | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a017_hwPedalMonitor` | Drive inverter: a017 hw pedal monitor | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a018_hwLVSupplyUV` | Drive inverter: a018 hw LV supply UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a019_hwAccelPedalPower` | Drive inverter: a019 hw accel pedal power | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a020_systemHvilNotClosed` | Drive inverter: a020 system hvil not closed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a021_packOvervoltage` | Drive inverter: a021 pack overvoltage | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a022_hw5vSupplyUV` | Drive inverter: a022 hw5v supply UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a023_carNotParked` | Drive inverter: a023 car not parked | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a024_holdNForNeutral` | Drive inverter: a024 hold n for neutral | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a025_regenBackfillUnavailable` | Drive inverter: a025 regen backfill unavailable | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a026_parkPressedWithHighAPedal` | Drive inverter: a026 park pressed with high a pedal | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a031_closureAccelerationLimit` | Drive inverter: a031 closure acceleration limit | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a036_sysStandbyUnitLimitedWait` | Drive inverter: a036 sys standby unit limited wait | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a038_idleTaskStarving` | Drive inverter: a038 idle task starving | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a039_exceptionUndefinedInstruction` | Drive inverter: a039 exception undefined instruction | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a040_difMIA` | Drive inverter: a040 dif MIA | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a041_driverBrakeApplyStuck` | Drive inverter: a041 driver brake apply stuck | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a042_pmfMIA` | Drive inverter: a042 pmf MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a043_pmrMIA` | Drive inverter: a043 pmr MIA | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a048_ecuLogAvailable` | Drive inverter: a048 ecu log available | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a049_P0632_DI_ECU_OdometerNotProgrammed` | Drive inverter: a049 P0632 DI ECU odometer not programmed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a050_P1234_DI_ECU_DemoTimer` | Drive inverter: a050 P1234 DI ECU demo timer | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a051_batteryOvercurrent` | Drive inverter: a051 battery overcurrent | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a052_dirMIA` | Drive inverter: a052 dir MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a053_canDataBusC` | Drive inverter: a053 can data bus c | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a054_canOverrunBusC` | Drive inverter: a054 can overrun bus c | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a055_canHardwareBusC` | Drive inverter: a055 can hardware bus c | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a056_canDataBusD` | Drive inverter: a056 can data bus d | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a057_canOverrunBusD` | Drive inverter: a057 can overrun bus d | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a058_canHardwareBusD` | Drive inverter: a058 can hardware bus d | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a059_canDataBusE` | Drive inverter: a059 can data bus e | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a060_canOverrunBusE` | Drive inverter: a060 can overrun bus e | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a061_canHardwareBusE` | Drive inverter: a061 can hardware bus e | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a062_systemLimpMode` | Drive inverter: a062 system limp mode | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a063_systemGracefulPowerOff` | Drive inverter: a063 system graceful power off | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a064_pmsrmUnitMiaWithHvDown` | Drive inverter: a064 pmsrm unit mia with hv down | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
