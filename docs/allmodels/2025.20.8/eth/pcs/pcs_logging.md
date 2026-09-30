---
layout: default
title: "PCS_logging (0x2C4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Power conversion system (on-board charger and DC-DC converter) message: logging. Ethernet-side message PCS_logging of Power conversion system (on-board charger and DC-DC converter) for Tesla Model 3 / Model Y firmware 2025.20.8, 97 signals (PCS_logMessageSelect, PCS_chgPhAInputIrms, PCS_chgPhAIntBusV, PCS_chgPhAIntBusVTarget and 93 more). Bit layout, scaling, units and value tables."
---

# PCS_logging (0x2C4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 / Model Y 2025.20.8 ETH

Power conversion system (on-board charger and DC-DC converter) message: logging. This page documents the 97 signals of PCS_logging as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_logging` |
| Ethernet-side id | 0x2C4 (708) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 97 |

## Signals of PCS_logging

Tesla Model 3 / Model Y CAN bus signals in `PCS_logging`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_logMessageSelect` | selector | Power conversion system (on-board charger and DC-DC converter): log message select | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `PHA_1`<br>1 = `PHB_1`<br>2 = `PHC_1`<br>3 = `CHG_1`<br>4 = `CHG_2`<br>5 = `CHG_3`<br>6 = `DCDC_1`<br>7 = `DCDC_2`<br>8 = `DCDC_3`<br>9 = `SYSTEM_1`<br>10 = `PHA_2`<br>11 = `PHB_2`<br>12 = `PHC_2`<br>13 = `CHG_4`<br>14 = `DLOG_1`<br>15 = `DLOG_2`<br>16 = `DLOG_3`<br>17 = `DLOG_4`<br>18 = `DCDC_4`<br>19 = `DCDC_5`<br>20 = `CHG_NO_FLOW`<br>21 = `CHG_LINE_OFFSET`<br>22 = `DCDC_STATISTICS`<br>23 = `CHG_MACHINEMODEL`<br>24 = `DCDC_HVBUS_PCHG_DATA`<br>25 = `DCDC_IMPEDANCE_EST`<br>26 = `PROCESSOR_DIE_ID`<br>27 = `NUM_MSGS` | plausible |
| `PCS_chgPhAInputIrms` | page 0 | AC charger phase A's sensed RMS input current | 5\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51.1 |  | validated |
| `PCS_chgPhAIntBusV` | page 0 | AC charger phase A's sensed intermediate bus voltage | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhAIntBusVTarget` | page 0 | AC charger phase A's intermediate bus voltage target | 23\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhAOutputI` | page 0 | AC charger phase A sensed output current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | validated |
| `PCS_chgPhAInputCurrentLimitReason` | page 0 | Provides the reason behind the input AC charging current limit for phase A | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PCS_IAC_LIMITED_BY_NONE`<br>1 = `PCS_IAC_LIMITED_BY_RIPPLE_RELAXED`<br>2 = `PCS_IAC_LIMITED_BY_OUTPUT_POWER`<br>3 = `PCS_IAC_LIMITED_BY_INPUT_POWER`<br>4 = `PCS_IAC_LIMITED_BY_PHASE_THERMAL_LIMIT`<br>5 = `PCS_IAC_LIMITED_BY_PHASE_MACHINE_MODEL` | validated |
| `PCS_chgPhBInputIrms` | page 1 | AC charger phase B's sensed RMS input current | 5\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51.1 |  | validated |
| `PCS_chgPhBIntBusV` | page 1 | AC charger phase B's sensed intermediate bus voltage | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhBIntBusVTarget` | page 1 | AC charger phase B's intermediate bus voltage target | 23\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhBOutputI` | page 1 | AC charger phase B sensed output current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | validated |
| `PCS_chgPhBInputCurrentLimitReason` | page 1 | Provides the reason behind the input AC charging current limit for phase B | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PCS_IAC_LIMITED_BY_NONE`<br>1 = `PCS_IAC_LIMITED_BY_RIPPLE_RELAXED`<br>2 = `PCS_IAC_LIMITED_BY_OUTPUT_POWER`<br>3 = `PCS_IAC_LIMITED_BY_INPUT_POWER`<br>4 = `PCS_IAC_LIMITED_BY_PHASE_THERMAL_LIMIT`<br>5 = `PCS_IAC_LIMITED_BY_PHASE_MACHINE_MODEL` | validated |
| `PCS_chgPhCInputIrms` | page 2 | AC charger phase C's sensed RMS input current | 5\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 51.1 |  | validated |
| `PCS_chgPhCIntBusV` | page 2 | AC charger phase C's sensed intermediate bus voltage | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhCIntBusVTarget` | page 2 | AC charger phase C's intermediate bus voltage target | 23\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhCOutputI` | page 2 | AC charger phase C sensed output current | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | validated |
| `PCS_chgPhCInputCurrentLimitReason` | page 2 | Provides the reason behind the input AC charging current limit for phase C | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PCS_IAC_LIMITED_BY_NONE`<br>1 = `PCS_IAC_LIMITED_BY_RIPPLE_RELAXED`<br>2 = `PCS_IAC_LIMITED_BY_OUTPUT_POWER`<br>3 = `PCS_IAC_LIMITED_BY_INPUT_POWER`<br>4 = `PCS_IAC_LIMITED_BY_PHASE_THERMAL_LIMIT`<br>5 = `PCS_IAC_LIMITED_BY_PHASE_MACHINE_MODEL` | validated |
| `PCS_chgInputL1NVrms` | page 3 | AC charger's sensed AC RMS voltage of L1-N voltage source | 5\|12 | little-endian | unsigned | 0.2 | 0 | V | 0 to 819 |  | validated |
| `PCS_chgInputL2NVrms` | page 3 | AC charger's sensed AC RMS voltage of L2-N voltage source | 17\|12 | little-endian | unsigned | 0.2 | 0 | V | 0 to 819 |  | validated |
| `PCS_chgInputL3NVrms` | page 3 | AC charger's sensed AC RMS voltage of L3-N voltage source | 29\|12 | little-endian | unsigned | 0.2 | 0 | V | 0 to 819 |  | validated |
| `PCS_chgInputL1L2Vrms` | page 3 | AC charger's sensed input frequency of L2-N voltage source | 41\|12 | little-endian | unsigned | 0.2 | 0 | V | 0 to 819 |  | validated |
| `PCS_chgInputNGVrms` | page 3 | AC charger's sensed AC RMS voltage of N-G voltage source | 53\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgInputFrequencyL1N` | page 4 | AC charger's sensed input frequency of L1-N voltage source | 5\|12 | little-endian | unsigned | 0.01 | 40 | Hz | 40 to 80.95 | 0 = `FREQUENCY_UNKNOWN` | validated |
| `PCS_chgInputFrequencyL2N` | page 4 | AC charger's sensed input frequency of L2-N voltage source | 17\|12 | little-endian | unsigned | 0.01 | 40 | Hz | 40 to 80.95 | 0 = `FREQUENCY_UNKNOWN` | validated |
| `PCS_chgInputFrequencyL3N` | page 4 | AC charger's sensed input frequency of L3-N voltage source | 29\|12 | little-endian | unsigned | 0.01 | 40 | Hz | 40 to 80.95 | 0 = `FREQUENCY_UNKNOWN` | validated |
| `PCS_chgInternalPhaseConfig` | page 4 | Internal phase configuration of the AC charger (three phase vs. single phase); raw 0 = signal not available (SNA) | 41\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `PHASE_CONFIG_SNA`<br>1 = `PHASE_CONFIG_SINGLE_PHASE`<br>2 = `PHASE_CONFIG_THREE_PHASE`<br>3 = `PHASE_CONFIG_THREE_PHASE_DELTA`<br>4 = `PHASE_CONFIG_SINGLE_PHASE_IEC_GB`<br>5 = `PHASE_CONFIG_MFG_TEST_CONFIG_1`<br>6 = `PHASE_CONFIG_MFG_TEST_CONFIG_2`<br>7 = `PHASE_CONFIG_SINGLE_PHASE_BRIDGED_HARNESS`<br>8 = `PHASE_CONFIG_SINGLE_PHASE_EVSE_PARALLEL`<br>9 = `PHASE_CONFIG_TOTAL_NUM` | validated |
| `PCS_chgPhasesPriority` | page 4 | AC charger phase manager's priority logic for enabling phases in single phase PCS variant | 45\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `UNDEFINED_PHASES_PRIORITY`<br>6 = `PHASES_PRIORITY_CBA`<br>9 = `PHASES_PRIORITY_BCA`<br>18 = `PHASES_PRIORITY_CAB`<br>24 = `PHASES_PRIORITY_ACB`<br>33 = `PHASES_PRIORITY_BAC`<br>36 = `PHASES_PRIORITY_ABC` | validated |
| `PCS_chgOutputV` | page 4 | Sensed output voltage of AC charger | 51\|12 | little-endian | unsigned | 0.146484375 | 0 | V | 0 to 599.853515625 |  | validated |
| `PCS_chgPhAState` | page 5 | State of AC charger phase A | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PCS_PH_STATE_INIT`<br>1 = `PCS_PH_STATE_IDLE`<br>2 = `PCS_PH_STATE_PRECHARGE`<br>3 = `PCS_PH_STATE_ENABLE`<br>4 = `PCS_PH_STATE_FAULT`<br>5 = `PCS_PH_STATE_CLEAR_FAULTS`<br>6 = `PCS_PH_STATE_SHUTTING_DOWN` | validated |
| `PCS_chgPhBState` | page 5 | State of AC charger phase B | 9\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PCS_PH_STATE_INIT`<br>1 = `PCS_PH_STATE_IDLE`<br>2 = `PCS_PH_STATE_PRECHARGE`<br>3 = `PCS_PH_STATE_ENABLE`<br>4 = `PCS_PH_STATE_FAULT`<br>5 = `PCS_PH_STATE_CLEAR_FAULTS`<br>6 = `PCS_PH_STATE_SHUTTING_DOWN` | validated |
| `PCS_chgPhCState` | page 5 | State of AC charger phase C | 13\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PCS_PH_STATE_INIT`<br>1 = `PCS_PH_STATE_IDLE`<br>2 = `PCS_PH_STATE_PRECHARGE`<br>3 = `PCS_PH_STATE_ENABLE`<br>4 = `PCS_PH_STATE_FAULT`<br>5 = `PCS_PH_STATE_CLEAR_FAULTS`<br>6 = `PCS_PH_STATE_SHUTTING_DOWN` | validated |
| `PCS_chgPhALastShutdownReason` | page 5 | Last reason for shutting down AC charger phase A | 17\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `PCS_PH_SHUTDOWN_REASON_NONE`<br>1 = `PCS_PH_SHUTDOWN_SW_ENABLE`<br>2 = `PCS_PH_SHUTDOWN_HW_ENABLE`<br>3 = `PCS_PH_SHUTDOWN_SW_FAULT`<br>4 = `PCS_PH_SHUTDOWN_HW_FAULT`<br>5 = `PCS_PH_SHUTDOWN_PLL_NOT_LOCKED`<br>6 = `PCS_PH_SHUTDOWN_INPUT_UV`<br>7 = `PCS_PH_SHUTDOWN_INPUT_OV`<br>8 = `PCS_PH_SHUTDOWN_OUTPUT_UV`<br>9 = `PCS_PH_SHUTDOWN_OUTPUT_OV`<br>10 = `PCS_PH_SHUTDOWN_PRECHARGE_TIMEOUT`<br>11 = `PCS_PH_SHUTDOWN_INT_BUS_UV`<br>12 = `PCS_PH_SHUTDOWN_CONTROL_REGULATION_FAULT`<br>13 = `PCS_PH_SHUTDOWN_OVER_TEMPERATURE`<br>14 = `PCS_PH_SHUTDOWN_TEMP_IRRATIONAL`<br>15 = `PCS_PH_SHUTDOWN_SENSOR_IRRATIONAL`<br>16 = `PCS_PH_SHUTDOWN_FREQ_OUT_OF_RANGE`<br>17 = `PCS_PH_SHUTDOWN_LINE_TRANSIENT_FAULT` | validated |
| `PCS_chgPhBLastShutdownReason` | page 5 | Last reason for shutting down AC charger phase B | 22\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `PCS_PH_SHUTDOWN_REASON_NONE`<br>1 = `PCS_PH_SHUTDOWN_SW_ENABLE`<br>2 = `PCS_PH_SHUTDOWN_HW_ENABLE`<br>3 = `PCS_PH_SHUTDOWN_SW_FAULT`<br>4 = `PCS_PH_SHUTDOWN_HW_FAULT`<br>5 = `PCS_PH_SHUTDOWN_PLL_NOT_LOCKED`<br>6 = `PCS_PH_SHUTDOWN_INPUT_UV`<br>7 = `PCS_PH_SHUTDOWN_INPUT_OV`<br>8 = `PCS_PH_SHUTDOWN_OUTPUT_UV`<br>9 = `PCS_PH_SHUTDOWN_OUTPUT_OV`<br>10 = `PCS_PH_SHUTDOWN_PRECHARGE_TIMEOUT`<br>11 = `PCS_PH_SHUTDOWN_INT_BUS_UV`<br>12 = `PCS_PH_SHUTDOWN_CONTROL_REGULATION_FAULT`<br>13 = `PCS_PH_SHUTDOWN_OVER_TEMPERATURE`<br>14 = `PCS_PH_SHUTDOWN_TEMP_IRRATIONAL`<br>15 = `PCS_PH_SHUTDOWN_SENSOR_IRRATIONAL`<br>16 = `PCS_PH_SHUTDOWN_FREQ_OUT_OF_RANGE`<br>17 = `PCS_PH_SHUTDOWN_LINE_TRANSIENT_FAULT` | validated |
| `PCS_chgPhCLastShutdownReason` | page 5 | Last reason for shutting down AC charger phase C | 27\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `PCS_PH_SHUTDOWN_REASON_NONE`<br>1 = `PCS_PH_SHUTDOWN_SW_ENABLE`<br>2 = `PCS_PH_SHUTDOWN_HW_ENABLE`<br>3 = `PCS_PH_SHUTDOWN_SW_FAULT`<br>4 = `PCS_PH_SHUTDOWN_HW_FAULT`<br>5 = `PCS_PH_SHUTDOWN_PLL_NOT_LOCKED`<br>6 = `PCS_PH_SHUTDOWN_INPUT_UV`<br>7 = `PCS_PH_SHUTDOWN_INPUT_OV`<br>8 = `PCS_PH_SHUTDOWN_OUTPUT_UV`<br>9 = `PCS_PH_SHUTDOWN_OUTPUT_OV`<br>10 = `PCS_PH_SHUTDOWN_PRECHARGE_TIMEOUT`<br>11 = `PCS_PH_SHUTDOWN_INT_BUS_UV`<br>12 = `PCS_PH_SHUTDOWN_CONTROL_REGULATION_FAULT`<br>13 = `PCS_PH_SHUTDOWN_OVER_TEMPERATURE`<br>14 = `PCS_PH_SHUTDOWN_TEMP_IRRATIONAL`<br>15 = `PCS_PH_SHUTDOWN_SENSOR_IRRATIONAL`<br>16 = `PCS_PH_SHUTDOWN_FREQ_OUT_OF_RANGE`<br>17 = `PCS_PH_SHUTDOWN_LINE_TRANSIENT_FAULT` | validated |
| `PCS_chgPhARetryCount` | page 5 | AC charger phase A number of retries used during the current charge session | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `PCS_chgPhBRetryCount` | page 5 | AC charger phase B number of retries used during the current charge session | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `PCS_chgPhCRetryCount` | page 5 | AC charger phase C number of retries used during the current charge session | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `PCS_chgRetryCount` | page 5 | AC charger number of system level retries used during the current charge session | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `PCS_chgPhManCurrentToDist` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg ph man current to dist | 44\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 100 |  | validated |
| `PCS_chgL1NPllLocked` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg L1 n pll locked | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgL2NPllLocked` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg L2 n pll locked | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgL3NPllLocked` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg L3 n pll locked | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgL1L2PllLocked` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg L1 L2 pll locked | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgNgPllLocked` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg ng pll locked | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgPhManOptimalPhsToUse` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg ph man optimal phs to use | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `PCS_chg5VL1Enable` | page 5 | Power conversion system (on-board charger and DC-DC converter): chg5 VL1 enable | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_dcdcMaxLvOutputCurrent` | page 6 | Overall maxmum LV output current capability of DCDC | 8\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `PCS_dcdcCurrentLimit` | page 6 | Power conversion system (on-board charger and DC-DC converter): dcdc current limit | 20\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `PCS_dcdcLvOutputCurrentTempLimit` | page 6 | Maximum LV output current capability of DCDC based on thermals | 32\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `PCS_dcdcLvOutputCurrentFiltered` | page 6 | DCDC's filtered LV output current | 44\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `PCS_dcdcUnifiedCommand` | page 7 | Power conversion system (on-board charger and DC-DC converter): dcdc unified command | 5\|10 | little-endian | unsigned | 0.001 | 0 | 1 | 0 to 1 |  | validated |
| `PCS_dcdcCLAControllerOutput` | page 7 | Power conversion system (on-board charger and DC-DC converter): dcdc CLA controller output | 16\|10 | little-endian | unsigned | 0.001 | 0 | 1 | 0 to 1 |  | validated |
| `PCS_dcdcTankVoltage` | page 7 | Power conversion system (on-board charger and DC-DC converter): dcdc tank voltage; raw 1024 = signal not available (SNA) | 26\|11 | little-endian | signed | 1 | 0 | V | -1024 to 1023 | -1024 = `TANK_VOLTAGE_SNA` | validated |
| `PCS_dcdcTankVoltageTarget` | page 7 | Power conversion system (on-board charger and DC-DC converter): dcdc tank voltage target | 37\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `PCS_dcdcClaCurrentFreq` | page 7 | Power conversion system (on-board charger and DC-DC converter): dcdc cla current freq | 48\|12 | little-endian | unsigned | 0.09765625 | 0 | kHz | 0 to 399.9 |  | validated |
| `PCS_dcdcTCommMeasured` | page 8 | Power conversion system (on-board charger and DC-DC converter): dcdc t comm measured | 5\|16 | little-endian | signed | 0.001953125 | 0 | us | -64 to 63.998 |  | validated |
| `PCS_dcdcShortTimeUs` | page 8 | Power conversion system (on-board charger and DC-DC converter): dcdc short time us | 21\|16 | little-endian | unsigned | 0.00048828125 | 0 | us | 0 to 31.9995 |  | validated |
| `PCS_dcdcHalfPeriodUs` | page 8 | Power conversion system (on-board charger and DC-DC converter): dcdc half period us | 37\|16 | little-endian | unsigned | 0.00048828125 | 0 | us | 0 to 31.9995 |  | validated |
| `PCS_dcdcLvBusVoltTargetWithOffset` | page 8 | LV support Voltage target with Feed-forward offset | 53\|11 | little-endian | unsigned | 0.01 | 0 | V | 0 to 20 |  | validated |
| `PCS_cpu2BootState` | page 9 | Power conversion system (on-board charger and DC-DC converter): cpu2 boot state | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CPU2_STATE_BOOTROM`<br>1 = `CPU2_STATE_BOOTLOADER`<br>2 = `CPU2_STATE_APPLICATION`<br>3 = `CPU2_STATE_ERROR` | validated |
| `PCS_acChargeSelfTestState` | page 9 | Power conversion system (on-board charger and DC-DC converter): ac charge self test state | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PCS_SELF_TEST_IDLE`<br>1 = `PCS_SELF_TEST_STARTED` | validated |
| `PCS_1V5Min10s` | page 9 | Power conversion system (on-board charger and DC-DC converter): 1 V5 min10s | 8\|11 | little-endian | unsigned | 0.001 | 0 | V | 0 to 2.047 |  | validated |
| `PCS_1V5Max10s` | page 9 | Power conversion system (on-board charger and DC-DC converter): 1 V5 max10s | 19\|11 | little-endian | unsigned | 0.001 | 0 | V | 0 to 2.047 |  | validated |
| `PCS_1V2Min10s` | page 9 | Power conversion system (on-board charger and DC-DC converter): 1 V2 min10s | 32\|11 | little-endian | unsigned | 0.001 | 0 | V | 0 to 2.047 |  | validated |
| `PCS_1V2Max10s` | page 9 | Power conversion system (on-board charger and DC-DC converter): 1 V2 max10s | 43\|11 | little-endian | unsigned | 0.001 | 0 | V | 0 to 2.047 |  | validated |
| `PCS_5VNMax10s` | page 9 | Power conversion system (on-board charger and DC-DC converter): 5 VN max10s | 54\|10 | little-endian | unsigned | 0.01 | 0 | V | 0 to 10.23 |  | validated |
| `PCS_chgPhAIntBusVMin10s` | page 10 | AC charger phase A's minimum sensed intermediate bus voltage over the last ten seconds | 5\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhAIntBusVMax10s` | page 10 | AC charger phase A's maximum sensed intermediate bus voltage over the last ten seconds | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhAPchgVoltDeltaMax10s` | page 10 | AC charger phase A maximum sensed voltage delta between line and intermediate bus in the last 10 seconds during SCR precharge | 23\|8 | little-endian | unsigned | 0.5 | 0 | V | 0 to 127.5 |  | validated |
| `PCS_chgPhALifetimekWh` | page 10 | Lifetime total energy throughput of AC charger phase A | 31\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.15 |  | validated |
| `PCS_chgPhATransientRetryCount` | page 10 | AC charger phase A number of transient retries used during the current charge session | 55\|9 | little-endian | unsigned | 0.1 | 0 | - | 0 to 51.1 |  | validated |
| `PCS_chgPhBIntBusVMin10s` | page 11 | AC charger phase B's minimum sensed intermediate bus voltage over the last ten seconds | 5\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhBIntBusVMax10s` | page 11 | AC charger phase B's maximum sensed intermediate bus voltage over the last ten seconds | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhBPchgVoltDeltaMax10s` | page 11 | AC charger phase B maximum sensed voltage delta between line and intermediate bus in the last 10 seconds during SCR precharge | 23\|8 | little-endian | unsigned | 0.5 | 0 | V | 0 to 127.5 |  | validated |
| `PCS_chgPhBLifetimekWh` | page 11 | Lifetime total energy throughput of AC charger phase B | 31\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.15 |  | validated |
| `PCS_chgPhBTransientRetryCount` | page 11 | AC charger phase B number of transient retries used during the current charge session | 55\|9 | little-endian | unsigned | 0.1 | 0 | - | 0 to 51.1 |  | validated |
| `PCS_chgPhCIntBusVMin10s` | page 12 | AC charger phase C's minimum sensed intermediate bus voltage over the last ten seconds | 5\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhCIntBusVMax10s` | page 12 | AC charger phase C's maximum sensed intermediate bus voltage over the last ten seconds | 14\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | validated |
| `PCS_chgPhCPchgVoltDeltaMax10s` | page 12 | AC charger phase C maximum sensed voltage delta between line and intermediate bus in the last 10 seconds during SCR precharge | 23\|8 | little-endian | unsigned | 0.5 | 0 | V | 0 to 127.5 |  | validated |
| `PCS_chgPhCLifetimekWh` | page 12 | Lifetime total energy throughput of AC charger phase C | 31\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.15 |  | validated |
| `PCS_chgPhCTransientRetryCount` | page 12 | AC charger phase C number of transient retries used during the current charge session | 55\|9 | little-endian | unsigned | 0.1 | 0 | - | 0 to 51.1 |  | validated |
| `PCS_chgPhANoFlowBucket` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg ph a no flow bucket | 5\|9 | little-endian | unsigned | 0.01 | 0 | - | 0 to 5.11 |  | validated |
| `PCS_chgPhBNoFlowBucket` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg ph b no flow bucket | 14\|9 | little-endian | unsigned | 0.01 | 0 | - | 0 to 5.11 |  | validated |
| `PCS_chgPhCNoFlowBucket` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg ph c no flow bucket | 23\|9 | little-endian | unsigned | 0.01 | 0 | - | 0 to 5.11 |  | validated |
| `PCS_chgCurrentSensorOutOfBandUs` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg current sensor out of band us | 32\|10 | little-endian | unsigned | 0.01 | 0 | us | 0 to 10.23 |  | validated |
| `PCS_chgAcpwHeartbeatState` | page 20 | A signal to indicate if PCS detects the heartbeat signature from AC Power Wall | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PCS_ACPW_HEARTBEAT_STATE_UNKNOWN`<br>1 = `PCS_ACPW_HEARTBEAT_STATE_NOT_DETECTED`<br>2 = `PCS_ACPW_HEARTBEAT_STATE_DETECTED_OFFGRID`<br>3 = `PCS_ACPW_HEARTBEAT_STATE_DETECTED_ONGRID`<br>4 = `PCS_ACPW_HEARTBEAT_STATE_NUM` | validated |
| `PCS_chgKwhLostByFreqDroop` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg kwh lost by freq droop | 48\|8 | little-endian | unsigned | 0.1 | 0 | kWh | 0 to 25.5 |  | validated |
| `PCS_chgReqKwhLostByFreqDroop` | page 20 | Power conversion system (on-board charger and DC-DC converter): chg req kwh lost by freq droop | 56\|8 | little-endian | unsigned | 0.1 | 0 | kWh | 0 to 25.5 |  | validated |
| `PCS_dcdcLvSupportLifetimekWh` | page 22 | Lifetime energy throughput of DCDC LV support mode | 8\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.15 |  | validated |
| `PCS_chgPwmEnableLineErrorCount` | page 22 | Power conversion system (on-board charger and DC-DC converter): chg pwm enable line error count | 32\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | validated |
| `PCS_dcdcPwmEnableLineErrorCount` | page 22 | Number of deassertions detected for DCDC PWM enable line | 42\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | validated |
| `PCS_numAlertsSet` | page 22 | Power conversion system (on-board charger and DC-DC converter): num alerts set | 56\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |
| `PCS_dcdcPchgStartLvBusVolt` | page 24 | Sensed LV bus votlage when beginning DCDC precharge | 5\|10 | little-endian | unsigned | 0.0390625 | 0 | V | 0 to 39.9609375 |  | validated |
| `PCS_dcdcPchgStartHvBusVolt` | page 24 | Sensed HV bus votlage when beginning DCDC precharge | 16\|12 | little-endian | unsigned | 0.146484375 | 0 | V | 0 to 599.853515625 |  | validated |
| `PCS_processorDieIdLot` | page 26 | Power conversion system (on-board charger and DC-DC converter): processor die id lot | 8\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | validated |
| `PCS_processorDieIdWafer` | page 26 | Power conversion system (on-board charger and DC-DC converter): processor die id wafer | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PCS_processorDieIdX` | page 26 | Power conversion system (on-board charger and DC-DC converter): processor die id x | 40\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |
| `PCS_processorDieIdY` | page 26 | Power conversion system (on-board charger and DC-DC converter): processor die id y | 52\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |

## Multiplexing

`PCS_logMessageSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (5 signals), page 2 (5 signals), page 3 (5 signals), page 4 (6 signals), page 5 (18 signals), page 6 (4 signals), page 7 (5 signals), page 8 (4 signals), page 9 (7 signals), page 10 (5 signals), page 11 (5 signals), page 12 (5 signals), page 20 (7 signals), page 22 (4 signals), page 24 (2 signals), page 26 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
