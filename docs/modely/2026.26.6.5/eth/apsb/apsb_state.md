---
layout: default
title: "APSB_state (0x748) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: state. Ethernet-side message APSB_state of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 18 signals (APSB_primaryTurbo, APSB_A_arbState, APSB_A_powerState, APSB_A_sleepState and 14 more). Bit layout, scaling, units and value tables."
---

# APSB_state (0x748) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: state. This page documents the 18 signals of APSB_state as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_state` |
| Ethernet-side id | 0x748 (1864) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 18 |

## Signals of APSB_state

Tesla Model Y CAN bus signals in `APSB_state`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_primaryTurbo` | APSB ECU: primary turbo | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURBO_A`<br>1 = `TURBO_B`<br>2 = `TURBO_UNKNOWN` | plausible |
| `APSB_A_arbState` | APSB ECU: a arb state | 2\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARB_STATE_INIT`<br>1 = `ARB_STATE_IDLE`<br>2 = `ARB_STATE_PRIMARY`<br>3 = `ARB_STATE_SECONDARY`<br>4 = `ARB_STATE_FAULT`<br>5 = `ARB_STATE_MIA`<br>6 = `ARB_STATE_UNKNOWN`<br>7 = `ARB_STATE_COUNT` | plausible |
| `APSB_A_powerState` | The state of the power state machine of Turbo A. | 5\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `POWER_STATE_IDLE`<br>1 = `POWER_STATE_AP_ON_PREPARE`<br>2 = `POWER_STATE_AP_ON_PREPARE_WAIT_FOR_ACK`<br>3 = `POWER_STATE_AP_ON_PREPARE_WAIT_FOR_RESPONSE`<br>4 = `POWER_STATE_AP_ON_READY`<br>5 = `POWER_STATE_AP_ON_READY_WAIT_FOR_ACK`<br>6 = `POWER_STATE_AP_ON_READY_WAIT_FOR_RESPONSE`<br>7 = `POWER_STATE_AP_BOOTING`<br>8 = `POWER_STATE_AP_IN_COREBOOT`<br>9 = `POWER_STATE_AP_ON`<br>10 = `POWER_STATE_AP_WAIT_FOR_SHUTDOWN`<br>11 = `POWER_STATE_AP_OFF_PREPARE`<br>12 = `POWER_STATE_AP_OFF_READY`<br>13 = `POWER_STATE_AP_OFF_READY_WAIT_FOR_ACK`<br>14 = `POWER_STATE_AP_OFF_READY_WAIT_FOR_RESPONSE`<br>15 = `POWER_STATE_AP_OFF_ABORT`<br>16 = `POWER_STATE_AP_OFF_ABORT_WAIT_FOR_ACK`<br>17 = `POWER_STATE_AP_SUSPENDED`<br>18 = `POWER_STATE_SOC_OFF_READY`<br>19 = `POWER_STATE_SOC_OFF`<br>20 = `POWER_STATE_SOC_OFF_ABORT`<br>21 = `POWER_STATE_FAULT`<br>22 = `POWER_STATE_MIA`<br>23 = `POWER_STATE_UNKNOWN`<br>24 = `POWER_STATE_VEH_BOOTING`<br>25 = `POWER_STATE_AP_IDLE`<br>26 = `POWER_STATE_AP_IN_LINUX`<br>27 = `POWER_STATE_AP_WAIT_FOR_SHUTDOWN_ABORT`<br>28 = `POWER_STATE_AP_FORCE_POWER_OFF` | plausible |
| `APSB_A_sleepState` | APSB ECU: a sleep state | 10\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SLEEP_STATE_IDLE`<br>1 = `SLEEP_STATE_WAIT_FOR_BUS_SILENCE`<br>2 = `SLEEP_STATE_READY`<br>3 = `SLEEP_STATE_GOING_TO_SLEEP`<br>4 = `SLEEP_STATE_SLEEPING`<br>5 = `SLEEP_STATE_ABORT`<br>6 = `SLEEP_STATE_FAULT`<br>7 = `SLEEP_STATE_MIA`<br>8 = `SLEEP_STATE_UNKNOWN`<br>9 = `SLEEP_STATE_COUNT` | plausible |
| `APSB_A_resetState` | APSB ECU: a reset state | 14\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RESET_STATE_NOT_RESETTING`<br>1 = `RESET_STATE_RESETTING`<br>2 = `RESET_STATE_FAULT`<br>3 = `RESET_STATE_MIA`<br>4 = `RESET_STATE_UNKNOWN`<br>5 = `RESET_STATE_COUNT` | plausible |
| `APSB_A_faultState` | APSB ECU: a fault state | 17\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `FAULT_STATE_NONE`<br>1 = `FAULT_STATE_GIC`<br>2 = `FAULT_STATE_MIF_ECC_CORRECTED`<br>3 = `FAULT_STATE_MIF_ECC_UNCORRECTED`<br>4 = `FAULT_STATE_MIF0_DFI_ALERT`<br>5 = `FAULT_STATE_MIF1_DFI_ALERT`<br>6 = `FAULT_STATE_MIF2_DFI_ALERT`<br>7 = `FAULT_STATE_MIF3_DFI_ALERT`<br>8 = `FAULT_STATE_MIF4_DFI_ALERT`<br>9 = `FAULT_STATE_MIF5_DFI_ALERT`<br>10 = `FAULT_STATE_MIF6_DFI_ALERT`<br>11 = `FAULT_STATE_MIF7_DFI_ALERT`<br>12 = `FAULT_STATE_MIF_ECC_AP`<br>13 = `FAULT_STATE_DROOP_CPUCL0`<br>14 = `FAULT_STATE_DROOP_CPUCL1`<br>15 = `FAULT_STATE_DROOP_CPUCL2`<br>16 = `FAULT_STATE_DROOP_GPU`<br>17 = `FAULT_STATE_DROOP_TRIP`<br>18 = `FAULT_STATE_CPU_FAULT`<br>19 = `FAULT_STATE_WDT`<br>20 = `FAULT_STATE_TRIP0_FAULT`<br>21 = `FAULT_STATE_TRIP1_FAULT`<br>22 = `FAULT_STATE_SOFTWARE_FAULT`<br>23 = `FAULT_STATE_SCS`<br>24 = `FAULT_STATE_UNEXPECTED`<br>25 = `FAULT_STATE_MIA`<br>26 = `FAULT_STATE_UNKNOWN`<br>27 = `FAULT_STATE_COUNT` | plausible |
| `APSB_secondaryTurbo` | APSB ECU: secondary turbo | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TURBO_A`<br>1 = `TURBO_B`<br>2 = `TURBO_UNKNOWN` | plausible |
| `APSB_B_arbState` | APSB ECU: b arb state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARB_STATE_INIT`<br>1 = `ARB_STATE_IDLE`<br>2 = `ARB_STATE_PRIMARY`<br>3 = `ARB_STATE_SECONDARY`<br>4 = `ARB_STATE_FAULT`<br>5 = `ARB_STATE_MIA`<br>6 = `ARB_STATE_UNKNOWN`<br>7 = `ARB_STATE_COUNT` | plausible |
| `APSB_B_powerState` | The state of the power state machine of Turbo B. | 27\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `POWER_STATE_IDLE`<br>1 = `POWER_STATE_AP_ON_PREPARE`<br>2 = `POWER_STATE_AP_ON_PREPARE_WAIT_FOR_ACK`<br>3 = `POWER_STATE_AP_ON_PREPARE_WAIT_FOR_RESPONSE`<br>4 = `POWER_STATE_AP_ON_READY`<br>5 = `POWER_STATE_AP_ON_READY_WAIT_FOR_ACK`<br>6 = `POWER_STATE_AP_ON_READY_WAIT_FOR_RESPONSE`<br>7 = `POWER_STATE_AP_BOOTING`<br>8 = `POWER_STATE_AP_IN_COREBOOT`<br>9 = `POWER_STATE_AP_ON`<br>10 = `POWER_STATE_AP_WAIT_FOR_SHUTDOWN`<br>11 = `POWER_STATE_AP_OFF_PREPARE`<br>12 = `POWER_STATE_AP_OFF_READY`<br>13 = `POWER_STATE_AP_OFF_READY_WAIT_FOR_ACK`<br>14 = `POWER_STATE_AP_OFF_READY_WAIT_FOR_RESPONSE`<br>15 = `POWER_STATE_AP_OFF_ABORT`<br>16 = `POWER_STATE_AP_OFF_ABORT_WAIT_FOR_ACK`<br>17 = `POWER_STATE_AP_SUSPENDED`<br>18 = `POWER_STATE_SOC_OFF_READY`<br>19 = `POWER_STATE_SOC_OFF`<br>20 = `POWER_STATE_SOC_OFF_ABORT`<br>21 = `POWER_STATE_FAULT`<br>22 = `POWER_STATE_MIA`<br>23 = `POWER_STATE_UNKNOWN`<br>24 = `POWER_STATE_VEH_BOOTING`<br>25 = `POWER_STATE_AP_IDLE`<br>26 = `POWER_STATE_AP_IN_LINUX`<br>27 = `POWER_STATE_AP_WAIT_FOR_SHUTDOWN_ABORT`<br>28 = `POWER_STATE_AP_FORCE_POWER_OFF` | plausible |
| `APSB_B_sleepState` | APSB ECU: b sleep state | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SLEEP_STATE_IDLE`<br>1 = `SLEEP_STATE_WAIT_FOR_BUS_SILENCE`<br>2 = `SLEEP_STATE_READY`<br>3 = `SLEEP_STATE_GOING_TO_SLEEP`<br>4 = `SLEEP_STATE_SLEEPING`<br>5 = `SLEEP_STATE_ABORT`<br>6 = `SLEEP_STATE_FAULT`<br>7 = `SLEEP_STATE_MIA`<br>8 = `SLEEP_STATE_UNKNOWN`<br>9 = `SLEEP_STATE_COUNT` | plausible |
| `APSB_B_resetState` | APSB ECU: b reset state | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RESET_STATE_NOT_RESETTING`<br>1 = `RESET_STATE_RESETTING`<br>2 = `RESET_STATE_FAULT`<br>3 = `RESET_STATE_MIA`<br>4 = `RESET_STATE_UNKNOWN`<br>5 = `RESET_STATE_COUNT` | plausible |
| `APSB_B_faultState` | APSB ECU: b fault state | 39\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `FAULT_STATE_NONE`<br>1 = `FAULT_STATE_GIC`<br>2 = `FAULT_STATE_MIF_ECC_CORRECTED`<br>3 = `FAULT_STATE_MIF_ECC_UNCORRECTED`<br>4 = `FAULT_STATE_MIF0_DFI_ALERT`<br>5 = `FAULT_STATE_MIF1_DFI_ALERT`<br>6 = `FAULT_STATE_MIF2_DFI_ALERT`<br>7 = `FAULT_STATE_MIF3_DFI_ALERT`<br>8 = `FAULT_STATE_MIF4_DFI_ALERT`<br>9 = `FAULT_STATE_MIF5_DFI_ALERT`<br>10 = `FAULT_STATE_MIF6_DFI_ALERT`<br>11 = `FAULT_STATE_MIF7_DFI_ALERT`<br>12 = `FAULT_STATE_MIF_ECC_AP`<br>13 = `FAULT_STATE_DROOP_CPUCL0`<br>14 = `FAULT_STATE_DROOP_CPUCL1`<br>15 = `FAULT_STATE_DROOP_CPUCL2`<br>16 = `FAULT_STATE_DROOP_GPU`<br>17 = `FAULT_STATE_DROOP_TRIP`<br>18 = `FAULT_STATE_CPU_FAULT`<br>19 = `FAULT_STATE_WDT`<br>20 = `FAULT_STATE_TRIP0_FAULT`<br>21 = `FAULT_STATE_TRIP1_FAULT`<br>22 = `FAULT_STATE_SOFTWARE_FAULT`<br>23 = `FAULT_STATE_SCS`<br>24 = `FAULT_STATE_UNEXPECTED`<br>25 = `FAULT_STATE_MIA`<br>26 = `FAULT_STATE_UNKNOWN`<br>27 = `FAULT_STATE_COUNT` | plausible |
| `APSB_A_autosteerMonitorState` | The state of the autosteer Monitor state machine for TurboA. | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTOSTEER_MONITOR_IDLE`<br>1 = `AUTOSTEER_MONITOR_ACTIVE`<br>2 = `AUTOSTEER_MONITOR_WAIT_FOR_MIA`<br>3 = `AUTOSTEER_MONITOR_TOI_TRIGGER`<br>4 = `AUTOSTEER_MONITOR_MIA`<br>5 = `AUTOSTEER_MONITOR_COUNT` | plausible |
| `APSB_B_autosteerMonitorState` | The state of the autosteer Monitor state machine for TurboB. | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTOSTEER_MONITOR_IDLE`<br>1 = `AUTOSTEER_MONITOR_ACTIVE`<br>2 = `AUTOSTEER_MONITOR_WAIT_FOR_MIA`<br>3 = `AUTOSTEER_MONITOR_TOI_TRIGGER`<br>4 = `AUTOSTEER_MONITOR_MIA`<br>5 = `AUTOSTEER_MONITOR_COUNT` | plausible |
| `APSB_eplannerState` | The state of the Eplanner of Turbo B. | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_EPLANNER_STATE_INIT`<br>1 = `APS_EPLANNER_STATE_READY`<br>2 = `APS_EPLANNER_STATE_VALID_PLAN`<br>3 = `APS_EPLANNER_STATE_EXECUTING_PLAN_TRAJ`<br>4 = `APS_EPLANNER_STATE_EXECUTING_FIXED_TRAJ`<br>5 = `APS_EPLANNER_STATE_EXECUTING_BOOT_FIXED_TRAJ`<br>6 = `APS_EPLANNER_NUM_STATES` | plausible |
| `APSB_A_faultInduced` | SGK Fault induced on Turbo A or not. | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APSB_B_faultInduced` | SGK Fault induced on Turbo B or not. | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `APSB_stateCounter` | APSB ECU: state counter | 55\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
