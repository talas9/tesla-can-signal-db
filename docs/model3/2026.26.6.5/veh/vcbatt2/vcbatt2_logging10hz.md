---
layout: default
title: "VCBATT2_logging10Hz (0x577) — VCBATT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "VCBATT2 ECU message: logging10 hz. Tesla Model 3 CAN bus message VCBATT2_logging10Hz (0x577) of VCBATT2 ECU, firmware 2026.26.6.5, 6 signals (VCBATT2_vehiclePowerStateDBG, VCBATT2_nmWakeUpReasonDBG, VCBATT2_nmKeepAwakeReasonDBG, VCBATT2_LIN_bus_0_busErrorCount and 2 more). Bit layout, scaling, units and value tables."
---

# VCBATT2_logging10Hz (0x577) — VCBATT2 ECU, Tesla Model 3 2026.26.6.5 VEH CAN

VCBATT2 ECU message: logging10 hz; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of VCBATT2_logging10Hz as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT2_logging10Hz` |
| CAN id | 0x577 (1399) |
| ECU | [VCBATT2 ECU](../../vcbatt2.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT2 |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of VCBATT2_logging10Hz

Tesla Model 3 CAN bus signals in `VCBATT2_logging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT2_vehiclePowerStateDBG` | VCBATT2 ECU: vehicle power state DBG | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `VEHICLE_POWER_STATE_DBG_INIT`<br>1 = `VEHICLE_POWER_STATE_DBG_LOW_POWER_AWAKE`<br>2 = `VEHICLE_POWER_STATE_DBG_CONDITIONING`<br>3 = `VEHICLE_POWER_STATE_DBG_ACCESSORY`<br>4 = `VEHICLE_POWER_STATE_DBG_ACCESSORY_PLUS`<br>5 = `VEHICLE_POWER_STATE_DBG_DRIVE`<br>6 = `VEHICLE_POWER_STATE_DBG_OTA`<br>7 = `VEHICLE_POWER_STATE_DBG_WAIT_FOR_HIGH_POWER`<br>8 = `VEHICLE_POWER_STATE_DBG_TURN_ON_LV`<br>9 = `VEHICLE_POWER_STATE_DBG_SYSTEM_CHECKS`<br>10 = `VEHICLE_POWER_STATE_DBG_LV_ON`<br>11 = `VEHICLE_POWER_STATE_DBG_JUMP_START`<br>12 = `VEHICLE_POWER_STATE_DBG_LV_SHUTDOWN`<br>13 = `VEHICLE_POWER_STATE_DBG_GO_QUIET`<br>14 = `VEHICLE_POWER_STATE_DBG_SLEEP_SHUTDOWN`<br>15 = `VEHICLE_POWER_STATE_DBG_LOW_POWER_STANDBY`<br>16 = `VEHICLE_POWER_STATE_DBG_RESET` | validated |
| `VCBATT2_nmWakeUpReasonDBG` | VCBATT2 ECU: nm wake up reason DBG | 5\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `VCBATT_WAKEUP_REASON_NONE`<br>1 = `VCBATT_WAKEUP_REASON_RESET`<br>2 = `VCBATT_WAKEUP_REASON_POWER_ON_RESET`<br>3 = `VCBATT_WAKEUP_REASON_HIGH_SLEEP_CURRENT`<br>4 = `VCBATT_WAKEUP_REASON_12V_SUPPORT_REQUIRED`<br>5 = `VCBATT_WAKEUP_REASON_CAN`<br>6 = `VCBATT_WAKEUP_REASON_LIN`<br>7 = `VCBATT_WAKEUP_REASON_TRUNK_EXTERIOR_SWITCH`<br>8 = `VCBATT_WAKEUP_REASON_FRUNK_ACCESS_POST`<br>9 = `VCBATT_WAKEUP_REASON_FRUNK_ACCESS_POST_MONITOR`<br>10 = `VCBATT_WAKEUP_REASON_FRUNK_LATCH_SWITCH`<br>11 = `VCBATT_WAKEUP_REASON_IPC_CAN`<br>12 = `VCBATT_WAKEUP_REASON_VEH_CAN`<br>13 = `VCBATT_WAKEUP_REASON_PARTY_BDY_CAN`<br>14 = `VCBATT_WAKEUP_REASON_FRUNK_EMERGENCY_RELEASE`<br>15 = `VCBATT_WAKEUP_REASON_LVBMB`<br>16 = `VCBATT_WAKEUP_REASON_AUTOPILOT_EFUSE`<br>17 = `VCBATT_WAKEUP_REASON_VCLEFT_EFUSE`<br>18 = `VCBATT_WAKEUP_REASON_EPAS_EFUSE`<br>19 = `VCBATT_WAKEUP_REASON_HW_PROT_SELF_TESTS`<br>20 = `VCBATT_WAKEUP_REASON_LIN_3`<br>21 = `VCBATT_WAKEUP_REASON_FRONTPRIV`<br>22 = `VCBATT_WAKEUP_REASON_PERSIST_ACC_PORT_POWER`<br>23 = `VCBATT_WAKEUP_REASON_LV_BATTERY_CAPACITY_TEST`<br>24 = `VCBATT_WAKEUP_REASON_LV_BATTERY_IMPEDANCE_TEST`<br>32 = `VCBATT_WAKEUP_REASON_UNKNOWN` | validated |
| `VCBATT2_nmKeepAwakeReasonDBG` | VCBATT2 ECU: nm keep awake reason DBG; raw 0 = signal not available (SNA) | 11\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `VCBATT_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `VCBATT_KEEPAWAKE_REASON_12V_SUPPORT_REQUIRED`<br>2 = `VCBATT_KEEPAWAKE_REASON_UDS_ACTIVE`<br>3 = `VCBATT_KEEPAWAKE_REASON_LVBMS_PACK_TEMPERATURE_LOW`<br>4 = `VCBATT_KEEPAWAKE_REASON_HIBERNATION_RECOVERY`<br>5 = `VCBATT_KEEPAWAKE_REASON_EXTERIOR_LIGHTS_ON`<br>6 = `VCBATT_KEEPAWAKE_REASON_SLEEP_BYPASS_NOT_SUPPORTING`<br>7 = `VCBATT_KEEPAWAKE_REASON_FRUNK_LIGHT`<br>8 = `VCBATT_KEEPAWAKE_REASON_FRUNK_ACCESS_POST`<br>9 = `VCBATT_KEEPAWAKE_REASON_CLOSURE_LATCH`<br>10 = `VCBATT_KEEPAWAKE_REASON_HEADLAMP_CALIBRATION`<br>11 = `VCBATT_KEEPAWAKE_REASON_HW_PROT_SELF_TESTS`<br>12 = `VCBATT_KEEPAWAKE_REASON_CLOSURE_SWITCH`<br>13 = `VCBATT_KEEPAWAKE_REASON_PERSIST_ACC_PORT_POWER`<br>15 = `VCBATT_KEEPAWAKE_REASON_MULTIPLE` | validated |
| `VCBATT2_LIN_bus_0_busErrorCount` | LIN bus 0 (Thermal) HW bus error count | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCBATT2_LIN_bus_1_busErrorCount` | LIN bus 1 (Homelink/Headlamp) HW bus error count | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCBATT2_hibernationStateDBG` | VCBATT2 ECU: hibernation state DBG | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_HIBERNATION_STATE_INIT`<br>1 = `VC_HIBERNATION_STATE_NOT_ACTIVE`<br>2 = `VC_HIBERNATION_STATE_ACTIVE`<br>3 = `VC_HIBERNATION_STATE_RECOVERY`<br>4 = `VC_HIBERNATION_STATE_EXIT`<br>5 = `VC_HIBERNATION_STATE_PREP` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All VCBATT2 ECU messages (VCBATT2)](../../vcbatt2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
