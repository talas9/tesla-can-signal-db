---
layout: default
title: "VCSEC_TPMSStatus (0x23A) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Vehicle security controller message: TPMS status. Ethernet-side message VCSEC_TPMSStatus of Vehicle security controller for Tesla Model 3 / Model Y firmware 2025.20.8, 50 signals (VCSEC_TPMSStatusIndex, VCSEC_TPMSSystemState, VCSEC_TPMSSensorMACAddress0, VCSEC_TPMSSensorMACAddress1 and 46 more). Bit layout, scaling, units and value tables."
---

# VCSEC_TPMSStatus (0x23A) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Vehicle security controller message: TPMS status. This page documents the 50 signals of VCSEC_TPMSStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_TPMSStatus` |
| Ethernet-side id | 0x23A (570) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 50 |

## Signals of VCSEC_TPMSStatus

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_TPMSStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_TPMSStatusIndex` | selector | Vehicle security controller: TPMS status index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `MACAddressSensor0`<br>1 = `MACAddressSensor1`<br>2 = `MACAddressSensor2`<br>3 = `MACAddressSensor3`<br>4 = `ConnMetricsSensor0`<br>5 = `ConnMetricsSensor1`<br>6 = `ConnMetricsSensor2`<br>7 = `ConnMetricsSensor3`<br>8 = `CRCSensor0`<br>9 = `CRCSensor1`<br>10 = `CRCSensor2`<br>11 = `CRCSensor3`<br>12 = `CPUTimeSensor0`<br>13 = `CPUTimeSensor1`<br>14 = `CPUTimeSensor2`<br>15 = `CPUTimeSensor3`<br>16 = `SleepStatsSensor0`<br>17 = `SleepStatsSensor1`<br>18 = `SleepStatsSensor2`<br>19 = `SleepStatsSensor3`<br>20 = `ResetCountsSensor0`<br>21 = `ResetCountsContinuedSensor0`<br>22 = `ResetCountsSensor1`<br>23 = `ResetCountsContinuedSensor1`<br>24 = `ResetCountsSensor2`<br>25 = `ResetCountsContinuedSensor2`<br>26 = `ResetCountsSensor3`<br>27 = `ResetCountsContinuedSensor3`<br>28 = `SensorConfiguration` | plausible |
| `VCSEC_TPMSSystemState` |  | High level state the TPMS system is in currently | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_SYSTEM_STATE_IDLE`<br>1 = `TPMS_SYSTEM_STATE_ACTIVE` | plausible |
| `VCSEC_TPMSSensorMACAddress0` | page 0 | Vehicle security controller: TPMS sensor MAC address0 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress1` | page 1 | Vehicle security controller: TPMS sensor MAC address1 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress2` | page 2 | Vehicle security controller: TPMS sensor MAC address2 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_TPMSSensorMACAddress3` | page 3 | Vehicle security controller: TPMS sensor MAC address3 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |
| `VCSEC_BLESuccessfulConnEventCount0` | page 4 | Count of successful BLE connection events | 6\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 |  | plausible |
| `VCSEC_BLEMissedConnEventCount0` | page 4 | Count of missed BLE connection events | 21\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLECRCErrorConnEventCount0` | page 4 | Count of BLE connection events ended with a CRC error | 35\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLEOtherFailuresCount0` | page 4 | Count of other radio related failures | 49\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | plausible |
| `VCSEC_BLEUnsuccessfulConnEventRate0` | page 4 | Vehicle security controller: BLE unsuccessful conn event rate0; raw 1023 = signal not available (SNA) | 54\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | plausible |
| `VCSEC_BLESuccessfulConnEventCount1` | page 5 | Count of successful BLE connection events | 6\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 |  | plausible |
| `VCSEC_BLEMissedConnEventCount1` | page 5 | Count of missed BLE connection events | 21\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLECRCErrorConnEventCount1` | page 5 | Count of BLE connection events ended with a CRC error | 35\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLEOtherFailuresCount1` | page 5 | Count of other radio related failures | 49\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | plausible |
| `VCSEC_BLEUnsuccessfulConnEventRate1` | page 5 | Vehicle security controller: BLE unsuccessful conn event rate1; raw 1023 = signal not available (SNA) | 54\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | plausible |
| `VCSEC_BLESuccessfulConnEventCount2` | page 6 | Count of successful BLE connection events | 6\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 |  | plausible |
| `VCSEC_BLEMissedConnEventCount2` | page 6 | Count of missed BLE connection events | 21\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLECRCErrorConnEventCount2` | page 6 | Count of BLE connection events ended with a CRC error | 35\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLEOtherFailuresCount2` | page 6 | Count of other radio related failures | 49\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | plausible |
| `VCSEC_BLEUnsuccessfulConnEventRate2` | page 6 | Vehicle security controller: BLE unsuccessful conn event rate2; raw 1023 = signal not available (SNA) | 54\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | plausible |
| `VCSEC_BLESuccessfulConnEventCount3` | page 7 | Count of successful BLE connection events | 6\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 |  | plausible |
| `VCSEC_BLEMissedConnEventCount3` | page 7 | Count of missed BLE connection events | 21\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLECRCErrorConnEventCount3` | page 7 | Count of BLE connection events ended with a CRC error | 35\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | plausible |
| `VCSEC_BLEOtherFailuresCount3` | page 7 | Count of other radio related failures | 49\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | plausible |
| `VCSEC_BLEUnsuccessfulConnEventRate3` | page 7 | Vehicle security controller: BLE unsuccessful conn event rate3; raw 1023 = signal not available (SNA) | 54\|10 | little-endian | unsigned | 0.08 | 0 | % | 0 to 81.76 | 1023 = `SNA` | plausible |
| `VCSEC_TPMSSensorTIAppCRC0` | page 8 | Vehicle security controller: TPMS sensor TI app CRC0; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC0` | page 8 | Vehicle security controller: TPMS sensor MLX app CRC0; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC1` | page 9 | Vehicle security controller: TPMS sensor TI app CRC1; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC1` | page 9 | Vehicle security controller: TPMS sensor MLX app CRC1; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC2` | page 10 | Vehicle security controller: TPMS sensor TI app CRC2; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC2` | page 10 | Vehicle security controller: TPMS sensor MLX app CRC2; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorTIAppCRC3` | page 11 | Vehicle security controller: TPMS sensor TI app CRC3; raw 0 = signal not available (SNA) | 8\|32 | little-endian | unsigned | 1 | 0 |  | 1 to 4294967295 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMSSensorMLXAppCRC3` | page 11 | Vehicle security controller: TPMS sensor MLX app CRC3; raw 0 = signal not available (SNA) | 40\|24 | little-endian | unsigned | 1 | 0 |  | 1 to 16777215 | 0 = `TPMS_CRC_SNA` | validated |
| `VCSEC_TPMStotalAwakeTime0` | page 16 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted0` | page 16 | Vehicle security controller: TPMS trim adjusted0 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState0` | page 16 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType0` | page 16 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime1` | page 17 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted1` | page 17 | Vehicle security controller: TPMS trim adjusted1 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState1` | page 17 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType1` | page 17 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime2` | page 18 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted2` | page 18 | Vehicle security controller: TPMS trim adjusted2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState2` | page 18 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType2` | page 18 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |
| `VCSEC_TPMStotalAwakeTime3` | page 19 | Sleep and CPU time count | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_TPMSTrimAdjusted3` | page 19 | Vehicle security controller: TPMS trim adjusted3 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSGenealogySensorState3` | page 19 | TPMS genealogy state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_STATE_WAIT_FOR_CONNECTION`<br>1 = `SENSOR_STATE_SEND_CODE_DESCRIPTOR_REQUEST`<br>2 = `SENSOR_STATE_WAIT_FOR_CODE_DESCRIPTOR_RESPONSE`<br>3 = `SENSOR_STATE_SEND_GENEALOGY_REQUEST`<br>4 = `SENSOR_STATE_WAIT_FOR_GENEALOGY_RESPONSE`<br>5 = `SENSOR_STATE_SEND_CAPABILITIES_REQUEST`<br>6 = `SENSOR_STATE_WAIT_FOR_CAPABILITIES_RESPONSE`<br>7 = `SENSOR_STATE_DONE` | validated |
| `VCSEC_TPMSSensorType3` | page 19 | Tesla TPMS type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_TYPE_NOT_IDENTIFIED`<br>1 = `SENSOR_TYPE_UNKNOWN`<br>2 = `SENSOR_TYPE_V1`<br>3 = `SENSOR_TYPE_V2`<br>4 = `SENSOR_TYPE_V3`<br>5 = `SENSOR_TYPE_V4`<br>6 = `SENSOR_TYPE_V5` | validated |

## Multiplexing

`VCSEC_TPMSStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (5 signals), page 5 (5 signals), page 6 (5 signals), page 7 (5 signals), page 8 (2 signals), page 9 (2 signals), page 10 (2 signals), page 11 (2 signals), page 16 (4 signals), page 17 (4 signals), page 18 (4 signals), page 19 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
