---
layout: default
title: "VCLEFT_restraintStatus (0x30A) — Left body controller, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Left body controller message: restraint status. Tesla Model Y CAN bus message VCLEFT_restraintStatus (0x30A) of Left body controller, firmware 2026.26.6.5, 12 signals (VCLEFT_frontOccupancyStatus, VCLEFT_frontBuckleStatus, VCLEFT_rearLeftOccupancyStatus, VCLEFT_rearCenterOccupancyStatus and 8 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_restraintStatus (0x30A) — Left body controller, Tesla Model Y 2026.26.6.5 PARTY CAN

Left body controller message: restraint status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of VCLEFT_restraintStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_restraintStatus` |
| CAN id | 0x30A (778) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 12 |

## Signals of VCLEFT_restraintStatus

Tesla Model Y CAN bus signals in `VCLEFT_restraintStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_frontOccupancyStatus` | Left body controller: front occupancy status; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED`<br>7 = `SEAT_OCCUPANCY_SNA` | validated |
| `VCLEFT_frontBuckleStatus` | Status of front left seatbelt buckle | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_rearLeftOccupancyStatus` | Status of rear left seat occupancy sensor | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearCenterOccupancyStatus` | Status of rear center seat occupancy sensor | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearRightOccupancyStatus` | Status of rear right seat occupancy sensor | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearLeftBuckleStatus` | Status of rear left seatbelt buckle | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_rearCenterBuckleStatus` | Status of rear center seatbelt buckle | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_seatTrackPosition` | Status of seat track position sensor; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_TRACK_POSITION_FORWARD`<br>1 = `SEAT_TRACK_POSITION_REARWARD`<br>2 = `SEAT_TRACK_POSITION_NOT_CONFIGURED`<br>3 = `SEAT_TRACK_POSITION_FAULTED`<br>7 = `SEAT_TRACK_POSITION_SNA` | validated |
| `VCLEFT_3RowLeftABStatus` | Reports status of third row left airbag suppression; raw 2 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AIRBAG_ALLOW`<br>1 = `AIRBAG_SUPPRESS`<br>2 = `AIRBAG_STATE_SNA` | validated |
| `VCLEFT_3RowLeftBuckleStatus` | Reports status of third row left seatbelt buckle | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_restraintStatusCounter` | Left body controller: restraint status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCLEFT_restraintStatusChecksum` | Left body controller: restraint status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
