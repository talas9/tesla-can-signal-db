---
layout: default
title: "VCSEC_TPMSStatus (0x23A) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: TPMS status. Tesla Model 3 / Model Y CAN bus message VCSEC_TPMSStatus (0x23A) of Vehicle security controller, firmware 2026.26.6.5, 50 signals (VCSEC_TPMSStatusIndex, VCSEC_TPMSSystemState, VCSEC_TPMSSensorMACAddress0, VCSEC_TPMSSensorMACAddress1 and 46 more). Bit layout, scaling, units and value tables."
---

# VCSEC_TPMSStatus (0x23A) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Vehicle security controller message: TPMS status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 50 signals of VCSEC_TPMSStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_TPMSStatus` |
| CAN id | 0x23A (570) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 50 |

## Signals of VCSEC_TPMSStatus

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_TPMSStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_TPMSStatusIndex` | selector | Vehicle security controller: TPMS status index | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `MACAddressSensor0`<br>1 = `MACAddressSensor1`<br>2 = `MACAddressSensor2`<br>3 = `MACAddressSensor3`<br>4 = `ConnMetricsSensor0`<br>5 = `ConnMetricsContinuedSensor0`<br>6 = `ConnMetricsSensor1`<br>7 = `ConnMetricsContinuedSensor1`<br>8 = `ConnMetricsSensor2`<br>9 = `ConnMetricsContinuedSensor2`<br>10 = `ConnMetricsSensor3`<br>11 = `ConnMetricsContinuedSensor3`<br>12 = `CRCSensor0`<br>13 = `CRCSensor1`<br>14 = `CRCSensor2`<br>15 = `CRCSensor3`<br>16 = `CPUTimeSensor0`<br>17 = `CPUTimeSensor1`<br>18 = `CPUTimeSensor2`<br>19 = `CPUTimeSensor3`<br>20 = `SleepStatsSensor0`<br>21 = `SleepStatsSensor1`<br>22 = `SleepStatsSensor2`<br>23 = `SleepStatsSensor3`<br>24 = `ResetCountsSensor0`<br>25 = `ResetCountsContinuedSensor0`<br>26 = `ResetCountsSensor1`<br>27 = `ResetCountsContinuedSensor1`<br>28 = `ResetCountsSensor2`<br>29 = `ResetCountsContinuedSensor2`<br>30 = `ResetCountsSensor3`<br>31 = `ResetCountsContinuedSensor3`<br>32 = `SensorConfiguration`<br>33 = `SensorHashInfo1`<br>34 = `SensorHashInfo2`<br>35 = `LastLocationInfo`<br>36 = `SensorTemperatureCompensatedVoltageInfo`<br>37 = `SensorFilteredVoltageInfo`<br>38 = `TireMileage`<br>39 = `TireMileageContinued` | validated |
| `VCSEC_TPMSSystemState` |  | High level state the TPMS system is in currently | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_SYSTEM_STATE_IDLE`<br>1 = `TPMS_SYSTEM_STATE_ACTIVE` | validated |
| `VCSEC_TPMSSensorMACAddress0` | page 0 | Vehicle security controller: TPMS sensor MAC address0 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress1` | page 1 | Vehicle security controller: TPMS sensor MAC address1 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress2` | page 2 | Vehicle security controller: TPMS sensor MAC address2 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress3` | page 3 | Vehicle security controller: TPMS sensor MAC address3 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_BLEUnsuccessfulConnEventRate0` | page 5 | Vehicle security controller: BLE unsuccessful conn event rate0; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | validated |
| `VCSEC_BLEUnsuccessfulConnEventRate1` | page 7 | Vehicle security controller: BLE unsuccessful conn event rate1; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | validated |
| `VCSEC_BLEUnsuccessfulConnEventRate2` | page 9 | Vehicle security controller: BLE unsuccessful conn event rate2; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | validated |
| `VCSEC_BLEUnsuccessfulConnEventRate3` | page 11 | Vehicle security controller: BLE unsuccessful conn event rate3; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC0` | page 12 | Vehicle security controller: TPMS sensor TI app CRC0; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC0` | page 12 | Vehicle security controller: TPMS sensor MLX app CRC0; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC1` | page 13 | Vehicle security controller: TPMS sensor TI app CRC1; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC1` | page 13 | Vehicle security controller: TPMS sensor MLX app CRC1; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC2` | page 14 | Vehicle security controller: TPMS sensor TI app CRC2; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC2` | page 14 | Vehicle security controller: TPMS sensor MLX app CRC2; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC3` | page 15 | Vehicle security controller: TPMS sensor TI app CRC3; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC3` | page 15 | Vehicle security controller: TPMS sensor MLX app CRC3; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMStotalAwakeTime0` | page 20 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted0` | page 20 | Vehicle security controller: TPMS trim adjusted0 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState0` | page 20 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType0` | page 20 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime1` | page 21 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted1` | page 21 | Vehicle security controller: TPMS trim adjusted1 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState1` | page 21 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType1` | page 21 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime2` | page 22 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted2` | page 22 | Vehicle security controller: TPMS trim adjusted2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState2` | page 22 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType2` | page 22 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime3` | page 23 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted3` | page 23 | Vehicle security controller: TPMS trim adjusted3 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState3` | page 23 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType3` | page 23 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMSSensor0Hash` | page 33 | Vehicle security controller: TPMS sensor0 hash | 8\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | validated |
| `VCSEC_TPMSSensor1Hash` | page 33 | Vehicle security controller: TPMS sensor1 hash | 36\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | validated |
| `VCSEC_TPMSSensor2Hash` | page 34 | Vehicle security controller: TPMS sensor2 hash | 8\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | validated |
| `VCSEC_TPMSSensor3Hash` | page 34 | Vehicle security controller: TPMS sensor3 hash | 36\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | validated |
| `VCSEC_TPMSLastLocationSensor0` | page 35 | Indicates the localization result | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSLastLocationSensor1` | page 35 | Indicates the localization result | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSLastLocationSensor2` | page 35 | Indicates the localization result | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSLastLocationSensor3` | page 35 | Indicates the localization result | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSTemperatureCompensatedBatVoltage0` | page 36 | Sensor battery voltage; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSTemperatureCompensatedBatVoltage1` | page 36 | Sensor battery voltage; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSTemperatureCompensatedBatVoltage2` | page 36 | Sensor battery voltage; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSTemperatureCompensatedBatVoltage3` | page 36 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSFilteredBatVoltage0` | page 37 | Sensor battery voltage; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSFilteredBatVoltage2` | page 37 | Sensor battery voltage; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSFilteredBatVoltage1` | page 37 | Sensor battery voltage; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSFilteredBatVoltage3` | page 37 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |

## Multiplexing

`VCSEC_TPMSStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 5 (1 signals), page 7 (1 signals), page 9 (1 signals), page 11 (1 signals), page 12 (2 signals), page 13 (2 signals), page 14 (2 signals), page 15 (2 signals), page 20 (4 signals), page 21 (4 signals), page 22 (4 signals), page 23 (4 signals), page 33 (2 signals), page 34 (2 signals), page 35 (4 signals), page 36 (4 signals), page 37 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
