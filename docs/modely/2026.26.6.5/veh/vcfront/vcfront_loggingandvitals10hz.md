---
layout: default
title: "VCFRONT_loggingAndVitals10Hz (0x201) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: logging and vitals10 hz. Tesla Model Y CAN bus message VCFRONT_loggingAndVitals10Hz (0x201) of Front body controller, firmware 2026.26.6.5, 50 signals (VCFRONT_loggingAndVitals10HzIndex, VCFRONT_pumpBatteryRPMActual, VCFRONT_pumpPowertrainRPMActual, VCFRONT_radiatorFanRPMActual and 46 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_loggingAndVitals10Hz (0x201) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: logging and vitals10 hz; frame length observed on a vehicle bus. This page documents the 50 signals of VCFRONT_loggingAndVitals10Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_loggingAndVitals10Hz` |
| CAN id | 0x201 (513) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 25 ms |
| Signals | 50 |

## Signals of VCFRONT_loggingAndVitals10Hz

Tesla Model Y CAN bus signals in `VCFRONT_loggingAndVitals10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_loggingAndVitals10HzIndex` | selector | Front body controller: logging and vitals10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TARGETS_AND_ACTUALS_0`<br>1 = `STATES_AND_SENSORS`<br>2 = `EXV_FLOW`<br>3 = `EXV_FLOW_TARGET`<br>4 = `END` | plausible |
| `VCFRONT_pumpBatteryRPMActual` | page 0 | Front body controller: pump battery RPM actual; raw 255 = signal not available (SNA) | 3\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | validated |
| `VCFRONT_pumpPowertrainRPMActual` | page 0 | Front body controller: pump powertrain RPM actual; raw 255 = signal not available (SNA) | 11\|8 | little-endian | unsigned | 30 | 0 | rpm | 0 to 7500 | 255 = `SNA` | validated |
| `VCFRONT_radiatorFanRPMActual` | page 0 | Front body controller: radiator fan RPM actual; raw 255 = signal not available (SNA) | 19\|8 | little-endian | unsigned | 40 | 0 | rpm | 0 to 10000 | 255 = `SNA` | validated |
| `VCFRONT_exvFlowTarget` | page 0 | Front body controller: exv flow target | 27\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_activeLouverOpenPosTarg` | page 0 | The target position for the active louver | 35\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_pressureRefrigLiquid` | page 0 | Refrigerant system Liquid line pressure; raw 511 = signal not available (SNA) | 42\|9 | little-endian | unsigned | 0.08 | 0 | bar | 0 to 37.25 | 511 = `SNA` | validated |
| `VCFRONT_compSleepRequest` | page 0 | Front body controller: comp sleep request | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_thermalHvPowerBudget` | page 0 | Front body controller: thermal hv power budget | 52\|7 | little-endian | unsigned | 0.2 | 0 | kW | 0 to 25.4 |  | validated |
| `VCFRONT_compMinOnTimeActive` | page 0 | Front body controller: comp min on time active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_compMinOffTimeActive` | page 0 | Front body controller: comp min off time active | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_fanDemand` | page 1 | Front body controller: fan demand | 3\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_compressorState` | page 1 | State of the refrigerant compressor. | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDBY`<br>1 = `READY`<br>2 = `RUNNING`<br>3 = `FAULT` | validated |
| `VCFRONT_compDemandEvap` | page 1 | Front body controller: comp demand evap | 12\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_exvState` | page 1 | Front body controller: exv state | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_solenoidEvapState` | page 1 | Front body controller: solenoid evap state | 23\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SOLENOID_UNDEFINED`<br>1 = `SOLENOID_OPENED`<br>2 = `SOLENOID_CLOSED`<br>3 = `SOLENOID_FAULTED` | validated |
| `VCFRONT_compDemandChiller` | page 1 | Front body controller: comp demand chiller | 25\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_coolantValveMode` | page 1 | Coolant mode of the powertrain cooling circuit | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SERIES`<br>1 = `PARALLEL`<br>2 = `BLEND`<br>3 = `AMBIENT_SOURCE` | validated |
| `VCFRONT_compFaultSeverity` | page 1 | Front body controller: comp fault severity | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `LOW`<br>2 = `MEDIUM`<br>3 = `HIGH` | validated |
| `VCFRONT_solenoidEngaged` | page 1 | Front body controller: solenoid engaged | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpHighSideHX` | page 1 | Front body controller: hp high side HX | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `hpHighSideHX_NONE`<br>1 = `hpHighSideHX_LCC`<br>2 = `hpHighSideHX_CC`<br>3 = `hpHighSideHX_BOTH` | validated |
| `VCFRONT_hpLowSideHX` | page 1 | Front body controller: hp low side HX | 39\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `hpLowSideHX_NONE`<br>1 = `hpLowSideHX_CHILLER`<br>2 = `hpLowSideHX_EVAP`<br>3 = `hpLowSideHX_BOTH` | validated |
| `VCFRONT_hpDominantLoad` | page 1 | Dominant load type for the refrigerant system | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `hpDominantLoad_NONE`<br>1 = `hpDominantLoad_EVAP`<br>2 = `hpDominantLoad_CHILLER`<br>3 = `hpDominantLoad_LOW_BOTH`<br>4 = `hpDominantLoad_LCC`<br>5 = `hpDominantLoad_CC`<br>6 = `hpDominantLoad_HIGH_BOTH` | validated |
| `VCFRONT_hpBlendType` | page 1 | Front body controller: hp blend type | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HP_NONE`<br>1 = `HP_PARTIAL`<br>2 = `HP_FULL` | validated |
| `VCFRONT_hpQuietModeEnabled` | page 1 | Front body controller: hp quiet mode enabled | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpCabinLoadType` | page 1 | Front body controller: hp cabin load type | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `hpCabinLoadType_NONE`<br>1 = `hpCabinLoadType_CC`<br>2 = `hpCabinLoadType_REHEAT`<br>3 = `hpCabinLoadType_EVAP` | validated |
| `VCFRONT_hpBatteryLoadType` | page 1 | Front body controller: hp battery load type | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `BATT_HEAT`<br>2 = `BATT_COOL` | validated |
| `VCFRONT_hpReqCoolantMode` | page 1 | Front body controller: hp req coolant mode | 51\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ANY`<br>1 = `SERIES_NO_BYPASS`<br>2 = `SERIES_BYPASS`<br>3 = `PARALLEL`<br>4 = `AMBIENT_SOURCE` | validated |
| `VCFRONT_hpReqTransScavenge` | page 1 | Front body controller: hp req trans scavenge | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_compLiqPumpOutState` | page 1 | Front body controller: comp liq pump out state | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `COMP_LIQ_PUMP_OUT_NOT_ALLOWED`<br>1 = `COMP_LIQ_PUMP_OUT_WAITING`<br>2 = `COMP_LIQ_PUMP_OUT_ALLOWED`<br>3 = `COMP_LIQ_PUMP_OUT_RUNNING`<br>4 = `COMP_LIQ_PUMP_OUT_COMPLETED`<br>5 = `COMP_LIQ_PUMP_OUT_ABORTED` | validated |
| `VCFRONT_frunkStateDBG` | page 1 | The verbose debug state of the frunk latch | 58\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `FRUNK_STATE_INIT`<br>1 = `FRUNK_STATE_CLOSED`<br>2 = `FRUNK_STATE_OPENED`<br>3 = `FRUNK_STATE_AJAR`<br>4 = `FRUNK_STATE_FAULT`<br>5 = `FRUNK_STATE_FAULT_OPENED`<br>6 = `FRUNK_STATE_FAULT_CLOSED`<br>7 = `FRUNK_STATE_RELEASING_RETRACTING_1`<br>8 = `FRUNK_STATE_RELEASING_EXTENDING_1`<br>9 = `FRUNK_STATE_RELEASING_RETRACTING_2`<br>10 = `FRUNK_STATE_RELEASING_EXTENDING_2`<br>11 = `FRUNK_STATE_RESETTING`<br>12 = `FRUNK_STATE_FAULT_RELEASED` | validated |
| `VCFRONT_frunkSwitchGroupState` | page 1 | Front body controller: frunk switch group state | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FRUNKSWITCH_GROUP_UNKNOWN`<br>1 = `FRUNKSWITCH_GROUP_MISMATCHED`<br>2 = `FRUNKSWITCH_GROUP_OPENED`<br>3 = `FRUNKSWITCH_GROUP_CLOSED` | validated |
| `VCFRONT_chillerExvFlow` | page 2 | Percent of full range that the Chiller EXV has opened | 3\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_evapExvFlow` | page 2 | Percent of full range that the evap EXV has opened | 11\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_recircExvFlow` | page 2 | Percent of full range that the recirc EXV has opened | 19\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_lccExvFlow` | page 2 | Percent of full range that the Liquid cooled condenser EXV has opened | 27\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_cclExvFlow` | page 2 | Percent of full range that the left cabin condenser EXV has opened | 35\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_ccrExvFlow` | page 2 | Percent of full range that the right cabin condenser EXV has opened | 43\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_chillerExvState` | page 2 | State of the chiller electronic expansion valve | 51\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_evapExvState` | page 2 | State of the evaporator electronic expansion valve | 55\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_recircExvState` | page 2 | State of the recirc electronic expansion valve | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_chillerExvFlowTarget` | page 3 | Target percentage of full range that the chiler electronic expansion valve is commanded to open | 3\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_evapExvFlowTarget` | page 3 | Target percentage of full range that the evap electronic expansion valve is commanded to open | 11\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_recircExvFlowTarget` | page 3 | Target percentage of full range that the recirc electronic expansion valve is commanded to open | 19\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_lccExvFlowTarget` | page 3 | Target percentage of full range that the liquid cooled condenser electronic expansion valve is commanded to open | 27\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_cclExvFlowTarget` | page 3 | Target percentage of full range that the cabin condenser left electronic expansion valve is commanded to open | 35\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_ccrExvFlowTarget` | page 3 | Target percentage of full range that the cabin condenser right electronic expansion valve is commanded to open | 43\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCFRONT_lccExvState` | page 3 | State of the liquid cooled condenser electronic expansion valve | 51\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_cclExvState` | page 3 | State of the cabin condenser left electronic expansion valve | 55\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |
| `VCFRONT_ccrExvState` | page 3 | State of the cabin conddenser left electronic expansion valve | 59\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNINIT`<br>1 = `INIT_OPEN`<br>2 = `INIT_CLOSE`<br>3 = `READY`<br>4 = `FAULTED`<br>5 = `WAIT`<br>6 = `OVERDRIVING_SHUT`<br>7 = `READY_SHUT`<br>8 = `CALIB_CLOSE`<br>9 = `CALIB_CLOSE_OVERDRIVE`<br>10 = `INIT_CLOSE_OVERDRIVE` | validated |

## Multiplexing

`VCFRONT_loggingAndVitals10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (10 signals), page 1 (21 signals), page 2 (9 signals), page 3 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
