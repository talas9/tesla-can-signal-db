---
layout: default
title: "DAS_warningMatrix0 (0x32A) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: warning matrix0. Tesla Model 3 CAN bus message DAS_warningMatrix0 (0x32A) of Driver assistance computer, firmware 2026.26.6.5, 63 signals (DAS_w002_ldwDisabled, DAS_w003_isaDisabled, DAS_w004_accDisabled, DAS_w005_fcwCancelled and 59 more). Bit layout, scaling, units and value tables."
---

# DAS_warningMatrix0 (0x32A) — Driver assistance computer, Tesla Model 3 2026.26.6.5 CH CAN

Driver assistance computer message: warning matrix0; frame length from the layout, not yet observed on a vehicle bus. This page documents the 63 signals of DAS_warningMatrix0 as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_warningMatrix0` |
| CAN id | 0x32A (810) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of DAS_warningMatrix0

Tesla Model 3 CAN bus signals in `DAS_warningMatrix0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_w002_ldwDisabled` | Driver assistance computer: w002 ldw disabled | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w003_isaDisabled` | Driver assistance computer: w003 isa disabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w004_accDisabled` | Driver assistance computer: w004 acc disabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w005_fcwCancelled` | Driver assistance computer: w005 fcw cancelled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w006_aebCancelled` | Driver assistance computer: w006 aeb cancelled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w007_ahlbDisabled` | Driver assistance computer: w007 ahlb disabled | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w008_parkDisabled` | Driver assistance computer: w008 park disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w009_aebFault` | Driver assistance computer: w009 aeb fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w010_radcCalibIssue` | Driver assistance computer: w010 radc calib issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w011_scaEvent` | Driver assistance computer: w011 sca event | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w012_Cam_BootFailure` | Driver assistance computer: w012 cam boot failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w013_Cam_Watchdog` | Driver assistance computer: w013 cam watchdog | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w014_swAssert` | Driver assistance computer: w014 sw assert | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w015_Camera_Failsafes` | Driver assistance computer: w015 camera failsafes | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w016_aeb_e_event` | Driver assistance computer: w016 aeb e event | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w017_Cam_Msg_MIA` | Driver assistance computer: w017 cam msg MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w018_ECU_Power_Issue` | Driver assistance computer: w018 ECU power issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w019_ECU_Stack_Overflow` | Driver assistance computer: w019 ECU stack overflow | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w020_ECU_checkstopError` | Driver assistance computer: w020 ECU checkstop error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w021_ECU_Temperature_Issue` | Driver assistance computer: w021 ECU temperature issue | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w022_ECU_EEPROM_Failure` | Driver assistance computer: w022 ECU EEPROM failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w023_ECU_Cam_Statemismatc` | Driver assistance computer: w023 ECU cam statemismatc | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w024_ECU_Watchdog_Reset` | Driver assistance computer: w024 ECU watchdog reset | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w025_LC_Steering_Override` | Driver assistance computer: w025 LC steering override | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w026_ECU_timingIssue` | Driver assistance computer: w026 ECU timing issue | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w027_ECU_Reset_Fault` | Driver assistance computer: w027 ECU reset fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w028_spi_rx_error` | Driver assistance computer: w028 spi rx error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w029_spi_tx_error` | Driver assistance computer: w029 spi tx error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w030_Heater_Issue` | Driver assistance computer: w030 heater issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w031_canRxError` | Driver assistance computer: w031 can rx error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w032_canTxError` | Driver assistance computer: w032 can tx error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w033_gtwMia` | Driver assistance computer: w033 gtw mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w034_sccmMia` | Driver assistance computer: w034 sccm mia | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w035_espMia` | Driver assistance computer: w035 esp mia | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w036_bdyMia` | Driver assistance computer: w036 bdy mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w037_camTacIssue` | Driver assistance computer: w037 cam tac issue | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w038_camFailure` | Driver assistance computer: w038 cam failure | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w039_sdm_rcm_Mia` | Driver assistance computer: w039 sdm rcm mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w040_autopilotAngleSaturated` | Driver assistance computer: w040 autopilot angle saturated | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w041_autopilotRateSaturated` | Driver assistance computer: w041 autopilot rate saturated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w042_autopilotAborting` | Driver assistance computer: w042 autopilot aborting | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w043_camLongRunTime` | Driver assistance computer: w043 cam long run time | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w044_appMobileyeFailure` | Driver assistance computer: w044 app mobileye failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w045_radMia` | Driver assistance computer: w045 rad mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w046_eepromRecordAbsent` | Driver assistance computer: w046 eeprom record absent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w047_edrEvent` | Driver assistance computer: w047 edr event | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w048_DAS_Features_Disabled` | Driver assistance computer: w048 DAS features disabled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w049_eyeqVersionMismatch` | Driver assistance computer: w049 eyeq version mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w050_aeb_event` | Driver assistance computer: w050 aeb event | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w051_radcEcuIssue` | Driver assistance computer: w051 radc ecu issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w052_radcSensorIssue` | Driver assistance computer: w052 radc sensor issue | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w053_radcCommIssue` | Driver assistance computer: w053 radc comm issue | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w054_camAutofix` | Driver assistance computer: w054 cam autofix | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w055_radcVersionMismatch` | Driver assistance computer: w055 radc version mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w056_diMia` | Driver assistance computer: w056 di mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w057_mcuMia` | Driver assistance computer: w057 mcu mia | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w058_epbMia` | Driver assistance computer: w058 epb mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w059_parkMia` | Driver assistance computer: w059 park mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w060_fcw_event` | Driver assistance computer: w060 fcw event | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w061_airSuspensionMia` | Driver assistance computer: w061 air suspension mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w062_radcAlignment` | Driver assistance computer: w062 radc alignment | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w063_parkVersionMismatch` | Driver assistance computer: w063 park version mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_w064_epasMia` | Driver assistance computer: w064 epas mia | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
