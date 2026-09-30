---
layout: default
title: "APS_warningMatrix0 (0x32B) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: warning matrix0. Tesla Model 3 / Model Y CAN bus message APS_warningMatrix0 (0x32B) of Driver assistance computer (secondary), firmware 2026.26.6.5, 64 signals (APS_w001_DEPRECATED, APS_w002_ldwDisabled, APS_w003_isaDisabled, APS_w004_accDisabled and 60 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix0 (0x32B) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: warning matrix0; frame length from the layout, not yet observed on a vehicle bus. This page documents the 64 signals of APS_warningMatrix0 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix0` |
| CAN id | 0x32B (811) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of APS_warningMatrix0

Tesla Model 3 / Model Y CAN bus signals in `APS_warningMatrix0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_w001_DEPRECATED` | Driver assistance computer (secondary): w001 DEPRECATED | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w002_ldwDisabled` | Driver assistance computer (secondary): w002 ldw disabled | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w003_isaDisabled` | Driver assistance computer (secondary): w003 isa disabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w004_accDisabled` | Driver assistance computer (secondary): w004 acc disabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w005_fcwCancelled` | Driver assistance computer (secondary): w005 fcw cancelled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w006_aebCancelled` | Driver assistance computer (secondary): w006 aeb cancelled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w007_ahlbDisabled` | Driver assistance computer (secondary): w007 ahlb disabled | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w008_parkDisabled` | Driver assistance computer (secondary): w008 park disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w009_aebFault` | Driver assistance computer (secondary): w009 aeb fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w010_radcCalibIssue` | Driver assistance computer (secondary): w010 radc calib issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w011_scaEvent` | Driver assistance computer (secondary): w011 sca event | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w012_Cam_BootFailure` | Driver assistance computer (secondary): w012 cam boot failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w013_Cam_Watchdog` | Driver assistance computer (secondary): w013 cam watchdog | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w014_swAssert` | Driver assistance computer (secondary): w014 sw assert | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w015_Camera_Failsafes` | Driver assistance computer (secondary): w015 camera failsafes | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w016_aeb_e_event` | Driver assistance computer (secondary): w016 aeb e event | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w017_Cam_Msg_MIA` | Driver assistance computer (secondary): w017 cam msg MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w018_ECU_Power_Issue` | Driver assistance computer (secondary): w018 ECU power issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w019_ECU_Stack_Overflow` | Driver assistance computer (secondary): w019 ECU stack overflow | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w020_ECU_checkstopError` | Driver assistance computer (secondary): w020 ECU checkstop error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w021_ECU_Temperature_Issue` | Driver assistance computer (secondary): w021 ECU temperature issue | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w022_ECU_EEPROM_Failure` | Driver assistance computer (secondary): w022 ECU EEPROM failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w023_ECU_Cam_Statemismatc` | Driver assistance computer (secondary): w023 ECU cam statemismatc | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w024_ECU_Watchdog_Reset` | Driver assistance computer (secondary): w024 ECU watchdog reset | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w025_LC_Steering_Override` | Driver assistance computer (secondary): w025 LC steering override | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w026_ECU_timingIssue` | Driver assistance computer (secondary): w026 ECU timing issue | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w027_ECU_Reset_Fault` | Driver assistance computer (secondary): w027 ECU reset fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w028_spi_rx_error` | Driver assistance computer (secondary): w028 spi rx error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w029_spi_tx_error` | Driver assistance computer (secondary): w029 spi tx error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w030_Heater_Issue` | Driver assistance computer (secondary): w030 heater issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w031_canRxError` | Driver assistance computer (secondary): w031 can rx error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w032_canTxError` | Driver assistance computer (secondary): w032 can tx error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w033_gtwMia` | Driver assistance computer (secondary): w033 gtw mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w034_sccmMia` | Driver assistance computer (secondary): w034 sccm mia | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w035_espMia` | Driver assistance computer (secondary): w035 esp mia | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w036_bdyMia` | Driver assistance computer (secondary): w036 bdy mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w037_camTacIssue` | Driver assistance computer (secondary): w037 cam tac issue | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w038_camFailure` | Driver assistance computer (secondary): w038 cam failure | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w039_sdm_rcm_Mia` | Driver assistance computer (secondary): w039 sdm rcm mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w040_autopilotAngleSaturated` | Driver assistance computer (secondary): w040 autopilot angle saturated | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w041_autopilotRateSaturated` | Driver assistance computer (secondary): w041 autopilot rate saturated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w042_autopilotAborting` | Driver assistance computer (secondary): w042 autopilot aborting | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w043_camLongRunTime` | Driver assistance computer (secondary): w043 cam long run time | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w044_appMobileyeFailure` | Driver assistance computer (secondary): w044 app mobileye failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w045_radMia` | Driver assistance computer (secondary): w045 rad mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w046_eepromRecordAbsent` | Driver assistance computer (secondary): w046 eeprom record absent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w047_edrEvent` | Driver assistance computer (secondary): w047 edr event | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w048_DAS_Features_Disabled` | Driver assistance computer (secondary): w048 DAS features disabled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w049_eyeqVersionMismatch` | Driver assistance computer (secondary): w049 eyeq version mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w050_aeb_event` | Driver assistance computer (secondary): w050 aeb event | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w051_radcEcuIssue` | Driver assistance computer (secondary): w051 radc ecu issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w052_radcSensorIssue` | Driver assistance computer (secondary): w052 radc sensor issue | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w053_radcCommIssue` | Driver assistance computer (secondary): w053 radc comm issue | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w054_camAutofix` | Driver assistance computer (secondary): w054 cam autofix | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w055_radcVersionMismatch` | Driver assistance computer (secondary): w055 radc version mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w056_diMia` | Driver assistance computer (secondary): w056 di mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w057_mcuMia` | Driver assistance computer (secondary): w057 mcu mia | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w058_epbMia` | Driver assistance computer (secondary): w058 epb mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w059_parkMia` | Driver assistance computer (secondary): w059 park mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w060_fcw_event` | Driver assistance computer (secondary): w060 fcw event | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w061_tasMia` | Driver assistance computer (secondary): w061 tas mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w062_radcAlignment` | Driver assistance computer (secondary): w062 radc alignment | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w063_parkVersionMismatch` | Driver assistance computer (secondary): w063 park version mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w064_epasMia` | Driver assistance computer (secondary): w064 epas mia | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
