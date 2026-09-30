---
layout: default
title: "APP_warningMatrix0 (0x329) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (primary) message: warning matrix0. Tesla Model Y CAN bus message APP_warningMatrix0 (0x329) of Driver assistance computer (primary), firmware 2026.26.6.5, 64 signals (APP_w001_DEPRECATED, APP_w002_ldwDisabled, APP_w003_isaDisabled, APP_w004_accDisabled and 60 more). Bit layout, scaling, units and value tables."
---

# APP_warningMatrix0 (0x329) — Driver assistance computer (primary), Tesla Model Y 2026.26.6.5 CH CAN

Driver assistance computer (primary) message: warning matrix0; frame length from the layout, not yet observed on a vehicle bus. This page documents the 64 signals of APP_warningMatrix0 as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_warningMatrix0` |
| CAN id | 0x329 (809) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of APP_warningMatrix0

Tesla Model Y CAN bus signals in `APP_warningMatrix0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_w001_DEPRECATED` | Driver assistance computer (primary): w001 DEPRECATED | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w002_ldwDisabled` | Driver assistance computer (primary): w002 ldw disabled | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w003_isaDisabled` | Driver assistance computer (primary): w003 isa disabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w004_accDisabled` | Driver assistance computer (primary): w004 acc disabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w005_fcwCancelled` | Driver assistance computer (primary): w005 fcw cancelled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w006_aebCancelled` | Driver assistance computer (primary): w006 aeb cancelled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w007_ahlbDisabled` | Driver assistance computer (primary): w007 ahlb disabled | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w008_parkDisabled` | Driver assistance computer (primary): w008 park disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w009_aebFault` | Driver assistance computer (primary): w009 aeb fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w010_radcCalibIssue` | Driver assistance computer (primary): w010 radc calib issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w011_scaEvent` | Driver assistance computer (primary): w011 sca event | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w012_Cam_BootFailure` | Driver assistance computer (primary): w012 cam boot failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w013_Cam_Watchdog` | Driver assistance computer (primary): w013 cam watchdog | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w014_swAssert` | Driver assistance computer (primary): w014 sw assert | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w015_Camera_Failsafes` | Driver assistance computer (primary): w015 camera failsafes | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w016_aeb_e_event` | Driver assistance computer (primary): w016 aeb e event | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w017_Cam_Msg_MIA` | Driver assistance computer (primary): w017 cam msg MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w018_ECU_Power_Issue` | Driver assistance computer (primary): w018 ECU power issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w019_ECU_Stack_Overflow` | Driver assistance computer (primary): w019 ECU stack overflow | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w020_ECU_checkstopError` | Driver assistance computer (primary): w020 ECU checkstop error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w021_ECU_Temperature_Issue` | Driver assistance computer (primary): w021 ECU temperature issue | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w022_ECU_EEPROM_Failure` | Driver assistance computer (primary): w022 ECU EEPROM failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w023_ECU_Cam_Statemismatc` | Driver assistance computer (primary): w023 ECU cam statemismatc | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w024_ECU_Watchdog_Reset` | Driver assistance computer (primary): w024 ECU watchdog reset | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w025_LC_Steering_Override` | Driver assistance computer (primary): w025 LC steering override | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w026_ECU_timingIssue` | Driver assistance computer (primary): w026 ECU timing issue | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w027_ECU_Reset_Fault` | Driver assistance computer (primary): w027 ECU reset fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w028_spi_rx_error` | Driver assistance computer (primary): w028 spi rx error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w029_spi_tx_error` | Driver assistance computer (primary): w029 spi tx error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w030_Heater_Issue` | Driver assistance computer (primary): w030 heater issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w031_canRxError` | Driver assistance computer (primary): w031 can rx error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w032_canTxError` | Driver assistance computer (primary): w032 can tx error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w033_gtwMia` | Driver assistance computer (primary): w033 gtw mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w034_sccmMia` | Driver assistance computer (primary): w034 sccm mia | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w035_espMia` | Driver assistance computer (primary): w035 esp mia | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w036_bdyMia` | Driver assistance computer (primary): w036 bdy mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w037_camTacIssue` | Driver assistance computer (primary): w037 cam tac issue | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w038_camFailure` | Driver assistance computer (primary): w038 cam failure | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w039_sdm_rcm_Mia` | Driver assistance computer (primary): w039 sdm rcm mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w040_autopilotAngleSaturated` | Driver assistance computer (primary): w040 autopilot angle saturated | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w041_autopilotRateSaturated` | Driver assistance computer (primary): w041 autopilot rate saturated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w042_autopilotAborting` | Driver assistance computer (primary): w042 autopilot aborting | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w043_camLongRunTime` | Driver assistance computer (primary): w043 cam long run time | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w044_appMobileyeFailure` | Driver assistance computer (primary): w044 app mobileye failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w045_radMia` | Driver assistance computer (primary): w045 rad mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w046_eepromRecordAbsent` | Driver assistance computer (primary): w046 eeprom record absent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w047_edrEvent` | Driver assistance computer (primary): w047 edr event | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w048_APP_Features_Disabled` | Driver assistance computer (primary): w048 APP features disabled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w049_eyeqVersionMismatch` | Driver assistance computer (primary): w049 eyeq version mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w050_aeb_event` | Driver assistance computer (primary): w050 aeb event | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w051_radcEcuIssue` | Driver assistance computer (primary): w051 radc ecu issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w052_radcSensorIssue` | Driver assistance computer (primary): w052 radc sensor issue | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w053_radcCommIssue` | Driver assistance computer (primary): w053 radc comm issue | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w054_camAutofix` | Driver assistance computer (primary): w054 cam autofix | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w055_radcVersionMismatch` | Driver assistance computer (primary): w055 radc version mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w056_diMia` | Driver assistance computer (primary): w056 di mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w057_mcuMia` | Driver assistance computer (primary): w057 mcu mia | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w058_epbMia` | Driver assistance computer (primary): w058 epb mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w059_parkMia` | Driver assistance computer (primary): w059 park mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w060_fcw_event` | Driver assistance computer (primary): w060 fcw event | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w061_airSuspensionMia` | Driver assistance computer (primary): w061 air suspension mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w062_radcAlignment` | Driver assistance computer (primary): w062 radc alignment | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w063_parkVersionMismatch` | Driver assistance computer (primary): w063 park version mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APP_w064_epasMia` | Driver assistance computer (primary): w064 epas mia | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
