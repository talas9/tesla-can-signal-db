---
layout: default
title: "OCS1P_status (0x303) — Occupant classification system, Tesla Model Y 2025.20.8 ETH"
description: "Occupant classification system message: status. Ethernet-side message OCS1P_status of Occupant classification system for Tesla Model Y firmware 2025.20.8, 25 signals (OCS1P_occupantClassification, OCS1P_occupantClassificationQF, OCS1P_occupiedState, OCS1P_triggerSnapshot and 21 more). Bit layout, scaling, units and value tables."
---

# OCS1P_status (0x303) — Occupant classification system, Tesla Model Y 2025.20.8 ETH

Occupant classification system message: status. This page documents the 25 signals of OCS1P_status as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `OCS1P_status` |
| Ethernet-side id | 0x303 (771) |
| ECU | [Occupant classification system](../../ocs1p.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | OCS1P |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 25 |

## Signals of OCS1P_status

Tesla Model Y CAN bus signals in `OCS1P_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `OCS1P_occupantClassification` | Occupant Classification (Filtered); raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 0 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>1 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>2 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_SMALL`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_LARGE`<br>4 = `OCCUPANT_CLASSIFICATION_INIT`<br>255 = `OCCUPANT_CLASSIFICATION_SNA` | validated |
| `OCS1P_occupantClassificationQF` | Occupant classification system: occupant classification QF | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCCUPANT_CLASSIFICATION_FAULTED`<br>1 = `OCCUPANT_CLASSIFICATION_NOT_FAULTED` | validated |
| `OCS1P_occupiedState` | Passenger seat occupied State; raw 3 = signal not available (SNA) | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OCCUPIED_STATE_UNOCCUPIED`<br>1 = `OCCUPIED_STATE_OCCUPIED`<br>3 = `OCCUPIED_STATE_SNA` | validated |
| `OCS1P_triggerSnapshot` | Occupant classification system: trigger snapshot | 11\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `REASON_NONE`<br>1 = `REASON_MISMATCH`<br>2 = `REASON_REBASELINED`<br>3 = `REASON_SANDWICH_LOW`<br>4 = `REASON_SENSOR_OPEN`<br>5 = `REASON_SENSOR_LOW_SHORT`<br>6 = `REASON_ENTRY_TRIGGERED`<br>7 = `REASON_ENTRY_FAILED`<br>8 = `REASON_ENTRY_REBASELINED`<br>9 = `REASON_EXIT_TRIGGERED`<br>10 = `REASON_EXIT_FAILED`<br>11 = `REASON_EXIT_REBASELINED`<br>12 = `REASON_EMPTY_CONFIDENT_REBASELINED`<br>13 = `REASON_EMPTY_CONFIDENT_EXITED`<br>14 = `REASON_MISSED_ENTRY_EVENT`<br>15 = `REASON_MISSED_EXIT_EVENT`<br>16 = `REASON_BORDERLINE_CLASSIFICATION`<br>17 = `REASON_LARGE_REBASELINE`<br>18 = `REASON_SWITCHED_TO_HCB`<br>19 = `REASON_LCB_TOO_HIGH` | validated |
| `OCS1P_occupantClassificationRaw` | Occupant classification system: occupant classification raw; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>1 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>2 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_SMALL`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_LARGE`<br>4 = `OCCUPANT_CLASSIFICATION_INIT`<br>7 = `OCCUPANT_CLASSIFICATION_SNA` | validated |
| `OCS1P_occupantClassificationSelf` | Occupant classification system: occupant classification self; raw 7 = signal not available (SNA) | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>1 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>2 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_SMALL`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_LARGE`<br>4 = `OCCUPANT_CLASSIFICATION_INIT`<br>7 = `OCCUPANT_CLASSIFICATION_SNA` | validated |
| `OCS1P_occupantClassificationRawCap` | Occupant classification system: occupant classification raw cap; raw 7 = signal not available (SNA) | 22\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>1 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>2 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_SMALL`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_LARGE`<br>4 = `OCCUPANT_CLASSIFICATION_INIT`<br>7 = `OCCUPANT_CLASSIFICATION_SNA` | validated |
| `OCS1P_occupantClassificationCap` | Occupant classification system: occupant classification cap; raw 7 = signal not available (SNA) | 25\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>1 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>2 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_SMALL`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW_LARGE`<br>4 = `OCCUPANT_CLASSIFICATION_INIT`<br>7 = `OCCUPANT_CLASSIFICATION_SNA` | validated |
| `OCS1P_classificationHeld` | Whether occupant classification is filtered due to door state or stability based on frequency | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_cushionStable` | Whether frequency reading is unchanging of Cushion Self sensor | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_classificationExtHold` | Occupant classification request to be filtered due to door state | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_classificationHoldState` | Occupant classification system: classification hold state | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OCCUPANCY_HOLD_OFF`<br>1 = `OCCUPANCY_HOLD_BASIC`<br>2 = `OCCUPANCY_HOLD_EXTERNAL`<br>3 = `OCCUPANCY_HOLD_FAULT` | validated |
| `OCS1P_classificationVariant` | The combination of sensors used to classify occupant | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CLASSIFICATION_VARIANT_ALL_SENSORS`<br>1 = `CLASSIFICATION_VARIANT_SELF_ONLY`<br>2 = `CLASSIFICATION_VARIANT_SELF_SBR`<br>3 = `CLASSIFICATION_VARIANT_SELF_SBR_RB`<br>7 = `CLASSIFICATION_VARIANT_UNKNOWN` | validated |
| `OCS1P_sandwichDisabled` | Cushion mutual sensor disabled by calibration | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_noSandwichType` | Configuration set in factory or service that determines logic around uninstalled sandwich | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SANDWICH_INSTALLED`<br>1 = `NO_SANDWICH_EU`<br>2 = `NO_SANDWICH_NA`<br>3 = `NO_SANDWICH_UNKNOWN` | validated |
| `OCS1P_sandwichBoundaryType` | Occupant classification system: sandwich boundary type | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SANDWICH_DEFAULT`<br>1 = `SANDWICH_LRD` | validated |
| `OCS1P_sbrBoundaryType` | Occupant classification system: sbr boundary type | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SBR_DEFAULT`<br>1 = `SBR_1669747_1763884` | validated |
| `OCS1P_occupiedStateCap` | Occupant classification system: occupied state cap; raw 3 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OCCUPIED_STATE_UNOCCUPIED`<br>1 = `OCCUPIED_STATE_OCCUPIED`<br>3 = `OCCUPIED_STATE_SNA` | validated |
| `OCS1P_seatbackStable` | Whether frequency reading is unchanging of Seatback Self sensor | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_sandwichStable` | Whether frequency reading is unchanging of Cushion Mutual sensor | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_cushionStableCap` | Occupant classification system: cushion stable cap | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_seatbackStableCap` | Occupant classification system: seatback stable cap | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_classificationHeldCap` | Occupant classification system: classification held cap | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `OCS1P_statusCounter` | Occupant classification system: status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `OCS1P_statusChecksum` | Occupant classification system: status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Occupant classification system messages (OCS1P)](../../ocs1p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
