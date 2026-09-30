---
layout: default
title: "APSB_warningMatrix0 (0x34D) — APSB ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: warning matrix0. Ethernet-side message APSB_warningMatrix0 of APSB ECU for Tesla Model 3 / Model Y firmware 2026.26.6.5, 64 signals (APSB_w001_DEPRECATED, APSB_w002_ldwDisabled, APSB_w003_isaDisabled, APSB_w004_accDisabled and 60 more). Bit layout, scaling, units and value tables."
---

# APSB_warningMatrix0 (0x34D) — APSB ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH

APSB ECU message: warning matrix0. This page documents the 64 signals of APSB_warningMatrix0 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_warningMatrix0` |
| Ethernet-side id | 0x34D (845) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of APSB_warningMatrix0

Tesla Model 3 / Model Y CAN bus signals in `APSB_warningMatrix0`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_w001_DEPRECATED` | APSB ECU: w001 DEPRECATED | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w002_ldwDisabled` | APSB ECU: w002 ldw disabled | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w003_isaDisabled` | APSB ECU: w003 isa disabled | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w004_accDisabled` | APSB ECU: w004 acc disabled | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w005_fcwCancelled` | APSB ECU: w005 fcw cancelled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w006_aebCancelled` | APSB ECU: w006 aeb cancelled | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w007_ahlbDisabled` | APSB ECU: w007 ahlb disabled | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w008_parkDisabled` | APSB ECU: w008 park disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w009_aebFault` | APSB ECU: w009 aeb fault | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w010_radcCalibIssue` | APSB ECU: w010 radc calib issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w011_scaEvent` | APSB ECU: w011 sca event | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w012_Cam_BootFailure` | APSB ECU: w012 cam boot failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w013_Cam_Watchdog` | APSB ECU: w013 cam watchdog | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w014_swAssert` | APSB ECU: w014 sw assert | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w015_Camera_Failsafes` | APSB ECU: w015 camera failsafes | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w016_aeb_e_event` | APSB ECU: w016 aeb e event | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w017_Cam_Msg_MIA` | APSB ECU: w017 cam msg MIA | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w018_ECU_Power_Issue` | APSB ECU: w018 ECU power issue | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w019_ECU_Stack_Overflow` | APSB ECU: w019 ECU stack overflow | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w020_ECU_checkstopError` | APSB ECU: w020 ECU checkstop error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w021_ECU_Temperature_Issue` | APSB ECU: w021 ECU temperature issue | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w022_ECU_EEPROM_Failure` | APSB ECU: w022 ECU EEPROM failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w023_ECU_Cam_Statemismatc` | APSB ECU: w023 ECU cam statemismatc | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w024_ECU_Watchdog_Reset` | APSB ECU: w024 ECU watchdog reset | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w025_LC_Steering_Override` | APSB ECU: w025 LC steering override | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w026_ECU_timingIssue` | APSB ECU: w026 ECU timing issue | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w027_ECU_Reset_Fault` | APSB ECU: w027 ECU reset fault | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w028_spi_rx_error` | APSB ECU: w028 spi rx error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w029_spi_tx_error` | APSB ECU: w029 spi tx error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w030_Heater_Issue` | APSB ECU: w030 heater issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w031_canRxError` | APSB ECU: w031 can rx error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w032_canTxError` | APSB ECU: w032 can tx error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w033_gtwMia` | APSB ECU: w033 gtw mia | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w034_sccmMia` | APSB ECU: w034 sccm mia | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w035_espMia` | APSB ECU: w035 esp mia | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w036_bdyMia` | APSB ECU: w036 bdy mia | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w037_camTacIssue` | APSB ECU: w037 cam tac issue | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w038_camFailure` | APSB ECU: w038 cam failure | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w039_sdm_rcm_Mia` | APSB ECU: w039 sdm rcm mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w040_autopilotAngleSaturated` | APSB ECU: w040 autopilot angle saturated | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w041_autopilotRateSaturated` | APSB ECU: w041 autopilot rate saturated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w042_autopilotAborting` | APSB ECU: w042 autopilot aborting | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w043_camLongRunTime` | APSB ECU: w043 cam long run time | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w044_appMobileyeFailure` | APSB ECU: w044 app mobileye failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w045_radMia` | APSB ECU: w045 rad mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w046_eepromRecordAbsent` | APSB ECU: w046 eeprom record absent | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w047_edrEvent` | APSB ECU: w047 edr event | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w048_DAS_Features_Disabled` | APSB ECU: w048 DAS features disabled | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w049_eyeqVersionMismatch` | APSB ECU: w049 eyeq version mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w050_aeb_event` | APSB ECU: w050 aeb event | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w051_radcEcuIssue` | APSB ECU: w051 radc ecu issue | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w052_radcSensorIssue` | APSB ECU: w052 radc sensor issue | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w053_radcCommIssue` | APSB ECU: w053 radc comm issue | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w054_camAutofix` | APSB ECU: w054 cam autofix | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w055_radcVersionMismatch` | APSB ECU: w055 radc version mismatch | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w056_diMia` | APSB ECU: w056 di mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w057_mcuMia` | APSB ECU: w057 mcu mia | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w058_epbMia` | APSB ECU: w058 epb mia | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w059_parkMia` | APSB ECU: w059 park mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w060_fcw_event` | APSB ECU: w060 fcw event | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w061_tasMia` | APSB ECU: w061 tas mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w062_radcAlignment` | APSB ECU: w062 radc alignment | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w063_parkVersionMismatch` | APSB ECU: w063 park version mismatch | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w064_epasMia` | APSB ECU: w064 epas mia | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
