---
layout: default
title: "BMS_alertMatrix (0x320) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH"
description: "High-voltage battery management system message: alert matrix. Ethernet-side message BMS_alertMatrix of High-voltage battery management system for Tesla Model 3 firmware 2025.20.8, 162 signals (BMS_matrixIndex, BMS_a001_Pack_Config_Mismatch, BMS_a002_Pack_Performance_Config_Mismatch, BMS_a003_SW_Pack_Birth_Date_Missing and 158 more). Bit layout, scaling, units and value tables."
---

# BMS_alertMatrix (0x320) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH

High-voltage battery management system message: alert matrix. This page documents the 162 signals of BMS_alertMatrix as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_alertMatrix` |
| Ethernet-side id | 0x320 (800) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 162 |

## Signals of BMS_alertMatrix

Tesla Model 3 CAN bus signals in `BMS_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_matrixIndex` | selector | High-voltage battery management system: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>1 = `AlertMatrix1`<br>2 = `AlertMatrix2`<br>3 = `AlertMatrix3` | plausible |
| `BMS_a001_Pack_Config_Mismatch` | page 0 | High-voltage battery management system: a001 pack config mismatch | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a002_Pack_Performance_Config_Mismatch` | page 0 | High-voltage battery management system: a002 pack performance config mismatch | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a003_SW_Pack_Birth_Date_Missing` | page 0 | High-voltage battery management system: a003 SW pack birth date missing | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a004_Cal_Vs_Serial_Birth_Date_Mismatch` | page 0 | High-voltage battery management system: a004 cal vs serial birth date mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a007_SW_Slowed_Chg_Batt_Cold` | page 0 | High-voltage battery management system: a007 SW slowed chg batt cold | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a016_Pack_Module_Id_Mismatch` | page 0 | High-voltage battery management system: a016 pack module id mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a017_SW_Brick_OV` | page 0 | High-voltage battery management system: a017 SW brick OV | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a018_SW_Brick_UV` | page 0 | High-voltage battery management system: a018 SW brick UV | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a019_SW_Module_OT` | page 0 | High-voltage battery management system: a019 SW module OT | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a020_SW_Brick_Instability` | page 0 | High-voltage battery management system: a020 SW brick instability | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a021_SW_Dr_Limits_Regulation` | page 0 | High-voltage battery management system: a021 SW dr limits regulation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a022_SW_Over_Current` | page 0 | High-voltage battery management system: a022 SW over current | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a023_SW_Stack_OV` | page 0 | High-voltage battery management system: a023 SW stack OV | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a024_SW_Islanded_Brick` | page 0 | High-voltage battery management system: a024 SW islanded brick | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a025_SW_PwrBalance_Anomaly` | page 0 | High-voltage battery management system: a025 SW pwr balance anomaly | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a026_SW_HFCurrent_Anomaly` | page 0 | High-voltage battery management system: a026 SW HF current anomaly | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a027_SW_Repeated_Isolation_Failure_In_Drive` | page 0 | High-voltage battery management system: a027 SW repeated isolation failure in drive | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a028_ShuntAsicCurrentOffsetDeviation` | page 0 | High-voltage battery management system: a028 shunt asic current offset deviation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a029_dSoc_Limiting` | page 0 | High-voltage battery management system: a029 d soc limiting | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a030_Impedance_Deviation` | page 0 | High-voltage battery management system: a030 impedance deviation | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a031_AlertsSetDuringSleep` | page 0 | High-voltage battery management system: a031 alerts set during sleep | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a032_VoltageLoss` | page 0 | High-voltage battery management system: a032 voltage loss | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a033_VoltageDeviation` | page 0 | High-voltage battery management system: a033 voltage deviation | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a034_SW_Passive_Isolation` | page 0 | High-voltage battery management system: a034 SW passive isolation | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a035_SW_Isolation` | page 0 | High-voltage battery management system: a035 SW isolation | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a036_SW_HvpHvilFault` | page 0 | High-voltage battery management system: a036 SW hvp hvil fault | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a037_SW_Flood_Port_Open` | page 0 | High-voltage battery management system: a037 SW flood port open | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a039_SW_DC_Link_Over_Voltage` | page 0 | High-voltage battery management system: a039 SW DC link over voltage | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a040_SW_Watch_Dog_HW_Triggered` | page 0 | High-voltage battery management system: a040 SW watch dog HW triggered | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a041_SW_Destructive_Reset_Source` | page 0 | High-voltage battery management system: a041 SW destructive reset source | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a042_SW_MPU_Error` | page 0 | High-voltage battery management system: a042 SW MPU error | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a043_SW_Watch_Dog_Reset` | page 0 | High-voltage battery management system: a043 SW watch dog reset | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a044_SW_Assertion` | page 0 | High-voltage battery management system: a044 SW assertion | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a045_SW_Exception` | page 0 | High-voltage battery management system: a045 SW exception | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a046_SW_Task_Stack_Usage` | page 0 | High-voltage battery management system: a046 SW task stack usage | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a047_SW_Task_Stack_Overflow` | page 0 | High-voltage battery management system: a047 SW task stack overflow | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a048_SW_Watch_Dog_Warning` | page 0 | High-voltage battery management system: a048 SW watch dog warning | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a049_SW_Thermal_Event` | page 0 | High-voltage battery management system: a049 SW thermal event | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a050_SW_Brick_Voltage_MIA` | page 0 | High-voltage battery management system: a050 SW brick voltage MIA | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a051_SW_HVC_Vref_Bad` | page 0 | High-voltage battery management system: a051 SW HVC vref bad | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a052_SW_PCS_MIA` | page 0 | High-voltage battery management system: a052 SW PCS MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a054_SW_Ver_Supply_Fault` | page 0 | High-voltage battery management system: a054 SW ver supply fault | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a055_SW_HvChain_Model_Fault` | page 0 | High-voltage battery management system: a055 SW hv chain model fault | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a056_SW_Standby_Supply_Fault` | page 0 | High-voltage battery management system: a056 SW standby supply fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a057_SW_Bandolier_Model_Warning` | page 0 | High-voltage battery management system: a057 SW bandolier model warning | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a058_SW_Bandolier_Model_Reset` | page 0 | High-voltage battery management system: a058 SW bandolier model reset | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a059_SW_Pack_Voltage_Sensing` | page 0 | High-voltage battery management system: a059 SW pack voltage sensing | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a060_SW_Leakage_Test_Failure` | page 0 | High-voltage battery management system: a060 SW leakage test failure | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a061_SW_BrickV_Change` | page 1 | High-voltage battery management system: a061 SW brick v change | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a062_SW_BrickV_Imbalance` | page 1 | High-voltage battery management system: a062 SW brick v imbalance | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a063_SW_ChargePort_Fault` | page 1 | High-voltage battery management system: a063 SW charge port fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a064_SW_SOC_Imbalance` | page 1 | High-voltage battery management system: a064 SW SOC imbalance | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a065_SW_CAC_Imbalance` | page 1 | High-voltage battery management system: a065 SW CAC imbalance | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a066_SOC_Imbalance_Warning` | page 1 | High-voltage battery management system: a066 SOC imbalance warning | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a067_CAC_Imbalance_Limiting` | page 1 | High-voltage battery management system: a067 CAC imbalance limiting | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a068_CAC_Imbalance_Limp` | page 1 | High-voltage battery management system: a068 CAC imbalance limp | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a069_SW_Low_Power` | page 1 | High-voltage battery management system: a069 SW low power | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a070_BrickV_Imbalance_Limiting` | page 1 | High-voltage battery management system: a070 brick v imbalance limiting | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a071_SW_SM_TransCon_Not_Met` | page 1 | High-voltage battery management system: a071 SW SM trans con not met | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a072_Module_Brick_Split` | page 1 | High-voltage battery management system: a072 module brick split | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a073_Unexpected_Loss_Of_Lv` | page 1 | High-voltage battery management system: a073 unexpected loss of lv | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a074_Max_Charge_Level_Reduced` | page 1 | High-voltage battery management system: a074 max charge level reduced | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a075_SW_Chg_Disable_Failure` | page 1 | High-voltage battery management system: a075 SW chg disable failure | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a076_SW_Dch_While_Charging` | page 1 | High-voltage battery management system: a076 SW dch while charging | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a077_SW_Charger_Regulation` | page 1 | High-voltage battery management system: a077 SW charger regulation | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a078_Rapid_Dch_While_Charging` | page 1 | High-voltage battery management system: a078 rapid dch while charging | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a079_Max_Charge_Level_Exceeded` | page 1 | High-voltage battery management system: a079 max charge level exceeded | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a080_SW_Pack_Ctr_Impedance` | page 1 | High-voltage battery management system: a080 SW pack ctr impedance | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a081_SW_Ctr_Close_Blocked` | page 1 | High-voltage battery management system: a081 SW ctr close blocked | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a082_SW_Ctr_Force_Open` | page 1 | High-voltage battery management system: a082 SW ctr force open | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a083_SW_Ctr_Close_Failure` | page 1 | High-voltage battery management system: a083 SW ctr close failure | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a084_SW_Sleep_Wake_Aborted` | page 1 | High-voltage battery management system: a084 SW sleep wake aborted | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_a085_SW_Pack_Contactor_Mismatch` | page 1 | High-voltage battery management system: a085 SW pack contactor mismatch | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a086_SW_FC_Contactor_Mismatch` | page 1 | High-voltage battery management system: a086 SW FC contactor mismatch | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a087_SW_Feim_Test_Blocked` | page 1 | High-voltage battery management system: a087 SW feim test blocked | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a088_SW_VcFront_MIA_InDrive` | page 1 | High-voltage battery management system: a088 SW vc front MIA in drive | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a089_SW_VcFront_MIA` | page 1 | High-voltage battery management system: a089 SW vc front MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a090_SW_Gateway_MIA` | page 1 | High-voltage battery management system: a090 SW gateway MIA | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a091_SW_ChargePort_MIA` | page 1 | High-voltage battery management system: a091 SW charge port MIA | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a092_SW_ChargePort_Mia_On_Hvs` | page 1 | High-voltage battery management system: a092 SW charge port mia on hvs | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a094_SW_Drive_Inverter_MIA` | page 1 | High-voltage battery management system: a094 SW drive inverter MIA | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a095_SW_UI_MIA` | page 1 | High-voltage battery management system: a095 SW UI MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a097_SW_BMB_Over_CAN_Communication` | page 1 | High-voltage battery management system: a097 SW BMB over CAN communication | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a098_SW_BMB_Data_Integrity_Loss` | page 1 | High-voltage battery management system: a098 SW BMB data integrity loss | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a099_SW_BMB_Communication` | page 1 | High-voltage battery management system: a099 SW BMB communication | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a100_ThermalEventSuspected` | page 1 | High-voltage battery management system: a100 thermal event suspected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a105_SW_One_Module_Tsense` | page 1 | High-voltage battery management system: a105 SW one module tsense | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a106_SW_All_Module_Tsense` | page 1 | High-voltage battery management system: a106 SW all module tsense | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a107_SW_Stack_Voltage_MIA` | page 1 | High-voltage battery management system: a107 SW stack voltage MIA | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a108_SW_BMB_Device_OT` | page 1 | High-voltage battery management system: a108 SW BMB device OT | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a109_HW_BMB_Mute_Status_Mismatch` | page 1 | High-voltage battery management system: a109 HW BMB mute status mismatch | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a110_LifeModel_AvgOffset_Change` | page 1 | High-voltage battery management system: a110 life model avg offset change | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a111_LifeModel_Spread_Change` | page 1 | High-voltage battery management system: a111 life model spread change | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a112_LifeModel_Discontinuity` | page 1 | High-voltage battery management system: a112 life model discontinuity | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a115_Energy_Rubberbanding_Reset` | page 1 | High-voltage battery management system: a115 energy rubberbanding reset | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a117_SW_Delta_SOC_Weak_Short` | page 1 | High-voltage battery management system: a117 SW delta SOC weak short | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a119_Fast_Open_Vsh_Detected` | page 1 | High-voltage battery management system: a119 fast open vsh detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a121_SW_NVRAM_Config_Error` | page 2 | High-voltage battery management system: a121 SW NVRAM config error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a122_SW_BMS_Therm_Irrational` | page 2 | High-voltage battery management system: a122 SW BMS therm irrational | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a123_SW_Internal_Isolation` | page 2 | High-voltage battery management system: a123 SW internal isolation | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a124_Battery_Coolant_Flood` | page 2 | High-voltage battery management system: a124 battery coolant flood | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a126_SW_Thermistor_Failure` | page 2 | High-voltage battery management system: a126 SW thermistor failure | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a127_SW_shunt_SNA` | page 2 | High-voltage battery management system: a127 SW shunt SNA | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a128_SW_shunt_MIA` | page 2 | High-voltage battery management system: a128 SW shunt MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a129_SW_VSH_Failure` | page 2 | High-voltage battery management system: a129 SW VSH failure | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a130_IO_CAN_Error` | page 2 | High-voltage battery management system: a130 IO CAN error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a131_Bleed_FET_Failure` | page 2 | High-voltage battery management system: a131 bleed FET failure | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a132_HW_BMB_OTP_Uncorrctbl` | page 2 | High-voltage battery management system: a132 HW BMB OTP uncorrctbl | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a133_IO_CAN_Bus_Off` | page 2 | High-voltage battery management system: a133 IO CAN bus off | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a134_SW_Delayed_Ctr_Off` | page 2 | High-voltage battery management system: a134 SW delayed ctr off | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a135_HW_BMB_Diagnostics_Failure` | page 2 | High-voltage battery management system: a135 HW BMB diagnostics failure | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a136_SW_Module_OT_Warning` | page 2 | High-voltage battery management system: a136 SW module OT warning | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a137_SW_Brick_UV_Warning` | page 2 | High-voltage battery management system: a137 SW brick UV warning | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a138_SW_Brick_OV_Warning` | page 2 | High-voltage battery management system: a138 SW brick OV warning | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a139_SW_DC_Link_V_Irrational` | page 2 | High-voltage battery management system: a139 SW DC link v irrational | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a140_HW_BMB_Status_Fault` | page 2 | High-voltage battery management system: a140 HW BMB status fault | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a141_SW_BMB_Status_Warning` | page 2 | High-voltage battery management system: a141 SW BMB status warning | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a142_SW_Isolation_Degradation` | page 2 | High-voltage battery management system: a142 SW isolation degradation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a143_SW_CAC_Change` | page 2 | High-voltage battery management system: a143 SW CAC change | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a144_Hvp_Config_Mismatch` | page 2 | High-voltage battery management system: a144 hvp config mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a145_SW_SOC_Change` | page 2 | High-voltage battery management system: a145 SW SOC change | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a146_SW_Brick_Overdischarged` | page 2 | High-voltage battery management system: a146 SW brick overdischarged | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a147_SW_SOC_High_Ah_Error` | page 2 | High-voltage battery management system: a147 SW SOC high ah error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a148_SW_Unsupported_BMB_ASIC_Type` | page 2 | High-voltage battery management system: a148 SW unsupported BMB ASIC type | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a149_SW_Missing_Config_Block` | page 2 | High-voltage battery management system: a149 SW missing config block | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a150_SW_Missing_Part_Number` | page 2 | High-voltage battery management system: a150 SW missing part number | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a151_SW_external_isolation` | page 2 | High-voltage battery management system: a151 SW external isolation | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a152_Isolation_In_Dc_Charge` | page 2 | High-voltage battery management system: a152 isolation in dc charge | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a154_SW_Brick_OV_Warning_Stop_Charge` | page 2 | High-voltage battery management system: a154 SW brick OV warning stop charge | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a155_SW_Weak_short_impedence` | page 2 | High-voltage battery management system: a155 SW weak short impedence | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a156_SW_BMB_Vref_bad` | page 2 | High-voltage battery management system: a156 SW BMB vref bad | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a157_SW_Hist_Update_Missed` | page 2 | High-voltage battery management system: a157 SW hist update missed | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a158_SW_HVP_HVI_Comms` | page 2 | High-voltage battery management system: a158 SW HVP HVI comms | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a159_SW_HVP_ECU_Error` | page 2 | High-voltage battery management system: a159 SW HVP ECU error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a160_SW_FC_Ctr_Clean_Failed` | page 2 | High-voltage battery management system: a160 SW FC ctr clean failed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a161_SW_BMB_Vref_warning` | page 2 | High-voltage battery management system: a161 SW BMB vref warning | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a162_SW_No_Power_For_Support` | page 2 | High-voltage battery management system: a162 SW no power for support | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a164_SW_Uncontrolled_Regen` | page 2 | High-voltage battery management system: a164 SW uncontrolled regen | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a165_SW_Pack_Partial_Weld` | page 2 | High-voltage battery management system: a165 SW pack partial weld | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a166_SW_Pack_Full_Weld` | page 2 | High-voltage battery management system: a166 SW pack full weld | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a167_SW_FC_Partial_Weld` | page 2 | High-voltage battery management system: a167 SW FC partial weld | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a168_SW_FC_Full_Weld` | page 2 | High-voltage battery management system: a168 SW FC full weld | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a169_SW_FC_Pack_Weld` | page 2 | High-voltage battery management system: a169 SW FC pack weld | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a170_SW_Limp_Mode` | page 2 | High-voltage battery management system: a170 SW limp mode | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a171_SW_Stack_Voltage_Sense` | page 2 | High-voltage battery management system: a171 SW stack voltage sense | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a172_SW_Isolation_Failure_In_Drive_Warning` | page 2 | High-voltage battery management system: a172 SW isolation failure in drive warning | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a174_SW_Charge_Failure` | page 2 | High-voltage battery management system: a174 SW charge failure | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a175_Charge_Failure_External` | page 2 | High-voltage battery management system: a175 charge failure external | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a176_SW_GracefulPowerOff` | page 2 | High-voltage battery management system: a176 SW graceful power off | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a177_SW_Energy_Buffer_Size` | page 2 | High-voltage battery management system: a177 SW energy buffer size | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a178_SW_Uncontrolled_Regen_PwrB` | page 2 | High-voltage battery management system: a178 SW uncontrolled regen pwr b | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a179_HvpGpoRequestActive` | page 2 | High-voltage battery management system: a179 hvp gpo request active | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a180_SW_ECU_reset_blocked` | page 2 | High-voltage battery management system: a180 SW ECU reset blocked | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a181_SW_Shunt_Over_Temperature` | page 3 | High-voltage battery management system: a181 SW shunt over temperature | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a182_LifeModel_NoCurrentLoss_Change` | page 3 | High-voltage battery management system: a182 life model no current loss change | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a183_LifeModel_StoDcrGrowth_Change` | page 3 | High-voltage battery management system: a183 life model sto dcr growth change | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a184_LifeModel_CyclingLoss_Change` | page 3 | High-voltage battery management system: a184 life model cycling loss change | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a185_LifeModel_CyclingDcrGrowth_Change` | page 3 | High-voltage battery management system: a185 life model cycling dcr growth change | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a186_RippleHeatingChargeFault` | page 3 | High-voltage battery management system: a186 ripple heating charge fault | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a187_RippleHeatingEmergencyShutdown` | page 3 | High-voltage battery management system: a187 ripple heating emergency shutdown | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_a188_DtcConfirmed` | page 3 | High-voltage battery management system: a188 dtc confirmed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`BMS_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (48 signals), page 1 (49 signals), page 2 (56 signals), page 3 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
