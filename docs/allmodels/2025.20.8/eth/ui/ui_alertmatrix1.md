---
layout: default
title: "UI_alertMatrix1 (0x123) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: alert matrix1. Ethernet-side message UI_alertMatrix1 of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 63 signals (UI_a001_DriverDoorOpen, UI_a002_DoorOpen, UI_a003_TrunkOpen, UI_a004_FrunkOpen and 59 more). Bit layout, scaling, units and value tables."
---

# UI_alertMatrix1 (0x123) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: alert matrix1. This page documents the 63 signals of UI_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_alertMatrix1` |
| Ethernet-side id | 0x123 (291) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of UI_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `UI_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_a001_DriverDoorOpen` | Touchscreen user interface computer: a001 driver door open | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a002_DoorOpen` | Touchscreen user interface computer: a002 door open | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a003_TrunkOpen` | Touchscreen user interface computer: a003 trunk open | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a004_FrunkOpen` | Touchscreen user interface computer: a004 frunk open | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a005_HeadlightsOnDoorOpen` | Touchscreen user interface computer: a005 headlights on door open | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a006_RemoteServiceAlert` | Touchscreen user interface computer: a006 remote service alert | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a007_SoftPackConfigMismatch` | Touchscreen user interface computer: a007 soft pack config mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a008_TouchScreenError` | Touchscreen user interface computer: a008 touch screen error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a009_SquashfsError` | Touchscreen user interface computer: a009 squashfs error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a010_MapsMissing` | Touchscreen user interface computer: a010 maps missing | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a011_IncorrectMap` | Touchscreen user interface computer: a011 incorrect map | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a012_NotOnPrivateProperty` | Touchscreen user interface computer: a012 not on private property | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a013_TPMSHardWarning` | Touchscreen user interface computer: a013 TPMS hard warning | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a014_TPMSSoftWarning` | Touchscreen user interface computer: a014 TPMS soft warning | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a015_TPMSOverPressureWarning` | Touchscreen user interface computer: a015 TPMS over pressure warning | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a016_TPMSTemperatureWarning` | Touchscreen user interface computer: a016 TPMS temperature warning | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a017_TPMSSystemFault` | Touchscreen user interface computer: a017 TPMS system fault | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a018_SlipStartOn` | Touchscreen user interface computer: a018 slip start on | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a019_ParkBrakeFault` | Touchscreen user interface computer: a019 park brake fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a020_SteeringReduced` | Touchscreen user interface computer: a020 steering reduced | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a021_RearSeatbeltUnbuckled` | Touchscreen user interface computer: a021 rear seatbelt unbuckled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a022_ApeFusesEtc` | Touchscreen user interface computer: a022 ape fuses etc | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a023_CellInternetCheckFailed` | Touchscreen user interface computer: a023 cell internet check failed | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a024_WifiInternetCheckFailed` | Touchscreen user interface computer: a024 wifi internet check failed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a026_ModemResetLoopDetected` | Touchscreen user interface computer: a026 modem reset loop detected | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a027_AutoSteerMIA` | Touchscreen user interface computer: a027 auto steer MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a028_FrontTrunkPopupClosed` | Touchscreen user interface computer: a028 front trunk popup closed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a029_ModemMIA` | Touchscreen user interface computer: a029 modem MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a030_ModemVMCrash` | Touchscreen user interface computer: a030 modem VM crash | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a031_BrakeFluidLow` | Touchscreen user interface computer: a031 brake fluid low | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a032_CellModemRecoveryResets` | Touchscreen user interface computer: a032 cell modem recovery resets | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a033_ApTrialExpired` | Touchscreen user interface computer: a033 ap trial expired | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a034_WakeupProblem` | Touchscreen user interface computer: a034 wakeup problem | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a035_FrunkOpenChime` | Touchscreen user interface computer: a035 frunk open chime | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a036_AudioWatchdog` | Touchscreen user interface computer: a036 audio watchdog | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a037_AudioWatchdogXrunStormError` | Touchscreen user interface computer: a037 audio watchdog xrun storm error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a038_AudioWatchdogA2bI2cLockupError` | Touchscreen user interface computer: a038 audio watchdog a2b i2c lockup error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a039_AudioA2bNeedRediscovery` | Touchscreen user interface computer: a039 audio a2b need rediscovery | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a040_HomelinkTransmit` | Touchscreen user interface computer: a040 homelink transmit | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a041_AudioDmesgXrun` | Touchscreen user interface computer: a041 audio dmesg xrun | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a042_AudioDmesgRtThrottling` | Touchscreen user interface computer: a042 audio dmesg rt throttling | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a043_InvalidMapDataOverride` | Touchscreen user interface computer: a043 invalid map data override | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a044_AudioDmesgDspException` | Touchscreen user interface computer: a044 audio dmesg dsp exception | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a045_ECallSystemCheckFailed` | Touchscreen user interface computer: a045 e call system check failed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a046_BackupCameraStreamError` | Touchscreen user interface computer: a046 backup camera stream error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a047_CellRoamingDisallowed` | Touchscreen user interface computer: a047 cell roaming disallowed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a048_AudioPremiumAmpCheckFailed` | Touchscreen user interface computer: a048 audio premium amp check failed | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a049_BrakeShiftRequired` | Touchscreen user interface computer: a049 brake shift required | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a050_BackupCameraIPUTimeout` | Touchscreen user interface computer: a050 backup camera IPU timeout | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a051_BackupCameraFrameTimeout` | Touchscreen user interface computer: a051 backup camera frame timeout | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a052_KernelPanicReported` | Touchscreen user interface computer: a052 kernel panic reported | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a053_QtCarExitError` | Signal reported by Touchscreen user interface computer | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a054_AudioBoostPowerBad` | Touchscreen user interface computer: a054 audio boost power bad | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a055_ManualECallDisabled` | Touchscreen user interface computer: a055 manual e call disabled | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a056_ManualECallButtonDisconnected` | Touchscreen user interface computer: a056 manual e call button disconnected | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a057_CellAntennaDisconnected` | Touchscreen user interface computer: a057 cell antenna disconnected | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a058_GPSAntennaDisconnected` | Touchscreen user interface computer: a058 GPS antenna disconnected | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a059_ECallSpeakerDisconnected` | Touchscreen user interface computer: a059 e call speaker disconnected | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a060_ECallMicDisconnected` | Touchscreen user interface computer: a060 e call mic disconnected | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a061_SIMTestFailed` | Touchscreen user interface computer: a061 SIM test failed | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a062_ENSTestFailed` | Touchscreen user interface computer: a062 ENS test failed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a063_CellularTestFailed` | Touchscreen user interface computer: a063 cellular test failed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a064_ModemFirmwareTestFailed` | Touchscreen user interface computer: a064 modem firmware test failed | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
