---
layout: default
title: "VCSEC_additionalAuthInfo (0x2F9) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH"
description: "Vehicle security controller message: additional auth info. Ethernet-side message VCSEC_additionalAuthInfo of Vehicle security controller for Tesla Model Y firmware 2025.20.8, 26 signals (VCSEC_activeKeyDebug, VCSEC_bleChannelDisconnected, VCSEC_bleDisconnectionReason, VCSEC_bleConnetionAttemptWLEntry and 22 more). Bit layout, scaling, units and value tables."
---

# VCSEC_additionalAuthInfo (0x2F9) — Vehicle security controller, Tesla Model Y 2025.20.8 ETH

Vehicle security controller message: additional auth info. This page documents the 26 signals of VCSEC_additionalAuthInfo as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_additionalAuthInfo` |
| Ethernet-side id | 0x2F9 (761) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 26 |

## Signals of VCSEC_additionalAuthInfo

Tesla Model Y CAN bus signals in `VCSEC_additionalAuthInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_activeKeyDebug` |  | Vehicle security controller: active key debug | 2\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_bleChannelDisconnected` |  | Connection between vehicle and the BLE authentication device is interrupted. | 7\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `VCSEC_bleDisconnectionReason` |  | Reasons of the disconnection between vehicle and BLE authentication device. | 11\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `UNKNOWN_REASON_0`<br>5 = `AUTHENTICATION_FAILURE`<br>8 = `CONNECTION_SUPERVISION_TIMEOUT`<br>19 = `REMOTE_USER_TERMINATED`<br>20 = `REMOTE_DEVICE_LOW_RESOURCES`<br>21 = `REMOTE_DEVICE_POWER_OFF`<br>22 = `HOST_REQUESTED_TERMINATION`<br>26 = `UNSUPPORTED_REMOTE_FEATURE`<br>34 = `CONTROL_PACKET_TIMEOUT`<br>40 = `CONTROL_PACKET_INSTANT_PASSED`<br>41 = `KEY_PAIRING_NOT_SUPPORTED`<br>59 = `UNACCEPTABLE_CONNECTION_INTERVAL`<br>61 = `MIC_FAILURE`<br>62 = `CONNECTION_FAILED_TO_ESTABLISH`<br>255 = `UNKNOWN_REASON_FF` | plausible |
| `VCSEC_bleConnetionAttemptWLEntry` |  | Vehicle security controller: ble connetion attempt WL entry | 19\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_AdditionalAuthInfoIndex` | selector | Vehicle security controller: additional auth info index | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ACTIVE_KEY_SHA1`<br>1 = `KEY_WITH_IN_SUMMON_RANGE_0`<br>2 = `KEY_WITH_IN_SUMMON_RANGE_1`<br>3 = `KEY_WITH_IN_SUMMON_RANGE_2`<br>4 = `UNKNOWN_BLE_DEVICE_WITH_IN_SUMMON_RANGE`<br>5 = `WALKUP_UNLOCK_BEHAVIOR` | plausible |
| `VCSEC_unsecureNotificationStatus` |  | Vehicle security controller: unsecure notification status | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `NOTIFY_DOOR_OPEN`<br>2 = `INHIBITED` | plausible |
| `VCSEC_activeKeyReason` | page 0 | Reason for picking the currently active key | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ACTIVE_KEY_SELECTION_REASON_NONE`<br>1 = `ACTIVE_KEY_SELECTION_REASON_NFC_AUTH`<br>2 = `ACTIVE_KEY_SELECTION_REASON_RKE_AUTH`<br>3 = `ACTIVE_KEY_SELECTION_REASON_BLE_DEVICE_CLOSEST_TO_DOOR`<br>4 = `ACTIVE_KEY_SELECTION_REASON_RKE_ACTION`<br>5 = `ACTIVE_KEY_SELECTION_REASON_ONLY_AUTHED_DEVICE`<br>6 = `ACTIVE_KEY_SELECTION_REASON_AUTO_PRESENT_DOOR_COMMAND`<br>7 = `ACTIVE_KEY_SELECTION_REASON_UWB_DEVICE_CLOSEST_TO_DOOR` | plausible |
| `VCSEC_activeKeySHA1` | page 0 | Vehicle security controller: active key SHA1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_algoUsedForSummonRange0` | page 1 | Vehicle security controller: algo used for summon range0 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | plausible |
| `VCSEC_keyWithinSummonRange0` | page 1 | Vehicle security controller: key within summon range0 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_algoUsedForSummonRange1` | page 2 | Vehicle security controller: algo used for summon range1 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | plausible |
| `VCSEC_keyWithinSummonRange1` | page 2 | Vehicle security controller: key within summon range1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_algoUsedForSummonRange2` | page 3 | Vehicle security controller: algo used for summon range2 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | plausible |
| `VCSEC_keyWithinSummonRange2` | page 3 | Vehicle security controller: key within summon range2 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_BLEDeviceWithinSummonRange` | page 4 | Vehicle security controller: BLE device within summon range | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_WalkupUnlockMitigationKeyIndex0` | page 5 | Vehicle security controller: walkup unlock mitigation key index0 | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_WalkupUnlockMitigationKeyIndex1` | page 5 | Vehicle security controller: walkup unlock mitigation key index1 | 37\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_WalkupUnlockMitigationKeyIndex2` | page 5 | Vehicle security controller: walkup unlock mitigation key index2 | 42\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | layout-only |
| `VCSEC_WalkupUnlockMitigationDesire0` | page 5 | Vehicle security controller: walkup unlock mitigation desire0 | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `OFF`<br>2 = `ON` | plausible |
| `VCSEC_WalkupUnlockMitigationReason0` | page 5 | Vehicle security controller: walkup unlock mitigation reason0 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CONTROL_REASON_NONE`<br>1 = `REASON_DISABLE_FOR_FREQUENT_FALSE_UNLOCKS` | plausible |
| `VCSEC_WalkupUnlockMitigationDesire1` | page 5 | Vehicle security controller: walkup unlock mitigation desire1 | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `OFF`<br>2 = `ON` | plausible |
| `VCSEC_WalkupUnlockMitigationReason1` | page 5 | Vehicle security controller: walkup unlock mitigation reason1 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CONTROL_REASON_NONE`<br>1 = `REASON_DISABLE_FOR_FREQUENT_FALSE_UNLOCKS` | plausible |
| `VCSEC_WalkupUnlockMitigationDesire2` | page 5 | Vehicle security controller: walkup unlock mitigation desire2 | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `OFF`<br>2 = `ON` | plausible |
| `VCSEC_WalkupUnlockMitigationReason2` | page 5 | Vehicle security controller: walkup unlock mitigation reason2 | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CONTROL_REASON_NONE`<br>1 = `REASON_DISABLE_FOR_FREQUENT_FALSE_UNLOCKS` | plausible |
| `VCSEC_NFCAuthFromBPillarFormFactor` | page 5 | Reports the form factor authentication at B-pillar Near Field Communication (NFC) reader. | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `KEY_FORM_FACTOR_COARSE_NONE`<br>1 = `KEY_FORM_FACTOR_COARSE_NFC_CARD`<br>2 = `KEY_FORM_FACTOR_COARSE_KEYFOB`<br>3 = `KEY_FORM_FACTOR_COARSE_ANDROID`<br>4 = `KEY_FORM_FACTOR_COARSE_UNKNOWN` | plausible |
| `VCSEC_NFCAuthFromCenterConsoleFormFactor` | page 5 | Reports the form factor authenticating at center console Near Field Communication (NFC) reader. | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `KEY_FORM_FACTOR_COARSE_NONE`<br>1 = `KEY_FORM_FACTOR_COARSE_NFC_CARD`<br>2 = `KEY_FORM_FACTOR_COARSE_KEYFOB`<br>3 = `KEY_FORM_FACTOR_COARSE_ANDROID`<br>4 = `KEY_FORM_FACTOR_COARSE_UNKNOWN` | plausible |

## Multiplexing

`VCSEC_AdditionalAuthInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (2 signals), page 1 (2 signals), page 2 (2 signals), page 3 (2 signals), page 4 (1 signals), page 5 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
