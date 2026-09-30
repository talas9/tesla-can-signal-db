---
layout: default
title: "PCS2_logging (0x2E4) — PCS2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "PCS2 ECU message: logging. Tesla Model 3 CAN bus message PCS2_logging (0x2E4) of PCS2 ECU, firmware 2026.26.6.5, 31 signals (PCS2_logMessageSelect, PCS2_dcdcUsingInternalDefLvTarget, PCS2_dcdcAStateMachineState, PCS2_dcdcBStateMachineState and 27 more). Bit layout, scaling, units and value tables."
---

# PCS2_logging (0x2E4) — PCS2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN

PCS2 ECU message: logging; frame length from the layout, not yet observed on a vehicle bus. This page documents the 31 signals of PCS2_logging as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS2_logging` |
| CAN id | 0x2E4 (740) |
| ECU | [PCS2 ECU](../../pcs2.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS2 |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 31 |

## Signals of PCS2_logging

Tesla Model 3 CAN bus signals in `PCS2_logging`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PCS2_logMessageSelect` | selector | PCS2 ECU: log message select | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DCDC_A_HV_VOLTAGE_SENSE`<br>1 = `DCDC_STATE_MACHINES`<br>2 = `DCDC_A_CURRENT_COMMAND`<br>3 = `DCDC_LV_BUS_SENSE`<br>4 = `SYSTEM_STATUS_1`<br>5 = `DCDC_A_VOLTAGE_SENSE_MIN_MAX`<br>6 = `DCDC_A_TANK_PARAMS`<br>7 = `DCDC_A_HALF_BUS_VOLTAGE_SENSE_MIN_MAX`<br>8 = `DCDC_A_TANK_MEASUREMENTS`<br>9 = `DCDC_A_VOLTAGE_TARGET`<br>10 = `DCDC_A_LIFETIME_ENERGY_STATS`<br>11 = `DCDC_A_THERMAL_MODELING_1`<br>12 = `MFG_FUNCTIONAL_TEST_INFO`<br>13 = `MFG_FUNCTIONAL_TEST_CALIBRATE`<br>14 = `MFG_FUNCTIONAL_TEST_CALIBRATE_ITERATIVE`<br>15 = `MFG_FUNCTIONAL_TEST_IOX`<br>16 = `RAIL_SENSE_18V0`<br>17 = `DCDC_A_STAGE_STATUS`<br>18 = `IPC_CPU0_LOCK_MONITOR`<br>19 = `DCDC_A_ARBITRATION_STATUS`<br>20 = `DCDC_A_ZCD_STATUS`<br>21 = `DCDC_A_SWITCHING_FREQ`<br>22 = `HEALTH_CHECK_STATUS`<br>23 = `CPU0_UTILIZATION`<br>24 = `RAIL_SENSE_10V0`<br>25 = `RAIL_SENSE_4V5`<br>26 = `RAIL_SENSE_1V6`<br>27 = `RAIL_SENSE_48V0`<br>28 = `CURRENT_SENSE_48V0_18V0`<br>29 = `RAIL_SENSE_13V5`<br>30 = `RAIL_SENSE_2V5`<br>31 = `FC_VOLTAGE_SENSE`<br>32 = `BUCK_BOOST_CONTROL_MONITOR`<br>33 = `RAIL_SENSE_LV_BIAS`<br>34 = `EFUSE_MONITOR`<br>35 = `PCS2_PRU_MONITOR_LOG`<br>36 = `PCS2_PRU_MONITOR_PCS2LITE_LOG`<br>37 = `PCS2_PRU_MONITOR_PCSCI_LOG`<br>38 = `BUCK_BOOST_CURRENT_MONITOR`<br>39 = `PCS2_WAKE_CONFIG`<br>40 = `DCDC_A_LV_CURRENT_SENSE`<br>41 = `DCDC_A_THERMAL_MODELING_2`<br>42 = `PCS2_LOGGING_SELECT_NUM_CPU0`<br>64 = `DCDC_B_HV_VOLTAGE_SENSE`<br>65 = `DCDC_B_CURRENT_COMMAND`<br>66 = `DCDC_B_HV_FULL_MIN_MAX`<br>67 = `DCDC_B_TANK_PARAMS`<br>68 = `DCDC_B_HALF_BUS_VOLTAGE_SENSE_MIN_MAX`<br>69 = `DCDC_B_TANK_MEASUREMENTS`<br>70 = `DCDC_B_VOLTAGE_TARGET`<br>71 = `DCDC_B_LIFETIME_ENERGY_STATS`<br>72 = `DCDC_B_THERMAL_MODELING_1`<br>73 = `DCDC_B_HV_BUS_IMPEDANCE_ESTIMATION`<br>74 = `DCDC_B_STAGE_STATUS`<br>75 = `IPC_CPU1_LOCK_MONITOR`<br>76 = `DCDC_B_ARBITRATION_STATUS`<br>77 = `DCDC_B_ZCD_STATUS`<br>78 = `DCDC_B_SWITCHING_FREQ`<br>79 = `DCDC_TEMP_MIN`<br>80 = `DCDC_TEMP_MAX`<br>81 = `PCSCI_DCDC_TEMP`<br>82 = `ADC_TEMP_SENSE_MAX`<br>83 = `DCDC_B_HV_BUS_CURRENT_SENSE`<br>84 = `PCS2LITE_TEMP_1`<br>85 = `PCS2LITE_TEMP_2`<br>86 = `CYCLO_A_TEMP`<br>87 = `CYCLO_B_TEMP`<br>88 = `DCDC_TEMP`<br>89 = `ADC_TEMP_SENSE`<br>90 = `CYCLO_A_TEMP_MIN`<br>91 = `CYCLO_A_TEMP_MAX`<br>92 = `CYCLO_B_TEMP_MIN`<br>93 = `CYCLO_B_TEMP_MAX`<br>94 = `ADC_TEMP_SENSE_MIN`<br>95 = `CPU1_UTILIZATION`<br>96 = `DCDC_B_THERMAL_MODELING_2`<br>97 = `DCDC_HW_ZCD`<br>98 = `DCDC_TEMP_AUX`<br>99 = `DCDC_B_LV_CURRENT_SENSE`<br>100 = `PCS2_LOGGING_SELECT_NUM_CPU1`<br>128 = `AC_LINE_TO_NEUTRAL_VOLT_SENSE`<br>129 = `AC_LINE_TO_LINE_VOLT_CALCULATED`<br>130 = `AC_LINE_CURRENT_SENSE`<br>131 = `AC_GRID_STATUS`<br>132 = `AC_LINE_TO_NEUTRAL_FREQUENCY`<br>133 = `AC_LINE_TO_LINE_FREQUENCY`<br>134 = `DCAC_HV_BUS_SENSE`<br>135 = `DCAC_STATE_MACHINES`<br>136 = `CYCLO_AC_LINE_TO_NEUTRAL_PEAK_V`<br>137 = `CYCLO_A_TANK_MEASUREMENTS`<br>138 = `AC_LINE_TO_CHASSIS_VOLT_CALCULATED`<br>139 = `DCAC_CHARGING_CURRENT_LIMITS`<br>140 = `AC_LINE_PHASE_STATUS`<br>141 = `AC_LINE_PHASE_ANGLE_DIFF`<br>142 = `CYCLO_A_TANK_PARAMS`<br>143 = `CYCLO_A_SURGE_DERATING_FACTOR`<br>144 = `CYCLO_A_MODEL_JUNCTION_TEMP`<br>145 = `CYCLO_A_MODEL_JUNCTION_TEMP_MAX`<br>146 = `CYCLO_A_INFO`<br>147 = `DCAC_CURRENT_LIMITS`<br>148 = `DCAC_CURRENT_LIMITS_2`<br>149 = `DCAC_CURRENT_LIMITS_3`<br>150 = `I2T_GENERATED_HEAT_HW_LIMIT`<br>151 = `DCAC_LIFETIME_KVAH`<br>152 = `OUTLET_GRID_FORM_LIFETIME_KVAH`<br>153 = `CABIN_AND_BED_GRID_FORM_LIFETIME_KVAH`<br>154 = `IPC_CPU2_LOCK_MONITOR`<br>155 = `CYCLO_A_ZCD_STATUS`<br>156 = `CYCLO_A_SWITCHING_FREQ`<br>157 = `AC_RELAY_INFO`<br>158 = `CPU2_UTILIZATION`<br>159 = `I2T_GENERATED_HEAT_CP_LIMIT`<br>160 = `CYCLO_AC_LINE_TO_LINE_PEAK_V`<br>161 = `CYCLO_AC_PRE_RELAY_PEAK_V`<br>162 = `EPTO_INFO`<br>163 = `PCS2_LOGGING_SELECT_NUM_CPU2`<br>192 = `CYCLO_LEG_PEAK_CURRENT`<br>193 = `CYCLO_B_TANK_MEASUREMENTS`<br>194 = `CYCLO_B_TANK_PARAMS`<br>195 = `CYCLO_B_SURGE_DERATING_FACTOR`<br>196 = `CYCLO_B_MODEL_JUNCTION_TEMP`<br>197 = `CYCLO_B_MODEL_JUNCTION_TEMP_MAX`<br>198 = `CYCLO_B_INFO`<br>199 = `DCAC_SWITCHING_FREQUENCY`<br>200 = `IPC_CPU3_LOCK_MONITOR`<br>201 = `MICROGRID_HEARTBEAT`<br>202 = `CYCLO_B_ZCD_STATUS`<br>203 = `CYCLO_B_SWITCHING_FREQ`<br>204 = `AC_LINE_DC_OFFSET_VOLT_SENSE`<br>205 = `AC_LINE_DC_OFFSET_PRE_RELAY_VOLT_SENSE`<br>206 = `CPU3_UTILIZATION`<br>207 = `PCS2_LOGGING_SELECT_NUM_CPU3`<br>208 = `PCS2_LOG_NUM_MSGS` | plausible |
| `PCS2_dcdcUsingInternalDefLvTarget` | page 1 | PCS2 ECU: dcdc using internal def lv target | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS2_dcdcAStateMachineState` | page 1 | DCDC A stage state machine state | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DCDC_STAGE_STATE_POWER_UP_INIT`<br>1 = `DCDC_STAGE_STATE_STANDBY`<br>2 = `DCDC_STAGE_STATE_PRECONDITION`<br>3 = `DCDC_STAGE_STATE_ACTIVE`<br>4 = `DCDC_STAGE_STATE_FAULTED`<br>5 = `DCDC_STAGE_STATE_NUM_STATES` | validated |
| `PCS2_dcdcBStateMachineState` | page 1 | DCDC B stage state machine state | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DCDC_STAGE_STATE_POWER_UP_INIT`<br>1 = `DCDC_STAGE_STATE_STANDBY`<br>2 = `DCDC_STAGE_STATE_PRECONDITION`<br>3 = `DCDC_STAGE_STATE_ACTIVE`<br>4 = `DCDC_STAGE_STATE_FAULTED`<br>5 = `DCDC_STAGE_STATE_NUM_STATES` | validated |
| `PCS2_dcdcAStageModeRequest` | page 1 | DCDC A stage state machine mode request | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DCDC_STAGE_MODE_DISABLE`<br>1 = `DCDC_STAGE_MODE_LV_REGULATION`<br>2 = `DCDC_STAGE_MODE_HV_PRECHARGE`<br>3 = `DCDC_STAGE_MODE_HV_DISCHARGE` | validated |
| `PCS2_dcdcBStageModeRequest` | page 1 | DCDC B stage state machine mode request | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DCDC_STAGE_MODE_DISABLE`<br>1 = `DCDC_STAGE_MODE_LV_REGULATION`<br>2 = `DCDC_STAGE_MODE_HV_PRECHARGE`<br>3 = `DCDC_STAGE_MODE_HV_DISCHARGE` | validated |
| `PCS2_dcdcAHvCurrentCommand` | page 2 | DCDC A controller commanded HV current | 8\|13 | little-endian | signed | 0.01 | 0 | A | -30 to 30 |  | validated |
| `PCS2_dcdcALvCurrentCommand` | page 2 | Reports the Direct Current to Direct Current (DCDC) A commanded Low Voltage (LV) current. | 24\|13 | little-endian | signed | 0.1 | 0 | A | -409 to 409 |  | validated |
| `PCS2_dcdcAPowerLimit` | page 2 | DCDC A power limit | 37\|12 | little-endian | unsigned | 1 | 0 | W | 0 to 4095 |  | validated |
| `PCS2_dcdcALvCurrentEstimated` | page 2 | DCDC A estimated LV current | 49\|13 | little-endian | signed | 0.1 | 0 | A | -400 to 400 |  | validated |
| `PCS2_dcdcLvBusVoltageFiltered` | page 3 | DCDC system filtered LV bus voltage | 8\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 81.9 |  | validated |
| `PCS2_dcdcALifetimekWh` | page 10 | Lifetime energy throughput of DCDC-A power conversion; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_dcdcBHvCurrentCommand` | page 65 | DCDC B controller commanded HV current | 8\|13 | little-endian | signed | 0.01 | 0 | A | -30 to 30 |  | validated |
| `PCS2_dcdcBLvCurrentCommand` | page 65 | Reports the Direct Current to Direct Current (DCDC) B commanded Low Voltage (LV) current. | 24\|13 | little-endian | signed | 0.1 | 0 | A | -409 to 409 |  | validated |
| `PCS2_dcdcBPowerLimit` | page 65 | DCDC B power limit | 37\|12 | little-endian | unsigned | 1 | 0 | W | 0 to 4095 |  | validated |
| `PCS2_dcdcBLvCurrentEstimated` | page 65 | DCDC B estimated LV current | 49\|13 | little-endian | signed | 0.1 | 0 | A | -400 to 400 |  | validated |
| `PCS2_dcdcBLifetimekWh` | page 71 | Lifetime energy throughput of DCDC-B power conversion; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_dcdcA_lv2Temp` | page 88 | Measures the temperature of the Printed Circuit Board (PCB) when it is near the winding DCDC converter (DCDCA) low voltage 2 planar transformer. The planar transformer is located at the drain of Q8 transistor or at the source of Q6 transistor near the S_LVB_1T electrical connection; raw 1025 = signal not available (SNA) | 8\|11 | little-endian | signed | 0.15 | 70.05 | C | -60 to 200 | -1023 = `SNA` | validated |
| `PCS2_dcdcA_lv2TempIrrational` | page 88 | PCS2 ECU: dcdc a lv2 temp irrational | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS2_dcdcB_lv2Temp` | page 88 | Sensing temperature of the PCB in the vicinity of dcdc1_Lv2 planer transformer winding at the drain of Q107/source of Q106, Covering net S_LVB_1T; raw 1025 = signal not available (SNA) | 20\|11 | little-endian | signed | 0.15 | 70.05 | C | -60 to 200 | -1023 = `SNA` | validated |
| `PCS2_dcdcB_lv2TempIrrational` | page 88 | PCS2 ECU: dcdc b lv2 temp irrational | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS2_dcdcA_hvTemp` | page 88 | Sensing temperature of the PCB in the vicinity of dcdc2_HV planer transformer winding at the drain of Q3781/source of Q3681, covering net DCDC2_BATTTANK+; raw 1025 = signal not available (SNA) | 32\|11 | little-endian | signed | 0.15 | 70.05 | C | -60 to 200 | -1023 = `SNA` | validated |
| `PCS2_dcdcA_hvTempIrrational` | page 88 | PCS2 ECU: dcdc a hv temp irrational | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS2_dcdcB_hvTemp` | page 88 | Sensing temperature of the PCB in the vicinity of dcdc1_HV planer transformer winding at the drain of Q3441/source of Q3341, Covering net DCDC1_HVTANK+; raw 1025 = signal not available (SNA) | 44\|11 | little-endian | signed | 0.15 | 70.05 | C | -60 to 200 | -1023 = `SNA` | validated |
| `PCS2_dcdcB_hvTempIrrational` | page 88 | PCS2 ECU: dcdc b hv temp irrational | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS2_acChargeLifetimekVAh` | page 151 | Lifetime energy throughput of AC Charging; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_v2xGridFormLifetimekVAh` | page 151 | Lifetime energy throughput of V2X grid forming; raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_cabinOnlyL2L3LifetimekVAh` | page 152 | Lifetime energy throughput of cabin only outlet grid forming; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_totalOutletLifetimekVAh` | page 152 | Lifetime energy throughput the total outlet grid forming (excluding Charge Port); raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_cabinAndBedL1L2LifetimekVAh` | page 153 | Lifetime energy throughput between L1L2 outlet grid forming when cabin and bed outlets are both enabled; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |
| `PCS2_cabinAndBedL2L3LifetimekVAh` | page 153 | Lifetime energy throughput of L2L3 outlet grid forming when both cabin and bed outlets are enabled; raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.01 | 0 | kVAh | 0 to 167772.14 | 16777215 = `SNA` | validated |

## Multiplexing

`PCS2_logMessageSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals), page 2 (4 signals), page 3 (1 signals), page 10 (1 signals), page 65 (4 signals), page 71 (1 signals), page 88 (8 signals), page 151 (2 signals), page 152 (2 signals), page 153 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All PCS2 ECU messages (PCS2)](../../pcs2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
