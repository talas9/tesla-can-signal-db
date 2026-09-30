---
layout: default
title: "RADC_alertLog (0x555) — Radar, Tesla Model Y 2025.20.8 CH CAN"
description: "Radar message: alert log. Tesla Model Y CAN bus message RADC_alertLog (0x555) of Radar, firmware 2025.20.8, 86 signals (RADC_alertID, RADC_alertState, RADC_a002_ecuAdcErrType, RADC_a008_interLockErrType and 82 more). Bit layout, scaling, units and value tables."
---

# RADC_alertLog (0x555) — Radar, Tesla Model Y 2025.20.8 CH CAN

Radar message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 86 signals of RADC_alertLog as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RADC_alertLog` |
| CAN id | 0x555 (1365) |
| ECU | [Radar](../../radc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RADC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 86 |

## Signals of RADC_alertLog

Tesla Model Y CAN bus signals in `RADC_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RADC_alertID` | selector | Radar: alert ID | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_can1BusOff`<br>2 = `a002_ecuAdcError`<br>3 = `a003_ecuBistDisabled`<br>4 = `a004_ecuCrcHwError`<br>5 = `a005_ecuEcuMError`<br>6 = `a006_ecuFimError`<br>7 = `a007_ecuGptCheckError`<br>8 = `a008_ecuHwSwInterlock`<br>9 = `a009_plantModeActive`<br>10 = `a010_ecuIoHwAbError`<br>11 = `a011_ecuMcemError`<br>12 = `a012_ecuSpiError`<br>13 = `a013_ecuWdgError`<br>14 = `a014_fctSelfTestNotDone`<br>15 = `a015_fctSenInterference`<br>16 = `a016_adcOverVolt`<br>17 = `a017_adcUnderVolt`<br>18 = `a018_internalHardwareFault`<br>19 = `a019_internalSoftwareFault`<br>20 = `a020_overTemp`<br>21 = `a021_overTempCrit`<br>22 = `a022_tempImplausible`<br>23 = `a023_underTemp`<br>24 = `a024_underTempCrit`<br>25 = `a025_overVoltage`<br>26 = `a026_underVoltage`<br>27 = `a027_nvmFailure`<br>28 = `a028_rfChipError`<br>29 = `a029_rhcError`<br>30 = `a030_rspError`<br>31 = `a031_sensorMisaligned`<br>32 = `a032_sensorBlocked`<br>33 = `a033_sensorNeverAligned`<br>34 = `a034_vehDynamicsError`<br>35 = `a035_vinMIA`<br>36 = `a036_carConfigMIA`<br>37 = `a037_inertialSignalsMIA`<br>38 = `a038_steeringWheelAngleMIA`<br>39 = `a039_vehicleStateMIA`<br>40 = `a040_wheelSpeedsMIA`<br>41 = `a041_vinErr`<br>42 = `a042_carConfigErr`<br>43 = `a043_inertialSignalsErr`<br>44 = `a044_steeringWheelAngleErr`<br>45 = `a045_vehicleStateErr`<br>46 = `a046_wheelSpeedsErr`<br>47 = `a047_mismatchChassisType`<br>48 = `a048_mismatchAirSuspension`<br>49 = `a049_mismatchFourWheelDrive`<br>50 = `a050_mismatchCountry`<br>51 = `a051_mismatchEPASType`<br>52 = `a052_mismatcRadPos`<br>53 = `a053_emError`<br>54 = `a054_blockageInfo_Frame_1`<br>55 = `a055_blockageInfo_Frame_2` | plausible |
| `RADC_alertState` |  | Radar: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `RADC_a002_ecuAdcErrType` | page 2 | Radar: a002 ecu adc err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `LIMIT_RANGE`<br>1 = `INVALID_CONV_MODE` | plausible |
| `RADC_a008_interLockErrType` | page 8 | Radar: a008 inter lock err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `HW_SW_PROJECT_ID_INCOMPATIBLE`<br>1 = `SW_VERSION_MISMATCH` | plausible |
| `RADC_a011_ecuMcemErrType` | page 11 | Radar: a011 ecu mcem err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `MCU_E_QUARTZ_FAILURE`<br>1 = `MCU_E_MCRGM_PERIODIC_CHECK`<br>2 = `MCU_E_MCPCU_PERIODIC_CHECK`<br>3 = `MCU_E_MCME_PERIODIC_CHECK`<br>4 = `MCU_E_CLOCK_FAILURE`<br>5 = `MCEM_E_OPERATION_FAILED`<br>6 = `MCEM_E_INIT_FAILED`<br>7 = `MCEM_E_FORBIDDEN_INVOCATION`<br>8 = `MCEM_E_FAULT`<br>9 = `MCEM_E_CORRUPTED_HW_CONFIG`<br>10 = `MCEM__ALARM_ISR` | plausible |
| `RADC_a013_ecuWdgErrType` | page 13 | Radar: a013 ecu wdg err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `UNLOCKED`<br>1 = `INVALID_CALL`<br>2 = `DISABLE_REJECTED`<br>3 = `CORRUPT_CONFIG` | plausible |
| `RADC_a016_adcOverVoltType` | page 16 | Radar: a016 adc over volt type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `1V25_SMPS_OVER_VOLTAGE`<br>1 = `3V3_LIN_VOLTAGECO_OVER_VOLTAGE`<br>2 = `3V3_LIN_PA_OVER_VOLTAGE`<br>3 = `3V3_LIN_DIGITAL_OVER_VOLTAGE`<br>4 = `3V3_LIN_ANALOG_OVER_VOLTAGE`<br>5 = `3V8_SMPS_OVER_VOLTAGE`<br>6 = `4V5_LIN_VOLTAGECO_OVER_VOLTAGE`<br>7 = `5V_SMPS_OVER_VOLTAGE` | plausible |
| `RADC_a016_adcVoltage` | page 16 | Radar: a016 adc voltage | 24\|6 | little-endian | unsigned | 0.1 | 0 | v | 0 to 6.3 |  | plausible |
| `RADC_a017_adcUnderVoltType` | page 17 | Radar: a017 adc under volt type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `1V25_SMPS_UNDER_VOLTAGE`<br>1 = `3V3_LIN_VOLTAGECO_UNDER_VOLTAGE`<br>2 = `3V3_LIN_PA_UNDER_VOLTAGE`<br>3 = `3V3_LIN_DIGITAL_UNDER_VOLTAGE`<br>4 = `3V3_LIN_ANALOG_UNDER_VOLTAGE`<br>5 = `3V8_SMPS_UNDER_VOLTAGE`<br>6 = `4V5_LIN_VOLTAGECO_UNDER_VOLTAGE`<br>7 = `5V_SMPS_UNDER_VOLTAGE` | plausible |
| `RADC_a017_adcVoltage` | page 17 | Radar: a017 adc voltage | 24\|6 | little-endian | unsigned | 0.1 | 0 | v | 0 to 6.3 |  | plausible |
| `RADC_a019_internalSWFaultType` | page 19 | Radar: a019 internal SW fault type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `TEMP_MON`<br>2 = `MCU_SUPPLY`<br>3 = `RAM_ECC_1BIT`<br>4 = `ROM_ECC_1BIT`<br>5 = `RAM_ECC_2BIT`<br>6 = `ROM_ECC_2BIT`<br>7 = `EXCEPT_CRIT_INPUT`<br>8 = `EXCEPT_MACH_CHECK`<br>9 = `EXCEPT_DATA_STORE`<br>10 = `EXCEPT_INSTRUCT_STORE`<br>11 = `EXCEPT_ALIGN`<br>12 = `EXCEPT_PROGRAM`<br>13 = `EXCEPT_PERFORMANCEMON`<br>14 = `EXCEPT_DEBUG`<br>15 = `EXCEPT_FIXED_INTER`<br>16 = `EXCEPT_WATCHDOG_TIMER`<br>17 = `EXCEPT_DATA_TLB_ERROR`<br>18 = `EXCEPT_INSTR_TLB_ERROR`<br>19 = `EXCEPT_SPE_UNAVAIL`<br>20 = `EXCEPT_EFP_DATA`<br>21 = `EXCEPT_EFP_ROUND`<br>22 = `EXCEPT_SHUTDOWN_OS`<br>23 = `EXCEPT_ERROR_SRAM`<br>24 = `EXCEPT_ERROR_TPU_RAM`<br>25 = `EXCEPT_UNDEFINED`<br>26 = `SYSTEM_CYCLE_MON`<br>27 = `TASK_MON_LOGIC`<br>28 = `TASK_STACK`<br>29 = `AD_CONVERTER`<br>30 = `DCACHE_MARCHC`<br>31 = `ECC_TIMEOUT`<br>32 = `SRAM_ADDRESS_BUS0`<br>33 = `SRAM_ADDRESS_BUS1`<br>34 = `TPU_RAM_ADDRESS_BUS0`<br>35 = `TPU_RAM_ADDRESS_BUS1`<br>36 = `CPU_REGISTER_CHECK`<br>37 = `CONFIG_REGISTER_CHECK`<br>38 = `APPL_CRC_CHECK`<br>39 = `MISC_CHECK`<br>40 = `ALU_CHECK`<br>41 = `UNEXPECTED_RESET`<br>42 = `BUS_TEST`<br>43 = `INVALID_SAFESECTION`<br>44 = `EXCEPT_CORE_FREEZE`<br>45 = `TESTCASE_ABORT`<br>46 = `TESTCASE_CONFIG`<br>47 = `CYCLE_MON`<br>48 = `INTENTIONAL_RESET`<br>49 = `FCCU`<br>50 = `E_FLOATINGPOINT_UNAVAIL`<br>51 = `EXCEPT_SYSTEM_CALL`<br>52 = `EXCEPT_AP_UNAVAILABLE`<br>53 = `EXCEPT_DECREMENTER`<br>54 = `EXCEPT_ECC1BITERROR`<br>55 = `EXCEPT_ECC2BITERROR`<br>56 = `NVM_TIMEOUT`<br>57 = `CORE1_STACK_OVERFLOW`<br>58 = `CORE2_STACK_OVERFLOW`<br>59 = `DRIVERINIT_FAILED`<br>60 = `ECC_HARDWARE_FAILURE`<br>61 = `ECC_DMA_2BIT`<br>62 = `ECC_SPT_2BIT`<br>63 = `FPU_CHECK`<br>64 = `SPE_CHECK`<br>65 = `HW_SW_INCOMPATIBLE`<br>66 = `FCCU_CORRUPTED_CONFIG`<br>67 = `FCCU_FAULT_SIGNALED`<br>68 = `CLKMON_INITIALIZATION`<br>69 = `CLKMON_CONFIG_CHECK`<br>70 = `CLKMON_CALIBRATION`<br>71 = `WATCHDOG_INITIALIZATION`<br>72 = `WATCHDOG`<br>73 = `ECC_PATTERN_MISSING`<br>74 = `IOHWAB`<br>75 = `SMPU`<br>76 = `ECC_SRAM_2BIT`<br>77 = `ECC_FLASH_2BIT`<br>78 = `ECC_EEPROM_2BIT`<br>79 = `ECC_CORE_DMEM_2BIT`<br>80 = `ECC_CORE_IMEM_2BIT`<br>81 = `ECC_CORE_DCACHE_2BIT`<br>82 = `ECC_CORE_ICACHE_2BIT`<br>83 = `ECC_OTHER_2BIT`<br>84 = `SPI_MMIC_FAULT`<br>85 = `SPI_MMIC_MISMATCH`<br>86 = `SPI_ATIC_FAULT`<br>87 = `ECUM_REQUEST`<br>88 = `PLL_STUCK`<br>89 = `FCCU_CHECKER_MISMATCH`<br>90 = `FCCU_HEALED_FAULT`<br>91 = `EXCEPT_CENTRAL`<br>92 = `EXCEPT_TRAP`<br>93 = `EXCEPT_RESERVED_13`<br>94 = `EXCEPT_RESERVED_14`<br>95 = `EXCEPT_RESERVED_15`<br>96 = `UBATT_OUT_OF_RANGE`<br>97 = `IOHWAB_TIMEOUT`<br>98 = `POWERUP_SEQ_TIMEOUT`<br>99 = `FLSP_INIT_FAILED`<br>100 = `RADAR_CYCLE_VIOLATION`<br>101 = `ECC_INIT_FAILED`<br>102 = `TEMP_CROSS_CHECK`<br>103 = `STARTUP_ERROR`<br>104 = `MBIST_FAILED`<br>105 = `LBIST_FAILED`<br>106 = `ATIC_RESET`<br>107 = `INTERNAL_VOLTAGE_FAILED`<br>108 = `FLASH_CYCLIC_CHECK`<br>109 = `PROCESSOR_VERSION`<br>110 = `ADC_CALIBRATION` | plausible |
| `RADC_a019_internalSWFaultCoreID` | page 19 | Radar: a019 internal SW fault core ID | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `0`<br>1 = `1`<br>2 = `2` | plausible |
| `RADC_a020_ecuTemp` | page 20 | Radar: a020 ecu temp | 16\|16 | little-endian | unsigned | 0.1 | -44 | deg | -44 to 6509.5 |  | plausible |
| `RADC_a023_ecuTemp` | page 23 | Radar: a023 ecu temp | 16\|16 | little-endian | unsigned | 0.1 | -44 | deg | -44 to 6509.5 |  | plausible |
| `RADC_a025_ecuVoltage` | page 25 | Radar: a025 ecu voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | v | 0 to 25.5 |  | plausible |
| `RADC_a026_ecuVoltage` | page 26 | Radar: a026 ecu voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | v | 0 to 25.5 |  | plausible |
| `RADC_a027_nvmFailureType` | page 27 | Radar: a027 nvm failure type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `RECORD_SIZE_MISSMATCH`<br>1 = `REQ_FAILED`<br>2 = `INTEGRITY_FAILED` | plausible |
| `RADC_a028_rfComRegCheckFail` | page 28 | Radar: a028 rf com reg check fail | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `REG_CHECK_CYCLE_FAILED`<br>1 = `REG_CHECK_FAILED`<br>2 = `REG_CHECK_FAILED_LT`<br>3 = `MON_RF_CHIP_TEMP_IMPLAUSIBLE`<br>4 = `MON_RF_OVERTEMP` | plausible |
| `RADC_a029_rhcChirpMonErrType` | page 29 | Radar: a029 rhc chirp mon err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `FREQ_ERROR_SPEC_TOO_LARGE_NS`<br>1 = `RMSE_TOO_LARGE_NS`<br>2 = `RG_LENGTH_ERROR_NS` | plausible |
| `RADC_a029_rhcRxLongTermErrType` | page 29 | Radar: a029 rhc rx long term err type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONLINEAR_ERR_LT`<br>1 = `STC_FILTER_ERR_LT`<br>2 = `CHANNEL_VARIATION_ERR_LT`<br>3 = `TRANSFER_FUNCTION_ERR_LT`<br>4 = `SIGNAL_POWER_TOO_LOW_LT`<br>5 = `SPURIOUS_PEAKS_TOO_HIGH_LT`<br>6 = `NOISE_POWER_TOO_HIGH_LT` | plausible |
| `RADC_a029_rhcRxErrType` | page 29 | Radar: a029 rhc rx err type | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `RX_NONLINEAR_ERR`<br>1 = `RX_STC_FILTER_ERR`<br>2 = `RX_CHANNEL_VARIATION_ERR`<br>3 = `RX_TRANSFER_FUNCTION_ERR`<br>4 = `RX_SIGNAL_POWER_TOO_LOW`<br>5 = `RX_NOISE_POWER_TOO_HIGH`<br>6 = `LOAD_PULLING_TOO_HIGH_NS`<br>7 = `RX_SPURIOUS_PEAKS_TOO_HIGH` | plausible |
| `RADC_a029_rhcVcoPowerErrType` | page 29 | Radar: a029 rhc vco power err type | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `HIGH`<br>1 = `LOW` | plausible |
| `RADC_a029_rhcSp1ErrType` | page 29 | Radar: a029 rhc sp1 err type | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `RHC_CTE_LUT_DUR_STUCK_ERR` | plausible |
| `RADC_a029_rhcFdcErrType` | page 29 | Radar: a029 rhc fdc err type | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DRIFT_FREQ_TOO_LARGE_NS`<br>1 = `RMSE_TOO_LARGE_NS`<br>2 = `LONG_TERM_ERROR_NS` | plausible |
| `RADC_a030_rspErrType` | page 30 | Radar: a030 rsp err type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `SHORT_TERM_ERROR`<br>1 = `LONG_TERM_ERROR` | plausible |
| `RADC_a031_horizMisalignAngle` | page 31 | Radar: a031 horiz misalign angle | 16\|8 | little-endian | unsigned | 0.001953125 | -0.25 | rad | -0.25 to 0.248046875 |  | plausible |
| `RADC_a031_vertMisalignAngle` | page 31 | Radar: a031 vert misalign angle | 24\|12 | little-endian | unsigned | 0.0001220703125 | -0.25 | rad | -0.25 to 0.249877929688 |  | plausible |
| `RADC_a032_blockageType` | page 32 | Radar: a032 blockage type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALN_PATH_COMP_HIGH_NEAR`<br>1 = `FCTSEN_INC_BLOCKAGE`<br>2 = `FCTSEN_DEC_BLOCKAGE`<br>3 = `FCTSEN_BLOCKAGE`<br>4 = `FCTSEN_OBJ_NOT_MEASURED` | plausible |
| `RADC_a032_block_SPMBlockageState` | page 32 | Radar: a032 block SPM blockage state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DB_NO_DAMP`<br>1 = `GDB_INC_DAMP`<br>2 = `GDB_FULL_DAMP`<br>3 = `GDB_RDC_DAMP`<br>4 = `GDB_UNKNOWN_DAMP` | plausible |
| `RADC_a032_block_dummy` | page 32 | Radar: a032 block dummy | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `RADC_a032_block_SPMSelfTestState` | page 32 | Radar: a032 block SPM self test state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ON`<br>2 = `STARTUP`<br>3 = `ROADBEAM_TEST` | plausible |
| `RADC_a032_block_ucEstiRange` | page 32 | Radar: a032 block uc esti range | 32\|8 | little-endian | unsigned | 1 | 0 | m | 0 to 255 |  | plausible |
| `RADC_a032_block_ucEstiRangeConf` | page 32 | Radar: a032 block uc esti range conf | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a032_block_ucEstiRangeProb` | page 32 | Radar: a032 block uc esti range prob | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a032_block_ucTimeoutBlkConf` | page 32 | Radar: a032 block uc timeout blk conf | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a035_msgId` | page 35 | Radar: a035 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a036_msgId` | page 36 | Radar: a036 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a037_msgId` | page 37 | Radar: a037 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a038_msgId` | page 38 | Radar: a038 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a039_msgId` | page 39 | Radar: a039 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a040_msgId` | page 40 | Radar: a040 msg id | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a041_vinErrType` | page 41 | Radar: a041 vin err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a041_vinErrExp` | page 41 | Radar: a041 vin err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a041_vinErrRx` | page 41 | Radar: a041 vin err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a041_msgId` | page 41 | Radar: a041 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a042_carConfigErrType` | page 42 | Radar: a042 car config err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a042_carConfigErrExp` | page 42 | Radar: a042 car config err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a042_carConfigErrRx` | page 42 | Radar: a042 car config err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a042_msgId` | page 42 | Radar: a042 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a043_inertialSignalsErrType` | page 43 | Radar: a043 inertial signals err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a043_inertialSignalsErrExp` | page 43 | Radar: a043 inertial signals err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a043_inertialSignalsErrRx` | page 43 | Radar: a043 inertial signals err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a043_msgId` | page 43 | Radar: a043 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a044_stwAngleErrType` | page 44 | Radar: a044 stw angle err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a044_stwAngleErrExp` | page 44 | Radar: a044 stw angle err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a044_stwAngleErrRx` | page 44 | Radar: a044 stw angle err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a044_msgId` | page 44 | Radar: a044 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a045_vehicleStateErrType` | page 45 | Radar: a045 vehicle state err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a045_vehicleStateErrExp` | page 45 | Radar: a045 vehicle state err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a045_vehicleStateErrRx` | page 45 | Radar: a045 vehicle state err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a045_msgId` | page 45 | Radar: a045 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a046_wheelSpeedsErrType` | page 46 | Radar: a046 wheel speeds err type | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `RADC_a046_wheelSpeedsErrExp` | page 46 | Radar: a046 wheel speeds err exp | 20\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a046_wheelSpeedsErrRx` | page 46 | Radar: a046 wheel speeds err rx | 36\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a046_msgId` | page 46 | Radar: a046 msg id | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `RADC_a047_chassisTypeExp` | page 47 | Radar: a047 chassis type exp; raw 7 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `MODEL_S_CHASSIS`<br>1 = `MODEL_X_CHASSIS`<br>2 = `MODEL_3_CHASSIS`<br>7 = `SNA` | plausible |
| `RADC_a047_chassisTypeRx` | page 47 | Radar: a047 chassis type rx; raw 7 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `MODEL_S_CHASSIS`<br>1 = `MODEL_X_CHASSIS`<br>2 = `MODEL_3_CHASSIS`<br>7 = `SNA` | plausible |
| `RADC_a048_airSuspensionExp` | page 48 | Radar: a048 air suspension exp; raw 7 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `STANDARD`<br>2 = `PLUS`<br>3 = `TESLA_STANDARD`<br>4 = `TESLA_PLUS`<br>5 = `TESLA_ADAPTIVE`<br>7 = `SNA` | plausible |
| `RADC_a048_airSuspensionRx` | page 48 | Radar: a048 air suspension rx; raw 7 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `NONE`<br>1 = `STANDARD`<br>2 = `PLUS`<br>3 = `TESLA_STANDARD`<br>4 = `TESLA_PLUS`<br>5 = `TESLA_ADAPTIVE`<br>7 = `SNA` | plausible |
| `RADC_a049_fourWheelDriveExp` | page 49 | Radar: a049 four wheel drive exp; raw 3 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `2WD`<br>1 = `4WD`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `RADC_a049_fourWheelDriveRx` | page 49 | Radar: a049 four wheel drive rx; raw 3 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `2WD`<br>1 = `4WD`<br>2 = `UNUSED`<br>3 = `SNA` | plausible |
| `RADC_a050_countryExp` | page 50 | Radar: a050 country exp | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a050_countryRx` | page 50 | Radar: a050 country rx | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_a051_epasTypeExp` | page 51 | Radar: a051 epas type exp; raw 7 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `BOSCH_L538`<br>1 = `BOSCH_L405`<br>2 = `MANDO_FGR64`<br>3 = `MANDO_VGR66`<br>4 = `MANDO_VGR63_GEN3`<br>7 = `SNA` | plausible |
| `RADC_a051_epasTypeRx` | page 51 | Radar: a051 epas type rx; raw 7 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `BOSCH_L538`<br>1 = `BOSCH_L405`<br>2 = `MANDO_FGR64`<br>3 = `MANDO_VGR66`<br>4 = `MANDO_VGR63_GEN3`<br>7 = `SNA` | plausible |
| `RADC_a052_radarPositionExp` | page 52 | Radar: a052 radar position exp; raw 7 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `MODELS`<br>1 = `MODELS_2`<br>2 = `MODELX`<br>3 = `MODEL_3`<br>7 = `SNA` | plausible |
| `RADC_a052_radarPositionRx` | page 52 | Radar: a052 radar position rx; raw 7 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `MODELS`<br>1 = `MODELS_2`<br>2 = `MODELX`<br>3 = `MODEL_3`<br>7 = `SNA` | plausible |
| `RADC_a054_block_ucObjLossProb` | page 54 | Radar: a054 block uc obj loss prob | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a054_block_ucObjLossConf` | page 54 | Radar: a054 block uc obj loss conf | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a054_block_ucOverallProb` | page 54 | Radar: a054 block uc overall prob | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a054_block_ucOverallConf` | page 54 | Radar: a054 block uc overall conf | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a054_block_RoadbeamTimeCnt` | page 54 | Radar: a054 block roadbeam time cnt | 48\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65535 |  | plausible |
| `RADC_a055_block_usTimeoutWayCnt` | page 55 | Radar: a055 block us timeout way cnt | 16\|16 | little-endian | unsigned | 1 | 0 | m | 0 to 65535 |  | plausible |
| `RADC_a055_block_ucTimeoutTimeCnt` | page 55 | Radar: a055 block uc timeout time cnt | 32\|8 | little-endian | unsigned | 1 | 0 | s | 0 to 255 |  | plausible |
| `RADC_a055_bblock_ucTimeoutBlkProb` | page 55 | Radar: a055 bblock uc timeout blk prob | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_a055_block_usFullBlkTimer` | page 55 | Radar: a055 block us full blk timer | 48\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65535 |  | plausible |

## Multiplexing

`RADC_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (1 signals), page 8 (1 signals), page 11 (1 signals), page 13 (1 signals), page 16 (2 signals), page 17 (2 signals), page 19 (2 signals), page 20 (1 signals), page 23 (1 signals), page 25 (1 signals), page 26 (1 signals), page 27 (1 signals), page 28 (1 signals), page 29 (6 signals), page 30 (1 signals), page 31 (2 signals), page 32 (8 signals), page 35 (1 signals), page 36 (1 signals), page 37 (1 signals), page 38 (1 signals), page 39 (1 signals), page 40 (1 signals), page 41 (4 signals), page 42 (4 signals), page 43 (4 signals), page 44 (4 signals), page 45 (4 signals), page 46 (4 signals), page 47 (2 signals), page 48 (2 signals), page 49 (2 signals), page 50 (2 signals), page 51 (2 signals), page 52 (2 signals), page 54 (5 signals), page 55 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Radar messages (RADC)](../../radc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
