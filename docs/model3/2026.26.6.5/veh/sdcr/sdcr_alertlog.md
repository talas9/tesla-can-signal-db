---
layout: default
title: "SDCR_alertLog (0x5FB) — SDCR ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "SDCR ECU message: alert log. Tesla Model 3 CAN bus message SDCR_alertLog (0x5FB) of SDCR ECU, firmware 2026.26.6.5, 130 signals (SDCR_alertID, SDCR_alertState, SDCR_a001_pyroSenseV, SDCR_a001_HVBackupSupplyV and 126 more). Bit layout, scaling, units and value tables."
---

# SDCR_alertLog (0x5FB) — SDCR ECU, Tesla Model 3 2026.26.6.5 VEH CAN

SDCR ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 130 signals of SDCR_alertLog as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SDCR_alertLog` |
| CAN id | 0x5FB (1531) |
| ECU | [SDCR ECU](../../sdcr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SDCR |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 130 |

## Signals of SDCR_alertLog

Tesla Model 3 CAN bus signals in `SDCR_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SDCR_alertID` | selector | SDCR ECU: alert ID | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_powerOnSelfTestFailed`<br>2 = `a002_diPstSkipped`<br>3 = `a003_diUartMIA`<br>4 = `a004_pmRunningFdbkIrrational`<br>5 = `a005_motorSpeedIrrational`<br>6 = `a006_pyroTriggered`<br>7 = `a007_faultCurrentsDetected`<br>8 = `a008_hvlinkMIA`<br>9 = `a009_uartVersionMismatch`<br>10 = `a010_vrefIrrational`<br>11 = `a011_phaseCurrentOffset`<br>12 = `a012_vBoostSecIrrational`<br>13 = `a013_vBkupIrrational`<br>14 = `a014_vBusIrrational`<br>15 = `a015_phaseVIrrational`<br>16 = `a016_systemReset`<br>17 = `a017_adcSPIError`<br>18 = `a018_historicalPyroTrigger`<br>19 = `a019_historicalFaultCurrents`<br>20 = `a020_eepromSPIError`<br>21 = `a021_busBarTempIrrational`<br>22 = `a022_TaskInitError`<br>23 = `a023_ecuLogAvailable`<br>24 = `a024_gtwMIA`<br>25 = `a025_diSwitchingFdbkIrrational`<br>26 = `a026_faultCurrentMonitoringDisabled`<br>27 = `a027_diCanMIA`<br>28 = `a028_vcLVStateMIA`<br>29 = `a029_diMIA`<br>30 = `a030_placeholder30`<br>31 = `a031_placeholder31`<br>32 = `a032_placeholder32`<br>33 = `a033_placeholder33`<br>34 = `a034_phaseCurrentIrrational` | plausible |
| `SDCR_alertState` |  | SDCR ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `SDCR_a001_pyroSenseV` | page 1 | SDCR ECU: a001 pyro sense v | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a001_HVBackupSupplyV` | page 1 | SDCR ECU: a001 HV backup supply v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a001_boostRailV` | page 1 | SDCR ECU: a001 boost rail v | 32\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a001_expectedPyroV_max` | page 1 | SDCR ECU: a001 expected pyro v max | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a001_expectedPyroV_min` | page 1 | SDCR ECU: a001 expected pyro v min | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a001_fromState` | page 1 | SDCR ECU: a001 from state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PENDING`<br>1 = `TEST_PYRO_BOTH_OFF1`<br>2 = `TEST_PYRO_H_ON`<br>3 = `TEST_PYRO_BOTH_OFF2`<br>4 = `TEST_PYRO_L_ON`<br>5 = `PASSED`<br>6 = `FAILED`<br>7 = `SKIPPED` | plausible |
| `SDCR_a004_HVBackupSupplyV` | page 4 | SDCR ECU: a004 HV backup supply v | 16\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a004_boostRailV` | page 4 | SDCR ECU: a004 boost rail v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a004_diPresent` | page 4 | SDCR ECU: a004 di present | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a004_pmRunningPin` | page 4 | SDCR ECU: a004 pm running pin | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_pyroArmed` | page 6 | SDCR ECU: a006 pyro armed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_triggerReason_faultCurrents` | page 6 | SDCR ECU: a006 trigger reason fault currents | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_triggerReason_hvBadAtSpeed` | page 6 | SDCR ECU: a006 trigger reason hv bad at speed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_triggerReason_highBackEMF` | page 6 | SDCR ECU: a006 trigger reason high back EMF | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_faultCurrentsDetected` | page 6 | SDCR ECU: a006 fault currents detected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_diUartMIA` | page 6 | SDCR ECU: a006 di uart MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_pmRunningPin` | page 6 | SDCR ECU: a006 pm running pin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_hvPowerGood` | page 6 | SDCR ECU: a006 hv power good | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_hvbkupPGoodPin` | page 6 | SDCR ECU: a006 hvbkup p good pin | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_hvPowerNotGoodQualified` | page 6 | SDCR ECU: a006 hv power not good qualified | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_speedValid` | page 6 | SDCR ECU: a006 speed valid | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_speedFromVoltage` | page 6 | SDCR ECU: a006 speed from voltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a006_HVBackupSupplyV` | page 6 | SDCR ECU: a006 HV backup supply v | 28\|7 | little-endian | unsigned | 0.3 | 0 | V | 0 to 38.1 |  | plausible |
| `SDCR_a006_boostRailV` | page 6 | SDCR ECU: a006 boost rail v | 35\|7 | little-endian | unsigned | 0.3 | 0 | V | 0 to 38.1 |  | plausible |
| `SDCR_a006_maxAbsSpeed` | page 6 | SDCR ECU: a006 max abs speed | 42\|12 | little-endian | signed | 1 | 0 | Hz | -2048 to 2047 |  | plausible |
| `SDCR_a006_vBat` | page 6 | SDCR ECU: a006 v bat | 54\|7 | little-endian | unsigned | 8 | 0 | V | 0 to 1016 |  | plausible |
| `SDCR_a007_faultReason_faultCurrentsAtSpeed` | page 7 | SDCR ECU: a007 fault reason fault currents at speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_faultReason_unmitigatedUCR` | page 7 | SDCR ECU: a007 fault reason unmitigated UCR | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_faultReason_propagating3PS` | page 7 | SDCR ECU: a007 fault reason propagating3 PS | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_speedWasValid` | page 7 | SDCR ECU: a007 speed was valid | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_imbalanceSeen` | page 7 | SDCR ECU: a007 imbalance seen | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_ucrSeen` | page 7 | SDCR ECU: a007 ucr seen | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_phaseVoltagePresent` | page 7 | SDCR ECU: a007 phase voltage present | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_speedFromVoltage` | page 7 | SDCR ECU: a007 speed from voltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a007_transientHandling` | page 7 | SDCR ECU: a007 transient handling | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ALL_SKIPPED`<br>1 = `SKIPPED_3PS`<br>2 = `3PS_EARLY_EXIT`<br>3 = `3PS_WAITED` | plausible |
| `SDCR_a007_maxAbsElcSpeed` | page 7 | SDCR ECU: a007 max abs elc speed | 26\|9 | little-endian | unsigned | 4 | 0 | Hz | 0 to 2044 |  | plausible |
| `SDCR_a007_avgIa` | page 7 | SDCR ECU: a007 avg ia | 35\|10 | little-endian | signed | 4 | 0 | A | -2048 to 2044 |  | plausible |
| `SDCR_a007_avgIb` | page 7 | SDCR ECU: a007 avg ib | 45\|10 | little-endian | signed | 4 | 0 | A | -2048 to 2044 |  | plausible |
| `SDCR_a007_maxAbsCurrents` | page 7 | SDCR ECU: a007 max abs currents | 55\|9 | little-endian | unsigned | 4 | 0 | A | 0 to 2044 |  | plausible |
| `SDCR_a008_dcLinkInfo` | page 8 | SDCR ECU: a008 dc link info | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a009_diVersion` | page 9 | SDCR ECU: a009 di version | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `SDCR_a009_sdcVersion` | page 9 | SDCR ECU: a009 sdc version | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `SDCR_a010_pgood` | page 10 | SDCR ECU: a010 pgood | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a010_boostRailV` | page 10 | SDCR ECU: a010 boost rail v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a010_Vref` | page 10 | SDCR ECU: a010 vref | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a011_IaAvg` | page 11 | SDCR ECU: a011 ia avg | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `SDCR_a011_IbAvg` | page 11 | SDCR ECU: a011 ib avg | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `SDCR_a012_boostRailV` | page 12 | SDCR ECU: a012 boost rail v | 16\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a012_HVBackupSupplyV` | page 12 | SDCR ECU: a012 HV backup supply v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a012_vBat` | page 12 | SDCR ECU: a012 v bat | 32\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a012_vbkupGoodFdbk` | page 12 | SDCR ECU: a012 vbkup good fdbk | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a013_boostRailV` | page 13 | SDCR ECU: a013 boost rail v | 16\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a013_HVBackupSupplyV` | page 13 | SDCR ECU: a013 HV backup supply v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a013_vBat` | page 13 | SDCR ECU: a013 v bat | 32\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a013_vbkupGoodFdbk` | page 13 | SDCR ECU: a013 vbkup good fdbk | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a014_reason_vBusShortedLow` | page 14 | SDCR ECU: a014 reason v bus shorted low | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a014_reason_vBusShortedHigh` | page 14 | SDCR ECU: a014 reason v bus shorted high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a014_boostRailV` | page 14 | SDCR ECU: a014 boost rail v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a014_HVBackupSupplyV` | page 14 | SDCR ECU: a014 HV backup supply v | 32\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a014_vBat` | page 14 | SDCR ECU: a014 v bat | 40\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a014_vbkupGoodFdbk` | page 14 | SDCR ECU: a014 vbkup good fdbk | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a015_reason_vPhaseShortedLow` | page 15 | SDCR ECU: a015 reason v phase shorted low | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a015_reason_vPhaseShortedHigh` | page 15 | SDCR ECU: a015 reason v phase shorted high | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a015_diSwitchingPin` | page 15 | SDCR ECU: a015 di switching pin | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a015_vBat` | page 15 | SDCR ECU: a015 v bat | 19\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a015_va` | page 15 | SDCR ECU: a015 va | 29\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a015_vb` | page 15 | SDCR ECU: a015 vb | 40\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a015_vc` | page 15 | SDCR ECU: a015 vc | 50\|10 | little-endian | unsigned | 2 | 0 | V | 0 to 2046 |  | plausible |
| `SDCR_a017_expectedConfigWord` | page 17 | SDCR ECU: a017 expected config word | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_a017_receivedConfigWord` | page 17 | SDCR ECU: a017 received config word | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_a017_configMismatch` | page 17 | SDCR ECU: a017 config mismatch | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_convStartTimeout` | page 17 | SDCR ECU: a017 conv start timeout | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_convCompleteTimeout` | page 17 | SDCR ECU: a017 conv complete timeout | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_dmaSpiTxTransferError` | page 17 | SDCR ECU: a017 dma spi tx transfer error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_dmaSpiRxTransferError` | page 17 | SDCR ECU: a017 dma spi rx transfer error | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a017_dmaSpiTimerEnabled` | page 17 | SDCR ECU: a017 dma spi timer enabled | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_pyroArmed` | page 18 | SDCR ECU: a018 pyro armed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_triggerReason_faultCurrents` | page 18 | SDCR ECU: a018 trigger reason fault currents | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_triggerReason_hvBadAtSpeed` | page 18 | SDCR ECU: a018 trigger reason hv bad at speed | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_triggerReason_highBackEMF` | page 18 | SDCR ECU: a018 trigger reason high back EMF | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_faultCurrentsDetected` | page 18 | SDCR ECU: a018 fault currents detected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_diUartMIA` | page 18 | SDCR ECU: a018 di uart MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_pmRunningPin` | page 18 | SDCR ECU: a018 pm running pin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_hvPowerGood` | page 18 | SDCR ECU: a018 hv power good | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_hvbkupPGoodPin` | page 18 | SDCR ECU: a018 hvbkup p good pin | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_hvPowerNotGoodQualified` | page 18 | SDCR ECU: a018 hv power not good qualified | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_speedValid` | page 18 | SDCR ECU: a018 speed valid | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_speedFromVoltage` | page 18 | SDCR ECU: a018 speed from voltage | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a018_HVBackupSupplyV` | page 18 | SDCR ECU: a018 HV backup supply v | 28\|7 | little-endian | unsigned | 0.3 | 0 | V | 0 to 38.1 |  | plausible |
| `SDCR_a018_boostRailV` | page 18 | SDCR ECU: a018 boost rail v | 35\|7 | little-endian | unsigned | 0.3 | 0 | V | 0 to 38.1 |  | plausible |
| `SDCR_a018_maxAbsSpeed` | page 18 | SDCR ECU: a018 max abs speed | 42\|12 | little-endian | signed | 1 | 0 | Hz | -2048 to 2047 |  | plausible |
| `SDCR_a018_vBat` | page 18 | SDCR ECU: a018 v bat | 54\|7 | little-endian | unsigned | 8 | 0 | V | 0 to 1016 |  | plausible |
| `SDCR_a019_faultReason_faultCurrentsAtSpeed` | page 19 | SDCR ECU: a019 fault reason fault currents at speed | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_faultReason_unmitigatedUCR` | page 19 | SDCR ECU: a019 fault reason unmitigated UCR | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_faultReason_propagating3PS` | page 19 | SDCR ECU: a019 fault reason propagating3 PS | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_speedWasValid` | page 19 | SDCR ECU: a019 speed was valid | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_imbalanceSeen` | page 19 | SDCR ECU: a019 imbalance seen | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_ucrSeen` | page 19 | SDCR ECU: a019 ucr seen | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_phaseVoltagePresent` | page 19 | SDCR ECU: a019 phase voltage present | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_speedFromVoltage` | page 19 | SDCR ECU: a019 speed from voltage | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a019_transientHandling` | page 19 | SDCR ECU: a019 transient handling | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ALL_SKIPPED`<br>1 = `SKIPPED_3PS`<br>2 = `3PS_EARLY_EXIT`<br>3 = `3PS_WAITED` | plausible |
| `SDCR_a019_maxAbsElcSpeed` | page 19 | SDCR ECU: a019 max abs elc speed | 26\|9 | little-endian | unsigned | 4 | 0 | Hz | 0 to 2044 |  | plausible |
| `SDCR_a019_avgIa` | page 19 | SDCR ECU: a019 avg ia | 35\|10 | little-endian | signed | 4 | 0 | A | -2048 to 2044 |  | plausible |
| `SDCR_a019_avgIb` | page 19 | SDCR ECU: a019 avg ib | 45\|10 | little-endian | signed | 4 | 0 | A | -2048 to 2044 |  | plausible |
| `SDCR_a019_maxAbsCurrents` | page 19 | SDCR ECU: a019 max abs currents | 55\|9 | little-endian | unsigned | 4 | 0 | A | 0 to 2044 |  | plausible |
| `SDCR_a020_errorCode` | page 20 | SDCR ECU: a020 error code | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 1 = `ADDRESS_OUT_OF_BOUNDS`<br>2 = `PAGE_ROLLOVER`<br>3 = `MUTEX_ERROR`<br>4 = `GENERIC_SPI_ERROR`<br>200 = `FAILED_READ_SANITY_CHECK`<br>201 = `FAILED_WRITE_SANITY_CHECK` | plausible |
| `SDCR_a020_rxData0` | page 20 | SDCR ECU: a020 rx data0 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_a020_rxData1` | page 20 | SDCR ECU: a020 rx data1 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_a020_rxData2` | page 20 | SDCR ECU: a020 rx data2 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_a020_rxData3` | page 20 | SDCR ECU: a020 rx data3 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_a020_rxData4` | page 20 | SDCR ECU: a020 rx data4 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_a021_busBarTempC` | page 21 | SDCR ECU: a021 bus bar temp c; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `SDCR_a021_busBarTempA` | page 21 | SDCR ECU: a021 bus bar temp a; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | plausible |
| `SDCR_a021_tempCVoltage` | page 21 | SDCR ECU: a021 temp c voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a021_tempAVoltage` | page 21 | SDCR ECU: a021 temp a voltage | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5.1 |  | plausible |
| `SDCR_a024_time` | page 24 | SDCR ECU: a024 time | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_diSwitchingFromUart` | page 25 | SDCR ECU: a025 di switching from uart | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_diSwitchingPin` | page 25 | SDCR ECU: a025 di switching pin | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_pmRunningPin` | page 25 | SDCR ECU: a025 pm running pin | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_diUartMIA` | page 25 | SDCR ECU: a025 di uart MIA | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a025_HVBackupSupplyV` | page 25 | SDCR ECU: a025 HV backup supply v | 24\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a025_boostRailV` | page 25 | SDCR ECU: a025 boost rail v | 32\|8 | little-endian | unsigned | 0.15 | 0 | V | 0 to 38.25 |  | plausible |
| `SDCR_a028_LVPowerState` | page 28 | SDCR ECU: a028 LV power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a029_uartCommsMissing` | page 29 | SDCR ECU: a029 uart comms missing | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a029_canCommsMissing` | page 29 | SDCR ECU: a029 can comms missing | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SDCR_a029_lvState` | page 29 | SDCR ECU: a029 lv state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ON`<br>2 = `GOING_DOWN`<br>3 = `FAULT` | plausible |
| `SDCR_a034_Ia` | page 34 | SDCR ECU: a034 ia | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `SDCR_a034_Ib` | page 34 | SDCR ECU: a034 ib | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |

## Multiplexing

`SDCR_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (6 signals), page 4 (4 signals), page 6 (16 signals), page 7 (13 signals), page 8 (1 signals), page 9 (2 signals), page 10 (3 signals), page 11 (2 signals), page 12 (4 signals), page 13 (4 signals), page 14 (6 signals), page 15 (7 signals), page 17 (8 signals), page 18 (16 signals), page 19 (13 signals), page 20 (6 signals), page 21 (4 signals), page 24 (1 signals), page 25 (6 signals), page 28 (1 signals), page 29 (3 signals), page 34 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All SDCR ECU messages (SDCR)](../../sdcr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
