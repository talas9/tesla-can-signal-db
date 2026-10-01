---
layout: default
title: "VCFRONT_vehicleStatus (0x3A1) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Front body controller message: vehicle status. Tesla Model 3 CAN bus message VCFRONT_vehicleStatus (0x3A1) of Front body controller, firmware 2026.26.6.5, 35 signals (VCFRONT_vehicleStatusMuxIndex, VCFRONT_vehicleStatusCounter, VCFRONT_vehicleStatusChecksum, VCFRONT_preconditionRequest and 31 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_vehicleStatus (0x3A1) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Front body controller message: vehicle status; frame length observed on a vehicle bus. This page documents the 35 signals of VCFRONT_vehicleStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_vehicleStatus` |
| CAN id | 0x3A1 (929) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 35 |

## Signals of VCFRONT_vehicleStatus

Tesla Model 3 CAN bus signals in `VCFRONT_vehicleStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_vehicleStatusMuxIndex` | selector | Front body controller: vehicle status mux index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MUX0`<br>1 = `MUX1` | validated |
| `VCFRONT_vehicleStatusCounter` |  | Front body controller: vehicle status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCFRONT_vehicleStatusChecksum` |  | Front body controller: vehicle status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_preconditionRequest` | page 0 | Front body controller: precondition request | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_APGlassHeaterState` | page 0 | Front body controller: AP glass heater state; raw 0 = signal not available (SNA) | 2\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCFRONT_thermalSystemType` | page 0 | Front body controller: thermal system type; raw 1 = signal not available (SNA) | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEGACY_THERMAL_SYSTEM`<br>1 = `HEAT_PUMP_THERMAL_SYSTEM` | validated |
| `VCFRONT_standbySupplySupported` | page 0 | Front body controller: standby supply supported | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_driverPresent` | page 0 | Front body controller: driver present | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_passengerPresent` | page 0 | Front body controller: passenger present | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_accPlusAvailable` | page 0 | Front body controller: acc plus available | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_diPowerOnState` | page 0 | Front body controller: di power on state | 10\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_POWERED_OFF`<br>1 = `DI_POWERED_ON_FOR_SUMMON`<br>2 = `DI_POWERED_ON_FOR_STATIONARY_HEAT`<br>3 = `DI_POWERED_ON_FOR_DRIVE`<br>4 = `DI_POWER_GOING_DOWN`<br>5 = `DI_POWERED_ON_FOR_WINCH` | validated |
| `VCFRONT_12vStatusForDrive` | page 0 | Front body controller: 12v status for drive | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_READY_FOR_DRIVE_12V`<br>1 = `READY_FOR_DRIVE_12V`<br>2 = `EXIT_DRIVE_REQUESTED_12V` | validated |
| `VCFRONT_dcr12VMilliOhms` | page 0 | Front body controller: dcr12 v milli ohms | 16\|8 | little-endian | unsigned | 1 | 0 | mOhm | 0 to 255 |  | validated |
| `VC_userPresenceState` | page 0 | User presence state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT`<br>3 = `TIMED_OUT` | validated |
| `VCFRONT_factoryLimitsOverrideOk` | page 0 | Front body controller: factory limits override ok | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_ota12VSupportRequest` | page 0 | Front body controller: ota12 v support request | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_driverBuckleStatus` | page 0 | Front body controller: driver buckle status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNBUCKLED`<br>1 = `BUCKLED` | validated |
| `VCFRONT_driverDoorStatus` | page 0 | Front body controller: driver door status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DOOR_OPEN`<br>1 = `DOOR_CLOSED` | validated |
| `VCFRONT_driverUnbuckled` | page 0 | Front body controller: driver unbuckled; raw 2 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_passengerUnbuckled` | page 0 | Front body controller: passenger unbuckled; raw 2 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_2RowLeftUnbuckled` | page 0 | Front body controller: 2 row left unbuckled; raw 2 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_2RowCenterUnbuckled` | page 0 | Front body controller: 2 row center unbuckled; raw 2 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_2RowRightUnbuckled` | page 0 | Front body controller: 2 row right unbuckled; raw 2 = signal not available (SNA) | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_pcsEFuseVoltage` | page 0 | Front body controller: pcs e fuse voltage; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.2 | 1023 = `SNA` | validated |
| `VCFRONT_bmsHvChargeEnable` | page 1 | Front body controller: bms hv charge enable | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_3RowLeftUnbuckled` | page 1 | Indication that the third row left passenger has unbuckled their seat belt; raw 2 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_3RowRightUnbuckled` | page 1 | Indication that the third row right passenger has unbuckled their seat belt; raw 2 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHIME_NONE`<br>1 = `CHIME_OCCUPIED_AND_UNBUCKLED`<br>2 = `CHIME_SNA` | validated |
| `VCFRONT_maxBattHeatRejection` | page 1 | Radiator max heat rejection estimated at zero vehicle speed. | 6\|10 | little-endian | unsigned | 30 | 0 | W | 0 to 30690 |  | validated |
| `VCFRONT_hvacReqBattCoolOutTemp` | page 1 | Battery outlet coolant temp target to allow HVAC min comfort | 16\|9 | little-endian | unsigned | 0.1 | 40 | degC | 40 to 91.1 |  | validated |
| `VCFRONT_PCSCurrent` | page 1 | Front body controller: PCS current | 25\|13 | little-endian | signed | 0.1 | 0 | A | -409.6 to 409.5 |  | validated |
| `VCFRONT_refSystemNominal` | page 1 | Front body controller: ref system nominal | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_driverEnteredCabinEstimateDBG` | page 1 | Front body controller: driver entered cabin estimate DBG | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_anySWEFuseActive` | page 1 | Front body controller: any SWE fuse active | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_hpBattHeatingPowerTrgt` | page 1 | Reports the heat pump battery heating power target. | 41\|7 | little-endian | unsigned | 100 | 0 | W | 0 to 10000 |  | validated |
| `VCFRONT_LVStatusForDriveVEH` | page 1 | Front body controller: LV status for drive VEH | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_FOR_DRIVE_NOT_READY`<br>1 = `STATUS_FOR_DRIVE_READY`<br>2 = `STATUS_FOR_DRIVE_READY_LIMITED`<br>3 = `STATUS_FOR_DRIVE_RETURN_TO_SERVICE`<br>4 = `STATUS_FOR_DRIVE_LIMP`<br>5 = `STATUS_FOR_DRIVE_PULL_TO_SHOULDER`<br>6 = `STATUS_FOR_DRIVE_ACTIVE_DECEL` | validated |

## Multiplexing

`VCFRONT_vehicleStatusMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (21 signals), page 1 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
