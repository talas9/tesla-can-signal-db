---
layout: default
title: "HVP_alertMatrix (0x3AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: alert matrix. Tesla Model 3 / Model Y CAN bus message HVP_alertMatrix (0x3AA) of High-voltage processor (pack contactor and isolation controller), firmware 2026.26.6.5, 71 signals (HVP_matrixIndex, HVP_w001_WatchdogReset, HVP_w002_UnusedAlert2, HVP_w003_SwAssertion and 67 more). Bit layout, scaling, units and value tables."
---

# HVP_alertMatrix (0x3AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: alert matrix; frame length observed on a vehicle bus. This page documents the 71 signals of HVP_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_alertMatrix` |
| CAN id | 0x3AA (938) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 71 |

## Signals of HVP_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `HVP_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_matrixIndex` | selector | High-voltage processor (pack contactor and isolation controller): matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1` | plausible |
| `HVP_w001_WatchdogReset` | page 0 | High-voltage processor (pack contactor and isolation controller): w001 watchdog reset | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w002_UnusedAlert2` | page 0 | High-voltage processor (pack contactor and isolation controller): w002 unused alert2 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w003_SwAssertion` | page 0 | High-voltage processor (pack contactor and isolation controller): w003 sw assertion | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w004_CrashEvent` | page 0 | High-voltage processor (pack contactor and isolation controller): w004 crash event | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w005_OverDchgCurrentFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w005 over dchg current fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w006_OverChargeCurrentFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w006 over charge current fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w007_OverCurrentFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w007 over current fault | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w008_OverTemperatureFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w008 over temperature fault | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w009_OverVoltageFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w009 over voltage fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w010_UnderVoltageFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w010 under voltage fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w011_PrimaryBmbMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w011 primary bmb mia fault | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w012_BmbDataIntegrityLoss` | page 0 | High-voltage processor (pack contactor and isolation controller): w012 bmb data integrity loss | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w013_BmbCommunication` | page 0 | High-voltage processor (pack contactor and isolation controller): w013 bmb communication | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w014_BmsMiaOnHviFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w014 bms mia on hvi fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w015_CpMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w015 cp mia fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w016_PcsMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w016 pcs mia fault | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w017_GtwMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w017 gtw mia fault | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w018_powerCyclingPcs` | page 0 | High-voltage processor (pack contactor and isolation controller): w018 power cycling pcs | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w019_CpFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w019 cp fault | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w020_ShuntHwMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w020 shunt hw mia fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w021_PyroMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w021 pyro mia fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w022_PyroMiaWarning` | page 0 | High-voltage processor (pack contactor and isolation controller): w022 pyro mia warning | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w023_BmbResetRecovery` | page 0 | High-voltage processor (pack contactor and isolation controller): w023 bmb reset recovery | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w024_Supply12vFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w024 supply12v fault | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w025_VerSupplyFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w025 ver supply fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w026_HvilFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w026 hvil fault | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w027_BmsMiaOnHvsFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w027 bms mia on hvs fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w028_PackVoltMismatchFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w028 pack volt mismatch fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w029_EnsMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w029 ens mia fault | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w030_PackPosCtrArcFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w030 pack pos ctr arc fault | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w031_packNegCtrArcFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w031 pack neg ctr arc fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w032_ShuntHwAndBmsMiaFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w032 shunt hw and bms mia fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w033_fcContHwFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w033 fc cont hw fault | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w034_cpMismatchFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w034 cp mismatch fault | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w035_packContHwFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w035 pack cont hw fault | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w036_pyroFuseBlown` | page 0 | High-voltage processor (pack contactor and isolation controller): w036 pyro fuse blown | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w037_pyroFuseFailedToBlow` | page 0 | High-voltage processor (pack contactor and isolation controller): w037 pyro fuse failed to blow | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w038_CpilFault` | page 0 | High-voltage processor (pack contactor and isolation controller): w038 cpil fault | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w039_PackContactorFellOpen` | page 0 | High-voltage processor (pack contactor and isolation controller): w039 pack contactor fell open | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w040_FcContactorFellOpen` | page 0 | High-voltage processor (pack contactor and isolation controller): w040 fc contactor fell open | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w041_packCtrCloseBlocked` | page 0 | High-voltage processor (pack contactor and isolation controller): w041 pack ctr close blocked | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w042_fcCtrCloseBlocked` | page 0 | High-voltage processor (pack contactor and isolation controller): w042 fc ctr close blocked | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w043_packContactorForceOpen` | page 0 | High-voltage processor (pack contactor and isolation controller): w043 pack contactor force open | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w044_fcContactorForceOpen` | page 0 | High-voltage processor (pack contactor and isolation controller): w044 fc contactor force open | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w045_dcLinkOverVoltage` | page 0 | High-voltage processor (pack contactor and isolation controller): w045 dc link over voltage | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w046_shuntOverTemperature` | page 0 | High-voltage processor (pack contactor and isolation controller): w046 shunt over temperature | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w047_passivePyroDeploy` | page 0 | High-voltage processor (pack contactor and isolation controller): w047 passive pyro deploy | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w048_swUnsupportedBmbAsicType` | page 0 | High-voltage processor (pack contactor and isolation controller): w048 sw unsupported bmb asic type | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w049_packCtrCloseFailed` | page 0 | High-voltage processor (pack contactor and isolation controller): w049 pack ctr close failed | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w050_fcCtrCloseFailed` | page 0 | High-voltage processor (pack contactor and isolation controller): w050 fc ctr close failed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w051_shuntThermistorMia` | page 0 | High-voltage processor (pack contactor and isolation controller): w051 shunt thermistor mia | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w052_BmbStatusRegError` | page 0 | High-voltage processor (pack contactor and isolation controller): w052 bmb status reg error | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w053_hvVoltageSensorRationality` | page 0 | High-voltage processor (pack contactor and isolation controller): w053 hv voltage sensor rationality | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w054_swMissingConfigBlock` | page 0 | High-voltage processor (pack contactor and isolation controller): w054 sw missing config block | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w055_swMissingPartNumber` | page 0 | High-voltage processor (pack contactor and isolation controller): w055 sw missing part number | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w056_contactorFailedToOpen` | page 0 | High-voltage processor (pack contactor and isolation controller): w056 contactor failed to open | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w057_BatmanDiagnosticsError` | page 0 | High-voltage processor (pack contactor and isolation controller): w057 batman diagnostics error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w058_BmbVrefBad` | page 0 | High-voltage processor (pack contactor and isolation controller): w058 bmb vref bad | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w059_BmbVrefWarning` | page 0 | High-voltage processor (pack contactor and isolation controller): w059 bmb vref warning | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w060_StackVoltageSense` | page 0 | High-voltage processor (pack contactor and isolation controller): w060 stack voltage sense | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w061_ShuntCurrentRationality` | page 1 | High-voltage processor (pack contactor and isolation controller): w061 shunt current rationality | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w062_BmbOtpConfigError` | page 1 | High-voltage processor (pack contactor and isolation controller): w062 bmb otp config error | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w063_BmbBrickVRationality` | page 1 | High-voltage processor (pack contactor and isolation controller): w063 bmb brick v rationality | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w064_BmbAuxVRationality` | page 1 | High-voltage processor (pack contactor and isolation controller): w064 bmb aux v rationality | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w065_FastOpenVshDetected` | page 1 | High-voltage processor (pack contactor and isolation controller): w065 fast open vsh detected | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w067_HvilCalNodeMismatch` | page 1 | High-voltage processor (pack contactor and isolation controller): w067 hvil cal node mismatch | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w068_shuntUnexpectedThermistor` | page 1 | High-voltage processor (pack contactor and isolation controller): w068 shunt unexpected thermistor | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w069_hviCanFrameRxDropped` | page 1 | High-voltage processor (pack contactor and isolation controller): w069 hvi can frame rx dropped | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w070_hvsCanFrameRxDropped` | page 1 | High-voltage processor (pack contactor and isolation controller): w070 hvs can frame rx dropped | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_w071_PassivePyroVrefRationality` | page 1 | High-voltage processor (pack contactor and isolation controller): w071 passive pyro vref rationality | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`HVP_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (10 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
