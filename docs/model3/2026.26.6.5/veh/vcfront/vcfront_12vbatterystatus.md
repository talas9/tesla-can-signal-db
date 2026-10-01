---
layout: default
title: "VCFRONT_12VBatteryStatus (0x261) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Front body controller message: 12 v battery status. Tesla Model 3 CAN bus message VCFRONT_12VBatteryStatus (0x261) of Front body controller, firmware 2026.26.6.5, 47 signals (VCFRONT_12VBatteryStatusIndex, VCFRONT_good12VforUpdate, VCFRONT_LVLoadRequest, VCFRONT_12VBatteryStatusCounter and 43 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_12VBatteryStatus (0x261) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Front body controller message: 12 v battery status; frame length observed on a vehicle bus. This page documents the 47 signals of VCFRONT_12VBatteryStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_12VBatteryStatus` |
| CAN id | 0x261 (609) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 16 ms |
| Signals | 47 |

## Signals of VCFRONT_12VBatteryStatus

Tesla Model 3 CAN bus signals in `VCFRONT_12VBatteryStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_12VBatteryStatusIndex` | selector | Front body controller: 12 v battery status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5` | validated |
| `VCFRONT_good12VforUpdate` |  | Indicates the Low Voltage (LV) battery health as it pertains to permitting an Over-The-Air (OTA) update. | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVLoadRequest` |  | Controls the loading of the Low Voltage (LV) battery for diagnostic purposes. | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_12VBatteryStatusCounter` |  | Front body controller: 12 v battery status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCFRONT_12VBatteryStatusChecksum` |  | Front body controller: 12 v battery status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_batterySupportRequest` | page 1 | Reports the request to the Power Conversion System (PCS) to supply power to the Low Voltage (LV) battery. | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_batterySMState` | page 1 | Reports the Low Voltage (LV) battery maintenance state machine state. | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BATTERY_SM_STATE_INIT`<br>1 = `BATTERY_SM_STATE_CHARGE`<br>2 = `BATTERY_SM_STATE_DISCHARGE`<br>3 = `BATTERY_SM_STATE_STANDBY`<br>4 = `BATTERY_SM_STATE_RESISTANCE_ESTIMATION`<br>5 = `BATTERY_SM_STATE_OTA_STANDBY`<br>6 = `BATTERY_SM_STATE_DISCONNECTED_BATTERY_TEST`<br>7 = `BATTERY_SM_STATE_SHORTED_CELL_TEST`<br>8 = `BATTERY_SM_STATE_FAULT`<br>9 = `BATTERY_SM_STATE_RECOVERY`<br>10 = `BATTERY_SM_STATE_EXTERNAL_LV_BUS_CONTROL` | validated |
| `VCFRONT_eFuseRecoveryStateDBG` | page 1 | Reports the state of the Low Voltage (LV) battery eFuse recovery state machine. | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_LVBMB_EFUSE_RECOVERY_STATE_INACTIVE`<br>1 = `VC_LVBMB_EFUSE_RECOVERY_STATE_SETUP`<br>2 = `VC_LVBMB_EFUSE_RECOVERY_STATE_CONNECT`<br>3 = `VC_LVBMB_EFUSE_RECOVERY_STATE_FINISH`<br>4 = `VC_LVBMB_EFUSE_RECOVERY_STATE_BLOCKED` | validated |
| `VCFRONT_batteryLINScheduleDBG` | page 1 | Front body controller: battery LIN schedule DBG; raw 7 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `VC_LVBMS_LIN_SCHEDULE_OFF`<br>1 = `VC_LVBMS_LIN_SCHEDULE_RESET`<br>2 = `VC_LVBMS_LIN_SCHEDULE_DIAGNOSTIC`<br>3 = `VC_LVBMS_LIN_SCHEDULE_DEFAULT_1`<br>4 = `VC_LVBMS_LIN_SCHEDULE_DEFAULT_2`<br>6 = `VC_LVBMS_LIN_SCHEDULE_OTHER`<br>7 = `VC_LVBMS_LIN_SCHEDULE_SNA` | validated |
| `VCFRONT_resistanceEstimationTestCounter` | page 1 | Front body controller: resistance estimation test counter | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `VCFRONT_IBSCurrent` | page 1 | Electrical current into the 12V battery | 16\|16 | little-endian | signed | 0.005 | 0 | A | -163.84 to 163.835 |  | validated |
| `VCFRONT_IBSVoltage` | page 1 | Voltage of the 12V battery; raw 4095 = signal not available (SNA) | 32\|14 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 65.535 | 4095 = `SNA` | validated |
| `VCFRONT_reverseBatteryFault` | page 1 | Indicates a fault on the reverse battery eFuse. | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVBatterySupported` | page 1 | Indicates whether the Low Voltage (LV) battery is being supported. | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVBatteryCannotSupportVehicle` | page 1 | Front body controller: LV battery cannot support vehicle | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_goodTemp12VforUpdate` | page 1 | Front body controller: good temp12 vfor update | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_12VBatteryTargetVoltage` | page 2 | Reports the target Low Voltage (LV) battery voltage. | 3\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VCFRONT_IBSTemperature` | page 2 | Front body controller: IBS temperature; raw 2047 = signal not available (SNA) | 16\|11 | little-endian | unsigned | 0.1 | -24 | degC | -24 to 124 | 2047 = `IBS_TEMPERATURE_SNA` | validated |
| `VCFRONT_currentSensorMismatchLeakyBktPctDBG` | page 2 | Front body controller: current sensor mismatch leaky bkt pct DBG | 27\|7 | little-endian | unsigned | 2 | 0 | PCT | 0 to 254 |  | validated |
| `VCFRONT_LVBatteryEnergyRemainingPCT` | page 2 | Reports the percentage of energy remaining in the Low Voltage (LV) battery. | 37\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `VCFRONT_LVBatteryStatusForDrive` | page 2 | Indicates the Low Voltage (LV) battery health status as it pertains to drive readiness. May trigger a Graceful Power Off (GPO) and block drive. | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_BATTERY_NOT_READY_FOR_DRIVE`<br>1 = `LV_BATTERY_READY_FOR_DRIVE`<br>2 = `LV_BATTERY_EXIT_DRIVE_REQUESTED` | validated |
| `VCFRONT_LVBatteryType` | page 2 | Reports the type of Low Voltage (LV) battery that the firmware is configured for. | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LV_BATTERY_TYPE_UNKNOWN`<br>1 = `LV_BATTERY_TYPE_ATLASBX_B24_FLOODED`<br>2 = `LV_BATTERY_TYPE_CLARIOS_B24_FLOODED`<br>3 = `LV_BATTERY_TYPE_CATL_LI_ION`<br>4 = `LV_BATTERY_TYPE_TESLA_16V_LI_ION`<br>5 = `LV_BATTERY_TYPE_TESLA_48V_LI_ION` | validated |
| `VCFRONT_resistanceEstimationNeeded` | page 2 | Indication that the conditions which require a resistance estimation test to be performed have been met | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_IBSVoltageFiltered` | page 3 | Measures the filtered voltage of the Low Voltage (LV) bus; raw 16383 = signal not available (SNA) | 3\|14 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 65.535 | 16381 = `MIN`<br>16382 = `MAX`<br>16383 = `SNA` | validated |
| `VCFRONT_LVBMS_LVBusVoltageSourceDBG` | page 3 | Reports the source of the Low Voltage (LV) bus voltage used for the Low Voltage Battery Management System (LVBMS). | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_LVBMS_VOLTAGE_SOURCE_NONE`<br>1 = `VC_LVBMS_VOLTAGE_SOURCE_IBS`<br>2 = `VC_LVBMS_VOLTAGE_SOURCE_VBAT_MONITOR`<br>3 = `VC_LVBMS_VOLTAGE_SOURCE_LVBMS` | validated |
| `VCFRONT_LVBMS_LVPackCurrentSourceDBG` | page 3 | Reports the source of the Low Voltage (LV) pack current used for LV battery charge regulation. | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_LV_PACK_CURRENT_SOURCE_NONE`<br>1 = `VC_LV_PACK_CURRENT_SOURCE_IBS`<br>2 = `VC_LV_PACK_CURRENT_SOURCE_LVBMS` | validated |
| `VCFRONT_LVBatterySupportRqrdTrigger` | page 3 | Reports what caused the Low Voltage (LV) battery support required trigger when the vehicle wakes to charge. | 24\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 | 0 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_NONE`<br>1 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_IBS_FILTERED_VOLTAGE`<br>2 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_PACK_FILTERED_VOLTAGE`<br>3 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_FILTERED_VOLTAGES`<br>4 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_IBS_RAW_VOLTAGE`<br>5 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_IBS_VOLTAGES`<br>8 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_PACK_RAW_VOLTAGE`<br>10 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_PACK_VOLTAGES`<br>12 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_RAW_BATTERY_VOLTAGES`<br>16 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_VBAT_RAW_VOLTAGE`<br>20 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_RAW_VC_VOLTAGES`<br>32 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_UNKNOWN_VOLTAGE`<br>64 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_AH_COUNT`<br>128 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_PERIODIC_CHARGE`<br>256 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_POWER_ON_RESET`<br>512 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_EXIT_TRANSPORT_MODE`<br>1024 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_POST_OTA`<br>2048 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_SOC`<br>4096 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_IMBALANCE`<br>6144 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_SOC_AND_IMBALANCE`<br>8192 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_CORRECTION`<br>10240 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_SOC_AND_CORRECTION`<br>12288 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_IMBALANCE_AND_CORRECTION`<br>14336 = `LV_BATTERY_SUPPORT_REQUIRED_TRIGGER_SOC_IMBALANCE_AND_CORRECTION` | validated |
| `VCFRONT_goodForPCSPowerCycleLeakyBktDBG` | page 3 | Front body controller: good for PCS power cycle leaky bkt DBG | 40\|5 | little-endian | unsigned | 0.0005 | 0 | Ah | 0 to 0.0155 |  | validated |
| `VCFRONT_LVBusControlsFutile` | page 3 | Indicates that a required condition is not met for the Low Voltage (LV) bus controllers to operate properly. | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_resistanceEstimationTestValid` | page 3 | Front body controller: resistance estimation test valid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_resistanceEstimationTestsExpended` | page 3 | Front body controller: resistance estimation tests expended | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_goodLVChargeForUpdate` | page 3 | Indicates that the Low Voltage (LV) battery charge is sufficient to permit an Over-The-Air (OTA) update. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_opportunisticDCRTestNeeded` | page 3 | Front body controller: opportunistic DCR test needed | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_voltageProfile` | page 4 | Indicates which voltage profile is used to support the 12V battery | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VOLTAGE_PROFILE_CHARGE`<br>1 = `VOLTAGE_PROFILE_FLOAT`<br>2 = `VOLTAGE_PROFILE_REDUCED_FLOAT`<br>3 = `VOLTAGE_PROFILE_ALWAYS_CLOSED_CONTACTORS` | validated |
| `VCFRONT_IBSAmpHours` | page 4 | Measures the energy state of the Low Voltage (LV) battery in amp hours. | 5\|14 | little-endian | signed | 0.005 | 0 | Ah | -40.96 to 40.955 |  | validated |
| `VCFRONT_IBSVoltageRawDBG` | page 4 | Front body controller: IBS voltage raw DBG; raw 16383 = signal not available (SNA) | 19\|14 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 65.535 | 16381 = `MIN`<br>16382 = `MAX`<br>16383 = `SNA` | validated |
| `VCFRONT_LVBatteryLINCommsDetectedDBG` | page 4 | Front body controller: LV battery LIN comms detected DBG | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_voltageSensorMismatchLeakyBktPctDBG` | page 4 | Front body controller: voltage sensor mismatch leaky bkt pct DBG | 34\|7 | little-endian | unsigned | 2 | 0 | PCT | 0 to 254 |  | validated |
| `VCFRONT_LVBusControlMode` | page 4 | Front body controller: LV bus control mode | 41\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LV_BUS_IDLE`<br>1 = `HW_PROT_SELF_TESTS`<br>2 = `BLOCK_LV_BATT_CHARGING`<br>3 = `BRIDGE_MANAGER`<br>4 = `BATTERY_CAPACITY_TEST`<br>5 = `LVBMB_EFUSE_TEST`<br>6 = `BATTERY_IMPEDANCE_TEST`<br>7 = `LVBMB_EFUSE_RECOVERY`<br>8 = `DISCONNECTED_BATTERY_TEST`<br>9 = `JUMP_POST`<br>15 = `MODE_RESERVED` | validated |
| `VCFRONT_resistanceEstimationExtendedTestEnabled` | page 4 | Front body controller: resistance estimation extended test enabled | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVBatteryFctryLimOverrideOk` | page 4 | Front body controller: LV battery fctry lim override ok | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVBatterySPICommsDetectedDBG` | page 4 | Front body controller: LV battery SPI comms detected DBG | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_targetCurrent` | page 5 | Reports the target current set by the Low Voltage Battery Management System (LVBMS). | 3\|11 | little-endian | unsigned | 0.125 | -127 | A | 0 to 120 |  | validated |
| `VCFRONT_PCSMia` | page 5 | Indicates that the Power Conversion System (PCS) is not communicating on CAN. | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chargeNeeded` | page 5 | Indicates that the Low Voltage (LV) battery needs to be charged. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_voltageControlLoopIntegrationVal` | page 5 | Front body controller: voltage control loop integration val | 16\|14 | little-endian | unsigned | 0.006 | 0 | V | 0 to 65.535 |  | validated |
| `VCFRONT_currentControlLoopIntegrationVal` | page 5 | Front body controller: current control loop integration val | 30\|14 | little-endian | unsigned | 0.006 | 0 | V | 0 to 65.535 |  | validated |

## Multiplexing

`VCFRONT_12VBatteryStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (11 signals), page 2 (7 signals), page 3 (10 signals), page 4 (9 signals), page 5 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
