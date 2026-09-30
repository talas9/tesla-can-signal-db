---
layout: default
title: "VCSEC_additionalAuthInfo (0x2F9) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: additional auth info. Tesla Model 3 / Model Y CAN bus message VCSEC_additionalAuthInfo (0x2F9) of Vehicle security controller, firmware 2026.26.6.5, 25 signals (VCSEC_activeKeyDebug, VCSEC_bleChannelDisconnected, VCSEC_bleDisconnectionReason, VCSEC_bleConnetionAttemptWLEntry and 21 more). Bit layout, scaling, units and value tables."
---

# VCSEC_additionalAuthInfo (0x2F9) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Vehicle security controller message: additional auth info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 25 signals of VCSEC_additionalAuthInfo as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_additionalAuthInfo` |
| CAN id | 0x2F9 (761) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 25 |

## Signals of VCSEC_additionalAuthInfo

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_additionalAuthInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_activeKeyDebug` |  | Vehicle security controller: active key debug | 2\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_bleChannelDisconnected` |  | Connection between vehicle and the BLE authentication device is interrupted. | 7\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCSEC_bleDisconnectionReason` |  | Reasons of the disconnection between vehicle and BLE authentication device. | 11\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `UNKNOWN_REASON_0`<br>5 = `AUTHENTICATION_FAILURE`<br>8 = `CONNECTION_SUPERVISION_TIMEOUT`<br>19 = `REMOTE_USER_TERMINATED`<br>20 = `REMOTE_DEVICE_LOW_RESOURCES`<br>21 = `REMOTE_DEVICE_POWER_OFF`<br>22 = `HOST_REQUESTED_TERMINATION`<br>26 = `UNSUPPORTED_REMOTE_FEATURE`<br>34 = `CONTROL_PACKET_TIMEOUT`<br>40 = `CONTROL_PACKET_INSTANT_PASSED`<br>41 = `KEY_PAIRING_NOT_SUPPORTED`<br>59 = `UNACCEPTABLE_CONNECTION_INTERVAL`<br>61 = `MIC_FAILURE`<br>62 = `CONNECTION_FAILED_TO_ESTABLISH`<br>255 = `UNKNOWN_REASON_FF` | validated |
| `VCSEC_bleConnetionAttemptWLEntry` |  | Vehicle security controller: ble connetion attempt WL entry | 19\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_AdditionalAuthInfoIndex` | selector | Vehicle security controller: additional auth info index | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ACTIVE_KEY_SHA1`<br>1 = `KEY_WITH_IN_SUMMON_RANGE_0`<br>2 = `KEY_WITH_IN_SUMMON_RANGE_1`<br>3 = `KEY_WITH_IN_SUMMON_RANGE_2`<br>4 = `UNKNOWN_BLE_DEVICE_WITH_IN_SUMMON_RANGE`<br>5 = `WALKUP_UNLOCK_BEHAVIOR` | plausible |
| `VCSEC_activeKeyReason` | page 0 | Reason for picking the currently active key | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ACTIVE_KEY_SELECTION_REASON_NONE`<br>1 = `ACTIVE_KEY_SELECTION_REASON_NFC_AUTH`<br>2 = `ACTIVE_KEY_SELECTION_REASON_RKE_AUTH`<br>3 = `ACTIVE_KEY_SELECTION_REASON_BLE_DEVICE_CLOSEST_TO_DOOR`<br>4 = `ACTIVE_KEY_SELECTION_REASON_RKE_ACTION`<br>5 = `ACTIVE_KEY_SELECTION_REASON_ONLY_AUTHED_DEVICE`<br>6 = `ACTIVE_KEY_SELECTION_REASON_AUTO_PRESENT_DOOR_COMMAND`<br>7 = `ACTIVE_KEY_SELECTION_REASON_UWB_DEVICE_CLOSEST_TO_DOOR` | validated |
| `VCSEC_activeKeySHA1` | page 0 | Vehicle security controller: active key SHA1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_algoUsedForSummonRange0` | page 1 | Vehicle security controller: algo used for summon range0 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | validated |
| `VCSEC_keyWithinSummonRange0` | page 1 | Vehicle security controller: key within summon range0 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_algoUsedForSummonRange1` | page 2 | Vehicle security controller: algo used for summon range1 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | validated |
| `VCSEC_keyWithinSummonRange1` | page 2 | Vehicle security controller: key within summon range1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_algoUsedForSummonRange2` | page 3 | Vehicle security controller: algo used for summon range2 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SUMMON_RANGE_ALGO_USED_BLE`<br>1 = `SUMMON_RANGE_ALGO_USED_UWB` | validated |
| `VCSEC_keyWithinSummonRange2` | page 3 | Vehicle security controller: key within summon range2 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLEDeviceWithinSummonRange` | page 4 | Vehicle security controller: BLE device within summon range | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_algoUWBInteriorPresence` | page 5 | Vehicle security controller: algo UWB interior presence | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_frunkOpenSuggestionResponse` | page 5 | Vehicle security controller: frunk open suggestion response | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SUGGESTIONS_RESPONSE_UNKNOWN`<br>1 = `SUGGESTIONS_RESPONSE_ACCEPTED_BY_USER`<br>2 = `SUGGESTIONS_RESPONSE_REJECTED_BY_USER`<br>3 = `SUGGESTIONS_RESPONSE_CLEARED_BY_USER`<br>4 = `SUGGESTIONS_RESPONSE_TIMEOUT_CLEARED`<br>5 = `SUGGESTIONS_RESPONSE_FAIL_TO_SETUP`<br>6 = `SUGGESTIONS_RESPONSE_CLOSURE_SUGGESTION_DISABLED` | validated |
| `VCSEC_NFCAuthFromBPillarFormFactor` | page 5 | Reports the form factor authentication at B-pillar Near Field Communication (NFC) reader. | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `KEY_FORM_FACTOR_COARSE_NONE`<br>1 = `KEY_FORM_FACTOR_COARSE_NFC_CARD`<br>2 = `KEY_FORM_FACTOR_COARSE_KEYFOB`<br>3 = `KEY_FORM_FACTOR_COARSE_ANDROID`<br>4 = `KEY_FORM_FACTOR_COARSE_UNKNOWN` | validated |
| `VCSEC_NFCAuthFromCenterConsoleFormFactor` | page 5 | Reports the form factor authenticating at center console Near Field Communication (NFC) reader. | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `KEY_FORM_FACTOR_COARSE_NONE`<br>1 = `KEY_FORM_FACTOR_COARSE_NFC_CARD`<br>2 = `KEY_FORM_FACTOR_COARSE_KEYFOB`<br>3 = `KEY_FORM_FACTOR_COARSE_ANDROID`<br>4 = `KEY_FORM_FACTOR_COARSE_UNKNOWN` | validated |
| `VCSEC_trunkOpenSuggestionResponse` | page 5 | Vehicle security controller: trunk open suggestion response | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SUGGESTIONS_RESPONSE_UNKNOWN`<br>1 = `SUGGESTIONS_RESPONSE_ACCEPTED_BY_USER`<br>2 = `SUGGESTIONS_RESPONSE_REJECTED_BY_USER`<br>3 = `SUGGESTIONS_RESPONSE_CLEARED_BY_USER`<br>4 = `SUGGESTIONS_RESPONSE_TIMEOUT_CLEARED`<br>5 = `SUGGESTIONS_RESPONSE_FAIL_TO_SETUP`<br>6 = `SUGGESTIONS_RESPONSE_CLOSURE_SUGGESTION_DISABLED` | validated |
| `VCSEC_algoTrunkSuggestionRaw` | page 5 | Vehicle security controller: algo trunk suggestion raw | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoTrunkSuggestionProc` | page 5 | Vehicle security controller: algo trunk suggestion proc | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoTrunkSuggestionRearmAllowed` | page 5 | Vehicle security controller: algo trunk suggestion rearm allowed | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoFrunkSuggestionRaw` | page 5 | Vehicle security controller: algo frunk suggestion raw | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoFrunkSuggestionProc` | page 5 | Vehicle security controller: algo frunk suggestion proc | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoFrunkSuggestionRearmAllowed` | page 5 | Vehicle security controller: algo frunk suggestion rearm allowed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCSEC_AdditionalAuthInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (2 signals), page 1 (2 signals), page 2 (2 signals), page 3 (2 signals), page 4 (1 signals), page 5 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
