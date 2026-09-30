---
layout: default
title: "RCM_status (0x211) — Restraint control module, Tesla Model Y 2025.20.8 CH CAN"
description: "Restraint control module message: status. Tesla Model Y CAN bus message RCM_status (0x211) of Restraint control module, firmware 2025.20.8, 19 signals (RCM_statusChecksum, RCM_statusCounter, RCM_armStatus, RCM_warningIndicatorState and 15 more). Bit layout, scaling, units and value tables."
---

# RCM_status (0x211) — Restraint control module, Tesla Model Y 2025.20.8 CH CAN

Restraint control module message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of RCM_status as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_status` |
| CAN id | 0x211 (529) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 19 |

## Signals of RCM_status

Tesla Model Y CAN bus signals in `RCM_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_statusChecksum` | Restraint control module: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_statusCounter` | Restraint control module: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `RCM_armStatus` | Reports the arm status of the Restraint Control Module (RCM); raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_UNARMED`<br>1 = `RCM_ARMED`<br>2 = `ARMED_WITH_NOFIRE_CAL`<br>3 = `SNA` | validated |
| `RCM_warningIndicatorState` | Reports whether the Restraint Control Module (RCM) warning indicator is present on the User Interface (UI); raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_WARNING_INDICATOR_OFF`<br>1 = `RCM_WARNING_INDICATOR_ON`<br>3 = `SNA` | validated |
| `RCM_passAirbagIndicatorRequest` | Reports status of the Front Passenger Airbag Off telltale; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_PASSENGER_AIRBAG_INDICATOR_ON`<br>1 = `RCM_PASSENGER_AIRBAG_INDICATOR_OFF`<br>3 = `SNA` | validated |
| `RCM_airbagCutoffStatus` | Reports the front passenger airbag enabled or disabled status; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_PASSENGER_AIRBAG_ENABLED`<br>1 = `RCM_PASSENGER_AIRBAG_DISABLED`<br>3 = `SNA` | validated |
| `RCM_alrSwitchStatus` | Reports status of the front passenger automatic locking seat belt retractor; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_ALR_NOT_ENGAGED`<br>1 = `RCM_ALR_ENGAGED`<br>2 = `RCM_ALR_FAULTED`<br>3 = `SNA` | validated |
| `RCM_vinLearnFlag` | Reports whether the Vehicle Identification Number has been learned; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_VIN_NOT_STORED`<br>1 = `RCM_VIN_STORED`<br>2 = `RCM_VIN_STORED_MISMATCH`<br>3 = `SNA` | validated |
| `RCM_seatTrackPositionDrvr` | Driver seat track position status; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_SEAT_POSITION_NEAR`<br>1 = `RCM_SEAT_POSITION_FAR`<br>2 = `RCM_SEAT_POSITION_FAULTED`<br>3 = `SNA` | validated |
| `RCM_seatTrackPositionPass` | Passenger seat track position status; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_SEAT_POSITION_NEAR`<br>1 = `RCM_SEAT_POSITION_FAR`<br>2 = `RCM_SEAT_POSITION_FAULTED`<br>3 = `SNA` | validated |
| `RCM_edr1State` | Reports status of Restraint Control Module (RCM) Event Data Recorder (EDR) memory slot 1. | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_EDR_EMPTY`<br>1 = `RCM_EDR_STORED`<br>2 = `RCM_EDR_LOCKED`<br>3 = `RCM_EDR_UNAVAILABLE` | validated |
| `RCM_edr2State` | Reports status of Restraint Control Module (RCM) Event Data Recorder (EDR) memory slot 2. | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_EDR_EMPTY`<br>1 = `RCM_EDR_STORED`<br>2 = `RCM_EDR_LOCKED`<br>3 = `RCM_EDR_UNAVAILABLE` | validated |
| `RCM_keepPowerReason` | Restraint Control Module request to maintain power; raw 8 = signal not available (SNA) | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RCM_NO_KEEP_POWER_REQUEST`<br>1 = `RCM_IN_IDLE_MODE`<br>2 = `RCM_CRASH_ALGO_ACTIVE`<br>3 = `RCM_EDR_STORING_TO_EEPROM`<br>4 = `RCM_EDR_UPLOADING`<br>5 = `RCM_CANNOT_POWER_DOWN`<br>6 = `RCM_INITIALIZATION_PHASE`<br>7 = `RCM_INVALID_POWER_OFF_REQUEST`<br>8 = `RCM_KEEP_POWER_REASON_SNA` | validated |
| `RCM_imuOffsetLearnState` | Restraint control module: imu offset learn state | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IMU_OFFSET_LEARNING_OFF`<br>1 = `IMU_SLOW_LEARNING_DISTANCE`<br>2 = `IMU_FAST_LEARNING_TIME`<br>3 = `IMU_OFFSETS_UNABLE_TO_LEARN` | validated |
| `RCM_edr3State` | Reports status of Restraint Control Module (RCM) Event Data Recorder (EDR) memory slot 3. | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_EDR_EMPTY`<br>1 = `RCM_EDR_STORED`<br>2 = `RCM_EDR_LOCKED`<br>3 = `RCM_EDR_UNAVAILABLE` | validated |
| `RCM_driverOrientationInitStatus` | Restraint control module: driver orientation init status; raw 7 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `RCM_DRIVER_ORIENTATION_INIT_NOT_COMPLETE`<br>1 = `RCM_DRIVER_ORIENTATION_MATCHED_LHD`<br>2 = `RCM_DRIVER_ORIENTATION_MATCHED_RHD`<br>3 = `RCM_DRIVER_ORIENTATION_MISMATCH_DEFAULT_LHD`<br>4 = `RCM_DRIVER_ORIENTATION_MISMATCH_DEFAULT_RHD`<br>7 = `SNA` | validated |
| `RCM_occupantClassificationSource` | Indicates whether the occupant classification source is the Right Vehicle Controller (VCRIGHT) or the Occupancy Classification System - 1st Row Passenger (OCS1P). | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCS1P_CLASSIFICATION_SOURCE`<br>1 = `VCRIGHT_CLASSIFICATION_SOURCE` | validated |
| `RCM_pedProEDR1State` | Reports status of the PedPro Event Data Recorder (EDR) memory slot 1. | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_EDR_EMPTY`<br>1 = `RCM_EDR_STORED`<br>2 = `RCM_EDR_LOCKED`<br>3 = `RCM_EDR_UNAVAILABLE` | validated |
| `RCM_pedProEDR2State` | Reports status of the PedPro Event Data Recorder (EDR) memory slot 2. | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `RCM_EDR_EMPTY`<br>1 = `RCM_EDR_STORED`<br>2 = `RCM_EDR_LOCKED`<br>3 = `RCM_EDR_UNAVAILABLE` | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
