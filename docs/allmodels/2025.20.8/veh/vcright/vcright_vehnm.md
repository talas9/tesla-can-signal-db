---
layout: default
title: "VCRIGHT_vehNm (0x423) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Right body controller message: veh nm. Tesla Model 3 / Model Y CAN bus message VCRIGHT_vehNm (0x423) of Right body controller, firmware 2025.20.8, 7 signals (VCRIGHT_nmGoingToSleep, VCRIGHT_nmWakeUpBus, VCRIGHT_nmKeepAwakeReason, VCRIGHT_nmWakeUpReason and 3 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_vehNm (0x423) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Right body controller message: veh nm; frame length observed on a vehicle bus. This page documents the 7 signals of VCRIGHT_vehNm as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_vehNm` |
| CAN id | 0x423 (1059) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of VCRIGHT_vehNm

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_vehNm`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_nmGoingToSleep` | Right body controller: nm going to sleep | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_nmWakeUpBus` | Right body controller: nm wake up bus | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_nmKeepAwakeReason` | Reason controller is preventing the vehicle from sleeping; raw 0 = signal not available (SNA) | 3\|5 | little-endian | unsigned | 1 | 0 |  | 1 to 31 | 0 = `VCRIGHT_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `VCRIGHT_KEEPAWAKE_REASON_EPB_STATE_NOT_SAVED`<br>2 = `VCRIGHT_KEEPAWAKE_REASON_EPB_NOT_SECURE`<br>3 = `VCRIGHT_KEEPAWAKE_REASON_HVAC_CABIN_PURGE`<br>4 = `VCRIGHT_KEEPAWAKE_REASON_HVAC_PRECONDITIONING`<br>5 = `VCRIGHT_KEEPAWAKE_REASON_CLOSURE_LATCH`<br>6 = `VCRIGHT_KEEPAWAKE_REASON_EPB_SUMMON_ACTIVE`<br>7 = `VCRIGHT_KEEPAWAKE_REASON_HANDLE`<br>8 = `VCRIGHT_KEEPAWAKE_REASON_SEAT`<br>9 = `VCRIGHT_KEEPAWAKE_REASON_TRUNK_LIGHT`<br>10 = `VCRIGHT_KEEPAWAKE_REASON_UDS_ACTIVE`<br>11 = `VCRIGHT_KEEPAWAKE_REASON_HVAC_EVAP_DRYING`<br>12 = `VCRIGHT_KEEPAWAKE_REASON_TRUNK_SWITCH`<br>14 = `VCRIGHT_KEEPAWAKE_REASON_OTHER`<br>15 = `VCRIGHT_KEEPAWAKE_REASON_VOC_PURGE`<br>16 = `VCRIGHT_KEEPAWAKE_REASON_DEFOG_CAMERA`<br>17 = `VCRIGHT_KEEPAWAKE_REASON_DEFOG_CMD`<br>31 = `VCRIGHT_KEEPAWAKE_REASON_MULTIPLE` | validated |
| `VCRIGHT_nmWakeUpReason` | Right body controller: nm wake up reason | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `VCRIGHT_WAKEUP_REASON_NONE`<br>1 = `VCRIGHT_WAKEUP_REASON_ECU_SPECIFIC`<br>2 = `VCRIGHT_WAKEUP_REASON_SWITCH_INPUT`<br>3 = `VCRIGHT_WAKEUP_REASON_RESET`<br>4 = `VCRIGHT_WAKEUP_REASON_DOOR_LATCH`<br>5 = `VCRIGHT_WAKEUP_REASON_INTERIOR_HANDLE`<br>6 = `VCRIGHT_WAKEUP_REASON_EXTERIOR_HANDLE`<br>7 = `VCRIGHT_WAKEUP_REASON_LIN_RX`<br>8 = `VCRIGHT_WAKEUP_REASON_TRUNK_SWITCH`<br>9 = `VCRIGHT_WAKEUP_REASON_TRUNK_LATCH`<br>10 = `VCRIGHT_WAKEUP_REASON_CABIN_HOT`<br>11 = `VCRIGHT_WAKEUP_REASON_POWER_ON_RESET`<br>12 = `VCRIGHT_WAKEUP_REASON_VOC_PURGE`<br>13 = `VCRIGHT_WAKEUP_REASON_DEFOG_CAMERA`<br>14 = `VCRIGHT_WAKEUP_REASON_DEFOG_CMD`<br>15 = `VCRIGHT_WAKEUP_REASON_UNKNOWN` | validated |
| `VCRIGHT_nmDebugWakeUp` | Right body controller: nm debug wake up | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `WKPU_NONE`<br>1 = `WKPU_0`<br>2 = `WKPU_1`<br>4 = `WKPU_2`<br>8 = `WKPU_3`<br>16 = `WKPU_4`<br>32 = `WKPU_5`<br>64 = `WKPU_6`<br>128 = `WKPU_7`<br>256 = `WKPU_8`<br>512 = `WKPU_9`<br>1024 = `WKPU_10`<br>2048 = `WKPU_11`<br>4096 = `WKPU_12`<br>8192 = `WKPU_13`<br>16384 = `WKPU_14`<br>32768 = `WKPU_15`<br>65536 = `WKPU_16`<br>131072 = `WKPU_17`<br>262144 = `WKPU_18`<br>524288 = `WKPU_19`<br>1048576 = `WKPU_20`<br>2097152 = `WKPU_21`<br>4194304 = `WKPU_22`<br>8388608 = `WKPU_23`<br>16777216 = `WKPU_24`<br>33554432 = `WKPU_25`<br>67108864 = `WKPU_26`<br>134217728 = `WKPU_27`<br>268435456 = `WKPU_28`<br>536870912 = `WKPU_29`<br>1073741824 = `WKPU_30`<br>2147483648 = `WKPU_31` | validated |
| `VCRIGHT_nmEthKeepAwakeReason` | Right body controller: nm eth keep awake reason; raw 0 = signal not available (SNA) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `VCRIGHT_ETH_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_TRANSITION_FROM_ACC`<br>2 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_TRANSITION_FROM_OFF`<br>3 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_DWELL_TIME_END`<br>4 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_VCSEC_WAKE`<br>5 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_POLL`<br>6 = `VCRIGHT_ETH_KEEPAWAKE_REASON_TEMP_SENSE_COP_VARIANT_ACTIVE`<br>14 = `VCRIGHT_ETH_KEEPAWAKE_REASON_OTHER`<br>15 = `VCRIGHT_ETH_KEEPAWAKE_REASON_MULTIPLE` | validated |
| `VCRIGHT_nmChKeepAwakeReason` | Right body controller: nm ch keep awake reason; raw 0 = signal not available (SNA) | 52\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `VCRIGHT_CH_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `VCRIGHT_CH_KEEPAWAKE_REASON_DEFOG_CAMERA`<br>2 = `VCRIGHT_CH_KEEPAWAKE_REASON_DEFOG_CMD`<br>14 = `VCRIGHT_CH_KEEPAWAKE_REASON_OTHER`<br>15 = `VCRIGHT_CH_KEEPAWAKE_REASON_MULTIPLE` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
