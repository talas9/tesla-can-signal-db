---
layout: default
title: "VCFRONT_systemStatus (0x545) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: system status. Tesla Model Y CAN bus message VCFRONT_systemStatus (0x545) of Front body controller, firmware 2025.20.8, 34 signals (VCFRONT_systemStatusMuxIndex, VCFRONT_systemStatusCounter, VCFRONT_systemStatusChecksum, VCFRONT_loadShedReason and 30 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_systemStatus (0x545) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN

Front body controller message: system status; frame length observed on a vehicle bus. This page documents the 34 signals of VCFRONT_systemStatus as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_systemStatus` |
| CAN id | 0x545 (1349) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 33 ms |
| Signals | 34 |

## Signals of VCFRONT_systemStatus

Tesla Model Y CAN bus signals in `VCFRONT_systemStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_systemStatusMuxIndex` | selector | Front body controller: system status mux index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SYSTEM_DATA`<br>1 = `ACTIVE_LOAD_SHED_REASONS`<br>2 = `LOAD_SHED_STATUSES_AND_COMMANDS` | plausible |
| `VCFRONT_systemStatusCounter` |  | Front body controller: system status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCFRONT_systemStatusChecksum` |  | Front body controller: system status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_loadShedReason` | page 1 | Front body controller: load shed reason | 3\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 | 0 = `VCFRONT_LOAD_SHED_REASON_NONE`<br>1 = `VCFRONT_LOAD_SHED_REASON_DCDC_SATURATION`<br>2 = `VCFRONT_LOAD_SHED_REASON_VCLEFT_EFUSE_PROTECTION`<br>4 = `VCFRONT_LOAD_SHED_REASON_VCRIGHT_EFUSE_PROTECTION`<br>8 = `VCFRONT_LOAD_SHED_REASON_POST_CRASH`<br>16 = `VCFRONT_LOAD_SHED_REASON_HV_FAULT`<br>32 = `VCFRONT_LOAD_SHED_REASON_FACTORY`<br>64 = `VCFRONT_LOAD_SHED_REASON_CUSTOM`<br>128 = `VCFRONT_LOAD_SHED_REASON_PRECHARGE`<br>256 = `VCFRONT_LOAD_SHED_REASON_LV_HEALTH` | validated |
| `VCFRONT_VCRightEFuseLoadShedStage` | page 1 | Front body controller: VC right e fuse load shed stage | 12\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `IDLE`<br>31 = `MAX` | validated |
| `VCFRONT_VCLeftEFuseLoadShedStage` | page 1 | Front body controller: VC left e fuse load shed stage | 20\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `IDLE`<br>31 = `MAX` | validated |
| `VCFRONT_DCDCSaturationLoadShedStage` | page 1 | Front body controller: DCDC saturation load shed stage | 28\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `IDLE`<br>31 = `MAX` | validated |
| `VCFRONT_vehicleLoadShedStage` | page 1 | Front body controller: vehicle load shed stage | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VEHICLE_LOADSHEDDING_STAGE_IDLE_OR_UNDEFINED`<br>1 = `VEHICLE_LOADSHEDDING_STAGE_1`<br>2 = `VEHICLE_LOADSHEDDING_STAGE_2`<br>3 = `VEHICLE_LOADSHEDDING_STAGE_3` | validated |
| `VCFRONT_HVFaultVehicleLoadShedRequest` | page 1 | Front body controller: HV fault vehicle load shed request | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_postCrashVehicleLoadShedActive` | page 1 | Front body controller: post crash vehicle load shed active | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_HVFaultVehicleLoadShedActive` | page 1 | Front body controller: HV fault vehicle load shed active | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_factoryVehicleLoadShedActive` | page 1 | Indicates that vehicle is factory load shedding | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_anyVehicleLoadShedActive` | page 1 | Front body controller: any vehicle load shed active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_DIVehLoadShedActive` | page 1 | Front body controller: DI veh load shed active | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_HVFaultLoadShedStateDBG` | page 1 | Front body controller: HV fault load shed state DBG | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HV_FAULT_LOADSHED_SM_STATE_INIT`<br>1 = `HV_FAULT_LOADSHED_SM_STATE_IDLE`<br>2 = `HV_FAULT_LOADSHED_SM_STATE_BLOCKED`<br>3 = `HV_FAULT_LOADSHED_SM_STATE_ACTIVE` | validated |
| `VCFRONT_LVUnhealthyVehicleLoadShedActive` | page 1 | Front body controller: LV unhealthy vehicle load shed active | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedStsCondenserFan` | page 2 | Front body controller: load shed sts condenser fan | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedStsPTPump` | page 2 | Front body controller: load shed sts PT pump | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedMCUAudio` | page 2 | Front body controller: load shed MCU audio | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedHVDownTriggerDBG` | page 2 | Front body controller: load shed HV down trigger DBG | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedPCSSatTriggerDBG` | page 2 | Front body controller: load shed PCS sat trigger DBG | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedStsBatteryPump` | page 2 | Front body controller: load shed sts battery pump | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedStsAPGlassHeater` | page 2 | Front body controller: load shed sts AP glass heater | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedStsMCUGraphics` | page 2 | Front body controller: load shed sts MCU graphics | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_IBSCurrentRMS_loadShed` | page 2 | Front body controller: IBS current RMS load shed | 16\|7 | little-endian | unsigned | 0.05 | 0 | A | 0 to 6.35 |  | validated |
| `VCFRONT_loadShedAhLeakyBktCntDBG` | page 2 | Front body controller: load shed ah leaky bkt cnt DBG | 23\|9 | little-endian | unsigned | 0.001 | 0 | Ah | 0 to 0.511 |  | validated |
| `VCFRONT_loadShedPcs` | page 2 | Front body controller: load shed pcs | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedGTWDownstrmRails` | page 2 | Front body controller: load shed GTW downstrm rails | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedPCSMIATriggerDBG` | page 2 | Front body controller: load shed PCSMIA trigger DBG | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedTAS` | page 2 | Front body controller: load shed TAS | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedBackStopBktCntDBG` | page 2 | Front body controller: load shed back stop bkt cnt DBG | 38\|5 | little-endian | unsigned | 0.05 | 0 | Ah | 0 to 1.55 |  | validated |
| `VCFRONT_loadShedPCSLeakyBktCtDBG` | page 2 | Front body controller: load shed PCS leaky bkt ct DBG | 44\|6 | little-endian | unsigned | 100 | 0 | mV | 0 to 6300 |  | validated |
| `VCFRONT_loadShedUI` | page 2 | Front body controller: load shed UI | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_loadShedAutoPilot` | page 2 | Front body controller: load shed auto pilot | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCFRONT_systemStatusMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (13 signals), page 2 (18 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
