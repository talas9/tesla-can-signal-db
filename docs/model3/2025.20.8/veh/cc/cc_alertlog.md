---
layout: default
title: "CC_alertLog (0x45C) — Charge cable controller, Tesla Model 3 2025.20.8 VEH CAN"
description: "Charge cable controller message: alert log. Tesla Model 3 CAN bus message CC_alertLog (0x45C) of Charge cable controller, firmware 2025.20.8, 62 signals (CC_alertID, CC_alertType, CC_a001_groundResistance, CC_a003_gfciRmsCurrent and 58 more). Bit layout, scaling, units and value tables."
---

# CC_alertLog (0x45C) — Charge cable controller, Tesla Model 3 2025.20.8 VEH CAN

Charge cable controller message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 62 signals of CC_alertLog as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CC_alertLog` |
| CAN id | 0x45C (1116) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 62 |

## Signals of CC_alertLog

Tesla Model 3 CAN bus signals in `CC_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CC_alertID` | selector | Charge cable controller: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_gndMonIntrptLineSide`<br>2 = `a002_gndMonIntrptLoadSide`<br>3 = `a003_CCIDTripped`<br>4 = `a004_CCIDSelfTestFault`<br>5 = `a005_groundedNeutral`<br>6 = `a006_inputOverCurrent`<br>7 = `a007_inputOverVoltage`<br>8 = `a008_inputUnderVoltage`<br>9 = `a009_inputMiswired`<br>10 = `a010_contactorWelded`<br>11 = `a011_ambientOT`<br>12 = `a012_wallPlugOT`<br>13 = `a013_vehConnOT`<br>14 = `a014_mcuSelfTestFault`<br>15 = `a015_PilotAFault`<br>16 = `a016_PilotBFault`<br>17 = `a017_PilotCFault`<br>18 = `a018_PilotDFault`<br>19 = `a019_proxDisconnected`<br>20 = `a020_3vRailIncorrect`<br>21 = `a021_CB_noMaster`<br>22 = `a022_CB_tooManyMasters`<br>23 = `a023_CB_tooManySlaves`<br>24 = `a024_CB_masterISetTooLow`<br>25 = `a025_evseTemp`<br>26 = `a026_wallPlugTemp`<br>27 = `a027_vehicleHandleTemp`<br>28 = `a028_CB_rotarySelect`<br>29 = `a029_PilotFFault`<br>30 = `a030_masterSlaveMismatch`<br>31 = `a031_pllLockLost`<br>32 = `a032_meteringFailure`<br>33 = `a033_vRefOutOfRange`<br>34 = `a034_bootAlert`<br>35 = `a035_CCIDCalibration`<br>36 = `a036_contactorStuckOpen`<br>37 = `a037_internalModuleWatchdogExpired`<br>38 = `a038_internalModuleMia`<br>39 = `a039_internalModuleOverTemp`<br>40 = `a040_handleTempFoldback`<br>41 = `a041_inputWiringFoldback`<br>42 = `a042_pcbaTempFoldback`<br>43 = `a043_configurationRequired`<br>44 = `a044_relayCoilVoltageRationality`<br>45 = `a045_ACPowerLoss`<br>46 = `a046_GFCIConfigInvalid`<br>47 = `a047_MDMotorContFault`<br>48 = `a048_ACMDAdapterFault`<br>49 = `a049_rs485Fault`<br>50 = `a050_eFuseFault`<br>51 = `a051_chcCriticalFault`<br>52 = `a052_vRefOutOfRangePWM`<br>57 = `a057_chcVitalsRequestFailure`<br>60 = `a060_persistenceFault`<br>61 = `a061_unfinishedCommissioning` | plausible |
| `CC_alertType` |  | Charge cable controller: alert type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `CC_a001_groundResistance` | page 1 | Charge cable controller: a001 ground resistance; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 1000 | 0 | Ohm | 0 to 4094000 | 4094 = `NO_GROUND`<br>4095 = `SNA` | plausible |
| `CC_a003_gfciRmsCurrent` | page 3 | Charge cable controller: a003 gfci rms current | 16\|12 | little-endian | unsigned | 0.001 | 0 | A | 0 to 4.095 |  | plausible |
| `CC_a003_gfciRmsCurrentAvg` | page 3 | Charge cable controller: a003 gfci rms current avg | 28\|12 | little-endian | unsigned | 0.001 | 0 | A | 0 to 4.095 |  | plausible |
| `CC_a003_dcGfciCurrent` | page 3 | Charge cable controller: a003 dc gfci current | 40\|10 | little-endian | signed | 0.001 | 0 | A | -0.512 to 0.511 |  | plausible |
| `CC_a003_gfciFaultReason` | page 3 | Charge cable controller: a003 gfci fault reason; raw 0 = signal not available (SNA) | 50\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `AC_LPF`<br>2 = `AC_PEAK`<br>3 = `DC_LPF`<br>4 = `DC_PEAK` | plausible |
| `CC_a003_gfciFaultBucket` | page 3 | Charge cable controller: a003 gfci fault bucket | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `CC_a004_gfciErrorReason` | page 4 | Charge cable controller: a004 gfci error reason; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 1 to 255 | 0 = `SNA`<br>1 = `IO_ERROR`<br>2 = `ASIC_REASON`<br>3 = `DC_OFFSET_ERROR`<br>4 = `AC_OFFSET_ERROR`<br>5 = `TEST_SIGNAL_ERROR` | plausible |
| `CC_a004_gfciAsicErrorBitfield` | page 4 | Charge cable controller: a004 gfci asic error bitfield | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a004_gfciSelfTestDuty` | page 4 | Charge cable controller: a004 gfci self test duty | 32\|16 | little-endian | signed | 0.0001 | 50 | A | 46.7232 to 53.2767 |  | plausible |
| `CC_a004_gfciSelfTestCurrent` | page 4 | Charge cable controller: a004 gfci self test current | 48\|16 | little-endian | signed | 0.0001 | 0 | A | -3.2768 to 3.2767 |  | plausible |
| `CC_a006_line1Current` | page 6 | Charge cable controller: a006 line1 current | 16\|16 | little-endian | unsigned | 0.01 | 0 | A | 0 to 655.35 |  | plausible |
| `CC_a006_line2Current` | page 6 | Charge cable controller: a006 line2 current | 32\|16 | little-endian | unsigned | 0.01 | 0 | A | 0 to 655.35 |  | plausible |
| `CC_a006_line3Current` | page 6 | Charge cable controller: a006 line3 current | 48\|16 | little-endian | unsigned | 0.01 | 0 | A | 0 to 655.35 |  | plausible |
| `CC_a007_inputVoltage` | page 7 | Charge cable controller: a007 input voltage | 16\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a007_inputLineVoltage` | page 7 | Charge cable controller: a007 input line voltage | 32\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a007_inputNeutralVoltage` | page 7 | Charge cable controller: a007 input neutral voltage | 48\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a008_inputVoltage` | page 8 | Charge cable controller: a008 input voltage | 16\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a008_inputLineVoltage` | page 8 | Charge cable controller: a008 input line voltage | 32\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a008_inputNeutralVoltage` | page 8 | Charge cable controller: a008 input neutral voltage | 48\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `CC_a010_line1Voltage` | page 10 | Charge cable controller: a010 line1 voltage | 16\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a010_line2Voltage` | page 10 | Charge cable controller: a010 line2 voltage | 28\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a010_line3Voltage` | page 10 | Charge cable controller: a010 line3 voltage | 40\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a010_line1StuckClosed` | page 10 | Charge cable controller: a010 line1 stuck closed | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a010_line2StuckClosed` | page 10 | Charge cable controller: a010 line2 stuck closed | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a010_line3StuckClosed` | page 10 | Charge cable controller: a010 line3 stuck closed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a011_pcbaTemp` | page 11 | Charge cable controller: a011 pcba temp | 16\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |
| `CC_a012_inputThermopile` | page 12 | Charge cable controller: a012 input thermopile | 16\|12 | little-endian | unsigned | 1.0e-06 | 0 | V | 0 to 0.004095 |  | plausible |
| `CC_a012_inputThermopileDvdt` | page 12 | Charge cable controller: a012 input thermopile dvdt | 28\|12 | little-endian | unsigned | 1.0e-06 | 0 | V/sec | 0 to 0.004095 |  | plausible |
| `CC_a013_handleTemp` | page 13 | Charge cable controller: a013 handle temp | 16\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |
| `CC_a014_failureCause` | page 14 | Charge cable controller: a014 failure cause | 16\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 | 1 = `OTHER`<br>2 = `CONFIG_NOT_RECEIVED`<br>3 = `METER_INIT_FAILED`<br>4 = `DCGFCI_INIT_FAILED` | plausible |
| `CC_a014_meterFaultAddress` | page 14 | Charge cable controller: a014 meter fault address | 25\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `CC_a014_meterFaultData` | page 14 | Charge cable controller: a014 meter fault data | 41\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `CC_a014_meterRetryCount` | page 14 | Charge cable controller: a014 meter retry count | 57\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `CC_a015_pilotHighVolage` | page 15 | Charge cable controller: a015 pilot high volage | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | plausible |
| `CC_a015_smState` | page 15 | Charge cable controller: a015 sm state | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a027_handleTemperature` | page 27 | Charge cable controller: a027 handle temperature | 16\|12 | little-endian | signed | 0.1 | 0 | DegC | -204.8 to 204.7 |  | plausible |
| `CC_a027_handleTempFaultReason` | page 27 | Charge cable controller: a027 handle temp fault reason | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TEMP_GOOD`<br>1 = `NTC_OPEN_CIRCUIT`<br>2 = `NTC_BUTTON_PRESSED`<br>3 = `CHC_INVALID_VITAL`<br>4 = `CHC_SHORT_CIRCUIT`<br>5 = `CHC_OPEN_CIRCUIT` | plausible |
| `CC_a032_meteringSpiCommsFailure` | page 32 | Charge cable controller: a032 metering spi comms failure | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a032_meteringConfigMismatch` | page 32 | Charge cable controller: a032 metering config mismatch | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a033_nominalVoltage` | page 33 | Charge cable controller: a033 nominal voltage | 16\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `CC_a033_measuredVoltage` | page 33 | Charge cable controller: a033 measured voltage | 25\|9 | little-endian | unsigned | 0.01 | 0 | V | 0 to 5.11 |  | plausible |
| `CC_a036_line1Voltage` | page 36 | Charge cable controller: a036 line1 voltage | 16\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a036_line2Voltage` | page 36 | Charge cable controller: a036 line2 voltage | 28\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a036_line3Voltage` | page 36 | Charge cable controller: a036 line3 voltage | 40\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `CC_a036_line1StuckOpen` | page 36 | Charge cable controller: a036 line1 stuck open | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a036_line2StuckOpen` | page 36 | Charge cable controller: a036 line2 stuck open | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a036_line3StuckOpen` | page 36 | Charge cable controller: a036 line3 stuck open | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CC_a037_expiredWatchdogModuleId` | page 37 | Charge cable controller: a037 expired watchdog module id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a037_expiredWatchdogTaskId` | page 37 | Charge cable controller: a037 expired watchdog task id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a037_expiredWatchdogAppCRC` | page 37 | Charge cable controller: a037 expired watchdog app CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `CC_a038_moduleMiaModuleId` | page 38 | Charge cable controller: a038 module mia module id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a038_moduleMiaTaskId` | page 38 | Charge cable controller: a038 module mia task id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CC_a038_moduleMiaAppCRC` | page 38 | Charge cable controller: a038 module mia app CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `CC_a039_intModuleTemperature` | page 39 | Charge cable controller: a039 int module temperature | 16\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |
| `CC_a040_handleTemperature` | page 40 | Charge cable controller: a040 handle temperature | 16\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |
| `CC_a041_inputThermopile` | page 41 | Charge cable controller: a041 input thermopile | 16\|16 | little-endian | signed | 1.0e-06 | 0 | V | -0.032768 to 0.032767 |  | plausible |
| `CC_a041_inputThermopileDvdt` | page 41 | Charge cable controller: a041 input thermopile dvdt | 32\|16 | little-endian | signed | 1.0e-06 | 0 | V/sec | -0.032768 to 0.032767 |  | plausible |
| `CC_a042_pcbaTemperature` | page 42 | Charge cable controller: a042 pcba temperature | 16\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |
| `CC_a044_relayCoilVoltage` | page 44 | Charge cable controller: a044 relay coil voltage | 16\|8 | little-endian | unsigned | 0.14 | 0 | V | 0 to 35.7 |  | plausible |
| `CC_a044_pcbaTemperature` | page 44 | Charge cable controller: a044 pcba temperature | 24\|9 | little-endian | signed | 1 | 88 | DegC | -168 to 343 |  | plausible |

## Multiplexing

`CC_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 3 (5 signals), page 4 (4 signals), page 6 (3 signals), page 7 (3 signals), page 8 (3 signals), page 10 (6 signals), page 11 (1 signals), page 12 (2 signals), page 13 (1 signals), page 14 (4 signals), page 15 (2 signals), page 27 (2 signals), page 32 (2 signals), page 33 (2 signals), page 36 (6 signals), page 37 (3 signals), page 38 (3 signals), page 39 (1 signals), page 40 (1 signals), page 41 (2 signals), page 42 (1 signals), page 44 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
