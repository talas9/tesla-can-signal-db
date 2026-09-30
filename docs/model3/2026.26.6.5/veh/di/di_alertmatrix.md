---
layout: default
title: "DI_alertMatrix (0x367) — Drive inverter, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Drive inverter message: alert matrix. Tesla Model 3 CAN bus message DI_alertMatrix (0x367) of Drive inverter, firmware 2026.26.6.5, 220 signals (DI_matrixIndex, DI_a001_frunkSpeedLimitActive, DI_a002_parkButtonDuringStalkReq, DI_a003_suggestedGearOverride and 216 more). Bit layout, scaling, units and value tables."
---

# DI_alertMatrix (0x367) — Drive inverter, Tesla Model 3 2026.26.6.5 VEH CAN

Drive inverter message: alert matrix; frame length from the layout, not yet observed on a vehicle bus. This page documents the 220 signals of DI_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_alertMatrix` |
| CAN id | 0x367 (871) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 220 |

## Signals of DI_alertMatrix

Tesla Model 3 CAN bus signals in `DI_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DI_matrixIndex` | selector | Drive inverter: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4` | plausible |
| `DI_a001_frunkSpeedLimitActive` | page 0 | Drive inverter: a001 frunk speed limit active | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a002_parkButtonDuringStalkReq` | page 0 | Drive inverter: a002 park button during stalk req | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a003_suggestedGearOverride` | page 0 | Drive inverter: a003 suggested gear override | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a004_smartShiftUnavailable` | page 0 | Drive inverter: a004 smart shift unavailable | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a005_stalkPanicked` | page 0 | Drive inverter: a005 stalk panicked | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a006_shifterUnavailable` | page 0 | Drive inverter: a006 shifter unavailable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a007_secGearSelButtonStuck` | page 0 | Drive inverter: a007 sec gear sel button stuck | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a010_unintendedReset` | page 0 | Drive inverter: a010 unintended reset | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a012_accel5VSupply` | page 0 | Drive inverter: a012 accel5 v supply | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a013_eccError` | page 0 | Drive inverter: a013 ecc error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a014_secGearSelActivated` | page 0 | Drive inverter: a014 sec gear sel activated | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a015_immobilizer` | page 0 | Drive inverter: a015 immobilizer | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a016_parkRequestByPM` | page 0 | Drive inverter: a016 park request by PM | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a017_hwPedalMonitor` | page 0 | Drive inverter: a017 hw pedal monitor | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a018_hwLVSupplyUV` | page 0 | Drive inverter: a018 hw LV supply UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a019_hwAccelPedalPower` | page 0 | Drive inverter: a019 hw accel pedal power | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a020_systemHvilNotClosed` | page 0 | Drive inverter: a020 system hvil not closed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a021_packOvervoltage` | page 0 | Drive inverter: a021 pack overvoltage | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a022_hw5vSupplyUV` | page 0 | Drive inverter: a022 hw5v supply UV | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a023_carNotParked` | page 0 | Drive inverter: a023 car not parked | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a024_holdNForNeutral` | page 0 | Drive inverter: a024 hold n for neutral | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a025_regenBackfillUnavailable` | page 0 | Drive inverter: a025 regen backfill unavailable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a026_parkPressedWithHighAPedal` | page 0 | Drive inverter: a026 park pressed with high a pedal | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a027_steeringAngleOffsetService` | page 0 | Drive inverter: a027 steering angle offset service | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a028_secondaryShifterMuted` | page 0 | Drive inverter: a028 secondary shifter muted | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a031_closureAccelerationLimit` | page 0 | Drive inverter: a031 closure acceleration limit | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a036_sysStandbyUnitLimitedWait` | page 0 | Drive inverter: a036 sys standby unit limited wait | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a039_exceptionUndefinedInstruction` | page 0 | Drive inverter: a039 exception undefined instruction | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a040_difMIA` | page 0 | Drive inverter: a040 dif MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a041_driverBrakeApplyStuck` | page 0 | Drive inverter: a041 driver brake apply stuck | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a042_pmfMIA` | page 0 | Drive inverter: a042 pmf MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a043_pmrMIA` | page 0 | Drive inverter: a043 pmr MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d047_interfacePowerSupplyIssue` | page 0 | Drive inverter: d047 interface power supply issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a048_ecuLogAvailable` | page 0 | Drive inverter: a048 ecu log available | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d049_invalidOdometerReading` | page 0 | Drive inverter: d049 invalid odometer reading | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d050_interfaceUnitCommunicationIssue` | page 0 | Drive inverter: d050 interface unit communication issue | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a051_batteryOvercurrent` | page 0 | Drive inverter: a051 battery overcurrent | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a052_dirMIA` | page 0 | Drive inverter: a052 dir MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a053_canDataBusC` | page 0 | Drive inverter: a053 can data bus c | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a054_canOverrunBusC` | page 0 | Drive inverter: a054 can overrun bus c | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a055_canHardwareBusC` | page 0 | Drive inverter: a055 can hardware bus c | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a056_canDataBusD` | page 0 | Drive inverter: a056 can data bus d | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a057_canOverrunBusD` | page 0 | Drive inverter: a057 can overrun bus d | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a058_canHardwareBusD` | page 0 | Drive inverter: a058 can hardware bus d | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a059_canDataBusE` | page 0 | Drive inverter: a059 can data bus e | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a060_canOverrunBusE` | page 0 | Drive inverter: a060 can overrun bus e | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a061_canHardwareBusE` | page 1 | Drive inverter: a061 can hardware bus e | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a062_systemLimpMode` | page 1 | Drive inverter: a062 system limp mode | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a063_systemGracefulPowerOff` | page 1 | Drive inverter: a063 system graceful power off | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a064_pmsrmUnitMiaWithHvDown` | page 1 | Drive inverter: a064 pmsrm unit mia with hv down | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a065_canHardwareBusB` | page 1 | Drive inverter: a065 can hardware bus b | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a066_canDataBusB` | page 1 | Drive inverter: a066 can data bus b | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a067_canOverrunBusB` | page 1 | Drive inverter: a067 can overrun bus b | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a068_secondaryWheelSpeedIrrational` | page 1 | Drive inverter: a068 secondary wheel speed irrational | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a070_udsTransactionInitiated` | page 1 | Drive inverter: a070 uds transaction initiated | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d072_accelPedalSensorIssue` | page 1 | Drive inverter: d072 accel pedal sensor issue | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d073_accelPedalVoltSupplyIssue` | page 1 | Drive inverter: d073 accel pedal volt supply issue | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a074_unintendedResetAutoshift` | page 1 | Drive inverter: a074 unintended reset autoshift | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_d075_incorrectImmobilizerKey` | page 1 | Drive inverter: d075 incorrect immobilizer key | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a076_lvSupplyOV` | page 1 | Drive inverter: a076 lv supply OV | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a077_lvSupplyUV` | page 1 | Drive inverter: a077 lv supply UV | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a078_adcRefLow` | page 1 | Drive inverter: a078 adc ref low | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a079_adcRefHigh` | page 1 | Drive inverter: a079 adc ref high | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a080_accelSynch` | page 1 | Drive inverter: a080 accel synch | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a081_accelTrack1` | page 1 | Drive inverter: a081 accel track1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a082_accelTrack2` | page 1 | Drive inverter: a082 accel track2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a083_brakePedalSensor` | page 1 | Drive inverter: a083 brake pedal sensor | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a084_eccTestData0` | page 1 | Drive inverter: a084 ecc test data0 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a085_proximityInEnable` | page 1 | Drive inverter: a085 proximity in enable | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a086_dpbMIA` | page 1 | Drive inverter: a086 dpb MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a087_gtwMIA` | page 1 | Drive inverter: a087 gtw MIA | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a088_uiMIA` | page 1 | Drive inverter: a088 ui MIA | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a089_sccmMIA` | page 1 | Drive inverter: a089 sccm MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a090_pmMIA` | page 1 | Drive inverter: a090 pm MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a091_espMIA` | page 1 | Drive inverter: a091 esp MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a092_bmsMIA` | page 1 | Drive inverter: a092 bms MIA | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a093_canHardwareBusA` | page 1 | Drive inverter: a093 can hardware bus a | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a094_canDataBusA` | page 1 | Drive inverter: a094 can data bus a | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a095_canOverrunBusA` | page 1 | Drive inverter: a095 can overrun bus a | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a096_memoryError` | page 1 | Drive inverter: a096 memory error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a097_eepromError` | page 1 | Drive inverter: a097 eeprom error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a098_eepromManagerError` | page 1 | Drive inverter: a098 eeprom manager error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a099_threadOverrun` | page 1 | Drive inverter: a099 thread overrun | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a100_nvramError` | page 1 | Drive inverter: a100 nvram error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a101_eccTestData1` | page 1 | Drive inverter: a101 ecc test data1 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a102_exceptionPrefetchAbort` | page 1 | Drive inverter: a102 exception prefetch abort | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a103_bbMIA` | page 1 | Drive inverter: a103 bb MIA | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a104_proximityIrrational` | page 1 | Drive inverter: a104 proximity irrational | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a105_cpMIA` | page 1 | Drive inverter: a105 cp MIA | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a106_idleTaskStarving` | page 1 | Drive inverter: a106 idle task starving | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a107_idbBrakeCircuitPressureOffsetSuspect` | page 1 | Drive inverter: a107 idb brake circuit pressure offset suspect | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a108_appMIA` | page 1 | Drive inverter: a108 app MIA | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a109_ahbWriteError` | page 1 | Drive inverter: a109 ahb write error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a110_brakeMIA` | page 1 | Drive inverter: a110 brake MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a111_idbMIA` | page 1 | Drive inverter: a111 idb MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a112_accelTrack1Incons` | page 1 | Drive inverter: a112 accel track1 incons | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a113_lowBrakeMCPressure` | page 1 | Drive inverter: a113 low brake MC pressure | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a114_exceptionDataAbort` | page 1 | Drive inverter: a114 exception data abort | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a115_exceptionDataAbort2` | page 1 | Drive inverter: a115 exception data abort2 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a116_motorRecovered` | page 1 | Drive inverter: a116 motor recovered | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a117_latentFaultCheckTripped` | page 1 | Drive inverter: a117 latent fault check tripped | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a118_diImmobilizedForFactoryFailsafe` | page 1 | Drive inverter: a118 di immobilized for factory failsafe | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a119_latentFaultCheckFailedOnce` | page 1 | Drive inverter: a119 latent fault check failed once | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a120_regenBlendingUnavailable` | page 1 | Drive inverter: a120 regen blending unavailable | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a121_qualifiedBrakeEventMitigation` | page 2 | Drive inverter: a121 qualified brake event mitigation | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a122_highStackUsage` | page 2 | Drive inverter: a122 high stack usage | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a124_cruiseFault` | page 2 | Drive inverter: a124 cruise fault | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a125_noBatteryPower` | page 2 | Drive inverter: a125 no battery power | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a129_epbNotApplied` | page 2 | Drive inverter: a129 epb not applied | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a130_aebFault` | page 2 | Drive inverter: a130 aeb fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a131_highSpeedWearLimit` | page 2 | Drive inverter: a131 high speed wear limit | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a133_vehicleHoldTimedOut` | page 2 | Drive inverter: a133 vehicle hold timed out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a134_wheelSpeedIrrational` | page 2 | Drive inverter: a134 wheel speed irrational | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a135_vehicleHoldFault` | page 2 | Drive inverter: a135 vehicle hold fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a137_noCapableDriveUnits` | page 2 | Drive inverter: a137 no capable drive units | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a138_frontUnitDisabled` | page 2 | Drive inverter: a138 front unit disabled | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a139_rearUnitDisabled` | page 2 | Drive inverter: a139 rear unit disabled | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a140_ptcMIA` | page 2 | Drive inverter: a140 ptc MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a141_dasMIA` | page 2 | Drive inverter: a141 das MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a142_potholeDetected` | page 2 | Drive inverter: a142 pothole detected | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a143_mcuLimitActive` | page 2 | Drive inverter: a143 mcu limit active | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a144_configMismatch` | page 2 | Drive inverter: a144 config mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a146_pbrkPanicEpbFault` | page 2 | Drive inverter: a146 pbrk panic epb fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a154_vdcRearSteering` | page 2 | Drive inverter: a154 vdc rear steering | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a155_vcfrontMIA` | page 2 | Drive inverter: a155 vcfront MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a157_rcmMIA` | page 2 | Drive inverter: a157 rcm MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a158_ibstMIA` | page 2 | Drive inverter: a158 ibst MIA | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a159_cruiseSelfCheck` | page 2 | Drive inverter: a159 cruise self check | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a160_fastLearnComplete` | page 2 | Drive inverter: a160 fast learn complete | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a161_epas3pMIA` | page 2 | Drive inverter: a161 epas3p MIA | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a162_shiftDenied` | page 2 | Drive inverter: a162 shift denied | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a163_shiftMotorSpeed` | page 2 | Drive inverter: a163 shift motor speed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a164_brakeOverride` | page 2 | Drive inverter: a164 brake override | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a165_cruiseCancelled` | page 2 | Drive inverter: a165 cruise cancelled | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a166_driverLeft` | page 2 | Drive inverter: a166 driver left | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a167_keyNotAuthenticated` | page 2 | Drive inverter: a167 key not authenticated | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a168_proximityDriveDenial` | page 2 | Drive inverter: a168 proximity drive denial | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a169_regenOffOverride` | page 2 | Drive inverter: a169 regen off override | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a170_tireConfigUpdated` | page 2 | Drive inverter: a170 tire config updated | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a171_driveRailNotRequested` | page 2 | Drive inverter: a171 drive rail not requested | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a172_accelPressedInNP` | page 2 | Drive inverter: a172 accel pressed in NP | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a173_bothPedalsPressed` | page 2 | Drive inverter: a173 both pedals pressed | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a174_notOkToStartDrive` | page 2 | Drive inverter: a174 not ok to start drive | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a175_crsNotAvailable` | page 2 | Drive inverter: a175 crs not available | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a176_EBRreleased` | page 2 | Drive inverter: a176 EB rreleased | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a177_tireFitmentChanged` | page 2 | Drive inverter: a177 tire fitment changed | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a178_steeringAngleOffsetFault` | page 2 | Drive inverter: a178 steering angle offset fault | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a179_steeringAngleOffsetWarning` | page 2 | Drive inverter: a179 steering angle offset warning | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a180_crsSeatbeltUnbuckled` | page 2 | Drive inverter: a180 crs seatbelt unbuckled | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a181_rearMotorMode` | page 3 | Drive inverter: a181 rear motor mode | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a182_frontMotorMode` | page 3 | Drive inverter: a182 front motor mode | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a183_holdReleaseRqrd` | page 3 | Drive inverter: a183 hold release rqrd | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a184_autoparkCanceled` | page 3 | Drive inverter: a184 autopark canceled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a185_autoparkAborted` | page 3 | Drive inverter: a185 autopark aborted | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a186_brakeStand` | page 3 | Drive inverter: a186 brake stand | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a187_pedalMisapplication` | page 3 | Drive inverter: a187 pedal misapplication | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a188_tireRotationRecommendedGhosted` | page 3 | Drive inverter: a188 tire rotation recommended ghosted | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a189_garageShiftWithPedal` | page 3 | Drive inverter: a189 garage shift with pedal | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a190_tireRotationRecommended` | page 3 | Drive inverter: a190 tire rotation recommended | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a191_brakeShiftReq` | page 3 | Drive inverter: a191 brake shift req | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a192_invalidOdometer` | page 3 | Drive inverter: a192 invalid odometer | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a193_vdcBrakeTorqueFr` | page 3 | Drive inverter: a193 vdc brake torque fr | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a194_vdcBrakeTorqueRe` | page 3 | Drive inverter: a194 vdc brake torque re | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a195_vdcEspSlipFr` | page 3 | Drive inverter: a195 vdc esp slip fr | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a196_vdcEspSlipRe` | page 3 | Drive inverter: a196 vdc esp slip re | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a197_vdcEspWheelSaturations` | page 3 | Drive inverter: a197 vdc esp wheel saturations | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a198_vdcEspMCPressAndSteering` | page 3 | Drive inverter: a198 vdc esp MC press and steering | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a199_vdcFaulted` | page 3 | Drive inverter: a199 vdc faulted | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a200_vdcModelBasedPlausibility` | page 3 | Drive inverter: a200 vdc model based plausibility | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a201_decelTorqueLimited` | page 3 | Drive inverter: a201 decel torque limited | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a202_excessHeatUnavailable` | page 3 | Drive inverter: a202 excess heat unavailable | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a203_TCReducedByADD` | page 3 | Drive inverter: a203 TC reduced by ADD | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a204_vdcRcmLongitudinal` | page 3 | Drive inverter: a204 vdc rcm longitudinal | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a205_vdcRcmLateral` | page 3 | Drive inverter: a205 vdc rcm lateral | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a206_vdcRcmVertical` | page 3 | Drive inverter: a206 vdc rcm vertical | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a207_vdcPowertrainTorque_dif` | page 3 | Drive inverter: a207 vdc powertrain torque dif | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a208_vdcPowertrainTorque_dir` | page 3 | Drive inverter: a208 vdc powertrain torque dir | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a210_vdcOtherControllerStates` | page 3 | Drive inverter: a210 vdc other controller states | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a211_vdcMotorSpeed_dif` | page 3 | Drive inverter: a211 vdc motor speed dif | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a212_vdcWheelRotations` | page 3 | Drive inverter: a212 vdc wheel rotations | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a213_lowMuProbabilityChange` | page 3 | Drive inverter: a213 low mu probability change | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a214_vdcWheelSpeedFr` | page 3 | Drive inverter: a214 vdc wheel speed fr | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a215_vdcWheelSpeedRe` | page 3 | Drive inverter: a215 vdc wheel speed re | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a216_vdcMBPAlmostTripped` | page 3 | Drive inverter: a216 vdc MBP almost tripped | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a217_vdcOutputIrrational` | page 3 | Drive inverter: a217 vdc output irrational | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a218_vdcOSPreControlActive` | page 3 | Drive inverter: a218 vdc OS pre control active | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a219_vdcOversteerdMzActive` | page 3 | Drive inverter: a219 vdc oversteerd mz active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a220_vdcUndersteerDecelActive` | page 3 | Drive inverter: a220 vdc understeer decel active | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a221_vdcUndersteerdMzActive` | page 3 | Drive inverter: a221 vdc understeerd mz active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a222_vdcDisabled` | page 3 | Drive inverter: a222 vdc disabled | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a223_tractionControlDisabled` | page 3 | Drive inverter: a223 traction control disabled | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a224_brakeOverTemp` | page 3 | Drive inverter: a224 brake over temp | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a225_vyEstimatorDegradedDebug` | page 3 | Drive inverter: a225 vy estimator degraded debug | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a226_sysStartConditionNotMet` | page 3 | Drive inverter: a226 sys start condition not met | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a227_contactorsNotClosed` | page 3 | Drive inverter: a227 contactors not closed | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a228_brakeTempEstUnavailable` | page 3 | Drive inverter: a228 brake temp est unavailable | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a230_cmpMIA` | page 3 | Drive inverter: a230 cmp MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a231_softSystemLimpMode` | page 3 | Drive inverter: a231 soft system limp mode | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a232_velocityEstimatorDegraded` | page 3 | Drive inverter: a232 velocity estimator degraded | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a233_frontWheelImpactDetected` | page 3 | Drive inverter: a233 front wheel impact detected | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a235_trackModeActive` | page 3 | Drive inverter: a235 track mode active | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a236_tasMIA` | page 3 | Drive inverter: a236 tas MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a237_undersideAbuse` | page 3 | Drive inverter: a237 underside abuse | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a238_secondaryCollisionMitigationActive` | page 3 | Drive inverter: a238 secondary collision mitigation active | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a239_neutralRequestByPM` | page 3 | Drive inverter: a239 neutral request by PM | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a240_torqueSplitStuck` | page 3 | Drive inverter: a240 torque split stuck | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a241_vdcMotorSpeed_dir` | page 4 | Drive inverter: a241 vdc motor speed dir | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a242_vdcTrailerSwayDetected` | page 4 | Drive inverter: a242 vdc trailer sway detected | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a243_rcuMIA` | page 4 | Drive inverter: a243 rcu MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a244_vseRLSMassMismatch` | page 4 | Drive inverter: a244 vse RLS mass mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a245_opdReducedWithoutEbr` | page 4 | Drive inverter: a245 opd reduced without ebr | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a246_opdUnavailable` | page 4 | Drive inverter: a246 opd unavailable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a248_vdcPreControlHighDynamicActive` | page 4 | Drive inverter: a248 vdc pre control high dynamic active | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a249_spinDownLearningInProgress` | page 4 | Drive inverter: a249 spin down learning in progress | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a250_tasSpeedLimitActive` | page 4 | Drive inverter: a250 tas speed limit active | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a251_diPowerOnStateMismatch` | page 4 | Drive inverter: a251 di power on state mismatch | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a253_accelSynchWarn` | page 4 | Drive inverter: a253 accel synch warn | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a254_vehicleStuckDetected` | page 4 | Drive inverter: a254 vehicle stuck detected | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a255_manualRecoveryMode` | page 4 | Drive inverter: a255 manual recovery mode | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`DI_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (46 signals), page 1 (58 signals), page 2 (45 signals), page 3 (57 signals), page 4 (13 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
