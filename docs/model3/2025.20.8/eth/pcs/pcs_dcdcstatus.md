---
layout: default
title: "PCS_dcdcStatus (0x224) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2025.20.8 ETH"
description: "Power conversion system (on-board charger and DC-DC converter) message: dcdc status. Ethernet-side message PCS_dcdcStatus of Power conversion system (on-board charger and DC-DC converter) for Tesla Model 3 firmware 2025.20.8, 18 signals (PCS_dcdcPrechargeStatus, PCS_dcdcLvSupportStatus, PCS_dcdcHvBusDischargeStatus, PCS_coldSleepAllowed and 14 more). Bit layout, scaling, units and value tables."
---

# PCS_dcdcStatus (0x224) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2025.20.8 ETH

Power conversion system (on-board charger and DC-DC converter) message: dcdc status. This page documents the 18 signals of PCS_dcdcStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_dcdcStatus` |
| Ethernet-side id | 0x224 (548) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 18 |

## Signals of PCS_dcdcStatus

Tesla Model 3 CAN bus signals in `PCS_dcdcStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_dcdcPrechargeStatus` | Status of DCDC HV bus precharge | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PCS_DCDC_PRECHARGE_IDLE`<br>1 = `PCS_DCDC_PRECHARGE_ACTIVE`<br>2 = `PCS_DCDC_PRECHARGE_FAULTED`<br>3 = `PCS_DCDC_PRECHARGE_IMPEDANCE_CHECK` | plausible |
| `PCS_dcdcLvSupportStatus` | Status of DCDC LV support | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PCS_DCDC_LV_SUPPORT_IDLE`<br>1 = `PCS_DCDC_LV_SUPPORT_ACTIVE`<br>2 = `PCS_DCDC_LV_SUPPORT_FAULTED` | plausible |
| `PCS_dcdcHvBusDischargeStatus` | Power conversion system (on-board charger and DC-DC converter): dcdc hv bus discharge status | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PCS_DCDC_DIS_HVBUS_IDLE`<br>1 = `PCS_DCDC_DIS_HVBUS_ACTIVE`<br>2 = `PCS_DCDC_DIS_HVBUS_FAULTED` | plausible |
| `PCS_coldSleepAllowed` | Power conversion system (on-board charger and DC-DC converter): cold sleep allowed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS_dcdcPchgHVBusLowRDetected` | Power conversion system (on-board charger and DC-DC converter): dcdc pchg HV bus low r detected | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS_dcdcSubState` | Substate of DCDC state machine | 10\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `DCDC_SUBSTATE_PWR_UP_INIT`<br>1 = `DCDC_SUBSTATE_STANDBY`<br>2 = `DCDC_SUBSTATE_LV_SUPPORT_ACTIVE`<br>3 = `DCDC_SUBSTATE_FAST_DIS_HVBUS`<br>4 = `DCDC_SUBSTATE_SLOW_DIS_HVBUS`<br>5 = `DCDC_SUBSTATE_PCHG_FAST_DIS_HVBUS`<br>6 = `DCDC_SUBSTATE_PCHG_SLOW_DIS_HVBUS`<br>7 = `DCDC_SUBSTATE_PCHG_DWELL_CHARGE`<br>8 = `DCDC_SUBSTATE_PCHG_DWELL_WAIT`<br>9 = `DCDC_SUBSTATE_PCHG_DI_RECOVERY_WAIT`<br>10 = `DCDC_SUBSTATE_PCHG_ACTIVE`<br>11 = `DCDC_SUBSTATE_PCHG_FLT_FAST_DIS_HVBUS`<br>12 = `DCDC_SUBSTATE_SHUTDOWN`<br>13 = `DCDC_SUBSTATE_LV_SUPPORT_FAULTED`<br>14 = `DCDC_SUBSTATE_DIS_HVBUS_FAULTED`<br>15 = `DCDC_SUBSTATE_PCHG_FAULTED`<br>16 = `DCDC_SUBSTATE_CLEAR_FAULTS`<br>17 = `DCDC_SUBSTATE_FAULTED`<br>18 = `DCDC_SUBSTATE_NUM` | plausible |
| `PCS_dcdcFaulted` | Whether the DCDC is in faulted state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_okToBePowerCycled` | Power conversion system (on-board charger and DC-DC converter): ok to be power cycled | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PCS_dcdcOutputIsLimited` | Whether the DCDC's output is current limiting | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_dcdcMaxOutputCurrentAllowed` | Maximum LV output current capability of DCDC based on operating point | 29\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | plausible |
| `PCS_dcdcPrechargeRtyCnt` | Power conversion system (on-board charger and DC-DC converter): dcdc precharge rty cnt | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `PCS_dcdcLvSupportRtyCnt` | Power conversion system (on-board charger and DC-DC converter): dcdc lv support rty cnt | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PCS_dcdcDischargeRtyCnt` | Power conversion system (on-board charger and DC-DC converter): dcdc discharge rty cnt | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `PCS_dcdcPwmEnableLine` | Sensed state of the DCDC PWM enable hardline | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_dcdcSupportingFixedLvTarget` | Whether DCDC is running LV support at a fixed voltage target | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_ecuLogUploadRequest` | Power conversion system (on-board charger and DC-DC converter): ecu log upload request | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REQUEST_PRIORITY_NONE`<br>1 = `REQUEST_PRIORITY_1`<br>2 = `REQUEST_PRIORITY_2`<br>3 = `REQUEST_PRIORITY_3` | plausible |
| `PCS_dcdcPrechargeRestartCnt` | Power conversion system (on-board charger and DC-DC converter): dcdc precharge restart cnt | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `PCS_dcdcInitialPrechargeSubState` | Power conversion system (on-board charger and DC-DC converter): dcdc initial precharge sub state | 59\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `DCDC_SUBSTATE_PWR_UP_INIT`<br>1 = `DCDC_SUBSTATE_STANDBY`<br>2 = `DCDC_SUBSTATE_LV_SUPPORT_ACTIVE`<br>3 = `DCDC_SUBSTATE_FAST_DIS_HVBUS`<br>4 = `DCDC_SUBSTATE_SLOW_DIS_HVBUS`<br>5 = `DCDC_SUBSTATE_PCHG_FAST_DIS_HVBUS`<br>6 = `DCDC_SUBSTATE_PCHG_SLOW_DIS_HVBUS`<br>7 = `DCDC_SUBSTATE_PCHG_DWELL_CHARGE`<br>8 = `DCDC_SUBSTATE_PCHG_DWELL_WAIT`<br>9 = `DCDC_SUBSTATE_PCHG_DI_RECOVERY_WAIT`<br>10 = `DCDC_SUBSTATE_PCHG_ACTIVE`<br>11 = `DCDC_SUBSTATE_PCHG_FLT_FAST_DIS_HVBUS`<br>12 = `DCDC_SUBSTATE_SHUTDOWN`<br>13 = `DCDC_SUBSTATE_LV_SUPPORT_FAULTED`<br>14 = `DCDC_SUBSTATE_DIS_HVBUS_FAULTED`<br>15 = `DCDC_SUBSTATE_PCHG_FAULTED`<br>16 = `DCDC_SUBSTATE_CLEAR_FAULTS`<br>17 = `DCDC_SUBSTATE_FAULTED`<br>18 = `DCDC_SUBSTATE_NUM` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
