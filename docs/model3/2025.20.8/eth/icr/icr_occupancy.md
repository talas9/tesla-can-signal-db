---
layout: default
title: "ICR_occupancy (0x7E9) — ICR ECU, Tesla Model 3 2025.20.8 ETH"
description: "ICR ECU message: occupancy. Ethernet-side message ICR_occupancy of ICR ECU for Tesla Model 3 firmware 2025.20.8, 18 signals (ICR_occupancy1LRaw, ICR_occupancy1RRaw, ICR_occupancy1LVoteCnt, ICR_occupancy1RVoteCnt and 14 more). Bit layout, scaling, units and value tables."
---

# ICR_occupancy (0x7E9) — ICR ECU, Tesla Model 3 2025.20.8 ETH

ICR ECU message: occupancy. This page documents the 18 signals of ICR_occupancy as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_occupancy` |
| Ethernet-side id | 0x7E9 (2025) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 18 |

## Signals of ICR_occupancy

Tesla Model 3 CAN bus signals in `ICR_occupancy`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_occupancy1LRaw` | (Non-Functional Interface) Occupancy detection status of First Row left seat; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy1RRaw` | (Non-Functional Interface) Occupancy detection status of First Row right seat; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy1LVoteCnt` | ICR ECU: occupancy1 l vote cnt | 4\|6 | little-endian | signed | 1 | 0 |  | -32 to 31 |  | layout-only |
| `ICR_occupancy1RVoteCnt` | ICR ECU: occupancy1 r vote cnt | 10\|6 | little-endian | signed | 1 | 0 |  | -32 to 31 |  | layout-only |
| `ICR_userPresenceFilt` | Detection status of User Presence Detection feature; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_userPresenceRaw` | ICR ECU: user presence raw; raw 3 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy1LFilt` | (Non-Functional Interface) Occupancy detection status of First Row left seat; raw 3 = signal not available (SNA) | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy1RFilt` | (Non-Functional Interface) Occupancy detection status of First Row right seat; raw 3 = signal not available (SNA) | 23\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy2LFilt` | ICR ECU: occupancy2 l filt; raw 3 = signal not available (SNA) | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy2CFilt` | ICR ECU: occupancy2 c filt; raw 3 = signal not available (SNA) | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancy2RFilt` | ICR ECU: occupancy2 r filt; raw 3 = signal not available (SNA) | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_childPresenceFilt` | ICR ECU: child presence filt; raw 0 = signal not available (SNA) | 31\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `DETECTED_SNA`<br>1 = `NOT_DETECTED`<br>2 = `DETECTED` | plausible |
| `ICR_childPresenceRaw` | ICR ECU: child presence raw; raw 0 = signal not available (SNA) | 34\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `DETECTED_SNA`<br>1 = `NOT_DETECTED`<br>2 = `DETECTED` | plausible |
| `ICR_classification1LFilt` | ICR ECU: classification1 l filt; raw 0 = signal not available (SNA) | 37\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | plausible |
| `ICR_classification1RqF` | ICR ECU: classification1 rq f | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCCUPANT_CLASSIFICATION_FAULTED`<br>1 = `OCCUPANT_CLASSIFICATION_NOT_FAULTED` | plausible |
| `ICR_occupancy1RFiltExp` | ICR ECU: occupancy1 r filt exp; raw 3 = signal not available (SNA) | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | plausible |
| `ICR_occupancyCounter` | ICR ECU: occupancy counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ICR_occupancyChecksum` | ICR ECU: occupancy checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
