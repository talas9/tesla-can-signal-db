---
layout: default
title: "EPASTS_alertMatrix (0x398) — EPASTS ECU, Tesla Model 3 2026.26.6.5 ETH"
description: "EPASTS ECU message: alert matrix. Ethernet-side message EPASTS_alertMatrix of EPASTS ECU for Tesla Model 3 firmware 2026.26.6.5, 271 signals (EPASTS_matrixIndex, EPASTS_a001_adcCalibrationOrInitFail, EPASTS_a002_adcMuxErr, EPASTS_a003_pspInvalidParamset and 267 more). Bit layout, scaling, units and value tables."
---

# EPASTS_alertMatrix (0x398) — EPASTS ECU, Tesla Model 3 2026.26.6.5 ETH

EPASTS ECU message: alert matrix. This page documents the 271 signals of EPASTS_alertMatrix as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPASTS_alertMatrix` |
| Ethernet-side id | 0x398 (920) |
| ECU | [EPASTS ECU](../../epasts.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPASTS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 271 |

## Signals of EPASTS_alertMatrix

Tesla Model 3 CAN bus signals in `EPASTS_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPASTS_matrixIndex` | selector | EPASTS ECU: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3`<br>4 = `AlertMatrix4` | plausible |
| `EPASTS_a001_adcCalibrationOrInitFail` | page 0 | EPASTS ECU: a001 adc calibration or init fail | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a002_adcMuxErr` | page 0 | EPASTS ECU: a002 adc mux err | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a003_pspInvalidParamset` | page 0 | EPASTS ECU: a003 psp invalid paramset | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a004_scpInputMia` | page 0 | EPASTS ECU: a004 scp input mia | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a005_scpUnknownResetSource` | page 0 | EPASTS ECU: a005 scp unknown reset source | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a006_swrhResetByInvalidErrid` | page 0 | EPASTS ECU: a006 swrh reset by invalid errid | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a007_tsmcCoreTempDiff` | page 0 | EPASTS ECU: a007 tsmc core temp diff | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a008_psdcPlatformShutdown` | page 0 | EPASTS ECU: a008 psdc platform shutdown | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a009_mcusscLbistPermanentFail` | page 0 | EPASTS ECU: a009 mcussc lbist permanent fail | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a010_svcIncompatibleSwVersions` | page 0 | EPASTS ECU: a010 svc incompatible sw versions | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a011_mcusscMonbistErr` | page 0 | EPASTS ECU: a011 mcussc monbist err | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a012_mcusscMbistEccErr` | page 0 | EPASTS ECU: a012 mcussc mbist ecc err | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a013_mcusscSffMonitoringFailed` | page 0 | EPASTS ECU: a013 mcussc sff monitoring failed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a014_mcusscSffMonitoringMia` | page 0 | EPASTS ECU: a014 mcussc sff monitoring mia | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a015_mcusscCsErrorCheckFail` | page 0 | EPASTS ECU: a015 mcussc cs error check fail | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a016_mcufcCsErrorCheckFail` | page 0 | EPASTS ECU: a016 mcufc cs error check fail | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a017_stmdStmPlausibilityCheckErr` | page 0 | EPASTS ECU: a017 stmd stm plausibility check err | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a018_exchCsErrorCheck` | page 0 | EPASTS ECU: a018 exch cs error check | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a019_rsthHwResetInfoCorruptionCheck` | page 0 | EPASTS ECU: a019 rsth hw reset info corruption check | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a020_mcusscEolEcuIdIntegritiyFail` | page 0 | EPASTS ECU: a020 mcussc eol ecu id integritiy fail | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a021_osehCsErrorCheck` | page 0 | EPASTS ECU: a021 oseh cs error check | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a022_swrhSwResetInfoCorruptionCheck` | page 0 | EPASTS ECU: a022 swrh sw reset info corruption check | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a023_btarcCorruptionCheck` | page 0 | EPASTS ECU: a023 btarc corruption check | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a024_srhCsErrorCheckFail` | page 0 | EPASTS ECU: a024 srh cs error check fail | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a025_btarcCorruptionCheck` | page 0 | EPASTS ECU: a025 btarc corruption check | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a026_mrccCsErrorCheckFail` | page 0 | EPASTS ECU: a026 mrcc cs error check fail | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a027_mcusscDmuHfErr` | page 0 | EPASTS ECU: a027 mcussc dmu hf err | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a028_smuhNonInitDataCorruption` | page 0 | EPASTS ECU: a028 smuh non init data corruption | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a029_smuhSmuCoreCntErrorTestFail` | page 0 | EPASTS ECU: a029 smuh smu core cnt error test fail | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a030_rsthClockReset` | page 0 | EPASTS ECU: a030 rsth clock reset | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a031_pmsProductionModeFailed` | page 0 | EPASTS ECU: a031 pms production mode failed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a032_eolpEolCheckFailed` | page 0 | EPASTS ECU: a032 eolp eol check failed | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a033_icsvcPswVersionMismatch` | page 0 | EPASTS ECU: a033 icsvc psw version mismatch | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a034_sbchReadbackRegFail` | page 0 | EPASTS ECU: a034 sbch readback reg fail | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a035_sbchChipIdFail` | page 0 | EPASTS ECU: a035 sbch chip id fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a036_sbcmSbcBistFailed` | page 0 | EPASTS ECU: a036 sbcm sbc bist failed | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a037_epmV5P2Fail` | page 0 | EPASTS ECU: a037 epm V5 P2 fail | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a038_csohCh1CsErrorErrAtReset` | page 0 | EPASTS ECU: a038 csoh ch1 cs error err at reset | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a039_csohCh2CsErrorErrAtReset` | page 0 | EPASTS ECU: a039 csoh ch2 cs error err at reset | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a040_swrhLimitedResetRetriesExpired` | page 0 | EPASTS ECU: a040 swrh limited reset retries expired | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a041_imcmCoreConfigurationMismatch` | page 0 | EPASTS ECU: a041 imcm core configuration mismatch | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a042_wdhWdTestFail` | page 0 | EPASTS ECU: a042 wdh wd test fail | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a043_sbcmWdStateDisabled` | page 0 | EPASTS ECU: a043 sbcm wd state disabled | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a044_sbcmSbcEepromFail` | page 0 | EPASTS ECU: a044 sbcm sbc eeprom fail | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a045_psumSbcBandgapVoltErr` | page 0 | EPASTS ECU: a045 psum sbc bandgap volt err | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a046_mcusscOscillatorNotReliable` | page 0 | EPASTS ECU: a046 mcussc oscillator not reliable | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a047_epmVregVoltFail` | page 0 | EPASTS ECU: a047 epm vreg volt fail | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a048_epmVcpVoltFail` | page 0 | EPASTS ECU: a048 epm vcp volt fail | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a049_epmLgFail` | page 0 | EPASTS ECU: a049 epm lg fail | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a050_erlErr` | page 0 | EPASTS ECU: a050 erl err | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a051_ermMessageErr` | page 0 | EPASTS ECU: a051 erm message err | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a052_ermSdcInputBufferOverflow` | page 0 | EPASTS ECU: a052 erm sdc input buffer overflow | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a053_adcUnexpectedNumOfData` | page 0 | EPASTS ECU: a053 adc unexpected num of data | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a054_adcUnexpectedData` | page 0 | EPASTS ECU: a054 adc unexpected data | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a055_amExtendedGduTest` | page 0 | EPASTS ECU: a055 am extended gdu test | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a056_amGduConfigCsErrorCheck` | page 0 | EPASTS ECU: a056 am gdu config cs error check | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a057_amGduVds` | page 0 | EPASTS ECU: a057 am gdu vds | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a058_amIntVgsUndervtgErr` | page 0 | EPASTS ECU: a058 am int vgs undervtg err | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a059_amStartupTestFailed` | page 0 | EPASTS ECU: a059 am startup test failed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a060_amGduFail` | page 0 | EPASTS ECU: a060 am gdu fail | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a061_amIntSerialErr` | page 1 | EPASTS ECU: a061 am int serial err | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a062_amPhaseBridgeCheck` | page 1 | EPASTS ECU: a062 am phase bridge check | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a063_amIntRegulatorErr` | page 1 | EPASTS ECU: a063 am int regulator err | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a064_amBridgeShort` | page 1 | EPASTS ECU: a064 am bridge short | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a065_amGduJuncTemp` | page 1 | EPASTS ECU: a065 am gdu junc temp | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a066_amVoltQfErr` | page 1 | EPASTS ECU: a066 am volt qf err | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a067_tspmPowermoduleTempImplausible` | page 1 | EPASTS ECU: a067 tspm powermodule temp implausible | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a068_rsthCoreRedundancyErr` | page 1 | EPASTS ECU: a068 rsth core redundancy err | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a069_rsthCoreTempOutOfRangeHwCheck` | page 1 | EPASTS ECU: a069 rsth core temp out of range hw check | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a070_rsthInternalLowVolt` | page 1 | EPASTS ECU: a070 rsth internal low volt | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a071_rsthInternalHighVolt` | page 1 | EPASTS ECU: a071 rsth internal high volt | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a072_rsthFlashUncorrEccOrOvfl` | page 1 | EPASTS ECU: a072 rsth flash uncorr ecc or ovfl | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a073_rsthOtherEdcEcc` | page 1 | EPASTS ECU: a073 rsth other edc ecc | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a074_rsthUnexpectedAlarm` | page 1 | EPASTS ECU: a074 rsth unexpected alarm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a075_rsthUnusedOtherModuleAlarm` | page 1 | EPASTS ECU: a075 rsth unused other module alarm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a076_exchGeneralException` | page 1 | EPASTS ECU: a076 exch general exception | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a077_dmDeadlineViolation` | page 1 | EPASTS ECU: a077 dm deadline violation | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a078_dmDeadlineViolation` | page 1 | EPASTS ECU: a078 dm deadline violation | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a079_gduhComErr` | page 1 | EPASTS ECU: a079 gduh com err | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a080_pwmTimerSyncCheck` | page 1 | EPASTS ECU: a080 pwm timer sync check | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a081_exchFloatingPointException` | page 1 | EPASTS ECU: a081 exch floating point exception | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a082_adcTriggerTimeChk` | page 1 | EPASTS ECU: a082 adc trigger time chk | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a083_tdaDclinkcapacitorTempChecker` | page 1 | EPASTS ECU: a083 tda dclinkcapacitor temp checker | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a084_adcTriggerCheck` | page 1 | EPASTS ECU: a084 adc trigger check | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a085_amGduSwitchOffTestByMcu` | page 1 | EPASTS ECU: a085 am gdu switch off test by mcu | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a086_rsthRamUncorrEcc` | page 1 | EPASTS ECU: a086 rsth ram uncorr ecc | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a087_rsthFlashConfigErr` | page 1 | EPASTS ECU: a087 rsth flash config err | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a088_tedMainboardTempChecker` | page 1 | EPASTS ECU: a088 ted mainboard temp checker | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a089_tedRevercebattfetjunctionTempChecker` | page 1 | EPASTS ECU: a089 ted revercebattfetjunction temp checker | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a090_etsmWarning` | page 1 | EPASTS ECU: a090 etsm warning | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a091_bvpBattVoltCrossChkFailed` | page 1 | EPASTS ECU: a091 bvp batt volt cross chk failed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a092_amGduSwitchOffTestBySbc` | page 1 | EPASTS ECU: a092 am gdu switch off test by sbc | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a093_sctpTsuSingleStaticFail` | page 1 | EPASTS ECU: a093 sctp tsu single static fail | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a094_sctpTsuMultipleStaticFail` | page 1 | EPASTS ECU: a094 sctp tsu multiple static fail | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a095_mdModelBasedMotorIntegrityCheck` | page 1 | EPASTS ECU: a095 md model based motor integrity check | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a096_rppRpsSingleStaticFail` | page 1 | EPASTS ECU: a096 rpp rps single static fail | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a097_rppRpsMultipleStaticFail` | page 1 | EPASTS ECU: a097 rpp rps multiple static fail | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a098_invErr` | page 1 | EPASTS ECU: a098 inv err | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a099_mcdTorqueMismatchFault` | page 1 | EPASTS ECU: a099 mcd torque mismatch fault | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a100_amVbrgLssFault` | page 1 | EPASTS ECU: a100 am vbrg lss fault | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a101_sdrvSpcIdMismatch` | page 1 | EPASTS ECU: a101 sdrv spc id mismatch | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a102_amPhasecurrentQosErr` | page 1 | EPASTS ECU: a102 am phasecurrent qos err | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a103_exhaUnusedInterruptCallException` | page 1 | EPASTS ECU: a103 exha unused interrupt call exception | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a104_exhaBusMpuException` | page 1 | EPASTS ECU: a104 exha bus mpu exception | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a105_exhaSriBusErrException` | page 1 | EPASTS ECU: a105 exha sri bus err exception | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a106_exhaSpbBusErrException` | page 1 | EPASTS ECU: a106 exha spb bus err exception | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a107_exhaOtherNmiException` | page 1 | EPASTS ECU: a107 exha other nmi exception | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a108_exhaInternalProtectionException` | page 1 | EPASTS ECU: a108 exha internal protection exception | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a109_exhaSysBusOrPeriphErrException` | page 1 | EPASTS ECU: a109 exha sys bus or periph err exception | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a110_amPhaseRelaySwitchOffTest` | page 1 | EPASTS ECU: a110 am phase relay switch off test | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a111_amCurrentSensingDisconnection` | page 1 | EPASTS ECU: a111 am current sensing disconnection | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a112_rsthSafetyFlipflopErr` | page 1 | EPASTS ECU: a112 rsth safety flipflop err | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a113_rsthUncorrectableEndToEndBusErr` | page 1 | EPASTS ECU: a113 rsth uncorrectable end to end bus err | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a114_osehOsErr` | page 1 | EPASTS ECU: a114 oseh os err | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a115_mcusscLbistSingleFail` | page 1 | EPASTS ECU: a115 mcussc lbist single fail | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a116_mrccStartupRegCsErrorStaticErr` | page 1 | EPASTS ECU: a116 mrcc startup reg cs error static err | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a117_mrccStartupRegCsErrorTransientErr` | page 1 | EPASTS ECU: a117 mrcc startup reg cs error transient err | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a118_mcusscFlashCsErrorErr` | page 1 | EPASTS ECU: a118 mcussc flash cs error err | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a119_mcusscFlashEccCriticalErr` | page 1 | EPASTS ECU: a119 mcussc flash ecc critical err | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a120_mcusscFlashEccLatentErr` | page 1 | EPASTS ECU: a120 mcussc flash ecc latent err | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a121_mcusscMbistEccErr` | page 2 | EPASTS ECU: a121 mcussc mbist ecc err | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a122_pcpBridgeFetShort` | page 2 | EPASTS ECU: a122 pcp bridge fet short | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a123_imcmCommErr` | page 2 | EPASTS ECU: a123 imcm comm err | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a124_mcusscMbistEccTransientErr` | page 2 | EPASTS ECU: a124 mcussc mbist ecc transient err | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a125_mcusscMbistMiaErr` | page 2 | EPASTS ECU: a125 mcussc mbist mia err | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a126_mcusscMonbistMiaErr` | page 2 | EPASTS ECU: a126 mcussc monbist mia err | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a127_exchAdditionalExceptionAfterRst` | page 2 | EPASTS ECU: a127 exch additional exception after rst | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a128_exchExceptionStopRestart` | page 2 | EPASTS ECU: a128 exch exception stop restart | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a129_exchAdditionalExceptionStopRestart` | page 2 | EPASTS ECU: a129 exch additional exception stop restart | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a130_mrccConfigCsErrorErr` | page 2 | EPASTS ECU: a130 mrcc config cs error err | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a131_exchGuardedResetAfterPartitionStop` | page 2 | EPASTS ECU: a131 exch guarded reset after partition stop | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a132_mcusscNotSupportedMcu` | page 2 | EPASTS ECU: a132 mcussc not supported mcu | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a133_mcusscLbistEcuIdIsNotSupported` | page 2 | EPASTS ECU: a133 mcussc lbist ecu id is not supported | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a134_osehGuardedResetAfterErrWithoutReset` | page 2 | EPASTS ECU: a134 oseh guarded reset after err without reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a135_tmpsfetjCalculationOverflowErr` | page 2 | EPASTS ECU: a135 tmpsfetj calculation overflow err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a136_ftElectricalAngleQf` | page 2 | EPASTS ECU: a136 ft electrical angle qf | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a137_osehErrWithoutImmediateReset` | page 2 | EPASTS ECU: a137 oseh err without immediate reset | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a138_osehAdditionalErrWithoutImmReset` | page 2 | EPASTS ECU: a138 oseh additional err without imm reset | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a139_osehAdditionalOsErr` | page 2 | EPASTS ECU: a139 oseh additional os err | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a140_imcmConfigurationErr` | page 2 | EPASTS ECU: a140 imcm configuration err | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a141_amFetShortTest` | page 2 | EPASTS ECU: a141 am fet short test | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a142_tedEmifilterDmcTempChecker` | page 2 | EPASTS ECU: a142 ted emifilter dmc temp checker | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a143_tedEmifilterCmcTempChecker` | page 2 | EPASTS ECU: a143 ted emifilter cmc temp checker | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a144_mriCoreRaminitFailed` | page 2 | EPASTS ECU: a144 mri core raminit failed | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a145_mriPeripheralRaminitFailed` | page 2 | EPASTS ECU: a145 mri peripheral raminit failed | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a146_btarcRcCircuitCheck` | page 2 | EPASTS ECU: a146 btarc rc circuit check | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a147_amDcLinkShortedFail` | page 2 | EPASTS ECU: a147 am dc link shorted fail | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a148_mrccExitFromStandbyDetected` | page 2 | EPASTS ECU: a148 mrcc exit from standby detected | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a149_amReversibleEmergencyOffRequested` | page 2 | EPASTS ECU: a149 am reversible emergency off requested | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a150_amExternalEmergencyOffRequested` | page 2 | EPASTS ECU: a150 am external emergency off requested | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a151_amPermanentEmergencyOffRequested` | page 2 | EPASTS ECU: a151 am permanent emergency off requested | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a152_exchFlashEccException` | page 2 | EPASTS ECU: a152 exch flash ecc exception | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a153_sdsmBlockSelectorInvalid` | page 2 | EPASTS ECU: a153 sdsm block selector invalid | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a154_sdsmCsErrorInvalidPrimary` | page 2 | EPASTS ECU: a154 sdsm cs error invalid primary | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a155_sdsmDataInvalidAll` | page 2 | EPASTS ECU: a155 sdsm data invalid all | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a156_amIntSerialErrSafetyReset` | page 2 | EPASTS ECU: a156 am int serial err safety reset | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a157_mcudcpInvalidEcuId` | page 2 | EPASTS ECU: a157 mcudcp invalid ecu id | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a158_amGduFailDuringRecovery` | page 2 | EPASTS ECU: a158 am gdu fail during recovery | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a159_exchFlashWordlineTransientErr` | page 2 | EPASTS ECU: a159 exch flash wordline transient err | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a160_rsthCpu1UnexpectedAlarm` | page 2 | EPASTS ECU: a160 rsth cpu1 unexpected alarm | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a161_tdaRelayfetjunctionTempChecker` | page 2 | EPASTS ECU: a161 tda relayfetjunction temp checker | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a162_tdaBridgefetjunctionTempChecker` | page 2 | EPASTS ECU: a162 tda bridgefetjunction temp checker | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a163_tdaPowermoduleTempChecker` | page 2 | EPASTS ECU: a163 tda powermodule temp checker | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a164_tdaBattfetjunctionTempChecker` | page 2 | EPASTS ECU: a164 tda battfetjunction temp checker | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a165_tdaDcbusshuntTempChecker` | page 2 | EPASTS ECU: a165 tda dcbusshunt temp checker | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a166_tdaPhasecurrentshuntTempChecker` | page 2 | EPASTS ECU: a166 tda phasecurrentshunt temp checker | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a167_iccd1ErrQueueOverflow` | page 2 | EPASTS ECU: a167 iccd1 err queue overflow | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a168_c1csInvalidC1App` | page 2 | EPASTS ECU: a168 c1cs invalid C1 app | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a169_scpSafetyReset` | page 2 | EPASTS ECU: a169 scp safety reset | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a170_pmpDcvoltAge` | page 2 | EPASTS ECU: a170 pmp dcvolt age | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a171_pmpKgvalueAge` | page 2 | EPASTS ECU: a171 pmp kgvalue age | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a172_pmpElangMotorcurrentAge` | page 2 | EPASTS ECU: a172 pmp elang motorcurrent age | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a173_pmpRotorspeedAge` | page 2 | EPASTS ECU: a173 pmp rotorspeed age | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a174_pmpPhasecurrentAge` | page 2 | EPASTS ECU: a174 pmp phasecurrent age | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a175_exchFlashStoredConfigErr` | page 2 | EPASTS ECU: a175 exch flash stored config err | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a176_exchCpu1ExceptionReset` | page 2 | EPASTS ECU: a176 exch cpu1 exception reset | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a177_etsrInvalidated` | page 2 | EPASTS ECU: a177 etsr invalidated | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a178_exchWdtException` | page 2 | EPASTS ECU: a178 exch wdt exception | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a179_tedMotorcoilTempChecker` | page 2 | EPASTS ECU: a179 ted motorcoil temp checker | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a180_dmDeadlineViolationC1` | page 2 | EPASTS ECU: a180 dm deadline violation C1 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a181_dmDeadlineViolationC1` | page 3 | EPASTS ECU: a181 dm deadline violation C1 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a182_mcdInputMia` | page 3 | EPASTS ECU: a182 mcd input mia | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a183_sbchCommErrSbcToMcu` | page 3 | EPASTS ECU: a183 sbch comm err sbc to mcu | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a184_sbcmCommBufferOverflow` | page 3 | EPASTS ECU: a184 sbcm comm buffer overflow | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a185_sbcscpQAWatchdogReset` | page 3 | EPASTS ECU: a185 sbcscp QA watchdog reset | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a186_wdhCommBufferOverflow` | page 3 | EPASTS ECU: a186 wdh comm buffer overflow | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a187_epmVoltFail` | page 3 | EPASTS ECU: a187 epm volt fail | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a188_epmCommBufferOverflow` | page 3 | EPASTS ECU: a188 epm comm buffer overflow | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a189_sbchCommErrMcuToSbc` | page 3 | EPASTS ECU: a189 sbch comm err mcu to sbc | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a190_sbchCommBufferOverflow` | page 3 | EPASTS ECU: a190 sbch comm buffer overflow | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a191_sbcscpVcp2VucVoltFail` | page 3 | EPASTS ECU: a191 sbcscp vcp2 vuc volt fail | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a192_osumC0CsaNearFull` | page 3 | EPASTS ECU: a192 osum C0 csa near full | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a193_osumC0StackNearFull` | page 3 | EPASTS ECU: a193 osum C0 stack near full | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a194_amNvdataLoss` | page 3 | EPASTS ECU: a194 am nvdata loss | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a195_imcmCommErrC1` | page 3 | EPASTS ECU: a195 imcm comm err C1 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a196_topEolTasOffsetInvalid` | page 3 | EPASTS ECU: a196 top eol tas offset invalid | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a197_difpDifactorInvalid` | page 3 | EPASTS ECU: a197 difp difactor invalid | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a198_osumC1CsaNearFull` | page 3 | EPASTS ECU: a198 osum C1 csa near full | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a199_osumC1StackNearFull` | page 3 | EPASTS ECU: a199 osum C1 stack near full | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a200_ammInputBufferOverflow` | page 3 | EPASTS ECU: a200 amm input buffer overflow | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a201_ammOutputBufferOverflow` | page 3 | EPASTS ECU: a201 amm output buffer overflow | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a202_ohnvmpStoredOffsetLost` | page 3 | EPASTS ECU: a202 ohnvmp stored offset lost | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a203_ctcInterfaceErr` | page 3 | EPASTS ECU: a203 ctc interface err | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a204_fdpPrevTrqErr` | page 3 | EPASTS ECU: a204 fdp prev trq err | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a205_fdrOclFail` | page 3 | EPASTS ECU: a205 fdr ocl fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a206_fdrOclPartialBlocking` | page 3 | EPASTS ECU: a206 fdr ocl partial blocking | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a207_fdrOclFreezing` | page 3 | EPASTS ECU: a207 fdr ocl freezing | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a208_fdrLowSeverityBlocking` | page 3 | EPASTS ECU: a208 fdr low severity blocking | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a209_fdrLowSeverityFreezing` | page 3 | EPASTS ECU: a209 fdr low severity freezing | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a210_fdrTotalBlocking` | page 3 | EPASTS ECU: a210 fdr total blocking | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a211_frmInternalErr` | page 3 | EPASTS ECU: a211 frm internal err | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a212_frmDataLost` | page 3 | EPASTS ECU: a212 frm data lost | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a213_frmHighFrictionDetected` | page 3 | EPASTS ECU: a213 frm high friction detected | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a214_velInterfaceErr` | page 3 | EPASTS ECU: a214 vel interface err | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a215_vsgSafeViolErr` | page 3 | EPASTS ECU: a215 vsg safe viol err | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a216_isdgImproperShutdown` | page 3 | EPASTS ECU: a216 isdg improper shutdown | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a217_msdMasterSilentErr` | page 3 | EPASTS ECU: a217 msd master silent err | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a218_aadApplicationStateErr` | page 3 | EPASTS ECU: a218 aad application state err | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a219_frhFastRestartFailed` | page 3 | EPASTS ECU: a219 frh fast restart failed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a220_transceiverInputqueueOverflow` | page 3 | EPASTS ECU: a220 transceiver inputqueue overflow | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a221_apsCntError` | page 3 | EPASTS ECU: a221 aps cnt error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a222_apsCsError` | page 3 | EPASTS ECU: a222 aps cs error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a223_apsMia` | page 3 | EPASTS ECU: a223 aps mia | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a224_dasCntError` | page 3 | EPASTS ECU: a224 das cnt error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a225_dasCsError` | page 3 | EPASTS ECU: a225 das cs error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a226_dasMia` | page 3 | EPASTS ECU: a226 das mia | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a227_dirTorqueCntError` | page 3 | EPASTS ECU: a227 dir torque cnt error | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a228_dirTorqueCsError` | page 3 | EPASTS ECU: a228 dir torque cs error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a229_dirTorqueMia` | page 3 | EPASTS ECU: a229 dir torque mia | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a230_diSpdCntError` | page 3 | EPASTS ECU: a230 di spd cnt error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a231_diSpdCsError` | page 3 | EPASTS ECU: a231 di spd cs error | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a232_diSpdMia` | page 3 | EPASTS ECU: a232 di spd mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a233_ecu1StatCntError` | page 3 | EPASTS ECU: a233 ecu1 stat cnt error | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a234_ecu1StatCsError` | page 3 | EPASTS ECU: a234 ecu1 stat cs error | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a235_ecu1StatMia` | page 3 | EPASTS ECU: a235 ecu1 stat mia | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a236_espWrCntError` | page 3 | EPASTS ECU: a236 esp wr cnt error | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a237_espWrCsError` | page 3 | EPASTS ECU: a237 esp wr cs error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a238_espWrMia` | page 3 | EPASTS ECU: a238 esp wr mia | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a239_espWsCntError` | page 3 | EPASTS ECU: a239 esp ws cnt error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a240_espWsCsError` | page 3 | EPASTS ECU: a240 esp ws cs error | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a241_espWsMia` | page 4 | EPASTS ECU: a241 esp ws mia | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a242_gtwConfigMia` | page 4 | EPASTS ECU: a242 gtw config mia | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a243_rcmCntError` | page 4 | EPASTS ECU: a243 rcm cnt error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a244_rcmCsError` | page 4 | EPASTS ECU: a244 rcm cs error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a245_rcmMia` | page 4 | EPASTS ECU: a245 rcm mia | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a246_sccmCntError` | page 4 | EPASTS ECU: a246 sccm cnt error | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a247_sccmCsError` | page 4 | EPASTS ECU: a247 sccm cs error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a248_sccmMia` | page 4 | EPASTS ECU: a248 sccm mia | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a249_uiTuneReqCntError` | page 4 | EPASTS ECU: a249 ui tune req cnt error | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a250_uiTuneReqCsError` | page 4 | EPASTS ECU: a250 ui tune req cs error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a251_uiTuneReqMia` | page 4 | EPASTS ECU: a251 ui tune req mia | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a252_vcFrontCntError` | page 4 | EPASTS ECU: a252 vc front cnt error | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a253_vcFrontCsError` | page 4 | EPASTS ECU: a253 vc front cs error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a254_vcFrontMia` | page 4 | EPASTS ECU: a254 vc front mia | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a255_pmState2Mia` | page 4 | EPASTS ECU: a255 pm state2 mia | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a256_dcvmOverVolt` | page 4 | EPASTS ECU: a256 dcvm over volt | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a257_dcvmUnderVolt` | page 4 | EPASTS ECU: a257 dcvm under volt | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a258_pspInvalidProjectParamset` | page 4 | EPASTS ECU: a258 psp invalid project paramset | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a259_scoCanBusOff` | page 4 | EPASTS ECU: a259 sco can bus off | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a260_scoPrivateBusOff` | page 4 | EPASTS ECU: a260 sco private bus off | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a261_sccmStatusError` | page 4 | EPASTS ECU: a261 sccm status error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a262_yawRateStatus` | page 4 | EPASTS ECU: a262 yaw rate status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a263_espWsStatus` | page 4 | EPASTS ECU: a263 esp ws status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a264_assistTorqueLimited` | page 4 | EPASTS ECU: a264 assist torque limited | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a265_overheatProtect` | page 4 | EPASTS ECU: a265 overheat protect | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a266_overloadProtect` | page 4 | EPASTS ECU: a266 overload protect | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a267_safeSpeedAssist` | page 4 | EPASTS ECU: a267 safe speed assist | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a268_eacCancelled` | page 4 | EPASTS ECU: a268 eac cancelled | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a269_assistTorqueDisabled` | page 4 | EPASTS ECU: a269 assist torque disabled | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `EPASTS_a270_oscillationCompTrqLimReached` | page 4 | EPASTS ECU: a270 oscillation comp trq lim reached | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`EPASTS_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (60 signals), page 1 (60 signals), page 2 (60 signals), page 3 (60 signals), page 4 (30 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All EPASTS ECU messages (EPASTS)](../../epasts.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
