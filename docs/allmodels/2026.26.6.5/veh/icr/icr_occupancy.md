---
layout: default
title: "ICR_occupancy (0x218) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: occupancy. Tesla Model 3 / Model Y CAN bus message ICR_occupancy (0x218) of ICR ECU, firmware 2026.26.6.5, 12 signals (ICR_occupancy1LRaw, ICR_occupancy1RRaw, ICR_occupancy1LVoteCnt, ICR_occupancy1RVoteCnt and 8 more). Bit layout, scaling, units and value tables."
---

# ICR_occupancy (0x218) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

ICR ECU message: occupancy; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of ICR_occupancy as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_occupancy` |
| CAN id | 0x218 (536) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 12 |

## Signals of ICR_occupancy

Tesla Model 3 / Model Y CAN bus signals in `ICR_occupancy`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_occupancy1LRaw` | (Non-Functional Interface) Occupancy detection status of First Row left seat; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy1RRaw` | (Non-Functional Interface) Occupancy detection status of First Row right seat; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy1LVoteCnt` | ICR ECU: occupancy1 l vote cnt | 4\|6 | little-endian | signed | 1 | 0 |  | -32 to 31 |  | validated |
| `ICR_occupancy1RVoteCnt` | ICR ECU: occupancy1 r vote cnt | 10\|6 | little-endian | signed | 1 | 0 |  | -32 to 31 |  | validated |
| `ICR_occupancy1LFilt` | (Non-Functional Interface) Occupancy detection status of First Row left seat; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy1RFilt` | (Non-Functional Interface) Occupancy detection status of First Row right seat; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy2LFilt` | ICR ECU: occupancy2 l filt; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy2CFilt` | ICR ECU: occupancy2 c filt; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy2RFilt` | ICR ECU: occupancy2 r filt; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancy1RFiltExp` | ICR ECU: occupancy1 r filt exp; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_occupancyCounter` | ICR ECU: occupancy counter | 28\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `ICR_occupancyChecksum` | ICR ECU: occupancy checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
