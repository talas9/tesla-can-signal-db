---
layout: default
title: "VCSEC_ChildSeatStatus (0x25F) — Vehicle security controller, Tesla Model 3 2025.20.8 VEH CAN"
description: "Vehicle security controller message: child seat status. Tesla Model 3 CAN bus message VCSEC_ChildSeatStatus (0x25F) of Vehicle security controller, firmware 2025.20.8, 21 signals (VCSEC_childSeat0_connectionState, VCSEC_childSeat0_taskDisconnectionReason, VCSEC_childSeat0_state, VCSEC_childSeat0_taskErrorCode and 17 more). Bit layout, scaling, units and value tables."
---

# VCSEC_ChildSeatStatus (0x25F) — Vehicle security controller, Tesla Model 3 2025.20.8 VEH CAN

Vehicle security controller message: child seat status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 21 signals of VCSEC_ChildSeatStatus as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_ChildSeatStatus` |
| CAN id | 0x25F (607) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 21 |

## Signals of VCSEC_ChildSeatStatus

Tesla Model 3 CAN bus signals in `VCSEC_ChildSeatStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_childSeat0_connectionState` | Vehicle security controller: child seat0 connection state | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `WAIT_FOR_ADV`<br>2 = `CONNECTION_REQUEST`<br>3 = `WAIT_FOR_CONNECTION`<br>4 = `CONNECTED`<br>5 = `DISCONNECTING` | plausible |
| `VCSEC_childSeat0_taskDisconnectionReason` | Vehicle security controller: child seat0 task disconnection reason | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `REQUESTED`<br>2 = `BAD_CONNECTION_DROPPED`<br>3 = `CONNECTION_STATE_MISMATCH` | plausible |
| `VCSEC_childSeat0_state` | Vehicle security controller: child seat0 state | 5\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DEVICE_IDLE`<br>1 = `DEVICE_INIT_REQUEST`<br>2 = `DEVICE_INIT_WAIT_FOR_RESPONSE`<br>3 = `DEVICE_INIT_RESPONSE`<br>4 = `DEVICE_SIGNUP_NOTIFICATION`<br>5 = `DEVICE_SIGNUP_NOTIFICATION_WAIT_FOR_RESPONSE`<br>6 = `DEVICE_READ_STATUS`<br>7 = `DEVICE_READ_STATUS_WAIT_FOR_RESPONSE`<br>8 = `DEVICE_READY` | plausible |
| `VCSEC_childSeat0_taskErrorCode` | Vehicle security controller: child seat0 task error code | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INIT_ERROR`<br>2 = `SIGN_UP_NOTIFICATION_ERROR`<br>3 = `READ_STATUS_ERROR`<br>4 = `TIMEOUT` | plausible |
| `VCSEC_childSeat0_RSSI` | Vehicle security controller: child seat0 RSSI; raw 127 = signal not available (SNA) | 12\|8 | little-endian | signed | 1 | 0 |  | -128 to 126 | 127 = `SNA` | plausible |
| `VCSEC_childSeat0_ISOFixStatus` | Vehicle security controller: child seat0 ISO fix status | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_INSTALLED`<br>2 = `INSTALLED` | plausible |
| `VCSEC_childSeat0_buckleStatus` | Vehicle security controller: child seat0 buckle status | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_BUCKLED`<br>2 = `BUCKLED` | plausible |
| `VCSEC_childSeat0_occupancyStatus` | Vehicle security controller: child seat0 occupancy status | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_OCCUPIED`<br>2 = `OCCUPIED` | plausible |
| `VCSEC_childSeat1_connectionState` | Vehicle security controller: child seat1 connection state | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INVALID`<br>1 = `WAIT_FOR_ADV`<br>2 = `CONNECTION_REQUEST`<br>3 = `WAIT_FOR_CONNECTION`<br>4 = `CONNECTED`<br>5 = `DISCONNECTING` | plausible |
| `VCSEC_childSeat1_taskDisconnectionReason` | Vehicle security controller: child seat1 task disconnection reason | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `REQUESTED`<br>2 = `BAD_CONNECTION_DROPPED`<br>3 = `CONNECTION_STATE_MISMATCH` | plausible |
| `VCSEC_childSeat1_state` | Vehicle security controller: child seat1 state | 31\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DEVICE_IDLE`<br>1 = `DEVICE_INIT_REQUEST`<br>2 = `DEVICE_INIT_WAIT_FOR_RESPONSE`<br>3 = `DEVICE_INIT_RESPONSE`<br>4 = `DEVICE_SIGNUP_NOTIFICATION`<br>5 = `DEVICE_SIGNUP_NOTIFICATION_WAIT_FOR_RESPONSE`<br>6 = `DEVICE_READ_STATUS`<br>7 = `DEVICE_READ_STATUS_WAIT_FOR_RESPONSE`<br>8 = `DEVICE_READY` | plausible |
| `VCSEC_childSeat1_taskErrorCode` | Vehicle security controller: child seat1 task error code | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `INIT_ERROR`<br>2 = `SIGN_UP_NOTIFICATION_ERROR`<br>3 = `READ_STATUS_ERROR`<br>4 = `TIMEOUT` | plausible |
| `VCSEC_childSeat1_RSSI` | Vehicle security controller: child seat1 RSSI; raw 127 = signal not available (SNA) | 38\|8 | little-endian | signed | 1 | 0 |  | -128 to 126 | 127 = `SNA` | plausible |
| `VCSEC_childSeat1_ISOFixStatus` | Vehicle security controller: child seat1 ISO fix status | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_INSTALLED`<br>2 = `INSTALLED` | plausible |
| `VCSEC_childSeat1_buckleStatus` | Vehicle security controller: child seat1 buckle status | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_BUCKLED`<br>2 = `BUCKLED` | plausible |
| `VCSEC_childSeat1_occupancyStatus` | Vehicle security controller: child seat1 occupancy status | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INVALID`<br>1 = `NOT_OCCUPIED`<br>2 = `OCCUPIED` | plausible |
| `VCSEC_childPresenceDetectionWarningActive` | Vehicle security controller: child presence detection warning active | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCSEC_childSeatScanStatus` | Vehicle security controller: child seat scan status | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `SCANNING`<br>2 = `TIMEOUT` | plausible |
| `VCSEC_childPresenceDetectionState` | Vehicle security controller: child presence detection state | 55\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_CONFIGURED`<br>1 = `FAULTED`<br>2 = `DEACTIVE`<br>3 = `IDLE`<br>4 = `WAIT_FOR_LOCK`<br>5 = `ARMED`<br>6 = `INITIAL_WARNING`<br>7 = `INTERVENTION`<br>8 = `ESCALATED_WARNING` | plausible |
| `VCSEC_childPresenceDetectionSupportType` | Vehicle security controller: child presence detection support type | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `CN_REG`<br>2 = `EU_REG` | plausible |
| `VCSEC_childPresenceDetectionNotificationEnabled` | Vehicle security controller: child presence detection notification enabled | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
