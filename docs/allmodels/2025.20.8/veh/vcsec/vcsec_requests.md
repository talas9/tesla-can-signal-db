---
layout: default
title: "VCSEC_requests (0x1F9) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: requests. Tesla Model 3 / Model Y CAN bus message VCSEC_requests (0x1F9) of Vehicle security controller, firmware 2025.20.8, 19 signals (VCSEC_chargePortRequest, VCSEC_presentHandles, VCSEC_frontLeftClosureRequest, VCSEC_frontRightClosureRequest and 15 more). Bit layout, scaling, units and value tables."
---

# VCSEC_requests (0x1F9) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vehicle security controller message: requests; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of VCSEC_requests as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_requests` |
| CAN id | 0x1F9 (505) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 19 |

## Signals of VCSEC_requests

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_requests`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_chargePortRequest` | Open and close requests of the charge port door; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `REQUEST_NONE`<br>1 = `REQUEST_OPEN`<br>2 = `REQUEST_CLOSE`<br>3 = `REQUEST_SNA` | validated |
| `VCSEC_presentHandles` | VCSEC command to present the handles. Applicable to Model S. | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_frontLeftClosureRequest` | VCSEC command to present the front left door. | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_frontRightClosureRequest` | VCSEC command to present the front right door. | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_rearLeftClosureRequest` | open and close requests of the left rear door. | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_rearRightClosureRequest` | open and close requests of the right rear door. | 14\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_rearTrunkClosureRequest` | VCSEC command to operate the rear trunk. | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_frontLeftRequestReason` | VCSEC reason to present the front left door. | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |
| `VCSEC_frontRightRequestReason` | VCSEC reason to present the front right door. | 23\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |
| `VCSEC_rearLeftRequestReason` | open and close request reason of the left rear door. | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |
| `VCSEC_rearRightRequestReason` | open and close request reason of the right rear door. | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |
| `VCSEC_rearTrunkRequestReason` | VCSEC reason for command to operate the rear trunk. | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |
| `VCSEC_rdMapDumpRequested` | Vehicle security controller: rd map dump requested | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_driveAttemptedWithoutAuth` | Driver is attempting shift into drive wihout a key present | 36\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NO_NFC_POPUP_DESIRED`<br>1 = `SHOW_DEVICE_DISCONNECTED_IOS_CENTER_VARIANT`<br>2 = `SHOW_DEVICE_DISCONNECTED_IOS_BPILLAR_VARIANT`<br>3 = `SHOW_DEVICE_DISCONNECTED_GENERIC_CENTER_VARIANT`<br>4 = `SHOW_DEVICE_DISCONNECTED_GENERIC_BPILLAR_VARIANT`<br>5 = `SHOW_APP_DOWNLOAD_AND_PHONEKEY_PAIR_CENTER_VARIANT`<br>6 = `SHOW_APP_DOWNLOAD_AND_PHONEKEY_PAIR_BPILLAR_VARIANT`<br>7 = `SHOW_BRING_PHONE_CLOSER_CENTER_VARIANT`<br>8 = `SHOW_BRING_PHONE_CLOSER_BPILLAR_VARIANT`<br>9 = `SHOW_CENTER_NFC_CARD_TAP`<br>10 = `SHOW_B_PILLAR_NFC_CARD_TAP` | validated |
| `VCSEC_closeAllStatus` | Vehicle security controller: close all status | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CLOSEALL_STATE_NOT_AVAILABLE`<br>1 = `CLOSEALL_STATE_AVAILABLE`<br>2 = `CLOSEALL_STATE_CANCELABLE` | validated |
| `VCSEC_snapshotRequested` | Vehicle security controller: snapshot requested | 43\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `HANDLE_PULL_WITHOUT_AUTH`<br>2 = `AUTHED_WITHOUT_HANDLE_PULL`<br>3 = `AUTO_PRESENT_DOOR_CLOSE_TIMEOUT`<br>4 = `AUTO_PRESENT_DOOR_CLOSE_WITHOUT_PEDESTRIAN_DETECTED`<br>5 = `UNASSIGNED_5`<br>6 = `UNASSIGNED_6`<br>7 = `AUTO_TRUNK_FALSE_BEEP`<br>8 = `RAW_RSSI_ECU_LOG_HANDLE_PULL`<br>9 = `RSSI_THRESHOLD_ALGO_FALSE_POSITIVE`<br>10 = `RSSI_NN_ALGO_FALSE_POSITIVE`<br>11 = `AUTO_TRUNK`<br>12 = `AUTHENTICATION_REJECTION_DEVICE_STATIONARY`<br>13 = `AUTO_FRUNK`<br>14 = `AUTO_FRUNK_FALSE_BEEP`<br>15 = `EXTERNAL_THERMALS_HIGH` | validated |
| `VCSEC_chargeportRequestReason` | VCSEC reason to open the chargeport door. | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCSEC_CHARGEPORT_REQUEST_REASON_NONE`<br>1 = `VCSEC_CHARGEPORT_REQUEST_REASON_RKE`<br>2 = `VCSEC_CHARGEPORT_REQUEST_REASON_UHF`<br>3 = `VCSEC_CHARGEPORT_REQUEST_REASON_BLE_CHARGE_HANDLE`<br>4 = `VCSEC_CHARGEPORT_REQUEST_REASON_LONG_PULL_DOOR_HANDLE` | validated |
| `VCSEC_frontTrunkClosureRequest` | VCSEC command to operate front trunk. | 51\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_MOVE`<br>2 = `POWERED_CLOSURE_REQUEST_STOP`<br>3 = `POWERED_CLOSURE_REQUEST_OPEN`<br>4 = `POWERED_CLOSURE_REQUEST_QUICK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_OPEN_REDUCED`<br>6 = `POWERED_CLOSURE_REQUEST_CLOSE` | validated |
| `VCSEC_frontTrunkRequestReason` | VCSEC reason to present the front left door. | 54\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERED_CLOSURE_REQUEST_REASON_NONE`<br>1 = `POWERED_CLOSURE_REQUEST_REASON_RKE`<br>2 = `POWERED_CLOSURE_REQUEST_REASON_CLOSE_ALL`<br>3 = `POWERED_CLOSURE_REQUEST_REASON_AUTO_PRESENT`<br>4 = `POWERED_CLOSURE_REQUEST_KEYFOB_UNLOCK_OPEN`<br>5 = `POWERED_CLOSURE_REQUEST_UI_STOP_ALL`<br>6 = `POWERED_CLOSURE_REQUEST_REASON_UI_REQUEST`<br>7 = `POWERED_CLOSURE_REQUEST_TAP_TO_OPEN` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
