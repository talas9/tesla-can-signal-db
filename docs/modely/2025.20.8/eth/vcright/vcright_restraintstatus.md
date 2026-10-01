---
layout: default
title: "VCRIGHT_restraintStatus (0x746) — Right body controller, Tesla Model Y 2025.20.8 ETH"
description: "Right body controller message: restraint status. Ethernet-side message VCRIGHT_restraintStatus of Right body controller for Tesla Model Y firmware 2025.20.8, 16 signals (VCRIGHT_frontOccupancyStatus, VCRIGHT_frontBuckleStatus, VCRIGHT_rearCenterBuckleStatus, VCRIGHT_rearRightBuckleStatus and 12 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_restraintStatus (0x746) — Right body controller, Tesla Model Y 2025.20.8 ETH

Right body controller message: restraint status. This page documents the 16 signals of VCRIGHT_restraintStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_restraintStatus` |
| Ethernet-side id | 0x746 (1862) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 16 |

## Signals of VCRIGHT_restraintStatus

Tesla Model Y CAN bus signals in `VCRIGHT_restraintStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_frontOccupancyStatus` | Right body controller: front occupancy status; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED`<br>7 = `SEAT_OCCUPANCY_SNA` | plausible |
| `VCRIGHT_frontBuckleStatus` | Status of front right seatbelt buckle; raw 3 = signal not available (SNA) | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | plausible |
| `VCRIGHT_rearCenterBuckleStatus` | Right body controller: rear center buckle status; raw 3 = signal not available (SNA) | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | plausible |
| `VCRIGHT_rearRightBuckleStatus` | Right body controller: rear right buckle status; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | plausible |
| `VCRIGHT_rearRightOccupancyStatus` | Right body controller: rear right occupancy status; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | plausible |
| `VCRIGHT_3RowLeftBuckleStatus` | Status of third row left seatbelt buckle; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | plausible |
| `VCRIGHT_3RowRightBuckleStatus` | Right body controller: 3 row right buckle status; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | plausible |
| `VCRIGHT_3RowLeftOccupancyStatus` | Right body controller: 3 row left occupancy status; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | plausible |
| `VCRIGHT_3RowRightOccupancyStatus` | Right body controller: 3 row right occupancy status; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | plausible |
| `VCRIGHT_seatTrackPosition` | Right body controller: seat track position; raw 7 = signal not available (SNA) | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_TRACK_POSITION_FORWARD`<br>1 = `SEAT_TRACK_POSITION_REARWARD`<br>2 = `SEAT_TRACK_POSITION_NOT_CONFIGURED`<br>3 = `SEAT_TRACK_POSITION_FAULTED`<br>7 = `SEAT_TRACK_POSITION_SNA` | plausible |
| `VCRIGHT_occupantClassification` | Right body controller: occupant classification; raw 7 = signal not available (SNA) | 23\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_OCCUPANT_CLASSIFICATON_EMPTY`<br>1 = `SEAT_OCCUPANT_CLASSIFICATON_INHIBIT`<br>2 = `SEAT_OCCUPANT_CLASSIFICATON_SMALL`<br>3 = `SEAT_OCCUPANT_CLASSIFICATON_LARGE`<br>4 = `SEAT_OCCUPANT_CLASSIFICATON_INIT`<br>5 = `SEAT_OCCUPANT_CLASSIFICATON_NOT_CONFIGURED`<br>6 = `SEAT_OCCUPANT_CLASSIFICATON_OUT_OF_POSITION`<br>7 = `SEAT_OCCUPANT_CLASSIFICATON_SNA` | plausible |
| `VCRIGHT_occupantClassificationQF` | Right body controller: occupant classification QF | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SEAT_OCCUPANT_CLASSIFICATON_FAULTED`<br>1 = `SEAT_OCCUPANT_CLASSIFICATON_NOT_FAULTED` | plausible |
| `VCRIGHT_classificationEnabled` | Indicates whether the RCM should consume VCRIGHT occupant classification rather than another source such as OCS1P | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCS1P_CLASSIFICATION_SOURCE`<br>1 = `VCRIGHT_CLASSIFICATION_SOURCE` | plausible |
| `VCRIGHT_classificationEnabledQF` | Indicates whether the VCRIGHT_classificationEnabled signal is valid | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLASSIFICATION_ENABLED_FAULTED`<br>1 = `CLASSIFICATION_ENABLED_NOT_FAULTED` | plausible |
| `VCRIGHT_restraintStatusCounter` | Right body controller: restraint status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCRIGHT_restraintStatusChecksum` | Right body controller: restraint status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
