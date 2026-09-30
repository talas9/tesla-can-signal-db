---
layout: default
title: "VCLEFT_restraintStatus (0x747) — Left body controller, Tesla Model Y 2025.20.8 ETH"
description: "Left body controller message: restraint status. Ethernet-side message VCLEFT_restraintStatus of Left body controller for Tesla Model Y firmware 2025.20.8, 10 signals (VCLEFT_frontOccupancyStatus, VCLEFT_frontBuckleStatus, VCLEFT_rearLeftOccupancyStatus, VCLEFT_rearCenterOccupancyStatus and 6 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_restraintStatus (0x747) — Left body controller, Tesla Model Y 2025.20.8 ETH

Left body controller message: restraint status. This page documents the 10 signals of VCLEFT_restraintStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_restraintStatus` |
| Ethernet-side id | 0x747 (1863) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 10 |

## Signals of VCLEFT_restraintStatus

Tesla Model Y CAN bus signals in `VCLEFT_restraintStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_frontOccupancyStatus` | Left body controller: front occupancy status; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED`<br>7 = `SEAT_OCCUPANCY_SNA` | validated |
| `VCLEFT_frontBuckleStatus` | Status of front left seatbelt buckle; raw 3 = signal not available (SNA) | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_rearLeftOccupancyStatus` | Status of rear left seat occupancy sensor; raw 3 = signal not available (SNA) | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearCenterOccupancyStatus` | Status of rear center seat occupancy sensor; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearRightOccupancyStatus` | Status of rear right seat occupancy sensor; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_UNOCCUPIED`<br>1 = `SEAT_OCCUPIED`<br>2 = `SEAT_OCCUPANCY_FAULTED`<br>3 = `SEAT_NOT_CONFIGURED` | validated |
| `VCLEFT_rearLeftBuckleStatus` | Status of rear left seatbelt buckle; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_rearCenterBuckleStatus` | Status of rear center seatbelt buckle; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SEAT_BELT_BUCKLE_STATUS_UNLATCHED`<br>1 = `SEAT_BELT_BUCKLE_STATUS_LATCHED`<br>2 = `SEAT_BELT_BUCKLE_STATUS_FAULTED`<br>3 = `SEAT_BELT_BUCKLE_NOT_CONFIGURED` | validated |
| `VCLEFT_seatTrackPosition` | Status of seat track position sensor; raw 7 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `SEAT_TRACK_POSITION_FORWARD`<br>1 = `SEAT_TRACK_POSITION_REARWARD`<br>2 = `SEAT_TRACK_POSITION_NOT_CONFIGURED`<br>3 = `SEAT_TRACK_POSITION_FAULTED`<br>7 = `SEAT_TRACK_POSITION_SNA` | validated |
| `VCLEFT_restraintStatusCounter` | Left body controller: restraint status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCLEFT_restraintStatusChecksum` | Left body controller: restraint status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
