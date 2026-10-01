---
layout: default
title: "VC_LVBMS_statusLow (0x718) — VC ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VC ECU message: LVBMS status low. Tesla Model Y CAN bus message VC_LVBMS_statusLow (0x718) of VC ECU, firmware 2026.26.6.5, 37 signals (VC_lvbmsStatusLowIndex, VC_LVBMS_SOC, VC_LVBMS_SOE, VC_LVBMS_SOH and 33 more). Bit layout, scaling, units and value tables."
---

# VC_LVBMS_statusLow (0x718) — VC ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VC ECU message: LVBMS status low; frame length observed on a vehicle bus. This page documents the 37 signals of VC_LVBMS_statusLow as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VC_LVBMS_statusLow` |
| CAN id | 0x718 (1816) |
| ECU | [VC ECU](../../vc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VC |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 37 |

## Signals of VC_LVBMS_statusLow

Tesla Model Y CAN bus signals in `VC_LVBMS_statusLow`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_lvbmsStatusLowIndex` | selector | VC ECU: lvbms status low index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATE_AND_FAULTS`<br>1 = `THROUGHPUT_1`<br>2 = `THROUGHPUT_2`<br>3 = `THROUGHPUT_3`<br>4 = `PACK_VITALS_2`<br>5 = `INVALID` | validated |
| `VC_LVBMS_SOC` | page 0 | State of charge reported by the low voltage battery sensor; raw 1023 = signal not available (SNA) | 3\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 | 1023 = `SNA` | validated |
| `VC_LVBMS_SOE` | page 0 | State of energy reported by the low voltage battery; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | validated |
| `VC_LVBMS_SOH` | page 0 | State of health reported by the low voltage battery; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | validated |
| `VC_LVBMS_CellOVLevel1` | page 0 | VC ECU: LVBMS cell OV level1 | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_CellOVLevel2` | page 0 | VC ECU: LVBMS cell OV level2 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_CellOVLevel3` | page 0 | VC ECU: LVBMS cell OV level3 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_CellUVLevel1` | page 0 | VC ECU: LVBMS cell UV level1 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_CellUVLevel2` | page 0 | VC ECU: LVBMS cell UV level2 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_ModuleOTLevel1` | page 0 | VC ECU: LVBMS module OT level1 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_PackOVLevel1` | page 0 | VC ECU: LVBMS pack OV level1 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_PackOVLevel2` | page 0 | Pack Over Voltage Level 2 flag status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_DischrgOCLevel1` | page 0 | VC ECU: LVBMS dischrg OC level1 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_DischrgOCLevel2` | page 0 | Discharge Over Current Level 2 flag status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_ChrgOCLevel1` | page 0 | VC ECU: LVBMS chrg OC level1 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_ChrgOCLevel2` | page 0 | Charge Over Current Level 2 flag status | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_MOSFETOTLevel1` | page 0 | VC ECU: LVBMS MOSFETOT level1 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_KBValueLostFault` | page 0 | Loss of CATL specific internal value flag status. Lost value causes offset in current sensor reading. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_BalanceCircuitFault` | page 0 | Balance Circuit Fault flag status | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_MOSStateFault` | page 0 | Mosfet fault state flag status. Not to be confused with VC_LVBMS_MOSState. | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_NTCTempDiffWarnLevel1` | page 0 | VC ECU: LVBMS NTC temp diff warn level1 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_DeepDischargeFlag` | page 0 | Deep Discharge flag status | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_SamplingError` | page 0 | Sampling Error flag status | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_MosfetStuckCloseError` | page 0 | Mosfet Stuck Close flag status | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_MosfetStuckOpenError` | page 0 | Mosfet Stuck Open flag status | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBMS_AvgSleepCurrent` | page 1 | Low voltage battery average sleep current; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | validated |
| `VC_LVBMS_TimeSlept` | page 1 | VC ECU: LVBMS time slept; raw 16777215 = signal not available (SNA) | 24\|24 | little-endian | unsigned | 1 | 0 | min | 0 to 16777214 | 16777215 = `SNA` | validated |
| `VC_LVBMS_SOP` | page 1 | VC ECU: LVBMS SOP; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 20 | 0 | W | 0 to 5080 | 255 = `SNA` | validated |
| `VC_LVBMS_AhCharged` | page 2 | Low voltage battery charge state; raw 4294967295 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 4294967.294 | 4294967295 = `SNA` | validated |
| `VC_LVBMS_MinSleepCurrent` | page 2 | VC ECU: LVBMS min sleep current; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | validated |
| `VC_LVBMS_AhDischarged` | page 3 | Low voltage battery charge state; raw 4294967295 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 4294967.294 | 4294967295 = `SNA` | validated |
| `VC_LVBMS_MaxSleepCurrent` | page 3 | VC ECU: LVBMS max sleep current; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | validated |
| `VC_LVBMS_sumCellVoltageFiltered` | page 4 | VC ECU: LVBMS sum cell voltage filtered; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65534 = `INVALID`<br>65535 = `SNA` | validated |
| `VC_LVBMS_maxCellSOC` | page 4 | SOC estimate of the highest SOC cell; raw 1023 = signal not available (SNA) | 24\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 | 1023 = `SNA` | validated |
| `VC_LVBMS_minCellSOC` | page 4 | SOC estimate of the lowest SOC cell; raw 1023 = signal not available (SNA) | 34\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 | 1023 = `SNA` | validated |
| `VC_LVBMS_staticSOCCorrection` | page 4 | Flag indicating the LVBMS is performing static SOC correction. | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_CORRECTION_STATE_INACTIVE`<br>1 = `LVBMS_CORRECTION_STATE_ACTIVE` | validated |
| `VC_LVBMS_dynamicSOCCorrection` | page 4 | Flag indicating the LVBMS is performing dynamic SOC correction. | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_CORRECTION_STATE_INACTIVE`<br>1 = `LVBMS_CORRECTION_STATE_ACTIVE` | validated |

## Multiplexing

`VC_lvbmsStatusLowIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (24 signals), page 1 (3 signals), page 2 (2 signals), page 3 (2 signals), page 4 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VC ECU messages (VC)](../../vc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
