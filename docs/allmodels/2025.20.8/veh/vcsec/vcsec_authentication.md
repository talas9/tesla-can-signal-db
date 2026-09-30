---
layout: default
title: "VCSEC_authentication (0x339) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: authentication. Tesla Model 3 / Model Y CAN bus message VCSEC_authentication (0x339) of Vehicle security controller, firmware 2025.20.8, 30 signals (VCSEC_BLEConnectionCounter, VCSEC_authRejectionReason, VCSEC_IDRequested, VCSEC_operationMode and 26 more). Bit layout, scaling, units and value tables."
---

# VCSEC_authentication (0x339) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vehicle security controller message: authentication; frame length from the layout, not yet observed on a vehicle bus. This page documents the 30 signals of VCSEC_authentication as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_authentication` |
| CAN id | 0x339 (825) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 30 |

## Signals of VCSEC_authentication

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_authentication`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_BLEConnectionCounter` | The number of devices connected to the host Bluetooth endpoint. | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCSEC_authRejectionReason` | Reason it was rejected | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTHENTICATIONREJECTION_NONE`<br>1 = `AUTHENTICATIONREJECTION_DEVICE_STATIONARY`<br>2 = `AUTHENTICATIONREJECTION_PASSIVE_DISABLED`<br>3 = `AUTHENTICATIONREJECTION_NO_TOKEN`<br>4 = `AUTHENTICATIONREJECTION_PASSIVE_DISABLED_AUTOMATION`<br>5 = `AUTHENTICATIONREJECTION_DEVICE_NOT_UNLOCKED_ON_WRIST` | validated |
| `VCSEC_IDRequested` | Vehicle security controller: ID requested | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_operationMode` | Reports the operation mode of the vehicle. | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OPERATION_MODE_UNKNOWN`<br>1 = `OPERATION_MODE_OWNER`<br>2 = `OPERATION_MODE_FLEET` | validated |
| `VCSEC_vehicleLockStatus` | Lock status of the vehicle; raw 0 = signal not available (SNA) | 12\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `LOCK_STATUS_SNA`<br>1 = `LOCK_STATUS_ACTIVE_NFC_UNLOCKED`<br>2 = `LOCK_STATUS_ACTIVE_NFC_LOCKED`<br>3 = `LOCK_STATUS_PASSIVE_SELECTIVE_UNLOCKED`<br>4 = `LOCK_STATUS_PASSIVE_BLE_UNLOCKED`<br>5 = `LOCK_STATUS_PASSIVE_BLE_LOCKED`<br>6 = `LOCK_STATUS_ACTIVE_SELECTIVE_UNLOCKED`<br>7 = `LOCK_STATUS_ACTIVE_BLE_UNLOCKED`<br>8 = `LOCK_STATUS_ACTIVE_BLE_LOCKED`<br>9 = `LOCK_STATUS_ACTIVE_UI_UNLOCKED`<br>10 = `LOCK_STATUS_ACTIVE_UI_LOCKED`<br>11 = `LOCK_STATUS_ACTIVE_REMOTE_UNLOCKED`<br>12 = `LOCK_STATUS_ACTIVE_REMOTE_LOCKED`<br>13 = `LOCK_STATUS_CRASH_UNLOCKED`<br>14 = `LOCK_STATUS_PASSIVE_INTERNAL_UNLOCKED`<br>15 = `LOCK_STATUS_PASSIVE_INTERNAL_LOCKED` | validated |
| `VCSEC_authenticationStatus` | Reports the vehicle authentication status. | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTHENTICATION_NONE`<br>1 = `AUTHENTICATION_AUTHENTICATED_FOR_UNLOCK`<br>2 = `AUTHENTICATION_AUTHENTICATED_FOR_DRIVE` | validated |
| `VCSEC_chargePortLockStatus` | Lock status of the charge port. | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_leftFrontLockStatus` | Lock status of the left front door. | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_leftRearLockStatus` | Lock status of the left rear door. | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_rightFrontLockStatus` | Lock status of the right front door. | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_rightRearLockStatus` | Lock status of right rear door. | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_trunkLockStatus` | Lock status of the trunk. | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_lockRequestType` | Reports the type of lock and unlock request received. | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `LOCK_REQUEST_NONE`<br>1 = `LOCK_REQUEST_PASSIVE_SHIFT_TO_P_UNLOCK`<br>2 = `LOCK_REQUEST_PASSIVE_PARKBUTTON_UNLOCK`<br>3 = `LOCK_REQUEST_PASSIVE_INTERNAL_HANDLE_UNLOCK`<br>4 = `LOCK_REQUEST_PASSIVE_DRIVE_AWAY_LOCK`<br>5 = `LOCK_REQUEST_PASSIVE_BLE_WALKUP_UNLOCK`<br>6 = `LOCK_REQUEST_PASSIVE_BLE_EXTERIOR_CHARGEHANDLEBUTTON_UNLOCK`<br>7 = `LOCK_REQUEST_PASSIVE_BLE_EXTERIOR_HANDLE_UNLOCK`<br>8 = `LOCK_REQUEST_PASSIVE_BLE_INTERIOR_HANDLE_UNLOCK`<br>9 = `LOCK_REQUEST_PASSIVE_BLE_LOCK`<br>10 = `LOCK_REQUEST_CRASH_UNLOCK`<br>11 = `LOCK_REQUEST_ACTIVE_UI_BUTTON_UNLOCK`<br>12 = `LOCK_REQUEST_ACTIVE_UI_BUTTON_LOCK`<br>13 = `LOCK_REQUEST_ACTIVE_REMOTE_UNLOCK`<br>14 = `LOCK_REQUEST_ACTIVE_REMOTE_LOCK`<br>15 = `LOCK_REQUEST_ACTIVE_NFC_UNLOCK`<br>16 = `LOCK_REQUEST_ACTIVE_NFC_LOCK`<br>17 = `LOCK_REQUEST_ACTIVE_BLE_UNLOCK`<br>18 = `LOCK_REQUEST_ACTIVE_BLE_LOCK`<br>19 = `LOCK_REQUEST_PASSIVE_INTERNAL_LOCK_PROMOTION`<br>20 = `LOCK_REQUEST_PASSIVE_AUTO_PRESENT_DOOR_REQUEST`<br>21 = `LOCK_REQUEST_KEYFOB_OPEN_DOOR_REQUEST` | validated |
| `VCSEC_summonRequest` | Reports the Summon request state; raw 5 = signal not available (SNA) | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SUMMON_REQUEST_IDLE`<br>1 = `SUMMON_REQUEST_PRIME`<br>2 = `SUMMON_REQUEST_FORWARD`<br>3 = `SUMMON_REQUEST_BACKWARD`<br>4 = `SUMMON_REQUEST_STOP`<br>5 = `SUMMON_REQUEST_SNA` | validated |
| `VCSEC_3rdPartyPLGRequest` | Vehicle security controller: 3rd party PLG request; raw 3 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CLOSURE_REQUEST_NONE`<br>1 = `CLOSURE_REQUEST_MOVE`<br>2 = `CLOSURE_REQUEST_STOP`<br>3 = `CLOSURE_REQUEST_SNA` | validated |
| `VCSEC_3rdPartyFrunkPLGRequest` | Vehicle security controller: 3rd party frunk PLG request; raw 3 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CLOSURE_REQUEST_NONE`<br>1 = `CLOSURE_REQUEST_MOVE`<br>2 = `CLOSURE_REQUEST_STOP`<br>3 = `CLOSURE_REQUEST_SNA` | validated |
| `VCSEC_MCUCommandType` | Vehicle security controller: MCU command type | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MCU_COMMAND_NONE`<br>1 = `MCU_COMMAND_REMOTE_UNLOCK`<br>2 = `MCU_COMMAND_REMOTE_START`<br>3 = `MCU_COMMAND_COMMAND3`<br>4 = `MCU_COMMAND_COMMAND4`<br>5 = `MCU_COMMAND_COMMAND5` | validated |
| `VCSEC_frunkLockStatus` | Lock status of the frunk | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLOSURE_UNLOCKED`<br>1 = `CLOSURE_LOCKED` | validated |
| `VCSEC_usingModifiedMACAddress` | Vehicle security controller: using modified MAC address | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_isKeyWithinSummonRange` | Key is within the range of the car where summon can be enabled | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_isBLEDeviceWithinSummonRange` | Indicates whether a Bluetooth Low Energy (BLE) device is within the range where Summon can be enabled. | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_alarmStatus` | Reports the vehicle alarm status; raw 15 = signal not available (SNA) | 43\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `ALARM_STATUS_DISARMED`<br>1 = `ALARM_STATUS_ARMED`<br>2 = `ALARM_STATUS_PARTIAL_ARMED`<br>3 = `ALARM_STATUS_TRIGGERED_FLASH_ACTIVE`<br>4 = `ALARM_STATUS_ERROR`<br>5 = `ALARM_STATUS_TRIGGERED_FLASH_INACTIVE`<br>6 = `ALARM_STATUS_IMMINENT`<br>7 = `ALARM_STATUS_DEFAULT`<br>15 = `ALARM_STATUS_SNA` | validated |
| `VCSEC_serviceDiagnosticRequest` | Vehicle security controller: service diagnostic request | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_immobilizerState` | State of the immobilizer. | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `IMMOBILIZER_STATE_IDLE`<br>1 = `IMMOBILIZER_STATE_PREPARE`<br>2 = `IMMOBILIZER_STATE_ENCRYPT_BEGIN`<br>3 = `IMMOBILIZER_STATE_ENCRYPT`<br>4 = `IMMOBILIZER_STATE_SEND_AUTH_RESPONSE`<br>5 = `IMMOBILIZER_STATE_SEND_NO_GO_AUTH_RESPONSE`<br>6 = `IMMOBILIZER_STATE_IMMOBILIZED` | validated |
| `VCSEC_lockIndicationRequest` | Requests to turn on vehicle turn indicators based on lock and unlock states; raw 0 = signal not available (SNA) | 51\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `INDICATION_NONE_SNA`<br>1 = `INDICATION_SINGLE`<br>2 = `INDICATION_DOUBLE`<br>3 = `INDICATION_TRIPLE`<br>4 = `INDICATION_HOLD` | validated |
| `VCSEC_simpleLockStatus` | Vehicle lock status with simplfied two states: lock and unlock; raw 0 = signal not available (SNA) | 54\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SIMPLE_LOCK_STATUS_SNA`<br>1 = `SIMPLE_LOCK_STATUS_UNLOCKED`<br>2 = `SIMPLE_LOCK_STATUS_LOCKED` | validated |
| `VCSEC_keyChannelIndexed` | Vehicle security controller: key channel indexed; raw 15 = signal not available (SNA) | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 15 = `SNA` | validated |
| `VCSEC_authRequested` | An authentication request was sent from the security controller to the authentication device. | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_remoteStartActive` | Indicates when a remote start request terminated by the Vehicle Security Controller (VCSEC) is active. | 61\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCSEC_REMOTE_START_TYPE_NONE`<br>1 = `VCSEC_REMOTE_START_TYPE_LEGACY`<br>2 = `VCSEC_REMOTE_START_TYPE_SIGNED_COMMAND`<br>3 = `VCSEC_REMOTE_START_TYPE_SIGNED_COMMAND_PIN_REQUIRED` | validated |
| `VCSEC_keyPairDesired` | Vehicle security controller: key pair desired | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
