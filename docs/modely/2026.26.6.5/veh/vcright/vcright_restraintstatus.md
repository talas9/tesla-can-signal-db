---
layout: default
title: "VCRIGHT_restraintStatus (0x31A) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: restraint status. Tesla Model Y CAN bus message VCRIGHT_restraintStatus (0x31A) of Right body controller, firmware 2026.26.6.5, 17 signals (VCRIGHT_frontOccupancyStatus, VCRIGHT_frontBuckleStatus, VCRIGHT_rearCenterBuckleStatus, VCRIGHT_rearRightBuckleStatus and 13 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_restraintStatus (0x31A) — Right body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Right body controller message: restraint status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 17 signals of VCRIGHT_restraintStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_restraintStatus` |
| CAN id | 0x31A (794) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 17 |

## Signals of VCRIGHT_restraintStatus

Tesla Model Y CAN bus signals in `VCRIGHT_restraintStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_frontOccupancyStatus` | Right body controller: front occupancy status; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED`<br>7 = `SEAT_OCCUPANCY_SNA` | validated |
| `VCRIGHT_frontBuckleStatus` | Status of front right seatbelt buckle | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCRIGHT_rearCenterBuckleStatus` | Right body controller: rear center buckle status | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCRIGHT_rearRightBuckleStatus` | Right body controller: rear right buckle status | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCRIGHT_rearRightOccupancyStatus` | Right body controller: rear right occupancy status | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCRIGHT_3RowLeftBuckleStatus` | Status of third row left seatbelt buckle | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCRIGHT_3RowRightBuckleStatus` | Right body controller: 3 row right buckle status | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCRIGHT_3RowLeftOccupancyStatus` | Right body controller: 3 row left occupancy status | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCRIGHT_3RowRightOccupancyStatus` | Right body controller: 3 row right occupancy status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCRIGHT_seatTrackPosition` | Right body controller: seat track position; raw 7 = signal not available (SNA) | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_TRACK_POSITION_FORWARD`<br>1 = `SEAT_TRACK_POSITION_REARWARD`<br>2 = `SEAT_TRACK_POSITION_NOT_CONFIGURED`<br>3 = `SEAT_TRACK_POSITION_FAULTED`<br>7 = `SEAT_TRACK_POSITION_SNA` | validated |
| `VCRIGHT_occupantClassification` | Right body controller: occupant classification; raw 7 = signal not available (SNA) | 23\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_OCCUPANT_CLASSIFICATON_EMPTY`<br>1 = `SEAT_OCCUPANT_CLASSIFICATON_INHIBIT`<br>2 = `SEAT_OCCUPANT_CLASSIFICATON_SMALL`<br>3 = `SEAT_OCCUPANT_CLASSIFICATON_LARGE`<br>4 = `SEAT_OCCUPANT_CLASSIFICATON_INIT`<br>5 = `SEAT_OCCUPANT_CLASSIFICATON_NOT_CONFIGURED`<br>6 = `SEAT_OCCUPANT_CLASSIFICATON_OUT_OF_POSITION`<br>7 = `SEAT_OCCUPANT_CLASSIFICATON_SNA` | validated |
| `VCRIGHT_occupantClassificationQF` | Right body controller: occupant classification QF | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SEAT_OCCUPANT_CLASSIFICATON_FAULTED`<br>1 = `SEAT_OCCUPANT_CLASSIFICATON_NOT_FAULTED` | validated |
| `VCRIGHT_classificationEnabled` | Indicates whether the RCM should consume VCRIGHT occupant classification rather than another source such as OCS1P | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCS1P_CLASSIFICATION_SOURCE`<br>1 = `VCRIGHT_CLASSIFICATION_SOURCE` | validated |
| `VCRIGHT_classificationEnabledQF` | Indicates whether the VCRIGHT_classificationEnabled signal is valid | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLASSIFICATION_ENABLED_FAULTED`<br>1 = `CLASSIFICATION_ENABLED_NOT_FAULTED` | validated |
| `VCRIGHT_3RowRightABStatus` | Reports status of third row right airbag suppression; raw 2 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AIRBAG_ALLOW`<br>1 = `AIRBAG_SUPPRESS`<br>2 = `AIRBAG_STATE_SNA` | validated |
| `VCRIGHT_restraintStatusCounter` | Right body controller: restraint status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCRIGHT_restraintStatusChecksum` | Right body controller: restraint status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
