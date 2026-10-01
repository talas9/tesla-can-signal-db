---
layout: default
title: "VC_LVBMS_statusLow (0x718) — VC ECU, Tesla Model Y 2025.20.8 ETH"
description: "VC ECU message: LVBMS status low. Ethernet-side message VC_LVBMS_statusLow of VC ECU for Tesla Model Y firmware 2025.20.8, 38 signals (VC_lvbmsStatusLowIndex, VC_LVBMS_SOC, VC_LVBMS_SOE, VC_LVBMS_SOH and 34 more). Bit layout, scaling, units and value tables."
---

# VC_LVBMS_statusLow (0x718) — VC ECU, Tesla Model Y 2025.20.8 ETH

VC ECU message: LVBMS status low. This page documents the 38 signals of VC_LVBMS_statusLow as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VC_LVBMS_statusLow` |
| Ethernet-side id | 0x718 (1816) |
| ECU | [VC ECU](../../vc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VC |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 38 |

## Signals of VC_LVBMS_statusLow

Tesla Model Y CAN bus signals in `VC_LVBMS_statusLow`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_lvbmsStatusLowIndex` | selector | VC ECU: lvbms status low index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATE`<br>1 = `THROUGHPUT_1`<br>2 = `THROUGHPUT_2`<br>3 = `THROUGHPUT_3`<br>4 = `PACK_VITALS_2`<br>5 = `FAULT_STATS`<br>6 = `INVALID` | plausible |
| `VC_LVBMS_SOC` | page 0 | State of charge reported by the low voltage battery sensor; raw 127 = signal not available (SNA) | 8\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 102.2 | 127 = `SNA` | plausible |
| `VC_LVBMS_SOE` | page 0 | State of energy reported by the low voltage battery; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | plausible |
| `VC_LVBMS_SOH` | page 0 | State of health reported by the low voltage battery; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 126 | 127 = `SNA` | plausible |
| `VC_LVBMS_SOP` | page 0 | VC ECU: LVBMS SOP; raw 16777215 = signal not available (SNA) | 32\|24 | little-endian | unsigned | 0.001 | 0 | W | 0 to 5080 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_AvgSleepCurrent` | page 1 | Low voltage battery average sleep current; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | plausible |
| `VC_LVBMS_TimeSlept` | page 1 | VC ECU: LVBMS time slept; raw 16777215 = signal not available (SNA) | 24\|24 | little-endian | unsigned | 1 | 0 | min | 0 to 16777214 | 16777215 = `SNA` | plausible |
| `VC_LVBMS_AhCharged` | page 2 | Low voltage battery charge state; raw 4294967295 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 4294967.294 | 4294967295 = `SNA` | plausible |
| `VC_LVBMS_MinSleepCurrent` | page 2 | VC ECU: LVBMS min sleep current; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | plausible |
| `VC_LVBMS_AhDischarged` | page 3 | Low voltage battery charge state; raw 4294967295 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 4294967.294 | 4294967295 = `SNA` | plausible |
| `VC_LVBMS_MaxSleepCurrent` | page 3 | VC ECU: LVBMS max sleep current; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 0.01 | -200 | A | -200 to 455.34 | 65535 = `SNA` | plausible |
| `VC_LVBMS_sumCellVoltageFiltered` | page 4 | VC ECU: LVBMS sum cell voltage filtered; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65534 = `INVALID`<br>65535 = `SNA` | plausible |
| `VC_LVBMS_maxCellSOC` | page 4 | SOC estimate of the highest SOC cell; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 102.2 | 127 = `SNA` | plausible |
| `VC_LVBMS_minCellSOC` | page 4 | SOC estimate of the lowest SOC cell; raw 127 = signal not available (SNA) | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 102.2 | 127 = `SNA` | plausible |
| `VC_LVBMS_staticSOCCorrection` | page 4 | Flag indicating the LVBMS is performing static SOC correction. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_CORRECTION_STATE_INACTIVE`<br>1 = `LVBMS_CORRECTION_STATE_ACTIVE` | plausible |
| `VC_LVBMS_dynamicSOCCorrection` | page 4 | Flag indicating the LVBMS is performing dynamic SOC correction. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_CORRECTION_STATE_INACTIVE`<br>1 = `LVBMS_CORRECTION_STATE_ACTIVE` | plausible |
| `VC_LVBMS_usableEnergyAvailable` | page 4 | Available/remaining usable pack energy; raw 4095 = signal not available (SNA) | 41\|12 | little-endian | unsigned | 1 | 0 | Wh | 0 to 4000 | 4095 = `SNA` | plausible |
| `VC_LVBMS_CellOVLevel1` | page 5 | VC ECU: LVBMS cell OV level1 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_CellOVLevel2` | page 5 | VC ECU: LVBMS cell OV level2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_CellOVLevel3` | page 5 | VC ECU: LVBMS cell OV level3 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_CellUVLevel1` | page 5 | VC ECU: LVBMS cell UV level1 | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_CellUVLevel2` | page 5 | VC ECU: LVBMS cell UV level2 | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_ModuleOTLevel1` | page 5 | VC ECU: LVBMS module OT level1 | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_PackOVLevel1` | page 5 | VC ECU: LVBMS pack OV level1 | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_PackOVLevel2` | page 5 | Pack Over Voltage Level 2 flag status | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_DischrgOCLevel1` | page 5 | VC ECU: LVBMS dischrg OC level1 | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_DischrgOCLevel2` | page 5 | Discharge Over Current Level 2 flag status | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_ChrgOCLevel1` | page 5 | VC ECU: LVBMS chrg OC level1 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_ChrgOCLevel2` | page 5 | Charge Over Current Level 2 flag status | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_MOSFETOTLevel1` | page 5 | VC ECU: LVBMS MOSFETOT level1 | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_KBValueLostFault` | page 5 | Loss of CATL specific internal value flag status. Lost value causes offset in current sensor reading. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_BalanceCircuitFault` | page 5 | Balance Circuit Fault flag status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_MOSStateFault` | page 5 | Mosfet fault state flag status. Not to be confused with VC_LVBMS_MOSState. | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_NTCTempDiffWarnLevel1` | page 5 | VC ECU: LVBMS NTC temp diff warn level1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_DeepDischargeFlag` | page 5 | Deep Discharge flag status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_SamplingError` | page 5 | Sampling Error flag status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_MosfetStuckCloseError` | page 5 | Mosfet Stuck Close flag status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_LVBMS_MosfetStuckOpenError` | page 5 | Mosfet Stuck Open flag status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`VC_lvbmsStatusLowIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (2 signals), page 2 (2 signals), page 3 (2 signals), page 4 (6 signals), page 5 (21 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All VC ECU messages (VC)](../../vc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
